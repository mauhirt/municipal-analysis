# Table 1 v3 — Partisan interaction (constituency × party)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 Constituency×Party (GBI) | I2 Constituency×Party (Self) |
|---|---|---|
| `Dem_Mayor` | -0.0552* (0.0292) | -0.0633** (0.0284) |
| `qncr_nonsevere_asinh_lag1` | +0.0063** (0.0025) | +0.0054** (0.0021) |
| `pres_dem_two_party_share_lag2` | +0.0040 (0.0256) | -0.0066 (0.0220) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0004 (0.0003) | +0.0003 (0.0003) |
| `reserve_ratio_lag2` | +0.0042 (0.0031) | +0.0030 (0.0027) |
| `debt_service_burden_lag2` | -0.0757 (0.0527) | -0.0538 (0.0442) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0051 (0.0052) | -0.0023 (0.0043) |
| `dem_x_pres_dem` | +0.0986* (0.0515) | +0.1125** (0.0500) |
| N | 7413 | 7413 |
| R² | 0.089 | 0.091 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
