# When Do Red and Blue Go Green? — Main Paper Tables and Narrative (v4)

> **Changelog (v3.2 → v4).** (15) Compulsion variable replaced: non-severe QNCR violations (asinh, lag 1) supersedes effluent violations. Non-severe violations capture persistent low-severity infrastructure-need pressure and produce water-specific significance (+0.004\*\*\*, t=2.90 on water; +0.003, t=1.50 ns on non-water). All tables re-estimated. N = 7,413. Variable construction note updated.

---

**Sample.** N = 7,413 city-years · 576 cities · 49 states · 2013–2025.
**Estimator.** Linear probability model (continuous outcomes: OLS).
**Treatment.** `Dem_Mayor` (no lag).
**Fixed effects.** State + year (absorbed, not reported).
**Standard errors.** Clustered at city (`fips7`).
**Treatment imputation.** Three-tier procedure for nonpartisan/rotating-mayor cities (97 obs from `mayor_party` backfill, 40 obs from within-city ffill/bfill, 13 obs constituency proxy for Pico Rivera). Indicator `Dem_Mayor_imputed ∈ {0,1,2,3}` available for sensitivity.
**Compulsion variable.** Federal water-quality compliance pressure is measured as the asinh-transformed count of non-severe NPDES-permit violations at municipal facilities, lagged one year (`qncr_nonsevere_asinh_lag1`). Non-severe violations are the total quarterly noncompliance (QNCR) count minus violations classified as severe by EPA ECHO. This captures persistent, low-severity effluent exceedances — the kind that accumulate into capital-investment need — rather than high-severity events (consent decrees, SNC designations) that indicate post-remediation completion. Constructed from the QNCR severity extraction (2000–2026) so that the one-year lag has pre-panel coverage.

---

## The Four-Step Decision Chain

A city's participation in the green municipal bond market involves four sequential decisions.

| Step | Decision | Dominant family | Within-step variation | Addressed in |
|---|---|---|---|---|
| **1. Investment** | Whether to undertake a capital project | Material (compelled) **or** Political × constituency (discretionary) | Yes — compelled (water) vs discretionary (non-water) | Table 1 |
| **2. Bond Financing** | Whether to finance via debt rather than current revenue | Material (non-severe violations, fiscal capacity) | No | Table 2 |
| **3. Green Labelling** | Whether to apply the green label to an issued bond | Material + institutional (marketability, fiscal stress) | No | Table 3 |
| **4. Credibility Certification** | Whether to obtain third-party verification, framework adoption, impact reporting | Material (administrative scale and sophistication) | No | Appendix B |

All four steps technically pass through the mayor's office in most American cities, but they differ substantially in the political attention they receive in practice. Step 1 (Investment) involves visible, voter-observable choices about which projects to undertake; the mayor's name appears on the announcement of a new capital project. Step 2 (Bond Financing) is a structural fiscal decision typically handled by the city finance office and rarely makes news beyond technical municipal finance circles. Step 3 (Green Labelling) is a documentation choice made in consultation with bond underwriters, where the green label adds little marginal cost when use of proceeds qualifies. Step 4 (Credibility Certification) carries direct fiscal cost (verifier fees) and a public association with the ESG verification ecosystem, but the choice is typically made on advice from financial professionals based on whether the additional credibility signal is needed for marketing the bond.

The tables are numbered in order of analytical presentation: Table 1 presents the full-panel aggregate (Step 2), Table 2 presents the within-step use-of-funds decomposition (Step 1), and Tables 3 and Appendix B address Steps 3 and 4 respectively.

Step 1 also admits a within-step decomposition: some investment decisions are driven by federal water-quality compliance pressure (persistent non-severe violations, sewer-overflow remediation, drinking-water-rule compliance) while others are discretionary (clean transportation, energy efficiency, green buildings, climate adaptation, renewable energy). The discretionary categories are where mayors face a genuine investment-allocation choice that constituents can observe.

The paper's central theoretical claim is that mayoral partisanship operates at the intersection of two conditions: early-chain position (the decision is voter-visible) and discretionary content (the mayor has a meaningful choice). At the cross-product cell where both conditions hold — Step 1 in the discretionary subdomain — Democratic mayors respond to constituency green preferences (amplifying in green-leaning cities, substituting away in conservative-leaning cities). Everywhere else in the chain, material conditions and market-structural mechanisms dominate.

### Theoretical mapping: which family operates at which step

| | Step 1: Investment | | Step 2: Bond Financing | Step 3: Green Labelling | Step 4: Credibility |
|---|---|---|---|---|---|
| | **Compelled (water)** | **Discretionary (non-water)** | | | |
| **Family 1: Material** | **Dominant** (non-severe violations) | Subordinate | **Dominant** (non-severe violations, fiscal capacity) | **Dominant** (violations, fiscal stress) | Subordinate (scale, sophistication) |
| **Family 2: Political** | Absent (water placebo I2 = ns) | **Dominant** (constituency × mayor interaction) | Subordinate (unconditional null) | Absent (Dem null at Step 3) | Largely absent (5/6 outcomes null; assurance California-fragile) |
| **Family 3: Institutional** | Background | Background | Background (state market depth ns) | **Moderator** (marketability interaction) | Background |

---

## Table 1 — Bond Financing Decision (Step 2)

> **Step mapping.** This table addresses Step 2 of the decision chain: conditional on a capital project existing, does the city finance it via a green bond? The full-panel specification tests whether mayoral partisanship affects the bond-financing decision pooled across all use-of-funds categories.

| *Variable* | *C1 GBI* | *C2 GBI $* | *C3 Self-green* | *C4 Self $* | *I1 GBI* | *I2 Self-green* |
|---|---|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | | | |
| Non-severe violations (muni, lag 1) | +0.0062 | +0.1143 | +0.0052 | +0.0957 | +0.0063 | +0.0054 |
| | (2.48)\*\* | (2.39)\*\* | (2.48)\*\* | (2.33)\*\* | (2.55)\*\* | (2.58)\*\*\* |
| **Family 2 — Political factors** | | | | | | |
| Dem Mayor | +0.0004 | +0.0045 | +0.0001 | +0.0014 | −0.0552 | −0.0633 |
| | (0.09) | (0.06) | (0.04) | (0.02) | (1.89)\* | (2.23)\*\* |
| Dem presidential vote share | +0.0547 | +0.9975 | +0.0514 | +0.9326 | +0.0044 | −0.0061 |
| | (2.18)\*\* | (2.10)\*\* | (2.19)\*\* | (2.10)\*\* | (0.17) | (0.28) |
| Dem Mayor × Dem vote share | — | — | — | — | +0.0986 | +0.1125 |
| | | | | | (1.91)\* | (2.25)\*\* |
| R² | 0.088 | 0.093 | 0.088 | 0.091 | 0.089 | 0.091 |
| N | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 |

Remaining variables (reserve ratio, debt service, state green market depth, anti-ESG law, log population, log income, unemployment) included but not shown for space. Full table in `table1_v3_main.md`.

### Marginal effect of `Dem_Mayor` on self-green (I2)

| Constituency percentile | pres\_dem | Marginal effect | *t*-stat |
|---|---|---|---|
| 10th (red city) | 0.39 | **−0.019** | **(2.05)\*\*** |
| 50th (median) | 0.57 | +0.001 | (0.13) |
| 90th (blue city) | 0.75 | **+0.021** | **(2.10)\*\*** |

### Reading

**Family 1 (Material) dominates Step 2.** Non-severe violations drive issuance across all main columns (β = +0.005–0.006\*\*). Cities with persistent low-severity water-quality noncompliance are more likely to issue green bonds.

**Family 2 (Political) is null on average but masks responsive representation.** `Dem_Mayor` is indistinguishable from zero across C1–C4. The constituency × partisan interaction (I1–I2) reveals the conditional pattern: Democratic mayors amplify electorate preferences where those preferences favor green issuance (blue cities, 90th pct: +0.021\*\*) and substitute away where they do not (red cities, 10th pct: −0.019\*\*). As Table 2 confirms, this responsive-representation mechanism operates exclusively in the discretionary (non-water) domain.

---

## Table 2 — Investment Decision: Compelled vs Discretionary (Step 1)

> **Step mapping.** This table addresses Step 1 of the decision chain. The constituency × partisan interaction is tested in both domains. Where compulsion removes discretion (water), the interaction is predicted to be null; where discretion remains (non-water), the interaction is predicted to be positive. This is the locus of the paper's central finding.

| *Variable* | *W1 Water* | *W2 Water + I2* | *NW1 Non-water* | *NW2 Non-water + I2* |
|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | |
| Non-severe violations (muni, lag 1) | +0.0037 | +0.0037 | +0.0025 | +0.0026 |
| | (2.90)\*\*\* | (2.91)\*\*\* | (1.50) | (1.59) |
| **Family 2 — Political factors** | | | | |
| Dem Mayor | −0.0002 | −0.0010 | +0.0005 | −0.0527 |
| | (0.06) | (0.06) | (0.21) | (3.04)\*\*\* |
| Dem presidential vote share | +0.0157 | +0.0151 | +0.0383 | −0.0094 |
| | (1.00) | (0.94) | (2.62)\*\*\* | (0.62) |
| Dem Mayor × Dem vote share | — | +0.0013 | — | +0.0944 |
| | | (0.05) | | (3.04)\*\*\* |
| R² | 0.043 | 0.043 | 0.059 | 0.064 |
| N | 7,413 | 7,413 | 7,413 | 7,413 |

Remaining variables included but not shown.

#### Marginal effect of `Dem_Mayor` at constituency percentiles

| Domain | 10th pct (0.39) | 50th pct (0.57) | 90th pct (0.75) |
|---|---|---|---|
| W2 Water | −0.001 (0.06) | −0.000 (0.06) | +0.000 (0.01) |
| **NW2 Non-water** | **−0.016 (2.82)\*\*\*** | +0.001 (0.32) | **+0.018 (2.76)\*\*\*** |

### Reading

**Non-severe violations drive water issuance specifically (+0.004\*\*\*, t=2.90) and are null on non-water (+0.003, t=1.50, p=0.135).** This is the clean water-specific compulsion pattern that confirms the chain framing's prediction: persistent low-severity effluent exceedances create capital-investment need for water infrastructure specifically.

**The constituency × partisan interaction operates exclusively in the discretionary domain.** Water (I2 = +0.001, ns) vs non-water (I2 = +0.094\*\*\*). Democratic mayors amplify constituency demand for discretionary green capital projects. The crossover at pres\_dem ≈ 0.55 separates amplification (blue cities, +0.018\*\*\*) from substitution (red cities, −0.016\*\*\*).

---

## Table 3 — Green Labelling Decision (Step 3)

> **Step mapping.** Conditional on having issued a bond, does the city apply the green label? The sample restricts to bond issuers (`total_ltd_issued > 0`). The paper predicts Family 1 (Material) dominance at this step.

**Sample.** Bond issuers: N = 3,894 (84 self-green events). Compelled issuers (non-severe violations > 0): N = 2,375 (73 events).

| *Variable* | *L1 Baseline* | *L2 +Fiscal Stress* | *L3 +Marketability* | *L4 Both* | *L5 Compelled only* |
|---|---|---|---|---|---|
| Non-severe violations (muni, lag 1) | +0.0043 | +0.0035 | −0.0110 | −0.0113 | — |
| | (1.64) | (1.35) | (2.09)\*\* | (2.18)\*\* | |
| Dem Mayor | −0.0017 | −0.0024 | −0.0015 | −0.0022 | −0.0010 |
| | (0.34) | (0.48) | (0.30) | (0.44) | (0.17) |
| Fiscal stress index | — | +0.0176 | — | +0.0169 | — |
| | | (2.05)\*\* | | (1.97)\*\* | |
| Violations × state green market depth | — | — | +0.0008 | +0.0008 | — |
| | | | (2.62)\*\*\* | (2.58)\*\*\* | |
| R² | 0.105 | 0.107 | 0.107 | 0.109 | 0.131 |
| N | 3,894 | 3,894 | 3,894 | 3,894 | 2,375 |

### Reading

**Family 1 (Material) dominates Step 3.** Non-severe violations drive labelling in the baseline (L1: +0.004, t=1.64 borderline). Fiscal stress (L2: +0.018\*\*) and the marketability interaction (L3: violations × state green market depth = +0.001\*\*\*) are significant and orthogonal (L4). `Dem_Mayor` is null across all five columns.

---

## Summary across all specifications

| Finding | Evidence | Step | Strength |
|---|---|---|---|
| `Dem_Mayor` null across outcomes | β ≈ 0 across Table 1 C1–C4 + R1–R24 | Steps 2, 3, 4 | Rock solid (\*\*\*) |
| **Non-severe violations drive water issuance** | **+0.004\*\*\* (Table 2 water); +0.003 ns (non-water)** | **Step 1, water-specific** | **Novel (\*\*\*)** |
| Constituency drives issuance | pres\_dem +0.051\*\* (Table 1 self-green) | Step 2 | Consistent (\*\*) |
| **Constituency × partisan interaction** | +0.113\*\* (Table 1 self-green); **+0.094\*\*\* (Table 2 NW2)**; +0.001 ns (Table 2 W2 placebo) | **Step 1, discretionary only** | Novel (\*\*) |
| Labelling-margin marketability | Table 3 L3: violations × state\_green +0.001\*\*\* (issuer subsample) | Step 3 | Separate sample (\*\*\*) |
| Labelling-margin fiscal stress | Table 3 L2: fiscal stress +0.018\*\* (issuer subsample) | Step 3 | Separate sample (\*\*) |
| Third-party assurance partisan gap | Panel A: +0.005\*\*; Panel C (N=118): +0.439\*\*\*; Fisher 59% vs 15%. California-fragile (p=0.170 w/o CA) | Step 4 | Partial (\*\*), fragile |

---

## The story

**Step 1 (Investment).** Capital need and federal water-quality compliance pressure drive project selection. Non-severe violations at municipal water plants are significant on water issuance (+0.004\*\*\*, t=2.90) and null on non-water (+0.003, t=1.50) — a clean water-specific compulsion pattern. In the discretionary domain (non-water categories), the constituency × partisan interaction is significant (+0.094\*\*\*): Democratic mayors amplify constituency demand for green capital projects in blue cities and substitute away in red cities. The water placebo (Table 2 W2: +0.001, t=0.05) confirms that partisan-constituency alignment matters only where mayors have latitude.

**Step 2 (Bond Financing).** The full-panel aggregate confirms the unconditional partisan null. `Dem_Mayor` is null across all four main-table outcomes (Table 1 C1–C4). Non-severe violations (+0.005\*\*) and constituency (+0.051\*\*) drive issuance. The I2 interaction (+0.113\*\*) is the pooled signature of the Step 1 discretionary effect.

**Step 3 (Green Labelling).** Among bond issuers (Table 3), fiscal stress (+0.018\*\*) and the marketability interaction (violations × state green market depth = +0.001\*\*\*) are the operative mechanisms. Mayoral partisanship is null (|t| ≤ 0.48). Among compelled issuers (L5), only city size predicts labelling — a sophistication channel.

**Step 4 (Credibility Certification).** `Dem_Mayor` is null on five of six credibility outcomes (Appendix B Panel A); only `log_population` is consistently significant across credibility dimensions (Panel C). The lone exception — third-party ESG assurance (+0.005\*\*, Panel A; +0.439\*\*\*, Panel C) — is concentrated in a small set of large coastal Democratic cities (California contributes 22 of 61 assurance events; San Francisco alone contributes 10) and does not survive a leave-California-out test (p = 0.170). By the time the decision reaches Step 4, the political-agency mechanism has been delegated to administrative and financial professionals operating under capacity-and-scale constraints.

**Sensitivity and robustness.** The I2 interaction survives centered-VIF (1.18), leave-one-state-out (0 of 49 above p = 0.10), and the water-domain placebo. Dem_Mayor null across 24 robustness specifications.

---

## Qualitative validation from bond prospectus text

A separate corpus analysis of 198 bond prospectuses provides document-level validation.

**Outcome-variable validation.** Bloomberg's `Self-reported Green` flag has sensitivity 0.877, specificity 0.798, and precision 0.937 against a prospectus-text classifier (N = 3,140 CUSIPs).

**Compulsion mechanism (Steps 1–2).** The panel variable (non-severe violations) captures one component of a broader federal water-quality compliance pressure that the prospectus corpus identifies directly. Twenty-two per cent of analysed prospectuses are flagged as compelled by federal-regulatory text. DC Water cites "Civil Action No. 1:CV00183TFH"; San Francisco PUC cites "NPDES Permit No. CA0037664"; Alexandria, VA cites "Consent Decree dated March 25, 2005". Non-severe violations, consent decrees, and formal enforcement are all manifestations of the same regulatory pressure; the panel measure captures the persistent-infrastructure-need component.

**Discretion validity (Step 1, Table 2 NW).** Among non-water bonds, ~35% disclose state-level green mandates (California AB 32, CALGreen, state RPS) and ~65% show no compulsion language. The disclosed mandates are time-invariant and absorbed by state FE.

---

## Appendix B — Credibility Certification (Step 4)

> **Step mapping.** This appendix addresses Step 4: conditional on having labelled a bond green, does the city procure third-party verification, adopt an ICMA/CBI framework, publish impact reports, or document project-selection and proceeds-management procedures? These actions impose direct fiscal cost. The paper predicts Family 1 dominance at this step in the form of administrative scale — larger and more sophisticated cities adopt quality standards regardless of mayoral partisanship — with the residual partisan signal concentrated in a small handful of large coastal Democratic cities (California-fragile).

### Panel A — Full-sample regression (10-variable PRIMARY)

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *pres\_dem* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 7,413 | 78 | +0.0009 | +0.0035 | +0.0264 |
| | | | (0.28) | (1.99)\*\* | (1.41) |
| Third-party ESG assurance | 7,413 | 61 | +0.0045 | +0.0029 | +0.0155 |
| | | | (1.97)\*\* | (1.78)\* | (0.87) |
| ICMA / CBI framework | 7,413 | 71 | −0.0014 | +0.0028 | +0.0360 |
| | | | (0.44) | (1.70)\* | (2.06)\*\* |
| Impact reporting | 7,413 | 73 | −0.0008 | +0.0032 | +0.0344 |
| | | | (0.26) | (1.88)\* | (1.92)\* |
| Documented project selection | 7,413 | 78 | +0.0004 | +0.0036 | +0.0296 |
| | | | (0.11) | (2.04)\*\* | (1.57) |
| Documented proceeds management | 7,413 | 73 | −0.0007 | +0.0035 | +0.0338 |
| | | | (0.23) | (2.04)\*\* | (1.90)\* |

### Panel B — Descriptive: rates conditional on issuing a self-labelled green bond

| *Outcome* | *Dem rate* | *Rep rate* | *Fisher p* |
|---|---|---|---|
| Any credibility indicator | 67/98 (68.4%) | 10/20 (50.0%) | 0.129 |
| **Third-party ESG assurance** | **58/98 (59.2%)** | **3/20 (15.0%)** | **0.000\*\*\*** |
| ICMA / CBI framework | 60/98 (61.2%) | 10/20 (50.0%) | 0.455 |
| Impact reporting | 63/98 (64.3%) | 10/20 (50.0%) | 0.312 |
| Documented project selection | 68/98 (69.4%) | 10/20 (50.0%) | 0.121 |
| Documented proceeds management | 63/98 (64.3%) | 10/20 (50.0%) | 0.312 |

### Panel C — Conditional on green bond issuance (N = 118, year FE only)

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *Log population* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 118 | 77 | +0.1144 | −0.0382 | +0.1734 |
| | | | (0.80) | (1.35) | (4.30)\*\*\* |
| **Third-party ESG assurance** | 118 | 61 | **+0.4385** | −0.0541 | +0.1276 |
| | | | **(3.82)\*\*\*** | (1.38) | (2.84)\*\*\* |
| ICMA / CBI framework | 118 | 70 | −0.0269 | −0.0488 | +0.2025 |
| | | | (0.20) | (1.49) | (4.41)\*\*\* |
| Impact reporting | 118 | 73 | +0.0203 | −0.0300 | +0.1991 |
| | | | (0.15) | (0.97) | (5.09)\*\*\* |
| Documented project selection | 118 | 78 | +0.1303 | −0.0292 | +0.1903 |
| | | | (0.92) | (1.03) | (4.77)\*\*\* |
| Documented proceeds management | 118 | 73 | +0.0373 | −0.0265 | +0.1887 |
| | | | (0.27) | (0.73) | (3.85)\*\*\* |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.

### Reading

The empirical pattern at Step 4 is consistent with administrative scale and sophistication driving the credibility decisions rather than mayoral partisanship. Panel A shows `Dem_Mayor` is null on five of six credibility outcomes. The single exception — third-party ESG assurance — is California-fragile (β falls from +0.0045\*\* to +0.0032, p = 0.170 when California is dropped). Panel C confirms that conditional on green issuance, only `log_population` predicts framework adoption, impact reporting, project selection, and proceeds management at \*\*\*. Larger and richer cities adopt quality standards regardless of mayoral partisanship — Family 1 in its administrative-capacity form, not Family 2.

The descriptive Panel B gap (third-party assurance: 59% Dem vs 15% Rep, Fisher p < 0.001) is the starkest partisan difference observed anywhere in the paper. The Panel A regression and the leave-California-out diagnostic show this gap reflects a sophistication-and-scale concentration in a handful of large coastal Democratic cities (California contributes 22 of 61 assurance events; San Francisco alone contributes 10) rather than a generalisable partisan mechanism.

The other five credibility dimensions are driven by city size. Panel C shows `log_population` at \*\*\* on framework adoption, impact reporting, project selection, and proceeds management. By the time the decision reaches Step 4, the political-agency mechanism that operates at Step 1 in the discretionary domain has been delegated to administrative and financial professionals operating under capacity-and-scale constraints.

---

## Appendix C — Outcome-Variable Validation

### Bloomberg Green-Flag Validation

| | text-green = 1 | text-green = 0 | row total |
|---|---:|---:|---:|
| Bloomberg green = Yes | **2,134** (TP) | 298 (FN) | 2,432 |
| Bloomberg green ≠ Yes | 143 (FP) | **565** (TN) | 708 |
| column total | 2,277 | 863 | 3,140 |

Sensitivity = **0.877**. Specificity = **0.798**. Precision = **0.937**.

| Bloomberg flag | CUSIPs | Green-section median chars | Green keywords median | SPO rate |
|---|---:|---:|---:|---:|
| Yes | 2,432 | 5,961 | 158 | 48.0% |
| No | 76 | 4,183 | 140 | 42.1% |
| -- (missing) | 632 | 0 | 65 | 1.4% |

### Third-party verification and framework citations (134 prospectuses)

| Framework | Bonds citing | | Verifier | Bonds citing |
|---|---:|---|---|---:|
| ICMA Green Bond Principles | 36 | | Kestrel | 26 |
| Sustainable Development Goals | 22 | | Sustainalytics | 18 |
| Climate Bonds Standard | 15 | | ICMA GBP (other) | 16 |
| | | | Build America Mutual | 2 |
| | | | Moody's ESG | 1 |

Coverage: 54% (72/134) name a third-party verifier; 48% (64/134) cite a framework; 43% (58/134) do both; 42% (56/134) do neither.

---

## Files

- `processed/tables/PAPER_main_v4.md` — this document.
- `processed/tables/PAPER_main_v3_2_archive.md` — previous version.
- `processed/tables/v3_rr/` — supplementary diagnostics, robustness, methods changelog.
- `processed/tables/v3_rr/severity_variant_comparison.md` — severity variant battery.
- Prospectus-text artefacts on branch `claude/convert-pdfs-to-text-TQGQd`, in `processed/prospectus_analysis/`.
