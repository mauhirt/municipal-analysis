# Parts C–E of the variable audit: remaining open questions

Parts A–B (outcomes, Family 1a compulsion) were addressed in the previous
exchange. This document closes out the audit for Parts C–E with the same
peer-review rigour: every variable flagged by provenance, every meaningful
interaction proposed with theoretical justification.

---

## Part C — Family 1b (fiscal depth / spillover / controls)

### C1. Fiscal depth — which variables survive peer review

| Variable | Coverage | Source | Use |
|---|---|---|---|
| `charges_to_own_source_lag2` | 2013–2025 | Census ASLGF (`fiscal_tel_merged_2007_2024.csv`) | **Primary** enterprise-fund-depth measure |
| `property_tax_dependence_lag2` | 2013–2025 | Census ASLGF | Primary tax-base composition measure |
| `tax_autonomy_ratio` | 2013–2023 | Census ASLGF | Alternative tax-base measure (drops 2024-25) |
| `reserve_ratio_lag2` | 2013–2025 | Census ASLGF | Primary fiscal-capacity gate |
| `debt_service_burden_lag2` | 2013–2025 | Census ASLGF | Existing-debt constraint |
| `capital_stock_pc_lag2` | 2015–2025 | Constructed in 00 (6-yr depreciated sum of per-capita capital outlays, 2% annual depreciation) | Infrastructure-stock proxy |
| `fiscal_stress_index_lag2` | 2013–2025 | Constructed in 00 from multiple fiscal indicators | Primary stress measure |
| `fiscal_stress_pca` | 2013–2021 | Constructed in 00 (PCA) | **Robustness only** — drops 2022-25 |
| `tel_stringency_normalized` | 2013–2025 | `raw/institutional/tel.csv` (ACIR / Lincoln Institute) | **Absorbed by state FE** — use only in TEL × city-fiscal interactions |
| `igr_share`, `fed_igr_share_lag2`, `state_igr_share_lag2` | 2013–2025 | Census ASLGF | Fiscal-autonomy controls |

**Open Q resolution:**
- **Primary fiscal spec**: `charges_to_own_source_lag2 + reserve_ratio_lag2 + debt_service_burden_lag2 + fiscal_stress_index_lag2 + tel_x_prop_tax_dep + tel_x_charges`. This is four fiscal dimensions (depth / capacity / debt / stress) plus the two TEL-substitution interactions. No main TEL effect (absorbed).
- **Robustness fiscal spec**: swap `fiscal_stress_index_lag2` → `fiscal_stress_pca` (loses 2022-2025). Report N reduction in table notes.
- **`capital_outlay`** is currently MISSING in the panel (referenced in `helpers.py` but not built in 00 or 01). Fix needed in `01_construct_audit_variables.py`: derive from `capital_stock_pc` divergence. Flag for a follow-up build; not in scope of current commit.

### C2. Intergovernmental revenue — additions

Both `fed_igr_share_lag2` and `state_igr_share_lag2` are in the panel and
authoritatively sourced from Census ASLGF. Previously not in T1 main RHS —
add them now.

**Proposed new interaction:** `fed_igr_share_lag2 × Rep_Mayor_lag1`. Tests
whether Republican mayors in fiscally federally-dependent cities behave
differently (e.g., more inclined to accept federal conditions on green
spending when dependent on federal transfers). Theoretically interesting,
but requires justification in the paper since it doesn't come directly
from the memo.

### C3. Capital stock + other fiscal

Recommended: add `capital_stock_pc_lag2` to T1 main RHS (it's there in
`helpers.py` but not used in my current analysis scripts). It's the closest
continuous proxy for "infrastructure need" after `cwns_needs_real_lag2`,
and captures accumulated vs. depleted infrastructure stock.

Other fiscal variables (`debt_affordability`, `operating_balance`,
`budget_flexibility_squeeze`, `dsb_worsening`) — keep in a robustness
appendix column, don't multiply the main spec.

### C4. Spillover — state-level green-bond market × partisanship

This is the **single highest-priority new interaction** from this audit.

| Variable | What it captures | Source |
|---|---|---|
| `state_green_bond_ever_lag1` | Binary — any green bond in state by year t−1 | Bloomberg Terminal (aggregated in 00) |
| `state_green_bond_cum_count_lag1` | Cumulative count of green bonds issued in state up to year t−1 | Bloomberg Terminal (aggregated in 00) |
| `asinh_state_all_green_cum_amt_lag1` | Cumulative dollar amount (asinh) | Bloomberg Terminal (aggregated in 00) |

**Current gap:** the aggregation in `00_build_panel.py` is over **all**
issuers (state government, cities, special districts), not just self-
labelled bonds. Your spec preference is for self-labelled only. Fix:

1. In `00_build_panel.py`, build a new panel `state_self_green_cum_count_lag1`
   / `asinh_state_self_green_cum_amt_lag1` by aggregating only bonds where
   `Y_self_green == 1` (or `Self-reported Green__Yes > 0` in the raw
   detail columns) at the state-year level.
2. Expose as a new canonical spillover variable.

**Proposed interactions (main finding for peer review):**

```
rep_x_state_green_cum = Rep_Mayor_lag1 * state_green_bond_cum_count_lag1
rep_x_state_self_green_cum = Rep_Mayor_lag1 * state_self_green_cum_count_lag1
```

**Theoretical prediction:** if market normalisation reduces the partisan
gap, these interactions should be **positive** (Republicans more
responsive to a mature state green-bond market). If the sticky-partisan-
identity story dominates (memo H3b), they should be null.

### C5. Economic / demographic controls — audit

- `log_population_city_lag2`, `log_percapita_income_city_lag2`,
  `unemployment_city_lag2`: all 2013-2025, in panel, authoritatively
  sourced from BLS + ACS.
- `pct_college_educated`, `pct_nonwhite`, `median_home_value`:
  cross-sectional (ACS 2022 5-year estimates). **Absorbed by city FE.**
  Useful under state+year FE as cross-city controls.
- `is_principal_city_lag2`: static city characteristic. Same absorption.
- `manufacturing_city`, `management_city`, `transport_city`, `lfpr_city`:
  time-varying (2013-2023), from BLS/ACS. **These have meaningful within-
  city variation** and should be added to the controls block in T1 and T2
  as economic/industrial structure controls.

**Action:** add `manufacturing_city`, `management_city`, `transport_city`,
`lfpr_city` as lag-2 variants to the main RHS. These capture city-specific
economic structure heterogeneity that would otherwise leak into the
Rep_Mayor coefficient through omitted-variable bias.

---

## Part D — Family 2 (Political)

### D1. Rep_Mayor variants — provenance

All mayor variables derive from `raw/mayor/mayor_party.csv` which is
hand-coded by the author (Maurice Hirt) using:
1. Voter registration records where publicly available
2. DIME Campaign Finance scores (Bonica 2014)
3. Endorsement data from state/local party records
4. Imputation for nonpartisan cities

**Peer-review implication:** this is a "constructed dataset" that needs to
be described in the data section of the paper, with:
- Coverage (1,824 cities, subset to 578 in the Bloomberg sample)
- Coding protocol
- Reliability checks (inter-coder agreement, or comparison to other
  mayoral-party datasets such as Carnes 2013)
- Treatment of nonpartisan cities (currently: imputed via DIME CF-scores)

The `fn_partisan_lag1 × Rep_Mayor_lag1` interaction I already implemented
(`rep_x_fn_partisan`) tests whether Rep_Mayor is attenuated in nonpartisan
cities, which addresses some of the coding-reliability concern. Continue
using it.

### D2. Continuous mayor vote-share variable

You flagged this as a preferred alternative to binary Rep_Mayor. The
underlying data is in `raw/mayor/MayoralCandidates270326.xlsx` (2001-2025,
1,824 cities). It's not currently merged into the panel.

**Required build step:**
1. Parse the Excel file for winning-candidate vote share and runner-up
   vote share.
2. Compute `mayor_vote_margin = winner_share - runnerup_share` (signed:
   positive for Rep win, negative for Dem win).
3. Merge into 00_build_panel.py as a city-year variable.
4. Build `mayor_vote_margin_lag1`.

**Not yet done.** Flag as a follow-up build for the next iteration.
Currently `mayor_prob_rep_lag1` (DIME CF-score-based) is the best
continuous proxy.

### D3. City institutional × Rep_Mayor interactions

These are built/verified:

| Interaction | Partner variable source | Status |
|---|---|---|
| `rep_x_fn_partisan` | ICMA FOG | Built |
| `c40_x_rep_mayor` | C40 public roster | Built |
| `rep_x_esg_intensity` | Anti-ESG law database | Built |

**Proposed new ones to add:**

| Interaction | Partner variable | Source |
|---|---|---|
| `rep_x_termlimits` | `termlimits` | ICMA FOG |
| `rep_x_termlength` | `termlength` | ICMA FOG |
| `rep_x_fog` | `fog` (form of government) | ICMA FOG |
| `rep_x_initiative` | `initiative` (ballot initiative availability) | ICMA FOG |

All ICMA FOG variables are in the panel from `raw/institutional/fog_institutions_panel_2010_2024.csv`. Build as city-level × mayor interactions
(identified under state+year FE, absorbed under city+year FE).

### D4. Presidential vote share variants

Currently in panel:
- `pres_dem_two_party_share_lag2` — D share of D+R votes (excludes
  third-party)
- `pres_dem_vote_share_lag2` — D share of all votes

Source: `raw/political/presidential_elections.csv` (MIT MEDSL).

**You asked for "Rep over Dem":** easily constructed as
`pres_dem_two_party_share - 0.5` (negative when R>D) or
`pres_rep_vote_share - pres_dem_vote_share`. Both are in the raw file.
Can be added to 02 as `pres_rep_minus_dem_share`.

### D5. YCOM climate opinion — robustness-only per your note

All four YCOM variables present: `opinion_regulate`, `opinion_fundrenewables`,
`opinion_happening`, `opinion_worried`. Coverage 2016-2025 under lag 2,
N = 5,088.

**Correlation concern you flagged:** YCOM vs. `pres_dem_two_party_share`
state-year correlations are likely ≥ 0.7. Proposal:

1. Include YCOM **only** in a dedicated robustness column (as currently in
   T1 R1), not in main RHS.
2. Report explicit correlation matrix between YCOM and
   `pres_dem_two_party_share_lag2` in a paper appendix table.
3. If a reviewer asks whether the Rep_Mayor null in T1 survives conditioning
   on YCOM, R1 column already answers: yes, β stays ~0.

---

## Part E — State-level variables

### E1. Market infrastructure — the headline new interaction

Already resolved above in §C4. Two follow-ups:

1. **Build `state_self_green_cum_count_lag1` / `state_self_green_cum_amt_asinh_lag1`**
   (self-labelled only), not just all-issuer version. Requires 00 update.

2. **Pre-commit the interaction test**:
   `Rep_Mayor_lag1 × state_self_green_cum_count_lag1` on
   `Y_self_green`. Positive ⇒ market normalisation hypothesis
   supported; null/negative ⇒ sticky-identity hypothesis supported.

### E2. ESG legislation endogeneity test (time-variant)

You requested: "make time variant i.e. 1 after enactment; also one if there
was any green bond issuance activity by any entity with in the state before
enactment to see if the legislation actually suppresses issuance."

**Current state:**
- `fn_esg_has_muni_bond_law_post` (time-variant, 1 after state's first anti-
  ESG law enactment) is **built** from `esg_first_law_year` in 02 §5.1.
- `state_pre_esg_activity` (your second variable — any prior green-bond
  activity in state before first anti-ESG law) is **not yet built**.

**Required to build `state_pre_esg_activity`:**
1. In `00_build_panel.py`, after the Bloomberg skeleton merge, aggregate
   green-bond activity by state_abb for each state-year.
2. Identify the first year of any green-bond issuance in each state.
3. Create `state_pre_esg_activity` = 1 if `first_green_issuance_year <
   esg_first_law_year` (i.e. market was active when the law was passed).
4. Build `esg_law_active × state_pre_esg_activity` interaction.

**Theoretical test:** If anti-ESG laws actually suppress, the suppression
should be stronger in states that had existing activity. If laws were
reactively passed in already-quiescent states, the interaction is null.

**Flag:** not yet done. Follow-up build.

### E3. Bond commissions

`has_state_bond_commission` (988 positives) and `has_state_approval_body`
(2,288 positives) are both in panel, static per state. Use only in no-FE
or state-FE-only specs, or as interactions with city-level variables.

### E4. State-level party — symmetric triple

Already implemented: `state_dem_governor_lag1 + state_dem_trifecta_lag1 +
state_rep_trifecta_lag1` with "unified opposite" implicit as reference.

### E5. Other state-level variables — additions

Now fully sourced and added:

| Variable | Status |
|---|---|
| `state_rggi_member_lag1`, `state_wci_member_lag1` | **Now sourced from `raw/policy/rggi_wci_membership.csv`** with per-row citations |
| `state_ghg_law_active_lag1`, `state_ghg_law_years_since` | **New from `raw/policy/state_ghg_reduction_laws.csv`** |
| `state_zev_mandate_active_lag1` | **New from `raw/policy/state_zev_mandate.csv`** |
| `state_carbon_price_usd_lag1` | From DSIRE (existing) |
| `state_rps_target_pct_lag1` | From DSIRE (existing) |
| `rps_target_x_muni_electric` (interaction) | **New** — state policy × city capacity |

### E6. State-level variables as controls — consolidated main RHS

Proposed Family 3 block for main T1 / T2 / T3:

```
F3 = [
    # Partisanship environment
    'state_dem_governor_lag1',
    'state_dem_trifecta_lag1',
    'state_rep_trifecta_lag1',
    # Anti-ESG legislation (time-varying)
    'fn_esg_has_muni_bond_law_post_lag1',  # replaces contemporaneous esg_has_muni_bond_law
    'esg_underwriter_block_lag1',
    # Market infrastructure
    'asinh_state_all_green_cum_amt_lag1',  # or state_self_green variant when built
    # Climate policy (state-level compulsion)
    'state_carbon_pricing_lag1',
    'state_rggi_member_lag1',
    'state_ghg_law_active_lag1',
]
```

This is 9 variables, which is on the high side but all peer-review-defensible.
A parsimony-focused specification could drop the redundant RGGI/WCI/carbon-
pricing triad and keep only `state_carbon_pricing_lag1` (binary) + `state_ghg_law_active_lag1`.

---

## Summary of follow-up builds (not yet done)

| # | Item | File to modify |
|---|---|---|
| 1 | `Y_Mgmt_Proceeds_Yes` / `Y_Proj_Selection_Yes` | `01_construct_audit_variables.py` |
| 2 | `capital_outlay` | `01_construct_audit_variables.py` |
| 3 | `state_self_green_cum_count_lag1` / `_amt` | `00_build_panel.py` |
| 4 | `state_pre_esg_activity` and its interaction with ESG-law-post | `00_build_panel.py` + `02` |
| 5 | Mayor vote-share from candidates file | `00_build_panel.py` |
| 6 | EPA CAA county-level nonattainment | External data pull (EPA Green Book) |
| 7 | ICMA FOG × Rep_Mayor interactions (4 new) | `02_variable_additions.py` |
| 8 | `pres_rep_minus_dem_share_lag2` | `02_variable_additions.py` |
| 9 | Economic structure controls to main RHS (`manufacturing_city`, `management_city`, `transport_city`, `lfpr_city` at lag-2) | All three analysis scripts |
| 10 | `fed_igr_share_lag2 × Rep_Mayor_lag1` interaction | `02_variable_additions.py` |

Items 1, 2, 7, 8, 9, 10 are inside-repo changes that can be done quickly.
Items 3, 4, 5 require structural changes to `00_build_panel.py` (larger).
Item 6 requires an external data pull (EPA Green Book) that is blocked.
