# Diagnostic 1 — Why is NPDES non-significant on water-only?

## Question

In Table 1 (Step 1), `npdes_formal_prior3yr_muni` on `Y_water_only` is +0.0075 (t = 1.53, ns). In Table 2 (Step 2), the same NPDES coefficient on `Y_self_green` is +0.016\*\* (t = 2.36). NPDES should be the strongest driver of water-specific issuance.

---

## 1a — Outcome variable construction

`Y_water_only` = 1 if the city-year has at least one bond classified under Sustainable Water ESG project categories **AND** no other non-water ESG categories. This is a **strict** definition: mixed-purpose bonds (water + non-water proceeds) are excluded.

| Outcome | Positive city-years | Definition |
|---|---:|---|
| `Y_water_only` (strict) | 90 | Water category only, no non-water |
| `Y_water_inclusive` | 105 | Any bond with water proceeds (including mixed) |
| `Y_self_green` | 118 | Any self-labelled green bond |
| `Y_has_non_water` | 60 | Any non-water ESG category |
| `Green_Bond_Issued` | 152 | Any green bond (including third-party classified) |

15 city-years are mixed-purpose (water + non-water) and are excluded from `Y_water_only` but included in `Y_water_inclusive`.

| Overlap with NPDES > 0 | Count |
|---|---:|
| NPDES > 0 & Y_water_only = 1 | 28 |
| NPDES > 0 & Y_water_inclusive = 1 | 33 |
| NPDES > 0 & Y_self_green = 1 | 47 |

---

## 1b — NPDES on alternative water outcomes

| Outcome | N | n+ | NPDES β | SE | t | p |
|---|---:|---:|---|---|---|---|
| Water-only (strict) | 6,825 | 89 | +0.0075 | 0.0049 | 1.53 | 0.127 |
| Water-inclusive | 6,825 | 104 | +0.0084 | 0.0056 | 1.50 | 0.135 |
| **Self-green (all)** | 6,825 | 117 | **+0.0164** | 0.0070 | **2.36** | **0.018\*\*** |
| Non-water | 6,825 | 57 | +0.0064 | 0.0047 | 1.34 | 0.179 |
| Bloomberg Water/Sewer industry | 6,825 | 83 | +0.0096 | 0.0055 | 1.75 | 0.080\* |

Broadening from `Y_water_only` to `Y_water_inclusive` does **not** recover NPDES significance. The coefficient moves from +0.0075 to +0.0084 — marginal improvement, still ns (t = 1.50). The strict outcome definition is not the issue.

Bloomberg's industry-level Water/Sewer tag produces a borderline result (+0.0096\*, t = 1.75). This is closer to significance but remains weaker than the pooled self-green effect.

---

## 1c — Power analysis

| Parameter | Value |
|---|---|
| SE on water-only outcome | 0.0049 |
| MDE at 80% power (two-sided, α = 0.05) | 0.0137 |
| Table 2 effect size (NPDES on Y_self_green) | 0.0164 |
| Ratio (effect / MDE) | 1.20 |

The Table 2 effect size (0.0164) exceeds the MDE (0.0137). **The water-only specification is NOT underpowered** to detect an effect of the Table 2 magnitude if it existed on water specifically. The non-significance reflects a genuinely smaller effect on water-only (+0.0075) than on the pooled self-green outcome (+0.0164).

---

## 1d — Alternative water specifications

No separate SSO/overflow-remediation or sewer-specific outcome variable exists in the panel. The available alternative is Bloomberg's industry-level Water/Sewer classification:

| Outcome | N | n+ | NPDES β | t | p |
|---|---:|---:|---|---|---|
| Y_water_only (ESG category) | 6,825 | 89 | +0.0075 | 1.53 | 0.127 |
| Y_water_inclusive (ESG) | 6,825 | 104 | +0.0084 | 1.50 | 0.135 |
| Bloomberg Water/Sewer | 6,825 | 83 | +0.0096 | 1.75 | 0.080\* |

---

## Reading

The original observation is **confirmed**: NPDES is not significant on water-specific outcomes in any specification tested (strict, inclusive, or Bloomberg Water/Sewer), while it is significant on the broader self-green outcome (+0.016\*\*). The power analysis rules out sample-size insufficiency.

**Likely explanation.** NPDES enforcement predicts green bond issuance **broadly**, not specifically through a water-compulsion channel. The coefficient on self-green (+0.016\*\*) is approximately twice the coefficient on water-only (+0.008). This means roughly half the NPDES effect operates on non-water categories (+0.006, directionally positive but ns individually). NPDES may function as a marker of general environmental regulatory engagement or administrative capacity rather than as a narrow water-compulsion mechanism. Cities under NPDES scrutiny issue green bonds for water AND non-water purposes, suggesting the enforcement event triggers a broader institutional shift toward environmental finance rather than a project-specific compulsion pathway.

This is a substantive finding, not a measurement artifact. The paper's compulsion framing should acknowledge that NPDES enforcement operates as a general environmental-finance trigger rather than a narrow water-specific compulsion.
