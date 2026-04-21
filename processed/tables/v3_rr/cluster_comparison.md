# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | +0.0009 | 0.0044 | +0.19 | 0.846 | 0.0041 | +0.21 | 0.835 | 0.0054 | +0.16 | 0.874 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0502 | 0.0281 | +1.78 | 0.074* | 0.0294 | +1.71 | 0.087* | 0.0281 | +1.79 | 0.074* |
| C1 GBI | `npdes_formal_prior3yr_muni` | +0.0156 | 0.0082 | +1.91 | 0.057* | 0.0093 | +1.69 | 0.091* | 0.0086 | +1.83 | 0.068* |
| C1 GBI | `reserve_ratio_lag2` | +0.0049 | 0.0035 | +1.38 | 0.167 | 0.0043 | +1.14 | 0.256 | 0.0033 | +1.50 | 0.134 |
| C1 GBI | `debt_service_burden_lag2` | -0.0528 | 0.0565 | -0.94 | 0.350 | 0.0563 | -0.94 | 0.348 | 0.0473 | -1.12 | 0.264 |
| C3 Self-green | `Dem_Mayor` | -0.0009 | 0.0040 | -0.23 | 0.819 | 0.0042 | -0.22 | 0.828 | 0.0036 | -0.25 | 0.799 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0526 | 0.0266 | +1.98 | 0.048** | 0.0292 | +1.80 | 0.071* | 0.0258 | +2.03 | 0.042** |
| C3 Self-green | `npdes_formal_prior3yr_muni` | +0.0178 | 0.0073 | +2.43 | 0.015** | 0.0088 | +2.03 | 0.042** | 0.0069 | +2.60 | 0.009*** |
| C3 Self-green | `reserve_ratio_lag2` | +0.0034 | 0.0030 | +1.11 | 0.267 | 0.0038 | +0.89 | 0.376 | 0.0029 | +1.18 | 0.239 |
| C3 Self-green | `debt_service_burden_lag2` | -0.0323 | 0.0503 | -0.64 | 0.520 | 0.0487 | -0.66 | 0.506 | 0.0474 | -0.68 | 0.495 |
| C5 NPDES×Party | `Dem_Mayor` | -0.0030 | 0.0046 | -0.65 | 0.518 | 0.0034 | -0.88 | 0.378 | 0.0054 | -0.56 | 0.577 |
| C5 NPDES×Party | `pres_dem_two_party_share_lag2` | +0.0482 | 0.0280 | +1.72 | 0.085* | 0.0290 | +1.66 | 0.097* | 0.0279 | +1.73 | 0.084* |
| C5 NPDES×Party | `npdes_formal_prior3yr_muni` | -0.0022 | 0.0055 | -0.40 | 0.688 | 0.0044 | -0.51 | 0.612 | 0.0052 | -0.43 | 0.669 |
| C5 NPDES×Party | `reserve_ratio_lag2` | +0.0051 | 0.0035 | +1.45 | 0.147 | 0.0043 | +1.19 | 0.234 | 0.0032 | +1.57 | 0.117 |
| C5 NPDES×Party | `debt_service_burden_lag2` | -0.0535 | 0.0563 | -0.95 | 0.341 | 0.0560 | -0.96 | 0.339 | 0.0472 | -1.13 | 0.257 |
| C5 NPDES×Party | `dem_x_npdes` | +0.0286 | 0.0149 | +1.91 | 0.056* | 0.0176 | +1.62 | 0.105 | 0.0154 | +1.85 | 0.064* |
| C6 Demonstration | `Dem_Mayor` | -0.0262 | 0.0097 | -2.69 | 0.007*** | 0.0128 | -2.05 | 0.041** | 0.0121 | -2.17 | 0.030** |
| C6 Demonstration | `pres_dem_two_party_share_lag2` | +0.0526 | 0.0265 | +1.98 | 0.047** | 0.0293 | +1.80 | 0.072* | 0.0259 | +2.03 | 0.042** |
| C6 Demonstration | `npdes_formal_prior3yr_muni` | +0.0178 | 0.0073 | +2.43 | 0.015** | 0.0088 | +2.02 | 0.043** | 0.0068 | +2.61 | 0.009*** |
| C6 Demonstration | `reserve_ratio_lag2` | +0.0034 | 0.0030 | +1.12 | 0.263 | 0.0038 | +0.90 | 0.369 | 0.0029 | +1.18 | 0.239 |
| C6 Demonstration | `debt_service_burden_lag2` | -0.0353 | 0.0500 | -0.70 | 0.481 | 0.0490 | -0.72 | 0.471 | 0.0474 | -0.74 | 0.457 |
| C6 Demonstration | `dem_x_state_green_cum` | +0.0013 | 0.0005 | +2.63 | 0.009*** | 0.0007 | +1.86 | 0.063* | 0.0006 | +2.22 | 0.026** |

## Reading

### Coefficients where significance is attenuated by alternative clustering:
- **`dem_x_npdes` in C5 NPDES×Party:** significant under city clustering (p=0.056) but NOT under state clustering (p=0.105). SE inflates from 0.0149 to 0.0176.

* p<0.10, ** p<0.05, *** p<0.01.
