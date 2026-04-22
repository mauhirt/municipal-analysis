# Table 1 v3 — Partisan interaction (constituency × party)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 Constituency×Party (GBI) | I2 Constituency×Party (Self) |
|---|---|---|
| `Dem_Mayor` | -0.0560* (0.0305) | -0.0646** (0.0298) |
| `npdes_formal_prior3yr_muni` | -0.0201 (0.0147) | -0.0144 (0.0133) |
| `pres_dem_two_party_share_lag2` | +0.0034 (0.0254) | -0.0027 (0.0228) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0004) | +0.0001 (0.0004) |
| `reserve_ratio_lag2` | +0.0044 (0.0033) | +0.0031 (0.0029) |
| `debt_service_burden_lag2` | -0.0656 (0.0536) | -0.0463 (0.0471) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0068 (0.0065) | -0.0069 (0.0053) |
| `npdes_x_state_green` | +0.0017* (0.0010) | +0.0015* (0.0009) |
| `dem_x_pres_dem` | +0.1005* (0.0532) | +0.1143** (0.0521) |
| N | 6825 | 6825 |
| R² | 0.095 | 0.097 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
