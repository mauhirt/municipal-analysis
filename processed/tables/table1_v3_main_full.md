# Table 1 v3 — Main 4 columns (FULL, all controls shown)

**Outcome × scale:** Any green bond / self-labelled, each as probability and asinh amount.
**PRIMARY_EXPANDED =** lean PRIMARY + `fiscal_stress_index_lag2` + `npdes × state_green_cum`.
**FE:** state + year. **SE:** clustered at city (fips7).

| Variable | C1 GBI | C2 GBI $ | C3 Self-green | C4 Self $ |
|---|---|---|---|---|
| *Treatment* | | | | |
| `Dem_Mayor` | +0.0001 (0.0044) | -0.0053 (0.0820) | -0.0015 (0.0039) | -0.0316 (0.0733) |
| *Constituency* | | | | |
| `pres_dem_two_party_share_lag2` | +0.0573** (0.0282) | +1.0626** (0.5363) | +0.0584** (0.0266) | +1.0657** (0.5066) |
| *Compulsion* | | | | |
| `npdes_formal_prior3yr_muni` | -0.0219 (0.0151) | -0.4557 (0.2998) | -0.0163 (0.0136) | -0.3517 (0.2682) |
| *Marketability (NPDES × state green)* | | | | |
| `npdes_x_state_green` | +0.0018* (0.0010) | +0.0375* (0.0201) | +0.0017* (0.0009) | +0.0343* (0.0180) |
| *Greenium-seeking (fiscal stress)* | | | | |
| `fiscal_stress_index_lag2` | +0.0195** (0.0081) | +0.3853** (0.1570) | +0.0157** (0.0073) | +0.3140** (0.1424) |
| *Fiscal capacity* | | | | |
| `reserve_ratio_lag2` | +0.0081** (0.0037) | +0.1450** (0.0688) | +0.0059* (0.0033) | +0.1103* (0.0612) |
| `debt_service_burden_lag2` | -0.2473** (0.0965) | -4.7341** (1.8535) | -0.1892** (0.0854) | -3.6914** (1.6453) |
| *Policy environment* | | | | |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0077 (0.0067) | -0.1462 (0.1295) | -0.0077 (0.0056) | -0.1454 (0.1062) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0002 (0.0005) | +0.0033 (0.0093) | +0.0001 (0.0005) | +0.0007 (0.0085) |
| *State politics* | | | | |
| `state_dem_governor_lag1` | +0.0026 (0.0132) | +0.0318 (0.2433) | +0.0012 (0.0119) | +0.0100 (0.2204) |
| `state_dem_trifecta_lag1` | -0.0132 (0.0119) | -0.2323 (0.2233) | -0.0098 (0.0114) | -0.1736 (0.2145) |
| `state_rep_trifecta_lag1` | -0.0082 (0.0129) | -0.1459 (0.2396) | -0.0052 (0.0120) | -0.0955 (0.2220) |
| *Demographics* | | | | |
| `log_population_city_lag2` | +0.0343*** (0.0088) | +0.6612*** (0.1740) | +0.0284*** (0.0080) | +0.5516*** (0.1590) |
| `log_percapita_income_city_lag2` | +0.0363** (0.0182) | +0.7301** (0.3716) | +0.0299* (0.0180) | +0.6123* (0.3662) |
| `unemployment_city_lag2` | +0.0033** (0.0016) | +0.0632** (0.0310) | +0.0029* (0.0015) | +0.0562** (0.0281) |
| N | 6477 | 6477 | 6477 | 6477 |
| R² | 0.102 | 0.107 | 0.102 | 0.106 |

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

Group labels in italics indicate the theoretical role; each listed variable is a separate regressor.
State and year fixed effects included (not shown).
