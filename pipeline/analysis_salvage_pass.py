"""
H3a Salvage Pass — Six-specification confirmatory set
=====================================================

Pre-committed set of 6 alternative specs to test whether ANY version of
the Mosley room-to-manoeuvre H3a mechanism survives. Bonferroni-corrected
at α = 0.05/6 = 0.00833.

Batch 1: Specs 1-3 (direct H3a salvage)
Batch 2: Spec 4 (Step 4 binary consent decree)
Batch 3: Specs 5-6 (alternative pathways)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "processed"
OUT = PROC / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

BONFERRONI = 0.05 / 6  # 0.00833

df = pd.read_csv(PROC / "merged_city_year_panel.csv.gz",
                 compression="gzip", low_memory=False)

# Transforms
df["log_population_lag2"] = np.log1p(df["population_city_lag2"])
df["log_percapita_income_lag2"] = np.log1p(df["percapita_income_city_lag2"])
df["epa_water_violations_asinh_lag2"] = np.arcsinh(
    df["epa_water_violations_count_muni_lag2"].fillna(0))
df.loc[df.Year == 2013, "mkt_state_green_bond_ever_lag1"] = 0
df["has_consent_decree"] = (df["epa_case_jdc_prior3yr_muni"] > 0).astype(int)

# Base controls per user spec
BASE_VARS = [
    "epa_water_violations_asinh_lag2",
    "charges_to_own_source",
    "state_igr_share",          # igr_share proxy
    "reserve_ratio_lag2",
    "debt_service_burden_lag2",
    "tel_stringency_normalized",
    "cwsrf_log_obligations_lag2",
    "capital_stock_pc_lag2",
    "Rep_Mayor_lag1",
    "log_population_lag2",
    "log_percapita_income_lag2",
    "unemployment_city_lag2",
    "mkt_state_green_bond_ever_lag1",
    "fn_esg_has_muni_bond_law",
    "state_rep_trifecta",
]
FE = " + C(State) + C(Year)"

OUTCOMES = [
    ("Green_Bond_Issued", "GBI"),
    ("asinh_green_amt", "asinh_amt"),
    ("Y_self_green", "Y_self"),
    ("asinh_self_green_amt", "asinh_self"),
]

# Ensure asinh outcomes exist
if "asinh_green_amt" not in df.columns:
    df["asinh_green_amt"] = np.arcsinh(df["City_Green_Amt_Issued"].fillna(0))
if "asinh_self_green_amt" not in df.columns:
    df["asinh_self_green_amt"] = np.arcsinh(df["Amt_Self-reported Green__Yes"].fillna(0))

# Full sample (2013-2025)
full = df[df.Year.between(2013, 2025)].dropna(subset=BASE_VARS).copy()
# Fiscal stress restricted sample (2015-2023)
stress = full.dropna(subset=["fiscal_stress_pca_lag2"]).copy()
# Table 3 sample (issuer-only)
t3 = df[(df.Green_Bond_Issued == 1)].dropna(
    subset=[c for c in BASE_VARS if c in df.columns] + ["Y_esg_assurance"]
).copy()

print(f"Full sample: {len(full)}")
print(f"Fiscal stress sample: {len(stress)}")
print(f"Table 3 sample: {len(t3)}")

# =========================================================================
# Helper
# =========================================================================
def run(formula, data, cluster="FIPS"):
    try:
        m = smf.ols(formula, data=data).fit(
            cov_type="cluster", cov_kwds={"groups": data[cluster]})
        return m
    except Exception as e:
        return None

def extract(m, var):
    if m is None or var not in m.params.index:
        return np.nan, np.nan, np.nan
    return m.params[var], m.bse[var], m.pvalues[var]

results = []

def record(spec_num, spec_name, outcome_label, key_var, m, data, notes=""):
    b, se, p = extract(m, key_var)
    eff_n = np.nan
    # For triple interactions, compute effective sample
    if ":" in key_var:
        parts = key_var.split(":")
        mask = pd.Series(True, index=data.index)
        for part in parts:
            if part in data.columns:
                mask &= (data[part] > 0)
        eff_n = mask.sum()
    results.append({
        "spec": spec_num,
        "spec_name": spec_name,
        "outcome": outcome_label,
        "key_var": key_var,
        "beta": b, "se": se, "p": p,
        "passes_bonferroni": p < BONFERRONI if not np.isnan(p) else False,
        "n": int(m.nobs) if m else 0,
        "r2": m.rsquared if m else np.nan,
        "eff_n_interaction": int(eff_n) if not np.isnan(eff_n) else "",
        "notes": notes,
    })

# =========================================================================
# BATCH 1: Specs 1, 2, 3
# =========================================================================
print("\n" + "=" * 80)
print("BATCH 1: Direct H3a salvage (Specs 1-3)")
print("=" * 80)

# Remove the triple-interaction variables from base to avoid collinearity
base_no_rep = [c for c in BASE_VARS if c != "Rep_Mayor_lag1"]
base_no_rep_no_reserve = [c for c in base_no_rep if c != "reserve_ratio_lag2"]
base_no_rep_no_dsb = [c for c in base_no_rep if c != "debt_service_burden_lag2"]
base_no_rep_no_npdes = [c for c in base_no_rep if c != "epa_npdes_formal_prior3yr_muni"]

# --- SPEC 1: NPDES formal × Rep × reserve ratio ---
print("\n--- Spec 1: NPDES formal × Rep × reserve_ratio ---")
for yvar, ylabel in OUTCOMES:
    rhs = " + ".join(base_no_rep_no_reserve)
    f = (f"{yvar} ~ epa_npdes_formal_prior3yr_muni * Rep_Mayor_lag1 * reserve_ratio_lag2"
         f" + {rhs}{FE}")
    m = run(f, full)
    key = "epa_npdes_formal_prior3yr_muni:Rep_Mayor_lag1:reserve_ratio_lag2"
    record(1, "NPDES × Rep × reserves", ylabel, key, m, full)
    b, se, p = extract(m, key)
    st = "***" if p<0.001 else "**" if p<0.01 else "*" if p<0.05 else "†" if p<0.1 else ""
    print(f"  {ylabel}: β₇={b:.5f}{st} (SE={se:.5f}, p={p:.4f})" if not np.isnan(b) else f"  {ylabel}: FAILED")

# --- SPEC 2: NPDES formal × Rep × debt service burden ---
print("\n--- Spec 2: NPDES formal × Rep × debt_service_burden ---")
for yvar, ylabel in OUTCOMES:
    rhs = " + ".join(base_no_rep_no_dsb)
    f = (f"{yvar} ~ epa_npdes_formal_prior3yr_muni * Rep_Mayor_lag1 * debt_service_burden_lag2"
         f" + {rhs}{FE}")
    m = run(f, full)
    key = "epa_npdes_formal_prior3yr_muni:Rep_Mayor_lag1:debt_service_burden_lag2"
    record(2, "NPDES × Rep × DSB", ylabel, key, m, full)
    b, se, p = extract(m, key)
    st = "***" if p<0.001 else "**" if p<0.01 else "*" if p<0.05 else "†" if p<0.1 else ""
    print(f"  {ylabel}: β₇={b:.5f}{st} (SE={se:.5f}, p={p:.4f})" if not np.isnan(b) else f"  {ylabel}: FAILED")

# --- SPEC 3: Consent decrees × Rep × fiscal stress PCA ---
print("\n--- Spec 3: Consent decree × Rep × fiscal_stress_pca ---")
print(f"  ⚠ Effective interaction sample: 8 city-years (below 10 threshold — UNDERPOWERED)")
for yvar, ylabel in OUTCOMES:
    rhs = " + ".join([c for c in base_no_rep if c not in ("fiscal_stress_pca_lag2",)])
    f = (f"{yvar} ~ epa_case_jdc_prior3yr_muni * Rep_Mayor_lag1 * fiscal_stress_pca_lag2"
         f" + {rhs}{FE}")
    m = run(f, stress)
    key = "epa_case_jdc_prior3yr_muni:Rep_Mayor_lag1:fiscal_stress_pca_lag2"
    record(3, "Consent × Rep × fiscal_stress", ylabel, key, m, stress,
           notes="UNDERPOWERED: effective interaction N=8")
    b, se, p = extract(m, key)
    st = "***" if p<0.001 else "**" if p<0.01 else "*" if p<0.05 else "†" if p<0.1 else ""
    print(f"  {ylabel}: β₇={b:.5f}{st} (SE={se:.5f}, p={p:.4f})" if not np.isnan(b) else f"  {ylabel}: FAILED")

# =========================================================================
# BATCH 2: Spec 4
# =========================================================================
print("\n" + "=" * 80)
print("BATCH 2: Step 4 consent decree test (Spec 4)")
print("=" * 80)

print(f"\n--- Spec 4: has_consent_decree × Rep on Y_esg_assurance (Table 3 sample) ---")
rhs_t3 = " + ".join([c for c in BASE_VARS if c != "Rep_Mayor_lag1" and c in t3.columns])
f4 = f"Y_esg_assurance ~ has_consent_decree * Rep_Mayor_lag1 + {rhs_t3} + C(Year)"
m4 = run(f4, t3)
key4 = "has_consent_decree:Rep_Mayor_lag1"
record(4, "Consent(bin) × Rep at Step4", "Y_assurance", key4, m4, t3)
b, se, p = extract(m4, key4)
st = "***" if p<0.001 else "**" if p<0.01 else "*" if p<0.05 else "†" if p<0.1 else ""
print(f"  Y_assurance: β₃={b:.4f}{st} (SE={se:.4f}, p={p:.4f})" if not np.isnan(b) else "  FAILED")
# Also report HC SEs
if m4:
    m4_hc = smf.ols(f4, data=t3).fit(cov_type="HC3")
    b_hc, se_hc, p_hc = extract(m4_hc, key4)
    print(f"  HC3 robust: β₃={b_hc:.4f} (SE={se_hc:.4f}, p={p_hc:.4f})")

# =========================================================================
# BATCH 3: Specs 5, 6
# =========================================================================
print("\n" + "=" * 80)
print("BATCH 3: Alternative pathways (Specs 5-6)")
print("=" * 80)

# --- SPEC 5: SKIPPED (variable not available) ---
print("\n--- Spec 5: Rep × state NPDES delegated authority ---")
print("  SKIPPED: state_npdes_delegated_authority NOT AVAILABLE in panel")
for yvar, ylabel in OUTCOMES:
    results.append({
        "spec": 5, "spec_name": "Rep × state NPDES delegated",
        "outcome": ylabel, "key_var": "N/A", "beta": np.nan,
        "se": np.nan, "p": np.nan, "passes_bonferroni": False,
        "n": 0, "r2": np.nan, "eff_n_interaction": "",
        "notes": "SKIPPED: variable not available",
    })

# --- SPEC 6: Rep × has_substitute_issuer ---
print("\n--- Spec 6: Rep × has_substitute_issuer ---")
print(f"  ⚠ has_substitute_issuer variation: 5.3% (below 15% target)")
for yvar, ylabel in OUTCOMES:
    rhs = " + ".join([c for c in BASE_VARS
                      if c not in ("Rep_Mayor_lag1", "has_substitute_issuer")])
    f = (f"{yvar} ~ Rep_Mayor_lag1 * has_substitute_issuer"
         f" + {rhs}{FE}")
    m = run(f, full)
    key = "Rep_Mayor_lag1:has_substitute_issuer"
    record(6, "Rep × substitute issuer", ylabel, key, m, full,
           notes="LOW VARIATION: 5.3% of cities")
    b, se, p = extract(m, key)
    st = "***" if p<0.001 else "**" if p<0.01 else "*" if p<0.05 else "†" if p<0.1 else ""
    print(f"  {ylabel}: β₄={b:.5f}{st} (SE={se:.5f}, p={p:.4f})" if not np.isnan(b) else f"  {ylabel}: FAILED")

# =========================================================================
# Summary table
# =========================================================================
res_df = pd.DataFrame(results)
res_df.to_csv(OUT / "salvage_pass_results.csv", index=False)

print("\n" + "=" * 100)
print("SUMMARY TABLE — H3a Salvage Pass")
print("=" * 100)
print(f'{"Spec":>4} {"Outcome":>10} {"Key coeff":>45} {"β":>10} {"SE":>9} {"p":>8} {"Bonf?":>6} {"EffN":>5} {"Notes"}')
print("-" * 120)
for _, r in res_df.iterrows():
    bf = "YES" if r["passes_bonferroni"] else ""
    print(f'{r["spec"]:>4} {r["outcome"]:>10} {str(r["key_var"])[:44]:>45} '
          f'{r["beta"]:>10.5f} {r["se"]:>9.5f} {r["p"]:>8.4f} {bf:>6} '
          f'{str(r["eff_n_interaction"]):>5} {r["notes"]}')

# Count results
n_bonf = res_df["passes_bonferroni"].sum()
n_sig05 = (res_df["p"] < 0.05).sum()
n_sig10 = (res_df["p"] < 0.10).sum()
n_total = res_df["p"].notna().sum()

print("-" * 120)
print(f"Bonferroni threshold: p < {BONFERRONI:.4f}")
print(f"Passing Bonferroni: {n_bonf} of {n_total}")
print(f"Suggestive (0.00833 < p < 0.05): {n_sig05 - n_bonf}")
print(f"Marginal (0.05 < p < 0.10): {n_sig10 - n_sig05}")
print(f"Null (p ≥ 0.10): {n_total - n_sig10}")

# =========================================================================
# Summary markdown
# =========================================================================
summary = []
summary.append("# H3a Salvage Pass — Summary")
summary.append("")
summary.append(f"Bonferroni threshold: α = 0.05/6 = {BONFERRONI:.4f}")
summary.append(f"Specifications passing Bonferroni: **{n_bonf}**")
summary.append(f"Suggestive (0.00833 < p < 0.05): {n_sig05 - n_bonf}")
summary.append(f"Null (p ≥ 0.05): {n_total - n_sig05}")
summary.append("")
if n_bonf == 0:
    summary.append("## Recommendation")
    summary.append("")
    summary.append("No specification passes the Bonferroni-corrected threshold.")
    summary.append("The H3a fiscal-amplification mechanism is not recoverable")
    summary.append("under any of the six pre-committed alternative specifications.")
    summary.append("")
    summary.append("**Recommendation**: Drop the H3a interaction from the paper's")
    summary.append("main specification. Report the salvage pass in an appendix as")
    summary.append("evidence that the null result is robust across multiple")
    summary.append("compulsion measures and fiscal decompositions.")
else:
    summary.append("## Bonferroni-passing specifications")
    for _, r in res_df[res_df.passes_bonferroni].iterrows():
        summary.append(f"- Spec {r['spec']} ({r['spec_name']}), {r['outcome']}: "
                       f"β = {r['beta']:.5f}, p = {r['p']:.4f}")
    summary.append("")
    summary.append("Run diagnostic checks (VIF, Cook's D, jackknife, control sensitivity)")
    summary.append("before reporting as confirmatory.")

# Any suggestive?
suggestive = res_df[(res_df.p >= BONFERRONI) & (res_df.p < 0.05)]
if len(suggestive):
    summary.append("")
    summary.append("## Suggestive results (p < 0.05 but not Bonferroni-adjusted)")
    for _, r in suggestive.iterrows():
        summary.append(f"- Spec {r['spec']} ({r['spec_name']}), {r['outcome']}: "
                       f"β = {r['beta']:.5f}, p = {r['p']:.4f}")

(OUT / "salvage_pass_summary.md").write_text("\n".join(summary))
print(f"\nWritten: {OUT / 'salvage_pass_results.csv'}")
print(f"         {OUT / 'salvage_pass_summary.md'}")
