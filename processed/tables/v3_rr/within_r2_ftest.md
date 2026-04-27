# Within-R² and Compulsion-Block F-Test (Task 8)

Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.
Cluster-robust SE at city level.

Compulsion block tested: qncr_nonsevere_asinh_lag1, reserve_ratio_lag2, debt_service_burden_lag2

| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |
|---|---|---|---|---|---|---|
| C1 GBI | `Green_Bond_Issued` | 7413 | -0.0006 | 2.66 | 0.0465** | 3 |
| C2 GBI amt | `asinh_green_amt` | 7413 | -0.0027 | 2.72 | 0.0428** | 3 |
| C3 Self-green | `Y_self_green` | 7413 | -0.0055 | 2.32 | 0.0729* | 3 |
| C4 Self amt | `asinh_self_green_amt` | 7413 | -0.0083 | 2.23 | 0.0820* | 3 |
| I1 Const×Party | `Green_Bond_Issued` | 7413 | -0.0010 | 2.57 | 0.0522* | 3 |
| I2 Const×Party | `Y_self_green` | 7413 | -0.0059 | 2.29 | 0.0759* | 3 |

Within-R² = variation explained after absorbing city and year FE.
F-test: joint null that all compulsion-block coefficients = 0.

* p<0.10, ** p<0.05, *** p<0.01.
