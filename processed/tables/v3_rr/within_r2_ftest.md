# Within-R² and Compulsion-Block F-Test (Task 8)

Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.
Cluster-robust SE at city level.

Compulsion block tested: npdes_formal_prior3yr_muni, reserve_ratio_lag2, debt_service_burden_lag2

| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |
|---|---|---|---|---|---|---|
| C1 GBI | `Green_Bond_Issued` | 6825 | 0.0007 | 1.47 | 0.2198 | 3 |
| C2 GBI amt | `asinh_green_amt` | 6825 | -0.0006 | 1.37 | 0.2505 | 3 |
| C3 Self-green | `Y_self_green` | 6825 | -0.0029 | 0.56 | 0.6433 | 3 |
| C4 Self amt | `asinh_self_green_amt` | 6825 | -0.0045 | 0.55 | 0.6461 | 3 |
| I1 Const×Party | `Green_Bond_Issued` | 6825 | 0.0042 | 1.44 | 0.2283 | 3 |
| I2 Const×Party | `Y_self_green` | 6825 | 0.0016 | 0.49 | 0.6891 | 3 |

Within-R² = variation explained after absorbing city and year FE.
F-test: joint null that all compulsion-block coefficients = 0.

* p<0.10, ** p<0.05, *** p<0.01.
