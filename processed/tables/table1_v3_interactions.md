# Table 1 v3 — Partisan interactions (complement to main table)

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | I1 NPDES×Party | I2 NPDES×Party Self | I3 Demonstration | I4 Demonstration Water |
|---|---|---|---|---|
| `Dem_Mayor` | -0.0041 (0.0047) | -0.0052 (0.0042) | -0.0241*** (0.0089) | +0.0003 (0.0074) |
| `pres_dem_two_party_share_lag2` | +0.0554** (0.0280) | +0.0567** (0.0264) | +0.0583** (0.0266) | +0.0167 (0.0181) |
| `npdes_formal_prior3yr_muni` | -0.0414** (0.0207) | -0.0333* (0.0183) | -0.0134 (0.0131) | -0.0076 (0.0091) |
| `reserve_ratio_lag2` | +0.0084** (0.0037) | +0.0062* (0.0032) | +0.0059* (0.0033) | +0.0049* (0.0028) |
| `debt_service_burden_lag2` | -0.2559*** (0.0985) | -0.1966** (0.0871) | -0.1909** (0.0855) | -0.1043* (0.0570) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0083 (0.0067) | -0.0082 (0.0055) | -0.0069 (0.0056) | -0.0103* (0.0061) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0002 (0.0005) | +0.0001 (0.0004) | -0.0006 (0.0005) | +0.0003 (0.0004) |
| `state_dem_governor_lag1` | +0.0026 (0.0131) | +0.0011 (0.0119) | +0.0009 (0.0120) | -0.0006 (0.0108) |
| `state_dem_trifecta_lag1` | -0.0131 (0.0118) | -0.0097 (0.0114) | -0.0099 (0.0115) | -0.0048 (0.0093) |
| `state_rep_trifecta_lag1` | -0.0082 (0.0129) | -0.0053 (0.0120) | -0.0050 (0.0120) | -0.0064 (0.0093) |
| `fiscal_stress_index_lag2` | +0.0203** (0.0082) | +0.0164** (0.0074) | +0.0156** (0.0073) | +0.0060 (0.0042) |
| `npdes_x_state_green` | +0.0018* (0.0010) | +0.0017* (0.0009) | +0.0015* (0.0009) | +0.0008 (0.0006) |
| `dem_x_npdes` | +0.0307** (0.0151) | +0.0267* (0.0138) | — | — |
| `dem_x_state_green_cum` | — | — | +0.0011*** (0.0004) | -0.0000 (0.0003) |
| N | 6477 | 6477 | 6477 | 6477 |
| R² | 0.103 | 0.104 | 0.103 | 0.051 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.
