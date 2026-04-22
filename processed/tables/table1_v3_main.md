# Table 1 v3 — Main 4 columns (2 outcomes × prob/amount)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | C1 GBI | C2 GBI amt | C3 Self-green | C4 Self amt |
|---|---|---|---|---|
| `Dem_Mayor` | +0.0005 (0.0044) | +0.0045 (0.0810) | -0.0004 (0.0039) | -0.0100 (0.0730) |
| `npdes_formal_prior3yr_muni` | +0.0145* (0.0078) | +0.2917* (0.1526) | +0.0164** (0.0070) | +0.3238** (0.1367) |
| `pres_dem_two_party_share_lag2` | +0.0535** (0.0269) | +0.9837* (0.5090) | +0.0545** (0.0254) | +0.9872** (0.4810) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0006 (0.0004) | +0.0102 (0.0074) | +0.0004 (0.0003) | +0.0065 (0.0065) |
| `reserve_ratio_lag2` | +0.0044 (0.0034) | +0.0753 (0.0627) | +0.0031 (0.0029) | +0.0551 (0.0554) |
| `debt_service_burden_lag2` | -0.0616 (0.0545) | -1.0602 (1.0320) | -0.0416 (0.0482) | -0.7348 (0.9160) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0076 (0.0064) | -0.1427 (0.1237) | -0.0078 (0.0053) | -0.1461 (0.1018) |
| N | 6825 | 6825 | 6825 | 6825 |
| R² | 0.092 | 0.098 | 0.094 | 0.097 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
