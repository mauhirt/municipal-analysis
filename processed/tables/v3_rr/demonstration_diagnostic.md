# Demonstration Interaction Diagnostic

Tests four candidate state-prior-issuance measures interacted with mayoral
partisanship on `Y_self_green`. Full baseline controls, state + year FE,
city-clustered SEs.

**Spec A:** `Dem_Mayor × [measure]` only.
**Spec B:** `Dem_Mayor × [measure]` and `Rep_Mayor × [measure]` jointly.

## Comparison table

| Measure | Variable | States w/ variation | Dem-pos obs | Rep-pos obs | Spec | Party | β | SE | t | p | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | `asinh_state_all_green_cum_amt_lag1` | 47 | 3588 | 2701 | A | Dem | +0.0015** | 0.0007 | +2.32 | 0.0203 | 5962 |
| | | | | | B | Dem | +0.0014 | 0.0010 | +1.37 | 0.1698 | 5948 |
| | | | | | B | Rep | -0.0002 | 0.0011 | -0.22 | 0.8272 | |
| M2 | `state_any_prior_green_issuance_lag1` | 40 | 3213 | 2306 | A | Dem | +0.0241** | 0.0120 | +2.00 | 0.0451 | 5962 |
| | | | | | B | Dem | +0.0147 | 0.0102 | +1.43 | 0.1523 | 5948 |
| | | | | | B | Rep | -0.0108 | 0.0120 | -0.90 | 0.3707 | |
| M3 | `state_city_prior_green_issuance_lag1` | 26 | 1923 | 1201 | A | Dem | +0.0241** | 0.0098 | +2.47 | 0.0134 | 5962 |
| | | | | | B | Dem | +0.0129 | 0.0122 | +1.05 | 0.2916 | 5948 |
| | | | | | B | Rep | -0.0127 | 0.0114 | -1.11 | 0.2668 | |
| M4 | `state_city_count_prior_green_lag1` | 26 | 1923 | 1201 | A | Dem | +0.0042** | 0.0019 | +2.23 | 0.0257 | 5962 |
| | | | | | B | Dem | +0.0023 | 0.0015 | +1.52 | 0.1288 | 5948 |
| | | | | | B | Rep | -0.0020 | 0.0012 | -1.64 | 0.1013 | |

## Reading

### Which interactions reach p < 0.10?
- **Spec A M1:** Dem × `asinh_state_all_green_cum_amt_lag1` β = +0.0015, p = 0.0203 (**)
- **Spec A M2:** Dem × `state_any_prior_green_issuance_lag1` β = +0.0241, p = 0.0451 (**)
- **Spec A M3:** Dem × `state_city_prior_green_issuance_lag1` β = +0.0241, p = 0.0134 (**)
- **Spec A M4:** Dem × `state_city_count_prior_green_lag1` β = +0.0042, p = 0.0257 (**)
- None reach p < 0.10 in Spec B.

### Symmetry / asymmetry
- M1: Dem β = +0.0014, Rep β = -0.0002 → **asymmetric**
- M2: Dem β = +0.0147, Rep β = -0.0108 → **asymmetric**
- M3: Dem β = +0.0129, Rep β = -0.0127 → **asymmetric**
- M4: Dem β = +0.0023, Rep β = -0.0020 → **asymmetric**

### Fragility flags (< 15 contributing states)
- All measures have ≥ 15 contributing states.

### Theoretically cleanest measure

Not auto-selected. Review the table above and decide based on:
1. Statistical significance (p < 0.10 in both Spec A and B)
2. Number of contributing states (fragility)
3. Symmetry vs asymmetry of Dem/Rep interactions
4. Theoretical interpretability of the measure

* p<0.10, ** p<0.05, *** p<0.01.
