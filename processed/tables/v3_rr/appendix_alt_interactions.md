# Appendix — Alternative Interaction Specifications

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | Ax1 Dem×Stress | Ax2 Stress² | Ax3 M2 Binary | Ax4 M3 City Bin | Ax5 M4 City Cnt |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0014 (0.0040) | -0.0004 (0.0039) | -0.0159** (0.0077) | -0.0108** (0.0054) | -0.0004 (0.0039) |
| `npdes_formal_prior3yr_muni` | +0.0167** (0.0070) | +0.0164** (0.0069) | +0.0163** (0.0069) | +0.0169** (0.0070) | +0.0164** (0.0070) |
| `pres_dem_two_party_share_lag2` | +0.0529** (0.0259) | +0.0546** (0.0253) | +0.0535** (0.0253) | +0.0550** (0.0253) | +0.0545** (0.0254) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0003) | +0.0004 (0.0003) | -0.0002 (0.0004) | +0.0004 (0.0003) | +0.0004 (0.0003) |
| `reserve_ratio_lag2` | +0.0039 (0.0030) | +0.0031 (0.0029) | +0.0033 (0.0029) | +0.0030 (0.0029) | +0.0031 (0.0029) |
| `debt_service_burden_lag2` | -0.1450** (0.0579) | -0.0455 (0.0535) | -0.0431 (0.0482) | -0.0408 (0.0479) | -0.0416 (0.0482) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0085 (0.0055) | -0.0079 (0.0053) | -0.0069 (0.0054) | -0.0076 (0.0055) | -0.0078 (0.0053) |
| `dem_x_fiscal_stress` | +0.0212** (0.0083) | — | — | — | — |
| `fiscal_stress_sq` | — | +0.0006 (0.0036) | — | — | — |
| `state_any_prior_green_issuance_lag1` | — | — | +0.0033 (0.0087) | — | — |
| `dem_x_state_any_prior_green_issuance_lag1` | — | — | +0.0192** (0.0089) | — | — |
| `state_city_prior_green_issuance_lag1` | — | — | — | -0.0161** (0.0072) | — |
| `dem_x_state_city_prior_green_issuance_lag1` | — | — | — | +0.0212** (0.0087) | — |
| `state_city_count_prior_green_lag1` | — | — | — | — | — |
| `dem_x_state_city_count_prior_green_lag1` | — | — | — | — | — |
| N | 6698 | 6825 | 6825 | 6825 | 6825 |
| R² | 0.099 | 0.094 | 0.095 | 0.095 | 0.094 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
