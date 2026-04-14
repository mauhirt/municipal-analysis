# TEL × city-level fiscal interactions — targeted test

Tests the two theoretically-motivated interactions of state-level `tel_stringency_normalized` with city-level fiscal variables (which provide the within-state-across-city identifying variation that TEL alone lacks).

- **tel × property_tax_dependence** — Mullins/Joyce revenue-substitution hypothesis. TELs bite on property-tax revenue; the effect should scale with how property-tax-dependent a city is.
- **tel × charges_to_own_source** — enterprise-fund escape-valve. Enterprise-fund charges (water/sewer) are exempt from TEL; deep enterprise funds let a city issue revenue-backed green bonds that bypass the property-tax-based TEL ceiling.

TEL main effect is dropped (absorbed by state FE in 48/49 states). Clustering is at `state_id` (not fips7) since TEL is state-level.

Specifications: state+year FE for T1 outcomes; year FE for T3 (issuer subsample).

| Spec | y | n | FE | β(tel×prop_tax_dep) | β(tel×charges) | β(Rep_Mayor) |
|---|---|---|---|---|---|---|
| A1 | Green_Bond_Issued | 5893 | state_id+year | +0.0042*** (se 0.0012) | — | -0.0028 (se 0.0054) |
| A2 | Green_Bond_Issued | 5893 | state_id+year | — | +0.0010 (se 0.0017) | -0.0026 (se 0.0054) |
| A3 | Green_Bond_Issued | 5893 | state_id+year | +0.0042*** (se 0.0012) | +0.0012 (se 0.0017) | -0.0031 (se 0.0057) |
| B1 | Y_self_green | 5893 | state_id+year | +0.0038*** (se 0.0011) | — | -0.0017 (se 0.0054) |
| B2 | Y_self_green | 5893 | state_id+year | — | +0.0012 (se 0.0013) | -0.0016 (se 0.0054) |
| B3 | Y_self_green | 5893 | state_id+year | +0.0038*** (se 0.0011) | +0.0014 (se 0.0013) | -0.0021 (se 0.0056) |
| C1 | Y_esg_assurance | 138 | year | +0.0049 (se 0.0041) | — | -0.2327** (se 0.1160) |
| C2 | Y_esg_assurance | 138 | year | — | +0.0064 (se 0.0081) | -0.2282* (se 0.1184) |
| C3 | Y_esg_assurance | 138 | year | +0.0068 (se 0.0093) | -0.0037 (se 0.0174) | -0.2339** (se 0.1143) |

Stars: * p<0.10, ** p<0.05, *** p<0.01. Cluster-robust SE at **state** level. Both interaction variables are continuous × continuous; signs are interpreted at the mean.
