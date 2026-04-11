"""
Integrate remaining memo variables into a single city-year controls panel.

This script reads all the raw files that were not previously merged into the
main panel and produces one consolidated output at processed/memo_integration_
city_year_panel.csv. Pipeline/15 then attaches it alongside the existing
sub-panels.

Raw files consumed:
  raw/mayor/mayor_party.csv                      (9,216 rows, 2010-2025, 576 cities)
  raw/epa/city_year_epa_enforcement_expanded_*   (15,552 rows, 2000-2026, 576 cities)
  raw/srf/srf_bond_merged.csv                    (7,514 rows, 2013-2025, 578 cities)
  raw/fiscal/fiscal_tel_merged_2013_2025.csv.gz  (6,936 rows, 2013-2024, 578 cities)
  raw/geospatial/substitute_water_panel.csv      (7,501 rows, 2013-2025, 577 cities)
  raw/market/state_green_bond_capacity.csv       (550 rows, 2013-2023, state-year)
  raw/market/esg_aum.csv                         (11 rows, 2013-2023, national year)
  raw/institutional/state_bond_banks.csv         (50 rows, static state)
  raw/institutional/state_bond_referenda_requirements.csv (50 rows, static state)
  raw/political/state_msrb_rfi_position.csv      (50 rows, static state)
  raw/disasters/fema_disaster_declarations.csv   (49,408 rows, 2010-2025, county)
  raw/disasters/nfip_flood_claims.csv            (2,273 rows, cross-section, county)
  raw/crosswalk/Crosswalk.csv                    (578 cities, for FIPS + county lookup)

Output:
  processed/memo_integration_city_year_panel.csv (7,514 rows, ~80 columns)

Variable namespace (prefixes to avoid collisions):
  mayor_*    - mayoral partisanship
  epa_*      - EPA ECHO enforcement (NPDES Family 1a)
  cwsrf_*    - SRF Family 1b
  fn_*       - newer fiscal file (cwns, pct_deficient, muni bond law)
  subst_*    - substitute water issuer availability
  mkt_*      - market capacity (state green bond capacity, ESG AUM)
  inst_*     - state institutional (bond banks, referenda, MSRB)
  fema_*     - FEMA disaster declarations (county)
  nfip_*     - NFIP flood claims (county)
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "processed"
YEARS = list(range(2011, 2026))  # 2011-2025: includes 2 extra years of
# pre-panel history so that pipeline/15's attach() can compute lag1 and
# lag2 for variables whose raw sources go back before 2013 (mayor_party
# 2010-2025, EPA enforcement 2000-2026, MIT pres 2012/2016/2020/2024).

# ---------------------------------------------------------------------------
# 0. Build skeleton from crosswalk
# ---------------------------------------------------------------------------
crosswalk = pd.read_csv(RAW / "crosswalk" / "Crosswalk.csv")
skel = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb", "county_geo_id", "NAME_county"]]
    .rename(columns={
        "fips7": "FIPS", "geo_name": "City",
        "city_name": "City_Name", "state_abb": "State",
        "county_geo_id": "county_fips", "NAME_county": "county_name",
    })
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
skel["FIPS"] = skel["FIPS"].astype(int)
print(f"Skeleton: {skel.shape}")

# county_fips may be a full GEOID like '1500000US01001' — extract the 5-digit county FIPS
def extract_county_fips5(val):
    if pd.isna(val):
        return None
    s = str(val)
    # GEOID format "1500000USNNNNN" or just "NNNNN"
    if "US" in s:
        s = s.split("US")[-1]
    try:
        return int(s[-5:]) if s.strip() else None
    except ValueError:
        return None

skel["county_fips5"] = skel["county_fips"].apply(extract_county_fips5)
print(f"Cities with county_fips5: {skel[skel.Year==2013].county_fips5.notna().sum()}")

panel = skel.copy()

# ---------------------------------------------------------------------------
# 1. Mayor party (Family 2 primary treatment)
# ---------------------------------------------------------------------------
print("\n[1/11] Mayor party...")
mp = pd.read_csv(RAW / "mayor" / "mayor_party.csv")
mp["fips"] = mp["fips"].astype(int)
mp_slim = mp[["fips", "year", "mayor_name", "mayor_pid", "prob_democrat", "prob_republican",
              "election_year", "election_type"]].rename(columns={
    "fips": "FIPS", "year": "Year",
    "mayor_name": "mayor_name",
    "mayor_pid": "mayor_pid",
    "prob_democrat": "mayor_prob_dem",
    "prob_republican": "mayor_prob_rep",
    "election_year": "mayor_election_year",
    "election_type": "mayor_election_type",
})
# Construct Rep_Mayor binary
mp_slim["Rep_Mayor"] = (mp_slim["mayor_prob_rep"] > 0.5).astype(int)
mp_slim["Dem_Mayor"] = (mp_slim["mayor_prob_dem"] > 0.5).astype(int)
panel = panel.merge(mp_slim, on=["FIPS", "Year"], how="left")
print(f"  Rows with Rep_Mayor: {panel.Rep_Mayor.notna().sum()}")
print(f"  Republican mayors by year:")
print(panel.groupby("Year").Rep_Mayor.sum().to_string())

# ---------------------------------------------------------------------------
# 2. EPA ECHO enforcement (Family 1a primary compulsion)
# ---------------------------------------------------------------------------
print("\n[2/11] EPA ECHO enforcement...")
epa_path = RAW / "epa" / "city_year_epa_enforcement_expanded_20260407_125920.csv"
epa = pd.read_csv(epa_path, low_memory=False)

# Rename key cols - the full picture across THREE enforcement dimensions:
#   1. ACTIONS (formal + informal regulatory responses)
#   2. VIOLATIONS (measured infractions detected during compliance monitoring)
#   3. ENFORCEMENT/CASES (administrative and judicial cases, penalties)
# Across three ownership tiers (muni/locgov/private) and six EPA programs:
#   NPDES (Clean Water Act point sources) - memo primary
#   SDWA (Safe Drinking Water Act) - crucial for water utility bonds
#   Overflow events (sanitary sewer overflows) - infrastructure failure signal
#   RCRA (hazardous waste) - secondary
#   Air (Clean Air Act) - robustness
#   Case totals (administrative + judicial + penalties)
epa_key = [
    "FIPS", "YEAR",
    # === NPDES (Clean Water Act) — primary memo compulsion channel ===
    # Actions
    "npdes_formal_prior3yr_muni", "npdes_formal_prior3yr_locgov", "npdes_formal_prior3yr_private",
    "npdes_formal_count_muni", "npdes_formal_cum_muni", "npdes_formal_any_muni",
    "npdes_informal_actions_count_muni", "npdes_informal_actions_count_locgov",
    "npdes_informal_actions_count_private",
    # Violations (by type)
    "npdes_effluent_violations_count_muni", "npdes_effluent_violations_count_locgov",
    "npdes_effluent_violations_count_private",
    "npdes_cs_violations_count_muni", "npdes_cs_violations_count_locgov",
    "npdes_cs_violations_count_private",
    "npdes_ps_violations_count_muni", "npdes_ps_violations_count_locgov",
    "npdes_ps_violations_count_private",
    "npdes_se_violations_count_muni", "npdes_se_violations_count_locgov",
    "npdes_se_violations_count_private",
    # Inspections (exposure/monitoring)
    "npdes_inspections_count_muni", "npdes_inspections_count_locgov",
    "npdes_inspections_count_private",
    # === SDWA (Safe Drinking Water Act) ===
    "sdwa_events_milestones_count_muni", "sdwa_events_milestones_count_locgov",
    "sdwa_events_milestones_count_private",
    "sdwa_lcr_samples_count_muni", "sdwa_lcr_samples_count_locgov",
    "sdwa_lcr_samples_count_private",
    "sdwa_site_visits_count_muni", "sdwa_site_visits_count_locgov",
    "sdwa_site_visits_count_private",
    # === Overflow events (sanitary sewer overflows) ===
    "overflow_events_muni", "overflow_events_locgov", "overflow_events_private",
    # === Cases (administrative + judicial consent decrees, penalties) ===
    "case_jdc_prior3yr_muni", "case_jdc_prior3yr_locgov", "case_jdc_prior3yr_private",
    "case_afr_prior3yr_muni", "case_afr_prior3yr_locgov", "case_afr_prior3yr_private",
    "case_all_prior3yr_muni", "case_all_prior3yr_locgov", "case_all_prior3yr_private",
    "case_jdc_count_muni", "case_jdc_cum_muni",
    "case_penalty_total_muni", "case_penalty_total_locgov", "case_penalty_total_private",
    # === RCRA (hazardous waste - secondary) ===
    "rcra_enforcements_count_muni", "rcra_enforcements_count_locgov",
    "rcra_enforcements_count_private",
    "rcra_snc_vio_months_count_muni", "rcra_snc_vio_months_count_locgov",
    "rcra_snc_vio_months_count_private",
    # === Air (CAA - robustness only, not expected to drive green bonds) ===
    "air_formal_actions_count_muni", "air_formal_actions_count_locgov",
    "air_formal_actions_count_private",
    "air_violations_count_muni", "air_violations_count_locgov",
    "air_violations_count_private",
]
epa_key = [c for c in epa_key if c in epa.columns]
epa_slim = epa[epa_key].rename(columns={"YEAR": "Year"})

# Prefix with epa_ and fill NaN with 0 for cities where enforcement file has
# no matching record (non-muni infrastructure presence, etc.)
rename_map = {c: f"epa_{c}" for c in epa_slim.columns if c not in ("FIPS", "Year")}
epa_slim = epa_slim.rename(columns=rename_map)
numeric_epa = [c for c in epa_slim.columns if c not in ("FIPS", "Year")]
epa_slim[numeric_epa] = epa_slim[numeric_epa].fillna(0)

# Build composite compulsion indices at the muni/locgov/private level.
# The memo's Four-Family theory treats compulsion as a directed capital-
# demand channel (regulatory bite forces infrastructure investment). The
# three dimensions the user flagged (actions, violations, enforcement) map
# to the following composites:
for tier in ("muni", "locgov", "private"):
    # Water violations: sum of effluent + CS + PS + SE (direct infractions)
    cols_viol = [f"epa_npdes_{v}_violations_count_{tier}"
                 for v in ("effluent", "cs", "ps", "se")]
    cols_viol = [c for c in cols_viol if c in epa_slim.columns]
    if cols_viol:
        epa_slim[f"epa_water_violations_count_{tier}"] = epa_slim[cols_viol].sum(axis=1)

    # Water actions: formal + informal NPDES responses
    cols_act = [f"epa_npdes_formal_count_{tier}" if tier == "muni" else None,
                f"epa_npdes_informal_actions_count_{tier}"]
    cols_act = [c for c in cols_act if c and c in epa_slim.columns]
    if cols_act:
        epa_slim[f"epa_water_actions_count_{tier}"] = epa_slim[cols_act].sum(axis=1)

    # Cases total (enforcement): all EPA cases closed (admin + judicial)
    # "case_all_prior3yr_<tier>" is already in whitelist.
    # Just ensure it's numeric.

    # SDWA composite (drinking water events)
    cols_sdwa = [f"epa_sdwa_events_milestones_count_{tier}",
                 f"epa_sdwa_lcr_samples_count_{tier}",
                 f"epa_sdwa_site_visits_count_{tier}"]
    cols_sdwa = [c for c in cols_sdwa if c in epa_slim.columns]
    if cols_sdwa:
        epa_slim[f"epa_sdwa_total_count_{tier}"] = epa_slim[cols_sdwa].sum(axis=1)

    # Combined water compulsion = NPDES formal actions prior3yr + violations
    # + overflow + SDWA events. This is the richer "compulsion" measure that
    # captures all three dimensions (actions, violations, enforcement) in
    # a single scale-normalized index.
    base_cols = [
        f"epa_npdes_formal_prior3yr_{tier}",
        f"epa_water_violations_count_{tier}",
        f"epa_overflow_events_{tier}",
        f"epa_sdwa_total_count_{tier}",
    ]
    base_cols = [c for c in base_cols if c in epa_slim.columns]
    if base_cols:
        # asinh transform to handle zero-heavy distributions
        epa_slim[f"epa_water_compulsion_asinh_{tier}"] = np.arcsinh(
            epa_slim[base_cols].sum(axis=1)
        )

panel = panel.merge(epa_slim, on=["FIPS", "Year"], how="left")
print(f"  EPA columns merged: {len(numeric_epa)} raw + composites")
print(f"  Cities with non-zero npdes_formal_prior3yr_muni: "
      f"{(panel.epa_npdes_formal_prior3yr_muni > 0).sum()}")
print(f"  Cities with non-zero water_violations_count_muni: "
      f"{(panel.epa_water_violations_count_muni > 0).sum() if 'epa_water_violations_count_muni' in panel.columns else 0}")
print(f"  Cities with non-zero overflow_events_muni: "
      f"{(panel.epa_overflow_events_muni > 0).sum()}")
print(f"  Cities with non-zero sdwa_events_milestones_muni: "
      f"{(panel.epa_sdwa_events_milestones_count_muni > 0).sum() if 'epa_sdwa_events_milestones_count_muni' in panel.columns else 0}")

# ---------------------------------------------------------------------------
# 3. SRF (CWSRF Family 1b)
# ---------------------------------------------------------------------------
print("\n[3/11] SRF / CWSRF...")
srf = pd.read_csv(RAW / "srf" / "srf_bond_merged.csv", low_memory=False)
srf_key = [
    "fips", "year",
    "usaspending_cwsrf", "usaspending_dwsrf", "usaspending_total",
    "cwsrf_total_allotment", "cwsrf_arra_supplement",
    "portal_total_lending", "portal_cw_total_lending", "portal_cw_n_agreements",
    "state_srf_allotment_per_capita",
]
srf_key = [c for c in srf_key if c in srf.columns]
srf_slim = srf[srf_key].rename(columns={"fips": "FIPS", "year": "Year"})
srf_slim["FIPS"] = srf_slim["FIPS"].astype(int)

# Back-fill 2011 and 2012 with the 2013 value per city. CWSRF federal
# allocations are sticky year-over-year (state formula allotments change
# slowly), so propagating the earliest observed year backwards by 2 years
# is a conservative approximation that preserves lag2 computability at
# outcome year 2013.
cwsrf_vars = [c for c in srf_slim.columns if c not in ("FIPS", "Year")]
backfill_2013 = srf_slim[srf_slim["Year"] == 2013][["FIPS"] + cwsrf_vars].copy()
for fill_year in (2011, 2012):
    add = backfill_2013.copy()
    add["Year"] = fill_year
    srf_slim = pd.concat([srf_slim, add], ignore_index=True)
srf_slim = srf_slim.sort_values(["FIPS", "Year"]).reset_index(drop=True)
print(f"  SRF backfill: added 2 years x {len(backfill_2013)} cities = "
      f"{2 * len(backfill_2013)} rows for 2011-2012")

# Prefix
rename_srf = {c: f"cwsrf_{c}" for c in srf_slim.columns if c not in ("FIPS", "Year")}
srf_slim = srf_slim.rename(columns=rename_srf)
# Construct log_cwsrf_obligations
srf_slim["cwsrf_log_obligations"] = np.log1p(srf_slim["cwsrf_usaspending_cwsrf"].fillna(0))
panel = panel.merge(srf_slim, on=["FIPS", "Year"], how="left")
print(f"  Non-zero cwsrf_usaspending_cwsrf: {(panel.cwsrf_usaspending_cwsrf > 0).sum()}")

# ---------------------------------------------------------------------------
# 4. Newer fiscal file (cwns_needs_real, pct_deficient, esg_has_muni_bond_law)
# ---------------------------------------------------------------------------
print("\n[4/11] Newer fiscal file (cwns, pct_deficient, muni bond law)...")
fn = pd.read_csv(RAW / "fiscal" / "fiscal_tel_merged_2013_2025.csv.gz",
                 compression="gzip", low_memory=False)
fn_key = [
    "fips7", "year",
    "cwns_needs_real", "pct_deficient",
    "esg_has_muni_bond_law",
    # Also pull the FOG institutional block (form of government, initiative,
    # referendum, term limits) for institutional controls
    "fog", "initiative", "referendum", "partisan", "termlimits", "termlength", "districts",
    "years_since_election", "election_vote_share",
]
fn_key = [c for c in fn_key if c in fn.columns]
fn_slim = fn[fn_key].rename(columns={"fips7": "FIPS", "year": "Year"})
fn_slim["FIPS"] = fn_slim["FIPS"].astype(int)

# Extrapolate cwns_needs_real and pct_deficient to 2011-2012 per city.
# The raw cwns_source column shows these are "interpolated" from the
# 2022 EPA Clean Water Needs Survey. Chicago's trajectory shows ~3%
# year-over-year linear growth back from 2022. We extend the same linear
# trend backward by 2 more years (2011, 2012) using per-city linear
# regression on available years. If a city has <2 observations, we
# forward-fill from the earliest observed value.
from scipy import stats as _stats

def extrapolate_city(group, var):
    """Fit linear trend on observed years, predict 2011 and 2012."""
    obs = group.dropna(subset=[var])
    if len(obs) == 0:
        return {2011: np.nan, 2012: np.nan}
    if len(obs) == 1:
        return {2011: obs[var].iloc[0], 2012: obs[var].iloc[0]}
    slope, intercept, *_ = _stats.linregress(obs["Year"].values, obs[var].values)
    return {2011: intercept + slope * 2011, 2012: intercept + slope * 2012}

def add_extrapolated_years(frame, var):
    rows = []
    for fips, grp in frame.groupby("FIPS"):
        ext = extrapolate_city(grp, var)
        for yr, val in ext.items():
            rows.append({"FIPS": fips, "Year": yr, var: val})
    return pd.DataFrame(rows)

# Subset fn_slim to cwns vars only for extrapolation
cwns_subset = fn_slim[["FIPS", "Year", "cwns_needs_real", "pct_deficient"]].copy()
cwns_ext = add_extrapolated_years(cwns_subset, "cwns_needs_real")
pct_ext = add_extrapolated_years(cwns_subset, "pct_deficient")
cwns_ext_all = cwns_ext.merge(pct_ext, on=["FIPS", "Year"], how="outer")

# For cols in fn_slim that aren't cwns-related, back-fill 2011-2012 with
# the 2013 value (similar to CWSRF)
other_fn_cols = [c for c in fn_slim.columns
                 if c not in ("FIPS", "Year", "cwns_needs_real", "pct_deficient")]
fn_2013 = fn_slim[fn_slim["Year"] == 2013][["FIPS"] + other_fn_cols].copy()
for fill_year in (2011, 2012):
    add = fn_2013.copy()
    add["Year"] = fill_year
    ext_row = cwns_ext_all[cwns_ext_all["Year"] == fill_year][["FIPS", "cwns_needs_real", "pct_deficient"]]
    add = add.merge(ext_row, on="FIPS", how="left")
    fn_slim = pd.concat([fn_slim, add], ignore_index=True)
fn_slim = fn_slim.sort_values(["FIPS", "Year"]).reset_index(drop=True)
print(f"  cwns backfill: extrapolated 2011-2012 via linear trend per city")

# Prefix
fn_rename = {c: f"fn_{c}" for c in fn_slim.columns if c not in ("FIPS", "Year")}
fn_slim = fn_slim.rename(columns=fn_rename)
panel = panel.merge(fn_slim, on=["FIPS", "Year"], how="left")
print(f"  Non-null cwns_needs_real: {panel.fn_cwns_needs_real.notna().sum()}")
print(f"  Non-null pct_deficient: {panel.fn_pct_deficient.notna().sum()}")

# ---------------------------------------------------------------------------
# 5. Substitute water issuer panel (Family 3 feasibility)
# ---------------------------------------------------------------------------
print("\n[5/11] Substitute water issuer...")
subst = pd.read_csv(RAW / "geospatial" / "substitute_water_panel.csv")
subst_slim = subst[["fips7", "year",
                    "substitute_water_25km", "substitute_water_any_25km",
                    "substitute_water_n_25km", "substitute_water_50km",
                    "asinh_substitute_water_25km", "asinh_substitute_water_50km"]].rename(
    columns={"fips7": "FIPS", "year": "Year"}
)
subst_slim["FIPS"] = subst_slim["FIPS"].astype(int)
subst_rename = {c: f"subst_{c}" for c in subst_slim.columns if c not in ("FIPS", "Year")}
subst_slim = subst_slim.rename(columns=subst_rename)
panel = panel.merge(subst_slim, on=["FIPS", "Year"], how="left")
# Build has_substitute_issuer alias matching memo naming
panel["has_substitute_issuer"] = panel["subst_substitute_water_any_25km"].fillna(0).astype(int)
print(f"  Cities with substitute water issuer within 25km: {panel[panel.Year==2025].has_substitute_issuer.sum()}")

# ---------------------------------------------------------------------------
# 6. State green bond capacity (Family 3 feasibility)
# ---------------------------------------------------------------------------
print("\n[6/11] State green bond capacity...")
mkt_gb = pd.read_csv(RAW / "market" / "state_green_bond_capacity.csv")
# Drop the raw _lag1 columns — attach() will compute its own lags downstream
# so including pre-lagged columns here produces "_lag1_lag1" collisions.
mkt_gb_slim = mkt_gb[[
    "state_abb", "year",
    "state_green_bond_ever",
    "state_green_bond_cum_amt",
    "state_green_bond_count",
    "state_green_bond_amt",
]].rename(columns={"state_abb": "State", "year": "Year"})
mkt_gb_rename = {c: f"mkt_{c}" for c in mkt_gb_slim.columns if c not in ("State", "Year")}
mkt_gb_slim = mkt_gb_slim.rename(columns=mkt_gb_rename)
panel = panel.merge(mkt_gb_slim, on=["State", "Year"], how="left")
print(f"  State-years with state_green_bond_ever = 1: {(panel.mkt_state_green_bond_ever == 1).sum()}")

# ---------------------------------------------------------------------------
# 7. ESG AUM (market discipline - Appendix I)
# ---------------------------------------------------------------------------
print("\n[7/11] ESG AUM...")
aum = pd.read_csv(RAW / "market" / "esg_aum.csv")
aum_slim = aum.rename(columns={
    "year": "Year",
    "global_esg_aum_trillion": "mkt_esg_aum_global",
    "us_esg_aum_trillion": "mkt_esg_aum_us",
    "esg_aum_growth_pct": "mkt_esg_aum_growth_pct",
    "esg_share_global_aum": "mkt_esg_share_global",
})
panel = panel.merge(aum_slim, on="Year", how="left")
# Carry forward 2023 values to 2024-2025 as a linear extrapolation
last_known = aum["year"].max()
last_row = aum[aum.year == last_known].iloc[0]
panel.loc[panel.Year > last_known, "mkt_esg_aum_global"] = last_row["global_esg_aum_trillion"]
panel.loc[panel.Year > last_known, "mkt_esg_aum_us"] = last_row["us_esg_aum_trillion"]
panel.loc[panel.Year > last_known, "mkt_esg_aum_growth_pct"] = last_row["esg_aum_growth_pct"]
panel.loc[panel.Year > last_known, "mkt_esg_share_global"] = last_row["esg_share_global_aum"]
print(f"  ESG AUM years covered: {YEARS[0]}-{YEARS[-1]} (2024-2025 carry forward from 2023)")

# ---------------------------------------------------------------------------
# 8. State bond banks (Family 3)
# ---------------------------------------------------------------------------
print("\n[8/11] State bond banks...")
bb = pd.read_csv(RAW / "institutional" / "state_bond_banks.csv")
bb_slim = bb[["state_abb", "has_bond_bank", "bond_bank_established",
              "bond_bank_cumulative_billion", "bond_bank_active_2013_2025"]].rename(
    columns={"state_abb": "State"}
)
bb_rename = {c: f"inst_{c}" for c in bb_slim.columns if c != "State"}
bb_slim = bb_slim.rename(columns=bb_rename)
panel = panel.merge(bb_slim, on="State", how="left")
print(f"  States with bond bank: {bb['has_bond_bank'].sum()}")

# ---------------------------------------------------------------------------
# 9. State bond referenda requirements (Family 3)
# ---------------------------------------------------------------------------
print("\n[9/11] State bond referenda requirements...")
br = pd.read_csv(RAW / "institutional" / "state_bond_referenda_requirements.csv")
br_slim = br[[
    "state_abb",
    "go_voter_approval_required", "go_vote_threshold", "go_supermajority",
    "revenue_bond_voter_approval", "has_state_bond_commission",
    "has_constitutional_debt_limit", "has_state_approval_body",
]].rename(columns={"state_abb": "State"})
br_rename = {c: f"inst_{c}" for c in br_slim.columns if c != "State"}
br_slim = br_slim.rename(columns=br_rename)
panel = panel.merge(br_slim, on="State", how="left")
print(f"  States requiring GO voter approval: {br['go_voter_approval_required'].sum()}")

# ---------------------------------------------------------------------------
# 10. State MSRB RFI position (Family 3 political willingness)
# ---------------------------------------------------------------------------
print("\n[10/11] State MSRB RFI position...")
msrb = pd.read_csv(RAW / "political" / "state_msrb_rfi_position.csv")
msrb_slim = msrb[["state_abb", "signed_utah_antiesg_letter", "msrb_rfi_position"]].rename(
    columns={"state_abb": "State"}
)
# Encode msrb_rfi_position categorically or as binary
msrb_slim["inst_signed_utah_antiesg_letter"] = msrb_slim["signed_utah_antiesg_letter"].fillna(0).astype(int)
msrb_slim["inst_msrb_position_anti_esg"] = (
    msrb_slim["msrb_rfi_position"].fillna("").str.lower().str.contains("oppose|anti").astype(int)
)
msrb_slim = msrb_slim[["State", "inst_signed_utah_antiesg_letter", "inst_msrb_position_anti_esg"]]
panel = panel.merge(msrb_slim, on="State", how="left")
print(f"  States signed Utah anti-ESG letter: {msrb_slim['inst_signed_utah_antiesg_letter'].sum()}")

# ---------------------------------------------------------------------------
# 11. FEMA disaster declarations + NFIP flood claims (county -> city)
# ---------------------------------------------------------------------------
print("\n[11/11] FEMA disasters + NFIP flood claims...")
fema = pd.read_csv(RAW / "disasters" / "fema_disaster_declarations.csv")
fema_slim = fema.rename(columns={
    "county_fips": "county_fips5",
    "year": "Year",
    "fema_disaster_any": "fema_disaster_any",
    "fema_disaster_count": "fema_disaster_count",
    "fema_disaster_cum": "fema_disaster_cum",
    "fema_disaster_flood": "fema_disaster_flood",
    "fema_disaster_hurricane": "fema_disaster_hurricane",
    "fema_disaster_fire": "fema_disaster_fire",
})
fema_slim["county_fips5"] = pd.to_numeric(fema_slim["county_fips5"], errors="coerce")
fema_rename = {c: f"fema_{c}" if not c.startswith("fema_") else c
               for c in fema_slim.columns if c not in ("county_fips5", "Year")}
fema_slim = fema_slim.rename(columns=fema_rename)
panel = panel.merge(fema_slim, on=["county_fips5", "Year"], how="left")
# Fill with 0 for county-years without any declaration
fema_cols = [c for c in panel.columns if c.startswith("fema_")]
panel[fema_cols] = panel[fema_cols].fillna(0)
print(f"  Cities with any FEMA disaster 2013-2025: {(panel.groupby('FIPS')['fema_disaster_any'].max() > 0).sum()}")

# NFIP flood claims (cross-section, time-invariant at county)
nfip = pd.read_csv(RAW / "disasters" / "nfip_flood_claims.csv")
nfip_slim = nfip.rename(columns={"county_fips": "county_fips5"})
nfip_slim["county_fips5"] = pd.to_numeric(nfip_slim["county_fips5"], errors="coerce")
nfip_rename = {c: f"nfip_{c}" if not c.startswith("nfip_") else c
               for c in nfip_slim.columns if c != "county_fips5"}
nfip_slim = nfip_slim.rename(columns=nfip_rename)
panel = panel.merge(nfip_slim, on="county_fips5", how="left")
nfip_cols = [c for c in panel.columns if c.startswith("nfip_")]
panel[nfip_cols] = panel[nfip_cols].fillna(0)
print(f"  Cities with NFIP repetitive loss data: {(panel.groupby('FIPS')['nfip_repetitive_loss'].max() > 0).sum()}")

# ---------------------------------------------------------------------------
# Sanity checks + output
# ---------------------------------------------------------------------------
assert panel.shape[0] == 578 * len(YEARS), f"Expected {578*len(YEARS)} rows, got {panel.shape[0]}"
assert panel.groupby(["FIPS", "Year"]).size().max() == 1

# Sort for output
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

# Drop helper cols that aren't analysis variables
panel = panel.drop(columns=["county_fips", "county_name", "county_fips5"], errors="ignore")

panel.to_csv(OUT / "memo_integration_city_year_panel.csv", index=False)
print(f"\nWritten: {OUT / 'memo_integration_city_year_panel.csv'}")
print(f"Shape: {panel.shape}")
print(f"\nCol prefixes summary:")
prefixes = ["mayor_", "epa_", "cwsrf_", "fn_", "subst_", "mkt_", "inst_", "fema_", "nfip_"]
for p in prefixes:
    cols = [c for c in panel.columns if c.startswith(p)]
    print(f"  {p:8s} {len(cols)} cols")
