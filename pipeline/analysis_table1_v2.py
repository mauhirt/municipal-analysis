"""
analysis_table1_v2.py — Table 1 rewritten with all Part A-E decisions
======================================================================
Supersedes analysis_table1_threefamily.py. Incorporates:

  - Part D primary: Dem_Mayor (no lag, drops Ind_Mayor)
  - TEL main effect dropped (absorbed by state FE), replaced by
    tel_x_prop_tax_dep (Mullins revenue-substitution)
  - State clustering (not fips7 — TEL is state-level)
  - Symmetric state party triple (dem_gov + dem_trifecta + rep_trifecta)
  - ESG law post-enactment (fn_esg_has_muni_bond_law_post_lag1)
  - State market depth (asinh_state_all_green_cum_amt_lag1)
  - MEDSL-backed pres_dem_two_party_share_lag2 (full 2013-2025)
  - igr_share_lag2 as primary aid-dependence measure
  - capital_outlay_pc_lag2 (fiscal doc J27, previously MISSING)

Effective N = 5,962 city-years (572 cities, 49 states).

This script is designed to run in modules to avoid timeout. Each module
writes its output to processed/tables/ and can be run independently.

Module selection via env var: `TABLE1_MODULE={main,r1_6,r7_12,all}`
Default: main (6 primary columns only).
"""
import os
import sys
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_panel, stars

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'processed' / 'tables'
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODULE = os.environ.get('TABLE1_MODULE', 'main')

# ──────────────────────────────────────────────────────────────────────
# Primary RHS (19 variables, all Part A-E decisions integrated)
# ──────────────────────────────────────────────────────────────────────
PRIMARY_RHS = [
    # Treatment (Part D: Dem_Mayor primary, no lag)
    'Dem_Mayor',
    # Constituency (MEDSL-backed)
    'pres_dem_two_party_share_lag2',
    # Family 1a compulsion
    'npdes_formal_prior3yr_muni',
    'overflow_events_lag2',
    # Family 1b fiscal (user-distilled 5)
    'charges_to_own_source_lag2',
    'reserve_ratio_lag2',
    'debt_service_burden_lag2',
    'igr_share_lag2',
    'tel_x_prop_tax_dep',
    # Family 3 state (symmetric triple + ESG post + market)
    'state_dem_governor_lag1',
    'state_dem_trifecta_lag1',
    'state_rep_trifecta_lag1',
    'fn_esg_has_muni_bond_law_post_lag1',
    'asinh_state_all_green_cum_amt_lag1',
    # Controls
    'log_population_city_lag2',
    'log_percapita_income_city_lag2',
    'unemployment_city_lag2',
    'has_substitute_issuer',
    'capital_outlay_pc_lag2',
]


# ──────────────────────────────────────────────────────────────────────
# Regression helper — state-clustered SE, state+year FE via dummies
# ──────────────────────────────────────────────────────────────────────
def fit_ols(df, y, xs, fe=('state_id', 'year'), cluster='state_id'):
    raw = ['fips7', cluster] + list(fe) + [y] + xs
    seen, cols = set(), []
    for c in raw:
        if c in df.columns and c not in seen:
            cols.append(c); seen.add(c)
    d = df[cols].copy()
    d = d.dropna(subset=[y] + [x for x in xs if x in d.columns])
    xs_live = [x for x in xs if x in d.columns and d[x].nunique(dropna=True) > 1]
    if len(d) < 30 or not xs_live:
        return None, 0
    X_parts = [d[xs_live].astype(float)]
    for f in fe:
        if f in d.columns and d[f].nunique() > 1:
            X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
    X = pd.concat(X_parts, axis=1)
    X = sm.add_constant(X).astype(float)
    y_vec = d[y].astype(float).values
    try:
        res = sm.OLS(y_vec, X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d[cluster].values})
        res._xnames = list(X.columns)
        res._n_cities = d['fips7'].nunique()
        res._n_states = d['state_id'].nunique() if 'state_id' in d.columns else 0
        return res, len(d)
    except Exception as e:
        print(f"    fit error: {e}")
        return None, 0


def coef(res, name):
    if res is None:
        return np.nan, np.nan, np.nan
    try:
        i = res._xnames.index(name)
        return float(res.params[i]), float(res.bse[i]), float(res.pvalues[i])
    except (ValueError, KeyError):
        return np.nan, np.nan, np.nan


def fmt(b, se, p):
    if np.isnan(b):
        return '—'
    return f'{b:+.4f}{stars(p)} ({se:.4f})'


# ──────────────────────────────────────────────────────────────────────
# Load panel
# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel loaded: {df.shape}")
print(f"Running module: {MODULE}\n")


# ──────────────────────────────────────────────────────────────────────
# MODULE: main — 6 primary columns
# ──────────────────────────────────────────────────────────────────────
def run_main():
    # Triple interaction columns for Col 5.
    if {'Dem_Mayor', 'npdes_formal_prior3yr_muni'}.issubset(df.columns):
        df['dem_x_npdes'] = df['Dem_Mayor'] * df['npdes_formal_prior3yr_muni']
    if {'Dem_Mayor', 'overflow_events_lag2'}.issubset(df.columns):
        df['dem_x_overflow'] = df['Dem_Mayor'] * df['overflow_events_lag2']
    if {'Dem_Mayor', 'npdes_formal_prior3yr_muni', 'fiscal_stress_index_lag2'}.issubset(df.columns):
        df['dem_x_npdes_x_fiscal'] = (
            df['Dem_Mayor'] * df['npdes_formal_prior3yr_muni']
            * df['fiscal_stress_index_lag2']
        )

    cols_spec = [
        ('Col 1', 'Green_Bond_Issued',    PRIMARY_RHS, 'LPM; H1b: Dem_Mayor null at extensive margin'),
        ('Col 2', 'asinh_green_amt',      PRIMARY_RHS, 'Intensive margin'),
        ('Col 3', 'Y_self_green',         PRIMARY_RHS, 'Pivot: Dem_Mayor expected +'),
        ('Col 4', 'asinh_self_green_amt', PRIMARY_RHS, 'Self-label amount'),
        ('Col 5', 'Green_Bond_Issued',
         PRIMARY_RHS + [v for v in ['dem_x_npdes', 'dem_x_overflow', 'dem_x_npdes_x_fiscal']
                        if v in df.columns],
         'Triple interactions (Dem × compulsion × fiscal)'),
        ('Col 6', 'asinh_green_amt',      PRIMARY_RHS, '§4.1 intensive margin replication'),
    ]

    print("=== Table 1 main (Parts A–E integrated) ===\n")
    results = []
    for label, y, xs, note in cols_spec:
        if y not in df.columns:
            print(f"  [skip] {label}: outcome {y} missing"); continue
        res, n = fit_ols(df, y, xs, fe=('state_id', 'year'), cluster='state_id')
        results.append((label, y, xs, note, res, n))
        if res is None:
            print(f"  [skip] {label}: fit failed"); continue
        b, se, p = coef(res, 'Dem_Mayor')
        focal = 'Dem_Mayor'
        print(f"  {label:6s}  y={y:25s}  n={n:4d} "
              f"({res._n_cities} cities, {res._n_states} states)  "
              f"β({focal})={b:+.4f}{stars(p)} (se={se:.4f})  [{note}]")
        for x in xs:
            if x.startswith('dem_x_'):
                bb, ss, pp = coef(res, x)
                if not np.isnan(bb):
                    print(f"           β({x})={bb:+.4f}{stars(pp)} (se={ss:.4f})")

    # Write markdown output.
    focus = [
        'Dem_Mayor', 'pres_dem_two_party_share_lag2',
        'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
        'charges_to_own_source_lag2', 'reserve_ratio_lag2',
        'debt_service_burden_lag2', 'igr_share_lag2', 'tel_x_prop_tax_dep',
        'state_dem_governor_lag1', 'state_dem_trifecta_lag1', 'state_rep_trifecta_lag1',
        'fn_esg_has_muni_bond_law_post_lag1', 'asinh_state_all_green_cum_amt_lag1',
        'log_population_city_lag2', 'log_percapita_income_city_lag2',
        'unemployment_city_lag2', 'has_substitute_issuer', 'capital_outlay_pc_lag2',
        'dem_x_npdes', 'dem_x_overflow', 'dem_x_npdes_x_fiscal',
    ]
    lines = ['# Table 1 — Three-Family Compulsion Pipeline (v2, all Parts A-E integrated)', '',
             '**Primary treatment:** Dem_Mayor (Part D, no lag — mayor_party.csv coding',
             'effectively lags). Standard errors clustered at STATE (not fips7). State + year FE.',
             'TEL main effect dropped (absorbed by state FE); replaced by `tel_x_prop_tax_dep`',
             '(Mullins revenue-substitution interaction).', '',
             'Effective sample: 5,962 city-years; 572 cities; 49 states.', '', '']
    lines.append('| Variable | ' + ' | '.join(f'{lbl}<br>{y}' for (lbl, y, *_) in results) + ' |')
    lines.append('|---' + '|---' * len(results) + '|')
    for v in focus:
        cells = []
        for (_, _, _, _, res, _) in results:
            b, se, p = coef(res, v)
            cells.append(fmt(b, se, p))
        lines.append(f'| `{v}` | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, _, _, n) in results) + ' |')
    lines.append('| R² | ' + ' | '.join(
        f'{getattr(r, "rsquared", float("nan")):.3f}' if r is not None else '—'
        for (_, _, _, _, r, _) in results) + ' |')
    lines.append('')
    lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01.')
    (OUT_DIR / 'table1_v2_main.md').write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT_DIR / 'table1_v2_main.md'}")
    return results


if MODULE in ('main', 'all'):
    main_results = run_main()


# ──────────────────────────────────────────────────────────────────────
# MODULE: r1_6 — first six robustness columns
# ──────────────────────────────────────────────────────────────────────
def run_rob(specs, outfile_md, title):
    print(f"\n=== {title} ===\n")
    results = []
    for label, y, xs, note in specs:
        if y not in df.columns:
            print(f"  [skip] {label}: outcome missing"); continue
        res, n = fit_ols(df, y, xs, fe=('state_id', 'year'), cluster='state_id')
        results.append((label, y, xs, note, res, n))
        if res is None:
            print(f"  [skip] {label}: fit failed"); continue
        focal = 'Dem_Mayor' if 'Dem_Mayor' in xs else \
                ('prob_democrat' if 'prob_democrat' in xs else \
                ('mayor_vote_share_win' if 'mayor_vote_share_win' in xs else
                ('Rep_Mayor_lag1' if 'Rep_Mayor_lag1' in xs else xs[0])))
        b, se, p = coef(res, focal)
        print(f"  {label:16s}  y={y:25s}  n={n:4d}  β({focal})={b:+.4f}{stars(p)} (se={se:.4f})  [{note}]")

    # Build a focus variable list that union-covers all robustness additions.
    focus = list(dict.fromkeys([v for (_, _, xs, *_) in results for v in xs]))
    lines = [f'# {title}', '',
             'Standard errors clustered at STATE. State + year FE. Primary treatment',
             '= Dem_Mayor (no lag) unless otherwise noted in the column label.', '', '']
    lines.append('| Variable | ' + ' | '.join(f'{lbl}<br>{y}' for (lbl, y, *_) in results) + ' |')
    lines.append('|---' + '|---' * len(results) + '|')
    for v in focus:
        cells = []
        for (_, _, _, _, res, _) in results:
            b, se, p = coef(res, v)
            cells.append(fmt(b, se, p))
        lines.append(f'| `{v}` | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, _, _, n) in results) + ' |')
    lines.append('| R² | ' + ' | '.join(
        f'{getattr(r, "rsquared", float("nan")):.3f}' if r is not None else '—'
        for (_, _, _, _, r, _) in results) + ' |')
    lines.append('')
    lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01.')
    (OUT_DIR / outfile_md).write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT_DIR / outfile_md}")
    return results


if MODULE in ('r1_6', 'all'):
    Y = 'Y_self_green'  # use pivot as the robustness dependent variable
    rob_specs_1_6 = []

    # R1: + YCOM opinion (regulate + fundrenewables)
    ycom = [v for v in ['opinion_regulate_lag2', 'opinion_fundrenewables_lag2']
            if v in df.columns]
    if ycom:
        rob_specs_1_6.append(('R1 + YCOM', Y, PRIMARY_RHS + ycom,
                              'Does Dem_Mayor survive conditioning on climate opinion?'))

    # R2: + IIJA/IRA/FEMA federal grants (critical endogeneity test)
    grants = [v for v in [
        'iija_water_grant_amt_asinh_lag1',
        'ira_eecbg_grant_amt_asinh_lag1',
        'ira_ggrf_grant_amt_asinh_lag1',
        'iija_transit_grant_amt_asinh_lag1',
        'fema_resil_grant_amt_asinh_lag1',
    ] if v in df.columns]
    if grants:
        rob_specs_1_6.append(('R2 + Grants', Y, PRIMARY_RHS + grants,
                              'Critical test: partisan gap narrows when grants added?'))

    # R3: swap Dem_Mayor → prob_democrat (continuous probability, no lag)
    rhs_prob = [v for v in PRIMARY_RHS if v != 'Dem_Mayor']
    if 'prob_democrat' in df.columns:
        rob_specs_1_6.append(('R3 Prob Dem', Y, rhs_prob + ['prob_democrat'],
                              'Continuous probability replaces binary Dem_Mayor (Part D)'))

    # R4: swap Dem_Mayor → mayor_vote_share_win (continuous vote share)
    if 'mayor_vote_share_win' in df.columns:
        rob_specs_1_6.append(('R4 Vote Share', Y, rhs_prob + ['mayor_vote_share_win'],
                              'Continuous mayor vote share (MayoralCandidates, Part D)'))

    # R5: + state climate policy (carbon pricing + GHG law + RGGI + ZEV)
    state_climate = [v for v in ['state_carbon_pricing_lag1',
                                  'state_ghg_law_active_lag1',
                                  'state_rggi_member_lag1',
                                  'state_zev_mandate_active_lag1']
                      if v in df.columns]
    if state_climate:
        rob_specs_1_6.append(('R5 State Climate', Y, PRIMARY_RHS + state_climate,
                              'Adds state carbon pricing + GHG law + RGGI + ZEV (authoritative sources)'))

    # R6: + ESG law intensity (continuous)
    if 'esg_law_intensity_lag1' in df.columns:
        rob_specs_1_6.append(('R6 ESG Int', Y, PRIMARY_RHS + ['esg_law_intensity_lag1'],
                              'Continuous ESG-law intensity replaces binary post flag'))

    run_rob(rob_specs_1_6, 'table1_v2_robustness_1_6.md',
            'Table 1 Robustness — R1-R6 (YCOM, grants, probabilistic, vote-share, state climate, ESG intensity)')


if MODULE in ('r7_12', 'all'):
    Y = 'Y_self_green'
    rob_specs_7_12 = []

    # R7: + climate-network membership (combined + individual)
    nets = [v for v in ['climate_commitment_static', 'c40_member_lag1',
                        'iclei_member_lag1', 'mcpa_signatory_lag1']
            if v in df.columns]
    if nets:
        rob_specs_7_12.append(('R7 Networks', Y, PRIMARY_RHS + nets,
                               'C40/ICLEI/MCPA network membership'))

    # R8: + urbanisation controls
    urb = [v for v in ['pop_density_sqkm_lag2', 'is_principal_city_lag2']
           if v in df.columns]
    if urb:
        rob_specs_7_12.append(('R8 Urban', Y, PRIMARY_RHS + urb,
                               'Pop density + principal city status'))

    # R9: + BPS/IECC compulsion (fiscal doc audit primary choice)
    bps = [v for v in ['bcode_iecc_lag_yrs_lag1',
                       'bcode_state_weakening_amendments_lag1',
                       'bcode_state_bps_adopted_lag1']
           if v in df.columns]
    if bps:
        rob_specs_7_12.append(('R9 BPS/IECC', Y, PRIMARY_RHS + bps,
                               'Building Performance Standards + IECC lag + weakening amendments'))

    # R10: swap compulsion variables for pooled compulsion_index_z
    rhs_no_compulsion = [v for v in PRIMARY_RHS
                         if v not in ('npdes_formal_prior3yr_muni', 'overflow_events_lag2')]
    if 'compulsion_index_z' in df.columns:
        rob_specs_7_12.append(('R10 Pooled Index', Y,
                               rhs_no_compulsion + ['compulsion_index_z'],
                               'Pooled compulsion index (equal-weighted z-score composite, 5 cmps)'))

    # R11: + CAA nonattainment (EPA Green Book)
    caa = [v for v in ['caa_any_criteria_nonattainment_lag1',
                       'caa_ozone_nonattainment_any_lag1',
                       'caa_ozone_class_ordinal_lag1']
           if v in df.columns]
    if caa:
        rob_specs_7_12.append(('R11 CAA', Y, PRIMARY_RHS + caa,
                               'EPA Green Book CAA nonattainment (transportation compulsion channel)'))

    # R12: Water compulsion ladder (informal + formal + violations + JDC simultaneously)
    ladder = [v for v in [
        'npdes_formal_prior3yr_muni',
        'epa_npdes_informal_asinh_lag2',
        'epa_water_violations_asinh_lag2',
        'case_jdc_prior3yr_muni',
    ] if v in df.columns]
    rhs_no_npdes = [v for v in PRIMARY_RHS if v != 'npdes_formal_prior3yr_muni']
    if ladder:
        rob_specs_7_12.append(('R12 Water Ladder', Y, rhs_no_npdes + ladder,
                               'Water compulsion ladder: informal + formal + violations + JDC'))

    run_rob(rob_specs_7_12, 'table1_v2_robustness_7_12.md',
            'Table 1 Robustness — R7-R12 (networks, urban, BPS, pooled compulsion, CAA, water ladder)')


if MODULE in ('r13_18', 'all'):
    Y = 'Y_self_green'
    rob_specs_13_18 = []

    # R13: + state market × partisanship interaction (E1 key test)
    if 'state_green_cum_x_rep' in df.columns:
        rob_specs_13_18.append(('R13 Market×Rep', Y,
                                PRIMARY_RHS + ['Rep_Mayor_lag1', 'state_green_cum_x_rep'],
                                'E1: state market depth × Rep_Mayor (normalisation test)'))

    # R14: + co-partisan spillover (state's Rep-led self-label activity × Dem mayor)
    copartisan = [v for v in ['state_any_rep_self_green_lag1',
                               'rep_x_state_rep_green',
                               'state_any_self_green_lag1']
                  if v in df.columns]
    if copartisan:
        rob_specs_13_18.append(('R14 CoPartisan', Y,
                                PRIMARY_RHS + ['Rep_Mayor_lag1'] + copartisan,
                                'Co-partisan state spillover: has Rep-led city previously self-labelled?'))

    # R15: + ESG pre/post × state_pre_esg_activity (E2 endogeneity test)
    endog = [v for v in ['state_pre_esg_activity',
                         'esg_post_x_pre_activity',
                         'esg_years_since_x_pre_activity']
             if v in df.columns]
    if endog:
        rob_specs_13_18.append(('R15 ESG Endog', Y, PRIMARY_RHS + endog,
                                'E2: anti-ESG suppression conditional on pre-law market activity'))

    # R16: + ICMA FOG × Dem_Mayor interactions (all five)
    fog_int = [v for v in ['dem_x_termlimits', 'dem_x_termlength',
                            'dem_x_fog', 'dem_x_initiative', 'dem_x_referendum']
               if v in df.columns]
    if fog_int:
        rob_specs_13_18.append(('R16 FOG×Dem', Y, PRIMARY_RHS + fog_int,
                                'ICMA FOG institutional interactions with Dem_Mayor'))

    # R17: swap Dem_Mayor → Rep_Mayor_lag1 (memo legacy mirror)
    rhs_rep = [v for v in PRIMARY_RHS if v != 'Dem_Mayor']
    if 'Rep_Mayor_lag1' in df.columns:
        rob_specs_13_18.append(('R17 Rep Mayor', Y, rhs_rep + ['Rep_Mayor_lag1'],
                                'Legacy mirror: Rep_Mayor_lag1 instead of Dem_Mayor'))

    # R18: + Rep × pres_dem interaction (T1 symmetry with T3 Col 4)
    extras = [v for v in ['rep_x_pres_dem_share', 'dem_x_pres_dem_share']
              if v in df.columns]
    if extras:
        rob_specs_13_18.append(('R18 Rep×PresDem', Y,
                                PRIMARY_RHS + ['Rep_Mayor_lag1'] + extras,
                                'Electoral discipline: mayor × presidential share interaction'))

    run_rob(rob_specs_13_18, 'table1_v2_robustness_13_18.md',
            'Table 1 Robustness — R13-R18 (Part E state market, co-partisan, ESG endog, FOG×Dem, Rep mirror, electoral discipline)')
