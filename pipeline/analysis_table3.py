"""
Table 3 — The Credibility Gap and Its Boundary Conditions
==========================================================

Tests H2b, H3a, H3b conditional on Green_Bond_Issued == 1.

Sample: city-years where Green_Bond_Issued == 1 (the 170 green-leaf issuers).
Outcome: Y_esg_assurance (did the issuer obtain third-party ESG verification?).

Six columns:
  Col 1: Baseline — Rep_Mayor_lag1. Establishes H2b.
  Col 2: + Rep × water_violations (regulatory moderation, H3a)
  Col 3: + Rep × fiscal_stress_pca (fiscal moderation, H3a)
  Col 4: + Rep × pres_dem_vote_share (electoral discipline, H3b)
  Col 5: Rep_Mayor lag 4 (reverse causation check, H3b)
  Col 6: City + Year FE (within-city robustness)

Plus: water-only Fisher exact test (memo's signature inline result).

All columns: LPM, clustered at FIPS (or city FE for Col 6).
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
print("TABLE 3 — The Credibility Gap")
print("Conditional on Green_Bond_Issued == 1")
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

# -------------------------------------------------------------------------
# 0. Pre-table: Water-only Fisher exact test (memo's signature result)
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PRE-TABLE: Water-only Fisher exact test")
print("=" * 80)

water_issuers = df[(df.Green_Bond_Issued == 1) & (df.Y_water_only == 1)].copy()
water_issuers = water_issuers.dropna(subset=["Rep_Mayor_lag1", "Y_esg_assurance"])
print(f"Water-only issuers with Rep_Mayor data: {len(water_issuers)}")

dem_water = water_issuers[water_issuers.Rep_Mayor_lag1 == 0]
rep_water = water_issuers[water_issuers.Rep_Mayor_lag1 == 1]
a = int(dem_water.Y_esg_assurance.sum())
b = int(len(dem_water) - a)
c = int(rep_water.Y_esg_assurance.sum())
d = int(len(rep_water) - c)
dem_rate = a / (a + b) * 100 if (a + b) > 0 else 0
rep_rate = c / (c + d) * 100 if (c + d) > 0 else 0
odds, p_fisher = fisher_exact([[a, b], [c, d]])

print(f"  Democratic mayors: {a}/{a+b} = {dem_rate:.1f}% assurance rate")
print(f"  Republican mayors: {c}/{c+d} = {rep_rate:.1f}% assurance rate")
print(f"  Gap: {dem_rate - rep_rate:.1f} percentage points")
print(f"  Fisher exact p = {p_fisher:.4f}")
print(f"  Odds ratio = {odds:.3f}")
print(f"  Memo claimed: 46% vs 14%, p = 0.010")

# Also do ALL issuers (not just water)
all_issuers = df[df.Green_Bond_Issued == 1].copy()
all_issuers = all_issuers.dropna(subset=["Rep_Mayor_lag1", "Y_esg_assurance"])
dem_all = all_issuers[all_issuers.Rep_Mayor_lag1 == 0]
rep_all = all_issuers[all_issuers.Rep_Mayor_lag1 == 1]
print(f"\n  ALL issuers (not just water):")
print(f"  Dem: {int(dem_all.Y_esg_assurance.sum())}/{len(dem_all)} "
      f"= {dem_all.Y_esg_assurance.mean()*100:.1f}%")
print(f"  Rep: {int(rep_all.Y_esg_assurance.sum())}/{len(rep_all)} "
      f"= {rep_all.Y_esg_assurance.mean()*100:.1f}%")

# -------------------------------------------------------------------------
# 1. Sample construction: condition on Green_Bond_Issued == 1
# -------------------------------------------------------------------------
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

issuers = df[df.Green_Bond_Issued == 1].copy()
issuers = issuers.dropna(subset=[c for c in BASE if c in issuers.columns] +
                         ["Y_esg_assurance", "FIPS", "State", "Year"])
print(f"\nTable 3 sample: {len(issuers)} issuer city-years, "
      f"{issuers.FIPS.nunique()} unique cities")
print(f"Y_esg_assurance = 1: {int(issuers.Y_esg_assurance.sum())} "
      f"({issuers.Y_esg_assurance.mean()*100:.1f}%)")
print(f"Rep_Mayor_lag1 = 1: {int(issuers.Rep_Mayor_lag1.sum())} "
      f"({issuers.Rep_Mayor_lag1.mean()*100:.1f}%)")

# -------------------------------------------------------------------------
# 2. Helper
# -------------------------------------------------------------------------
def run_reg(formula, data, label, cluster_col="FIPS"):
    try:
        m = smf.ols(formula, data=data).fit(
            cov_type="cluster", cov_kwds={"groups": data[cluster_col]}
        )
    except Exception as e:
        print(f"\n--- {label} --- FAILED: {e}")
        return None
    print(f"\n--- {label} ---")
    print(f"  N = {int(m.nobs)}, R² = {m.rsquared:.4f}")
    return m

def coef(r, var):
    if r is None or var not in r.params.index:
        return (np.nan, np.nan, np.nan, "")
    b, se, p = r.params[var], r.bse[var], r.pvalues[var]
    st = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "†" if p < 0.10 else ""
    return (b, se, p, st)

def fmt(r, var):
    b, se, p, st = coef(r, var)
    if np.isnan(b): return "", ""
    return f"{b:.4f}{st}", f"({se:.4f})"

# -------------------------------------------------------------------------
# 3. Regressions (Cols 1-6)
# -------------------------------------------------------------------------
# Note: with only ~130-150 observations, adding 50+ state FE dummies is
# aggressive. Use Year FE only for the main spec, then add state FE as
# robustness. For Col 6, city FE with ~80 cities and 130 obs will be
# severely underpowered.

rhs_base = " + ".join([c for c in BASE if c != "Rep_Mayor_lag1"])

# Check if we have enough states for state FE
n_states = issuers.State.nunique()
print(f"Number of states in issuer sample: {n_states}")

# Use Year FE only (state FE with 130 obs and 30+ states overfits)
FE_main = " + C(Year)"

# Col 1: Baseline
f1 = f"Y_esg_assurance ~ Rep_Mayor_lag1 + {rhs_base}{FE_main}"
c1 = run_reg(f1, issuers, "Col 1: Baseline")

# Col 2: + Rep × water_violations (regulatory moderation)
f2 = f"Y_esg_assurance ~ Rep_Mayor_lag1 * epa_water_violations_asinh_lag2 + {rhs_base}{FE_main}"
c2 = run_reg(f2, issuers, "Col 2: + Rep × water violations")

# Col 3: + Rep × fiscal_stress_pca
sub3 = issuers.dropna(subset=["fiscal_stress_pca_lag2"])
f3 = f"Y_esg_assurance ~ Rep_Mayor_lag1 * fiscal_stress_pca_lag2 + {rhs_base}{FE_main}"
c3 = run_reg(f3, sub3, "Col 3: + Rep × fiscal stress")

# Col 4: + Rep × pres_dem_vote_share (electoral discipline)
sub4 = issuers.dropna(subset=["pres_dem_two_party_share_lag2"])
f4 = f"Y_esg_assurance ~ Rep_Mayor_lag1 * pres_dem_two_party_share_lag2 + {rhs_base}{FE_main}"
c4 = run_reg(f4, sub4, "Col 4: + Rep × pres_dem_vote_share (electoral discipline)")

# Col 5: Rep_Mayor lag 4 (reverse causation)
if "Rep_Mayor_lag2" in issuers.columns:
    # Use lag2 as approximation for lag4 (mayor data has limited pre-period)
    sub5 = issuers.dropna(subset=["Rep_Mayor_lag2"])
    f5 = f"Y_esg_assurance ~ Rep_Mayor_lag2 + {rhs_base}{FE_main}"
    c5 = run_reg(f5, sub5, "Col 5: Rep_Mayor lag 2 (reverse causation proxy)")
else:
    c5 = None
    print("\n--- Col 5: Rep_Mayor_lag2 not available ---")

# Col 6: City + Year FE (within-city robustness)
# Only works if there are cities with variation in BOTH party AND assurance
switchers = issuers.groupby("FIPS").agg(
    rep_var=("Rep_Mayor_lag1", "nunique"),
    assur_var=("Y_esg_assurance", "nunique"),
    n=("Y_esg_assurance", "count"),
)
both_vary = switchers[(switchers.rep_var > 1) & (switchers.assur_var > 1)]
print(f"\nCities with BOTH party switch AND assurance variation: {len(both_vary)}")
if len(both_vary) >= 3:
    f6 = f"Y_esg_assurance ~ Rep_Mayor_lag1 + {rhs_base} + C(FIPS) + C(Year)"
    c6 = run_reg(f6, issuers, "Col 6: City + Year FE")
else:
    c6 = None
    print("  Insufficient within-city variation for city FE — skipping Col 6")

# -------------------------------------------------------------------------
# 4. Print key coefficients
# -------------------------------------------------------------------------
print("\n" + "=" * 90)
print("TABLE 3 — Key Coefficients")
print("=" * 90)

models = {"C1": c1, "C2": c2, "C3": c3, "C4": c4, "C5": c5, "C6": c6}
key_vars = [
    ("Rep_Mayor_lag1", "Rep Mayor (lag 1)"),
    ("Rep_Mayor_lag2", "Rep Mayor (lag 2, Col 5 only)"),
    ("epa_water_violations_asinh_lag2", "Water violations asinh"),
    ("charges_to_own_source", "Charges / own-source"),
    ("Rep_Mayor_lag1:epa_water_violations_asinh_lag2", "Rep × water violations"),
    ("fiscal_stress_pca_lag2", "Fiscal stress PCA"),
    ("Rep_Mayor_lag1:fiscal_stress_pca_lag2", "Rep × fiscal stress"),
    ("pres_dem_two_party_share_lag2", "Pres Dem vote share"),
    ("Rep_Mayor_lag1:pres_dem_two_party_share_lag2", "Rep × Dem vote share"),
]

header = f'{"Variable":40s}'
for c in models:
    header += f' {c:>10s}'
print(header)
print("-" * 100)
for var, label in key_vars:
    line = f'{label[:39]:40s}'
    for cname, m in models.items():
        b, se = fmt(m, var)
        line += f' {b[:10]:>10s}'
    print(line)
    se_line = " " * 40
    has_se = False
    for cname, m in models.items():
        b, se = fmt(m, var)
        se_line += f' {se[:10]:>10s}'
        if se:
            has_se = True
    if has_se:
        print(se_line)

# Add N and R²
for stat, getter in [("N", lambda m: f"{int(m.nobs)}" if m else ""),
                     ("R²", lambda m: f"{m.rsquared:.3f}" if m else "")]:
    line = f'{stat:40s}'
    for cname, m in models.items():
        line += f' {getter(m):>10s}'
    print(line)

print("-" * 100)
print("Year FE in all. City FE in Col 6 only. SE clustered at FIPS.")
print(f"Sample: {len(issuers)} issuer city-years (Green_Bond_Issued == 1)")

# -------------------------------------------------------------------------
# 5. Hypothesis check
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("HYPOTHESIS CHECK")
print("=" * 80)

def interp(m, var, expected, label):
    b, se, p, st = coef(m, var)
    if np.isnan(b):
        print(f"  {label}: {var} not in model")
        return
    match = (
        (expected == "negative" and b < 0 and p < 0.05) or
        (expected == "positive" and b > 0 and p < 0.05) or
        (expected == "null" and p >= 0.05)
    )
    verdict = "✓" if match else "✗"
    print(f"  {verdict} {label}: β = {b:.4f} (p={p:.4f}){st}  expected={expected}")

print("\nH2b — Rep_Mayor negative (credibility gap):")
interp(c1, "Rep_Mayor_lag1", "negative", "Col 1 baseline")

print("\nH3a — Regulatory moderation (compulsion compresses gap):")
interp(c2, "Rep_Mayor_lag1:epa_water_violations_asinh_lag2", "positive", "Col 2 Rep×violations")

print("\nH3a — Fiscal stress moderation (sign reversal vs Table 1):")
if c3:
    interp(c3, "Rep_Mayor_lag1:fiscal_stress_pca_lag2", "negative", "Col 3 Rep×fiscal_stress")
    interp(c3, "fiscal_stress_pca_lag2", "positive", "Col 3 fiscal_stress main (Dems invest more)")

print("\nH3b — Electoral discipline failure:")
if c4:
    interp(c4, "Rep_Mayor_lag1:pres_dem_two_party_share_lag2", "negative", "Col 4 Rep×Dem_vote")

print("\nH3b — Reverse causation check:")
if c5:
    interp(c5, "Rep_Mayor_lag2", "negative", "Col 5 Rep lag 2")

# -------------------------------------------------------------------------
# 6. Save
# -------------------------------------------------------------------------
text = []
text.append("=" * 90)
text.append("TABLE 3 — The Credibility Gap")
text.append("Conditional on Green_Bond_Issued == 1")
text.append("=" * 90)
text.append("")
text.append(f"Water-only Fisher exact test:")
text.append(f"  Democratic mayors: {a}/{a+b} = {dem_rate:.1f}% assurance")
text.append(f"  Republican mayors: {c}/{c+d} = {rep_rate:.1f}% assurance")
text.append(f"  Fisher p = {p_fisher:.4f}")
text.append("")
text.append(header)
text.append("-" * 100)
for var, label in key_vars:
    line = f'{label[:39]:40s}'
    for cname, m in models.items():
        b, se = fmt(m, var)
        line += f' {b[:10]:>10s}'
    text.append(line)
text.append("-" * 100)
for stat, getter in [("N", lambda m: f"{int(m.nobs)}" if m else ""),
                     ("R²", lambda m: f"{m.rsquared:.3f}" if m else "")]:
    line = f'{stat:40s}'
    for cname, m in models.items():
        line += f' {getter(m):>10s}'
    text.append(line)

(OUT / "table3_results.txt").write_text("\n".join(text))

res_rows = []
for var, label in key_vars:
    row = {"variable": label}
    for cname, m in models.items():
        b, se, p, st = coef(m, var)
        row[cname] = f"{b:.5f}{st}" if not np.isnan(b) else ""
        row[f"{cname}_se"] = f"{se:.5f}" if not np.isnan(se) else ""
    res_rows.append(row)
pd.DataFrame(res_rows).to_csv(OUT / "table3_coefficients.csv", index=False)

print(f"\nWritten: {OUT / 'table3_results.txt'}")
print(f"         {OUT / 'table3_coefficients.csv'}")
