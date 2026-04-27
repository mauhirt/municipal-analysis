# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | +0.0004 | 0.0041 | +0.09 | 0.929 | 0.0034 | +0.11 | 0.915 | 0.0049 | +0.07 | 0.940 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0538 | 0.0249 | +2.16 | 0.031** | 0.0270 | +1.99 | 0.046** | 0.0253 | +2.12 | 0.034** |
| C1 GBI | `reserve_ratio_lag2` | +0.0041 | 0.0032 | +1.29 | 0.197 | 0.0036 | +1.14 | 0.255 | 0.0032 | +1.30 | 0.194 |
| C1 GBI | `debt_service_burden_lag2` | -0.0707 | 0.0532 | -1.33 | 0.184 | 0.0503 | -1.40 | 0.160 | 0.0446 | -1.58 | 0.113 |
| C3 Self-green | `Dem_Mayor` | +0.0001 | 0.0037 | +0.04 | 0.969 | 0.0034 | +0.04 | 0.967 | 0.0034 | +0.04 | 0.966 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0502 | 0.0232 | +2.16 | 0.031** | 0.0273 | +1.84 | 0.066* | 0.0236 | +2.13 | 0.033** |
| C3 Self-green | `reserve_ratio_lag2` | +0.0029 | 0.0028 | +1.03 | 0.304 | 0.0033 | +0.87 | 0.383 | 0.0028 | +1.04 | 0.298 |
| C3 Self-green | `debt_service_burden_lag2` | -0.0481 | 0.0450 | -1.07 | 0.285 | 0.0437 | -1.10 | 0.271 | 0.0398 | -1.21 | 0.226 |
| I1 Const×Party | `Dem_Mayor` | -0.0552 | 0.0292 | -1.89 | 0.059* | 0.0268 | -2.06 | 0.039** | 0.0280 | -1.97 | 0.048** |
| I1 Const×Party | `pres_dem_two_party_share_lag2` | +0.0040 | 0.0256 | +0.16 | 0.877 | 0.0223 | +0.18 | 0.859 | 0.0266 | +0.15 | 0.881 |
| I1 Const×Party | `reserve_ratio_lag2` | +0.0042 | 0.0031 | +1.35 | 0.177 | 0.0035 | +1.21 | 0.227 | 0.0031 | +1.37 | 0.171 |
| I1 Const×Party | `debt_service_burden_lag2` | -0.0757 | 0.0527 | -1.44 | 0.151 | 0.0505 | -1.50 | 0.134 | 0.0440 | -1.72 | 0.086* |
| I1 Const×Party | `dem_x_pres_dem` | +0.0986 | 0.0515 | +1.91 | 0.056* | 0.0472 | +2.09 | 0.037** | 0.0483 | +2.04 | 0.041** |
| I2 Const×Party | `Dem_Mayor` | -0.0633 | 0.0284 | -2.23 | 0.026** | 0.0271 | -2.33 | 0.020** | 0.0280 | -2.26 | 0.024** |
| I2 Const×Party | `pres_dem_two_party_share_lag2` | -0.0066 | 0.0220 | -0.30 | 0.763 | 0.0169 | -0.39 | 0.696 | 0.0225 | -0.29 | 0.769 |
| I2 Const×Party | `reserve_ratio_lag2` | +0.0030 | 0.0027 | +1.10 | 0.273 | 0.0032 | +0.95 | 0.344 | 0.0027 | +1.11 | 0.266 |
| I2 Const×Party | `debt_service_burden_lag2` | -0.0538 | 0.0442 | -1.22 | 0.224 | 0.0433 | -1.24 | 0.215 | 0.0392 | -1.37 | 0.170 |
| I2 Const×Party | `dem_x_pres_dem` | +0.1125 | 0.0500 | +2.25 | 0.024** | 0.0468 | +2.41 | 0.016** | 0.0491 | +2.29 | 0.022** |

## Reading

No coefficients change significance category across clustering schemes.

* p<0.10, ** p<0.05, *** p<0.01.
