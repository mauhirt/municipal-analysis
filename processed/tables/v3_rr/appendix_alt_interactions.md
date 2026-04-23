# Appendix — Alternative Interaction Specifications

Dem_Mayor (no lag), state+year FE, city-clustered SE.

| Variable | Ax1 Dem×Stress | Ax2 Stress² | Ax3 M2 Binary | Ax4 M3 City Bin | Ax5 M4 City Cnt |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.0014 (0.0040) | -0.0004 (0.0039) | -0.0159** (0.0077) | -0.0108** (0.0054) | -0.0004 (0.0039) |
| `npdes_formal_prior3yr_muni` | +0.0167** (0.0070) | +0.0164** (0.0069) | +0.0163** (0.0069) | +0.0169** (0.0070) | +0.0164** (0.0070) |
| `pres_dem_two_party_share_lag2` | +0.0529** (0.0259) | +0.0546** (0.0253) | +0.0535** (0.0253) | +0.0550** (0.0253) | +0.0545** (0.0254) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0003 (0.0003) | +0.0004 (0.0003) | -0.0002 (0.0004) | +0.0004 (0.0003) | +0.0004 (0.0003) |
| `reserve_ratio_lag2` | +0.0039 (0.0030) | +0.0031 (0.0029) | +0.0033 (0.0029) | +0.0030 (0.0029) | +0.0031 (0.0029) |
| `debt_service_burden_lag2` | -0.1450** (0.0579) | -0.0455 (0.0535) | -0.0431 (0.0482) | -0.0408 (0.0479) | -0.0416 (0.0482) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0085 (0.0055) | -0.0079 (0.0053) | -0.0069 (0.0054) | -0.0076 (0.0055) | -0.0078 (0.0053) |
| `dem_x_fiscal_stress` | +0.0212** (0.0083) | — | — | — | — |
| `fiscal_stress_sq` | — | +0.0006 (0.0036) | — | — | — |
| `state_any_prior_green_issuance_lag1` | — | — | +0.0033 (0.0087) | — | — |
| `dem_x_state_any_prior_green_issuance_lag1` | — | — | +0.0192** (0.0089) | — | — |
| `state_city_prior_green_issuance_lag1` | — | — | — | -0.0161** (0.0072) | — |
| `dem_x_state_city_prior_green_issuance_lag1` | — | — | — | +0.0212** (0.0087) | — |
| `state_city_count_prior_green_lag1` | — | — | — | — | — |
| `dem_x_state_city_count_prior_green_lag1` | — | — | — | — | — |
| N | 6698 | 6825 | 6825 | 6825 | 6825 |
| R² | 0.099 | 0.094 | 0.095 | 0.095 | 0.094 |

Controls included but not shown: `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`.

* p<0.10, ** p<0.05, *** p<0.01.

---

## Discarded interaction specifications

Three interaction terms were tested during the specification search and removed from the main table on diagnostic grounds. Each is documented here for the audit trail.

### Dem Mayor × NPDES formal enforcement (`dem_x_npdes`)

The interaction produced unstable signs across domains. On water-only outcomes, the Dem × NPDES interaction was +0.008 (t = 0.75, ns) — neither partisan group responded differently to water-specific compulsion. On non-water outcomes, the interaction was +0.019 (t = 2.18, p = 0.030), but the NPDES main effect simultaneously turned negative (−0.023, t = 1.75), producing a counterintuitive sign pattern: Republican mayors under high NPDES enforcement issued *fewer* non-water green bonds, while Democratic mayors were unaffected. Since NPDES is a water-specific regulation, a significant Dem × NPDES interaction on non-water bonds lacks a clean theoretical interpretation. The constituency × partisan interaction (`Dem_Mayor × pres_dem_share`) captures the partisan-conditional variation on non-water outcomes more cleanly and with a direct political-economy interpretation.

### Dem Mayor × state green bond market depth (`dem_x_state_green_cum`)

The interaction (`Dem_Mayor × asinh_state_all_green_cum_amt_lag1`) tested whether Democratic mayors follow existing state-level green-bond markets (a demonstration/imitation channel). The coefficient was +0.0011 (t = 2.65, p = 0.008) on `Y_self_green`, with a centered VIF of 1.14. Diagnostically, the interaction was robust. However, it tests the same underlying variation as `Dem_Mayor × pres_dem_two_party_share_lag2`: state green-bond market depth and county-level Democratic vote share are correlated (states with deep green markets are blue states), so both interactions capture whether the partisan effect depends on how green/blue the environment is. We retain `Dem × pres_dem_share` in the main table because the constituency variable has a direct political-economy interpretation (responsive representation) and the scale (county-level Dem vote share, 0 to 1) is transparent and comparable across specifications. The demonstration interaction is preserved in `demonstration_diagnostic.md` for readers interested in the market-maturity formulation.

### NPDES × state green bond market depth (`npdes_x_state_green`) — marketability interaction

The interaction tested whether NPDES compulsion drives green bond issuance only where the state ESG investor base exists (a marketability channel). On the pooled self-green outcome, the coefficient was +0.0016 (t = 1.79, p = 0.074). However, Task 10 diagnostics revealed three fragility flags. (1) Leave-one-state-out: dropping California halved the coefficient (from +0.0016 to +0.0007) and pushed p from 0.074 to 0.232; two additional states pushed p above 0.10. (2) Domain subsample: the interaction was not significant in either water-only (p = 0.19) or non-water (p = 0.12) when estimated on subsamples; the pooled significance derived from combining two individually-insignificant subsamples. (3) In contrast, the constituency × partisan interaction passed the same LOSO test with 0 of 49 states above p = 0.10. We retain the marketability interaction in Table 3 L3 (labelling margin, conditional on bond issuance, N = 3,888), where the coefficient is +0.0022 (t = 2.23, p = 0.026) on a separately-identified issuer subsample. Full diagnostics in `marketability_interaction_diagnostics.md` and `marketability_decision.md`.
