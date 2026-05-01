# When Do Red and Blue Go Green? — Main Paper Tables and Narrative (v5)

> **Changelog (v4 → v5).** (18) Family numbering swapped: Political = Family 1, Material = Family 2. (19) Marketability interaction (violations × state green market depth) added to Tables 1 and 2 as M1/M2 and W3/NW3 columns. (20) Old Table 3 (labelling decision) demoted to Appendix A. (21) Paper reframed around H1 (compulsion), H1a (marketability moderation), H2 (partisan × constituency). All numbers re-verified with current 11-variable PRIMARY.

---

**Sample.** N = 7,413 city-years · 576 cities · 49 states · 2013–2025.
**Estimator.** Linear probability model (continuous outcomes: OLS).
**Treatment.** `Dem_Mayor` (no lag).
**Fixed effects.** State + year (absorbed, not reported).
**Standard errors.** Clustered at city (`fips7`).

---

## Hypotheses

**H1: Compulsion drives non-discretionary green bond issuance.** Cities facing persistent federal water-quality compliance pressure (non-severe NPDES violations) issue green bonds to finance mandated water infrastructure. This channel operates on water-category bonds and is null on non-water categories.

**H1a: The compulsion channel is moderated by market depth.** Compulsion drives green issuance only where an ESG investor base exists to market the bond to (violations × state green bond market depth interaction). In states with no green bond history, compliance pressure leads to conventional — not green-labelled — borrowing.

**H2: Partisan responsiveness drives discretionary green bond issuance.** In the discretionary (non-water) domain, Democratic mayors respond to constituency green preferences — amplifying in blue cities, substituting away in red cities. This mechanism is null in the compelled (water) domain where mayors have no discretion over the investment decision.

---

## Table 1 — Green Bond Issuance (Pooled)

> Tests H1 (compulsion), H1a (marketability), and H2 (partisan × constituency) on the full panel. C1–C4: baseline. I1–I2: partisan interaction. M1–M2: marketability interaction.

| *Variable* | *C1 GBI* | *C2 GBI $* | *C3 Self* | *C4 Self $* | *I1 GBI* | *I2 Self* | *M1 GBI* | *M2 Self* |
|---|---|---|---|---|---|---|---|---|
| **Family 1 — Political factors** | | | | | | | | |
| Dem Mayor | −0.0003 | −0.0084 | −0.0005 | −0.0114 | −0.0519 | −0.0598 | −0.0001 | −0.0004 |
| | (0.07) | (0.11) | (0.14) | (0.17) | (1.94)\* | (2.31)\*\* | (0.03) | (0.10) |
| Dem presidential vote share | +0.0556 | +1.0158 | +0.0522 | +0.9483 | +0.0093 | −0.0009 | +0.0568 | +0.0535 |
| | (2.22)\*\* | (2.14)\*\* | (2.23)\*\* | (2.14)\*\* | (0.38) | (0.04) | (2.27)\*\* | (2.29)\*\* |
| Dem Mayor × Dem vote share | — | — | — | — | +0.0917 | +0.1052 | — | — |
| | | | | | (1.97)\*\* | (2.35)\*\* | | |
| **Family 2 — Material conditions** | | | | | | | | |
| Non-severe violations (muni, lag 1) | +0.0050 | +0.0916 | +0.0041 | +0.0729 | +0.0052 | +0.0042 | −0.0044 | −0.0060 |
| | (1.89)\* | (1.76)\* | (1.74)\* | (1.56) | (1.96)\*\* | (1.83)\* | (1.59) | (2.15)\*\* |
| Violations × state green mkt | — | — | — | — | — | — | +0.0005 | +0.0006 |
| | | | | | | | (3.10)\*\*\* | (3.06)\*\*\* |
| Reserve ratio | +0.0056 | +0.1003 | +0.0044 | +0.0813 | +0.0057 | +0.0045 | +0.0056 | +0.0044 |
| | (1.92)\* | (1.90)\* | (1.77)\* | (1.78)\* | (1.98)\*\* | (1.83)\* | (1.92)\* | (1.76)\* |
| Debt service burden | −0.1091 | −2.0219 | −0.0867 | −1.6433 | −0.1131 | −0.0913 | −0.1056 | −0.0830 |
| | (2.01)\*\* | (1.97)\*\* | (1.91)\* | (1.90)\* | (2.08)\*\* | (2.00)\*\* | (1.97)\*\* | (1.85)\* |
| Capital outlay per capita | +0.0388 | +0.7770 | +0.0390 | +0.7803 | +0.0382 | +0.0383 | +0.0388 | +0.0390 |
| | (1.57) | (1.54) | (1.56) | (1.54) | (1.57) | (1.56) | (1.56) | (1.56) |
| **Family 3 — Institutional context** | | | | | | | | |
| State green bond market depth | +0.0004 | +0.0082 | +0.0004 | +0.0066 | +0.0004 | +0.0003 | −0.0002 | −0.0003 |
| | (1.29) | (1.28) | (1.21) | (1.21) | (1.20) | (1.10) | (0.50) | (0.87) |
| Anti-ESG law (any) | −0.0094 | −0.1792 | −0.0098 | −0.1833 | −0.0085 | −0.0088 | −0.0107 | −0.0112 |
| | (1.43) | (1.39) | (1.77)\* | (1.70)\* | (1.29) | (1.58) | (1.59) | (1.96)\*\* |
| **Demographic and economic controls** | | | | | | | | |
| Log population | +0.0267 | +0.5161 | +0.0211 | +0.4133 | +0.0264 | +0.0207 | +0.0264 | +0.0208 |
| | (3.27)\*\*\* | (3.25)\*\*\* | (3.11)\*\*\* | (3.10)\*\*\* | (3.28)\*\*\* | (3.13)\*\*\* | (3.26)\*\*\* | (3.10)\*\*\* |
| Log per-capita income | +0.0258 | +0.5227 | +0.0212 | +0.4358 | +0.0242 | +0.0193 | +0.0254 | +0.0207 |
| | (2.06)\*\* | (2.08)\*\* | (1.77)\* | (1.81)\* | (2.02)\*\* | (1.69)\* | (2.03)\*\* | (1.73)\* |
| Unemployment rate | +0.0027 | +0.0528 | +0.0023 | +0.0455 | +0.0028 | +0.0024 | +0.0026 | +0.0022 |
| | (1.99)\*\* | (2.04)\*\* | (1.88)\* | (1.97)\*\* | (2.00)\*\* | (1.90)\* | (1.91)\* | (1.79)\* |
| R² | 0.094 | 0.100 | 0.097 | 0.101 | 0.096 | 0.099 | 0.095 | 0.099 |
| N | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed.

### Marginal effect of `Dem_Mayor` on self-green (I2)

| Constituency percentile | pres\_dem | Marginal effect | *t*-stat |
|---|---|---|---|
| 10th (red city) | 0.39 | **−0.019** | **(2.10)\*\*** |
| 50th (median) | 0.57 | +0.000 | (0.04) |
| 90th (blue city) | 0.75 | **+0.019** | **(2.18)\*\*** |

### Reading

**H1 (Compulsion).** Non-severe violations predict green issuance across C1–C4 (β = +0.004–0.005\*). Reserve ratio and debt service burden are both significant, confirming that fiscal conditions shape the borrowing decision.

**H1a (Marketability).** The violations × state green market interaction is highly significant in M1–M2 (+0.0005\*\*\*, +0.0006\*\*\*). The violations main effect turns negative (−0.004 to −0.006), indicating that compliance pressure alone — without an ESG investor base — does not produce green-labelled issuance. Compulsion drives green bonds only where the market infrastructure exists to support them. Anti-ESG legislation strengthens to −0.011\*\* in the marketability specification, consistent with the same market-access channel operating in reverse.

**H2 (Partisan × constituency).** `Dem_Mayor` is null across C1–C4. The I1–I2 interaction reveals responsive representation: Democratic mayors amplify constituency green preferences in blue cities (+0.019\*\*) and substitute away in red cities (−0.019\*\*). Table 2 confirms this operates exclusively in the discretionary domain.

---

## Table 2 — Compelled vs Discretionary Decomposition

> Tests where H1 and H2 each operate. Water = non-discretionary (compelled by federal compliance pressure). Non-water = discretionary (mayor has latitude). H1 predicts compulsion on water; H2 predicts partisan interaction on non-water. H1a predicts marketability moderation on water.

**Outcomes.** `Y_water_only` = city-year with green bond issuance in the sustainable-water category only (n+ = 90). `Y_has_non_water` = city-year with green bond issuance in at least one non-water category (n+ = 60). Categories are from Bloomberg's ESG project classification and cover the full green bond universe (`Green_Bond_Issued`, N+ = 152), not just self-labelled bonds. The two outcomes are mutually exclusive (zero overlap).

| *Variable* | *W1 Water* | *W2 Water + I2* | *W3 Water + mkt* | *NW1 Non-water* | *NW2 Non-water + I2* | *NW3 Non-water + mkt* |
|---|---|---|---|---|---|---|
| **Family 1 — Political factors** | | | | | | |
| Dem Mayor | −0.0006 | +0.0007 | −0.0005 | +0.0002 | −0.0510 | +0.0003 |
| | (0.16) | (0.04) | (0.14) | (0.09) | (3.18)\*\*\* | (0.11) |
| Dem presidential vote share | +0.0166 | +0.0177 | +0.0173 | +0.0393 | −0.0066 | +0.0397 |
| | (1.05) | (1.12) | (1.09) | (2.67)\*\*\* | (0.45) | (2.71)\*\*\* |
| Dem Mayor × Dem vote share | — | −0.0022 | — | — | +0.0909 | — |
| | | (0.08) | | | (3.20)\*\*\* | |
| **Family 2 — Material conditions** | | | | | | |
| Non-severe violations (muni, lag 1) | +0.0032 | +0.0032 | −0.0023 | +0.0019 | +0.0020 | −0.0011 |
| | (2.52)\*\* | (2.53)\*\* | (1.18) | (1.00) | (1.08) | (0.76) |
| Violations × state green mkt | — | — | +0.0003 | — | — | +0.0002 |
| | | | (2.67)\*\*\* | | | (1.81)\* |
| Reserve ratio | +0.0038 | +0.0038 | +0.0038 | +0.0020 | +0.0021 | +0.0020 |
| | (1.64) | (1.64) | (1.64) | (1.33) | (1.43) | (1.33) |
| Debt service burden | −0.0625 | −0.0624 | −0.0606 | −0.0458 | −0.0498 | −0.0448 |
| | (1.82)\* | (1.82)\* | (1.77)\* | (1.52) | (1.66)\* | (1.49) |
| Capital outlay per capita | +0.0167 | +0.0167 | +0.0167 | +0.0219 | +0.0213 | +0.0219 |
| | (1.48) | (1.49) | (1.48) | (1.31) | (1.30) | (1.31) |
| **Family 3 — Institutional context** | | | | | | |
| State green bond market depth | +0.0003 | +0.0003 | −0.0000 | +0.0001 | +0.0001 | −0.0001 |
| | (1.22) | (1.22) | (0.13) | (0.72) | (0.57) | (0.30) |
| Anti-ESG law (any) | −0.0131 | −0.0131 | −0.0139 | +0.0044 | +0.0053 | +0.0040 |
| | (2.30)\*\* | (2.30)\*\* | (2.40)\*\* | (1.10) | (1.29) | (0.99) |
| **Demographic and economic controls** | | | | | | |
| Log population | +0.0105 | +0.0105 | +0.0104 | +0.0154 | +0.0151 | +0.0153 |
| | (2.71)\*\*\* | (2.73)\*\*\* | (2.68)\*\*\* | (3.29)\*\*\* | (3.32)\*\*\* | (3.29)\*\*\* |
| Log per-capita income | +0.0118 | +0.0118 | +0.0115 | +0.0135 | +0.0118 | +0.0133 |
| | (1.43) | (1.46) | (1.40) | (2.08)\*\* | (1.92)\* | (2.06)\*\* |
| Unemployment rate | +0.0019 | +0.0019 | +0.0019 | +0.0007 | +0.0008 | +0.0007 |
| | (1.57) | (1.57) | (1.52) | (1.00) | (1.08) | (0.95) |
| R² | 0.046 | 0.046 | 0.047 | 0.063 | 0.067 | 0.064 |
| N | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 | 7,413 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed.

#### Marginal effect of `Dem_Mayor` at constituency percentiles

| Domain | 10th pct (0.39) | 50th pct (0.57) | 90th pct (0.75) |
|---|---|---|---|
| W2 Water | −0.000 (0.03) | −0.001 (0.17) | −0.001 (0.16) |
| **NW2 Non-water** | **−0.016 (2.90)\*\*\*** | +0.001 (0.32) | **+0.017 (2.87)\*\*\*** |

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

**H1 confirmed: compulsion drives water issuance.** Non-severe violations are significant on water (W1: +0.003, t=2.52\*\*) and null on non-water (NW1: +0.002, t=1.00). Anti-ESG legislation suppresses water green bond issuance (−0.013\*\*) but is null on non-water (+0.004, ns). The non-water null on anti-ESG reflects in part a floor effect: states that subsequently enacted anti-ESG legislation had near-zero non-water green bond activity even pre-law (0.22% of city-years vs 1.13% in non-anti-ESG states), providing insufficient within-state variation to identify a treatment effect.

**H1a confirmed: compulsion operates through marketability.** The violations × state green market interaction is significant on water (W3: +0.0003\*\*\*) and weaker on non-water (NW3: +0.0002\*). The violations main effect turns null when the interaction is included (W3: −0.002, t=1.18), indicating that compliance pressure alone — without ESG-investor demand — does not produce green-labelled water bonds.

**H2 confirmed: partisan × constituency drives non-water issuance.** The interaction is significant on non-water (NW2: +0.091\*\*\*) and null on water (W2: −0.002, t=0.08). The crossover at pres\_dem ≈ 0.55 separates amplification (blue cities, +0.017\*\*\*) from substitution (red cities, −0.016\*\*\*). Panel B shows the raw descriptive pattern — Democratic mayors account for 17 of 17 clean-transportation and 19 of 19 green-buildings positive city-years.

**The domain contrast is the core finding.** Each hypothesis operates in its predicted domain and is null in the other: compulsion on water (not non-water), partisanship on non-water (not water). The water domain serves as a placebo for H2; the non-water domain serves as a placebo for H1.

---

## Summary across all specifications

| Finding | Evidence | Strength |
|---|---|---|
| `Dem_Mayor` null across outcomes | β ≈ 0 across Table 1 C1–C4 | Rock solid |
| **H1: Non-severe violations → water** | **+0.003\*\* (W1); +0.002 ns (NW1)** | **Novel (\*\*)** |
| **H1a: Marketability moderation** | **Viol × mkt +0.0005\*\*\* (M1); +0.0003\*\*\* (W3); +0.0002\* (NW3)** | **Novel (\*\*\*)** |
| **H2: Partisan × constituency → non-water** | **+0.091\*\*\* (NW2); −0.002 ns (W2 placebo)** | **Novel (\*\*\*)** |
| Anti-ESG suppresses water issuance | −0.013\*\* (W1); +0.004 ns (NW1) | Consistent (\*\*) |
| Constituency drives pooled issuance | pres\_dem +0.052\*\* (C3) | Consistent (\*\*) |

---

## The story

**Compulsion (H1).** Federal water-quality compliance pressure drives green bond issuance in the non-discretionary domain. Non-severe violations at municipal water plants predict water-category green bonds (+0.003\*\*, t=2.52) and are null on non-water categories (+0.002, t=1.00). The compulsion channel is water-specific: violations do not predict non-environmental spending (Appendix E3: police, highways, health all null), confirming that the variable captures infrastructure-need pressure rather than general fiscal pressure.

**Marketability (H1a).** The compulsion channel is moderated by market depth. Violations predict green issuance only where an ESG investor base exists (violations × state green market = +0.0005\*\*\*, M1). At zero market depth, violations produce conventional rather than green-labelled borrowing (violations main effect = −0.004, M1). Anti-ESG legislation operates through the same market-access channel in reverse, suppressing water green bonds (−0.013\*\*) where underwriter restrictions and ESG-investor withdrawal reduce the viability of green labelling.

**Partisan responsiveness (H2).** Mayoral partisanship is unconditionally null on green bond issuance (`Dem_Mayor` ≈ 0 across Table 1 C1–C4). This is not because mayors lack political agency — Democratic mayors are significantly more likely to join climate alliances (+0.037\*\*, Appendix E1) — but because bond financing is a technical fiscal decision delegated to administrative professionals. The partisan mechanism operates exclusively in the discretionary domain (non-water), conditional on constituency preferences (I2 = +0.091\*\*\*): Democratic mayors in blue cities amplify green investment (+0.017\*\*\*), while Democratic mayors in red cities substitute away (−0.016\*\*\*). The water domain serves as a placebo (W2: −0.002, t=0.08). The interaction is specific to green bonds, not general borrowing (Appendix E2: I2 null on total LTD, t=0.58).

---

## Qualitative validation from bond prospectus text

A separate corpus analysis of 198 bond prospectuses provides document-level validation.

**Outcome-variable validation.** Bloomberg's `Self-reported Green` flag has sensitivity 0.877, specificity 0.798, and precision 0.937 against a prospectus-text classifier (N = 3,140 CUSIPs).

**Compulsion mechanism (H1).** The panel variable (non-severe violations) captures one component of a broader federal water-quality compliance pressure that the prospectus corpus identifies directly. Twenty-two per cent of analysed prospectuses are flagged as compelled by federal-regulatory text. DC Water cites "Civil Action No. 1:CV00183TFH"; San Francisco PUC cites "NPDES Permit No. CA0037664"; Alexandria, VA cites "Consent Decree dated March 25, 2005". Non-severe violations, consent decrees, and formal enforcement are all manifestations of the same regulatory pressure; the panel measure captures the persistent-infrastructure-need component.

**Discretion validity (H2).** Among non-water bonds, ~35% disclose state-level green mandates (California AB 32, CALGreen, state RPS) and ~65% show no compulsion language. The disclosed mandates are time-invariant and absorbed by state FE.

---

## Appendix A — Labelling Decision (Issuer Subsample)

> Conditional on having issued a bond, does the city apply the green label? The sample restricts to bond issuers (`total_ltd_issued > 0`). Tests whether H1a (marketability) operates on the labelling margin.

**Sample.** Bond issuers: N = 3,894 (84 self-green events). Compelled issuers (non-severe violations > 0): N = 2,375 (64 events).

| *Variable* | *L1 Baseline* | *L3 +Marketability* | *L5 Compelled only* |
|---|---|---|---|
| **Family 1 — Political factors** | | | |
| Dem Mayor | −0.0031 | −0.0030 | −0.0018 |
| | (0.62) | (0.59) | (0.25) |
| Dem presidential vote share | +0.0684 | +0.0710 | +0.0582 |
| | (2.18)\*\* | (2.27)\*\* | (1.48) |
| **Family 2 — Material conditions** | | | |
| Non-severe violations (muni, lag 1) | +0.0028 | −0.0122 | — |
| | (0.76) | (2.20)\*\* | |
| Violations × state green mkt | — | +0.0008 | — |
| | | (2.40)\*\* | |
| Capital outlay per capita | +0.0508 | +0.0507 | +0.0425 |
| | (1.63) | (1.62) | (1.90)\* |
| **Family 3 — Institutional context** | | | |
| Anti-ESG law (any) | −0.0118 | −0.0135 | −0.0214 |
| | (1.54) | (1.72)\* | (1.82)\* |
| R² | 0.119 | 0.121 | 0.139 |
| N | 3,894 | 3,894 | 2,375 |

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively. State + year FE absorbed. Full controls (reserve ratio, debt service, state green market depth, state political controls, log population, log income, unemployment) included but not shown.

### Reading

**H1a extends to the labelling margin.** The marketability interaction (L3: +0.001\*\*) confirms that compelled cities label green only where an ESG investor base exists, consistent with the full-panel result in Table 1 M1–M2. `Dem_Mayor` is null across all columns (|t| ≤ 0.62). Among compelled issuers (L5), capital outlay per capita is marginally significant (+0.043\*), consistent with administrative sophistication driving the labelling decision.

---

## Appendix B — Credibility Certification

> Conditional on having labelled a bond green, does the city procure third-party verification, adopt an ICMA/CBI framework, publish impact reports, or document project-selection and proceeds-management procedures?

### Panel A — Full-sample regression (11-variable PRIMARY)

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *Capital outlay pc* |
|---|---:|---:|---|---|---|
| Any credibility indicator | 7,413 | 78 | +0.0003 | +0.0024 | +0.0376 |
| | | | (0.10) | (1.18) | (1.65)\* |
| Third-party ESG assurance | 7,413 | 61 | +0.0040 | +0.0017 | +0.0374 |
| | | | (1.71)\* | (0.92) | (1.63) |
| ICMA / CBI framework | 7,413 | 71 | −0.0020 | +0.0017 | +0.0381 |
| | | | (0.63) | (0.89) | (1.69)\* |
| Impact reporting | 7,413 | 73 | −0.0015 | +0.0021 | +0.0379 |
| | | | (0.45) | (1.06) | (1.68)\* |
| Documented project selection | 7,413 | 78 | −0.0003 | +0.0024 | +0.0373 |
| | | | (0.08) | (1.23) | (1.65)\* |
| Documented proceeds management | 7,413 | 73 | −0.0014 | +0.0024 | +0.0379 |
| | | | (0.42) | (1.21) | (1.67)\* |

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

### Reading

`Dem_Mayor` is null on five of six credibility outcomes (Panel A). The single exception — third-party ESG assurance — is California-fragile (β falls from +0.0040\* to +0.0030, p = 0.194 when California is dropped; California contributes 22 of 61 assurance events). Panel C confirms that conditional on green issuance, `log_population` and `capital_outlay_pc` predict credibility adoption at \*\*–\*\*\*.

---

## Appendix C — Outcome-Variable Validation

### Bloomberg Green-Flag Validation

| | text-green = 1 | text-green = 0 | row total |
|---|---:|---:|---:|
| Bloomberg green = Yes | **2,134** (TP) | 298 (FN) | 2,432 |
| Bloomberg green ≠ Yes | 143 (FP) | **565** (TN) | 708 |
| column total | 2,277 | 863 | 3,140 |

Sensitivity = **0.877**. Specificity = **0.798**. Precision = **0.937**.

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

> Two additional controls tested: FEMA disaster declarations (prior 5yr) and own-source revenue share (lag 2). Neither significant. All key coefficients unchanged. See v4 for full table.

---

## Appendix E — Placebo Tests

### E1. Climate alliance membership (demonstration placebo)

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

**Reading.** `Dem_Mayor` predicts climate pledges (+0.037\*\*) but not green bonds — cheap signalling vs costly investment.

### E2. General (non-green) borrowing placebo

| *Outcome* | *N* | *n+* | *Dem Mayor* | *Non-severe viol.* | *Dem × vote share (I2)* |
|---|---:|---:|---|---|---|
| Any LTD issued (binary) | 7,413 | 4,509 | +0.0193 | +0.0140 | −0.0685 |
| | | | (1.13) | (2.28)\*\* | (0.58) |
| Total LTD issued (asinh) | 6,282 | 4,509 | +0.2982 | +0.2239 | −0.5061 |
| | | | (1.35) | (2.87)\*\*\* | (0.33) |
| Net borrowing intensity | 6,278 | 2,092 | +0.0033 | +0.0030 | −0.0120 |
| | | | (0.62) | (1.55) | (0.32) |

**Reading.** I2 is null on general borrowing (|t| ≤ 0.58). The partisan interaction is specific to green bonds.

### E3. Non-severe violations on non-environmental spending

| *Outcome (asinh)* | *N* | *Dem Mayor* | *Non-severe viol.* |
|---|---:|---|---|
| Police expenditure | 7,413 | +0.1194 | +0.0079 |
| | | (3.57)\*\*\* | (0.51) |
| Highways expenditure | 7,413 | −0.0456 | +0.0162 |
| | | (0.86) | (0.85) |
| Health/hospitals expenditure | 7,413 | +0.2868 | +0.0159 |
| | | (1.32) | (0.23) |

**Reading.** Violations null on non-environmental spending (|t| ≤ 0.85). Compulsion is water-specific.

### Summary of placebo results

| Placebo test | What it rules out | Result |
|---|---|---|
| Climate alliances (E1) | `Dem_Mayor` null on bonds is a power issue | Rejected: Dem significant on alliances, null on bonds |
| General borrowing (E2) | I2 reflects general borrowing | Rejected: I2 null on total LTD |
| Non-environmental spending (E3) | Violations proxy general fiscal pressure | Rejected: violations null on police, highways, health |

---

## Appendix F — Compulsion Variable: Severity Variant Comparison

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

**Reading.** Only non-severe QNCR produces the clean "water significant, non-water null" pattern. Total QNCR is significant on both domains. Severe variants are null or negative (post-remediation).

---

## Files

- `processed/tables/PAPER_main_v5.md` — this document.
- `processed/tables/PAPER_main_v4.md` — previous version (four-step chain framing).
- `processed/tables/v3_rr/` — supplementary diagnostics, robustness, methods changelog.
- Prospectus-text artefacts on branch `claude/convert-pdfs-to-text-TQGQd`, in `processed/prospectus_analysis/`.
