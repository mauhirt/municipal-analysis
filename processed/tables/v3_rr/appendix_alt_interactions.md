# Appendix — Alternative Interaction Specifications

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | Ax1 Dem×Stress | Ax2 Stress² | Ax3 M2 Binary | Ax4 M3 City Bin | Ax5 M4 City Cnt |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0013 (0.0040) | -0.0009 (0.0040) | -0.0173** (0.0081) | -0.0126** (0.0057) | -0.0009 (0.0040) |
| `pres_dem_two_party_share_lag2` | +0.0558** (0.0266) | +0.0527** (0.0265) | +0.0515* (0.0265) | +0.0533** (0.0265) | +0.0526** (0.0266) |
| `npdes_formal_prior3yr_muni` | +0.0175** (0.0071) | +0.0180** (0.0073) | +0.0179** (0.0072) | +0.0186** (0.0074) | +0.0180** (0.0073) |
| `reserve_ratio_lag2` | +0.0044 (0.0031) | +0.0031 (0.0030) | +0.0033 (0.0030) | +0.0031 (0.0030) | +0.0032 (0.0030) |
| `debt_service_burden_lag2` | -0.1469** (0.0596) | -0.0406 (0.0551) | -0.0353 (0.0500) | -0.0333 (0.0495) | -0.0340 (0.0499) |
| `state_dem_governor_lag1` | -0.0001 (0.0074) | +0.0001 (0.0074) | +0.0001 (0.0074) | -0.0001 (0.0075) | +0.0002 (0.0074) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0077 (0.0054) | -0.0067 (0.0053) | -0.0059 (0.0054) | -0.0064 (0.0054) | -0.0067 (0.0053) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0004 (0.0004) | +0.0004 (0.0004) | -0.0001 (0.0005) | +0.0004 (0.0004) | +0.0004 (0.0004) |
| `dem_x_fiscal_stress` | +0.0210** (0.0084) | — | — | — | — |
| `fiscal_stress_sq` | — | +0.0010 (0.0037) | — | — | — |
| `state_any_prior_green_issuance_lag1` | — | — | +0.0023 (0.0095) | — | — |
| `dem_x_state_any_prior_green_issuance_lag1` | — | — | +0.0202** (0.0094) | — | — |
| `state_city_prior_green_issuance_lag1` | — | — | — | -0.0183** (0.0077) | — |
| `dem_x_state_city_prior_green_issuance_lag1` | — | — | — | +0.0235** (0.0091) | — |
| `state_city_count_prior_green_lag1` | — | — | — | — | — |
| `dem_x_state_city_count_prior_green_lag1` | — | — | — | — | — |
| N | 6477 | 6477 | 6477 | 6477 | 6477 |
| R² | 0.102 | 0.100 | 0.101 | 0.101 | 0.100 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
