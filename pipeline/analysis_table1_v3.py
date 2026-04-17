"""
analysis_table1_v3.py — Table 1 with labelling-incentive + gravity additions
=============================================================================
Supersedes v2. Adds:
  - Cols 7-8: fiscal-stress labelling incentive (Dem × fiscal stress
    interaction + inverted-U squared term) on Y_self_green
  - Gravity-weighted spatial peer/substitute variables as robustness
  - Y_has_non_water outcome column for compositional-gap absorption test

Module execution: TABLE1_MODULE = {main, rob1, rob2, all}
"""
import os, sys, warnings
from pathlib import Path
import numpy as np, pandas as pd, statsmodels.api as sm

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import stars

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'processed' / 'tables'
OUT.mkdir(parents=True, exist_ok=True)
MODULE = os.environ.get('TABLE1_MODULE', 'main')

# ── RHS blocks ──
PRIMARY = [
    'Dem_Mayor',
    'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'debt_service_burden_lag2', 'igr_share_lag2', 'tel_x_prop_tax_dep',
    'state_dem_governor_lag1', 'state_dem_trifecta_lag1', 'state_rep_trifecta_lag1',
    'fn_esg_has_muni_bond_law_post_lag1', 'asinh_state_all_green_cum_amt_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2', 'has_substitute_issuer', 'capital_outlay_pc_lag2',
]

def fit(df, y, xs, fe=('state_id','year'), cluster='fips7'):
    raw = ['fips7','state_id'] + list(fe) + [y] + xs
    seen, cols = set(), []
    for c in raw:
        if c in df.columns and c not in seen:
            cols.append(c); seen.add(c)
    d = df[cols].copy().dropna()
    xs_live = [x for x in xs if x in d.columns and d[x].nunique()>1]
    if len(d)<30 or not xs_live: return None, 0
    X_parts = [d[xs_live].astype(float)]
    for f in fe:
        if f in d.columns and d[f].nunique()>1:
            X_parts.append(pd.get_dummies(d[f],prefix=f,drop_first=True,dtype=float))
    X = pd.concat(X_parts, axis=1)
    X = sm.add_constant(X).astype(float)
    try:
        res = sm.OLS(d[y].values.astype(float), X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d[cluster].values})
        res._xnames = list(X.columns)
        return res, len(d)
    except: return None, 0

def c(res, name):
    if res is None: return np.nan, np.nan, np.nan
    try:
        i = res._xnames.index(name)
        return float(res.params[i]), float(res.bse[i]), float(res.pvalues[i])
    except: return np.nan, np.nan, np.nan

def fmt(b, se, p):
    if np.isnan(b): return '—'
    return f'{b:+.4f}{stars(p)} ({se:.4f})'

def run_block(df, specs, outfile, title):
    print(f"\n=== {title} ===\n")
    results = []
    for label, y, xs, note in specs:
        if y not in df.columns: continue
        res, n = fit(df, y, xs)
        results.append((label, y, xs, note, res, n))
        if res is None:
            print(f"  {label:20s}  fit failed"); continue
        # Find focal treatment variable
        focal = next((v for v in ['Dem_Mayor','prob_democrat','mayor_vote_share_win',
                                   'Rep_Mayor_lag1'] if v in xs), xs[0])
        b, se, p = c(res, focal)
        extras = ''
        for v in xs:
            if v.startswith('dem_x_') or v.startswith('fiscal_stress_sq') or v.startswith('gravity_') or v.startswith('asinh_gravity_'):
                bb, ss, pp = c(res, v)
                if not np.isnan(bb) and abs(bb) > 1e-8:
                    extras += f'  {v.split("_lag")[0][:25]}={bb:+.4f}{stars(pp)}'
        print(f"  {label:20s}  y={y:25s}  n={n:4d}  β({focal})={b:+.4f}{stars(p)} (se={se:.4f}){extras}")

    # Write md
    focus = list(dict.fromkeys(v for (_, _, xs, *_) in results for v in xs
                               if not v.startswith('log_') and not v.startswith('unemployment')
                               and v != 'has_substitute_issuer' and v != 'capital_outlay_pc_lag2'))
    lines = [f'# {title}', '',
             'Dem_Mayor (no lag), state+year FE, city-clustered SE.', '']
    lines.append('| Variable | ' + ' | '.join(f'{lbl}' for (lbl, *_) in results) + ' |')
    lines.append('|---' + '|---' * len(results) + '|')
    for v in focus:
        cells = [fmt(*c(res, v)) for (_, _, _, _, res, _) in results]
        lines.append(f'| `{v}` | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, _, _, n) in results) + ' |')
    lines.append('| R² | ' + ' | '.join(
        f'{res.rsquared:.3f}' if res else '—' for (_, _, _, _, res, _) in results) + ' |')
    lines.append('\n* p<0.10, ** p<0.05, *** p<0.01.')
    (OUT / outfile).write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT / outfile}")
    return results

# ── Load ──
df = pd.read_pickle(ROOT / 'processed' / 'panel' / 'panel.pkl')
print(f"Panel: {df.shape}, Module: {MODULE}")

# Build interaction terms needed for main cols
if 'dem_x_npdes' not in df.columns:
    df['dem_x_npdes'] = df['Dem_Mayor'] * df.get('npdes_formal_prior3yr_muni', 0)
if 'dem_x_overflow' not in df.columns:
    df['dem_x_overflow'] = df['Dem_Mayor'] * df.get('overflow_events_lag2', 0)

# ══════════════════════════════════════════════════════════════════════
# MODULE: main — 8 primary columns
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('main', 'all'):
    specs = [
        ('C1 GBI',          'Green_Bond_Issued',    PRIMARY, 'H1b: Dem_Mayor null'),
        ('C2 GBI amt',      'asinh_green_amt',      PRIMARY, 'Intensive margin'),
        ('C3 Self-green',   'Y_self_green',         PRIMARY, 'Step 3 pivot'),
        ('C4 Self amt',     'asinh_self_green_amt',  PRIMARY, 'Self-label amount'),
        ('C5 Interactions', 'Green_Bond_Issued',
         PRIMARY + ['dem_x_npdes', 'dem_x_overflow'], 'Dem × compulsion'),
        ('C6 Non-water',    'Y_has_non_water',      PRIMARY, 'Compositional gap'),
        ('C7 Dem×Stress',   'Y_self_green',
         PRIMARY + ['dem_x_fiscal_stress'], 'Labelling incentive: Dem × fiscal stress'),
        ('C8 Stress U',     'Y_self_green',
         PRIMARY + ['fiscal_stress_sq'], 'Inverted-U: moderate stress → label'),
    ]
    run_block(df, specs, 'table1_v3_main.md',
              'Table 1 v3 — Main 8 columns (H1b + labelling incentive)')

# ══════════════════════════════════════════════════════════════════════
# MODULE: rob1 — robustness R1–R10
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('rob1', 'all'):
    Y = 'Y_self_green'
    specs = []

    # R1 YCOM
    ycom = [v for v in ['opinion_regulate_lag2','opinion_fundrenewables_lag2'] if v in df.columns]
    if ycom: specs.append(('R1 YCOM', Y, PRIMARY + ycom, 'Climate opinion'))

    # R2 Grants
    grants = [v for v in ['iija_water_grant_amt_asinh_lag1','ira_eecbg_grant_amt_asinh_lag1',
              'ira_ggrf_grant_amt_asinh_lag1','iija_transit_grant_amt_asinh_lag1',
              'fema_resil_grant_amt_asinh_lag1'] if v in df.columns]
    if grants: specs.append(('R2 Grants', Y, PRIMARY + grants, 'Federal grants'))

    # R3 prob_democrat (continuous, no lag)
    rhs_no_dem = [v for v in PRIMARY if v != 'Dem_Mayor']
    if 'prob_democrat' in df.columns:
        specs.append(('R3 Prob Dem', Y, rhs_no_dem + ['prob_democrat'], 'Continuous probability'))

    # R4 Vote share
    if 'mayor_vote_share_win' in df.columns:
        specs.append(('R4 Vote Share', Y, rhs_no_dem + ['mayor_vote_share_win'], 'Mayor vote share'))

    # R5 State climate policy
    climate = [v for v in ['state_carbon_pricing_lag1','state_ghg_law_active_lag1',
               'state_rggi_member_lag1','state_zev_mandate_active_lag1'] if v in df.columns]
    if climate: specs.append(('R5 State Clim', Y, PRIMARY + climate, 'Carbon + GHG + RGGI + ZEV'))

    # R6 ESG intensity
    if 'esg_law_intensity_lag1' in df.columns:
        specs.append(('R6 ESG Int', Y, PRIMARY + ['esg_law_intensity_lag1'], 'Continuous ESG intensity'))

    # R7 Networks
    nets = [v for v in ['climate_commitment_static','c40_member_lag1','iclei_member_lag1'] if v in df.columns]
    if nets: specs.append(('R7 Networks', Y, PRIMARY + nets, 'C40/ICLEI/MCPA'))

    # R8 Urban
    urb = [v for v in ['pop_density_sqkm_lag2','is_principal_city_lag2'] if v in df.columns]
    if urb: specs.append(('R8 Urban', Y, PRIMARY + urb, 'Density + principal city'))

    # R9 BPS/IECC
    bps = [v for v in ['bcode_iecc_lag_yrs_lag1','bcode_state_weakening_amendments_lag1'] if v in df.columns]
    if bps: specs.append(('R9 BPS/IECC', Y, PRIMARY + bps, 'Building codes'))

    # R10 Pooled compulsion index
    rhs_no_comp = [v for v in PRIMARY if v not in ('npdes_formal_prior3yr_muni','overflow_events_lag2')]
    if 'compulsion_index_z' in df.columns:
        specs.append(('R10 Pooled Idx', Y, rhs_no_comp + ['compulsion_index_z'], 'Pooled 5-comp z-score'))

    run_block(df, specs, 'table1_v3_rob1.md',
              'Table 1 v3 — Robustness R1-R10')

# ══════════════════════════════════════════════════════════════════════
# MODULE: rob2 — robustness R11–R20
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('rob2', 'all'):
    Y = 'Y_self_green'
    specs = []

    # R11 CAA nonattainment
    caa = [v for v in ['caa_ozone_nonattainment_any_lag1'] if v in df.columns]
    if caa: specs.append(('R11 CAA', Y, PRIMARY + caa, 'EPA Green Book'))

    # R12 Water ladder
    ladder = [v for v in ['epa_npdes_informal_asinh_lag2','epa_water_violations_asinh_lag2',
              'case_jdc_prior3yr_muni'] if v in df.columns]
    rhs_no_npdes = [v for v in PRIMARY if v != 'npdes_formal_prior3yr_muni']
    if ladder: specs.append(('R12 Water Ladder', Y, rhs_no_npdes + ['npdes_formal_prior3yr_muni'] + ladder, 'Full enforcement ladder'))

    # R13 Gravity: city peer (self-labelled)
    if 'asinh_gravity_city_peer_self' in df.columns:
        specs.append(('R13 Gravity Peer', Y, PRIMARY + ['asinh_gravity_city_peer_self'], 'City peer normalisation (1/d²)'))

    # R14 Gravity: special district (substitute)
    if 'asinh_gravity_special_self' in df.columns:
        specs.append(('R14 Gravity Subst', Y, PRIMARY + ['asinh_gravity_special_self'], 'Special district crowding out (1/d²)'))

    # R15 Gravity: county
    if 'asinh_gravity_county_self' in df.columns:
        specs.append(('R15 Gravity County', Y, PRIMARY + ['asinh_gravity_county_self'], 'County issuance (1/d²)'))

    # R16 Gravity: all three channels + all vs self
    grav_all = [v for v in ['asinh_gravity_city_peer_self','asinh_gravity_special_self',
                'asinh_gravity_county_self'] if v in df.columns]
    if grav_all: specs.append(('R16 Gravity All', Y, PRIMARY + grav_all, 'All 3 gravity channels'))

    # R17 ESG endogeneity
    endog = [v for v in ['state_pre_esg_activity','esg_post_x_pre_activity'] if v in df.columns]
    if endog: specs.append(('R17 ESG Endog', Y, PRIMARY + endog, 'Anti-ESG suppression × prior market'))

    # R18 Co-partisan spillover
    copart = [v for v in ['state_any_rep_self_green_lag1','rep_x_state_rep_green'] if v in df.columns]
    if copart: specs.append(('R18 CoPartisan', Y, PRIMARY + ['Rep_Mayor_lag1'] + copart, 'Co-partisan state spillover'))

    # R19 Rep_Mayor legacy mirror
    rhs_no_dem = [v for v in PRIMARY if v != 'Dem_Mayor']
    if 'Rep_Mayor_lag1' in df.columns:
        specs.append(('R19 Rep Mirror', Y, rhs_no_dem + ['Rep_Mayor_lag1'], 'Legacy Rep_Mayor_lag1'))

    # R20 FOG × Dem interactions
    fog = [v for v in ['dem_x_termlimits','dem_x_fog','dem_x_initiative'] if v in df.columns]
    if fog: specs.append(('R20 FOG×Dem', Y, PRIMARY + fog, 'ICMA FOG institutional interactions'))

    run_block(df, specs, 'table1_v3_rob2.md',
              'Table 1 v3 — Robustness R11-R20 (gravity, ESG endog, co-partisan, FOG)')
