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
# Three-family spec, aligned with VARIABLE_ADDITIONS_SPEC.md.
#
# FAMILY 1 — MATERIAL (compulsion + fiscal capacity):
#   npdes_formal_prior3yr_muni, npdes_x_state_green (marketability interaction),
#   reserve_ratio_lag2, debt_service_burden_lag2
#
# FAMILY 2 — POLITICAL (partisan identity + constituency):
#   Dem_Mayor, pres_dem_two_party_share_lag2
#
# FAMILY 3 — STATE/INSTITUTIONAL (state political + ESG policy + market depth):
#   state_dem_governor_lag1, fn_esg_has_muni_bond_law_post_lag1,
#   asinh_state_all_green_cum_amt_lag1
#
# CONTROLS (standard muni-finance demographics):
#   log_population_city_lag2, log_percapita_income_city_lag2, unemployment_city_lag2
#
# Total: 12 variables (including the npdes_x_state_green interaction).
# Dropped from earlier iterations (available in robustness R22 kitchen-sink):
#   charges_to_own_source_lag2, igr_share_lag2, tel_x_prop_tax_dep,
#   capital_outlay_pc_lag2, has_substitute_issuer, state_dem_trifecta_lag1,
#   state_rep_trifecta_lag1, fiscal_stress_index_lag2 (collinear composite)
PRIMARY = [
    # Family 1: Material
    'Dem_Mayor',  # moved up as treatment (reported first for clarity)
    'pres_dem_two_party_share_lag2',  # Family 2
    'npdes_formal_prior3yr_muni',
    'reserve_ratio_lag2', 'debt_service_burden_lag2',
    # Family 3: State/Institutional
    'state_dem_governor_lag1',
    'fn_esg_has_muni_bond_law_post_lag1',
    'asinh_state_all_green_cum_amt_lag1',
    # Controls
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2',
]

# 18-var "kitchen-sink" spec for the R22 robustness column below.
PRIMARY_KITCHEN = PRIMARY + [
    'charges_to_own_source_lag2', 'igr_share_lag2', 'tel_x_prop_tax_dep',
    'capital_outlay_pc_lag2', 'has_substitute_issuer',
    'state_dem_trifecta_lag1', 'state_rep_trifecta_lag1',
    'fiscal_stress_index_lag2',
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
    # Note omitted controls for transparency
    omitted = list(dict.fromkeys(v for (_, _, xs, *_) in results for v in xs
                                  if (v.startswith('log_') or v.startswith('unemployment')
                                      or v in ('has_substitute_issuer','capital_outlay_pc_lag2'))))
    if omitted:
        lines.append('\nControls included but not shown: ' + ', '.join(f'`{v}`' for v in omitted) + '.')
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
# M1 demonstration interaction (Task 2 winner)
if 'dem_x_state_green_cum' not in df.columns:
    df['dem_x_state_green_cum'] = (
        df['Dem_Mayor'] * df.get('asinh_state_all_green_cum_amt_lag1', 0))
# Marketability interaction: NPDES × state green market depth
if 'npdes_x_state_green' not in df.columns:
    df['npdes_x_state_green'] = (
        df.get('npdes_formal_prior3yr_muni', 0) * df.get('asinh_state_all_green_cum_amt_lag1', 0))
# Water-only amount (for C6 main column)
if 'asinh_water_only_amt' not in df.columns:
    water_amt = df.get('City_Green_Amt_Issued', 0) * df.get('Y_water_only', 0)
    df['asinh_water_only_amt'] = np.arcsinh(water_amt)

# PRIMARY_EXPANDED = three-family PRIMARY + marketability interaction (F1×F3)
# fiscal_stress_index moved to robustness; debt_service carries the
# greenium-incentive story (high marginal borrowing cost).
PRIMARY_EXPANDED = PRIMARY + ['npdes_x_state_green']

# ══════════════════════════════════════════════════════════════════════
# MODULE: main — 8 primary columns
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('main', 'all'):
    # Main 8 cols: 4 outcome × scale combos × (no interaction, with interaction).
    # PRIMARY      = three families + controls (no marketability interaction)
    # PRIMARY_EXPANDED = PRIMARY + npdes × state_green_cum (marketability)
    # Paired columns let readers see the NPDES main effect flip when the
    # interaction is added.
    specs = [
        ('C1 GBI',          'Green_Bond_Issued',    PRIMARY,          'No interaction'),
        ('C2 GBI+int',      'Green_Bond_Issued',    PRIMARY_EXPANDED, 'With marketability interaction'),
        ('C3 GBI amt',      'asinh_green_amt',      PRIMARY,          'No interaction'),
        ('C4 GBI amt+int',  'asinh_green_amt',      PRIMARY_EXPANDED, 'With marketability interaction'),
        ('C5 Self',         'Y_self_green',         PRIMARY,          'No interaction'),
        ('C6 Self+int',     'Y_self_green',         PRIMARY_EXPANDED, 'With marketability interaction'),
        ('C7 Self amt',     'asinh_self_green_amt', PRIMARY,          'No interaction'),
        ('C8 Self amt+int', 'asinh_self_green_amt', PRIMARY_EXPANDED, 'With marketability interaction'),
    ]
    run_block(df, specs, 'table1_v3_main.md',
              'Table 1 v3 — Main 8 columns (4 outcomes × {no interaction, with interaction})')

    # Partisan-interaction sub-block (separate output: complements main table)
    interaction_specs = [
        ('I1 NPDES×Party',   'Green_Bond_Issued',
         PRIMARY_EXPANDED + ['dem_x_npdes'],
         'NPDES compulsion × Dem'),
        ('I2 NPDES×Party Self','Y_self_green',
         PRIMARY_EXPANDED + ['dem_x_npdes'],
         'NPDES compulsion × Dem on self-green'),
        ('I3 Demonstration', 'Y_self_green',
         PRIMARY_EXPANDED + ['dem_x_state_green_cum'],
         'Dem × state green cum (demonstration/imitation)'),
    ]
    run_block(df, interaction_specs, 'table1_v3_interactions.md',
              'Table 1 v3 — Partisan interactions (complement to main table)')

# ══════════════════════════════════════════════════════════════════════
# MODULE: appendix — demoted interaction specs + M2-M4
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('appendix', 'all'):
    Y = 'Y_self_green'
    # Build M2-M4 interactions if not present
    for mvar in ['state_any_prior_green_issuance_lag1',
                 'state_city_prior_green_issuance_lag1',
                 'state_city_count_prior_green_lag1']:
        if mvar not in df.columns:
            if mvar == 'state_any_prior_green_issuance_lag1':
                df[mvar] = df['state_green_bond_ever_lag1'].fillna(0).astype(int)
            elif mvar == 'state_city_prior_green_issuance_lag1':
                df[mvar] = df['state_any_self_green_lag1'].fillna(0).astype(int)
            elif mvar == 'state_city_count_prior_green_lag1':
                df[mvar] = 0  # simplified; full build in diagnostic script
        ivar = f'dem_x_{mvar}'
        if ivar not in df.columns:
            df[ivar] = df['Dem_Mayor'] * df[mvar]
    # Fiscal stress interactions
    if 'dem_x_fiscal_stress' not in df.columns:
        df['dem_x_fiscal_stress'] = df['Dem_Mayor'] * df.get('fiscal_stress_index_lag2', 0)
    if 'fiscal_stress_sq' not in df.columns:
        df['fiscal_stress_sq'] = df.get('fiscal_stress_index_lag2', 0) ** 2

    specs = [
        ('Ax1 Dem×Stress',  Y, PRIMARY + ['dem_x_fiscal_stress'],
         'Demoted: Dem × fiscal stress (labelling incentive)'),
        ('Ax2 Stress²',     Y, PRIMARY + ['fiscal_stress_sq'],
         'Demoted: inverted-U fiscal stress'),
        ('Ax3 M2 Binary',   Y, PRIMARY + ['state_any_prior_green_issuance_lag1',
         'dem_x_state_any_prior_green_issuance_lag1'],
         'M2: Dem × any-entity binary (40 states)'),
        ('Ax4 M3 City Bin', Y, PRIMARY + ['state_city_prior_green_issuance_lag1',
         'dem_x_state_city_prior_green_issuance_lag1'],
         'M3: Dem × city-issuer binary (26 states — fragility flag)'),
        ('Ax5 M4 City Cnt', Y, PRIMARY + ['state_city_count_prior_green_lag1',
         'dem_x_state_city_count_prior_green_lag1'],
         'M4: Dem × city-issuer count (26 states — fragility flag)'),
    ]
    run_block(df, specs, 'v3_rr/appendix_alt_interactions.md',
              'Appendix — Alternative Interaction Specifications')

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
    rhs_no_comp = [v for v in PRIMARY if v not in ('npdes_formal_prior3yr_muni',)]
    if 'compulsion_index_z' in df.columns:
        specs.append(('R10 Pooled Idx', Y, rhs_no_comp + ['compulsion_index_z'], 'Pooled compulsion z-score'))

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

    # R18 Rep_Mayor legacy mirror
    rhs_no_dem = [v for v in PRIMARY if v != 'Dem_Mayor']
    if 'Rep_Mayor_lag1' in df.columns:
        specs.append(('R18 Rep Mirror', Y, rhs_no_dem + ['Rep_Mayor_lag1'], 'Legacy Rep_Mayor_lag1'))

    # R19 FOG × Dem interactions
    fog = [v for v in ['dem_x_termlimits','dem_x_fog','dem_x_initiative'] if v in df.columns]
    if fog: specs.append(('R19 FOG×Dem', Y, PRIMARY + fog, 'ICMA FOG institutional interactions'))

    # R20 EPA ownership tier: replace _muni with _locgov (local-gov water districts)
    rhs_no_muni = [v for v in PRIMARY if v != 'npdes_formal_prior3yr_muni']
    if 'npdes_formal_prior3yr_locgov' in df.columns:
        specs.append(('R20 NPDES Locgov', Y, rhs_no_muni + ['npdes_formal_prior3yr_locgov'],
                      'Supplement: replace _muni with _locgov (water districts)'))

    # R21 EPA ownership placebo: _private enforcement (expected null)
    if 'npdes_formal_prior3yr_private' in df.columns:
        specs.append(('R21 NPDES Private', Y, rhs_no_muni + ['npdes_formal_prior3yr_private'],
                      'Placebo: _private enforcement (expected null)'))

    # R22 Kitchen-sink: PRIMARY + all previously-dropped controls
    specs.append(('R22 Kitchen-sink', Y, PRIMARY_KITCHEN,
                  'Kitchen-sink: PRIMARY + charges, IGR, TEL, capital_outlay, substitute_issuer, state trifectas, fiscal_stress composite'))

    # R23 Fiscal-stress composite (replaces components)
    rhs_no_fiscal = [v for v in PRIMARY if v not in ('reserve_ratio_lag2','debt_service_burden_lag2')]
    if 'fiscal_stress_index_lag2' in df.columns:
        specs.append(('R23 Fiscal Stress', Y, rhs_no_fiscal + ['fiscal_stress_index_lag2'],
                      'Composite fiscal stress in place of reserve + debt_service'))

    # R24 State trifectas (federalism courtesy)
    trifectas = [v for v in ['state_dem_trifecta_lag1','state_rep_trifecta_lag1'] if v in df.columns]
    if trifectas:
        specs.append(('R24 State Trifectas', Y, PRIMARY + trifectas,
                      'Add state trifecta dummies alongside governor'))

    run_block(df, specs, 'table1_v3_rob2.md',
              'Table 1 v3 — Robustness R11-R24 (gravity, ESG endog, Rep mirror, FOG, EPA tiers, kitchen-sink, fiscal stress, trifectas)')

# ══════════════════════════════════════════════════════════════════════
# MODULE: ftest — within-R² and compulsion-block F-test (Task 8)
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('ftest', 'all'):
    from linearmodels.panel import PanelOLS
    print("\n=== Task 8: Within-R² and compulsion-block F-test ===\n")

    # Build interaction terms if missing
    if 'dem_x_npdes' not in df.columns:
        df['dem_x_npdes'] = df['Dem_Mayor'] * df.get('npdes_formal_prior3yr_muni', 0)
    if 'dem_x_state_green_cum' not in df.columns:
        df['dem_x_state_green_cum'] = (
            df['Dem_Mayor'] * df.get('asinh_state_all_green_cum_amt_lag1', 0))

    COMPULSION_BLOCK = ['npdes_formal_prior3yr_muni',
                        'reserve_ratio_lag2', 'debt_service_burden_lag2',
                        'tel_x_prop_tax_dep']

    specs = [
        ('C1 GBI',          'Green_Bond_Issued',    PRIMARY),
        ('C2 GBI amt',      'asinh_green_amt',      PRIMARY),
        ('C3 Self-green',   'Y_self_green',         PRIMARY),
        ('C4 Self amt',     'asinh_self_green_amt',  PRIMARY),
        ('C5 NPDES×Party',  'Green_Bond_Issued',    PRIMARY + ['dem_x_npdes']),
        ('C6 Demonstration','Y_self_green',         PRIMARY + ['dem_x_state_green_cum']),
    ]

    results = []
    for label, y, xs in specs:
        if y not in df.columns:
            continue
        # Prepare data for PanelOLS
        all_cols = ['fips7', 'year', y] + xs
        all_cols = list(dict.fromkeys(c for c in all_cols if c in df.columns))
        d = df[all_cols].copy().dropna()
        xs_live = [x for x in xs if x in d.columns and d[x].nunique() > 1]
        if len(d) < 30 or not xs_live:
            continue

        d2 = d.set_index(['fips7', 'year'])
        try:
            mod = PanelOLS(d2[y], d2[xs_live].astype(float),
                           entity_effects=True, time_effects=True, check_rank=False)
            res = mod.fit(cov_type='clustered', cluster_entity=True)
            within_r2 = float(res.rsquared_within)

            # Compulsion-block Wald test: joint null that all compulsion vars = 0
            comp_in_model = [v for v in COMPULSION_BLOCK if v in xs_live and v in res.params.index]
            if comp_in_model:
                from scipy.stats import f as fdist
                beta = res.params[comp_in_model].values
                V = res.cov[comp_in_model].loc[comp_in_model].values
                try:
                    f_stat = float(beta @ np.linalg.inv(V) @ beta / len(comp_in_model))
                    f_p = float(1 - fdist.cdf(f_stat, len(comp_in_model),
                                              res.nobs - len(res.params)))
                except Exception:
                    f_stat, f_p = np.nan, np.nan
            else:
                f_stat, f_p = np.nan, np.nan

            results.append((label, y, len(d), within_r2, f_stat, f_p, len(comp_in_model)))
            print(f"  {label:20s}  N={len(d):4d}  within-R²={within_r2:.4f}  "
                  f"F({len(comp_in_model)})={f_stat:.2f}  p={f_p:.4f}{stars(f_p)}")
        except Exception as e:
            print(f"  {label:20s}  PanelOLS error: {e}")

    # Write ftest output
    lines = [
        '# Within-R² and Compulsion-Block F-Test (Task 8)',
        '',
        'Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.',
        'Cluster-robust SE at city level.',
        '',
        f'Compulsion block tested: {", ".join(COMPULSION_BLOCK)}',
        '',
        '| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |',
        '|---|---|---|---|---|---|---|',
    ]
    for label, y, n, wr2, fst, fp, dfn in results:
        lines.append(f'| {label} | `{y}` | {n} | {wr2:.4f} | {fst:.2f} | {fp:.4f}{stars(fp)} | {dfn} |')
    lines.extend([
        '',
        'Within-R² = variation explained after absorbing city and year FE.',
        'F-test: joint null that all compulsion-block coefficients = 0.',
        '',
        '* p<0.10, ** p<0.05, *** p<0.01.',
    ])
    (OUT / 'v3_rr' / 'within_r2_ftest.md').write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT / 'v3_rr' / 'within_r2_ftest.md'}")


# ══════════════════════════════════════════════════════════════════════
# MODULE: cluster_check — three SE schemes (Task 4)
# ══════════════════════════════════════════════════════════════════════
if MODULE in ('cluster_check', 'all'):
    print("\n=== Task 4: Clustering comparison (city / state / two-way) ===\n")

    if 'dem_x_npdes' not in df.columns:
        df['dem_x_npdes'] = df['Dem_Mayor'] * df.get('npdes_formal_prior3yr_muni', 0)
    if 'dem_x_state_green_cum' not in df.columns:
        df['dem_x_state_green_cum'] = (
            df['Dem_Mayor'] * df.get('asinh_state_all_green_cum_amt_lag1', 0))

    FOCUS_VARS = [
        'Dem_Mayor', 'pres_dem_two_party_share_lag2',
        'npdes_formal_prior3yr_muni',
        'reserve_ratio_lag2', 'debt_service_burden_lag2',
        'dem_x_npdes', 'dem_x_state_green_cum',
    ]

    specs = [
        ('C1 GBI',          'Green_Bond_Issued',    PRIMARY),
        ('C3 Self-green',   'Y_self_green',         PRIMARY),
        ('C5 NPDES×Party',  'Green_Bond_Issued',    PRIMARY + ['dem_x_npdes']),
        ('C6 Demonstration','Y_self_green',         PRIMARY + ['dem_x_state_green_cum']),
    ]

    all_rows = []
    for label, y, xs in specs:
        if y not in df.columns:
            continue
        all_cols = ['fips7', 'state_id', 'year', y] + xs
        all_cols = list(dict.fromkeys(c for c in all_cols if c in df.columns))
        d = df[all_cols].copy().dropna()
        xs_live = [x for x in xs if x in d.columns and d[x].nunique() > 1]
        if len(d) < 30 or not xs_live:
            continue

        # (a) City-clustered via OLS + dummies (baseline)
        X_parts = [d[xs_live].astype(float)]
        for f in ('state_id', 'year'):
            if f in d.columns and d[f].nunique() > 1:
                X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
        X = pd.concat(X_parts, axis=1)
        X = sm.add_constant(X).astype(float)
        yv = d[y].values.astype(float)

        res_city = sm.OLS(yv, X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d['fips7'].values})
        res_city._xnames = list(X.columns)

        res_state = sm.OLS(yv, X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d['state_id'].values})
        res_state._xnames = list(X.columns)

        # (c) Two-way: Cameron-Gelbach-Miller = V_city + V_state - V_city∩state
        # city∩state = city (cities don't span states), so V_twoway = V_city + V_state - V_city
        # = V_state. Actually CGM two-way with non-nested clusters:
        # V = V1 + V2 - V_intersection. Since each city is in exactly one state,
        # the intersection cluster = city. So V_twoway = V_city + V_state - V_city = V_state.
        # This means two-way = state clustering when clusters are nested.
        # For non-nested (city × year): V = V_city + V_year - V_city×year.
        # V_city×year = HC0 (each obs is its own cluster). Let's do city × year.
        res_hc0 = sm.OLS(yv, X.values).fit(cov_type='HC0')
        res_hc0._xnames = list(X.columns)

        # Two-way (city, year): V = V_city + V_year - V_HC0
        res_year = sm.OLS(yv, X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d['year'].values})
        res_year._xnames = list(X.columns)

        V_twoway = (np.diag(res_city.bse**2) + np.diag(res_year.bse**2)
                    - np.diag(res_hc0.bse**2))
        se_twoway = np.sqrt(np.maximum(np.diag(V_twoway), 0))

        for v in FOCUS_VARS:
            if v not in xs_live and v not in list(X.columns):
                continue
            try:
                i = list(X.columns).index(v)
            except ValueError:
                continue
            b = float(res_city.params[i])
            se_c = float(res_city.bse[i])
            se_s = float(res_state.bse[i])
            se_tw = float(se_twoway[i])
            t_c = b / se_c if se_c > 0 else np.nan
            t_s = b / se_s if se_s > 0 else np.nan
            t_tw = b / se_tw if se_tw > 0 else np.nan
            from scipy.stats import norm
            p_c = float(2 * (1 - norm.cdf(abs(t_c)))) if not np.isnan(t_c) else np.nan
            p_s = float(2 * (1 - norm.cdf(abs(t_s)))) if not np.isnan(t_s) else np.nan
            p_tw = float(2 * (1 - norm.cdf(abs(t_tw)))) if not np.isnan(t_tw) else np.nan

            all_rows.append({
                'col': label, 'var': v, 'b': b,
                'se_city': se_c, 't_city': t_c, 'p_city': p_c,
                'se_state': se_s, 't_state': t_s, 'p_state': p_s,
                'se_twoway': se_tw, 't_twoway': t_tw, 'p_twoway': p_tw,
                'n': len(d),
            })

        print(f"  {label} done (N={len(d)})")

    # Write output
    lines = [
        '# Clustering Comparison: City vs State vs Two-Way (Task 4)',
        '',
        'Same coefficient estimated under three SE schemes:',
        '- **(a) City-clustered** (baseline, 572 clusters)',
        '- **(b) State-clustered** (49 clusters)',
        '- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)',
        '',
        '| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |',
        '|---|---|---|---|---|---|---|---|---|---|---|---|',
    ]
    for r in all_rows:
        lines.append(
            f'| {r["col"]} | `{r["var"]}` | {r["b"]:+.4f} | '
            f'{r["se_city"]:.4f} | {r["t_city"]:+.2f} | {r["p_city"]:.3f}{stars(r["p_city"])} | '
            f'{r["se_state"]:.4f} | {r["t_state"]:+.2f} | {r["p_state"]:.3f}{stars(r["p_state"])} | '
            f'{r["se_twoway"]:.4f} | {r["t_twoway"]:+.2f} | {r["p_twoway"]:.3f}{stars(r["p_twoway"])} |'
        )

    # Reading: flag any variable where significance changes across schemes
    lines.extend(['', '## Reading', ''])
    attenuated = []
    for r in all_rows:
        city_sig = r['p_city'] < 0.10
        state_sig = r['p_state'] < 0.10
        tw_sig = r['p_twoway'] < 0.10
        if city_sig and not state_sig:
            attenuated.append(f'- **`{r["var"]}` in {r["col"]}:** significant under city clustering '
                            f'(p={r["p_city"]:.3f}) but NOT under state clustering '
                            f'(p={r["p_state"]:.3f}). SE inflates from {r["se_city"]:.4f} to {r["se_state"]:.4f}.')
        if city_sig and not tw_sig:
            attenuated.append(f'- **`{r["var"]}` in {r["col"]}:** significant under city clustering '
                            f'(p={r["p_city"]:.3f}) but NOT under two-way '
                            f'(p={r["p_twoway"]:.3f}).')
    if attenuated:
        lines.append('### Coefficients where significance is attenuated by alternative clustering:')
        lines.extend(attenuated)
    else:
        lines.append('No coefficients change significance category across clustering schemes.')

    lines.extend(['', '* p<0.10, ** p<0.05, *** p<0.01.'])
    (OUT / 'v3_rr' / 'cluster_comparison.md').write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT / 'v3_rr' / 'cluster_comparison.md'}")
