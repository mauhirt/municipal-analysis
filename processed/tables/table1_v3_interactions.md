# Table 1 v3 — Partisan interactions (complement to main table)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 NPDES×Party | I2 NPDES×Party Self | I3 Demonstration |
|---|---|---|---|
| `Dem_Mayor` | -0.0032 (0.0046) | -0.0036 (0.0041) | -0.0222*** (0.0084) |
| `npdes_formal_prior3yr_muni` | -0.0385* (0.0201) | -0.0305* (0.0178) | -0.0123 (0.0128) |
| `pres_dem_two_party_share_lag2` | +0.0525** (0.0268) | +0.0537** (0.0253) | +0.0550** (0.0254) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0004) | +0.0001 (0.0004) | -0.0005 (0.0005) |
| `reserve_ratio_lag2` | +0.0044 (0.0034) | +0.0031 (0.0029) | +0.0030 (0.0030) |
| `debt_service_burden_lag2` | -0.0616 (0.0542) | -0.0415 (0.0480) | -0.0433 (0.0480) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0083 (0.0064) | -0.0085 (0.0053) | -0.0070 (0.0053) |
| `npdes_x_state_green` | +0.0018* (0.0010) | +0.0016* (0.0009) | +0.0014* (0.0009) |
| `dem_x_npdes` | +0.0282* (0.0146) | +0.0243* (0.0133) | — |
| `dem_x_state_green_cum` | — | — | +0.0011*** (0.0004) |
| N | 6825 | 6825 | 6825 |
| R² | 0.094 | 0.095 | 0.095 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
