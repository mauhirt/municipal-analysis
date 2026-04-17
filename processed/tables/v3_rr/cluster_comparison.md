# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | +0.0001 | 0.0048 | +0.03 | 0.980 | 0.0043 | +0.03 | 0.978 | 0.0058 | +0.02 | 0.983 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0566 | 0.0298 | +1.90 | 0.057* | 0.0317 | +1.79 | 0.074* | 0.0295 | +1.92 | 0.055* |
| C1 GBI | `npdes_formal_prior3yr_muni` | +0.0151 | 0.0083 | +1.82 | 0.069* | 0.0084 | +1.80 | 0.073* | 0.0085 | +1.77 | 0.076* |
| C1 GBI | `overflow_events_lag2` | +0.0062 | 0.0020 | +3.14 | 0.002*** | 0.0024 | +2.62 | 0.009*** | 0.0050 | +1.25 | 0.211 |
| C1 GBI | `reserve_ratio_lag2` | +0.0075 | 0.0035 | +2.11 | 0.035** | 0.0038 | +1.99 | 0.047** | 0.0031 | +2.41 | 0.016** |
| C1 GBI | `debt_service_burden_lag2` | -0.1242 | 0.0656 | -1.89 | 0.058* | 0.0712 | -1.74 | 0.081* | 0.0613 | -2.03 | 0.043** |
| C3 Self-green | `Dem_Mayor` | -0.0015 | 0.0043 | -0.35 | 0.728 | 0.0044 | -0.34 | 0.732 | 0.0040 | -0.38 | 0.707 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0582 | 0.0279 | +2.08 | 0.037** | 0.0308 | +1.89 | 0.059* | 0.0259 | +2.25 | 0.025** |
| C3 Self-green | `npdes_formal_prior3yr_muni` | +0.0179 | 0.0073 | +2.46 | 0.014** | 0.0079 | +2.27 | 0.023** | 0.0063 | +2.82 | 0.005*** |
| C3 Self-green | `overflow_events_lag2` | +0.0062 | 0.0020 | +3.05 | 0.002*** | 0.0024 | +2.56 | 0.011** | 0.0050 | +1.22 | 0.221 |
| C3 Self-green | `reserve_ratio_lag2` | +0.0058 | 0.0029 | +1.97 | 0.049** | 0.0032 | +1.82 | 0.068* | 0.0029 | +1.97 | 0.049** |
| C3 Self-green | `debt_service_burden_lag2` | -0.1021 | 0.0588 | -1.74 | 0.083* | 0.0653 | -1.56 | 0.118 | 0.0619 | -1.65 | 0.099* |
| C5 NPDES×Party | `Dem_Mayor` | -0.0037 | 0.0051 | -0.72 | 0.473 | 0.0040 | -0.91 | 0.361 | 0.0058 | -0.63 | 0.528 |
| C5 NPDES×Party | `pres_dem_two_party_share_lag2` | +0.0547 | 0.0298 | +1.84 | 0.066* | 0.0314 | +1.75 | 0.081* | 0.0294 | +1.86 | 0.062* |
| C5 NPDES×Party | `npdes_formal_prior3yr_muni` | -0.0029 | 0.0058 | -0.50 | 0.615 | 0.0049 | -0.59 | 0.554 | 0.0050 | -0.57 | 0.566 |
| C5 NPDES×Party | `overflow_events_lag2` | +0.0062 | 0.0020 | +3.17 | 0.002*** | 0.0023 | +2.66 | 0.008*** | 0.0049 | +1.26 | 0.207 |
| C5 NPDES×Party | `reserve_ratio_lag2` | +0.0076 | 0.0035 | +2.16 | 0.031** | 0.0038 | +2.03 | 0.042** | 0.0031 | +2.45 | 0.014** |
| C5 NPDES×Party | `debt_service_burden_lag2` | -0.1227 | 0.0652 | -1.88 | 0.060* | 0.0707 | -1.73 | 0.083* | 0.0610 | -2.01 | 0.044** |
| C5 NPDES×Party | `dem_x_npdes` | +0.0288 | 0.0149 | +1.93 | 0.054* | 0.0171 | +1.68 | 0.092* | 0.0150 | +1.93 | 0.054* |
| C6 Overflow×Party | `Dem_Mayor` | +0.0004 | 0.0048 | +0.08 | 0.938 | 0.0043 | +0.09 | 0.932 | 0.0057 | +0.06 | 0.948 |
| C6 Overflow×Party | `pres_dem_two_party_share_lag2` | +0.0563 | 0.0298 | +1.89 | 0.059* | 0.0317 | +1.78 | 0.075* | 0.0295 | +1.91 | 0.056* |
| C6 Overflow×Party | `npdes_formal_prior3yr_muni` | +0.0151 | 0.0083 | +1.82 | 0.069* | 0.0084 | +1.79 | 0.073* | 0.0085 | +1.77 | 0.077* |
| C6 Overflow×Party | `overflow_events_lag2` | +0.0086 | 0.0008 | +10.40 | 0.000*** | 0.0006 | +14.83 | 0.000*** | 0.0039 | +2.20 | 0.028** |
| C6 Overflow×Party | `reserve_ratio_lag2` | +0.0075 | 0.0035 | +2.11 | 0.034** | 0.0038 | +2.00 | 0.046** | 0.0031 | +2.42 | 0.016** |
| C6 Overflow×Party | `debt_service_burden_lag2` | -0.1242 | 0.0656 | -1.89 | 0.059* | 0.0712 | -1.74 | 0.081* | 0.0613 | -2.02 | 0.043** |
| C6 Overflow×Party | `dem_x_overflow` | -0.0086 | 0.0010 | -8.87 | 0.000*** | 0.0007 | -11.50 | 0.000*** | 0.0038 | -2.27 | 0.023** |
| C7 Demonstration | `Dem_Mayor` | -0.0333 | 0.0142 | -2.35 | 0.019** | 0.0192 | -1.73 | 0.083* | 0.0198 | -1.68 | 0.093* |
| C7 Demonstration | `pres_dem_two_party_share_lag2` | +0.0585 | 0.0279 | +2.10 | 0.036** | 0.0310 | +1.89 | 0.059* | 0.0260 | +2.25 | 0.024** |
| C7 Demonstration | `npdes_formal_prior3yr_muni` | +0.0178 | 0.0072 | +2.45 | 0.014** | 0.0078 | +2.26 | 0.024** | 0.0063 | +2.82 | 0.005*** |
| C7 Demonstration | `overflow_events_lag2` | +0.0062 | 0.0020 | +3.13 | 0.002*** | 0.0024 | +2.63 | 0.009*** | 0.0050 | +1.24 | 0.215 |
| C7 Demonstration | `reserve_ratio_lag2` | +0.0057 | 0.0029 | +1.95 | 0.051* | 0.0032 | +1.81 | 0.070* | 0.0030 | +1.93 | 0.054* |
| C7 Demonstration | `debt_service_burden_lag2` | -0.1048 | 0.0591 | -1.77 | 0.076* | 0.0661 | -1.58 | 0.113 | 0.0623 | -1.68 | 0.093* |
| C7 Demonstration | `dem_x_state_green_cum` | +0.0015 | 0.0007 | +2.34 | 0.019** | 0.0010 | +1.62 | 0.105 | 0.0009 | +1.73 | 0.084* |

## Reading

### Coefficients where significance is attenuated by alternative clustering:
- **`overflow_events_lag2` in C1 GBI:** significant under city clustering (p=0.002) but NOT under two-way (p=0.211).
- **`overflow_events_lag2` in C3 Self-green:** significant under city clustering (p=0.002) but NOT under two-way (p=0.221).
- **`debt_service_burden_lag2` in C3 Self-green:** significant under city clustering (p=0.083) but NOT under state clustering (p=0.118). SE inflates from 0.0588 to 0.0653.
- **`overflow_events_lag2` in C5 NPDES×Party:** significant under city clustering (p=0.002) but NOT under two-way (p=0.207).
- **`overflow_events_lag2` in C7 Demonstration:** significant under city clustering (p=0.002) but NOT under two-way (p=0.215).
- **`debt_service_burden_lag2` in C7 Demonstration:** significant under city clustering (p=0.076) but NOT under state clustering (p=0.113). SE inflates from 0.0591 to 0.0661.
- **`dem_x_state_green_cum` in C7 Demonstration:** significant under city clustering (p=0.019) but NOT under state clustering (p=0.105). SE inflates from 0.0007 to 0.0010.

* p<0.10, ** p<0.05, *** p<0.01.
