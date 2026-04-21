# Table 1 — Main spec (three families + marketability interaction, all controls shown)

**Outcomes × scales:** Green_Bond_Issued / asinh_green_amt / Y_self_green / asinh_self_green_amt.
**Structure:** 12 regressors grouped into three theoretical families + standard controls.
**FE:** state + year. **SE:** clustered at city (fips7).

| Variable | C1 GBI | C2 GBI $ | C3 Self-green | C4 Self $ |
|---|---|---|---|---|
| **Family 1: Material (compulsion + fiscal)** | | | | |
| `npdes_formal_prior3yr_muni` — NPDES formal enforcement (prior 3 yrs) | -0.0208 (0.0153) | -0.4363 (0.3030) | -0.0155 (0.0138) | -0.3376 (0.2710) |
| `npdes_x_state_green` — NPDES × state green market depth *(interaction)* | +0.0018* (0.0010) | +0.0379* (0.0206) | +0.0017* (0.0009) | +0.0347* (0.0185) |
| `reserve_ratio_lag2` — Reserve ratio | +0.0045 (0.0035) | +0.0745 (0.0652) | +0.0031 (0.0031) | +0.0533 (0.0576) |
| `debt_service_burden_lag2` — Debt service burden | -0.0547 (0.0563) | -0.9261 (1.0681) | -0.0335 (0.0499) | -0.5828 (0.9484) |
| **Family 2: Political (partisan + constituency)** | | | | |
| `Dem_Mayor` — Dem mayor *(treatment)* | +0.0009 (0.0044) | +0.0110 (0.0826) | -0.0009 (0.0040) | -0.0183 (0.0743) |
| `pres_dem_two_party_share_lag2` — Dem presidential vote share (county) | +0.0508* (0.0282) | +0.9341* (0.5356) | +0.0531** (0.0266) | +0.9608* (0.5065) |
| **Family 3: State/Institutional** | | | | |
| `state_dem_governor_lag1` — Dem state governor | +0.0017 (0.0077) | +0.0177 (0.1427) | +0.0000 (0.0074) | -0.0070 (0.1374) |
| `fn_esg_has_muni_bond_law_post_lag1` — Anti-ESG muni bond law (post, lag 1) | -0.0065 (0.0066) | -0.1237 (0.1270) | -0.0068 (0.0053) | -0.1283 (0.1016) |
| `asinh_state_all_green_cum_amt_lag1` — State cumulative green bond amount | +0.0003 (0.0005) | +0.0045 (0.0093) | +0.0001 (0.0004) | +0.0016 (0.0084) |
| **Controls** | | | | |
| `log_population_city_lag2` — Log population | +0.0352*** (0.0090) | +0.6797*** (0.1783) | +0.0291*** (0.0082) | +0.5666*** (0.1626) |
| `log_percapita_income_city_lag2` — Log per-capita income | +0.0343* (0.0180) | +0.6894* (0.3668) | +0.0283 (0.0178) | +0.5791 (0.3614) |
| `unemployment_city_lag2` — Unemployment rate | +0.0030* (0.0016) | +0.0579* (0.0310) | +0.0026* (0.0015) | +0.0519* (0.0282) |
| N | 6477 | 6477 | 6477 | 6477 |
| R² | 0.099 | 0.104 | 0.100 | 0.104 |

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

State and year fixed effects absorbed (not shown).
