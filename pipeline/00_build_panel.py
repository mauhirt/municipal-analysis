"""
00_build_panel.py — Assemble master panel from upstream sources (2013-2025)
============================================================================
Uses actual upstream data files (not the stale data/clean/ derivatives) to build
a maximalist panel: every variable for its full available year range and city coverage.

Skeleton: Exports/city_year_issuance_panel.xlsx (578 cities x 13 years, 2013-2025)

Run: python pipeline/00_build_panel.py
"""

import pandas as pd
import numpy as np
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')
ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent.parent / 'processed' / 'panel'
OUT.mkdir(exist_ok=True)

def log(msg):
    print(msg)

log("=" * 70)
log("PHASE 0: BUILD MASTER PANEL (2013-2025)")
log("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 1. GREEN BOND SKELETON — Exports/city_year_issuance_panel.xlsx
# ═══════════════════════════════════════════════════════════════════════
log("\n── 1. Green bond skeleton ──")
df = pd.read_excel(ROOT / 'raw' / 'bloomberg' / 'city_year_issuance_panel.xlsx')
df = df.rename(columns={'FIPS': 'fips7', 'Year': 'year', 'City': 'city_name', 'State': 'state_abb'})
df['fips7'] = df['fips7'].astype(int)
log(f"  Skeleton: {df.shape}, cities={df.fips7.nunique()}, years={df.year.min()}-{df.year.max()}")
log(f"  Green bonds: {df.Green_Bond_Issued.sum():.0f}")

# Construct Y_ indicators from the detailed columns
sr_yes = [c for c in df.columns if c.startswith('Count_Self-reported Green__Yes')]
esg_fw = [c for c in df.columns if c.startswith('Count_ESG Framework__Yes')]
esg_rp = [c for c in df.columns if c.startswith('Count_ESG Reporting__Yes')]
esg_as = [c for c in df.columns if c.startswith('Count_ESG Assurance Providers__Yes')]
esg_proj_cols = [c for c in df.columns if c.startswith('Count_ESG Project Categories__') and c != 'Count_ESG Project Categories']

df['Y_self_green'] = (df[sr_yes].sum(axis=1) > 0).astype(int) if sr_yes else 0
df['Y_esg_framework'] = (df[esg_fw].sum(axis=1) > 0).astype(int) if esg_fw else 0
df['Y_esg_reporting'] = (df[esg_rp].sum(axis=1) > 0).astype(int) if esg_rp else 0
df['Y_esg_assurance'] = (df[esg_as].sum(axis=1) > 0).astype(int) if esg_as else 0
df['Y_any_esg_project'] = (df[esg_proj_cols].sum(axis=1) > 0).astype(int) if esg_proj_cols else 0

log(f"  After Y_ construction: {df.shape}")


# ═══════════════════════════════════════════════════════════════════════
# 1b. CROSSWALK — county_fips5 from Census crosswalk (needed for CAA merge)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 1b. Crosswalk county FIPS ──")
cw = pd.read_csv(ROOT / 'raw' / 'crosswalk' / 'Crosswalk.csv')
# county_geo_id is "0500000US<county_fips5>", extract last 5 digits.
if 'county_geo_id' in cw.columns:
    cw['county_fips5'] = (
        cw['county_geo_id'].astype(str)
        .str.split('US', n=1).str[1]
        .where(lambda s: s.str.len() == 5, other=None)
    )
    cw['county_fips5'] = pd.to_numeric(cw['county_fips5'], errors='coerce')
    cw_keep = cw[['fips', 'county_fips5']].rename(columns={'fips': 'fips7'})
    cw_keep = cw_keep.drop_duplicates('fips7')
    df = df.merge(cw_keep, on='fips7', how='left')
    log(f"  county_fips5 merged from crosswalk: "
        f"{int(df['county_fips5'].notna().sum())} non-null")
else:
    log("  [warn] county_geo_id not found in crosswalk — county_fips5 not built")


# ═══════════════════════════════════════════════════════════════════════
# HELPER: merge with logging
# ═══════════════════════════════════════════════════════════════════════
def safe_merge(df, right, on, name, how='left'):
    """Merge and report new columns added."""
    before_cols = set(df.columns)
    n_before = len(df)
    df = df.merge(right, on=on, how=how, suffixes=('', '_DROP'))
    drop_cols = [c for c in df.columns if c.endswith('_DROP')]
    df = df.drop(columns=drop_cols)
    new_cols = set(df.columns) - before_cols
    log(f"  After {name}: {df.shape}, new cols={len(new_cols)}, rows {'OK' if len(df)==n_before else 'CHANGED: '+str(len(df))}")
    return df


# ═══════════════════════════════════════════════════════════════════════
# 2. MAYOR PARTY — data/clean/mayor_party/mayor_party.csv (2010-2025)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 2. Mayor party (2010-2025) ──")
mayor = pd.read_csv(ROOT / 'raw' / 'mayor' / 'mayor_party.csv')
mayor = mayor.rename(columns={'fips': 'fips7'})
# D = baseline (Rep_Mayor=0, Ind_Mayor=0), R = Rep_Mayor=1, I = Ind_Mayor=1
mayor['Rep_Mayor'] = np.where(mayor['mayor_pid'] == 'R', 1.0,
                    np.where(mayor['mayor_pid'].isin(['D', 'I']), 0.0, np.nan))
mayor['Ind_Mayor'] = np.where(mayor['mayor_pid'] == 'I', 1.0,
                    np.where(mayor['mayor_pid'].isin(['D', 'R']), 0.0, np.nan))
# Dem_Mayor indicator — Democrat = 1, else 0 (R or I). Preferred per variable-audit Part D
# because mayor_pid coding already effectively lags through "year following
# election = mayor's first year in office" convention; use WITHOUT lag.
mayor['Dem_Mayor'] = np.where(mayor['mayor_pid'] == 'D', 1.0,
                    np.where(mayor['mayor_pid'].isin(['R', 'I']), 0.0, np.nan))
mayor = mayor.sort_values(['fips7', 'year'])
mayor['Rep_Mayor_L1'] = mayor.groupby('fips7')['Rep_Mayor'].shift(1)
mayor['Ind_Mayor_L1'] = mayor.groupby('fips7')['Ind_Mayor'].shift(1)
mayor['Dem_Mayor_L1'] = mayor.groupby('fips7')['Dem_Mayor'].shift(1)
mayor['party_switch'] = ((mayor['Rep_Mayor'] != mayor['Rep_Mayor_L1']) &
                         mayor['Rep_Mayor'].notna() &
                         mayor['Rep_Mayor_L1'].notna()).astype(float)
mayor['switch_to_R'] = ((mayor['party_switch'] == 1) & (mayor['Rep_Mayor'] == 1)).astype(float)
mayor['switch_to_D'] = ((mayor['party_switch'] == 1) & (mayor['Rep_Mayor'] == 0) & (mayor['Ind_Mayor'] == 0)).astype(float)
mayor['Rep_Mayor_L2'] = mayor.groupby('fips7')['Rep_Mayor'].shift(2)
mayor['Rep_Mayor_L3'] = mayor.groupby('fips7')['Rep_Mayor'].shift(3)
mayor['Rep_Mayor_L4'] = mayor.groupby('fips7')['Rep_Mayor'].shift(4)
mayor['prob_republican_L1'] = mayor.groupby('fips7')['prob_republican'].shift(1)
mayor['prob_republican_L2'] = mayor.groupby('fips7')['prob_republican'].shift(2)
mayor['prob_republican_L3'] = mayor.groupby('fips7')['prob_republican'].shift(3)
mayor_cols = ['fips7', 'year', 'mayor_name', 'mayor_pid', 'Rep_Mayor', 'Ind_Mayor',
              'Dem_Mayor',
              'prob_democrat', 'prob_republican', 'election_year', 'election_type',
              'Rep_Mayor_L1', 'Rep_Mayor_L2', 'Rep_Mayor_L3', 'Rep_Mayor_L4',
              'Ind_Mayor_L1', 'Dem_Mayor_L1',
              'prob_republican_L1', 'prob_republican_L2', 'prob_republican_L3',
              'party_switch', 'switch_to_R', 'switch_to_D']
df = safe_merge(df, mayor[mayor_cols], on=['fips7', 'year'], name='mayor')


# ═══════════════════════════════════════════════════════════════════════
# 2b. MAYORAL CANDIDATES — MayoralCandidates270326.xlsx (2001-2025)
#     Builds city-year vote-share + margin-of-victory variables from the
#     full candidate-election dataset (8,255 candidate-rows, 576 cities,
#     2001-2025). Only WINNING-candidate rows are retained, then
#     expanded to city-year with forward-fill between elections (same
#     convention as mayor_party.csv: the year following an election is
#     the mayor's first year in office).
#
# Variables built:
#   mayor_vote_share_win       — winning candidate's vote share
#   mayor_vote_share_total     — total votes in the winning election
#   mayor_margin_victory       — winner's share minus second-place share
#   mayor_win_is_dem           — 1 if winner's pid_est == 'D'
#   mayor_win_is_rep           — 1 if winner's pid_est == 'R'
#   mayor_win_prob_democrat    — winner's DIME-based prob_democrat
#   mayor_win_prob_republican  — winner's DIME-based prob_republican
#   mayor_win_cfscore          — winner's CF score (continuous ideology)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 2b. Mayoral candidates vote-share panel (2001-2025) ──")
candidates_path = ROOT / 'raw' / 'mayor' / 'MayoralCandidates270326.xlsx'
if candidates_path.exists():
    cand = pd.read_excel(candidates_path)
    cand = cand.rename(columns={'fips': 'fips7'})
    cand['fips7'] = cand['fips7'].astype(int)

    # Winners only — one row per (city, election-year).
    winners = cand[cand['winner'] == 1].copy()

    # Compute margin of victory = winner share − runner-up share per contest.
    runner_up_share = (
        cand[cand['winner'] == 0]
        .sort_values(['contest', 'vote_share'], ascending=[True, False])
        .groupby('contest')['vote_share']
        .max()
        .rename('runner_up_share')
        .reset_index()
    )
    winners = winners.merge(runner_up_share, on='contest', how='left')
    winners['mayor_margin_victory'] = (
        winners['vote_share'] - winners['runner_up_share'].fillna(0)
    )

    # Per user spec: "the year following the election is coded as the mayor's
    # first year in office". So attribute the election outcome to (year+1)
    # onwards, forward-filling until the next election.
    winners['effective_year'] = winners['year'] + 1
    winners = winners.sort_values(['fips7', 'effective_year'])
    winners['mayor_win_is_dem'] = (winners['pid_est'] == 'D').astype(int)
    winners['mayor_win_is_rep'] = (winners['pid_est'] == 'R').astype(int)

    keep = ['fips7', 'effective_year', 'year', 'month',
            'vote_share', 'total_votes',
            'mayor_margin_victory', 'mayor_win_is_dem', 'mayor_win_is_rep',
            'prob_democrat', 'prob_republican', 'cfscore']
    winners_small = winners[keep].copy()
    # When a city has two elections with the same effective_year (e.g. regular +
    # special election in same calendar year), keep the LATER election (by
    # year+month). This matches the mayor_party.csv convention of using the
    # most recent transition for a given year.
    winners_small = (
        winners_small.sort_values(['fips7', 'effective_year', 'year', 'month'],
                                  ascending=[True, True, False, False])
        .drop_duplicates(['fips7', 'effective_year'], keep='first')
    )
    winners_small = winners_small.drop(columns=['year', 'month']).rename(columns={
        'effective_year': 'year',
        'vote_share': 'mayor_vote_share_win',
        'total_votes': 'mayor_vote_share_total',
        'prob_democrat': 'mayor_win_prob_democrat',
        'prob_republican': 'mayor_win_prob_republican',
        'cfscore': 'mayor_win_cfscore',
    })
    # Forward-fill within city across years — but only for years after the
    # election, up to the next election. Achieved by outer-joining to a
    # full (fips7 × year) grid and applying a city-level ffill.
    full_grid = df[['fips7', 'year']].drop_duplicates()
    winners_grid = full_grid.merge(winners_small, on=['fips7', 'year'], how='left')
    winners_grid = winners_grid.sort_values(['fips7', 'year'])
    candidate_vars = [c for c in winners_small.columns if c not in ('fips7', 'year')]
    winners_grid[candidate_vars] = winners_grid.groupby('fips7')[candidate_vars].ffill()

    before = set(df.columns)
    df = df.merge(winners_grid, on=['fips7', 'year'], how='left', suffixes=('', '_CAND'))
    for c in list(df.columns):
        if c.endswith('_CAND'):
            df = df.drop(columns=c)
    new_cols = set(df.columns) - before
    log(f"  mayoral candidates: added {len(new_cols)} cols "
        f"(winners: {winners.shape[0]}, "
        f"cities covered in panel: {df['mayor_vote_share_win'].notna().groupby(df['fips7']).any().sum()})")
else:
    log(f"  [skip] {candidates_path} not found")


# ═══════════════════════════════════════════════════════════════════════
# 3. FISCAL/TEL MERGED — fiscal_tel_merged_2007_2024.csv (2007-2024)
#    Extends back to 2007 for lag construction; rows outside 2013-2025
#    are added temporarily and trimmed after lag construction.
# ═══════════════════════════════════════════════════════════════════════
log("\n── 3. Fiscal/TEL merged (2007-2024) ──")
fiscal_path_new = ROOT / 'raw' / 'fiscal' / 'fiscal_tel_merged_2007_2024.csv'
fiscal_path_old = ROOT / 'raw' / 'fiscal' / 'fiscal_tel_merged_2013_2025.csv.gz'
if fiscal_path_new.exists():
    fiscal = pd.read_csv(fiscal_path_new, low_memory=False)
    # Use entity_id as primary key (fips7 column is only filled for 2007-2012)
    if 'entity_id' in fiscal.columns:
        fiscal['fips7'] = fiscal['entity_id'].astype(int)
    elif 'fips7' in fiscal.columns:
        fiscal = fiscal.dropna(subset=['fips7'])
        fiscal['fips7'] = fiscal['fips7'].astype(float).astype(int)
    log(f"  Using expanded fiscal file: {fiscal.shape}, years {fiscal['year'].min()}-{fiscal['year'].max()}")

    # Add pre-2013 rows to panel for lag construction
    pre_panel_years = fiscal[fiscal['year'] < 2013][['fips7', 'year']].drop_duplicates()
    if len(pre_panel_years) > 0:
        # Create skeleton rows for 2007-2012 with just fips7, year, and basic identifiers
        pre_rows = pre_panel_years.copy()
        # Carry forward city_name and state_abb from the main panel
        city_info = df[['fips7', 'city_name', 'state_abb']].drop_duplicates(subset='fips7')
        pre_rows = pre_rows.merge(city_info, on='fips7', how='left')
        df = pd.concat([pre_rows, df], ignore_index=True)
        df = df.sort_values(['fips7', 'year']).reset_index(drop=True)
        log(f"  Added {len(pre_rows)} pre-2013 skeleton rows for lag construction")
else:
    fiscal = pd.read_csv(fiscal_path_old, compression='gzip', low_memory=False)
    log(f"  Using original fiscal file: {fiscal.shape}")

skip = {'city_name', 'state_abb', 'state', 'City', 'State', 'geo_name',
        'Green_Bond_Issued', 'City_Green_Amt_Issued', 'City_Green_Issuance_Count',
        'State_Total_Amt_Issued', 'State_Total_Issuance_Count',
        'State_Govt_Amt_Issued', 'State_Govt_Issuance_Count', 'City_Share_of_State_Pct',
        'data_source', 'entity_id'}
fiscal_new = [c for c in fiscal.columns if c not in df.columns and c not in skip]
fiscal_keep = ['fips7', 'year'] + fiscal_new
fiscal_keep = [c for c in fiscal_keep if c in fiscal.columns]
df = safe_merge(df, fiscal[fiscal_keep].drop_duplicates(subset=['fips7', 'year']), on=['fips7', 'year'], name='fiscal/TEL')

# Also load variables from old fiscal source that may not be in the new file
# (e.g., cwns_needs_real, pct_deficient, NRI columns)
if fiscal_path_new.exists() and fiscal_path_old.exists():
    log("  Loading supplementary variables from old fiscal file...")
    fiscal_old = pd.read_csv(fiscal_path_old, compression='gzip', low_memory=False)
    old_new_cols = [c for c in fiscal_old.columns if c not in df.columns and c not in skip]
    if old_new_cols:
        old_keep = ['fips7', 'year'] + old_new_cols
        old_keep = [c for c in old_keep if c in fiscal_old.columns]
        df = safe_merge(df, fiscal_old[old_keep].drop_duplicates(subset=['fips7', 'year']),
                        on=['fips7', 'year'], name='fiscal/TEL supplement')


# ═══════════════════════════════════════════════════════════════════════
# 4. CONSTRUCTED FISCAL — data/clean/constructed_fiscal/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 4. Constructed fiscal (2013-2023) ──")
cf = pd.read_csv(ROOT / 'raw' / 'fiscal' / 'constructed_fiscal.csv')
cf_new = [c for c in cf.columns if c not in df.columns and c not in ('city_name',)]
if cf_new:
    df = safe_merge(df, cf[['fips7', 'year'] + cf_new], on=['fips7', 'year'], name='constructed_fiscal')
else:
    log("  No new columns to add from constructed_fiscal")


# ═══════════════════════════════════════════════════════════════════════
# 5. EPA ECHO (AUTHORITATIVE) — expanded ownership-split file (2000-2026, 195 cols)
#    Aggregates (overflow_events, npdes_formal_any, etc.) constructed from splits.
# ═══════════════════════════════════════════════════════════════════════
log("\n── 5. EPA ECHO authoritative (2000-2026, expanded) ──")
epa_path = ROOT / 'raw' / 'epa' / 'city_year_epa_enforcement_expanded_20260407_125920.csv'
epa = pd.read_csv(epa_path)
epa = epa.rename(columns={'FIPS': 'fips7', 'YEAR': 'year'})
epa_drop = ['CITY_ID', 'CITY_NAME', 'CITY_STATE']
epa_cols = [c for c in epa.columns if c not in epa_drop]
# Construct aggregate columns by summing across ownership types
suffixes = ['_muni', '_locgov', '_private']
agg_stems = set()
for c in epa.columns:
    for s in suffixes:
        if c.endswith(s):
            agg_stems.add(c[:-len(s)])
for stem in sorted(agg_stems):
    parts = [f'{stem}{s}' for s in suffixes if f'{stem}{s}' in epa.columns]
    if len(parts) > 1:
        epa[stem] = epa[parts].sum(axis=1)
        if stem not in epa_cols:
            epa_cols.append(stem)
# Construct derived aggregates used in regressions
if 'npdes_formal_any_muni' in epa.columns:
    epa['npdes_formal_any'] = ((epa['npdes_formal_any_muni'] > 0) |
                                (epa['npdes_formal_any_locgov'] > 0) |
                                (epa['npdes_formal_any_private'] > 0)).astype(int)
    if 'npdes_formal_any' not in epa_cols:
        epa_cols.append('npdes_formal_any')
if 'case_jdc_any_muni' in epa.columns:
    epa['case_jdc_any'] = ((epa['case_jdc_any_muni'] > 0) |
                            (epa['case_jdc_any_locgov'] > 0) |
                            (epa['case_jdc_any_private'] > 0)).astype(int)
    if 'case_jdc_any' not in epa_cols:
        epa_cols.append('case_jdc_any')
if 'case_afr_any_muni' in epa.columns:
    epa['case_afr_any'] = ((epa['case_afr_any_muni'] > 0) |
                            (epa['case_afr_any_locgov'] > 0) |
                            (epa['case_afr_any_private'] > 0)).astype(int)
    if 'case_afr_any' not in epa_cols:
        epa_cols.append('case_afr_any')
if 'case_all_any_muni' in epa.columns:
    epa['case_all_any'] = ((epa['case_all_any_muni'] > 0) |
                            (epa['case_all_any_locgov'] > 0) |
                            (epa['case_all_any_private'] > 0)).astype(int)
    if 'case_all_any' not in epa_cols:
        epa_cols.append('case_all_any')
epa_cols = [c for c in epa_cols if c in epa.columns]
df = safe_merge(df, epa[epa_cols], on=['fips7', 'year'], name='EPA ECHO')
log(f"  {len(epa_cols)} cols ({len(agg_stems)} aggregates constructed from ownership splits)")
# Fix: cities with no ECHO overflow data have genuinely zero overflow events (not missing).
# Two cases: (a) cities not in EPA source at all (no NPDES facilities — use regional sewers),
# (b) cities in EPA source but only for non-panel years (facility exists but no panel-year data).
# Both get overflow = 0: no overflow was reported for these city-years.
epa_overflow_cols = [c for c in df.columns if 'overflow' in c.lower() and not c.endswith('_lag')]
filled_overflow = 0
for c in epa_overflow_cols:
    n_before = df[c].isna().sum()
    df.loc[df[c].isna(), c] = 0
    filled = n_before - df[c].isna().sum()
    filled_overflow += filled
if filled_overflow > 0:
    log(f"  Filled {filled_overflow} NaN overflow values with 0 (no reported overflows)")


# ═══════════════════════════════════════════════════════════════════════
# 6. EPA STATE ENFORCEMENT — data/clean/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 6. EPA state enforcement ──")
es = pd.read_csv(ROOT / 'raw' / 'epa' / 'epa_state_enforcement.csv')
es_new = [c for c in es.columns if c not in df.columns and c not in ('city_name',)]
if es_new:
    df = safe_merge(df, es[['fips7', 'year'] + es_new], on=['fips7', 'year'], name='EPA state enforcement')


# ═══════════════════════════════════════════════════════════════════════
# 6b. EPA CAA Green Book county-level nonattainment (1992-2026 history)
#     Source: raw/epa_greenbook/phistory.xls + nayro.xls
#     Retrieved 2026-03-31 from https://www.epa.gov/green-book/green-book-data-download
#     Authority: US EPA Office of Air Quality Planning and Standards
#
#     PHISTORY encodes pw_YYYY column = "P" (part county in nonattainment that year)
#     or "W" (whole county). We treat both as nonattainment (binary 1) and also
#     retain the W/P distinction as `caa_*_whole` variants for robustness.
#
#     NAYRO provides the classification ordinal (Marginal/Moderate/Serious/Severe/
#     Extreme for ozone) which we merge per (county, pollutant).
# ═══════════════════════════════════════════════════════════════════════
log("\n── 6b. EPA CAA Green Book nonattainment ──")
gb_dir = ROOT / 'raw' / 'epa_greenbook'
phistory_path = gb_dir / 'phistory.xls'
nayro_path = gb_dir / 'nayro.xls'

if phistory_path.exists():
    ph = pd.read_excel(phistory_path, sheet_name='phistory')
    log(f"  PHISTORY: {ph.shape[0]} (county × pollutant) rows, "
        f"{ph['pollutant'].nunique()} pollutants")

    # Build 5-digit county FIPS from state + county. Drop rows with missing FIPS
    # (rare; occasional non-county tribal/territorial rows).
    ph = ph.dropna(subset=['fips_state', 'fips_cnty']).copy()
    ph['county_fips5'] = (
        ph['fips_state'].astype(int) * 1000 + ph['fips_cnty'].astype(int)
    )

    # Pollutant → short code mapping (NAAQS-aware, includes revocation metadata).
    # Keys use uppercase and punctuation preserved; short codes are safe for
    # Python identifiers.
    pollutant_code = {
        '8-Hour Ozone (2008)': 'ozone_2008',
        '8-Hour Ozone (2015)': 'ozone_2015',
        '8-Hour Ozone (1997)': 'ozone_1997',  # revoked
        '1-Hour Ozone (1979)': 'ozone_1hr',   # revoked
        'PM-2.5 (2012)':       'pm25_2012',
        'PM-2.5 (2006)':       'pm25_2006',   # revoked 2015
        'PM-2.5 (1997)':       'pm25_1997',   # revoked
        'PM-10 (1987)':        'pm10_1987',
        'Carbon Monoxide (1971)': 'co_1971',
        'Sulfur Dioxide (2010)': 'so2_2010',
        'Sulfur Dioxide (1971)': 'so2_1971',  # largely revoked
        'Lead (2008)':         'pb_2008',
        'Lead (1978)':         'pb_1978',      # revoked
        'Nitrogen Dioxide (1971)': 'no2_1971',
    }
    ph['pollutant_code'] = ph['pollutant'].map(pollutant_code)
    unknown = ph[ph['pollutant_code'].isna()]['pollutant'].unique()
    if len(unknown):
        log(f"  WARNING — unmapped pollutants: {list(unknown)}")

    # Tag which NAAQS are currently in force (not revoked). This drives the
    # primary aggregate `caa_any_criteria_nonattainment` variable.
    current_naaqs = {
        'ozone_2008', 'ozone_2015',  # 2008 is being phased out but still binding
        'pm25_2012',
        'pm10_1987',  # still in force
        'co_1971',    # still in force
        'so2_2010',
        'pb_2008',
        'no2_1971',
    }

    # Melt the pw_YYYY columns into long form (county × pollutant × year).
    year_cols = [c for c in ph.columns if c.startswith('pw_')]
    ph_long = ph.melt(
        id_vars=['county_fips5', 'pollutant_code', 'revoked_naaqs'],
        value_vars=year_cols,
        var_name='year', value_name='na_status',
    )
    ph_long['year'] = ph_long['year'].str.replace('pw_', '').astype(int)
    # na_status is "P" (part), "W" (whole), or NaN (not in nonattainment).
    ph_long['nonattain_any'] = ph_long['na_status'].notna().astype(int)
    ph_long['nonattain_whole'] = (ph_long['na_status'] == 'W').astype(int)
    log(f"  PHISTORY melted: {len(ph_long):,} county-pollutant-year rows; "
        f"{int(ph_long['nonattain_any'].sum()):,} nonattainment observations")

    # Aggregate per (county_fips5, year): build the criterion-pollutant indicators.
    def _aggregate(pollutants_set, name, wide_col):
        """For each (county, year), 1 iff any pollutant in the set is nonattainment."""
        sub = ph_long[ph_long['pollutant_code'].isin(pollutants_set)]
        agg = sub.groupby(['county_fips5', 'year'])[wide_col].max().reset_index()
        agg = agg.rename(columns={wide_col: name})
        return agg

    # Ozone (any — 2008 or 2015 currently binding).
    caa_ozone = _aggregate({'ozone_2008', 'ozone_2015'}, 'caa_ozone_nonattainment_any', 'nonattain_any')
    caa_ozone_whole = _aggregate({'ozone_2008', 'ozone_2015'},
                                  'caa_ozone_nonattainment_whole', 'nonattain_whole')

    # PM2.5 (current 2012 + phased-out 2006).
    caa_pm25 = _aggregate({'pm25_2012'}, 'caa_pm25_2012_nonattainment', 'nonattain_any')

    # PM10, CO, SO2, Lead (current NAAQS each).
    caa_pm10 = _aggregate({'pm10_1987'}, 'caa_pm10_nonattainment', 'nonattain_any')
    caa_co = _aggregate({'co_1971'}, 'caa_co_nonattainment', 'nonattain_any')
    caa_so2 = _aggregate({'so2_2010'}, 'caa_so2_nonattainment', 'nonattain_any')
    caa_pb = _aggregate({'pb_2008'}, 'caa_lead_nonattainment', 'nonattain_any')

    # Any current NAAQS.
    caa_any = _aggregate(current_naaqs, 'caa_any_criteria_nonattainment', 'nonattain_any')

    # Merge all CAA indicators into a single county-year panel, then left-join
    # to the main city-year panel on county_fips5.
    caa = caa_any
    for extra in [caa_ozone, caa_ozone_whole, caa_pm25, caa_pm10, caa_co, caa_so2, caa_pb]:
        caa = caa.merge(extra, on=['county_fips5', 'year'], how='outer')
    caa = caa.fillna(0)

    # If nayro.xls is available, add the ozone classification ordinal.
    if nayro_path.exists():
        na = pd.read_excel(nayro_path, sheet_name='nayro')
        na = na.dropna(subset=['fips_state', 'fips_cnty']).copy()
        na['county_fips5'] = (
            na['fips_state'].astype(int) * 1000 + na['fips_cnty'].astype(int)
        )
        na['pollutant_code'] = na['pollutant'].map(pollutant_code)
        # Classification ordinal for ozone (2008 or 2015): map strings → 1-5.
        class_ordinal = {
            'Marginal': 1, 'Marginal (Rural Transport)': 1, 'Rural Transport (Marginal)': 1,
            'Moderate': 2, 'Moderate <= 12.7ppm': 2, 'Moderate > 12.7ppm': 2,
            'Serious': 3,
            'Severe 15': 4, 'Severe 17': 4, 'Severe-15': 4, 'Severe-17': 4,
            'Extreme': 5,
            'Former Subpart 1': 0, 'Not Classified': 0, 'Incomplete Data': 0,
        }
        na_ozone = na[na['pollutant_code'].isin({'ozone_2008', 'ozone_2015'})].copy()
        na_ozone['class_ord'] = na_ozone['class'].map(class_ordinal).fillna(0).astype(int)
        # One observation per county (max across ozone standards).
        na_class = na_ozone.groupby('county_fips5')['class_ord'].max().reset_index()
        na_class = na_class.rename(columns={'class_ord': 'caa_ozone_class_ordinal'})
        caa = caa.merge(na_class, on='county_fips5', how='left')
        # Classification ordinal is time-invariant (current snapshot). Cities in
        # counties with no ozone nonattainment history get 0.
        caa['caa_ozone_class_ordinal'] = caa['caa_ozone_class_ordinal'].fillna(0).astype(int)
        log(f"  NAYRO: merged {int(caa['caa_ozone_class_ordinal'].gt(0).sum()):,} "
            f"county-years with ozone classification ordinal")

    # Retain only panel years (2013-2025). Green Book covers 1992-2026.
    caa = caa[(caa['year'] >= 2013) & (caa['year'] <= 2025)]

    if 'county_fips5' in df.columns:
        # NaN county_fips5 = city not matched in crosswalk; preserve but don't cast.
        df['county_fips5'] = pd.to_numeric(df['county_fips5'], errors='coerce')
        caa['county_fips5'] = pd.to_numeric(caa['county_fips5'], errors='coerce').astype('Int64')
        df['county_fips5'] = df['county_fips5'].astype('Int64')
        caa_cols = [c for c in caa.columns if c.startswith('caa_')]
        before = set(df.columns)
        df = df.merge(
            caa[['county_fips5', 'year'] + caa_cols].drop_duplicates(['county_fips5', 'year']),
            on=['county_fips5', 'year'], how='left', suffixes=('', '_CAA'),
        )
        for c in list(df.columns):
            if c.endswith('_CAA'):
                df = df.drop(columns=c)
        # Fill NaN with 0 (counties with no CAA nonattainment history).
        for c in caa_cols:
            if c in df.columns:
                df[c] = df[c].fillna(0)
        log(f"  Merged {len(caa_cols)} CAA variables onto city-year panel. "
            f"caa_any_criteria_nonattainment: "
            f"{int(df['caa_any_criteria_nonattainment'].sum()):,} positive city-years.")
    else:
        log("  [skip] county_fips5 not in panel yet — CAA merge requires it")
else:
    log(f"  [skip] PHISTORY not found at {phistory_path}")


# ═══════════════════════════════════════════════════════════════════════
# 7. VULCAN EMISSIONS — Vulcan_data.csv (2013-2024)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 7. Vulcan emissions (2013-2024) ──")
vulcan = pd.read_csv(ROOT / 'raw' / 'vulcan' / 'Vulcan_data.csv')
vulcan = vulcan.rename(columns={'fips': 'fips7'})
vulcan_new = [c for c in vulcan.columns if c not in df.columns and c not in ('geo_name', 'state_abb')]
if vulcan_new:
    df = safe_merge(df, vulcan[['fips7', 'year'] + vulcan_new], on=['fips7', 'year'], name='Vulcan')


# ═══════════════════════════════════════════════════════════════════════
# 8. NRI — data/clean/epa_nri/ (2013-2023, static risk indices)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 8. NRI natural risk ──")
nri = pd.read_csv(ROOT / 'raw' / 'nri' / 'epa_nri.csv')
nri_new = [c for c in nri.columns if c not in df.columns and c not in ('city_name',)]
if nri_new:
    df = safe_merge(df, nri[['fips7', 'year'] + nri_new], on=['fips7', 'year'], name='NRI')


# ═══════════════════════════════════════════════════════════════════════
# 9. ANTI-ESG LAWS — data/clean/antiesg_laws/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 9. Anti-ESG laws ──")
ae = pd.read_csv(ROOT / 'raw' / 'political' / 'antiesg_laws.csv')
ae_new = [c for c in ae.columns if c not in df.columns and c not in ('city_name',)]
if ae_new:
    df = safe_merge(df, ae[['fips7', 'year'] + ae_new], on=['fips7', 'year'], name='anti-ESG')
# Fix: overwrite NaN values for esg columns that were stale from the fiscal supplement
# (4 cities: Augusta-Richmond GA, Lexington-Fayette KY, Rio Rancho NM, West Valley City UT)
esg_overwrite_cols = [c for c in ae.columns if c.startswith('esg_') and c in df.columns]
if esg_overwrite_cols:
    ae_fill = ae.set_index(['fips7', 'year'])[esg_overwrite_cols]
    for c in esg_overwrite_cols:
        mask = df[c].isna()
        if mask.any():
            filled = 0
            for idx in df[mask].index:
                key = (df.loc[idx, 'fips7'], df.loc[idx, 'year'])
                if key in ae_fill.index:
                    val = ae_fill.loc[key, c]
                    if not pd.isna(val):
                        df.loc[idx, c] = val
                        filled += 1
            if filled > 0:
                log(f"  Patched {filled} NaN values in {c} from anti-ESG source")


# ═══════════════════════════════════════════════════════════════════════
# 10. STATE POLITICAL — data/clean/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 10. State political ──")
sp = pd.read_csv(ROOT / 'raw' / 'political' / 'state_political.csv')
sp_new = [c for c in sp.columns if c not in df.columns and c not in ('city_name',)]
if sp_new:
    df = safe_merge(df, sp[['fips7', 'year'] + sp_new], on=['fips7', 'year'], name='state political')


# ═══════════════════════════════════════════════════════════════════════
# 11. CLIMATE OPINION — data/clean/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 11. Climate opinion ──")
co = pd.read_csv(ROOT / 'raw' / 'climate' / 'climate_opinion_ycom.csv')
co_new = [c for c in co.columns if c not in df.columns and c not in ('city_name',)]
if co_new:
    df = safe_merge(df, co[['fips7', 'year'] + co_new], on=['fips7', 'year'], name='climate opinion')


# ═══════════════════════════════════════════════════════════════════════
# 12. PRESIDENTIAL ELECTIONS — data/clean/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 12. Presidential elections ──")
pe = pd.read_csv(ROOT / 'raw' / 'political' / 'presidential_elections.csv')
pe_new = [c for c in pe.columns if c not in df.columns and c not in ('city_name',)]
if pe_new:
    df = safe_merge(df, pe[['fips7', 'year'] + pe_new], on=['fips7', 'year'], name='presidential')


# ═══════════════════════════════════════════════════════════════════════
# 13. CLIMATE POLICY — data/clean/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 13. Climate policy ──")
cp = pd.read_csv(ROOT / 'raw' / 'climate' / 'climate_policy_controls.csv')
cp_new = [c for c in cp.columns if c not in df.columns and c not in ('city_name', 'state_abb')]
if cp_new:
    df = safe_merge(df, cp[['fips7', 'year'] + cp_new], on=['fips7', 'year'], name='climate policy')


# ═══════════════════════════════════════════════════════════════════════
# 14. FOG INSTITUTIONS — fog_institutions_panel_2010_2024.csv (2010-2024)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 14. FOG institutions (2010-2024) ──")
fog = pd.read_csv(ROOT / 'raw' / 'institutional' / 'fog_institutions_panel_2010_2024.csv')
fog = fog.rename(columns={'FIPS_7digit': 'fips7'})
fog_vars = ['fog', 'initiative', 'referendum', 'partisan', 'termlimits', 'termlength', 'districts']
fog_keep = ['fips7', 'year'] + [v for v in fog_vars if v in fog.columns and v not in df.columns]
if len(fog_keep) > 2:
    df = safe_merge(df, fog[fog_keep].drop_duplicates(subset=['fips7', 'year']), on=['fips7', 'year'], name='FOG')


# ═══════════════════════════════════════════════════════════════════════
# 15. TEL — data/clean/tel/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 15. TEL ──")
tel = pd.read_csv(ROOT / 'raw' / 'institutional' / 'tel.csv')
tel_new = [c for c in tel.columns if c not in df.columns and c not in ('city_name',)]
if tel_new:
    df = safe_merge(df, tel[['fips7', 'year'] + tel_new], on=['fips7', 'year'], name='TEL')


# ═══════════════════════════════════════════════════════════════════════
# 16. SRF — srf_processed/srf_bond_merged.csv (2013-2025)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 16. SRF (2013-2025) ──")
srf = pd.read_csv(ROOT / 'raw' / 'srf' / 'srf_bond_merged.csv')
# Identify the right FIPS column
fips_candidates = [c for c in srf.columns if 'fips' in c.lower() and 'county' not in c.lower() and 'state' not in c.lower()]
if fips_candidates:
    srf_fips_col = fips_candidates[0]
    srf = srf.rename(columns={srf_fips_col: 'fips7_srf'})
    srf['fips7'] = srf['fips7_srf'].astype(int)
    # Drop lowercase 'year' if 'Year' also exists (avoid duplicate after rename)
    if 'Year' in srf.columns and 'year' in srf.columns:
        srf = srf.drop(columns=['year'])
        srf = srf.rename(columns={'Year': 'year'})
    elif 'Year' in srf.columns:
        srf = srf.rename(columns={'Year': 'year'})
    srf_cols = [c for c in srf.columns if any(p in c.lower() for p in ['srf', 'dwsrf', 'cwsrf', 'portal', 'allotment', 'usaspending'])]
    srf_new = [c for c in srf_cols if c not in df.columns]
    if srf_new:
        df = safe_merge(df, srf[['fips7', 'year'] + srf_new].drop_duplicates(subset=['fips7', 'year']),
                        on=['fips7', 'year'], name='SRF')


# ═══════════════════════════════════════════════════════════════════════
# 17. ESG AUM — data/clean/esg_aum/ (year-level)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 17. ESG AUM ──")
ea = pd.read_csv(ROOT / 'raw' / 'market' / 'esg_aum.csv')
ea_vars = [c for c in ea.columns if c != 'year' and c not in df.columns]
if ea_vars:
    df = safe_merge(df, ea[['year'] + ea_vars], on=['year'], name='ESG AUM')


# ═══════════════════════════════════════════════════════════════════════
# 18. FEDERAL GREEN FUNDING — data/clean/ (2022-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 18. Federal green funding ──")
fg = pd.read_csv(ROOT / 'raw' / 'grants' / 'federal_green_funding.csv')
fg_new = [c for c in fg.columns if c not in df.columns and c not in ('state_abb',)]
if fg_new and 'state_abb' in df.columns:
    df = safe_merge(df, fg[['year', 'state_abb'] + fg_new], on=['year', 'state_abb'], name='federal green')


# ═══════════════════════════════════════════════════════════════════════
# 19. ADDITIONAL CITY VARS — additional_city_variables_2010_2024.csv
# ═══════════════════════════════════════════════════════════════════════
log("\n── 19. Additional city variables (2010-2024) ──")
addl_path = ROOT / 'raw' / 'census_acs' / 'additional_city_variables_2010_2024.csv'
if addl_path.exists():
    addl = pd.read_csv(addl_path)
    addl = addl.rename(columns={'fips': 'fips7', 'Year': 'year'})
    addl_new = [c for c in addl.columns if c not in df.columns and c not in ('GEO_ID_city', 'geo_name', 'county_geo_id')]
    if addl_new:
        df = safe_merge(df, addl[['fips7', 'year'] + addl_new], on=['fips7', 'year'], name='additional city vars')


# ═══════════════════════════════════════════════════════════════════════
# 20. ECONOMIC — data/clean/economic_bls_acs/ (2013-2023)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 20. Economic BLS/ACS ──")
ec = pd.read_csv(ROOT / 'raw' / 'census_acs' / 'economic_bls_acs.csv')
ec_new = [c for c in ec.columns if c not in df.columns and c not in ('city_name',)]
if ec_new:
    df = safe_merge(df, ec[['fips7', 'year'] + ec_new], on=['fips7', 'year'], name='economic')


# ═══════════════════════════════════════════════════════════════════════
# 21. NEW DATASETS — cross-sectional and time-varying
# ═══════════════════════════════════════════════════════════════════════
log("\n── 21. Bond referenda requirements (cross-sectional) ──")
br = pd.read_csv(ROOT / 'raw' / 'institutional' / 'state_bond_referenda_requirements.csv')
br_vars = ['state_abb', 'go_voter_approval_required', 'go_vote_threshold', 'go_supermajority',
           'revenue_bond_voter_approval', 'has_state_bond_commission', 'has_constitutional_debt_limit',
           'has_state_approval_body']
br_keep = [c for c in br_vars if c in br.columns and (c == 'state_abb' or c not in df.columns)]
if len(br_keep) > 1 and 'state_abb' in df.columns:
    df = safe_merge(df, br[br_keep], on=['state_abb'], name='bond referenda')

log("\n── 22. State green bond capacity (2013-2023, time-varying) ──")
sgb = pd.read_csv(ROOT / 'raw' / 'market' / 'state_green_bond_capacity.csv')
sgb_new = [c for c in sgb.columns if c not in df.columns and c != 'state_abb']
if sgb_new and 'state_abb' in df.columns:
    df = safe_merge(df, sgb[['state_abb', 'year'] + sgb_new], on=['state_abb', 'year'], name='state green bond capacity')

log("\n── 23. MSRB RFI ESG positions (cross-sectional) ──")
rfi = pd.read_csv(ROOT / 'raw' / 'political' / 'state_msrb_rfi_position.csv')
rfi['pro_esg_rfi_response'] = (rfi['msrb_rfi_position'] == 'pro_esg').astype(int)
rfi_keep = ['state_abb', 'signed_utah_antiesg_letter', 'pro_esg_rfi_response']
rfi_keep = [c for c in rfi_keep if c in rfi.columns and (c == 'state_abb' or c not in df.columns)]
if len(rfi_keep) > 1 and 'state_abb' in df.columns:
    df = safe_merge(df, rfi[rfi_keep], on=['state_abb'], name='MSRB RFI')

log("\n── 24. State bond banks (cross-sectional) ──")
bb_path = ROOT / 'raw' / 'institutional' / 'state_bond_banks.csv'
if bb_path.exists():
    bb = pd.read_csv(bb_path)
    bb_keep = ['state_abb', 'has_bond_bank', 'bond_bank_rating']
    bb_keep = [c for c in bb_keep if c in bb.columns and (c == 'state_abb' or c not in df.columns)]
    if len(bb_keep) > 1 and 'state_abb' in df.columns:
        df = safe_merge(df, bb[bb_keep], on=['state_abb'], name='bond banks')


# ═══════════════════════════════════════════════════════════════════════
# DERIVED VARIABLES
# ═══════════════════════════════════════════════════════════════════════
log("\n── Constructing derived variables ──")

# State-wide total green bond capacity (ALL issuers, not just state govt)
if 'State_Total_Amt_Issued' in df.columns and 'state_abb' in df.columns:
    log("  Building state-wide all-issuer green bond capacity...")
    state_yr = df.groupby(['state_abb','year']).agg({
        'State_Total_Amt_Issued': 'first',
        'State_Total_Issuance_Count': 'first'
    }).reset_index().sort_values(['state_abb','year'])
    state_yr['state_all_green_cum_amt'] = state_yr.groupby('state_abb')['State_Total_Amt_Issued'].cumsum()
    state_yr['state_all_green_cum_count'] = state_yr.groupby('state_abb')['State_Total_Issuance_Count'].cumsum()
    state_yr['state_all_green_cum_amt_lag1'] = state_yr.groupby('state_abb')['state_all_green_cum_amt'].shift(1)
    state_yr['state_all_green_cum_count_lag1'] = state_yr.groupby('state_abb')['state_all_green_cum_count'].shift(1)
    state_yr['asinh_state_all_green_cum_amt_lag1'] = np.arcsinh(state_yr['state_all_green_cum_amt_lag1'])
    merge_cols = ['state_abb','year','state_all_green_cum_amt','state_all_green_cum_count',
                  'state_all_green_cum_amt_lag1','state_all_green_cum_count_lag1',
                  'asinh_state_all_green_cum_amt_lag1']
    df = safe_merge(df, state_yr[merge_cols], on=['state_abb','year'], name='state-wide green capacity')

# asinh green bond amount
df['asinh_green_amt'] = np.arcsinh(df['City_Green_Amt_Issued'])

# Three-level green bond classification
# Level 1: Project supply (Bloomberg-classified, no city choice) = Green_Bond_Issued
# Level 2: Labelling (city chose to call it green) = Y_self_green
# Level 3: Credibility (city paid for assurance/framework) = Y_esg_assurance, Y_esg_framework
# Incidentally green: Bloomberg says green, city never claimed it
df['incidentally_green'] = ((df['Green_Bond_Issued'] == 1) & (df['Y_self_green'] == 0)).astype(int)
df['Y_any_credibility'] = ((df['Y_esg_assurance'] == 1) | (df['Y_esg_framework'] == 1)).astype(int)

# Water-only and non-water indicators
water_cnt_cols = [c for c in df.columns if 'Sustainable_Water' in c and c.startswith('Count_ESG Project')]
non_water_cnt_cols = [c for c in df.columns if c.startswith('Count_ESG Project') and 'Sustainable_Water' not in c]
df['count_water'] = df[water_cnt_cols].sum(axis=1) if water_cnt_cols else 0
df['count_non_water'] = df[non_water_cnt_cols].sum(axis=1) if non_water_cnt_cols else 0
df['Y_water_only'] = ((df['count_water'] > 0) & (df['count_non_water'] == 0) & (df['Green_Bond_Issued'] == 1)).astype(int)
df['Y_has_non_water'] = (df['count_non_water'] > 0).astype(int)

# N ESG categories
df['N_esg_categories'] = 0
for c in [c for c in df.columns if c.startswith('Count_ESG Project Categories__') and ',' not in c]:
    df['N_esg_categories'] += (df[c] > 0).astype(int)

# Switcher cities
df_party = df.dropna(subset=['Rep_Mayor'])
switchers = df_party.groupby('fips7')['Rep_Mayor'].nunique()
switcher_ids = switchers[switchers > 1].index
df['is_switcher'] = df['fips7'].isin(switcher_ids).astype(int)

# State ID for FE
if 'state_abb' in df.columns:
    df['state_id'] = df['state_abb'].astype('category').cat.codes

# Log transforms
for raw, logged in [('population_city', 'log_population_city'),
                     ('percapita_income_city', 'log_percapita_income_city'),
                     ('totalincome_city', 'log_totalincome_city')]:
    if raw in df.columns and logged not in df.columns:
        df[logged] = np.log(df[raw].clip(lower=1))

# ── Forward-fill slow-moving / cross-sectional variables into 2024-2025 ──
log("\n── Forward-filling slow-moving variables ──")
df = df.sort_values(['fips7', 'year'])
ff_count = 0

# NRI risk indices (static), TEL limits (rarely change), FOG (cross-sectional),
# anti-ESG laws (cumulative, only grow), state political (annual but lagging source),
# climate policy (commitments persist), presidential vote (carry forward last election)
ff_prefixes = ['nri_', 'tel_overall', 'tel_specific', 'tel_levy', 'tel_assessment',
               'tel_general_', 'tel_full_disclosure', 'tel_stringency',
               'fog', 'initiative', 'referendum', 'partisan', 'termlimits', 'termlength', 'districts',
               'esg_has_', 'esg_cum_', 'esg_num_', 'esg_law_', 'esg_governor_', 'esg_msrb_',
               'esg_first_', 'esg_has_proesg', 'esg_has_fossil', 'esg_has_esg_disclosure',
               'esg_has_board_diversity',
               'state_dem_', 'state_rep_', 'state_dem_governor', 'state_legis_control',
               'state_govt_trifecta', 'state_divided_govt',
               'c40_member', 'mayors_climate_signatory', 'iclei_member', 'climate_commitment_score',
               'state_rps_', 'state_carbon_', 'state_climate_plan',
               'pres_dem_vote_share', 'pres_rep_vote_share', 'pres_dem_two_party_share',
               'epa_state_stringency_index', 'epa_state_response_rate',
               'state_green_bond_ever', 'state_green_bond_cum_']

for c in df.columns:
    if any(c.startswith(p) or c == p for p in ff_prefixes):
        na_before = df[c].isna().sum()
        if na_before > 0:
            df[c] = df.groupby('fips7')[c].ffill()
            na_after = df[c].isna().sum()
            if na_after < na_before:
                ff_count += 1

log(f"  Forward-filled {ff_count} variables")

# ── Lag construction (1-4 years) for key variables ──
# NOTE: Overwrite any stale pre-built lags from data/clean/ files (which stop at 2023)
# by removing the "if lag_name not in df.columns" guard for critical variables
log("\n── Constructing lags (1-4) ──")
df = df.sort_values(['fips7', 'year'])

# Water infrastructure lags
lag_vars_4 = ['cwns_needs_real', 'pct_deficient']
# Fiscal lags
lag_vars_4 += ['reserve_ratio', 'debt_service_burden', 'operating_balance', 'fiscal_stress_index']
# Enforcement lags (from EPA authoritative)
lag_vars_4 += ['npdes_formal_count', 'npdes_formal_cum', 'case_jdc_count', 'case_jdc_cum',
               'case_jdc_any', 'case_all_count', 'case_afr_count', 'overflow_events']
# Demographics and economic (lag-2 enables full 2013-2025 coverage for 2023-ending sources)
lag_vars_4 += ['log_population_city', 'log_percapita_income_city', 'unemployment_city']
# Fiscal capacity lags (lag-2 minimum for full coverage)
lag_vars_2 = ['sewerage_expend', 'expenditure_rigidity', 'revenue_hhi',
              'net_borrowing_ratio', 'highways_expend', 'direct_expenditure_pc',
              'total_expenditure_pc', 'net_borrowing_intensity',
              'police_expend', 'health_hospitals_expend', 'solid_waste_expend',
              # Revenue structure / fiscal federalism (for 2024-2025 coverage)
              'charges_to_own_source', 'tax_autonomy_ratio', 'vfi',
              'days_cash', 'debt_affordability', 'tax_effort_pc',
              'property_tax_dependence', 'own_source_rev_share',
              'fiscal_self_sufficiency', 'expenditure_gap_pc',
              'short_term_debt_share', 'chg_sewerage',
              'budget_flexibility_squeeze', 'rating_agency_composite',
              'dsb_worsening', 'operating_deficit', 'low_reserves',
              # State green bond capacity (forward-filled, rebuild lag-1)
              'state_green_bond_ever', 'state_green_bond_cum_count',
              'state_green_bond_cum_amt']

lag_count = 0
for var in lag_vars_4:
    if var not in df.columns:
        continue
    for k in range(1, 5):
        lag_name = f'{var}_lag{k}'
        # Always rebuild lags from the current (extended) data, overwriting any stale
        # pre-built lags from data/clean/ files that stopped at 2023
        df[lag_name] = df.groupby('fips7')[var].shift(k)
        lag_count += 1

for var in lag_vars_2:
    if var not in df.columns:
        continue
    for k in range(1, 3):
        lag_name = f'{var}_lag{k}'
        df[lag_name] = df.groupby('fips7')[var].shift(k)
        lag_count += 1

# Prior-3yr rolling indicators for enforcement
for var in ['npdes_formal_any', 'case_jdc_any', 'case_afr_any', 'case_all_any']:
    if var not in df.columns:
        continue
    roll_name = f'{var}_prior3yr'
    shifted = df.groupby('fips7')[var].shift(1).fillna(0)
    for k in [2, 3]:
        shifted = shifted + df.groupby('fips7')[var].shift(k).fillna(0)
    df[roll_name] = (shifted > 0).astype(int)
    lag_count += 1

# NRI water risk composite (from NRI full-name columns in fiscal_tel_merged)
water_risk_cols = [c for c in df.columns if 'Hazard Type Risk Index Rating' in c and
                   any(p in c for p in ['Inland Flooding', 'Coastal Flooding', 'Hurricane', 'Tsunami'])]
if water_risk_cols:
    # Convert ratings to numeric: Very Low=1, Relatively Low=2, Relatively Moderate=3, Relatively High=4, Very High=5
    rating_map = {'Very Low': 1, 'Relatively Low': 2, 'Relatively Moderate': 3, 'Relatively High': 4, 'Very High': 5}
    for c in water_risk_cols:
        df[c + '_num'] = df[c].map(rating_map)
    num_cols = [c + '_num' for c in water_risk_cols]
    df['nri_water_risk_score'] = df[num_cols].mean(axis=1)
    df.drop(columns=num_cols, inplace=True)
    lag_count += 1
    log(f"  Built nri_water_risk_score from {len(water_risk_cols)} rating columns")

# NRI overall risk score
if 'National Risk Index - Score - Composite' in df.columns:
    df['nri_overall_risk_score'] = df['National Risk Index - Score - Composite']
    lag_count += 1

log(f"  Created {lag_count} new lag/derived variables")

# ── Trim pre-2013 rows (only needed for lag construction) ──
pre_2013_mask = df['year'] < 2013
if pre_2013_mask.sum() > 0:
    log(f"\n── Trimming {pre_2013_mask.sum()} pre-2013 rows (lag scaffolding) ──")
    df = df[~pre_2013_mask].reset_index(drop=True)

log(f"\n{'='*70}")
log(f"FINAL PANEL: {df.shape[0]:,} rows x {df.shape[1]:,} cols")
log(f"Cities: {df['fips7'].nunique()}, Years: {df['year'].min()}-{df['year'].max()}")
log(f"Green bonds: {df['Green_Bond_Issued'].sum():.0f}")
if 'Rep_Mayor' in df.columns:
    log(f"Rep_Mayor: D={int((df['Rep_Mayor']==0).sum())}, R={int((df['Rep_Mayor']==1).sum())}, NA={int(df['Rep_Mayor'].isna().sum())}")
    log(f"Switcher cities: {len(switcher_ids)}")
log(f"{'='*70}")

# Save
df.to_pickle(OUT / 'panel.pkl')
log(f"\nSaved: {OUT / 'panel.pkl'}")
