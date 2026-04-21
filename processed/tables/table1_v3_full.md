# Table 1 (v3) — Three-Family Specification

**Sample:** 6,477 city-years, 572 cities, 49 states, 2013–2025.
**Treatment:** `Dem_Mayor` (no lag). **FE:** state + year. **SE:** clustered at city (fips7).

**Structure.** Four main columns (two outcomes × two scales), one RHS, twelve regressors grouped into the paper's three theoretical families plus standard muni-finance controls. The single cross-family interaction (`npdes × state_green_cum`) tests the marketability channel.

---

## Main columns (C1–C4)

| Variable | C1 GBI | C2 GBI $ | C3 Self-green | C4 Self $ |
|---|---|---|---|---|
| **Family 1: Material** | | | | |
| `npdes_formal_prior3yr_muni` | -0.021 | -0.436 | -0.016 | -0.338 |
| `npdes × state_green_cum` | **+0.0018\*** | **+0.038\*** | **+0.0017\*** | **+0.035\*** |
| `reserve_ratio_lag2` | +0.005 | +0.075 | +0.003 | +0.053 |
| `debt_service_burden_lag2` | -0.055 | -0.926 | -0.034 | -0.583 |
| **Family 2: Political** | | | | |
| `Dem_Mayor` | +0.001 | +0.011 | -0.001 | -0.018 |
| `pres_dem_two_party_share_lag2` | **+0.051\*** | **+0.934\*** | **+0.053\*\*** | **+0.961\*** |
| **Family 3: State/Institutional** | | | | |
| `state_dem_governor_lag1` | +0.002 | +0.018 | +0.000 | -0.007 |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.007 | -0.124 | -0.007 | -0.128 |
| `asinh_state_all_green_cum_amt_lag1` | +0.000 | +0.005 | +0.000 | +0.002 |
| N | 6,477 | 6,477 | 6,477 | 6,477 |
| R² | 0.099 | 0.104 | 0.100 | 0.104 |

Controls not shown: `log_population_city_lag2`\*\*\*, `log_percapita_income_city_lag2`\*, `unemployment_city_lag2`\*. Full version with all controls: `table1_v3_main_full.md`. Stars: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

### Reading by family

**Family 1 — Material.** NPDES compulsion operates *through the marketability interaction*. The interaction `npdes × state_green_cum` is significant (\*) on all four outcomes; the NPDES main effect flips null once the interaction is in. Reading: compelled cities issue and label green where an ESG investor base exists, not otherwise. Reserve ratio and debt service burden are directional but not individually significant in this spec.

**Family 2 — Political.** `Dem_Mayor` is null across all four columns — **H1b holds**. Constituency (`pres_dem_two_party_share_lag2`) is robustly positive (\*–\*\*) across all outcomes — the partisan signal operates through the electorate, not the mayor.

**Family 3 — State/Institutional.** All three variables are null in the main spec. State FE absorb most variation; what remains (governor party changes, anti-ESG laws, state green cum) does not operate as a main effect once Family 1 and Family 2 are in. The anti-ESG law story surfaces in the R17 endogeneity robustness column — see below.

---

## Partisan interactions (complement to main table)

Three specs testing whether the `Dem_Mayor` null hides a conditional partisan margin.

| Variable | I1 NPDES×Party (GBI) | I2 NPDES×Party (Self) | I3 Demonstration (Self) |
|---|---|---|---|
| `Dem_Mayor` | -0.004 | -0.005 | **-0.024\*\*\*** |
| `dem_x_npdes` | **+0.031\*\*** | **+0.027\*** | — |
| `dem_x_state_green_cum` | — | — | **+0.0011\*\*\*** |

**Reading.**
- **NPDES × Party.** Dem mayors are slightly more responsive to NPDES compulsion than Rep mayors (+0.031\*\*). Main-effect `Dem_Mayor` stays null.
- **Demonstration.** Once `Dem × state_green_cum` is added, `Dem_Mayor` turns −0.024\*\*\* with interaction +0.0011\*\*\*. Dem mayors respond to existing state markets (imitation), not autonomously.

---

## Robustness R1–R10 (on `Y_self_green`)

Full coefficients in `table1_v3_rob1.md`. `Dem_Mayor` null across all 10 specs. Notable: IRA GGRF and FEMA resilience grants negative; state ZEV mandate strongly negative (\*\*\*); RGGI and C40 weakly positive.

## Robustness R11–R24 (on `Y_self_green`)

Full coefficients in `table1_v3_rob2.md`. `Dem_Mayor` null across all 14 specs (range -0.002 to +0.027).

| Spec | β(Dem_Mayor) | Notable extras |
|---|---|---|
| R11 CAA nonattainment | -0.001 | ozone ns |
| R12 Water ladder (informal+violations+JDC) | -0.002 | water_violations weakly + |
| R13–R16 Gravity (peer/special/county/all) | -0.001 | all ns — no spatial spillover |
| R17 ESG endogeneity | -0.001 | **`state_pre_esg_activity` +0.064\*\*\*** |
| R18 Rep_Mayor mirror | — | confirms null |
| R19 FOG × Dem | +0.027 | ns |
| R20 NPDES Locgov | -0.001 | **`_locgov` +0.014\*\*** |
| R21 NPDES Private placebo | -0.000 | ns (wrong sign) |
| R22 Kitchen-sink (+all dropped vars) | -0.002 | confirms drop was inert |
| **R23 Fiscal stress composite** | -0.001 | composite replaces components |
| **R24 State trifectas** | -0.001 | trifecta dummies ns |

**R22 Kitchen-sink** includes all previously-dropped variables (`charges_to_own_source`, `igr_share`, `tel_x_prop_tax_dep`, `capital_outlay_pc`, `has_substitute_issuer`, state trifectas, `fiscal_stress_index`). `Dem_Mayor` still null; confirms the trimmed main spec loses no information.

**R23 Fiscal stress composite** replaces reserve + debt_service with the composite `fiscal_stress_index_lag2`. Alternative greenium-story framing, available if reviewer requests.

**R24 State trifectas** adds `state_dem_trifecta_lag1` + `state_rep_trifecta_lag1` alongside `state_dem_governor_lag1`. All null — confirms governor alone is sufficient state-political control.

---

## Summary

| Finding | Evidence | Strength |
|---|---|---|
| **H1b: Dem_Mayor null across outcomes** | β ≈ 0 across C1–C4 + R1–R24 | \*\*\* Rock solid (27 specs) |
| **Constituency drives issuance** | pres_dem +0.051\* to +0.053\*\* | \*–\*\* Consistent |
| **Marketability channel** | npdes × state_green +0.0018\*, +0.0017\* | \* Novel |
| **Demonstration (conditional partisan)** | I3 Dem_Mayor -0.024\*\*\*, interaction +0.0011\*\*\* | \*\*\* Novel |
| **NPDES × Party interaction** | I1 dem_x_npdes +0.031\*\* | \*\* Conditional partisan |
| **Pre-ESG-law market** | R17: state_pre_esg_activity +0.064\*\*\* | \*\*\* Confirmed |
| **NPDES effect ownership-specific** | R20 _locgov +0.014\*\*, R21 _private null | \*\* Placebo clean |

---

## The story

**Partisan ideology does not drive green bond issuance.** `Dem_Mayor` is null across all outcomes and every robustness column (27 specs total).

**The engine is material + political interacting with institutional.**
- **Family 1 (Material)**: Compulsion matters *where ESG markets exist* — the marketability interaction is the active channel.
- **Family 2 (Political)**: Constituency matters; mayoral agency does not.
- **Family 3 (Institutional)**: No main effects once Family 1 is in; the pre-ESG-law endogeneity result (R17) carries the institutional story.

**The partisan signal, where it appears, is conditional.** Dem mayors respond to NPDES compulsion (I1) and to existing state green markets (I3 demonstration). They don't create markets; they amplify on top of them.

---

## Files

```
processed/tables/
├── table1_v3_full.md                ← this document
├── table1_v3_main.md                ← C1–C4 main table
├── table1_v3_main_full.md           ← C1–C4 with ALL controls visible, family-grouped
├── table1_v3_interactions.md        ← Partisan interactions I1–I3
├── table1_v3_rob1.md                ← R1–R10 robustness
├── table1_v3_rob2.md                ← R11–R24 robustness
├── table3_labelling.md              ← Labelling decision (issuer subsample)
└── v3_rr/                           ← R&R supplementary package (Tasks 2–8)
```

Reproduce: `TABLE1_MODULE=all python3 pipeline/analysis_table1_v3.py`
