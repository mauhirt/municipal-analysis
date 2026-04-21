# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | +0.0008 | 0.0044 | +0.19 | 0.848 | 0.0041 | +0.21 | 0.837 | 0.0054 | +0.16 | 0.875 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0502 | 0.0281 | +1.78 | 0.074* | 0.0292 | +1.72 | 0.086* | 0.0280 | +1.79 | 0.073* |
| C1 GBI | `npdes_formal_prior3yr_muni` | +0.0159 | 0.0082 | +1.95 | 0.051* | 0.0092 | +1.73 | 0.084* | 0.0085 | +1.88 | 0.061* |
| C1 GBI | `reserve_ratio_lag2` | +0.0046 | 0.0035 | +1.30 | 0.193 | 0.0042 | +1.08 | 0.281 | 0.0032 | +1.43 | 0.152 |
| C1 GBI | `debt_service_burden_lag2` | -0.0552 | 0.0563 | -0.98 | 0.327 | 0.0558 | -0.99 | 0.323 | 0.0481 | -1.15 | 0.251 |
| C3 Self-green | `Dem_Mayor` | -0.0009 | 0.0040 | -0.23 | 0.819 | 0.0042 | -0.22 | 0.827 | 0.0036 | -0.25 | 0.799 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0526 | 0.0266 | +1.98 | 0.048** | 0.0290 | +1.81 | 0.070* | 0.0258 | +2.04 | 0.042** |
| C3 Self-green | `npdes_formal_prior3yr_muni` | +0.0180 | 0.0073 | +2.47 | 0.013** | 0.0087 | +2.06 | 0.039** | 0.0068 | +2.66 | 0.008*** |
| C3 Self-green | `reserve_ratio_lag2` | +0.0032 | 0.0030 | +1.04 | 0.299 | 0.0038 | +0.83 | 0.404 | 0.0028 | +1.12 | 0.264 |
| C3 Self-green | `debt_service_burden_lag2` | -0.0340 | 0.0499 | -0.68 | 0.496 | 0.0476 | -0.71 | 0.475 | 0.0475 | -0.72 | 0.474 |
| C5 NPDES×Party | `Dem_Mayor` | -0.0030 | 0.0046 | -0.65 | 0.516 | 0.0034 | -0.88 | 0.378 | 0.0054 | -0.56 | 0.576 |
| C5 NPDES×Party | `pres_dem_two_party_share_lag2` | +0.0482 | 0.0280 | +1.72 | 0.085* | 0.0289 | +1.67 | 0.095* | 0.0278 | +1.73 | 0.083* |
| C5 NPDES×Party | `npdes_formal_prior3yr_muni` | -0.0019 | 0.0055 | -0.35 | 0.725 | 0.0044 | -0.44 | 0.660 | 0.0051 | -0.38 | 0.705 |
| C5 NPDES×Party | `reserve_ratio_lag2` | +0.0048 | 0.0035 | +1.37 | 0.171 | 0.0042 | +1.13 | 0.257 | 0.0032 | +1.50 | 0.134 |
| C5 NPDES×Party | `debt_service_burden_lag2` | -0.0559 | 0.0561 | -1.00 | 0.319 | 0.0555 | -1.01 | 0.314 | 0.0480 | -1.16 | 0.244 |
| C5 NPDES×Party | `dem_x_npdes` | +0.0286 | 0.0149 | +1.91 | 0.056* | 0.0176 | +1.62 | 0.106 | 0.0154 | +1.85 | 0.064* |
| C6 Demonstration | `Dem_Mayor` | -0.0261 | 0.0098 | -2.68 | 0.007*** | 0.0128 | -2.04 | 0.041** | 0.0121 | -2.16 | 0.031** |
| C6 Demonstration | `pres_dem_two_party_share_lag2` | +0.0526 | 0.0265 | +1.98 | 0.048** | 0.0291 | +1.80 | 0.071* | 0.0258 | +2.03 | 0.042** |
| C6 Demonstration | `npdes_formal_prior3yr_muni` | +0.0180 | 0.0073 | +2.47 | 0.013** | 0.0088 | +2.05 | 0.040** | 0.0067 | +2.67 | 0.008*** |
| C6 Demonstration | `reserve_ratio_lag2` | +0.0032 | 0.0030 | +1.05 | 0.295 | 0.0037 | +0.85 | 0.397 | 0.0028 | +1.12 | 0.264 |
| C6 Demonstration | `debt_service_burden_lag2` | -0.0369 | 0.0497 | -0.74 | 0.458 | 0.0479 | -0.77 | 0.441 | 0.0474 | -0.78 | 0.437 |
| C6 Demonstration | `dem_x_state_green_cum` | +0.0013 | 0.0005 | +2.62 | 0.009*** | 0.0007 | +1.86 | 0.063* | 0.0006 | +2.21 | 0.027** |

## Reading

### Coefficients where significance is attenuated by alternative clustering:
- **`dem_x_npdes` in C5 NPDES×Party:** significant under city clustering (p=0.056) but NOT under state clustering (p=0.106). SE inflates from 0.0149 to 0.0176.

* p<0.10, ** p<0.05, *** p<0.01.
