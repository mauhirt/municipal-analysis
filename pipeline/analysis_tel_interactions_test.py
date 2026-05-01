"""
analysis_tel_interactions_test.py — TEL × city-level fiscal interactions
=========================================================================
Tests the two theoretically-motivated TEL interactions:

  tel_x_prop_tax_dep  (Mullins revenue-substitution)
  tel_x_charges       (enterprise-fund escape-valve)

TEL main effect is **absorbed by state FE** (48/49 states have invariant
TEL across the panel) — so reporting it as a standalone is misleading.
Here we drop the TEL main effect and include only the two interactions,
holding the city-level partner variables as controls.

Outcomes tested:
  Green_Bond_Issued (Step 1+2 joint)    — Table 1 Col 1 analogue
  Y_self_green      (Step 3 discretion) — Table 1 Col 3 analogue
  Y_esg_assurance   (Step 4 credibility, Green_Bond_Issued==1 sample)

Clustering: state_id (not fips7) — TEL is state-level, so the relevant
serial-correlation unit is the state, not the city.
FE: state + year for T1 outcomes; year only for T3 outcome.
"""
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


def fit_ols(df, y, xs, fe, cluster='state_id'):
    # Dedupe while preserving order — cluster may be same as a FE dimension.
    raw = ['fips7', cluster] + list(fe) + [y] + xs
    seen, cols = set(), []
    for c in raw:
        if c in df.columns and c not in seen:
            cols.append(c)
            seen.add(c)
    d = df[cols].copy()
    d = d.dropna(subset=[y] + [x for x in xs if x in d.columns])
    xs_live = [x for x in xs if x in d.columns and d[x].nunique() > 1]
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
        return res, len(d)
    except Exception as e:
        print(f"  fit error: {e}")
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
    return f'{b:+.4f}{stars(p)} (se {se:.4f})'


# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel: {df.shape}")

# Harmonise treatment name
if 'Rep_Mayor_lag1' not in df.columns and 'Rep_Mayor_L1' in df.columns:
    df['Rep_Mayor_lag1'] = df['Rep_Mayor_L1']
if 'Ind_Mayor_lag1' not in df.columns and 'Ind_Mayor_L1' in df.columns:
    df['Ind_Mayor_lag1'] = df['Ind_Mayor_L1']
for tgt, cands in [('npdes_formal_prior3yr_muni',
                    ['npdes_formal_any_muni_prior3yr', 'npdes_formal_prior3yr_muni']),
                   ('overflow_events_lag2',
                    ['overflow_events_lag2', 'overflow_events_muni_lag2'])]:
    if tgt not in df.columns:
        for c in cands:
            if c in df.columns:
                df[tgt] = df[c]
                break

# Sanity-check: how much variation does TEL have within-state?
tel_within_state = df.groupby('state_abb')['tel_stringency_normalized'].nunique()
print(f"\nTEL within-state unique values:")
print(f"  states with 1 value (invariant): {(tel_within_state == 1).sum()}/{len(tel_within_state)}")
print(f"  → TEL main effect is absorbed by state FE in most specifications")
print(f"  → identification of tel_x_* comes from WITHIN-STATE ACROSS-CITY variation in the city partner")

# ──────────────────────────────────────────────────────────────────────
# Three-family RHS (drop the TEL main effect)
# ──────────────────────────────────────────────────────────────────────
BASE_RHS = [v for v in [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'debt_service_burden_lag2', 'property_tax_dependence_lag2',
    'log_cwsrf_obligations_lag2', 'cwns_needs_real_lag2',
    'state_rep_trifecta', 'esg_has_muni_bond_law', 'state_green_bond_ever_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2', 'has_substitute_issuer',
] if v in df.columns]
print(f"\nBase RHS: {len(BASE_RHS)} variables (TEL main effect dropped)")

# Build the two TEL interactions' presence check
assert 'tel_x_prop_tax_dep' in df.columns, "tel_x_prop_tax_dep missing — run 02_variable_additions.py"
assert 'tel_x_charges' in df.columns,       "tel_x_charges missing — run 02_variable_additions.py"


# ──────────────────────────────────────────────────────────────────────
# Run per-outcome specifications
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 80)
print("TEL × city-fiscal interaction tests")
print("=" * 80)

specs = []

# (A) Full panel — Green_Bond_Issued
specs.append(('A1', 'Green_Bond_Issued', BASE_RHS + ['tel_x_prop_tax_dep'],
              ('state_id', 'year'), df,  'prop-tax-dep only'))
specs.append(('A2', 'Green_Bond_Issued', BASE_RHS + ['tel_x_charges'],
              ('state_id', 'year'), df,  'charges only'))
specs.append(('A3', 'Green_Bond_Issued', BASE_RHS + ['tel_x_prop_tax_dep', 'tel_x_charges'],
              ('state_id', 'year'), df,  'both interactions'))

# (B) Y_self_green
specs.append(('B1', 'Y_self_green', BASE_RHS + ['tel_x_prop_tax_dep'],
              ('state_id', 'year'), df,  'prop-tax-dep only'))
specs.append(('B2', 'Y_self_green', BASE_RHS + ['tel_x_charges'],
              ('state_id', 'year'), df,  'charges only'))
specs.append(('B3', 'Y_self_green', BASE_RHS + ['tel_x_prop_tax_dep', 'tel_x_charges'],
              ('state_id', 'year'), df,  'both interactions'))

# (C) Y_esg_assurance on issuer subsample (year FE only, per Table 3)
issuer = df[df['Green_Bond_Issued'] == 1].copy()
print(f"\n  Issuer subsample (Green_Bond_Issued==1): {len(issuer)} city-years")
specs.append(('C1', 'Y_esg_assurance', BASE_RHS + ['tel_x_prop_tax_dep'],
              ('year',), issuer, 'prop-tax-dep only'))
specs.append(('C2', 'Y_esg_assurance', BASE_RHS + ['tel_x_charges'],
              ('year',), issuer, 'charges only'))
specs.append(('C3', 'Y_esg_assurance', BASE_RHS + ['tel_x_prop_tax_dep', 'tel_x_charges'],
              ('year',), issuer, 'both interactions'))


results = []
print()
for label, y, xs, fe, dsource, note in specs:
    res, n = fit_ols(dsource, y, xs, fe=fe, cluster='state_id')
    results.append((label, y, xs, fe, note, res, n))
    if res is None:
        print(f"  {label}  {y:22s} [{note:20s}] fit failed")
        continue
    b1, se1, p1 = coef(res, 'tel_x_prop_tax_dep')
    b2, se2, p2 = coef(res, 'tel_x_charges')
    line = f"  {label}  {y:22s} n={n:4d}  fe={'+'.join(fe):15s} [{note}]"
    if 'tel_x_prop_tax_dep' in xs:
        line += f"  tel×prop_tax={b1:+.5f}{stars(p1)}"
    if 'tel_x_charges' in xs:
        line += f"  tel×charges={b2:+.5f}{stars(p2)}"
    print(line)
    # Also check if charges_to_own_source_lag2 / property_tax_dependence_lag2 main effects shift
    bC, seC, pC = coef(res, 'charges_to_own_source_lag2')
    bP, seP, pP = coef(res, 'property_tax_dependence_lag2')
    # And Rep_Mayor baseline stability
    bR, seR, pR = coef(res, 'Rep_Mayor_lag1')
    print(f"           main β(charges)={bC:+.3f}{stars(pC)}  "
          f"β(prop_tax_dep)={bP:+.3f}{stars(pP)}  β(Rep_Mayor)={bR:+.3f}{stars(pR)}")


# ──────────────────────────────────────────────────────────────────────
# Write output markdown
# ──────────────────────────────────────────────────────────────────────
md_lines = [
    '# TEL × city-level fiscal interactions — targeted test',
    '',
    'Tests the two theoretically-motivated interactions of state-level `tel_stringency_normalized` '
    'with city-level fiscal variables (which provide the within-state-across-city identifying '
    'variation that TEL alone lacks).',
    '',
    '- **tel × property_tax_dependence** — Mullins/Joyce revenue-substitution hypothesis. '
    'TELs bite on property-tax revenue; the effect should scale with how property-tax-dependent '
    'a city is.',
    '- **tel × charges_to_own_source** — enterprise-fund escape-valve. Enterprise-fund charges '
    '(water/sewer) are exempt from TEL; deep enterprise funds let a city issue revenue-backed '
    'green bonds that bypass the property-tax-based TEL ceiling.',
    '',
    'TEL main effect is dropped (absorbed by state FE in 48/49 states). Clustering is at '
    '`state_id` (not fips7) since TEL is state-level.',
    '',
    'Specifications: state+year FE for T1 outcomes; year FE for T3 (issuer subsample).',
    '',
    '| Spec | y | n | FE | β(tel×prop_tax_dep) | β(tel×charges) | β(Rep_Mayor) |',
    '|---|---|---|---|---|---|---|',
]
for (lbl, y, xs, fe, note, res, n) in results:
    b1 = coef(res, 'tel_x_prop_tax_dep')
    b2 = coef(res, 'tel_x_charges')
    bR = coef(res, 'Rep_Mayor_lag1')
    md_lines.append(
        f'| {lbl} | {y} | {n} | {"+".join(fe)} | '
        f'{fmt(*b1) if "tel_x_prop_tax_dep" in xs else "—"} | '
        f'{fmt(*b2) if "tel_x_charges" in xs else "—"} | '
        f'{fmt(*bR)} |'
    )
md_lines.extend([
    '',
    'Stars: * p<0.10, ** p<0.05, *** p<0.01. Cluster-robust SE at **state** level. '
    'Both interaction variables are continuous × continuous; signs are interpreted at the mean.',
])
(OUT_DIR / 'tel_interaction_test.md').write_text('\n'.join(md_lines) + '\n')
print(f"\nWrote: {OUT_DIR / 'tel_interaction_test.md'}")
