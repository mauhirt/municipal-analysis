# Methods Appendix and Changelog

For the response-to-reviewer letter. Documents what changed between iterations of the v3 specification, what is in the final main table, and the rationale for each decision.

---

## Final main-table specification

**Outcome variables (4):**
- `Green_Bond_Issued` — probability of any green bond issuance in the city-year
- `asinh_green_amt` — asinh-transformed total green bond amount
- `Y_self_green` — probability of self-labelled green bond issuance
- `asinh_self_green_amt` — asinh-transformed self-labelled amount

**Columns (8):** Each outcome appears twice — once without and once with the marketability interaction `npdes × state_green_cum`.

**Treatment:** `Dem_Mayor` (no lag; three-tier imputation for nonpartisan rotating-mayor cities and data-engineering gaps).

**PRIMARY regressors (10), grouped theoretically:**

| Family | Variables |
|---|---|
| Partisan / constituency | `Dem_Mayor`, `pres_dem_two_party_share_lag2` |
| Compulsion | `npdes_formal_prior3yr_muni` |
| Market / institutional | `asinh_state_all_green_cum_amt_lag1`, `fn_esg_has_muni_bond_law_post_lag1` |
| Fiscal capacity | `reserve_ratio_lag2`, `debt_service_burden_lag2` |
| Demographic controls | `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2` |

**Interaction (even columns):** `npdes × asinh_state_all_green_cum_amt_lag1`.

**Fixed effects:** state + year. **Standard errors:** clustered at city (fips7).
**Sample:** N = 6,825 city-years, 576 cities, 49 states, 2014–2025.

---

## `Dem_Mayor` three-tier imputation

Upstream panel construction (`pipeline/00_build_panel.py` §2) derives `Dem_Mayor` from `mayor_pid` only (direct coding of a named mayor's party affiliation). This leaves 150 city-years missing, concentrated in (a) cities where a separately-coded `mayor_party` variable is populated but `mayor_pid` was not, (b) single-year gaps in otherwise-coded panels, and (c) formally nonpartisan cities with rotating council-manager mayors where individual party affiliation is not available.

Three-tier imputation (`pipeline/patch_dem_mayor_imputation.py`, logic also added to `pipeline/02_variable_additions.py` §2.2b):

| Tier | Rule | Obs recovered |
|---|---|---|
| 1 | If `Dem_Mayor` missing and `mayor_party` ∈ {D, R}, fill from `mayor_party` | 97 (38 D + 59 R) |
| 2 | Within-city forward/back fill for single-year gaps | 40 |
| 3 | If all mayor-level partisan data missing, set `Dem_Mayor = 1{pres_dem_two_party_share_lag2 > 0.5}` (constituency proxy for nonpartisan cities) | 13 (Pico Rivera, CA) |

An indicator column `Dem_Mayor_imputed ∈ {0, 1, 2, 3}` is included in the panel for transparency. Robustness: excluding all Tier-1/2/3 observations does not change the null finding on `Dem_Mayor`.

---

## Variable-list evolution (changelog)

**Version 1 (initial 18-variable spec).** Included five variables that were consistently null and/or introduced significant sample restrictions: `charges_to_own_source_lag2`, `igr_share_lag2`, `tel_x_prop_tax_dep`, `capital_outlay_pc_lag2`, `has_substitute_issuer`. Sample N = 5,962 because of Census of Governments fiscal gaps on `igr_share_lag2` and `capital_outlay_pc_lag2` (both ~16% missing, zero coverage 2013–2014).

**Version 2 (13-variable lean spec).** Dropped the 5 null controls listed above. Verified inert via R22 kitchen-sink. Sample grew to N = 6,477.

**Version 3 (three-family restructure).** Reorganised 13 variables into material / political / state-institutional families per `VARIABLE_ADDITIONS_SPEC.md`. Temporarily included `fiscal_stress_index_lag2` and `state_dem_governor_lag1`. Both dropped from final main spec after testing: the composite overlaps with reserve + debt (R23 confirms ns), and the governor main effect is absorbed by state FE year-to-year residual variation (R24 confirms ns).

**Final (10-variable spec).** All variables have ≥98% panel coverage. N = 6,825 after three-tier `Dem_Mayor` imputation (see above). Robustness columns R22–R24 demonstrate the trimming is inert.

---

## Main-spec design decisions

**Why drop `tel_x_prop_tax_dep` from PRIMARY.** Under state FE, the simple binary `has_tel_binding_lag1` is not identified (0 within-state variation across 49 states). The Mullins interaction form (TEL × property-tax dependence) is identified via city-level variation in property-tax dependence, but produces only a non-significant coefficient (+0.00091, p=0.15) in the full 10-variable PRIMARY spec. Continuous `tel_stringency_index_lag1` is identified but null. Recommendation: keep Mullins interaction in fiscal robustness only (see `tel_robustness.md`), not main table.

**Why drop `fiscal_stress_index_lag2` from PRIMARY.** The composite is a z-score sum of `debt_service_burden_lag2 − reserve_ratio_lag2 + tel_x_prop_tax_dep − charges_to_own_source_lag2`. `debt_service_burden_lag2` and `reserve_ratio_lag2` are already in PRIMARY as separate variables. Including the composite alongside its components introduces collinearity (component correlation 0.30 between debt and reserves). R23 shows `Dem_Mayor` stays null when the composite replaces the components (-0.001). Composite is retained for robustness but not in main.

**Why drop state-political trifectas.** `state_dem_trifecta_lag1` and `state_rep_trifecta_lag1` have 0 within-state variation during the panel for most states, and are always null (R24 confirms -0.001). `state_dem_governor_lag1` has some year-to-year variation but is also null in every spec tested. State FE absorb the cross-sectional political variation. One state-political variable included (anti-ESG law dummy) is the more policy-relevant state-level control for this paper.

**Why the marketability interaction (`npdes × state_green_cum`) is in the main table and not `dem × npdes`.** The user explicitly wanted the labelling-mechanism story to be a **main-table** finding, not siloed in an appendix. Both `dem × state_green` (I3 demonstration, -0.024\*\*\* with +0.0011\*\*\*) and `npdes × state_green` (marketability, +0.0018\*) survive the VIF-centering test. The partisan interactions (I1–I3) are reported as a complement sub-table to preserve the partisan-null story in the main. The marketability interaction is the main-table interaction because it gives the core compulsion channel its theoretical content.

---

## Robustness sweep (24 columns)

| Block | Specs | Purpose |
|---|---|---|
| R1–R10 | YCOM, grants, probabilistic mayor, vote share, state climate policy, ESG intensity, networks, density, building codes, pooled index | Alternative constituency measures, state-climate policy, urban character |
| R11–R12 | CAA, NPDES enforcement ladder | Alternative regulatory-pressure measures |
| R13–R16 | Gravity-weighted peer, special, county, all | Local spatial spillover (all ns) |
| R17 | ESG endogeneity | State pre-law activity explains the anti-ESG suppression heterogeneity |
| R18 | Rep_Mayor_lag1 mirror | Confirms null in opposite-party framing |
| R19 | FOG × Dem | Form-of-government institutional interactions |
| R20–R21 | NPDES _locgov and _private | Ownership-tier robustness (_locgov confirms effect, _private placebo clean) |
| R22 | Kitchen-sink (all dropped vars) | Trimming is inert |
| R23 | Fiscal stress composite | Alternative fiscal representation |
| R24 | State trifectas | State-political controls |

`Dem_Mayor` null across all 24. Range -0.002 to +0.025. Always ns.

---

## Identification and inference notes

**Interaction-term VIFs.** Raw VIFs for both significant interactions (C6 demonstration and the marketability interaction) are flagged at 13–14. This is the standard mechanical correlation between X and X·Z when Z has limited variation. The centered-interaction robustness check (`interaction_vif_diagnostics.md`) demeans X and Z before constructing X·Z: VIFs drop to 1.14 and 1.13 respectively while coefficients and p-values are **identical to six decimal places**. Both findings are not collinearity artifacts.

**Common support.** For the C6 demonstration interaction, 284 Dem-mayor city-years have `asinh_state_all_green_cum_amt_lag1 = 0` (above the 200-observation threshold). Common-support requirement met.

**Clustering.** Main findings are stable under city, state, and two-way city × year clustering (Cameron-Gelbach-Miller). The state-clustered SE is approximately 1.5× the city-clustered SE, insufficient to flip significance on the core findings.

**Two-way fixed effects.** Moving to entity (city) + time (year) FE drops the within-R² of the compulsion block to near-zero, because NPDES enforcement has limited within-city time variation (cities with high enforcement tend to stay high). This is expected and not a defect — the state + year FE specification reported in the main table is the appropriate design for the cross-sectional-within-state identification strategy the paper pursues.

---

## Outstanding items deferred to the next revision

- **Callaway-Sant'Anna power for anti-ESG laws.** Only 28 self-labelled events in treated cohorts. Pre-trend and post-trend point estimates are directionally consistent with a suppression effect (−0.009 to −0.016 in post-treatment event-time) but no individual coefficient is significant. Returning to this in the next iteration would require either extending the panel (not possible with current data) or switching to a continuous-treatment design.

- **Bond-level pricing / greenium test.** The paper's greenium-seeking story (Table 3 L2: `fiscal_stress_index +0.018**`) is an indirect test. A direct greenium estimate would require bond-level yield data matched to issuer fiscal conditions. Out of scope for the current paper.

- **Callaway-Sant'Anna sensitivity** (Rambachan-Roth honest DiD). Available if a reviewer requests; package installed, results not yet generated.
