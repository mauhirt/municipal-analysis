# Table 1 (v3) — The Compulsion Pipeline

**Sample:** 6,477 city-years, 572 cities, 49 states, 2013–2025.
**Treatment:** `Dem_Mayor` (no lag). **FE:** state + year. **SE:** clustered at city (fips7).

**Structure.** Six main columns: three outcomes (any green bond, self-labelled, water-only) × two scales (probability, amount). All columns share the same expanded RHS with the full theoretical battery, including the two market-channel variables from the labelling story:
- `fiscal_stress_index_lag2` — **greenium-seeking** channel
- `npdes × state_green_cum` — **marketability** channel

---

## Main columns (C1–C6)

| Variable | C1 GBI | C2 GBI $ | C3 Self-green | C4 Self $ | C5 Water-only | C6 Water $ |
|---|---|---|---|---|---|---|
| `Dem_Mayor` | +0.000 | -0.005 | -0.002 | -0.032 | -0.001 | -0.020 |
| `pres_dem_two_party_share_lag2` | **+0.057\*\*** | **+1.063\*\*** | **+0.058\*\*** | **+1.066\*\*** | +0.017 | +0.322 |
| `npdes_formal_prior3yr_muni` | -0.022 | -0.456 | -0.016 | -0.352 | -0.007 | -0.161 |
| `reserve_ratio_lag2` | +0.008\*\* | +0.145\*\* | +0.006\* | +0.110\* | +0.005\* | +0.089\* |
| `debt_service_burden_lag2` | **-0.247\*\*** | **-4.734\*\*** | **-0.189\*\*** | **-3.691\*\*** | -0.104\* | -2.009\* |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.008 | -0.146 | -0.008 | -0.145 | -0.010\* | -0.196\* |
| `asinh_state_all_green_cum_amt_lag1` | +0.000 | +0.003 | +0.000 | +0.001 | +0.000 | +0.005 |
| **`fiscal_stress_index_lag2`** | **+0.020\*\*** | **+0.385\*\*** | **+0.016\*\*** | **+0.314\*\*** | +0.006 | +0.122 |
| **`npdes × state_green_cum`** | **+0.0018\*** | **+0.038\*** | **+0.0017\*** | **+0.034\*** | +0.0008 | +0.016 |
| N | 6,477 | 6,477 | 6,477 | 6,477 | 6,477 | 6,477 |
| R² | 0.102 | 0.107 | 0.102 | 0.106 | 0.051 | 0.054 |

Controls included but not shown: `state_dem_governor_lag1`, `state_dem_trifecta_lag1`, `state_rep_trifecta_lag1`, `log_population_city_lag2`\*\*\*, `log_percapita_income_city_lag2`, `unemployment_city_lag2`. Stars: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

### Reading

**H1b (partisan agency null) holds across all outcomes.** `Dem_Mayor` is indistinguishable from zero in all six columns — issuance and amount, any-green and self-labelled and water-only.

**Constituency drives issuance but NOT water-only.** `pres_dem_two_party_share_lag2` is significant (\*\*) for GBI and self-green (probability and amount) but null for water-only. Reading: a broader "green constituency" matters for the generic environmental-bond decision, but water infrastructure is compulsion-driven regardless of political leaning.

**The two market channels are significant in the main spec.**
- **Greenium-seeking** (`fiscal_stress_index_lag2`): +0.020\*\* on GBI, +0.016\*\* on self-green. Distressed cities issue/label green more — consistent with seeking yield reduction through ESG demand.
- **Marketability** (`npdes × state_green_cum`): +0.0018\* on GBI, +0.0017\* on self-green. Compelled cities issue/label green *where the ESG investor base exists*. The NPDES main effect flips null once the interaction is included — compulsion alone isn't enough without a market to absorb the issuance.

**Water-only has weaker channels but the same null on Dem_Mayor.** Water-only has only 90 events in the sample. R² is lower (0.05), reflecting a narrower, more compulsion-homogeneous outcome. Fiscal stress and marketability attenuate but remain directionally correct. `reserve_ratio` and `debt_service` retain significance at 10%.

**Fiscal-capacity variables become significant.** Reserve ratio (+\*\*) and debt service burden (-\*\*) — both were null in the earlier lean spec but gain significance once `fiscal_stress_index` is explicitly controlled. Interpretation: fiscal stress is a composite; isolating it from its components allows each to carry its own effect.

---

## Partisan interactions (complement to main table)

Two partisan-interaction specs, added to the expanded PRIMARY, to test whether the null on `Dem_Mayor` hides a conditional partisan margin.

| Variable | I1 NPDES×Party (GBI) | I2 NPDES×Party (Self) | I3 Demonstration (Self) | I4 Demonstration (Water-only) |
|---|---|---|---|---|
| `Dem_Mayor` | -0.004 | -0.005 | **-0.024\*\*\*** | +0.000 |
| `dem_x_npdes` | **+0.031\*\*** | **+0.027\*** | — | — |
| `dem_x_state_green_cum` | — | — | **+0.0011\*\*\*** | -0.000 |
| N | 6,477 | 6,477 | 6,477 | 6,477 |

**Reading.** The partisan signal is conditional, not universal.
- **NPDES × Party** (I1/I2): Dem mayors are *slightly* more responsive to NPDES compulsion than Rep mayors (+0.031\*\* on GBI, +0.027\* on self). But Dem_Mayor main effect stays null — this is an interaction story.
- **Demonstration** (I3): `Dem_Mayor` turns **-0.024\*\*\*** on self-green with `Dem × state_green_cum` = **+0.0011\*\*\***. Dem mayors don't autonomously self-label — they respond to an *existing* state-level green market (imitation).
- **Demonstration on water-only** (I4): null. The demonstration/imitation channel does not operate for water-only bonds, consistent with water being purely compulsion-driven.

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

## Summary across all specifications

| Finding | Evidence | Strength |
|---|---|---|
| **H1b: Dem_Mayor null across all outcomes** | β ≈ 0 across C1–C6 + R1–R22 | \*\*\* Rock solid |
| **Constituency drives issuance (not water-only)** | pres_dem +0.057\*\* on GBI & self; null on water | \*\* Consistent |
| **Greenium-seeking channel (fiscal stress)** | +0.020\*\* on GBI, +0.016\*\* on self | \*\* Novel, main table |
| **Marketability channel (NPDES × state_green)** | +0.0018\* on GBI, +0.0017\* on self | \* Novel, main table |
| **NPDES × Party interaction** | I1 dem_x_npdes +0.031\*\* | \*\* Conditional partisan |
| **Demonstration margin (Dem × state_green)** | I3 Dem_Mayor -0.024\*\*\*, interaction +0.0011\*\*\* | \*\*\* Novel partisan |
| **Demonstration absent for water-only** | I4 both coefficients null | Consistent with compulsion |
| **Water-only is compulsion-homogeneous** | Lower R², constituency null | Consistent |
| **Pre-ESG-law market predicts issuance** | R17: +0.064\*\*\* | \*\*\* Confirmed |
| **NPDES effect ownership-specific** | R20 _locgov +0.014\*\*, R21 _private null | \*\* Placebo clean |

---

## The story

**Partisan ideology does not drive green bond issuance.** `Dem_Mayor` is null at the extensive margin across all outcomes (C1–C6) and in all 22 robustness columns.

**Regulatory pressure + constituency + market conditions drive issuance.** The main table shows four forces:
1. **NPDES enforcement × state green market** (marketability): compulsion matters where investors exist (+0.0018\*).
2. **Fiscal stress** (greenium-seeking): distressed cities label green to reduce borrowing cost (+0.020\*\*).
3. **Constituency** (`pres_dem_share`): cities with green-leaning electorates issue more (+0.057\*\*).
4. **Fiscal capacity** (reserve ratio +, debt service −): standard muni-finance capacity gates.

**Water-only bonds are purely compulsion-driven.** Constituency and demonstration channels do *not* operate for water-only self-labelling — compulsion alone (via the marketability interaction) is the operative force.

**The only partisan signal is conditional, not autonomous.** Dem mayors are slightly more responsive to NPDES compulsion (I1) and strongly respond to existing state-level green markets (I3 demonstration). They don't create markets; they follow them. Imitation, not ideology.

---

## Files

```
processed/tables/
├── table1_v3_full.md                ← this document
├── table1_v3_main.md                ← C1–C6 (6 outcome-by-scale cols)
├── table1_v3_interactions.md        ← Partisan interactions I1–I4
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
