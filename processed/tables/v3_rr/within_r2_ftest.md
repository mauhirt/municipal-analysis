# Within-R² and Compulsion-Block F-Test (Task 8)

Estimated via `linearmodels.PanelOLS` with entity (city) + time (year) effects.
Cluster-robust SE at city level.

Compulsion block tested: npdes_formal_prior3yr_muni, reserve_ratio_lag2, debt_service_burden_lag2, tel_x_prop_tax_dep

| Column | Outcome | N | Within-R² | F-stat (compulsion block) | p-value | df |
|---|---|---|---|---|---|---|
| C1 GBI | `Green_Bond_Issued` | 5962 | 0.0065 | 2.21 | 0.0658* | 4 |
| C2 GBI amt | `asinh_green_amt` | 5962 | 0.0068 | 2.25 | 0.0613* | 4 |
| C3 Self-green | `Y_self_green` | 5962 | 0.0050 | 0.84 | 0.5024 | 4 |
| C4 Self amt | `asinh_self_green_amt` | 5962 | 0.0051 | 0.84 | 0.4974 | 4 |
| C5 NPDES×Party | `Green_Bond_Issued` | 5962 | 0.0065 | 2.08 | 0.0808* | 4 |
| C6 Demonstration | `Y_self_green` | 5962 | 0.0049 | 0.82 | 0.5106 | 4 |

Within-R² = variation explained after absorbing city and year FE.
F-test: joint null that all compulsion-block coefficients = 0.

* p<0.10, ** p<0.05, *** p<0.01.
