"""
Task 7: Constituency decomposition (pres_dem_share vs Dem_Mayor)
================================================================
Two outputs:
  1. Scatter of pres_dem_two_party_share_lag2 vs Dem_Mayor (jittered)
     with LOESS overlay, colored by Census region.
  2. Three variants of C3 (Y_self_green):
     V1: pres_dem_share only (no Dem_Mayor)
     V2: Dem_Mayor only (no pres_dem_share)
     V3: both + interaction

Run: TABLE1_MODULE=constituency_decomp python3 pipeline/analysis_table1_v3.py
  or: python3 pipeline/analysis_table1_v3.py  (with MODULE set)
"""
import os, sys, warnings
from pathlib import Path
import numpy as np, pandas as pd, statsmodels.api as sm

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import stars

ROOT = Path(__file__).resolve().parent.parent
OUT_T = ROOT / 'processed' / 'tables' / 'v3_rr'
OUT_F = ROOT / 'processed' / 'figures' / 'v3_rr'
OUT_T.mkdir(parents=True, exist_ok=True)
OUT_F.mkdir(parents=True, exist_ok=True)

PRIMARY = [
    'Dem_Mayor', 'pres_dem_two_party_share_lag2',
    'qncr_nonsevere_asinh_lag1',
    'reserve_ratio_lag2', 'debt_service_burden_lag2',
    'state_dem_governor_lag1',
    'esg_has_antiesg_law_lag1', 'asinh_state_all_green_cum_amt_lag1',
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
            X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
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

# ── Load ──
df = pd.read_pickle(ROOT / 'processed' / 'panel' / 'panel.pkl')
print(f"Panel: {df.shape}")

# ── 1. Scatter plot ──
print("\n=== Scatter: pres_dem_share vs Dem_Mayor ===")

# Census region mapping from state_abb
REGION = {
    'CT':'Northeast','ME':'Northeast','MA':'Northeast','NH':'Northeast',
    'RI':'Northeast','VT':'Northeast','NJ':'Northeast','NY':'Northeast','PA':'Northeast',
    'IL':'Midwest','IN':'Midwest','MI':'Midwest','OH':'Midwest','WI':'Midwest',
    'IA':'Midwest','KS':'Midwest','MN':'Midwest','MO':'Midwest','NE':'Midwest',
    'ND':'Midwest','SD':'Midwest',
    'DE':'South','FL':'South','GA':'South','MD':'South','NC':'South',
    'SC':'South','VA':'South','WV':'South','AL':'South','KY':'South',
    'MS':'South','TN':'South','AR':'South','LA':'South','OK':'South','TX':'South','DC':'South',
    'AZ':'West','CO':'West','ID':'West','MT':'West','NV':'West','NM':'West',
    'UT':'West','WY':'West','AK':'West','CA':'West','HI':'West','OR':'West','WA':'West',
}

plot_df = df[['fips7','Dem_Mayor','pres_dem_two_party_share_lag2','state_abb']].dropna().copy()
plot_df['region'] = plot_df['state_abb'].map(REGION).fillna('Other')
# Jitter Dem_Mayor for visibility
np.random.seed(42)
plot_df['Dem_Mayor_jittered'] = plot_df['Dem_Mayor'] + np.random.uniform(-0.08, 0.08, len(plot_df))

# Discordant counts
disc_dem_in_rep_city = int(((plot_df['pres_dem_two_party_share_lag2'] > 0.55) &
                            (plot_df['Dem_Mayor'] == 0)).sum())
disc_rep_in_dem_city = int(((plot_df['pres_dem_two_party_share_lag2'] < 0.45) &
                            (plot_df['Dem_Mayor'] == 1)).sum())
total = len(plot_df)
print(f"  Discordant city-years:")
print(f"    pres_dem > 0.55 but Dem_Mayor = 0 (Rep mayor in blue city): {disc_dem_in_rep_city} ({disc_dem_in_rep_city/total:.1%})")
print(f"    pres_dem < 0.45 but Dem_Mayor = 1 (Dem mayor in red city):  {disc_rep_in_dem_city} ({disc_rep_in_dem_city/total:.1%})")

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = {'Northeast': '#1f77b4', 'Midwest': '#ff7f0e', 'South': '#2ca02c', 'West': '#d62728'}
    for region, color in colors.items():
        sub = plot_df[plot_df['region'] == region]
        ax.scatter(sub['pres_dem_two_party_share_lag2'], sub['Dem_Mayor_jittered'],
                   alpha=0.15, s=8, c=color, label=region)
    # LOESS overlay
    try:
        from statsmodels.nonparametric.smoothers_lowess import lowess
        lo = lowess(plot_df['Dem_Mayor'], plot_df['pres_dem_two_party_share_lag2'],
                    frac=0.3, return_sorted=True)
        ax.plot(lo[:, 0], lo[:, 1], 'k-', linewidth=2, label='LOESS')
    except Exception:
        pass
    ax.set_xlabel('Presidential Dem Two-Party Share (lag 2)')
    ax.set_ylabel('Dem_Mayor (jittered)')
    ax.set_title('Constituency vs Mayoral Partisanship')
    ax.legend(fontsize=8, loc='lower right')
    ax.axhline(0.5, color='gray', linestyle='--', alpha=0.3)
    ax.axvline(0.5, color='gray', linestyle='--', alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_F / 'pres_vs_mayor_scatter.png', dpi=150)
    plt.close()
    print(f"  Saved: {OUT_F / 'pres_vs_mayor_scatter.png'}")
except ImportError:
    print("  [skip] matplotlib not available for scatter plot")

# ── 2. Three regression variants ──
print("\n=== Constituency decomposition regressions ===")

Y = 'Y_self_green'

# V1: pres_dem only (no Dem_Mayor)
rhs_v1 = [v for v in PRIMARY if v != 'Dem_Mayor']
res_v1, n_v1 = fit(df, Y, rhs_v1)
b_pres_v1, se_pres_v1, p_pres_v1 = c(res_v1, 'pres_dem_two_party_share_lag2')
print(f"  V1 (pres only):  β(pres_dem)={b_pres_v1:+.4f}{stars(p_pres_v1)} (se={se_pres_v1:.4f})  N={n_v1}")

# V2: Dem_Mayor only (no pres_dem)
rhs_v2 = [v for v in PRIMARY if v != 'pres_dem_two_party_share_lag2']
res_v2, n_v2 = fit(df, Y, rhs_v2)
b_dem_v2, se_dem_v2, p_dem_v2 = c(res_v2, 'Dem_Mayor')
print(f"  V2 (Dem only):   β(Dem_Mayor)={b_dem_v2:+.4f}{stars(p_dem_v2)} (se={se_dem_v2:.4f})  N={n_v2}")

# V3: both + interaction
df['dem_x_pres_dem'] = df['Dem_Mayor'] * df['pres_dem_two_party_share_lag2']
rhs_v3 = PRIMARY + ['dem_x_pres_dem']
res_v3, n_v3 = fit(df, Y, rhs_v3)
b_dem_v3, se_dem_v3, p_dem_v3 = c(res_v3, 'Dem_Mayor')
b_pres_v3, se_pres_v3, p_pres_v3 = c(res_v3, 'pres_dem_two_party_share_lag2')
b_int_v3, se_int_v3, p_int_v3 = c(res_v3, 'dem_x_pres_dem')
print(f"  V3 (both+int):   β(Dem_Mayor)={b_dem_v3:+.4f}{stars(p_dem_v3)}  "
      f"β(pres_dem)={b_pres_v3:+.4f}{stars(p_pres_v3)}  "
      f"β(interaction)={b_int_v3:+.4f}{stars(p_int_v3)}  N={n_v3}")

# Also report C3 baseline for comparison
res_c3, n_c3 = fit(df, Y, PRIMARY)
b_dem_c3, se_dem_c3, p_dem_c3 = c(res_c3, 'Dem_Mayor')
b_pres_c3, se_pres_c3, p_pres_c3 = c(res_c3, 'pres_dem_two_party_share_lag2')
print(f"  C3 baseline:     β(Dem_Mayor)={b_dem_c3:+.4f}{stars(p_dem_c3)}  "
      f"β(pres_dem)={b_pres_c3:+.4f}{stars(p_pres_c3)}  N={n_c3}")

# ── Write output ──
lines = [
    '# Constituency Decomposition: `pres_dem_share` vs `Dem_Mayor` (Task 7)',
    '',
    '## Discordant city-years',
    '',
    f'- `pres_dem > 0.55` but `Dem_Mayor = 0` (Rep mayor in blue city): '
    f'**{disc_dem_in_rep_city}** ({disc_dem_in_rep_city/total:.1%})',
    f'- `pres_dem < 0.45` but `Dem_Mayor = 1` (Dem mayor in red city): '
    f'**{disc_rep_in_dem_city}** ({disc_rep_in_dem_city/total:.1%})',
    f'- Total city-years with both non-null: {total}',
    '',
    'See `processed/figures/v3_rr/pres_vs_mayor_scatter.png` for the scatter.',
    '',
    '## Regression comparison on `Y_self_green`',
    '',
    '| Variant | β(Dem_Mayor) | SE | p | β(pres_dem_share) | SE | p | β(interaction) | SE | p | N |',
    '|---|---|---|---|---|---|---|---|---|---|---|',
    f'| V1 (pres only) | — | — | — | {fmt(b_pres_v1, se_pres_v1, p_pres_v1)} | | | — | — | — | {n_v1} |',
    f'| V2 (Dem only) | {fmt(b_dem_v2, se_dem_v2, p_dem_v2)} | | | — | — | — | — | — | — | {n_v2} |',
    f'| C3 baseline | {fmt(b_dem_c3, se_dem_c3, p_dem_c3)} | | | {fmt(b_pres_c3, se_pres_c3, p_pres_c3)} | | | — | — | — | {n_c3} |',
    f'| V3 (both+int) | {fmt(b_dem_v3, se_dem_v3, p_dem_v3)} | | | {fmt(b_pres_v3, se_pres_v3, p_pres_v3)} | | | {fmt(b_int_v3, se_int_v3, p_int_v3)} | | | {n_v3} |',
    '',
    '## Reading',
    '',
]
# Automated reading
int_null = p_int_v3 > 0.10 if not np.isnan(p_int_v3) else True
pres_stable = (abs(b_pres_v1 - b_pres_v3) / max(abs(b_pres_v1), 1e-8)) < 0.30 if not np.isnan(b_pres_v1) else False

lines.append(f'- **Interaction null:** {"Yes" if int_null else "No"} '
             f'(β = {b_int_v3:+.4f}, p = {p_int_v3:.3f}). '
             f'{"The interaction is null, meaning `pres_dem_share` and `Dem_Mayor` operate independently." if int_null else "The interaction is significant — the two variables do NOT operate independently."}')
lines.append(f'- **`pres_dem_share` coefficient stability:** V1 β = {b_pres_v1:+.4f}, '
             f'V3 β = {b_pres_v3:+.4f}. '
             f'{"Stable (< 30% change) — constituency operates independently of mayoral partisanship." if pres_stable else "Unstable — adding the interaction changes the constituency coefficient materially."}')
lines.append(f'- **`Dem_Mayor` in V2 (without pres_dem):** β = {b_dem_v2:+.4f} (p = {p_dem_v2:.3f}). '
             f'{"Still null even without the constituency control — mayoral partisanship has no marginal effect." if p_dem_v2 > 0.10 else "Becomes significant without the constituency control — some of the constituency effect operates through mayoral identity."}')

lines.extend(['', '* p<0.10, ** p<0.05, *** p<0.01.'])
(OUT_T / 'constituency_decomposition.md').write_text('\n'.join(lines) + '\n')
print(f"\nWrote: {OUT_T / 'constituency_decomposition.md'}")
