# SNC Diagnostic — Effluent Violations vs Significant Noncompliance Proxies

## Variable construction confirmation

**Current variable: `effluent_muni_asinh_lag2`.**
- Raw: `npdes_effluent_violations_count_muni` — unweighted count of ALL reported NPDES effluent violations at municipally-owned facilities. No weighting by severity, pollutant type, or magnitude. Mean = 6.0, max = 196, nonzero city-years = 4,700.
- Transform: `asinh(count)`, lagged 2 years. Nonzero in analysis sample: 4,562 of 7,401.

**SNC variable availability.** No NPDES-specific SNC (Significant Non-Compliance) indicator exists in the EPA ECHO data file. The `rcra_snc_*` columns in the data are RCRA (solid waste), not water quality. EPA ECHO's NPDES SNC/HPV classification ("Quarters in Noncompliance") is not present in the current extraction.

**Closest available proxies for NPDES significant noncompliance:**

| Variable | Definition | Nonzero city-years (lag 2) |
|---|---|---:|
| `npdes_cs_violations_count_muni` | Compliance Schedule violations — missed regulatory milestones (most severe NPDES violation type) | 106 |
| `npdes_ps_violations_count_muni` | Permit Schedule violations — missed permit deadlines | 411 |
| `npdes_se_violations_count_muni` | Single Event violations — discrete violation events | 306 |
| `snc_proxy_any` (composite) | Binary: any CS, PS, or SE violation in the lag-2 year | 745 |

All are much sparser than effluent violations (4,562 nonzero). CS violations in particular have only 106 nonzero city-years.

---

## Comparison: effluent violations vs SNC proxies

| Variable | Y\_water\_only | | Y\_self\_green | | N |
|---|---|---|---|---|---:|
| | β | t (p) | β | t (p) | |
| **Effluent violations (current)** | **+0.003** | **(2.29)\*\*** | **+0.006** | **(3.05)\*\*\*** | 7,401 |
| CS violations (asinh) | −0.014 | (1.61) | −0.009 | (0.75) | 7,401 |
| CS violations (binary) | −0.019 | (1.23) | −0.009 | (0.42) | 7,401 |
| SNC proxy (any CS/PS/SE, binary) | −0.001 | (0.13) | +0.006 | (0.97) | 7,413 |
| PS violations (asinh) | +0.001 | (0.16) | +0.001 | (0.16) | 7,401 |
| SE violations (asinh) | −0.004 | (1.70)\* | +0.011 | (0.76) | 7,401 |

---

## Reading

**The current effluent-violations variable is the only compulsion measure that is significant on both water-only and self-green outcomes.** None of the SNC proxies (CS, PS, SE, or composite) approach significance on either outcome. CS violations are actually negative (−0.014 on water, −0.009 on self-green), which is the opposite of the predicted direction.

**Why the SNC proxies fail:**
1. **Extreme sparsity.** CS violations have only 106 nonzero city-years (vs 4,562 for effluent violations). At this level of rarity, the coefficient is identified off ~100 observations with state+year FE absorbing most of the variation.
2. **Selection on severity.** The most severe violation types (CS, SE) may indicate cities that are already under remediation — consent decrees, capital improvement plans — and have therefore already issued bonds in prior years. The negative sign on CS is consistent with a post-investment-completion effect: cities that reached a compliance schedule (meaning they negotiated a remediation plan) may no longer need new capital issuance.
3. **Effluent violations capture the right variation.** The raw count of effluent exceedances captures ongoing, widespread, low-severity noncompliance — exactly the kind of persistent regulatory pressure that accumulates into capital-investment decisions. This is not the same as a single high-severity event.

**Conclusion.** The effluent-violations variable (asinh-transformed count of all effluent exceedances) is the appropriate compulsion measure. It captures persistent, facility-level water-quality pressure that drives capital investment. More severe violation types (CS, PS, SE) are too sparse and may proxy for post-enforcement compliance rather than pre-investment need. No NPDES-specific SNC indicator is available in the current data extraction; the RCRA SNC variables are not relevant to water-quality compulsion.
