# Table 1 v3 — Partisan interaction (constituency × party)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 Constituency×Party (GBI) | I2 Constituency×Party (Self) |
|---|---|---|
| `Dem_Mayor` | -0.0559* (0.0295) | -0.0642** (0.0287) |
| `effluent_muni_asinh_lag2` | +0.0062*** (0.0024) | +0.0061*** (0.0020) |
| `pres_dem_two_party_share_lag2` | +0.0044 (0.0255) | -0.0061 (0.0219) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0004 (0.0003) | +0.0003 (0.0003) |
| `reserve_ratio_lag2` | +0.0043 (0.0031) | +0.0031 (0.0027) |
| `debt_service_burden_lag2` | -0.0736 (0.0519) | -0.0526 (0.0436) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0048 (0.0053) | -0.0020 (0.0043) |
| `dem_x_pres_dem` | +0.0995* (0.0519) | +0.1139** (0.0505) |
| N | 7401 | 7401 |
| R² | 0.089 | 0.092 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
