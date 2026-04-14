"""
analysis_table3.py — Table 3: Credibility Gap & Boundary Conditions
=====================================================================
Tests H2b / H3a / H3b on the assurance decision (Y_esg_assurance),
conditional on Green_Bond_Issued == 1, with the spec additions
(§2.3, §2.4, §3.3, §3.4, §3.6).

Structure (6 cols, + Fisher exact and robustness rows):
  Col 1  Baseline                                               [H2b]
  Col 2  + Rep_Mayor × npdes_formal_prior3yr_muni               [H3a: regulation]
  Col 3  + Rep_Mayor × fiscal_stress_pca_lag2                   [H3a: fiscal]
  Col 4  + Rep_Mayor × pres_dem_two_party_share_lag2            [H3b: electoral]
  Col 5  Rep_Mayor_lag4 (persistence)                           [H3b: temporal]
  Col 6  city + year FE (within-city)                           [H3b: identification]

Plus robustness columns using the new spec variables:
  R1  + esg_law_intensity_lag1 + rep_x_esg_intensity (§2.3)
  R2  + climate_commitment_static (§2.4)
  R3  + state_carbon_price_usd_lag1 (§3.3)
  R4  + esg_underwriter_block_lag1 (§3.4)
  R5  + inst_utah_antiesg_lag1 (§3.6)
  R6  Baseline with no FE (lower bound) (§5.3)

Sample: cities with at least one Bloomberg-classified green bond during panel.
Clustering: FIPS.
"""
import sys
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import fisher_exact
from linearmodels.panel import PanelOLS

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_panel, stars

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'processed' / 'tables'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def fit_ols(df, y, xs, fe=('year',)):
    cols = ['fips7'] + list(fe) + [y] + xs
    d = df[[c for c in cols if c in df.columns]].copy()
    d = d.dropna(subset=[y] + [x for x in xs if x in d.columns])
    xs_live = [x for x in xs if x in d.columns and d[x].nunique(dropna=True) > 1]
    if len(d) < 20 or not xs_live:
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
    except Exception:
        return None, 0


def fit_within_city(df, y, xs):
    """City + year FE via linearmodels (for Col 6)."""
    d = df[['fips7', 'year', y] + xs].copy()
    d = d.dropna(subset=[y] + xs)
    if len(d) < 20:
        return None, 0
    xs_live = [x for x in xs if d[x].nunique() > 1]
    if not xs_live:
        return None, 0
    try:
        d2 = d.set_index(['fips7', 'year'])
        mod = PanelOLS(d2[y], d2[xs_live].astype(float),
                       entity_effects=True, time_effects=True, check_rank=False)
        res = mod.fit(cov_type='clustered', cluster_entity=True)
        res._xnames = xs_live
        res._is_panel = True
        return res, len(d)
    except Exception:
        return None, 0


def coef(res, name):
    if res is None:
        return np.nan, np.nan, np.nan
    try:
        if getattr(res, '_is_panel', False):
            return float(res.params[name]), float(res.std_errors[name]), float(res.pvalues[name])
        i = res._xnames.index(name)
        return float(res.params[i]), float(res.bse[i]), float(res.pvalues[i])
    except (KeyError, ValueError):
        return np.nan, np.nan, np.nan


def fmt(b, se, p):
    if np.isnan(b):
        return '—'
    return f'{b:+.3f}{stars(p)} ({se:.3f})'


# ──────────────────────────────────────────────────────────────────────
# Load and restrict to green-bond issuer sample
# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel loaded: {df.shape}")

if 'Rep_Mayor_lag1' not in df.columns and 'Rep_Mayor_L1' in df.columns:
    df['Rep_Mayor_lag1'] = df['Rep_Mayor_L1']
if 'Rep_Mayor_L4' in df.columns and 'Rep_Mayor_lag4' not in df.columns:
    df['Rep_Mayor_lag4'] = df['Rep_Mayor_L4']
if 'Ind_Mayor_lag1' not in df.columns and 'Ind_Mayor_L1' in df.columns:
    df['Ind_Mayor_lag1'] = df['Ind_Mayor_L1']

for tgt, cands in [
    ('npdes_formal_prior3yr_muni',
     ['npdes_formal_any_muni_prior3yr', 'npdes_formal_prior3yr_muni']),
]:
    if tgt not in df.columns:
        for c in cands:
            if c in df.columns:
                df[tgt] = df[c]
                break

# fiscal_stress_pca_lag2: build if only fiscal_stress_pca exists
if 'fiscal_stress_pca_lag2' not in df.columns and 'fiscal_stress_pca' in df.columns:
    df = df.sort_values(['fips7', 'year'])
    df['fiscal_stress_pca_lag2'] = df.groupby('fips7')['fiscal_stress_pca'].shift(2)

# ── Table-3 sample: Green_Bond_Issued == 1 ──
issuer_rows = df[df['Green_Bond_Issued'] == 1].copy()
print(f"Table-3 base sample: {len(issuer_rows)} city-years "
      f"({issuer_rows['fips7'].nunique()} unique cities)")

# Interactions needed for Cols 2-4
issuer_rows['rep_x_npdes'] = (issuer_rows['Rep_Mayor_lag1']
                              * issuer_rows.get('npdes_formal_prior3yr_muni', 0))
if 'fiscal_stress_pca_lag2' in issuer_rows.columns:
    issuer_rows['rep_x_fiscal'] = (issuer_rows['Rep_Mayor_lag1']
                                   * issuer_rows['fiscal_stress_pca_lag2'])
if 'pres_dem_two_party_share_lag2' in issuer_rows.columns:
    issuer_rows['rep_x_presdem'] = (issuer_rows['Rep_Mayor_lag1']
                                    * issuer_rows['pres_dem_two_party_share_lag2'])


# ──────────────────────────────────────────────────────────────────────
# Shared RHS (three-family spec)
# ──────────────────────────────────────────────────────────────────────
RHS = [v for v in [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'charges_to_own_source_lag2',
    'reserve_ratio_lag2', 'tel_stringency_normalized',
    'log_cwsrf_obligations_lag2',
    'state_rep_trifecta', 'esg_has_muni_bond_law', 'state_green_bond_ever_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2', 'has_substitute_issuer',
] if v in issuer_rows.columns]


# ──────────────────────────────────────────────────────────────────────
# Main columns
# ──────────────────────────────────────────────────────────────────────
print("\n=== Table 3 main columns ===")

specs = []

specs.append(('Col 1 Baseline', RHS, 'year'))

if 'rep_x_npdes' in issuer_rows.columns:
    specs.append(('Col 2 Rep × NPDES', RHS + ['rep_x_npdes'], 'year'))
if 'rep_x_fiscal' in issuer_rows.columns:
    specs.append(('Col 3 Rep × FiscStress',
                  RHS + ['fiscal_stress_pca_lag2', 'rep_x_fiscal'], 'year'))
if 'rep_x_presdem' in issuer_rows.columns:
    specs.append(('Col 4 Rep × PresDem', RHS + ['rep_x_presdem'], 'year'))

# Col 5 – replace Rep_Mayor_lag1 with Rep_Mayor_lag4
if 'Rep_Mayor_lag4' in issuer_rows.columns:
    rhs_l4 = [v for v in RHS if v != 'Rep_Mayor_lag1'] + ['Rep_Mayor_lag4']
    specs.append(('Col 5 Lag4', rhs_l4, 'year'))

# Col 6 – city + year FE (within-city)
# We run this with linearmodels below (not OLS+dummies).

results = []
Y = 'Y_esg_assurance'

for label, xs, fe in specs:
    res, n = fit_ols(issuer_rows, Y, xs, fe=(fe,) if fe else ())
    results.append((label, xs, res, n))
    if res is None:
        print(f"  [skip] {label}: fit failed (n={n})")
        continue
    # Extract the focal coefficient(s)
    focal = 'Rep_Mayor_lag4' if 'Rep_Mayor_lag4' in xs else 'Rep_Mayor_lag1'
    b, se, p = coef(res, focal)
    print(f"  {label:25s}  n={n:4d}  β({focal})={b:+.3f}{stars(p)} (se={se:.3f})")
    # If it's an interaction col, also print the interaction coefficient
    for x in xs:
        if x.startswith('rep_x_'):
            bb, ss, pp = coef(res, x)
            print(f"    + β({x})={bb:+.3f}{stars(pp)} (se={ss:.3f})")


# Col 6: city + year FE via linearmodels
print()
res_c6, n_c6 = fit_within_city(issuer_rows, Y,
                               [v for v in RHS if v != 'Rep_Mayor_lag1'] + ['Rep_Mayor_lag1'])
if res_c6 is not None:
    b, se, p = coef(res_c6, 'Rep_Mayor_lag1')
    print(f"  Col 6 City+Year FE         n={n_c6:4d}  β(Rep_Mayor_lag1)={b:+.3f}{stars(p)} (se={se:.3f})")
else:
    print("  Col 6 City+Year FE         fit failed")
results.append(('Col 6 City+Year FE', RHS, res_c6, n_c6))


# ──────────────────────────────────────────────────────────────────────
# Robustness appendix with the new spec variables
# ──────────────────────────────────────────────────────────────────────
print("\n=== Table 3 robustness (new spec vars) ===")

rob_specs = []

# R1 — ESG law intensity + interaction
if {'esg_law_intensity_lag1', 'rep_x_esg_intensity'}.issubset(issuer_rows.columns):
    rob_specs.append(('R1 ESG intensity',
                      RHS + ['esg_law_intensity_lag1', 'rep_x_esg_intensity'], 'year'))

# R2 — climate commitment
if 'climate_commitment_static' in issuer_rows.columns:
    rob_specs.append(('R2 Climate commit',
                      RHS + ['climate_commitment_static'], 'year'))

# R3 — continuous state carbon price
if 'state_carbon_price_usd_lag1' in issuer_rows.columns:
    rob_specs.append(('R3 Carbon price',
                      RHS + ['state_carbon_price_usd_lag1'], 'year'))

# R4 — underwriter block
if 'esg_underwriter_block_lag1' in issuer_rows.columns:
    rob_specs.append(('R4 Underwriter block',
                      RHS + ['esg_underwriter_block_lag1'], 'year'))

# R5 — institutional anti-ESG positions
extras_inst = [v for v in ['inst_utah_antiesg_lag1', 'inst_msrb_antiesg_lag1']
               if v in issuer_rows.columns]
if extras_inst:
    rob_specs.append(('R5 Anti-ESG inst',
                      RHS + extras_inst, 'year'))

# R6 — IIJA water grant (does co-financing explain the assurance gap?)
if 'iija_water_grant_amt_asinh_lag1' in issuer_rows.columns:
    rob_specs.append(('R6 IIJA water',
                      RHS + ['iija_water_grant_amt_asinh_lag1'], 'year'))

# R7 — no FE lower bound (§5.3)
rob_specs.append(('R7 No FE', RHS, None))

# R8 — state FE only (§5.3)
rob_specs.append(('R8 State FE', RHS, 'state_id'))


rob_results = []
for label, xs, fe in rob_specs:
    fe_tuple = (fe,) if fe else ()
    res, n = fit_ols(issuer_rows, Y, xs, fe=fe_tuple)
    rob_results.append((label, xs, res, n))
    if res is None:
        print(f"  [skip] {label}")
        continue
    b, se, p = coef(res, 'Rep_Mayor_lag1')
    extras_str = ''
    for v in xs:
        if v not in RHS:
            bb, ss, pp = coef(res, v)
            if not np.isnan(bb):
                extras_str += f'  β({v})={bb:+.3f}{stars(pp)}'
    print(f"  {label:22s}  n={n:4d}  β(Rep_Mayor_lag1)={b:+.3f}{stars(p)} (se={se:.3f}){extras_str}")


# ──────────────────────────────────────────────────────────────────────
# Fisher exact — water-only sample
# ──────────────────────────────────────────────────────────────────────
print("\n=== Fisher exact: water-only assurance gap ===")
wmask = (df.get('Y_water_only', 0) == 1)
wsub = df[wmask & df[Y].notna() & df['Rep_Mayor_lag1'].notna()]
if len(wsub):
    tab = pd.crosstab(wsub['Rep_Mayor_lag1'], wsub[Y])
    if tab.shape == (2, 2):
        dr_ass = tab.loc[0.0, 1] / tab.loc[0.0].sum() if 0.0 in tab.index else 0
        rr_ass = tab.loc[1.0, 1] / tab.loc[1.0].sum() if 1.0 in tab.index else 0
        _, p_f = fisher_exact(tab)
        print(f"  Water-only (N={len(wsub)}): Dem assurance rate = {dr_ass:.1%}, "
              f"Rep assurance rate = {rr_ass:.1%}, Fisher p = {p_f:.3f}")
    else:
        p_f = np.nan
        print(f"  Water-only N={len(wsub)}, crosstab shape={tab.shape}")
else:
    p_f = np.nan


# ──────────────────────────────────────────────────────────────────────
# Write outputs
# ──────────────────────────────────────────────────────────────────────
focus = [
    'Rep_Mayor_lag1', 'Rep_Mayor_lag4', 'Ind_Mayor_lag1',
    'pres_dem_two_party_share_lag2', 'npdes_formal_prior3yr_muni',
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'tel_stringency_normalized', 'state_rep_trifecta',
    'esg_has_muni_bond_law', 'has_substitute_issuer',
    'rep_x_npdes', 'rep_x_fiscal', 'rep_x_presdem',
    'fiscal_stress_pca_lag2',
    'esg_law_intensity_lag1', 'rep_x_esg_intensity',
    'climate_commitment_static',
    'state_carbon_price_usd_lag1',
    'esg_underwriter_block_lag1',
    'inst_utah_antiesg_lag1', 'inst_msrb_antiesg_lag1',
    'iija_water_grant_amt_asinh_lag1',
]


def write_md(path, title, block_results, include_fisher=False):
    lines = [f'# {title}', '']
    col_labels = [lbl for (lbl, *_) in block_results]
    lines.append('| Variable | ' + ' | '.join(col_labels) + ' |')
    lines.append('|' + '---|' * (len(col_labels) + 1))
    for v in focus:
        cells = []
        for (_, _, res, _) in block_results:
            b, se, p = coef(res, v)
            cells.append(fmt(b, se, p))
        lines.append('| ' + v + ' | ' + ' | '.join(cells) + ' |')
    lines.append('| N | ' + ' | '.join(str(n) for (_, _, _, n) in block_results) + ' |')
    lines.append('| R² | ' + ' | '.join(
        f'{getattr(r, "rsquared", float("nan")):.3f}' if r is not None else '—'
        for (_, _, r, _) in block_results) + ' |')
    if include_fisher and not np.isnan(p_f):
        lines.append('')
        lines.append(f'**Water-only Fisher exact test**: Dem={dr_ass:.1%}, Rep={rr_ass:.1%}, '
                     f'p={p_f:.3f} (N={len(wsub)}).')
    lines.append('')
    lines.append('Stars: * p<0.10, ** p<0.05, *** p<0.01. '
                 'Cluster-robust SE (FIPS). Year FE (unless noted).')
    Path(path).write_text('\n'.join(lines) + '\n')


write_md(OUT_DIR / 'table3_assurance.md',
         'Table 3 — Credibility Gap & Boundary Conditions (main 6 cols)',
         results, include_fisher=True)

write_md(OUT_DIR / 'table3_robustness.md',
         'Table 3 — Robustness (new spec variables)',
         rob_results)


# CSV dumps
def to_csv_dict(block_results):
    out = {'Variable': focus}
    for (lbl, _, res, n) in block_results:
        vals = []
        for v in focus:
            b, se, p = coef(res, v)
            vals.append(fmt(b, se, p))
        out[lbl] = vals
    return pd.DataFrame(out)


to_csv_dict(results).to_csv(OUT_DIR / 'table3_assurance.csv', index=False)
to_csv_dict(rob_results).to_csv(OUT_DIR / 'table3_robustness.csv', index=False)

print(f"\nWrote: {OUT_DIR / 'table3_assurance.md'}")
print(f"Wrote: {OUT_DIR / 'table3_robustness.md'}")
print(f"Wrote: {OUT_DIR / 'table3_assurance.csv'}")
print(f"Wrote: {OUT_DIR / 'table3_robustness.csv'}")
