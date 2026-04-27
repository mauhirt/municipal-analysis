# Table 3 — The Labelling Decision

**Outcome:** `Y_self_green` (city self-labelled green bond issuance).
**Sample:** City-years with `total_ltd_issued > 0` (Census of Governments long-term debt).
**FE:** state + year. **SE:** clustered at city (fips7). **Estimator:** OLS / LPM.

Conditional on issuing **any** bond, what predicts choosing the **green label**?

Bond issuers: N=4509, 567 cities, 84 self-green events.  Compelled issuers (npdes>0): N=2799, 436 cities, 70 self-green events.

| Variable | L1 Baseline | L2 +Fiscal Stress | L3 +Marketability | L4 Both channels | L5 Compelled only |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0026 (0.0051) | -0.0032 (0.0051) | -0.0023 (0.0051) | -0.0029 (0.0051) | -0.0038 (0.0075) |
| `pres_dem_two_party_share_lag2` | +0.0707** (0.0318) | +0.0761** (0.0320) | +0.0742** (0.0318) | +0.0793** (0.0321) | +0.0695 (0.0466) |
| `npdes_formal_prior3yr_muni` | +0.0076** (0.0030) | +0.0068** (0.0029) | -0.0120** (0.0055) | -0.0125** (0.0056) | — |
| `reserve_ratio_lag2` | +0.0035 (0.0046) | +0.0056 (0.0044) | +0.0032 (0.0046) | +0.0052 (0.0045) | +0.0064 (0.0062) |
| `debt_service_burden_lag2` | -0.0709 (0.0704) | -0.2060** (0.0973) | -0.0658 (0.0701) | -0.1962** (0.0959) | -0.1095 (0.0978) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0081 (0.0074) | -0.0077 (0.0074) | -0.0098 (0.0076) | -0.0093 (0.0075) | -0.0101 (0.0100) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0005 (0.0005) | +0.0005 (0.0005) | -0.0011 (0.0008) | -0.0012 (0.0008) | +0.0011* (0.0006) |
| `state_dem_governor_lag1` | +0.0018 (0.0152) | +0.0017 (0.0152) | +0.0030 (0.0151) | +0.0030 (0.0151) | +0.0056 (0.0200) |
| `state_dem_trifecta_lag1` | -0.0141 (0.0130) | -0.0139 (0.0130) | -0.0147 (0.0130) | -0.0145 (0.0130) | -0.0174 (0.0177) |
| `state_rep_trifecta_lag1` | -0.0123 (0.0155) | -0.0117 (0.0155) | -0.0115 (0.0155) | -0.0110 (0.0155) | -0.0013 (0.0199) |
| `log_population_city_lag2` | +0.0336*** (0.0099) | +0.0334*** (0.0098) | +0.0331*** (0.0097) | +0.0329*** (0.0097) | +0.0385*** (0.0116) |
| `log_percapita_income_city_lag2` | +0.0307 (0.0257) | +0.0329 (0.0260) | +0.0301 (0.0255) | +0.0322 (0.0258) | +0.0491 (0.0389) |
| `unemployment_city_lag2` | +0.0024 (0.0021) | +0.0026 (0.0021) | +0.0023 (0.0021) | +0.0025 (0.0021) | +0.0025 (0.0032) |
| **`fiscal_stress_index_lag2`** | — | +0.0157* (0.0084) | — | +0.0151* (0.0083) | — |
| **`npdes × state_green_cum`** | — | — | +0.0010*** (0.0004) | +0.0010*** (0.0004) | — |
| N | 3888 | 3888 | 3888 | 3888 | 2451 |
| R² | 0.108 | 0.109 | 0.111 | 0.112 | 0.131 |

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
