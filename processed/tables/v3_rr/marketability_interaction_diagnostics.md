# Task 10 — Marketability Interaction Diagnostics

**Spec under test:** C6 — `Y_self_green` ~ PRIMARY + `npdes_x_state_green`. Baseline coefficient: **+0.00160\*** (SE 0.00090, p=0.0744).

---

## 10a — VIF (raw vs centered)

| Variable | β (raw) | SE | p | Raw VIF | β (centered) | SE | p | Centered VIF |
|---|---|---|---|---|---|---|---|---|
| `npdes_formal_prior3yr_muni` | -0.0153 | 0.0133 | 0.252 | **13.30 ⚠** | +0.0138** | 0.0059 | 0.020 | 1.25 |
| `asinh_state_all_green_cum_amt_lag1` | +0.0001 | 0.0004 | 0.792 | 3.21 | +0.0004 | 0.0003 | 0.288 | 3.00 |
| `npdes × state_green_cum` | **+0.0016\*** | 0.0009 | 0.074 | **13.25 ⚠** | **+0.0016\*** | 0.0009 | 0.074 | **1.13** |

Centering produces identical interaction coefficient with VIF 1.13. **Raw VIF flag is the standard mechanical-correlation pattern, not a substantive collinearity issue.** Same diagnostic verdict as the I2 constituency interaction.

---

## 10b — Leave-one-state-out (top-10 NPDES-positive contributors)

Top-10 states by count of NPDES-positive city-years:

| state_id | NPDES-pos city-years |
|---|---|
| 43 | 177 |
| 4 (California) | 160 |
| 9 | 97 |
| 14 | 68 |
| 34 | 62 |
| 31 | 61 |
| 36 | 43 |
| 10 | 41 |
| 19 | 39 |
| 38 | 36 |

**Baseline:** β = +0.00160\* (p = 0.0744).

| Dropped state | β | SE | p | N |
|---|---|---|---|---|
| 43 | +0.00194\*\* | 0.00098 | 0.048 | 6,245 |
| **4 (CA)** | **+0.00074** | **0.00062** | **0.232 ⚠** | 5,786 |
| **9** | **+0.00156** | **0.00098** | **0.109 ⚠** | 6,334 |
| 14 | +0.00161\* | 0.00091 | 0.078 | 6,490 |
| 34 | +0.00179\* | 0.00096 | 0.061 | 6,671 |
| 31 | +0.00174\* | 0.00098 | 0.075 | 6,670 |
| 36 | +0.00172\* | 0.00094 | 0.067 | 6,741 |
| **10** | **+0.00142** | **0.00089** | **0.113 ⚠** | 6,705 |
| 19 | +0.00171\* | 0.00091 | 0.061 | 6,597 |
| 38 | +0.00154\* | 0.00091 | 0.089 | 6,717 |

**Three single-state exclusions drop p above 0.10:** California (state_id=4) is the most damaging — coefficient falls 53% (from +0.00160 to +0.00074) and p moves from 0.074 to 0.232. State_id=9 and state_id=10 also push p above 0.10.

The marketability interaction is **fragile to California exclusion.** The other 7 single-state drops preserve significance.

---

## 10c — Water vs non-water domain check

| Outcome | N | n+ | NPDES main | npdes × state_green |
|---|---|---|---|---|
| Water-only (Y_water_only) | 6,825 | 89 | -0.0071 (0.0087, p=0.41) | **+0.0007 (0.0006, p=0.19)** |
| Non-water (Y_has_non_water) | 6,825 | 57 | -0.0117 (0.0088, p=0.18) | **+0.0009 (0.0006, p=0.12)** |
| Self-green (pooled) | 6,825 | 117 | -0.0153 (0.0133, p=0.25) | **+0.0016\* (0.0009, p=0.07)** |

**The marketability interaction is not significant in either water or non-water subsample alone.** Coefficients are directionally consistent (both ≈ +0.0008) but only the pooled spec reaches conventional significance.

---

## Verdict

**Three fragility flags raised:**

1. **VIF (10a):** Raw VIF flag dismissed by centering (canonical interaction-term pattern; same as I2). ✓ pass.
2. **LOSO (10b):** California exclusion drops p from 0.074 to 0.232; coefficient halves. State_id=9 and state_id=10 also push p above 0.10. **Three of ten LOSO tests fail.** ⚠ flag.
3. **Domain check (10c):** Significance exists only in the pooled spec. Water alone p=0.19, non-water alone p=0.12. **The interaction does not survive in either subdomain.** ⚠ flag.

The marketability interaction is materially weaker than I2:
- I2 (constituency × party) on non-water: +0.101\*\*\* (p=0.002), strengthens in the discretionary subsample
- Marketability (npdes × state_green) on non-water: +0.0009 (p=0.12), weakens in the subsample

**Recommendation per instructions:** stop and request user decision before proceeding to Tasks 12–15. The two-interaction framing is defensible only if the marketability interaction is treated as a marginal/qualified finding rather than as a co-equal mechanism. If the paper foregrounds it as the "second mechanism" alongside I2, the LOSO and domain results need to be acknowledged.

---

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01. SEs clustered at city (fips7). State + year FE.
