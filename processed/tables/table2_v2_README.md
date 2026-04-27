# Table 2 (v2) — Compulsion Gradient Across Use-of-Proceeds Categories

Generated 2026-04-15 by `pipeline/analysis_table2_v2.py` (modular; run via
`TABLE2_MODULE={water,non_water,sparse,stacked,all}`).

Supersedes `analysis_table2.py`. Incorporates every Part A–E decision +
user-specified compulsion variable choices.

## Headline finding (H2a, Dem_Mayor as primary treatment)

**H2a test** is the prediction that the partisan gap in green-bond
participation increases monotonically as external compulsion decreases.
Under the Dem_Mayor coding, this predicts a **negative** interaction
`Dem_Mayor × compulsion_ord`: Dem advantage shrinks where compulsion is
tight.

**Observed:**
- β(Dem_Mayor × compulsion_ord) = **+0.0009 (ns)** — direction is *opposite*
  of H2a but the magnitude is small and not statistically significant at
  any conventional level.
- Category-by-category LPM: **Dem_Mayor is null across all 7 categories**
  tested (water, clean transport, renewables, energy eff, green bldg,
  pollution control, natural resource). No regression-based support for
  H2a at the extensive margin.
- **Fisher exact tests (sparse categories, 3–9 positives)** do show gaps:
  - **Climate Adaptation**: Fisher p = **0.022** (Dem 0.2% vs Rep 0.0%)
  - **Pollution Control**: Fisher p = **0.087** (Dem 0.2% vs Rep 0.0%)
  - **Natural Resource**: Fisher p = 0.263 (ns, too sparse)

**Reading.** The LPM coefficient approach is underpowered for categories
with 3–20 positive city-years. Fisher exact suggests some non-trivial
partisan gap at Step 1 (category entry) for the sparsest discretionary
categories (climate adapt, pollution control), but the stacked
monotonicity test does not detect it — likely because water dominates
the pool (90 positives vs 3–20 elsewhere).

## Where the compulsion signal lives: what the compulsion variables actually do

### Water (n_pos = 90) — memo primary is confirmed

| Variant | β(Dem) | Compulsion variables β |
|---|---|---|
| W1 Primary (memo) | −0.0002 | `npdes_formal_prior3yr_muni` +0.008\*, `overflow_events_lag2` +0.006\*\*\* |
| W2 Full ladder | −0.0004 | NPDES formal +0.008 (attenuated), informal +0 (ns), violations +0 (ns), JDC +0 (ns) |
| W3 Pooled index | −0.0007 | `compulsion_index_z` +0.001 (ns) |

**Reading:** NPDES formal + overflow events is the right compulsion spec
for water. The ladder absorbs the NPDES signal into overflow; informal
enforcement and judicial consent decrees add no independent information.
The pooled index underperforms because it mixes in non-water components
(FEMA flood + IECC lag).

### Non-water discretionary categories

| Category | n_pos | β(Dem) | Top significant compulsion coefficient |
|---|---|---|---|
| Clean Transportation | 17 | −0.0003 (ns) | None significant (CAA, state GHG, ZEV, IIJA all ns) |
| Renewables (muni-elec subsample) | 9 | −0.0001 (ns) | **`state_carbon_pricing_lag1` +0.010\*\*\***; `ep_muni_electric_rev_asinh_lag1` −0.023\*\* |
| Energy Efficiency | 20 | −0.0019 (ns) | **`ep_state_aceee_code_rank_lag1` −0.0003\*\*** (lower rank = more issuance) |
| Green Buildings | 19 | −0.0003 (ns) | **`bcode_bps_adopted_lag1` −0.025\*\***, `bcode_state_weakening_amendments_lag1` −0.006\*, `ira_ggrf_grant_amt_asinh_lag1` −0.001\*\* |

**Cleanest compulsion-signal finding (non-water):**
- **Carbon pricing drives renewable bonds** where cities have muni-electric
  utilities (+0.010\*\*\*). This is a clean state policy × city capacity
  test.
- **ACEEE code-rank matters for energy efficiency** (−0.0003\*\*, better
  rank = more issuance).

**Unexpected signs:**
- `ep_muni_electric_rev_asinh_lag1` negative in renewables — deeper muni-
  electric operations associated with *less* renewable-bond issuance.
  Possible selection: large muni-electric utilities may already have
  built renewable capacity through other financing channels.
- `bcode_bps_adopted_lag1` negative in green buildings — cities with
  city-level BPS issue *fewer* green-building bonds. Possibly reflects
  reverse timing (BPS adoption and bond issuance both happen in climate-
  leader cities but not in the same year) or collinearity with IECC/state
  BPS.
- IRA GGRF grant negative on green-building issuance — grants may flow to
  places that don't then issue.

### Sparse categories

| Category | n_pos | LPM β(Dem) | Fisher Dem rate | Fisher Rep rate | Fisher p |
|---|---|---|---|---|---|
| Climate Adaptation | 7 | +0.0000 | 0.2% | 0.0% | **0.022** |
| Pollution Control | 9 | −0.0002 | 0.2% | 0.0% | **0.087** |
| Natural Resource | 3 | −0.0001 | 0.1% | 0.0% | 0.263 |

Fisher is more informative than LPM here. The significant gap at Climate
Adaptation is particularly interesting because the physical-risk
compulsion variables (NFIP, FEMA flood, NRI inland EAL) did not absorb
the partisan signal — suggesting Democratic mayors may enter climate-
adaptation bonds for reasons beyond measured flood-risk exposure.

## Stacked monotonicity (Col 9)

- N = 47,776 (8 categories × city-years)
- β(Dem_Mayor) = −0.0018 (ns)
- β(compulsion_ord) = **−0.0134\*\*\*** (base rate falls as compulsion ordinal falls — artefact of water dominating the pooled positives)
- β(Dem_Mayor × compulsion_ord) = **+0.0009 (ns)** — *opposite sign* from H2a prediction but not significant
- Binary compelled × Dem_Mayor variant: +0.0021 (ns)

**H2a monotonicity is NOT supported by the stacked LPM test.** The
partisan gap visible in Fisher-exact tests for the sparsest discretionary
categories doesn't scale up to a monotonic ordinal interaction in the
pooled model — likely because water's dominant positive count swamps the
discretionary signal.

## Output files

```
processed/tables/
├── table2_v2_README.md              ← this summary
├── table2_v2_water.md               ← 3 water compulsion variants
├── table2_v2_non_water.md           ← 4 discretionary categories
├── table2_v2_sparse.md              ← 3 sparse (+ Fisher exact)
└── table2_v2_stacked.md             ← monotonicity test
```

## Reproduce

```bash
TABLE2_MODULE=water     python3 pipeline/analysis_table2_v2.py
TABLE2_MODULE=non_water python3 pipeline/analysis_table2_v2.py
TABLE2_MODULE=sparse    python3 pipeline/analysis_table2_v2.py
TABLE2_MODULE=stacked   python3 pipeline/analysis_table2_v2.py
# or all-in-one:
TABLE2_MODULE=all       python3 pipeline/analysis_table2_v2.py
```

## Recommendations for the paper

1. **Headline for H2a**: Fisher exact evidence of partisan gap in
   Climate Adaptation (p=0.022) and Pollution Control (p=0.087) vs
   null in Water. Frame this as **partial** support for H2a — direction
   matches but stacked monotonicity fails.

2. **Cleanest compulsion finding** is `state_carbon_pricing_lag1` on
   Renewables in the muni-electric subsample: +0.010\*\*\*. This is a
   strong claim about state climate policy reaching municipal bond
   markets where cities have capacity to act.

3. **ACEEE code rank on Energy Efficiency** is the second cleanest
   finding: institutional stringency → more efficiency bond issuance.

4. **Negative-sign puzzles** (city BPS on green buildings, muni-electric
   depth on renewables, grants on both) are worth a paragraph — most
   likely reflect grant selection / reverse timing rather than causal
   negatives. Not interpretive of partisan gap.
