# Variable List for Completeness Audit
## Green Bond Paper — "When Do Red and Blue Go Green?"

**Purpose:** exhaustive list of every variable called for by the Table 1 / Table 2 / Table 3 specifications, for a completeness audit of data availability.

**Status codes:**
- ✅ **READY** — variable exists in the current processed panel, verified coverage
- 🟡 **PARTIAL** — variable exists but coverage is incomplete (years, cities, or both)
- 🔧 **PROPOSED** — variable is called for by the revised specification but not yet built
- ❓ **MISSING** — variable is needed but no data source identified
- 🚫 **DEFERRED** — variable was in earlier drafts, now excluded on principle

**How to use this file:** work through each section and fill in the Status, Source File, and Notes columns. Flag anything that is not READY so we can plan construction or substitution.

---

## 1. Outcome variables

The decision chain has four steps; Step 3 is now split into 3a (rate) and 3b (composition) per the revised memo.

| # | Variable | Definition | Decision step | Source | Status | Notes |
|---|---|---|---|---|---|---|
| O1 | `Green_Bond_Issued` | Binary. Bloomberg green leaf = 1 in city-year. Assigned algorithmically on use of funds. | Steps 1+2 joint | Bloomberg | | |
| O2 | `asinh_green_amt` | Inverse hyperbolic sine of total green bond par amount issued by city in year. Zero if no issuance. | Steps 1+2 joint, intensive margin | Bloomberg | | |
| O3 | `Y_self_green` | Binary. Bloomberg issuer self-designation field = 1. Distinct from green leaf. | Step 3a (label rate) | Bloomberg | | |
| O4 | `asinh_self_green_amt` | asinh of self-designated green bond amount. | Step 3a intensive | Bloomberg | | |
| O5 | `Y_esg_assurance` | Binary. Third-party verification from external reviewer (Sustainalytics, Vigeo, CICERO, etc.) present. | Step 4 | Bloomberg | | |
| O6 | `Y_water_only` | Binary. City-year has green bond(s) all of which are water/sewer category. | Table 2 Col 1 | Bloomberg, hand-coded categories | | |
| O7 | `Y_clean_trans` | Binary. Clean transportation green bond issued. | Table 2 Col 2 | Bloomberg, hand-coded categories | | |
| O8 | `Y_renewable` | Binary. Renewable energy green bond issued. | Table 2 Col 3 | Bloomberg, hand-coded categories | | |
| O9 | `Y_energy_eff` | Binary. Energy efficiency green bond issued. | Table 2 Col 4 | Bloomberg, hand-coded categories | | |
| O10 | `Y_green_bldg` | Binary. Green building green bond issued. | Table 2 Col 5 | Bloomberg, hand-coded categories | | |
| O11 | `Y_climate_adapt` | Binary. Climate adaptation green bond issued. | Table 2 Col 6 (descriptive only) | Bloomberg, hand-coded categories | | |
| O12 | `Y_pollution_control` | Binary. Pollution control green bond issued. | Table 2 Col 7 | Bloomberg, hand-coded categories | | |
| O13 | `category_composition_share` | For Step 3b composition test: among self-labelled bonds, share that are water-only vs. diversified. | Step 3b composition | Derived from O3 + O6–O12 | 🔧 PROPOSED | Needed for the Step 3a/3b split; currently only the Fisher exact is reported, not a regression outcome |

**Audit questions for outcomes:**
- Are all seven category variables (O6–O12) coded consistently across the full 2013–2025 panel?
- Does the Step 3b composition outcome (O13) need to be a continuous share or a categorical indicator? Decide before construction.
- For Y_climate_adapt: confirm N = 7 events total and that Fisher exact is the right inferential tool.

---

## 2. Family 1a — Legal-regulatory compulsion (category-matched)

**Framing:** the original memo had NPDES and overflow as the only 1a variables, which created the pan-category misspecification problem (NPDES is water-specific but was being regressed on all-category outcomes). The revised Table 1 uses a category-matched compulsion vector where every use-of-proceeds category gets its own compulsion variable. Table 1 includes all of them jointly; Table 2 uses each variable only in its own category column.

### 2a. Water & sewer compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C1 | `npdes_formal_prior3yr_muni` | Rolling 3-year stock of NPDES formal enforcement actions against city-owned water/sewer facilities. | Water | EPA ECHO, municipal ownership tier | ✅ READY | Primary compulsion variable for water. 278 cities nonzero; 1,239 nonzero city-years. |
| C2 | `npdes_formal_prior3yr_locgov` | Same as C1, adds water/sewer district facilities (MWRD, EBMUD, WSSC). | Water robustness | EPA ECHO, local government tier | ✅ READY | Robustness supplement |
| C3 | `npdes_formal_prior3yr_private` | Same as C1, private facility enforcement. | Water placebo | EPA ECHO, private tier | ✅ READY | Expected null — identifies general regulatory intensity confound |
| C4 | `overflow_events_lag2` | 2-year-lagged count of CSO/SSO overflow events at city-operated facilities. | Water co-primary | EPA ECHO SSO/CSO module | ✅ READY | Zero-filled for 28 cities with no ECHO facility. Constituency-visibility variable. |
| C5 | `case_jdc_prior3yr_muni` | Rolling 3-year stock of consent decrees filed against municipal facilities. | Water robustness | EPA ECHO, judicial cases | ✅ READY | 89 nonzero city-years. Used as robustness in Appendix D. |

### 2b. Clean transportation compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C6 | `highway_federal_match_intensity` | Federal highway/transit formula grant dollars per capita to the city's MPO or state DOT, allocated to city. | Clean transportation | FHWA/FTA NTD | 🔧 PROPOSED | Needs construction. Candidate sources: FHWA Highway Statistics, FTA NTD. Allocation to city level is non-trivial — may need to use MPO-level values as proxy. |
| C7 | `ada_nepa_capital_obligation` | Binary or continuous indicator of outstanding ADA paratransit or NEPA review triggering capital obligation. | Clean transportation | FTA compliance records, DOT ADA enforcement | 🔧 PROPOSED | Very difficult to construct at city level. May need to drop in favour of C6 alone. |
| C8 | `has_municipal_transit_agency` | Binary. City operates its own transit agency (vs. being served by county/regional agency). | Clean transportation scope | NTD | 🔧 PROPOSED | Analogue to has_municipal_electric. Restricts the Col 2 risk set. |

### 2c. Renewable energy compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C9 | `state_rps_stringency` | State renewable portfolio standard target × year × binding indicator. | Renewables | DSIRE database, LBNL RPS tracker | 🔧 PROPOSED | DSIRE is the standard source. LBNL publishes cleaned annual updates. |
| C10 | `has_municipal_electric` | Binary. City operates its own electric utility (vs. served by IOU or co-op). | Renewables scope | EIA Form 861 | 🟡 PARTIAL | Memo notes "PENDING" in data status table. Required for Table 2 Col 3 risk set restriction to 82-city subsample. |
| C11 | `rps_x_muni_electric` | Interaction: RPS stringency × has_municipal_electric. Binds only for municipal utilities in high-RPS states. | Renewables primary | Derived from C9 × C10 | 🔧 PROPOSED | The actual test variable. Requires both C9 and C10. |

### 2d. Energy efficiency compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C12 | `state_eers_stringency` | Energy Efficiency Resource Standard annual savings target × binding indicator. | Energy efficiency | ACEEE state scorecard, DSIRE | 🔧 PROPOSED | ACEEE publishes an annual state scorecard; EERS component extractable. |
| C13 | `state_ee_program_spend_pc` | State ratepayer-funded EE programme spending per capita. | Energy efficiency supplementary | ACEEE, EIA | 🔧 PROPOSED | Alternative to C12. |

### 2e. Green buildings compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C14 | `iecc_vintage` | Most recent IECC (International Energy Conservation Code) version adopted by state or city. | Green buildings | DOE Building Energy Codes Program | 🔧 PROPOSED | State-level for most cities; some home-rule cities adopt earlier/later. |
| C15 | `local_benchmark_ordinance` | Binary. City has a commercial building energy benchmarking ordinance in force. | Green buildings | IMT (Institute for Market Transformation) database | 🔧 PROPOSED | IMT maintains a database of ~40 cities with benchmarking ordinances. |

### 2f. Climate adaptation compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C16 | `fema_disaster_declarations_prior5yr` | Count of FEMA-declared disasters affecting the city's county in the prior 5 years. | Climate adaptation | FEMA OpenFEMA | 🔧 PROPOSED | County-level, assignable to city via county FIPS. |
| C17 | `nfip_repetitive_loss_pc` | NFIP repetitive loss property count per capita. | Climate adaptation | FEMA NFIP | 🔧 PROPOSED | Access restrictions — may need FOIA or aggregated state data. |

### 2g. Pollution control compulsion

| # | Variable | Definition | Category | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C18 | `rcra_formal_prior3yr_muni` | Rolling 3-year stock of RCRA (hazardous waste) formal enforcement against municipal facilities. | Pollution control | EPA ECHO RCRA module | ✅ READY | Already in EPA pipeline alongside NPDES. |
| C19 | `air_formal_prior3yr_muni` | Rolling 3-year stock of Clean Air Act formal enforcement against municipal facilities. | Pollution control | EPA ECHO AIR module | ✅ READY | Already in EPA pipeline. |
| C20 | `sdwa_formal_prior3yr_muni` | Rolling 3-year stock of Safe Drinking Water Act enforcement. | Secondary water compulsion | EPA ECHO SDWA module | ✅ READY | Drinking water analogue to NPDES; complements C1. |

### 2h. Pooled compulsion index

| # | Variable | Definition | Role | Source | Status | Notes |
|---|---|---|---|---|---|---|
| C21 | `compulsion_intensity_index` | Row sum or PCA first component of standardised category-specific compulsion variables (C1, C4, C6, C11, C12, C14, C16, C18). | Table 1 Col 1 single-coefficient version | Derived | 🔧 PROPOSED | Built after all category variables are in place. Presented as the headline Table 1 compulsion test. |

**Audit questions for Family 1a:**
- Which of C6–C17 are genuinely recoverable from existing datasets vs. requiring substantial new construction?
- If C7 (ADA/NEPA) and C17 (NFIP repetitive loss) are infeasible, is the remaining vector enough to support the category-matched argument?
- For C9 (RPS), confirm DSIRE coverage matches our panel years (2013–2025).
- Decide now whether any category will remain without a compulsion variable; if so, Table 2 needs to note this as a scope limit.

---

## 3. Family 1b — Fiscal-economic necessity

All variables act at Step 2 primarily but may also enter Steps 3 and 4 per the all-families-all-stages reframing.

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| F1 | `charges_to_own_source` | Enterprise fund revenue / total own-source revenue. Measures bond independence from general fund. | GFOA / Census ASLGF | ✅ READY | Primary Family 1b variable. |
| F2 | `igr_share` | Intergovernmental revenue / total revenue. | Census ASLGF | ✅ READY | Wang & Wu 2018 primary predictor. High values = high federal dependency = compressed room-to-manoeuvre. |
| F3 | `fed_igr_share` | Federal intergovernmental revenue / total revenue. | Census ASLGF | ✅ READY | Decomposition of F2. |
| F4 | `state_igr_share` | State intergovernmental revenue / total revenue. | Census ASLGF | ✅ READY | Decomposition of F2. |
| F5 | `tax_autonomy_ratio` | Own-tax revenue / total revenue. | Census ASLGF | ✅ READY | Tax capacity substitute for bond market access. Tested as alternative to F1. |
| F6 | `vfi` | Vertical fiscal imbalance = expenditures − own-source revenues, normalised. | Census ASLGF | ✅ READY | Positive on self-labelled (p = 0.049 in prior results). |
| F7 | `reserve_ratio_lag2` | 2-year lagged unrestricted fund balance / total expenditures. | Census ASLGF | ✅ READY | Fiscal capacity gate. |
| F8 | `debt_service_burden_lag2` | 2-year lagged debt service / total revenue. | Census ASLGF | ✅ READY | |
| F9 | `tel_stringency_normalized` | Tax and Expenditure Limit stringency index, normalised 0–1. | Amiel-Deller-Stallmann or own construction | ✅ READY | Note: structural zeros in 2013–2014 require 2015–2025 sample window per the TEL reversal finding. |
| F10 | `log_cwsrf_obligations_lag2` | Log, 2-year lagged, state-level CWSRF federal obligations. | USASpending FY2008–2025 | ✅ READY | 894 state-year obs, FY2008–2025. Substitute financing channel control. |
| F11 | `capital_stock_pc_lag2` | 6-year depreciated sum of real per-capita capital outlays, 2% annual depreciation, lag 2. | Census ASLGF | ✅ READY | Replaces cwns_needs_real_lag2 and pct_deficient_lag2 in preferred spec. |
| F12 | `water_sewer_capital_pc` | Water/sewer capital outlay per capita. | Census ASLGF | ✅ READY | Used in Appendix K mediation test. |
| F13 | `has_substitute_issuer` | Binary. City has access to a state bond bank, regional authority, or other conduit issuer. | Hand-coded from state bond commission records | 🟡 PARTIAL | Memo references this as a Table 3 Col 1 control; confirm completeness. |
| F14 | `fiscal_stress_pca_lag2` | First principal component of fiscal stress indicators (reserve ratio, debt service, revenue volatility). | Derived from F7, F8, additional fiscal variables | 🟡 PARTIAL | Used in Table 1 Col 5 triple interaction and Table 3 Col 3. Confirm construction matches across tables. |
| F15 | `cwns_needs_real_lag2` | Real Clean Watersheds Needs Survey estimated needs, 2-year lagged. | EPA CWNS | 🚫 DEFERRED | Excluded from preferred spec due to 2013–2014 missingness. Retained in Appendix D robustness on 2015–2025 subsample. |
| F16 | `pct_deficient_lag2` | Percent of infrastructure deficient, 2-year lagged. | EPA CWNS | 🚫 DEFERRED | Same as F15. |

**Audit questions for Family 1b:**
- Confirm F13 (has_substitute_issuer) coverage is complete for all 573 cities.
- Confirm F14 (fiscal_stress_pca_lag2) construction is documented and reproducible.
- Confirm F9 (TEL) normalisation is consistent across the 2015–2025 preferred sample and the full 2013–2025 robustness sample.

---

## 4. Family 2 — Partisan identity

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| P1 | `Rep_Mayor` | Binary. 1 if Republican mayor, 0 if Democratic. Lag 1 for capital planning cycle. | Hand-coded, ~1,824 cities, tiered evidence methodology | ✅ READY | Primary Family 2 variable. |
| P2 | `Ind_Mayor` | Binary. 1 if independent mayor, 0 otherwise. Lag 1. | Same raw file as P1 | 🔧 PROPOSED | Pending CC Task 6 implementation. Recovers Oak Park IL, Bowie MD, and others. Democrats are the omitted baseline. |
| P3 | `prob_republican` | Continuous [0, 1]. Probability the mayor is Republican based on tiered evidence (DIME CF-scores, endorsements, registration). | Hand-coded, same as P1 | ✅ READY | Continuous robustness alternative. Already accommodates independents as ~0.1 values. Does not need Ind_Mayor. |
| P4 | `Rep_Mayor_lag4` | Rep_Mayor with 4-year lag. | Derived from P1 | ✅ READY | Reverse causation check, Table 3 Col 5. |

**Audit questions for Family 2:**
- After Ind_Mayor is built, confirm the sum of Rep_Mayor + Ind_Mayor + Dem_Mayor = 1 for all city-years (no NaNs, no double-counting).
- Confirm prob_republican for all independent-mayor city-years is in the expected range (~0.05–0.25, not 0.5).

---

## 5. Family 3 — State-level modulators

**Framing:** Family 3 is a modulator family, not an independent causal channel. It splits into three sub-groups, each of which modulates one of Families 1a, 1b, and 2.

### 5a. Sub-group 3.i — Modulates Family 1a (state enforcement capacity)

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| S1 | `state_npdes_delegated_authority` | Binary or ordinal. Whether the state has primary enforcement authority for NPDES and how aggressively it exercises it. | EPA regional office records, state EPA websites | 🔧 PROPOSED | Hand-coded construction. |
| S2 | `state_coenforcement_intensity` | Count or rate of state-initiated enforcement actions alongside federal NPDES actions. | EPA ECHO state tier | 🟡 PARTIAL | Requires aggregation from existing ECHO data. |

### 5b. Sub-group 3.ii — Modulates Family 1b (market infrastructure)

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| S3 | `state_green_bond_ever_lag1` | Binary. State has ever had a green bond issuance (any issuer) prior to current year. | Bloomberg state aggregation | ✅ READY | |
| S4 | `esg_has_muni_bond_law` | Binary. State has a specific municipal green bond enabling statute. | Hand-coded from state statutes | ✅ READY | Patched via CC Task 3 for 4 consolidated city-counties. |
| S5 | `state_bond_commission` | Binary. State has a centralised bond commission reviewing municipal issuances. | State government websites | ✅ READY | Highly significant negative effect per Appendix G/H. |
| S6 | `state_green_bond_cap` | State-level aggregate green bond market size (par amount outstanding). | Bloomberg state aggregation | ✅ READY | Used in Table 3 Col 4 (Rep_Mayor × state market depth interaction). |
| S7 | `esg_aum_growth_national` | National ESG assets under management growth rate. | Morningstar / US SIF | ✅ READY | Used in Appendix I market discipline test. National, not state. |

### 5c. Sub-group 3.iii — Modulates Family 2 (political environment)

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| S8 | `state_rep_trifecta` | Binary. State has Republican governor, senate majority, and house majority. | NCSL | ✅ READY | Patched via CC Task 3 for 4 consolidated city-counties. |
| S9 | `state_antiesg_law` | Binary. State has enacted an anti-ESG law restricting green bond activity. | Hand-coded; Ropes & Gray tracker | 🟡 PARTIAL | Confirm coverage through 2025 and that the Callaway-Sant'Anna staggered DiD variable is constructed. |
| S10 | `pres_dem_vote_share` | Democratic presidential vote share in the city's precincts (most recent election). | MEDSL / Dave Leip, precinct-to-city crosswalk | ✅ READY | CC Task 1 recovered 5 cities via county-level proxy for consolidated city-counties. |
| S11 | `pres_dem_vote_share_lag2` | 2-year lagged version of S10. | Derived from S10 | ✅ READY | Used in Table 3 Col 4 electoral discipline test. |

**Audit questions for Family 3:**
- S1 (state NPDES delegated authority) and S2 (co-enforcement intensity) are the backbone of the 3.i modulator argument but are not yet built. Decide whether to construct them or reframe the 1a × 3.i interaction as "state-fixed-effects absorbed" in robustness.
- Confirm S9 (anti-ESG law) has timing of enactment coded, not just a binary ever/never.

---

## 6. City-level controls

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| X1 | `log_population_city_lag2` | Log of city population, 2-year lag. | Census ACS | ✅ READY | |
| X2 | `log_percapita_income_city_lag2` | Log of per-capita income, 2-year lag. | Census ACS | ✅ READY | |
| X3 | `unemployment_city_lag2` | Unemployment rate, 2-year lag. | BLS LAUS | ✅ READY | |
| X4 | `pct_college_educated` | Share of adults with bachelor's degree or higher. | Census ACS | 🟡 PARTIAL | Confirm inclusion in current build. |
| X5 | `pct_nonwhite` | Share of population non-white. | Census ACS | 🟡 PARTIAL | Confirm inclusion. |
| X6 | `median_home_value_lag2` | Median home value, 2-year lag. | Census ACS | 🟡 PARTIAL | Confirm inclusion. |
| X7 | `form_of_government` | Categorical. Mayor-council, council-manager, commission, town meeting. | ICMA FOG survey | 🟡 PARTIAL | Relevant for the scope condition excluding pure rotating-chair systems. |

**Audit questions for controls:**
- Confirm which of X4–X7 are in the current preferred specification vs. retained for robustness.
- If form_of_government is not yet in the panel, add it to support the scope condition footnote excluding rotating-chair cities.

---

## 7. Fixed effects and clustering

| # | Item | Specification | Status | Notes |
|---|---|---|---|---|
| FE1 | State fixed effects | All main specifications | ✅ READY | |
| FE2 | Year fixed effects | All main specifications | ✅ READY | |
| FE3 | City fixed effects | Table 3 Col 6 within-city robustness only | ✅ READY | Identified from ~8 cities that switch mayoral party. |
| FE4 | Standard errors | Clustered at city level throughout | ✅ READY | |

---

## 8. Interaction terms called for by the specifications

Interactions are constructed at estimation time from base variables. This is the checklist of which interactions each table column calls for.

### Table 1 interactions

- Col 5 Triple 1: `Rep_Mayor × npdes_formal_prior3yr_muni × fiscal_stress_pca_lag2` — the Step 2 instrumental narrowing test
- Col 5 Triple 2: `Rep_Mayor × npdes_formal_prior3yr_muni` — two-way baseline for the triple
- Col 5 Triple 3: `Rep_Mayor × fiscal_stress_pca_lag2` — two-way baseline for the triple

### Table 3 interactions

- Col 2: `Rep_Mayor × npdes_formal_prior3yr_muni` — regulatory moderation (compulsion compresses gap)
- Col 3: `Rep_Mayor × fiscal_stress_pca_lag2` — fiscal stress moderation (widens gap at Step 4, opposite sign from Table 1 Col 5)
- Col 4: `Rep_Mayor × pres_dem_vote_share_lag2` — electoral discipline failure
- Col 4 (alt): `Rep_Mayor × state_green_bond_cap` — state market depth interaction

### Appendix interactions

- Appendix I: `Rep_Mayor × esg_aum_growth_national` — market discipline failure
- Appendix B: `Rep_Mayor × [22 climate opinion items]` — constituent discipline battery
- Appendix K.2: `npdes_formal × expenditure_rigidity × Rep_Mayor` — compulsion amplifier triple

**Audit questions for interactions:**
- Confirm `expenditure_rigidity` is constructed (likely from igr_share and own-source flexibility measures) or flag as 🔧 PROPOSED.
- Confirm the 22-item climate opinion battery source and merge key.

---

## 9. Mediation and downstream outcomes (Appendix K)

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| M1 | `water_sewer_capital_pc` | See F12. Mediator in the Baron-Kenny test: NPDES → water capex → Green_Bond_Issued. | Census ASLGF | ✅ READY | |
| M2 | `expenditure_rigidity` | Index of fiscal rigidity: high igr_share, low own-source flexibility. | Derived from F1–F5 | 🔧 PROPOSED | Needed for Appendix K.2 triple interaction. |
| M3 | `investment_gap` | `capital_outlay_pc − MA5(capital_outlay_pc)_{t−1 to t−5}`. Deviation from city's own historical investment trend. | Derived from Census ASLGF capital outlay series | 🔧 PROPOSED | Appendix K.3 downstream outcome. |

---

## 10. Sample selection variables

| # | Variable | Definition | Source | Status | Notes |
|---|---|---|---|---|---|
| N1 | `in_panel` | Binary. City-year is in the 573-city preferred sample. | Derived | ✅ READY | |
| N2 | `principled_drop_reason` | Categorical. Reason for exclusion of the 5 remaining dropped cities: rotating-chair, independent, Edison-township. | Derived | 🔧 PROPOSED | Build for the Appendix robustness documentation. Will become ~2 drops after Ind_Mayor recovers independents. |
| N3 | `dc_special` | Binary indicator for DC observations (no state-level analogues). | Derived | ❓ | Memo CC Task 3 analysis concluded DC was not dropped. Confirm whether dc_special was built or is unnecessary. |
| N4 | `delegated_wastewater_flag` | Binary. City in Twin Cities Metropolitan Council or equivalent regional wastewater service area. | Hand-coded from regional authority records | 🚫 DEFERRED | Discussed and rejected in favour of the zero-fill + scope footnote approach. |

---

## 11. Summary: current status at a glance

Fill this in after working through sections 1–10.

| Family | READY | PARTIAL | PROPOSED | MISSING | DEFERRED | Total |
|---|---|---|---|---|---|---|
| Outcomes (§1) | | | | | | 13 |
| Family 1a (§2) | | | | | | 21 |
| Family 1b (§3) | | | | | | 16 |
| Family 2 (§4) | | | | | | 4 |
| Family 3 (§5) | | | | | | 11 |
| Controls (§6) | | | | | | 7 |
| Fixed effects (§7) | | | | | | 4 |
| Mediation (§9) | | | | | | 3 |
| Sample selection (§10) | | | | | | 4 |
| **Total** | | | | | | **83** |

---

## 12. Immediate priorities after the audit

Once the status columns are filled, the following questions determine the next steps:

1. **Is the category-matched compulsion vector feasible?** If fewer than 5 of the 7 categories have a viable compulsion variable (C1/C4 for water + 4 of C6/C11/C12/C14/C16/C18), the Table 1 restructure is not defensible and we fall back to the NPDES-only specification with an explicit interaction by water-category indicator.

2. **Which PROPOSED variables are hand-coded construction vs. existing dataset pulls?** Hand-coded variables are expensive. Dataset pulls (DSIRE, FEMA OpenFEMA, ACEEE scorecard, EPA ECHO RCRA/AIR) are cheap. Prioritise cheap recoveries first.

3. **Are F13 (has_substitute_issuer) and F14 (fiscal_stress_pca_lag2) fully built?** These are load-bearing variables referenced across multiple tables; if they are partial, several specifications silently lose observations.

4. **Does the panel need FOG (form of government) for the scope condition?** If yes, add to priority construction list.

5. **S1 and S2 (state enforcement capacity) — build or abandon?** If abandoned, the 1a × 3.i interaction is unsupported and the Family 3 sub-group story needs rewriting.

---

*Working audit document — Maurice Hirt, Oxford DPIR — April 2026*
