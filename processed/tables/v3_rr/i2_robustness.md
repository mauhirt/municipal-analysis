# I2 Robustness — Constituency × Partisan Interaction

**Spec:** `Y_self_green` ~ PRIMARY + `Dem_Mayor × pres_dem_two_party_share_lag2`. State + year FE, city-clustered SE. N = 6,825.

**Baseline:** `dem_x_pres_dem` = +0.1155\*\* (SE 0.0526, p = 0.028).

---

## 11a — Discordant observation count

| Category | Count |
|---|---|
| (i) Dem_Mayor = 1 & pres_dem < 0.45 (Dem mayor in red city) | 324 |
| (ii) Dem_Mayor = 0 & pres_dem > 0.55 (Rep mayor in blue city) | 1,026 |
| (iii) **Combined discordant** | **1,350 ✓ ≥ 200** |

### (iv) Distribution by state

Top contributors to Dem-in-red:

| State | Count |
|---|---|
| IN | 38 |
| TN | 32 |
| TX | 21 |
| FL | 19 |
| UT | 18 |
| PA | 16 |
| AZ | 15 |

Top contributors to Rep-in-blue:

| State | Count |
|---|---|
| CA | 279 |
| IL | 141 |
| TX | 106 |
| FL | 70 |
| MN | 60 |
| GA | 44 |
| MA | 38 |

Discordant observations span 30+ states. No single state dominates the identification source. California provides the most Rep-in-blue observations (279, 27% of the Rep-in-blue total) but the interaction survives California exclusion at p < 0.10 (see 11b).

---

## 11b — Leave-one-state-out sensitivity

Baseline: +0.1155\*\* (p = 0.028).

| Dropped state | β | SE | p | Flag |
|---|---|---|---|---|
| 4 (CA) | +0.0632 | 0.0359 | 0.078\* | ⚠ p > 0.05 |
| 47 | +0.0991 | 0.0529 | 0.061\* | ⚠ p > 0.05 |
| 38 | +0.1050 | 0.0541 | 0.052\* | ⚠ p > 0.05 |
| 43 | +0.1060 | 0.0532 | 0.046\*\* | |
| 10 | +0.1079 | 0.0526 | 0.040\*\* | |
| 19 | +0.1133 | 0.0543 | 0.037\*\* | |
| 3 | +0.1111 | 0.0523 | 0.034\*\* | |
| 32 | +0.1126 | 0.0527 | 0.033\*\* | |
| ... | ... | ... | ... | |
| 15 (best) | +0.1239 | 0.0539 | 0.022\*\* | |

**Summary across all 49 states:**

| Metric | Value |
|---|---|
| Coefficient range | [+0.063, +0.130] |
| p-value range | [0.022, 0.078] |
| **States where p > 0.05** | **3 / 49** |
| **States where p > 0.10** | **0 / 49** |

**California is the most influential single state.** Dropping it reduces the coefficient by 45% (from +0.116 to +0.063) and pushes p from 0.028 to 0.078. The coefficient remains positive and significant at the 10% level. The other two states exceeding p > 0.05 (state_id 47 and 38) produce smaller perturbations (p = 0.061 and 0.052 respectively). **No single-state exclusion pushes p above 0.10.**

Relative to the marketability interaction (Task 10): the marketability interaction had 3 of 10 LOSO tests dropping below p = 0.10, with California pushing p to 0.232. The I2 interaction has 0 of 49 dropping below p = 0.10. I2 is materially more robust.

---

## Verdict

| Diagnostic | Result | Threshold | Status |
|---|---|---|---|
| Combined discordant count | 1,350 | ≥ 200 | **✓ pass** |
| VIF (from prior diagnostic) | 1.18 centered | < 10 | **✓ pass** |
| LOSO: states above p = 0.10 | 0 / 49 | flag if any | **✓ pass** |
| LOSO: states above p = 0.05 | 3 / 49 | flag if any | **⚠ flagged** |

Three states push p above 0.05 (CA at 0.078, state 47 at 0.061, state 38 at 0.052). All three remain significant at p < 0.10. **The finding is robust to any single-state exclusion at the 10% level but not at the 5% level for three states.** The paper should acknowledge California sensitivity in the methods section.

---

\*, \*\*, \*\*\* denote significance at the 10 per cent, 5 per cent and 1 per cent level, respectively.
