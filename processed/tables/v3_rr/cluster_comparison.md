# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | +0.0005 | 0.0044 | +0.11 | 0.913 | 0.0037 | +0.13 | 0.897 | 0.0054 | +0.09 | 0.930 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0535 | 0.0269 | +1.99 | 0.046** | 0.0301 | +1.78 | 0.075* | 0.0274 | +1.95 | 0.051* |
| C1 GBI | `npdes_formal_prior3yr_muni` | +0.0145 | 0.0078 | +1.85 | 0.065* | 0.0084 | +1.72 | 0.086* | 0.0083 | +1.74 | 0.081* |
| C1 GBI | `reserve_ratio_lag2` | +0.0044 | 0.0034 | +1.31 | 0.192 | 0.0039 | +1.14 | 0.255 | 0.0033 | +1.36 | 0.175 |
| C1 GBI | `debt_service_burden_lag2` | -0.0616 | 0.0545 | -1.13 | 0.258 | 0.0522 | -1.18 | 0.238 | 0.0459 | -1.34 | 0.179 |
| C3 Self-green | `Dem_Mayor` | -0.0004 | 0.0039 | -0.11 | 0.914 | 0.0037 | -0.11 | 0.909 | 0.0036 | -0.12 | 0.907 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0545 | 0.0254 | +2.15 | 0.032** | 0.0297 | +1.83 | 0.067* | 0.0254 | +2.15 | 0.031** |
| C3 Self-green | `npdes_formal_prior3yr_muni` | +0.0164 | 0.0070 | +2.36 | 0.018** | 0.0079 | +2.08 | 0.037** | 0.0066 | +2.48 | 0.013** |
| C3 Self-green | `reserve_ratio_lag2` | +0.0031 | 0.0029 | +1.05 | 0.293 | 0.0035 | +0.89 | 0.376 | 0.0029 | +1.08 | 0.279 |
| C3 Self-green | `debt_service_burden_lag2` | -0.0416 | 0.0482 | -0.86 | 0.389 | 0.0450 | -0.92 | 0.355 | 0.0426 | -0.97 | 0.330 |
| C5 NPDES×Party | `Dem_Mayor` | -0.0032 | 0.0046 | -0.71 | 0.479 | 0.0032 | -1.02 | 0.307 | 0.0056 | -0.58 | 0.559 |
| C5 NPDES×Party | `pres_dem_two_party_share_lag2` | +0.0518 | 0.0267 | +1.94 | 0.053* | 0.0297 | +1.75 | 0.081* | 0.0273 | +1.90 | 0.058* |
| C5 NPDES×Party | `npdes_formal_prior3yr_muni` | -0.0027 | 0.0052 | -0.53 | 0.597 | 0.0043 | -0.64 | 0.525 | 0.0048 | -0.58 | 0.564 |
| C5 NPDES×Party | `reserve_ratio_lag2` | +0.0046 | 0.0034 | +1.36 | 0.175 | 0.0039 | +1.18 | 0.239 | 0.0032 | +1.41 | 0.158 |
| C5 NPDES×Party | `debt_service_burden_lag2` | -0.0626 | 0.0543 | -1.15 | 0.248 | 0.0519 | -1.21 | 0.227 | 0.0455 | -1.38 | 0.169 |
| C5 NPDES×Party | `dem_x_npdes` | +0.0281 | 0.0146 | +1.92 | 0.055* | 0.0171 | +1.64 | 0.101 | 0.0153 | +1.83 | 0.067* |
| C6 Demonstration | `Dem_Mayor` | -0.0244 | 0.0092 | -2.66 | 0.008*** | 0.0125 | -1.95 | 0.051* | 0.0111 | -2.20 | 0.028** |
| C6 Demonstration | `pres_dem_two_party_share_lag2` | +0.0545 | 0.0253 | +2.15 | 0.032** | 0.0298 | +1.83 | 0.068* | 0.0254 | +2.15 | 0.032** |
| C6 Demonstration | `npdes_formal_prior3yr_muni` | +0.0164 | 0.0070 | +2.36 | 0.018** | 0.0079 | +2.07 | 0.039** | 0.0066 | +2.49 | 0.013** |
| C6 Demonstration | `reserve_ratio_lag2` | +0.0031 | 0.0029 | +1.05 | 0.294 | 0.0035 | +0.89 | 0.374 | 0.0029 | +1.07 | 0.283 |
| C6 Demonstration | `debt_service_burden_lag2` | -0.0444 | 0.0480 | -0.93 | 0.355 | 0.0453 | -0.98 | 0.326 | 0.0426 | -1.04 | 0.297 |
| C6 Demonstration | `dem_x_state_green_cum` | +0.0012 | 0.0005 | +2.67 | 0.008*** | 0.0006 | +1.92 | 0.055* | 0.0005 | +2.28 | 0.023** |

## Reading

### Coefficients where significance is attenuated by alternative clustering:
- **`dem_x_npdes` in C5 NPDES×Party:** significant under city clustering (p=0.055) but NOT under state clustering (p=0.101). SE inflates from 0.0146 to 0.0171.

* p<0.10, ** p<0.05, *** p<0.01.
