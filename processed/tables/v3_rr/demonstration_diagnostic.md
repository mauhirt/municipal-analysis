# Demonstration Interaction Diagnostic

Tests four candidate state-prior-issuance measures interacted with mayoral
partisanship on `Y_self_green`. Full baseline controls, state + year FE,
city-clustered SEs.

**Spec A:** `Dem_Mayor × [measure]` only.
**Spec B:** `Dem_Mayor × [measure]` and `Rep_Mayor × [measure]` jointly.

## Comparison table

| Measure | Variable | States w/ variation | Dem-pos obs | Rep-pos obs | Spec | Party | β | SE | t | p | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | `asinh_state_all_green_cum_amt_lag1` | 47 | 3588 | 2701 | A | Dem | +0.0015** | 0.0007 | +2.34 | 0.0193 | 5962 |
| | | | | | B | Dem | +0.0016** | 0.0008 | +2.02 | 0.0430 | 5948 |
| | | | | | B | Rep | +0.0001 | 0.0009 | +0.06 | 0.9532 | |
| M2 | `state_any_prior_green_issuance_lag1` | 40 | 3213 | 2306 | A | Dem | +0.0244** | 0.0120 | +2.04 | 0.0417 | 5962 |
| | | | | | B | Dem | +0.0193* | 0.0103 | +1.87 | 0.0618 | 5948 |
| | | | | | B | Rep | -0.0062 | 0.0121 | -0.51 | 0.6085 | |
| M3 | `state_city_prior_green_issuance_lag1` | 26 | 1923 | 1201 | A | Dem | +0.0246** | 0.0097 | +2.54 | 0.0110 | 5962 |
| | | | | | B | Dem | +0.0152 | 0.0117 | +1.30 | 0.1939 | 5948 |
| | | | | | B | Rep | -0.0107 | 0.0111 | -0.96 | 0.3366 | |
| M4 | `state_city_count_prior_green_lag1` | 26 | 1923 | 1201 | A | Dem | +0.0042** | 0.0019 | +2.21 | 0.0268 | 5962 |
| | | | | | B | Dem | +0.0023 | 0.0015 | +1.54 | 0.1241 | 5948 |
| | | | | | B | Rep | -0.0020* | 0.0012 | -1.66 | 0.0961 | |

## Reading

### Which interactions reach p < 0.10?
- **Spec A M1:** Dem × `asinh_state_all_green_cum_amt_lag1` β = +0.0015, p = 0.0193 (**)
- **Spec A M2:** Dem × `state_any_prior_green_issuance_lag1` β = +0.0244, p = 0.0417 (**)
- **Spec A M3:** Dem × `state_city_prior_green_issuance_lag1` β = +0.0246, p = 0.0110 (**)
- **Spec A M4:** Dem × `state_city_count_prior_green_lag1` β = +0.0042, p = 0.0268 (**)
- **Spec B Dem M1:** β = +0.0016, p = 0.0430
- **Spec B Dem M2:** β = +0.0193, p = 0.0618
- **Spec B Rep M4:** β = -0.0020, p = 0.0961

### Symmetry / asymmetry
- M1: Dem β = +0.0016, Rep β = +0.0001 → **asymmetric**
- M2: Dem β = +0.0193, Rep β = -0.0062 → **asymmetric**
- M3: Dem β = +0.0152, Rep β = -0.0107 → **asymmetric**
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
