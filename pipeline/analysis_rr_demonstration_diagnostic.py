"""
analysis_rr_demonstration_diagnostic.py — Task 2: Demonstration interaction diagnostic
========================================================================================
Tests four candidate state-prior-issuance measures interacted with Dem_Mayor
on Y_self_green. For each measure, estimates (A) Dem_Mayor × measure only,
(B) Dem_Mayor × measure and Rep_Mayor × measure jointly. 8 regressions total.

Output: processed/tables/v3_rr/demonstration_diagnostic.md

Run: python3 pipeline/analysis_rr_demonstration_diagnostic.py
"""
import sys, warnings
from pathlib import Path
import numpy as np, pandas as pd, statsmodels.api as sm

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import stars

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'processed' / 'tables' / 'v3_rr'
OUT.mkdir(parents=True, exist_ok=True)

# ── Load and prepare ──
df = pd.read_pickle(ROOT / 'processed' / 'panel' / 'panel.pkl')
print(f"Panel: {df.shape}")

# Build missing measures
# M1: asinh_state_all_green_cum_amt_lag1 — already exists (all entities, continuous)

# M2: state_any_prior_green_issuance_lag1 — binary, any entity (all types) in state
# Maps to existing state_green_bond_ever_lag1
df['state_any_prior_green_issuance_lag1'] = df['state_green_bond_ever_lag1'].fillna(0).astype(int)

# M3: state_city_prior_green_issuance_lag1 — binary, city issuers only
# Maps to existing state_any_self_green_lag1 (which counts city self-green only)
df['state_city_prior_green_issuance_lag1'] = df['state_any_self_green_lag1'].fillna(0).astype(int)

# M4: state_city_count_prior_green_lag1 — count of distinct prior city issuers
# Build from panel: cumulative distinct fips7 with Y_self_green==1 per state through t-1
df_sorted = df.sort_values(['state_abb', 'year', 'fips7'])
# For each state-year, count distinct cities that have EVER self-labelled up to year t-1
issuer_first = df[df['Y_self_green'] == 1].groupby('fips7')['year'].min().reset_index()
issuer_first.columns = ['fips7', 'first_self_green_year']
issuer_first = issuer_first.merge(
    df[['fips7', 'state_abb']].drop_duplicates('fips7'), on='fips7', how='left')

state_yr_counts = []
for st in df['state_abb'].unique():
    st_issuers = issuer_first[issuer_first['state_abb'] == st]
    for yr in range(2013, 2026):
        n_prior = int((st_issuers['first_self_green_year'] < yr).sum())
        state_yr_counts.append({'state_abb': st, 'year': yr,
                                'state_city_count_prior_green_lag1': n_prior})
counts_df = pd.DataFrame(state_yr_counts)
df = df.merge(counts_df, on=['state_abb', 'year'], how='left', suffixes=('', '_NEW'))
if 'state_city_count_prior_green_lag1_NEW' in df.columns:
    df['state_city_count_prior_green_lag1'] = df['state_city_count_prior_green_lag1_NEW']
    df = df.drop(columns='state_city_count_prior_green_lag1_NEW')
df['state_city_count_prior_green_lag1'] = df['state_city_count_prior_green_lag1'].fillna(0).astype(int)

print(f"\nMeasure coverage:")
measures = [
    ('M1', 'asinh_state_all_green_cum_amt_lag1', 'Continuous cumulative $ (all entities, asinh)'),
    ('M2', 'state_any_prior_green_issuance_lag1', 'Binary: any entity in state'),
    ('M3', 'state_city_prior_green_issuance_lag1', 'Binary: any city self-labelled in state'),
    ('M4', 'state_city_count_prior_green_lag1', 'Count of distinct prior city issuers'),
]
for label, var, desc in measures:
    pos = int((df[var] > 0).sum())
    n_states_vary = df.groupby('state_abb')[var].nunique()
    n_states_with_var = int((n_states_vary > 1).sum())
    n_dem_pos = int(((df[var] > 0) & (df['Dem_Mayor'] == 1)).sum())
    n_rep_pos = int(((df[var] > 0) & (df['Dem_Mayor'] == 0)).sum())
    print(f"  {label} {var:45s}  pos={pos:>5}  states_with_variation={n_states_with_var:>3}  "
          f"Dem_pos={n_dem_pos:>5}  Rep_pos={n_rep_pos:>5}")

# ── Primary RHS (same as Table 1 v3) ──
PRIMARY = [
    'Dem_Mayor', 'pres_dem_two_party_share_lag2',
    'effluent_muni_asinh_lag2',
    'reserve_ratio_lag2', 'debt_service_burden_lag2',
    'state_dem_governor_lag1',
    'fn_esg_has_muni_bond_law_post_lag1', 'asinh_state_all_green_cum_amt_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2', 'unemployment_city_lag2',
]

def fit(df, y, xs, fe=('state_id','year'), cluster='fips7'):
    raw = ['fips7','state_id'] + list(fe) + [y] + xs
    seen, cols = set(), []
    for c in raw:
        if c in df.columns and c not in seen:
            cols.append(c); seen.add(c)
    d = df[cols].copy().dropna()
    xs_live = [x for x in xs if x in d.columns and d[x].nunique()>1]
    if len(d)<30 or not xs_live: return None, 0, 0
    X_parts = [d[xs_live].astype(float)]
    for f in fe:
        if f in d.columns and d[f].nunique()>1:
            X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
    X = pd.concat(X_parts, axis=1)
    X = sm.add_constant(X).astype(float)
    try:
        res = sm.OLS(d[y].values.astype(float), X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d[cluster].values})
        res._xnames = list(X.columns)
        return res, len(d), d['state_id'].nunique()
    except: return None, 0, 0

def c(res, name):
    if res is None: return np.nan, np.nan, np.nan, np.nan
    try:
        i = res._xnames.index(name)
        b, se, p = float(res.params[i]), float(res.bse[i]), float(res.pvalues[i])
        t = b / se if se > 0 else np.nan
        return b, se, t, p
    except: return np.nan, np.nan, np.nan, np.nan

# ── Run 8 regressions ──
print("\n" + "=" * 90)
print("DEMONSTRATION INTERACTION DIAGNOSTIC")
print("=" * 90)

Y = 'Y_self_green'
results = []

for mlabel, mvar, mdesc in measures:
    # Need Rep_Mayor_lag1 for spec B
    if 'Rep_Mayor_lag1' not in df.columns:
        df['Rep_Mayor_lag1'] = df.get('Rep_Mayor_L1', np.nan)

    # Build interactions
    dem_int = f'dem_x_{mvar}'
    rep_int = f'rep_x_{mvar}'
    df[dem_int] = df['Dem_Mayor'] * df[mvar]
    df[rep_int] = df['Rep_Mayor_lag1'] * df[mvar]

    # Measure variation stats
    n_states_vary = int((df.groupby('state_abb')[mvar].nunique() > 1).sum())
    n_dem_pos = int(((df[mvar] > 0) & (df['Dem_Mayor'] == 1)).sum())
    n_rep_pos = int(((df[mvar] > 0) & (df['Dem_Mayor'] == 0)).sum())

    # Spec A: Dem × measure only
    # For M1, mvar is already in PRIMARY (asinh_state_all_green_cum_amt_lag1)
    # For M2-M4, add mvar as main effect + interaction
    if mvar in PRIMARY:
        rhs_a = PRIMARY + [dem_int]
    else:
        rhs_a = PRIMARY + [mvar, dem_int]

    res_a, n_a, ns_a = fit(df, Y, rhs_a)
    b_a, se_a, t_a, p_a = c(res_a, dem_int)

    # Spec B: Dem × measure AND Rep × measure jointly
    if mvar in PRIMARY:
        rhs_b = PRIMARY + ['Rep_Mayor_lag1', dem_int, rep_int]
    else:
        rhs_b = PRIMARY + ['Rep_Mayor_lag1', mvar, dem_int, rep_int]

    res_b, n_b, ns_b = fit(df, Y, rhs_b)
    b_dem_b, se_dem_b, t_dem_b, p_dem_b = c(res_b, dem_int)
    b_rep_b, se_rep_b, t_rep_b, p_rep_b = c(res_b, rep_int)

    results.append({
        'measure': mlabel, 'var': mvar, 'desc': mdesc,
        'states_with_variation': n_states_vary,
        'dem_pos': n_dem_pos, 'rep_pos': n_rep_pos,
        # Spec A
        'A_b': b_a, 'A_se': se_a, 'A_t': t_a, 'A_p': p_a, 'A_n': n_a,
        # Spec B - Dem
        'B_dem_b': b_dem_b, 'B_dem_se': se_dem_b, 'B_dem_t': t_dem_b, 'B_dem_p': p_dem_b,
        # Spec B - Rep
        'B_rep_b': b_rep_b, 'B_rep_se': se_rep_b, 'B_rep_t': t_rep_b, 'B_rep_p': p_rep_b,
        'B_n': n_b,
    })

    print(f"\n  {mlabel}: {mvar}")
    print(f"    States with variation: {n_states_vary}  |  Dem-mayor obs where positive: {n_dem_pos}  |  Rep-mayor: {n_rep_pos}")
    print(f"    Spec A (Dem × measure only):     β={b_a:+.4f}  se={se_a:.4f}  t={t_a:+.2f}  p={p_a:.3f}{stars(p_a)}  N={n_a}")
    print(f"    Spec B (Dem × measure):          β={b_dem_b:+.4f}  se={se_dem_b:.4f}  t={t_dem_b:+.2f}  p={p_dem_b:.3f}{stars(p_dem_b)}")
    print(f"    Spec B (Rep × measure):          β={b_rep_b:+.4f}  se={se_rep_b:.4f}  t={t_rep_b:+.2f}  p={p_rep_b:.3f}{stars(p_rep_b)}  N={n_b}")

# ── Write output ──
lines = [
    '# Demonstration Interaction Diagnostic',
    '',
    'Tests four candidate state-prior-issuance measures interacted with mayoral',
    'partisanship on `Y_self_green`. Full baseline controls, state + year FE,',
    'city-clustered SEs.',
    '',
    '**Spec A:** `Dem_Mayor × [measure]` only.',
    '**Spec B:** `Dem_Mayor × [measure]` and `Rep_Mayor × [measure]` jointly.',
    '',
    '## Comparison table',
    '',
    '| Measure | Variable | States w/ variation | Dem-pos obs | Rep-pos obs | Spec | Party | β | SE | t | p | N |',
    '|---|---|---|---|---|---|---|---|---|---|---|---|',
]
for r in results:
    lines.append(
        f'| {r["measure"]} | `{r["var"]}` | {r["states_with_variation"]} | '
        f'{r["dem_pos"]} | {r["rep_pos"]} | A | Dem | '
        f'{r["A_b"]:+.4f}{stars(r["A_p"])} | {r["A_se"]:.4f} | {r["A_t"]:+.2f} | {r["A_p"]:.4f} | {r["A_n"]} |'
    )
    lines.append(
        f'| | | | | | B | Dem | '
        f'{r["B_dem_b"]:+.4f}{stars(r["B_dem_p"])} | {r["B_dem_se"]:.4f} | {r["B_dem_t"]:+.2f} | {r["B_dem_p"]:.4f} | {r["B_n"]} |'
    )
    lines.append(
        f'| | | | | | B | Rep | '
        f'{r["B_rep_b"]:+.4f}{stars(r["B_rep_p"])} | {r["B_rep_se"]:.4f} | {r["B_rep_t"]:+.2f} | {r["B_rep_p"]:.4f} | |'
    )

lines.extend([
    '',
    '## Reading',
    '',
])

# Automated reading flags
sig_a = [r for r in results if r['A_p'] < 0.10]
sig_b_dem = [r for r in results if r['B_dem_p'] < 0.10]
sig_b_rep = [r for r in results if r['B_rep_p'] < 0.10]
fragile = [r for r in results if r['states_with_variation'] < 15]

lines.append('### Which interactions reach p < 0.10?')
if sig_a:
    for r in sig_a:
        lines.append(f'- **Spec A {r["measure"]}:** Dem × `{r["var"]}` β = {r["A_b"]:+.4f}, p = {r["A_p"]:.4f} ({stars(r["A_p"])})')
else:
    lines.append('- None reach p < 0.10 in Spec A.')

if sig_b_dem:
    for r in sig_b_dem:
        lines.append(f'- **Spec B Dem {r["measure"]}:** β = {r["B_dem_b"]:+.4f}, p = {r["B_dem_p"]:.4f}')
if sig_b_rep:
    for r in sig_b_rep:
        lines.append(f'- **Spec B Rep {r["measure"]}:** β = {r["B_rep_b"]:+.4f}, p = {r["B_rep_p"]:.4f}')
if not sig_b_dem and not sig_b_rep:
    lines.append('- None reach p < 0.10 in Spec B.')

lines.append('')
lines.append('### Symmetry / asymmetry')
for r in results:
    if not np.isnan(r['B_dem_b']) and not np.isnan(r['B_rep_b']):
        same_sign = (r['B_dem_b'] > 0) == (r['B_rep_b'] > 0)
        ratio = r['B_dem_b'] / r['B_rep_b'] if abs(r['B_rep_b']) > 1e-8 else np.nan
        sym = 'symmetric' if same_sign and 0.5 < abs(ratio) < 2 else 'asymmetric'
        lines.append(f'- {r["measure"]}: Dem β = {r["B_dem_b"]:+.4f}, Rep β = {r["B_rep_b"]:+.4f} → **{sym}**')

lines.append('')
lines.append('### Fragility flags (< 15 contributing states)')
if fragile:
    for r in fragile:
        lines.append(f'- **{r["measure"]}:** only {r["states_with_variation"]} states with within-panel variation')
else:
    lines.append('- All measures have ≥ 15 contributing states.')

lines.append('')
lines.append('### Theoretically cleanest measure')
lines.append('')
lines.append('Not auto-selected. Review the table above and decide based on:')
lines.append('1. Statistical significance (p < 0.10 in both Spec A and B)')
lines.append('2. Number of contributing states (fragility)')
lines.append('3. Symmetry vs asymmetry of Dem/Rep interactions')
lines.append('4. Theoretical interpretability of the measure')
lines.append('')
lines.append('* p<0.10, ** p<0.05, *** p<0.01.')

(OUT / 'demonstration_diagnostic.md').write_text('\n'.join(lines) + '\n')
print(f"\nWrote: {OUT / 'demonstration_diagnostic.md'}")
