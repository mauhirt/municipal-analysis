# Table 2 — Use of Proceeds: Discretion Test

**Purpose.** Test whether the `Dem_Mayor` null in Table 1 is hiding a partisan effect in discretionary (non-water) green bond categories. Test whether the constituency × partisan interaction (I2) operates in the discretionary domain and is absent in the compelled domain.

**Sample:** N = 6,825 city-years · 576 cities · 49 states · 2014–2025.
**Spec:** 10-variable PRIMARY (same as Table 1). W2 and NW2 add `Dem_Mayor × pres_dem_two_party_share_lag2`.
**FE:** state + year. **SE:** clustered at city.

---

## Panel A — Regression: water vs non-water

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

### Marginal effect of `Dem_Mayor` at constituency percentiles

| Domain | 10th pct (0.39) | 50th pct (0.57) | 90th pct (0.75) |
|---|---|---|---|
| **W2 Water** | −0.0003 (0.06) | −0.0006 (0.15) | −0.0009 (0.12) |
| **NW2 Non-water** | **−0.0167 (2.74)\*\*\*** | +0.0015 (0.56) | **+0.0202 (3.01)\*\*\*** |

### Reading

**Water (W1/W2).** `Dem_Mayor` is null with and without the interaction. The I2 interaction is **−0.002 (t = 0.05)** — flat zero. Marginal effects at all percentiles are indistinguishable from zero (|t| < 0.15). Water issuance is compulsion-driven. The constituency × partisan mechanism has no traction in this domain.

**Non-water (NW1/NW2).** Without the interaction (NW1), `Dem_Mayor` is null (+0.001, t = 0.41) and constituency (`pres_dem_share`) is significant (+0.037\*\*). With the interaction (NW2), `Dem_Mayor` turns **−0.056\*\*\*** (t = 3.08) and the interaction is **+0.102\*\*\*** (t = 3.14). The constituency main effect absorbs into the interaction (−0.014, ns). Democratic mayors amplify in blue cities (90th pct: +0.020\*\*\*) and substitute away in red cities (10th pct: −0.017\*\*\*). The crossover is at pres\_dem ≈ 0.55, close to the sample median.

**Anti-ESG muni bond law** is weakly negative in water (−0.011\*, t = 1.88) but null in non-water. Consistent with anti-ESG legal friction biting where the regulatory channel is most active.

**The domain contrast is the finding.** Water (I2 = −0.002, ns) vs non-water (I2 = +0.102\*\*\*). The constituency × partisan interaction operates **exclusively in the discretionary domain**. Where compulsion forces issuance (water), mayoral partisan-constituency alignment is irrelevant. Where mayors have latitude (non-water), Democratic mayors respond to their electorate's green preferences.

---

## Panel B — Descriptive: individual sparse categories

Seven individual use-of-proceeds categories with 3–20 positive city-years. Too sparse for regression with FE. Raw counts and Fisher exact tests.

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

**The raw partisan gap is stark.** Democratic mayors account for virtually all issuance in every discretionary category: 17 of 17 clean-transportation, 19 of 19 green-buildings, 7 of 7 climate-adaptation positive city-years. Fisher exact p-values are \*\* to \*\*\* for all but natural resource management.

**Panel A shows this gap is not autonomous partisan agency.** The NW1 regression (without the interaction) absorbs the entire Fisher gap into state FE and constituency. The NW2 regression (with the interaction) reveals that the residual partisan variation operates through constituency alignment: Democratic mayors issue more in blue cities and fewer in red cities, with the two tails cancelling to produce the NW1 null.

**H2a (stronger partisan effect where compulsion is weaker) is not supported in the identified regressions.** The apparent Fisher gap is a geographic-selection artifact, modulated by constituency × partisan responsive representation in the discretionary domain.

---

## Summary

**Table 2 answers the composition-artifact attack on Table 1.** Panel A shows `Dem_Mayor` is null on both water and non-water aggregate outcomes in the baseline specifications. The Panel A interaction columns reveal what drives the non-water pattern: constituency × partisan amplification (+0.102\*\*\*), discretion-specific (water placebo: −0.002, ns).

Panel B shows the raw descriptive pattern that reviewers will see: Democratic mayors do essentially all non-water issuance. Panel A decomposes this: it is a constituency-responsive pattern operating through mayoral partisan alignment in the discretionary domain, not autonomous partisan ideology.

**The channel differs across domains.** Water: compulsion (NPDES) dominates, no partisan mechanism. Non-water: constituency × partisan responsive representation dominates, with the two equal-and-opposite tails at the 10th and 90th percentiles of constituency composition producing the population-weighted null.
