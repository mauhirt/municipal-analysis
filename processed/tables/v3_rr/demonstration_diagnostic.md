# Demonstration Interaction Diagnostic

Tests four candidate state-prior-issuance measures interacted with mayoral
partisanship on `Y_self_green`. Full baseline controls, state + year FE,
city-clustered SEs.

**Spec A:** `Dem_Mayor × [measure]` only.
**Spec B:** `Dem_Mayor × [measure]` and `Rep_Mayor × [measure]` jointly.

## Comparison table

| Measure | Variable | States w/ variation | Dem-pos obs | Rep-pos obs | Spec | Party | β | SE | t | p | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | `asinh_state_all_green_cum_amt_lag1` | 47 | 3640 | 2764 | A | Dem | +0.0012** | 0.0005 | +2.48 | 0.0132 | 6577 |
| | | | | | B | Dem | +0.0007 | 0.0005 | +1.51 | 0.1298 | 6484 |
| | | | | | B | Rep | -0.0006 | 0.0006 | -1.02 | 0.3059 | |
| M2 | `state_any_prior_green_issuance_lag1` | 40 | 3257 | 2364 | A | Dem | +0.0194** | 0.0093 | +2.10 | 0.0360 | 6577 |
| | | | | | B | Dem | +0.0078 | 0.0072 | +1.10 | 0.2732 | 6484 |
| | | | | | B | Rep | -0.0149 | 0.0097 | -1.53 | 0.1264 | |
| M3 | `state_city_prior_green_issuance_lag1` | 26 | 1957 | 1225 | A | Dem | +0.0223** | 0.0088 | +2.52 | 0.0117 | 6577 |
| | | | | | B | Dem | +0.0077 | 0.0100 | +0.77 | 0.4440 | 6484 |
| | | | | | B | Rep | -0.0174* | 0.0103 | -1.68 | 0.0921 | |
| M4 | `state_city_count_prior_green_lag1` | 26 | 1957 | 1225 | A | Dem | +0.0042** | 0.0019 | +2.19 | 0.0285 | 6577 |
| | | | | | B | Dem | +0.0018 | 0.0012 | +1.54 | 0.1234 | 6484 |
| | | | | | B | Rep | -0.0025* | 0.0014 | -1.78 | 0.0757 | |

## Reading

### Which interactions reach p < 0.10?
- **Spec A M1:** Dem × `asinh_state_all_green_cum_amt_lag1` β = +0.0012, p = 0.0132 (**)
- **Spec A M2:** Dem × `state_any_prior_green_issuance_lag1` β = +0.0194, p = 0.0360 (**)
- **Spec A M3:** Dem × `state_city_prior_green_issuance_lag1` β = +0.0223, p = 0.0117 (**)
- **Spec A M4:** Dem × `state_city_count_prior_green_lag1` β = +0.0042, p = 0.0285 (**)
- **Spec B Rep M3:** β = -0.0174, p = 0.0921
- **Spec B Rep M4:** β = -0.0025, p = 0.0757

### Symmetry / asymmetry
- M1: Dem β = +0.0007, Rep β = -0.0006 → **asymmetric**
- M2: Dem β = +0.0078, Rep β = -0.0149 → **asymmetric**
- M3: Dem β = +0.0077, Rep β = -0.0174 → **asymmetric**
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
