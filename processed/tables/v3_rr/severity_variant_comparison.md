# Severity-Variant Comparison

**Purpose.** Compare NPDES violation severity variants as substitutes for the current `effluent_muni_asinh_lag2` in the compulsion role. The predicted pattern: water-significant, non-water weaker or null (consistent with water-specific compulsion rather than general administrative capacity).

**Specification.** Each variant substituted into the 10-variable PRIMARY. State + year FE. City-clustered SE. N ≈ 7,401.

## Results

| Variant | nz | W β | W t | W p | NW β | NW t | NW p | Pool β | Pool t | Pool p | Pattern |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| **Baseline (current effluent)** | 4,562 | **+0.003** | **2.29** | **0.022\*\*** | +0.003 | 2.26 | 0.024\*\* | +0.006 | 3.05 | 0.002\*\*\* | W > NW ✓ |
| **QNCR all, lag2 asinh** | 4,562 | **+0.003** | **2.31** | **0.021\*\*** | +0.003 | 2.27 | 0.023\*\* | +0.006 | 3.07 | 0.002\*\*\* | W > NW ✓ |
| **QNCR all, prior 3yr asinh** | 5,179 | **+0.002** | **2.52** | **0.012\*\*** | +0.003 | 2.34 | 0.020\*\* | +0.005 | 3.17 | 0.002\*\*\* | W > NW ✓ |
| SNC, lag2 asinh | 239 | −0.006 | 1.37 | 0.170 | −0.006 | 1.73 | 0.084\* | −0.009 | 1.76 | 0.078\* | NW ≥ W |
| SNC, prior 3yr asinh | 422 | −0.005 | 1.94 | 0.052\* | −0.004 | 1.88 | 0.060\* | −0.007 | 2.05 | 0.040\*\* | W > NW ✓ (but negative) |
| Severe effluent, lag2 asinh | 2,036 | +0.003 | 1.25 | 0.210 | +0.003 | 1.00 | 0.319 | +0.006 | 1.45 | 0.146 | NW ≥ W |
| Severe effluent, prior 3yr asinh | 2,686 | +0.002 | 1.24 | 0.213 | +0.003 | 1.44 | 0.149 | +0.005 | 1.60 | 0.110 | NW ≥ W |
| Severe combined, lag2 asinh | 2,156 | +0.002 | 1.01 | 0.313 | +0.002 | 0.76 | 0.446 | +0.005 | 1.19 | 0.233 | NW ≥ W |
| Severe combined, prior 3yr asinh | 2,835 | +0.001 | 0.85 | 0.394 | +0.002 | 1.26 | 0.209 | +0.004 | 1.31 | 0.190 | NW ≥ W |
| Any effluent, lag2 asinh | 2,713 | +0.002 | 0.97 | 0.330 | +0.003 | 1.25 | 0.212 | +0.005 | 1.52 | 0.128 | NW ≥ W |

## Reading

**Three variants meet the W > NW criterion (water t > non-water t, water p < 0.10):**
1. Baseline (current effluent): W t = 2.29\*\*, NW t = 2.26\*\*
2. QNCR all lag2: W t = 2.31\*\*, NW t = 2.27\*\* (virtually identical to baseline)
3. QNCR all prior 3yr: W t = 2.52\*\*, NW t = 2.34\*\* (strongest water signal)

**No variant produces the "water significant, non-water null" pattern.** The top three variants are all significant on both water and non-water at p < 0.05. The differential is small (water t marginally higher than NW t). Severity-filtered variants (severe effluent, severe combined, SNC) are too sparse to reach significance on either outcome, or produce negative coefficients (SNC).

**The QNCR all-violations prior-3-year variant** produces the strongest water-specific signal (t = 2.52\*\* vs 2.34\*\* for non-water) with the widest t-gap (0.18). But the difference is not statistically distinguishable — a formal test of water vs non-water coefficient equality would not reject at any conventional level.

**SNC is counterproductive.** Both SNC variants produce negative coefficients, consistent with the earlier SNC diagnostic finding: significant noncompliance status may proxy for post-remediation completion rather than pre-investment need.

**Severity filtering weakens the signal.** Every severity-filtered variant (severe effluent, severe combined, any effluent) is weaker than the baseline on both water and non-water. The count of all violations — including low-severity effluent exceedances — captures the persistent regulatory pressure that drives capital investment. Filtering to only severe violations removes the high-frequency, low-severity signal that accumulates into capital-need decisions.

## Recommendation

**Keep the current variable** (`effluent_muni_asinh_lag2`) or swap to the nearly-identical `npdes_qncr_count_lag2_asinh` from the new QNCR extraction. The substantive finding — that compulsion operates on water and non-water at similar magnitudes — is robust to the severity specification. No variant produces the desired water-specific pattern that would sharpen the chain framing's Step 1 prediction. The institutional-capacity interpretation (cities under any form of regulatory pressure issue green bonds across multiple categories) holds regardless of severity weighting.
