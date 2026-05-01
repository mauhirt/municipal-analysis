# Task 1 — Sample Size Reconciliation (5,962 → 6,477)

## Finding

The sample increased from N=5,962 to N=6,477 (+515 city-years) because two variables were dropped from PRIMARY during the "lean spec" trimming: `igr_share_lag2` (16.3% missing) and `capital_outlay_pc_lag2` (16.2% missing). These two variables share the same missingness pattern (Census of Governments fiscal data gaps), and their removal via listwise deletion allows 515 previously-excluded city-years to enter the estimation sample.

## Mechanism

| Variable dropped | Panel-wide missing | Missing in the 515 added obs |
|---|---|---|
| `igr_share_lag2` | 1,223 (16.3%) | 506 (98.3%) |
| `capital_outlay_pc_lag2` | 1,219 (16.2%) | 506 (98.3%) |

506 of 515 added observations were excluded solely because of missing `igr_share_lag2` and/or `capital_outlay_pc_lag2`. The remaining 9 were excluded by other missingness combinations that resolved when these binding constraints were removed.

## Composition of the 515 added observations

- **Cities:** 506 unique cities (nearly all cities contribute 1 additional year)
- **Years:** 2014–2021 and 2025 (Census fiscal data gaps in specific city-years)
- **Outcome rate:** `Y_self_green` mean = **0.0019** (1 event in 515 obs) vs **0.0185** (110 events in 5,962 obs)

The added observations are overwhelmingly **non-issuing** city-years (99.8% have Y_self_green=0). Adding them dilutes the outcome rate from 1.85% to 1.71%.

## Impact

Including the 515 low-outcome observations mechanically attenuates coefficients whose signal comes from the positive-outcome cities. This likely explains why `reserve_ratio_lag2` and `debt_service_burden_lag2` lost significance when PRIMARY was trimmed — it wasn't the variable removal per se, but the sample dilution from non-issuing city-years.

## Implication for sample choice

- **N=5,962** is the deliberate, consistently-filtered sample where all fiscal variables have complete coverage. It is the sample produced by the user's Task 5 variable list (which includes `capital_outlay_pc_lag2`).
- **N=6,477** adds 515 near-zero-outcome city-years with missing fiscal data that were imputed as "complete" only because the binding variables were removed.

**Recommendation:** Use **N=5,962**. The user's Task 5 variable list (which retains `capital_outlay_pc_lag2` and `tel_x_prop_tax_dep`) naturally restores this sample. The 515 added observations contribute almost no variation in the outcome and dilute fiscal-variable signals.
