# Table 1 with city + year FE — within-city robustness

## What city + year fixed effects mean

State + year FE (the Table 1 default) identifies the effect of a variable off cross-city variation **within a state in a given year**. Cities that never change the variable value (e.g., a never-switcher city on `Rep_Mayor_lag1`) still contribute through their cross-city position.

City + year FE removes that cross-city variation entirely. Identification is only from **within-city changes over time**. This is a much stricter test:

- A city with no within-city variation in the treatment contributes nothing  to identifying that coefficient.
- A city with no within-city variation in the outcome contributes nothing  to identifying *any* coefficient.
- Time-invariant variables (static city characteristics, state-level  variables that do not change over the panel window) are perfectly absorbed  and become unidentified — linearmodels drops them.

## Which observations effectively identify each coefficient

- Panel total: **578 cities × 13 years = 7514 city-years**
- Party switchers (Rep_Mayor_lag1 varies over time): **180/578 cities**
- Never-switchers: **395 cities** — contribute zero to β(Rep_Mayor) under city FE
- Ever-issuer cities (Green_Bond_Issued ever = 1): **85/578**
- Ever-self-labelled cities (Y_self_green ever = 1): **65/578**
- Switchers ∩ Green_Bond_Issued varies over time: **24**
- Switchers ∩ Y_self_green varies over time: **16**

These last two numbers are the **effective city count** identifying β(Rep_Mayor) under city + year FE. In practice, β is pinned down by only those cities.

## RHS variables — which survive city FE

| Variable | within-city SD (75th pct) | under city FE |
|---|---|---|
| `Rep_Mayor_lag1` | 0.3608 | YES |
| `Ind_Mayor_lag1` | 0.0000 | **ABSORBED** |
| `pres_dem_two_party_share_lag2` | 0.0296 | YES |
| `npdes_formal_prior3yr_muni` | 0.4213 | YES |
| `overflow_events_lag2` | 0.0000 | **ABSORBED** |
| `charges_to_own_source_lag2` | 0.0424 | YES |
| `reserve_ratio_lag2` | 0.5096 | YES |
| `debt_service_burden_lag2` | 0.0240 | YES |
| `property_tax_dependence_lag2` | 0.0519 | YES |
| `log_cwsrf_obligations_lag2` | 0.8465 | YES |
| `state_rep_trifecta` | 0.0000 | **ABSORBED** |
| `esg_has_muni_bond_law` | 0.0000 | **ABSORBED** |
| `state_green_bond_ever_lag1` | 0.3727 | YES |
| `log_population_city_lag2` | 0.0480 | YES |
| `log_percapita_income_city_lag2` | 0.1630 | YES |
| `unemployment_city_lag2` | 1.6230 | YES |
| `has_substitute_issuer` | 0.2665 | YES |
| `tel_x_prop_tax_dep` | 1.8634 | YES |
| `tel_x_charges` | 1.5753 | YES |

Variables marked ABSORBED (75th-percentile within-city SD ≈ 0) have no within-city variation for at least three quarters of cities — under city FE their coefficients are unidentified and `linearmodels` drops them.

## Results — Rep_Mayor_lag1 under three FE structures

| Outcome | state+year FE, cluster=fips7 (Tables 1/2 default) | state+year FE, cluster=state_id | city+year FE (within-city) |
|---|---|---|---|
| `Green_Bond_Issued` | -0.0031 (se 0.0052), N=5893 | -0.0031 (se 0.0057), N=5893 | -0.0039 (se 0.0085), N=5893 |
| `Y_self_green` | -0.0021 (se 0.0047), N=5893 | -0.0021 (se 0.0056), N=5893 | -0.0042 (se 0.0087), N=5893 |
| `asinh_green_amt` | -0.0536 (se 0.0974), N=5893 | -0.0536 (se 0.1075), N=5893 | -0.0591 (se 0.1645), N=5893 |
| `asinh_self_green_amt` | -0.0373 (se 0.0882), N=5893 | -0.0373 (se 0.1068), N=5893 | -0.0750 (se 0.1640), N=5893 |

## How to read this

- If β(Rep_Mayor_lag1) is null under all three FE structures, the finding is robust.
- If β collapses to zero (or becomes noisier with wider SE) under city FE,  the cross-city baseline was picking up something time-invariant at the  city level that correlates with partisan identity (e.g., state, region,  city size, urban/suburban status) — not partisan identity per se.
- The small effective sample under city FE (only switcher-issuer cities  contribute) means wider SEs are expected. Absence of significance here  reflects power, not evidence against the effect.

## Notable variables lost to city FE

- `has_substitute_issuer` (near-static — whether there is a nearby water  special district — does not change year-to-year for most cities)
- State-level political and institutional variables where the state did  not change status over 2013–2025: `state_rep_trifecta`, `state_dem_governor_lag1`,  `state_carbon_pricing_lag1`, `state_rggi_member_lag1`, `state_wci_member_lag1`,  `state_medicaid_expanded_lag1`, `state_right_to_work_lag1`, `esg_has_underwriter_block`  (in all but a handful of states), `inst_*` institutional variables (cross-sectional).
- Cross-sectional ACS controls: `pct_college_educated`, `pct_nonwhite`,  `median_home_value`, `is_principal_city_lag2`, `pop_density_sqkm_lag2`.
- NRI risk scores (static): `nri_water_risk_score`, `nri_overall_risk_score`,  `nri_inland_flooding_eal_bv`.
- Climate-network memberships that do not change: `climate_commitment_static`,  `iclei_member_static`, `mcpa_signatory_static`.

City FE identifies only the **time-varying** channels: regulatory enforcement events, fiscal condition shocks, tax/expenditure shifts, federal grant receipts, and the small number of mayoral party switches.
