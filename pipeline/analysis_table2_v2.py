"""
analysis_table2_v2.py — Table 2 (compulsion gradient H2a) rewritten
====================================================================
Supersedes analysis_table2.py. Incorporates all Part A-E decisions:

  - Dem_Mayor (no lag) primary per Part D
  - State-level clustering
  - Category-specific compulsion variables chosen per variable audit:
      Water         → NPDES primary + ladder (informal + formal + viol + JDC)
                      + pooled compulsion index robustness
      Clean trans.  → CAA nonattainment (EPA Green Book) + state GHG/ZEV
                      + IIJA transit grants
      Renewables    → RPS × muni-electric interaction (state policy × city
                      capacity) — restricts to muni-electric cities
      Energy eff.   → IECC lag (primary per audit) + BPS + ACEEE rank
      Green bldg.   → IECC lag + BPS + weakening amendments
      Climate adapt → NFIP losses + FEMA flood + NRI inland EAL
      Pollution     → EPA violations + informal + CAA any-criteria
      Natural res.  → NRI overall (time-invariant)
  - Stacked monotonicity regression with compulsion ordinal × Dem_Mayor

Modular execution: TABLE2_MODULE = {water, non_water, sparse, stacked, all}.
"""
import os
import sys
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import fisher_exact

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_panel, stars

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'processed' / 'tables'
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODULE = os.environ.get('TABLE2_MODULE', 'water')

# ──────────────────────────────────────────────────────────────────────
# Shared RHS (Part A-E primary spec from Table 1 v2, minus category-
# specific compulsion channel which each column picks up separately).
# ──────────────────────────────────────────────────────────────────────
SHARED_RHS = [
    'Dem_Mayor',
    'pres_dem_two_party_share_lag2',
    'charges_to_own_source_lag2',
    'reserve_ratio_lag2',
    'debt_service_burden_lag2',
    'igr_share_lag2',
    'tel_x_prop_tax_dep',
    'state_dem_governor_lag1',
    'state_dem_trifecta_lag1',
    'state_rep_trifecta_lag1',
    'fn_esg_has_muni_bond_law_post_lag1',
    'asinh_state_all_green_cum_amt_lag1',
    'log_population_city_lag2',
    'log_percapita_income_city_lag2',
    'unemployment_city_lag2',
    'has_substitute_issuer',
    'capital_outlay_pc_lag2',
]


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


def fisher_on_party(sub, y, treatment='Dem_Mayor'):
    m = sub[[y, treatment]].dropna()
    if len(m) < 10:
        return np.nan, 0, 0
    tab = pd.crosstab(m[treatment], m[y])
    if tab.shape != (2, 2):
        return np.nan, 0, 0
    try:
        _, p = fisher_exact(tab)
    except Exception:
        return np.nan, 0, 0
    if 0 in tab.index and 1 in tab.index and 1 in tab.columns:
        rate_d = tab.loc[1, 1] / tab.loc[1].sum() if tab.loc[1].sum() > 0 else 0
        rate_r = tab.loc[0, 1] / tab.loc[0].sum() if tab.loc[0].sum() > 0 else 0
    else:
        rate_d = rate_r = 0
    return p, rate_d, rate_r


# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel loaded: {df.shape}\nRunning module: {MODULE}\n")


# ──────────────────────────────────────────────────────────────────────
# MODULE: water — 3 variants for Y_water_only
# ──────────────────────────────────────────────────────────────────────
if MODULE in ('water', 'all'):
    print("=== Table 2 — Water category (3 compulsion variants) ===\n")
    Y = 'Y_water_only'
    n_pos = int(df[Y].fillna(0).sum())

    # Variant 1: memo primary compulsion (NPDES formal)
    rhs_primary = SHARED_RHS + [
        'npdes_formal_prior3yr_muni',
    ]
    # Variant 2: water compulsion ladder (simultaneously)
    rhs_ladder = SHARED_RHS + [
        'npdes_formal_prior3yr_muni',
        'epa_npdes_informal_asinh_lag2',
        'epa_water_violations_asinh_lag2',
        'case_jdc_prior3yr_muni',
    ]
    # Variant 3: pooled compulsion index (replaces individual cmp vars)
    rhs_pooled = SHARED_RHS + ['compulsion_index_z']

    specs = [
        ('W1 Primary (memo)', Y, rhs_primary,
         'Memo primary: NPDES formal enforcement'),
        ('W2 Ladder',          Y, rhs_ladder,
         'Full ladder: informal + formal + violations + JDC'),
        ('W3 Pooled Index',    Y, rhs_pooled,
         'Equal-weighted compulsion z-score composite'),
    ]
    results = []
    for label, y, xs, note in specs:
        res, n = fit_ols(df, y, xs)
        results.append((label, y, xs, note, res, n))
        if res is None:
            print(f"  [skip] {label}: fit failed"); continue
        b, se, p = coef(res, 'Dem_Mayor')
        print(f"  {label:18s}  n={n:4d}  n_pos={n_pos}  β(Dem_Mayor)={b:+.4f}{stars(p)} (se={se:.4f})")
        # Report each compulsion variable coefficient for comparison
        for v in xs:
            if v in ('npdes_formal_prior3yr_muni',
                     'epa_npdes_informal_asinh_lag2', 'epa_water_violations_asinh_lag2',
                     'case_jdc_prior3yr_muni', 'compulsion_index_z'):
                bb, ss, pp = coef(res, v)
                if not np.isnan(bb):
                    print(f"           β({v:40s})={bb:+.4f}{stars(pp)} (se={ss:.4f})")

    # Write md
    focus = ['Dem_Mayor', 'npdes_formal_prior3yr_muni',
             'epa_npdes_informal_asinh_lag2', 'epa_water_violations_asinh_lag2',
             'case_jdc_prior3yr_muni', 'compulsion_index_z',
             'pres_dem_two_party_share_lag2',
             'charges_to_own_source_lag2', 'reserve_ratio_lag2',
             'debt_service_burden_lag2', 'igr_share_lag2', 'tel_x_prop_tax_dep']
    lines = ['# Table 2 Col 1 — Water (3 compulsion-variable variants)',
             '', 'Primary treatment: `Dem_Mayor` (no lag). State+year FE. State clustering.',
             f'Water-only outcome; **{n_pos} positive city-years**.', '', '']
    lines.append('| Variable | ' + ' | '.join(f'{lbl}<br>{y}' for (lbl, y, *_) in results) + ' |')
    lines.append('|---' + '|---' * len(results) + '|')
    for v in focus:
        cells = []
        for (_, _, _, _, res, _) in results:
            cells.append(fmt(*coef(res, v)))
        lines.append(f'| `{v}` | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, _, _, n) in results) + ' |')
    lines.append('| R² | ' + ' | '.join(
        f'{getattr(r, "rsquared", float("nan")):.3f}' if r is not None else '—'
        for (_, _, _, _, r, _) in results) + ' |')
    lines.append('')
    lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01.')
    (OUT_DIR / 'table2_v2_water.md').write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT_DIR / 'table2_v2_water.md'}")


# ──────────────────────────────────────────────────────────────────────
# MODULE: non_water — clean transport, renewables, energy eff, green bldg
# ──────────────────────────────────────────────────────────────────────
if MODULE in ('non_water', 'all'):
    print("=== Table 2 — Non-water discretionary categories ===\n")

    non_water_specs = []
    # Clean Transportation
    Y = 'Y_Clean_Transportation'
    if Y in df.columns:
        extras = [v for v in ['caa_ozone_nonattainment_any_lag1',
                               'caa_any_criteria_nonattainment_lag1',
                               'state_ghg_law_active_lag1',
                               'state_zev_mandate_active_lag1',
                               'iija_transit_grant_amt_asinh_lag1']
                  if v in df.columns]
        non_water_specs.append(('T1 Clean Transport', Y, SHARED_RHS + extras,
                                'CAA + state GHG/ZEV + IIJA transit', extras,
                                None))

    # Renewables (muni-electric subsample only per memo)
    Y = 'Y_Renewable_Energy'
    if Y in df.columns:
        extras = [v for v in ['ep_muni_electric_rev_asinh_lag1',
                               'state_rps_active_lag1',
                               'state_rps_target_pct_lag1',
                               'rps_target_x_muni_electric',
                               'state_rggi_member_lag1',
                               'state_carbon_pricing_lag1']
                  if v in df.columns]
        # Restrict to muni-electric subsample
        subsample_mask = df.get('ep_has_muni_electric', 0) == 1
        non_water_specs.append(('T2 Renewables', Y, SHARED_RHS + extras,
                                'Muni-electric subsample; RPS × muni-electric interaction',
                                extras, subsample_mask))

    # Energy Efficiency
    Y = 'Y_Energy_Efficiency'
    if Y in df.columns:
        extras = [v for v in ['bcode_iecc_lag_yrs_lag1',
                               'bcode_state_bps_adopted_lag1',
                               'bcode_state_weakening_amendments_lag1',
                               'ep_state_aceee_code_rank_lag1',
                               'state_carbon_pricing_lag1',
                               'ira_eecbg_grant_amt_asinh_lag1']
                  if v in df.columns]
        non_water_specs.append(('T3 Energy Eff', Y, SHARED_RHS + extras,
                                'IECC lag (primary) + BPS + ACEEE rank + carbon + IRA EECBG',
                                extras, None))

    # Green Buildings
    Y = 'Y_Green_Buildings'
    if Y in df.columns:
        extras = [v for v in ['bcode_iecc_lag_yrs_lag1',
                               'bcode_state_bps_adopted_lag1',
                               'bcode_bps_adopted_lag1',
                               'bcode_state_weakening_amendments_lag1',
                               'ira_ggrf_grant_amt_asinh_lag1']
                  if v in df.columns]
        non_water_specs.append(('T4 Green Bldg', Y, SHARED_RHS + extras,
                                'IECC lag + state+city BPS + weakening + IRA GGRF',
                                extras, None))

    results = []
    for label, y, xs, note, extras, mask in non_water_specs:
        if y not in df.columns:
            print(f"  [skip] {label}: outcome missing"); continue
        d = df if mask is None else df[mask]
        npos = int(d[y].fillna(0).sum())
        res, n = fit_ols(d, y, xs)
        results.append((label, y, xs, note, res, n, npos, extras))
        if res is None:
            print(f"  [skip] {label}: fit failed"); continue
        b, se, p = coef(res, 'Dem_Mayor')
        print(f"  {label:22s}  n={n:4d}  n_pos={npos:3d}  β(Dem_Mayor)={b:+.4f}{stars(p)} (se={se:.4f})")
        # Report compulsion variable coefficients for comparison
        for v in extras:
            bb, ss, pp = coef(res, v)
            if not np.isnan(bb):
                print(f"           β({v:40s})={bb:+.4f}{stars(pp)} (se={ss:.4f})")

    # Write md
    focus = ['Dem_Mayor', 'pres_dem_two_party_share_lag2',
             # CAA / transport-compulsion
             'caa_ozone_nonattainment_any_lag1', 'caa_any_criteria_nonattainment_lag1',
             'state_ghg_law_active_lag1', 'state_zev_mandate_active_lag1',
             'iija_transit_grant_amt_asinh_lag1',
             # Renewables
             'ep_muni_electric_rev_asinh_lag1',
             'state_rps_active_lag1', 'state_rps_target_pct_lag1',
             'rps_target_x_muni_electric',
             'state_rggi_member_lag1', 'state_carbon_pricing_lag1',
             # Energy eff / green buildings
             'bcode_iecc_lag_yrs_lag1', 'bcode_state_bps_adopted_lag1',
             'bcode_bps_adopted_lag1', 'bcode_state_weakening_amendments_lag1',
             'ep_state_aceee_code_rank_lag1',
             'ira_eecbg_grant_amt_asinh_lag1', 'ira_ggrf_grant_amt_asinh_lag1',
             # Fiscal shared
             'charges_to_own_source_lag2', 'reserve_ratio_lag2',
             'debt_service_burden_lag2', 'tel_x_prop_tax_dep']
    lines = ['# Table 2 — Non-water discretionary categories',
             '', 'Primary treatment: `Dem_Mayor` (no lag). State + year FE, state clustering.',
             'Category-specific compulsion variables chosen per variable-audit Parts A-E.', '', '']
    lines.append('| Variable | ' + ' | '.join(f'{lbl}<br>{y}' for (lbl, y, *_) in results) + ' |')
    lines.append('|---' + '|---' * len(results) + '|')
    for v in focus:
        cells = []
        for (_, _, _, _, res, _, _, _) in results:
            cells.append(fmt(*coef(res, v)))
        lines.append(f'| `{v}` | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, _, _, n, _, _) in results) + ' |')
    lines.append('| n_pos | ' + ' | '.join(str(p) for (_, _, _, _, _, _, p, _) in results) + ' |')
    lines.append('| R² | ' + ' | '.join(
        f'{getattr(r, "rsquared", float("nan")):.3f}' if r is not None else '—'
        for (_, _, _, _, r, _, _, _) in results) + ' |')
    lines.append('')
    lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01.')
    (OUT_DIR / 'table2_v2_non_water.md').write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT_DIR / 'table2_v2_non_water.md'}")


# ──────────────────────────────────────────────────────────────────────
# MODULE: sparse — climate adaptation, pollution control, natural resource
#                   (LPM + Fisher exact test for separation concerns)
# ──────────────────────────────────────────────────────────────────────
if MODULE in ('sparse', 'all'):
    print("=== Table 2 — Sparse categories (LPM + Fisher exact) ===\n")

    sparse_specs = []
    Y = 'Y_climate_adapt'
    if Y in df.columns:
        extras = [v for v in ['nfip_total_losses_asinh_lag2',
                               'fema_disaster_flood_lag2',
                               'nri_inland_flooding_eal_bv',
                               'fema_resil_grant_amt_asinh_lag1']
                  if v in df.columns]
        sparse_specs.append(('T5 Climate Adapt',  Y, SHARED_RHS + extras,
                             'NFIP + FEMA flood + NRI inland EAL + FEMA resil grant', extras))

    Y = 'Y_Pollution_Control'
    if Y in df.columns:
        extras = [v for v in ['epa_water_violations_asinh_lag2',
                               'epa_npdes_informal_asinh_lag2',
                               'caa_any_criteria_nonattainment_lag1',
                               'rcra_violations_count_muni']
                  if v in df.columns]
        sparse_specs.append(('T6 Pollution Control', Y, SHARED_RHS + extras,
                             'EPA violations + informal + CAA any-criteria + RCRA', extras))

    Y = 'Y_natural_resource'
    if Y in df.columns:
        extras = [v for v in ['nri_overall_risk_score',
                               'nri_water_risk_score']
                  if v in df.columns]
        sparse_specs.append(('T7 Natural Resource', Y, SHARED_RHS + extras,
                             'NRI overall + water risk', extras))

    results = []
    for label, y, xs, note, extras in sparse_specs:
        npos = int(df[y].fillna(0).sum())
        res, n = fit_ols(df, y, xs)
        # Fisher on Dem_Mayor too
        p_f, rate_d, rate_r = fisher_on_party(df, y, 'Dem_Mayor')
        results.append((label, y, xs, note, res, n, npos, extras, p_f, rate_d, rate_r))
        if res is None:
            print(f"  {label:22s}  n_pos={npos}  LPM failed.  Fisher: "
                  f"Dem={rate_d:.1%} Rep/Ind={rate_r:.1%}, p={p_f:.3f}"); continue
        b, se, p = coef(res, 'Dem_Mayor')
        print(f"  {label:22s}  n={n:4d}  n_pos={npos:3d}  "
              f"β(Dem_Mayor)={b:+.4f}{stars(p)} (se={se:.4f})  "
              f"Fisher: Dem={rate_d:.1%} Rep={rate_r:.1%}, p={p_f:.3f}")
        for v in extras:
            bb, ss, pp = coef(res, v)
            if not np.isnan(bb):
                print(f"           β({v:40s})={bb:+.4f}{stars(pp)} (se={ss:.4f})")

    # Write md
    focus = ['Dem_Mayor', 'pres_dem_two_party_share_lag2',
             'nfip_total_losses_asinh_lag2', 'fema_disaster_flood_lag2',
             'nri_inland_flooding_eal_bv', 'fema_resil_grant_amt_asinh_lag1',
             'epa_water_violations_asinh_lag2', 'epa_npdes_informal_asinh_lag2',
             'caa_any_criteria_nonattainment_lag1', 'rcra_violations_count_muni',
             'nri_overall_risk_score', 'nri_water_risk_score']
    lines = ['# Table 2 — Sparse categories (climate adapt, pollution control, natural resource)',
             '', 'LPM + Fisher exact test. Primary treatment `Dem_Mayor`.',
             'Categories have low positive counts (3-9), so coefficients are imprecise',
             'and Fisher exact p-values are more informative.', '', '']
    lines.append('| Variable | ' + ' | '.join(f'{lbl}<br>{y}' for (lbl, y, *_) in results) + ' |')
    lines.append('|---' + '|---' * len(results) + '|')
    for v in focus:
        cells = []
        for (_, _, _, _, res, _, _, _, _, _, _) in results:
            cells.append(fmt(*coef(res, v)))
        lines.append(f'| `{v}` | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, _, _, n, _, _, _, _, _) in results) + ' |')
    lines.append('| n_pos | ' + ' | '.join(str(p) for (_, _, _, _, _, _, p, _, _, _, _) in results) + ' |')
    lines.append('| Fisher Dem rate | ' + ' | '.join(f'{r:.1%}' for (_, _, _, _, _, _, _, _, _, r, _) in results) + ' |')
    lines.append('| Fisher Rep rate | ' + ' | '.join(f'{r:.1%}' for (_, _, _, _, _, _, _, _, _, _, r) in results) + ' |')
    lines.append('| Fisher p-value | ' + ' | '.join(f'{p:.3f}' if not np.isnan(p) else '—' for (_, _, _, _, _, _, _, _, p, _, _) in results) + ' |')
    lines.append('')
    lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01.')
    (OUT_DIR / 'table2_v2_sparse.md').write_text('\n'.join(lines) + '\n')
    print(f"\nWrote: {OUT_DIR / 'table2_v2_sparse.md'}")


# ──────────────────────────────────────────────────────────────────────
# MODULE: stacked — H2a monotonicity test via Dem_Mayor × compulsion ordinal
# ──────────────────────────────────────────────────────────────────────
if MODULE in ('stacked', 'all'):
    print("=== Table 2 Col 9 — Stacked monotonicity (H2a) ===\n")

    # Compulsion ordinal: 4 = fully compelled → 0 = no compulsion.
    # Mapping reflects memo §Table 2 compulsion gradient theory.
    compulsion_ord = {
        'Y_water_only':                4,  # fully compelled (NPDES + CWA)
        'Y_Pollution_Control':         3,  # EPA enforcement
        'Y_Clean_Transportation':      3,  # CAA + ADA/NEPA federal match
        'Y_Renewable_Energy':          2,  # RPS at muni-electric subsample
        'Y_Climate_Change_Adaptation': 2,  # NFIP/FEMA + CWA
        'Y_Energy_Efficiency':         1,  # weak (IECC + state EERS)
        'Y_Green_Buildings':           0,  # no federal compulsion
        'Y_natural_resource':          0,  # no compulsion
    }

    # Build stacked panel: one row per (city, year, category).
    stack_frames = []
    for y, ord_val in compulsion_ord.items():
        if y not in df.columns:
            continue
        sub = df[['fips7', 'year', 'state_id', 'state_abb', y] + SHARED_RHS].copy()
        sub = sub.rename(columns={y: 'Y_stack'})
        sub['compulsion_ord'] = ord_val
        sub['cat'] = y
        stack_frames.append(sub)
    stacked = pd.concat(stack_frames, ignore_index=True)

    # Dem_Mayor × compulsion_ord interaction. H2a: partisan gap INCREASES
    # as compulsion DECREASES. Under the Dem_Mayor coding, the expected
    # sign on the interaction is NEGATIVE:
    #    β(Dem_Mayor × compulsion_ord) < 0
    # means the Dem advantage shrinks with compulsion.
    stacked['dem_x_compulsion_ord'] = stacked['Dem_Mayor'] * stacked['compulsion_ord']
    # Category fixed effects
    cat_dums = pd.get_dummies(stacked['cat'], prefix='cat', drop_first=True, dtype=float)
    stacked = pd.concat([stacked, cat_dums], axis=1)

    stacked_xs = SHARED_RHS + ['compulsion_ord', 'dem_x_compulsion_ord'] + list(cat_dums.columns)
    res_stack, n_stack = fit_ols(stacked, 'Y_stack', stacked_xs)
    if res_stack is not None:
        b_dem, se_dem, p_dem = coef(res_stack, 'Dem_Mayor')
        b_ord, se_ord, p_ord = coef(res_stack, 'compulsion_ord')
        b_int, se_int, p_int = coef(res_stack, 'dem_x_compulsion_ord')
        print(f"  Stacked N={n_stack:,}")
        print(f"  β(Dem_Mayor)                     = {b_dem:+.4f}{stars(p_dem)} (se={se_dem:.4f})")
        print(f"  β(compulsion_ord)                = {b_ord:+.4f}{stars(p_ord)} (se={se_ord:.4f})")
        print(f"  β(Dem_Mayor × compulsion_ord)    = {b_int:+.4f}{stars(p_int)} (se={se_int:.4f})")
        print(f"  H2a prediction: interaction sign NEGATIVE (Dem advantage shrinks with compulsion)")

        # Additional robustness: replace ordinal with binary (compelled vs discretionary)
        stacked['is_compelled'] = (stacked['compulsion_ord'] >= 3).astype(int)
        stacked['dem_x_compelled'] = stacked['Dem_Mayor'] * stacked['is_compelled']
        stacked_xs_bin = SHARED_RHS + ['is_compelled', 'dem_x_compelled'] + list(cat_dums.columns)
        res_bin, n_bin = fit_ols(stacked, 'Y_stack', stacked_xs_bin)
        if res_bin is not None:
            b_b, se_b, p_b = coef(res_bin, 'dem_x_compelled')
            print(f"\n  Binary-compelled variant:")
            print(f"  β(Dem_Mayor × is_compelled)      = {b_b:+.4f}{stars(p_b)} (se={se_b:.4f})")

        # Write md
        lines = ['# Table 2 Col 9 — Stacked Monotonicity (H2a)', '',
                 f'Stacked panel across 8 use-of-proceeds categories, N = {n_stack:,}.',
                 'Category fixed effects included. State + year FE. State clustering.', '',
                 'Compulsion ordinal: water=4, pollution/transport=3, renew/adapt=2, ',
                 'energy-eff=1, green-bldg/natural-res=0.', '',
                 'H2a prediction (with `Dem_Mayor` coding): interaction is **negative** —',
                 'the Democratic advantage should shrink in highly-compelled categories.', '',
                 '| Variable | Coefficient |',
                 '|---|---|',
                 f'| `Dem_Mayor` | {fmt(b_dem, se_dem, p_dem)} |',
                 f'| `compulsion_ord` | {fmt(b_ord, se_ord, p_ord)} |',
                 f'| `Dem_Mayor × compulsion_ord` | **{fmt(b_int, se_int, p_int)}** |',
                 f'| N | {n_stack:,} |',
                 f'| R² | {res_stack.rsquared:.4f} |',
                 '']
        if res_bin is not None:
            b_bin_dem, _, _ = coef(res_bin, 'Dem_Mayor')
            b_bin_comp, _, _ = coef(res_bin, 'is_compelled')
            lines.extend([
                '## Binary-compelled variant',
                '',
                '| Variable | Coefficient |',
                '|---|---|',
                f'| `Dem_Mayor` | {fmt(b_bin_dem, 0, 1)} |',
                f'| `is_compelled` (ord ≥ 3) | {fmt(b_bin_comp, 0, 1)} |',
                f'| `Dem_Mayor × is_compelled` | **{fmt(b_b, se_b, p_b)}** |',
                f'| N | {n_bin:,} |',
                ''
            ])
        lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01.')
        (OUT_DIR / 'table2_v2_stacked.md').write_text('\n'.join(lines) + '\n')
        print(f"\nWrote: {OUT_DIR / 'table2_v2_stacked.md'}")
