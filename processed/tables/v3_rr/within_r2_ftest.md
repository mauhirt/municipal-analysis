# Within-R² and Compulsion-Block F-Test (Task 8)

Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.
Cluster-robust SE at city level.

Compulsion block tested: effluent_muni_asinh_lag2, reserve_ratio_lag2, debt_service_burden_lag2

| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |
|---|---|---|---|---|---|---|
| C1 GBI | `Green_Bond_Issued` | 7401 | -0.0016 | 1.63 | 0.1808 | 3 |
| C2 GBI amt | `asinh_green_amt` | 7401 | -0.0038 | 1.67 | 0.1723 | 3 |
| C3 Self-green | `Y_self_green` | 7401 | -0.0062 | 2.01 | 0.1103 | 3 |
| C4 Self amt | `asinh_self_green_amt` | 7401 | -0.0091 | 2.05 | 0.1051 | 3 |
| I1 Const×Party | `Green_Bond_Issued` | 7401 | -0.0021 | 1.57 | 0.1943 | 3 |
| I2 Const×Party | `Y_self_green` | 7401 | -0.0066 | 1.99 | 0.1134 | 3 |

Within-R² = variation explained after absorbing city and year FE.
F-test: joint null that all compulsion-block coefficients = 0.

* p<0.10, ** p<0.05, *** p<0.01.
