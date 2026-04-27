# Fiscal Stress Composite Construction

`fiscal_stress_composite_lag2` is a four-component z-score composite where higher values indicate greater combined fiscal stress.

## Construction

1. Standardize each component (z-score across the panel).
2. Flip sign on the two protective variables so higher = more stressed.
3. Sum the four standardized components.
4. Re-standardize the sum so the composite has mean 0, SD 1.

| Component | Sign | Rationale |
|---|---|---|
| `debt_service_burden_lag2` | + | Higher debt load = more stressed |
| `reserve_ratio_lag2` | − | Lower reserves = more stressed |
| `tel_x_prop_tax_dep` | + | TEL bite × property-tax dependence = revenue constraint binding |
| `charges_to_own_source_lag2` | − | Lower user-fee autonomy = more dependent on other revenue = more stressed |

## Component correlations (raw, signed)

```
                            debt_service_burden_lag2  reserve_ratio_lag2  tel_x_prop_tax_dep  charges_to_own_source_lag2
debt_service_burden_lag2                       1.000               0.302              -0.005                      -0.019
reserve_ratio_lag2                             0.302               1.000               0.030                       0.027
tel_x_prop_tax_dep                            -0.005               0.030               1.000                       0.057
charges_to_own_source_lag2                    -0.019               0.027               0.057                       1.000
```

## Distribution by mayor party

| Party | N | Mean | Median | p25 | p75 |
|---|---|---|---|---|---|
| Rep/Ind | 3217 | -0.124 | -0.098 | -0.784 | +0.547 |
| Dem | 4182 | +0.095 | +0.104 | -0.503 | +0.733 |

## Distribution by Census region

| Region | N | Mean | Median |
|---|---|---|---|
| Northeast | 931 | +0.817 | +0.759 |
| Midwest | 1943 | +0.056 | +0.174 |
| South | 2336 | -0.359 | -0.303 |
| West | 2189 | -0.014 | -0.037 |

Panel N = 7399 city-years with composite available.
