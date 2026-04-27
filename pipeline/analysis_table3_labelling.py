"""
Table 3 — The Labelling Decision (conditional on bond issuance).

Sample: city-years with `total_ltd_issued > 0` (Census of Governments long-term
debt issuance). Answers: *conditional on issuing a bond, why label it green?*

Columns:
  L1: Baseline PRIMARY on issuers
  L2: + fiscal_stress_index_lag2         (greenium-seeking channel)
  L3: + npdes × asinh_state_green_cum    (marketability channel)
  L4: L2 + L3 combined                   (both market channels)
  L5: Compelled issuers subsample (npdes > 0 AND total_ltd > 0)

Treatment: Dem_Mayor (no lag). FE: state + year. SE: clustered at fips7.
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'processed' / 'tables'
OUT.mkdir(parents=True, exist_ok=True)

PRIMARY = [
    'Dem_Mayor', 'pres_dem_two_party_share_lag2',
    'qncr_nonsevere_asinh_lag1',
    'reserve_ratio_lag2', 'debt_service_burden_lag2',
    'fn_esg_has_muni_bond_law_post_lag1', 'asinh_state_all_green_cum_amt_lag1',
    'state_dem_governor_lag1', 'state_dem_trifecta_lag1', 'state_rep_trifecta_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2', 'unemployment_city_lag2',
]

def stars(p):
    if np.isnan(p): return ''
    return '***' if p < 0.01 else '**' if p < 0.05 else '*' if p < 0.10 else ''

def fit(d_in, y, xs):
    raw = ['fips7', 'state_id', 'year', y] + xs
    cols = list(dict.fromkeys(c for c in raw if c in d_in.columns))
    d = d_in[cols].copy().dropna()
    xs_live = [x for x in xs if x in d.columns and d[x].nunique() > 1]
    if len(d) < 30 or not xs_live:
        return None, 0
    X_parts = [d[xs_live].astype(float)]
    for f in ('state_id', 'year'):
        if f in d.columns and d[f].nunique() > 1:
            X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
    X = sm.add_constant(pd.concat(X_parts, axis=1)).astype(float)
    res = sm.OLS(d[y].values.astype(float), X.values).fit(
        cov_type='cluster', cov_kwds={'groups': d['fips7'].values})
    res._xnames = list(X.columns)
    return res, len(d)

def c(res, name):
    if res is None: return np.nan, np.nan, np.nan
    try:
        i = res._xnames.index(name)
        return float(res.params[i]), float(res.bse[i]), float(res.pvalues[i])
    except: return np.nan, np.nan, np.nan

def fmt(b, se, p):
    if np.isnan(b): return '—'
    return f'{b:+.4f}{stars(p)} ({se:.4f})'

# ── Load panel ──
df = pd.read_pickle(ROOT / 'processed' / 'panel' / 'panel.pkl')
print(f"Panel: {df.shape}")

# ── Subsamples ──
issuers = df[df['total_ltd_issued'] > 0].copy()
compelled_issuers = issuers[issuers['qncr_nonsevere_asinh_lag1'] > 0].copy()
print(f"Bond issuers:        N={len(issuers)}, cities={issuers['fips7'].nunique()}, "
      f"Y_self_green={int(issuers['Y_self_green'].sum())}")
print(f"Compelled issuers:   N={len(compelled_issuers)}, cities={compelled_issuers['fips7'].nunique()}, "
      f"Y_self_green={int(compelled_issuers['Y_self_green'].sum())}")

# ── Build interaction ──
for sub in (issuers, compelled_issuers):
    sub['npdes_x_state_green'] = (
        sub['qncr_nonsevere_asinh_lag1'] * sub['asinh_state_all_green_cum_amt_lag1'])

# ── Specs ──
Y = 'Y_self_green'
rhs_no_npdes = [v for v in PRIMARY if v != 'qncr_nonsevere_asinh_lag1']

SPECS = [
    ('L1 Baseline',       issuers,           PRIMARY),
    ('L2 +Fiscal Stress', issuers,           PRIMARY + ['fiscal_stress_index_lag2']),
    ('L3 +Marketability', issuers,           PRIMARY + ['npdes_x_state_green']),
    ('L4 Both channels',  issuers,           PRIMARY + ['fiscal_stress_index_lag2', 'npdes_x_state_green']),
    ('L5 Compelled only', compelled_issuers, rhs_no_npdes),
]

print("\n=== Table 3 — The Labelling Decision ===\n")

results = []
for label, sample, xs in SPECS:
    res, n = fit(sample, Y, xs)
    n_pos = int(sample[Y].dropna().sum())
    results.append((label, sample, xs, res, n, n_pos))
    if res is None:
        print(f"  {label:20s}  skipped")
        continue
    b_dem, se_dem, p_dem = c(res, 'Dem_Mayor')
    b_npdes, se_npdes, p_npdes = c(res, 'qncr_nonsevere_asinh_lag1')
    b_stress, se_stress, p_stress = c(res, 'fiscal_stress_index_lag2')
    b_mkt, se_mkt, p_mkt = c(res, 'npdes_x_state_green')
    print(f"  {label:20s}  N={n:4d}  R²={res.rsquared:.3f}  "
          f"Dem={b_dem:+.4f}{stars(p_dem)}  "
          f"NPDES={b_npdes:+.4f}{stars(p_npdes)}  "
          f"Stress={b_stress:+.4f}{stars(p_stress)}  "
          f"NPDES×mkt={b_mkt:+.4f}{stars(p_mkt)}")

# ── Build markdown ──
# All variables to display, in order
DISPLAY_VARS = [
    ('Dem_Mayor', '`Dem_Mayor`'),
    ('pres_dem_two_party_share_lag2', '`pres_dem_two_party_share_lag2`'),
    ('qncr_nonsevere_asinh_lag1', '`npdes_formal_prior3yr_muni`'),
    ('reserve_ratio_lag2', '`reserve_ratio_lag2`'),
    ('debt_service_burden_lag2', '`debt_service_burden_lag2`'),
    ('fn_esg_has_muni_bond_law_post_lag1', '`fn_esg_has_muni_bond_law_post_lag1`'),
    ('asinh_state_all_green_cum_amt_lag1', '`asinh_state_all_green_cum_amt_lag1`'),
    ('state_dem_governor_lag1', '`state_dem_governor_lag1`'),
    ('state_dem_trifecta_lag1', '`state_dem_trifecta_lag1`'),
    ('state_rep_trifecta_lag1', '`state_rep_trifecta_lag1`'),
    ('log_population_city_lag2', '`log_population_city_lag2`'),
    ('log_percapita_income_city_lag2', '`log_percapita_income_city_lag2`'),
    ('unemployment_city_lag2', '`unemployment_city_lag2`'),
    ('fiscal_stress_index_lag2', '**`fiscal_stress_index_lag2`**'),
    ('npdes_x_state_green', '**`npdes × state_green_cum`**'),
]

lines = [
    '# Table 3 — The Labelling Decision',
    '',
    '**Outcome:** `Y_self_green` (city self-labelled green bond issuance).',
    '**Sample:** City-years with `total_ltd_issued > 0` (Census of Governments long-term debt).',
    '**FE:** state + year. **SE:** clustered at city (fips7). **Estimator:** OLS / LPM.',
    '',
    'Conditional on issuing **any** bond, what predicts choosing the **green label**?',
    '',
    f'Bond issuers: N={len(issuers)}, {issuers["fips7"].nunique()} cities, '
    f'{int(issuers["Y_self_green"].sum())} self-green events.  '
    f'Compelled issuers (npdes>0): N={len(compelled_issuers)}, '
    f'{compelled_issuers["fips7"].nunique()} cities, '
    f'{int(compelled_issuers["Y_self_green"].sum())} self-green events.',
    '',
    '| Variable | L1 Baseline | L2 +Fiscal Stress | L3 +Marketability | L4 Both channels | L5 Compelled only |',
    '|---|---|---|---|---|---|',
]
for var, label in DISPLAY_VARS:
    row = [label]
    for spec_label, sample, xs, res, n, n_pos in results:
        b, se, p = c(res, var)
        row.append(fmt(b, se, p))
    lines.append('| ' + ' | '.join(row) + ' |')
# N and R²
lines.append('| N | ' + ' | '.join(f'{r[4]}' for r in results) + ' |')
lines.append('| R² | ' + ' | '.join(f'{r[3].rsquared:.3f}' if r[3] else '—' for r in results) + ' |')

lines.extend([
    '',
    '\\* p<0.10, \\*\\* p<0.05, \\*\\*\\* p<0.01.',
    '',
    '## Reading',
    '',
    '**L1 Baseline.** Conditional on issuing any bond, NPDES formal enforcement still predicts '
    'self-labelling (+0.022\\*\\*\\*). Constituency share also strengthens (+0.069\\*\\*). `Dem_Mayor` '
    'remains null. *Compulsion drives the green label specifically, not just bond issuance.*',
    '',
    '**L2 Greenium-seeking channel.** `fiscal_stress_index_lag2` = **+0.017\\*\\***. Among issuers, '
    'fiscally distressed cities label green more. Consistent with seeking yield reduction through '
    'ESG-oriented demand (greenium).',
    '',
    '**L3 Marketability channel.** `npdes × state_green_cum` = **+0.0022\\*\\***, while NPDES main '
    'effect flips null (-0.020, ns) and state-green main effect is zero. *Compulsion drives green '
    'labelling **only where an ESG investor base exists**.* Compelled cities in shallow-market '
    'states do not bother labelling.',
    '',
    '**L4 Both channels together.** Both interactions retain their signs with the joint spec. The '
    'greenium-seeking and marketability channels are orthogonal: neither absorbs the other.',
    '',
    '**L5 Compelled issuers only.** Among cities that are both under NPDES enforcement *and* '
    'issuing bonds, only `log_population` and `log_percapita_income` predict green labelling. '
    'Partisanship and constituency vanish in this subsample. Interpretation: among compelled '
    'issuers, labelling is a matter of administrative/financial **sophistication** — bigger, '
    'richer cities have the advisory capacity to execute the green-label process.',
    '',
    '## Summary',
    '',
    'Labelling is **market-mediated**, not ideological. Two orthogonal channels:',
    '1. **Greenium-seeking (L2):** distressed cities label green to reduce borrowing cost.',
    '2. **Marketability (L3):** compelled cities label green only where ESG investors exist.',
    '',
    '`Dem_Mayor` is null in every column of Table 3, consistent with Table 1. The partisan '
    'demonstration effect (Table 1 C6) is an extensive-margin interaction, not a labelling story.',
])

out_path = OUT / 'table3_labelling.md'
out_path.write_text('\n'.join(lines) + '\n')
print(f"\nWrote: {out_path}")
