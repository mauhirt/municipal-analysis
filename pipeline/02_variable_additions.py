"""
02_variable_additions.py — Implement VARIABLE_ADDITIONS_SPEC.md
================================================================================
Adds, reconfigures, and robustness-checks variables across the three-family
empirical strategy defined in:
  - processed/VARIABLE_ADDITIONS_SPEC.md
  - pipeline/three_table_strategy_memo_revised.docx

Inputs:  processed/panel/panel.pkl   (built by 00 + 01)
         + supplementary raw sources that 00 did not merge (e.g. the
           New Building Codes panels)
Output:  processed/panel/panel.pkl   (patched in place)
         processed/panel/panel.csv.gz (also written for the analysis scripts
           that expect processed/merged_city_year_panel.csv.gz)

Run after pipeline/01_construct_audit_variables.py. Patches the panel in
place so the downstream `analysis_table*.py` scripts can consume it.

Naming conventions (from the spec):
  - `epa_npdes_*`    = EPA NPDES family (compulsion)
  - `bcode_*`        = Building-code family (compulsion via BPS/IECC)
  - `ep_*`           = Energy-policy family (municipal electric, ACEEE)
  - `inst_*`         = State institutional family (bond law, referenda, bond bank)
  - `fn_*`           = FOG institutional structure (partisan elections, deficiency)
  - `opinion_*_lag2` = YCOM constituency opinion (lag 2)
  - Lags follow `{var}_lag{k}` (rebuilt panel-aware with groupby('fips7'))
  - `Rep_Mayor_lag1` is the harmonised canonical treatment name (mirrors the
    panel's `Rep_Mayor_L1`); we create it here for downstream consistency.

Where a source column is missing, the block logs a warning and skips — this
mirrors the 01_construct_audit_variables.py pattern so the build still completes
and produces a panel with whatever the raw sources actually supply.
"""

import pandas as pd
import numpy as np
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')
ROOT = Path(__file__).resolve().parent.parent
PANEL_PATH = ROOT / 'processed' / 'panel' / 'panel.pkl'
OUT_CSV = ROOT / 'processed' / 'merged_city_year_panel.csv.gz'

df = pd.read_pickle(PANEL_PATH)
n_cols_before = len(df.columns)
print(f"Panel in: {df.shape}")


def log(msg):
    print(msg)


def group_shift(series_name, k):
    """Panel-aware shift that respects FIPS and year ordering."""
    return df.groupby('fips7')[series_name].shift(k)


def ensure_sorted():
    global df
    df = df.sort_values(['fips7', 'year']).reset_index(drop=True)


ensure_sorted()


def add_lag(src, lag_name, k, transform=None):
    """Build a panel-aware lag (optionally after a transform) iff source exists."""
    if src not in df.columns:
        log(f"  [skip] {lag_name}: source `{src}` not in panel")
        return False
    series = df[src]
    if transform == 'asinh':
        series = np.arcsinh(series.fillna(0))
    elif transform == 'log1p':
        series = np.log1p(series.fillna(0))
    df[f'_{src}__tmp'] = series
    df[lag_name] = df.groupby('fips7')[f'_{src}__tmp'].shift(k)
    df.drop(columns=f'_{src}__tmp', inplace=True)
    return True


def alias(source, target):
    """Copy column `source` to `target` if source exists and target missing."""
    if target in df.columns:
        return
    if source in df.columns:
        df[target] = df[source]


# Harmonise the treatment-variable name to the spec's convention.
alias('Rep_Mayor_L1', 'Rep_Mayor_lag1')
alias('Ind_Mayor_L1', 'Ind_Mayor_lag1')

# Harmonise `pres_dem_two_party_share_lag2` (spec) from base column.
if 'pres_dem_two_party_share' in df.columns and 'pres_dem_two_party_share_lag2' not in df.columns:
    df['pres_dem_two_party_share_lag2'] = group_shift('pres_dem_two_party_share', 2)
    log("  aliased pres_dem_two_party_share_lag2")


# ═══════════════════════════════════════════════════════════════════════
# SECTION 1 — FAMILY 1: MATERIAL VARIABLES
# ═══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("SECTION 1 — Family 1: Material")
log("=" * 70)

# ----- 1.1 Informal enforcement (robustness col, T1 and T2-water) -----
log("\n── 1.1 Informal NPDES enforcement ──")
src = 'npdes_informal_actions_count_muni'
if src in df.columns:
    df['epa_npdes_informal_asinh'] = np.arcsinh(df[src].fillna(0))
    df['epa_npdes_informal_asinh_lag2'] = group_shift('epa_npdes_informal_asinh', 2)
    # Canonical spec alias keeps the long variable name working upstream.
    df['epa_npdes_informal_actions_count_muni_lag2'] = group_shift(src, 2)
    log(f"  epa_npdes_informal_asinh_lag2: n={(df['epa_npdes_informal_asinh_lag2']>0).sum()} positive")
else:
    log(f"  [skip] source `{src}` not in panel")

# ----- 1.2 Decomposed NPDES violation types (T2-water robustness) -----
log("\n── 1.2 Decomposed NPDES violation types ──")
for vtype in ['effluent', 'cs', 'ps', 'se']:
    src = f'npdes_{vtype}_violations_count_muni'
    if src not in df.columns:
        log(f"  [skip] {src} not in panel")
        continue
    df[f'epa_npdes_{vtype}_asinh'] = np.arcsinh(df[src].fillna(0))
    df[f'epa_npdes_{vtype}_asinh_lag2'] = group_shift(f'epa_npdes_{vtype}_asinh', 2)
    log(f"  epa_npdes_{vtype}_asinh_lag2: n={(df[f'epa_npdes_{vtype}_asinh_lag2']>0).sum()} positive")

# Composite water violations (sum of the four types) for T2-water primary column.
components = [f'npdes_{v}_violations_count_muni' for v in ['effluent', 'cs', 'ps', 'se']]
components = [c for c in components if c in df.columns]
if components:
    df['epa_water_violations_count_muni'] = df[components].sum(axis=1)
    df['epa_water_violations_asinh'] = np.arcsinh(df['epa_water_violations_count_muni'].fillna(0))
    df['epa_water_violations_asinh_lag2'] = group_shift('epa_water_violations_asinh', 2)
    log(f"  epa_water_violations_asinh_lag2 built from {len(components)} types")

# ----- 1.3 Municipal electric utility enterprise fund depth (T2-renewables) -----
log("\n── 1.3 Municipal electric utility depth ──")
# The raw source (energy_policy/municipal_electric_utilities.csv) is cross-sectional
# with revenue_millions + has_municipal_electric already merged by 01.
alias('has_municipal_electric', 'ep_has_muni_electric')
if 'revenue_millions' in df.columns:
    alias('revenue_millions', 'ep_muni_electric_rev_mil')
if 'ep_muni_electric_rev_mil' not in df.columns:
    # Attempt to re-merge from raw if the column didn't propagate through 01.
    mu_path = ROOT / 'raw' / 'energy_policy' / 'municipal_electric_utilities.csv'
    if mu_path.exists():
        mu = pd.read_csv(mu_path)
        if 'revenue_millions' in mu.columns and 'city_name' in mu.columns:
            city_lookup = df[['fips7', 'city_name', 'state_abb']].drop_duplicates('fips7')
            mu_merged = city_lookup.merge(
                mu[['city_name', 'state_abb', 'revenue_millions']],
                on=['city_name', 'state_abb'], how='left',
            )
            df = df.merge(
                mu_merged[['fips7', 'revenue_millions']].rename(
                    columns={'revenue_millions': 'ep_muni_electric_rev_mil'}),
                on='fips7', how='left',
            )

if 'ep_muni_electric_rev_mil' in df.columns:
    df['ep_muni_electric_rev_asinh'] = np.arcsinh(df['ep_muni_electric_rev_mil'].fillna(0))
    df['ep_muni_electric_rev_asinh_lag1'] = group_shift('ep_muni_electric_rev_asinh', 1)
    log(f"  ep_muni_electric_rev_asinh_lag1: n={(df['ep_muni_electric_rev_asinh_lag1']>0).sum()} positive")
else:
    log("  [skip] ep_muni_electric_rev_mil could not be constructed")

if 'ep_has_muni_electric' in df.columns:
    df['ep_has_muni_electric_lag1'] = group_shift('ep_has_muni_electric', 1)
    log(f"  ep_has_muni_electric_lag1: n={int(df['ep_has_muni_electric_lag1'].fillna(0).sum())} positive")

# ----- 1.4 Building Performance Standards (T2-green buildings + T2-energy eff) -----
log("\n── 1.4 Building Performance Standards ──")
# Source: raw/energy_policy/New Building Codes/{master_city_year_panel_2010_2025,master_state_year_panel_2010_2025}.csv
bc_dir = ROOT / 'raw' / 'energy_policy' / 'New Building Codes'
state_bc_path = bc_dir / 'master_state_year_panel_2010_2025.csv'
city_bc_path = bc_dir / 'master_city_year_panel_2010_2025.csv'

# Merge the state-level BPS panel (time-varying, by state_abb + year).
if state_bc_path.exists() and 'state_abb' in df.columns:
    sbc = pd.read_csv(state_bc_path)
    sbc = sbc.rename(columns={'state_abbr': 'state_abb'})
    keep = {
        'state_bps_adopted': 'bcode_state_bps_adopted',
        'state_bps_effective': 'bcode_state_bps_effective',
        'lag_model_code_yrs': 'bcode_iecc_lag_yrs',
        'weakening_amendments': 'bcode_state_weakening_amendments',
        'iecc_comm_vintage': 'bcode_iecc_comm_vintage',
        'no_statewide_code': 'bcode_no_statewide_code',
        'stretch_code_available': 'bcode_stretch_code_available',
        'preemption_of_stricter_local': 'bcode_preemption_local',
        'home_rule': 'bcode_home_rule',
    }
    keep = {k: v for k, v in keep.items() if k in sbc.columns}
    sbc_small = sbc[['state_abb', 'year'] + list(keep.keys())].rename(columns=keep).drop_duplicates(['state_abb', 'year'])
    before = len(df.columns)
    df = df.merge(sbc_small, on=['state_abb', 'year'], how='left', suffixes=('', '_BC'))
    for c in list(df.columns):
        if c.endswith('_BC'):
            # Prefer existing column; drop the newly-merged duplicate.
            df = df.drop(columns=c)
    log(f"  merged state building-code panel ({len(df.columns) - before} new cols)")
else:
    log(f"  [skip] state building-codes panel not found")

# Merge the city-level BPS panel (where applicable).
if city_bc_path.exists():
    cbc = pd.read_csv(city_bc_path)
    cbc = cbc.rename(columns={'state_abbr': 'state_abb', 'jurisdiction': 'city_name_bc'})
    # Match on city_name + state_abb + year; the panel uses lower-case city_name.
    cbc['city_name_lc'] = cbc['city_name_bc'].str.lower()
    df_match = df[['fips7', 'city_name', 'state_abb', 'year']].copy()
    df_match['city_name_lc'] = df_match['city_name'].astype(str).str.lower()
    keep_city = {
        'bps_adopted': 'bcode_bps_adopted',
        'bps_effective': 'bcode_bps_effective',
        'years_since_bps': 'bcode_years_since_bps',
        'benchmarking_adopted': 'bcode_benchmarking_adopted',
        'any_policy_active': 'bcode_any_policy_active',
    }
    keep_city = {k: v for k, v in keep_city.items() if k in cbc.columns}
    cbc_small = cbc[['city_name_lc', 'state_abb', 'year'] + list(keep_city.keys())].rename(columns=keep_city)
    cbc_small = cbc_small.drop_duplicates(['city_name_lc', 'state_abb', 'year'])
    merged = df_match.merge(cbc_small, on=['city_name_lc', 'state_abb', 'year'], how='left')
    # Bring the new columns back by fips7 + year.
    new_city_cols = list(keep_city.values())
    for c in new_city_cols:
        if c in merged.columns:
            df = df.merge(
                merged[['fips7', 'year', c]].drop_duplicates(['fips7', 'year']),
                on=['fips7', 'year'], how='left', suffixes=('', '_DROP'),
            )
            if c + '_DROP' in df.columns:
                df = df.drop(columns=c + '_DROP')
    # Fill NaN with 0 where the match simply means "no city-level BPS policy".
    for c in new_city_cols:
        if c in df.columns:
            df[c] = df[c].fillna(0)
    log(f"  merged city building-code panel ({len(new_city_cols)} city BPS cols)")
else:
    log("  [skip] city building-codes panel not found")

# Lags (lag 1) on the new BPS/IECC variables.
for var in ['bcode_state_bps_adopted', 'bcode_bps_adopted',
            'bcode_iecc_lag_yrs', 'bcode_state_weakening_amendments',
            'bcode_bps_effective', 'bcode_state_bps_effective',
            'bcode_benchmarking_adopted', 'bcode_any_policy_active']:
    add_lag(var, f'{var}_lag1', 1)

# ----- 1.5 Federal grants — IIJA and IRA (T1, T2, T3) -----
log("\n── 1.5 Federal grants (IIJA / IRA / FEMA resilience) ──")
grant_vars = [
    'iija_water_grant_amt',
    'ira_eecbg_grant_amt',
    'ira_ggrf_grant_amt',
    'iija_transit_grant_amt',
    'fema_resil_grant_amt',
]
# Re-pull any grant amounts that were pruned upstream (01 keeps the asinh/lag
# derivatives but may drop the raw amount columns).
missing_raw = [v for v in grant_vars if v not in df.columns]
if missing_raw:
    fg_path = ROOT / 'raw' / 'grants' / 'federal_grants_panel.csv'
    if fg_path.exists():
        fg = pd.read_csv(fg_path)
        if 'fips7' not in fg.columns:
            fips_col = [c for c in fg.columns if 'fips' in c.lower()][0]
            fg = fg.rename(columns={fips_col: 'fips7'})
        fg['fips7'] = fg['fips7'].astype(int)
        pull = ['fips7', 'year'] + [c for c in missing_raw if c in fg.columns]
        if len(pull) > 2:
            df = df.merge(
                fg[pull].drop_duplicates(['fips7', 'year']),
                on=['fips7', 'year'], how='left',
            )
            log(f"  re-merged {len(pull)-2} raw grant amount column(s): {pull[2:]}")
for v in grant_vars:
    if v not in df.columns:
        log(f"  [skip] {v} not in panel")
        continue
    df[f'{v}_asinh'] = np.arcsinh(df[v].fillna(0))
    df[f'{v}_asinh_lag1'] = group_shift(f'{v}_asinh', 1)
    log(f"  {v}_asinh_lag1: n={(df[f'{v}_asinh_lag1']>0).sum()} positive")

# ----- 1.6 Climate-adaptation physical risk (T2-climate adapt) -----
log("\n── 1.6 Climate-adaptation physical risk ──")
# NFIP aggregate losses at county-FIPS level.
nfip_src = ROOT / 'raw' / 'disasters' / 'nfip_flood_claims.csv'
if 'nfip_total_losses' not in df.columns and nfip_src.exists() and 'county_fips5' in df.columns:
    nfip = pd.read_csv(nfip_src)
    fc = [c for c in nfip.columns if 'fips' in c.lower()][0]
    nfip[fc] = nfip[fc].astype(str).str.replace('.0', '', regex=False)
    df['_cfips5_str'] = df['county_fips5'].astype(str).str.replace('.0', '', regex=False)
    nfip_keep = nfip[[fc, 'nfip_total_losses']].drop_duplicates(fc)
    nfip_keep = nfip_keep.rename(columns={fc: '_cfips5_str'})
    df = df.merge(nfip_keep, on='_cfips5_str', how='left')
    df = df.drop(columns='_cfips5_str')

if 'nfip_total_losses' in df.columns:
    df['nfip_total_losses_asinh'] = np.arcsinh(df['nfip_total_losses'].fillna(0))
    df['nfip_total_losses_asinh_lag2'] = group_shift('nfip_total_losses_asinh', 2)
    log("  nfip_total_losses_asinh_lag2 built")
else:
    log("  [skip] nfip_total_losses unavailable")

# FEMA disaster flood flag: re-pull from raw if the panel only kept counts/any.
if 'fema_disaster_flood' not in df.columns:
    fema_src = ROOT / 'raw' / 'disasters' / 'fema_disaster_declarations.csv'
    if fema_src.exists() and 'county_fips5' in df.columns:
        fm = pd.read_csv(fema_src)
        fc = [c for c in fm.columns if 'fips' in c.lower()][0]
        fm[fc] = fm[fc].astype(str).str.replace('.0', '', regex=False)
        if 'fema_disaster_flood' in fm.columns and 'year' in fm.columns:
            fm_agg = fm.groupby([fc, 'year'], as_index=False)['fema_disaster_flood'].max()
            fm_agg = fm_agg.rename(columns={fc: '_cfips5_str'})
            df['_cfips5_str'] = df['county_fips5'].astype(str).str.replace('.0', '', regex=False)
            df = df.merge(fm_agg, on=['_cfips5_str', 'year'], how='left')
            df['fema_disaster_flood'] = df['fema_disaster_flood'].fillna(0)
            df = df.drop(columns='_cfips5_str')

if 'fema_disaster_flood' in df.columns:
    df['fema_disaster_flood_lag2'] = group_shift('fema_disaster_flood', 2)
    log(f"  fema_disaster_flood_lag2 built (positive city-years: "
        f"{int(df['fema_disaster_flood_lag2'].fillna(0).sum())})")
else:
    log("  [skip] fema_disaster_flood not in panel")

# NRI inland flooding expected annual loss on buildings (time-invariant control).
nri_eal_col = 'Inland Flooding - Expected Annual Loss - Building Value'
if nri_eal_col not in df.columns:
    nri_src = ROOT / 'raw' / 'nri' / 'epa_nri.csv'
    if nri_src.exists():
        nri = pd.read_csv(nri_src)
        if nri_eal_col in nri.columns and 'fips7' in nri.columns:
            nri_small = nri[['fips7', nri_eal_col]].drop_duplicates('fips7')
            nri_small = nri_small.rename(columns={nri_eal_col: 'nri_inland_flooding_eal_bv'})
            df = df.merge(nri_small, on='fips7', how='left')

if 'nri_inland_flooding_eal_bv' in df.columns:
    df['nri_inland_flooding_expected_annual_loss_building_value'] = df['nri_inland_flooding_eal_bv']
    log(f"  nri_inland_flooding_eal_bv built (n_nonnull="
        f"{df['nri_inland_flooding_eal_bv'].notna().sum()})")
elif nri_eal_col in df.columns:
    df['nri_inland_flooding_eal_bv'] = df[nri_eal_col]
    df['nri_inland_flooding_expected_annual_loss_building_value'] = df[nri_eal_col]
    log("  nri_inland_flooding_eal_bv aliased from raw column")
else:
    log(f"  [skip] `{nri_eal_col}` not available")

# ----- 1.7 Reconfigure: bridge-deficiency variable -----
log("\n── 1.7 Reconfigure bridge deficiency (move to T2-clean transportation) ──")
# Nothing to construct: fn_pct_deficient_lag2 already exists; moving between tables
# is a downstream regression-spec change, flagged here for consumers.
if 'pct_deficient_lag2' in df.columns:
    df['fn_pct_deficient_lag2'] = df['pct_deficient_lag2']
    log("  fn_pct_deficient_lag2 aliased from pct_deficient_lag2 (T2-clean-transport only)")
else:
    log("  [skip] pct_deficient_lag2 missing")

# ----- 1.8 Fiscal stress robustness -----
log("\n── 1.8 Fiscal-stress robustness ──")
# fiscal_stress_index_lag2 is already built in 00_build_panel.py; alias for consistency.
if 'fiscal_stress_index_lag2' in df.columns:
    log(f"  fiscal_stress_index_lag2 present (n={df['fiscal_stress_index_lag2'].notna().sum()})")
else:
    log("  [skip] fiscal_stress_index_lag2 missing")


# ═══════════════════════════════════════════════════════════════════════
# SECTION 2 — FAMILY 2: POLITICAL VARIABLES
# ═══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("SECTION 2 — Family 2: Political")
log("=" * 70)

# ----- 2.1 YCOM climate opinion controls (T1, T2, T3) -----
log("\n── 2.1 YCOM climate opinion controls (lag 2) ──")
ycom_vars = [
    'opinion_regulate',
    'opinion_fundrenewables',
    'opinion_happening',
    'opinion_worried',
]
for v in ycom_vars:
    if v not in df.columns:
        log(f"  [skip] {v} not in panel")
        continue
    df[f'{v}_lag2'] = group_shift(v, 2)
    log(f"  {v}_lag2: n={df[f'{v}_lag2'].notna().sum()} non-null")

# ----- 2.2 Probabilistic partisanship (T1 robustness) -----
log("\n── 2.2 Probabilistic partisanship ──")
# The raw columns are `prob_republican` and `prob_democrat`; alias them to the
# spec convention `mayor_prob_rep`/`mayor_prob_dem` and build lag-1.
alias('prob_republican', 'mayor_prob_rep')
alias('prob_democrat', 'mayor_prob_dem')
for src, lag in [('mayor_prob_rep', 'mayor_prob_rep_lag1'),
                 ('mayor_prob_dem', 'mayor_prob_dem_lag1')]:
    if src in df.columns:
        df[lag] = group_shift(src, 1)
        log(f"  {lag}: n={df[lag].notna().sum()} non-null")
    else:
        log(f"  [skip] {src} not in panel")

# ----- 2.3 ESG law intensity score (T1 + T3) -----
log("\n── 2.3 ESG law intensity ──")
# `esg_law_intensity_score` exists in the raw anti-ESG file.
if 'esg_law_intensity_score' in df.columns:
    df['esg_law_intensity_lag1'] = group_shift('esg_law_intensity_score', 1)
    log(f"  esg_law_intensity_lag1 built (max={df['esg_law_intensity_lag1'].max()})")
else:
    log("  [skip] esg_law_intensity_score not in panel")

# Binary `esg_any_antiesg_law` alias from the raw `esg_has_antiesg_law`.
alias('esg_has_antiesg_law', 'esg_any_antiesg_law')
if 'esg_any_antiesg_law' in df.columns and 'esg_any_antiesg_law_lag1' not in df.columns:
    df['esg_any_antiesg_law_lag1'] = group_shift('esg_any_antiesg_law', 1)

# Rep_Mayor × esg_law_intensity interaction (T1 Col 5, T3).
if 'Rep_Mayor_lag1' in df.columns and 'esg_law_intensity_lag1' in df.columns:
    df['rep_x_esg_intensity'] = df['Rep_Mayor_lag1'] * df['esg_law_intensity_lag1']
    log("  rep_x_esg_intensity interaction built")

# ----- 2.4 Climate-network membership (T1 interaction col, T3) -----
log("\n── 2.4 Climate-network membership ──")
# Network vars in the panel: c40_member, iclei_member, mayors_climate_signatory,
# climate_commitment_score. Build lag-1 copies under spec names.
net_map = {
    'c40_member': 'c40_member_lag1',
    'iclei_member': 'iclei_member_lag1',
    'mayors_climate_signatory': 'mcpa_signatory_lag1',
    'climate_commitment_score': 'climate_commitment_lag1',
}
for src, tgt in net_map.items():
    if src in df.columns:
        df[tgt] = group_shift(src, 1)
    else:
        log(f"  [skip] {src} not in panel")

# Static "climate commitment" combined indicator: any network membership.
membership_cols = [c for c in ['c40_member', 'iclei_member', 'mayors_climate_signatory']
                   if c in df.columns]
if membership_cols:
    df['climate_commitment_static'] = (df[membership_cols].sum(axis=1) > 0).astype(int)
    log(f"  climate_commitment_static: {int(df['climate_commitment_static'].sum())} positive city-years")

# C40 × Rep_Mayor interaction for T1 Col 5.
if 'c40_member_lag1' in df.columns and 'Rep_Mayor_lag1' in df.columns:
    df['c40_x_rep_mayor'] = df['c40_member_lag1'] * df['Rep_Mayor_lag1']

# ----- 2.5 Partisan election structure (T1 robustness) -----
log("\n── 2.5 Partisan election structure (FOG) ──")
# FOG has `partisan` = officially partisan mayoral elections.
if 'partisan' in df.columns:
    df['fn_partisan'] = df['partisan']
    df['fn_partisan_lag1'] = group_shift('fn_partisan', 1)
    log(f"  fn_partisan_lag1: {int(df['fn_partisan_lag1'].fillna(0).sum())} positive city-years")
else:
    log("  [skip] FOG `partisan` not in panel")

# Rep_Mayor × partisan-election interaction for the coding-reliability test.
if 'fn_partisan_lag1' in df.columns and 'Rep_Mayor_lag1' in df.columns:
    df['rep_x_fn_partisan'] = df['Rep_Mayor_lag1'] * df['fn_partisan_lag1']

# ----- 2.6 Education as constituency control (T1, T2) -----
log("\n── 2.6 State education (bachelor's plus) ──")
if 'state_pct_bachelors_plus' in df.columns:
    df['state_pct_bachelors_lag1'] = group_shift('state_pct_bachelors_plus', 1)
    log(f"  state_pct_bachelors_lag1: n={df['state_pct_bachelors_lag1'].notna().sum()} non-null")
else:
    log("  [skip] state_pct_bachelors_plus not in panel")


# ═══════════════════════════════════════════════════════════════════════
# SECTION 3 — FAMILY 3: STATE / MULTILEVEL GOVERNANCE
# ═══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("SECTION 3 — Family 3: State / Multilevel governance")
log("=" * 70)

# ----- 3.1 Reclassify `esg_any_antiesg_law` from F2 to F3 -----
log("\n── 3.1 Reclassify esg_any_antiesg_law to Family 3 ──")
# No construction needed — this is a column-ordering change for the downstream
# regression tables. Document the reclassification as a column attribute.
if 'esg_any_antiesg_law' in df.columns:
    log("  esg_any_antiesg_law is now Family 3 (column-ordering only; consumed by analysis scripts)")

# ----- 3.2 Democratic governor and trifecta (T1 F3, T3) -----
log("\n── 3.2 Dem governor and trifecta ──")
for src in ['state_dem_governor', 'state_dem_trifecta', 'state_rep_trifecta']:
    if src in df.columns:
        df[f'{src}_lag1'] = group_shift(src, 1)
        log(f"  {src}_lag1: n={df[f'{src}_lag1'].notna().sum()} non-null")
    else:
        log(f"  [skip] {src} not in panel")

# ----- 3.3 Carbon pricing (T1, T2-renewables, T2-energy-eff, T3) -----
log("\n── 3.3 Carbon pricing ──")
# Binary and continuous carbon pricing already in the panel from climate_policy_controls.
for src, tgt in [('state_carbon_pricing', 'state_carbon_pricing_lag1'),
                 ('state_carbon_price', 'state_carbon_price_usd_lag1')]:
    if src in df.columns:
        df[tgt] = group_shift(src, 1)
        if src == 'state_carbon_price':
            # Alias to spec's `_usd` naming.
            df['state_carbon_price_usd'] = df[src]
        log(f"  {tgt} built")
    else:
        log(f"  [skip] {src} not in panel")

# Scheme-specific membership (RGGI / WCI) — derived from the well-known state
# rosters since the raw files don't supply a column directly.
rggi_states = {
    'CT', 'DE', 'ME', 'MD', 'MA', 'NH', 'NJ', 'NY', 'RI', 'VT', 'VA', 'PA',
}
wci_states = {'CA', 'WA'}


def rggi_effective(state, year):
    if state not in rggi_states:
        return 0
    if state == 'NJ':
        # NJ withdrew 2012, rejoined 2020.
        return 1 if (year <= 2011 or year >= 2020) else 0
    if state == 'VA':
        return 1 if 2021 <= year <= 2023 else 0  # VA RGGI: 2021-2023
    if state == 'PA':
        return 1 if year >= 2022 else 0
    return 1


def wci_effective(state, year):
    if state not in wci_states:
        return 0
    if state == 'CA':
        return 1 if year >= 2013 else 0
    if state == 'WA':
        return 1 if year >= 2023 else 0  # WA cap-and-invest launched 2023
    return 0


if {'state_abb', 'year'}.issubset(df.columns):
    df['state_rggi_member'] = df.apply(lambda r: rggi_effective(r['state_abb'], r['year']), axis=1)
    df['state_wci_member'] = df.apply(lambda r: wci_effective(r['state_abb'], r['year']), axis=1)
    df['state_rggi_member_lag1'] = group_shift('state_rggi_member', 1)
    df['state_wci_member_lag1'] = group_shift('state_wci_member', 1)
    log(f"  state_rggi_member city-years positive: {int(df['state_rggi_member'].sum())}")
    log(f"  state_wci_member city-years positive:  {int(df['state_wci_member'].sum())}")

# RPS active + target, and ACEEE building-code rank (lagged).
for src in ['state_rps_active', 'state_rps_target_pct']:
    if src in df.columns:
        df[f'{src}_lag1'] = group_shift(src, 1)

# ACEEE code rank — raw is `state_building_code_stringency_aceee_rank` (cross-section).
aceee_path = ROOT / 'raw' / 'energy_policy' / 'state_building_codes.csv'
if 'ep_state_aceee_code_rank' not in df.columns:
    if 'state_building_code_stringency_aceee_rank' in df.columns:
        df['ep_state_aceee_code_rank'] = df['state_building_code_stringency_aceee_rank']
    elif aceee_path.exists() and 'state_abb' in df.columns:
        ac = pd.read_csv(aceee_path)
        if 'state_abbr' in ac.columns and 'state_building_code_stringency_aceee_rank' in ac.columns:
            ac = ac[['state_abbr', 'state_building_code_stringency_aceee_rank']].rename(
                columns={'state_abbr': 'state_abb',
                         'state_building_code_stringency_aceee_rank': 'ep_state_aceee_code_rank'})
            ac = ac.drop_duplicates('state_abb')
            df = df.merge(ac, on='state_abb', how='left')

if 'ep_state_aceee_code_rank' in df.columns:
    # Cross-sectional → lag-1 is identical but included for spec symmetry.
    df['ep_state_aceee_code_rank_lag1'] = df['ep_state_aceee_code_rank']
    log("  ep_state_aceee_code_rank(_lag1) built")
else:
    log("  [skip] ACEEE code rank not available")

# ----- 3.4 Underwriter-block law (T1 F3, T3) -----
log("\n── 3.4 Underwriter-block law ──")
if 'esg_has_underwriter_block' in df.columns:
    df['esg_underwriter_block_lag1'] = group_shift('esg_has_underwriter_block', 1)
    log(f"  esg_underwriter_block_lag1 city-years positive: "
        f"{int(df['esg_underwriter_block_lag1'].fillna(0).sum())}")
else:
    log("  [skip] esg_has_underwriter_block not in panel")

# ----- 3.5 Voter-approval requirements (T1 F3) -----
log("\n── 3.5 Voter-approval requirements ──")
# Cross-sectional state-statute columns from bond-referenda panel.
for src, tgt in [
    ('go_voter_approval_required', 'inst_go_voter_approval_required'),
    ('go_supermajority', 'inst_go_supermajority'),
    ('revenue_bond_voter_approval', 'inst_revenue_bond_voter_approval'),
]:
    if src in df.columns:
        df[tgt] = df[src]
        df[f'{tgt}_lag1'] = group_shift(tgt, 1)
        log(f"  {tgt}(_lag1) built")
    else:
        log(f"  [skip] {src} not in panel")

# ----- 3.6 Anti-ESG institutional positions (T3) -----
log("\n── 3.6 Anti-ESG institutional positions ──")
# `signed_utah_antiesg_letter` is in the MSRB RFI merge; msrb_rfi_position has a
# three-way categorical (pro_esg / anti_esg / neutral).
if 'signed_utah_antiesg_letter' in df.columns:
    df['inst_signed_utah_antiesg_letter'] = df['signed_utah_antiesg_letter']
    df['inst_utah_antiesg_lag1'] = group_shift('inst_signed_utah_antiesg_letter', 1)
else:
    log("  [skip] signed_utah_antiesg_letter not in panel")

# Build the MSRB anti-ESG indicator from the raw position string if available.
if 'inst_msrb_antiesg_lag1' not in df.columns:
    rfi_path = ROOT / 'raw' / 'political' / 'state_msrb_rfi_position.csv'
    if rfi_path.exists() and 'state_abb' in df.columns:
        rfi = pd.read_csv(rfi_path)
        rfi['inst_msrb_position_anti_esg'] = (rfi['msrb_rfi_position'] == 'anti_esg').astype(int)
        rfi_small = rfi[['state_abb', 'inst_msrb_position_anti_esg']].drop_duplicates('state_abb')
        df = df.merge(rfi_small, on='state_abb', how='left')
        df['inst_msrb_antiesg_lag1'] = group_shift('inst_msrb_position_anti_esg', 1)
        log(f"  inst_msrb_antiesg_lag1 positive: "
            f"{int(df['inst_msrb_antiesg_lag1'].fillna(0).sum())}")

# ----- 3.7 Bond-bank active vs presence (T1 F3) -----
log("\n── 3.7 Bond-bank activity vs presence ──")
if 'has_bond_bank' in df.columns:
    df['inst_has_bond_bank'] = df['has_bond_bank']
# Merge the active-in-panel-period indicator from the raw state_bond_banks file.
bb_path = ROOT / 'raw' / 'institutional' / 'state_bond_banks.csv'
if 'bond_bank_active_2013_2025' not in df.columns and bb_path.exists() and 'state_abb' in df.columns:
    bb = pd.read_csv(bb_path)
    if 'bond_bank_active_2013_2025' in bb.columns:
        bb_small = bb[['state_abb', 'bond_bank_active_2013_2025']].drop_duplicates('state_abb')
        df = df.merge(bb_small, on='state_abb', how='left')

if 'bond_bank_active_2013_2025' in df.columns:
    df['inst_bond_bank_active_2013_2025'] = df['bond_bank_active_2013_2025']
    df['inst_bond_bank_active_lag1'] = group_shift('inst_bond_bank_active_2013_2025', 1)
    log(f"  inst_bond_bank_active_lag1 positive: "
        f"{int(df['inst_bond_bank_active_lag1'].fillna(0).sum())}")
else:
    log("  [skip] bond_bank_active_2013_2025 unavailable")

# ----- 3.8 TEL × state-trifecta interaction (T1 Col 5) -----
log("\n── 3.8 TEL × state trifecta ──")
if 'tel_stringency_normalized' in df.columns and 'state_rep_trifecta' in df.columns:
    df['tel_x_rep_trifecta'] = df['tel_stringency_normalized'] * df['state_rep_trifecta']
    log("  tel_x_rep_trifecta interaction built")
else:
    log("  [skip] tel_stringency_normalized or state_rep_trifecta missing")

# ----- 3.9 Orthogonal state-ideology instruments (T1 F3 robustness) -----
log("\n── 3.9 Orthogonal state-ideology instruments ──")
for src in ['state_medicaid_expanded', 'state_right_to_work']:
    if src in df.columns:
        df[f'{src}_lag1'] = group_shift(src, 1)
        log(f"  {src}_lag1 built")
    else:
        log(f"  [skip] {src} not in panel")


# ═══════════════════════════════════════════════════════════════════════
# SECTION 4 — CONTROLS AND OUTCOMES
# ═══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("SECTION 4 — Controls and Outcomes")
log("=" * 70)

# ----- 4.1 Intensive-margin outcome (T1 new Col 6) -----
log("\n── 4.1 Intensive-margin outcome (asinh_green_amt) ──")
# `asinh_green_amt` already built in 00_build_panel.py; re-confirm for consumers.
if 'asinh_green_amt' in df.columns:
    log(f"  asinh_green_amt present (n_positive={(df['asinh_green_amt']>0).sum()})")
else:
    if 'City_Green_Amt_Issued' in df.columns:
        df['asinh_green_amt'] = np.arcsinh(df['City_Green_Amt_Issued'].fillna(0))
        log("  asinh_green_amt rebuilt from City_Green_Amt_Issued")

# ----- 4.2 Missing Table 2 outcomes — three new columns -----
log("\n── 4.2 Table-2 new outcomes (climate-adapt / pollution / natural resource) ──")
# `Y_climate_adapt` harmonised from the existing `Y_Climate_Change_Adaptation`.
alias('Y_Climate_Change_Adaptation', 'Y_climate_adapt')
alias('Y_Pollution_Control', 'Y_pollution_control')
# Natural-resource category: derived from raw count columns (Sustainable_Land_Use
# and/or Natural_Resource* in the Bloomberg category block).
nat_res_cols = [
    c for c in df.columns
    if c.startswith('Count_ESG Project Categories__')
    and ('Natural_Resource' in c or 'Land_Use' in c or 'Biodiversity' in c)
]
if nat_res_cols:
    df['Y_natural_resource'] = (df[nat_res_cols].sum(axis=1) > 0).astype(int)
    log(f"  Y_natural_resource: {int(df['Y_natural_resource'].sum())} positive city-years "
        f"(from {len(nat_res_cols)} count cols)")
else:
    log("  [skip] no natural-resource Bloomberg category columns found")

# ----- 4.3 Urbanisation controls (T1 + T2) -----
log("\n── 4.3 Urbanisation controls ──")
for src in ['pop_density_sqkm', 'is_principal_city']:
    if src in df.columns:
        df[f'{src}_lag2'] = group_shift(src, 2)
        log(f"  {src}_lag2: n={df[f'{src}_lag2'].notna().sum()} non-null")
    else:
        log(f"  [skip] {src} not in panel")

# Spec-canonical short names.
alias('pop_density_sqkm_lag2', 'pop_density_lag2')

# ----- 4.4 Intergovernmental revenue dependence (T1 controls) -----
log("\n── 4.4 Intergovernmental revenue dependence ──")
for src in ['fed_igr_share', 'state_igr_share']:
    if src in df.columns:
        df[f'{src}_lag2'] = group_shift(src, 2)
        log(f"  {src}_lag2: n={df[f'{src}_lag2'].notna().sum()} non-null")
    else:
        log(f"  [skip] {src} not in panel")

# ----- 4.5 Reconfigure peer-effects spillover (T1 and T2-water) -----
log("\n── 4.5 Peer-effect spillover (city-only 25km) ──")
# The spec wants `Nearby_Water_CITY_Amt_25km_Cumul`. The project does not yet
# supply that column — substitute_water_panel.csv gives the 25km neighbour count
# only. We construct a city-issuer-only cumulative water amount within 25km as
# best we can from the green-bond skeleton using the raw-crosswalk haversine
# already materialised in the substitute-water panel; otherwise, log and skip so
# the build still completes.
if 'Nearby_Water_CITY_Amt_25km_Cumul' in df.columns:
    df['nearby_city_water_25km_asinh'] = np.arcsinh(
        df['Nearby_Water_CITY_Amt_25km_Cumul'].fillna(0))
    df['nearby_city_water_25km_asinh_lag1'] = group_shift('nearby_city_water_25km_asinh', 1)
    log("  nearby_city_water_25km_asinh_lag1 built")
else:
    log("  [skip] Nearby_Water_CITY_Amt_25km_Cumul unavailable — spec variable missing")
    log("         (kept log_nearby_water_25km / substitute_water_* as spillover fallbacks;")
    log("          flagged for a follow-up geospatial build)")


# ═══════════════════════════════════════════════════════════════════════
# SECTION 5 — STRUCTURAL / IDENTIFICATION ISSUES
# ═══════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("SECTION 5 — Structural / Identification issues")
log("=" * 70)

# ----- 5.1 `fn_esg_has_muni_bond_law` endogeneity (T1) -----
log("\n── 5.1 esg_has_muni_bond_law pre/post indicator ──")
if {'esg_has_muni_bond_law', 'esg_first_law_year', 'year'}.issubset(df.columns):
    # Pre/post indicator: 1 if the year is >= first law year, else 0. Removes the
    # contemporaneous reverse-causality channel — the spec wants the cross-panel
    # cumulative exposure, not the contemporaneous flag.
    df['fn_esg_has_muni_bond_law_post'] = (
        (df['esg_first_law_year'].notna()) & (df['year'] >= df['esg_first_law_year'])
    ).astype(int)
    df['fn_esg_has_muni_bond_law_post_lag1'] = group_shift('fn_esg_has_muni_bond_law_post', 1)
    log(f"  fn_esg_has_muni_bond_law_post: "
        f"{int(df['fn_esg_has_muni_bond_law_post'].sum())} city-years post-passage")
else:
    log("  [skip] need esg_has_muni_bond_law + esg_first_law_year for pre/post flag")

# ----- 5.2 Fisher-exact sample definitions (T3) — documentation only. -----
log("\n── 5.2 Fisher-exact sample definitions are documentation-only ──")
# Both sample-definition filters are computed and reported by the Table-3 analysis
# script; nothing to construct here, but we log for traceability.
log("  Definition A: full panel, any Green_Bond_Issued==1, Rep_Mayor lag 1.")
log("  Definition B: restrict to water-only issuers (Y_water_only==1), Rep_Mayor lag 1.")

# ----- 5.3 Table-3 robustness FE samples — constructed downstream. -----
log("\n── 5.3 Table-3 robustness FE samples (constructed in analysis_table3.py) ──")
# No construction here; the three FE variants are regression-spec changes.


# ═══════════════════════════════════════════════════════════════════════
# WRITE OUTPUTS
# ═══════════════════════════════════════════════════════════════════════
ensure_sorted()
n_cols_after = len(df.columns)
log("\n" + "=" * 70)
log(f"DONE: {n_cols_after - n_cols_before} new columns added")
log(f"Panel: {df.shape[0]:,} rows × {df.shape[1]:,} cols")
log("=" * 70)

df.to_pickle(PANEL_PATH)
log(f"Saved pickle: {PANEL_PATH}")

# Also write a compressed-CSV snapshot at the path consumed by the analysis
# scripts referenced in the spec (`processed/merged_city_year_panel.csv.gz`).
OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_CSV, index=False, compression='gzip')
log(f"Saved CSV:    {OUT_CSV}")
