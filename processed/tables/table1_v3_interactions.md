# Table 1 v3 — Partisan interaction (constituency × party)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 Constituency×Party (GBI) | I2 Constituency×Party (Self) |
|---|---|---|
| `Dem_Mayor` | -0.0569* (0.0307) | -0.0654** (0.0301) |
| `npdes_formal_prior3yr_muni` | +0.0140* (0.0076) | +0.0159** (0.0067) |
| `pres_dem_two_party_share_lag2` | +0.0019 (0.0257) | -0.0040 (0.0231) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0005 (0.0004) | +0.0003 (0.0003) |
| `reserve_ratio_lag2` | +0.0045 (0.0033) | +0.0032 (0.0029) |
| `debt_service_burden_lag2` | -0.0667 (0.0537) | -0.0473 (0.0472) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0066 (0.0064) | -0.0068 (0.0053) |
| `dem_x_pres_dem` | +0.1019* (0.0536) | +0.1155** (0.0526) |
| N | 6825 | 6825 |
| R² | 0.094 | 0.096 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
