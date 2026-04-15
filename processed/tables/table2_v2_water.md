# Table 2 Col 1 — Water (3 compulsion-variable variants)

Primary treatment: `Dem_Mayor` (no lag). State+year FE. State clustering.
Water-only outcome; **90 positive city-years**.


| Variable | W1 Primary (memo)<br>Y_water_only | W2 Ladder<br>Y_water_only | W3 Pooled Index<br>Y_water_only |
|---|---|---|---|
| `Dem_Mayor` | -0.0002 (0.0041) | -0.0004 (0.0041) | -0.0007 (0.0042) |
| `npdes_formal_prior3yr_muni` | +0.0082* (0.0047) | +0.0075 (0.0049) | — |
| `overflow_events_lag2` | +0.0065*** (0.0024) | +0.0065*** (0.0024) | — |
| `epa_npdes_informal_asinh_lag2` | — | -0.0008 (0.0023) | — |
| `epa_water_violations_asinh_lag2` | — | +0.0010 (0.0017) | — |
| `case_jdc_prior3yr_muni` | — | +0.0039 (0.0172) | — |
| `compulsion_index_z` | — | — | +0.0009 (0.0009) |
| `pres_dem_two_party_share_lag2` | +0.0166 (0.0165) | +0.0168 (0.0165) | +0.0156 (0.0164) |
| `charges_to_own_source_lag2` | +0.0196 (0.0210) | +0.0186 (0.0219) | +0.0224 (0.0211) |
| `reserve_ratio_lag2` | +0.0051** (0.0026) | +0.0052** (0.0026) | +0.0051** (0.0026) |
| `debt_service_burden_lag2` | -0.0752* (0.0436) | -0.0762* (0.0446) | -0.0773* (0.0443) |
| `igr_share_lag2` | +0.0057 (0.0153) | +0.0061 (0.0151) | +0.0071 (0.0152) |
| `tel_x_prop_tax_dep` | +0.0008* (0.0004) | +0.0008* (0.0004) | +0.0008* (0.0004) |
| N | 5962 | 5962 | 5972 |
| R² | 0.060 | 0.060 | 0.057 |

Stars: * p<0.10, ** p<0.05, *** p<0.01.
