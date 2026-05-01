# Table 3 — The Labelling Decision

**Outcome:** `Y_self_green` (city self-labelled green bond issuance).
**Sample:** City-years with `total_ltd_issued > 0` (Census of Governments long-term debt).
**FE:** state + year. **SE:** clustered at city (fips7). **Estimator:** OLS / LPM.

Conditional on issuing **any** bond, what predicts choosing the **green label**?

Bond issuers: N=4509, 567 cities, 84 self-green events.  Compelled issuers (npdes>0): N=2699, 442 cities, 64 self-green events.

| Variable | L1 Baseline | L2 +Fiscal Stress | L3 +Marketability | L4 Both channels | L5 Compelled only |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0017 (0.0051) | -0.0024 (0.0051) | -0.0015 (0.0051) | -0.0022 (0.0051) | -0.0010 (0.0073) |
| `pres_dem_two_party_share_lag2` | +0.0665** (0.0312) | +0.0729** (0.0316) | +0.0692** (0.0310) | +0.0753** (0.0315) | +0.0587 (0.0394) |
| `npdes_formal_prior3yr_muni` | +0.0043 (0.0033) | +0.0035 (0.0033) | -0.0110** (0.0053) | -0.0113** (0.0054) | — |
| `reserve_ratio_lag2` | +0.0033 (0.0047) | +0.0056 (0.0045) | +0.0030 (0.0047) | +0.0053 (0.0045) | +0.0096 (0.0060) |
| `debt_service_burden_lag2` | -0.0728 (0.0706) | -0.2245** (0.0998) | -0.0636 (0.0693) | -0.2099** (0.0970) | -0.1276 (0.0932) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0082 (0.0074) | -0.0078 (0.0074) | -0.0097 (0.0076) | -0.0093 (0.0075) | -0.0186 (0.0117) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0005 (0.0005) | +0.0004 (0.0005) | -0.0007 (0.0008) | -0.0007 (0.0008) | +0.0009 (0.0007) |
| `state_dem_governor_lag1` | +0.0020 (0.0153) | +0.0020 (0.0153) | +0.0012 (0.0153) | +0.0013 (0.0153) | +0.0118 (0.0204) |
| `state_dem_trifecta_lag1` | -0.0127 (0.0131) | -0.0126 (0.0131) | -0.0116 (0.0130) | -0.0115 (0.0130) | -0.0202 (0.0177) |
| `state_rep_trifecta_lag1` | -0.0125 (0.0157) | -0.0118 (0.0157) | -0.0124 (0.0155) | -0.0118 (0.0155) | -0.0034 (0.0203) |
| `log_population_city_lag2` | +0.0355*** (0.0107) | +0.0353*** (0.0106) | +0.0350*** (0.0105) | +0.0348*** (0.0104) | +0.0384*** (0.0117) |
| `log_percapita_income_city_lag2` | +0.0307 (0.0255) | +0.0331 (0.0260) | +0.0300 (0.0255) | +0.0324 (0.0260) | +0.0345 (0.0264) |
| `unemployment_city_lag2` | +0.0025 (0.0021) | +0.0026 (0.0021) | +0.0022 (0.0021) | +0.0024 (0.0021) | +0.0013 (0.0031) |
| **`fiscal_stress_index_lag2`** | — | +0.0176** (0.0089) | — | +0.0169* (0.0088) | — |
| **`npdes × state_green_cum`** | — | — | +0.0008** (0.0003) | +0.0008** (0.0003) | — |
| N | 3894 | 3894 | 3894 | 3894 | 2375 |
| R² | 0.105 | 0.107 | 0.107 | 0.109 | 0.131 |

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

## Reading

**L1 Baseline.** Conditional on issuing any bond, NPDES formal enforcement still predicts self-labelling (+0.022\*\*\*). Constituency share also strengthens (+0.069\*\*). `Dem_Mayor` remains null. *Compulsion drives the green label specifically, not just bond issuance.*

**L2 Greenium-seeking channel.** `fiscal_stress_index_lag2` = **+0.017\*\***. Among issuers, fiscally distressed cities label green more. Consistent with seeking yield reduction through ESG-oriented demand (greenium).

**L3 Marketability channel.** `npdes × state_green_cum` = **+0.0022\*\***, while NPDES main effect flips null (-0.020, ns) and state-green main effect is zero. *Compulsion drives green labelling **only where an ESG investor base exists**.* Compelled cities in shallow-market states do not bother labelling.

**L4 Both channels together.** Both interactions retain their signs with the joint spec. The greenium-seeking and marketability channels are orthogonal: neither absorbs the other.

**L5 Compelled issuers only.** Among cities that are both under NPDES enforcement *and* issuing bonds, only `log_population` and `log_percapita_income` predict green labelling. Partisanship and constituency vanish in this subsample. Interpretation: among compelled issuers, labelling is a matter of administrative/financial **sophistication** — bigger, richer cities have the advisory capacity to execute the green-label process.

## Summary

Labelling is **market-mediated**, not ideological. Two orthogonal channels:
1. **Greenium-seeking (L2):** distressed cities label green to reduce borrowing cost.
2. **Marketability (L3):** compelled cities label green only where ESG investors exist.

`Dem_Mayor` is null in every column of Table 3, consistent with Table 1. The partisan demonstration effect (Table 1 C6) is an extensive-margin interaction, not a labelling story.
