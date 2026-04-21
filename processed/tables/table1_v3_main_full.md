# Table 1 — Main spec (8 columns: each outcome with/without marketability interaction)

**Structure:** 4 outcome-scale combinations (GBI prob/amt, Self-green prob/amt), each run with and without the `npdes × state_green_cum` marketability interaction to show the NPDES main-effect flip.
**FE:** state + year. **SE:** clustered at city (fips7).

| Variable | C1 GBI | C2 GBI +int | C3 GBI $ | C4 GBI $ +int | C5 Self | C6 Self +int | C7 Self $ | C8 Self $ +int |
|---|---|---|---|---|---|---|---|---|
| **Family 1: Material (compulsion + fiscal)** | | | | | | | | |
| `npdes_formal_prior3yr_muni` — NPDES formal enforcement (prior 3 yrs) | +0.0159* (0.0082) | -0.0208 (0.0153) | +0.3195** (0.1594) | -0.4363 (0.3030) | +0.0180** (0.0073) | -0.0155 (0.0138) | +0.3542** (0.1432) | -0.3376 (0.2710) |
| `npdes_x_state_green` — NPDES × state green market depth *(interaction)* | — | +0.0018* (0.0010) | — | +0.0379* (0.0206) | — | +0.0017* (0.0009) | — | +0.0347* (0.0185) |
| `reserve_ratio_lag2` — Reserve ratio | +0.0046 (0.0035) | +0.0045 (0.0035) | +0.0768 (0.0651) | +0.0745 (0.0652) | +0.0032 (0.0030) | +0.0031 (0.0031) | +0.0554 (0.0573) | +0.0533 (0.0576) |
| `debt_service_burden_lag2` — Debt service burden | -0.0552 (0.0563) | -0.0547 (0.0563) | -0.9368 (1.0677) | -0.9261 (1.0681) | -0.0340 (0.0499) | -0.0335 (0.0499) | -0.5926 (0.9492) | -0.5828 (0.9484) |
| **Family 2: Political (partisan + constituency)** | | | | | | | | |
| `Dem_Mayor` — Dem mayor *(treatment)* | +0.0008 (0.0044) | +0.0009 (0.0044) | +0.0099 (0.0826) | +0.0110 (0.0826) | -0.0009 (0.0040) | -0.0009 (0.0040) | -0.0193 (0.0744) | -0.0183 (0.0743) |
| `pres_dem_two_party_share_lag2` — Dem presidential vote share (county) | +0.0502* (0.0281) | +0.0508* (0.0282) | +0.9221* (0.5348) | +0.9341* (0.5356) | +0.0526** (0.0266) | +0.0531** (0.0266) | +0.9498* (0.5054) | +0.9608* (0.5065) |
| **Family 3: State/Institutional** | | | | | | | | |
| `state_dem_governor_lag1` — Dem state governor | +0.0018 (0.0077) | +0.0017 (0.0077) | +0.0202 (0.1425) | +0.0177 (0.1427) | +0.0002 (0.0074) | +0.0000 (0.0074) | -0.0047 (0.1371) | -0.0070 (0.1374) |
| `fn_esg_has_muni_bond_law_post_lag1` — Anti-ESG muni bond law (post, lag 1) | -0.0063 (0.0066) | -0.0065 (0.0066) | -0.1207 (0.1265) | -0.1237 (0.1270) | -0.0067 (0.0053) | -0.0068 (0.0053) | -0.1255 (0.1015) | -0.1283 (0.1016) |
| `asinh_state_all_green_cum_amt_lag1` — State cumulative green bond amount | +0.0006 (0.0005) | +0.0003 (0.0005) | +0.0110 (0.0084) | +0.0045 (0.0093) | +0.0004 (0.0004) | +0.0001 (0.0004) | +0.0075 (0.0075) | +0.0016 (0.0084) |
| **Controls** | | | | | | | | |
| `log_population_city_lag2` — Log population | +0.0353*** (0.0091) | +0.0352*** (0.0090) | +0.6818*** (0.1798) | +0.6797*** (0.1783) | +0.0292*** (0.0082) | +0.0291*** (0.0082) | +0.5685*** (0.1639) | +0.5666*** (0.1626) |
| `log_percapita_income_city_lag2` — Log per-capita income | +0.0350* (0.0182) | +0.0343* (0.0180) | +0.7049* (0.3716) | +0.6894* (0.3668) | +0.0290 (0.0180) | +0.0283 (0.0178) | +0.5933 (0.3660) | +0.5791 (0.3614) |
| `unemployment_city_lag2` — Unemployment rate | +0.0031* (0.0016) | +0.0030* (0.0016) | +0.0602* (0.0312) | +0.0579* (0.0310) | +0.0027* (0.0015) | +0.0026* (0.0015) | +0.0540* (0.0284) | +0.0519* (0.0282) |
| N | 6477 | 6477 | 6477 | 6477 | 6477 | 6477 | 6477 | 6477 |
| R² | 0.098 | 0.099 | 0.103 | 0.104 | 0.100 | 0.100 | 0.103 | 0.104 |

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

State and year fixed effects absorbed. Odd-numbered columns (C1, C3, C5, C7) exclude the marketability interaction; even-numbered (C2, C4, C6, C8) include it. Compare paired columns to see the NPDES main effect flip sign/significance when the interaction is added.
