# Table 2 — Non-water discretionary categories

Primary treatment: `Dem_Mayor` (no lag). State + year FE, state clustering.
Category-specific compulsion variables chosen per variable-audit Parts A-E.


| Variable | T1 Clean Transport<br>Y_Clean_Transportation | T2 Renewables<br>Y_Renewable_Energy | T3 Energy Eff<br>Y_Energy_Efficiency | T4 Green Bldg<br>Y_Green_Buildings |
|---|---|---|---|---|
| `Dem_Mayor` | -0.0003 (0.0010) | -0.0001 (0.0040) | -0.0019 (0.0020) | -0.0003 (0.0009) |
| `pres_dem_two_party_share_lag2` | +0.0115 (0.0089) | +0.0190 (0.0248) | +0.0251** (0.0128) | +0.0217* (0.0127) |
| `caa_ozone_nonattainment_any_lag1` | -0.0023 (0.0030) | — | — | — |
| `caa_any_criteria_nonattainment_lag1` | -0.0015 (0.0017) | — | — | — |
| `state_ghg_law_active_lag1` | +0.0035 (0.0028) | — | — | — |
| `state_zev_mandate_active_lag1` | -0.0024 (0.0023) | — | — | — |
| `iija_transit_grant_amt_asinh_lag1` | +0.0002 (0.0002) | — | — | — |
| `ep_muni_electric_rev_asinh_lag1` | — | -0.0230** (0.0101) | — | — |
| `state_rps_active_lag1` | — | -0.0210 (0.0172) | — | — |
| `state_rps_target_pct_lag1` | — | +0.0002 (0.0004) | — | — |
| `rps_target_x_muni_electric` | — | +0.0002 (0.0004) | — | — |
| `state_rggi_member_lag1` | — | -0.0011 (0.0051) | — | — |
| `state_carbon_pricing_lag1` | — | +0.0102*** (0.0030) | -0.0039 (0.0056) | — |
| `bcode_iecc_lag_yrs_lag1` | — | — | -0.0001 (0.0004) | -0.0001 (0.0002) |
| `bcode_state_bps_adopted_lag1` | — | — | +0.0038 (0.0061) | -0.0009 (0.0036) |
| `bcode_bps_adopted_lag1` | — | — | — | -0.0250** (0.0123) |
| `bcode_state_weakening_amendments_lag1` | — | — | -0.0031 (0.0027) | -0.0058* (0.0031) |
| `ep_state_aceee_code_rank_lag1` | — | — | -0.0003** (0.0001) | — |
| `ira_eecbg_grant_amt_asinh_lag1` | — | — | -0.0000 (0.0009) | — |
| `ira_ggrf_grant_amt_asinh_lag1` | — | — | — | -0.0010** (0.0005) |
| `charges_to_own_source_lag2` | +0.0040 (0.0042) | +0.0678* (0.0369) | -0.0019 (0.0098) | +0.0126** (0.0063) |
| `reserve_ratio_lag2` | -0.0007 (0.0010) | +0.0015 (0.0037) | +0.0020 (0.0019) | +0.0013 (0.0018) |
| `debt_service_burden_lag2` | -0.0276 (0.0338) | +0.0132 (0.0549) | -0.0435* (0.0256) | -0.0190 (0.0258) |
| `tel_x_prop_tax_dep` | +0.0005* (0.0003) | +0.0011** (0.0005) | +0.0000 (0.0003) | +0.0003 (0.0002) |
| N | 5972 | 854 | 5396 | 5445 |
| n_pos | 17 | 9 | 20 | 19 |
| R² | 0.066 | 0.213 | 0.037 | 0.059 |

Stars: * p<0.10, ** p<0.05, *** p<0.01.
