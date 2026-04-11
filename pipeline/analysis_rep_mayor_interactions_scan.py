"""
Rep_Mayor interaction scan — test whether ANY moderator significantly
interacts with Rep_Mayor in predicting Green_Bond_Issued.

For each candidate moderator Z, run:
  Green_Bond_Issued ~ Rep_Mayor_lag1 * Z + base_controls + C(State) + C(Year)

Record the coefficient on Rep_Mayor_lag1:Z, its SE, p-value, and the
main effect on Rep_Mayor_lag1 (which becomes the effect at Z = 0).

Report sorted by p-value.

Categories scanned:
  1. Compulsion (Family 1a): water violations, NPDES formal/informal, SDWA,
     overflow, all cases, case penalties
  2. Fiscal necessity (Family 1b): reserve ratio, debt service burden,
     TEL stringency, charges_to_own_source, fiscal_stress_pca, CWSRF,
     CWNS, pct_deficient
  3. Structural city characteristics: has_municipal_electric, BPS,
     benchmarking, log_population, has_substitute_issuer, state enterprise
     structure
  4. State institutional (Family 3): state_green_bond_ever, state_rep_
     trifecta, has_bond_bank, GO voter approval, muni bond law, MSRB
     position, signed_utah_antiesg
  5. Climate policy: muni_aaa_yield, state_rps_target_pct, state_carbon
     _price, state_climate_plan_legacy, state_pcap_2024, BPS coalition
  6. Peer effects: state and nearby water cumul
  7. Physical risk: NRI, FEMA disaster, NFIP
  8. Anti-ESG: esg_num_antiesg_laws
  9. Temporal: Year (does the partisan gap widen or narrow over time?)

Outputs: processed/analysis/rep_mayor_interactions_scan.csv
         processed/analysis/rep_mayor_interactions_scan.txt
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*inverted.*")
warnings.filterwarnings("ignore", category=RuntimeWarning)

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "processed"
OUT = PROC / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("REP_MAYOR INTERACTION SCAN — what moderates the partisan gap?")
print("=" * 80)

df = pd.read_csv(PROC / "merged_city_year_panel.csv.gz",
                 compression="gzip", low_memory=False)

# Derived transforms
df["log_population_lag2"] = np.log1p(df["population_city_lag2"])
df["log_percapita_income_lag2"] = np.log1p(df["percapita_income_city_lag2"])
df["log_cwns_needs_real_lag2"] = np.log1p(df["fn_cwns_needs_real_lag2"])
df["epa_water_violations_asinh_lag2"] = np.arcsinh(
    df["epa_water_violations_count_muni_lag2"].fillna(0))
df["epa_sdwa_events_asinh_lag2"] = np.arcsinh(
    df["epa_sdwa_events_milestones_count_muni_lag2"].fillna(0))
df["log_state_water_cumul"] = np.log1p(df["State_Total_Water_Ex_City_Amt_Cumul"])
df["log_nearby_water_cumul_25km"] = np.log1p(df["Nearby_NonState_Water_Total_Amt_25km_Cumul"])
# Year z-score for a cleaner time interaction
df["year_z"] = (df["Year"] - df["Year"].mean()) / df["Year"].std()

# ---------------------------------------------------------------------------
# Base controls (same as Table 1 main spec, minus the variable being tested)
# ---------------------------------------------------------------------------
BASE = [
    "epa_npdes_formal_prior3yr_muni",
    "epa_water_violations_asinh_lag2",
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
REP = "Rep_Mayor_lag1"
OUTCOME = "Green_Bond_Issued"

# ---------------------------------------------------------------------------
# Candidate moderators (one interaction test each)
# ---------------------------------------------------------------------------
# (var, display_name, category)
CANDIDATES = [
    # 1. Compulsion (Family 1a)
    ("epa_water_violations_asinh_lag2", "Water violations asinh", "Compulsion"),
    ("epa_npdes_formal_prior3yr_muni", "NPDES formal prior3yr", "Compulsion"),
    ("epa_sdwa_events_asinh_lag2", "SDWA events asinh", "Compulsion"),
    ("epa_overflow_events_muni_lag2", "Overflow events lag2", "Compulsion"),
    ("epa_case_all_prior3yr_muni", "All EPA cases prior3yr", "Compulsion"),
    # 2. Fiscal necessity (Family 1b)
    ("charges_to_own_source", "Charges / own-source", "Fiscal"),
    ("reserve_ratio_lag2", "Reserve ratio (lag2)", "Fiscal"),
    ("debt_service_burden_lag2", "Debt service burden (lag2)", "Fiscal"),
    ("tel_stringency_normalized", "TEL stringency", "Fiscal"),
    ("fiscal_stress_pca_lag2", "Fiscal stress PCA (lag2)", "Fiscal"),
    ("cwsrf_log_obligations_lag2", "log CWSRF obligations", "Fiscal"),
    ("log_cwns_needs_real_lag2", "log CWNS needs", "Fiscal"),
    ("fn_pct_deficient_lag2", "Pct deficient bridges", "Fiscal"),
    ("budget_flexibility_squeeze_lag2", "Budget flexibility squeeze", "Fiscal"),
    # 3. Structural city
    ("ep_has_muni_electric", "Has muni electric utility", "Structural"),
    ("bcode_bps_adopted", "BPS adopted (bcode)", "Structural"),
    ("bcode_state_bps_adopted", "State BPS adopted", "Structural"),
    ("bcode_benchmark_adopted", "Benchmarking adopted", "Structural"),
    ("log_population_lag2", "log Population (lag2)", "Structural"),
    ("log_percapita_income_lag2", "log PCI (lag2)", "Structural"),
    ("unemployment_city_lag2", "Unemployment (lag2)", "Structural"),
    ("has_substitute_issuer", "Has substitute issuer", "Structural"),
    # 4. State institutional (Family 3)
    ("mkt_state_green_bond_ever_lag1", "State green bond ever", "Institutional"),
    ("fn_esg_has_muni_bond_law", "State has muni bond law", "Institutional"),
    ("state_rep_trifecta", "State Rep trifecta", "Institutional"),
    ("state_dem_governor", "State Dem governor", "Institutional"),
    ("inst_has_bond_bank", "State has bond bank", "Institutional"),
    ("inst_go_voter_approval_required", "State GO voter approval req", "Institutional"),
    ("inst_has_constitutional_debt_limit", "State const debt limit", "Institutional"),
    ("inst_signed_utah_antiesg_letter", "Signed Utah anti-ESG letter", "Institutional"),
    # 5. Climate policy
    ("muni_aaa_yield", "Muni AAA 10Y yield", "Climate policy"),
    ("state_rps_target_pct", "State RPS target %", "Climate policy"),
    ("state_carbon_price_usd", "State carbon price USD", "Climate policy"),
    ("state_climate_plan_legacy", "State climate plan (legacy)", "Climate policy"),
    ("state_pcap_2024", "State PCAP (2024)", "Climate policy"),
    ("state_rggi_member", "State RGGI member", "Climate policy"),
    ("state_catp_member", "State CA cap-and-trade", "Climate policy"),
    # 6. Peer effects (water only)
    ("log_state_water_cumul", "log State water cumul (ex-city)", "Peer"),
    ("log_nearby_water_cumul_25km", "log Nearby water 25km cumul", "Peer"),
    # 7. Physical risk
    ("fema_disaster_any_lag2", "FEMA disaster any (lag2)", "Physical"),
    ("fema_disaster_count_lag2", "FEMA disaster count (lag2)", "Physical"),
    ("nfip_repetitive_loss", "NFIP repetitive loss", "Physical"),
    # 8. Anti-ESG legislation
    ("esg_num_antiesg_laws", "Number of anti-ESG laws", "ESG legislation"),
    ("esg_num_esg_friendly_laws", "Number of ESG-friendly laws", "ESG legislation"),
    ("esg_any_antiesg_law", "Any anti-ESG law", "ESG legislation"),
    # 9. Temporal
    ("year_z", "Year (z-scored)", "Temporal"),
]

# Filter to vars actually in panel
CANDIDATES = [(v, n, c) for v, n, c in CANDIDATES if v in df.columns]
print(f"Testing {len(CANDIDATES)} moderators")

# ---------------------------------------------------------------------------
# Sample: 2013-2025, drop rows missing the core base controls
# ---------------------------------------------------------------------------
sample = df[df.Year.between(2013, 2025)].copy()
core = BASE + [REP, OUTCOME, "FIPS", "State", "Year"]
sample = sample.dropna(subset=core).copy()
print(f"Sample: {len(sample)} city-years, {sample.FIPS.nunique()} cities, 2013-2025")

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def run_one(var):
    """Run Green_Bond_Issued ~ Rep_Mayor_lag1 * var + BASE + FE"""
    data = sample.dropna(subset=[var]).copy()
    # If var is in BASE remove it from BASE to avoid duplicate (its main effect
    # will be in the interaction expansion)
    other = [c for c in BASE if c != var and c != REP]
    rhs = " + ".join(other)
    formula = f"{OUTCOME} ~ {REP}*{var} + {rhs}{FE}"
    try:
        m = smf.ols(formula, data=data).fit(
            cov_type="cluster",
            cov_kwds={"groups": data["FIPS"]},
        )
    except Exception as e:
        return None
    return m, len(data)

def get_coef(m, var):
    if var not in m.params.index:
        return (np.nan, np.nan, np.nan)
    return (m.params[var], m.bse[var], m.pvalues[var])

# ---------------------------------------------------------------------------
# Run all interactions
# ---------------------------------------------------------------------------
results = []
for var, name, cat in CANDIDATES:
    out = run_one(var)
    if out is None:
        results.append({
            "category": cat, "moderator": name, "var": var,
            "int_beta": np.nan, "int_se": np.nan, "int_p": np.nan,
            "rep_main": np.nan, "rep_main_se": np.nan, "rep_main_p": np.nan,
            "n": 0, "error": "fit_failed",
        })
        continue
    m, n = out
    ib, ise, ip = get_coef(m, f"{REP}:{var}")
    rb, rse, rp = get_coef(m, REP)
    results.append({
        "category": cat, "moderator": name, "var": var,
        "int_beta": ib, "int_se": ise, "int_p": ip,
        "rep_main": rb, "rep_main_se": rse, "rep_main_p": rp,
        "n": n, "error": "",
    })

res_df = pd.DataFrame(results)
# Sort by interaction p-value
res_df_sorted = res_df.sort_values("int_p", na_position="last").reset_index(drop=True)

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def stars(p):
    if p is None or np.isnan(p):
        return ""
    if p < 0.001: return "***"
    if p < 0.01:  return "**"
    if p < 0.05:  return "*"
    if p < 0.10:  return "†"
    return ""

print()
print("=" * 115)
print("RESULTS — sorted by interaction p-value")
print("=" * 115)
print(f'{"Rank":>4} {"Category":15s} {"Moderator":35s} {"β (int)":>11s} {"SE":>9s} {"p":>7s} {"":<5s} {"N":>6s}')
print("-" * 115)
for i, r in res_df_sorted.iterrows():
    if pd.isna(r["int_p"]):
        continue
    print(f'{i+1:>4} {r["category"]:15s} {r["moderator"][:34]:35s} '
          f'{r["int_beta"]:>11.5f} {r["int_se"]:>9.5f} '
          f'{r["int_p"]:>7.4f} {stars(r["int_p"]):<5s} '
          f'{int(r["n"]):>6d}')

# Summary: how many significant at different thresholds
n_sig_01 = (res_df["int_p"] < 0.01).sum()
n_sig_05 = (res_df["int_p"] < 0.05).sum()
n_sig_10 = (res_df["int_p"] < 0.10).sum()
n_total = res_df["int_p"].notna().sum()

print("-" * 115)
print(f"Of {n_total} moderators tested:")
print(f"  p < 0.01 : {n_sig_01}")
print(f"  p < 0.05 : {n_sig_05}")
print(f"  p < 0.10 : {n_sig_10}")
print(f"  Bonferroni-adjusted 0.05 threshold = {0.05/n_total:.4f}")
print(f"  Number surviving Bonferroni: "
      f"{(res_df['int_p'] < 0.05/n_total).sum()}")

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
res_df_sorted.to_csv(OUT / "rep_mayor_interactions_scan.csv", index=False)

text = []
text.append("=" * 115)
text.append("Rep_Mayor_lag1 interaction scan — what moderates the partisan gap?")
text.append("=" * 115)
text.append("")
text.append("For each candidate moderator Z, fit:")
text.append("  Green_Bond_Issued ~ Rep_Mayor_lag1 * Z + base_controls + C(State) + C(Year)")
text.append("SE clustered at FIPS. LPM. Sample: 2013-2025, N varies by moderator availability.")
text.append("")
text.append(f'{"Rank":>4} {"Category":15s} {"Moderator":35s} {"β (int)":>11s} {"SE":>9s} {"p":>7s} {"":<5s} {"N":>6s}')
text.append("-" * 115)
for i, r in res_df_sorted.iterrows():
    if pd.isna(r["int_p"]):
        continue
    text.append(f'{i+1:>4} {r["category"]:15s} {r["moderator"][:34]:35s} '
                f'{r["int_beta"]:>11.5f} {r["int_se"]:>9.5f} '
                f'{r["int_p"]:>7.4f} {stars(r["int_p"]):<5s} '
                f'{int(r["n"]):>6d}')
text.append("-" * 115)
text.append(f"Of {n_total} moderators tested:")
text.append(f"  p < 0.01 : {n_sig_01}")
text.append(f"  p < 0.05 : {n_sig_05}")
text.append(f"  p < 0.10 : {n_sig_10}")
text.append(f"  Bonferroni 0.05 threshold: {0.05/n_total:.4f}")
text.append(f"  Surviving Bonferroni: {(res_df['int_p'] < 0.05/n_total).sum()}")

(OUT / "rep_mayor_interactions_scan.txt").write_text("\n".join(text))
print(f"\nWritten: {OUT / 'rep_mayor_interactions_scan.csv'}")
print(f"         {OUT / 'rep_mayor_interactions_scan.txt'}")
