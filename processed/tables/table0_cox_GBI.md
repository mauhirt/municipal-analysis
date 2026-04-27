# Cox Proportional Hazards: Time-to-First Green_Bond_Issued

**Event:** first city-year with `Green_Bond_Issued == 1` during 2013-2025.
**Censoring:** cities that never issue are censored at 2025.
**Strata:** `state_id` (state-level baseline hazards absorbed).
**Time-varying covariates:** all listed in `pipeline/analysis_table0_survival.py` COVARIATES.

- At-risk rows: 5,512
- Cities in risk set: 562
- Events: 72
- Log-likelihood: -159.31

| Variable | Hazard Ratio | 95% CI | p-value |
|---|---|---|---|
| `Dem_Mayor` | **1.4319** | (0.7583, 2.7040) | 0.2683 |
| `pres_dem_two_party_share_lag2` | **15.4811**** | (1.1711, 204.6541) | 0.0375 |
| `npdes_formal_prior3yr_muni` | **1.1952** | (0.6049, 2.3616) | 0.6078 |
| `overflow_events_lag2` | **1.0000** | (0.2067, 4.8389) | 1.0000 |
| `charges_to_own_source_lag2` | **5.9661** | (0.4916, 72.4125) | 0.1608 |
| `reserve_ratio_lag2` | **1.1343** | (0.7451, 1.7268) | 0.5567 |
| `debt_service_burden_lag2` | **0.0870** | (0.0000, 161.0038) | 0.5246 |
| `igr_share_lag2` | **1.0780** | (0.0556, 20.8941) | 0.9604 |
| `tel_x_prop_tax_dep` | **1.0265** | (0.9811, 1.0741) | 0.2569 |
| `state_self_green_cum_count_lag1` | **1.0000** | (0.8756, 1.1420) | 1.0000 |
| `state_any_rep_self_green_lag1` | **1.0000** | (0.1401, 7.1367) | 1.0000 |
| `state_dem_governor_lag1` | **0.5587** | (0.1331, 2.3443) | 0.4263 |
| `state_rep_trifecta_lag1` | **1.9240** | (0.4424, 8.3677) | 0.3829 |
| `fn_esg_has_muni_bond_law_post_lag1` | **1.1539** | (0.2169, 6.1386) | 0.8667 |
| `log_population_city_lag2` | **2.1651***** | (1.5664, 2.9926) | 0.0000 |
| `log_percapita_income_city_lag2` | **2.5951** | (0.7901, 8.5237) | 0.1160 |
| `unemployment_city_lag2` | **1.1629** | (0.9170, 1.4749) | 0.2131 |

HR > 1: covariate increases the instantaneous hazard of first-ever green-bond issuance.
HR < 1: covariate delays first issuance.

**Widmann (2026) comparison:** the `state_self_green_cum_count_lag1` hazard ratio here
is directly comparable to Widmann's Corporate Private Cumulative (HR ≈ 1.017-1.021,
each +1 corporate bond raises sovereign-entry hazard by 1.7-2.1%). Our equivalent
tests whether each prior muni self-green bond in the state raises the hazard of a new
muni entering.

Stars: * p < 0.10, ** p < 0.05, *** p < 0.01.
