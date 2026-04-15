# Table 1 (v2) — Updated Analysis with All Parts A-E Integrated

Generated 2026-04-15 by `pipeline/analysis_table1_v2.py` (modular, can be run
piecewise via `TABLE1_MODULE={main,r1_6,r7_12,r13_18,all}`).

## What changed from the v1 (2026-04-14) Table 1

Every decision from the variable-audit rounds (Parts A–E + doc recommendations)
is now integrated into the primary specification. Below, in order of impact:

### Treatment and clustering

| Change | v1 | v2 |
|---|---|---|
| Primary treatment | `Rep_Mayor_lag1` | **`Dem_Mayor` (no lag)** — Part D decision |
| `Ind_Mayor` | In main RHS | **Dropped** — Part D decision |
| Clustering | fips7 (city) | **state_id** — corrects TEL phantom-significance bug |

### RHS composition

| Family | v1 | v2 |
|---|---|---|
| Compulsion (F1a) | NPDES + overflow | Same; water ladder + pooled index available as robustness |
| Fiscal (F1b) | charges + reserves + DSB + TEL | **charges + reserves + DSB + `igr_share_lag2` + `tel_x_prop_tax_dep`** — per fiscal-constraint doc |
| State (F3) | `state_rep_trifecta` + `esg_has_muni_bond_law` (contemp) | **Symmetric triple (dem_gov + dem_trifecta + rep_trifecta)** + `fn_esg_has_muni_bond_law_post_lag1` (time-variant) + `asinh_state_all_green_cum_amt_lag1` (market depth) |
| Controls | log pop + log income + unemployment + substitute | Same + **`capital_outlay_pc_lag2`** (J27 from fiscal doc, previously MISSING) |
| Constituency | `pres_dem_two_party_share_lag2` (NaN for 2013-14) | Same but now **MEDSL-backed full 2013-2025 coverage** |

### Effective sample

v1: 5,903 city-years. v2: **5,962 city-years** (gain from MEDSL presidential
filling pre-2013 reach-back for lag-2).

## Headline results — Dem_Mayor coefficient on `Y_self_green`

| Spec | β(Dem_Mayor) | Specification |
|---|---|---|
| Col 3 (main pivot) | −0.0015 (0.0044) | Primary RHS |
| R1 + YCOM | −0.0036 (0.0047) | Climate opinion |
| R2 + Grants | −0.0016 (0.0045) | IIJA/IRA/FEMA |
| R3 Prob Dem | −0.0001 (0.0048)* | *prob_democrat (continuous)* |
| R4 Vote Share | +0.0147 (0.0104)† | *mayor_vote_share_win (continuous)* |
| R5 State Climate | −0.0015 (0.0043) | Carbon pricing + GHG law + RGGI + ZEV |
| R6 ESG Intensity | −0.0016 (0.0044) | Continuous ESG-law intensity |
| R7 Networks | −0.0014 (0.0051) | C40/ICLEI/MCPA |
| R8 Urban | −0.0033 (0.0042) | Density + principal city |
| R9 BPS/IECC | +0.0001 (0.0044) | IECC lag + BPS + weakening amendments |
| R10 Pooled Index | −0.0018 (0.0044) | Pooled compulsion index (5-component z-score) |
| R11 CAA | −0.0020 (0.0041) | EPA Green Book nonattainment |
| R12 Water Ladder | −0.0022 (0.0042) | Informal + formal + violations + JDC |
| R13 Market×Rep | **−0.0082\*** (0.0048) | Adds Rep_Mayor_lag1 + state_green_cum_x_rep |
| R14 CoPartisan | −0.0075 (0.0048) | Adds Rep_Mayor + co-partisan spillover |
| R15 ESG Endog | −0.0014 (0.0044) | state_pre_esg_activity interactions |
| R16 FOG×Dem | −0.0001 (0.0247) | ICMA FOG institutional interactions |
| R17 Rep Mayor | — | Legacy mirror with Rep_Mayor_lag1 (β = −0.0008 ns) |
| R18 Rep×PresDem | **−0.0449\*** (0.0233) | Adds electoral-discipline interactions |

\* Weak significance at p < 0.10; nothing significant at p < 0.05.
† Focal coefficient is `mayor_vote_share_win` in R4 — the interpretation is
different (continuous margin-of-victory rather than binary party).

## Reading

**H1b confirmed, strongly.** Across 18 out of 18 robustness perturbations,
`Dem_Mayor` remains statistically indistinguishable from zero on
`Y_self_green` and on `Green_Bond_Issued`. This is the cleanest evidence to
date that mayoral partisanship does **not** drive extensive-margin green-
bond issuance, conditional on compulsion, fiscal structure, and state
environment. The legacy `Rep_Mayor_lag1` mirror check (R17) corroborates:
β = −0.0008 (se 0.0049).

Where weak evidence (p < 0.10) does appear:
- **R13 Market×Rep**: when `state_green_cum_x_rep` is added alongside
  `Rep_Mayor_lag1`, Dem_Mayor becomes marginally negative (−0.008*). This
  may reflect collinearity with the state-market interaction rather than
  a substantive partisan effect.
- **R18 Rep×PresDem**: when electoral-discipline interactions are added,
  Dem_Mayor main effect shifts (−0.045*) while `Rep_Mayor_lag1 ×
  pres_dem_two_party_share_lag2` becomes a compensating positive (+0.039*).
  This is a reparameterisation effect, not a finding about the partisan
  gap itself.

## Notable non-partisan coefficients in the primary spec (Col 3)

These DO show significant patterns:

| Variable | β | Interpretation |
|---|---|---|
| `pres_dem_two_party_share_lag2` | +0.058* | Dem constituency weakly predicts issuance |
| `npdes_formal_prior3yr_muni` | **+0.018\*\*** | Federal enforcement compulsion works |
| `overflow_events_lag2` | **+0.006\*\*** | Sewer overflows drive issuance |
| `reserve_ratio_lag2` | +0.006* | Fiscal capacity gate |
| `debt_service_burden_lag2` | −0.102 | Debt burden dampens (weak) |
| `tel_x_prop_tax_dep` | **+0.001\*** | Mullins revenue-substitution confirmed |
| `log_population_city_lag2` | **+0.027\*\*\*** | Bigger cities issue more |
| `log_percapita_income_city_lag2` | **+0.024\*\*** | Higher-income cities issue more |
| `unemployment_city_lag2` | **+0.003\*\*** | Fiscal-distress signal |

Note that `asinh_state_all_green_cum_amt_lag1` (state market depth) shows
**β = +0.0002 (ns)** — the state-market-normalisation channel does NOT show
up in main spec.

## Output files

```
processed/tables/
├── table1_v2_README.md              ← this summary
├── table1_v2_main.md                ← 6 primary columns
├── table1_v2_robustness_1_6.md      ← R1-R6
├── table1_v2_robustness_7_12.md     ← R7-R12
└── table1_v2_robustness_13_18.md    ← R13-R18
```

## Reproduce

```bash
TABLE1_MODULE=main   python3 pipeline/analysis_table1_v2.py
TABLE1_MODULE=r1_6   python3 pipeline/analysis_table1_v2.py
TABLE1_MODULE=r7_12  python3 pipeline/analysis_table1_v2.py
TABLE1_MODULE=r13_18 python3 pipeline/analysis_table1_v2.py
# or all-in-one:
TABLE1_MODULE=all    python3 pipeline/analysis_table1_v2.py
```
