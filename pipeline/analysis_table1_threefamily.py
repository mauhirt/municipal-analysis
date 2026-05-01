"""
analysis_table1_threefamily.py — Table 1: The Compulsion Pipeline
=================================================================
Tests H1a/H1b from three_table_strategy_memo_revised.docx, updated with
the spec variables added in pipeline/02_variable_additions.py.

Structure (6 main cols, plus robustness appendix):
  Col 1  Green_Bond_Issued ~ compulsion pipeline (LPM)  [H1b: Rep_Mayor null]
  Col 2  asinh_green_amt   ~ same RHS                   [intensive margin]
  Col 3  Y_self_green      ~ full three-family spec     [pivot: Rep_Mayor -]
  Col 4  asinh_self_green_amt ~ same                    [amount at Step 3]
  Col 5  Green_Bond_Issued + triple interactions        [Step-2 moderations]
  Col 6  asinh_green_amt (intensive margin)             [§4.1 new column]

Robustness appendix (§1.5, §2.1, §2.2, §2.3, §3.2, §3.3):
  R1  Col 3 + YCOM opinion (opinion_regulate_lag2 + opinion_fundrenewables_lag2)
  R2  Col 3 + IIJA/IRA/FEMA grants (does Rep_Mayor gap narrow?)
  R3  Col 3 with mayor_prob_rep_lag1 replacing binary Rep_Mayor_lag1
  R4  Col 3 + symmetric F3: Dem governor + Dem/Rep trifectas + carbon pricing

Standard errors: clustered at FIPS. Fixed effects: state + year.
"""
import sys
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_panel, stars

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'processed' / 'tables'
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ──────────────────────────────────────────────────────────────────────
# Regression helper (OLS + state/year FE + FIPS cluster SE)
# ──────────────────────────────────────────────────────────────────────
def fit_ols(df, y, xs, fe=('state_id', 'year')):
    """OLS with explicit FE dummies; cluster SE on fips7."""
    cols = ['fips7'] + list(fe) + [y] + xs
    d = df[[c for c in cols if c in df.columns]].copy()
    d = d.dropna(subset=[y] + [x for x in xs if x in d.columns])
    if len(d) < 50:
        return None, 0
    X_parts = [d[[x for x in xs if x in d.columns]].astype(float)]
    for f in fe:
        if f in d.columns:
            X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
    X = pd.concat(X_parts, axis=1)
    X = sm.add_constant(X).astype(float)
    y_vec = d[y].astype(float).values
    try:
        res = sm.OLS(y_vec, X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d['fips7'].values})
        # Tag column names for extraction
        res._xnames = list(X.columns)
        return res, len(d)
    except Exception as e:
        print(f"    fit failed: {e}")
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
    return f'{b:+.3f}{stars(p)}\n({se:.3f})'


# ──────────────────────────────────────────────────────────────────────
# Load panel and stage variables
# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel loaded: {df.shape}")

# Harmonise the canonical names that feature in the spec.
if 'Rep_Mayor_lag1' not in df.columns and 'Rep_Mayor_L1' in df.columns:
    df['Rep_Mayor_lag1'] = df['Rep_Mayor_L1']
if 'Ind_Mayor_lag1' not in df.columns and 'Ind_Mayor_L1' in df.columns:
    df['Ind_Mayor_lag1'] = df['Ind_Mayor_L1']

# Some compulsion/fiscal variables use different lag names in the panel —
# build local aliases so the RHS block stays legible.
needed = {
    'npdes_formal_prior3yr_muni': 'npdes_formal_any_muni_prior3yr',
    'overflow_events_muni_lag2': 'overflow_events_muni_lag2',
    'charges_to_own_source_lag2': 'charges_to_own_source_lag2',
}
for tgt, candidates in [
    ('npdes_formal_prior3yr_muni',
     ['npdes_formal_any_muni_prior3yr', 'npdes_formal_prior3yr_muni']),
    ('overflow_events_lag2', ['overflow_events_lag2', 'overflow_events_muni_lag2']),
]:
    if tgt not in df.columns:
        for c in candidates:
            if c in df.columns:
                df[tgt] = df[c]
                break

# Triple-interaction terms for Col 5.
if {'npdes_formal_prior3yr_muni', 'Rep_Mayor_lag1'}.issubset(df.columns):
    df['npdes_x_rep'] = df['npdes_formal_prior3yr_muni'] * df['Rep_Mayor_lag1']
if {'overflow_events_lag2', 'Rep_Mayor_lag1'}.issubset(df.columns):
    df['overflow_x_rep'] = df['overflow_events_lag2'] * df['Rep_Mayor_lag1']
if {'npdes_formal_prior3yr_muni', 'fiscal_stress_pca', 'Rep_Mayor_lag1'}.issubset(df.columns):
    df['npdes_x_fiscal_x_rep'] = (
        df['npdes_formal_prior3yr_muni']
        * df['fiscal_stress_pca']
        * df['Rep_Mayor_lag1']
    )

# ──────────────────────────────────────────────────────────────────────
# Variable blocks
# ──────────────────────────────────────────────────────────────────────
F1a_COMPULSION = [
    'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
]
F1b_FISCAL = [
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'debt_service_burden_lag2', 'tel_stringency_normalized',
    'log_cwsrf_obligations_lag2', 'cwns_needs_real_lag2',
]
F2_POLITICAL = [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
]
F3_STATE = [
    'state_green_bond_ever_lag1', 'esg_has_muni_bond_law',
    'state_rep_trifecta',
]
CONTROLS = [
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2', 'has_substitute_issuer',
]

RHS_FULL = F1a_COMPULSION + F1b_FISCAL + F2_POLITICAL + F3_STATE + CONTROLS
RHS_FULL = [v for v in RHS_FULL if v in df.columns]
print(f"RHS_FULL: {len(RHS_FULL)} variables present")


# ──────────────────────────────────────────────────────────────────────
# Main table (Cols 1-6)
# ──────────────────────────────────────────────────────────────────────
print("\n=== Running Table 1 main columns ===")
cols_spec = [
    ('Col 1', 'Green_Bond_Issued',    RHS_FULL, 'LPM; H1b: Rep_Mayor null'),
    ('Col 2', 'asinh_green_amt',      RHS_FULL, 'intensive margin'),
    ('Col 3', 'Y_self_green',         RHS_FULL, 'pivot: Rep_Mayor expected -'),
    ('Col 4', 'asinh_self_green_amt', RHS_FULL, 'self-label amount'),
    ('Col 5', 'Green_Bond_Issued',
     RHS_FULL + [v for v in ['npdes_x_rep', 'overflow_x_rep', 'npdes_x_fiscal_x_rep']
                 if v in df.columns],
     'triple interactions'),
    ('Col 6', 'asinh_green_amt',      RHS_FULL, '§4.1 intensive margin replication'),
]

results = []
for label, y, xs, note in cols_spec:
    if y not in df.columns:
        print(f"  [skip] {label}: outcome {y} missing")
        continue
    res, n = fit_ols(df, y, xs)
    results.append((label, y, xs, note, res, n))
    if res is None:
        print(f"  [skip] {label}: fit failed (n={n})")
        continue
    b, se, p = coef(res, 'Rep_Mayor_lag1')
    print(f"  {label:6s}  y={y:25s}  n={n:4d}  "
          f"β(Rep_Mayor_lag1)={b:+.3f}{stars(p)} (se={se:.3f})")


# ──────────────────────────────────────────────────────────────────────
# Robustness appendix (R1-R4) — uses Col 3 (Y_self_green) as the base
# ──────────────────────────────────────────────────────────────────────
print("\n=== Running Table 1 robustness appendix ===")

Y = 'Y_self_green'

rob_specs = []

# R1: + YCOM
ycom_extras = [v for v in ['opinion_regulate_lag2', 'opinion_fundrenewables_lag2']
               if v in df.columns]
if ycom_extras:
    rob_specs.append(('R1 + YCOM', Y, RHS_FULL + ycom_extras,
                      'Does Rep_Mayor survive conditioning on climate opinion?'))

# R2: + federal grants (IIJA water, IRA EECBG, IRA GGRF, IIJA transit, FEMA resil)
grant_extras = [v for v in [
    'iija_water_grant_amt_asinh_lag1',
    'ira_eecbg_grant_amt_asinh_lag1',
    'ira_ggrf_grant_amt_asinh_lag1',
    'iija_transit_grant_amt_asinh_lag1',
    'fema_resil_grant_amt_asinh_lag1',
] if v in df.columns]
if grant_extras:
    rob_specs.append(('R2 + Grants', Y, RHS_FULL + grant_extras,
                      'Critical test: partisan gap narrows when grants added?'))

# R3: probabilistic partisanship
rhs_prob = [v for v in RHS_FULL if v != 'Rep_Mayor_lag1']
if 'mayor_prob_rep_lag1' in df.columns:
    rob_specs.append(('R3 Prob Rep', Y, rhs_prob + ['mayor_prob_rep_lag1'],
                      'Continuous treatment replacing binary Rep_Mayor'))

# R4: symmetric F3 (drop esg_has_muni_bond_law + add Dem gov/trifecta + carbon pricing)
f3_symmetric = [v for v in [
    'state_rep_trifecta_lag1', 'state_dem_trifecta_lag1',
    'state_dem_governor_lag1', 'state_carbon_pricing_lag1',
] if v in df.columns]
rhs_r4 = [v for v in RHS_FULL if v not in ('esg_has_muni_bond_law', 'state_rep_trifecta')] + f3_symmetric
if f3_symmetric:
    rob_specs.append(('R4 Sym F3', Y, rhs_r4, 'Symmetric F3 + carbon pricing'))

# R5: + ESG law intensity (instead of binary esg_has_muni_bond_law)
if 'esg_law_intensity_lag1' in df.columns:
    rhs_r5 = [v for v in RHS_FULL if v != 'esg_has_muni_bond_law'] + ['esg_law_intensity_lag1']
    rob_specs.append(('R5 ESG Int.', Y, rhs_r5,
                      'Continuous ESG-intensity replaces binary'))

# R6: + climate-network membership
net_extras = [v for v in ['c40_member_lag1', 'iclei_member_lag1',
                          'climate_commitment_static']
              if v in df.columns]
if net_extras:
    rob_specs.append(('R6 Networks', Y, RHS_FULL + net_extras,
                      'C40/ICLEI/MCPA network membership'))

# R7: + urbanisation controls (pop density, principal city)
urb_extras = [v for v in ['pop_density_sqkm_lag2', 'is_principal_city_lag2']
              if v in df.columns]
if urb_extras:
    rob_specs.append(('R7 Urban', Y, RHS_FULL + urb_extras,
                      'Urbanisation controls'))

# R8: + BPS compulsion (for green-buildings test — spec §1.4)
bps_extras = [v for v in ['bcode_state_bps_adopted_lag1',
                          'bcode_iecc_lag_yrs_lag1',
                          'bcode_state_weakening_amendments_lag1']
              if v in df.columns]
if bps_extras:
    rob_specs.append(('R8 BPS', Y, RHS_FULL + bps_extras,
                      'Building Performance Standards compulsion'))

# R9: fiscal-stress robustness
if 'fiscal_stress_index_lag2' in df.columns:
    rob_specs.append(('R9 FiscStr', Y, RHS_FULL + ['fiscal_stress_index_lag2'],
                      'Fiscal-stress index robustness (§1.8)'))

# R10: + informal NPDES enforcement (§1.1)
if 'epa_npdes_informal_asinh_lag2' in df.columns:
    rob_specs.append(('R10 Informal', Y, RHS_FULL + ['epa_npdes_informal_asinh_lag2'],
                      'Informal NPDES enforcement'))


rob_results = []
for label, y, xs, note in rob_specs:
    res, n = fit_ols(df, y, xs)
    rob_results.append((label, y, xs, note, res, n))
    if res is None:
        print(f"  [skip] {label}: fit failed")
        continue
    b, se, p = coef(res, 'Rep_Mayor_lag1' if 'Rep_Mayor_lag1' in xs else 'mayor_prob_rep_lag1')
    key = 'Rep_Mayor_lag1' if 'Rep_Mayor_lag1' in xs else 'mayor_prob_rep_lag1'
    print(f"  {label:14s}  n={n:4d}  β({key})={b:+.3f}{stars(p)} (se={se:.3f})   [{note}]")


# ──────────────────────────────────────────────────────────────────────
# Write outputs
# ──────────────────────────────────────────────────────────────────────
def rows_for_table(results_list, focus_vars):
    """Build an [coef × column] markdown-style rows dict."""
    out = []
    # Variable rows
    for v in focus_vars:
        row = [v]
        for (_, _, _, _, res, _) in results_list:
            b, se, p = coef(res, v)
            row.append(fmt(b, se, p))
        out.append(row)
    # N row
    out.append(['N'] + [str(n) for (_, _, _, _, _, n) in results_list])
    # R² row
    out.append(['R²'] + [f"{getattr(r, 'rsquared', float('nan')):.3f}" if r is not None else '—'
                         for (_, _, _, _, r, _) in results_list])
    return out


focus_main = [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'tel_stringency_normalized', 'log_cwsrf_obligations_lag2',
    'state_rep_trifecta', 'esg_has_muni_bond_law', 'state_green_bond_ever_lag1',
    'has_substitute_issuer',
    # Interactions (Col 5)
    'npdes_x_rep', 'overflow_x_rep', 'npdes_x_fiscal_x_rep',
]

focus_rob = focus_main + [
    'opinion_regulate_lag2', 'opinion_fundrenewables_lag2',
    'iija_water_grant_amt_asinh_lag1', 'ira_eecbg_grant_amt_asinh_lag1',
    'ira_ggrf_grant_amt_asinh_lag1', 'iija_transit_grant_amt_asinh_lag1',
    'fema_resil_grant_amt_asinh_lag1',
    'mayor_prob_rep_lag1',
    'state_dem_governor_lag1', 'state_dem_trifecta_lag1',
    'state_carbon_pricing_lag1', 'esg_law_intensity_lag1',
    'c40_member_lag1', 'iclei_member_lag1', 'climate_commitment_static',
    'pop_density_sqkm_lag2', 'is_principal_city_lag2',
    'bcode_state_bps_adopted_lag1', 'bcode_iecc_lag_yrs_lag1',
    'bcode_state_weakening_amendments_lag1',
    'fiscal_stress_index_lag2',
    'epa_npdes_informal_asinh_lag2',
]


def write_md(path, title, col_labels, rows):
    with open(path, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write('| Variable | ' + ' | '.join(col_labels) + ' |\n')
        f.write('|' + '---|' * (len(col_labels) + 1) + '\n')
        for row in rows:
            cells = [(row[0],)]
            # Escape newlines within coefficient/SE cells
            cells = [row[0]] + [c.replace('\n', '<br>') for c in row[1:]]
            f.write('| ' + ' | '.join(cells) + ' |\n')
        f.write("\nStars: * p<0.10, ** p<0.05, *** p<0.01. "
                "Cluster-robust SE (FIPS). FE: state + year (main); state + year (robustness).\n")


main_labels = [f"{lbl}\n{y}" for (lbl, y, _, _, _, _) in results]
write_md(
    OUT_DIR / 'table1_threefamily.md',
    'Table 1 — The Compulsion Pipeline (main 6 columns)',
    main_labels, rows_for_table(results, focus_main),
)

rob_labels = [f"{lbl}\nY_self_green" for (lbl, _, _, _, _, _) in rob_results]
write_md(
    OUT_DIR / 'table1_robustness.md',
    'Table 1 — Robustness Appendix (new spec variables)',
    rob_labels, rows_for_table(rob_results, focus_rob),
)

# CSV dumps for machine-readable review
def rows_to_df(results_list, focus, col_labels):
    import pandas as pd
    out = {'Variable': focus}
    for (lbl, _, _, _, res, _), cl in zip(results_list, col_labels):
        vals = []
        for v in focus:
            b, se, p = coef(res, v)
            if np.isnan(b):
                vals.append('')
            else:
                vals.append(f'{b:+.4f}{stars(p)} ({se:.4f})')
        out[lbl] = vals
    out['__N'] = None
    return pd.DataFrame(out)


main_df = rows_to_df(results, focus_main, [lbl for (lbl, *_) in results])
main_df.to_csv(OUT_DIR / 'table1_threefamily.csv', index=False)
rob_df = rows_to_df(rob_results, focus_rob, [lbl for (lbl, *_) in rob_results])
rob_df.to_csv(OUT_DIR / 'table1_robustness.csv', index=False)

print(f"\nWrote: {OUT_DIR / 'table1_threefamily.md'}")
print(f"Wrote: {OUT_DIR / 'table1_robustness.md'}")
print(f"Wrote: {OUT_DIR / 'table1_threefamily.csv'}")
print(f"Wrote: {OUT_DIR / 'table1_robustness.csv'}")
