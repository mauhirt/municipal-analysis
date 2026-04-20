# Clustering Comparison: City vs State vs Two-Way (Task 4)

Same coefficient estimated under three SE schemes:
- **(a) City-clustered** (baseline, 572 clusters)
- **(b) State-clustered** (49 clusters)
- **(c) Two-way city × year** (Cameron-Gelbach-Miller: V_city + V_year − V_HC0)

| Column | Variable | β | SE(city) | t | p | SE(state) | t | p | SE(2way) | t | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 GBI | `Dem_Mayor` | -0.0003 | 0.0048 | -0.06 | 0.954 | 0.0044 | -0.06 | 0.950 | 0.0060 | -0.05 | 0.963 |
| C1 GBI | `pres_dem_two_party_share_lag2` | +0.0577 | 0.0298 | +1.94 | 0.053* | 0.0317 | +1.82 | 0.069* | 0.0295 | +1.96 | 0.050* |
| C1 GBI | `npdes_formal_prior3yr_muni` | +0.0149 | 0.0083 | +1.80 | 0.072* | 0.0084 | +1.78 | 0.075* | 0.0085 | +1.75 | 0.081* |
| C1 GBI | `reserve_ratio_lag2` | +0.0076 | 0.0036 | +2.15 | 0.031** | 0.0038 | +2.02 | 0.043** | 0.0031 | +2.47 | 0.013** |
| C1 GBI | `debt_service_burden_lag2` | -0.1249 | 0.0656 | -1.90 | 0.057* | 0.0712 | -1.75 | 0.079* | 0.0611 | -2.04 | 0.041** |
| C3 Self-green | `Dem_Mayor` | -0.0019 | 0.0043 | -0.44 | 0.661 | 0.0044 | -0.43 | 0.669 | 0.0040 | -0.47 | 0.637 |
| C3 Self-green | `pres_dem_two_party_share_lag2` | +0.0593 | 0.0280 | +2.12 | 0.034** | 0.0308 | +1.92 | 0.055* | 0.0260 | +2.28 | 0.023** |
| C3 Self-green | `npdes_formal_prior3yr_muni` | +0.0177 | 0.0073 | +2.44 | 0.015** | 0.0078 | +2.26 | 0.024** | 0.0063 | +2.79 | 0.005*** |
| C3 Self-green | `reserve_ratio_lag2` | +0.0060 | 0.0030 | +2.02 | 0.043** | 0.0032 | +1.87 | 0.062* | 0.0029 | +2.04 | 0.042** |
| C3 Self-green | `debt_service_burden_lag2` | -0.1027 | 0.0588 | -1.75 | 0.081* | 0.0652 | -1.58 | 0.115 | 0.0616 | -1.67 | 0.095* |
| C5 NPDES×Party | `Dem_Mayor` | -0.0041 | 0.0051 | -0.79 | 0.430 | 0.0041 | -0.99 | 0.321 | 0.0060 | -0.68 | 0.499 |
| C5 NPDES×Party | `pres_dem_two_party_share_lag2` | +0.0558 | 0.0298 | +1.88 | 0.061* | 0.0314 | +1.78 | 0.075* | 0.0293 | +1.91 | 0.057* |
| C5 NPDES×Party | `npdes_formal_prior3yr_muni` | -0.0030 | 0.0058 | -0.52 | 0.603 | 0.0049 | -0.61 | 0.542 | 0.0051 | -0.59 | 0.557 |
| C5 NPDES×Party | `reserve_ratio_lag2` | +0.0078 | 0.0035 | +2.21 | 0.027** | 0.0038 | +2.07 | 0.038** | 0.0031 | +2.51 | 0.012** |
| C5 NPDES×Party | `debt_service_burden_lag2` | -0.1233 | 0.0652 | -1.89 | 0.058* | 0.0707 | -1.75 | 0.081* | 0.0609 | -2.03 | 0.043** |
| C5 NPDES×Party | `dem_x_npdes` | +0.0287 | 0.0149 | +1.92 | 0.055* | 0.0171 | +1.68 | 0.094* | 0.0149 | +1.92 | 0.055* |
| C6 Demonstration | `Dem_Mayor` | -0.0335 | 0.0142 | -2.36 | 0.018** | 0.0193 | -1.73 | 0.083* | 0.0203 | -1.65 | 0.100* |
| C6 Demonstration | `pres_dem_two_party_share_lag2` | +0.0596 | 0.0279 | +2.13 | 0.033** | 0.0311 | +1.92 | 0.055* | 0.0261 | +2.29 | 0.022** |
| C6 Demonstration | `npdes_formal_prior3yr_muni` | +0.0176 | 0.0072 | +2.44 | 0.015** | 0.0078 | +2.25 | 0.024** | 0.0063 | +2.79 | 0.005*** |
| C6 Demonstration | `reserve_ratio_lag2` | +0.0059 | 0.0029 | +2.01 | 0.045** | 0.0032 | +1.85 | 0.064* | 0.0030 | +2.00 | 0.046** |
| C6 Demonstration | `debt_service_burden_lag2` | -0.1054 | 0.0591 | -1.78 | 0.074* | 0.0660 | -1.60 | 0.110 | 0.0621 | -1.70 | 0.089* |
| C6 Demonstration | `dem_x_state_green_cum` | +0.0015 | 0.0007 | +2.32 | 0.020** | 0.0010 | +1.60 | 0.110 | 0.0009 | +1.66 | 0.097* |

## Reading

### Coefficients where significance is attenuated by alternative clustering:
- **`debt_service_burden_lag2` in C3 Self-green:** significant under city clustering (p=0.081) but NOT under state clustering (p=0.115). SE inflates from 0.0588 to 0.0652.
- **`debt_service_burden_lag2` in C6 Demonstration:** significant under city clustering (p=0.074) but NOT under state clustering (p=0.110). SE inflates from 0.0591 to 0.0660.
- **`dem_x_state_green_cum` in C6 Demonstration:** significant under city clustering (p=0.020) but NOT under state clustering (p=0.110). SE inflates from 0.0007 to 0.0010.

* p<0.10, ** p<0.05, *** p<0.01.
