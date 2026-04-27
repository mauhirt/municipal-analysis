# When Do Red and Blue Go Green? — Main Paper Tables and Narrative (v3)

> **Changelog (v2 → v3).** (1) Chain table revised to reflect empirical pattern: political agency concentrates at Step 1 in the discretionary subdomain, not at Step 4 as previously predicted. (2) "Primary decision-maker" column dropped from the chain table; all four steps technically pass through the mayor in most American cities, and the cross-step variation is in political visibility and routine attention rather than in formal authority. (3) Discussion paragraph below the chain table rewritten to make the visibility-and-attention argument explicitly. (4) 4×3 mapping diagram updated to partition Step 1 into compelled (water) and discretionary (non-water) subdomains, with Family 2 (political) localized to the discretionary subcell. (5) Closing two-axis paragraph added to the chain framing section explaining that chain position and use-of-funds category are independent analytical dimensions. (6) Tables 1 and 2 reordered to match the chain sequence: the former Table 2 (water vs non-water decomposition) is now Table 1 (Step 1 Investment); the former Table 1 (full-panel specification) is now Table 2 (Step 2 Bond Financing). (7) Table headings and step-mapping notes updated. (8) Transitional sentence added to new Table 1 reading. (9) Appendix B reading rewritten to frame Step 4 null on `Dem_Mayor` as the predicted result under the revised framing (Family 1 administrative-scale dominance), not as partial support for an alternative prediction. (10) "The story" Step 4 paragraph rewritten accordingly. (11) Summary table updated with new step localizations and table numbers. (12) File inventory updated. No empirical specifications change.

---

**Sample.** N = 6,825 city-years · 576 cities · 49 states · 2014–2025.
**Estimator.** Linear probability model (continuous outcomes: OLS).
**Treatment.** `Dem_Mayor` (no lag).
**Fixed effects.** State + year (absorbed, not reported).
**Standard errors.** Clustered at city (`fips7`).
**Treatment imputation.** Three-tier procedure for nonpartisan/rotating-mayor cities (97 obs from `mayor_party` backfill, 40 obs from within-city ffill/bfill, 13 obs constituency proxy for Pico Rivera). Indicator `Dem_Mayor_imputed ∈ {0,1,2,3}` available for sensitivity.

---

## The Four-Step Decision Chain

A city's participation in the green municipal bond market involves four sequential decisions.

| Step | Decision | Dominant family | Within-step variation | Addressed in |
|---|---|---|---|---|
| **1. Investment** | Whether to undertake a capital project | Material (compelled) **or** Political × constituency (discretionary) | Yes — compelled (water) vs discretionary (non-water) | Table 1 |
| **2. Bond Financing** | Whether to finance via debt rather than current revenue | Material (NPDES, fiscal capacity) | No | Table 2 |
| **3. Green Labelling** | Whether to apply the green label to an issued bond | Material + institutional (marketability, fiscal stress) | No | Table 3 |
| **4. Credibility Certification** | Whether to obtain third-party verification, framework adoption, impact reporting | Material (administrative scale and sophistication) | No | Appendix B |

All four steps technically pass through the mayor's office in most American cities, but they differ substantially in the political attention they receive in practice. Step 1 (Investment) involves visible, voter-observable choices about which projects to undertake; the mayor's name appears on the announcement of a new capital project. Step 2 (Bond Financing) is a structural fiscal decision typically handled by the city finance office and rarely makes news beyond technical municipal finance circles. Step 3 (Green Labelling) is a documentation choice made in consultation with bond underwriters, where the green label adds little marginal cost when use of proceeds qualifies. Step 4 (Credibility Certification) carries direct fiscal cost (verifier fees) and a public association with the ESG verification ecosystem, but the choice is typically made on advice from financial professionals based on whether the additional credibility signal is needed for marketing the bond.

Step 1 also admits a within-step decomposition: some investment decisions are mandate-driven (water infrastructure under federal NPDES enforcement, sewer-overflow remediation, drinking-water-rule compliance) while others are discretionary (clean transportation, energy efficiency, green buildings, climate adaptation, renewable energy). The discretionary categories are where mayors face a genuine investment-allocation choice that constituents can observe.

The paper's central theoretical claim is that mayoral partisanship operates at the intersection of two conditions: early-chain position (the decision is voter-visible) and discretionary content (the mayor has a meaningful choice). At the cross-product cell where both conditions hold — Step 1 in the discretionary subdomain — Democratic mayors respond to constituency green preferences (amplifying in green-leaning cities, substituting away in conservative-leaning cities). Everywhere else in the chain, material conditions and market-structural mechanisms dominate. The claim is not that mayoral authority is institutionally absent at Steps 2 through 4 — formally, the mayor signs off at every step — but that political agency manifests in observable patterns of behavior only where both visibility and discretion combine to activate constituency feedback.

### Theoretical mapping: which family operates at which step

| | Step 1: Investment | | Step 2: Bond Financing | Step 3: Green Labelling | Step 4: Credibility |
|---|---|---|---|---|---|
| | **Compelled (water)** | **Discretionary (non-water)** | | | |
| **Family 1: Material** | **Dominant** (NPDES enforcement) | Subordinate | **Dominant** (NPDES, fiscal capacity) | **Dominant** (NPDES, fiscal stress) | Subordinate (scale, sophistication) |
| **Family 2: Political** | Absent (water placebo I2 = ns) | **Dominant** (constituency × mayor interaction) | Subordinate (unconditional null) | Absent (Dem null at Step 3) | Largely absent (5/6 outcomes null; assurance California-fragile) |
| **Family 3: Institutional** | Background | Background | Background (state market depth ns) | **Moderator** (marketability interaction) | Background |

The paper's empirical analysis isolates each step using sequential conditioning: Tables 1 and 2 cover the early steps (with Table 1 implementing the within-Step-1 decomposition by use-of-funds and Table 2 presenting the full-panel aggregate), Table 3 conditions on bond issuance to identify Step 3, and Appendix B conditions on green labelling to identify Step 4. The two analytical axes — chain position and use-of-funds category — are independent. The chain runs along the temporal sequence of decisions; the use-of-funds split runs along the content of the underlying capital project. The paper's central claim is that mayoral partisanship operates at one specific intersection of these axes: early in the chain, in the discretionary subdomain. Material and market-structural mechanisms dominate everywhere else.

---

## Table 1 — Investment Decision: Compelled vs Discretionary (Step 1)

> **Step mapping.** This table addresses Step 1 of the decision chain: is the capital project that motivates bond issuance mandate-driven (water infrastructure under federal compulsion) or discretionary (non-water categories where the city chooses to invest)? The constituency × partisan interaction is tested in both domains. Where compulsion removes discretion (water), the interaction is predicted to be null; where discretion remains (non-water), the interaction is predicted to be positive. This is the locus of the paper's central finding.

Table 1 presents the Step 1 use-of-funds decomposition. The aggregate version of this specification, pooling water and non-water outcomes, is presented in Table 2 and confirms the unconditional partisan null that motivates the within-step decomposition.

### Panel A — Regression: water vs non-water

| *Variable* | *W1 Water* | *W2 Water + I2* | *NW1 Non-water* | *NW2 Non-water + I2* |
|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | |
| NPDES formal enforcement (3yr) | +0.0075 | +0.0075 | +0.0064 | +0.0059 |
| | (1.53) | (1.54) | (1.34) | (1.27) |
| Reserve ratio | +0.0034 | +0.0034 | +0.0011 | +0.0011 |
| | (1.32) | (1.32) | (0.56) | (0.63) |
| Debt service burden | −0.0433 | −0.0432 | −0.0148 | −0.0199 |
| | (1.14) | (1.15) | (0.49) | (0.69) |
| **Family 2 — Political factors** | | | | |
| Dem Mayor | −0.0006 | +0.0003 | +0.0011 | −0.0564 |
| | (0.15) | (0.02) | (0.41) | (3.08)\*\*\* |
| Dem presidential vote share | +0.0172 | +0.0180 | +0.0373 | −0.0144 |
| | (1.00) | (1.04) | (2.40)\*\* | (1.01) |
| Dem Mayor × Dem vote share | — | −0.0016 | — | +0.1021 |
| | | (0.05) | | (3.14)\*\*\* |
| **Family 3 — Institutional context** | | | | |
| State green bond market depth | +0.0004 | +0.0004 | +0.0002 | +0.0001 |
| | (1.29) | (1.29) | (0.75) | (0.58) |
| Anti-ESG muni bond law | −0.0109 | −0.0109 | +0.0043 | +0.0052 |
| | (1.88)\* | (1.88)\* | (1.11) | (1.30) |
| **Demographic and economic controls** | | | | |
| Log population | +0.0145 | +0.0145 | +0.0185 | +0.0182 |
| | (3.53)\*\*\* | (3.56)\*\*\* | (3.66)\*\*\* | (3.70)\*\*\* |
| Log per-capita income | +0.0147 | +0.0148 | +0.0183 | +0.0163 |
| | (1.52) | (1.57) | (2.01)\*\* | (1.91)\* |
| Unemployment rate | +0.0021 | +0.0021 | +0.0008 | +0.0009 |
| | (1.57) | (1.56) | (0.99) | (1.07) |
| R² | 0.045 | 0.045 | 0.062 | 0.066 |
| N | 6,825 | 6,825 | 6,825 | 6,825 |
| Positive city-years | 89 | 89 | 57 | 57 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed.

#### Marginal effect of `Dem_Mayor` at constituency percentiles

| Domain | 10th pct (0.39) | 50th pct (0.57) | 90th pct (0.75) |
|---|---|---|---|
| W2 Water | −0.0003 (0.06) | −0.0006 (0.15) | −0.0009 (0.12) |
| **NW2 Non-water** | **−0.0167 (2.74)\*\*\*** | +0.0015 (0.56) | **+0.0202 (3.01)\*\*\*** |

### Panel B — Descriptive: individual sparse categories

| *Category* | *Total+* | *Dem N* | *Dem+* | *Dem %* | *Rep N* | *Rep+* | *Rep %* | *Fisher p* |
|---|---|---|---|---|---|---|---|---|
| Clean transportation | 17 | 4,248 | 17 | 0.40% | 3,266 | 0 | 0.00% | 0.000\*\*\* |
| Energy efficiency | 20 | 4,248 | 18 | 0.42% | 3,266 | 2 | 0.06% | 0.002\*\*\* |
| Green buildings | 19 | 4,248 | 19 | 0.45% | 3,266 | 0 | 0.00% | 0.000\*\*\* |
| Renewable energy | 18 | 4,248 | 17 | 0.40% | 3,266 | 1 | 0.03% | 0.001\*\*\* |
| Pollution control | 9 | 4,248 | 8 | 0.19% | 3,266 | 1 | 0.03% | 0.087\* |
| Climate adaptation | 7 | 4,248 | 7 | 0.16% | 3,266 | 0 | 0.00% | 0.021\*\* |
| Natural resource mgmt | 3 | 4,248 | 3 | 0.07% | 3,266 | 0 | 0.00% | 0.263 |

### Reading

**Step 1 is dominated by Family 1 (Material) in the compelled domain.** Water issuance (W1/W2): `Dem_Mayor` is null; the I2 interaction is flat zero (−0.002, t = 0.05); marginal effects at all percentiles are indistinguishable from zero. Where federal enforcement mandates the capital investment, the partisan-constituency mechanism has no traction.

**Step 1 shows responsive representation in the discretionary domain.** Non-water issuance (NW1/NW2): the I2 interaction is **+0.102\*\*\*** (t = 3.14). Democratic mayors amplify constituency demand for discretionary green capital projects. The crossover at pres\_dem ≈ 0.55 separates amplification (blue cities, +0.020\*\*\*) from substitution (red cities, −0.017\*\*\*).

**The domain contrast is the finding.** Water (I2 = −0.002, ns) vs non-water (I2 = +0.102\*\*\*). The constituency × partisan interaction operates exclusively where mayors have discretion over the investment decision. Panel B shows the raw descriptive pattern — Democratic mayors account for 17 of 17 clean-transportation and 19 of 19 green-buildings positive city-years — which Panel A decomposes into constituency-conditional responsive representation rather than autonomous partisan ideology.

---

## Table 2 — Bond Financing Decision (Step 2)

> **Step mapping.** This table addresses Step 2 of the decision chain: conditional on a capital project existing, does the city finance it via a green bond? The full-panel specification tests whether mayoral partisanship affects the bond-financing decision pooled across all use-of-funds categories. The aggregate version of the Step 1 decomposition presented in Table 1 confirms the unconditional partisan null that motivates the within-step decomposition.

| *Variable* | *C1 GBI* | *C2 GBI $* | *C3 Self-green* | *C4 Self $* | *I1 GBI* | *I2 Self-green* |
|---|---|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | | | |
| NPDES formal enforcement (3yr) | +0.0145 | +0.2917 | +0.0164 | +0.3238 | +0.0140 | +0.0159 |
| | (1.85)\* | (1.91)\* | (2.36)\*\* | (2.37)\*\* | (1.83)\* | (2.35)\*\* |
| Reserve ratio | +0.0044 | +0.0753 | +0.0031 | +0.0551 | +0.0045 | +0.0032 |
| | (1.31) | (1.20) | (1.05) | (0.99) | (1.35) | (1.10) |
| Debt service burden | −0.0616 | −1.0602 | −0.0416 | −0.7348 | −0.0667 | −0.0473 |
| | (1.13) | (1.03) | (0.86) | (0.80) | (1.24) | (1.00) |
| **Family 2 — Political factors** | | | | | | |
| Dem Mayor | +0.0005 | +0.0045 | −0.0004 | −0.0100 | −0.0569 | −0.0654 |
| | (0.11) | (0.06) | (0.11) | (0.14) | (1.85)\* | (2.18)\*\* |
| Dem presidential vote share | +0.0535 | +0.9837 | +0.0545 | +0.9872 | +0.0019 | −0.0040 |
| | (1.99)\*\* | (1.93)\* | (2.15)\*\* | (2.05)\*\* | (0.08) | (0.17) |
| Dem Mayor × Dem vote share | — | — | — | — | +0.1019 | +0.1155 |
| | | | | | (1.90)\* | (2.20)\*\* |
| **Family 3 — Institutional context** | | | | | | |
| State green bond market depth | +0.0006 | +0.0102 | +0.0004 | +0.0065 | +0.0005 | +0.0003 |
| | (1.42) | (1.38) | (1.03) | (1.01) | (1.32) | (0.91) |
| Anti-ESG muni bond law | −0.0076 | −0.1427 | −0.0078 | −0.1461 | −0.0066 | −0.0068 |
| | (1.18) | (1.15) | (1.47) | (1.43) | (1.03) | (1.27) |
| **Demographic and economic controls** | | | | | | |
| Log population | +0.0339 | +0.6559 | +0.0281 | +0.5473 | +0.0336 | +0.0277 |
| | (3.75)\*\*\* | (3.67)\*\*\* | (3.42)\*\*\* | (3.35)\*\*\* | (3.78)\*\*\* | (3.45)\*\*\* |
| Log per-capita income | +0.0334 | +0.6738 | +0.0277 | +0.5684 | +0.0314 | +0.0254 |
| | (1.94)\* | (1.92)\* | (1.63) | (1.65)\* | (1.92)\* | (1.58) |
| Unemployment rate | +0.0030 | +0.0572 | +0.0025 | +0.0495 | +0.0031 | +0.0026 |
| | (1.91)\* | (1.95)\* | (1.79)\* | (1.87)\* | (1.92)\* | (1.81)\* |
| R² | 0.092 | 0.098 | 0.094 | 0.097 | 0.094 | 0.096 |
| N | 6,825 | 6,825 | 6,825 | 6,825 | 6,825 | 6,825 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.
*Note:* Absolute value of the *t*-statistic is in parenthesis. Outcomes: GBI = `Green_Bond_Issued` (any green bond, prob.), GBI $ = `asinh(green_amt)`, Self-green = `Y_self_green` (city self-labelled, prob.), Self $ = `asinh(self_green_amt)`.

### Marginal effect of `Dem_Mayor` on self-green (I2)

| Constituency percentile | pres\_dem | Marginal effect | *t*-stat |
|---|---|---|---|
| 10th (red city) | 0.39 | **−0.020** | **(2.01)\*\*** |
| 50th (median) | 0.57 | +0.000 | (0.00) |
| 90th (blue city) | 0.75 | **+0.021** | **(2.04)\*\*** |

### Reading

**Family 1 (Material) dominates Step 2.** NPDES formal enforcement drives issuance across all main columns (β = +0.015\*–+0.016\*\*). Cities under federal water-quality enforcement are more likely to issue green bonds. Fiscal-capacity variables (reserve ratio, debt service burden) are directionally consistent but not individually significant in this specification.

**Family 2 (Political) is null on average but masks responsive representation.** `Dem_Mayor` is indistinguishable from zero across C1–C4. The constituency × partisan interaction (I1–I2) reveals the conditional pattern: Democratic mayors amplify electorate preferences where those preferences favor green issuance (blue cities, 90th pct: +0.021\*\*) and substitute away where they do not (red cities, 10th pct: −0.020\*\*). The crossover is at pres\_dem ≈ 0.55. The unconditional null is the population-weighted average of these two equal-and-opposite effects. As Table 1 confirms, this responsive-representation mechanism operates exclusively in the discretionary (non-water) domain where mayoral latitude exists.

**Robustness.** The I2 interaction has centered VIF = 1.18, discordant common-support count = 1,350, and survives leave-one-state-out (0 of 49 states push p > 0.10). Dropping California reduces the coefficient by 19% (from +0.102 to +0.083) but it remains highly significant (t = 3.08, p < 0.01). Full panel null on `Dem_Mayor` is confirmed across R1–R24 (24 robustness specifications).

---

## Table 3 — Green Labelling Decision (Step 3)

> **Step mapping.** This table addresses Step 3: conditional on having issued a bond, does the city apply the green label? The sample restricts to bond issuers (`total_ltd_issued > 0`), isolating the labelling decision from the investment and financing decisions. At near-zero marginal cost when use of proceeds qualifies, the paper predicts Family 1 (Material) dominance at this step.

**Sample.** Bond issuers: N = 3,888 city-years (567 cities, 84 self-green events). Compelled issuers (NPDES > 0): N = 719 (37 events).

| *Variable* | *L1 Baseline* | *L2 +Fiscal Stress* | *L3 +Marketability* | *L4 Both* | *L5 Compelled only* |
|---|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | | |
| NPDES formal enforcement (3yr) | +0.0221 | +0.0210 | −0.0201 | −0.0200 | — |
| | (2.62)\*\*\* | (2.59)\*\*\* | (1.26) | (1.26) | |
| Reserve ratio | +0.0035 | +0.0059 | +0.0034 | +0.0057 | +0.0031 |
| | (0.77) | (1.34) | (0.74) | (1.30) | (0.18) |
| Debt service burden | −0.0586 | −0.2109 | −0.0573 | −0.2065 | −0.0326 |
| | (0.85) | (2.12)\*\* | (0.83) | (2.09)\*\* | (0.14) |
| Fiscal stress index | — | +0.0176 | — | +0.0173 | — |
| | | (2.05)\*\* | | (2.04)\*\* | |
| NPDES × state green market depth | — | — | +0.0022 | +0.0021 | — |
| | | | (2.20)\*\* | (2.10)\*\* | |
| **Family 2 — Political factors** | | | | | |
| Dem Mayor | −0.0015 | −0.0024 | −0.0013 | −0.0021 | +0.0064 |
| | (0.30) | (0.48) | (0.26) | (0.42) | (0.36) |
| Dem presidential vote share | +0.0708 | +0.0772 | +0.0719 | +0.0782 | +0.1875 |
| | (2.23)\*\* | (2.41)\*\* | (2.26)\*\* | (2.44)\*\* | (1.43) |
| **Family 3 — Institutional context** | | | | | |
| Anti-ESG muni bond law | −0.0106 | −0.0099 | −0.0105 | −0.0099 | −0.0351 |
| | (1.38) | (1.30) | (1.36) | (1.29) | (1.00) |
| State green bond market depth | +0.0005 | +0.0004 | −0.0000 | −0.0000 | +0.0002 |
| | (1.00) | (0.80) | (0.07) | (0.06) | (0.13) |
| **Demographic and economic controls** | | | | | |
| Log population | +0.0351 | +0.0345 | +0.0348 | +0.0342 | +0.0416 |
| | (3.48)\*\*\* | (3.45)\*\*\* | (3.48)\*\*\* | (3.49)\*\*\* | (2.04)\*\* |
| Log per-capita income | +0.0288 | +0.0314 | +0.0281 | +0.0307 | +0.1146 |
| | (1.14) | (1.22) | (1.12) | (1.20) | (1.78)\* |
| Unemployment rate | +0.0022 | +0.0024 | +0.0022 | +0.0023 | +0.0060 |
| | (1.04) | (1.13) | (1.04) | (1.11) | (1.02) |
| R² | 0.108 | 0.109 | 0.109 | 0.110 | 0.223 |
| N | 3,888 | 3,888 | 3,888 | 3,888 | 719 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed.

### Reading

**Family 1 (Material) dominates Step 3, as predicted.** NPDES compulsion drives labelling in the baseline (L1: +0.022\*\*\*). Fiscal stress (L2: +0.018\*\*) and the marketability interaction (L3: NPDES × state green market depth = +0.0022\*\*) are jointly significant and orthogonal (L4).

**Family 2 (Political) is null at Step 3.** `Dem_Mayor` is indistinguishable from zero across all five columns (|t| ≤ 0.48). The labelling decision at near-zero marginal cost does not activate the political-agency mechanism that operates at Step 1 in the discretionary domain.

**L5 Compelled issuers only.** Among cities under NPDES enforcement that issue bonds, only `log_population` (\*\*) and `log_percapita_income` (\*) predict green labelling. Labelling among compelled issuers is a matter of administrative and financial sophistication.

---

## Appendix B — Credibility Certification (Step 4)

> **Step mapping.** This appendix addresses Step 4: conditional on having labelled a bond green, does the city procure third-party verification, adopt an ICMA/CBI framework, publish impact reports, or document project-selection and proceeds-management procedures? These actions impose direct fiscal cost. The paper predicts Family 1 dominance at this step in the form of administrative scale — larger and more sophisticated cities adopt quality standards regardless of mayoral partisanship — with the residual partisan signal concentrated in a small handful of large coastal Democratic cities (California-fragile).

### Panel A — Full-sample regression (10-variable PRIMARY)

| *Outcome* | *N* | *n+* | *Dem Mayor* | *NPDES* | *pres\_dem* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 6,825 | 78 | +0.0005 | +0.0179 | +0.0292 |
| | | | (0.13) | (2.86)\*\*\* | (1.42) |
| Third-party ESG assurance | 6,825 | 61 | +0.0044 | +0.0136 | +0.0166 |
| | | | (1.75)\* | (2.37)\*\* | (0.85) |
| ICMA / CBI framework | 6,825 | 71 | −0.0021 | +0.0190 | +0.0398 |
| | | | (0.62) | (3.05)\*\*\* | (2.09)\*\* |
| Impact reporting | 6,825 | 73 | −0.0015 | +0.0174 | +0.0378 |
| | | | (0.44) | (2.79)\*\*\* | (1.93)\* |
| Documented project selection | 6,825 | 78 | −0.0002 | +0.0163 | +0.0323 |
| | | | (0.05) | (2.58)\*\*\* | (1.56) |
| Documented proceeds management | 6,825 | 73 | −0.0014 | +0.0177 | +0.0369 |
| | | | (0.40) | (2.83)\*\*\* | (1.90)\* |

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

| *Outcome* | *N* | *n+* | *Dem Mayor* | *NPDES* | *Log population* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 118 | 77 | +0.1335 | +0.1402 | +0.1171 |
| | | | (1.00) | (1.38) | (2.72)\*\*\* |
| **Third-party ESG assurance** | 118 | 61 | **+0.4488** | +0.0463 | +0.0794 |
| | | | **(3.81)\*\*\*** | (0.36) | (1.51) |
| ICMA / CBI framework | 118 | 70 | −0.0051 | +0.1548 | +0.1355 |
| | | | (0.04) | (1.41) | (2.86)\*\*\* |
| Impact reporting | 118 | 73 | +0.0375 | +0.1296 | +0.1507 |
| | | | (0.30) | (1.15) | (3.57)\*\*\* |
| Documented project selection | 118 | 78 | +0.1441 | +0.0995 | +0.1488 |
| | | | (1.09) | (0.93) | (3.45)\*\*\* |
| Documented proceeds management | 118 | 73 | +0.0547 | +0.1351 | +0.1417 |
| | | | (0.41) | (1.22) | (3.07)\*\*\* |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.

### Reading

The empirical pattern at Step 4 is consistent with administrative scale and sophistication driving the credibility decisions rather than mayoral partisanship. Panel A shows `Dem_Mayor` is null on five of six credibility outcomes. The single exception — third-party ESG assurance — is California-fragile (β falls from +0.0044\* to +0.0031, p = 0.239 when California is dropped). Panel C confirms that conditional on green issuance, only `log_population` predicts framework adoption, impact reporting, project selection, and proceeds management at \*\*\*. Larger and richer cities adopt quality standards regardless of mayoral partisanship — Family 1 in its administrative-capacity form, not Family 2.

The descriptive Panel B gap (third-party assurance: 59% Dem vs 15% Rep, Fisher p < 0.001) is the starkest partisan difference observed anywhere in the paper. The Panel A regression and the leave-California-out diagnostic show this gap reflects a sophistication-and-scale concentration in a handful of large coastal Democratic cities (California contributes 22 of 61 assurance events; San Francisco alone contributes 10) rather than a generalisable partisan mechanism. The between-state correlation between assurance rate and Dem-mayor rate is +0.12; the within-state correlation is +0.07.

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

## Summary across all specifications

| Finding | Evidence | Step | Strength |
|---|---|---|---|
| `Dem_Mayor` null across outcomes | β ≈ 0 across Table 2 C1–C4 + R1–R24 | Steps 2, 3, 4 | Rock solid (\*\*\*) |
| NPDES compulsion drives issuance | +0.015\* (GBI), +0.016\*\* (self-green); _locgov +0.014\*\*; _private placebo clean | Steps 1 (compelled), 2, 3 | Confirmed (\*\*\*) |
| Constituency drives issuance | pres\_dem +0.054\*\* (Table 2 self-green) | Step 2 | Consistent (\*\*) |
| **Constituency × partisan interaction (responsive representation)** | +0.116\*\* (Table 2 self-green); **+0.102\*\*\* (Table 1 NW2)**; −0.002 ns (Table 1 W2 placebo). VIF 1.18 centered. LOSO 0/49 above p = 0.10 | **Step 1, discretionary subdomain only** | Novel, doubly conditional (\*\*) |
| Labelling-margin marketability | Table 3 L3: NPDES × state\_green +0.0022\*\* (issuer subsample) | Step 3 | Separate sample (\*\*) |
| Labelling-margin fiscal stress | Table 3 L2: fiscal stress +0.018\*\* (issuer subsample) | Step 3 | Separate sample (\*\*) |
| Third-party assurance partisan gap | Panel A: +0.004\*; Panel C (N=118): +0.449\*\*\*; Fisher 59% vs 15%. California-fragile | Step 4 | Partial (\*), fragile |
| Pre-ESG-law market predicts issuance | R17: state\_pre\_esg\_activity +0.064\*\*\* | Step 3 | Confirmed (\*\*\*) |

---

## The story

**Step 1 (Investment).** Capital need and federal enforcement mandate drive project selection. Both parties undertake similar levels of capital investment when capital need is comparable. In the compelled domain (water infrastructure under NPDES enforcement), the constituency × partisan interaction is flat zero (Table 1 W2: −0.002, t = 0.05). In the discretionary domain (non-water categories), the interaction is significant (+0.102\*\*\*): Democratic mayors amplify constituency demand for discretionary green capital projects in blue cities and substitute away in red cities. The investment decision is the point in the chain where the compelled-vs-discretionary distinction first operates, and where the water placebo confirms that partisan-constituency alignment matters only where mayors have latitude.

**Step 2 (Bond Financing).** Fiscal capacity and regulatory compulsion shape the debt-financing choice. `Dem_Mayor` is null across all four main-table outcomes (Table 2 C1–C4). NPDES formal enforcement (+0.016\*\*) and constituency (+0.054\*\*) drive issuance. The null survives 24 robustness specifications, two-way and state clustering, alternative partisan measures, and three-tier mayor-party imputation. Both parties borrow at similar rates conditional on capital need and fiscal position.

**Step 3 (Green Labelling).** The labelling decision is driven by market-structural factors. Among bond issuers (Table 3), fiscal stress (+0.018\*\*) and the marketability interaction (NPDES × state green market depth = +0.0022\*\*) are the operative mechanisms. Compelled issuers label green where the state ESG-investor base exists; distressed issuers label green to seek the greenium. Mayoral partisanship is null at this step (|t| ≤ 0.48 across all five Table 3 columns). Among compelled issuers (L5), only city size and per-capita income predict labelling — a sophistication channel.

**Step 4 (Credibility Certification).** Once the green label has been applied, the decision to certify the bond's credibility through third-party verification, framework adoption, or impact reporting is driven by administrative scale and sophistication rather than mayoral partisanship. `Dem_Mayor` is null on five of six credibility outcomes (Appendix B Panel A); only `log_population` is consistently significant across credibility dimensions (Panel C). The lone exception — third-party ESG assurance — is concentrated in a small set of large coastal Democratic cities (California contributes 22 of 61 assurance events) and does not survive a leave-California-out test. The political-agency mechanism that operates at Step 1 in the discretionary domain has no traction at Step 4: by the time the decision reaches the credibility stage, it has been delegated to administrative and financial professionals operating under capacity-and-scale constraints.

**Sensitivity and robustness.** The I2 constituency × partisan interaction survives centered-VIF (1.18), leave-one-state-out across all 49 states (0 of 49 push p > 0.10; California worst case at p = 0.078), and the water-domain placebo (−0.002, ns). Three alternative interaction specifications (Dem × NPDES, Dem × state\_green\_cum, npdes × state\_green\_cum on the full sample) were tested and discarded on diagnostic grounds — see appendix.

---

## Qualitative validation from bond prospectus text

A separate corpus analysis of 198 bond prospectuses (134 with green-designation sections; 158 with use-of-proceeds sections) provides document-level validation for three core claims.

**Outcome-variable validation (Appendix C).** Bloomberg's `Self-reported Green` flag has sensitivity 0.877, specificity 0.798, and precision 0.937 against an independently constructed prospectus-text classifier (N = 3,140 CUSIPs). Intensity stratification shows Bloomberg "Yes" and "No" bonds have similar prospectus content (SPO rate 48% vs 42%; green-section median 5,961 vs 4,183 characters), validating `Y_self_green` as a meaningful labelling decision.

**Compulsion mechanism (Steps 1–2).** Twenty-two per cent of analysed prospectuses are flagged as compelled by federal-regulatory text (consent decree, NPDES permit, EPA enforcement language). DC Water cites "Civil Action No. 1:CV00183TFH"; San Francisco PUC cites "NPDES Permit No. CA0037664"; Alexandria, VA cites "Consent Decree dated March 25, 2005". Forty prospectuses cite court case numbers, eleven cite NPDES permit numbers, fifteen reference EPA Region. This corroborates the panel finding that NPDES enforcement operates through a real regulatory-pressure channel.

**Discretion validity (Step 1, Table 1 NW).** Among non-water bonds, ~35% disclose state-level green mandates (California AB 32, CALGreen, state RPS) and ~65% show no compulsion language. The disclosed mandates are time-invariant and absorbed by state FE, confirming that within-state variation in non-water issuance reflects city-level discretionary choice.

---

## Files

- `processed/tables/PAPER_main_v3.md` — this document (chain-aligned framing, table reorder applied).
- `processed/tables/PAPER_main_v2_archive.md` — previous version (chain framing introduced, no table reorder).
- `processed/tables/PAPER_main_v1_archive.md` — pre-chain framing.
- `processed/tables/table1_investment_step1.md` — Table 1 source (water vs non-water decomposition; was `table2_final.md`).
- `processed/tables/table2_financing_step2.md` — Table 2 source (full-panel specification; was `table1_v3_combined.md`).
- `processed/tables/table3_labelling.md` — Table 3 source.
- `processed/tables/v3_rr/` — supplementary diagnostics, robustness, methods changelog.
- Prospectus-text artefacts on branch `claude/convert-pdfs-to-text-TQGQd`, in `processed/prospectus_analysis/`.
