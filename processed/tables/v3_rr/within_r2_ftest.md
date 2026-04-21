# Within-R² and Compulsion-Block F-Test (Task 8)

Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.
Cluster-robust SE at city level.

Compulsion block tested: npdes_formal_prior3yr_muni, reserve_ratio_lag2, debt_service_burden_lag2, tel_x_prop_tax_dep

| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |
|---|---|---|---|---|---|---|
| C1 GBI | `Green_Bond_Issued` | 6477 | 0.0050 | 0.98 | 0.4014 | 3 |
| C2 GBI amt | `asinh_green_amt` | 6477 | 0.0051 | 0.89 | 0.4444 | 3 |
| C3 Self-green | `Y_self_green` | 6477 | 0.0026 | 0.20 | 0.8964 | 3 |
| C4 Self amt | `asinh_self_green_amt` | 6477 | 0.0027 | 0.19 | 0.9006 | 3 |
| C5 NPDES×Party | `Green_Bond_Issued` | 6477 | 0.0051 | 0.52 | 0.6651 | 3 |
| C6 Demonstration | `Y_self_green` | 6477 | 0.0027 | 0.19 | 0.9061 | 3 |

Within-R² = variation explained after absorbing city and year FE.
F-test: joint null that all compulsion-block coefficients = 0.

* p<0.10, ** p<0.05, *** p<0.01.
