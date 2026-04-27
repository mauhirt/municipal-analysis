# Appendix — Alternative Interaction Specifications

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | Ax1 Dem×Stress | Ax2 Stress² | Ax3 M2 Binary | Ax4 M3 City Bin | Ax5 M4 City Cnt |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0009 (0.0037) | -0.0001 (0.0036) | -0.0138** (0.0061) | -0.0092* (0.0047) | -0.0001 (0.0037) |
| `effluent_muni_asinh_lag2` | +0.0056*** (0.0019) | +0.0060*** (0.0020) | +0.0060*** (0.0020) | +0.0060*** (0.0019) | +0.0060*** (0.0020) |
| `pres_dem_two_party_share_lag2` | +0.0501** (0.0241) | +0.0515** (0.0234) | +0.0506** (0.0233) | +0.0517** (0.0234) | +0.0514** (0.0235) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0003) | +0.0004 (0.0003) | -0.0002 (0.0004) | +0.0004 (0.0003) | +0.0004 (0.0003) |
| `reserve_ratio_lag2` | +0.0038 (0.0028) | +0.0030 (0.0028) | +0.0030 (0.0027) | +0.0029 (0.0028) | +0.0030 (0.0028) |
| `debt_service_burden_lag2` | -0.1397*** (0.0534) | -0.0477 (0.0484) | -0.0478 (0.0444) | -0.0465 (0.0441) | -0.0471 (0.0444) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0031 (0.0043) | -0.0029 (0.0042) | -0.0031 (0.0042) | -0.0023 (0.0043) | -0.0029 (0.0042) |
| `dem_x_fiscal_stress` | +0.0195** (0.0079) | — | — | — | — |
| `fiscal_stress_sq` | — | +0.0001 (0.0035) | — | — | — |
| `state_any_prior_green_issuance_lag1` | — | — | +0.0032 (0.0074) | — | — |
| `dem_x_state_any_prior_green_issuance_lag1` | — | — | +0.0185** (0.0074) | — | — |
| `state_city_prior_green_issuance_lag1` | — | — | — | -0.0119** (0.0060) | — |
| `dem_x_state_city_prior_green_issuance_lag1` | — | — | — | +0.0203** (0.0083) | — |
| `state_city_count_prior_green_lag1` | — | — | — | — | — |
| `dem_x_state_city_count_prior_green_lag1` | — | — | — | — | — |
| N | 7254 | 7401 | 7401 | 7401 | 7401 |
| R² | 0.094 | 0.089 | 0.090 | 0.090 | 0.089 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
