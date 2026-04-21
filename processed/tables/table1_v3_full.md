# Table 1 (v3) — The Compulsion Pipeline

**Sample:** 6,477 city-years, 572 cities, 49 states, 2013–2025.
**Treatment:** `Dem_Mayor` (no lag). **FE:** state + year. **SE:** clustered at city (fips7).

**Structure.** Four main columns: two outcomes (any green bond, self-labelled) × two scales (probability, amount). All columns share the same expanded RHS including the two market-channel variables that answer *why a city labels its bond green*:
- `fiscal_stress_index_lag2` — **greenium-seeking** channel
- `npdes × state_green_cum` — **marketability** channel

---

## Main columns (C1–C4)

| Variable | C1 GBI | C2 GBI $ | C3 Self-green | C4 Self $ |
|---|---|---|---|---|
| `Dem_Mayor` | +0.000 | -0.005 | -0.002 | -0.032 |
| `pres_dem_two_party_share_lag2` | **+0.057\*\*** | **+1.063\*\*** | **+0.058\*\*** | **+1.066\*\*** |
| `npdes_formal_prior3yr_muni` | -0.022 | -0.456 | -0.016 | -0.352 |
| **`npdes × state_green_cum`** | **+0.0018\*** | **+0.038\*** | **+0.0017\*** | **+0.034\*** |
| **`fiscal_stress_index_lag2`** | **+0.020\*\*** | **+0.385\*\*** | **+0.016\*\*** | **+0.314\*\*** |
| `reserve_ratio_lag2` | **+0.008\*\*** | **+0.145\*\*** | +0.006\* | +0.110\* |
| `debt_service_burden_lag2` | **-0.247\*\*** | **-4.734\*\*** | **-0.189\*\*** | **-3.691\*\*** |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.008 | -0.146 | -0.008 | -0.145 |
| `asinh_state_all_green_cum_amt_lag1` | +0.000 | +0.003 | +0.000 | +0.001 |
| N | 6,477 | 6,477 | 6,477 | 6,477 |
| R² | 0.102 | 0.107 | 0.102 | 0.106 |

Controls included but not shown: `state_dem_governor_lag1`, `state_dem_trifecta_lag1`, `state_rep_trifecta_lag1`, `log_population_city_lag2`\*\*\*, `log_percapita_income_city_lag2`\*\*, `unemployment_city_lag2`\*\*. Full table with every control visible: `table1_v3_main_full.md`. Stars: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

### Reading

**H1b (partisan agency null) holds across all outcomes.** `Dem_Mayor` is indistinguishable from zero on every outcome — issuance (C1, C3) and amount (C2, C4), any-green and self-labelled alike.

**Constituency drives issuance.** `pres_dem_two_party_share_lag2` is **+0.057\*\*** to **+0.058\*\*** across all four columns. A 10 pp higher Dem vote share → ~0.6 pp higher issuance probability. Constituency, not mayoral agency.

**Two market channels are significant in the main spec.**
- **Greenium-seeking** (`fiscal_stress_index_lag2`): **+0.020\*\*** on GBI, **+0.016\*\*** on self-green. Distressed cities issue and label green more — consistent with seeking yield reduction through ESG demand.
- **Marketability** (`npdes × state_green_cum`): **+0.0018\*** on GBI, **+0.0017\*** on self-green. Compelled cities issue/label green *where the ESG investor base exists*. NPDES main effect flips null once the interaction is in — compulsion alone isn't enough without a market to absorb.

**Fiscal capacity gates.** Reserve ratio (+\*\*) and debt service burden (−\*\*) are both significant. Well-reserved cities issue more; debt-burdened cities issue less.

**Policy environment controls attenuate.** Anti-ESG law dummy and state green cum (main effect) are null once the interaction is included — their effects operate through the marketability channel rather than as main effects.

---

## Partisan interactions (complement to main table)

Three partisan-interaction specs added to the expanded PRIMARY, testing whether the null on `Dem_Mayor` hides a conditional partisan margin.

| Variable | I1 NPDES×Party (GBI) | I2 NPDES×Party (Self) | I3 Demonstration (Self) |
|---|---|---|---|
| `Dem_Mayor` | -0.004 | -0.005 | **-0.024\*\*\*** |
| `dem_x_npdes` | **+0.031\*\*** | **+0.027\*** | — |
| `dem_x_state_green_cum` | — | — | **+0.0011\*\*\*** |
| N | 6,477 | 6,477 | 6,477 |

**Reading.** The partisan signal is conditional, not universal.
- **NPDES × Party** (I1/I2): Dem mayors are slightly more responsive to NPDES compulsion than Rep mayors (+0.031\*\* on GBI, +0.027\* on self). `Dem_Mayor` main effect stays null.
- **Demonstration** (I3): `Dem_Mayor` turns **-0.024\*\*\*** with `Dem × state_green_cum` = **+0.0011\*\*\***. Dem mayors don't autonomously self-label — they respond to an existing state-level green market. Imitation, not ideology.

---

## Robustness R1–R10

Full coefficients in `table1_v3_rob1.md`. All on `Y_self_green`. `Dem_Mayor` null across all 10 specs (range -0.003 to +0.017). Notable ancillary findings: IRA GGRF and FEMA resilience grants negative; state ZEV mandate strongly negative; RGGI and C40 membership weakly positive.

## Robustness R11–R22

Full coefficients in `table1_v3_rob2.md`. All on `Y_self_green`. `Dem_Mayor` null across all 12 specs (range -0.002 to +0.026). Notable findings:
- **R17 ESG endogeneity:** `state_pre_esg_activity` = +0.064\*\*\* — states with pre-existing green markets before anti-ESG law adoption issue more self-labelled bonds.
- **R20 NPDES Locgov:** `_locgov` +0.014\*\* — effect generalises to local-government-owned water districts.
- **R21 NPDES Private placebo:** null (wrong sign) — private-facility enforcement doesn't predict labelling, ruling out general regulatory-intensity confound.
- **R22 Kitchen-sink:** confirms 5 dropped fiscal controls are inert.

---

## Summary

| Finding | Evidence | Strength |
|---|---|---|
| **H1b: Dem_Mayor null across outcomes** | β ≈ 0 across C1–C4 + R1–R22 | \*\*\* Rock solid |
| **Constituency drives issuance** | pres_dem +0.057\*\* to +0.058\*\* | \*\* Consistent |
| **Greenium-seeking channel** | fiscal_stress +0.020\*\* GBI, +0.016\*\* self | \*\* Novel, main table |
| **Marketability channel** | npdes × state_green +0.0018\*, +0.0017\* | \* Novel, main table |
| **Fiscal-capacity gates** | reserve +\*\*, debt service −\*\* | \*\* Consistent |
| **NPDES × Party interaction** | I1 dem_x_npdes +0.031\*\* | \*\* Conditional partisan |
| **Demonstration margin** | I3 Dem_Mayor -0.024\*\*\*, interaction +0.0011\*\*\* | \*\*\* Novel partisan |
| **Pre-ESG-law market predicts issuance** | R17: +0.064\*\*\* | \*\*\* Confirmed |
| **NPDES effect ownership-specific** | R20 _locgov +0.014\*\*, R21 _private null | \*\* Placebo clean |

---

## The story

**Partisan ideology does not drive green bond issuance.** `Dem_Mayor` is null at the extensive margin across all outcomes and in all 22 robustness columns.

**Four forces drive issuance.**
1. **Regulatory pressure interacting with market depth** (marketability): compulsion matters *where ESG investors exist*.
2. **Fiscal distress** (greenium-seeking): distressed cities label green to reduce borrowing cost.
3. **Constituency** (`pres_dem_share`): cities with green-leaning electorates issue more.
4. **Fiscal capacity** (reserve ratio +, debt service −): standard muni-finance gates.

**The only partisan signal is conditional, not autonomous.** Dem mayors are slightly more responsive to NPDES compulsion (I1) and strongly respond to existing state-level green markets (I3). They don't create markets; they follow them. Imitation, not ideology.

---

## Files

```
processed/tables/
├── table1_v3_full.md                ← this document
├── table1_v3_main.md                ← C1–C4 (2 outcomes × prob/amount)
├── table1_v3_main_full.md           ← C1–C4 with ALL controls visible
├── table1_v3_interactions.md        ← Partisan interactions I1–I3
├── table1_v3_rob1.md                ← R1–R10 robustness
├── table1_v3_rob2.md                ← R11–R22 robustness
├── table3_labelling.md              ← Labelling decision (issuer subsample)
└── v3_rr/                           ← R&R supplementary package (Tasks 2–8)
```

Reproduce:
```
TABLE1_MODULE=all python3 pipeline/analysis_table1_v3.py
python3 pipeline/analysis_table3_labelling.py
```
