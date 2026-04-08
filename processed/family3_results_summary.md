# Family 3: State Institutional Environment — Systematic Results

Panel: 7,514 rows × 3,304 cols
Base controls: Rep_Mayor, pres_dem_vote_share, log_population_city_lag2, log_percapita_income_city_lag2, unemployment_city_lag2, cwns_needs_real_lag2, pct_deficient_lag2, reserve_ratio_lag2, debt_service_burden_lag2, npdes_formal_any_prior3yr, overflow_events_lag2, net_borrowing_ratio_lag2, esg_has_muni_bond_law, state_rep_trifecta, tel_stringency_normalized
Preferred FE: state+year (direct), city+year (interactions)

## Direct Effects (state+year FE)

| Variable | → Self-labelled | → Assurance | → Water-only | → Amount |
|---|---|---|---|---|
| epa_state_response_rate_npdes | -0.0012 (p=0.263) | -0.0003 (p=0.547) | -0.0004 (p=0.501) | -0.0368 (p=0.044)** |
| epa_state_stringency_index | -0.0069 (p=0.808) | -0.0119 (p=0.403) | +0.0174 (p=0.486) | -0.2623 (p=0.640) |
| esg_cum_exec_actions | +0.0001 (p=0.770) | +0.0002 (p=0.475) | +0.0002 (p=0.475) | +0.0052 (p=0.343) |
| esg_governor_alliance_member | +0.0082 (p=0.396) | +0.0104 (p=0.235) | -0.0045 (p=0.459) | +0.1164 (p=0.544) |
| esg_has_esg_disclosure_requirement | +0.0078 (p=0.454) | +0.0066 (p=0.434) | +0.0170 (p=0.249) | +0.2437 (p=0.302) |
| esg_has_fossil_divestment | +0.0053 (p=0.544) | +0.0082 (p=0.263) | +0.0043 (p=0.650) | +0.1053 (p=0.556) |
| esg_has_law_esg_score_ban_govt | -0.0085 (p=0.312) | -0.0043 (p=0.376) | -0.0099 (p=0.280) | -0.1602 (p=0.372) |
| esg_has_muni_bond_law | -0.0107 (p=0.095)* | -0.0082 (p=0.123) | -0.0095 (p=0.192) | -0.1973 (p=0.169) |
| esg_has_proesg_law | -0.0190 (p=0.024)** | -0.0061 (p=0.363) | -0.0109 (p=0.159) | -0.3304 (p=0.040)** |
| esg_has_underwriter_block | +0.0056 (p=0.310) | +0.0021 (p=0.617) | +0.0018 (p=0.767) | +0.0138 (p=0.912) |
| esg_law_intensity_score | -0.0016 (p=0.604) | +0.0007 (p=0.758) | -0.0003 (p=0.920) | +0.0221 (p=0.730) |
| esg_msrb_letter_signatory | +0.0085 (p=0.384) | +0.0059 (p=0.506) | +0.0018 (p=0.827) | +0.2370 (p=0.219) |
| muni_aaa_yield | -0.1844 (p=0.007)*** | -0.1313 (p=0.029)** | -0.1047 (p=0.003)*** | -4.2656 (p=0.002)*** |
| portal_total_lending | -0.0000 (p=0.652) | +0.0000 (p=0.459) | +0.0000 (p=0.660) | +0.0000 (p=0.541) |
| srf_received_any | -0.0208 (p=0.103) | -0.0083 (p=0.481) | -0.0027 (p=0.858) | -0.2469 (p=0.507) |
| state_carbon_price | -0.0006 (p=0.307) | -0.0000 (p=0.993) | -0.0007 (p=0.336) | -0.0176 (p=0.175) |
| state_carbon_pricing | -0.0113 (p=0.381) | -0.0060 (p=0.518) | -0.0077 (p=0.575) | -0.2437 (p=0.382) |
| state_climate_plan | +0.0663 (p=0.000)*** | +0.0047 (p=0.395) | +0.0437 (p=0.000)*** | +1.3920 (p=0.000)*** |
| state_dem_governor | -0.0040 (p=0.627) | -0.0011 (p=0.844) | -0.0046 (p=0.531) | -0.1077 (p=0.547) |
| state_dem_trifecta | -0.0079 (p=0.447) | -0.0041 (p=0.609) | -0.0040 (p=0.610) | -0.1929 (p=0.334) |
| state_divided_govt | +0.0075 (p=0.359) | +0.0035 (p=0.596) | +0.0055 (p=0.446) | +0.1976 (p=0.222) |
| state_gini_index | +0.1279 (p=0.904) | +0.0460 (p=0.962) | +0.7653 (p=0.517) | -11.0687 (p=0.590) |
| state_green_bond_cum_count_lag1 | +0.0000 (p=0.167) | +0.0000 (p=0.343) | -0.0000 (p=0.757) | +0.0003 (p=0.528) |
| state_green_bond_ever_lag1 | +0.0087 (p=0.441) | +0.0021 (p=0.822) | +0.0019 (p=0.833) | +0.2488 (p=0.233) |
| state_green_bond_issued_prior_yr | -0.0056 (p=0.255) | -0.0060 (p=0.147) | -0.0047 (p=0.435) | -0.0274 (p=0.812) |
| state_has_income_tax | +0.0611 (p=0.000)*** | +0.0108 (p=0.079)* | +0.0318 (p=0.000)*** | +1.3330 (p=0.000)*** |
| state_homeownership_rate | +0.0024 (p=0.541) | +0.0011 (p=0.738) | +0.0082 (p=0.241) | +0.0988 (p=0.211) |
| state_median_hh_income | -0.0000 (p=0.512) | +0.0000 (p=0.839) | -0.0000 (p=0.680) | -0.0000 (p=0.364) |
| state_medicaid_expanded | -0.0090 (p=0.275) | -0.0058 (p=0.311) | -0.0128 (p=0.125) | -0.2617 (p=0.177) |
| state_pct_bachelors_plus | -0.0069 (p=0.127) | -0.0015 (p=0.678) | -0.0071 (p=0.330) | -0.1021 (p=0.440) |
| state_poverty_rate | +0.0011 (p=0.790) | -0.0020 (p=0.561) | +0.0046 (p=0.309) | +0.0030 (p=0.970) |
| state_rep_trifecta | -0.0066 (p=0.456) | -0.0103 (p=0.300) | -0.0071 (p=0.322) | -0.1706 (p=0.246) |
| state_right_to_work | +0.0054 (p=0.605) | +0.0113 (p=0.253) | +0.0116 (p=0.238) | +0.1964 (p=0.311) |
| state_rps_active | +0.0203 (p=0.357) | +0.0234 (p=0.283) | +0.0360 (p=0.148) | +0.2521 (p=0.678) |
| state_rps_target_pct | +0.0002 (p=0.357) | +0.0002 (p=0.283) | +0.0004 (p=0.148) | +0.0025 (p=0.678) |
| tel_assessment_limit | +0.0572 (p=0.000)*** | +0.0253 (p=0.013)** | +0.0463 (p=0.000)*** | +1.3447 (p=0.000)*** |
| tel_general_expenditure_limit | +0.0541 (p=0.000)*** | +0.0236 (p=0.027)** | +0.0393 (p=0.000)*** | +1.2315 (p=0.000)*** |
| tel_general_revenue_limit | +0.0658 (p=0.000)*** | +0.0122 (p=0.174) | +0.0400 (p=0.000)*** | +1.5004 (p=0.000)*** |
| tel_levy_limit | +0.0658 (p=0.000)*** | +0.0253 (p=0.014)** | +0.0488 (p=0.000)*** | +1.5050 (p=0.000)*** |
| tel_overall_rate_limit | +0.0648 (p=0.000)*** | +0.0296 (p=0.007)*** | +0.0482 (p=0.000)*** | +1.5234 (p=0.000)*** |
| tel_stringency_normalized | +0.0018 (p=0.000)*** | +0.0007 (p=0.010)** | +0.0013 (p=0.000)*** | +0.0406 (p=0.000)*** |
| total_srf_allotment | -0.0000 (p=0.896) | +0.0000 (p=0.720) | -0.0000 (p=0.335) | -0.0000 (p=0.425) |
| us_esg_aum_trillion | -0.0198 (p=0.013)** | -0.0141 (p=0.033)** | -0.0104 (p=0.005)*** | -0.4546 (p=0.005)*** |

## Interactions × Rep_Mayor (city+year FE)

| Variable × Rep | → Self-labelled | → Assurance | → Water-only | → Amount |
|---|---|---|---|---|
| esg_cum_exec_actions × Rep | +0.0001 (p=0.868) | -0.0001 (p=0.765) | +0.0003 (p=0.398) | +0.0018 (p=0.806) |
| esg_governor_alliance_member × Rep | -0.0050 (p=0.770) | -0.0074 (p=0.627) | +0.0088 (p=0.407) | -0.1664 (p=0.626) |
| esg_has_esg_disclosure_requirement × Rep | +0.0284 (p=0.217) | -0.0072 (p=0.611) | +0.0406 (p=0.225) | +0.9268 (p=0.095)* |
| esg_has_fossil_divestment × Rep | +0.0092 (p=0.569) | -0.0092 (p=0.267) | +0.0251 (p=0.234) | +0.4630 (p=0.223) |
| esg_has_law_esg_score_ban_govt × Rep | +0.0279 (p=0.054)* | +0.0149 (p=0.169) | +0.0179 (p=0.312) | +0.3760 (p=0.266) |
| esg_has_muni_bond_law × Rep | +0.0098 (p=0.368) | +0.0095 (p=0.259) | -0.0011 (p=0.937) | -0.0016 (p=0.995) |
| esg_has_proesg_law × Rep | +0.0049 (p=0.672) | +0.0000 (p=0.998) | +0.0158 (p=0.226) | +0.4074 (p=0.091)* |
| esg_has_underwriter_block × Rep | +0.0031 (p=0.557) | +0.0055 (p=0.271) | +0.0036 (p=0.499) | +0.0687 (p=0.505) |
| esg_law_intensity_score × Rep | +0.0049 (p=0.147) | +0.0012 (p=0.646) | +0.0039 (p=0.291) | +0.0455 (p=0.558) |
| esg_msrb_letter_signatory × Rep | -0.0076 (p=0.559) | -0.0063 (p=0.589) | -0.0033 (p=0.737) | -0.3286 (p=0.211) |
| go_supermajority × Rep | — | — | — | — |
| has_bond_bank × Rep | — | — | — | — |
| has_constitutional_debt_limit × Rep | — | — | — | — |
| has_state_approval_body × Rep | — | — | — | — |
| has_state_bond_commission × Rep | — | — | — | — |
| muni_aaa_yield × Rep | — | — | — | — |
| pro_esg_rfi_response × Rep | — | — | — | — |
| signed_utah_antiesg_letter × Rep | — | — | — | — |
| state_carbon_price × Rep | -0.0006 (p=0.463) | -0.0002 (p=0.695) | -0.0008 (p=0.369) | -0.0082 (p=0.596) |
| state_carbon_pricing × Rep | -0.0143 (p=0.383) | -0.0005 (p=0.952) | -0.0171 (p=0.422) | -0.1157 (p=0.750) |
| state_climate_plan × Rep | — | — | — | — |
| state_dem_governor × Rep | -0.0068 (p=0.510) | -0.0071 (p=0.414) | -0.0067 (p=0.629) | -0.1971 (p=0.358) |
| state_dem_trifecta × Rep | +0.0033 (p=0.795) | -0.0059 (p=0.509) | +0.0155 (p=0.393) | +0.2499 (p=0.328) |
| state_divided_govt × Rep | -0.0083 (p=0.434) | -0.0038 (p=0.715) | -0.0203 (p=0.080)* | -0.4129 (p=0.055)* |
| state_green_bond_cum_count_lag1 × Rep | — | — | — | — |
| state_green_bond_ever_lag1 × Rep | — | — | — | — |
| state_green_bond_issued_prior_yr × Rep | — | — | — | — |
| state_rep_trifecta × Rep | +0.0059 (p=0.602) | +0.0095 (p=0.343) | +0.0064 (p=0.653) | +0.2037 (p=0.339) |
| state_rps_active × Rep | +0.0060 (p=0.593) | -0.0026 (p=0.705) | +0.0204 (p=0.211) | +0.3023 (p=0.211) |
| state_rps_target_pct × Rep | +0.0002 (p=0.634) | -0.0001 (p=0.731) | +0.0007 (p=0.409) | +0.0076 (p=0.362) |
| us_esg_aum_trillion × Rep | — | — | — | — |
