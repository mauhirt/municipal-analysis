"""
Build a unified, lag-friendly city-year panel for the 2013-2025 outcome period.

Strategy (Option B — lagged controls, no carry-forward):
  - Outcome variables span 2013-2025.
  - For each control variable, compute lag1 and lag2 from the RAW data
    frame (which may extend back to 2007 for fiscal, 2010 for census)
    BEFORE filtering to 2013-2025. So lag1/lag2 for early outcome years
    are real pre-sample observations.
  - Contemporaneous values at year Y are the actual Y values from the raw
    file. If the raw file does not cover Y (e.g., fiscal ends 2024), the
    contemporaneous column is NaN — but lag1 at Y=2025 is the real 2024
    value, so the user can still use lagged RHS at 2025.
  - Availability matrix by outcome year:
      Fiscal + TEL (raw 2007-2024):
        contemporaneous: 2013-2024 real, 2025 NaN
        lag1: 2013-2025 real (lag1 at 2025 = raw 2024)
        lag2: 2013-2025 real (lag2 at 2025 = raw 2023)
      Census additional (raw 2010-2024): same as fiscal
      Climate / anti-ESG / state political (raw 2013-2023):
        contemporaneous: 2013-2023 real, 2024-2025 NaN
        lag1: 2014-2024 real, 2025 NaN
        lag2: 2015-2025 real (lag2 at 2025 = raw 2023)
      Federal grants (raw 2013-2025):
        contemporaneous, lag1, lag2: all available

Output:
  processed/merged_city_year_panel.{csv,xlsx}

Structure: 578 cities x 13 years (2013-2025), keyed on FIPS + Year.
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
PROC = ROOT / "processed"
YEARS = list(range(2013, 2026))

crosswalk = pd.read_csv(RAW / "crosswalk" / "Crosswalk.csv")
skeleton = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City",
                     "city_name": "City_Name", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
print(f"Skeleton: {skeleton.shape}")


def attach(panel, raw, raw_fips, raw_year, cols, source_label):
    """Merge raw (fips, year) data with lag1/lag2.

    Lags are computed via three separate merges so lag1 at outcome year Y
    equals raw[fips, year=Y-1] and lag2 at Y equals raw[fips, year=Y-2],
    regardless of whether raw has a row at year Y itself.

    No carry-forward: contemporaneous values that aren't in raw become NaN.
    Lag values are populated whenever raw has a row at year Y-L, which for
    pre-2013 raw data means 2013-2014 outcome years get real pre-sample lags.
    """
    r = raw[[raw_fips, raw_year] + cols].copy()
    r[raw_fips] = pd.to_numeric(r[raw_fips], errors="coerce").astype("Int64")
    r[raw_year] = pd.to_numeric(r[raw_year], errors="coerce").astype("Int64")
    r = r.dropna(subset=[raw_fips, raw_year])
    r = r.rename(columns={raw_fips: "FIPS", raw_year: "Year"})
    r["FIPS"] = r["FIPS"].astype(int)
    r["Year"] = r["Year"].astype(int)

    # Contemporaneous merge: panel[Y] gets raw[Y]
    out = panel.merge(r, on=["FIPS", "Year"], how="left")

    # Lag1 merge: panel[Y] gets raw[Y-1]
    r_lag1 = r.copy()
    r_lag1["Year"] = r_lag1["Year"] + 1  # shift raw year forward so raw[2012] aligns with outcome[2013]
    r_lag1 = r_lag1.rename(columns={c: f"{c}_lag1" for c in cols})
    out = out.merge(r_lag1, on=["FIPS", "Year"], how="left")

    # Lag2 merge: panel[Y] gets raw[Y-2]
    r_lag2 = r.copy()
    r_lag2["Year"] = r_lag2["Year"] + 2
    r_lag2 = r_lag2.rename(columns={c: f"{c}_lag2" for c in cols})
    out = out.merge(r_lag2, on=["FIPS", "Year"], how="left")

    out.attrs[f"{source_label}_last_year"] = int(r["Year"].max())
    return out


panel = skeleton.copy()

# ---------------------------------------------------------------------------
# 1. Fiscal + TEL (2007-2024) — 1,022 cols. Pick a targeted subset to keep
#    the file manageable; you can re-run with a broader list if needed.
# ---------------------------------------------------------------------------
print("\n[1/10] Loading fiscal 2007-2024...")
fiscal = pd.read_csv(RAW / "fiscal" / "fiscal_tel_merged_2007_2024.csv", low_memory=False)
fiscal_cols = [
    # Population / economy
    "population_city", "unemployment_city", "percapita_income_city",
    "totalincome_city",
    # Revenue / expenditure totals (pc = per capita)
    "total_revenue_pc", "general_revenue_pc", "own_source_rev_pc",
    "capital_outlay_pc", "debt_pc", "capital_stock_pc",
    # Composition shares
    "own_source_rev_share", "share_property", "share_sales", "share_income",
    "share_charges", "fed_igr_share", "state_igr_share",
    "property_tax_share", "sales_tax_share", "income_tax_share",
    "capital_share",
    # Fiscal health / stress indicators
    "fiscal_stress_index", "fiscal_stress_pca",
    "debt_to_revenue", "debt_affordability", "debt_service_burden",
    "pension_expenditure_burden", "combined_liability_burden",
    "budget_flexibility_squeeze", "expenditure_rigidity",
    "tax_effort_pc", "tax_effort_pc_3yr",
    "revenue_autonomy", "tax_autonomy_ratio",
    "reserve_ratio", "reserve_ratio_3yr",
    "expenditure_gap_pc",
    "vfi",
    # Enterprise fund depth (memo Family 1b - charges_to_own_source)
    "charges_to_own_source",
    # Debt composition
    "short_term_debt_share", "go_bond_share_outstanding",
    "go_bond_share_issuance",
    # Tax/expenditure limitation (TEL)
    "tel_overall_rate_limit", "tel_specific_rate_limit", "tel_levy_limit",
    "tel_assessment_limit", "tel_general_revenue_limit",
    "tel_general_expenditure_limit", "tel_full_disclosure",
    "tel_stringency_simple", "tel_stringency_ads",
    "tel_stringency_normalized",
    "tel_x_tax_effort", "tel_x_dsb", "tel_x_revenue_autonomy", "tel_x_vfi",
]
fiscal_cols = [c for c in fiscal_cols if c in fiscal.columns]
print(f"  Using {len(fiscal_cols)} fiscal columns (fiscal file uses entity_id as the FIPS key — fips7 is only populated 2007-2012)")
panel = attach(panel, fiscal, "entity_id", "year", fiscal_cols, "fiscal")

# ---------------------------------------------------------------------------
# 2. Census additional city variables (2010-2024)
# ---------------------------------------------------------------------------
print("\n[2/10] Loading additional_city_variables_2010_2024...")
add = pd.read_csv(RAW / "census_acs" / "additional_city_variables_2010_2024.csv", low_memory=False)
add_cols = [
    "land_area_sqkm", "pop_density_sqkm", "is_principal_city",
    "state_gov_party", "state_govt_trifecta", "state_dem_trifecta",
    "state_rep_trifecta", "state_dem_governor", "state_medicaid_expanded",
    "state_right_to_work", "state_pct_bachelors_plus",
    "opinion_happening", "opinion_human", "opinion_worried", "opinion_regulate",
    "opinion_fundrenewables", "opinion_priority",
    "pres_dem_two_party_share", "pres_dem_vote_share", "pres_rep_vote_share",
]
add_cols = [c for c in add_cols if c in add.columns]
panel = attach(panel, add, "fips", "Year", add_cols, "census_add")

# ---------------------------------------------------------------------------
# 3. SKIPPED: economic_bls_acs — these variables are already included in
#    fiscal_tel_merged_2007_2024 (which covers 2007-2024 for the same columns).
# ---------------------------------------------------------------------------
print("\n[3/10] Skipping economic_bls_acs (already covered by fiscal_tel_merged_2007_2024)")

# ---------------------------------------------------------------------------
# 4. Climate opinion (2013-2023)
# ---------------------------------------------------------------------------
print("\n[4/10] Loading climate_opinion...")
climate = pd.read_csv(RAW / "climate" / "climate_opinion_ycom.csv")
climate_cols = [c for c in climate.columns if c.startswith("opinion_")]
# These partially overlap with the census-additional opinions; we prefix them
# with 'ycom_' to keep the sources distinct
climate = climate.rename(columns={c: f"ycom_{c}" for c in climate_cols})
climate_cols = [f"ycom_{c}" for c in climate_cols]
panel = attach(panel, climate, "fips7", "year", climate_cols, "ycom")

# ---------------------------------------------------------------------------
# 5. Climate policy controls.
#    Prefers processed/climate_policy_controls_v2.csv if present — the
#    peer-review-grade rebuild from pipeline/17_build_climate_policy_controls_v2.py
#    which sources every value from committed provenance-tracked CSVs in
#    raw/climate/sourced/.
#    Falls back to processed/climate_policy_controls_extended.csv (pipeline/16)
#    and then to the original raw file (2013-2023) for backwards compatibility.
# ---------------------------------------------------------------------------
print("\n[5/10] Loading climate_policy_controls...")
v2_path = PROC / "climate_policy_controls_v2.csv"
ext_path = PROC / "climate_policy_controls_extended.csv"
if v2_path.exists():
    cpol = pd.read_csv(v2_path)
    print(f"  Using peer-review v2 file (2007-2025): {cpol.shape}")
    cpol_cols = [
        "muni_aaa_yield",
        "state_rps_active", "state_rps_target_pct",
        "state_rggi_member", "state_rggi_price_usd",
        "state_catp_member", "state_catp_price_usd",
        "state_wci_member", "state_wci_price_usd",
        "state_carbon_pricing", "state_carbon_price_usd",
        "state_climate_plan_legacy", "state_pcap_2024",
        "c40_member",
        "mcpa_signatory_static", "iclei_member_static",
        "climate_commitment_static",
    ]
elif ext_path.exists():
    cpol = pd.read_csv(ext_path)
    print(f"  Using extended file (2007-2025): {cpol.shape}")
    cpol_cols = [
        "muni_aaa_yield", "c40_member", "mayors_climate_signatory",
        "iclei_member", "climate_commitment_score",
        "state_rps_active", "state_rps_target_pct",
        "state_carbon_pricing", "state_carbon_price", "state_climate_plan",
    ]
else:
    cpol = pd.read_csv(RAW / "climate" / "climate_policy_controls.csv")
    print(f"  Using original raw file (2013-2023): {cpol.shape}")
    cpol_cols = [
        "muni_aaa_yield", "c40_member", "mayors_climate_signatory",
        "iclei_member", "climate_commitment_score",
        "state_rps_active", "state_rps_target_pct",
        "state_carbon_pricing", "state_carbon_price", "state_climate_plan",
    ]
cpol_cols = [c for c in cpol_cols if c in cpol.columns]
panel = attach(panel, cpol, "fips7", "year", cpol_cols, "cpol")

# ---------------------------------------------------------------------------
# 6. ESG legislation panel (2010-2025, state-year).
#    The newer esg_legislation_panel.csv (state-year, 2010-2025) supersedes
#    the older antiesg_laws.csv (city-year broadcast, 2013-2023). We
#    broadcast state-year values to city-year via the crosswalk state_abb
#    and prefix all variable columns with "esg_" to match the prior naming.
# ---------------------------------------------------------------------------
print("\n[6/10] Loading ESG legislation panel...")
esg_path_new = RAW / "political" / "esg_legislation_panel.csv"
if esg_path_new.exists():
    esg_state = pd.read_csv(esg_path_new)
    # Broadcast state-year to city-year via the crosswalk
    cw = crosswalk[["fips7", "state_abb"]].rename(columns={"fips7": "city_fips7"})
    esg_city = esg_state.merge(cw, left_on="state_abbrev", right_on="state_abb", how="left")
    esg_city = esg_city[esg_city["city_fips7"].notna()].copy()
    esg_city["city_fips7"] = esg_city["city_fips7"].astype(int)
    # Prefix variable columns with esg_ to match previous naming convention
    var_cols = [c for c in esg_state.columns
                if c not in ("state", "state_abbrev", "fips", "year")]
    rename_map = {c: f"esg_{c}" for c in var_cols}
    esg_city = esg_city.rename(columns=rename_map)
    esg_cols = list(rename_map.values())
    print(f"  Broadcast to {esg_city['city_fips7'].nunique()} cities across {esg_state['year'].min()}-{esg_state['year'].max()}")
    panel = attach(panel, esg_city, "city_fips7", "year", esg_cols, "antiesg")
else:
    esg = pd.read_csv(RAW / "political" / "antiesg_laws.csv")
    esg_cols = [c for c in esg.columns if c.startswith("esg_")]
    panel = attach(panel, esg, "fips7", "year", esg_cols, "antiesg")

# ---------------------------------------------------------------------------
# 7. Political state (2013-2023)
# ---------------------------------------------------------------------------
print("\n[7/10] Loading state political...")
pol = pd.read_csv(RAW / "political" / "state_political.csv")
# Drop columns that are already in additional_city_variables (state_*_trifecta,
# state_dem_governor) to avoid _x/_y collisions
already_in_census_add = {
    "state_dem_governor", "state_dem_trifecta", "state_govt_trifecta",
    "state_rep_trifecta", "state_divided_govt", "state_dem_legislature",
    "state_legis_control", "state_gov_party",
}
pol_cols = [c for c in pol.columns
            if c not in ("year", "fips7", "city_name") and c not in already_in_census_add]
panel = attach(panel, pol, "fips7", "year", pol_cols, "pol_state")

# ---------------------------------------------------------------------------
# 8. SKIPPED: TEL institutional — all TEL variables are already in
#    fiscal_tel_merged_2007_2024 (loaded in step 1).
# ---------------------------------------------------------------------------
print("\n[8/10] Skipping tel.csv (already covered by fiscal_tel_merged_2007_2024)")

# ---------------------------------------------------------------------------
# 9. Federal grants (2013-2025) — already has lag columns built in,
#    but we treat it uniformly and let attach() compute its own.
# ---------------------------------------------------------------------------
print("\n[9/10] Loading federal grants...")
fg = pd.read_csv(RAW / "grants" / "federal_grants_panel.csv")
fg_cols = [c for c in fg.columns
           if c not in ("fips7", "year") and not c.endswith(("_lag1", "_lag2", "_cum"))]
panel = attach(panel, fg, "fips7", "year", fg_cols, "fed_grants")

# ---------------------------------------------------------------------------
# 10. NRI — time-invariant, merge once
# ---------------------------------------------------------------------------
print("\n[10/10] Loading NRI (time-invariant)...")
nri = pd.read_csv(RAW / "nri" / "epa_nri.csv", low_memory=False)
# Take just the 2013 row per city (all years are identical)
nri_t0 = nri[nri["year"] == 2013].copy()
nri_cols = [c for c in nri.columns if c not in ("year", "fips7", "city_name")]
# Clean column names (they contain spaces and dashes)
rename_map = {c: "nri_" + c.lower().replace(" - ", "_").replace(" ", "_").replace("/", "_") for c in nri_cols}
nri_t0 = nri_t0.rename(columns=rename_map)
nri_cols_clean = list(rename_map.values())
nri_t0 = nri_t0[["fips7"] + nri_cols_clean]
nri_t0["fips7"] = nri_t0["fips7"].astype(int)
nri_t0 = nri_t0.rename(columns={"fips7": "FIPS"})
panel = panel.merge(nri_t0, on="FIPS", how="left")
print(f"  NRI columns merged: {len(nri_cols_clean)}")

# ---------------------------------------------------------------------------
# 10b. Building Codes + BPS (pipeline/18) — city-year panel
# ---------------------------------------------------------------------------
print("\n[10b/11] Loading building codes + BPS panel...")
bcode_path = PROC / "building_codes_city_year_panel.csv"
if bcode_path.exists():
    bcode = pd.read_csv(bcode_path)
    bcode_cols = [c for c in bcode.columns if c.startswith("bcode_")]
    # Drop duplicate ID columns so attach() can merge cleanly
    bcode_slim = bcode[["FIPS", "Year"] + bcode_cols].rename(
        columns={"FIPS": "fips7", "Year": "year"}
    )
    panel = attach(panel, bcode_slim, "fips7", "year", bcode_cols, "bcode")
    print(f"  Building codes columns merged: {len(bcode_cols)}")
else:
    print(f"  SKIPPED: {bcode_path} not found - run pipeline/18 first")

# ---------------------------------------------------------------------------
# 10c. Energy Policy (pipeline/19) — state controls + muni electric
# ---------------------------------------------------------------------------
print("\n[10c/11] Loading energy policy panel...")
ep_path = PROC / "energy_policy_city_year_panel.csv"
if ep_path.exists():
    ep = pd.read_csv(ep_path)
    ep_cols = [c for c in ep.columns if c.startswith("ep_")]
    ep_slim = ep[["FIPS", "Year"] + ep_cols].rename(
        columns={"FIPS": "fips7", "Year": "year"}
    )
    panel = attach(panel, ep_slim, "fips7", "year", ep_cols, "ep")
    print(f"  Energy policy columns merged: {len(ep_cols)}")
else:
    print(f"  SKIPPED: {ep_path} not found - run pipeline/19 first")

# ---------------------------------------------------------------------------
# 11. Bring in existing green bond outcome + controls (already built, 2013-2025)
# ---------------------------------------------------------------------------
print("\n[11/11] Merging in green bond outcome + controls panels...")
outcome = pd.read_csv(PROC / "outcome_city_year_panel.csv", low_memory=False)
gb_controls = pd.read_csv(PROC / "controls_city_year_panel.csv", low_memory=False)
for df in (outcome, gb_controls):
    df.drop(columns=[c for c in ("City", "City_Name", "State") if c in df.columns],
            inplace=True, errors="ignore")
panel = panel.merge(outcome, on=["FIPS", "Year"], how="left")
panel = panel.merge(gb_controls, on=["FIPS", "Year"], how="left")

# ---------------------------------------------------------------------------
# 11b. Water-only green bond panels (pipeline/21) — state cumul + nearby
# ---------------------------------------------------------------------------
print("\n[11b] Loading water-only green bond panels...")
water_state_path = PROC / "state_controls_city_year_panel_water_only.csv"
water_nearby_path = PROC / "nearby_by_jurisdiction_panel_water_only.csv"
if water_state_path.exists():
    ws = pd.read_csv(water_state_path, low_memory=False)
    ws.drop(columns=[c for c in ("City", "City_Name", "State") if c in ws.columns],
            inplace=True, errors="ignore")
    panel = panel.merge(ws, on=["FIPS", "Year"], how="left")
    print(f"  State water cols merged: {sum(1 for c in ws.columns if c.startswith(('State_', 'City_Own_')))}")
else:
    print(f"  SKIPPED: {water_state_path} not found - run pipeline/21 first")

if water_nearby_path.exists():
    wn = pd.read_csv(water_nearby_path, low_memory=False)
    wn.drop(columns=[c for c in ("City", "City_Name", "State") if c in wn.columns],
            inplace=True, errors="ignore")
    panel = panel.merge(wn, on=["FIPS", "Year"], how="left")
    print(f"  Nearby water cols merged: {sum(1 for c in wn.columns if c.startswith('Nearby_'))}")
else:
    print(f"  SKIPPED: {water_nearby_path} not found - run pipeline/21 first")

# ---------------------------------------------------------------------------
# 11c. Memo variable integration (pipeline/20) — mayor, EPA, CWSRF,
#      cwns/pct_deficient, substitute water, state green bond capacity,
#      ESG AUM, state bond banks, referenda, MSRB position, FEMA, NFIP.
#      All lags computed via attach() for consistency.
# ---------------------------------------------------------------------------
print("\n[11c] Loading memo integration panel...")
memo_path = PROC / "memo_integration_city_year_panel.csv"
if memo_path.exists():
    memo = pd.read_csv(memo_path, low_memory=False)
    memo_cols = [c for c in memo.columns
                 if c not in ("FIPS", "City", "City_Name", "State", "Year",
                              "mayor_name", "mayor_election_type")]
    memo_slim = memo[["FIPS", "Year"] + memo_cols].rename(
        columns={"FIPS": "fips7", "Year": "year"}
    )
    panel = attach(panel, memo_slim, "fips7", "year", memo_cols, "memo")
    print(f"  Memo integration columns merged: {len(memo_cols)}")
else:
    print(f"  SKIPPED: {memo_path} not found - run pipeline/20 first")

# ---------------------------------------------------------------------------
# 11c2. Presidential vote city-year panel (pipeline/22)
#       MIT MEDSL county returns 2012-2024 mapped to cities.
#       REPLACES the partial 2013-2023 coverage from the older file.
# ---------------------------------------------------------------------------
print("\n[11c2] Loading presidential vote panel (MIT MEDSL 2012-2024)...")
pres_path = PROC / "presidential_vote_city_year_panel.csv"
if pres_path.exists():
    pres = pd.read_csv(pres_path)
    pres_cols = [
        "pres_dem_two_party_share", "pres_dem_vote_share", "pres_rep_vote_share",
        "applicable_election_year",
    ]
    pres_slim = pres[["FIPS", "Year"] + pres_cols].rename(
        columns={"FIPS": "fips7", "Year": "year"}
    )
    # Drop any existing (older) presidential cols from panel so we use the
    # new MIT-based ones; those older cols may have come from census_acs add.
    for c in pres_cols + [f"{c}_lag1" for c in pres_cols] + [f"{c}_lag2" for c in pres_cols]:
        if c in panel.columns:
            panel = panel.drop(columns=[c])
    panel = attach(panel, pres_slim, "fips7", "year", pres_cols, "pres")
    print(f"  Presidential columns (re)merged: {len(pres_cols)}")
else:
    print(f"  SKIPPED: {pres_path} not found - run pipeline/22 first")

# ---------------------------------------------------------------------------
# 11d. Derive memo-specific outcome aliases (Y_self_green, Y_esg_assurance,
#      Y_water_only, Y_clean_trans, Y_renewable, Y_energy_eff, Y_green_bldg,
#      Y_climate_adapt, Y_pollution_control, asinh_*_amt)
# ---------------------------------------------------------------------------
print("\n[11d] Deriving memo outcome aliases...")
import numpy as np

# Y_self_green: issuer explicitly self-designated as green
if "Issued_Self-reported Green__Yes" in panel.columns:
    panel["Y_self_green"] = (panel["Issued_Self-reported Green__Yes"] > 0).astype(int)

# Y_esg_assurance: issuer obtained third-party ESG assurance
if "Issued_ESG Assurance Providers__Yes" in panel.columns:
    panel["Y_esg_assurance"] = (panel["Issued_ESG Assurance Providers__Yes"] > 0).astype(int)

# Amount versions with asinh transform
if "City_Green_Amt_Issued" in panel.columns:
    panel["asinh_green_amt"] = np.arcsinh(panel["City_Green_Amt_Issued"].fillna(0))
if "Amt_Self-reported Green__Yes" in panel.columns:
    panel["asinh_self_green_amt"] = np.arcsinh(panel["Amt_Self-reported Green__Yes"].fillna(0))

# Category-specific binary outcomes — collapse multi-category combos
def any_col_positive(df, keyword):
    """Return 1 if any Issued_ESG Project Categories__* col containing keyword is positive."""
    cols = [c for c in df.columns
            if c.startswith("Issued_ESG Project Categories__") and keyword in c]
    if not cols:
        return pd.Series(0, index=df.index, dtype=int)
    return (df[cols].fillna(0).sum(axis=1) > 0).astype(int)

panel["Y_water_only"] = any_col_positive(panel, "Sustainable_Water")
panel["Y_clean_trans"] = any_col_positive(panel, "Clean_Transportation")
panel["Y_renewable"] = any_col_positive(panel, "Renewable_Energy")
panel["Y_energy_eff"] = any_col_positive(panel, "Energy_Efficiency")
panel["Y_green_bldg"] = any_col_positive(panel, "Green_Buildings")
panel["Y_climate_adapt"] = any_col_positive(panel, "Climate_Change_Adaptation")
panel["Y_pollution_control"] = any_col_positive(panel, "Pollution_Control")
panel["Y_natural_resource"] = any_col_positive(panel, "Natural_Resource")

# Print sanity counts
y_cols = ["Y_self_green", "Y_esg_assurance", "Y_water_only", "Y_clean_trans",
          "Y_renewable", "Y_energy_eff", "Y_green_bldg", "Y_climate_adapt",
          "Y_pollution_control", "Y_natural_resource"]
for y in y_cols:
    if y in panel.columns:
        print(f"  {y}: {int(panel[y].sum())} city-years")

# ---------------------------------------------------------------------------
# Final panel
# ---------------------------------------------------------------------------
print(f"\nFinal panel shape: {panel.shape}")

# Put id cols first
id_cols = ["FIPS", "City", "City_Name", "State", "Year"]
other = [c for c in panel.columns if c not in id_cols]
panel = panel[id_cols + other]
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

PROC.mkdir(parents=True, exist_ok=True)
panel.to_csv(PROC / "merged_city_year_panel.csv", index=False)
# XLSX is skipped when the panel is very wide — pandas needs a lot of memory
# to write ~1600 columns to XLSX. The CSV is the canonical output.

# Save an availability report
print("\n=== Non-null counts per column (sample) ===")
nn = panel.notna().sum().sort_values()
print(f"Total columns: {len(panel.columns)}")
print(f"  <10% non-null: {(nn < len(panel)*0.1).sum()}")
print(f"  >=90% non-null: {(nn >= len(panel)*0.9).sum()}")

cf_flags = [c for c in panel.columns if c.startswith("__")]
print(f"\nCarry-forward flags: {len(cf_flags)}")
for c in cf_flags:
    print(f"  {c}: {int(panel[c].sum())} rows flagged carry-forward")

print(f"\nWritten: {PROC / 'merged_city_year_panel.csv'}")
