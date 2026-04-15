"""
01_construct_audit_variables.py — Build missing variables from existing sources
================================================================================
Constructs variables flagged as EASY/BUILDABLE in the variable_list_audit.md
completeness audit. Run after 00_build_panel.py; patches panel.pkl in place.

Inputs: pipeline/panel.pkl + 8 data/clean/ source files
Output: pipeline/panel.pkl (patched with new columns)
"""

import pandas as pd
import numpy as np
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')
ROOT = Path(__file__).resolve().parent.parent
PANEL_PATH = Path(__file__).resolve().parent.parent / 'processed' / 'panel' / 'panel.pkl'

df = pd.read_pickle(PANEL_PATH)
n_cols_before = len(df.columns)
print(f"Panel: {df.shape}")


def log(msg):
    print(msg)


# ═══════════════════════════════════════════════════════════════════════
# 1. CATEGORY OUTCOME DVs (O4, O7–O13)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 1. Category outcome DVs ──")

# O4: asinh of self-labelled green bond amount
if 'Amt_Self-reported Green__Yes' in df.columns:
    df['asinh_self_green_amt'] = np.arcsinh(df['Amt_Self-reported Green__Yes'].fillna(0))
    log(f"  O4 asinh_self_green_amt: {(df['asinh_self_green_amt'] > 0).sum()} positive")

# O7–O12: category-specific binary DVs
# A bond has a category if ANY Count_ column containing that category name is > 0
category_map = {
    'Y_Clean_Transportation': 'Clean_Transportation',
    'Y_Renewable_Energy': 'Renewable_Energy',
    'Y_Energy_Efficiency': 'Energy_Efficiency',
    'Y_Green_Buildings': 'Green_Buildings',
    'Y_Climate_Change_Adaptation': 'Climate_Change_Adaptation',
    'Y_Pollution_Control': 'Pollution_Control',
}

for yvar, cat_key in category_map.items():
    cat_cols = [c for c in df.columns if c.startswith('Count_ESG Project Categories__') and cat_key in c]
    if cat_cols:
        df[yvar] = (df[cat_cols].sum(axis=1) > 0).astype(int)
        log(f"  {yvar}: {df[yvar].sum()} positive city-years (from {len(cat_cols)} count cols)")

# O13: category composition share (water-only share among self-labelled issuers)
if 'Y_self_green' in df.columns and 'Y_water_only' in df.columns:
    df['category_composition_share'] = np.where(
        df['Y_self_green'] == 1,
        df['Y_water_only'].astype(float),
        np.nan
    )
    log(f"  O13 category_composition_share: {df['category_composition_share'].notna().sum()} obs")

# O14-O15: Additional ESG credibility outcomes for Table 3 (user-requested).
# These are distinct Bloomberg fields capturing specific operational dimensions
# of ESG credibility investment beyond assurance + framework + reporting:
#
#   Y_Mgmt_Proceeds_Yes: bond explicitly ring-fences proceeds for green use
#                        (management-of-proceeds commitment). Bloomberg's
#                        `Mgmt of Proc__Yes` field.
#   Y_Proj_Selection_Yes: bond documents pre-screen process for eligible
#                         projects. Bloomberg's `Proj Sel Proc__Yes` field.
#
# Plus matching asinh-amount variables for intensive-margin analysis.
credibility_map = {
    'Y_Mgmt_Proceeds_Yes':  ('Count_Mgmt of Proc__Yes',   'Amt_Mgmt of Proc__Yes'),
    'Y_Proj_Selection_Yes': ('Count_Proj Sel Proc__Yes',  'Amt_Proj Sel Proc__Yes'),
}
for yvar, (cnt_col, amt_col) in credibility_map.items():
    if cnt_col in df.columns:
        df[yvar] = (df[cnt_col] > 0).astype(int)
        log(f"  {yvar}: {int(df[yvar].sum())} positive city-years")
    else:
        log(f"  [skip] {yvar}: source {cnt_col} missing")
    if amt_col in df.columns:
        amt_var = f'asinh_{yvar.replace("Y_", "").lower()}_amt'
        df[amt_var] = np.arcsinh(df[amt_col].fillna(0))
        log(f"  {amt_var}: {(df[amt_var] > 0).sum()} positive")


# ═══════════════════════════════════════════════════════════════════════
# 2. SIMPLE LAGS AND DERIVATIONS (S11, F11)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 2. Simple lags ──")

df = df.sort_values(['fips7', 'year'])

# S11: pres_dem_vote_share_lag2
# NOTE: 00_build_panel.py now builds pres_*_lag1/lag2 BEFORE trimming
# pre-2013 rows so that lag-2 values for 2013-2014 reach back to 2011/2012
# MEDSL data. Only re-build here if the pre-trim lag is absent.
if 'pres_dem_vote_share' in df.columns and 'pres_dem_vote_share_lag2' not in df.columns:
    df['pres_dem_vote_share_lag2'] = df.groupby('fips7')['pres_dem_vote_share'].shift(2)
    log(f"  S11 pres_dem_vote_share_lag2 (post-trim fallback): {df['pres_dem_vote_share_lag2'].notna().sum()} non-null")
elif 'pres_dem_vote_share_lag2' in df.columns:
    log(f"  S11 pres_dem_vote_share_lag2: {df['pres_dem_vote_share_lag2'].notna().sum()} non-null (pre-trim from 00)")

# F11: capital_stock_pc_lag2
if 'capital_stock_pc' in df.columns:
    df['capital_stock_pc_lag2'] = df.groupby('fips7')['capital_stock_pc'].shift(2)
    log(f"  F11 capital_stock_pc_lag2: {df['capital_stock_pc_lag2'].notna().sum()} non-null")

# F10: log_cwsrf_obligations_lag2
if 'usaspending_cwsrf' in df.columns:
    df['log_cwsrf_obligations'] = np.log1p(df['usaspending_cwsrf'].fillna(0))
    df['log_cwsrf_obligations_lag2'] = df.groupby('fips7')['log_cwsrf_obligations'].shift(2)
    log(f"  F10 log_cwsrf_obligations_lag2: {df['log_cwsrf_obligations_lag2'].notna().sum()} non-null")


# ═══════════════════════════════════════════════════════════════════════
# 3. EPA ENFORCEMENT ROLLING 3-YEAR (C18–C20)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 3. EPA enforcement rolling 3yr (RCRA/Air/SDWA) ──")

# Build prior3yr rolling indicators from ownership-split columns
enforcement_map = {
    # C18: RCRA formal enforcement (hazardous waste)
    'rcra_formal_prior3yr_muni': 'rcra_enforcements_count_muni',
    'rcra_formal_prior3yr_locgov': 'rcra_enforcements_count_locgov',
    'rcra_formal_prior3yr_private': 'rcra_enforcements_count_private',
    # C19: Air formal enforcement (Clean Air Act)
    'air_formal_prior3yr_muni': 'air_formal_actions_count_muni',
    'air_formal_prior3yr_locgov': 'air_formal_actions_count_locgov',
    'air_formal_prior3yr_private': 'air_formal_actions_count_private',
    # C20: SDWA (Safe Drinking Water Act) — use sdwa_events_milestones as proxy
    'sdwa_formal_prior3yr_muni': 'sdwa_events_milestones_count_muni',
    'sdwa_formal_prior3yr_locgov': 'sdwa_events_milestones_count_locgov',
    'sdwa_formal_prior3yr_private': 'sdwa_events_milestones_count_private',
}

for new_var, source_var in enforcement_map.items():
    if source_var in df.columns:
        # Rolling 3-year: any positive value in t-1, t-2, or t-3
        s1 = df.groupby('fips7')[source_var].shift(1).fillna(0)
        s2 = df.groupby('fips7')[source_var].shift(2).fillna(0)
        s3 = df.groupby('fips7')[source_var].shift(3).fillna(0)
        df[new_var] = ((s1 + s2 + s3) > 0).astype(int)
        log(f"  {new_var}: {df[new_var].sum()} positive")
    else:
        log(f"  {new_var}: source {source_var} NOT IN PANEL")


# ═══════════════════════════════════════════════════════════════════════
# 4. MUNICIPAL UTILITIES (C10)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 4. Municipal utilities ──")
muni_util_path = ROOT / 'raw' / 'energy_policy' / 'municipal_electric_utilities.csv'
if muni_util_path.exists():
    mu = pd.read_csv(muni_util_path)
    # This file has city_name + state_abb but no fips — merge via name match
    if 'has_municipal_electric' in mu.columns and 'city_name' in mu.columns:
        city_lookup = df[['fips7', 'city_name', 'state_abb']].drop_duplicates('fips7')
        mu_merged = city_lookup.merge(mu[['city_name', 'state_abb', 'has_municipal_electric']],
                                       on=['city_name', 'state_abb'], how='left')
        mu_merged['has_municipal_electric'] = mu_merged['has_municipal_electric'].fillna(0).astype(int)
        df = df.merge(mu_merged[['fips7', 'has_municipal_electric']], on='fips7', how='left',
                       suffixes=('', '_MU'))
        if 'has_municipal_electric_MU' in df.columns:
            df['has_municipal_electric'] = df['has_municipal_electric_MU']
            df = df.drop(columns='has_municipal_electric_MU')
        log(f"  C10 has_municipal_electric: {int(df['has_municipal_electric'].sum())} positive ({df['has_municipal_electric'].mean()*100:.1f}%)")
    else:
        log(f"  C10: columns={list(mu.columns)}")
else:
    log(f"  C10: file not found")


# ═══════════════════════════════════════════════════════════════════════
# 5. STATE ENERGY POLICY (C9, C12, C14, C15)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 5. State energy policy ──")

# RPS stringency — already have state_rps_active and state_rps_target_pct in panel
if 'state_rps_active' in df.columns and 'state_rps_target_pct' in df.columns:
    df['state_rps_stringency'] = df['state_rps_active'] * df['state_rps_target_pct']
    log(f"  C9 state_rps_stringency: {(df['state_rps_stringency'] > 0).sum()} positive")

# Building codes and EERS from state_energy_policy
codes_path = ROOT / 'raw' / 'energy_policy' / 'state_building_codes.csv'
if codes_path.exists():
    codes = pd.read_csv(codes_path)
    if 'state_abb' in codes.columns:
        code_vars = ['state_building_code_residential_iecc', 'state_building_code_commercial_iecc',
                     'state_has_commercial_benchmarking']
        code_keep = ['state_abb'] + [c for c in code_vars if c in codes.columns]
        codes_merge = codes[code_keep].drop_duplicates('state_abb')
        # Rename for audit variables
        rename = {'state_building_code_residential_iecc': 'iecc_vintage',
                  'state_has_commercial_benchmarking': 'local_benchmark_ordinance'}
        codes_merge = codes_merge.rename(columns={k: v for k, v in rename.items() if k in codes_merge.columns})
        before = set(df.columns)
        df = df.merge(codes_merge, on='state_abb', how='left', suffixes=('', '_NEW'))
        for c in df.columns:
            if c.endswith('_NEW'):
                base = c[:-4]
                df[base] = df[c]
                df = df.drop(columns=c)
        new_cols = set(df.columns) - before
        log(f"  C14/C15 building codes: added {len(new_cols)} cols")

cef_path = ROOT / 'raw' / 'energy_policy' / 'state_clean_energy_funds.csv'
if cef_path.exists():
    cef = pd.read_csv(cef_path)
    if 'state_abb' in cef.columns:
        cef_vars = ['state_eers_target', 'state_eers_has']
        cef_keep = ['state_abb'] + [c for c in cef_vars if c in cef.columns]
        cef_merge = cef[cef_keep].drop_duplicates('state_abb')
        if 'state_eers_target' in cef_merge.columns:
            cef_merge = cef_merge.rename(columns={'state_eers_target': 'state_eers_stringency'})
        before = set(df.columns)
        df = df.merge(cef_merge, on='state_abb', how='left', suffixes=('', '_NEW'))
        for c in list(df.columns):
            if c.endswith('_NEW'):
                df[c[:-4]] = df[c]
                df = df.drop(columns=c)
        new_cols = set(df.columns) - before
        log(f"  C12 EERS: added {len(new_cols)} cols")


# ═══════════════════════════════════════════════════════════════════════
# 6. FEMA DISASTERS (C16)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 6. FEMA disasters ──")
fema_path = ROOT / 'raw' / 'disasters' / 'fema_disaster_declarations.csv'
if fema_path.exists():
    fema = pd.read_csv(fema_path)
    # This is county-year level; merge on county_fips5 + year
    fips_col = [c for c in fema.columns if 'fips' in c.lower() and 'county' in c.lower()]
    if not fips_col:
        fips_col = [c for c in fema.columns if 'fips' in c.lower()]

    if fips_col and 'county_fips5' in df.columns:
        fc = fips_col[0]
        fema[fc] = fema[fc].astype(str).str.replace('.0', '', regex=False)
        df['county_fips5_str'] = df['county_fips5'].astype(str).str.replace('.0', '', regex=False)

        # Build 5-year rolling disaster count
        if 'fema_disaster_count' in fema.columns and 'year' in fema.columns:
            fema_agg = fema.groupby([fc, 'year']).agg(
                fema_disaster_count=('fema_disaster_count', 'sum'),
                fema_disaster_any=('fema_disaster_any', 'max')
            ).reset_index()
            fema_agg = fema_agg.rename(columns={fc: 'county_fips5_str'})

            before = set(df.columns)
            df = df.merge(fema_agg, left_on=['county_fips5_str', 'year'],
                         right_on=['county_fips5_str', 'year'], how='left',
                         suffixes=('', '_FEMA'))
            for c in list(df.columns):
                if c.endswith('_FEMA'):
                    df[c[:-5]] = df[c]
                    df = df.drop(columns=c)

            # Build prior-5yr rolling
            df = df.sort_values(['fips7', 'year'])
            df['fema_disaster_count'] = df['fema_disaster_count'].fillna(0)
            rolling = pd.Series(0.0, index=df.index)
            for k in range(1, 6):
                rolling = rolling + df.groupby('fips7')['fema_disaster_count'].shift(k).fillna(0)
            df['fema_disaster_declarations_prior5yr'] = rolling
            log(f"  C16 fema_disaster_declarations_prior5yr: {(df['fema_disaster_declarations_prior5yr'] > 0).sum()} positive")

        df = df.drop(columns='county_fips5_str', errors='ignore')
    else:
        log(f"  C16: merge key issue (fips_col={fips_col})")
else:
    log(f"  C16: file not found")


# ═══════════════════════════════════════════════════════════════════════
# 7. NFIP FLOOD (C17)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 7. NFIP flood ──")
nfip_path = ROOT / 'raw' / 'disasters' / 'nfip_flood_claims.csv'
if nfip_path.exists():
    nfip = pd.read_csv(nfip_path)
    fips_col = [c for c in nfip.columns if 'fips' in c.lower() and 'county' in c.lower()]
    if not fips_col:
        fips_col = [c for c in nfip.columns if 'fips' in c.lower()]

    if fips_col and 'nfip_repetitive_loss' in nfip.columns:
        fc = fips_col[0]
        nfip[fc] = nfip[fc].astype(str).str.replace('.0', '', regex=False)
        df['county_fips5_str'] = df['county_fips5'].astype(str).str.replace('.0', '', regex=False)

        nfip_merge = nfip[[fc, 'nfip_repetitive_loss', 'nfip_total_properties']].copy()
        nfip_merge = nfip_merge.rename(columns={fc: 'county_fips5_str'})
        nfip_merge = nfip_merge.drop_duplicates('county_fips5_str')

        before = set(df.columns)
        df = df.merge(nfip_merge, on='county_fips5_str', how='left', suffixes=('', '_NFIP'))
        for c in list(df.columns):
            if c.endswith('_NFIP'):
                df[c[:-5]] = df[c]
                df = df.drop(columns=c)

        # Per capita
        if 'population_city' in df.columns and 'nfip_repetitive_loss' in df.columns:
            df['nfip_repetitive_loss_pc'] = df['nfip_repetitive_loss'] / df['population_city'].clip(lower=1)
            log(f"  C17 nfip_repetitive_loss_pc: {df['nfip_repetitive_loss_pc'].notna().sum()} non-null")

        df = df.drop(columns='county_fips5_str', errors='ignore')
else:
    log(f"  C17: file not found")


# ═══════════════════════════════════════════════════════════════════════
# 8. FEDERAL GRANTS / TRANSIT (C6, C8)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 8. Federal grants and transit ──")

# Federal grants (has iija_transit_grant_amt)
fg_path = ROOT / 'raw' / 'grants' / 'federal_grants_panel.csv'
if fg_path.exists():
    fg = pd.read_csv(fg_path)
    fips_col = [c for c in fg.columns if 'fips' in c.lower()][0]
    fg = fg.rename(columns={fips_col: 'fips7'})
    fg_new = [c for c in fg.columns if c not in df.columns and c not in ('city_name', 'state_abb', 'year', 'fips7')]
    if fg_new:
        df = df.merge(fg[['fips7', 'year'] + fg_new].drop_duplicates(['fips7', 'year']),
                       on=['fips7', 'year'], how='left', suffixes=('', '_FG'))
        for c in list(df.columns):
            if c.endswith('_FG'):
                df = df.drop(columns=c)
        log(f"  C6 federal_grants: added {len(fg_new)} cols (incl iija_transit)")
    else:
        log(f"  C6 federal_grants: no new columns")

# State transit
st_path = ROOT / 'raw' / 'grants' / 'state_transit_funding.csv'
if st_path.exists():
    st = pd.read_csv(st_path)
    if 'state_abb' in st.columns and 'year' in st.columns:
        st_new = [c for c in st.columns if c not in df.columns and c not in ('state_abb', 'year')]
        if st_new:
            df = df.merge(st[['state_abb', 'year'] + st_new].drop_duplicates(['state_abb', 'year']),
                           on=['state_abb', 'year'], how='left', suffixes=('', '_ST'))
            for c in list(df.columns):
                if c.endswith('_ST'):
                    df = df.drop(columns=c)
            log(f"  C8 state_transit: added {len(st_new)} cols")


# ═══════════════════════════════════════════════════════════════════════
# 9. SUBSTITUTE ISSUER (F13)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 9. Substitute issuer ──")
sub_path = ROOT / 'raw' / 'geospatial' / 'substitute_water_panel.csv'
if sub_path.exists():
    sub = pd.read_csv(sub_path)
    fips_col = [c for c in sub.columns if 'fips' in c.lower()][0]
    sub = sub.rename(columns={fips_col: 'fips7'})
    if 'substitute_water_any_25km' in sub.columns:
        sub_vars = [c for c in sub.columns if c not in df.columns and c not in ('city_name', 'state_abb', 'year', 'fips7')]
        if sub_vars:
            df = df.merge(sub[['fips7', 'year'] + sub_vars].drop_duplicates(['fips7', 'year']),
                           on=['fips7', 'year'], how='left', suffixes=('', '_SUB'))
            for c in list(df.columns):
                if c.endswith('_SUB'):
                    df = df.drop(columns=c)
        # Map to has_substitute_issuer
        if 'substitute_water_any_25km' in df.columns:
            df['has_substitute_issuer'] = df['substitute_water_any_25km']
            log(f"  F13 has_substitute_issuer: {int(df['has_substitute_issuer'].sum())} positive")
        log(f"  Substitute water vars: added {len(sub_vars)} cols")


# ═══════════════════════════════════════════════════════════════════════
# 10. RPS × MUNICIPAL ELECTRIC INTERACTION (C11)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 10. Interactions ──")
if 'state_rps_stringency' in df.columns and 'has_municipal_electric' in df.columns:
    df['rps_x_muni_electric'] = df['state_rps_stringency'] * df['has_municipal_electric']
    log(f"  C11 rps_x_muni_electric: {(df['rps_x_muni_electric'] > 0).sum()} positive")


# ═══════════════════════════════════════════════════════════════════════
# 11. STATE NPDES DELEGATION (S1)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 11. State NPDES delegation ──")
# EPA CWA Section 402: 47 states have delegated NPDES authority.
# 4 states + DC retain federal EPA direct oversight: ID, MA, NH, NM
no_delegation = ['ID', 'MA', 'NH', 'NM', 'DC']
if 'state_abb' in df.columns:
    df['state_npdes_delegated'] = np.where(df['state_abb'].isin(no_delegation), 0, 1)
    log(f"  S1 state_npdes_delegated: {int(df['state_npdes_delegated'].sum())} delegated, "
        f"{int((df['state_npdes_delegated']==0).sum())} federal")


# ═══════════════════════════════════════════════════════════════════════
# 12. STATE CO-ENFORCEMENT INTENSITY (S2)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 12. State co-enforcement intensity ──")
# Use epa_state_response_rate_npdes as the co-enforcement proxy:
# the rate at which the state responds to NPDES violations with enforcement.
if 'epa_state_response_rate_npdes' in df.columns:
    df['state_coenforcement_intensity'] = df['epa_state_response_rate_npdes']
    log(f"  S2 state_coenforcement_intensity: {df['state_coenforcement_intensity'].notna().sum()} non-null")
else:
    log(f"  S2: epa_state_response_rate_npdes not in panel")


# ═══════════════════════════════════════════════════════════════════════
# 13. CITY-LEVEL ACS DEMOGRAPHICS (X4, X5, X6)
# ═══════════════════════════════════════════════════════════════════════
log("\n── 13. ACS demographics (X4–X6) ──")
acs_path = ROOT / 'raw' / 'census_acs' / 'acs_demographics_2022.csv'
if acs_path.exists():
    acs = pd.read_csv(acs_path)
    acs['fips7'] = acs['fips7'].astype(int)
    # These are cross-sectional (2022 ACS 5-year estimates cover 2018-2022)
    # Merge as time-invariant city characteristics
    before = set(df.columns)
    acs_vars = [c for c in acs.columns if c != 'fips7']
    for v in acs_vars:
        if v in df.columns:
            df = df.drop(columns=v)
    df = df.merge(acs[['fips7'] + acs_vars].drop_duplicates('fips7'),
                   on='fips7', how='left')
    new = set(df.columns) - before
    for v in ['pct_college_educated', 'pct_nonwhite', 'median_home_value']:
        if v in df.columns:
            nn = df[v].notna().sum()
            mean = df[v].mean()
            log(f"  {v}: {nn} non-null, mean={mean:.1f}")
    # Construct lag-2 for median_home_value
    if 'median_home_value' in df.columns:
        # Cross-sectional, so lag-2 = same value (time-invariant)
        df['median_home_value_lag2'] = df['median_home_value']
        log(f"  X6 median_home_value_lag2: {df['median_home_value_lag2'].notna().sum()} non-null (cross-sectional)")
else:
    log(f"  ACS file not found at {acs_path} — run Census API pull first")


# ═══════════════════════════════════════════════════════════════════════
# 14. DROP REDUNDANT / ZERO-COVERAGE COLUMNS
# ═══════════════════════════════════════════════════════════════════════
log("\n── 14. Dropping redundant columns ──")
n_before_drop = len(df.columns)

# Keep identifiers always
keep_always = {'fips7','year','city_name','state_abb','state_id','county_fips','county_fips5',
               'CITY_ID','epa_fips7','fips7_srf'}

# Prefixes for columns we need (from variable_list_audit.md + regressions)
needed_prefixes = [
    # DVs
    'Green_Bond_','Y_self_green','Y_esg_','Y_water_only','Y_has_non_water','Y_any_',
    'Y_Clean_','Y_Renewable_','Y_Energy_','Y_Green_Buildings','Y_Climate_','Y_Pollution_',
    'Y_Mgmt_','Y_Proj_','Y_natural_',
    'incidentally_green','asinh_','City_Green_','City_Total_','City_Share_',
    'N_esg_categories','category_composition','count_water','count_non_water',
    # Bloomberg detail
    'Count_','Amt_','Dum_',
    # Mayor
    'Rep_Mayor','Ind_Mayor','Dem_Mayor','mayor_','prob_democrat','prob_republican',
    'party_switch','switch_to_','is_switcher',
    # Demographics & economic
    'population_','percapita_income_','totalincome_','unemployment_',
    'log_population_','log_percapita_','log_totalincome_',
    'lfpr_','management_','manufacturing_','naturalresources_','production_','transport_',
    'pop_density','is_principal_city','pct_college','pct_nonwhite','median_home_value',
    # State demographics
    'state_poverty','state_median_','state_gini','state_pct_','state_homeownership',
    'state_right_to_work','state_has_income','state_medicaid','state_pct_foreign',
    # Fiscal constructed
    'reserve_ratio','debt_service_burden','operating_balance','fiscal_stress',
    'expenditure_rigidity','revenue_hhi','tax_effort_pc','charges_to_own',
    'vfi','tax_autonomy','days_cash','debt_affordability','net_borrowing',
    'operating_deficit','budget_flexibility','rating_agency_composite',
    'low_reserves','dsb_worsening','dsb_change','reserve_months','reserve_change',
    'reserve_declin','short_term_debt','own_source_rev','fiscal_self_suff',
    'expenditure_gap','property_tax_depend','tax_to_rev','tax_to_own',
    'payroll_share','aid_volatility','aid_growth','igr_share','fed_igr','state_igr',
    'local_ig','direct_exp_share','current_oper_share','high_fiscal_stress',
    'fiscal_stress_tercile','fiscal_stress_pca','combined_liability','pension_',
    'tel_x_','tel_stringency','tel_overall','tel_specific','tel_levy',
    'tel_assessment','tel_general_','tel_full_disclosure',
    'capital_stock_pc','capital_outlay','capital_share','investment_gap',
    # Key Census fiscal aggregates
    'total_revenue','total_taxes','total_expenditure','direct_expenditure',
    'general_revenue','property_tax','gen_rev_own_sources',
    'total_long_term_debt','general_debt_interest','total_general_charges',
    'nonin_trust_cash','total_ltd_issued','total_ltd_retired',
    'sewerage_','highways_expend','police_expend','health_hospitals',
    'solid_waste','water_sewer_capital',
    'total_revenue_pc','general_revenue_pc','total_taxes_pc','property_tax_pc',
    'total_expenditure_pc','direct_expenditure_pc','total_ig_revenue',
    'debt_pc','debt_to_revenue','cash_securities','st_debt_end',
    'total_debt_outstanding','liquidity_tier',
    # EPA enforcement
    'npdes_','overflow_','case_','rcra_','air_formal','air_informal',
    'air_inspections','air_violations','air_stack','air_titlev',
    'sdwa_','epa_state_','state_npdes_delegated','state_coenforcement',
    # Anti-ESG / ESG
    'esg_has_','esg_cum_','esg_num_','esg_law_','esg_governor_',
    'esg_msrb_','esg_first_','signed_utah','pro_esg_rfi',
    # State political
    'state_dem_','state_rep_','state_divided','state_legis','state_govt_trifecta',
    'state_gov_party',
    # Presidential
    'pres_dem_','pres_rep_',
    # Climate
    'c40_','mayors_climate','iclei_','climate_commitment',
    'state_rps_','state_carbon_','state_climate_plan',
    'happening','regulate','opinion_',
    # NRI
    'nri_','National Risk',
    # Vulcan
    'production_city','consumption',
    # FOG
    'fog','initiative','referendum','partisan','termlimits','termlength','districts',
    # SRF
    'srf_','cwsrf_','dwsrf_','portal_','usaspending_','allotment','log_cwsrf',
    # Bond regulation
    'go_supermajority','go_voter','go_vote_threshold',
    'has_state_bond_commission','has_state_approval','has_constitutional_debt',
    'has_bond_bank','revenue_bond_voter',
    # State green bond capacity
    'state_green_bond_','state_all_green_','asinh_state_all_green',
    # ESG AUM / bond market
    'us_esg_aum','muni_aaa_yield',
    # Federal green funding
    'federal_green_','ira_','bil_',
    # Municipal utilities
    'has_municipal_electric','electric_utility',
    # State energy policy
    'state_eers_','iecc_vintage','local_benchmark','state_building_code',
    'rps_x_muni_electric','state_rps_stringency','net_metering',
    # FEMA / NFIP
    'fema_disaster','nfip_',
    # EPA Green Book CAA nonattainment (from phistory.xls / nayro.xls merged in 00)
    'caa_',
    # Federal grants
    'iija_','federal_grant',
    # Transit
    'state_transit_','state_has_transit',
    # Substitute water
    'substitute_water','has_substitute_issuer','crowding_',
    # Election / timing
    'election_','years_since_election','timing',
    # Other
    'state_population','deflator','imputation','data_source',
    'chg_sewerage',
]

def is_needed(col):
    if col in keep_always:
        return True
    for prefix in needed_prefixes:
        if col.startswith(prefix) or col == prefix:
            return True
    return False

drop_cols = [c for c in df.columns if not is_needed(c)]
df = df.drop(columns=drop_cols)
log(f"  Dropped {len(drop_cols)} redundant columns ({n_before_drop} → {len(df.columns)})")


# ═══════════════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════════════
n_cols_after = len(df.columns)
log(f"\n{'='*70}")
log(f"DONE: {n_cols_after - n_cols_before} new columns added")
log(f"Panel: {df.shape[0]:,} rows × {df.shape[1]:,} cols")
log(f"{'='*70}")

df.to_pickle(PANEL_PATH)
log(f"Saved: {PANEL_PATH}")
