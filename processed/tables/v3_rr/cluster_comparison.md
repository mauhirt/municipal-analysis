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
| I1 Const×Party | `Dem_Mayor` | -0.0569 | 0.0307 | -1.85 | 0.064* | 0.0275 | -2.07 | 0.039** | 0.0294 | -1.94 | 0.053* |
| I1 Const×Party | `pres_dem_two_party_share_lag2` | +0.0019 | 0.0257 | +0.08 | 0.940 | 0.0228 | +0.08 | 0.932 | 0.0272 | +0.07 | 0.943 |
| I1 Const×Party | `npdes_formal_prior3yr_muni` | +0.0140 | 0.0076 | +1.83 | 0.067* | 0.0081 | +1.72 | 0.086* | 0.0082 | +1.71 | 0.087* |
| I1 Const×Party | `reserve_ratio_lag2` | +0.0045 | 0.0033 | +1.35 | 0.177 | 0.0038 | +1.20 | 0.230 | 0.0032 | +1.42 | 0.157 |
| I1 Const×Party | `debt_service_burden_lag2` | -0.0667 | 0.0537 | -1.24 | 0.214 | 0.0518 | -1.29 | 0.198 | 0.0450 | -1.48 | 0.139 |
| I1 Const×Party | `dem_x_pres_dem` | +0.1019 | 0.0536 | +1.90 | 0.057* | 0.0481 | +2.12 | 0.034** | 0.0502 | +2.03 | 0.042** |
| I2 Const×Party | `Dem_Mayor` | -0.0654 | 0.0301 | -2.18 | 0.030** | 0.0284 | -2.30 | 0.021** | 0.0295 | -2.21 | 0.027** |
| I2 Const×Party | `pres_dem_two_party_share_lag2` | -0.0040 | 0.0231 | -0.17 | 0.863 | 0.0184 | -0.22 | 0.828 | 0.0239 | -0.17 | 0.867 |
| I2 Const×Party | `npdes_formal_prior3yr_muni` | +0.0159 | 0.0067 | +2.35 | 0.019** | 0.0076 | +2.10 | 0.036** | 0.0065 | +2.45 | 0.014** |
| I2 Const×Party | `reserve_ratio_lag2` | +0.0032 | 0.0029 | +1.10 | 0.270 | 0.0034 | +0.95 | 0.342 | 0.0028 | +1.14 | 0.255 |
| I2 Const×Party | `debt_service_burden_lag2` | -0.0473 | 0.0472 | -1.00 | 0.316 | 0.0440 | -1.08 | 0.282 | 0.0421 | -1.13 | 0.261 |
| I2 Const×Party | `dem_x_pres_dem` | +0.1155 | 0.0526 | +2.20 | 0.028** | 0.0490 | +2.36 | 0.018** | 0.0515 | +2.24 | 0.025** |

## Reading

No coefficients change significance category across clustering schemes.

* p<0.10, ** p<0.05, *** p<0.01.
