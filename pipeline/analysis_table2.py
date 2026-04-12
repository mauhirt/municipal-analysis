"""
Table 2 — The Compositional Gap and the Compulsion Gradient
============================================================

Tests H2a: the partisan gap in green bond participation increases
monotonically as external compulsion decreases across use-of-proceeds
categories.

Eight columns, one per category + stacked regression:
  Col 1: Y_water_only         (fully compelled)
  Col 2: Y_clean_trans        (moderately compelled)
  Col 3: Y_renewable          (muni utility subsample)
  Col 4: Y_energy_eff         (weakly compelled)
  Col 5: Y_green_bldg         (weakly compelled)
  Col 6: Y_climate_adapt      (descriptive only, Fisher exact)
  Col 7: Y_pollution_control   (Fisher exact)
  Col 8: Stacked regression    (Rep_Mayor x compulsion_ordinal)

Same base RHS as Table 1. State + Year FE, city-clustered SEs.
Firth penalised logistic for sparse outcomes (Cols 4-5).
Fisher exact tests reported for Cols 6-7.

Output: processed/analysis/table2_results.txt
        processed/analysis/table2_coefficients.csv
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy.stats import fisher_exact
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "processed"
OUT = PROC / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("TABLE 2 — Compositional Gap and Compulsion Gradient")
print("=" * 80)

df = pd.read_csv(PROC / "merged_city_year_panel.csv.gz",
                 compression="gzip", low_memory=False)

# Transforms
df["log_population_lag2"] = np.log1p(df["population_city_lag2"])
df["log_percapita_income_lag2"] = np.log1p(df["percapita_income_city_lag2"])
df["log_cwns_needs_real_lag2"] = np.log1p(df["fn_cwns_needs_real_lag2"])
df["epa_water_violations_asinh_lag2"] = np.arcsinh(
    df["epa_water_violations_count_muni_lag2"].fillna(0))
df.loc[df.Year == 2013, "mkt_state_green_bond_ever_lag1"] = 0

# Base controls (same as Table 1)
BASE = [
    "epa_npdes_formal_prior3yr_muni",
    "epa_water_violations_asinh_lag2",
    "charges_to_own_source",
    "reserve_ratio_lag2",
    "tel_stringency_normalized",
    "cwsrf_log_obligations_lag2",
    "log_cwns_needs_real_lag2",
    "fn_pct_deficient_lag2",
    "Rep_Mayor_lag1",
    "log_population_lag2",
    "log_percapita_income_lag2",
    "unemployment_city_lag2",
    "has_substitute_issuer",
    "mkt_state_green_bond_ever_lag1",
    "fn_esg_has_muni_bond_law",
    "state_rep_trifecta",
]
FE = " + C(State) + C(Year)"

# Sample
sample = df[df.Year.between(2013, 2025)].dropna(subset=BASE).copy()
print(f"Sample: {len(sample)} city-years, {sample.FIPS.nunique()} cities")

# Category outcomes
categories = [
    ("Y_water_only", "Water/Sewer", "fully compelled", 5),
    ("Y_clean_trans", "Clean Transportation", "moderately compelled", 4),
    ("Y_renewable", "Renewable Energy", "muni utility compelled", 3),
    ("Y_energy_eff", "Energy Efficiency", "weakly compelled", 2),
    ("Y_green_bldg", "Green Buildings", "weakly compelled", 2),
    ("Y_climate_adapt", "Climate Adaptation", "none", 1),
    ("Y_pollution_control", "Pollution Control", "none", 1),
]

# -------------------------------------------------------------------------
# Descriptive: participation rates by party
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PANEL A — Participation rates by party (raw)")
print("=" * 80)
print(f'{"Category":25s} {"Dem":>6s} {"Rep":>6s} {"Dem N":>6s} {"Rep N":>6s} {"Gap":>8s}')
print("-" * 65)
for yvar, label, compulsion, _ in categories:
    if yvar not in sample.columns:
        continue
    dem = sample[sample.Rep_Mayor_lag1 == 0]
    rep = sample[sample.Rep_Mayor_lag1 == 1]
    dem_rate = dem[yvar].mean() * 100
    rep_rate = rep[yvar].mean() * 100
    dem_n = dem[yvar].sum()
    rep_n = rep[yvar].sum()
    gap = dem_rate - rep_rate
    print(f'{label:25s} {dem_rate:>5.2f}% {rep_rate:>5.2f}% {int(dem_n):>6d} {int(rep_n):>6d} {gap:>+7.2f}pp')

# -------------------------------------------------------------------------
# Cols 1-5: LPM regressions
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PANEL B — LPM regressions (Cols 1-5)")
print("=" * 80)

rhs = " + ".join(BASE) + FE
results = {}

for yvar, label, compulsion, ordinal in categories[:5]:
    if yvar not in sample.columns:
        print(f"\n{label}: {yvar} not in panel — SKIPPED")
        continue

    formula = f"{yvar} ~ {rhs}"

    # For Col 3 (renewables), restrict to muni utility subsample
    if yvar == "Y_renewable":
        sub = sample[sample.ep_has_muni_electric == 1].copy()
        note = f" (muni electric subsample, N={len(sub)})"
    else:
        sub = sample.copy()
        note = ""

    try:
        m = smf.ols(formula, data=sub).fit(
            cov_type="cluster", cov_kwds={"groups": sub["FIPS"]}
        )
        b = m.params.get("Rep_Mayor_lag1", np.nan)
        se = m.bse.get("Rep_Mayor_lag1", np.nan)
        p = m.pvalues.get("Rep_Mayor_lag1", np.nan)
        stars = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "†" if p < 0.10 else ""
        n = int(m.nobs)
        r2 = m.rsquared
        results[yvar] = {"label": label, "beta": b, "se": se, "p": p, "stars": stars,
                         "n": n, "r2": r2, "compulsion": compulsion, "ordinal": ordinal}
        print(f"\n{label}{note}:")
        print(f"  Rep_Mayor_lag1: β = {b:.5f}{stars} (SE={se:.5f}, p={p:.4f})")
        print(f"  N = {n}, R² = {r2:.4f}")

        # Also report water_violations
        bv = m.params.get("epa_water_violations_asinh_lag2", np.nan)
        pv = m.pvalues.get("epa_water_violations_asinh_lag2", np.nan)
        sv = "***" if pv < 0.001 else "**" if pv < 0.01 else "*" if pv < 0.05 else "†" if pv < 0.10 else ""
        print(f"  Water violations: β = {bv:.5f}{sv} (p={pv:.4f})")

    except Exception as e:
        print(f"\n{label}: FAILED — {e}")
        results[yvar] = {"label": label, "beta": np.nan, "se": np.nan, "p": np.nan,
                         "stars": "", "n": 0, "r2": np.nan, "compulsion": compulsion,
                         "ordinal": ordinal}

# -------------------------------------------------------------------------
# Cols 6-7: Fisher exact tests
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PANEL C — Fisher exact tests (Cols 6-7)")
print("=" * 80)

for yvar, label, compulsion, ordinal in categories[5:]:
    if yvar not in sample.columns:
        continue
    dem = sample[sample.Rep_Mayor_lag1 == 0]
    rep = sample[sample.Rep_Mayor_lag1 == 1]

    a = int(dem[yvar].sum())  # Dem issued
    b = int(len(dem) - a)     # Dem not issued
    c = int(rep[yvar].sum())  # Rep issued
    d = int(len(rep) - c)     # Rep not issued

    if a + c == 0:
        print(f"\n{label}: no events in either group — skip Fisher")
        continue

    table = [[a, b], [c, d]]
    odds, p_fisher = fisher_exact(table, alternative="two-sided")

    dem_rate = a / (a + b) * 100 if (a + b) > 0 else 0
    rep_rate = c / (c + d) * 100 if (c + d) > 0 else 0

    print(f"\n{label} ({compulsion}):")
    print(f"  Dem: {a}/{a+b} = {dem_rate:.2f}%")
    print(f"  Rep: {c}/{c+d} = {rep_rate:.2f}%")
    print(f"  Fisher exact p = {p_fisher:.4f}, odds ratio = {odds:.3f}")

    results[yvar] = {"label": label, "beta": np.nan, "se": np.nan,
                     "p": p_fisher, "stars": "", "n": a + b + c + d,
                     "r2": np.nan, "compulsion": compulsion, "ordinal": ordinal,
                     "dem_rate": dem_rate, "rep_rate": rep_rate,
                     "fisher_p": p_fisher, "odds_ratio": odds}

# -------------------------------------------------------------------------
# Col 8: Stacked regression with Rep_Mayor x compulsion_ordinal
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PANEL D — Stacked regression (Col 8)")
print("=" * 80)

# Stack all categories into long format
stack_rows = []
for yvar, label, compulsion, ordinal in categories[:5]:
    if yvar not in sample.columns:
        continue
    sub = sample.copy()
    sub["Y_category"] = sub[yvar]
    sub["category_label"] = label
    sub["compulsion_ordinal"] = ordinal
    stack_rows.append(sub)

stacked = pd.concat(stack_rows, ignore_index=True)
print(f"Stacked sample: {len(stacked)} rows ({len(stacked)//len(sample)} categories × ~{len(sample)} city-years)")

# Stacked regression: Y_category ~ Rep_Mayor * compulsion_ordinal + BASE + C(category) + C(State) + C(Year)
stacked_rhs = " + ".join(BASE) + " + C(category_label) + C(State) + C(Year)"
stacked_formula = f"Y_category ~ Rep_Mayor_lag1 * compulsion_ordinal + {stacked_rhs}"

try:
    m_stacked = smf.ols(stacked_formula, data=stacked).fit(
        cov_type="cluster", cov_kwds={"groups": stacked["FIPS"]}
    )
    b_int = m_stacked.params.get("Rep_Mayor_lag1:compulsion_ordinal", np.nan)
    se_int = m_stacked.bse.get("Rep_Mayor_lag1:compulsion_ordinal", np.nan)
    p_int = m_stacked.pvalues.get("Rep_Mayor_lag1:compulsion_ordinal", np.nan)
    st_int = "***" if p_int < 0.001 else "**" if p_int < 0.01 else "*" if p_int < 0.05 else "†" if p_int < 0.10 else ""
    b_rep = m_stacked.params.get("Rep_Mayor_lag1", np.nan)
    p_rep = m_stacked.pvalues.get("Rep_Mayor_lag1", np.nan)

    print(f"  Rep_Mayor × compulsion_ordinal: β = {b_int:.5f}{st_int} (SE={se_int:.5f}, p={p_int:.4f})")
    print(f"  Rep_Mayor main effect: β = {b_rep:.5f} (p={p_rep:.4f})")
    print(f"  N = {int(m_stacked.nobs)}, R² = {m_stacked.rsquared:.4f}")
    print()
    print(f"  Interpretation: a 1-unit increase in compulsion ordinal")
    if b_int > 0:
        print(f"  NARROWS the partisan gap by {abs(b_int):.4f} pp per ordinal step")
    else:
        print(f"  WIDENS the partisan gap by {abs(b_int):.4f} pp per ordinal step")
except Exception as e:
    print(f"  Stacked regression FAILED: {e}")
    b_int, se_int, p_int = np.nan, np.nan, np.nan

# -------------------------------------------------------------------------
# Save results
# -------------------------------------------------------------------------
res_df = pd.DataFrame(results).T
res_df.to_csv(OUT / "table2_coefficients.csv")

text = []
text.append("=" * 80)
text.append("TABLE 2 — Compositional Gap and Compulsion Gradient")
text.append("=" * 80)
text.append("")
text.append("Panel A: raw participation rates by party")
text.append(f'{"Category":25s} {"Dem %":>8s} {"Rep %":>8s} {"Gap":>8s}')
text.append("-" * 55)
for yvar, label, comp, _ in categories:
    if yvar not in sample.columns:
        continue
    dem = sample[sample.Rep_Mayor_lag1 == 0][yvar].mean() * 100
    rep = sample[sample.Rep_Mayor_lag1 == 1][yvar].mean() * 100
    text.append(f'{label:25s} {dem:>7.2f}% {rep:>7.2f}% {dem - rep:>+7.2f}pp')
text.append("")
text.append("Panel B: Rep_Mayor_lag1 coefficient from LPM regressions (Cols 1-5)")
text.append(f'{"Category":25s} {"β":>10s} {"SE":>9s} {"p":>7s} {"N":>6s}')
text.append("-" * 60)
for yvar, label, comp, _ in categories[:5]:
    if yvar in results and not np.isnan(results[yvar]["beta"]):
        r = results[yvar]
        text.append(f'{label:25s} {r["beta"]:>9.5f}{r["stars"]:<3s} {r["se"]:>9.5f} {r["p"]:>7.4f} {r["n"]:>6d}')
text.append("")
text.append(f"Panel D: Stacked regression — Rep_Mayor × compulsion_ordinal")
if not np.isnan(b_int):
    text.append(f"  β(interaction) = {b_int:.5f} (SE={se_int:.5f}, p={p_int:.4f})")
text.append("")
text.append("All: State + Year FE, SE clustered at FIPS. Sample: 2013-2025.")

(OUT / "table2_results.txt").write_text("\n".join(text))
print(f"\nWritten: {OUT / 'table2_results.txt'}")
print(f"         {OUT / 'table2_coefficients.csv'}")
