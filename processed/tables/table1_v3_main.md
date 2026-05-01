# Table 1 v3 — Main 4 columns (2 outcomes × prob/amount)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | C1 GBI | C2 GBI amt | C3 Self-green | C4 Self amt |
|---|---|---|---|---|
| `Dem_Mayor` | +0.0004 (0.0041) | +0.0045 (0.0758) | +0.0001 (0.0037) | +0.0014 (0.0680) |
| `qncr_nonsevere_asinh_lag1` | +0.0062** (0.0025) | +0.1143** (0.0479) | +0.0052** (0.0021) | +0.0957** (0.0412) |
| `pres_dem_two_party_share_lag2` | +0.0538** (0.0249) | +0.9782** (0.4702) | +0.0502** (0.0232) | +0.9081** (0.4400) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0005 (0.0003) | +0.0083 (0.0064) | +0.0003 (0.0003) | +0.0064 (0.0055) |
| `reserve_ratio_lag2` | +0.0041 (0.0032) | +0.0702 (0.0590) | +0.0029 (0.0028) | +0.0509 (0.0527) |
| `debt_service_burden_lag2` | -0.0707 (0.0532) | -1.2526 (1.0083) | -0.0481 (0.0450) | -0.8710 (0.8571) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0059 (0.0052) | -0.1007 (0.0972) | -0.0032 (0.0042) | -0.0568 (0.0785) |
| N | 7413 | 7413 | 7413 | 7413 |
| R² | 0.088 | 0.093 | 0.088 | 0.091 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
