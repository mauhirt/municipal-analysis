# Methods Appendix: Fiscal Constraint Variable Construction

## Municipal Green Bond Issuance Analysis (2013–2023)

Maurice Hirt, University of Oxford — February 2026

---

## 1. Dataset Overview

| Property | Value |
|----------|-------|
| **File** | `fiscal_tel_merged_2007_2024.csv` |
| **Dimensions** | 10,404 rows × 1,022 columns |
| **Entities** | 578 U.S. municipalities |
| **Time span** | 2007–2024 (18 years) |
| **Analysis window** | 2013–2023 (post-Census format change) |
| **Primary unit** | Municipality-year |
| **Entity identifier** | `entity_id` (FIPS7 code) |

### Data Sources

| Source | Columns | Years |
|--------|---------|-------|
| Census ASLGF Historical Individual Unit Files | ~550 | 2007–2012 |
| Census ASLGF Current Individual Unit Files | ~550 | 2012–2023 |
| Advisory Commission on Intergovernmental Relations (ACIR) TEL panel | 11 | 2007–2023 |
| ACS/BLS county & city economic indicators | ~60 (+ lags) | 2007–2023 |
| ICMA Forms of Government survey (FOG) | 15 | Time-invariant |
| BEA Price Index (Y650RG3A086NBEA) | 2 | 2007–2024 |
| **Constructed fiscal constraint variables** | **102** | **2007–2023** |

---

## 2. Variable Construction Framework

The 102 constructed variables map to the six evaluation pillars used by credit rating agencies (Moody's, S&P, Fitch) plus fiscal federalism dimensions (Rodden, 2004), standard controls, and composite indices. Each variable is assigned a pillar-specific ID.

### Key Substitutions

Three Census aggregate variables available only in historical files (2007–2012) were substituted for the current period (2013–2023):

| Historical Variable | Substitute | Verification |
|---------------------|-----------|-------------|
| `interest_on_gen_debt` (#195) | `general_debt_interest` (#152) | Exact match at 2012 (r = 1.000, max diff = $0) |
| `total_cash_&_securities` − `insur_trust_cash_&_sec` | `nonin_trust_cash_&_sec` (#346) | Exact match at 2012 (max diff = $0) |
| `emp_ret_total_expend` (#93) | `pension_benefit_payments` (#688) | Stitched; see note below |

**Pension expenditure note:** `emp_ret_total_expend` (historical) captures both pension benefit payments and employer contributions for city-administered systems. `pension_benefit_payments` (current) covers only benefit payments from self-administered funds. Coverage drops from ~34% of entities (historical) to ~11% (current) because most municipalities participate in state-administered pension systems that do not report through Census item codes. Variables using this input (A4, E5, E7, J64, J65) are sparse for 2013+ and should be interpreted as lower-bound estimates of pension burden.

### Deflation and Per-Capita Normalisation

- **Price deflator:** BEA Price Index for State & Local Government Gross Investment (Y650RG3A086NBEA), rebased to 2012 = 100. Stored as `deflator_factor` (#892), where `real_value = nominal_value × deflator_factor`.
- **Population:** Unified population series `pop_unified` (#890), stitching Census fiscal `population` (2007–2009) with ACS `population_city` (2010–2023).
- **Per-capita convention:** All fiscal data are reported in **thousands of dollars** (Census convention). Per-capita values are therefore in $1,000s per capita (e.g., `tax_effort_pc = 3.23` means $3,230 per capita).

### Winsorisation

All continuous ratio variables are winsorised at the 1st and 99th percentiles within each year to limit the influence of extreme outliers while preserving cross-sectional variation.

### Functional Expenditure Stitching

Several functional expenditure totals have different column names in historical vs. current Census formats. These were stitched using the historical column for 2007–2012 and the current column for 2013+:

| Function | Historical Column | Current Column | Note |
|----------|------------------|----------------|------|
| Police | `police_prot_total_exp` | `police_prot_total_expend` | Slight level difference at 2012 overlap due to E+F+G reconstruction |
| Highways | `total_highways_tot_exp` | `regular_hwy_total_exp` | Current excludes toll highways (very sparse for cities) |
| Sewerage | `sewerage_total_expend` | `sewerage_total_exp` | — |
| Solid waste | `sw_mgmt_total_expend` | `solid_wst_curr_oper` | Current = operating only (75% coverage); capital component unavailable |
| Health + Hospitals | `health_total_exp` + `total_hospital_total_exp` | `health_total_exp` | Hospital expenditure unavailable for 2013+ |

---

## 3. Pillar A — Budgetary Flexibility

Rating agencies assess the demonstrated and legal ability to raise revenues or cut spending. These variables capture both the revenue ceiling (tax effort, tax reliance) and the expenditure floor (mandatory spending rigidity).

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| A1 | `tax_effort_pc` | `(total_taxes × deflator_factor) / pop_unified` | 99% |
| A2 | `tax_effort_pc_3yr` | 3-year rolling mean of A1 within entity | 99% |
| A3 | `tax_to_rev` | `total_taxes / total_revenue` | 99% |
| A4 | `expenditure_rigidity` | `(general_debt_interest + pension_benefit_payments + public_welf_total_exp) / direct_expenditure` | 99%* |
| A5 | `budget_flexibility_squeeze` | `tax_to_rev × expenditure_rigidity` | 99% |

*A4 note: For 2013+, only `general_debt_interest` has near-full coverage. The pension and welfare components are sparse/absent, making this a debt-service-dominated rigidity measure for the current period. For 2007–2012, all three components are available.

---

## 4. Pillar B — Liquidity & Reserves

Rating agencies evaluate near-term shock-absorption capacity. GFOA recommends a minimum of two months' reserves (~16.7% of expenditures).

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| B1 | `reserve_ratio` | `max(nonin_trust_cash_&_sec, 0) / direct_expenditure` | 99% |
| B2 | `reserve_months` | `reserve_ratio × 12` | 99% |
| B3 | `low_reserves` | `1 if reserve_months < 2` | 99% |
| B4 | `days_cash` | `nonin_trust_cash_&_sec / (direct_expenditure / 365)` | 99% |
| B5 | `liquidity_tier` | Strong (≥180d), Adequate (90–179d), Weak (30–89d), Vulnerable (<30d) | 99% |
| B6 | `reserve_change_1yr` | `reserve_ratio − lag(reserve_ratio, 1)` | 99% |
| B7 | `reserve_change_3yr` | `reserve_ratio − lag(reserve_ratio, 3)` | 99% |
| B8 | `reserve_declining` | `1 if reserve_change_1yr < 0` | 99% |
| B9 | `reserve_decline_streak` | Consecutive years where `reserve_change_1yr < 0` | 99% |
| B10 | `reserve_ratio_3yr` | 3-year rolling mean of B1 | 99% |

**Construction note for B1:** Census data does not map to GAAP unrestricted fund balance. `nonin_trust_cash_&_sec` (= total cash & securities minus insurance trust holdings) approximates unrestricted funds available for general operations. Validated as an exact match for `total_cash_&_securities − insur_trust_cash_&_sec` at the 2012 overlap.

---

## 5. Pillar C — Revenue Framework

Rating agencies judge the predictability and stability of the revenue base.

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| C1a | `share_property` | `property_tax / gen_rev_own_sources` | 99% |
| C1b | `share_sales` | `total_gen_sales_tax / gen_rev_own_sources` | 56% |
| C1c | `share_income` | `total_income_taxes / gen_rev_own_sources` | 99% |
| C1d | `share_charges` | `total_general_charges / gen_rev_own_sources` | 99% |
| C1 | `revenue_hhi` | `share_property² + share_sales² + share_income² + share_charges²` | 99% |
| C2 | `property_tax_dependence` | `property_tax / total_taxes` | 99% |
| C3 | `tax_revenue_volatility` | Rolling 3yr SD of `(total_taxes − lag) / lag` | 100% |
| C4 | `own_source_rev_share` | `gen_rev_own_sources / general_revenue` | 99% |

**HHI interpretation:** Values range from 0.25 (perfectly diversified across four sources) to 1.0 (single-source). Municipalities above 0.5 face meaningful concentration risk. C1b (`share_sales`) is NaN for municipalities that do not levy a general sales tax.

---

## 6. Pillar D — Intergovernmental Aid Dependence

Rating agencies flag exposure to policy risk from state and federal budget decisions.

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| D1 | `igr_share` | `total_ig_revenue / total_revenue` | 99% |
| D2 | `fed_igr_share` | `total_fed_ig_revenue / total_revenue` | 99% |
| D3 | `state_igr_share` | `total_state_ig_revenue / total_revenue` | 99% |
| D4 | `aid_volatility` | Rolling 3yr SD of `(total_ig_revenue − lag) / lag` | 100% |
| D5 | `aid_growth_trend` | `(total_ig_revenue − lag(3)) / lag(3)` | 99% |

D1–D3 were constructed in a prior merge step; D4–D5 are new.

---

## 7. Pillar E — Long-Term Liabilities

Rating agencies measure long-term burdens that reduce future fiscal flexibility. **E1 (`debt_service_burden`) is the recommended primary replacement for `TaxToRev` in the Rep_Mayor interaction model.**

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| E1 | `debt_service_burden` | `general_debt_interest / gen_rev_own_sources` | 99% |
| E2 | `debt_affordability` | `total_long_term_debt_out / gen_rev_own_sources` | 99% |
| E3 | `debt_to_revenue` | Already in dataset (#910) | 99% |
| E4 | `debt_pc` | Already in dataset (#909) | 99% |
| E5 | `pension_expenditure_burden` | `pension_expend / total_revenue` | 11%** |
| E7 | `combined_liability_burden` | `(total_long_term_debt_out + pension_expend × 10) / total_revenue` | 99% |
| E8 | `net_borrowing_intensity` | `(total_ltd_issued − total_ltd_retired) / total_revenue` | 99% |
| E9 | `dsb_change_1yr` | `debt_service_burden − lag(1)` | 99% |
| E10 | `dsb_change_3yr` | `debt_service_burden − lag(3)` | 99% |
| E11 | `dsb_worsening` | `1 if dsb_change_1yr > 0` | 99% |

**E6 (`pension_funded_ratio_proxy`) NOT FEASIBLE:** `emp_retire_cash_&_sec` is available only for 2007–2012. A proper funded ratio requires actuarial data from the Public Plans Database or individual CAFRs.

**E5 sparse coverage: Most municipalities participate in state pension systems. Census item codes only capture benefit payments from city-administered funds (~11% of entities for 2013+). For E7, the pension component defaults to 0 where unavailable, making it a debt-only measure for most entities.

---

## 8. Pillar F — Legal/Institutional Constraints

Tax and expenditure limitations (TELs) are state-imposed constraints on local fiscal autonomy.

### Pre-Existing TEL Variables (from ACIR panel)

| # | Variable | Description |
|---|----------|-------------|
| F1 | `tel_overall_rate_limit` (#753) | Binary: overall property tax rate limit |
| F2 | `tel_specific_rate_limit` (#754) | Binary: specific rate restriction |
| F3 | `tel_levy_limit` (#755) | Binary: cap on total property tax levy |
| F4 | `tel_assessment_limit` (#756) | Binary: limit on assessed value growth |
| F5 | `tel_general_revenue_limit` (#757) | Binary: cap on general revenue growth |
| F6 | `tel_general_expenditure_limit` (#758) | Binary: cap on total expenditure growth |
| F7 | `tel_full_disclosure` (#759) | Binary: transparency requirement |
| F8 | `tel_stringency_simple` (#760) | Composite: simple sum |
| F9 | `tel_stringency_ads` (#761) | Composite: ADS weighting |
| F10 | `tel_stringency_normalized` (#762) | Normalised 0–1 index (primary TEL variable) |
| F11 | `tel_stringency_category` (#763) | Categorical: None/Low/Medium/High |

### New Interaction Variables

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| F12 | `tel_x_tax_effort` | `tel_stringency_normalized × tax_effort_pc` | 99% |
| F13 | `tel_x_dsb` | `tel_stringency_normalized × debt_service_burden` | 99% |

---

## 9. Pillar G — Market/Security Structure

GO vs. revenue bond composition affects recovery assessment and green-label strategy.

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| G1 | `go_bond_share_outstanding` | `ltd_out_general / total_long_term_debt_out` | **0%** |
| G2 | `go_bond_share_issuance` | `ltd_iss_general / total_ltd_issued` | **0%** |

**Historical only (2007–2012):** `ltd_out_general` and `ltd_iss_general` are not available in the current Census item-code structure. GO/revenue bond breakdowns require external data (e.g., Mergent MBSD, Bloomberg) for 2013+.

---

## 10. Pillar H — Composite Indices

Single-variable measures are subject to measurement error. Composite indices combine multiple dimensions of fiscal weakness into a single latent measure.

### H1: Standardised Additive Index (`fiscal_stress_index`)

Within-year z-scores of five components, all coded so higher = more fiscal stress:

| Component | Source Variable | Coding |
|-----------|----------------|--------|
| Debt service burden | `debt_service_burden` (E1) | z-score (higher = more stress) |
| Debt affordability | `debt_affordability` (E2) | z-score |
| Inverted reserves | `−reserve_ratio` (B1) | z-score of negated value |
| Inverted operating balance | `−operating_balance` (H7) | z-score of negated value |
| Debt-to-revenue | `debt_to_revenue` (#910) | z-score |

Mean of available components, requiring ≥ 3 non-missing. Coverage: 99% (2013+).

### H2: PCA-Based Index (`fiscal_stress_pca`)

First principal component extracted from the same five standardised inputs:

| Loading | Value |
|---------|-------|
| Debt affordability (z_da) | 0.551 |
| Debt-to-revenue (z_dtr) | 0.536 |
| Debt service burden (z_dsb) | 0.496 |
| Inverted reserves (z_inv_res) | −0.381 |
| Inverted operating balance (z_inv_op) | 0.134 |
| **Variance explained** | **54.5%** |

PC1 loads positively on all debt measures and negatively on reserves, confirming a single latent "fiscal stress" dimension. Signed so that higher values = more stress. Coverage: 81% (requires all 5 inputs simultaneously).

### H3: Rating-Agency-Aligned Composite (`rating_agency_composite`)

Extends H1 to cover all six pillars where feasible:

| Component | Source | Coding |
|-----------|--------|--------|
| DSB | `debt_service_burden` (E1) | z-score |
| Inverted reserves | `−reserve_ratio` (B1) | z-score |
| Revenue concentration | `revenue_hhi` (C1) | z-score |
| Aid dependence | `igr_share` (D1) | z-score |
| Expenditure rigidity | `expenditure_rigidity` (A4) | z-score |
| TEL stringency | `tel_stringency_normalized` (F10) | z-score |

Mean of z-scores, requiring ≥ 3. Coverage: 99%.

### Binary and Categorical Variables

| # | Variable | Formula | Coverage |
|---|----------|---------|----------|
| H4 | `high_fiscal_stress` | `1 if fiscal_stress_index > 75th percentile` (by year) | 99% |
| H5 | `fiscal_stress_tercile` | Tercile of `fiscal_stress_index` (by year): 1, 2, 3 | 99% |
| H6 | `operating_deficit` | `1 if (general_revenue − general_expenditure) < 0` | 99% |
| H7 | `operating_balance` | `(general_revenue − general_expenditure) / general_revenue` | 99% |
| H8 | `operating_balance_3yr` | 3-year rolling mean of H7 | 99% |

---

## 11. Pillar I — Fiscal Federalism / Decentralisation

Operationalises Rodden (2004) dimensions of fiscal autonomy at the municipal level.

### I.1 Revenue Autonomy

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I1 | `revenue_autonomy` | `1 − igr_share` | 99% |
| I2 | `tax_autonomy_ratio` | `total_taxes / total_revenue` | 99% |
| I3 | `tax_to_own_source` | `total_taxes / gen_rev_own_sources` | 99% |
| I4 | `charges_to_own_source` | `total_general_charges / gen_rev_own_sources` | 99% |

### I.2 Tax Structure

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I5 | `property_tax_share` | `property_tax / total_taxes` | 99% |
| I6 | `sales_tax_share` | `total_gen_sales_tax / total_taxes` | 56% |
| I7 | `income_tax_share` | `total_income_taxes / total_taxes` | 99% |
| I8 | `tax_hhi` | `Σ share_i²` across property, sales, income, other | 99% |

I6 is NaN for municipalities that do not levy a sales tax. I8 uses a four-category decomposition (property, sales, income, other = residual).

### I.3 Vertical Fiscal Imbalance

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I9 | `vfi` | `1 − (gen_rev_own_sources / direct_general_expend)` | 99% |
| I10 | `fiscal_self_sufficiency` | `gen_rev_own_sources / direct_general_expend` | 99% |
| I11 | `expenditure_gap_pc` | `(direct_general_expend − gen_rev_own_sources) × deflator_factor / pop_unified` | 99% |

### I.4 Grant Composition

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I12 | `fed_grant_share_of_grants` | `total_fed_ig_revenue / total_ig_revenue` | 99% |
| I13 | `state_grant_share_of_grants` | `total_state_ig_revenue / total_ig_revenue` | 99% |
| I14 | `local_ig_share_of_grants` | `tot_local_ig_rev / total_ig_revenue` | 99% |

### I.5 Expenditure Structure

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I15 | `ig_exp_share` | `total_ig_expenditure / total_expenditure` | **0%** (historical only) |
| I16 | `direct_exp_share` | `direct_expenditure / total_expenditure` | 99% |

### I.6 Borrowing & Debt Structure

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I17 | `short_term_debt_share` | `st_debt_end_of_year / total_debt_outstanding` | 98% |
| I18 | `debt_service_gen_rev` | `general_debt_interest / general_revenue` | 99% |

### I.7 TEL Interaction Variables

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| I19 | `tel_x_revenue_autonomy` | `tel_stringency_normalized × revenue_autonomy` | 99% |
| I20 | `tel_x_vfi` | `tel_stringency_normalized × vfi` | 99% |

---

## 12. Pillar J — Standard Fiscal Controls

Fundamental fiscal building blocks typically controlled for in municipal finance research.

### J.1 Revenue Levels (per-capita, real 2012$)

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| J2 | `total_revenue_pc` | `(total_revenue × deflator_factor) / pop_unified` | 99% |
| J4 | `general_revenue_pc` | `(general_revenue × deflator_factor) / pop_unified` | 99% |
| J6 | `total_taxes_pc` | `(total_taxes × deflator_factor) / pop_unified` | 99% |
| J8 | `property_tax_pc` | `(property_tax × deflator_factor) / pop_unified` | 99% |
| J13 | `own_source_rev_pc` | Already in dataset (#911) | 99% |
| J15 | `total_ig_revenue_pc` | `(total_ig_revenue × deflator_factor) / pop_unified` | 99% |

### J.2 Expenditure Levels

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| J20 | `total_expenditure_pc` | `(total_expenditure × deflator_factor) / pop_unified` | 99% |
| J22 | `direct_expenditure_pc` | `(direct_expenditure × deflator_factor) / pop_unified` | 99% |
| J25 | `current_oper_share` | `total_current_oper / direct_expenditure` | 99% |
| J27 | `capital_outlay_pc` | Already in dataset (#894) | 99% |
| J28 | `capital_share` | Already in dataset (#897) | 99% |

### J.3 Functional Expenditure (stitched historical + current)

| # | Variable | Green-eligible? | Coverage (2013+) |
|---|----------|----------------|-----------------|
| J31 | `police_expend` | No | 99% |
| — | `fire_prot_total_expend` (#136) | No | 99% |
| J33 | `highways_expend` | Yes | 99% |
| J34 | `sewerage_expend` | Yes | 99% |
| J35 | `solid_waste_expend` | Yes | 75%* |
| J36 | `parks_&_rec_total_exp` (#366) | Yes | 99% |
| J37 | `hous_&_com_total_exp` (#185) | Yes | 99% |
| J38 | `public_welf_total_exp` (#389) | No | 0% (historical only) |
| J39 | `health_hospitals_expend` | No | 99% |
| J40 | `total_educ_total_exp` (#448) | No | 0% (historical only) |

*J35 note: Current-period data includes only current operations (`solid_wst_curr_oper`); capital outlay component unavailable for 2013+.

### J.4 Debt Stock

| # | Variable | Description | Coverage (2013+) |
|---|----------|-------------|-----------------|
| J41 | `total_debt_outstanding` (#443) | Total debt outstanding | 99% |
| J42 | `debt_pc` (#909) | Per-capita debt (real) | 99% |
| J43 | `total_long_term_debt_out` (#472) | Long-term debt outstanding | 99% |
| J44 | `st_debt_end_of_year` (#407) | Short-term debt at year end | 99% |
| J45 | `ltd_out_general` (#276) | GO bonds outstanding | 0% (historical only) |
| J46 | `revenue_bonds_outstanding` | `total_long_term_debt_out − ltd_out_general` | 0% (historical only) |

### J.5 Debt Flow

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| J48 | `total_ltd_issued` (#476) | LTD issued during year | 99% |
| J49 | `total_ltd_retired` (#483) | LTD retired during year | 99% |
| J50 | `net_borrowing` | `total_ltd_issued − total_ltd_retired` | 99% |
| J51 | `net_borrowing_ratio` | `net_borrowing / total_revenue` | 99% |

### J.6 Balance Sheet / Liquidity

| # | Variable | Description | Coverage (2013+) |
|---|----------|-------------|-----------------|
| J54 | `total_cash_&_securities` (#439) | Total cash and securities | 0% (historical only) |
| J55 | `insur_trust_cash_&_sec` (#193) | Insurance trust cash (restricted) | 0% (historical only) |
| J57 | `unrestricted_cash` | `nonin_trust_cash_&_sec` clipped ≥ 0 | 99% |
| J58 | `cash_securities_pc` (#912) | Per-capita cash & securities | 99% |

### J.7 Payroll

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| J61 | `total_salaries_&_wages` (#486) | Total payroll | 62% |
| J62 | `payroll_share` | `total_salaries_&_wages / direct_expenditure` | 62% |

### J.8 Pension & Retirement

| # | Variable | Formula | Coverage (2013+) |
|---|----------|---------|-----------------|
| J63 | `pension_expenditure_burden` (= E5) | `pension_expend / total_revenue` | 11% |
| J64 | `pension_exp_own_source` | `pension_expend / gen_rev_own_sources` | 11% |

### J.9 Pre-Constructed Ratios (already in dataset)

| # | Variable | Column # |
|---|----------|----------|
| J66 | `tax_to_rev` (= A3) | #923 |
| J68 | `debt_to_revenue` | #910 |
| J69 | `igr_share` | #904 |
| J70 | `fed_igr_share` | #905 |
| J71 | `state_igr_share` | #906 |

---

## 13. Lagged Variables

All primary fiscal constraint measures are lagged 1 and 2 years to reflect the bond issuance process timeline (Faraglia et al., 2019):

| Variable | Lag-1 | Lag-2 |
|----------|-------|-------|
| `debt_service_burden` | `debt_service_burden_lag1` | `debt_service_burden_lag2` |
| `debt_affordability` | `debt_affordability_lag1` | `debt_affordability_lag2` |
| `reserve_ratio` | `reserve_ratio_lag1` | `reserve_ratio_lag2` |
| `operating_balance` | `operating_balance_lag1` | `operating_balance_lag2` |
| `fiscal_stress_index` | `fiscal_stress_index_lag1` | `fiscal_stress_index_lag2` |
| `expenditure_rigidity` | `expenditure_rigidity_lag1` | `expenditure_rigidity_lag2` |
| `revenue_hhi` | `revenue_hhi_lag1` | `revenue_hhi_lag2` |
| `tax_to_rev` | `tax_to_rev_lag1` | `tax_to_rev_lag2` |
| `tax_effort_pc` | `tax_effort_pc_lag1` | `tax_effort_pc_lag2` |

---

## 14. Variables Not Feasible from Current Data

| Variable | Why Not Feasible | External Data Required |
|----------|-----------------|----------------------|
| Net Pension Liability (NPL) | Census reports cash flows, not GASB 68 liabilities | CAFR/ACFR or Public Plans Database |
| OPEB Liability | GASB 75 liabilities not in Census | CAFR GASB 75 schedules |
| Actuarial Funded Ratio | Requires actuarial accrued liability | Plan actuarial reports |
| UAAL / Revenues | Requires unfunded actuarial accrued liability | Same as above |
| Unrestricted Net Position | GAAP concept not reported in Census | CAFR Statement of Net Position |
| GO/Revenue Bond Split (2013+) | `ltd_out_general`, `ltd_iss_general` not in current item codes | Mergent MBSD, Bloomberg |
| IG Expenditure (2013+) | `total_ig_expenditure` not in current item codes | — |
| FTE Employment | `total_full_time_employ` not in current item codes | BLS QCEW or OES |
| Levy Gap | Requires statutory allowable growth rates | State comptroller data |
| Pension Fund Assets (2013+) | `emp_retire_cash_&_sec` not in current item codes | Public Plans Database |

---

## 15. Recommended Model Specifications

Per `fiscal_constraint_variables_updated.docx`, the recommended model hierarchy for replacing `TaxToRev` in the Rep_Mayor interaction:

| Priority | Fiscal Constraint Variable | Rationale |
|----------|---------------------------|-----------|
| **Primary** | E1: `debt_service_burden` | Closest to what agencies weight; captures capital-market signalling |
| Robustness 1 | H1: `fiscal_stress_index` | Multi-dimensional; reduces measurement error |
| Robustness 2 | B1: `reserve_ratio` (inverted) | Leading indicator of credit deterioration; liquidity channel |
| Robustness 3 | F12: `tel_x_tax_effort` | Tests the political-legal constraint channel |
| Mechanism | B4: `days_cash` | Most concrete "need for market access" measure |
| Dynamic | E11: `dsb_worsening` | Tests deterioration channel: worsening triggers labelling |

Additional controls: `own_source_rev_pc`, log population, log per-capita GDP, labour force participation rate, log total debt, expenditure-to-own-revenue ratio. County-level: county GDP per capita, NRI climate risk, log county emissions, Trump vote share. All continuous variables lagged one year.

---

## 16. Complete Column Index

The dataset contains 1,022 columns organised into the following blocks:

| Block | Columns | Count | Description |
|-------|---------|-------|-------------|
| Identifiers | 1–3 | 3 | `year`, `entity_id`, `data_source` |
| Census Historical Fiscal | 4–549 | 546 | Raw Census ASLGF variables (historical + current format) |
| Census Current Fiscal | 550–749 | 200 | Current-format item-code variables |
| Imputation & Geography | 750–752 | 3 | `imputation_flag`, `city_name`, `state_abb` |
| TEL Variables | 753–765 | 13 | Tax & expenditure limitations |
| ACS/BLS Economic | 766–874 | 109 | City/county/state economic indicators + lags |
| FOG Institutional | 875–889 | 15 | Form of government, electoral institutions |
| Investment Variables | 890–920 | 31 | Capital stock, investment gap (Wang & Wu 2018) |
| **Fiscal Constraint Variables** | **921–1022** | **102** | **This document** |

### Fiscal Constraint Variables (columns 921–1022)

| Col | Variable | Pillar |
|-----|----------|--------|
| 921 | `tax_effort_pc` | A |
| 922 | `tax_effort_pc_3yr` | A |
| 923 | `tax_to_rev` | A |
| 924 | `expenditure_rigidity` | A |
| 925 | `budget_flexibility_squeeze` | A |
| 926 | `reserve_ratio` | B |
| 927 | `reserve_months` | B |
| 928 | `low_reserves` | B |
| 929 | `days_cash` | B |
| 930 | `liquidity_tier` | B |
| 931 | `reserve_change_1yr` | B |
| 932 | `reserve_change_3yr` | B |
| 933 | `reserve_declining` | B |
| 934 | `reserve_decline_streak` | B |
| 935 | `reserve_ratio_3yr` | B |
| 936 | `share_property` | C |
| 937 | `share_sales` | C |
| 938 | `share_income` | C |
| 939 | `share_charges` | C |
| 940 | `revenue_hhi` | C |
| 941 | `property_tax_dependence` | C |
| 942 | `tax_revenue_volatility` | C |
| 943 | `own_source_rev_share` | C |
| 944 | `aid_volatility` | D |
| 945 | `aid_growth_trend` | D |
| 946 | `debt_service_burden` | E |
| 947 | `debt_affordability` | E |
| 948 | `pension_expenditure_burden` | E |
| 949 | `combined_liability_burden` | E |
| 950 | `net_borrowing_intensity` | E |
| 951 | `dsb_change_1yr` | E |
| 952 | `dsb_change_3yr` | E |
| 953 | `dsb_worsening` | E |
| 954 | `tel_x_tax_effort` | F |
| 955 | `tel_x_dsb` | F |
| 956 | `go_bond_share_outstanding` | G |
| 957 | `go_bond_share_issuance` | G |
| 958 | `operating_deficit` | H |
| 959 | `operating_balance` | H |
| 960 | `operating_balance_3yr` | H |
| 961 | `fiscal_stress_index` | H |
| 962 | `fiscal_stress_pca` | H |
| 963 | `rating_agency_composite` | H |
| 964 | `high_fiscal_stress` | H |
| 965 | `fiscal_stress_tercile` | H |
| 966 | `revenue_autonomy` | I |
| 967 | `tax_autonomy_ratio` | I |
| 968 | `tax_to_own_source` | I |
| 969 | `charges_to_own_source` | I |
| 970 | `property_tax_share` | I |
| 971 | `sales_tax_share` | I |
| 972 | `income_tax_share` | I |
| 973 | `tax_hhi` | I |
| 974 | `vfi` | I |
| 975 | `fiscal_self_sufficiency` | I |
| 976 | `expenditure_gap_pc` | I |
| 977 | `fed_grant_share_of_grants` | I |
| 978 | `state_grant_share_of_grants` | I |
| 979 | `local_ig_share_of_grants` | I |
| 980 | `ig_exp_share` | I |
| 981 | `direct_exp_share` | I |
| 982 | `short_term_debt_share` | I |
| 983 | `debt_service_gen_rev` | I |
| 984 | `tel_x_revenue_autonomy` | I |
| 985 | `tel_x_vfi` | I |
| 986 | `total_revenue_pc` | J |
| 987 | `general_revenue_pc` | J |
| 988 | `total_taxes_pc` | J |
| 989 | `property_tax_pc` | J |
| 990 | `total_ig_revenue_pc` | J |
| 991 | `total_expenditure_pc` | J |
| 992 | `direct_expenditure_pc` | J |
| 993 | `current_oper_share` | J |
| 994 | `police_expend` | J |
| 995 | `highways_expend` | J |
| 996 | `sewerage_expend` | J |
| 997 | `solid_waste_expend` | J |
| 998 | `health_hospitals_expend` | J |
| 999 | `revenue_bonds_outstanding` | J |
| 1000 | `net_borrowing` | J |
| 1001 | `net_borrowing_ratio` | J |
| 1002 | `unrestricted_cash` | J |
| 1003 | `payroll_share` | J |
| 1004 | `pension_exp_own_source` | J |
| 1005 | `debt_service_burden_lag1` | Lag |
| 1006 | `debt_service_burden_lag2` | Lag |
| 1007 | `debt_affordability_lag1` | Lag |
| 1008 | `debt_affordability_lag2` | Lag |
| 1009 | `reserve_ratio_lag1` | Lag |
| 1010 | `reserve_ratio_lag2` | Lag |
| 1011 | `operating_balance_lag1` | Lag |
| 1012 | `operating_balance_lag2` | Lag |
| 1013 | `fiscal_stress_index_lag1` | Lag |
| 1014 | `fiscal_stress_index_lag2` | Lag |
| 1015 | `expenditure_rigidity_lag1` | Lag |
| 1016 | `expenditure_rigidity_lag2` | Lag |
| 1017 | `revenue_hhi_lag1` | Lag |
| 1018 | `revenue_hhi_lag2` | Lag |
| 1019 | `tax_to_rev_lag1` | Lag |
| 1020 | `tax_to_rev_lag2` | Lag |
| 1021 | `tax_effort_pc_lag1` | Lag |
| 1022 | `tax_effort_pc_lag2` | Lag |

---

## 17. Validation

### NYC (entity_id = 3651000) Spot Checks

| Variable | 2012 | 2015 | 2020 | Plausibility |
|----------|------|------|------|-------------|
| `tax_effort_pc` | 3.23 ($3,230/cap) | 3.48 | 3.76 | Consistent upward trend |
| `tax_to_rev` | 0.456 | 0.499 | 0.507 | ~50% tax reliance, reasonable for NYC |
| `debt_service_burden` | 0.078 | 0.087 | 0.090 | 7.8–9% of own-source → moderate |
| `reserve_ratio` | 0.436 | 0.498 | 0.445 | ~5 months reserves |
| `days_cash` | 159 | 182 | 162 | Adequate–Strong tier |
| `operating_balance` | 0.046 | 0.039 | 0.018 | Narrowing surplus, COVID impact |
| `revenue_hhi` | 0.223 | 0.212 | 0.241 | Well diversified (near 0.25 floor) |
| `vfi` | 0.251 | 0.298 | 0.321 | ~25–32% spending gap filled by transfers |

### Infinity and Missing Value Checks

- Zero infinities across all 1,022 columns
- Division by zero handled uniformly with NaN
- All continuous ratios winsorised at 1st/99th percentiles by year

---

## 18. Disclosure Language

> Fiscal constraint variables are constructed from U.S. Census Bureau Annual Survey of State and Local Government Finances (ASLGF) Individual Unit Files. Three historical-only aggregate variables (`interest_on_gen_debt`, `total_cash_&_securities − insur_trust_cash_&_sec`, `emp_ret_total_expend`) are substituted with current-period equivalents validated at the 2012 overlap year. Pension expenditure variables (E5, E7, J64, J65) have limited coverage for 2013–2023 because most municipalities participate in state-administered pension systems not captured in Census item codes. GO/revenue bond decomposition (G1–G2), intergovernmental expenditure share (I15), and FTE employment data are available only for 2007–2012. All continuous ratios are winsorised at the 1st and 99th percentiles within each year. Fiscal data are reported in thousands of dollars; per-capita values use a unified population series stitching Census fiscal population (2007–2009) with ACS 5-year estimates (2010–2023), deflated to constant 2012 dollars using the BEA Price Index for State & Local Government Gross Investment.
