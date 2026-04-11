"""
Table 1 — The Compulsion Pipeline
================================

Implements the memo's five-column Table 1 specification from
three_table_strategy_memo_revised.docx.

Hypotheses tested:
  H1a: regulatory and fiscal compulsion drives green bond issuance
       regardless of mayoral party.
  H1b: Rep_Mayor is null at the extensive issuance margin conditional
       on compulsion.

Columns:
  Col 1 — Green_Bond_Issued (LPM)                  — baseline pipeline
  Col 2 — asinh_green_amt (OLS)                    — amount
  Col 3 — Y_self_green (LPM)                       — PIVOT, Step 3
  Col 4 — asinh_self_green_amt (OLS)               — amount of self-green
  Col 5 — Green_Bond_Issued with three interactions
          (i)  npdes_formal_prior3yr_muni x Rep_Mayor
          (ii) overflow_events_muni x Rep_Mayor
          (iii) npdes_formal_prior3yr_muni x fiscal_stress_pca_lag2 x
                Rep_Mayor   [THE KEY TRIPLE]

Specification:
  - State + Year fixed effects (all columns)
  - Standard errors clustered at city (FIPS)
  - Sample window: 2015-2025 outcome years (lag2-safe)
  - Col 5 restricted to 2015-2023 because fiscal_stress_pca_lag2 is
    bounded by the fiscal file ending 2021
  - Linear Probability Model (LPM) for binary outcomes per memo

Inputs: processed/merged_city_year_panel.csv
         raw/epa/city_year_epa_enforcement_expanded_20260407_125920.csv
         (for overflow_events_muni only)

Output: processed/analysis/table1_results.txt
        processed/analysis/table1_coefficients.csv
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*inverted.*")

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "processed"
OUT = PROC / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

print("=" * 78)
print("TABLE 1 — The Compulsion Pipeline")
print("Paper: When Do Red and Blue Go Green?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Load merged panel
# ---------------------------------------------------------------------------
df = pd.read_csv(PROC / "merged_city_year_panel.csv", low_memory=False)
print(f"\nPanel loaded: {df.shape}")

# ---------------------------------------------------------------------------
# 2. Add overflow_events_muni (not in pipeline/20 whitelist)
# ---------------------------------------------------------------------------
epa = pd.read_csv(
    ROOT / "raw" / "epa" / "city_year_epa_enforcement_expanded_20260407_125920.csv",
    usecols=["FIPS", "YEAR", "overflow_events_muni"],
    low_memory=False,
)
epa = epa.rename(columns={
    "YEAR": "Year",
    "overflow_events_muni": "epa_overflow_events_muni",
})
df = df.merge(epa, on=["FIPS", "Year"], how="left")
df["epa_overflow_events_muni"] = df["epa_overflow_events_muni"].fillna(0)
print(f"  Merged overflow_events_muni: {(df.epa_overflow_events_muni > 0).sum()} non-zero rows")

# ---------------------------------------------------------------------------
# 3. Derive log transforms for size variables
# ---------------------------------------------------------------------------
df["log_population_lag2"] = np.log1p(df["population_city_lag2"])
df["log_percapita_income_lag2"] = np.log1p(df["percapita_income_city_lag2"])
df["log_cwns_needs_real_lag2"] = np.log1p(df["fn_cwns_needs_real_lag2"])

# ---------------------------------------------------------------------------
# 4. Define control vector (shared across Cols 1-4)
# ---------------------------------------------------------------------------
BASE_CONTROLS = [
    # Family 1a — PRIMARY compulsion
    "epa_npdes_formal_prior3yr_muni",
    # Family 1b — fiscal necessity
    "charges_to_own_source",
    "reserve_ratio_lag2",
    "tel_stringency_normalized",
    "cwsrf_log_obligations_lag2",
    "log_cwns_needs_real_lag2",
    "fn_pct_deficient_lag2",
    # Family 2 — partisan
    "Rep_Mayor_lag1",
    # City controls
    "log_population_lag2",
    "log_percapita_income_lag2",
    "unemployment_city_lag2",
    "has_substitute_issuer",
    # State institutional (Family 3)
    "mkt_state_green_bond_ever_lag1",
    "fn_esg_has_muni_bond_law",
    "state_rep_trifecta",
]

# ---------------------------------------------------------------------------
# 5. Sample construction for Cols 1-4
# ---------------------------------------------------------------------------
# Core window: 2015-2025 (lag2 safe for most vars)
s14 = df[df.Year.between(2015, 2025)].copy()
# Drop rows with NA on the core set
keep_vars = BASE_CONTROLS + ["Green_Bond_Issued", "Y_self_green",
                             "asinh_green_amt", "asinh_self_green_amt",
                             "FIPS", "State", "Year"]
s14 = s14.dropna(subset=BASE_CONTROLS).copy()
print(f"\nCols 1-4 sample: {len(s14)} city-years, {s14.FIPS.nunique()} cities")

# Col 5 sample: 2015-2023 because fiscal_stress_pca_lag2 requires 2013-2021
# source data (ends 2021 in the raw fiscal file)
s5 = df[df.Year.between(2015, 2023)].copy()
s5 = s5.dropna(subset=BASE_CONTROLS + ["fiscal_stress_pca_lag2"]).copy()
print(f"Col 5 sample:    {len(s5)} city-years, {s5.FIPS.nunique()} cities "
      f"(restricted to 2015-2023 for fiscal_stress_pca_lag2)")

# ---------------------------------------------------------------------------
# 6. Helper to run a clustered FE regression
# ---------------------------------------------------------------------------
def run_reg(formula, data, label, cluster_col="FIPS"):
    model = smf.ols(formula, data=data)
    result = model.fit(
        cov_type="cluster",
        cov_kwds={"groups": data[cluster_col]},
    )
    print(f"\n--- {label} ---")
    print(f"  N     = {int(result.nobs)}")
    print(f"  R²    = {result.rsquared:.4f}")
    print(f"  R²adj = {result.rsquared_adj:.4f}")
    return result

def coef_row(result, var):
    """Return (beta, se, p, stars) for a variable."""
    if var not in result.params.index:
        return (np.nan, np.nan, np.nan, "")
    b = result.params[var]
    se = result.bse[var]
    p = result.pvalues[var]
    stars = ""
    if p < 0.001:
        stars = "***"
    elif p < 0.01:
        stars = "**"
    elif p < 0.05:
        stars = "*"
    elif p < 0.10:
        stars = "†"
    return (b, se, p, stars)

# ---------------------------------------------------------------------------
# 7. Run Cols 1-4
# ---------------------------------------------------------------------------
# Shared RHS (excluding fixed effects)
rhs = " + ".join(BASE_CONTROLS)
fe = " + C(State) + C(Year)"

# Col 1: Green_Bond_Issued (LPM)
f1 = f"Green_Bond_Issued ~ {rhs}{fe}"
c1 = run_reg(f1, s14, "Col 1: Green_Bond_Issued (LPM)")

# Col 2: asinh_green_amt
f2 = f"asinh_green_amt ~ {rhs}{fe}"
c2 = run_reg(f2, s14, "Col 2: asinh_green_amt (OLS)")

# Col 3: Y_self_green (LPM) — PIVOT
f3 = f"Y_self_green ~ {rhs}{fe}"
c3 = run_reg(f3, s14, "Col 3: Y_self_green (LPM)  — STEP 3 PIVOT")

# Col 4: asinh_self_green_amt
f4 = f"asinh_self_green_amt ~ {rhs}{fe}"
c4 = run_reg(f4, s14, "Col 4: asinh_self_green_amt (OLS)")

# ---------------------------------------------------------------------------
# 8. Col 5: triple interaction
# ---------------------------------------------------------------------------
# Terms:
#   main:     npdes, overflow, Rep_Mayor_lag1, fiscal_stress_pca_lag2
#   2-way:    npdes*Rep_Mayor, overflow*Rep_Mayor, npdes*fiscal_stress
#   3-way:    npdes*fiscal_stress*Rep_Mayor
#
# statsmodels formula: A*B*C expands to A + B + C + A:B + A:C + B:C + A:B:C
# We build the triple and add the overflow:Rep interaction separately.
base_no_rep = [c for c in BASE_CONTROLS
               if c not in ("Rep_Mayor_lag1", "epa_npdes_formal_prior3yr_muni")]
rhs5 = " + ".join(base_no_rep)
f5 = (
    "Green_Bond_Issued ~ "
    + "epa_npdes_formal_prior3yr_muni * Rep_Mayor_lag1 * fiscal_stress_pca_lag2"
    + " + epa_overflow_events_muni * Rep_Mayor_lag1"
    + " + " + rhs5
    + fe
)
c5 = run_reg(f5, s5, "Col 5: Green_Bond_Issued w/ triple interaction")

# ---------------------------------------------------------------------------
# 9. Assemble the compact Table 1 output
# ---------------------------------------------------------------------------
key_vars = [
    ("epa_npdes_formal_prior3yr_muni", "NPDES formal x prior3yr (muni)"),
    ("epa_overflow_events_muni", "Overflow events (muni)"),
    ("Rep_Mayor_lag1", "Rep Mayor (lag 1)"),
    ("charges_to_own_source", "Charges / own-source revenue"),
    ("reserve_ratio_lag2", "Reserve ratio (lag 2)"),
    ("tel_stringency_normalized", "TEL stringency (normalized)"),
    ("cwsrf_log_obligations_lag2", "log CWSRF obligations (lag 2)"),
    ("log_cwns_needs_real_lag2", "log CWNS needs (lag 2)"),
    ("fn_pct_deficient_lag2", "Pct deficient (lag 2)"),
    ("log_population_lag2", "log Population (lag 2)"),
    ("log_percapita_income_lag2", "log Per-capita income (lag 2)"),
    ("unemployment_city_lag2", "Unemployment (lag 2)"),
    ("has_substitute_issuer", "Has substitute issuer"),
    ("mkt_state_green_bond_ever_lag1", "State green bond ever (lag 1)"),
    ("fn_esg_has_muni_bond_law", "State has muni bond law"),
    ("state_rep_trifecta", "State Rep trifecta"),
    # Col 5 interaction terms
    ("epa_npdes_formal_prior3yr_muni:Rep_Mayor_lag1", "NPDES × Rep"),
    ("epa_overflow_events_muni:Rep_Mayor_lag1", "Overflow × Rep"),
    ("epa_npdes_formal_prior3yr_muni:fiscal_stress_pca_lag2",
     "NPDES × fiscal_stress"),
    ("Rep_Mayor_lag1:fiscal_stress_pca_lag2", "Rep × fiscal_stress"),
    ("epa_npdes_formal_prior3yr_muni:Rep_Mayor_lag1:fiscal_stress_pca_lag2",
     "NPDES × Rep × fiscal_stress (TRIPLE)"),
    ("fiscal_stress_pca_lag2", "Fiscal stress PCA (lag 2)"),
]

results_by_col = {"C1": c1, "C2": c2, "C3": c3, "C4": c4, "C5": c5}

rows = []
for var, label in key_vars:
    row = {"variable": label}
    for col_name, r in results_by_col.items():
        b, se, p, st = coef_row(r, var)
        if np.isnan(b):
            row[col_name] = ""
            row[f"{col_name}_se"] = ""
        else:
            row[col_name] = f"{b:.4f}{st}"
            row[f"{col_name}_se"] = f"({se:.4f})"
    rows.append(row)

summary_df = pd.DataFrame(rows)

# Add fit stats row
stats_rows = []
for stat_name, getter in [
    ("N", lambda r: f"{int(r.nobs)}"),
    ("R²", lambda r: f"{r.rsquared:.4f}"),
    ("State FE", lambda r: "Yes"),
    ("Year FE", lambda r: "Yes"),
    ("City clustering", lambda r: "Yes"),
]:
    row = {"variable": stat_name}
    for col_name, r in results_by_col.items():
        row[col_name] = getter(r)
        row[f"{col_name}_se"] = ""
    stats_rows.append(row)

summary_df = pd.concat([summary_df, pd.DataFrame(stats_rows)], ignore_index=True)
summary_df.to_csv(OUT / "table1_coefficients.csv", index=False)

# ---------------------------------------------------------------------------
# 10. Pretty-printed text table
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("TABLE 1 — Compulsion Pipeline — Key Coefficients")
print("=" * 100)

col_widths = {"variable": 45, "C1": 13, "C2": 13, "C3": 13, "C4": 13, "C5": 13}
header = f'{"variable":45s} {"C1":>13s} {"C2":>13s} {"C3":>13s} {"C4":>13s} {"C5":>13s}'
header_desc = f'{" ":45s} {"Bloomberg":>13s} {"asinh green":>13s} {"Self-green":>13s} {"asinh self":>13s} {"Triple int":>13s}'
print(header)
print(header_desc)
print("-" * 110)

for _, r in summary_df.iterrows():
    line = f'{str(r["variable"])[:44]:45s}'
    for c in ["C1", "C2", "C3", "C4", "C5"]:
        line += f' {str(r[c])[:12]:>13s}'
    print(line)
    # SE row
    has_se = any(r.get(f"{c}_se") for c in ["C1","C2","C3","C4","C5"])
    if has_se:
        se_line = " " * 45
        for c in ["C1","C2","C3","C4","C5"]:
            se_line += f' {str(r.get(f"{c}_se",""))[:12]:>13s}'
        print(se_line)

print("-" * 110)
print("Stars: † p<0.10, * p<0.05, ** p<0.01, *** p<0.001")
print("All columns: State + Year FE, standard errors clustered at city (FIPS)")
print(f"Cols 1-4 sample: {int(c1.nobs)} city-years, 2015-2025")
print(f"Col 5 sample:    {int(c5.nobs)} city-years, 2015-2023 (fiscal_stress_pca_lag2 restricts)")

# ---------------------------------------------------------------------------
# 11. Save text version for the author
# ---------------------------------------------------------------------------
text_out = []
text_out.append("=" * 100)
text_out.append("TABLE 1 — The Compulsion Pipeline")
text_out.append("Paper: When Do Red and Blue Go Green?")
text_out.append("=" * 100)
text_out.append("")
text_out.append("Hypotheses: H1a (compulsion drives issuance regardless of party)")
text_out.append("            H1b (Rep_Mayor null at extensive margin conditional on compulsion)")
text_out.append("")
text_out.append(header)
text_out.append(header_desc)
text_out.append("-" * 110)
for _, r in summary_df.iterrows():
    line = f'{str(r["variable"])[:44]:45s}'
    for c in ["C1", "C2", "C3", "C4", "C5"]:
        line += f' {str(r[c])[:12]:>13s}'
    text_out.append(line)
    has_se = any(r.get(f"{c}_se") for c in ["C1","C2","C3","C4","C5"])
    if has_se:
        se_line = " " * 45
        for c in ["C1","C2","C3","C4","C5"]:
            se_line += f' {str(r.get(f"{c}_se",""))[:12]:>13s}'
        text_out.append(se_line)
text_out.append("-" * 110)
text_out.append("Stars: † p<0.10, * p<0.05, ** p<0.01, *** p<0.001")
text_out.append("All columns: State + Year FE, standard errors clustered at city (FIPS)")
text_out.append(f"Cols 1-4: N={int(c1.nobs)}, window 2015-2025")
text_out.append(f"Col 5:    N={int(c5.nobs)}, window 2015-2023 (fiscal_stress_pca_lag2 restricts)")
text_out.append("")
text_out.append("Memo hypothesis predictions:")
text_out.append("  C1 Rep_Mayor: expected NULL (H1b) — compulsion overrides partisan preference")
text_out.append("  C3 Rep_Mayor: expected NEGATIVE — first discretionary step, partisan identity enters")
text_out.append("  C5 NPDES × Rep × fiscal_stress: expected POSITIVE triple interaction —")
text_out.append("    fiscally-distressed Republican mayors pulled into green market instrumentally")

(OUT / "table1_results.txt").write_text("\n".join(text_out))
print(f"\nWritten: {OUT / 'table1_results.txt'}")
print(f"         {OUT / 'table1_coefficients.csv'}")

# ---------------------------------------------------------------------------
# 12. Compact interpretation of key memo predictions
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("MEMO HYPOTHESIS CHECK")
print("=" * 100)

def interp(result, var, expected_sign, col_label, hypothesis):
    b, se, p, st = coef_row(result, var)
    if np.isnan(b):
        print(f"  {col_label}: {var} not in model")
        return
    sig = p < 0.05
    actual = "positive" if b > 0 else "negative"
    match = (
        (expected_sign == "positive" and b > 0 and sig) or
        (expected_sign == "negative" and b < 0 and sig) or
        (expected_sign == "null" and not sig)
    )
    verdict = "✓ matches" if match else "✗ does not match"
    print(f"  [{col_label} | {hypothesis}] {var}")
    print(f"     Expected: {expected_sign}")
    print(f"     Actual:   β = {b:.4f} (SE={se:.4f}, p={p:.4f}) — {actual}{st}")
    print(f"     Verdict:  {verdict}")

print("\nH1b — Rep_Mayor null at extensive margin (Cols 1-2):")
interp(c1, "Rep_Mayor_lag1", "null", "Col 1", "H1b")
interp(c2, "Rep_Mayor_lag1", "null", "Col 2", "H1b")

print("\nStep 3 pivot — Rep_Mayor negative at self-labelling (Cols 3-4):")
interp(c3, "Rep_Mayor_lag1", "negative", "Col 3", "Step 3")
interp(c4, "Rep_Mayor_lag1", "negative", "Col 4", "Step 3")

print("\nH1a — Compulsion positive across the pipeline:")
interp(c1, "epa_npdes_formal_prior3yr_muni", "positive", "Col 1", "H1a")
interp(c3, "epa_npdes_formal_prior3yr_muni", "positive", "Col 3", "H1a")

print("\nCol 5 — Triple interaction (key memo prediction):")
interp(c5, "epa_npdes_formal_prior3yr_muni:Rep_Mayor_lag1:fiscal_stress_pca_lag2",
       "positive", "Col 5", "Triple")
interp(c5, "epa_npdes_formal_prior3yr_muni:Rep_Mayor_lag1",
       "positive", "Col 5", "NPDES × Rep")

print("\n" + "=" * 100)
print("Analysis complete.")
