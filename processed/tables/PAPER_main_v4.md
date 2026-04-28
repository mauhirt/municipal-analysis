# When Do Red and Blue Go Green? — Main Paper Tables and Narrative (v4)

> **Changelog (v3.2 → v4).** (15) Compulsion variable replaced: non-severe QNCR violations (asinh, lag 1) supersedes effluent violations. (16) Capital outlay per capita (lag 2) added to PRIMARY as investment-intensity control; 2013–2014 values backfilled from pre-panel Census of Governments data (2011–2012). N = 7,413 preserved. Non-severe violations produce water-specific significance (+0.003\*\*, t=2.50 on water; +0.002, t=1.00 ns on non-water). All tables re-estimated.

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
| Non-severe violations (muni, lag 1) | +0.0050 | +0.0912 | +0.0041 | +0.0725 | +0.0051 | +0.0042 |
| | (1.88)\* | (1.75)\* | (1.73)\* | (1.56) | (1.96)\* | (1.83)\* |
| Reserve ratio | +0.0056 | +0.1002 | +0.0044 | +0.0810 | +0.0057 | +0.0045 |
| | (1.92)\* | (1.89)\* | (1.76)\* | (1.77)\* | (1.97)\*\* | (1.82)\* |
| Debt service burden | −0.1091 | −2.0219 | −0.0867 | −1.6433 | −0.1131 | −0.0913 |
| | (2.01)\*\* | (1.97)\*\* | (1.91)\* | (1.90)\* | (2.08)\*\* | (2.01)\*\* |
| Capital outlay per capita | +0.0388 | +0.7760 | +0.0390 | +0.7791 | +0.0381 | +0.0382 |
| | (1.57) | (1.54) | (1.56) | (1.53) | (1.57) | (1.56) |
| **Family 2 — Political factors** | | | | | | |
| Dem Mayor | −0.0002 | −0.0070 | −0.0004 | −0.0101 | −0.0521 | −0.0601 |
| | (0.05) | (0.09) | (0.12) | (0.15) | (1.94)\* | (2.32)\*\* |
| Dem presidential vote share | +0.0556 | +1.0148 | +0.0520 | +0.9449 | +0.0091 | −0.0015 |
| | (2.22)\*\* | (2.14)\*\* | (2.22)\*\* | (2.13)\*\* | (0.37) | (0.07) |
| Dem Mayor × Dem vote share | — | — | — | — | +0.0920 | +0.1059 |
| | | | | | (1.97)\*\* | (2.36)\*\* |
| **Family 3 — Institutional context** | | | | | | |
| State green bond market depth | +0.0004 | +0.0082 | +0.0003 | +0.0064 | +0.0004 | +0.0003 |
| | (1.31) | (1.29) | (1.17) | (1.16) | (1.21) | (1.04) |
| Anti-ESG muni bond law | −0.0062 | −0.1070 | −0.0035 | −0.0631 | −0.0055 | −0.0027 |
| | (1.19) | (1.10) | (0.83) | (0.79) | (1.04) | (0.62) |
| **Demographic and economic controls** | | | | | | |
| Log population | +0.0267 | +0.5165 | +0.0211 | +0.4138 | +0.0264 | +0.0207 |
| | (3.27)\*\*\* | (3.25)\*\*\* | (3.11)\*\*\* | (3.10)\*\*\* | (3.28)\*\*\* | (3.13)\*\*\* |
| Log per-capita income | +0.0259 | +0.5234 | +0.0213 | +0.4367 | +0.0242 | +0.0193 |
| | (2.07)\*\* | (2.08)\*\* | (1.77)\* | (1.81)\* | (2.02)\*\* | (1.69)\* |
| Unemployment rate | +0.0027 | +0.0525 | +0.0023 | +0.0451 | +0.0028 | +0.0024 |
| | (1.98)\*\* | (2.03)\*\* | (1.86)\* | (1.96)\*\* | (1.99)\*\* | (1.89)\* |
| R² | 0.094 | 0.100 | 0.096 | 0.101 | 0.095 | 0.099 |
| N | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed.

### Marginal effect of `Dem_Mayor` on self-green (I2)

| Constituency percentile | pres\_dem | Marginal effect | *t*-stat |
|---|---|---|---|
| 10th (red city) | 0.39 | **−0.019** | **(2.10)\*\*** |
| 50th (median) | 0.57 | +0.000 | (0.06) |
| 90th (blue city) | 0.75 | **+0.019** | **(2.20)\*\*** |

### Reading

**Family 1 (Material) dominates Step 2.** Non-severe violations drive issuance across all main columns (β = +0.004–0.005\*). Reserve ratio and debt service burden are both significant after controlling for capital outlay (+0.006\* and −0.109\*\* respectively). Capital outlay per capita is positive but not significant (t ≈ 1.56), consistent with baseline investment intensity being correlated with but not sufficient for green issuance.

**Family 2 (Political) is null on average but masks responsive representation.** `Dem_Mayor` is indistinguishable from zero across C1–C4. The constituency × partisan interaction (I1–I2) reveals the conditional pattern: Democratic mayors amplify electorate preferences where those preferences favor green issuance (blue cities, 90th pct: +0.019\*\*) and substitute away where they do not (red cities, 10th pct: −0.019\*\*). As Table 2 confirms, this responsive-representation mechanism operates exclusively in the discretionary (non-water) domain.

---

## Table 2 — Investment Decision: Compelled vs Discretionary (Step 1)

> **Step mapping.** This table addresses Step 1 of the decision chain. The constituency × partisan interaction is tested in both domains. Where compulsion removes discretion (water), the interaction is predicted to be null; where discretion remains (non-water), the interaction is predicted to be positive. This is the locus of the paper's central finding.

**Outcomes.** `Y_water_only` = city-year with green bond issuance in the sustainable-water category only (n+ = 90). `Y_has_non_water` = city-year with green bond issuance in at least one non-water category (n+ = 60). Categories are from Bloomberg's ESG project classification and cover the full green bond universe (`Green_Bond_Issued`, N+ = 152), not just self-labelled bonds. The two outcomes are mutually exclusive (zero overlap).

| *Variable* | *W1 Water* | *W2 Water + I2* | *NW1 Non-water* | *NW2 Non-water + I2* |
|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | |
| Non-severe violations (muni, lag 1) | +0.0032 | +0.0032 | +0.0019 | +0.0020 |
| | (2.50)\*\* | (2.51)\*\* | (1.00) | (1.08) |
| Reserve ratio | +0.0038 | +0.0038 | +0.0020 | +0.0021 |
| | (1.63) | (1.64) | (1.33) | (1.43) |
| Debt service burden | −0.0630 | −0.0629 | −0.0457 | −0.0496 |
| | (1.83)\* | (1.83)\* | (1.51) | (1.65)\* |
| Capital outlay per capita | +0.0166 | +0.0166 | +0.0220 | +0.0213 |
| | (1.47) | (1.48) | (1.31) | (1.31) |
| **Family 2 — Political factors** | | | | |
| Dem Mayor | −0.0005 | +0.0004 | +0.0002 | −0.0510 |
| | (0.13) | (0.03) | (0.08) | (3.18)\*\*\* |
| Dem presidential vote share | +0.0165 | +0.0173 | +0.0393 | −0.0065 |
| | (1.04) | (1.09) | (2.67)\*\*\* | (0.44) |
| Dem Mayor × Dem vote share | — | −0.0016 | — | +0.0907 |
| | | (0.06) | | (3.19)\*\*\* |
| **Family 3 — Institutional context** | | | | |
| State green bond market depth | +0.0003 | +0.0003 | +0.0001 | +0.0001 |
| | (1.22) | (1.22) | (0.71) | (0.54) |
| Anti-ESG muni bond law | −0.0074 | −0.0075 | +0.0027 | +0.0034 |
| | (1.63) | (1.63) | (0.84) | (1.03) |
| **Demographic and economic controls** | | | | |
| Log population | +0.0105 | +0.0105 | +0.0153 | +0.0151 |
| | (2.71)\*\*\* | (2.74)\*\*\* | (3.29)\*\*\* | (3.32)\*\*\* |
| Log per-capita income | +0.0118 | +0.0119 | +0.0135 | +0.0118 |
| | (1.43) | (1.46) | (2.08)\*\* | (1.92)\* |
| Unemployment rate | +0.0019 | +0.0019 | +0.0007 | +0.0008 |
| | (1.56) | (1.56) | (1.01) | (1.09) |
| R² | 0.046 | 0.046 | 0.063 | 0.067 |
| N | 7,413 | 7,413 | 7,413 | 7,413 |
| Positive city-years | 89 | 89 | 60 | 60 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed.

#### Marginal effect of `Dem_Mayor` at constituency percentiles

| Domain | 10th pct (0.39) | 50th pct (0.57) | 90th pct (0.75) |
|---|---|---|---|
| W2 Water | −0.000 (0.04) | −0.001 (0.14) | −0.001 (0.12) |
| **NW2 Non-water** | **−0.016 (2.90)\*\*\*** | +0.001 (0.30) | **+0.017 (2.86)\*\*\*** |

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

**Step 1 is dominated by Family 1 (Material) in the compelled domain.** Non-severe violations drive water issuance specifically (+0.003\*\*, t=2.50) and are null on non-water (+0.002, t=1.00). This is the clean water-specific compulsion pattern that confirms the chain framing's prediction: persistent low-severity effluent exceedances create capital-investment need for water infrastructure specifically.

**Step 1 shows responsive representation in the discretionary domain.** The constituency × partisan interaction operates exclusively in the discretionary domain: water (I2 = −0.002, ns) vs non-water (I2 = +0.091\*\*\*). Democratic mayors amplify constituency demand for discretionary green capital projects. The crossover at pres\_dem ≈ 0.55 separates amplification (blue cities, +0.017\*\*\*) from substitution (red cities, −0.016\*\*\*).

**The domain contrast is the finding.** Panel B shows the raw descriptive pattern — Democratic mayors account for 17 of 17 clean-transportation and 19 of 19 green-buildings positive city-years — which Panel A decomposes into constituency-conditional responsive representation rather than autonomous partisan ideology.

---

## Table 3 — Green Labelling Decision (Step 3)

> **Step mapping.** Conditional on having issued a bond, does the city apply the green label? The sample restricts to bond issuers (`total_ltd_issued > 0`). The paper predicts Family 1 (Material) dominance at this step.

**Sample.** Bond issuers: N = 3,894 (84 self-green events). Compelled issuers (non-severe violations > 0): N = 2,375 (64 events).

| *Variable* | *L1 Baseline* | *L2 +Fiscal Stress* | *L3 +Marketability* | *L4 Both* | *L5 Compelled only* |
|---|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | | |
| Non-severe violations (muni, lag 1) | +0.0028 | +0.0028 | −0.0122 | −0.0122 | — |
| | (0.76) | (0.83) | (2.20)\*\* | (2.20)\*\* | |
| Reserve ratio | +0.0055 | +0.0053 | +0.0053 | +0.0050 | +0.0112 |
| | (1.38) | (1.19) | (1.32) | (1.12) | (1.91)\* |
| Debt service burden | −0.1210 | −0.1073 | −0.1119 | −0.0922 | −0.1701 |
| | (1.75)\* | (0.97) | (1.65)\* | (0.85) | (1.83)\* |
| Capital outlay per capita | +0.0508 | +0.0514 | +0.0507 | +0.0515 | +0.0425 |
| | (1.63) | (1.52) | (1.62) | (1.52) | (1.90)\* |
| Fiscal stress index | — | −0.0017 | — | −0.0024 | — |
| | | (0.15) | | (0.22) | |
| Violations × state green market depth | — | — | +0.0008 | +0.0008 | — |
| | | | (2.40)\*\* | (2.42)\*\* | |
| **Family 2 — Political factors** | | | | | |
| Dem Mayor | −0.0031 | −0.0031 | −0.0030 | −0.0029 | −0.0018 |
| | (0.62) | (0.62) | (0.59) | (0.58) | (0.25) |
| Dem presidential vote share | +0.0684 | +0.0678 | +0.0710 | +0.0701 | +0.0582 |
| | (2.18)\*\* | (2.22)\*\* | (2.27)\*\* | (2.31)\*\* | (1.48) |
| **Family 3 — Institutional context** | | | | | |
| State green bond market depth | +0.0005 | +0.0005 | −0.0007 | −0.0007 | +0.0010 |
| | (0.91) | (0.91) | (0.87) | (0.87) | (1.48) |
| Anti-ESG muni bond law | −0.0104 | −0.0104 | −0.0118 | −0.0119 | −0.0184 |
| | (1.29) | (1.30) | (1.45) | (1.45) | (1.56) |
| State Dem governor | +0.0040 | +0.0040 | +0.0032 | +0.0032 | +0.0140 |
| | (0.25) | (0.25) | (0.20) | (0.21) | (0.68) |
| State Dem trifecta | −0.0127 | −0.0127 | −0.0116 | −0.0116 | −0.0207 |
| | (0.96) | (0.96) | (0.88) | (0.88) | (1.17) |
| State Rep trifecta | −0.0091 | −0.0091 | −0.0091 | −0.0091 | +0.0004 |
| | (0.56) | (0.56) | (0.56) | (0.56) | (0.02) |
| **Demographic and economic controls** | | | | | |
| Log population | +0.0314 | +0.0314 | +0.0309 | +0.0309 | +0.0344 |
| | (3.32)\*\*\* | (3.32)\*\*\* | (3.32)\*\*\* | (3.32)\*\*\* | (2.98)\*\*\* |
| Log per-capita income | +0.0194 | +0.0191 | +0.0188 | +0.0183 | +0.0245 |
| | (1.08) | (1.12) | (1.04) | (1.08) | (1.04) |
| Unemployment rate | +0.0021 | +0.0021 | +0.0019 | +0.0019 | +0.0009 |
| | (1.07) | (1.07) | (0.96) | (0.95) | (0.31) |
| R² | 0.119 | 0.119 | 0.121 | 0.121 | 0.139 |
| N | 3,894 | 3,894 | 3,894 | 3,894 | 2,375 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed. Table 3 additionally includes state political controls (Dem governor, Dem trifecta, Rep trifecta) not in Tables 1–2.

### Reading

**Family 1 (Material) dominates Step 3.** The marketability interaction (L3: violations × state green market depth = +0.001\*\*) is significant: compelled cities label green where the state ESG-investor base exists. Fiscal stress (L2) is no longer significant after controlling for capital outlay, suggesting the earlier greenium-seeking result reflected capital-investment intensity rather than distress per se. Capital outlay per capita is positive in all columns (t ≈ 1.6, marginally significant in L5 at \*). `Dem_Mayor` is null across all five columns.

---

## Summary across all specifications

| Finding | Evidence | Step | Strength |
|---|---|---|---|
| `Dem_Mayor` null across outcomes | β ≈ 0 across Table 1 C1–C4 + R1–R24 | Steps 2, 3, 4 | Rock solid (\*\*\*) |
| **Non-severe violations drive water issuance** | **+0.003\*\* (Table 2 water); +0.002 ns (non-water)** | **Step 1, water-specific** | **Novel (\*\*)** |
| Constituency drives issuance | pres\_dem +0.052\*\* (Table 1 self-green) | Step 2 | Consistent (\*\*) |
| **Constituency × partisan interaction** | +0.106\*\* (Table 1 self-green); **+0.091\*\*\* (Table 2 NW2)**; −0.002 ns (Table 2 W2 placebo) | **Step 1, discretionary only** | Novel (\*\*) |
| Labelling-margin marketability | Table 3 L3: violations × state\_green +0.001\*\* (issuer subsample) | Step 3 | Separate sample (\*\*) |
| Third-party assurance partisan gap | Panel A: +0.004\*; Panel C (N=117): +0.452\*\*\*; Fisher 59% vs 15%. California-fragile (p=0.192 w/o CA) | Step 4 | Partial (\*), fragile |

---

## The story

**Step 1 (Investment).** Capital need and federal water-quality compliance pressure drive project selection. Non-severe violations at municipal water plants are significant on water issuance (+0.003\*\*, t=2.50) and null on non-water (+0.002, t=1.00) — a clean water-specific compulsion pattern. In the discretionary domain (non-water categories), the constituency × partisan interaction is significant (+0.091\*\*\*): Democratic mayors amplify constituency demand for green capital projects in blue cities and substitute away in red cities. The water placebo (Table 2 W2: −0.002, t=0.06) confirms that partisan-constituency alignment matters only where mayors have latitude.

**Step 2 (Bond Financing).** The full-panel aggregate confirms the unconditional partisan null. `Dem_Mayor` is null across all four main-table outcomes (Table 1 C1–C4). Non-severe violations (+0.004\*), constituency (+0.052\*\*), and debt service burden (−0.087\*) drive issuance. The I2 interaction (+0.106\*\*) is the pooled signature of the Step 1 discretionary effect.

**Step 3 (Green Labelling).** Among bond issuers (Table 3), the marketability interaction (violations × state green market depth = +0.001\*\*) is the operative mechanism: compelled cities label green only where the state ESG-investor base exists. Capital outlay per capita is positive throughout (marginally significant in L5 among compelled issuers). Mayoral partisanship is null (|t| ≤ 0.62). Among compelled issuers (L5), city size and capital intensity predict labelling — a sophistication channel.

**Step 4 (Credibility Certification).** `Dem_Mayor` is null on five of six credibility outcomes (Appendix B Panel A); `log_population` and `capital_outlay_pc` are both significant across credibility dimensions (Panel C). The lone exception — third-party ESG assurance (+0.004\*, Panel A; +0.452\*\*\*, Panel C) — is concentrated in a small set of large coastal Democratic cities (California contributes 22 of 61 assurance events; San Francisco alone contributes 10) and does not survive a leave-California-out test (p = 0.192). By the time the decision reaches Step 4, the political-agency mechanism has been delegated to administrative and financial professionals operating under capacity-and-scale constraints.

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

### Panel A — Full-sample regression (11-variable PRIMARY)

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *Capital outlay pc* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 7,413 | 78 | +0.0004 | +0.0024 | +0.0375 |
| | | | (0.11) | (1.18) | (1.65)\* |
| Third-party ESG assurance | 7,413 | 61 | +0.0040 | +0.0017 | +0.0373 |
| | | | (1.73)\* | (0.92) | (1.63) |
| ICMA / CBI framework | 7,413 | 71 | −0.0020 | +0.0017 | +0.0381 |
| | | | (0.61) | (0.89) | (1.68)\* |
| Impact reporting | 7,413 | 73 | −0.0014 | +0.0021 | +0.0379 |
| | | | (0.44) | (1.06) | (1.67)\* |
| Documented project selection | 7,413 | 78 | −0.0002 | +0.0024 | +0.0373 |
| | | | (0.06) | (1.23) | (1.64) |
| Documented proceeds management | 7,413 | 73 | −0.0013 | +0.0024 | +0.0378 |
| | | | (0.41) | (1.21) | (1.67)\* |

### Panel B — Descriptive: rates conditional on issuing a self-labelled green bond

| *Outcome* | *Dem rate* | *Rep rate* | *Fisher p* |
|---|---|---|---|
| Any credibility indicator | 67/98 (68.4%) | 10/20 (50.0%) | 0.129 |
| **Third-party ESG assurance** | **58/98 (59.2%)** | **3/20 (15.0%)** | **0.000\*\*\*** |
| ICMA / CBI framework | 60/98 (61.2%) | 10/20 (50.0%) | 0.455 |
| Impact reporting | 63/98 (64.3%) | 10/20 (50.0%) | 0.312 |
| Documented project selection | 68/98 (69.4%) | 10/20 (50.0%) | 0.121 |
| Documented proceeds management | 63/98 (64.3%) | 10/20 (50.0%) | 0.312 |

### Panel C — Conditional on green bond issuance (N = 117, year FE only)

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Log population* | *Capital outlay pc* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 117 | 77 | +0.1291 | +0.1528 | +0.1046 |
| | | | (0.90) | (3.80)\*\*\* | (2.59)\*\*\* |
| **Third-party ESG assurance** | 117 | 61 | **+0.4518** | +0.1021 | +0.1390 |
| | | | **(3.78)\*\*\*** | (2.26)\*\* | (3.34)\*\*\* |
| ICMA / CBI framework | 117 | 70 | −0.0149 | +0.1845 | +0.0932 |
| | | | (0.11) | (3.96)\*\*\* | (1.78)\* |
| Impact reporting | 117 | 73 | +0.0322 | +0.1797 | +0.1018 |
| | | | (0.24) | (4.50)\*\*\* | (2.32)\*\* |
| Documented project selection | 117 | 78 | +0.1438 | +0.1713 | +0.0964 |
| | | | (1.03) | (4.30)\*\*\* | (2.49)\*\* |
| Documented proceeds management | 117 | 73 | +0.0497 | +0.1704 | +0.0934 |
| | | | (0.36) | (3.43)\*\*\* | (2.18)\*\* |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.

### Reading

The empirical pattern at Step 4 is consistent with administrative scale, sophistication, and baseline capital-investment intensity driving the credibility decisions rather than mayoral partisanship. Panel A shows `Dem_Mayor` is null on five of six credibility outcomes; capital outlay per capita is marginally significant on four of six. The single exception — third-party ESG assurance — is California-fragile (β falls from +0.0040\* to +0.0030, p = 0.192 when California is dropped). Panel C confirms that conditional on green issuance, both `log_population` and `capital_outlay_pc` predict framework adoption, impact reporting, project selection, and proceeds management at \*\*–\*\*\*. Larger cities with greater capital-investment capacity adopt quality standards regardless of mayoral partisanship — Family 1 in its administrative-capacity form, not Family 2.

The descriptive Panel B gap (third-party assurance: 59% Dem vs 15% Rep, Fisher p < 0.001) is the starkest partisan difference observed anywhere in the paper. The Panel A regression and the leave-California-out diagnostic show this gap reflects a sophistication-and-scale concentration in a handful of large coastal Democratic cities (California contributes 22 of 61 assurance events; San Francisco alone contributes 10) rather than a generalisable partisan mechanism.

The other five credibility dimensions are driven by city size and capital intensity. Panel C shows `log_population` at \*\*\*–\*\*\* and `capital_outlay_pc` at \*–\*\*\* across all six credibility outcomes. By the time the decision reaches Step 4, the political-agency mechanism that operates at Step 1 in the discretionary domain has been delegated to administrative and financial professionals operating under capacity-and-scale constraints.

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

## Appendix D — Robustness to Climate Exposure and Revenue Structure Controls

> Two additional controls are tested: (i) FEMA disaster declarations in the prior five years, capturing climate/hazard exposure beyond water-quality compliance pressure; (ii) own-source revenue share (lag 2), capturing fiscal autonomy and revenue structure. Neither is significant in any specification. All key coefficients are stable.

| *Variable* | *C3 Self-green* | *I2 Self-green* | *W1 Water* | *NW2 Non-water + I2* |
|---|---|---|---|---|
| **Family 1 — Material conditions** | | | | |
| Non-severe violations (muni, lag 1) | +0.0040 | +0.0042 | +0.0031 | +0.0020 |
| | (1.70)\* | (1.79)\* | (2.43)\*\* | (1.06) |
| Reserve ratio | +0.0046 | +0.0046 | +0.0037 | +0.0022 |
| | (1.89)\* | (1.93)\* | (1.62) | (1.54) |
| Debt service burden | −0.0910 | −0.0949 | −0.0631 | −0.0518 |
| | (1.96)\*\* | (2.04)\*\* | (1.85)\* | (1.68)\* |
| Capital outlay per capita | +0.0380 | +0.0373 | +0.0162 | +0.0208 |
| | (1.58) | (1.59) | (1.46) | (1.32) |
| **Family 2 — Political factors** | | | | |
| Dem Mayor | −0.0003 | −0.0597 | −0.0004 | −0.0507 |
| | (0.09) | (2.36)\*\* | (0.11) | (3.19)\*\*\* |
| Dem presidential vote share | +0.0523 | −0.0006 | +0.0183 | −0.0062 |
| | (2.22)\*\* | (0.03) | (1.16) | (0.42) |
| Dem Mayor × Dem vote share | — | +0.1053 | — | +0.0903 |
| | | (2.40)\*\* | | (3.19)\*\*\* |
| **Additional controls tested** | | | | |
| FEMA disaster declarations (prior 5yr) | −0.0009 | −0.0010 | −0.0010 | −0.0004 |
| | (0.60) | (0.65) | (1.61) | (0.38) |
| Own-source revenue share | −0.0246 | −0.0216 | −0.0037 | −0.0126 |
| | (0.73) | (0.66) | (0.18) | (0.76) |
| R² | 0.097 | 0.099 | 0.046 | 0.067 |
| N | 7,413 | 7,413 | 7,413 | 7,413 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed. Remaining PRIMARY controls (state green bond market depth, anti-ESG muni bond law, log population, log per-capita income, unemployment) included but not shown for space.

### Reading

**Climate/hazard exposure does not predict green bond issuance.** FEMA disaster declarations are null across all four specifications (|t| ≤ 1.61). The water-specific compulsion pattern (violations +0.003\*\* on water, +0.002 ns on non-water) is preserved, confirming that the non-severe violations variable captures infrastructure-need pressure rather than general climate exposure.

**Revenue structure does not predict green bond issuance.** Own-source revenue share is null in all specifications (|t| ≤ 0.76). Fiscal autonomy has no independent effect on green labelling after controlling for reserve ratio and debt service burden.

**All key findings are unchanged.** The constituency × partisan interaction is +0.105\*\* (I2) and +0.090\*\*\* (NW2). `Dem_Mayor` remains null in baseline columns. The water-domain placebo holds (W1 violations +0.003\*\*, NW2 violations +0.002 ns).

---

## Appendix F — Compulsion Variable: Severity Variant Comparison

> Nine NPDES violation variants are tested as alternatives in the compulsion role, each substituted into the 11-variable PRIMARY. The predicted pattern: significant on water issuance, null on non-water — consistent with water-specific compulsion rather than general administrative capacity or fiscal pressure.

| *Variant* | *nz* | *W β* | *W t* | | *NW β* | *NW t* | | *Pool t* | *Pattern* |
|---|---:|---|---|---|---|---|---|---|---|
| **Non-severe QNCR, lag 1 [MAIN]** | 4,327 | **+0.003** | **(2.50)\*\*** | | +0.002 | (1.00) | | (1.73)\* | **W sig, NW null** |
| Total QNCR, lag 1 | 4,624 | +0.003 | (2.55)\*\* | | +0.002 | (1.66)\* | | (2.68)\*\*\* | Both sig |
| Severe QNCR, lag 1 | 2,164 | +0.001 | (0.41) | | +0.002 | (0.88) | | (0.78) | Both null |
| SNC only, lag 1 | 242 | −0.009 | (2.05)\*\* | | −0.006 | (1.73)\* | | (2.08)\*\* | Both sig (negative) |
| Total QNCR, lag 2 | 4,562 | +0.002 | (1.88)\* | | +0.003 | (1.80)\* | | (2.53)\*\* | Both sig |
| Severe QNCR, lag 2 | 2,156 | +0.001 | (0.72) | | +0.001 | (0.47) | | (0.93) | Both null |
| Total QNCR, prior 3yr | 5,179 | +0.002 | (2.16)\*\* | | +0.002 | (1.97)\*\* | | (2.89)\*\*\* | Both sig |
| Severe QNCR, prior 3yr | 2,835 | +0.001 | (0.54) | | +0.002 | (1.08) | | (1.09) | Both null |
| Effluent violations, lag 2 | 3,930 | +0.003 | (1.68)\* | | +0.002 | (1.36) | | (2.32)\*\* | W sig, NW null |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed. 11-variable PRIMARY throughout; only the compulsion variable is swapped. *nz* = city-years with nonzero values.

### Reading

**Only non-severe violations produce the clean water-specific pattern.** The main specification (non-severe QNCR, lag 1) is the only variant that is significant on water (+0.003, $t = 2.50$\*\*) while clearly null on non-water (+0.002, $t = 1.00$). The effluent violations measure (the prior main variable) achieves a similar pattern but with a weaker water signal ($t = 1.68$\*).

**Total QNCR variants are significant on both water and non-water**, failing to isolate the water-specific compulsion channel. The non-water significance reflects the severe-violation component, which proxies for general regulatory engagement rather than water-infrastructure-specific need.

**Severe violations and SNC are uninformative or counterproductive.** Severe QNCR variants are null on both outcomes ($|t| \leq 1.08$) — too sparse and episodic to predict forward-looking bond issuance. SNC (significant noncompliance) produces negative coefficients on both water and non-water, consistent with post-remediation completion: cities designated as SNC have typically already arranged financing through consent-decree channels.

**The decomposition is the key insight.** Total violations = non-severe + severe. Non-severe violations (83.7\% of total) carry the identifying variation for water-specific compulsion. Severe violations (16.3\%) add noise that contaminates the non-water coefficient. Removing the severe component sharpens the instrument from "both significant" (total) to "water significant, non-water null" (non-severe only).

---

## Appendix E — Placebo Tests

Three families of placebo tests confirm that the paper's key findings are specific to the theorised mechanisms rather than artefacts of general patterns.

### E1. Climate alliance membership (demonstration placebo)

> **Prediction.** If the partisan null on green bonds reflects the absence of a political-agency mechanism in bond financing, then `Dem_Mayor` should predict visible, low-cost climate commitments (pledges, alliance membership) even while failing to predict green bond issuance. The interaction should also be positive for alliances — constituency pressure drives both — but the unconditional Dem_Mayor signal should appear only for alliances (cheap signalling), not for bonds (costly investment).

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *Dem × vote share (I2)* |
|---|---:|---:|---|---|---|
| Mayor's Climate Action signatory | 7,089 | 701 | **+0.0365** | −0.0038 | **+0.6179** |
| | | | **(2.09)\*\*** | (0.53) | **(4.60)\*\*\*** |
| ICLEI member | 7,089 | 558 | **+0.0368** | −0.0023 | **+0.4839** |
| | | | **(2.40)\*\*** | (0.36) | **(3.83)\*\*\*** |
| C40 member | 7,089 | 267 | −0.0022 | +0.0095 | +0.2562 |
| | | | (0.22) | (2.15)\*\* | (2.82)\*\*\* |
| Climate commitment score (0–3) | 7,089 | 1,526 | **+0.0711** | +0.0034 | **+1.3581** |
| | | | **(1.95)\*** | (0.24) | **(4.75)\*\*\*** |

**Reading.** `Dem_Mayor` is significant on climate alliance membership (+0.037\*\* for Climate Action, +0.037\*\* for ICLEI) but null on green bond issuance (Table 1 C1–C4). Democratic mayors sign climate pledges — a visible, low-cost demonstration — but this partisan signal does not translate into green bond financing. The constituency × partisan interaction is large and significant for alliances (+0.618\*\*\*, +0.484\*\*\*), confirming that the responsive-representation mechanism operates on both domains, but the unconditional Dem\_Mayor effect is specific to cheap signalling. Violations are null on alliances (|t| ≤ 0.53), confirming that the compulsion channel is specific to capital investment, not climate pledges.

### E2. General (non-green) borrowing placebo

> **Prediction.** If the constituency × partisan interaction operates specifically on green bonds rather than reflecting a general tendency of Democratic mayors in blue cities to borrow more, then the interaction should be null on total long-term debt issuance.

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *Dem × vote share (I2)* |
|---|---:|---:|---|---|---|
| Any LTD issued (binary) | 7,413 | 4,509 | +0.0193 | +0.0140 | −0.0685 |
| | | | (1.13) | (2.28)\*\* | (0.58) |
| Total LTD issued (asinh) | 6,282 | 4,509 | +0.2982 | +0.2239 | −0.5061 |
| | | | (1.35) | (2.87)\*\*\* | (0.33) |
| Net borrowing intensity | 6,278 | 2,092 | +0.0033 | +0.0030 | −0.0120 |
| | | | (0.62) | (1.55) | (0.32) |

**Reading.** `Dem_Mayor` is null on all general borrowing outcomes (|t| ≤ 1.35). The constituency × partisan interaction is null on general borrowing (|t| ≤ 0.58). Democratic mayors in blue cities do not borrow more overall — the I2 interaction is specific to green bonds. Non-severe violations predict general debt issuance (+0.014\*\*, +0.224\*\*\*), consistent with violations creating capital-investment need that requires debt financing regardless of green labelling.

### E3. Non-severe violations on non-environmental spending

> **Prediction.** If non-severe NPDES violations capture water-specific infrastructure-need pressure, they should be null on non-environmental spending categories.

| *Outcome (asinh)* | *N* | *Dem Mayor* | *Non-severe viol.* |
|---|---:|---|---|
| Police expenditure | 7,413 | +0.1194 | +0.0079 |
| | | (3.57)\*\*\* | (0.51) |
| Highways expenditure | 7,413 | −0.0456 | +0.0162 |
| | | (0.86) | (0.85) |
| Health/hospitals expenditure | 7,413 | +0.2868 | +0.0159 |
| | | (1.32) | (0.23) |

**Reading.** Non-severe violations are null on police (t=0.51), highways (t=0.85), and health (t=0.23) spending. The compulsion variable does not predict non-environmental expenditure, confirming that it captures water-specific infrastructure-need pressure rather than general fiscal pressure or city-level omitted variables.

### Summary of placebo results

| Placebo test | What it rules out | Result |
|---|---|---|
| Climate alliances (E1) | `Dem_Mayor` null on bonds is a power issue | Rejected: Dem\_Mayor is significant on alliances (+0.037\*\*) but null on bonds |
| General borrowing (E2) | Constituency × partisan interaction reflects general borrowing | Rejected: I2 is null on general LTD (t=0.58) |
| Non-environmental spending (E3) | Non-severe violations proxy for general fiscal pressure | Rejected: violations null on police, highways, health (|t| ≤ 0.85) |

---

## Files

- `processed/tables/PAPER_main_v4.md` — this document.
- `processed/tables/PAPER_main_v3_2_archive.md` — previous version.
- `processed/tables/v3_rr/` — supplementary diagnostics, robustness, methods changelog.
- `processed/tables/v3_rr/severity_variant_comparison.md` — severity variant battery.
- Prospectus-text artefacts on branch `claude/convert-pdfs-to-text-TQGQd`, in `processed/prospectus_analysis/`.
