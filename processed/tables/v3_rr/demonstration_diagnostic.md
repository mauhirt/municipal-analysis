# Demonstration Interaction Diagnostic

Tests four candidate state-prior-issuance measures interacted with mayoral
partisanship on `Y_self_green`. Full baseline controls, state + year FE,
city-clustered SEs.

**Spec A:** `Dem_Mayor × [measure]` only.
**Spec B:** `Dem_Mayor × [measure]` and `Rep_Mayor × [measure]` jointly.

## Comparison table

| Measure | Variable | States w/ variation | Dem-pos obs | Rep-pos obs | Spec | Party | β | SE | t | p | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | `asinh_state_all_green_cum_amt_lag1` | 47 | 3640 | 2764 | A | Dem | +0.0012** | 0.0005 | +2.56 | 0.0105 | 6567 |
| | | | | | B | Dem | +0.0008 | 0.0005 | +1.63 | 0.1024 | 6474 |
| | | | | | B | Rep | -0.0006 | 0.0006 | -0.94 | 0.3470 | |
| M2 | `state_any_prior_green_issuance_lag1` | 40 | 3257 | 2364 | A | Dem | +0.0190** | 0.0092 | +2.07 | 0.0386 | 6567 |
| | | | | | B | Dem | +0.0075 | 0.0073 | +1.03 | 0.3028 | 6474 |
| | | | | | B | Rep | -0.0146 | 0.0100 | -1.46 | 0.1436 | |
| M3 | `state_city_prior_green_issuance_lag1` | 26 | 1957 | 1225 | A | Dem | +0.0228** | 0.0090 | +2.52 | 0.0117 | 6567 |
| | | | | | B | Dem | +0.0091 | 0.0104 | +0.88 | 0.3813 | 6474 |
| | | | | | B | Rep | -0.0163 | 0.0106 | -1.55 | 0.1221 | |
| M4 | `state_city_count_prior_green_lag1` | 26 | 1957 | 1225 | A | Dem | +0.0042** | 0.0019 | +2.20 | 0.0280 | 6567 |
| | | | | | B | Dem | +0.0018 | 0.0012 | +1.52 | 0.1284 | 6474 |
| | | | | | B | Rep | -0.0025* | 0.0014 | -1.80 | 0.0726 | |

## Reading

### Which interactions reach p < 0.10?
- **Spec A M1:** Dem × `asinh_state_all_green_cum_amt_lag1` β = +0.0012, p = 0.0105 (**)
- **Spec A M2:** Dem × `state_any_prior_green_issuance_lag1` β = +0.0190, p = 0.0386 (**)
- **Spec A M3:** Dem × `state_city_prior_green_issuance_lag1` β = +0.0228, p = 0.0117 (**)
- **Spec A M4:** Dem × `state_city_count_prior_green_lag1` β = +0.0042, p = 0.0280 (**)
- **Spec B Rep M4:** β = -0.0025, p = 0.0726

### Symmetry / asymmetry
- M1: Dem β = +0.0008, Rep β = -0.0006 → **asymmetric**
- M2: Dem β = +0.0075, Rep β = -0.0146 → **asymmetric**
- M3: Dem β = +0.0091, Rep β = -0.0163 → **asymmetric**
- M4: Dem β = +0.0018, Rep β = -0.0025 → **asymmetric**

### Fragility flags (< 15 contributing states)
- All measures have ≥ 15 contributing states.

### Theoretically cleanest measure

Not auto-selected. Review the table above and decide based on:
1. Statistical significance (p < 0.10 in both Spec A and B)
2. Number of contributing states (fragility)
3. Symmetry vs asymmetry of Dem/Rep interactions
4. Theoretical interpretability of the measure

* p<0.10, ** p<0.05, *** p<0.01.
