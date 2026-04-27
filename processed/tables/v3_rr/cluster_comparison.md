# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | +0.0002 | 0.0041 | +0.05 | 0.963 | 0.0034 | +0.06 | 0.955 | 0.0048 | +0.04 | 0.968 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0547 | 0.0251 | +2.18 | 0.029** | 0.0273 | +2.00 | 0.045** | 0.0254 | +2.15 | 0.031** |
| C1 GBI | `reserve_ratio_lag2` | +0.0042 | 0.0032 | +1.32 | 0.187 | 0.0036 | +1.15 | 0.250 | 0.0031 | +1.36 | 0.175 |
| C1 GBI | `debt_service_burden_lag2` | -0.0687 | 0.0524 | -1.31 | 0.190 | 0.0510 | -1.35 | 0.178 | 0.0443 | -1.55 | 0.121 |
| C3 Self-green | `Dem_Mayor` | -0.0001 | 0.0037 | -0.02 | 0.984 | 0.0034 | -0.02 | 0.983 | 0.0033 | -0.02 | 0.982 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0514 | 0.0235 | +2.19 | 0.028** | 0.0276 | +1.86 | 0.062* | 0.0237 | +2.17 | 0.030** |
| C3 Self-green | `reserve_ratio_lag2` | +0.0030 | 0.0028 | +1.08 | 0.280 | 0.0033 | +0.91 | 0.363 | 0.0027 | +1.10 | 0.269 |
| C3 Self-green | `debt_service_burden_lag2` | -0.0471 | 0.0444 | -1.06 | 0.289 | 0.0445 | -1.06 | 0.290 | 0.0398 | -1.18 | 0.237 |
| I1 Const×Party | `Dem_Mayor` | -0.0559 | 0.0295 | -1.89 | 0.059* | 0.0273 | -2.05 | 0.040** | 0.0283 | -1.97 | 0.048** |
| I1 Const×Party | `pres_dem_two_party_share_lag2` | +0.0044 | 0.0255 | +0.17 | 0.862 | 0.0225 | +0.20 | 0.843 | 0.0265 | +0.17 | 0.867 |
| I1 Const×Party | `reserve_ratio_lag2` | +0.0043 | 0.0031 | +1.38 | 0.167 | 0.0035 | +1.22 | 0.222 | 0.0030 | +1.43 | 0.153 |
| I1 Const×Party | `debt_service_burden_lag2` | -0.0736 | 0.0519 | -1.42 | 0.157 | 0.0511 | -1.44 | 0.150 | 0.0438 | -1.68 | 0.093* |
| I1 Const×Party | `dem_x_pres_dem` | +0.0995 | 0.0519 | +1.92 | 0.055* | 0.0478 | +2.08 | 0.038** | 0.0488 | +2.04 | 0.041** |
| I2 Const×Party | `Dem_Mayor` | -0.0642 | 0.0287 | -2.23 | 0.025** | 0.0275 | -2.34 | 0.019** | 0.0282 | -2.28 | 0.023** |
| I2 Const×Party | `pres_dem_two_party_share_lag2` | -0.0061 | 0.0219 | -0.28 | 0.779 | 0.0171 | -0.36 | 0.719 | 0.0225 | -0.27 | 0.786 |
| I2 Const×Party | `reserve_ratio_lag2` | +0.0031 | 0.0027 | +1.15 | 0.249 | 0.0032 | +0.99 | 0.323 | 0.0026 | +1.18 | 0.238 |
| I2 Const×Party | `debt_service_burden_lag2` | -0.0526 | 0.0436 | -1.21 | 0.227 | 0.0441 | -1.19 | 0.233 | 0.0395 | -1.33 | 0.182 |
| I2 Const×Party | `dem_x_pres_dem` | +0.1139 | 0.0505 | +2.26 | 0.024** | 0.0472 | +2.41 | 0.016** | 0.0494 | +2.31 | 0.021** |

## Reading

No coefficients change significance category across clustering schemes.

* p<0.10, ** p<0.05, *** p<0.01.
