"""
Table 1 Col 5 — interaction panel with the correct compulsion variable.

Tests several interaction structures to identify which (if any) version of
the memo's "compulsion × distress" and "compulsion × distress × Rep_Mayor"
story survives. Runs six variants side-by-side:

  M1: baseline (no interactions) - for reference
  M2: compulsion × distress only (Family 1a × 1b, no partisan)
  M3: compulsion × Rep_Mayor only (Family 1a × 2, no distress)
  M4: compulsion × Rep × distress TRIPLE (Family 1a × 1b × 2) — memo Col 5
  M5: double decomposition — all 2-way interactions without the triple
  M6: both the NPDES (memo) and water_violations compulsion variables in
      the same spec with their respective interactions (horse race)

The compulsion variable is `epa_water_violations_asinh_lag2` — the denser
infraction signal that came out significant and positive at 1% in the
enriched Table 1 main spec. fiscal_stress_pca_lag2 is the distress variable
(restricts sample to 2015-2023 because raw fiscal_stress_pca ends 2021).

Sample: city-years 2015-2023 with Rep_Mayor_lag1 non-missing.
Outcome: Green_Bond_Issued (LPM).
Fixed effects: State + Year.
SE: clustered at FIPS.

Outputs: processed/analysis/table1_col5_interactions.txt
         processed/analysis/table1_col5_interactions.csv
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*inverted.*")

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "processed"
OUT = PROC / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("TABLE 1 Col 5 — Interaction panel")
print("Compulsion × Distress × Rep_Mayor, with the correct compulsion variable")
print("=" * 80)

# ---------------------------------------------------------------------------
# 1. Load panel and derive transforms
# ---------------------------------------------------------------------------
df = pd.read_csv(PROC / "merged_city_year_panel.csv.gz",
                 compression="gzip", low_memory=False)
print(f"\nPanel: {df.shape}")

df["log_population_lag2"] = np.log1p(df["population_city_lag2"])
df["log_percapita_income_lag2"] = np.log1p(df["percapita_income_city_lag2"])
df["log_cwns_needs_real_lag2"] = np.log1p(df["fn_cwns_needs_real_lag2"])
df["epa_water_violations_asinh_lag2"] = np.arcsinh(
    df["epa_water_violations_count_muni_lag2"].fillna(0))

# ---------------------------------------------------------------------------
# 2. Base controls (same as Table 1 main spec, MINUS the compulsion vars
#    and fiscal_stress — those are the focus of interactions here)
# ---------------------------------------------------------------------------
BASE = [
    "charges_to_own_source",
    "reserve_ratio_lag2",
    "tel_stringency_normalized",
    "cwsrf_log_obligations_lag2",
    "log_cwns_needs_real_lag2",
    "fn_pct_deficient_lag2",
    "log_population_lag2",
    "log_percapita_income_lag2",
    "unemployment_city_lag2",
    "has_substitute_issuer",
    "mkt_state_green_bond_ever_lag1",
    "fn_esg_has_muni_bond_law",
    "state_rep_trifecta",
]
FE = " + C(State) + C(Year)"

# ---------------------------------------------------------------------------
# 3. Sample: 2015-2023 (bounded by fiscal_stress_pca_lag2)
# ---------------------------------------------------------------------------
needed = BASE + [
    "epa_water_violations_asinh_lag2",
    "epa_npdes_formal_prior3yr_muni",
    "Rep_Mayor_lag1",
    "fiscal_stress_pca_lag2",
    "Green_Bond_Issued",
    "FIPS", "State", "Year",
]
sample = df[df.Year.between(2015, 2023)].copy()
sample = sample.dropna(subset=needed).copy()
print(f"Sample: {len(sample)} city-years, {sample.FIPS.nunique()} cities, 2015-2023")

# ---------------------------------------------------------------------------
# 4. Helper
# ---------------------------------------------------------------------------
def run_reg(formula, data, label):
    m = smf.ols(formula, data=data)
    r = m.fit(cov_type="cluster", cov_kwds={"groups": data["FIPS"]})
    print(f"\n--- {label} ---")
    print(f"  N     = {int(r.nobs)}")
    print(f"  R²    = {r.rsquared:.4f}")
    return r

def coef(r, var):
    if var not in r.params.index:
        return (np.nan, np.nan, np.nan, "")
    b = r.params[var]
    se = r.bse[var]
    p = r.pvalues[var]
    st = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "†" if p < 0.10 else ""
    return (b, se, p, st)

def fmt(r, var):
    b, se, p, st = coef(r, var)
    if np.isnan(b):
        return "", ""
    return f"{b:.5f}{st}", f"({se:.5f})"

# ---------------------------------------------------------------------------
# 5. The six specifications
# ---------------------------------------------------------------------------
CMP = "epa_water_violations_asinh_lag2"    # compulsion (correct variable)
NPD = "epa_npdes_formal_prior3yr_muni"     # compulsion (memo's original)
REP = "Rep_Mayor_lag1"                     # partisan
DIS = "fiscal_stress_pca_lag2"             # distress

rhs_base = " + ".join(BASE)

# M1: baseline — compulsion + Rep + distress as main effects, no interactions
f1 = f"Green_Bond_Issued ~ {CMP} + {REP} + {DIS} + {rhs_base}{FE}"
m1 = run_reg(f1, sample, "M1: Baseline (no interactions)")

# M2: compulsion × distress (Family 1a × 1b, no partisan)
f2 = f"Green_Bond_Issued ~ {CMP}*{DIS} + {REP} + {rhs_base}{FE}"
m2 = run_reg(f2, sample, "M2: Compulsion × Distress")

# M3: compulsion × Rep (Family 1a × 2, no distress)
f3 = f"Green_Bond_Issued ~ {CMP}*{REP} + {DIS} + {rhs_base}{FE}"
m3 = run_reg(f3, sample, "M3: Compulsion × Rep_Mayor")

# M4: compulsion × Rep × distress TRIPLE
f4 = f"Green_Bond_Issued ~ {CMP}*{REP}*{DIS} + {rhs_base}{FE}"
m4 = run_reg(f4, sample, "M4: Compulsion × Rep × Distress (TRIPLE)")

# M5: all 2-way interactions without triple (compulsion×Rep + compulsion×distress + Rep×distress)
f5 = (
    f"Green_Bond_Issued ~ {CMP} + {REP} + {DIS} "
    f"+ {CMP}:{REP} + {CMP}:{DIS} + {REP}:{DIS} + {rhs_base}{FE}"
)
m5 = run_reg(f5, sample, "M5: All 2-way interactions (no triple)")

# M6: horse race — both compulsion measures with their own interactions
f6 = (
    f"Green_Bond_Issued ~ {CMP} + {NPD} + {REP} + {DIS} "
    f"+ {CMP}:{REP} + {CMP}:{DIS} + {NPD}:{REP} + {NPD}:{DIS} + {REP}:{DIS} "
    f"+ {rhs_base}{FE}"
)
m6 = run_reg(f6, sample, "M6: Horse race (water_violations vs NPDES formal)")

# ---------------------------------------------------------------------------
# 6. Compact interactions table
# ---------------------------------------------------------------------------
models = {"M1": m1, "M2": m2, "M3": m3, "M4": m4, "M5": m5, "M6": m6}
key_terms = [
    (CMP, "Water violations asinh (lag2)"),
    (NPD, "NPDES formal prior3yr (muni)"),
    (REP, "Rep Mayor (lag 1)"),
    (DIS, "Fiscal stress PCA (lag 2)"),
    (f"{CMP}:{REP}", "Water viol × Rep"),
    (f"{CMP}:{DIS}", "Water viol × distress"),
    (f"{REP}:{DIS}", "Rep × distress"),
    (f"{CMP}:{REP}:{DIS}", "Water viol × Rep × distress (TRIPLE)"),
    (f"{NPD}:{REP}", "NPDES formal × Rep"),
    (f"{NPD}:{DIS}", "NPDES formal × distress"),
]

rows = []
for var, label in key_terms:
    row = {"term": label}
    for name, m in models.items():
        b, se = fmt(m, var)
        row[name] = b
        row[f"{name}_se"] = se
    rows.append(row)

# Fit stats
for name, getter in [("N", lambda r: f"{int(r.nobs)}"),
                     ("R²", lambda r: f"{r.rsquared:.4f}")]:
    row = {"term": name}
    for mname, m in models.items():
        row[mname] = getter(m)
        row[f"{mname}_se"] = ""
    rows.append(row)

out_df = pd.DataFrame(rows)
out_df.to_csv(OUT / "table1_col5_interactions.csv", index=False)

# ---------------------------------------------------------------------------
# 7. Pretty print
# ---------------------------------------------------------------------------
print("\n" + "=" * 110)
print("COL 5 INTERACTION PANEL — coefficients")
print("=" * 110)
header = f'{"term":45s} {"M1":>11s} {"M2":>11s} {"M3":>11s} {"M4":>11s} {"M5":>11s} {"M6":>11s}'
sub = f'{" ":45s} {"base":>11s} {"C×D":>11s} {"C×R":>11s} {"triple":>11s} {"2-way":>11s} {"horse":>11s}'
print(header)
print(sub)
print("-" * 120)
for _, r in out_df.iterrows():
    line = f'{str(r["term"])[:44]:45s}'
    for c in ["M1","M2","M3","M4","M5","M6"]:
        line += f' {str(r[c])[:10]:>11s}'
    print(line)
    if any(r.get(f"{c}_se") for c in ["M1","M2","M3","M4","M5","M6"]):
        se_line = " " * 45
        for c in ["M1","M2","M3","M4","M5","M6"]:
            se_line += f' {str(r.get(f"{c}_se",""))[:10]:>11s}'
        print(se_line)
print("-" * 120)
print("Stars: † p<0.10, * p<0.05, ** p<0.01, *** p<0.001")
print("All: State + Year FE, SE clustered at city (FIPS)")
print(f"Sample: {int(m1.nobs)} city-years, 2015-2023 (bounded by fiscal_stress_pca_lag2)")
print()

# ---------------------------------------------------------------------------
# 8. Interpretation
# ---------------------------------------------------------------------------
print("=" * 110)
print("INTERPRETATION")
print("=" * 110)

def interp(m, var, expected, hypothesis):
    b, se, p, st = coef(m, var)
    if np.isnan(b):
        return
    match = (
        (expected == "positive" and b > 0 and p < 0.05) or
        (expected == "negative" and b < 0 and p < 0.05) or
        (expected == "null" and p >= 0.05)
    )
    verdict = "✓ matches" if match else "✗ does not match"
    print(f"  {hypothesis}: {var}")
    print(f"     β = {b:.5f} (SE={se:.5f}, p={p:.4f}) {st}")
    print(f"     Expected: {expected} — {verdict}")
    print()

print("\n-- M2: Compulsion × Distress (no partisan moderation) --")
print("Memo implication: fiscal distress should amplify the compulsion effect")
print("(stressed cities under compulsion issue MORE green bonds instrumentally)")
interp(m2, f"{CMP}:{DIS}", "positive", "H1a amplification")

print("\n-- M3: Compulsion × Rep_Mayor (no distress) --")
print("Memo implication: compulsion should NARROW the partisan gap (Republicans")
print("pulled in by enforcement, which would give a positive interaction)")
interp(m3, f"{CMP}:{REP}", "positive", "H1b attenuation")

print("\n-- M4: Triple interaction (memo's Col 5 primary prediction) --")
print("Memo: fiscally distressed Republican mayors pulled in instrumentally")
print("under compulsion — positive triple expected")
interp(m4, f"{CMP}:{REP}:{DIS}", "positive", "Col 5 triple")
print("Plus the 2-way building blocks:")
interp(m4, f"{CMP}:{REP}", "positive", "  C × R")
interp(m4, f"{CMP}:{DIS}", "positive", "  C × D")
interp(m4, f"{REP}:{DIS}", None, "  R × D (no prior)")

print("\n-- M6: Horse race between NPDES formal (memo) and water violations --")
print("Which compulsion measure is the identified one?")
for label, var in [("NPDES × R", f"{NPD}:{REP}"),
                    ("Water viol × R", f"{CMP}:{REP}"),
                    ("NPDES × D", f"{NPD}:{DIS}"),
                    ("Water viol × D", f"{CMP}:{DIS}")]:
    b, se, p, st = coef(m6, var)
    if not np.isnan(b):
        print(f"  {label}: β = {b:.5f} (p={p:.4f}) {st}")

# ---------------------------------------------------------------------------
# 9. Save text output for author
# ---------------------------------------------------------------------------
text = []
text.append("=" * 110)
text.append("TABLE 1 Col 5 — Interaction panel")
text.append("Testing the compulsion × distress × Rep_Mayor story")
text.append("=" * 110)
text.append("")
text.append("Six specifications (all with State + Year FE, city-clustered SEs):")
text.append("  M1: baseline (no interactions)")
text.append("  M2: compulsion × distress (Family 1a × 1b)")
text.append("  M3: compulsion × Rep_Mayor (Family 1a × 2)")
text.append("  M4: compulsion × Rep × distress TRIPLE (memo Col 5 target)")
text.append("  M5: all 2-way interactions without triple")
text.append("  M6: horse race — NPDES formal vs water_violations_asinh")
text.append("")
text.append(header)
text.append(sub)
text.append("-" * 120)
for _, r in out_df.iterrows():
    line = f'{str(r["term"])[:44]:45s}'
    for c in ["M1","M2","M3","M4","M5","M6"]:
        line += f' {str(r[c])[:10]:>11s}'
    text.append(line)
    if any(r.get(f"{c}_se") for c in ["M1","M2","M3","M4","M5","M6"]):
        se_line = " " * 45
        for c in ["M1","M2","M3","M4","M5","M6"]:
            se_line += f' {str(r.get(f"{c}_se",""))[:10]:>11s}'
        text.append(se_line)
text.append("-" * 120)
text.append("Stars: † p<0.10, * p<0.05, ** p<0.01, *** p<0.001")
text.append(f"Sample: {int(m1.nobs)} city-years, 2015-2023 "
            f"(bounded by fiscal_stress_pca_lag2 raw ending 2021)")

(OUT / "table1_col5_interactions.txt").write_text("\n".join(text))
print(f"\nWritten: {OUT / 'table1_col5_interactions.txt'}")
print(f"         {OUT / 'table1_col5_interactions.csv'}")
