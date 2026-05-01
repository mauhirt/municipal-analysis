# Table 2 — Sparse categories (climate adapt, pollution control, natural resource)

LPM + Fisher exact test. Primary treatment `Dem_Mayor`.
Categories have low positive counts (3-9), so coefficients are imprecise
and Fisher exact p-values are more informative.


| Variable | T5 Climate Adapt<br>Y_climate_adapt | T6 Pollution Control<br>Y_Pollution_Control | T7 Natural Resource<br>Y_natural_resource |
|---|---|---|---|
| `Dem_Mayor` | +0.0000 (0.0008) | -0.0002 (0.0010) | -0.0001 (0.0004) |
| `pres_dem_two_party_share_lag2` | +0.0092 (0.0059) | +0.0131 (0.0083) | -0.0002 (0.0037) |
| `nfip_total_losses_asinh_lag2` | +0.0002 (0.0006) | — | — |
| `fema_disaster_flood_lag2` | +0.0017 (0.0026) | — | — |
| `nri_inland_flooding_eal_bv` | -0.0000*** (0.0000) | — | — |
| `fema_resil_grant_amt_asinh_lag1` | -0.0003*** (0.0001) | — | — |
| `epa_water_violations_asinh_lag2` | — | -0.0003 (0.0004) | — |
| `epa_npdes_informal_asinh_lag2` | — | +0.0001 (0.0007) | — |
| `caa_any_criteria_nonattainment_lag1` | — | -0.0011 (0.0020) | — |
| `rcra_violations_count_muni` | — | -0.0003 (0.0005) | — |
| `nri_overall_risk_score` | — | — | +0.0001 (0.0001) |
| `nri_water_risk_score` | — | — | -0.0005 (0.0005) |
| N | 5917 | 5962 | 5420 |
| n_pos | 7 | 9 | 3 |
| Fisher Dem rate | 0.2% | 0.2% | 0.1% |
| Fisher Rep rate | 0.0% | 0.0% | 0.0% |
| Fisher p-value | 0.022 | 0.087 | 0.263 |

Stars: * p<0.10, ** p<0.05, *** p<0.01.
