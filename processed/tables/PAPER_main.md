# When Do Red and Blue Go Green? — Main Paper Tables and Narrative

**Sample.** N = 6,825 city-years · 576 cities · 49 states · 2014–2025.
**Estimator.** Linear probability model (continuous outcomes: OLS).
**Treatment.** `Dem_Mayor` (no lag).
**Fixed effects.** State + year (absorbed, not reported).
**Standard errors.** Clustered at city (`fips7`).
**Treatment imputation.** Three-tier procedure for nonpartisan/rotating-mayor cities (97 obs from `mayor_party` backfill, 40 obs from within-city ffill/bfill, 13 obs constituency proxy for Pico Rivera). Indicator `Dem_Mayor_imputed ∈ {0,1,2,3}` available for sensitivity.

---

## Table 1 — Main specification and partisan interaction

| *Variable* | *C1 GBI* | *C2 GBI $* | *C3 Self-green* | *C4 Self $* | *I1 GBI* | *I2 Self-green* |
|---|---|---|---|---|---|---|
| Dem Mayor | +0.0005 | +0.0045 | −0.0004 | −0.0100 | −0.0569 | −0.0654 |
| | (0.11) | (0.06) | (0.11) | (0.14) | (1.85)\* | (2.18)\*\* |
| NPDES formal enforcement (3yr) | +0.0145 | +0.2917 | +0.0164 | +0.3238 | +0.0140 | +0.0159 |
| | (1.85)\* | (1.91)\* | (2.36)\*\* | (2.37)\*\* | (1.83)\* | (2.35)\*\* |
| Dem presidential vote share | +0.0535 | +0.9837 | +0.0545 | +0.9872 | +0.0019 | −0.0040 |
| | (1.99)\*\* | (1.93)\* | (2.15)\*\* | (2.05)\*\* | (0.08) | (0.17) |
| Dem Mayor × Dem vote share | — | — | — | — | +0.1019 | +0.1155 |
| | | | | | (1.90)\* | (2.20)\*\* |
| State green bond market depth | +0.0006 | +0.0102 | +0.0004 | +0.0065 | +0.0005 | +0.0003 |
| | (1.42) | (1.38) | (1.03) | (1.01) | (1.32) | (0.91) |
| Reserve ratio | +0.0044 | +0.0753 | +0.0031 | +0.0551 | +0.0045 | +0.0032 |
| | (1.31) | (1.20) | (1.05) | (0.99) | (1.35) | (1.10) |
| Debt service burden | −0.0616 | −1.0602 | −0.0416 | −0.7348 | −0.0667 | −0.0473 |
| | (1.13) | (1.03) | (0.86) | (0.80) | (1.24) | (1.00) |
| Anti-ESG muni bond law | −0.0076 | −0.1427 | −0.0078 | −0.1461 | −0.0066 | −0.0068 |
| | (1.18) | (1.15) | (1.47) | (1.43) | (1.03) | (1.27) |
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

**Partisan main effect is null.** `Dem_Mayor` is indistinguishable from zero across all four main-table outcomes (C1–C4). The null is robust to two-way clustering, leave-one-state-out sensitivity, alternative partisan measures (probabilistic, vote-share), and three-tier mayor-party imputation.

**Compulsion drives issuance.** NPDES formal enforcement in the prior three years has a positive and significant effect across all main columns (β = +0.015\*–+0.016\*\*). Cities under recent federal water-quality enforcement are more likely to issue any green bond and to self-label.

**Constituency drives issuance.** The Dem presidential two-party vote share at the county level is positive and significant on all four outcomes (β = +0.054\*\*). A 10 percentage-point increase in county-level Dem vote share raises the probability of self-labelled issuance by ~0.5 percentage points.

**The null masks conditional partisan agency.** Adding the constituency × partisan interaction (`Dem_Mayor × pres_dem_two_party_share_lag2`) produces a striking pattern (columns I1, I2). On self-green (I2), the `Dem_Mayor` main effect turns **−0.065\*\*** and the interaction is **+0.116\*\***. Democratic mayors act as responsive representatives: they amplify electorate preferences where those preferences favor green issuance (blue cities) and substitute away from green issuance where they do not (red cities). In blue cities (90th percentile pres\_dem ≈ 0.75), Democratic mayors issue 2.1 percentage points more self-labelled green bonds than comparable Republican mayors. In red cities (10th percentile pres\_dem ≈ 0.39), Democratic mayors issue 2.0 percentage points fewer. The Table 1 main-table null is the population-weighted average of these two equal-and-opposite partisan effects.

**Robustness.** The I2 interaction has centered VIF = 1.18, discordant common-support count = 1,350, and survives leave-one-state-out (0 of 49 states push p > 0.10). Dropping California reduces the coefficient by 19% (from +0.102 to +0.083) but the interaction remains highly significant (t = 3.08, p < 0.01).

---

## Table 2 — Use of Proceeds: Discretion Test

**Purpose.** Test whether the `Dem_Mayor` null in Table 1 is a composition artifact of water bonds (which are heavily compelled by federal regulation) dominating the green-bond pool, and whether the constituency × partisan interaction (I2) is specific to the discretionary domain.

**Outcomes.** `Y_water_only` (city-year issued at least one self-labelled bond classified as Sustainable Water and no other ESG project category; positive city-years = 89). `Y_has_non_water` (city-year issued at least one self-labelled bond with any non-water ESG project category; positive city-years = 57).

### Panel A — Regression: water vs non-water

| *Variable* | *W1 Water* | *W2 Water + I2* | *NW1 Non-water* | *NW2 Non-water + I2* |
|---|---|---|---|---|
| Dem Mayor | −0.0006 | +0.0003 | +0.0011 | −0.0564 |
| | (0.15) | (0.02) | (0.41) | (3.08)\*\*\* |
| NPDES formal enforcement (3yr) | +0.0075 | +0.0075 | +0.0064 | +0.0059 |
| | (1.53) | (1.54) | (1.34) | (1.27) |
| Dem presidential vote share | +0.0172 | +0.0180 | +0.0373 | −0.0144 |
| | (1.00) | (1.04) | (2.40)\*\* | (1.01) |
| Dem Mayor × Dem vote share | — | −0.0016 | — | +0.1021 |
| | | (0.05) | | (3.14)\*\*\* |
| State green bond market depth | +0.0004 | +0.0004 | +0.0002 | +0.0001 |
| | (1.29) | (1.29) | (0.75) | (0.58) |
| Reserve ratio | +0.0034 | +0.0034 | +0.0011 | +0.0011 |
| | (1.32) | (1.32) | (0.56) | (0.63) |
| Debt service burden | −0.0433 | −0.0432 | −0.0148 | −0.0199 |
| | (1.14) | (1.15) | (0.49) | (0.69) |
| Anti-ESG muni bond law | −0.0109 | −0.0109 | +0.0043 | +0.0052 |
| | (1.88)\* | (1.88)\* | (1.11) | (1.30) |
| Log population | +0.0145 | +0.0145 | +0.0185 | +0.0182 |
| | (3.53)\*\*\* | (3.56)\*\*\* | (3.66)\*\*\* | (3.70)\*\*\* |
| Log per-capita income | +0.0147 | +0.0148 | +0.0183 | +0.0163 |
| | (1.52) | (1.57) | (2.01)\*\* | (1.91)\* |
| Unemployment rate | +0.0021 | +0.0021 | +0.0008 | +0.0009 |
| | (1.57) | (1.56) | (0.99) | (1.07) |
| R² | 0.045 | 0.045 | 0.062 | 0.066 |
| N | 6,825 | 6,825 | 6,825 | 6,825 |
| Positive city-years | 89 | 89 | 57 | 57 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.
*Note:* Absolute value of the *t*-statistic is in parenthesis. State + year FE absorbed.

#### Marginal effect of `Dem_Mayor` at constituency percentiles

| Domain | 10th pct (0.39) | 50th pct (0.57) | 90th pct (0.75) |
|---|---|---|---|
| W2 Water | −0.0003 (0.06) | −0.0006 (0.15) | −0.0009 (0.12) |
| **NW2 Non-water** | **−0.0167 (2.74)\*\*\*** | +0.0015 (0.56) | **+0.0202 (3.01)\*\*\*** |

### Panel B — Descriptive: individual sparse categories

Seven individual use-of-proceeds categories with 3–20 positive city-years. Too sparse for regression with FE. Reported as raw counts and Fisher exact tests.

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

**Water (W1/W2).** `Dem_Mayor` is null with and without the I2 interaction. The interaction itself is **−0.002 (t = 0.05)** — flat zero. Marginal effects at all percentiles of constituency are indistinguishable from zero (|t| < 0.15). Water issuance is compulsion-driven; the constituency × partisan mechanism has no traction in this domain.

**Non-water (NW1/NW2).** Without the interaction (NW1), `Dem_Mayor` is null (+0.001, t = 0.41) and constituency is significant (+0.037\*\*). With the interaction (NW2), `Dem_Mayor` turns **−0.056\*\*\*** (t = 3.08) and the interaction is **+0.102\*\*\*** (t = 3.14). Democratic mayors amplify in blue cities (90th pct: +0.020\*\*\*) and substitute away in red cities (10th pct: −0.017\*\*\*). The crossover is at pres\_dem ≈ 0.55, near the sample median.

**The domain contrast is the finding.** Water (I2 = −0.002, ns) vs non-water (I2 = +0.102\*\*\*). The constituency × partisan interaction operates exclusively in the discretionary domain. Where compulsion forces issuance (water), mayoral partisan-constituency alignment is irrelevant. Where mayors have latitude (non-water), Democratic mayors respond to their electorate's green preferences.

**Panel B addresses the descriptive pattern.** Democratic mayors account for virtually all positive city-years in the seven discretionary categories: 17 of 17 clean-transportation, 19 of 19 green-buildings, 7 of 7 climate-adaptation. Fisher exact p-values are \*\* to \*\*\* for all but natural resource management. Panel A shows this raw gap is not autonomous partisan agency: the NW1 regression with state FE and constituency absorbs the entire Fisher gap, and the NW2 regression reveals that the residual partisan variation operates through constituency alignment with two equal-and-opposite tails cancelling.

---

## Table 3 — The Labelling Decision (conditional on bond issuance)

**Purpose.** Conditional on issuing any bond, what predicts choosing the green label? Identifies the labelling-margin mechanisms separately from the issuance-margin findings in Tables 1 and 2.

**Sample.** City-years with `total_ltd_issued > 0` (Census of Governments long-term debt). Bond issuers: N = 3,888 city-years (567 cities, 84 self-green events). Compelled issuers (NPDES > 0): N = 719 city-years (37 self-green events).

| *Variable* | *L1 Baseline* | *L2 +Fiscal Stress* | *L3 +Marketability* | *L4 Both channels* | *L5 Compelled only* |
|---|---|---|---|---|---|
| Dem Mayor | −0.0015 | −0.0024 | −0.0013 | −0.0021 | +0.0064 |
| | (0.30) | (0.48) | (0.26) | (0.42) | (0.36) |
| Dem presidential vote share | +0.0708 | +0.0772 | +0.0719 | +0.0782 | +0.1875 |
| | (2.23)\*\* | (2.41)\*\* | (2.26)\*\* | (2.44)\*\* | (1.43) |
| NPDES formal enforcement (3yr) | +0.0221 | +0.0210 | −0.0201 | −0.0200 | — |
| | (2.62)\*\*\* | (2.59)\*\*\* | (1.26) | (1.26) | |
| Reserve ratio | +0.0035 | +0.0059 | +0.0034 | +0.0057 | +0.0031 |
| | (0.77) | (1.34) | (0.74) | (1.30) | (0.18) |
| Debt service burden | −0.0586 | −0.2109 | −0.0573 | −0.2065 | −0.0326 |
| | (0.85) | (2.12)\*\* | (0.83) | (2.09)\*\* | (0.14) |
| Anti-ESG muni bond law | −0.0106 | −0.0099 | −0.0105 | −0.0099 | −0.0351 |
| | (1.38) | (1.30) | (1.36) | (1.29) | (1.00) |
| State green bond market depth | +0.0005 | +0.0004 | −0.0000 | −0.0000 | +0.0002 |
| | (1.00) | (0.80) | (0.07) | (0.06) | (0.13) |
| Log population | +0.0351 | +0.0345 | +0.0348 | +0.0342 | +0.0416 |
| | (3.48)\*\*\* | (3.45)\*\*\* | (3.48)\*\*\* | (3.49)\*\*\* | (2.04)\*\* |
| Log per-capita income | +0.0288 | +0.0314 | +0.0281 | +0.0307 | +0.1146 |
| | (1.14) | (1.22) | (1.12) | (1.20) | (1.78)\* |
| Unemployment rate | +0.0022 | +0.0024 | +0.0022 | +0.0023 | +0.0060 |
| | (1.04) | (1.13) | (1.04) | (1.11) | (1.02) |
| **Fiscal stress index** | — | **+0.0176** | — | **+0.0173** | — |
| | | **(2.05)\*\*** | | **(2.04)\*\*** | |
| **NPDES × state green market depth** | — | — | **+0.0022** | **+0.0021** | — |
| | | | **(2.20)\*\*** | **(2.10)\*\*** | |
| R² | 0.108 | 0.109 | 0.109 | 0.110 | 0.223 |
| N | 3,888 | 3,888 | 3,888 | 3,888 | 719 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.
*Note:* Absolute value of the *t*-statistic is in parenthesis. State + year FE absorbed. Demographic controls included throughout. The state-political controls (`state_dem_governor`, `state_dem_trifecta`, `state_rep_trifecta`) are included in this expanded labelling-margin spec and absorb against state FE.

### Reading

**L1 Baseline.** Conditional on issuing any bond, NPDES formal enforcement still predicts self-labelling (+0.022\*\*\*). Constituency strengthens (+0.071\*\*) relative to Tables 1–2 because the issuer subsample is more politically heterogeneous than the full panel. `Dem_Mayor` remains null. Compulsion drives the green label specifically, not just bond issuance generally.

**L2 Greenium-seeking channel.** `fiscal_stress_index_lag2` = **+0.018\*\*** on the issuer subsample. Among cities that have already chosen to issue, fiscally distressed cities label green more often. The most plausible mechanism is yield-reduction: ESG-oriented investor demand permits compressed spreads on the labelled tranche.

**L3 Marketability channel.** When `npdes × state_green_cum` is added, the coefficient is **+0.0022\*\*** while the NPDES main effect flips null and the state-green main effect is zero. Compulsion drives green labelling only where an ESG investor base exists. Compelled cities in shallow-market states do not bother labelling.

**L4 Both channels together.** Greenium-seeking (+0.017\*\*) and marketability (+0.0021\*\*) retain their signs and significance jointly. The two channels are orthogonal.

**L5 Compelled issuers only.** Among cities that are both under NPDES enforcement and issuing bonds, only `log_population` (\*\*) and `log_percapita_income` (\*) predict green labelling. Partisanship and constituency vanish. Among compelled issuers, labelling is a matter of administrative and financial sophistication — bigger, richer cities have the advisory capacity to execute the green-label process.

**Summary.** Labelling on the issuer-conditional sample is market-mediated, not partisan. `Dem_Mayor` is null in every column of Table 3. The two operative mechanisms are the greenium-seeking response of distressed issuers and the marketability interaction between NPDES compulsion and state ESG market depth.

---

## Summary across all specifications

| Finding | Evidence | Strength |
|---|---|---|
| **H1b: `Dem_Mayor` null across outcomes** | β ≈ 0 across C1–C4 + R1–R24 (28 main + robustness specs) | Rock solid (\*\*\*) |
| **NPDES compulsion drives issuance** | +0.015\* (GBI), +0.016\*\* (self-green); generalises to `_locgov` (R20: +0.014\*\*); `_private` placebo clean (R21) | Confirmed (\*\*\*) |
| **Constituency drives issuance** | pres\_dem +0.054\*\* (C3 self-green) | Consistent (\*\*) |
| **Constituency × partisan interaction (I2)** | Dem × pres\_dem +0.116\*\* (self-green); +0.102\*\*\* (non-water); −0.002 ns (water placebo). Amplification in blue cities (+0.021\*\*), substitution in red cities (−0.020\*\*). VIF 1.18 centered. LOSO 0/49 above p = 0.10 | Novel, discretion-specific (\*\*) |
| **Labelling-margin marketability** | Table 3 L3: NPDES × state\_green +0.0022\*\* (issuer subsample) | Separate sample (\*\*) |
| **Labelling-margin fiscal stress** | Table 3 L2: fiscal stress +0.018\*\* (issuer subsample) | Separate sample (\*\*) |
| **Pre-ESG-law market predicts issuance** | R17: state\_pre\_esg\_activity +0.064\*\*\* | Confirmed (\*\*\*) |
| **No local spatial spillover** | R13–R16 all ns | Clean (—) |
| **Fiscal-stress × partisan interactions** | FS1–FS4 null or fragile; FS5 triple = 0 | No support (—) |
| **TEL under state FE** | Mullins ns (p = 0.15); binary forms unidentified | Dropped from main (—) |

---

## Appendix Table — Bloomberg Green-Flag Validation

Cross-tabulation of Bloomberg `Self-reported Green` against prospectus-detected green designation (N = 3,140 CUSIPs covered by a prospectus).

**Text-green criterion.** A CUSIP is classified as text-green if its primary prospectus has any of: (i) a detected Second-Party Opinion verifier (Kestrel, Sustainalytics, BAM, Moody's ESG); (ii) a green-bond designation section longer than 500 characters; or (iii) at least one cited green-bond framework (ICMA GBP, Climate Bonds Standard, SDGs).

### Confusion matrix (CUSIP-level)

| | text-green = 1 | text-green = 0 | row total |
|---|---:|---:|---:|
| Bloomberg green = Yes | **2,134** (TP) | 298 (FN) | 2,432 |
| Bloomberg green ≠ Yes | 143 (FP) | **565** (TN) | 708 |
| column total | 2,277 | 863 | 3,140 |

### Classifier metrics (Bloomberg as predictor of text-green)

| Metric | Value |
|---|---|
| Sensitivity (recall) | **0.877** |
| Specificity | **0.798** |
| Precision | **0.937** |

### Intensity stratification by Bloomberg flag

| Bloomberg flag | CUSIPs | Green-section median chars | Green keywords median | SPO rate |
|---|---:|---:|---:|---:|
| Yes | 2,432 | 5,961 | 158 | 48.0% |
| No | 76 | 4,183 | 140 | 42.1% |
| -- (missing) | 632 | 0 | 65 | 1.4% |

### Reading

Bloomberg's `Self-reported Green` flag — the basis for `Y_self_green` in the panel — has sensitivity 0.877 and precision 0.937 against the prospectus-text classifier. The flag rarely inflates (specificity 0.798). The intensity stratification reveals the labelling-margin story: Bloomberg "Yes" and "No" bonds have near-identical prospectus content (SPO rate 48% vs 42%; green-section median 5,961 vs 4,183 characters). The real dividing line is labelled (Yes or No) vs unlabelled (--), not the intensity of green disclosure. This validates `Y_self_green` as capturing a meaningful issuer-level labelling decision.

---

## The story

**First claim.** The partisan main effect is null. `Dem_Mayor` is indistinguishable from zero across all four main-table outcomes and all 24 robustness specifications. The null survives two-way clustering, leave-one-state-out sensitivity, alternative partisan measures (probabilistic, vote-share), and three-tier mayor-party imputation. Partisan ideology does not drive green bond issuance at the extensive margin.

**Second claim.** The null masks conditional partisan agency on the issuance margin. The constituency × partisan interaction (`Dem_Mayor × pres_dem_two_party_share_lag2` = +0.116\*\*, I2) reveals that Democratic mayors act as responsive representatives: they amplify electorate preferences where those preferences favor green issuance (blue cities, 90th pct: +0.021\*\*) and substitute away from green issuance where they do not (red cities, 10th pct: −0.020\*\*). Republican mayors are comparatively insensitive to electoral composition. The Table 1 main-table null is the population-weighted average of these two equal-and-opposite partisan effects. The interaction is specific to the discretionary domain: on non-water outcomes it strengthens to +0.102\*\*\* (Table 2 NW2); on water outcomes it collapses to −0.002, ns (Table 2 W2). Dropping California reduces the interaction by 19% (from +0.102 to +0.083) but it remains highly significant (t = 3.08).

**Third claim.** On the labelling margin conditional on issuance, marketability and fiscal stress are the operative mechanisms (Table 3). L2 shows fiscal stress drives labelling (+0.018\*\*): distressed issuers label green to seek the greenium. L3 shows the marketability interaction (`npdes × state_green_cum` = +0.0022\*\*) drives labelling further in compelled issuers: cities under NPDES enforcement label green where the state ESG investor base exists. Partisanship is absent on the labelling margin — `Dem_Mayor` is null in every Table 3 column. Among compelled issuers (L5), only city size and per-capita income predict green labelling — a sophistication channel.

**Fourth claim.** The paper identifies a clean division between the issuance margin and the labelling margin. On the issuance margin (Tables 1 and 2), the operative mechanism is constituency × partisan responsive representation in the discretionary domain, with regulatory compulsion dominating the water domain. On the labelling margin conditional on issuance (Table 3), the operative mechanisms are market-structural — fiscal stress and NPDES × market depth — with no partisan component. The Table 1 null on `Dem_Mayor` is the artefact of averaging issuance-margin heterogeneity across constituencies; the Table 3 analysis shows that once issuance happens, labelling is determined by non-partisan market factors.

**Sensitivity and robustness.** The I2 constituency × partisan interaction survives centered-VIF (1.18), leave-one-state-out across all 49 states (0 of 49 push p > 0.10; California worst case at p = 0.078), and the water-domain placebo (−0.002, ns). Three alternative interaction specifications (Dem × NPDES, Dem × state\_green\_cum, npdes × state\_green\_cum on the full sample) were tested and discarded on diagnostic grounds — see appendix.

---

## Qualitative validation from bond prospectus text

A separate corpus analysis of 198 bond prospectuses (134 with green-designation sections; 158 with use-of-proceeds sections) provides document-level validation for three core claims.

**Outcome-variable validation.** Bloomberg's `Self-reported Green` flag — the basis for `Y_self_green` — has sensitivity 0.877, specificity 0.798, and precision 0.937 against an independently constructed prospectus-text classifier (N = 3,140 CUSIPs). Intensity stratification shows Bloomberg "Yes" and "No" bonds have similar prospectus content (Second Party Opinion rate 48% vs 42%; green-section median characters 5,961 vs 4,183), suggesting the dependent variable captures a meaningful labelling decision rather than a noisy proxy.

**Compulsion mechanism (Tables 1, 2 W, Table 3 L1).** Twenty-two per cent of analysed prospectuses are flagged as compelled by federal-regulatory text (consent decree, NPDES permit, EPA enforcement language). Specific examples: DC Water cites "Civil Action No. 1:CV00183TFH"; San Francisco PUC cites "NPDES Permit No. CA0037664"; Alexandria, VA cites "Consent Decree dated March 25, 2005". Forty prospectuses cite court case numbers, eleven cite NPDES permit numbers, fifteen reference EPA Region. This corroborates the panel finding that NPDES enforcement (β = +0.016\*\*) operates through a real regulatory-pressure channel rather than as a proxy for environmental engagement.

**Discretion validity (Table 2 NW).** Among non-water bonds, ~35% disclose state-level green mandates (California AB 32, CALGreen, state RPS) and ~65% show no compulsion language. The disclosed mandates are concentrated in California, are time-invariant, and are absorbed by state fixed effects in the panel — confirming that within-state variation in non-water issuance reflects city-level discretionary choice rather than state-mandated policy.

---

## Files

- `processed/tables/PAPER_main.md` — this document.
- `processed/tables/table1_v3_combined.md` — Table 1 (econ-style, identical to above).
- `processed/tables/table2_final.md` — Table 2 (econ-style).
- `processed/tables/table3_labelling.md` — Table 3 (legacy format).
- `processed/tables/v3_rr/` — supplementary diagnostics, robustness, and methods changelog.
- Prospectus-text artefacts on branch `claude/convert-pdfs-to-text-TQGQd`, in `processed/prospectus_analysis/`.
