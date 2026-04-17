# Within-R² and Compulsion-Block F-Test (Task 8)

Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.
Cluster-robust SE at city level.

Compulsion block tested: npdes_formal_prior3yr_muni, overflow_events_lag2, reserve_ratio_lag2, debt_service_burden_lag2, tel_x_prop_tax_dep

| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |
|---|---|---|---|---|---|---|
| C1 GBI | `Green_Bond_Issued` | 5962 | 0.0075 | 3.24 | 0.0064*** | 5 |
| C2 GBI amt | `asinh_green_amt` | 5962 | 0.0080 | 3.22 | 0.0067*** | 5 |
| C3 Self-green | `Y_self_green` | 5962 | 0.0065 | 1.98 | 0.0780* | 5 |
| C4 Self amt | `asinh_self_green_amt` | 5962 | 0.0067 | 1.97 | 0.0798* | 5 |
| C5 NPDES×Party | `Green_Bond_Issued` | 5962 | 0.0075 | 2.94 | 0.0119** | 5 |
| C6 Overflow×Party | `Green_Bond_Issued` | 5962 | 0.0081 | 75.03 | 0.0000*** | 5 |
| C7 Demonstration | `Y_self_green` | 5962 | 0.0064 | 2.00 | 0.0754* | 5 |

Within-R² = variation explained after absorbing city and year FE.
F-test: joint null that all compulsion-block coefficients = 0.

* p<0.10, ** p<0.05, *** p<0.01.
