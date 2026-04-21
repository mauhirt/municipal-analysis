# Table 1 v3 — Partisan interactions (complement to main table)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 NPDES×Party | I2 NPDES×Party Self | I3 Demonstration |
|---|---|---|---|
| `Dem_Mayor` | -0.0033 (0.0045) | -0.0043 (0.0041) | -0.0234*** (0.0088) |
| `npdes_formal_prior3yr_muni` | -0.0397** (0.0202) | -0.0317* (0.0179) | -0.0129 (0.0129) |
| `pres_dem_two_party_share_lag2` | +0.0476* (0.0272) | +0.0493* (0.0257) | +0.0511** (0.0259) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0004) | +0.0001 (0.0004) | -0.0005 (0.0005) |
| `reserve_ratio_lag2` | +0.0043 (0.0034) | +0.0028 (0.0029) | +0.0026 (0.0030) |
| `debt_service_burden_lag2` | -0.0550 (0.0548) | -0.0335 (0.0486) | -0.0348 (0.0485) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0081 (0.0065) | -0.0080 (0.0053) | -0.0066 (0.0054) |
| `npdes_x_state_green` | +0.0019* (0.0010) | +0.0017* (0.0009) | +0.0015* (0.0009) |
| `dem_x_npdes` | +0.0283* (0.0146) | +0.0248* (0.0133) | — |
| `dem_x_state_green_cum` | — | — | +0.0011*** (0.0004) |
| N | 6698 | 6698 | 6698 |
| R² | 0.098 | 0.099 | 0.098 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
