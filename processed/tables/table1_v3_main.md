# Table 1 v3 — Main 4 columns (2 outcomes × prob/amount)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | C1 GBI | C2 GBI amt | C3 Self-green | C4 Self amt |
|---|---|---|---|---|
| `Dem_Mayor` | +0.0002 (0.0041) | +0.0009 (0.0758) | -0.0001 (0.0037) | -0.0029 (0.0679) |
| `effluent_muni_asinh_lag2` | +0.0061*** (0.0023) | +0.1165*** (0.0450) | +0.0060*** (0.0020) | +0.1140*** (0.0380) |
| `pres_dem_two_party_share_lag2` | +0.0547** (0.0251) | +0.9975** (0.4751) | +0.0514** (0.0235) | +0.9326** (0.4450) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0005 (0.0003) | +0.0088 (0.0064) | +0.0004 (0.0003) | +0.0069 (0.0055) |
| `reserve_ratio_lag2` | +0.0042 (0.0032) | +0.0716 (0.0585) | +0.0030 (0.0028) | +0.0531 (0.0520) |
| `debt_service_burden_lag2` | -0.0687 (0.0524) | -1.2175 (0.9925) | -0.0471 (0.0444) | -0.8546 (0.8430) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0056 (0.0052) | -0.0957 (0.0973) | -0.0029 (0.0042) | -0.0514 (0.0787) |
| N | 7401 | 7401 | 7401 | 7401 |
| R² | 0.088 | 0.093 | 0.089 | 0.092 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
