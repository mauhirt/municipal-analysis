# Cox Proportional Hazards: Time-to-First Y_self_green

**Event:** first city-year with `Y_self_green == 1` (bond self-designated green).
**Censoring:** cities that never self-label are censored at 2025.
**Strata:** `state_id`.

- At-risk rows: 5,619
- Cities in risk set: 567
- Events: 57
- Log-likelihood: -126.24

| Variable | Hazard Ratio | 95% CI | p-value |
|---|---|---|---|
| `Dem_Mayor` | **1.4107** | (0.6893, 2.8872) | 0.3464 |
| `pres_dem_two_party_share_lag2` | **45.9665***** | (2.6256, 804.7371) | 0.0088 |
| `npdes_formal_prior3yr_muni` | **1.7588** | (0.8423, 3.6728) | 0.1328 |
| `overflow_events_lag2` | **1.0000** | (0.2067, 4.8388) | 1.0000 |
| `charges_to_own_source_lag2` | **5.0727** | (0.3329, 77.3060) | 0.2426 |
| `reserve_ratio_lag2` | **1.1544** | (0.7089, 1.8800) | 0.5639 |
| `debt_service_burden_lag2` | **0.0637** | (0.0000, 256.7086) | 0.5156 |
| `igr_share_lag2` | **0.8364** | (0.0288, 24.2990) | 0.9172 |
| `tel_x_prop_tax_dep` | **1.0349** | (0.9877, 1.0843) | 0.1495 |
| `state_self_green_cum_count_lag1` | **1.0000** | (0.8765, 1.1408) | 1.0000 |
| `state_any_rep_self_green_lag1` | **1.0000** | (0.1431, 6.9871) | 1.0000 |
| `state_dem_governor_lag1` | **0.5593** | (0.1314, 2.3808) | 0.4318 |
| `state_rep_trifecta_lag1` | **1.8462** | (0.4255, 8.0102) | 0.4129 |
| `fn_esg_has_muni_bond_law_post_lag1` | **1.0487** | (0.1872, 5.8741) | 0.9568 |
| `log_population_city_lag2` | **2.1251***** | (1.4951, 3.0205) | 0.0000 |
| `log_percapita_income_city_lag2` | **1.6599** | (0.4605, 5.9830) | 0.4386 |
| `unemployment_city_lag2` | **1.1971** | (0.9310, 1.5392) | 0.1606 |

HR > 1: covariate accelerates first self-green designation.
HR < 1: covariate delays.

Step-3 discretion (per memo): self-designation is the first genuinely discretionary
step in the decision chain. If `Dem_Mayor` predicts timing here (HR > 1), that is a
hazard-model analogue of the memo's expected Rep_Mayor-negative at Col 3.

Stars: * p < 0.10, ** p < 0.05, *** p < 0.01.
