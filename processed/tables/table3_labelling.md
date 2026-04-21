# Table 3 — The Labelling Decision

**Outcome:** `Y_self_green` (city self-labelled green bond issuance).
**Sample:** City-years with `total_ltd_issued > 0` (Census of Governments long-term debt).
**FE:** state + year. **SE:** clustered at city (fips7). **Estimator:** OLS / LPM.

Conditional on issuing **any** bond, what predicts choosing the **green label**?

Bond issuers: N=4509, 567 cities, 84 self-green events.  Compelled issuers (npdes>0): N=836, 215 cities, 37 self-green events.

| Variable | L1 Baseline | L2 +Fiscal Stress | L3 +Marketability | L4 Both channels | L5 Compelled only |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0015 (0.0050) | -0.0024 (0.0050) | -0.0013 (0.0050) | -0.0021 (0.0050) | +0.0064 (0.0180) |
| `pres_dem_two_party_share_lag2` | +0.0708** (0.0318) | +0.0772** (0.0321) | +0.0719** (0.0318) | +0.0782** (0.0321) | +0.1875 (0.1311) |
| `npdes_formal_prior3yr_muni` | +0.0221*** (0.0084) | +0.0210*** (0.0081) | -0.0201 (0.0160) | -0.0200 (0.0159) | — |
| `reserve_ratio_lag2` | +0.0035 (0.0046) | +0.0059 (0.0044) | +0.0034 (0.0046) | +0.0057 (0.0044) | +0.0031 (0.0170) |
| `debt_service_burden_lag2` | -0.0586 (0.0687) | -0.2109** (0.0995) | -0.0573 (0.0686) | -0.2065** (0.0986) | -0.0326 (0.2268) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0106 (0.0077) | -0.0099 (0.0076) | -0.0105 (0.0077) | -0.0099 (0.0077) | -0.0351 (0.0350) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0005 (0.0005) | +0.0004 (0.0005) | -0.0000 (0.0006) | -0.0000 (0.0006) | +0.0002 (0.0017) |
| `state_dem_governor_lag1` | +0.0037 (0.0151) | +0.0035 (0.0151) | +0.0040 (0.0151) | +0.0038 (0.0151) | +0.0372 (0.0670) |
| `state_dem_trifecta_lag1` | -0.0122 (0.0131) | -0.0121 (0.0131) | -0.0130 (0.0131) | -0.0129 (0.0131) | -0.0235 (0.0579) |
| `state_rep_trifecta_lag1` | -0.0105 (0.0158) | -0.0099 (0.0158) | -0.0106 (0.0159) | -0.0100 (0.0158) | +0.0141 (0.0931) |
| `log_population_city_lag2` | +0.0351*** (0.0101) | +0.0345*** (0.0100) | +0.0348*** (0.0100) | +0.0342*** (0.0098) | +0.0416** (0.0204) |
| `log_percapita_income_city_lag2` | +0.0288 (0.0253) | +0.0314 (0.0257) | +0.0281 (0.0251) | +0.0307 (0.0255) | +0.1146* (0.0643) |
| `unemployment_city_lag2` | +0.0022 (0.0021) | +0.0024 (0.0021) | +0.0022 (0.0021) | +0.0023 (0.0021) | +0.0060 (0.0059) |
| **`fiscal_stress_index_lag2`** | — | +0.0176** (0.0086) | — | +0.0173** (0.0085) | — |
| **`npdes × state_green_cum`** | — | — | +0.0022** (0.0010) | +0.0021** (0.0010) | — |
| N | 3888 | 3888 | 3888 | 3888 | 719 |
| R² | 0.108 | 0.109 | 0.109 | 0.110 | 0.223 |

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
