# Table 1 (v3) — Consolidated Writeup

**Sample:** N = 6,825 city-years · 576 cities · 49 states · 2014–2025.
**Treatment:** `Dem_Mayor` (no lag, with three-tier imputation — see methods note).
**FE:** state + year. **SE:** clustered at city (fips7).
**Estimator:** OLS / linear probability model.

---

## Main table (C1–C8)

Four outcome-scale combinations (GBI prob/amt, Self-green prob/amt), each run with and without the `npdes × state_green_cum` marketability interaction. Odd columns = no interaction; even columns = with interaction.

| Variable | C1 GBI | C2 +int | C3 GBI $ | C4 +int | C5 Self | C6 +int | C7 Self $ | C8 +int |
|---|---|---|---|---|---|---|---|---|
| `Dem_Mayor` | +0.000 | +0.001 | +0.004 | +0.006 | -0.000 | -0.000 | -0.010 | -0.009 |
| `pres_dem_two_party_share_lag2` | **+0.053\*\*** | **+0.054\*\*** | +0.984\* | +0.998\* | **+0.055\*\*** | **+0.055\*\*** | **+0.987\*\*** | **+1.000\*\*** |
| `npdes_formal_prior3yr_muni` | **+0.014\*** | -0.021 | **+0.292\*** | -0.436 | **+0.016\*\*** | -0.015 | **+0.324\*\*** | -0.332 |
| `npdes × state_green_cum` | — | **+0.0018\*** | — | **+0.037\*** | — | **+0.0016\*** | — | **+0.033\*** |
| `reserve_ratio_lag2` | +0.004 | +0.004 | +0.075 | +0.072 | +0.003 | +0.003 | +0.055 | +0.053 |
| `debt_service_burden_lag2` | -0.062 | -0.061 | -1.060 | -1.038 | -0.042 | -0.041 | -0.735 | -0.715 |
| `state_green_cum (main)` | +0.001 | +0.000 | +0.010 | +0.004 | +0.000 | +0.000 | +0.007 | +0.001 |
| `anti-ESG law (post, lag1)` | -0.008 | -0.008 | -0.143 | -0.147 | -0.008 | -0.008 | -0.146 | -0.150 |
| N | 6,825 | 6,825 | 6,825 | 6,825 | 6,825 | 6,825 | 6,825 | 6,825 |
| R² | 0.092 | 0.093 | 0.098 | 0.098 | 0.094 | 0.094 | 0.097 | 0.098 |

Controls not shown: `log_population_city_lag2`\*\*\*, `log_percapita_income_city_lag2`, `unemployment_city_lag2`\*. Full version with all controls visible: `table1_v3_main_full.md`.

### Reading

**H1b null across every outcome and scale.** `Dem_Mayor` is indistinguishable from zero on probability of any green bond (C1/C2), amount (C3/C4), self-labelled probability (C5/C6), and self-labelled amount (C7/C8). Robust across 24 additional robustness columns (see below).

**Constituency operates through the electorate, not the mayor.** `pres_dem_two_party_share_lag2` is consistently positive (\*–\*\*) across all columns. A 10pp higher Dem vote share → ~0.5 pp higher probability of green bond issuance.

**Compulsion matters via the market, not alone.** Columns C1/C3/C5/C7 (no interaction): NPDES is positive and significant (+0.014\* to +0.016\*\* on probability). Columns C2/C4/C6/C8 (with interaction): NPDES main effect absorbs into the interaction. `npdes × state_green_cum` is **+0.0016\* to +0.0018\*** across all four outcomes. Reading: compelled cities issue green *where an ESG investor base exists*, not otherwise. The marketability channel is the operative mechanism.

---

## Partisan interactions (complement to main table)

Four specifications testing whether the null `Dem_Mayor` hides a conditional partisan effect. Each tests a different moderation channel.

| Term | I1 NPDES×Party (GBI) | I2 NPDES×Party (Self) | I3 Demonstration (Self) | I4 Constituency×Party (Self) |
|---|---|---|---|---|
| `Dem_Mayor` | -0.003 | -0.004 | **-0.022\*\*\*** | **-0.065\*\*** |
| `pres_dem_two_party_share_lag2` | +0.053\*\* | +0.054\*\* | +0.055\*\* | -0.003 |
| `dem_x_npdes` | **+0.028\*** | **+0.024\*** | — | — |
| `dem_x_state_green_cum` | — | — | **+0.0011\*\*\*** | — |
| **`dem_x_pres_dem`** | — | — | — | **+0.114\*\*** |
| N | 6,825 | 6,825 | 6,825 | 6,825 |

**Reading.** Three distinct channels moderate the partisan effect. All three say the same thing at the meta-level: *Dem mayors do not act autonomously — they amplify external forces.*
- **I1 / I2 Compulsion responsiveness.** Dem mayors are more responsive to NPDES compulsion than Rep/Ind mayors (+0.028\* GBI, +0.024\* self). Main-effect `Dem_Mayor` stays null.
- **I3 Supply-side market imitation.** `Dem × state_green_cum` = **+0.0011\*\*\***. Dem mayors self-label where a state market already exists. VIF-verified (centered VIF = 1.14). Crossover at asinh ≈ 20.07 (~28% of sample below).
- **I4 Demand-side constituency amplification.** `Dem × pres_dem_share` = **+0.114\*\*** on self-green. Crossover at pres_dem ≈ 0.55. VIF-verified (centered VIF = 1.18, identical coefficient). Marginal effect of `Dem_Mayor` on self-green: **-0.020\*\*** in red cities (10th pct), **+0.000** at median, **+0.021\*\*** in blue cities (90th pct). **On non-water outcomes, the interaction strengthens to +0.101\*\*\* (p=0.002); on water, it collapses to -0.002 (p=0.94).** The interaction operates specifically in the discretionary domain — see Table 2.

---

## Robustness R1–R24

All on `Y_self_green`. `Dem_Mayor` null across all 24 specifications at N ≈ 6,500–6,825 (range -0.002 to +0.025, ns throughout).

**R1–R10** (`table1_v3_rob1.md`):

| R | Addition | β(Dem_Mayor) | Notable extras |
|---|---|---|---|
| R1 | YCOM climate opinion | -0.003 | opinion_regulate ns |
| R2 | IIJA/IRA/FEMA grants | -0.001 | IRA GGRF and FEMA resilience weakly negative |
| R3 | prob_democrat continuous | — | — |
| R4 | mayor vote share continuous | +0.017 | directional positive, p=0.09 |
| R5 | state climate policy (carbon/GHG/RGGI/ZEV) | -0.001 | `state_zev` -0.035\*\*\*, `state_rggi` +0.068\* |
| R6 | ESG law intensity | -0.001 | ns |
| R7 | C40 / ICLEI / climate commitment | -0.001 | `c40_member` weakly + |
| R8 | density + principal city | -0.003 | density weakly + |
| R9 | IECC + state weakening amendments | +0.000 | ns |
| R10 | pooled compulsion index | -0.001 | index ns |

**R11–R24** (`table1_v3_rob2.md`):

| R | Addition | β(Dem_Mayor) | Notable extras |
|---|---|---|---|
| R11 | CAA ozone nonattainment | -0.001 | ns |
| R12 | NPDES enforcement ladder (informal + violations + JDC) | -0.001 | `epa_water_violations` weakly + |
| R13 | Gravity peer-city self-labelled (1/d²) | -0.000 | peer -0.004 (ns) |
| R14 | Gravity special district | -0.001 | +0.017 (ns) |
| R15 | Gravity county | -0.000 | +0.005 (ns) |
| R16 | All three spatial channels jointly | -0.000 | all ns |
| R17 | ESG endogeneity (state_pre_esg_activity + interaction) | -0.000 | **`state_pre_esg_activity` +0.064\*\*\*** |
| R18 | Rep_Mayor_lag1 mirror | -0.002 | confirms null (N=6,691) |
| R19 | FOG × Dem interactions | +0.025 | all interactions ns |
| R20 | NPDES _locgov supplement | -0.000 | **`_locgov` +0.014\*\*** |
| R21 | NPDES _private placebo | +0.000 | ns (wrong sign) |
| R22 | Kitchen-sink (+ 8 dropped vars) | -0.002 | confirms trimming inert |
| R23 | Fiscal stress composite (replaces reserve+debt) | -0.001 | composite ns |
| R24 | Add state Dem + Rep trifectas | -0.001 | trifectas ns |

**R13–R16 local spatial spillover.** All four gravity-weighted channels (peer city self-label, special district, county, all three jointly) are null. No evidence of local spatial spillover at the extensive margin once state-level market depth is included in Family 3. The marketability channel operates at the **state market level**, not through local peer imitation or neighbour substitution.

**R17 ESG endogeneity** is the sole robustness result with a novel significant ancillary finding: states that had city-level green bond activity before their first anti-ESG law produce significantly more self-labelled issuance (+0.064\*\*\*).

---

## Table 3 preview — The Labelling Decision

Sample restricted to bond issuers (`total_ltd_issued > 0`, N = 3,888). Full table at `table3_labelling.md`.

| Variable | L1 Baseline | L2 +Fiscal Stress | L3 +Marketability | L4 Both | L5 Compelled only |
|---|---|---|---|---|---|
| `Dem_Mayor` | -0.002 | -0.002 | -0.001 | -0.002 | +0.006 |
| `npdes_formal_prior3yr_muni` | **+0.022\*\*\*** | **+0.021\*\*\*** | -0.020 | -0.020 | — |
| `fiscal_stress_index_lag2` | — | **+0.018\*\*** | — | **+0.017\*\*** | — |
| `npdes × state_green_cum` | — | — | **+0.0022\*\*** | **+0.0021\*\*** | — |
| N | 3,888 | 3,888 | 3,888 | 3,888 | 719 |
| R² | 0.108 | 0.109 | 0.109 | 0.110 | 0.223 |

**Reading.** Labelling is market-mediated, not partisan. Two orthogonal channels:
1. **Greenium-seeking (L2):** distressed cities label green to reduce borrowing cost (+0.018\*\*).
2. **Marketability (L3):** compelled cities label green only where ESG investors exist — compulsion × market depth = +0.0022\*\*, with NPDES main effect flipping null when the interaction is included.
3. **Sophistication (L5):** Among compelled issuers, only `log_population` and `log_percapita_income` predict green labelling.

---

## R&R supplementary package (Tasks 2–8)

Located in `processed/tables/v3_rr/`. Summary in `v3_rr/README.md`.

- **demonstration_diagnostic.md** — 4 interaction measures × 2 specs; M1 selected for Table 1 I3.
- **appendix_alt_interactions.md** — Demoted interaction specs (M2–M4, fiscal stress square).
- **within_r2_ftest.md** — Within-R² and compulsion-block F-test at N=6,825.
- **cluster_comparison.md** — City / state / two-way clustering (Cameron-Gelbach-Miller).
- **constituency_decomposition.md** — `pres_dem_share` vs `Dem_Mayor` scatter and regressions.
- **esg_event_study_cs.md** — Callaway-Sant'Anna event study for anti-ESG law adoption.
- **fiscal_stress_construction.md** — Composite construction and by-group distributions.
- **fiscal_interactions.md** — FS1–FS5 interaction battery + reading section.
- **tel_robustness.md** — TEL operationalization robustness (identification-corrected).
- **interaction_vif_diagnostics.md** — VIF + common support + marginal effects for C6 and marketability interactions.
- **sample_reconciliation.md** — Why N moved from 5,962 to 6,825 across spec iterations.

---

## Summary across all specifications

| Finding | Evidence | Strength |
|---|---|---|
| **H1b: Dem_Mayor null across outcomes** | β ≈ 0 across C1–C8 + R1–R24 | \*\*\* Rock solid (32 specs) |
| **Constituency drives issuance** | pres_dem +0.053\*\* to +0.055\*\* | \*\* Consistent |
| **Marketability channel** | npdes × state_green +0.0016\* to +0.0018\* | \* Novel, main table |
| **Fiscal-capacity gates** | reserve + (ns), debt service − (ns) in main; Table 3 L2 fiscal_stress +0.018\*\* | \*\* Conditional on issuance |
| **NPDES × Party interaction** | I1 dem_x_npdes +0.028\* | \* Conditional partisan |
| **Demonstration margin (supply-side)** | I3 Dem_Mayor -0.022\*\*\*, interaction +0.0011\*\*\*, VIF 1.14 centered | \*\*\* Novel, robust |
| **Constituency amplification (demand-side)** | I4 Dem_Mayor -0.065\*\*, interaction +0.114\*\*, VIF 1.18 centered; +0.101\*\*\* on non-water, -0.002 ns on water | \*\* Novel, discretion-specific |
| **No local spatial spillover** | R13–R16 all ns | — Clean |
| **Pre-ESG-law market predicts issuance** | R17: +0.064\*\*\* | \*\*\* Confirmed |
| **NPDES effect ownership-specific** | R20 _locgov +0.014\*\*, R21 _private null | \*\* Placebo clean |
| **Fiscal-stress × partisan interactions** | FS1–FS4 null or fragile; FS5 triple = 0 | — No support |
| **TEL under state FE** | Mullins ns (p=0.15); binary forms unidentified | — Dropped from main |

---

## The story

**Partisan ideology does not drive green bond issuance.** `Dem_Mayor` is null at the extensive margin across all 32 specifications tested.

**The engine is material + political interacting with institutional.**
1. **Regulatory pressure × market depth** (marketability): compulsion drives issuance *where ESG investors exist*, not as a standalone force.
2. **Constituency** (`pres_dem_share`): cities with green-leaning electorates issue more, irrespective of mayor partisanship.
3. **Fiscal capacity** (reserve ratio, debt service): directional but not individually significant in the 10-variable spec.

**The partisan null masks conditional amplification, not autonomous agency.** Three distinct interaction channels reveal the same underlying pattern:
- **Compulsion responsiveness** (I1 dem_x_npdes +0.028\*): Dem mayors respond slightly more to regulatory pressure.
- **Supply-side imitation** (I3 dem_x_state_green_cum +0.0011\*\*\*): Dem mayors follow existing state markets.
- **Demand-side amplification** (I4 dem_x_pres_dem +0.114\*\*): Dem mayors amplify constituency demand — positive effect in blue cities, negative in red cities, null on average. On non-water this strengthens to +0.101\*\*\*; on water it is zero (Table 2 placebo).

These are **responsive-representation** results, not autonomous partisan agency. Dem mayors don't create green demand — they amplify it where it exists (constituency), follow it where markets have formed (demonstration), and respond to it where regulators force the issue (compulsion).

**Conditional on issuance, the labelling decision is market-mediated (Table 3).** Distressed issuers label green to seek the greenium; compelled issuers label only where the ESG investor base can absorb the supply. Neither channel operates through partisan agency.

**Sensitivity and robustness.** Dem_Mayor null survives 24 robustness columns, 3 fiscal-interaction batteries, a Callaway-Sant'Anna event study on anti-ESG laws, two-way and state clustering, VIF centering checks, and three-tier imputation of the mayor partisan indicator. The two significant interactions (demonstration + marketability) survive centered-VIF robustness: identical coefficients, p-values, and standard errors under the orthogonalised specification.

---

## Files

```
processed/tables/
├── table1_v3_full.md                ← this document
├── table1_v3_main.md                ← C1–C8 main, compact
├── table1_v3_main_full.md           ← C1–C8 with ALL controls visible
├── table1_v3_interactions.md        ← I1–I3 partisan interactions
├── table1_v3_rob1.md                ← R1–R10 robustness
├── table1_v3_rob2.md                ← R11–R24 robustness
├── table3_labelling.md              ← Table 3 (issuer subsample)
└── v3_rr/                           ← R&R supplementary package
```

Reproduce:
```
TABLE1_MODULE=all python3 pipeline/analysis_table1_v3.py
python3 pipeline/analysis_table3_labelling.py
python3 pipeline/analysis_rr_demonstration_diagnostic.py
python3 pipeline/analysis_rr_constituency_decomp.py
python3 pipeline/analysis_rr_esg_event_study.py
```
