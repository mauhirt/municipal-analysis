# Provenance Audit — Every Constructed Variable

**Purpose.** This document lists every variable constructed in
`pipeline/02_variable_additions.py` that is not a direct raw-file pass-through,
and identifies its authoritative source and construction logic. Required for
peer-review compliance: no constructed variable should be usable without a
citable source.

**Audit scope.** The source files upstream of 02 (in `00_build_panel.py` and
`01_construct_audit_variables.py`) are listed in `README.md` lines 50–92
(Data sources table). This audit only covers transformations and constructions
introduced by 02.

---

## A. Direct pass-throughs from authoritative raw files (trusted)

These 02-introduced variables apply simple lag / asinh transforms to columns
sourced in 00 or 01 from documented public datasets. No new encoding.

| Variable | Upstream source column | Source file | Data authority |
|---|---|---|---|
| `epa_npdes_informal_asinh_lag2` | `npdes_informal_actions_count_muni` | `raw/epa/city_year_epa_enforcement_expanded_20260407_125920.csv` | EPA ECHO / ICIS-NPDES |
| `epa_water_violations_asinh_lag2` | sum of `npdes_{effluent,cs,ps,se}_violations_count_muni` | same | EPA ECHO / ICIS-NPDES |
| `epa_npdes_{effluent,cs,ps,se}_asinh_lag2` | respective raw columns | same | EPA ECHO / ICIS-NPDES |
| `ep_muni_electric_rev_asinh_lag1` | `revenue_millions` | `raw/energy_policy/municipal_electric_utilities.csv` | EIA Form 861 |
| `ep_has_muni_electric_lag1` | `has_municipal_electric` | same | EIA Form 861 |
| `bcode_state_bps_adopted_lag1` | `state_bps_adopted` | `raw/energy_policy/New Building Codes/master_state_year_panel_2010_2025.csv` | IMT BPS Matrix / ACEEE |
| `bcode_iecc_lag_yrs_lag1` | `lag_model_code_yrs` | same | IMT / ACEEE |
| `bcode_state_weakening_amendments_lag1` | `weakening_amendments` | same | IMT / ACEEE |
| `bcode_bps_adopted_lag1` | `bps_adopted` | `raw/energy_policy/New Building Codes/master_city_year_panel_2010_2025.csv` | IMT BPS Matrix |
| `{iija_water,ira_eecbg,ira_ggrf,iija_transit,fema_resil}_grant_amt_asinh_lag1` | respective raw columns | `raw/grants/federal_grants_panel.csv` | USASpending.gov |
| `nfip_total_losses_asinh_lag2` | `nfip_total_losses` | `raw/disasters/nfip_flood_claims.csv` | FEMA NFIP |
| `fema_disaster_flood_lag2` | `fema_disaster_flood` | `raw/disasters/fema_disaster_declarations.csv` | FEMA OpenFEMA |
| `nri_inland_flooding_eal_bv` | `Inland Flooding - Expected Annual Loss - Building Value` | `raw/nri/epa_nri.csv` | FEMA National Risk Index |
| `caa_any_criteria_nonattainment`, `caa_ozone_nonattainment_any`, `caa_ozone_nonattainment_whole`, `caa_pm25_2012_nonattainment`, `caa_pm10_nonattainment`, `caa_co_nonattainment`, `caa_so2_nonattainment`, `caa_lead_nonattainment` (plus `_lag1` / `_lag2` for each) | `pw_YYYY` columns in PHISTORY; aggregated across 8 current-NAAQS pollutants | `raw/epa_greenbook/phistory.xls` | **EPA Green Book, retrieved 2026-03-31** from https://www.epa.gov/green-book/green-book-data-download |
| `caa_ozone_class_ordinal` | `class` column in NAYRO (Marginal→Extreme mapped to 1–5) | `raw/epa_greenbook/nayro.xls` | **EPA Green Book, retrieved 2026-03-31** |
| `opinion_{regulate,fundrenewables,happening,worried}_lag2` | respective raw columns | `raw/climate/climate_opinion_ycom.csv` | Yale PCCC YCOM |
| `mayor_prob_{rep,dem}_lag1` | `prob_{republican,democrat}` | `raw/mayor/mayor_party.csv` | Hand-coded + DIME + endorsement tiered |
| `esg_law_intensity_lag1` | `esg_law_intensity_score` | `raw/political/antiesg_laws.csv` | State legislative tracking |
| `esg_underwriter_block_lag1` | `esg_has_underwriter_block` | same | State legislative tracking |
| `inst_go_{voter_approval_required,supermajority,revenue_bond_voter_approval}_lag1` | respective raw columns | `raw/institutional/state_bond_referenda_requirements.csv` | State statutes (author hand-coded) |
| `inst_utah_antiesg_lag1` | `signed_utah_antiesg_letter` | `raw/political/state_msrb_rfi_position.csv` | MSRB 2022 RFI public record |
| `inst_bond_bank_active_lag1` | `bond_bank_active_2013_2025` | `raw/institutional/state_bond_banks.csv` | State records |
| `state_{dem_governor,dem_trifecta,rep_trifecta}_lag1` | respective raw columns | `raw/political/state_political.csv` | NCSL + Ballotpedia |
| `state_carbon_pricing_lag1` / `state_carbon_price_usd_lag1` | `state_carbon_pricing` / `state_carbon_price` | `raw/climate/climate_policy_controls.csv` | DSIRE |
| `state_rps_active_lag1` / `state_rps_target_pct_lag1` | respective raw columns | same | DSIRE |
| `state_medicaid_expanded_lag1` / `state_right_to_work_lag1` | respective raw columns | `raw/census_acs/additional_city_variables_2010_2024.csv` | State legislative records |
| `pres_dem_vote_share`, `pres_rep_vote_share`, `pres_dem_two_party_share` (and their `_lag1` / `_lag2` variants for 2008-2012 and 2024-2025 years) | County-level Dem/Rep vote totals aggregated to city via `raw/crosswalk/Crosswalk.csv` `relevant_counties`; only `mode in {'TOTAL', 'TOTAL VOTES'}` rows retained | `raw/political/countypres_2000-2024.csv` | **MIT Election Data and Science Lab (MEDSL)**, County Presidential Election Returns 2000-2024, Harvard Dataverse DOI:10.7910/DVN/VOQCHQ |
| `ep_state_aceee_code_rank_lag1` | `state_building_code_stringency_aceee_rank` | `raw/energy_policy/state_building_codes.csv` | ACEEE |
| `{c40,iclei,mcpa}_member_lag1` / `mcpa_signatory_lag1` | `c40_member`, `iclei_member`, `mayors_climate_signatory` | `raw/climate/climate_policy_controls.csv` | C40 / ICLEI / MCPA public rosters |
| `state_pct_bachelors_lag1` | `state_pct_bachelors_plus` | `raw/census_acs/additional_city_variables_2010_2024.csv` | Census ACS 5-year |
| `pop_density_sqkm_lag2`, `is_principal_city_lag2`, `fed_igr_share_lag2`, `state_igr_share_lag2` | respective raw columns | various Census sources | Census ACS / ASLGF |

---

## B. Variables constructed from primary sources authored in this repository

These are new source files written as part of this analysis pipeline. Each
file carries per-row citations in its header or source column.

### B.1 `raw/policy/rggi_wci_membership.csv`

**Drives variables:** `state_rggi_member`, `state_wci_member`,
`state_rggi_member_lag1`, `state_wci_member_lag1`.

- Primary citations per row (`source` column in the CSV):
  - RGGI membership: https://www.rggi.org/program-overview-and-design/elements
  - NJ withdrawal (2012) / re-entry (2020): Gov. Christie EO-62 (2012);
    Murphy EO-7 (2018); first auction participation 2020-06.
  - VA entry (2021) / exit (2023-12-31): HB 981 (2020) + Youngkin
    regulation Reg. VAR 40:16-1651 (2024-03-25).
  - PA entry (2022) / invalidation (2023-11): 25 Pa. Code Ch. 145
    Subch. E final rule; *Shapiro v. Bowman* (Commonwealth Court 2023).
  - CA cap-and-trade: AB 32 (2006), implementation 2013;
    https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program
  - WA cap-and-invest: SB 5126 (2021), effective 2023-01-01;
    https://ecology.wa.gov/climate-commitment-act

**Construction conservatism.** PA 2023–2025 are coded 0 (program
invalidated by Commonwealth Court Nov 2023, not rescinded on appeal).
VA 2024–2025 are coded 0 (Youngkin regulatory withdrawal effective
end-2023). Any future re-entry of either state would require an
updated row with a date-stamped citation.

### B.2 `raw/policy/state_ghg_reduction_laws.csv`

**Drives variables:** `state_ghg_law_first_year`, `state_ghg_law_active`,
`state_ghg_law_active_lag1`, `state_ghg_law_years_since`.

**Scope restriction:** only **statutory, binding, economy-wide** GHG
reduction laws. Executive orders and administrative plans are excluded
because they do not survive an administration change (e.g. the MI and
NH Climate Council actions are intentionally omitted).

**Per-law citations (one row per statute):**
- CA AB 32 (2006) Cal. Health & Safety Code § 38500 et seq.
- CA SB 32 (2016) Cal. Health & Safety Code § 38566
- CT GWSA (2008) Conn. Gen. Stat. § 22a-200a
- CT Public Act 22-5 (2022) Conn. Pub. Acts 22-5
- CO HB 19-1261 (2019) Colo. Rev. Stat. § 25-7-102.8
- CO SB 21-200 (2021) Colo. Rev. Stat. § 25-7-140.5
- HI Act 234 (2007) Haw. Rev. Stat. § 342B-71
- HI Act 15 (2022) Haw. Rev. Stat. § 225P-5
- IL CEJA PA 102-0662 (2021)
- MA GWSA (2008) Mass. Gen. Laws ch. 21N
- MA Climate Roadmap Act (2021) Mass. Acts 2021 ch. 8
- MD GGRA (2009) Md. Envir. Code Ann. § 2-1201 et seq.
- MD Climate Solutions Now Act (2022) Md. Laws 2022 ch. 38
- ME LD 1679 (2019) 38 M.R.S. § 576-A
- MN HF 2 (2023) Minn. Stat. § 216B.1691
- NJ GWRA (2007) N.J. Stat. § 26:2C-37 et seq.
- NY CLCPA (2019) N.Y. Envtl. Conserv. Law § 75-0107
- OR HB 3543 (2007) Or. Rev. Stat. § 468A.205
- OR HB 2021 (2021) Or. Rev. Stat. § 469A.410
- RI Act on Climate (2021) R.I. Gen. Laws § 42-6.2
- VT GWSA (2020) 10 V.S.A. § 592
- WA CCA SB 5126 (2021) Wash. Rev. Code § 70A.65

Cross-referenced against: **Georgetown Climate Center State Climate Policy
Maps** and **LSE Grantham Research Institute Climate Change Laws of the
World Database**.

### B.3 `raw/policy/state_zev_mandate.csv`

**Drives variables:** `state_zev_adoption_year`, `state_zev_mandate_active`,
`state_zev_mandate_active_lag1`.

**Scope:** states that have adopted California's ZEV rules via Section 177
of the Clean Air Act (42 U.S.C. § 7507). NC is excluded (adopted clean-car
rules but rescinded before ZEV applicability). The file records adoption
year (state-level rulemaking final) and first compliance model year.

**Per-state regulatory citations:**
- CA: Title 13 CCR § 1962.4 (Advanced Clean Cars I/II), from 1990 ZEV
  regulation; current Advanced Clean Cars II finalized 2022.
- NY: 6 NYCRR Part 218
- NJ: N.J.A.C. 7:27-29
- MA: 310 CMR 7.40
- VT: VT Air Pollution Control Regulation § 5-1106
- ME: 06-096 CMR ch. 127
- CT: CT HB 5223 (2004) (Section 177 adoption); CT HB 6688 (2022) updates
- RI: 250-RICR-120-05-23
- OR: OAR 340-257
- WA: WAC 173-423
- MD: COMAR 26.11.34
- DE: 7 DE Admin. Code 1140
- CO: 5 CCR 1001-24
- MN: Minnesota Clean Cars Rule (2021)
- NM: NMAC 20.2.89
- NV: NAC 445B Clean Cars Nevada
- VA: 9VAC5-172

Cross-referenced against: **CARB Section 177 State Tracking**, **ICCT US ZEV
Regulation Tracker**, **NESCAUM**.

---

## C. Variables derived from authoritative upstream sources (transparent composition)

These are compositions (sums, maxes, indicators, products) of variables
already sourced authoritatively. The derivation logic is documented inline
in the code; no new source attestation required beyond the components.

| Variable | Derivation | Uses components from |
|---|---|---|
| `climate_commitment_static` | `OR(c40_member, iclei_member, mayors_climate_signatory)` | DSIRE + C40 + ICLEI + MCPA |
| `Y_natural_resource` | `(Count_ESG Project Categories__*Natural_Resource* OR *Biodiversity* OR *Land_Use*) > 0` | Bloomberg Terminal |
| `fn_esg_has_muni_bond_law_post` | `year >= esg_first_law_year` | Anti-ESG law database |
| `Y_climate_adapt`, `Y_pollution_control` | Aliases of `Y_Climate_Change_Adaptation` / `Y_Pollution_Control` | Bloomberg Terminal |
| `epa_water_violations_count_muni` | Sum of 4 NPDES violation types (effluent + CS + PS + SE) | EPA ECHO |
| `tel_x_prop_tax_dep`, `tel_x_charges` | Products of `tel_stringency_normalized` × city-level fiscal partner | ACIR TEL + Census ASLGF |
| `rps_target_x_muni_electric` | `state_rps_target_pct_lag1 × ep_has_muni_electric_lag1` | DSIRE × EIA Form 861 |
| `rep_x_esg_intensity` | `Rep_Mayor_lag1 × esg_law_intensity_lag1` | Hand-coded mayor + ESG-law DB |
| `tel_x_rep_trifecta` | `tel_stringency_normalized × state_rep_trifecta` | ACIR × NCSL |
| `c40_x_rep_mayor` | `c40_member_lag1 × Rep_Mayor_lag1` | C40 × hand-coded mayor |
| `rep_x_fn_partisan` | `Rep_Mayor_lag1 × fn_partisan_lag1` | Hand-coded mayor × ICMA FOG |
| `rep_x_fed_igr_share` | `Rep_Mayor_lag1 × fed_igr_share_lag2` | Hand-coded mayor × Census ASLGF |
| `rep_x_pres_dem_share` | `Rep_Mayor_lag1 × pres_dem_two_party_share_lag2` — electoral-discipline interaction (T1 symmetric with T3 Col 4) | Hand-coded mayor × MIT MEDSL |
| `dem_x_pres_dem_share` | `Dem_Mayor × pres_dem_two_party_share_lag2` — Part D mirror using the new primary treatment | Hand-coded mayor × MIT MEDSL |
| `pres_rep_minus_dem_share`, `pres_rep_minus_dem_share_lag2` | `pres_rep_vote_share − pres_dem_vote_share` signed margin (Part D user request) | MIT MEDSL |
| `Dem_Mayor`, `Dem_Mayor_L1` | Indicator for D vs. (R ∪ I); constructed in `00_build_panel.py` §2 from `mayor_pid == 'D'`. Primary treatment per Part D spec (drops Ind from analysis); used WITHOUT lag because the year following an election is coded as the mayor's first year in office, effectively lagging the variable by construction | `raw/mayor/mayor_party.csv` (hand-coded + DIME + endorsement) |
| `mayor_vote_share_win`, `mayor_margin_victory`, `mayor_win_is_dem`, `mayor_win_is_rep`, `mayor_win_prob_democrat`, `mayor_win_prob_republican`, `mayor_win_cfscore`, `mayor_vote_share_total` | Built in `00_build_panel.py` §2b from the MayoralCandidates270326.xlsx file by filtering `winner==1` and merging margin-of-victory (winner_share − runner-up_share). Effective-year convention: election year + 1. Forward-filled between elections. | `raw/mayor/MayoralCandidates270326.xlsx` (Harvard Dataverse municipal-elections dataset, 2001-2025, 8,255 candidates × 576 cities × ~3,505 winning elections) |
| `state_self_green_cum_count_lag1` | Per-state cumulative count of city-year `Y_self_green == 1` up to year t-1 | Bloomberg Terminal |
| `state_rep_self_green_cum_count_lag1` | As above, restricted to cities with `Rep_Mayor_lag1 == 1` (co-partisan spillover) | Bloomberg × hand-coded mayor |
| `state_any_self_green_lag1`, `state_any_rep_self_green_lag1` | Binary flags derived from the cumulatives above | Same as above |
| `rep_x_state_any_green`, `rep_x_state_self_green_cum`, `rep_x_state_rep_green`, `rep_x_state_rep_green_cum` | `Rep_Mayor_lag1 ×` each spillover variable — tests whether market maturity (all / self-labelled / co-partisan) pulls Republican mayors into issuance | Bloomberg × hand-coded mayor |
| `state_green_cum_x_rep` | `asinh_state_all_green_cum_amt_lag1 × Rep_Mayor_lag1` (Part E1 user-spec formula) — market-normalisation vs sticky-identity test using all-issuer dollar amount | Bloomberg × hand-coded mayor |
| `esg_cum_antiesg_laws_lag1` | lag-1 of `esg_num_antiesg_laws` (raw column is already a state-year cumulative count, since anti-ESG laws only accumulate) | `raw/political/antiesg_laws.csv` |
| `years_since_esg_law` | `year − esg_first_law_year` (0 if pre-enactment or state has no law). Suppression-decay test | `raw/political/antiesg_laws.csv` |
| `state_pre_esg_activity` | 1 if a state's city-level self-labelled green-bond cumulative was > 0 at any panel year BEFORE that state's first anti-ESG-law year; state-constant. Addresses memo §5.1 endogeneity: suppression should be concentrated in states with pre-law markets to suppress, not spread evenly across already-quiescent states | Bloomberg (self-green) × `raw/political/antiesg_laws.csv` (first law year) |
| `esg_post_x_pre_activity`, `esg_post_lag1_x_pre_activity`, `esg_years_since_x_pre_activity` | Interactions testing whether anti-ESG law effect is concentrated in states with prior market activity (genuine suppression) vs. spread evenly (spurious) | Same as above |
| `rep_x_bond_commission`, `rep_x_state_approval_body` | `Rep_Mayor_lag1 ×` institutional gatekeeper — cross-sectional heterogeneity tests | Hand-coded mayor × `raw/institutional/state_bond_referenda_requirements.csv` + `raw/institutional/state_bond_banks.csv` |
| `fiscal_stress_x_bond_commission` | `fiscal_stress_index_lag2 × has_state_bond_commission` — stressed cities × institutional gatekeeper | Census ASLGF × state-statute coding |
| `dem_x_bond_commission`, `ghg_law_x_bond_commission` | Additional bond-commission interactions with Dem_Mayor and state GHG law | Hand-coded mayor / raw/policy/state_ghg_reduction_laws.csv × state-statute coding |
| `capital_outlay_pc_lag2`, `capital_outlay_real_lag2`, `capital_share_lag2` | Lag-2 of Census ASLGF deflated per-capita / real / share variants (J26–J28 in the fiscal-constraint variables doc) | Census ASLGF |
| `igr_share_lag2`, `vfi_lag2`, `fiscal_self_sufficiency_lag2`, `expenditure_gap_pc_lag2`, `rating_agency_composite_lag2`, `net_borrowing_intensity_lag2`, `net_borrowing_ratio_lag2`, `high_fiscal_stress_lag2` | Standard lag-2 of Census-ASLGF-derived variables cited in `fiscal_constraint_variables_updated.docx` (D1, I9, I10, I11, H3, E8, J51, H4) | Census ASLGF |

---

## D. Pooled compulsion indices

### D.1 `compulsion_index_z` (equal-weighted z-score composite)

**Construction:** sum of standardised (z-score) transforms of five compulsion
components, covering both regulatory and physical-risk channels.

```
compulsion_index_z = z(npdes_formal_prior3yr_muni)
                   + z(asinh(npdes_informal_actions_count_muni))
                   + z(case_jdc_prior3yr_muni)
                   + z(sdwa_formal_prior3yr_muni)
                   + z(fema_disaster_flood_lag2)
```

All five components are from authoritative sources (EPA ECHO + FEMA
OpenFEMA). Equal-weighting is a modelling choice defensible under peer
review as the most interpretable aggregation that imposes no component
priority beyond presence.

### D.2 `compulsion_index_count` (step-count ladder)

**Construction:** count of how many of the five compulsion components are
positive in a given city-year. Values 0–5, with 0 meaning no compulsion of
any kind observed in the lookback window. Interpretable alternative to
the continuous z-score index.

### D.3 `compulsion_index_pca` (PCA first component, robustness)

**Construction:** first principal component of the five z-scored components,
via `sklearn.decomposition.PCA(n_components=1)`. Explained variance ratio
reported in the build log. Serves as a robustness check that the equal-
weighted composite is not driven by an arbitrary weighting choice.

### D.4 `water_compulsion_ladder` (ordinal within-water hierarchy)

**Construction:** ordinal 0–3 coding the highest level of water-related
EPA enforcement observed against city-owned facilities in the prior 3 years:

- 0: no enforcement of any kind
- 1: informal enforcement only (NOVs, warning letters)
- 2: formal enforcement (administrative orders, consent agreements)
- 3: judicial consent decree (`case_jdc_prior3yr_muni` > 0)

All three levels are from the same EPA ECHO / ICIS-NPDES source (memo-
authoritative); the ordinal structure reflects the memo's enforcement
ladder (Tier 1 broad pressure → Tier 4 judicial).

---

## E. Data gaps explicitly flagged (not fabricated)

| Variable | Reason | Next step |
|---|---|---|
| ~~EPA CAA county-level nonattainment~~ | **RESOLVED 2026-04.** Green Book phistory.xls + nayro.xls retrieved; merged into 00_build_panel.py §6b. See Section A above for the derived `caa_*` variables. | Done |
| ~~`capital_outlay`~~ | **RESOLVED 2026-04.** Panel already had `capital_outlay_pc` / `capital_outlay_real` / `capital_share` from Census ASLGF; lag-2 variants now built in `02_variable_additions.py` §4.4c. | Done |
| `pct_deficient_lag2` | Source data deferred in `variable_list_audit.md` (EPA CWNS unavailable) | Flagged as data gap |
| ~~Pre-2013 presidential vote share (2008-2012)~~ | **RESOLVED 2026-04.** `raw/political/countypres_2000-2024.csv` retrieved from MIT MEDSL; merged in `00_build_panel.py` §12b via county→city aggregation using `raw/crosswalk/Crosswalk.csv`. Presidential lag-2 variables now have full 2013-2025 coverage (was missing for 2013-2014 before this pull). | Done |
| `Nearby_Water_CITY_Amt_25km_Cumul` | Requires geospatial aggregation not yet run | Geospatial build pending |
| `Y_Mgmt_Proceeds_Yes`, `Y_Proj_Selection_Yes` | Bloomberg `Count_Mgmt of Proc__Yes` / `Count_Proj Sel Proc__Yes` not derived in `01` | Add construction step to `01_construct_audit_variables.py` |
| `esg_cum_antiesg_laws` | In `raw/political/antiesg_laws.csv` but dropped by 01 pruning | Add to retain list |

---

## F. Peer-review checklist

- ✅ All hand-coded state-year values (RGGI/WCI, GHG laws, ZEV) live in
  `raw/policy/` with per-row source citations rather than hard-coded in
  analysis code.
- ✅ All source CSV files include file-header comment blocks documenting
  authority, scope, and encoding decisions (e.g., PA 2023 conservatism).
- ✅ No constructed variable's value is opaque — either it is a sum of
  authoritatively sourced components, a product / lag / transform thereof,
  or it is drawn from a `raw/` file whose header cites a URL or statute.
- ✅ Data gaps are documented (Section E) rather than filled with synthetic
  values.
- ⚠️ The `fiscal_stress_pca` variable stops in 2021; the primary analysis
  uses `fiscal_stress_index_lag2` which runs through 2025. Robustness with
  `fiscal_stress_pca` drops observations for 2022+; document this in any
  paper draft.
- ⚠️ Mayoral partisanship (`Rep_Mayor`, `mayor_prob_rep`) is hand-coded by
  the memo author from voter registration, DIME CF-scores, and endorsements
  across 1,824 cities. This is authoritative by construction but downstream
  code should not describe it as an external dataset.
