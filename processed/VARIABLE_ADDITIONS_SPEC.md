# Variable Additions Spec — "When Do Red and Blue Go Green?"
## Instruction file for Claude Code
### Panel: `processed/merged_city_year_panel.csv.gz` — 578 cities × 2013–2025

**Purpose.** This file instructs Claude Code to add, reconfigure, and robustness-check variables across the three-family empirical strategy. All changes feed into the existing analysis scripts:
- `pipeline/analysis_table1_threefamily.py`
- `pipeline/analysis_table2.py`
- `pipeline/analysis_table3.py`

Work through each section in order. After each section, run the relevant analysis script and confirm the model compiles without error before proceeding. Do **not** change the main specification columns already reported — all additions are new columns or robustness appendix tables unless explicitly marked as replacing an existing variable.

---

## Section 1 — Family 1: Material Variables

### 1.1 Informal enforcement (new robustness column, T1 and T2-water)

Add `epa_npdes_informal_actions_count_muni_lag2` to Table 1 as a robustness column alongside the primary `epa_water_violations_asinh_lag2`. Apply asinh transform before lagging:

```python
panel['epa_npdes_informal_asinh'] = np.arcsinh(panel['epa_npdes_informal_actions_count_muni'])
panel['epa_npdes_informal_asinh_lag2'] = panel.groupby('FIPS')['epa_npdes_informal_asinh'].shift(2)
```

Add to T2-water column as a secondary predictor. The hypothesis is that informal enforcement (NOVs, warning letters) predicts issuance upstream of formal actions — a positive and significant coefficient would extend the compulsion pipeline.

### 1.2 Decomposed violation types (T2-water robustness)

The current composite `epa_water_violations_asinh_lag2` combines effluent, CS, PS, and SE violations. For the T2-water column, run a robustness specification decomposing into constituent types:

```python
for vtype in ['effluent', 'cs', 'ps', 'se']:
    col = f'epa_npdes_{vtype}_violations_count_muni'
    panel[f'{col}_asinh'] = np.arcsinh(panel[col])
    panel[f'{col}_asinh_lag2'] = panel.groupby('FIPS')[f'{col}_asinh'].shift(2)
```

Run T2-water with all four violation types entered simultaneously (dropping the composite). Report in a robustness appendix table. Expected result: CS (combined sewer) violations should be the strongest predictor given their direct Capital Works Act nexus.

### 1.3 Municipal electric utility variables (T2-renewables — required)

These are the enterprise fund depth variables for the renewables category. Add to the T2-renewables column, which already restricts to the municipal electric utility subsample (N≈732):

```python
panel['ep_muni_electric_rev_asinh'] = np.arcsinh(panel['ep_muni_electric_rev_mil'].fillna(0))
panel['ep_muni_electric_rev_asinh_lag1'] = panel.groupby('FIPS')['ep_muni_electric_rev_asinh'].shift(1)
# ep_has_muni_electric is binary — use directly with lag 1
panel['ep_has_muni_electric_lag1'] = panel.groupby('FIPS')['ep_has_muni_electric'].shift(1)
```

Add both to the T2-renewables column alongside the existing `charges_to_own_source`. This completes the enterprise fund depth mechanism for the energy sector, exactly as `charges_to_own_source` does for water.

### 1.4 Building Performance Standards (T2-green buildings and T2-energy efficiency — required)

BPS adoption is the compulsion analogue for the green buildings and energy efficiency categories. These are currently the two columns with zero Republican participation and no compulsion predictor.

Variables to construct:

```python
# State-level BPS (time-varying from IMT BPS Matrix)
panel['bcode_state_bps_adopted_lag1'] = panel.groupby('FIPS')['bcode_state_bps_adopted'].shift(1)

# City-level BPS (where applicable)
panel['bcode_bps_adopted_lag1'] = panel.groupby('FIPS')['bcode_bps_adopted'].shift(1)

# IECC code vintage: years since last update (larger = more outdated = more upgrade pressure)
panel['bcode_iecc_lag_yrs_lag1'] = panel.groupby('FIPS')['bcode_iecc_lag_yrs'].shift(1)

# State weakening amendments (negative compulsion)
panel['bcode_state_weakening_amendments_lag1'] = panel.groupby('FIPS')['bcode_state_weakening_amendments'].shift(1)
```

Add `bcode_state_bps_adopted_lag1` as the primary compulsion predictor in both T2-green buildings and T2-energy efficiency. Add `bcode_iecc_lag_yrs_lag1` and `bcode_state_weakening_amendments_lag1` as controls. Test: does BPS adoption significantly predict issuance in those categories, and does the `Rep_Mayor` coefficient change in magnitude or significance when BPS is added?

### 1.5 Federal grants — IIJA and IRA (T1, T2, T3 — critical omission)

These variables are absent from all three tables despite falling squarely in the 2021–2025 panel. They must be added as controls and tested as potential alternative explanations for the partisan gap.

Construct asinh-transformed versions with lag 1:

```python
grant_vars = [
    'iija_water_grant_amt',
    'ira_eecbg_grant_amt',
    'ira_ggrf_grant_amt',
    'iija_transit_grant_amt',
    'fema_resil_grant_amt',
]
for v in grant_vars:
    panel[f'{v}_asinh'] = np.arcsinh(panel[v].fillna(0))
    panel[f'{v}_asinh_lag1'] = panel.groupby('FIPS')[f'{v}_asinh'].shift(1)
```

**Table 1:** Add `iija_water_grant_amt_asinh_lag1` to the full-specification column (Col 3) as a control. If significant and positive, it is a new material driver. If null, report explicitly in the "no economic mechanism" battery (Section 6 of the memo).

**Table 2:** Add category-matched grants: `iija_water_grant_amt_asinh_lag1` to T2-water; `ira_eecbg_grant_amt_asinh_lag1` to T2-energy efficiency; `ira_ggrf_grant_amt_asinh_lag1` to T2-green buildings; `iija_transit_grant_amt_asinh_lag1` to T2-clean transportation.

**Table 3:** Add `iija_water_grant_amt_asinh_lag1` as a material predictor in the T3 assurance model. Tests whether federal co-financing explains the assurance gap (i.e., Democrats who received IIJA grants are more likely to seek assurance).

**Critical test:** After adding grants to Table 1, check whether the `Rep_Mayor` coefficient changes. If the partisan gap narrows substantially when grants are added, the grant-access mechanism is partially explaining it. Report the coefficient comparison explicitly.

### 1.6 Climate adaptation physical risk variables (T2-climate adapt — new column)

`Y_climate_adapt` is currently absent from Table 2. Add a new column using the following predictors:

```python
# NFIP losses (time-varying, county-level)
panel['nfip_total_losses_asinh'] = np.arcsinh(panel['nfip_total_losses'].fillna(0))
panel['nfip_total_losses_asinh_lag2'] = panel.groupby('FIPS')['nfip_total_losses_asinh'].shift(2)

# FEMA flood-specific disasters (already in panel)
panel['fema_disaster_flood_lag2'] = panel.groupby('FIPS')['fema_disaster_flood'].shift(2)
```

Add `nri_inland_flooding_expected_annual_loss_building_value` as a static (time-invariant) physical risk control — no lag needed. Note coverage (~6,630 obs vs 7,514 total).

Run T2-climate adapt with: full Family 1 material spec + `nfip_total_losses_asinh_lag2` + `fema_disaster_flood_lag2` + NRI flood EAL + Family 2 political + Family 3 state. Report the `Rep_Mayor` coefficient — a smaller gap here than in discretionary categories would confirm the defensive/material mechanism is partially pulling Republicans into climate adaptation.

### 1.7 Reconfigure: bridge deficiency variable

`fn_pct_deficient_lag2` is currently in Table 1 where it is theoretically misspecified — bridge deficiency is not a predictor of general green bond issuance. Move it to the T2-clean transportation column only. Remove from Table 1 main specification (may retain in a robustness appendix).

### 1.8 Fiscal stress robustness

Add `fiscal_stress_index_lag2` to Table 1 as an additional robustness column (separate from the main specification). Already constructed in the panel (r=0.80 with `fiscal_stress_pca`, covers 2013–2023). Confirms that the fiscal necessity channel is properly controlled.

---

## Section 2 — Family 2: Political Variables

### 2.1 YCOM climate opinion controls (T1, T2, T3 — high priority)

This is the most important addition. Presidential vote share (`pres_dem_two_party_share_lag2`) is an electoral proxy for constituency preferences; YCOM opinion is the direct measure. Adding YCOM alongside vote share lets reviewers see the partisan gap survives conditioning on actual climate attitudes.

Construct the following with lag 2:

```python
ycom_vars = [
    'opinion_regulate',
    'opinion_fundrenewables',
    'opinion_happening',
    'opinion_worried',
]
for v in ycom_vars:
    panel[f'{v}_lag2'] = panel.groupby('FIPS')[v].shift(2)
```

Note: YCOM covers 2014–2023 (~6,346 obs). The 2024–2025 gap means Table 1 columns with YCOM will have a slightly smaller N. Report this explicitly; run both the full sample (without YCOM) and the YCOM-restricted sample as parallel columns so the N reduction is transparent.

**Table 1:** Add `opinion_regulate_lag2` and `opinion_fundrenewables_lag2` to the full-specification column (Col 3). These are the two most directly relevant to the green bond decision. Add `opinion_happening_lag2` as a third alternative in a robustness column.

**Table 2 (discretionary categories — clean transport, green buildings, energy efficiency):** Add `opinion_worried_lag2` as an additional constituency variable. In voluntary categories, worry/salience should be a stronger predictor than regulatory-support measures.

**Table 3:** Add `opinion_regulate_lag2` and `opinion_fundrenewables_lag2`. The assurance decision is the most voluntary — if constituency climate opinion predicts assurance beyond partisan identity, it belongs here.

**Critical check:** After adding YCOM to Table 1 Col 3, inspect whether `Rep_Mayor_lag1` and `pres_dem_two_party_share_lag2` both remain significant. The goal is to show they capture distinct variance (mayor ideology vs constituency preferences). If one absorbs the other, report and discuss.

### 2.2 Probabilistic partisanship robustness (T1 robustness column)

Add a robustness column to Table 1 replacing the binary `Rep_Mayor_lag1` with the continuous `mayor_prob_rep_lag1`. This addresses potential measurement error in the hand-coded partisanship variable, particularly for nonpartisan cities where coding relies on DIME/endorsement imputation.

```python
panel['mayor_prob_rep_lag1'] = panel.groupby('FIPS')['mayor_prob_rep'].shift(1)
panel['mayor_prob_dem_lag1'] = panel.groupby('FIPS')['mayor_prob_dem'].shift(1)
```

Report the marginal effect at the mean of `mayor_prob_rep` and compare to the binary `Rep_Mayor` coefficient. The continuous treatment should produce a more conservative (smaller in magnitude) but more precisely identified effect if the binary has measurement error.

### 2.3 ESG law intensity score (T1 and T3 — replaces binary)

Replace the binary `esg_any_antiesg_law` with the continuous `esg_law_intensity_score` in the Family 3 block (see Section 3 for reclassification). Additionally, add the interaction `Rep_Mayor_lag1 × esg_law_intensity_score` to Table 1 Col 5 (the interaction column) and to Table 3. The hypothesis: the partisan assurance gap is larger in high-intensity anti-ESG environments, so the interaction should be negative and significant.

```python
panel['esg_law_intensity_lag1'] = panel.groupby('FIPS')['esg_law_intensity_score'].shift(1)
panel['rep_x_esg_intensity'] = panel['Rep_Mayor_lag1'] * panel['esg_law_intensity_lag1']
```

### 2.4 Climate network membership (T1 interaction column and T3)

`c40_member`, `iclei_member_static`, and `mcpa_signatory_static` are direct measures of mayoral ideological commitment to climate action — distinct from partisan identity.

```python
# These are static or near-static; use as-is or with lag 1
panel['climate_commitment_lag1'] = panel.groupby('FIPS')['climate_commitment_static'].shift(1)
panel['c40_member_lag1'] = panel.groupby('FIPS')['c40_member'].shift(1)
panel['iclei_member_lag1'] = panel.groupby('FIPS')['iclei_member_static'].shift(1)
```

Add `climate_commitment_static` (combined indicator) to Table 3 as a Family 2 predictor. Test whether C40/ICLEI membership predicts assurance beyond partisan identity — Republican ICLEI members are the boundary case (moderate Republicans in climate networks). If the `Rep_Mayor` coefficient is unchanged when climate commitment is added, partisan identity operates independently of network membership.

Also add `c40_member_lag1 × Rep_Mayor_lag1` interaction to Table 1 Col 5.

### 2.5 Partisan election structure control (T1 robustness)

`fn_partisan` (whether mayoral elections are officially partisan) is a structural confounder for the treatment variable. In nonpartisan cities the partisanship coding is more reliant on imputation.

```python
panel['fn_partisan_lag1'] = panel.groupby('FIPS')['fn_partisan'].shift(1)
```

Add to Table 1 as a control. If `Rep_Mayor` is attenuated in nonpartisan cities (interaction `Rep_Mayor × fn_partisan` should be tested), this informs a coding reliability discussion.

### 2.6 Education as constituency control (T1 and T2)

`state_pct_bachelors_plus` is a proxy for both constituency composition (educated electorates more pro-climate) and investor base sophistication (educated cities attract ESG-oriented institutional investors). Currently absent.

```python
panel['state_pct_bachelors_lag1'] = panel.groupby('FIPS')['state_pct_bachelors_plus'].shift(1)
```

Add to Table 1 controls block alongside `log_percapita_income_lag2`. If it absorbs part of the `pres_dem_two_party_share` coefficient, that is informative about the constituency mechanism channel.

---

## Section 3 — Family 3: State/Multilevel Governance Variables

### 3.1 Reclassify `esg_any_antiesg_law` from F2 to F3

`esg_any_antiesg_law` is a state-level institutional variable misclassified under Family 2. Move it to the Family 3 block in the Table 1 column ordering. Replace with `esg_law_intensity_score` (continuous) as the primary variable; retain binary as robustness. This does not change the N or coefficients — only the theoretical family assignment and the column ordering in the table.

### 3.2 Democratic governor and trifecta (T1 F3, T3 — required)

The memo already notes descriptively that Republican issuers are concentrated in states with Democratic governors. This needs to become a regression variable. Add `state_dem_governor` and `state_dem_trifecta` symmetrically alongside the existing `state_rep_trifecta`:

```python
panel['state_dem_governor_lag1'] = panel.groupby('FIPS')['state_dem_governor'].shift(1)
panel['state_dem_trifecta_lag1'] = panel.groupby('FIPS')['state_dem_trifecta'].shift(1)
```

In Table 1: drop the asymmetric `state_rep_trifecta` alone and replace with a three-category or three-variable setup: `state_rep_trifecta`, `state_dem_trifecta`, `state_dem_governor` (with unified/divided as the omitted category). In Table 3: all three as F3 predictors.

### 3.3 Carbon pricing variables (T1 F3, T2-renewables, T2-energy efficiency — required)

Currently zero Family 3 climate policy variables are in the model. Carbon pricing is a direct state-level incentive that should differentially predict energy and climate categories.

```python
# Binary carbon pricing (any scheme)
panel['state_carbon_pricing_lag1'] = panel.groupby('FIPS')['state_carbon_pricing'].shift(1)

# Continuous price ($/tonne CO2e)
panel['state_carbon_price_usd_lag1'] = panel.groupby('FIPS')['state_carbon_price_usd'].shift(1)

# Scheme-specific membership
panel['state_rggi_member_lag1'] = panel.groupby('FIPS')['state_rggi_member'].shift(1)
panel['state_wci_member_lag1'] = panel.groupby('FIPS')['state_wci_member'].shift(1)
```

**Table 1:** Add `state_carbon_pricing_lag1` to Family 3 block. Test `state_carbon_price_usd_lag1` in a separate robustness column (continuous vs binary).

**Table 2 (renewables):** Add `state_rggi_member_lag1` + `state_rps_active_lag1` + `state_rps_target_pct_lag1`. RGGI membership and RPS target are the state-level compulsion analogues for the renewables category.

**Table 2 (energy efficiency):** Add `state_carbon_pricing_lag1` + `ep_state_aceee_code_rank_lag1` (ACEEE energy efficiency ranking as a proxy for the regulatory stringency environment).

**Table 3:** Add `state_carbon_price_usd_lag1` as F3 predictor. The assurance decision is most sensitive to the regulatory environment — a higher carbon price should increase the value of credible green signalling.

```python
panel['state_rps_active_lag1'] = panel.groupby('FIPS')['state_rps_active'].shift(1)
panel['state_rps_target_pct_lag1'] = panel.groupby('FIPS')['state_rps_target_pct'].shift(1)
panel['ep_state_aceee_code_rank_lag1'] = panel.groupby('FIPS')['ep_state_aceee_code_rank'].shift(1)
```

### 3.4 Underwriter block law (T1 F3, T3 — new)

`esg_has_underwriter_block` captures states that have passed laws blocking certain underwriters from municipal bond deals. This is the most direct legal barrier to green bond issuance currently absent from the model.

```python
panel['esg_underwriter_block_lag1'] = panel.groupby('FIPS')['esg_has_underwriter_block'].shift(1)
```

Note limited coverage (~215 nonzero obs, 2018–2025). Add to Table 1 F3 block and Table 3. Report nonzero N in the table notes. If the sample is too thin for stable estimation, report in a footnote rather than as a main-table variable.

### 3.5 Voter approval requirements (T1 F3 — new)

`inst_go_voter_approval_required` and `inst_go_supermajority` raise the cost of bond issuance and are the structural fiscal constraint most directly relevant to the feasibility frontier argument.

```python
panel['inst_go_voter_approval_lag1'] = panel.groupby('FIPS')['inst_go_voter_approval_required'].shift(1)
panel['inst_go_supermajority_lag1'] = panel.groupby('FIPS')['inst_go_supermajority'].shift(1)
```

Add to Table 1 Family 3 block. Revenue bonds (which green bonds typically are) may not be subject to voter approval requirements in all states — check whether `inst_revenue_bond_voter_approval` is more appropriate given the bond structure.

### 3.6 Anti-ESG institutional positions (T3 — new)

For Table 3 specifically, add the two sharper anti-ESG institutional variables. These are more precise than the binary anti-ESG law for the assurance context:

```python
panel['inst_utah_antiesg_lag1'] = panel.groupby('FIPS')['inst_signed_utah_antiesg_letter'].shift(1)
panel['inst_msrb_antiesg_lag1'] = panel.groupby('FIPS')['inst_msrb_position_anti_esg'].shift(1)
```

Add both to Table 3 Family 3 block. Given N=130, do not add both simultaneously unless the collinearity with `esg_any_antiesg_law` is low — check VIF. If collinear, test separately in alternative T3 specifications.

### 3.7 Bond bank activity vs presence distinction (T1 F3)

The existing `inst_has_bond_bank` (−0.103***) is a static presence indicator. Add `inst_bond_bank_active_2013_2025` to distinguish actively operating bond banks from historically established ones:

```python
panel['inst_bond_bank_active_lag1'] = panel.groupby('FIPS')['inst_bond_bank_active_2013_2025'].shift(1)
```

Replace `inst_has_bond_bank` with `inst_bond_bank_active_lag1` in a robustness column. If the active indicator is stronger than the presence indicator, it confirms the intermediation-substitution mechanism is driven by current activity, not historical legacy.

### 3.8 TEL × state trifecta interaction (T1 — reconfigure, do not drop)

`tel_stringency_normalized` currently drops to zero when Family 3 is added (absorbed by state-level variation). Do not drop it. Instead add the interaction `tel_stringency_normalized × state_rep_trifecta` to Table 1 Col 5 alongside the existing `Rep_Mayor × pres_dem_two_party_share` interaction:

```python
panel['tel_x_rep_trifecta'] = panel['tel_stringency_normalized'] * panel['state_rep_trifecta']
```

The hypothesis: TEL stringency constrains green bond issuance only in hostile (Republican trifecta) state environments, not in permissive ones. A negative interaction coefficient would explain the absorption pattern and strengthen the Family 3 argument.

### 3.9 State ideology orthogonal instruments (T1 F3 robustness)

Add `state_medicaid_expanded` and `state_right_to_work` as orthogonal state ideology controls — distinct from ESG-specific legislation, which could be endogenous to green bond market activity:

```python
panel['state_medicaid_expanded_lag1'] = panel.groupby('FIPS')['state_medicaid_expanded'].shift(1)
panel['state_right_to_work_lag1'] = panel.groupby('FIPS')['state_right_to_work'].shift(1)
```

Add to a Table 1 robustness column. If `Rep_Mayor` remains stable, it confirms the partisan result is not driven by general state ideology proxied through ESG legislation endogeneity.

---

## Section 4 — Controls and Outcomes

### 4.1 Intensive margin outcome (T1 new column — required)

Add a new Column 6 to Table 1 using `asinh_green_amt` as the dependent variable (OLS, unconditional, same sample as Col 3). This captures whether partisan identity also predicts the *amount* issued conditional on the material and state environment.

The sample for Col 6 is the full panel (N=4,993) — the asinh transformation handles the large number of zeros. Report the `Rep_Mayor` coefficient in dollar-equivalent terms in a footnote (back-transform the asinh coefficient at the mean nonzero amount).

Also consider a conditional OLS on issuers only (N≈130 city-years) — this is the intensive margin proper. Report as a robustness column.

### 4.2 Missing Table 2 outcomes — add three new columns

Add the following columns to Table 2 using the full three-family specification from Table 1 Col 3:

**Column: `Y_climate_adapt`** — see Section 1.6 for the predictor variables specific to this column. Use the full sample (N=4,993).

**Column: `Y_pollution_control`** — add EPA violation variables (same as T2-water) as the primary compulsion predictors. Pollution control bonds are the most direct manifestation of the EPA enforcement channel beyond water/sewer.

**Column: `Y_natural_resource`** — add NRI natural hazard variables as the primary predictors. Natural resource bonds likely reflect a different rural/environmental dimension.

For all three new columns, use the identical three-family specification and report the `Rep_Mayor` coefficient alongside the compulsion predictor. The goal is to complete the compulsion gradient across all outcome categories.

### 4.3 Urbanisation controls (T1 and T2 — new)

Add population density and principal city status to the controls block:

```python
panel['pop_density_lag2'] = panel.groupby('FIPS')['pop_density_sqkm'].shift(2)
panel['is_principal_city_lag2'] = panel.groupby('FIPS')['is_principal_city'].shift(2)
```

Add to Table 1 controls (alongside `log_population_lag2`). Add `is_principal_city_lag2` to Table 2 discretionary category columns (clean transport, green buildings, energy efficiency) — without this control the partisan gap in T2 is partially confounded by urban/suburban composition.

### 4.4 Intergovernmental revenue dependence (T1 controls — new)

```python
panel['fed_igr_share_lag2'] = panel.groupby('FIPS')['fed_igr_share'].shift(2)
panel['state_igr_share_lag2'] = panel.groupby('FIPS')['state_igr_share'].shift(2)
```

Add to Table 1 controls block as fiscal autonomy controls. Cities with high intergovernmental revenue dependence have less fiscal autonomy and may substitute federal grants for own-source capital. This interacts with the IIJA/IRA grant variables added in Section 1.5.

### 4.5 Reconfigure peer effects spillover (T1 and T2 — reconfigure)

Replace the current `log_nearby_water_25km` with the more precise `Nearby_Water_CITY_Amt_25km_Cumul` (city issuers only, 25km radius):

```python
panel['nearby_city_water_25km_asinh'] = np.arcsinh(panel['Nearby_Water_CITY_Amt_25km_Cumul'].fillna(0))
panel['nearby_city_water_25km_asinh_lag1'] = panel.groupby('FIPS')['nearby_city_water_25km_asinh'].shift(1)
```

Replace in Table 1 and T2-water. Special districts (school districts, utility districts) are theoretically distinct peer issuers and should not be conflated with municipal government peers. Retain the old variable in a robustness column to show results are robust to the spillover specification.

---

## Section 5 — Structural / Identification Issues

### 5.1 `fn_esg_has_muni_bond_law` endogeneity (T1 — flag and address)

The negative coefficient (−0.038*) on `fn_esg_has_muni_bond_law` is likely reverse causality: states passed enabling legislation because activity was low, not vice versa. Do the following:

1. Add the variable's year-of-passage (`esg_first_law_year`) to construct a pre/post indicator rather than a contemporaneous one.
2. Run Table 1 both with and without this variable; if results are unchanged, report in a footnote and note the endogeneity concern. If results change materially, address in the identification section.

### 5.2 Fisher exact test sample definition (T3 — document)

The memo notes the water-only Fisher test p-value varies between p=0.075 and p=0.014 depending on sample definition. Before submission, document both sample definitions explicitly in a code comment and a table footnote:

- Definition A (current, p=0.075): [document exact filters]
- Definition B (p=0.014): [document exact filters — likely a different year range or city coverage threshold]

Both should be reported transparently. Do not present only the more favourable p-value.

### 5.3 Table 3 sample size (T3 — robustness)

N=130 with Year FE only is the weakest identification in the paper. After adding the new Family 3 variables (Section 3.6), run three robustness specifications:

1. Year FE only (current specification)
2. State FE only (dropping year FE, which may be overfit given sparse sample)
3. No FE (just clustering on FIPS) — provides a lower bound on the partisan effect

Report all three in a robustness panel. The `Rep_Mayor` coefficient should be stable across all three for the result to be credible at a top journal.

---

## Section 6 — Output Requirements

After all additions are implemented, produce the following updated outputs:

1. **Table 1:** Minimum 6 columns (Cols 1–5 as currently specified + Col 6 intensive margin). Robustness appendix with YCOM, probabilistic partisanship, probabilistic treatment, and federal grants columns.

2. **Table 2:** Minimum 8 columns: water, clean transport, renewables, energy efficiency, green buildings, climate adapt, pollution control, natural resource. Order by compulsion intensity (water → transport → renewables → energy eff → green bldg → adapt → pollution → natural resource).

3. **Table 3:** 5 columns as currently specified + 2 robustness columns (alternative FE, probabilistic treatment).

4. **Appendix table A:** 44-moderator interaction scan updated to include the new variables added in Sections 1–3.

5. **Appendix table B:** Variable means and standard deviations for all variables added in this spec, split by `Rep_Mayor` status (parallel to any existing descriptive statistics table).

---

## Notes on implementation

- All new lag constructions should use `panel.groupby('FIPS')[var].shift(n)` — do not use simple `.shift()` which ignores the panel structure.
- Where coverage differs from the main panel (e.g. YCOM 2014–2023, NFIP full coverage, NRI static), add a note to the table footnotes reporting the effective N for that column.
- Do not alter the `Rep_Mayor_lag1` treatment variable, the `pres_dem_two_party_share_lag2` constituency variable, or any of the five existing Table 1 columns. All additions are new columns or appendix tables.
- Standard errors throughout: clustered at FIPS (city) level. Do not change clustering strategy.
- Fixed effects: Tables 1 and 2 use state + year FE. Table 3 uses year FE only. Do not change unless running the explicit robustness columns in Section 5.3.

*Working spec — Oxford DPhil research — not for circulation — April 2026*
