# Table 1 v3 — Partisan interactions (complement to main table)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 NPDES×Party | I2 NPDES×Party Self | I3 Demonstration |
|---|---|---|---|
| `Dem_Mayor` | -0.0030 (0.0046) | -0.0042 (0.0042) | -0.0238*** (0.0090) |
| `pres_dem_two_party_share_lag2` | +0.0488* (0.0280) | +0.0514* (0.0264) | +0.0531** (0.0266) |
| `npdes_formal_prior3yr_muni` | -0.0390* (0.0207) | -0.0315* (0.0183) | -0.0125 (0.0132) |
| `reserve_ratio_lag2` | +0.0047 (0.0035) | +0.0032 (0.0030) | +0.0031 (0.0030) |
| `debt_service_burden_lag2` | -0.0554 (0.0561) | -0.0341 (0.0497) | -0.0362 (0.0497) |
| `state_dem_governor_lag1` | +0.0017 (0.0077) | +0.0001 (0.0074) | -0.0004 (0.0075) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0070 (0.0065) | -0.0073 (0.0053) | -0.0060 (0.0053) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0005) | +0.0001 (0.0004) | -0.0005 (0.0005) |
| `npdes_x_state_green` | +0.0019* (0.0010) | +0.0017* (0.0009) | +0.0015* (0.0009) |
| `dem_x_npdes` | +0.0287* (0.0149) | +0.0251* (0.0136) | — |
| `dem_x_state_green_cum` | — | — | +0.0012*** (0.0004) |
| N | 6477 | 6477 | 6477 |
| R² | 0.100 | 0.102 | 0.101 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
