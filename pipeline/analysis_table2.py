"""
analysis_table2.py — Table 2: The Compositional Gap & Compulsion Gradient
==========================================================================
Tests H2a: the partisan gap in green bond participation increases monotonically
as external compulsion decreases across use-of-proceeds categories.

Structure (8 outcome columns):
  Col 1  Y_water_only                [fully compelled — Rep_Mayor null]
  Col 2  Y_Clean_Transportation      [moderately compelled — Rep_Mayor -]
  Col 3  Y_Renewable_Energy          [partial compulsion via muni-electric]
  Col 4  Y_Energy_Efficiency         [weakly compelled — likely separation]
  Col 5  Y_Green_Buildings           [weakly compelled — likely separation]
  Col 6  Y_Climate_Change_Adaptation [new §4.2]
  Col 7  Y_Pollution_Control         [new §4.2]
  Col 8  Y_natural_resource          [new §4.2]
  Col 9  Stacked with Rep_Mayor × compulsion ordinal [single monotonicity test]

Each column shares the three-family RHS but adds category-specific predictors
from VARIABLE_ADDITIONS_SPEC.md (§1.1–§1.6):
  - Water:     epa_water_violations_asinh_lag2 + epa_npdes_informal_asinh_lag2
  - Clean tr:  iija_transit_grant_amt_asinh_lag1 + fn_pct_deficient_lag2
  - Renewabl.: ep_muni_electric_rev_asinh_lag1 + state_rggi_member_lag1
                + state_rps_target_pct_lag1
  - Eng eff:   bcode_state_bps_adopted_lag1 + ep_state_aceee_code_rank_lag1
                + state_carbon_pricing_lag1
  - Green bd.: bcode_state_bps_adopted_lag1 + bcode_iecc_lag_yrs_lag1
  - Climate:   nfip_total_losses_asinh_lag2 + fema_disaster_flood_lag2
                + nri_inland_flooding_eal_bv
  - Pollut:    epa_water_violations_asinh_lag2
  - Natural:   nri_overall_risk_score

Specification: LPM, state + year FE, cluster SE on FIPS. Firth logit not
attempted here — where the column has complete separation we log and move
on. Descriptive Fisher exacts reported alongside.
"""
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


def fit_ols(df, y, xs, fe=('state_id', 'year')):
    cols = ['fips7'] + list(fe) + [y] + xs
    d = df[[c for c in cols if c in df.columns]].copy()
    d = d.dropna(subset=[y] + [x for x in xs if x in d.columns])
    if len(d) < 30:
        return None, 0
    # Drop zero-variance columns to avoid rank issues in sparse categories.
    xs_live = [x for x in xs if x in d.columns and d[x].nunique(dropna=True) > 1]
    if not xs_live:
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
            cov_type='cluster', cov_kwds={'groups': d['fips7'].values})
        res._xnames = list(X.columns)
        return res, len(d)
    except Exception as e:
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
    return f'{b:+.3f}{stars(p)} ({se:.3f})'


# ──────────────────────────────────────────────────────────────────────
# Load panel and stage variables
# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel loaded: {df.shape}")

if 'Rep_Mayor_lag1' not in df.columns and 'Rep_Mayor_L1' in df.columns:
    df['Rep_Mayor_lag1'] = df['Rep_Mayor_L1']
if 'Ind_Mayor_lag1' not in df.columns and 'Ind_Mayor_L1' in df.columns:
    df['Ind_Mayor_lag1'] = df['Ind_Mayor_L1']

for tgt, cands in [
    ('npdes_formal_prior3yr_muni',
     ['npdes_formal_any_muni_prior3yr', 'npdes_formal_prior3yr_muni']),
    ('overflow_events_lag2', ['overflow_events_lag2', 'overflow_events_muni_lag2']),
]:
    if tgt not in df.columns:
        for c in cands:
            if c in df.columns:
                df[tgt] = df[c]
                break


# ──────────────────────────────────────────────────────────────────────
# Three-family RHS (shared across columns)
# ──────────────────────────────────────────────────────────────────────
RHS = [v for v in [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'debt_service_burden_lag2', 'tel_stringency_normalized',
    'log_cwsrf_obligations_lag2',
    'state_rep_trifecta', 'esg_has_muni_bond_law', 'state_green_bond_ever_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2', 'has_substitute_issuer',
] if v in df.columns]
print(f"Shared RHS: {len(RHS)} vars")


# Category-specific compulsion predictors from the spec.
CATEGORY_EXTRAS = {
    'Y_water_only': [
        'epa_water_violations_asinh_lag2',
        'epa_npdes_informal_asinh_lag2',
    ],
    'Y_Clean_Transportation': [
        'iija_transit_grant_amt_asinh_lag1',
        'fn_pct_deficient_lag2',
    ],
    'Y_Renewable_Energy': [
        'ep_muni_electric_rev_asinh_lag1',
        'ep_has_muni_electric_lag1',
        'state_rggi_member_lag1',
        'state_rps_target_pct_lag1',
    ],
    'Y_Energy_Efficiency': [
        'bcode_state_bps_adopted_lag1',
        'ep_state_aceee_code_rank_lag1',
        'state_carbon_pricing_lag1',
        'ira_eecbg_grant_amt_asinh_lag1',
    ],
    'Y_Green_Buildings': [
        'bcode_state_bps_adopted_lag1',
        'bcode_iecc_lag_yrs_lag1',
        'bcode_state_weakening_amendments_lag1',
        'ira_ggrf_grant_amt_asinh_lag1',
    ],
    'Y_Climate_Change_Adaptation': [
        'nfip_total_losses_asinh_lag2',
        'fema_disaster_flood_lag2',
        'nri_inland_flooding_eal_bv',
        'fema_resil_grant_amt_asinh_lag1',
    ],
    'Y_Pollution_Control': [
        'epa_water_violations_asinh_lag2',
        'epa_npdes_informal_asinh_lag2',
    ],
    'Y_natural_resource': [
        'nri_overall_risk_score',
    ],
}


# ──────────────────────────────────────────────────────────────────────
# Run per-category columns
# ──────────────────────────────────────────────────────────────────────
print("\n=== Table 2: category-by-category ===\n")
col_specs = list(CATEGORY_EXTRAS.keys())

results = []
for y in col_specs:
    if y not in df.columns:
        print(f"  [skip] {y}: outcome missing")
        continue
    # Positive count / sample diagnostic first.
    npos = int(df[y].fillna(0).sum())
    # Restrict renewables to municipal electric subsample per memo.
    d = df
    note = ''
    if y == 'Y_Renewable_Energy' and 'ep_has_muni_electric' in df.columns:
        d = df[df['ep_has_muni_electric'] == 1].copy()
        note = f' (muni-electric subsample, n_cities={d["fips7"].nunique()})'
    xs = RHS + [v for v in CATEGORY_EXTRAS[y] if v in d.columns]
    res, n = fit_ols(d, y, xs)
    results.append((y, res, n, npos, xs, note))
    if res is None:
        # Fisher exact against Rep_Mayor_lag1 alone.
        mask = d['Rep_Mayor_lag1'].notna() & d[y].notna()
        tab = pd.crosstab(d.loc[mask, 'Rep_Mayor_lag1'], d.loc[mask, y])
        if tab.shape == (2, 2):
            _, p_f = fisher_exact(tab)
            print(f"  {y:30s}  n_pos={npos:3d}  regression failed; Fisher p={p_f:.3f}{note}")
        else:
            print(f"  {y:30s}  n_pos={npos:3d}  regression failed (separation){note}")
        continue
    b, se, p = coef(res, 'Rep_Mayor_lag1')
    # Gather category-extra diagnostic coefficients.
    extras = []
    for v in CATEGORY_EXTRAS[y]:
        if v not in xs:
            continue
        bb, ss, pp = coef(res, v)
        if not np.isnan(bb):
            extras.append(f'{v.split("_")[0][:8]}={bb:+.2f}{stars(pp)}')
    print(f"  {y:30s}  n={n:4d}  n_pos={npos:3d}  "
          f"β(Rep_Mayor_lag1)={b:+.3f}{stars(p)} (se={se:.3f})"
          f"{note}   {'; '.join(extras) if extras else ''}")


# ──────────────────────────────────────────────────────────────────────
# Col 9: Stacked regression with Rep_Mayor × compulsion-ordinal interaction
# ──────────────────────────────────────────────────────────────────────
print("\n=== Table 2 Col 9: Stacked monotonicity test ===")

# Compulsion ordinal mapping: high (water) = 4, low (green building) = 0.
compulsion_ord = {
    'Y_water_only': 4,
    'Y_Pollution_Control': 3,
    'Y_Clean_Transportation': 3,
    'Y_Renewable_Energy': 2,
    'Y_Climate_Change_Adaptation': 2,
    'Y_Energy_Efficiency': 1,
    'Y_Green_Buildings': 0,
    'Y_natural_resource': 0,
}
stack_frames = []
for y, ord_val in compulsion_ord.items():
    if y not in df.columns:
        continue
    sub = df[['fips7', 'year', 'state_id', y] + RHS].copy()
    sub['Y_stack'] = sub[y]
    sub['compulsion_ord'] = ord_val
    sub['cat'] = y
    stack_frames.append(sub.drop(columns=y))

stacked = pd.concat(stack_frames, ignore_index=True)
stacked['rep_x_compulsion'] = stacked['Rep_Mayor_lag1'] * stacked['compulsion_ord']

stacked_xs = RHS + ['compulsion_ord', 'rep_x_compulsion']
# Include category fixed effects in the stacked model.
cat_dums = pd.get_dummies(stacked['cat'], prefix='cat', drop_first=True, dtype=float)
stacked = pd.concat([stacked, cat_dums], axis=1)
stacked_xs += list(cat_dums.columns)

res_stack, n_stack = fit_ols(stacked, 'Y_stack', stacked_xs)
b_int, se_int, p_int = coef(res_stack, 'rep_x_compulsion')
b_ord, se_ord, p_ord = coef(res_stack, 'compulsion_ord')
b_rep, se_rep, p_rep = coef(res_stack, 'Rep_Mayor_lag1')
print(f"  N={n_stack}")
print(f"  β(Rep_Mayor_lag1)       ={b_rep:+.4f}{stars(p_rep)} (se={se_rep:.4f})")
print(f"  β(compulsion_ord)       ={b_ord:+.4f}{stars(p_ord)} (se={se_ord:.4f})")
print(f"  β(Rep × compulsion_ord) ={b_int:+.4f}{stars(p_int)} (se={se_int:.4f})  "
      f"[H2a: expected positive — compulsion compresses the gap]")


# ──────────────────────────────────────────────────────────────────────
# Write outputs
# ──────────────────────────────────────────────────────────────────────
# Markdown summary
md_lines = ['# Table 2 — Compositional Gap & Compulsion Gradient', '']
md_lines.append('| Outcome | N | n_pos | β(Rep_Mayor_lag1) | Notes |')
md_lines.append('|---|---|---|---|---|')
for (y, res, n, npos, xs, note) in results:
    b, se, p = coef(res, 'Rep_Mayor_lag1')
    if res is None:
        row = f'| {y} | — | {npos} | fit failed | {note} |'
    else:
        row = f'| {y} | {n} | {npos} | {b:+.3f}{stars(p)} ({se:.3f}) | {note} |'
    md_lines.append(row)
md_lines.append('')
md_lines.append('## Col 9 — Stacked monotonicity test')
md_lines.append('')
md_lines.append(f'- **N** = {n_stack}')
md_lines.append(f'- **β(Rep_Mayor_lag1)** = {b_rep:+.4f}{stars(p_rep)} (se {se_rep:.4f})')
md_lines.append(f'- **β(compulsion_ord)** = {b_ord:+.4f}{stars(p_ord)} (se {se_ord:.4f})')
md_lines.append(f'- **β(Rep × compulsion_ord)** = {b_int:+.4f}{stars(p_int)} (se {se_int:.4f}) — '
                'H2a: expected **positive** (compulsion compresses the partisan gap).')
md_lines.append('')
md_lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01. Cluster-robust SE (FIPS). '
                'LPM + state + year FE.')

(OUT_DIR / 'table2_compulsion_gradient.md').write_text('\n'.join(md_lines) + '\n')

# Full coefficient CSV
rows = {'Variable': []}
cols_labels = [y for (y, *_) in results] + ['stacked']
for cl in cols_labels:
    rows[cl] = []
focus = [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'charges_to_own_source_lag2',
    'tel_stringency_normalized', 'log_cwsrf_obligations_lag2',
    'state_rep_trifecta', 'has_substitute_issuer',
    # Category-specific extras (union across columns)
    'epa_water_violations_asinh_lag2', 'epa_npdes_informal_asinh_lag2',
    'iija_transit_grant_amt_asinh_lag1', 'fn_pct_deficient_lag2',
    'ep_muni_electric_rev_asinh_lag1', 'ep_has_muni_electric_lag1',
    'state_rggi_member_lag1', 'state_rps_target_pct_lag1',
    'bcode_state_bps_adopted_lag1', 'bcode_iecc_lag_yrs_lag1',
    'bcode_state_weakening_amendments_lag1',
    'ep_state_aceee_code_rank_lag1', 'state_carbon_pricing_lag1',
    'ira_eecbg_grant_amt_asinh_lag1', 'ira_ggrf_grant_amt_asinh_lag1',
    'fema_resil_grant_amt_asinh_lag1',
    'nfip_total_losses_asinh_lag2', 'fema_disaster_flood_lag2',
    'nri_inland_flooding_eal_bv', 'nri_overall_risk_score',
    # Stacked-only
    'compulsion_ord', 'rep_x_compulsion',
]
for v in focus:
    rows['Variable'].append(v)
    for (y, res, *_) in results:
        b, se, p = coef(res, v)
        rows[y].append(fmt(b, se, p))
    b, se, p = coef(res_stack, v)
    rows['stacked'].append(fmt(b, se, p))
# Append N + R² rows (same length as Variable column)
rows['Variable'].append('N')
for (y, res, n, *_) in results:
    rows[y].append(str(n))
rows['stacked'].append(str(n_stack))
rows['Variable'].append('R²')
for (y, res, *_) in results:
    r2 = getattr(res, 'rsquared', float('nan')) if res is not None else float('nan')
    rows[y].append(f'{r2:.3f}' if not np.isnan(r2) else '—')
rows['stacked'].append(f'{res_stack.rsquared:.3f}' if res_stack is not None else '—')

pd.DataFrame(rows).to_csv(OUT_DIR / 'table2_compulsion_gradient.csv', index=False)

print(f"\nWrote: {OUT_DIR / 'table2_compulsion_gradient.md'}")
print(f"Wrote: {OUT_DIR / 'table2_compulsion_gradient.csv'}")
print(f"Wrote: {OUT_DIR / 'table2_Ns.csv'}")
