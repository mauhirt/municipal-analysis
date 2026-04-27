# Demonstration Interaction Diagnostic

Tests four candidate state-prior-issuance measures interacted with mayoral
partisanship on `Y_self_green`. Full baseline controls, state + year FE,
city-clustered SEs.

**Spec A:** `Dem_Mayor × [measure]` only.
**Spec B:** `Dem_Mayor × [measure]` and `Rep_Mayor × [measure]` jointly.

## Comparison table

| Measure | Variable | States w/ variation | Dem-pos obs | Rep-pos obs | Spec | Party | β | SE | t | p | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | `asinh_state_all_green_cum_amt_lag1` | 47 | 3640 | 2764 | A | Dem | +0.0012** | 0.0005 | +2.52 | 0.0116 | 6567 |
| | | | | | B | Dem | +0.0007 | 0.0005 | +1.54 | 0.1239 | 6474 |
| | | | | | B | Rep | -0.0006 | 0.0006 | -0.99 | 0.3210 | |
| M2 | `state_any_prior_green_issuance_lag1` | 40 | 3257 | 2364 | A | Dem | +0.0196** | 0.0093 | +2.11 | 0.0352 | 6567 |
| | | | | | B | Dem | +0.0082 | 0.0073 | +1.12 | 0.2621 | 6474 |
| | | | | | B | Rep | -0.0147 | 0.0100 | -1.48 | 0.1390 | |
| M3 | `state_city_prior_green_issuance_lag1` | 26 | 1957 | 1225 | A | Dem | +0.0222** | 0.0089 | +2.51 | 0.0122 | 6567 |
| | | | | | B | Dem | +0.0073 | 0.0101 | +0.72 | 0.4721 | 6474 |
| | | | | | B | Rep | -0.0178* | 0.0106 | -1.68 | 0.0926 | |
| M4 | `state_city_count_prior_green_lag1` | 26 | 1957 | 1225 | A | Dem | +0.0041** | 0.0019 | +2.20 | 0.0279 | 6567 |
| | | | | | B | Dem | +0.0018 | 0.0012 | +1.52 | 0.1295 | 6474 |
| | | | | | B | Rep | -0.0025* | 0.0014 | -1.79 | 0.0740 | |

## Reading

### Which interactions reach p < 0.10?
- **Spec A M1:** Dem × `asinh_state_all_green_cum_amt_lag1` β = +0.0012, p = 0.0116 (**)
- **Spec A M2:** Dem × `state_any_prior_green_issuance_lag1` β = +0.0196, p = 0.0352 (**)
- **Spec A M3:** Dem × `state_city_prior_green_issuance_lag1` β = +0.0222, p = 0.0122 (**)
- **Spec A M4:** Dem × `state_city_count_prior_green_lag1` β = +0.0041, p = 0.0279 (**)
- **Spec B Rep M3:** β = -0.0178, p = 0.0926
- **Spec B Rep M4:** β = -0.0025, p = 0.0740

### Symmetry / asymmetry
- M1: Dem β = +0.0007, Rep β = -0.0006 → **asymmetric**
- M2: Dem β = +0.0082, Rep β = -0.0147 → **asymmetric**
- M3: Dem β = +0.0073, Rep β = -0.0178 → **asymmetric**
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
