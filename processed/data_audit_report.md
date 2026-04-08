# Green Bond Municipal Analysis — Data Audit Report

**Date:** 2026-04-08
**Scope:** All raw/processed datasets in `municipal-analysis/raw/`
**Panel window:** 2013–2025 (13 years, green bond issuance period)
**Instruction:** Datasets are audited individually — no merging performed.

---

## 1. Dataset-Level Summary

| # | Dataset | File | Rows | Cols | City Col | Year Col | Cities | Years | Year Range |
|---|---------|------|------|------|----------|----------|--------|-------|------------|
| 1 | Bloomberg Issuance | `city_year_issuance_panel.xlsx` | 7,514 | 368 | `City` | `Year` | 548 | 13 | 2013-2025 |
| 2 | Mayor Party | `mayor_party.csv` | 9,216 | 12 | `—` | `year` | — | 16 | 2010-2025 |
| 3 | Mayoral Candidates | `MayoralCandidates270326.xlsx` | 8,255 | 30 | `—` | `year` | — | 25 | 2001-2025 |
| 4 | Constructed Fiscal | `constructed_fiscal.csv` | 5,598 | 173 | `city_name` | `year` | 542 | 11 | 2013-2023 |
| 5 | Fiscal TEL Merged 2007-2024 | `fiscal_tel_merged_2007_2024.csv` | 10,404 | 1022 | `city_name` | `year` | 577 | 18 | 2007-2024 |
| 6 | Fiscal TEL Merged 2013-2025 | `fiscal_tel_merged_2013_2025.csv.gz` | 6,936 | 1544 | `city_name` | `year` | 548 | 12 | 2013-2024 |
| 7 | ACS Additional | `additional_city_variables_2010_2024.csv` | 8,654 | 61 | `—` | `Year` | — | 15 | 2010-2024 |
| 8 | BLS ACS Economic | `economic_bls_acs.csv` | 8,036 | 16 | `city_name` | `year` | 544 | 14 | 2010-2023 |
| 9 | ACS Demographics 2022 | `acs_demographics_2022.csv` | 574 | 4 | `—` | `—` | — | — | — |
| 10 | EPA Enforcement | `city_year_epa_enforcement_expanded_20260407_125920.csv` | 15,552 | 200 | `CITY_NAME` | `YEAR` | 546 | 27 | 2000-2026 |
| 11 | EPA State Enforcement | `epa_state_enforcement.csv` | 5,598 | 9 | `city_name` | `year` | 542 | 11 | 2013-2023 |
| 12 | Vulcan CO2 | `Vulcan_data.csv` | 6,924 | 216 | `—` | `year` | — | 12 | 2013-2024 |
| 13 | FEMA NRI | `epa_nri.csv` | 5,598 | 435 | `city_name` | `year` | 542 | 11 | 2013-2023 |
| 14 | Yale Climate Opinion | `climate_opinion_ycom.csv` | 5,598 | 27 | `city_name` | `year` | 542 | 11 | 2013-2023 |
| 15 | Climate Policy Controls | `climate_policy_controls.csv` | 5,598 | 14 | `city_name` | `year` | 542 | 11 | 2013-2023 |
| 16 | FEMA Disasters | `fema_disaster_declarations.csv` | 49,408 | 8 | `—` | `year` | — | 16 | 2010-2025 |
| 17 | NFIP Flood Claims | `nfip_flood_claims.csv` | 2,273 | 9 | `—` | `—` | — | — | — |
| 18 | Federal Grants | `federal_grants_panel.csv` | 7,514 | 76 | `—` | `year` | — | 13 | 2013-2025 |
| 19 | State Transit Funding | `state_transit_funding.csv` | 627 | 30 | `—` | `year` | — | 13 | 2013-2025 |
| 20 | Federal Green Funding | `federal_green_funding.csv` | 102 | 9 | `—` | `year` | — | 2 | 2022-2023 |
| 21 | FOG Institutions | `fog_institutions_panel_2010_2024.csv` | 8,670 | 15 | `city_name` | `year` | 548 | 15 | 2010-2024 |
| 22 | TEL Data | `tel.csv` | 5,598 | 16 | `city_name` | `year` | 542 | 11 | 2013-2023 |
| 23 | Bond Referenda | `state_bond_referenda_requirements.csv` | 50 | 10 | `—` | `—` | — | — | — |
| 24 | Bond Banks | `state_bond_banks.csv` | 50 | 9 | `—` | `—` | — | — | — |
| 25 | Anti-ESG Laws | `antiesg_laws.csv` | 5,609 | 31 | `city_name` | `year` | 543 | 11 | 2013-2023 |
| 26 | Presidential Elections | `presidential_elections.csv` | 5,653 | 6 | `city_name` | `year` | 547 | 11 | 2013-2023 |
| 27 | State Political | `state_political.csv` | 5,653 | 9 | `city_name` | `year` | 547 | 11 | 2013-2023 |
| 28 | MSRB RFI Position | `state_msrb_rfi_position.csv` | 50 | 6 | `—` | `—` | — | — | — |
| 29 | SRF Bond Merged | `srf_bond_merged.csv` | 7,514 | 471 | `City` | `year` | 548 | 13 | 2013-2025 |
| 30 | ESG AUM | `esg_aum.csv` | 11 | 5 | `—` | `year` | — | 11 | 2013-2023 |
| 31 | State Green Bond Capacity | `state_green_bond_capacity.csv` | 550 | 13 | `—` | `year` | — | 11 | 2013-2023 |
| 32 | Municipal Electric | `municipal_electric_utilities.csv` | 578 | 8 | `city_name` | `—` | 548 | — | — |
| 33 | State Building Codes | `state_building_codes.csv` | 50 | 12 | `—` | `—` | — | — | — |
| 34 | State Clean Energy | `state_clean_energy_funds.csv` | 50 | 12 | `—` | `—` | — | — | — |
| 35 | State Net Metering | `state_net_metering.csv` | 800 | 6 | `—` | `year` | — | 16 | 2010-2025 |
| 36 | Water Panel | `substitute_water_panel.csv` | 7,501 | 14 | `—` | `year` | — | 13 | 2013-2025 |
| 37 | Crosswalk | `Crosswalk.csv` | 578 | 31 | `city_name` | `—` | 548 | — | — |

---

## 2. Variable-Level Coverage by Dataset

For each dataset, every non-ID variable is listed with its data type,
non-null rate, year span with data, and number of cities with data.

### Bloomberg Issuance
**File:** `raw/bloomberg/city_year_issuance_panel.xlsx`  
**Shape:** 7,514 rows × 368 columns  
**City column:** `City` (548 unique cities)  
**Year column:** `Year` — range 2013-2025 (13 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `Green_Bond_Issued` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `City_Green_Amt_Issued` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `City_Green_Issuance_Count` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Total_Amt_Issued` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Total_Issuance_Count` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Govt_Amt_Issued` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Govt_Issuance_Count` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `City_Share_of_State_Pct` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__AMT_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__AMT_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_&_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_&_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_BQ` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_BQ` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_BQ_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_BQ_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT_ST_TAX...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT_ST_TAX...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT_ST_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT_ST_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT_ST_TAX…` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT_ST_TAX…` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAXABLE_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAXABLE_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__NEW_MONEY` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__NEW_MONEY` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__New_Money` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__New_Money` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__REFUNDING` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__REFUNDING` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__REFUNDING...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__REFUNDING...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Education` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Education` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Financing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Financing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Financing...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Financing...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__General_Government` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__General_Government` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Public_Services` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Public_Services` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Transporta` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Transporta` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Transporta...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Transporta...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Utilities` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Utilities` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Self-reported Green__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Self-reported Green__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Self-reported Green__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Self-reported Green__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Self-reported Green__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Self-reported Green__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Mgmt of Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Mgmt of Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Mgmt of Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Mgmt of Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Mgmt of Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Mgmt of Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Reporting__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Reporting__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Reporting__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Reporting__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Reporting__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Reporting__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Assurance Providers__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Assurance Providers__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Assurance Providers__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Assurance Providers__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Assurance Providers__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Assurance Providers__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Proj Sel Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Proj Sel Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Proj Sel Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Proj Sel Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Proj Sel Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Proj Sel Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Framework__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Framework__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Framework__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Framework__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Framework__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Framework__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__APPROP` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__APPROP` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__ARPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__ARPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__DEV` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__DEV` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__GO` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__GO` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__GODIST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__GODIST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__LMFH` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__LMFH` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__MEL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__MEL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__MUNUTIL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__MUNUTIL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__NFPCULT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__NFPCULT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PILOT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PILOT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PORTS` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PORTS` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PUBPWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PUBPWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PUBTRAN` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PUBTRAN` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__SCD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__SCD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__SOLWST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__SOLWST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__SPLASMT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__SPLASMT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__TXMUD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__TXMUD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__WSGTD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__WSGTD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__WTRSWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__WTRSWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Airport` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Airport` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Appropriation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Appropriation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Development` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Development` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__General_Obligation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__General_Obligation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__General_Obligation_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__General_Obligation_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Limited_Multi-Family_Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Limited_Multi-Family_Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Mello-Roos` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Mello-Roos` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Municipal_Utility` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Municipal_Utility` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Not-for-Profit_–_Cultural` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Not-for-Profit_–_Cultural` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Payment_in_Lieu_of_Taxes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Payment_in_Lieu_of_Taxes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Ports_Marina` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Ports_Marina` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Public_Power` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Public_Power` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Public_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Public_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__School_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__School_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Solid_Waste` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Solid_Waste` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Special_Assessment` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Special_Assessment` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Texas_Municipal_Utility_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Texas_Municipal_Utility_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Water_Sewer` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Water_Sewer` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.45` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.45` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.7` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.7` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.72` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.72` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.78` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.78` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.84` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.84` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.94` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.94` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.95` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.95` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.97` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.97` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.05` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.05` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.08` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.08` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.2` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.2` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.22` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.22` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.25` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.25` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.26` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.26` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.4` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.4` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.43` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.43` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.58` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.58` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.6` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.6` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.63` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.63` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.65` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.65` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.75` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.75` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.8` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.8` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.88` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.88` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.93` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.93` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Biodiversity,_Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Biodiversity,_Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Biodiversity,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Biodiversity,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Energy_Efficiency,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Energy_Efficiency,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Natural_Resource_Management` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Natural_Resource_Management` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Circular_Design_and_Production` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Circular_Design_and_Production` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Conservation,_Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Conservation,_Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Star_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Star_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Star_Certified,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Star_Certified,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Storage,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Storage,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Hydrogen` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Hydrogen` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Circular_Value_Recovery` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Circular_Value_Recovery` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Vehicles` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Vehicles` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Information_Support,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Information_Support,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infrastructure,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infrastructure,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__LEED_Certified,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__LEED_Certified,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__LEED_Certified,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__LEED_Certified,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Plumbing_System,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Plumbing_System,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Pollution_Control,_Greenhouse_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Pollution_Control,_Greenhouse_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Public,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Public,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Rail_(Non_Passenger)` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Rail_(Non_Passenger)` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Soil_Remediation,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Soil_Remediation,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Bioenergy,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Bioenergy,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Wind,_Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Wind,_Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Sustainable_Forestry,_Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Sustainable_Forestry,_Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Vehicles,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Vehicles,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |

### Mayor Party
**File:** `raw/mayor/mayor_party.csv`  
**Shape:** 9,216 rows × 12 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2010-2025 (16 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `geo_name` | str | 9,216/9,216 | 100.0% | 2010–2025 | 16 | None |
| `state_abb` | str | 9,216/9,216 | 100.0% | 2010–2025 | 16 | None |
| `mayor_name` | str | 9,144/9,216 | 99.2% | 2010–2025 | 16 | None |
| `election_year` | float | 9,144/9,216 | 99.2% | 2010–2025 | 16 | None |
| `election_type` | str | 9,144/9,216 | 99.2% | 2010–2025 | 16 | None |
| `source` | str | 9,144/9,216 | 99.2% | 2010–2025 | 16 | None |
| `mayor_pid_raw` | str | 9,144/9,216 | 99.2% | 2010–2025 | 16 | None |
| `mayor_pid` | str | 9,037/9,216 | 98.1% | 2010–2025 | 16 | None |
| `prob_democrat` | float | 8,891/9,216 | 96.5% | 2010–2025 | 16 | None |
| `prob_republican` | float | 8,891/9,216 | 96.5% | 2010–2025 | 16 | None |

### Mayoral Candidates
**File:** `raw/mayor/MayoralCandidates270326.xlsx`  
**Shape:** 8,255 rows × 30 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2001-2025 (25 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `geo_name` | str | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `state_abb` | str | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `office_consolidated` | str | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `contest` | str | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `winner` | int | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `incumbent` | int | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `pid_est` | str | 8,253/8,255 | 100.0% | 2002–2025 | 24 | None |
| `election_type` | str | 8,254/8,255 | 100.0% | 2001–2025 | 25 | None |
| `source` | str | 8,255/8,255 | 100.0% | 2001–2025 | 25 | None |
| `full_name` | str | 8,250/8,255 | 99.9% | 2001–2025 | 25 | None |
| `firstname` | str | 8,244/8,255 | 99.9% | 2001–2025 | 25 | None |
| `lastname` | str | 8,243/8,255 | 99.9% | 2001–2025 | 25 | None |
| `month` | float | 8,249/8,255 | 99.9% | 2001–2025 | 25 | None |
| `termlength.1` | float | 8,166/8,255 | 98.9% | 2001–2025 | 25 | None |
| `district` | str | 7,977/8,255 | 96.6% | 2001–2025 | 24 | None |
| `termlength` | float | 7,928/8,255 | 96.0% | 2001–2025 | 25 | None |
| `vote_share` | float | 7,638/8,255 | 92.5% | 2005–2025 | 21 | None |
| `votes` | float | 7,536/8,255 | 91.3% | 2005–2025 | 21 | None |
| `total_votes` | str | 7,536/8,255 | 91.3% | 2005–2025 | 21 | None |
| `prob_democrat` | float | 7,351/8,255 | 89.0% | 2001–2025 | 25 | None |
| `prob_republican` | float | 7,351/8,255 | 89.0% | 2001–2025 | 25 | None |
| `mayor_selection` | float | 7,247/8,255 | 87.8% | 2001–2025 | 24 | None |
| `mayor_selection.1` | float | 7,045/8,255 | 85.3% | 2001–2025 | 25 | None |
| `comments` | str | 4,691/8,255 | 56.8% | 2003–2025 | 23 | None |
| `review_detail` | str | 3,685/8,255 | 44.6% | 2002–2025 | 24 | None |
| `cfscore` | float | 3,134/8,255 | 38.0% | 2005–2024 | 20 | 2025 |
| `flag` | str | 1,701/8,255 | 20.6% | 2001–2025 | 25 | None |
| `review_flag` | str | 1,272/8,255 | 15.4% | 2001–2025 | 25 | None |

### Constructed Fiscal
**File:** `raw/fiscal/constructed_fiscal.csv`  
**Shape:** 5,598 rows × 173 columns  
**City column:** `city_name` (542 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_medicaid_expanded` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_effort_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_effort_pc_3yr` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_revenue_volatility` | float | 5,597/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_x_tax_effort` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `operating_deficit` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `rating_agency_composite` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `expenditure_gap_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `total_revenue_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `general_revenue_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `total_taxes_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `total_ig_revenue_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `total_expenditure_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `direct_expenditure_pc` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `police_expend` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `highways_expend` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `sewerage_expend` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `health_hospitals_expend` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `net_borrowing` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `unrestricted_cash` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_affordability_lag1` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_affordability_lag2` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_ratio_lag2` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `operating_balance_lag1` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `operating_balance_lag2` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `fiscal_stress_index_lag1` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `fiscal_stress_index_lag2` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `revenue_hhi_lag1` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `revenue_hhi_lag2` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_to_rev_lag1` | float | 5,596/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_to_rev_lag2` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_effort_pc_lag1` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_effort_pc_lag2` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_general_revenue_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_general_expenditure_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_to_rev` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_ratio` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_months` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `low_reserves` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `days_cash` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `liquidity_tier` | str | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_change_1yr` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_change_3yr` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_declining` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_decline_streak` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_ratio_3yr` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `share_income` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `share_charges` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `revenue_hhi` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `own_source_rev_share` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `aid_growth_trend` | float | 5,590/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_affordability` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `combined_liability_burden` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `net_borrowing_intensity` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `operating_balance` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `operating_balance_3yr` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `fiscal_stress_index` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `high_fiscal_stress` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `fiscal_stress_tercile` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `revenue_autonomy` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_autonomy_ratio` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_to_own_source` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `charges_to_own_source` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `income_tax_share` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tax_hhi` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `vfi` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `fiscal_self_sufficiency` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `direct_exp_share` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_x_revenue_autonomy` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_x_vfi` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `current_oper_share` | float | 5,592/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `net_borrowing_ratio` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_service_burden_lag2` | float | 5,595/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `reserve_ratio_lag1` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `expenditure_rigidity_lag2` | float | 5,594/5,598 | 99.9% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `aid_volatility` | float | 5,589/5,598 | 99.8% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_service_burden_lag1` | float | 5,586/5,598 | 99.8% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `expenditure_rigidity_lag1` | float | 5,586/5,598 | 99.8% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `share_property` | float | 5,582/5,598 | 99.7% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `property_tax_dependence` | float | 5,581/5,598 | 99.7% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `property_tax_share` | float | 5,581/5,598 | 99.7% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `fed_grant_share_of_grants` | float | 5,581/5,598 | 99.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_grant_share_of_grants` | float | 5,581/5,598 | 99.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `local_ig_share_of_grants` | float | 5,581/5,598 | 99.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `property_tax_pc` | float | 5,584/5,598 | 99.7% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `ONR_share_lag2` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `COM_share_lag2` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `RES_share_lag2` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `IND_share_lag2` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `ONR_share_lag3` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `COM_share_lag3` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `RES_share_lag3` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `IND_share_lag3` | float | 5,576/5,598 | 99.6% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `expenditure_rigidity` | float | 5,573/5,598 | 99.6% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `budget_flexibility_squeeze` | float | 5,569/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_service_burden` | float | 5,572/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `dsb_change_1yr` | float | 5,572/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `dsb_change_3yr` | float | 5,572/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `dsb_worsening` | float | 5,572/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_x_dsb` | float | 5,572/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `debt_service_gen_rev` | float | 5,572/5,598 | 99.5% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `short_term_debt_share` | float | 5,555/5,598 | 99.2% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `ONR_share_lag4` | float | 5,068/5,598 | 90.5% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `COM_share_lag4` | float | 5,068/5,598 | 90.5% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `RES_share_lag4` | float | 5,068/5,598 | 90.5% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `IND_share_lag4` | float | 5,068/5,598 | 90.5% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `ONR_share_lag1` | float | 5,061/5,598 | 90.4% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `COM_share_lag1` | float | 5,061/5,598 | 90.4% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `RES_share_lag1` | float | 5,061/5,598 | 90.4% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `IND_share_lag1` | float | 5,061/5,598 | 90.4% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `rating_agency_composite_lag1` | float | 5,025/5,598 | 89.8% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `tel_x_tax_effort_lag1` | float | 5,026/5,598 | 89.8% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `reserve_declining_lag1` | float | 5,021/5,598 | 89.7% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `reserve_decline_streak_lag1` | float | 5,021/5,598 | 89.7% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `low_reserves_lag1` | float | 5,021/5,598 | 89.7% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `combined_liability_burden_lag1` | float | 5,023/5,598 | 89.7% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `tel_x_dsb_lag1` | float | 5,014/5,598 | 89.6% | 2014–2023 | 10 | 541 | 2013, 2024, 2025 |
| `solid_waste_expend` | float | 4,725/5,598 | 84.4% | 2013–2023 | 11 | 482 | 2024, 2025 |
| `fiscal_stress_pca` | float | 4,504/5,598 | 80.5% | 2013–2021 | 9 | 540 | 2022, 2023, 2024, 2025 |
| `fiscal_stress_pca_lag1` | float | 4,501/5,598 | 80.4% | 2014–2022 | 9 | 540 | 2013, 2023, 2024, 2025 |
| `combined_liability_burden_lag2` | float | 4,454/5,598 | 79.6% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `rating_agency_composite_lag2` | float | 4,455/5,598 | 79.6% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `tel_x_tax_effort_lag2` | float | 4,455/5,598 | 79.6% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `reserve_declining_lag2` | float | 4,452/5,598 | 79.5% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `reserve_decline_streak_lag2` | float | 4,452/5,598 | 79.5% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `low_reserves_lag2` | float | 4,452/5,598 | 79.5% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `fiscal_stress_pca_lag2` | float | 4,450/5,598 | 79.5% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `tel_x_dsb_lag2` | float | 4,452/5,598 | 79.5% | 2015–2023 | 9 | 525 | 2013, 2014, 2024, 2025 |
| `state_medicaid_expansion_year` | float | 4,182/5,598 | 74.7% | 2013–2023 | 11 | 412 | 2024, 2025 |
| `payroll_share` | float | 4,024/5,598 | 71.9% | 2013–2022 | 10 | 509 | 2023, 2024, 2025 |
| `combined_liability_burden_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `debt_service_burden_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `operating_balance_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `fiscal_stress_index_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `tax_to_rev_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `rating_agency_composite_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `tel_x_tax_effort_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `tel_x_dsb_lag3` | float | 3,900/5,598 | 69.7% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `reserve_declining_lag3` | float | 3,899/5,598 | 69.6% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `expenditure_rigidity_lag3` | float | 3,899/5,598 | 69.6% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `reserve_decline_streak_lag3` | float | 3,899/5,598 | 69.6% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `low_reserves_lag3` | float | 3,899/5,598 | 69.6% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `reserve_ratio_lag3` | float | 3,899/5,598 | 69.6% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `fiscal_stress_pca_lag3` | float | 3,899/5,598 | 69.6% | 2016–2023 | 8 | 501 | 2013, 2014, 2015, 2024, 2025 |
| `reserve_declining_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `expenditure_rigidity_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `reserve_decline_streak_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `low_reserves_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `combined_liability_burden_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `reserve_ratio_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `debt_service_burden_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `operating_balance_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `fiscal_stress_index_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `tax_to_rev_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `rating_agency_composite_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `fiscal_stress_pca_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `tel_x_tax_effort_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `tel_x_dsb_lag4` | float | 3,371/5,598 | 60.2% | 2017–2023 | 7 | 498 | 6 yrs missing |
| `ELC_share_lag2` | float | 3,352/5,598 | 59.9% | 2013–2023 | 11 | 347 | 2024, 2025 |
| `ELC_share_lag3` | float | 3,355/5,598 | 59.9% | 2013–2023 | 11 | 346 | 2024, 2025 |
| `share_sales` | float | 3,346/5,598 | 59.8% | 2013–2023 | 11 | 350 | 2024, 2025 |
| `sales_tax_share` | float | 3,345/5,598 | 59.8% | 2013–2023 | 11 | 350 | 2024, 2025 |
| `ELC_share_lag4` | float | 3,052/5,598 | 54.5% | 2014–2023 | 10 | 346 | 2013, 2024, 2025 |
| `ELC_share_lag1` | float | 3,046/5,598 | 54.4% | 2013–2022 | 10 | 346 | 2023, 2024, 2025 |
| `pension_expenditure_burden` | float | 757/5,598 | 13.5% | 2013–2016 | 4 | 237 | 9 yrs missing |
| `pension_exp_own_source` | float | 757/5,598 | 13.5% | 2013–2016 | 4 | 237 | 9 yrs missing |
| `go_bond_share_outstanding` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `go_bond_share_issuance` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `ig_exp_share` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `revenue_bonds_outstanding` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |

### Fiscal TEL Merged 2007-2024
**File:** `raw/fiscal/fiscal_tel_merged_2007_2024.csv`  
**Shape:** 10,404 rows × 1022 columns  
**City column:** `city_name` (577 unique cities)  
**Year column:** `year` — range 2007-2024 (18 years)  
**Panel-window coverage (2013–2025):** 12/13 years  
**Missing panel years:** 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `entity_id` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `data_source` | str | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `imputation_flag` | str | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `state_abb` | str | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_overall_rate_limit` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_specific_rate_limit` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_levy_limit` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_assessment_limit` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_general_revenue_limit` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_general_expenditure_limit` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_full_disclosure` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_stringency_simple` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_stringency_ads` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `tel_stringency_normalized` | float | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `manually_verified` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `verification_source` | str | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `data_year` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `fog` | float | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `termlimits` | float | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `termlength` | float | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `districts` | str | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `verified_2024` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `price_index_2012` | float | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `deflator_factor` | float | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `baseline_quality` | int | 10,404/10,404 | 100.0% | 2007–2024 | 18 | 577 | 2025 |
| `capital_share_baseline` | float | 10,386/10,404 | 99.8% | 2007–2024 | 18 | 576 | 2025 |
| `partisan` | float | 10,368/10,404 | 99.7% | 2007–2024 | 18 | 575 | 2025 |
| `initiative` | float | 10,188/10,404 | 97.9% | 2007–2024 | 18 | 565 | 2025 |
| `referendum` | float | 10,188/10,404 | 97.9% | 2007–2024 | 18 | 565 | 2025 |
| `capital_outlay_pc_state_median` | float | 9,826/10,404 | 94.4% | 2007–2023 | 17 | 548 | 2024, 2025 |
| `pop_unified` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `highway_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `sewerage_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `water_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `police_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fire_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `parks_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `water_sewer_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `safety_capital_pc` | float | 9,809/10,404 | 94.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `direct_expenditure` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `direct_general_expend` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fire_prot_total_expend` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `gen_rev_own_sources` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `general_capital_outlay` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `general_expenditure` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `general_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `hous_&_com_direct_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `hous_&_com_total_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `libraries_direct_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `misc_general_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `natural_res_direct_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `natural_res_total_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `nonin_trust_cash_&_sec` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `parks_&_rec_direct_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `parks_&_rec_total_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `regular_hwy_direct_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `regular_hwy_total_exp` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `st_debt_end_of_year` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tot_chgs_and_misc_rev` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tot_local_ig_rev` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tot_sales_&_gr_rec_tax` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_capital_outlays` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_construction` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_current_oper` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_debt_outstanding` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_emp_ret_rev` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_expenditure` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_fed_ig_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_general_charges` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_ig_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_income_taxes` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_insur_trust_ben` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_insur_trust_rev` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_license_taxes` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_long_term_debt_out` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_ltd_issued` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_ltd_out` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_ltd_retired` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_rev_own_sources` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_select_sales_tax` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_state_ig_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_taxes` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_utility_revenue` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `capital_outlay_real` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `capital_outlay_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `peer_shortfall` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `below_peer_median` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `own_source_rev_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `cash_securities_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tax_effort_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tel_x_tax_effort` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `operating_deficit` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `rating_agency_composite` | float | 9,755/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `expenditure_gap_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_revenue_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `general_revenue_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_taxes_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_ig_revenue_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_expenditure_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `direct_expenditure_pc` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `police_expend` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `highways_expend` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `sewerage_expend` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `health_hospitals_expend` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `net_borrowing` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `unrestricted_cash` | float | 9,757/10,404 | 93.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tax_effort_pc_lag1` | float | 9,757/10,404 | 93.8% | 2008–2024 | 17 | 574 | 2025 |
| `state_igr_other` | float | 9,750/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `capital_share` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `igr_share` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_igr_share` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_igr_share` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_to_revenue` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tax_to_rev` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `reserve_ratio` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `reserve_months` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `low_reserves` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `days_cash` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `liquidity_tier` | str | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `share_income` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `share_charges` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `revenue_hhi` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `own_source_rev_share` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_affordability` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `combined_liability_burden` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `net_borrowing_intensity` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `operating_balance` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fiscal_stress_index` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `high_fiscal_stress` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fiscal_stress_tercile` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `revenue_autonomy` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tax_autonomy_ratio` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tax_to_own_source` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `charges_to_own_source` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `income_tax_share` | float | 9,751/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tax_hhi` | float | 9,751/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `vfi` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fiscal_self_sufficiency` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `direct_exp_share` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tel_x_revenue_autonomy` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tel_x_vfi` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `current_oper_share` | float | 9,748/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `net_borrowing_ratio` | float | 9,753/10,404 | 93.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_affordability_lag1` | float | 9,753/10,404 | 93.7% | 2008–2024 | 17 | 574 | 2025 |
| `reserve_ratio_lag1` | float | 9,748/10,404 | 93.7% | 2008–2024 | 17 | 574 | 2025 |
| `operating_balance_lag1` | float | 9,753/10,404 | 93.7% | 2008–2024 | 17 | 574 | 2025 |
| `fiscal_stress_index_lag1` | float | 9,753/10,404 | 93.7% | 2008–2024 | 17 | 574 | 2025 |
| `revenue_hhi_lag1` | float | 9,753/10,404 | 93.7% | 2008–2024 | 17 | 574 | 2025 |
| `tax_to_rev_lag1` | float | 9,753/10,404 | 93.7% | 2008–2024 | 17 | 574 | 2025 |
| `property_tax` | float | 9,742/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `share_property` | float | 9,740/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `property_tax_dependence` | float | 9,739/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `property_tax_share` | float | 9,739/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_grant_share_of_grants` | float | 9,738/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_grant_share_of_grants` | float | 9,738/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `local_ig_share_of_grants` | float | 9,738/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `property_tax_pc` | float | 9,742/10,404 | 93.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `general_debt_interest` | float | 9,728/10,404 | 93.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `capital_intensity_deviation` | float | 9,731/10,404 | 93.5% | 2007–2023 | 17 | 546 | 2024, 2025 |
| `expenditure_rigidity` | float | 9,725/10,404 | 93.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_service_burden` | float | 9,724/10,404 | 93.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tel_x_dsb` | float | 9,724/10,404 | 93.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_service_gen_rev` | float | 9,724/10,404 | 93.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_service_burden_lag1` | float | 9,724/10,404 | 93.5% | 2008–2024 | 17 | 574 | 2025 |
| `expenditure_rigidity_lag1` | float | 9,725/10,404 | 93.5% | 2008–2024 | 17 | 574 | 2025 |
| `budget_flexibility_squeeze` | float | 9,721/10,404 | 93.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `short_term_debt_share` | float | 9,710/10,404 | 93.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `misc_general_rev_nec` | float | 9,696/10,404 | 93.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tel_stringency_category` | str | 9,684/10,404 | 93.1% | 2007–2024 | 18 | 537 | 2025 |
| `chg_all_other_nec` | float | 9,648/10,404 | 92.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `interest_revenue` | float | 9,586/10,404 | 92.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fines_and_forfeits` | float | 9,574/10,404 | 92.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_igr_other` | float | 9,545/10,404 | 91.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `other_license_taxes` | float | 9,395/10,404 | 90.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `chg_parks_&_recreation` | float | 9,310/10,404 | 89.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `debt_affordability_lag2` | float | 9,229/10,404 | 88.7% | 2009–2024 | 16 | 576 | 2025 |
| `operating_balance_lag2` | float | 9,229/10,404 | 88.7% | 2009–2024 | 16 | 576 | 2025 |
| `fiscal_stress_index_lag2` | float | 9,229/10,404 | 88.7% | 2009–2024 | 16 | 576 | 2025 |
| `revenue_hhi_lag2` | float | 9,229/10,404 | 88.7% | 2009–2024 | 16 | 576 | 2025 |
| `tax_to_rev_lag2` | float | 9,229/10,404 | 88.7% | 2009–2024 | 16 | 576 | 2025 |
| `tax_effort_pc_lag2` | float | 9,232/10,404 | 88.7% | 2009–2024 | 16 | 576 | 2025 |
| `reserve_ratio_lag2` | float | 9,223/10,404 | 88.6% | 2009–2024 | 16 | 576 | 2025 |
| `debt_service_burden_lag2` | float | 9,211/10,404 | 88.5% | 2009–2024 | 16 | 576 | 2025 |
| `expenditure_rigidity_lag2` | float | 9,211/10,404 | 88.5% | 2009–2024 | 16 | 576 | 2025 |
| `tax_revenue_volatility` | float | 9,176/10,404 | 88.2% | 2009–2024 | 16 | 574 | 2025 |
| `reserve_change_1yr` | float | 9,170/10,404 | 88.1% | 2008–2023 | 16 | 547 | 2024, 2025 |
| `reserve_declining` | float | 9,170/10,404 | 88.1% | 2008–2023 | 16 | 547 | 2024, 2025 |
| `reserve_decline_streak` | float | 9,170/10,404 | 88.1% | 2008–2023 | 16 | 547 | 2024, 2025 |
| `aid_volatility` | float | 9,165/10,404 | 88.1% | 2009–2024 | 16 | 574 | 2025 |
| `dsb_change_1yr` | float | 9,146/10,404 | 87.9% | 2008–2023 | 16 | 547 | 2024, 2025 |
| `dsb_worsening` | float | 9,146/10,404 | 87.9% | 2008–2023 | 16 | 547 | 2024, 2025 |
| `local_igr_other` | float | 9,101/10,404 | 87.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `chg_sewerage` | float | 8,978/10,404 | 86.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `solid_waste_expend` | float | 8,670/10,404 | 83.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `water_utility_revenue` | float | 8,636/10,404 | 83.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fiscal_stress_pca` | float | 8,640/10,404 | 83.0% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `tax_effort_pc_3yr` | float | 8,603/10,404 | 82.7% | 2009–2023 | 15 | 547 | 2024, 2025 |
| `reserve_ratio_3yr` | float | 8,592/10,404 | 82.6% | 2009–2023 | 15 | 547 | 2024, 2025 |
| `operating_balance_3yr` | float | 8,597/10,404 | 82.6% | 2009–2023 | 15 | 547 | 2024, 2025 |
| `police_prot_construct` | float | 8,426/10,404 | 81.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `rents_and_royalties` | float | 8,366/10,404 | 80.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `prop_sale_hous/com_dev` | float | 8,269/10,404 | 79.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `prop_sale_other` | float | 8,245/10,404 | 79.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `other_select_sales_tax` | float | 8,172/10,404 | 78.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `public_utility_tax` | float | 8,172/10,404 | 78.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_igr_oth_gen_sup` | float | 8,152/10,404 | 78.4% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `lfpr_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `management_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `manufacturing_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `naturalresources_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `production_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `transport_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `unemployment_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `percapita_income_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `population_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `totalincome_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `log_percapita_income_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `log_population_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `log_totalincome_city` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `percapita_income_real` | float | 8,078/10,404 | 77.6% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `lfpr_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `management_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `manufacturing_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `naturalresources_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `percapita_income_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `population_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `production_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `totalincome_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `transport_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `unemployment_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `log_percapita_income_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `log_population_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `log_totalincome_county` | float | 8,056/10,404 | 77.4% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `investment_gap` | float | 8,026/10,404 | 77.1% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `chg_solid_waste_mgmt` | float | 8,010/10,404 | 77.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `reserve_change_3yr` | float | 8,014/10,404 | 77.0% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `aid_growth_trend` | float | 8,012/10,404 | 77.0% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `dsb_change_3yr` | float | 7,991/10,404 | 76.8% | 2010–2023 | 14 | 547 | 2024, 2025 |
| `sewerage_construction` | float | 7,930/10,404 | 76.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `occup_and_bus_lic_nec` | float | 7,892/10,404 | 75.9% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_igr_highways` | float | 7,885/10,404 | 75.8% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `total_salaries_&_wages` | float | 7,782/10,404 | 74.8% | 2007–2022 | 16 | 547 | 2023, 2024, 2025 |
| `payroll_share` | float | 7,782/10,404 | 74.8% | 2007–2022 | 16 | 547 | 2023, 2024, 2025 |
| `fed_igr_hous/com_dev` | float | 7,672/10,404 | 73.7% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `water_util_construct` | float | 7,532/10,404 | 72.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `percapita_income_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `population_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `totalincome_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `unemployment_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `lfpr_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `lfpr_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `management_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `manufacturing_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `naturalresources_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `production_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `transport_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `unemployment_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `percapita_income_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `population_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `totalincome_city_lag1` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `log_percapita_income_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `log_population_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `log_totalincome_state` | float | 7,501/10,404 | 72.1% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `lfpr_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `management_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `manufacturing_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `naturalresources_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `percapita_income_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `population_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `production_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `totalincome_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `transport_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `unemployment_county_lag1` | float | 7,490/10,404 | 72.0% | 2011–2023 | 13 | 547 | 2024, 2025 |
| `special_assessments` | float | 7,451/10,404 | 71.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fire_prot_construction` | float | 7,362/10,404 | 70.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `total_gen_sales_tax` | float | 7,143/10,404 | 68.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `share_sales` | float | 7,141/10,404 | 68.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `sales_tax_share` | float | 7,140/10,404 | 68.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `percapita_income_state_lag1` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `population_state_lag1` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `totalincome_state_lag1` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `unemployment_state_lag1` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `lfpr_state_lag1` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `lfpr_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `management_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `manufacturing_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `naturalresources_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `production_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `transport_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `unemployment_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `percapita_income_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `population_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `totalincome_city_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `lfpr_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `management_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `manufacturing_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `naturalresources_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `percapita_income_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `population_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `production_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `totalincome_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `transport_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `unemployment_county_lag2` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `pop_growth_5yr` | float | 6,924/10,404 | 66.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `fire_prot_direct_expend` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `health_direct_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `health_total_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `libraries_total_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `parking_direct_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `parking_total_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `police_prot_direct_expend` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `police_prot_total_expend` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `sewerage_direct_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `sewerage_total_exp` | float | 6,872/10,404 | 66.1% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `capital_stock_pc` | float | 6,872/10,404 | 66.1% | 2013–2024 | 12 | 574 | 2025 |
| `ltd_beg_other` | float | 6,854/10,404 | 65.9% | 2012–2023 | 12 | 546 | 2024, 2025 |
| `ltd_outstanding_other` | float | 6,846/10,404 | 65.8% | 2012–2023 | 12 | 546 | 2024, 2025 |
| `cen_staff_curr_oper` | float | 6,831/10,404 | 65.7% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `police_prot_curr_oper` | float | 6,824/10,404 | 65.6% | 2012–2023 | 12 | 547 | 2024, 2025 |
| `ltd_retired_other` | float | 6,816/10,404 | 65.5% | 2012–2023 | 12 | 546 | 2024, 2025 |
| `reg_hwy_curr_oper` | float | 6,809/10,404 | 65.4% | 2012–2023 | 12 | 546 | 2024, 2025 |
| `parks_rec_curr_oper` | float | 6,715/10,404 | 64.5% | 2012–2023 | 12 | 541 | 2024, 2025 |
| `other_gen_curr_oper` | float | 6,667/10,404 | 64.1% | 2012–2023 | 12 | 545 | 2024, 2025 |
| `fire_prot_curr_oper` | float | 6,528/10,404 | 62.7% | 2012–2023 | 12 | 528 | 2024, 2025 |
| `finan_adm_curr_oper` | float | 6,505/10,404 | 62.5% | 2012–2023 | 12 | 545 | 2024, 2025 |
| `chg_parking` | float | 6,462/10,404 | 62.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `percapita_income_state_lag2` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `population_state_lag2` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `totalincome_state_lag2` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `unemployment_state_lag2` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `lfpr_state_lag2` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `lfpr_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `management_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `manufacturing_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `naturalresources_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `production_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `transport_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `unemployment_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `percapita_income_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `population_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `totalincome_city_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `lfpr_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `management_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `manufacturing_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `naturalresources_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `percapita_income_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `population_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `production_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `totalincome_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `transport_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `unemployment_county_lag3` | float | 6,347/10,404 | 61.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `hous_com_dev_curr_opr` | float | 6,318/10,404 | 60.7% | 2012–2023 | 12 | 533 | 2024, 2025 |
| `cen_staff_construction` | float | 6,115/10,404 | 58.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `sewerage_curr_oper` | float | 6,041/10,404 | 58.1% | 2012–2023 | 12 | 514 | 2024, 2025 |
| `chg_regular_highways` | float | 5,908/10,404 | 56.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `ltd_issued_other` | float | 5,855/10,404 | 56.3% | 2012–2023 | 12 | 539 | 2024, 2025 |
| `judicial_curr_oper` | float | 5,816/10,404 | 55.9% | 2012–2023 | 12 | 525 | 2024, 2025 |
| `reg_hwy_construction` | float | 5,792/10,404 | 55.7% | 2012–2023 | 12 | 529 | 2024, 2025 |
| `percapita_income_state_lag3` | float | 5,770/10,404 | 55.5% | 2014–2023 | 10 | 547 | 2013, 2024, 2025 |
| `population_state_lag3` | float | 5,770/10,404 | 55.5% | 2014–2023 | 10 | 547 | 2013, 2024, 2025 |
| `totalincome_state_lag3` | float | 5,770/10,404 | 55.5% | 2014–2023 | 10 | 547 | 2013, 2024, 2025 |
| `unemployment_state_lag3` | float | 5,770/10,404 | 55.5% | 2014–2023 | 10 | 547 | 2013, 2024, 2025 |
| `lfpr_state_lag3` | float | 5,770/10,404 | 55.5% | 2014–2023 | 10 | 547 | 2013, 2024, 2025 |
| `chg_housing_&_comm_dev` | float | 5,707/10,404 | 54.9% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `solid_wst_curr_oper` | float | 5,689/10,404 | 54.7% | 2012–2023 | 12 | 488 | 2024, 2025 |
| `water_util_curr_oper` | float | 5,613/10,404 | 54.0% | 2012–2023 | 12 | 464 | 2024, 2025 |
| `prot_insp_curr_oper` | float | 5,512/10,404 | 53.0% | 2012–2023 | 12 | 497 | 2024, 2025 |
| `other_fund_cash_sec` | float | 5,452/10,404 | 52.4% | 2012–2021 | 10 | 547 | 2022, 2023, 2024, 2025 |
| `libraries_construction` | float | 5,173/10,404 | 49.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `transit_utility_rev` | float | 5,135/10,404 | 49.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_igr_hous/com_dev` | float | 5,101/10,404 | 49.0% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `chg_misc_com_activ` | float | 5,067/10,404 | 48.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `parks_rec_construction` | float | 5,034/10,404 | 48.4% | 2012–2023 | 12 | 507 | 2024, 2025 |
| `chg_air_transportation` | float | 4,969/10,404 | 47.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `other_gen_construction` | float | 4,802/10,404 | 46.2% | 2012–2023 | 12 | 522 | 2024, 2025 |
| `fed_igr_highways` | float | 4,772/10,404 | 45.9% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `taxes_nec` | float | 4,684/10,404 | 45.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `health_curr_oper` | float | 4,663/10,404 | 44.8% | 2012–2023 | 12 | 440 | 2024, 2025 |
| `health_construction` | float | 4,641/10,404 | 44.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `docum_and_stock_tr_tax` | float | 4,632/10,404 | 44.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `air_trans_construction` | float | 4,598/10,404 | 44.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `alcoholic_beverage_lic` | float | 4,590/10,404 | 44.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `prot_insp_construction` | float | 4,549/10,404 | 43.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `bond_fund_cash_sec` | float | 4,548/10,404 | 43.7% | 2012–2021 | 10 | 525 | 2022, 2023, 2024, 2025 |
| `local_igr_oth_gen_sup` | float | 4,536/10,404 | 43.6% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `sinking_fund_cash_sec` | float | 4,506/10,404 | 43.3% | 2012–2021 | 10 | 506 | 2022, 2023, 2024, 2025 |
| `local_igr_highways` | float | 4,448/10,404 | 42.8% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `parking_construction` | float | 4,452/10,404 | 42.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `water_util_interest` | float | 4,417/10,404 | 42.5% | 2012–2023 | 12 | 410 | 2024, 2025 |
| `judicial_construction` | float | 4,268/10,404 | 41.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_igr_health_&_hos` | float | 4,269/10,404 | 41.0% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `pension_expenditure_burden` | float | 4,254/10,404 | 40.9% | 2007–2016 | 10 | 547 | 9 yrs missing |
| `pension_exp_own_source` | float | 4,254/10,404 | 40.9% | 2007–2016 | 10 | 547 | 9 yrs missing |
| `state_igr_sewerage` | float | 4,189/10,404 | 40.3% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `fed_igr_air_transport` | float | 4,152/10,404 | 39.9% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `state_igr_transit_sub` | float | 4,151/10,404 | 39.9% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `fed_igr_transit_sub` | float | 4,144/10,404 | 39.8% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `state_igr_public_welf` | float | 4,124/10,404 | 39.6% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `gen_bldg_curr_oper` | float | 4,114/10,404 | 39.5% | 2012–2023 | 12 | 397 | 2024, 2025 |
| `chg_total_nat_res` | float | 4,057/10,404 | 39.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `libraries_curr_oper` | float | 4,015/10,404 | 38.6% | 2012–2023 | 12 | 354 | 2024, 2025 |
| `motor_vehicle_license` | float | 3,982/10,404 | 38.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `electric_utility_rev` | float | 3,964/10,404 | 38.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_igr_health_&_hos` | float | 3,962/10,404 | 38.1% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `local_igr_hous/com_dev` | float | 3,858/10,404 | 37.1% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `amusement_tax` | float | 3,822/10,404 | 36.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `other_gen_oth_cap` | float | 3,790/10,404 | 36.4% | 2012–2021 | 10 | 483 | 2022, 2023, 2024, 2025 |
| `fed_igr_public_welf` | float | 3,774/10,404 | 36.3% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `police_prot_oth_cap` | float | 3,772/10,404 | 36.3% | 2012–2021 | 10 | 461 | 2022, 2023, 2024, 2025 |
| `elec_util_construct` | float | 3,678/10,404 | 35.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_igr_gen_support` | float | 3,663/10,404 | 35.2% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `elem_educ_construction` | float | 3,604/10,404 | 34.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `misc_com_activ_constr` | float | 3,578/10,404 | 34.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `state_igr_education` | float | 3,580/10,404 | 34.4% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `chg_elem_ed_nec` | float | 3,540/10,404 | 34.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `chg_elem_ed_sch_lunch` | float | 3,530/10,404 | 33.9% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `parks_rec_oth_cap` | float | 3,502/10,404 | 33.7% | 2012–2021 | 10 | 443 | 2022, 2023, 2024, 2025 |
| `amusement_license` | float | 3,494/10,404 | 33.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `air_trans_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `air_trans_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `air_trans_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `air_trans_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `air_trans_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `alcoholic_beverage_tax` | float | 3,468/10,404 | 33.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `beg_ltd_out_all_other` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_education` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_priv_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `beg_ltd_out_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `bond_fd_cash_&_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `cen_staff_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `cen_staff_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `cen_staff_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `cen_staff_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `cen_staff_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `census_region` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `chg_total_education` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `correct_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `correct_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `correct_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `correct_ig_to_st` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `correct_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_assistance` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_construction` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `educ_nec_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elec_util_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elec_util_inter_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elec_util_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elem_educ_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elem_educ_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elem_educ_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elem_educ_ig_sch_to_sch` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elem_educ_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `elem_educ_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_benefit_paymts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_from_other_gov` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_int_rev` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_loc_emp_ctrib` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_loc_to_loc_sys` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_other_paymts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_sta_to_sta_ctr` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_total_ctrib` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_ret_withdrawals` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_cash_&_dep` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_cash_&_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_corp_bds` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_corp_stk` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_misc_inv` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_mortgages` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_oth_nong` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_s&l_secur` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_tot_fed` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_sec_tot_nong` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_retire_total_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_sec_adm_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_sec_adm_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `emp_sec_adm_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fed_igr_gen_rev_shar` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fin_admin_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fin_admin_construction` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fin_admin_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fin_admin_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fin_admin_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fin_admin_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fips7` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fips_code_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fire_prot_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fire_prot_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fire_prot_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fire_prot_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fyenddate` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `gas_util_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `gas_util_inter_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `gas_util_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `gen_pub_bldg_cap_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `gen_pub_bldg_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `gen_pub_bldg_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_assist_&_sub` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_construction` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_current_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_current_oper` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_ig_to_fed` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_ig_to_st` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `general_nec_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `health_capital_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `health_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `health_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `health_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `health_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `higher_ed_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `higher_ed_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `higher_ed_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `higher_ed_ig_to_st` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `higher_ed_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hosp_other_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hosp_other_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hosp_other_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hosp_other_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hosp_other_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hosp_other_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hous_&_com_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hous_&_com_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hous_&_com_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hous_&_com_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `hunting_&_fishing_license` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `idchanged` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ig_exp_to_federal_govt` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ig_exp_to_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ig_exp_to_state_govt` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `imputed_record` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `insur_trust_cash_&_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `interest_on_gen_debt` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `jacketunit` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `judicial_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `judicial_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `judicial_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `judicial_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `judicial_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `libraries_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `libraries_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `libraries_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `libraries_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `liquor_stores_cap_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `liquor_stores_constr` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `liquor_stores_tot_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `local_igr_interschool_aid` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `local_igr_transit_sub` | float | 3,460/10,404 | 33.3% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `ltd_iss_all_other` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ffc_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_gen_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_gen_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_gen_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_ng_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_unsp_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_util_electric` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_util_gas_supply` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_util_transit` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_util_water` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_iss_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_all_other` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ffc_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_gen_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_gen_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_gen_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_ng_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_util_electric` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_util_gas_supply` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_util_transit` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_out_util_water` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_all_other` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ffc_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_gen_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_gen_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_gen_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_elec_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_ng_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_private_purp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_elec_utili` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_elem_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_gas_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_general` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_other_educ` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_other_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_trans_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_unsp_water_util` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_util_electric` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_util_gas_supply` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_util_transit` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_util_water` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ltd_ret_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `misc_com_activ_cap_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `misc_com_activ_tot_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `natural_res_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `natural_res_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `natural_res_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `natural_res_ig_to_sta` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `oth_nonin_fd_cash_&_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `own_hospital_cap_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `own_hospital_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `own_hospital_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parking_capital_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parking_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parking_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parking_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parking_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parks_&_rec_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parks_&_rec_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parks_&_rec_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `parks_&_rec_ig_to_sta` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `police_prot_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `police_prot_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `police_prot_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `police_prot_ig_to_sta` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `police_prot_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `population` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `prot_insp_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `prot_insp_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `prot_insp_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `prot_insp_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `prot_insp_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `public_welf_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `public_welf_cash_asst` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `public_welf_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `public_welf_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `public_welf_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `regular_hwy_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `regular_hwy_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `regular_hwy_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `regular_hwy_ig_to_sta` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sewerage_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sewerage_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sewerage_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sewerage_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sewerage_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sinking_fd_cash_&_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sortcode` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `state_code` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `state_igr_tax_relief` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `surveyyr` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sw_mgmt_capital_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sw_mgmt_construction` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sw_mgmt_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sw_mgmt_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sw_mgmt_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `sw_mgmt_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `toll_hwy_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `toll_hwy_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `tot_assist_&_subsidies` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `tot_ins_trust_inv_rev` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `tot_ltd_out_ng` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_beg_ltd_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_cash_&_securities` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_current_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_educ_assist_&_sub` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_educ_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_educ_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_educ_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_educ_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_highways_cap_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_highways_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_highways_dir_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_highways_tot_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_hospital_cap_out` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_hospital_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_hospital_dir_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_hospital_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_hospital_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_hospital_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ig_expenditure` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_insur_trust_ctrb` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_interest_on_debt` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_iss_ffc` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_iss_ng` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_iss_unsp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_out_ffc` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_out_utility` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_ret_ffc` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_ret_ng` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_ltd_ret_unsp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_unemp_rev` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_util_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_util_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_util_inter_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `total_util_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `trans_util_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `trans_util_construct` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `trans_util_inter_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `trans_util_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `transit_sub_direct_sub` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `transit_sub_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `transit_sub_ig_to_sta` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `transit_sub_to_own_sys` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `transit_sub_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `type_code` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_comp_bal_in_us_trs` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_comp_ben_paymts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_comp_cash_&_sec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_comp_other_balance` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_comp_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_ext_&_spec_pmts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_federal_advances` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_int_revenue` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `unemp_payroll_tax` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `vetbonus` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_trans_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_trans_direct_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_trans_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_trans_ig_to_sta` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_trans_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_util_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_util_inter_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `water_util_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `weight` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_cash_cash_assist` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_cash_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_cash_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_categ_cash_assist` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_categ_ig_loc_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_categ_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_categ_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_ins_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_ins_construction` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_ins_total_exp` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_nec_cap_outlay` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_nec_construction` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_nec_direct_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_nec_ig_local_govts` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_nec_ig_to_state` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_nec_total_expend` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_state_share_part_d` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_vend_pmts_medical` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `welf_vend_pmts_nec` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `year4` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `yearpop` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `zerodata` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `ig_exp_share` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `revenue_bonds_outstanding` | float | 3,462/10,404 | 33.3% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `go_bond_share_outstanding` | float | 3,459/10,404 | 33.2% | 2007–2012 | 6 | 547 | 13 yrs missing |
| `fed_igr_sewerage` | float | 3,444/10,404 | 33.1% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `individual_income_tax` | float | 3,445/10,404 | 33.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `hous_com_dev_construct` | float | 3,373/10,404 | 32.4% | 2012–2023 | 12 | 401 | 2024, 2025 |
| `chg_elem_ed_tuition` | float | 3,345/10,404 | 32.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `local_igr_other_education` | float | 3,349/10,404 | 32.2% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `motor_fuels_tax` | float | 3,345/10,404 | 32.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_igr_education` | float | 3,320/10,404 | 31.9% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `local_igr_sewerage` | float | 3,320/10,404 | 31.9% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `chg_water_transport` | float | 3,275/10,404 | 31.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fire_prot_oth_cap` | float | 3,276/10,404 | 31.5% | 2012–2021 | 10 | 421 | 2022, 2023, 2024, 2025 |
| `public_utility_license` | float | 3,259/10,404 | 31.3% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `insurance_premium_tax` | float | 3,240/10,404 | 31.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `local_igr_health_&_hos` | float | 3,226/10,404 | 31.0% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `local_igr_public_welf` | float | 3,228/10,404 | 31.0% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `gas_utility_rev` | float | 3,190/10,404 | 30.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `tobacco_tax` | float | 3,158/10,404 | 30.4% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `parking_curr_oper` | float | 3,139/10,404 | 30.2% | 2012–2023 | 12 | 299 | 2024, 2025 |
| `fed_igr_natural_res` | float | 3,132/10,404 | 30.1% | 2007–2021 | 15 | 547 | 2022, 2023, 2024, 2025 |
| `reg_hwy_oth_cap` | float | 3,115/10,404 | 29.9% | 2012–2021 | 10 | 415 | 2022, 2023, 2024, 2025 |
| `correct_construct` | float | 3,101/10,404 | 29.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `gas_util_construct` | float | 3,076/10,404 | 29.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `chg_hospitals` | float | 3,026/10,404 | 29.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `water_trans_construct` | float | 3,023/10,404 | 29.1% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `corp_net_income_tax` | float | 2,984/10,404 | 28.7% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `liquor_stores_revenue` | float | 2,891/10,404 | 27.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `pari_mutuels_tax` | float | 2,890/10,404 | 27.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `toll_hwy_construction` | float | 2,891/10,404 | 27.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `chg_toll_highways` | float | 2,868/10,404 | 27.6% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `death_and_gift_tax` | float | 2,861/10,404 | 27.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `severance_tax` | float | 2,866/10,404 | 27.5% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `motor_veh_oper_license` | float | 2,827/10,404 | 27.2% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `chg_total_high_ed` | float | 2,808/10,404 | 27.0% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `corporation_license` | float | 2,801/10,404 | 26.9% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `higher_ed_construct` | float | 2,800/10,404 | 26.9% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `emp_ret_other_earnings` | float | 2,788/10,404 | 26.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `net_lottery_revenue` | float | 2,788/10,404 | 26.8% | 2007–2023 | 17 | 547 | 2024, 2025 |
| `fed_igr_emp_sec_adm` | float | 2,780/10,404 | 26.7% | 2007–2015 | 9 | 547 | 10 yrs missing |
| `go_bond_share_issuance` | float | 2,758/10,404 | 26.5% | 2007–2012 | 6 | 538 | 13 yrs missing |
| `transit_curr_oper` | float | 2,602/10,404 | 25.0% | 2012–2023 | 12 | 256 | 2024, 2025 |
| `cen_staff_oth_cap` | float | 2,530/10,404 | 24.3% | 2012–2021 | 10 | 386 | 2022, 2023, 2024, 2025 |
| `ltd_beg_pdpp` | float | 2,309/10,404 | 22.2% | 2012–2021 | 10 | 288 | 2022, 2023, 2024, 2025 |
| `sewerage_oth_cap` | float | 2,309/10,404 | 22.2% | 2012–2021 | 10 | 360 | 2022, 2023, 2024, 2025 |
| `water_util_oth_cap` | float | 2,312/10,404 | 22.2% | 2012–2021 | 10 | 334 | 2022, 2023, 2024, 2025 |
| `air_trans_curr_oper` | float | 2,283/10,404 | 21.9% | 2012–2023 | 12 | 198 | 2024, 2025 |
| `nat_res_curr_oper` | float | 2,255/10,404 | 21.7% | 2012–2023 | 12 | 268 | 2024, 2025 |
| `ltd_outstanding_pdpp` | float | 2,240/10,404 | 21.5% | 2012–2021 | 10 | 282 | 2022, 2023, 2024, 2025 |
| `gen_bldg_construction` | float | 1,991/10,404 | 19.1% | 2012–2023 | 12 | 296 | 2024, 2025 |
| `ltd_retired_pdpp` | float | 1,932/10,404 | 18.6% | 2012–2021 | 10 | 260 | 2022, 2023, 2024, 2025 |
| `hous_com_dev_oth_cap` | float | 1,892/10,404 | 18.2% | 2012–2021 | 10 | 333 | 2022, 2023, 2024, 2025 |
| `welfare_nec_curr_oper` | float | 1,870/10,404 | 18.0% | 2012–2023 | 12 | 231 | 2024, 2025 |
| `solid_wst_oth_cap` | float | 1,766/10,404 | 17.0% | 2012–2021 | 10 | 283 | 2022, 2023, 2024, 2025 |
| `finan_adm_oth_cap` | float | 1,758/10,404 | 16.9% | 2012–2021 | 10 | 306 | 2022, 2023, 2024, 2025 |
| `solid_wst_construction` | float | 1,743/10,404 | 16.8% | 2012–2023 | 12 | 267 | 2024, 2025 |
| `misc_com_curr_oper` | float | 1,711/10,404 | 16.4% | 2012–2023 | 12 | 192 | 2024, 2025 |
| `other_gen_payroll` | float | 1,612/10,404 | 15.5% | 2012–2023 | 12 | 328 | 2024, 2025 |
| `gen_bldg_oth_cap` | float | 1,434/10,404 | 13.8% | 2012–2021 | 10 | 249 | 2022, 2023, 2024, 2025 |
| `libraries_oth_cap` | float | 1,346/10,404 | 12.9% | 2012–2021 | 10 | 211 | 2022, 2023, 2024, 2025 |
| `judicial_oth_cap` | float | 1,220/10,404 | 11.7% | 2012–2021 | 10 | 218 | 2022, 2023, 2024, 2025 |
| `std_beg_outstanding` | float | 1,206/10,404 | 11.6% | 2012–2023 | 12 | 180 | 2024, 2025 |
| `std_end_outstanding` | float | 1,191/10,404 | 11.4% | 2012–2023 | 12 | 172 | 2024, 2025 |
| `prot_insp_oth_cap` | float | 1,179/10,404 | 11.3% | 2012–2021 | 10 | 209 | 2022, 2023, 2024, 2025 |
| `ins_trust_elem_ed` | float | 1,152/10,404 | 11.1% | 2012–2016 | 5 | 284 | 9 yrs missing |
| `ins_trust_education` | float | 1,123/10,404 | 10.8% | 2012–2016 | 5 | 283 | 9 yrs missing |
| `elec_util_curr_oper` | float | 1,103/10,404 | 10.6% | 2012–2023 | 12 | 104 | 2024, 2025 |
| `health_oth_cap` | float | 1,100/10,404 | 10.6% | 2012–2021 | 10 | 200 | 2022, 2023, 2024, 2025 |
| `ins_trust_other_ed` | float | 1,107/10,404 | 10.6% | 2012–2016 | 5 | 278 | 9 yrs missing |
| `transit_construction` | float | 1,098/10,404 | 10.6% | 2012–2023 | 12 | 164 | 2024, 2025 |
| `ins_trust_highways` | float | 1,015/10,404 | 9.8% | 2012–2016 | 5 | 261 | 9 yrs missing |
| `pension_benefit_payments` | float | 1,001/10,404 | 9.6% | 2012–2016 | 5 | 259 | 9 yrs missing |
| `ins_trust_air_trans` | float | 954/10,404 | 9.2% | 2012–2016 | 5 | 231 | 9 yrs missing |
| `other_benefit_payments` | float | 961/10,404 | 9.2% | 2012–2016 | 5 | 235 | 9 yrs missing |
| `transit_oth_cap` | float | 941/10,404 | 9.0% | 2012–2021 | 10 | 153 | 2022, 2023, 2024, 2025 |
| `ins_trust_higher_ed` | float | 892/10,404 | 8.6% | 2012–2016 | 5 | 244 | 9 yrs missing |
| `elem_educ_curr_oper` | float | 884/10,404 | 8.5% | 2012–2023 | 12 | 87 | 2024, 2025 |
| `state_igr_water_util` | float | 882/10,404 | 8.5% | 2012–2021 | 10 | 202 | 2022, 2023, 2024, 2025 |
| `correct_curr_oper` | float | 875/10,404 | 8.4% | 2012–2023 | 12 | 91 | 2024, 2025 |
| `ins_trust_gen_support` | float | 841/10,404 | 8.1% | 2012–2016 | 5 | 234 | 9 yrs missing |
| `nat_res_construction` | float | 842/10,404 | 8.1% | 2012–2023 | 12 | 167 | 2024, 2025 |
| `air_trans_oth_cap` | float | 800/10,404 | 7.7% | 2012–2021 | 10 | 130 | 2022, 2023, 2024, 2025 |
| `parking_oth_cap` | float | 783/10,404 | 7.5% | 2012–2021 | 10 | 154 | 2022, 2023, 2024, 2025 |
| `elec_util_interest` | float | 774/10,404 | 7.4% | 2012–2023 | 12 | 79 | 2024, 2025 |
| `ins_trust_housing` | float | 746/10,404 | 7.2% | 2012–2016 | 5 | 212 | 9 yrs missing |
| `nat_res_oth_cap` | float | 750/10,404 | 7.2% | 2012–2021 | 10 | 147 | 2022, 2023, 2024, 2025 |
| `finan_adm_construction` | float | 742/10,404 | 7.1% | 2012–2023 | 12 | 187 | 2024, 2025 |
| `elem_educ_payroll` | float | 699/10,404 | 6.7% | 2012–2021 | 10 | 98 | 2022, 2023, 2024, 2025 |
| `ins_trust_corrections` | float | 688/10,404 | 6.6% | 2012–2016 | 5 | 226 | 9 yrs missing |
| `elem_educ_oth_cap` | float | 662/10,404 | 6.4% | 2012–2021 | 10 | 74 | 2022, 2023, 2024, 2025 |
| `other_gen_fte` | float | 671/10,404 | 6.4% | 2012–2023 | 12 | 133 | 2024, 2025 |
| `royalties` | float | 501/10,404 | 4.8% | 2012–2023 | 12 | 68 | 2024, 2025 |
| `health_payroll` | float | 477/10,404 | 4.6% | 2012–2021 | 10 | 93 | 2022, 2023, 2024, 2025 |
| `fed_igr_water_util` | float | 467/10,404 | 4.5% | 2012–2021 | 10 | 121 | 2022, 2023, 2024, 2025 |
| `misc_com_oth_cap` | float | 436/10,404 | 4.2% | 2012–2021 | 10 | 92 | 2022, 2023, 2024, 2025 |
| `police_payroll` | float | 412/10,404 | 4.0% | 2012–2021 | 10 | 94 | 2022, 2023, 2024, 2025 |
| `sewerage_payroll` | float | 405/10,404 | 3.9% | 2012–2021 | 10 | 81 | 2022, 2023, 2024, 2025 |
| `water_trans_curr_oper` | float | 397/10,404 | 3.8% | 2012–2023 | 12 | 54 | 2024, 2025 |
| `elec_util_oth_cap` | float | 384/10,404 | 3.7% | 2012–2021 | 10 | 68 | 2022, 2023, 2024, 2025 |
| `ltd_issued_pdpp` | float | 377/10,404 | 3.6% | 2012–2021 | 10 | 108 | 2022, 2023, 2024, 2025 |
| `correct_curr_other` | float | 364/10,404 | 3.5% | 2012–2023 | 12 | 47 | 2024, 2025 |
| `gas_util_curr_oper` | float | 340/10,404 | 3.3% | 2012–2023 | 12 | 39 | 2024, 2025 |
| `correction_payroll` | float | 323/10,404 | 3.1% | 2012–2021 | 10 | 50 | 2022, 2023, 2024, 2025 |
| `housing_payroll` | float | 323/10,404 | 3.1% | 2012–2021 | 10 | 88 | 2022, 2023, 2024, 2025 |
| `transit_payroll` | float | 316/10,404 | 3.0% | 2012–2021 | 10 | 63 | 2022, 2023, 2024, 2025 |
| `financial_admin_payroll` | float | 300/10,404 | 2.9% | 2012–2021 | 10 | 52 | 2022, 2023, 2024, 2025 |
| `notes` | str | 306/10,404 | 2.9% | 2007–2024 | 18 | 20 | 2025 |
| `water_util_payroll` | float | 276/10,404 | 2.7% | 2012–2021 | 10 | 75 | 2022, 2023, 2024, 2025 |
| `welfare_nec_oth_cap` | float | 272/10,404 | 2.6% | 2012–2021 | 10 | 73 | 2022, 2023, 2024, 2025 |
| `highways_payroll` | float | 247/10,404 | 2.4% | 2012–2021 | 10 | 68 | 2022, 2023, 2024, 2025 |
| `local_igr_water_util` | float | 253/10,404 | 2.4% | 2012–2021 | 10 | 71 | 2022, 2023, 2024, 2025 |
| `central_staff_payroll` | float | 238/10,404 | 2.3% | 2012–2021 | 10 | 42 | 2022, 2023, 2024, 2025 |
| `correct_oth_cap` | float | 214/10,404 | 2.1% | 2012–2021 | 10 | 51 | 2022, 2023, 2024, 2025 |
| `highways_fte` | float | 218/10,404 | 2.1% | 2012–2021 | 10 | 49 | 2022, 2023, 2024, 2025 |
| `transit_fte` | float | 215/10,404 | 2.1% | 2012–2021 | 10 | 27 | 2022, 2023, 2024, 2025 |
| `gas_util_interest` | float | 207/10,404 | 2.0% | 2012–2023 | 12 | 21 | 2024, 2025 |
| `parks_rec_payroll` | float | 210/10,404 | 2.0% | 2012–2021 | 10 | 53 | 2022, 2023, 2024, 2025 |
| `transit_interest` | float | 208/10,404 | 2.0% | 2012–2023 | 12 | 46 | 2024, 2025 |
| `welfare_nec_construct` | float | 212/10,404 | 2.0% | 2012–2023 | 12 | 59 | 2024, 2025 |
| `hospitals_curr_oper` | float | 178/10,404 | 1.7% | 2012–2023 | 12 | 23 | 2024, 2025 |
| `fire_prot_payroll` | float | 165/10,404 | 1.6% | 2012–2021 | 10 | 52 | 2022, 2023, 2024, 2025 |
| `judicial_payroll` | float | 158/10,404 | 1.5% | 2012–2021 | 10 | 44 | 2022, 2023, 2024, 2025 |
| `sewerage_fte` | float | 161/10,404 | 1.5% | 2012–2021 | 10 | 30 | 2022, 2023, 2024, 2025 |
| `hospitals_construction` | float | 142/10,404 | 1.4% | 2012–2023 | 12 | 13 | 2024, 2025 |
| `solid_waste_payroll` | float | 146/10,404 | 1.4% | 2012–2021 | 10 | 38 | 2022, 2023, 2024, 2025 |
| `state_igr_elec_util` | float | 150/10,404 | 1.4% | 2012–2021 | 10 | 32 | 2022, 2023, 2024, 2025 |
| `vendor_cash_nec` | float | 147/10,404 | 1.4% | 2012–2021 | 10 | 27 | 2022, 2023, 2024, 2025 |
| `workers_comp_benefits` | float | 138/10,404 | 1.3% | 2012–2021 | 10 | 27 | 2022, 2023, 2024, 2025 |
| `air_trans_payroll` | float | 122/10,404 | 1.2% | 2012–2021 | 10 | 28 | 2022, 2023, 2024, 2025 |
| `districts_change_year` | str | 126/10,404 | 1.2% | 2007–2024 | 18 | 9 | 2025 |
| `fed_igr_elec_util` | float | 115/10,404 | 1.1% | 2012–2021 | 10 | 32 | 2022, 2023, 2024, 2025 |
| `libraries_payroll` | float | 115/10,404 | 1.1% | 2012–2021 | 10 | 27 | 2022, 2023, 2024, 2025 |
| `liq_str_curr_oper` | float | 115/10,404 | 1.1% | 2012–2023 | 12 | 10 | 2024, 2025 |
| `water_util_fte` | float | 116/10,404 | 1.1% | 2012–2021 | 10 | 27 | 2022, 2023, 2024, 2025 |
| `gas_util_oth_cap` | float | 105/10,404 | 1.0% | 2012–2021 | 10 | 19 | 2022, 2023, 2024, 2025 |
| `nat_res_payroll` | float | 101/10,404 | 1.0% | 2012–2021 | 10 | 32 | 2022, 2023, 2024, 2025 |
| `fog_change_year` | str | 108/10,404 | 1.0% | 2007–2024 | 18 | 6 | 2025 |
| `hospitals_oth_cap` | float | 90/10,404 | 0.9% | 2012–2021 | 10 | 11 | 2022, 2023, 2024, 2025 |
| `toll_hwy_curr_oper` | float | 94/10,404 | 0.9% | 2012–2023 | 12 | 12 | 2024, 2025 |
| `welfare_nec_payroll` | float | 92/10,404 | 0.9% | 2012–2021 | 10 | 21 | 2022, 2023, 2024, 2025 |
| `correct_oth_cap_other` | float | 68/10,404 | 0.7% | 2012–2021 | 10 | 19 | 2022, 2023, 2024, 2025 |
| `police_fte` | float | 69/10,404 | 0.7% | 2012–2021 | 10 | 22 | 2022, 2023, 2024, 2025 |
| `unemployment_benefits` | float | 73/10,404 | 0.7% | 2012–2021 | 10 | 13 | 2022, 2023, 2024, 2025 |
| `welfare_inst_curr_opr` | float | 78/10,404 | 0.7% | 2012–2023 | 12 | 26 | 2024, 2025 |
| `judicial_fte` | float | 60/10,404 | 0.6% | 2012–2021 | 10 | 16 | 2022, 2023, 2024, 2025 |
| `local_igr_elec_util` | float | 58/10,404 | 0.6% | 2012–2021 | 10 | 17 | 2022, 2023, 2024, 2025 |
| `chg_higher_ed` | float | 53/10,404 | 0.5% | 2012–2023 | 12 | 5 | 2024, 2025 |
| `elem_educ_fte` | float | 55/10,404 | 0.5% | 2012–2021 | 10 | 13 | 2022, 2023, 2024, 2025 |
| `higher_ed_curr_oper` | float | 53/10,404 | 0.5% | 2012–2023 | 12 | 5 | 2024, 2025 |
| `toll_hwy_oth_cap` | float | 52/10,404 | 0.5% | 2012–2021 | 10 | 10 | 2022, 2023, 2024, 2025 |
| `vendor_cash_med` | float | 51/10,404 | 0.5% | 2012–2021 | 10 | 13 | 2022, 2023, 2024, 2025 |
| `termlength_change_year` | str | 54/10,404 | 0.5% | 2007–2024 | 18 | 3 | 2025 |
| `air_trans_fte` | float | 46/10,404 | 0.4% | 2012–2021 | 10 | 9 | 2022, 2023, 2024, 2025 |
| `central_staff_fte` | float | 44/10,404 | 0.4% | 2013–2021 | 9 | 9 | 2022, 2023, 2024, 2025 |
| `financial_admin_fte` | float | 37/10,404 | 0.4% | 2012–2021 | 10 | 9 | 2022, 2023, 2024, 2025 |
| `health_fte` | float | 44/10,404 | 0.4% | 2012–2021 | 10 | 10 | 2022, 2023, 2024, 2025 |
| `housing_fte` | float | 38/10,404 | 0.4% | 2012–2021 | 10 | 18 | 2022, 2023, 2024, 2025 |
| `ins_trust_health_hosp` | float | 43/10,404 | 0.4% | 2012–2016 | 5 | 19 | 9 yrs missing |
| `water_trans_oth_cap` | float | 41/10,404 | 0.4% | 2012–2021 | 10 | 10 | 2022, 2023, 2024, 2025 |
| `correction_payroll_oth` | float | 32/10,404 | 0.3% | 2012–2021 | 10 | 11 | 2022, 2023, 2024, 2025 |
| `elec_util_payroll` | float | 33/10,404 | 0.3% | 2012–2021 | 10 | 12 | 2022, 2023, 2024, 2025 |
| `elem_educ_assist_sub` | float | 27/10,404 | 0.3% | 2012–2023 | 12 | 3 | 2024, 2025 |
| `parks_rec_fte` | float | 36/10,404 | 0.3% | 2012–2021 | 10 | 13 | 2022, 2023, 2024, 2025 |
| `protective_insp_payroll` | float | 28/10,404 | 0.3% | 2012–2021 | 10 | 7 | 2022, 2023, 2024, 2025 |
| `partisan_change_year` | float | 36/10,404 | 0.3% | 2007–2024 | 18 | 3 | 2025 |
| `termlimits_change_year` | float | 36/10,404 | 0.3% | 2007–2024 | 18 | 2 | 2025 |
| `correct_constr_other` | float | 25/10,404 | 0.2% | 2012–2023 | 12 | 9 | 2024, 2025 |
| `fed_igr_gas_util` | float | 16/10,404 | 0.2% | 2012–2021 | 10 | 5 | 2022, 2023, 2024, 2025 |
| `gas_util_fte` | float | 19/10,404 | 0.2% | 2012–2021 | 10 | 3 | 2022, 2023, 2024, 2025 |
| `higher_ed_oth_cap` | float | 20/10,404 | 0.2% | 2012–2021 | 10 | 2 | 2022, 2023, 2024, 2025 |
| `higher_ed_payroll` | float | 18/10,404 | 0.2% | 2012–2018 | 7 | 9 | 7 yrs missing |
| `libraries_fte` | float | 22/10,404 | 0.2% | 2012–2021 | 10 | 5 | 2022, 2023, 2024, 2025 |
| `liq_str_oth_cap` | float | 18/10,404 | 0.2% | 2012–2021 | 10 | 4 | 2022, 2023, 2024, 2025 |
| `natural_resources_fte` | float | 19/10,404 | 0.2% | 2013–2020 | 8 | 6 | 2021, 2022, 2023, 2024, 2025 |
| `parking_payroll` | float | 26/10,404 | 0.2% | 2012–2021 | 10 | 12 | 2022, 2023, 2024, 2025 |
| `state_igr_gas_util` | float | 25/10,404 | 0.2% | 2012–2021 | 10 | 7 | 2022, 2023, 2024, 2025 |
| `welfare_inst_construct` | float | 20/10,404 | 0.2% | 2017–2023 | 7 | 11 | 6 yrs missing |
| `welfare_nec_fte` | float | 23/10,404 | 0.2% | 2012–2021 | 10 | 8 | 2022, 2023, 2024, 2025 |
| `correction_fte_other` | float | 9/10,404 | 0.1% | 2012–2020 | 7 | 3 | 7 yrs missing |
| `emp_ret_contributions` | float | 12/10,404 | 0.1% | 2012–2023 | 12 | 1 | 2024, 2025 |
| `emp_ret_interest` | float | 12/10,404 | 0.1% | 2012–2023 | 12 | 1 | 2024, 2025 |
| `emp_ret_loc_to_loc` | float | 12/10,404 | 0.1% | 2012–2023 | 12 | 1 | 2024, 2025 |
| `emp_ret_state_contrib` | float | 11/10,404 | 0.1% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `emp_sec_curr_oper` | float | 12/10,404 | 0.1% | 2012–2023 | 12 | 1 | 2024, 2025 |
| `emp_sec_oth_cap` | float | 10/10,404 | 0.1% | 2012–2021 | 10 | 1 | 2022, 2023, 2024, 2025 |
| `gas_util_payroll` | float | 14/10,404 | 0.1% | 2012–2020 | 9 | 5 | 2021, 2022, 2023, 2024, 2025 |
| `higher_ed_fte` | float | 10/10,404 | 0.1% | 2012–2019 | 8 | 3 | 6 yrs missing |
| `hospitals_fte` | float | 12/10,404 | 0.1% | 2012–2021 | 10 | 3 | 2022, 2023, 2024, 2025 |
| `hospitals_payroll` | float | 15/10,404 | 0.1% | 2012–2021 | 10 | 2 | 2022, 2023, 2024, 2025 |
| `ins_benefit_payments` | float | 11/10,404 | 0.1% | 2022–2023 | 2 | 7 | 11 yrs missing |
| `public_welf_fte` | float | 15/10,404 | 0.1% | 2012–2021 | 10 | 2 | 2022, 2023, 2024, 2025 |
| `solid_waste_fte` | float | 14/10,404 | 0.1% | 2012–2021 | 9 | 4 | 2013, 2022, 2023, 2024, 2025 |
| `water_trans_fte` | float | 8/10,404 | 0.1% | 2017–2020 | 4 | 3 | 9 yrs missing |
| `water_trans_payroll` | float | 13/10,404 | 0.1% | 2012–2021 | 10 | 3 | 2022, 2023, 2024, 2025 |
| `welfare_inst_oth_cap` | float | 6/10,404 | 0.1% | 2012–2020 | 4 | 3 | 10 yrs missing |
| `correction_fte` | float | 2/10,404 | 0.0% | 2015–2016 | 2 | 1 | 11 yrs missing |
| `emp_ret_from_state` | float | 4/10,404 | 0.0% | 2012–2015 | 4 | 1 | 10 yrs missing |
| `emp_ret_loc_contrib` | float | 1/10,404 | 0.0% | 2012–2012 | 1 | 1 | 13 yrs missing |
| `emp_sec_construction` | float | 2/10,404 | 0.0% | 2022–2023 | 2 | 1 | 11 yrs missing |
| `liq_str_construction` | float | 3/10,404 | 0.0% | 2022–2023 | 2 | 2 | 11 yrs missing |
| `local_igr_gas_util` | float | 2/10,404 | 0.0% | 2013–2014 | 2 | 1 | 11 yrs missing |
| `protective_insp_fte` | float | 5/10,404 | 0.0% | 2012–2018 | 4 | 4 | 10 yrs missing |

### Fiscal TEL Merged 2013-2025
**File:** `raw/fiscal/fiscal_tel_merged_2013_2025.csv.gz`  
**Shape:** 6,936 rows × 1544 columns  
**City column:** `city_name` (548 unique cities)  
**Year column:** `year` — range 2013-2024 (12 years)  
**Panel-window coverage (2013–2025):** 12/13 years  
**Missing panel years:** 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `fog` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `termlimits` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `termlength` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `districts` | str | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `City_Total_Amt_Issued` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `City_Total_Issuance_Count` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `City_Green_Amt_Issued` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `City_Green_Issuance_Count` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Biodiversity,_Clean_Transportation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Biodiversity,_Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Circular_Economy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Clean_Transportation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Clean_Transportation,_Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Clean_Transportation,_Pollution_Control` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Clean_Transportation,_Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Clean_Transportation,_Sustainable_Water` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Climate_Change_Adaptation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Natural_Resource_Management` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Pollution_Control` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Pollution_Control,_Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Pollution_Control,_Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Renewable_Energy,_Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Renewable_Energy,_Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Renewable_Energy,_Sustainable_Water` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Sustainable_Water` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Sustainable_Water,_Circular_Economy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Sustainable_Water,_Climate_Change_Adaptation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Sustainable_Water,_Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Amt_ESG Project Categories__Sustainable_Water,_Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Biodiversity,_Clean_Transportation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Biodiversity,_Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Circular_Economy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Clean_Transportation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Clean_Transportation,_Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Clean_Transportation,_Pollution_Control` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Clean_Transportation,_Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Clean_Transportation,_Sustainable_Water` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Climate_Change_Adaptation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Natural_Resource_Management` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Pollution_Control` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Pollution_Control,_Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Pollution_Control,_Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Renewable_Energy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Renewable_Energy,_Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Renewable_Energy,_Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Renewable_Energy,_Sustainable_Water` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Sustainable_Water` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Sustainable_Water,_Circular_Economy` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Sustainable_Water,_Climate_Change_Adaptation` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Sustainable_Water,_Energy_Efficiency` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG Project Categories__Sustainable_Water,_Green_Buildings` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG_Assurance_Yes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG_Framework_Yes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `Count_ESG_Reporting_Yes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `State_Total_Amt_Issued` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `State_Total_Issuance_Count` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `State_Govt_Amt_Issued` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `State_Govt_Issuance_Count` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `STATE_FIPS` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `YEAR` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_insp_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_insp_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_insp_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_violations` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_enf_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_enf_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_penalty_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_enf_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_penalty_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_penalty_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_informal_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_informal_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_informal_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_rcra_violations` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_rcra_enf_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_air_violations` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_air_enf_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_air_enf_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_air_penalty_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_air_enf_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_viol_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_viol_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_viol_health_based` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_enf_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_enf_epa` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_enf_state` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_viol_total` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_npdes_facilities` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_rcra_facilities` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_air_facilities` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_sdwa_systems` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_epa_insp_share_npdes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_epa_enf_share_sdwa` | float | 6,935/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_avg_penalty_epa_npdes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_avg_penalty_state_npdes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_penalty_ratio_epa_state_npdes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_detection_rate_npdes` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_state_insp_rate_npdes_norm` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_avg_penalty_state_npdes_norm` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_state_stringency_index` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_num_antiesg_laws` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_antiesg_law` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_first_law_year` | float | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_law_restricted_pension` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_law_restricted_contracts` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_law_proxy_voting` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_law_esg_score_ban_govt` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_law_esg_score_ban_private` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_law_civil_liability` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_cum_exec_actions` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_msrb_letter_signatory` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_governor_alliance_member` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_muni_bond_law` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `esg_has_underwriter_block` | int | 6,936/6,936 | 100.0% | 2013–2024 | 12 | 548 | 2025 |
| `partisan` | float | 6,912/6,936 | 99.7% | 2013–2024 | 12 | 546 | 2025 |
| `gov_party` | str | 6,912/6,936 | 99.7% | 2013–2024 | 12 | 547 | 2025 |
| `dem_trifecta` | float | 6,912/6,936 | 99.7% | 2013–2024 | 12 | 547 | 2025 |
| `rep_trifecta` | float | 6,912/6,936 | 99.7% | 2013–2024 | 12 | 547 | 2025 |
| `divided_govt` | float | 6,912/6,936 | 99.7% | 2013–2024 | 12 | 547 | 2025 |
| `NAME_city` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `NAME_county` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `multi_county_averaged` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Population (2020)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Building Value ($)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Agriculture Value ($)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `National Risk Index - Value - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `National Risk Index - Score - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `National Risk Index - Rating - Composite` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `National Risk Index - State Percentile - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Score - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Rating - Composite` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - State Percentile - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Total - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Building Value - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Population - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Population Equivalence - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss - Agriculture Value - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss Rate - Building - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss Rate - Population - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss Rate - Agriculture - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Expected Annual Loss Rate - National Percentile - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Social Vulnerability and Community Resilience Adjusted Expected Annual Loss Rate - National Percentile - Composite` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Social Vulnerability - Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Social Vulnerability - Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Social Vulnerability - State Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Community Resilience - Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Community Resilience - Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Community Resilience - State Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Community Resilience - Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Community Risk Factor - Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Avalanche - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Avalanche - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Avalanche - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Coastal Flooding - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Coastal Flooding - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Coastal Flooding - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Cold Wave - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Drought - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Earthquake - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hail - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Heat Wave - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Heat Wave - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Heat Wave - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hurricane - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hurricane - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Hurricane - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Ice Storm - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Ice Storm - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Ice Storm - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Landslide - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Lightning - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Inland Flooding - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Strong Wind - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tornado - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tsunami - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tsunami - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Tsunami - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Volcanic Activity - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Volcanic Activity - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Volcanic Activity - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Wildfire - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Number of Events` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Annualized Frequency` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Exposure - Impacted Area (sq mi)` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Exposure - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Exposure - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Exposure - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Exposure - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Exposure - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Historic Loss Ratio - Buildings` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Historic Loss Ratio - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Historic Loss Ratio - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Historic Loss Ratio - Total Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss - Building Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss - Population Equivalence` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss - Agriculture Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss - Total` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss Rate - Building` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss Rate - Population` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss Rate - Agriculture` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Expected Annual Loss Rate - National Percentile` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Hazard Type Risk Index Value` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Hazard Type Risk Index Score` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Winter Weather - Hazard Type Risk Index Rating` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `National Risk Index Version` | str | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Shape__Area` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `Shape__Length` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `county_fips5` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `dem_vote_share` | float | 6,876/6,936 | 99.1% | 2013–2024 | 12 | 543 | 2025 |
| `CITY_ID` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_permit_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_is_major_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_permit_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_is_major_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_permit_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_is_major_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_qncr_record_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_has_violation_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_effluent_violations_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_qncr_record_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_has_violation_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_effluent_violations_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_qncr_record_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_has_violation_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_qncr_effluent_violations_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_se_viol_violation_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_se_viol_violation_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_se_viol_violation_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_formal_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_penalty_amt_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_is_epa_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_is_state_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_formal_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_penalty_amt_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_is_epa_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_is_state_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_formal_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_penalty_amt_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_is_epa_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_formal_is_state_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_informal_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_is_epa_informal_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_is_state_informal_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_informal_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_is_epa_informal_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_is_state_informal_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_informal_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_is_epa_informal_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_informal_is_state_informal_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_inspection_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_is_epa_inspection_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_is_state_inspection_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_inspection_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_is_epa_inspection_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_is_state_inspection_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_inspection_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_is_epa_inspection_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_npdes_insp_is_state_inspection_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_facility_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_is_lqg_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_is_sqg_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_facility_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_is_lqg_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_is_sqg_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_facility_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_is_lqg_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_is_sqg_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_viol_violation_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_viol_violation_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_viol_violation_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_enforcement_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_is_epa_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_is_state_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_enforcement_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_is_epa_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_is_state_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_enforcement_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_is_epa_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_rcra_enf_is_state_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_facility_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_is_major_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_is_hpv_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_facility_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_is_major_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_is_hpv_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_facility_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_is_major_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_is_hpv_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_viol_violation_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_viol_is_hpv_violation_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_viol_violation_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_viol_is_hpv_violation_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_viol_violation_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_viol_is_hpv_violation_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_formal_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_is_epa_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_is_state_action_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_formal_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_is_epa_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_is_state_action_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_formal_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_is_epa_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_air_formal_is_state_action_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_case_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_consent_decree_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_epa_lead_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_state_lead_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_case_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_consent_decree_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_epa_lead_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_state_lead_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_case_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_consent_decree_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_epa_lead_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_is_state_lead_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_concl_conclusion_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_concl_conclusion_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_case_concl_conclusion_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_system_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_population_served_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_is_community_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_system_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_population_served_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_is_community_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_system_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_population_served_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_is_community_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_violation_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_health_based_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_major_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_mcl_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_lead_copper_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_viol_by_epa_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_viol_by_state_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_has_enforcement_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_enf_by_epa_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_enf_by_state_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_violation_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_health_based_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_major_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_mcl_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_lead_copper_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_viol_by_epa_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_viol_by_state_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_has_enforcement_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_enf_by_epa_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_enf_by_state_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_violation_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_health_based_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_major_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_mcl_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_is_lead_copper_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_viol_by_epa_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_viol_by_state_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_has_enforcement_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_enf_by_epa_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sdwa_viol_enf_by_state_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_event_count_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_discharge_volume_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_duration_hours_all_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_event_count_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_discharge_volume_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_duration_hours_muni_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_event_count_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_discharge_volume_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_sewer_duration_hours_locgov_x` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `epa_fips7` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Number of Events` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Annualized Frequency` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Exposure - Impacted Area (sq mi)` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Exposure - Building Value` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Exposure - Population` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Exposure - Population Equivalence` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Exposure - Agriculture Value` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Exposure - Total` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Historic Loss Ratio - Buildings` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Historic Loss Ratio - Population` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Historic Loss Ratio - Agriculture` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss - Building Value` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss - Population` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss - Population Equivalence` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss - Agriculture Value` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss - Total` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss Score` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss Rate - Building` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss Rate - Population` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss Rate - Agriculture` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Expected Annual Loss Rate - National Percentile` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Hazard Type Risk Index Value` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `Heat Wave - Hazard Type Risk Index Score` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `consumption_lag3` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `log_consumption_lag3` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `production_lag3` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `log_production_lag3` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `has_facilities_lag1` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `has_facilities_lag2` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `has_facilities_lag3` | float | 6,864/6,936 | 99.0% | 2013–2024 | 12 | 542 | 2025 |
| `legis_control` | str | 6,866/6,936 | 99.0% | 2013–2024 | 12 | 547 | 2025 |
| `state_control` | str | 6,866/6,936 | 99.0% | 2013–2024 | 12 | 547 | 2025 |
| `state_stringency_epa_enf_share_npdes` | float | 6,863/6,936 | 98.9% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_avg_penalty_npdes` | float | 6,863/6,936 | 98.9% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_epa_enf_share_air` | float | 6,850/6,936 | 98.8% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_avg_penalty_air` | float | 6,850/6,936 | 98.8% | 2013–2024 | 12 | 548 | 2025 |
| `TOT_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `log_TOT_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `TOT_mean_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `prod_cons_ratio_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `log_prod_cons_ratio_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `ONR_share_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `COM_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `log_COM_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `COM_share_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `ONR_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `log_ONR_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `RES_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `log_RES_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `RES_share_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `IND_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `log_IND_total_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `IND_share_lag3` | float | 6,840/6,936 | 98.6% | 2013–2024 | 12 | 540 | 2025 |
| `total_bridges` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `deficient_bridges` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `poor_bridges` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `fair_bridges` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `good_bridges` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `bridge_imp_cost_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `roadway_imp_cost_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `total_imp_cost_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `imp_cost_per_bridge_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `bridge_imp_cost_real_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `roadway_imp_cost_real_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `total_imp_cost_real_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `imp_cost_per_bridge_real_k` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `total_deck_area_sqm` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `deficient_deck_area_sqm` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `total_adt` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `avg_bridge_age` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `scour_critical_count` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `pct_deficient` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `pct_poor` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `cwns_needs_real` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `cwns_source` | str | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_violations` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_enf_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_enf_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_penalty_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_enf_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_penalty_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_penalty_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_violations` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_violations` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_enf_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_enf_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_penalty_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_enf_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_health_based` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_enf_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_enf_epa` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_enf_state` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_total` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_facilities` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_facilities` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_facilities` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_systems` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_epa_insp_share_npdes` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_epa_enf_share_sdwa` | float | 6,811/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_avg_penalty_epa_npdes` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_avg_penalty_state_npdes` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_penalty_ratio_epa_state_npdes` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_detection_rate_npdes` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_state_insp_rate_npdes_norm` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_avg_penalty_state_npdes_norm` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_state_stringency_index` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_permit_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_is_major_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_permit_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_is_major_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_permit_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_is_major_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_qncr_record_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_has_violation_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_effluent_violations_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_qncr_record_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_has_violation_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_effluent_violations_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_qncr_record_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_has_violation_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_qncr_effluent_violations_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_se_viol_violation_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_se_viol_violation_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_se_viol_violation_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_formal_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_penalty_amt_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_is_epa_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_is_state_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_formal_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_penalty_amt_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_is_epa_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_is_state_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_formal_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_penalty_amt_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_is_epa_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_formal_is_state_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_informal_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_is_epa_informal_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_is_state_informal_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_informal_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_is_epa_informal_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_is_state_informal_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_informal_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_is_epa_informal_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_informal_is_state_informal_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_inspection_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_is_epa_inspection_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_is_state_inspection_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_inspection_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_is_epa_inspection_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_is_state_inspection_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_inspection_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_is_epa_inspection_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_npdes_insp_is_state_inspection_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_facility_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_is_lqg_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_is_sqg_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_facility_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_is_lqg_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_is_sqg_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_facility_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_is_lqg_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_is_sqg_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_viol_violation_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_viol_violation_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_viol_violation_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_enforcement_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_is_epa_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_is_state_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_enforcement_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_is_epa_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_is_state_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_enforcement_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_is_epa_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_rcra_enf_is_state_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_facility_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_is_major_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_is_hpv_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_facility_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_is_major_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_is_hpv_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_facility_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_is_major_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_is_hpv_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_viol_violation_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_viol_is_hpv_violation_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_viol_violation_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_viol_is_hpv_violation_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_viol_violation_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_viol_is_hpv_violation_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_formal_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_is_epa_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_is_state_action_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_formal_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_is_epa_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_is_state_action_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_formal_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_is_epa_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_air_formal_is_state_action_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_case_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_consent_decree_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_epa_lead_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_state_lead_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_case_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_consent_decree_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_epa_lead_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_state_lead_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_case_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_consent_decree_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_epa_lead_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_is_state_lead_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_concl_conclusion_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_concl_conclusion_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_case_concl_conclusion_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_system_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_population_served_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_is_community_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_system_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_population_served_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_is_community_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_system_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_population_served_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_is_community_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_violation_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_health_based_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_major_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_mcl_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_lead_copper_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_viol_by_epa_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_viol_by_state_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_has_enforcement_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_enf_by_epa_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_enf_by_state_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_violation_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_health_based_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_major_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_mcl_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_lead_copper_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_viol_by_epa_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_viol_by_state_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_has_enforcement_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_enf_by_epa_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_enf_by_state_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_violation_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_health_based_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_major_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_mcl_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_is_lead_copper_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_viol_by_epa_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_viol_by_state_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_has_enforcement_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_enf_by_epa_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sdwa_viol_enf_by_state_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_event_count_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_discharge_volume_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_duration_hours_all_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_event_count_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_discharge_volume_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_duration_hours_muni_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_event_count_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_discharge_volume_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_sewer_duration_hours_locgov_y` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `deflator` | float | 6,812/6,936 | 98.2% | 2013–2024 | 12 | 540 | 2025 |
| `state_srf_per_capita` | float | 6,800/6,936 | 98.0% | 2013–2024 | 12 | 539 | 2025 |
| `state_srf_per_gdp` | float | 6,800/6,936 | 98.0% | 2013–2024 | 12 | 539 | 2025 |
| `state_srf_cumulative` | float | 6,800/6,936 | 98.0% | 2013–2024 | 12 | 539 | 2025 |
| `state_srf_commitment` | float | 6,800/6,936 | 98.0% | 2013–2024 | 12 | 539 | 2025 |
| `initiative` | float | 6,792/6,936 | 97.9% | 2013–2024 | 12 | 537 | 2025 |
| `referendum` | float | 6,792/6,936 | 97.9% | 2013–2024 | 12 | 537 | 2025 |
| `avg_min_condition` | float | 6,783/6,936 | 97.8% | 2013–2024 | 12 | 538 | 2025 |
| `epa_epa_enf_share_npdes` | float | 6,739/6,936 | 97.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_avg_penalty_npdes` | float | 6,739/6,936 | 97.2% | 2013–2024 | 12 | 540 | 2025 |
| `epa_epa_enf_share_air` | float | 6,727/6,936 | 97.0% | 2013–2024 | 12 | 540 | 2025 |
| `epa_avg_penalty_air` | float | 6,727/6,936 | 97.0% | 2013–2024 | 12 | 540 | 2025 |
| `mayor_name` | str | 6,708/6,936 | 96.7% | 2013–2024 | 12 | 529 | 2025 |
| `years_since_election` | float | 6,581/6,936 | 94.9% | 2013–2024 | 12 | 529 | 2025 |
| `election_vote_share` | float | 6,561/6,936 | 94.6% | 2013–2024 | 12 | 529 | 2025 |
| `cwns_flow_interp` | float | 6,344/6,936 | 91.5% | 2013–2024 | 12 | 509 | 2025 |
| `cwns_facilities_interp` | float | 6,344/6,936 | 91.5% | 2013–2024 | 12 | 509 | 2025 |
| `state_stringency_state_response_rate_npdes` | float | 6,329/6,936 | 91.2% | 2013–2024 | 12 | 548 | 2025 |
| `state_stringency_state_response_rate_npdes_norm` | float | 6,329/6,936 | 91.2% | 2013–2024 | 12 | 548 | 2025 |
| `consensus` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `devharm` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `fundrenewables` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `futuregen` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `happening` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `harmus` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `human` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `personal` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `regulate` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `timing` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `worried` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `consumption_lag2` | float | 6,292/6,936 | 90.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `log_consumption_lag2` | float | 6,292/6,936 | 90.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `production_lag2` | float | 6,292/6,936 | 90.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `log_production_lag2` | float | 6,292/6,936 | 90.7% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `consumption_lag4` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `log_consumption_lag4` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `production_lag4` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `log_production_lag4` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `has_facilities_lag4` | float | 6,292/6,936 | 90.7% | 2014–2024 | 11 | 542 | 2013, 2025 |
| `income_pc` | float | 6,281/6,936 | 90.6% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `population` | float | 6,281/6,936 | 90.6% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `log_pop` | float | 6,281/6,936 | 90.6% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `log_income` | float | 6,281/6,936 | 90.6% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `TOT_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_TOT_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `TOT_mean_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `prod_cons_ratio_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_prod_cons_ratio_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `ONR_share_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `COM_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_COM_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `COM_share_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `ONR_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_ONR_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `RES_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_RES_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `RES_share_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `IND_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_IND_total_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `IND_share_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `delta_log_TOT_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `pct_change_TOT_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `delta_log_production_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `delta_log_consumption_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `delta_prod_cons_ratio_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `TOT_total_ma2_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_TOT_total_ma2_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `log_production_ma2_lag2` | float | 6,270/6,936 | 90.4% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `TOT_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_TOT_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `TOT_mean_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `prod_cons_ratio_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_prod_cons_ratio_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `ONR_share_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `COM_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_COM_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `COM_share_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `ONR_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_ONR_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `RES_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_RES_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `RES_share_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `IND_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_IND_total_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `IND_share_lag4` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `delta_log_TOT_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `pct_change_TOT_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `delta_log_production_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `delta_log_consumption_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `delta_prod_cons_ratio_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `TOT_total_ma2_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_TOT_total_ma2_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `log_production_ma2_lag3` | float | 6,270/6,936 | 90.4% | 2014–2024 | 11 | 540 | 2013, 2025 |
| `state_stringency_state_response_rate_air` | float | 6,266/6,936 | 90.3% | 2013–2024 | 12 | 546 | 2025 |
| `epa_state_response_rate_npdes` | float | 6,207/6,936 | 89.5% | 2013–2024 | 12 | 540 | 2025 |
| `epa_state_response_rate_npdes_norm` | float | 6,207/6,936 | 89.5% | 2013–2024 | 12 | 540 | 2025 |
| `epa_state_response_rate_air` | float | 6,159/6,936 | 88.8% | 2013–2024 | 12 | 538 | 2025 |
| `mayor_party` | str | 6,129/6,936 | 88.4% | 2013–2024 | 12 | 520 | 2025 |
| `consumption_lag1` | float | 5,720/6,936 | 82.5% | 2013–2022 | 10 | 542 | 2023, 2024, 2025 |
| `log_consumption_lag1` | float | 5,720/6,936 | 82.5% | 2013–2022 | 10 | 542 | 2023, 2024, 2025 |
| `production_lag1` | float | 5,720/6,936 | 82.5% | 2013–2022 | 10 | 542 | 2023, 2024, 2025 |
| `log_production_lag1` | float | 5,720/6,936 | 82.5% | 2013–2022 | 10 | 542 | 2023, 2024, 2025 |
| `TOT_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_TOT_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `TOT_mean_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `prod_cons_ratio_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_prod_cons_ratio_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `ONR_share_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `COM_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_COM_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `COM_share_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `ONR_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_ONR_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `RES_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_RES_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `RES_share_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `IND_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_IND_total_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `IND_share_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `delta_log_TOT_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `pct_change_TOT_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `delta_log_production_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `delta_log_consumption_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `delta_prod_cons_ratio_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `TOT_total_ma2_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_TOT_total_ma2_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_production_ma2_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `TOT_total_ma3_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_TOT_total_ma3_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `log_production_ma3_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `prod_cons_ratio_ma3_lag1` | float | 5,700/6,936 | 82.2% | 2013–2022 | 10 | 540 | 2023, 2024, 2025 |
| `TOT_total_ma3_lag2` | float | 5,700/6,936 | 82.2% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `log_TOT_total_ma3_lag2` | float | 5,700/6,936 | 82.2% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `log_production_ma3_lag2` | float | 5,700/6,936 | 82.2% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `prod_cons_ratio_ma3_lag2` | float | 5,700/6,936 | 82.2% | 2014–2023 | 10 | 540 | 2013, 2024, 2025 |
| `delta_log_TOT_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `pct_change_TOT_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `delta_log_production_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `delta_log_consumption_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `delta_prod_cons_ratio_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `TOT_total_ma3_lag3` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `log_TOT_total_ma3_lag3` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `log_production_ma3_lag3` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `prod_cons_ratio_ma3_lag3` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `TOT_total_ma2_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `log_TOT_total_ma2_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `log_production_ma2_lag4` | float | 5,700/6,936 | 82.2% | 2015–2024 | 10 | 540 | 2013, 2014, 2025 |
| `fiscal_T01` | float | 5,700/6,936 | 82.2% | 2013–2023 | 11 | 538 | 2024, 2025 |
| `fiscal_19U` | float | 5,674/6,936 | 81.8% | 2013–2023 | 11 | 538 | 2024, 2025 |
| `fiscal_E62` | float | 5,676/6,936 | 81.8% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `fiscal_49U` | float | 5,646/6,936 | 81.4% | 2013–2023 | 11 | 538 | 2024, 2025 |
| `fiscal_E29` | float | 5,646/6,936 | 81.4% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `fiscal_I89` | float | 5,641/6,936 | 81.3% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `fiscal_E44` | float | 5,623/6,936 | 81.1% | 2013–2023 | 11 | 538 | 2024, 2025 |
| `fiscal_39U` | float | 5,604/6,936 | 80.8% | 2013–2023 | 11 | 538 | 2024, 2025 |
| `fiscal_U20` | float | 5,566/6,936 | 80.2% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `fiscal_U99` | float | 5,563/6,936 | 80.2% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `fiscal_E61` | float | 5,553/6,936 | 80.1% | 2013–2023 | 11 | 533 | 2024, 2025 |
| `fiscal_E89` | float | 5,488/6,936 | 79.1% | 2013–2023 | 11 | 535 | 2024, 2025 |
| `fiscal_A89` | float | 5,476/6,936 | 79.0% | 2013–2023 | 11 | 536 | 2024, 2025 |
| `fiscal_C89` | float | 5,463/6,936 | 78.8% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `fiscal_E24` | float | 5,464/6,936 | 78.8% | 2013–2023 | 11 | 520 | 2024, 2025 |
| `fiscal_U30` | float | 5,413/6,936 | 78.0% | 2013–2023 | 11 | 531 | 2024, 2025 |
| `Hurricane - Number of Events` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Annualized Frequency` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Exposure - Impacted Area (sq mi)` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Exposure - Building Value` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Exposure - Population` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Exposure - Population Equivalence` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Exposure - Agriculture Value` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Exposure - Total` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Historic Loss Ratio - Buildings` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Historic Loss Ratio - Population` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Historic Loss Ratio - Agriculture` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss - Building Value` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss - Population` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss - Population Equivalence` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss - Agriculture Value` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss - Total` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss Score` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss Rate - Building` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss Rate - Population` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss Rate - Agriculture` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Expected Annual Loss Rate - National Percentile` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Hazard Type Risk Index Value` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `Hurricane - Hazard Type Risk Index Score` | float | 5,388/6,936 | 77.7% | 2013–2024 | 12 | 429 | 2025 |
| `fiscal_E23` | float | 5,352/6,936 | 77.2% | 2013–2023 | 11 | 537 | 2024, 2025 |
| `fiscal_T29` | float | 5,272/6,936 | 76.0% | 2013–2023 | 11 | 526 | 2024, 2025 |
| `discuss` | float | 5,148/6,936 | 74.2% | 2016–2024 | 9 | 542 | 2013, 2014, 2015, 2025 |
| `harmplants` | float | 5,148/6,936 | 74.2% | 2016–2024 | 9 | 542 | 2013, 2014, 2015, 2025 |
| `teachgw` | float | 5,148/6,936 | 74.2% | 2016–2024 | 9 | 542 | 2013, 2014, 2015, 2025 |
| `fiscal_E50` | float | 5,139/6,936 | 74.1% | 2013–2023 | 11 | 521 | 2024, 2025 |
| `delta_log_TOT_3yr_lag1` | float | 5,130/6,936 | 74.0% | 2014–2022 | 9 | 540 | 2013, 2023, 2024, 2025 |
| `delta_log_production_3yr_lag1` | float | 5,130/6,936 | 74.0% | 2014–2022 | 9 | 540 | 2013, 2023, 2024, 2025 |
| `delta_log_TOT_3yr_lag2` | float | 5,130/6,936 | 74.0% | 2015–2023 | 9 | 540 | 2013, 2014, 2024, 2025 |
| `delta_log_production_3yr_lag2` | float | 5,130/6,936 | 74.0% | 2015–2023 | 9 | 540 | 2013, 2014, 2024, 2025 |
| `delta_log_TOT_3yr_lag3` | float | 5,130/6,936 | 74.0% | 2016–2024 | 9 | 540 | 2013, 2014, 2015, 2025 |
| `delta_log_production_3yr_lag3` | float | 5,130/6,936 | 74.0% | 2016–2024 | 9 | 540 | 2013, 2014, 2015, 2025 |
| `TOT_total_ma3_lag4` | float | 5,130/6,936 | 74.0% | 2016–2024 | 9 | 540 | 2013, 2014, 2015, 2025 |
| `log_TOT_total_ma3_lag4` | float | 5,130/6,936 | 74.0% | 2016–2024 | 9 | 540 | 2013, 2014, 2015, 2025 |
| `log_production_ma3_lag4` | float | 5,130/6,936 | 74.0% | 2016–2024 | 9 | 540 | 2013, 2014, 2015, 2025 |
| `prod_cons_ratio_ma3_lag4` | float | 5,130/6,936 | 74.0% | 2016–2024 | 9 | 540 | 2013, 2014, 2015, 2025 |
| `fiscal_A61` | float | 5,134/6,936 | 74.0% | 2013–2023 | 11 | 517 | 2024, 2025 |
| `Ice Storm - Number of Events` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Annualized Frequency` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Exposure - Impacted Area (sq mi)` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Exposure - Building Value` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Exposure - Population` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Exposure - Population Equivalence` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Exposure - Total` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Historic Loss Ratio - Buildings` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Historic Loss Ratio - Population` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss - Building Value` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss - Population` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss - Population Equivalence` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss - Total` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss Score` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss Rate - Building` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss Rate - Population` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Expected Annual Loss Rate - National Percentile` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Hazard Type Risk Index Value` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `Ice Storm - Hazard Type Risk Index Score` | float | 5,124/6,936 | 73.9% | 2013–2024 | 12 | 403 | 2025 |
| `fiscal_A80` | float | 5,034/6,936 | 72.6% | 2013–2023 | 11 | 502 | 2024, 2025 |
| `fiscal_E80` | float | 5,014/6,936 | 72.3% | 2013–2023 | 11 | 504 | 2024, 2025 |
| `fiscal_E25` | float | 4,826/6,936 | 69.6% | 2013–2023 | 11 | 501 | 2024, 2025 |
| `fiscal_A91` | float | 4,800/6,936 | 69.2% | 2013–2023 | 11 | 462 | 2024, 2025 |
| `fiscal_E81` | float | 4,725/6,936 | 68.1% | 2013–2023 | 11 | 479 | 2024, 2025 |
| `fiscal_E91` | float | 4,702/6,936 | 67.8% | 2013–2023 | 11 | 456 | 2024, 2025 |
| `unemployment_rate` | float | 4,690/6,936 | 67.6% | 2013–2023 | 11 | 407 | 2024, 2025 |
| `flight_emissions_lag2` | float | 4,641/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `log_flight_emissions_lag2` | float | 4,641/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `facility_count_lag2` | float | 4,641/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `log_facility_count_lag2` | float | 4,641/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `flight_emissions_lag3` | float | 4,643/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `log_flight_emissions_lag3` | float | 4,643/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `facility_count_lag3` | float | 4,643/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `log_facility_count_lag3` | float | 4,643/6,936 | 66.9% | 2013–2024 | 12 | 385 | 2025 |
| `flight_emissions_lag1` | float | 4,616/6,936 | 66.6% | 2013–2024 | 12 | 384 | 2025 |
| `log_flight_emissions_lag1` | float | 4,616/6,936 | 66.6% | 2013–2024 | 12 | 384 | 2025 |
| `facility_count_lag1` | float | 4,616/6,936 | 66.6% | 2013–2024 | 12 | 384 | 2025 |
| `log_facility_count_lag1` | float | 4,616/6,936 | 66.6% | 2013–2024 | 12 | 384 | 2025 |
| `flight_pct_of_vulcan_lag3` | float | 4,619/6,936 | 66.6% | 2013–2024 | 12 | 383 | 2025 |
| `flight_pct_of_production_lag3` | float | 4,620/6,936 | 66.6% | 2013–2024 | 12 | 383 | 2025 |
| `delta_log_flight_lag2` | float | 4,604/6,936 | 66.4% | 2013–2024 | 12 | 383 | 2025 |
| `pct_change_flight_lag2` | float | 4,604/6,936 | 66.4% | 2013–2024 | 12 | 383 | 2025 |
| `delta_facility_count_lag2` | float | 4,606/6,936 | 66.4% | 2013–2024 | 12 | 383 | 2025 |
| `log_flight_ma2_lag2` | float | 4,604/6,936 | 66.4% | 2013–2024 | 12 | 383 | 2025 |
| `delta_log_flight_lag1` | float | 4,600/6,936 | 66.3% | 2013–2024 | 12 | 383 | 2025 |
| `pct_change_flight_lag1` | float | 4,600/6,936 | 66.3% | 2013–2024 | 12 | 383 | 2025 |
| `delta_facility_count_lag1` | float | 4,602/6,936 | 66.3% | 2013–2024 | 12 | 383 | 2025 |
| `log_flight_ma2_lag1` | float | 4,600/6,936 | 66.3% | 2013–2024 | 12 | 383 | 2025 |
| `facility_count_ma3_lag1` | float | 4,569/6,936 | 65.9% | 2013–2024 | 12 | 383 | 2025 |
| `log_flight_ma3_lag1` | float | 4,567/6,936 | 65.8% | 2013–2024 | 12 | 383 | 2025 |
| `delta_log_TOT_3yr_lag4` | float | 4,560/6,936 | 65.7% | 2017–2024 | 8 | 540 | 2013, 2014, 2015, 2016, 2025 |
| `delta_log_production_3yr_lag4` | float | 4,560/6,936 | 65.7% | 2017–2024 | 8 | 540 | 2013, 2014, 2015, 2016, 2025 |
| `fiscal_B89` | float | 4,480/6,936 | 64.6% | 2013–2023 | 11 | 533 | 2024, 2025 |
| `fiscal_W61` | float | 4,474/6,936 | 64.5% | 2013–2021 | 9 | 535 | 2022, 2023, 2024, 2025 |
| `fiscal_E66` | float | 4,377/6,936 | 63.1% | 2013–2023 | 11 | 481 | 2024, 2025 |
| `fiscal_F44` | float | 4,303/6,936 | 62.0% | 2013–2023 | 11 | 519 | 2024, 2025 |
| `flight_emissions_lag4` | float | 4,265/6,936 | 61.5% | 2014–2024 | 11 | 385 | 2013, 2025 |
| `log_flight_emissions_lag4` | float | 4,265/6,936 | 61.5% | 2014–2024 | 11 | 385 | 2013, 2025 |
| `facility_count_lag4` | float | 4,265/6,936 | 61.5% | 2014–2024 | 11 | 385 | 2013, 2025 |
| `log_facility_count_lag4` | float | 4,265/6,936 | 61.5% | 2014–2024 | 11 | 385 | 2013, 2025 |
| `flight_pct_of_vulcan_lag2` | float | 4,243/6,936 | 61.2% | 2013–2023 | 11 | 383 | 2024, 2025 |
| `flight_pct_of_production_lag2` | float | 4,243/6,936 | 61.2% | 2013–2023 | 11 | 383 | 2024, 2025 |
| `flight_pct_of_vulcan_lag4` | float | 4,243/6,936 | 61.2% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `flight_pct_of_production_lag4` | float | 4,244/6,936 | 61.2% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `delta_log_flight_lag3` | float | 4,230/6,936 | 61.0% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `pct_change_flight_lag3` | float | 4,230/6,936 | 61.0% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `delta_facility_count_lag3` | float | 4,231/6,936 | 61.0% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `log_flight_ma2_lag3` | float | 4,230/6,936 | 61.0% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `fiscal_C30` | float | 4,209/6,936 | 60.7% | 2013–2021 | 9 | 523 | 2022, 2023, 2024, 2025 |
| `log_flight_ma3_lag2` | float | 4,194/6,936 | 60.5% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `facility_count_ma3_lag2` | float | 4,196/6,936 | 60.5% | 2014–2024 | 11 | 383 | 2013, 2025 |
| `delta_log_flight_3yr_lag1` | float | 4,162/6,936 | 60.0% | 2014–2024 | 11 | 382 | 2013, 2025 |
| `fiscal_T15` | float | 4,123/6,936 | 59.4% | 2013–2023 | 11 | 438 | 2024, 2025 |
| `fiscal_T19` | float | 4,091/6,936 | 59.0% | 2013–2023 | 11 | 432 | 2024, 2025 |
| `ELC_total_lag3` | float | 4,073/6,936 | 58.7% | 2013–2024 | 12 | 350 | 2025 |
| `log_ELC_total_lag3` | float | 4,073/6,936 | 58.7% | 2013–2024 | 12 | 350 | 2025 |
| `ELC_share_lag3` | float | 4,073/6,936 | 58.7% | 2013–2024 | 12 | 350 | 2025 |
| `fiscal_29U` | float | 4,061/6,936 | 58.5% | 2013–2023 | 11 | 528 | 2024, 2025 |
| `fiscal_A81` | float | 4,044/6,936 | 58.3% | 2013–2023 | 11 | 433 | 2024, 2025 |
| `fiscal_U40` | float | 4,031/6,936 | 58.1% | 2013–2023 | 11 | 461 | 2024, 2025 |
| `affectweather` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `citizens` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `congress` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `corporations` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `governor` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `localofficials` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `reducetax` | float | 4,004/6,936 | 57.7% | 2018–2024 | 7 | 542 | 6 yrs missing |
| `fiscal_C46` | float | 3,930/6,936 | 56.7% | 2013–2021 | 9 | 512 | 2022, 2023, 2024, 2025 |
| `fiscal_Z00` | float | 3,887/6,936 | 56.0% | 2013–2022 | 10 | 513 | 2023, 2024, 2025 |
| `delta_log_flight_lag4` | float | 3,853/6,936 | 55.6% | 2015–2024 | 10 | 383 | 2013, 2014, 2025 |
| `pct_change_flight_lag4` | float | 3,853/6,936 | 55.6% | 2015–2024 | 10 | 383 | 2013, 2014, 2025 |
| `delta_facility_count_lag4` | float | 3,853/6,936 | 55.6% | 2015–2024 | 10 | 383 | 2013, 2014, 2025 |
| `log_flight_ma2_lag4` | float | 3,853/6,936 | 55.6% | 2015–2024 | 10 | 383 | 2013, 2014, 2025 |
| `fiscal_D89` | float | 3,849/6,936 | 55.5% | 2013–2023 | 11 | 505 | 2024, 2025 |
| `flight_pct_of_vulcan_lag1` | float | 3,845/6,936 | 55.4% | 2013–2022 | 10 | 381 | 2023, 2024, 2025 |
| `flight_pct_of_production_lag1` | float | 3,845/6,936 | 55.4% | 2013–2022 | 10 | 381 | 2023, 2024, 2025 |
| `fiscal_U50` | float | 3,843/6,936 | 55.4% | 2013–2023 | 11 | 457 | 2024, 2025 |
| `log_flight_ma3_lag3` | float | 3,820/6,936 | 55.1% | 2015–2024 | 10 | 383 | 2013, 2014, 2025 |
| `facility_count_ma3_lag3` | float | 3,821/6,936 | 55.1% | 2015–2024 | 10 | 383 | 2013, 2014, 2025 |
| `delta_log_flight_3yr_lag2` | float | 3,789/6,936 | 54.6% | 2015–2024 | 10 | 382 | 2013, 2014, 2025 |
| `fiscal_T28` | float | 3,748/6,936 | 54.0% | 2013–2023 | 11 | 420 | 2024, 2025 |
| `ELC_total_lag4` | float | 3,739/6,936 | 53.9% | 2014–2024 | 11 | 349 | 2013, 2025 |
| `log_ELC_total_lag4` | float | 3,739/6,936 | 53.9% | 2014–2024 | 11 | 349 | 2013, 2025 |
| `ELC_share_lag4` | float | 3,739/6,936 | 53.9% | 2014–2024 | 11 | 349 | 2013, 2025 |
| `fiscal_B50` | float | 3,736/6,936 | 53.9% | 2013–2021 | 9 | 498 | 2022, 2023, 2024, 2025 |
| `ELC_total_lag2` | float | 3,733/6,936 | 53.8% | 2013–2023 | 11 | 349 | 2024, 2025 |
| `log_ELC_total_lag2` | float | 3,733/6,936 | 53.8% | 2013–2023 | 11 | 349 | 2024, 2025 |
| `ELC_share_lag2` | float | 3,733/6,936 | 53.8% | 2013–2023 | 11 | 349 | 2024, 2025 |
| `fiscal_E32` | float | 3,703/6,936 | 53.4% | 2013–2023 | 11 | 431 | 2024, 2025 |
| `fiscal_U11` | float | 3,703/6,936 | 53.4% | 2013–2023 | 11 | 469 | 2024, 2025 |
| `fiscal_W01` | float | 3,594/6,936 | 51.8% | 2013–2021 | 9 | 480 | 2022, 2023, 2024, 2025 |
| `fiscal_I91` | float | 3,585/6,936 | 51.7% | 2013–2023 | 11 | 403 | 2024, 2025 |
| `fiscal_F61` | float | 3,509/6,936 | 50.6% | 2013–2023 | 11 | 497 | 2024, 2025 |
| `fiscal_W31` | float | 3,478/6,936 | 50.1% | 2013–2021 | 9 | 511 | 2022, 2023, 2024, 2025 |
| `fiscal_E31` | float | 3,470/6,936 | 50.0% | 2013–2023 | 11 | 379 | 2024, 2025 |
| `log_flight_ma3_lag4` | float | 3,443/6,936 | 49.6% | 2016–2024 | 9 | 383 | 2013, 2014, 2015, 2025 |
| `facility_count_ma3_lag4` | float | 3,443/6,936 | 49.6% | 2016–2024 | 9 | 383 | 2013, 2014, 2015, 2025 |
| `fiscal_F89` | float | 3,430/6,936 | 49.5% | 2013–2023 | 11 | 513 | 2024, 2025 |
| `delta_log_flight_3yr_lag3` | float | 3,415/6,936 | 49.2% | 2016–2024 | 9 | 382 | 2013, 2014, 2015, 2025 |
| `avg_sufficiency` | float | 3,392/6,936 | 48.9% | 2013–2018 | 6 | 540 | 7 yrs missing |
| `ELC_total_lag1` | float | 3,393/6,936 | 48.9% | 2013–2022 | 10 | 348 | 2023, 2024, 2025 |
| `log_ELC_total_lag1` | float | 3,393/6,936 | 48.9% | 2013–2022 | 10 | 348 | 2023, 2024, 2025 |
| `ELC_share_lag1` | float | 3,393/6,936 | 48.9% | 2013–2022 | 10 | 348 | 2023, 2024, 2025 |
| `fiscal_F80` | float | 3,372/6,936 | 48.6% | 2013–2023 | 11 | 442 | 2024, 2025 |
| `fiscal_E52` | float | 3,299/6,936 | 47.6% | 2013–2023 | 11 | 346 | 2024, 2025 |
| `fiscal_T09` | float | 3,240/6,936 | 46.7% | 2013–2023 | 11 | 349 | 2024, 2025 |
| `fiscal_U01` | float | 3,238/6,936 | 46.7% | 2013–2023 | 11 | 412 | 2024, 2025 |
| `Coastal Flooding - Annualized Frequency` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Exposure - Impacted Area (sq mi)` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Exposure - Building Value` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Exposure - Population` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Exposure - Population Equivalence` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Exposure - Total` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Historic Loss Ratio - Buildings` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Historic Loss Ratio - Population` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss - Building Value` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss - Population` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss - Population Equivalence` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss - Total` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss Score` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss Rate - Building` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss Rate - Population` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Expected Annual Loss Rate - National Percentile` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Hazard Type Risk Index Value` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `Coastal Flooding - Hazard Type Risk Index Score` | float | 3,228/6,936 | 46.5% | 2013–2024 | 12 | 264 | 2025 |
| `fiscal_F91` | float | 3,212/6,936 | 46.3% | 2013–2023 | 11 | 410 | 2024, 2025 |
| `delta_log_flight_3yr_lag4` | float | 3,038/6,936 | 43.8% | 2017–2024 | 8 | 378 | 2013, 2014, 2015, 2016, 2025 |
| `fiscal_A60` | float | 2,933/6,936 | 42.3% | 2013–2023 | 11 | 312 | 2024, 2025 |
| `priority` | float | 2,860/6,936 | 41.2% | 2020–2024 | 5 | 542 | 8 yrs missing |
| `fiscal_G62` | float | 2,859/6,936 | 41.2% | 2013–2021 | 9 | 439 | 2022, 2023, 2024, 2025 |
| `fiscal_G89` | float | 2,757/6,936 | 39.7% | 2013–2021 | 9 | 465 | 2022, 2023, 2024, 2025 |
| `fiscal_E60` | float | 2,645/6,936 | 38.1% | 2013–2023 | 11 | 286 | 2024, 2025 |
| `fiscal_G61` | float | 2,622/6,936 | 37.8% | 2013–2021 | 9 | 429 | 2022, 2023, 2024, 2025 |
| `fiscal_G24` | float | 2,472/6,936 | 35.6% | 2013–2021 | 9 | 399 | 2022, 2023, 2024, 2025 |
| `fiscal_G44` | float | 2,303/6,936 | 33.2% | 2013–2021 | 9 | 394 | 2022, 2023, 2024, 2025 |
| `exp` | float | 2,288/6,936 | 33.0% | 2021–2024 | 4 | 542 | 9 yrs missing |
| `Avalanche - Number of Events` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Annualized Frequency` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Exposure - Impacted Area (sq mi)` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Exposure - Building Value` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Exposure - Population` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Exposure - Population Equivalence` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Exposure - Total` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Historic Loss Ratio - Buildings` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Historic Loss Ratio - Population` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss - Building Value` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss - Population` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss - Population Equivalence` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss - Total` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss Score` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss Rate - Building` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss Rate - Population` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Expected Annual Loss Rate - National Percentile` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Hazard Type Risk Index Value` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `Avalanche - Hazard Type Risk Index Score` | float | 2,280/6,936 | 32.9% | 2013–2024 | 12 | 185 | 2025 |
| `fiscal_F50` | float | 2,155/6,936 | 31.1% | 2013–2023 | 11 | 384 | 2024, 2025 |
| `fiscal_F62` | float | 2,141/6,936 | 30.9% | 2013–2023 | 11 | 457 | 2024, 2025 |
| `fiscal_E94` | float | 2,086/6,936 | 30.1% | 2013–2023 | 11 | 249 | 2024, 2025 |
| `fiscal_E01` | float | 1,939/6,936 | 28.0% | 2013–2023 | 11 | 192 | 2024, 2025 |
| `fiscal_A44` | float | 1,933/6,936 | 27.9% | 2013–2023 | 11 | 291 | 2024, 2025 |
| `fiscal_A50` | float | 1,852/6,936 | 26.7% | 2013–2023 | 11 | 277 | 2024, 2025 |
| `fiscal_F24` | float | 1,844/6,936 | 26.6% | 2013–2023 | 11 | 392 | 2024, 2025 |
| `fiscal_19T` | float | 1,826/6,936 | 26.3% | 2013–2021 | 9 | 274 | 2022, 2023, 2024, 2025 |
| `fiscal_A01` | float | 1,817/6,936 | 26.2% | 2013–2023 | 11 | 181 | 2024, 2025 |
| `fiscal_E59` | float | 1,803/6,936 | 26.0% | 2013–2023 | 11 | 250 | 2024, 2025 |
| `fiscal_G29` | float | 1,803/6,936 | 26.0% | 2013–2021 | 9 | 366 | 2022, 2023, 2024, 2025 |
| `fiscal_44T` | float | 1,776/6,936 | 25.6% | 2013–2021 | 9 | 267 | 2022, 2023, 2024, 2025 |
| `fiscal_G91` | float | 1,723/6,936 | 24.8% | 2013–2021 | 9 | 322 | 2022, 2023, 2024, 2025 |
| `generaterenewable` | float | 1,716/6,936 | 24.7% | 2022–2024 | 3 | 542 | 10 yrs missing |
| `fiscal_A94` | float | 1,674/6,936 | 24.1% | 2013–2023 | 11 | 194 | 2024, 2025 |
| `fiscal_A03` | float | 1,652/6,936 | 23.8% | 2013–2023 | 11 | 200 | 2024, 2025 |
| `fiscal_G80` | float | 1,640/6,936 | 23.6% | 2013–2021 | 9 | 336 | 2022, 2023, 2024, 2025 |
| `fiscal_E79` | float | 1,511/6,936 | 21.8% | 2013–2023 | 11 | 218 | 2024, 2025 |
| `Volcanic Activity - Number of Events` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Annualized Frequency` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Exposure - Impacted Area (sq mi)` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Exposure - Building Value` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Exposure - Population` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Exposure - Population Equivalence` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Exposure - Total` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Historic Loss Ratio - Buildings` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Historic Loss Ratio - Population` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss - Building Value` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss - Population` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss - Population Equivalence` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss - Total` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss Score` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss Rate - Building` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss Rate - Population` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Expected Annual Loss Rate - National Percentile` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Hazard Type Risk Index Value` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `Volcanic Activity - Hazard Type Risk Index Score` | float | 1,476/6,936 | 21.3% | 2013–2024 | 12 | 123 | 2025 |
| `fiscal_34T` | float | 1,473/6,936 | 21.2% | 2013–2021 | 9 | 241 | 2022, 2023, 2024, 2025 |
| `fiscal_F31` | float | 1,441/6,936 | 20.8% | 2013–2023 | 11 | 277 | 2024, 2025 |
| `fiscal_E03` | float | 1,412/6,936 | 20.4% | 2013–2023 | 11 | 181 | 2024, 2025 |
| `fiscal_C50` | float | 1,405/6,936 | 20.3% | 2013–2021 | 9 | 281 | 2022, 2023, 2024, 2025 |
| `fiscal_T20` | float | 1,335/6,936 | 19.2% | 2013–2023 | 11 | 156 | 2024, 2025 |
| `fiscal_G50` | float | 1,268/6,936 | 18.3% | 2013–2021 | 9 | 308 | 2022, 2023, 2024, 2025 |
| `fiscal_G81` | float | 1,270/6,936 | 18.3% | 2013–2021 | 9 | 268 | 2022, 2023, 2024, 2025 |
| `fiscal_F01` | float | 1,240/6,936 | 17.9% | 2013–2023 | 11 | 161 | 2024, 2025 |
| `fiscal_G23` | float | 1,226/6,936 | 17.7% | 2013–2021 | 9 | 283 | 2022, 2023, 2024, 2025 |
| `fiscal_F81` | float | 1,178/6,936 | 17.0% | 2013–2023 | 11 | 256 | 2024, 2025 |
| `fiscal_F29` | float | 1,165/6,936 | 16.8% | 2013–2023 | 11 | 309 | 2024, 2025 |
| `fiscal_D30` | float | 1,150/6,936 | 16.6% | 2013–2021 | 9 | 190 | 2022, 2023, 2024, 2025 |
| `fiscal_T51` | float | 1,146/6,936 | 16.5% | 2013–2023 | 11 | 161 | 2024, 2025 |
| `fiscal_M89` | float | 1,123/6,936 | 16.2% | 2013–2023 | 11 | 317 | 2024, 2025 |
| `relevant_counties` | str | 1,068/6,936 | 15.4% | 2013–2024 | 12 | 88 | 2025 |
| `recommended_approach` | str | 1,068/6,936 | 15.4% | 2013–2024 | 12 | 88 | 2025 |
| `fiscal_B46` | float | 1,029/6,936 | 14.8% | 2013–2021 | 9 | 270 | 2022, 2023, 2024, 2025 |
| `fiscal_G31` | float | 1,009/6,936 | 14.5% | 2013–2021 | 9 | 231 | 2022, 2023, 2024, 2025 |
| `Tsunami - Number of Events` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Annualized Frequency` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Exposure - Impacted Area (sq mi)` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Exposure - Building Value` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Exposure - Population` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Exposure - Population Equivalence` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Exposure - Total` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Historic Loss Ratio - Buildings` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Historic Loss Ratio - Population` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss - Building Value` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss - Population` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss - Population Equivalence` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss - Total` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss Score` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss Rate - Building` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss Rate - Population` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Expected Annual Loss Rate - National Percentile` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Hazard Type Risk Index Value` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `Tsunami - Hazard Type Risk Index Score` | float | 972/6,936 | 14.0% | 2013–2024 | 12 | 81 | 2025 |
| `fiscal_B01` | float | 968/6,936 | 14.0% | 2013–2021 | 9 | 146 | 2022, 2023, 2024, 2025 |
| `fiscal_C42` | float | 966/6,936 | 13.9% | 2013–2021 | 9 | 165 | 2022, 2023, 2024, 2025 |
| `fiscal_D46` | float | 966/6,936 | 13.9% | 2013–2021 | 9 | 198 | 2022, 2023, 2024, 2025 |
| `fiscal_G52` | float | 955/6,936 | 13.8% | 2013–2021 | 9 | 199 | 2022, 2023, 2024, 2025 |
| `fiscal_E92` | float | 952/6,936 | 13.7% | 2013–2023 | 11 | 102 | 2024, 2025 |
| `fiscal_T99` | float | 923/6,936 | 13.3% | 2013–2023 | 11 | 179 | 2024, 2025 |
| `fiscal_A92` | float | 919/6,936 | 13.2% | 2013–2023 | 11 | 99 | 2024, 2025 |
| `fiscal_B94` | float | 896/6,936 | 12.9% | 2013–2021 | 9 | 160 | 2022, 2023, 2024, 2025 |
| `fiscal_G25` | float | 873/6,936 | 12.6% | 2013–2021 | 9 | 202 | 2022, 2023, 2024, 2025 |
| `fiscal_61V` | float | 865/6,936 | 12.5% | 2013–2023 | 11 | 169 | 2024, 2025 |
| `fiscal_X11` | float | 867/6,936 | 12.5% | 2013–2016 | 4 | 260 | 9 yrs missing |
| `fiscal_F52` | float | 858/6,936 | 12.4% | 2013–2023 | 11 | 218 | 2024, 2025 |
| `fiscal_X08` | float | 857/6,936 | 12.4% | 2013–2016 | 4 | 258 | 9 yrs missing |
| `fiscal_T24` | float | 856/6,936 | 12.3% | 2013–2023 | 11 | 113 | 2024, 2025 |
| `fiscal_64V` | float | 843/6,936 | 12.2% | 2013–2023 | 11 | 157 | 2024, 2025 |
| `fiscal_T11` | float | 847/6,936 | 12.2% | 2013–2023 | 11 | 90 | 2024, 2025 |
| `fiscal_C94` | float | 840/6,936 | 12.1% | 2013–2021 | 9 | 153 | 2022, 2023, 2024, 2025 |
| `fiscal_X21` | float | 830/6,936 | 12.0% | 2013–2016 | 4 | 256 | 9 yrs missing |
| `fiscal_G66` | float | 791/6,936 | 11.4% | 2013–2021 | 9 | 199 | 2022, 2023, 2024, 2025 |
| `fiscal_E12` | float | 777/6,936 | 11.2% | 2013–2023 | 11 | 85 | 2024, 2025 |
| `fiscal_X44` | float | 779/6,936 | 11.2% | 2013–2016 | 4 | 242 | 9 yrs missing |
| `fiscal_C79` | float | 755/6,936 | 10.9% | 2013–2021 | 9 | 143 | 2022, 2023, 2024, 2025 |
| `fiscal_Z77` | float | 746/6,936 | 10.8% | 2013–2016 | 4 | 239 | 9 yrs missing |
| `fiscal_A59` | float | 728/6,936 | 10.5% | 2013–2023 | 11 | 115 | 2024, 2025 |
| `fiscal_G32` | float | 728/6,936 | 10.5% | 2013–2021 | 9 | 181 | 2022, 2023, 2024, 2025 |
| `fiscal_X01` | float | 713/6,936 | 10.3% | 2013–2016 | 4 | 212 | 9 yrs missing |
| `fiscal_Z78` | float | 710/6,936 | 10.2% | 2013–2016 | 4 | 215 | 9 yrs missing |
| `fiscal_E04` | float | 701/6,936 | 10.1% | 2013–2023 | 11 | 79 | 2024, 2025 |
| `fiscal_F60` | float | 693/6,936 | 10.0% | 2013–2023 | 11 | 155 | 2024, 2025 |
| `fiscal_F94` | float | 697/6,936 | 10.0% | 2013–2023 | 11 | 155 | 2024, 2025 |
| `fiscal_C80` | float | 679/6,936 | 9.8% | 2013–2021 | 9 | 180 | 2022, 2023, 2024, 2025 |
| `fiscal_G94` | float | 674/6,936 | 9.7% | 2013–2021 | 9 | 143 | 2022, 2023, 2024, 2025 |
| `fiscal_X12` | float | 659/6,936 | 9.5% | 2013–2016 | 4 | 224 | 9 yrs missing |
| `fiscal_A09` | float | 653/6,936 | 9.4% | 2013–2023 | 11 | 63 | 2024, 2025 |
| `fiscal_I92` | float | 647/6,936 | 9.3% | 2013–2023 | 11 | 77 | 2024, 2025 |
| `fiscal_C21` | float | 636/6,936 | 9.2% | 2013–2021 | 9 | 85 | 2022, 2023, 2024, 2025 |
| `fiscal_A12` | float | 629/6,936 | 9.1% | 2013–2023 | 11 | 67 | 2024, 2025 |
| `fiscal_F92` | float | 628/6,936 | 9.1% | 2013–2023 | 11 | 83 | 2024, 2025 |
| `fiscal_F59` | float | 610/6,936 | 8.8% | 2013–2023 | 11 | 159 | 2024, 2025 |
| `fiscal_C91` | float | 599/6,936 | 8.6% | 2013–2021 | 9 | 180 | 2022, 2023, 2024, 2025 |
| `fiscal_M12` | float | 595/6,936 | 8.6% | 2013–2021 | 9 | 91 | 2022, 2023, 2024, 2025 |
| `fiscal_X30` | float | 589/6,936 | 8.5% | 2013–2016 | 4 | 203 | 9 yrs missing |
| `fiscal_F12` | float | 566/6,936 | 8.2% | 2013–2023 | 11 | 70 | 2024, 2025 |
| `fiscal_F32` | float | 567/6,936 | 8.2% | 2013–2023 | 11 | 170 | 2024, 2025 |
| `fiscal_G01` | float | 571/6,936 | 8.2% | 2013–2021 | 9 | 121 | 2022, 2023, 2024, 2025 |
| `fiscal_G12` | float | 566/6,936 | 8.2% | 2013–2021 | 9 | 72 | 2022, 2023, 2024, 2025 |
| `srf_incl_count` | float | 557/6,936 | 8.0% | 2013–2024 | 12 | 207 | 2025 |
| `srf_incl_amount` | float | 557/6,936 | 8.0% | 2013–2024 | 12 | 207 | 2025 |
| `srf_incl_amount_real` | float | 557/6,936 | 8.0% | 2013–2024 | 12 | 207 | 2025 |
| `fiscal_T40` | float | 551/6,936 | 7.9% | 2013–2023 | 11 | 56 | 2024, 2025 |
| `fiscal_G60` | float | 542/6,936 | 7.8% | 2013–2021 | 9 | 142 | 2022, 2023, 2024, 2025 |
| `fiscal_X47` | float | 532/6,936 | 7.7% | 2013–2016 | 4 | 193 | 9 yrs missing |
| `fiscal_G59` | float | 530/6,936 | 7.6% | 2013–2021 | 9 | 133 | 2022, 2023, 2024, 2025 |
| `fiscal_F23` | float | 509/6,936 | 7.3% | 2013–2023 | 11 | 179 | 2024, 2025 |
| `fiscal_L89` | float | 508/6,936 | 7.3% | 2013–2023 | 11 | 130 | 2024, 2025 |
| `fiscal_D50` | float | 485/6,936 | 7.0% | 2013–2021 | 9 | 135 | 2022, 2023, 2024, 2025 |
| `fiscal_T10` | float | 485/6,936 | 7.0% | 2013–2023 | 11 | 55 | 2024, 2025 |
| `fiscal_T21` | float | 483/6,936 | 7.0% | 2013–2023 | 11 | 69 | 2024, 2025 |
| `fiscal_X05` | float | 483/6,936 | 7.0% | 2013–2016 | 4 | 192 | 9 yrs missing |
| `fiscal_B79` | float | 468/6,936 | 6.7% | 2013–2021 | 9 | 114 | 2022, 2023, 2024, 2025 |
| `fiscal_B42` | float | 455/6,936 | 6.6% | 2013–2021 | 9 | 139 | 2022, 2023, 2024, 2025 |
| `fiscal_A10` | float | 438/6,936 | 6.3% | 2013–2023 | 11 | 54 | 2024, 2025 |
| `fiscal_D21` | float | 431/6,936 | 6.2% | 2013–2021 | 9 | 63 | 2022, 2023, 2024, 2025 |
| `fiscal_T13` | float | 413/6,936 | 6.0% | 2013–2023 | 11 | 50 | 2024, 2025 |
| `fiscal_M32` | float | 403/6,936 | 5.8% | 2013–2021 | 9 | 87 | 2022, 2023, 2024, 2025 |
| `fiscal_B21` | float | 398/6,936 | 5.7% | 2013–2021 | 9 | 64 | 2022, 2023, 2024, 2025 |
| `fiscal_B30` | float | 397/6,936 | 5.7% | 2013–2021 | 9 | 113 | 2022, 2023, 2024, 2025 |
| `fiscal_U41` | float | 381/6,936 | 5.5% | 2013–2023 | 11 | 64 | 2024, 2025 |
| `srf_strict_count` | float | 371/6,936 | 5.3% | 2013–2024 | 12 | 163 | 2025 |
| `srf_strict_amount` | float | 371/6,936 | 5.3% | 2013–2024 | 12 | 163 | 2025 |
| `srf_strict_amount_real` | float | 371/6,936 | 5.3% | 2013–2024 | 12 | 163 | 2025 |
| `fiscal_F25` | float | 370/6,936 | 5.3% | 2013–2023 | 11 | 133 | 2024, 2025 |
| `fiscal_F66` | float | 362/6,936 | 5.2% | 2013–2023 | 11 | 162 | 2024, 2025 |
| `fiscal_T27` | float | 343/6,936 | 4.9% | 2013–2023 | 11 | 54 | 2024, 2025 |
| `fiscal_M80` | float | 330/6,936 | 4.8% | 2013–2021 | 9 | 75 | 2022, 2023, 2024, 2025 |
| `fiscal_E87` | float | 328/6,936 | 4.7% | 2013–2023 | 11 | 51 | 2024, 2025 |
| `fiscal_B91` | float | 319/6,936 | 4.6% | 2013–2021 | 9 | 105 | 2022, 2023, 2024, 2025 |
| `fiscal_T16` | float | 316/6,936 | 4.6% | 2013–2023 | 11 | 35 | 2024, 2025 |
| `fiscal_A87` | float | 311/6,936 | 4.5% | 2013–2023 | 11 | 46 | 2024, 2025 |
| `fiscal_G03` | float | 311/6,936 | 4.5% | 2013–2021 | 9 | 84 | 2022, 2023, 2024, 2025 |
| `fiscal_A93` | float | 306/6,936 | 4.4% | 2013–2023 | 11 | 37 | 2024, 2025 |
| `fiscal_D94` | float | 299/6,936 | 4.3% | 2013–2021 | 9 | 80 | 2022, 2023, 2024, 2025 |
| `fiscal_E93` | float | 300/6,936 | 4.3% | 2013–2023 | 11 | 37 | 2024, 2025 |
| `fiscal_M62` | float | 301/6,936 | 4.3% | 2013–2021 | 9 | 88 | 2022, 2023, 2024, 2025 |
| `fiscal_E05` | float | 285/6,936 | 4.1% | 2013–2023 | 11 | 45 | 2024, 2025 |
| `fiscal_G92` | float | 285/6,936 | 4.1% | 2013–2021 | 9 | 62 | 2022, 2023, 2024, 2025 |
| `fiscal_M04` | float | 281/6,936 | 4.1% | 2013–2021 | 9 | 47 | 2022, 2023, 2024, 2025 |
| `fiscal_T12` | float | 285/6,936 | 4.1% | 2013–2023 | 11 | 35 | 2024, 2025 |
| `fiscal_D80` | float | 268/6,936 | 3.9% | 2013–2021 | 9 | 70 | 2022, 2023, 2024, 2025 |
| `fiscal_M94` | float | 273/6,936 | 3.9% | 2013–2021 | 9 | 60 | 2022, 2023, 2024, 2025 |
| `fiscal_B80` | float | 256/6,936 | 3.7% | 2013–2021 | 9 | 95 | 2022, 2023, 2024, 2025 |
| `fiscal_M50` | float | 250/6,936 | 3.6% | 2013–2021 | 9 | 82 | 2022, 2023, 2024, 2025 |
| `fiscal_24T` | float | 239/6,936 | 3.4% | 2013–2021 | 9 | 89 | 2022, 2023, 2024, 2025 |
| `fiscal_D42` | float | 234/6,936 | 3.4% | 2013–2021 | 9 | 59 | 2022, 2023, 2024, 2025 |
| `fiscal_M23` | float | 238/6,936 | 3.4% | 2013–2021 | 9 | 50 | 2022, 2023, 2024, 2025 |
| `fiscal_F93` | float | 205/6,936 | 3.0% | 2013–2023 | 11 | 27 | 2024, 2025 |
| `fiscal_M91` | float | 211/6,936 | 3.0% | 2013–2021 | 9 | 70 | 2022, 2023, 2024, 2025 |
| `fiscal_M29` | float | 198/6,936 | 2.9% | 2013–2021 | 9 | 40 | 2022, 2023, 2024, 2025 |
| `fiscal_D79` | float | 195/6,936 | 2.8% | 2013–2021 | 9 | 49 | 2022, 2023, 2024, 2025 |
| `fiscal_F03` | float | 195/6,936 | 2.8% | 2013–2023 | 11 | 77 | 2024, 2025 |
| `fiscal_L94` | float | 195/6,936 | 2.8% | 2013–2021 | 9 | 27 | 2022, 2023, 2024, 2025 |
| `fiscal_M44` | float | 195/6,936 | 2.8% | 2013–2021 | 9 | 64 | 2022, 2023, 2024, 2025 |
| `fiscal_D91` | float | 187/6,936 | 2.7% | 2013–2021 | 9 | 68 | 2022, 2023, 2024, 2025 |
| `fiscal_G79` | float | 181/6,936 | 2.6% | 2013–2021 | 9 | 64 | 2022, 2023, 2024, 2025 |
| `fiscal_I93` | float | 174/6,936 | 2.5% | 2013–2023 | 11 | 19 | 2024, 2025 |
| `fiscal_L44` | float | 170/6,936 | 2.5% | 2013–2021 | 9 | 42 | 2022, 2023, 2024, 2025 |
| `fiscal_B59` | float | 158/6,936 | 2.3% | 2013–2021 | 9 | 50 | 2022, 2023, 2024, 2025 |
| `fiscal_I94` | float | 160/6,936 | 2.3% | 2013–2023 | 11 | 42 | 2024, 2025 |
| `fiscal_M61` | float | 150/6,936 | 2.2% | 2013–2021 | 9 | 46 | 2022, 2023, 2024, 2025 |
| `fiscal_F79` | float | 145/6,936 | 2.1% | 2013–2023 | 11 | 52 | 2024, 2025 |
| `fiscal_T41` | float | 144/6,936 | 2.1% | 2013–2023 | 11 | 16 | 2024, 2025 |
| `fiscal_A36` | float | 139/6,936 | 2.0% | 2013–2023 | 11 | 21 | 2024, 2025 |
| `fiscal_E36` | float | 136/6,936 | 2.0% | 2013–2023 | 11 | 21 | 2024, 2025 |
| `fiscal_G04` | float | 137/6,936 | 2.0% | 2013–2021 | 9 | 40 | 2022, 2023, 2024, 2025 |
| `fiscal_M25` | float | 139/6,936 | 2.0% | 2013–2021 | 9 | 42 | 2022, 2023, 2024, 2025 |
| `fiscal_F87` | float | 132/6,936 | 1.9% | 2013–2023 | 11 | 27 | 2024, 2025 |
| `fiscal_L80` | float | 132/6,936 | 1.9% | 2013–2021 | 9 | 29 | 2022, 2023, 2024, 2025 |
| `fiscal_E75` | float | 127/6,936 | 1.8% | 2013–2021 | 9 | 23 | 2022, 2023, 2024, 2025 |
| `fiscal_F04` | float | 126/6,936 | 1.8% | 2013–2023 | 11 | 31 | 2024, 2025 |
| `fiscal_J68` | float | 119/6,936 | 1.7% | 2013–2021 | 9 | 24 | 2022, 2023, 2024, 2025 |
| `fiscal_M24` | float | 119/6,936 | 1.7% | 2013–2021 | 9 | 45 | 2022, 2023, 2024, 2025 |
| `fiscal_M81` | float | 109/6,936 | 1.6% | 2013–2021 | 9 | 34 | 2022, 2023, 2024, 2025 |
| `fiscal_A90` | float | 101/6,936 | 1.5% | 2013–2023 | 11 | 10 | 2024, 2025 |
| `fiscal_E90` | float | 102/6,936 | 1.5% | 2013–2023 | 11 | 10 | 2024, 2025 |
| `fiscal_L91` | float | 101/6,936 | 1.5% | 2013–2021 | 9 | 27 | 2022, 2023, 2024, 2025 |
| `fiscal_C92` | float | 97/6,936 | 1.4% | 2013–2021 | 9 | 31 | 2022, 2023, 2024, 2025 |
| `fiscal_F36` | float | 98/6,936 | 1.4% | 2013–2023 | 11 | 12 | 2024, 2025 |
| `fiscal_M01` | float | 97/6,936 | 1.4% | 2013–2021 | 9 | 26 | 2022, 2023, 2024, 2025 |
| `fiscal_E45` | float | 87/6,936 | 1.3% | 2013–2023 | 11 | 12 | 2024, 2025 |
| `fiscal_M52` | float | 88/6,936 | 1.3% | 2013–2021 | 9 | 24 | 2022, 2023, 2024, 2025 |
| `fiscal_B92` | float | 81/6,936 | 1.2% | 2013–2021 | 9 | 28 | 2022, 2023, 2024, 2025 |
| `fiscal_G93` | float | 85/6,936 | 1.2% | 2013–2021 | 9 | 19 | 2022, 2023, 2024, 2025 |
| `fiscal_T14` | float | 86/6,936 | 1.2% | 2013–2023 | 11 | 13 | 2024, 2025 |
| `fiscal_A45` | float | 77/6,936 | 1.1% | 2013–2023 | 11 | 8 | 2024, 2025 |
| `fiscal_M79` | float | 74/6,936 | 1.1% | 2013–2021 | 9 | 18 | 2022, 2023, 2024, 2025 |
| `fiscal_E77` | float | 68/6,936 | 1.0% | 2013–2023 | 11 | 24 | 2024, 2025 |
| `fiscal_G36` | float | 69/6,936 | 1.0% | 2013–2021 | 9 | 10 | 2022, 2023, 2024, 2025 |
| `fiscal_M59` | float | 67/6,936 | 1.0% | 2013–2021 | 9 | 31 | 2022, 2023, 2024, 2025 |
| `fiscal_J67` | float | 61/6,936 | 0.9% | 2013–2021 | 9 | 11 | 2022, 2023, 2024, 2025 |
| `fiscal_T50` | float | 61/6,936 | 0.9% | 2013–2023 | 11 | 16 | 2024, 2025 |
| `fiscal_A18` | float | 48/6,936 | 0.7% | 2013–2023 | 11 | 5 | 2024, 2025 |
| `fiscal_E18` | float | 48/6,936 | 0.7% | 2013–2023 | 11 | 5 | 2024, 2025 |
| `fiscal_F45` | float | 49/6,936 | 0.7% | 2013–2023 | 11 | 11 | 2024, 2025 |
| `fiscal_L62` | float | 50/6,936 | 0.7% | 2013–2021 | 9 | 19 | 2022, 2023, 2024, 2025 |
| `fiscal_D92` | float | 44/6,936 | 0.6% | 2013–2021 | 9 | 16 | 2022, 2023, 2024, 2025 |
| `fiscal_E74` | float | 43/6,936 | 0.6% | 2013–2021 | 9 | 12 | 2022, 2023, 2024, 2025 |
| `fiscal_G45` | float | 43/6,936 | 0.6% | 2013–2021 | 9 | 9 | 2022, 2023, 2024, 2025 |
| `fiscal_L12` | float | 42/6,936 | 0.6% | 2013–2021 | 9 | 13 | 2022, 2023, 2024, 2025 |
| `fiscal_L25` | float | 45/6,936 | 0.6% | 2013–2021 | 9 | 15 | 2022, 2023, 2024, 2025 |
| `fiscal_T25` | float | 40/6,936 | 0.6% | 2013–2023 | 11 | 5 | 2024, 2025 |
| `fiscal_T53` | float | 41/6,936 | 0.6% | 2013–2023 | 11 | 11 | 2024, 2025 |
| `fiscal_G05` | float | 37/6,936 | 0.5% | 2013–2021 | 9 | 15 | 2022, 2023, 2024, 2025 |
| `fiscal_L29` | float | 35/6,936 | 0.5% | 2013–2021 | 9 | 9 | 2022, 2023, 2024, 2025 |
| `fiscal_E16` | float | 25/6,936 | 0.4% | 2013–2023 | 11 | 3 | 2024, 2025 |
| `fiscal_G87` | float | 29/6,936 | 0.4% | 2013–2021 | 9 | 10 | 2022, 2023, 2024, 2025 |
| `fiscal_L01` | float | 30/6,936 | 0.4% | 2013–2021 | 9 | 8 | 2022, 2023, 2024, 2025 |
| `fiscal_L23` | float | 29/6,936 | 0.4% | 2013–2021 | 9 | 9 | 2022, 2023, 2024, 2025 |
| `fiscal_L32` | float | 30/6,936 | 0.4% | 2013–2021 | 8 | 9 | 2014, 2022, 2023, 2024, 2025 |
| `fiscal_L50` | float | 30/6,936 | 0.4% | 2013–2021 | 9 | 17 | 2022, 2023, 2024, 2025 |
| `fiscal_L61` | float | 28/6,936 | 0.4% | 2013–2021 | 9 | 11 | 2022, 2023, 2024, 2025 |
| `fiscal_M05` | float | 28/6,936 | 0.4% | 2013–2021 | 9 | 9 | 2022, 2023, 2024, 2025 |
| `fiscal_M92` | float | 26/6,936 | 0.4% | 2013–2021 | 9 | 10 | 2022, 2023, 2024, 2025 |
| `fiscal_X42` | float | 30/6,936 | 0.4% | 2013–2016 | 4 | 14 | 9 yrs missing |
| `fiscal_A16` | float | 23/6,936 | 0.3% | 2013–2023 | 11 | 3 | 2024, 2025 |
| `fiscal_C93` | float | 19/6,936 | 0.3% | 2013–2021 | 9 | 4 | 2022, 2023, 2024, 2025 |
| `fiscal_F18` | float | 18/6,936 | 0.3% | 2013–2023 | 11 | 2 | 2024, 2025 |
| `fiscal_M60` | float | 22/6,936 | 0.3% | 2013–2021 | 9 | 10 | 2022, 2023, 2024, 2025 |
| `fiscal_M66` | float | 21/6,936 | 0.3% | 2013–2021 | 9 | 6 | 2022, 2023, 2024, 2025 |
| `fiscal_T22` | float | 22/6,936 | 0.3% | 2013–2023 | 11 | 3 | 2024, 2025 |
| `fiscal_B93` | float | 14/6,936 | 0.2% | 2013–2021 | 9 | 5 | 2022, 2023, 2024, 2025 |
| `fiscal_E22` | float | 11/6,936 | 0.2% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `fiscal_F05` | float | 12/6,936 | 0.2% | 2013–2023 | 8 | 6 | 2016, 2020, 2021, 2024, 2025 |
| `fiscal_F77` | float | 15/6,936 | 0.2% | 2019–2023 | 5 | 10 | 8 yrs missing |
| `fiscal_G18` | float | 14/6,936 | 0.2% | 2013–2021 | 9 | 2 | 2022, 2023, 2024, 2025 |
| `fiscal_G90` | float | 14/6,936 | 0.2% | 2013–2021 | 9 | 3 | 2022, 2023, 2024, 2025 |
| `fiscal_J19` | float | 11/6,936 | 0.2% | 2022–2023 | 2 | 7 | 11 yrs missing |
| `fiscal_L52` | float | 13/6,936 | 0.2% | 2013–2021 | 8 | 4 | 2020, 2022, 2023, 2024, 2025 |
| `fiscal_L59` | float | 17/6,936 | 0.2% | 2013–2020 | 8 | 6 | 2021, 2022, 2023, 2024, 2025 |
| `fiscal_L67` | float | 13/6,936 | 0.2% | 2013–2021 | 9 | 2 | 2022, 2023, 2024, 2025 |
| `fiscal_L79` | float | 13/6,936 | 0.2% | 2013–2021 | 9 | 6 | 2022, 2023, 2024, 2025 |
| `fiscal_L81` | float | 12/6,936 | 0.2% | 2014–2021 | 8 | 3 | 2013, 2022, 2023, 2024, 2025 |
| `fiscal_L93` | float | 16/6,936 | 0.2% | 2013–2021 | 9 | 3 | 2022, 2023, 2024, 2025 |
| `fiscal_M18` | float | 11/6,936 | 0.2% | 2013–2018 | 6 | 7 | 7 yrs missing |
| `fiscal_M36` | float | 14/6,936 | 0.2% | 2013–2021 | 9 | 2 | 2022, 2023, 2024, 2025 |
| `fiscal_M87` | float | 11/6,936 | 0.2% | 2013–2021 | 8 | 3 | 2020, 2022, 2023, 2024, 2025 |
| `fiscal_U95` | float | 11/6,936 | 0.2% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `fiscal_Y01` | float | 11/6,936 | 0.2% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `fiscal_Y02` | float | 11/6,936 | 0.2% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `fiscal_Y05` | float | 11/6,936 | 0.2% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `fiscal_Y07` | float | 11/6,936 | 0.2% | 2013–2023 | 11 | 1 | 2024, 2025 |
| `fiscal_G22` | float | 9/6,936 | 0.1% | 2013–2021 | 9 | 1 | 2022, 2023, 2024, 2025 |
| `fiscal_L05` | float | 7/6,936 | 0.1% | 2013–2020 | 5 | 3 | 8 yrs missing |
| `fiscal_L18` | float | 9/6,936 | 0.1% | 2013–2019 | 7 | 3 | 6 yrs missing |
| `fiscal_L36` | float | 10/6,936 | 0.1% | 2013–2021 | 9 | 2 | 2022, 2023, 2024, 2025 |
| `fiscal_L66` | float | 4/6,936 | 0.1% | 2016–2018 | 3 | 3 | 10 yrs missing |
| `fiscal_L87` | float | 7/6,936 | 0.1% | 2017–2020 | 4 | 3 | 9 yrs missing |
| `fiscal_M93` | float | 10/6,936 | 0.1% | 2013–2020 | 8 | 3 | 2021, 2022, 2023, 2024, 2025 |
| `state_stringency_state_insp_rate_npdes` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Coastal Flooding - Number of Events` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Earthquake - Number of Events` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Landslide - Number of Events` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Wildfire - Number of Events` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `epa_state_insp_rate_npdes` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `avg_facility_emissions_lag1` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `avg_facility_emissions_lag2` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `avg_facility_emissions_lag3` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `avg_facility_emissions_lag4` | float | 0/6,936 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `fiscal_B22` | float | 3/6,936 | 0.0% | 2013–2015 | 3 | 1 | 10 yrs missing |
| `fiscal_D93` | float | 2/6,936 | 0.0% | 2013–2014 | 2 | 1 | 11 yrs missing |
| `fiscal_F22` | float | 2/6,936 | 0.0% | 2022–2023 | 2 | 1 | 11 yrs missing |
| `fiscal_F90` | float | 3/6,936 | 0.0% | 2022–2023 | 2 | 2 | 11 yrs missing |
| `fiscal_G77` | float | 2/6,936 | 0.0% | 2014–2020 | 2 | 2 | 11 yrs missing |
| `fiscal_L04` | float | 2/6,936 | 0.0% | 2015–2016 | 2 | 1 | 11 yrs missing |
| `fiscal_Y06` | float | 3/6,936 | 0.0% | 2013–2015 | 3 | 1 | 10 yrs missing |
| `fiscal_Y08` | float | 3/6,936 | 0.0% | 2019–2023 | 3 | 1 | 10 yrs missing |

### ACS Additional
**File:** `raw/census_acs/additional_city_variables_2010_2024.csv`  
**Shape:** 8,654 rows × 61 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `Year` — range 2010-2024 (15 years)  
**Panel-window coverage (2013–2025):** 12/13 years  
**Missing panel years:** 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `GEO_ID_city` | str | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `geo_name` | str | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_abb` | str | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `county_geo_id` | str | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `land_area_sqkm` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `land_area_sqmi` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `pop_density_sqkm` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `pop_density_sqmi` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `is_principal_city` | int | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_gov_party` | str | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_dem_trifecta` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_rep_trifecta` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_divided_govt` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_dem_governor` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_dem_legislature` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_poverty_rate` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_median_hh_income` | int | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_gini_index` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_pct_bachelors_plus` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_pct_foreign_born` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_homeownership_rate` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_median_age` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_pct_white` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_pct_black` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_pct_hispanic` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_medicaid_expanded` | int | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_right_to_work` | int | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_has_income_tax` | int | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `election_year` | int | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `pres_dem_vote_share` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `pres_rep_vote_share` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `pres_dem_two_party_share` | float | 8,654/8,654 | 100.0% | 2010–2024 | 15 | 2025 |
| `state_legis_control` | str | 8,596/8,654 | 99.3% | 2010–2024 | 15 | 2025 |
| `state_govt_trifecta` | str | 8,596/8,654 | 99.3% | 2010–2024 | 15 | 2025 |
| `state_medicaid_expansion_year` | float | 6,539/8,654 | 75.6% | 2010–2024 | 15 | 2025 |
| `opinion_happening` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_human` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_consensus` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_worried` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_personal` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_harmus` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_devharm` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_futuregen` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_fundrenewables` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_regulate` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_timing` | float | 6,346/8,654 | 73.3% | 2014–2024 | 11 | 2013, 2025 |
| `opinion_harmplants` | float | 5,192/8,654 | 60.0% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `opinion_teachgw` | float | 5,192/8,654 | 60.0% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `opinion_discuss` | float | 5,192/8,654 | 60.0% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `opinion_reducetax` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_congress` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_governor` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_localofficials` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_citizens` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_corporations` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_affectweather` | float | 4,038/8,654 | 46.7% | 2018–2024 | 7 | 6 yrs missing |
| `opinion_priority` | float | 2,884/8,654 | 33.3% | 2020–2024 | 5 | 8 yrs missing |
| `opinion_exp` | float | 2,307/8,654 | 26.7% | 2021–2024 | 4 | 9 yrs missing |
| `opinion_generaterenewable` | float | 1,730/8,654 | 20.0% | 2022–2024 | 3 | 10 yrs missing |

### BLS ACS Economic
**File:** `raw/census_acs/economic_bls_acs.csv`  
**Shape:** 8,036 rows × 16 columns  
**City column:** `city_name` (544 unique cities)  
**Year column:** `year` — range 2010-2023 (14 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `management_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `manufacturing_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `lfpr_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `naturalresources_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `production_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `unemployment_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `transport_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `population_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `percapita_income_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `totalincome_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `log_population_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `log_percapita_income_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |
| `log_totalincome_city` | float | 8,036/8,036 | 100.0% | 2010–2023 | 14 | 544 | 2024, 2025 |

### ACS Demographics 2022
**File:** `raw/census_acs/acs_demographics_2022.csv`  
**Shape:** 574 rows × 4 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `fips7` | int | 574/574 | 100.0% |
| `pct_college_educated` | float | 574/574 | 100.0% |
| `pct_nonwhite` | float | 574/574 | 100.0% |
| `median_home_value` | int | 574/574 | 100.0% |

### EPA Enforcement
**File:** `raw/epa/city_year_epa_enforcement_expanded_20260407_125920.csv`  
**Shape:** 15,552 rows × 200 columns  
**City column:** `CITY_NAME` (546 unique cities)  
**Year column:** `YEAR` — range 2000-2026 (27 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `CITY_ID` | str | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `CITY_STATE` | str | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_formal_actions_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_formal_actions_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_informal_actions_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_informal_actions_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_inspections_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_inspections_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_stack_tests_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_stack_tests_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_titlev_certs_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_titlev_certs_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_violations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_violations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_any_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_cum_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_prior3yr_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_any_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_cum_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_prior3yr_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_conclusions_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_any_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_cum_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_prior3yr_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_milestones_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_cs_violations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_cs_violations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_effluent_violations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_effluent_violations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_actions_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_actions_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_any_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_cum_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_prior3yr_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_informal_actions_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_informal_actions_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_inspections_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_inspections_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_ps_violations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_ps_violations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_se_violations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_se_violations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `overflow_events_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `overflow_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_enforcements_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_enforcements_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_evaluations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_evaluations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_flag_months_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_flag_months_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_vio_months_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_vio_months_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_violations_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_violations_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_events_milestones_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_events_milestones_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_lcr_samples_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_lcr_samples_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_site_visits_count_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_site_visits_facilities_muni` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_formal_actions_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_formal_actions_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_informal_actions_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_informal_actions_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_inspections_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_inspections_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_stack_tests_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_stack_tests_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_titlev_certs_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_titlev_certs_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_violations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_violations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_any_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_cum_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_prior3yr_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_any_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_cum_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_prior3yr_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_conclusions_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_any_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_cum_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_prior3yr_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_milestones_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_cs_violations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_cs_violations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_effluent_violations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_effluent_violations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_actions_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_actions_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_any_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_cum_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_prior3yr_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_informal_actions_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_informal_actions_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_inspections_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_inspections_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_ps_violations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_ps_violations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_se_violations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_se_violations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `overflow_events_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `overflow_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_enforcements_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_enforcements_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_evaluations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_evaluations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_flag_months_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_flag_months_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_vio_months_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_vio_months_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_violations_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_violations_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_events_milestones_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_events_milestones_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_lcr_samples_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_lcr_samples_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_site_visits_count_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_site_visits_facilities_locgov` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_formal_actions_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_formal_actions_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_informal_actions_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_informal_actions_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_inspections_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_inspections_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_stack_tests_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_stack_tests_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_titlev_certs_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_titlev_certs_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_violations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `air_violations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_any_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_cum_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_afr_prior3yr_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_any_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_cum_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_all_prior3yr_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_conclusions_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_any_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_cum_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_jdc_prior3yr_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_milestones_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_cs_violations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_cs_violations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_effluent_violations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_effluent_violations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_actions_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_actions_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_any_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_cum_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_formal_prior3yr_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_informal_actions_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_informal_actions_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_inspections_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_inspections_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_ps_violations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_ps_violations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_se_violations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `npdes_se_violations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `overflow_events_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `overflow_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_enforcements_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_enforcements_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_evaluations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_evaluations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_flag_months_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_flag_months_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_vio_months_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_snc_vio_months_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_violations_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `rcra_violations_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_events_milestones_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_events_milestones_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_lcr_samples_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_lcr_samples_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_site_visits_count_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `sdwa_site_visits_facilities_private` | int | 15,552/15,552 | 100.0% | 2000–2026 | 27 | 546 | None |
| `case_milestones_unique_private` | float | 6,688/15,552 | 43.0% | 2000–2025 | 26 | 529 | None |
| `case_penalty_total_private` | float | 5,370/15,552 | 34.5% | 2000–2026 | 27 | 528 | None |
| `case_conclusions_unique_private` | float | 1,946/15,552 | 12.5% | 2000–2025 | 26 | 458 | None |
| `case_milestones_unique_locgov` | float | 1,238/15,552 | 8.0% | 2000–2025 | 26 | 301 | None |
| `case_milestones_unique_muni` | float | 995/15,552 | 6.4% | 2000–2025 | 26 | 262 | None |
| `case_penalty_total_locgov` | float | 782/15,552 | 5.0% | 2000–2026 | 27 | 298 | None |
| `case_penalty_total_muni` | float | 646/15,552 | 4.2% | 2000–2026 | 27 | 259 | None |
| `case_conclusions_unique_locgov` | float | 313/15,552 | 2.0% | 2000–2025 | 26 | 164 | None |
| `case_conclusions_unique_muni` | float | 221/15,552 | 1.4% | 2000–2023 | 24 | 131 | 2024, 2025 |

### EPA State Enforcement
**File:** `raw/epa/epa_state_enforcement.csv`  
**Shape:** 5,598 rows × 9 columns  
**City column:** `city_name` (542 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `epa_state_insp_rate_npdes_norm` | float | 5,549/5,598 | 99.1% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `epa_state_stringency_index` | float | 5,549/5,598 | 99.1% | 2013–2023 | 11 | 540 | 2024, 2025 |
| `epa_state_response_rate_npdes` | float | 5,113/5,598 | 91.3% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `epa_state_response_rate_npdes_norm` | float | 5,113/5,598 | 91.3% | 2013–2023 | 11 | 539 | 2024, 2025 |
| `epa_state_response_rate_air` | float | 4,992/5,598 | 89.2% | 2013–2023 | 11 | 538 | 2024, 2025 |
| `epa_state_insp_rate_npdes` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |

### Vulcan CO2
**File:** `raw/vulcan/Vulcan_data.csv`  
**Shape:** 6,924 rows × 216 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2013-2024 (12 years)  
**Panel-window coverage (2013–2025):** 12/13 years  
**Missing panel years:** 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `geo_name` | str | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `state_abb` | str | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `consumption_lag3` | float | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `log_consumption_lag3` | float | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `production_lag3` | float | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `log_production_lag3` | float | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `has_facilities_lag1` | int | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `has_facilities_lag2` | int | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `has_facilities_lag3` | int | 6,924/6,924 | 100.0% | 2013–2024 | 12 | 2025 |
| `TOT_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `log_TOT_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `TOT_mean_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `prod_cons_ratio_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `log_prod_cons_ratio_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `ONR_share_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `COM_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `log_COM_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `COM_share_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `ONR_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `log_ONR_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `RES_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `log_RES_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `RES_share_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `IND_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `log_IND_total_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `IND_share_lag3` | float | 6,900/6,924 | 99.7% | 2013–2024 | 12 | 2025 |
| `consumption_lag2` | float | 6,347/6,924 | 91.7% | 2013–2023 | 11 | 2024, 2025 |
| `log_consumption_lag2` | float | 6,347/6,924 | 91.7% | 2013–2023 | 11 | 2024, 2025 |
| `production_lag2` | float | 6,347/6,924 | 91.7% | 2013–2023 | 11 | 2024, 2025 |
| `log_production_lag2` | float | 6,347/6,924 | 91.7% | 2013–2023 | 11 | 2024, 2025 |
| `consumption_lag4` | float | 6,347/6,924 | 91.7% | 2014–2024 | 11 | 2013, 2025 |
| `log_consumption_lag4` | float | 6,347/6,924 | 91.7% | 2014–2024 | 11 | 2013, 2025 |
| `production_lag4` | float | 6,347/6,924 | 91.7% | 2014–2024 | 11 | 2013, 2025 |
| `log_production_lag4` | float | 6,347/6,924 | 91.7% | 2014–2024 | 11 | 2013, 2025 |
| `has_facilities_lag4` | float | 6,347/6,924 | 91.7% | 2014–2024 | 11 | 2013, 2025 |
| `TOT_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_TOT_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `TOT_mean_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `prod_cons_ratio_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_prod_cons_ratio_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `ONR_share_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `COM_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_COM_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `COM_share_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `ONR_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_ONR_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `RES_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_RES_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `RES_share_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `IND_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_IND_total_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `IND_share_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `delta_log_TOT_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `pct_change_TOT_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `delta_log_production_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `delta_log_consumption_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `delta_prod_cons_ratio_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `TOT_total_ma2_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_TOT_total_ma2_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `log_production_ma2_lag2` | float | 6,325/6,924 | 91.3% | 2013–2023 | 11 | 2024, 2025 |
| `TOT_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_TOT_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `TOT_mean_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `prod_cons_ratio_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_prod_cons_ratio_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `ONR_share_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `COM_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_COM_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `COM_share_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `ONR_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_ONR_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `RES_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_RES_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `RES_share_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `IND_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_IND_total_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `IND_share_lag4` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `delta_log_TOT_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `pct_change_TOT_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `delta_log_production_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `delta_log_consumption_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `delta_prod_cons_ratio_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `TOT_total_ma2_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_TOT_total_ma2_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `log_production_ma2_lag3` | float | 6,325/6,924 | 91.3% | 2014–2024 | 11 | 2013, 2025 |
| `consumption_lag1` | float | 5,770/6,924 | 83.3% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_consumption_lag1` | float | 5,770/6,924 | 83.3% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `production_lag1` | float | 5,770/6,924 | 83.3% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_production_lag1` | float | 5,770/6,924 | 83.3% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `TOT_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_TOT_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `TOT_mean_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `prod_cons_ratio_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_prod_cons_ratio_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `ONR_share_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `COM_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_COM_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `COM_share_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `ONR_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_ONR_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `RES_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_RES_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `RES_share_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `IND_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_IND_total_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `IND_share_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `delta_log_TOT_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `pct_change_TOT_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `delta_log_production_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `delta_log_consumption_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `delta_prod_cons_ratio_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `TOT_total_ma2_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_TOT_total_ma2_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_production_ma2_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `TOT_total_ma3_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_TOT_total_ma3_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_production_ma3_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `prod_cons_ratio_ma3_lag1` | float | 5,750/6,924 | 83.0% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `TOT_total_ma3_lag2` | float | 5,750/6,924 | 83.0% | 2014–2023 | 10 | 2013, 2024, 2025 |
| `log_TOT_total_ma3_lag2` | float | 5,750/6,924 | 83.0% | 2014–2023 | 10 | 2013, 2024, 2025 |
| `log_production_ma3_lag2` | float | 5,750/6,924 | 83.0% | 2014–2023 | 10 | 2013, 2024, 2025 |
| `prod_cons_ratio_ma3_lag2` | float | 5,750/6,924 | 83.0% | 2014–2023 | 10 | 2013, 2024, 2025 |
| `delta_log_TOT_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `pct_change_TOT_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `delta_log_production_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `delta_log_consumption_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `delta_prod_cons_ratio_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `TOT_total_ma3_lag3` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `log_TOT_total_ma3_lag3` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `log_production_ma3_lag3` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `prod_cons_ratio_ma3_lag3` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `TOT_total_ma2_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `log_TOT_total_ma2_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `log_production_ma2_lag4` | float | 5,750/6,924 | 83.0% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `delta_log_TOT_3yr_lag1` | float | 5,175/6,924 | 74.7% | 2014–2022 | 9 | 2013, 2023, 2024, 2025 |
| `delta_log_production_3yr_lag1` | float | 5,175/6,924 | 74.7% | 2014–2022 | 9 | 2013, 2023, 2024, 2025 |
| `delta_log_TOT_3yr_lag2` | float | 5,175/6,924 | 74.7% | 2015–2023 | 9 | 2013, 2014, 2024, 2025 |
| `delta_log_production_3yr_lag2` | float | 5,175/6,924 | 74.7% | 2015–2023 | 9 | 2013, 2014, 2024, 2025 |
| `delta_log_TOT_3yr_lag3` | float | 5,175/6,924 | 74.7% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `delta_log_production_3yr_lag3` | float | 5,175/6,924 | 74.7% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `TOT_total_ma3_lag4` | float | 5,175/6,924 | 74.7% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `log_TOT_total_ma3_lag4` | float | 5,175/6,924 | 74.7% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `log_production_ma3_lag4` | float | 5,175/6,924 | 74.7% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `prod_cons_ratio_ma3_lag4` | float | 5,175/6,924 | 74.7% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `flight_emissions_lag2` | float | 4,701/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `log_flight_emissions_lag2` | float | 4,701/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `facility_count_lag2` | float | 4,701/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `log_facility_count_lag2` | float | 4,701/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `flight_emissions_lag3` | float | 4,703/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `log_flight_emissions_lag3` | float | 4,703/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `facility_count_lag3` | float | 4,703/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `log_facility_count_lag3` | float | 4,703/6,924 | 67.9% | 2013–2024 | 12 | 2025 |
| `flight_pct_of_vulcan_lag3` | float | 4,679/6,924 | 67.6% | 2013–2024 | 12 | 2025 |
| `flight_pct_of_production_lag3` | float | 4,680/6,924 | 67.6% | 2013–2024 | 12 | 2025 |
| `flight_emissions_lag1` | float | 4,676/6,924 | 67.5% | 2013–2024 | 12 | 2025 |
| `log_flight_emissions_lag1` | float | 4,676/6,924 | 67.5% | 2013–2024 | 12 | 2025 |
| `facility_count_lag1` | float | 4,676/6,924 | 67.5% | 2013–2024 | 12 | 2025 |
| `log_facility_count_lag1` | float | 4,676/6,924 | 67.5% | 2013–2024 | 12 | 2025 |
| `delta_log_flight_lag2` | float | 4,664/6,924 | 67.4% | 2013–2024 | 12 | 2025 |
| `pct_change_flight_lag2` | float | 4,664/6,924 | 67.4% | 2013–2024 | 12 | 2025 |
| `delta_facility_count_lag2` | float | 4,666/6,924 | 67.4% | 2013–2024 | 12 | 2025 |
| `log_flight_ma2_lag2` | float | 4,664/6,924 | 67.4% | 2013–2024 | 12 | 2025 |
| `delta_log_flight_lag1` | float | 4,660/6,924 | 67.3% | 2013–2024 | 12 | 2025 |
| `pct_change_flight_lag1` | float | 4,660/6,924 | 67.3% | 2013–2024 | 12 | 2025 |
| `delta_facility_count_lag1` | float | 4,662/6,924 | 67.3% | 2013–2024 | 12 | 2025 |
| `log_flight_ma2_lag1` | float | 4,660/6,924 | 67.3% | 2013–2024 | 12 | 2025 |
| `facility_count_ma3_lag1` | float | 4,629/6,924 | 66.9% | 2013–2024 | 12 | 2025 |
| `log_flight_ma3_lag1` | float | 4,627/6,924 | 66.8% | 2013–2024 | 12 | 2025 |
| `delta_log_TOT_3yr_lag4` | float | 4,600/6,924 | 66.4% | 2017–2024 | 8 | 2013, 2014, 2015, 2016, 2025 |
| `delta_log_production_3yr_lag4` | float | 4,600/6,924 | 66.4% | 2017–2024 | 8 | 2013, 2014, 2015, 2016, 2025 |
| `flight_emissions_lag4` | float | 4,320/6,924 | 62.4% | 2014–2024 | 11 | 2013, 2025 |
| `log_flight_emissions_lag4` | float | 4,320/6,924 | 62.4% | 2014–2024 | 11 | 2013, 2025 |
| `facility_count_lag4` | float | 4,320/6,924 | 62.4% | 2014–2024 | 11 | 2013, 2025 |
| `log_facility_count_lag4` | float | 4,320/6,924 | 62.4% | 2014–2024 | 11 | 2013, 2025 |
| `flight_pct_of_vulcan_lag2` | float | 4,298/6,924 | 62.1% | 2013–2023 | 11 | 2024, 2025 |
| `flight_pct_of_production_lag2` | float | 4,298/6,924 | 62.1% | 2013–2023 | 11 | 2024, 2025 |
| `flight_pct_of_vulcan_lag4` | float | 4,298/6,924 | 62.1% | 2014–2024 | 11 | 2013, 2025 |
| `flight_pct_of_production_lag4` | float | 4,299/6,924 | 62.1% | 2014–2024 | 11 | 2013, 2025 |
| `delta_log_flight_lag3` | float | 4,285/6,924 | 61.9% | 2014–2024 | 11 | 2013, 2025 |
| `pct_change_flight_lag3` | float | 4,285/6,924 | 61.9% | 2014–2024 | 11 | 2013, 2025 |
| `delta_facility_count_lag3` | float | 4,286/6,924 | 61.9% | 2014–2024 | 11 | 2013, 2025 |
| `log_flight_ma2_lag3` | float | 4,285/6,924 | 61.9% | 2014–2024 | 11 | 2013, 2025 |
| `log_flight_ma3_lag2` | float | 4,249/6,924 | 61.4% | 2014–2024 | 11 | 2013, 2025 |
| `facility_count_ma3_lag2` | float | 4,251/6,924 | 61.4% | 2014–2024 | 11 | 2013, 2025 |
| `delta_log_flight_3yr_lag1` | float | 4,217/6,924 | 60.9% | 2014–2024 | 11 | 2013, 2025 |
| `ELC_total_lag3` | float | 4,084/6,924 | 59.0% | 2013–2024 | 12 | 2025 |
| `log_ELC_total_lag3` | float | 4,084/6,924 | 59.0% | 2013–2024 | 12 | 2025 |
| `ELC_share_lag3` | float | 4,084/6,924 | 59.0% | 2013–2024 | 12 | 2025 |
| `delta_log_flight_lag4` | float | 3,903/6,924 | 56.4% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `pct_change_flight_lag4` | float | 3,903/6,924 | 56.4% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `delta_facility_count_lag4` | float | 3,903/6,924 | 56.4% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `log_flight_ma2_lag4` | float | 3,903/6,924 | 56.4% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `flight_pct_of_vulcan_lag1` | float | 3,895/6,924 | 56.3% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `flight_pct_of_production_lag1` | float | 3,895/6,924 | 56.3% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_flight_ma3_lag3` | float | 3,870/6,924 | 55.9% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `facility_count_ma3_lag3` | float | 3,871/6,924 | 55.9% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `delta_log_flight_3yr_lag2` | float | 3,839/6,924 | 55.4% | 2015–2024 | 10 | 2013, 2014, 2025 |
| `ELC_total_lag4` | float | 3,750/6,924 | 54.2% | 2014–2024 | 11 | 2013, 2025 |
| `log_ELC_total_lag4` | float | 3,750/6,924 | 54.2% | 2014–2024 | 11 | 2013, 2025 |
| `ELC_share_lag4` | float | 3,750/6,924 | 54.2% | 2014–2024 | 11 | 2013, 2025 |
| `ELC_total_lag2` | float | 3,742/6,924 | 54.0% | 2013–2023 | 11 | 2024, 2025 |
| `log_ELC_total_lag2` | float | 3,742/6,924 | 54.0% | 2013–2023 | 11 | 2024, 2025 |
| `ELC_share_lag2` | float | 3,742/6,924 | 54.0% | 2013–2023 | 11 | 2024, 2025 |
| `log_flight_ma3_lag4` | float | 3,488/6,924 | 50.4% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `facility_count_ma3_lag4` | float | 3,488/6,924 | 50.4% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `delta_log_flight_3yr_lag3` | float | 3,460/6,924 | 50.0% | 2016–2024 | 9 | 2013, 2014, 2015, 2025 |
| `ELC_total_lag1` | float | 3,400/6,924 | 49.1% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `log_ELC_total_lag1` | float | 3,400/6,924 | 49.1% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `ELC_share_lag1` | float | 3,400/6,924 | 49.1% | 2013–2022 | 10 | 2023, 2024, 2025 |
| `delta_log_flight_3yr_lag4` | float | 3,078/6,924 | 44.5% | 2017–2024 | 8 | 2013, 2014, 2015, 2016, 2025 |
| `avg_facility_emissions_lag1` | float | 0/6,924 | 0.0% | — | 0 | 13 yrs missing |
| `avg_facility_emissions_lag2` | float | 0/6,924 | 0.0% | — | 0 | 13 yrs missing |
| `avg_facility_emissions_lag3` | float | 0/6,924 | 0.0% | — | 0 | 13 yrs missing |
| `avg_facility_emissions_lag4` | float | 0/6,924 | 0.0% | — | 0 | 13 yrs missing |

### FEMA NRI
**File:** `raw/nri/epa_nri.csv`  
**Shape:** 5,598 rows × 435 columns  
**City column:** `city_name` (542 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `National Risk Index Version` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tsunami - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tsunami - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Avalanche - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `National Risk Index - Rating - Composite` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Community Risk Factor - Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hurricane - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tsunami - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Ice Storm - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Avalanche - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Volcanic Activity - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `National Risk Index - Score - Composite` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Heat Wave - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `National Risk Index - Value - Composite` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Coastal Flooding - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Exposure - Impacted Area (sq mi)` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Exposure - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Hazard Type Risk Index Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Heat Wave - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Historic Loss Ratio - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Exposure - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss Rate - Building` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hurricane - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `National Risk Index - State Percentile - Composite` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Cold Wave - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss Rate - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Wildfire - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss - Agriculture Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Ice Storm - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Expected Annual Loss Rate - Agriculture` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hurricane - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Expected Annual Loss Score` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Historic Loss Ratio - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Coastal Flooding - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Expected Annual Loss - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Expected Annual Loss - Population Equivalence` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Winter Weather - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Avalanche - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Landslide - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Exposure - Population` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Lightning - Expected Annual Loss Rate - National Percentile` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Volcanic Activity - Hazard Type Risk Index Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Earthquake - Historic Loss Ratio - Total Rating` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Exposure - Building Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Strong Wind - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Hazard Type Risk Index Value` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Drought - Annualized Frequency` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Expected Annual Loss - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Tornado - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Exposure - Total` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Hail - Number of Events` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Inland Flooding - Historic Loss Ratio - Buildings` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `Heat Wave - Hazard Type Risk Index Score` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss Rate - Population` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Historic Loss Ratio - Agriculture` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Exposure - Impacted Area (sq mi)` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Historic Loss Ratio - Buildings` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss - Population` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss - Total` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss - Building Value` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss Rate - Agriculture` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss Score` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss - Population Equivalence` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Annualized Frequency` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Exposure - Agriculture Value` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Exposure - Building Value` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Exposure - Population Equivalence` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss - Agriculture Value` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss Rate - Building` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Number of Events` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Expected Annual Loss Rate - National Percentile` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Historic Loss Ratio - Population` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Exposure - Total` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Hazard Type Risk Index Value` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Heat Wave - Exposure - Population` | float | 5,587/5,598 | 99.8% | 2013–2023 | 11 | 541 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss Rate - Building` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss - Total` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss - Building Value` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss Score` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Historic Loss Ratio - Buildings` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Number of Events` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss - Population` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Historic Loss Ratio - Population` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss - Population Equivalence` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Exposure - Total` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Hazard Type Risk Index Score` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Exposure - Population` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Exposure - Population Equivalence` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Exposure - Impacted Area (sq mi)` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Annualized Frequency` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Hazard Type Risk Index Value` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss Rate - Population` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Expected Annual Loss Rate - National Percentile` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Ice Storm - Exposure - Building Value` | float | 4,490/5,598 | 80.2% | 2013–2023 | 11 | 402 | 2024, 2025 |
| `Hurricane - Expected Annual Loss - Population Equivalence` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Exposure - Population Equivalence` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss - Population` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Historic Loss Ratio - Population` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Number of Events` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Hazard Type Risk Index Value` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Historic Loss Ratio - Agriculture` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss Rate - Population` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Exposure - Agriculture Value` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss - Total` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Exposure - Total` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Exposure - Building Value` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Hazard Type Risk Index Score` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Annualized Frequency` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss Rate - National Percentile` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss Rate - Building` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss - Building Value` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss Score` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss Rate - Agriculture` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Exposure - Impacted Area (sq mi)` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Exposure - Population` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Expected Annual Loss - Agriculture Value` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Hurricane - Historic Loss Ratio - Buildings` | float | 4,435/5,598 | 79.2% | 2013–2023 | 11 | 426 | 2024, 2025 |
| `Coastal Flooding - Exposure - Population` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss Rate - National Percentile` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Annualized Frequency` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss - Total` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Historic Loss Ratio - Population` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Exposure - Total` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Exposure - Building Value` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss Rate - Building` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Exposure - Impacted Area (sq mi)` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Exposure - Population Equivalence` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss Score` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Historic Loss Ratio - Buildings` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss - Population Equivalence` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Hazard Type Risk Index Value` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss Rate - Population` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Hazard Type Risk Index Score` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss - Population` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Coastal Flooding - Expected Annual Loss - Building Value` | float | 2,520/5,598 | 45.0% | 2013–2023 | 11 | 264 | 2024, 2025 |
| `Avalanche - Exposure - Impacted Area (sq mi)` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Hazard Type Risk Index Value` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Exposure - Population` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Exposure - Total` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss - Population Equivalence` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Exposure - Building Value` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Historic Loss Ratio - Buildings` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss Rate - Building` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss Score` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Annualized Frequency` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss - Total` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Historic Loss Ratio - Population` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss Rate - National Percentile` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss - Population` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Exposure - Population Equivalence` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss Rate - Population` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Hazard Type Risk Index Score` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Expected Annual Loss - Building Value` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Avalanche - Number of Events` | float | 1,653/5,598 | 29.5% | 2013–2023 | 11 | 187 | 2024, 2025 |
| `Volcanic Activity - Exposure - Impacted Area (sq mi)` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Historic Loss Ratio - Buildings` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss - Building Value` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Hazard Type Risk Index Value` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss Rate - National Percentile` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss - Population Equivalence` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Number of Events` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss - Population` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Exposure - Total` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss Rate - Building` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Exposure - Building Value` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Annualized Frequency` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Exposure - Population Equivalence` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Hazard Type Risk Index Score` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss Rate - Population` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss Score` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Expected Annual Loss - Total` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Historic Loss Ratio - Population` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Volcanic Activity - Exposure - Population` | float | 1,056/5,598 | 18.9% | 2013–2023 | 11 | 125 | 2024, 2025 |
| `Tsunami - Hazard Type Risk Index Value` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss Rate - Population` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Exposure - Population Equivalence` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Historic Loss Ratio - Population` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss - Building Value` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Exposure - Impacted Area (sq mi)` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss Rate - National Percentile` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Hazard Type Risk Index Score` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss Rate - Building` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss - Population` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Historic Loss Ratio - Buildings` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Annualized Frequency` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss - Population Equivalence` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Number of Events` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss Score` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Expected Annual Loss - Total` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Exposure - Building Value` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Exposure - Total` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Tsunami - Exposure - Population` | float | 568/5,598 | 10.1% | 2013–2023 | 11 | 81 | 2024, 2025 |
| `Landslide - Number of Events` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Earthquake - Number of Events` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Wildfire - Number of Events` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |
| `Coastal Flooding - Number of Events` | float | 0/5,598 | 0.0% | — | 0 | 0 | 13 yrs missing |

### Yale Climate Opinion
**File:** `raw/climate/climate_opinion_ycom.csv`  
**Shape:** 5,598 rows × 27 columns  
**City column:** `city_name` (542 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `opinion_consensus` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_devharm` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_fundrenewables` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_futuregen` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_happening` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_harmus` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_human` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_personal` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_regulate` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_timing` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_worried` | float | 5,088/5,598 | 90.9% | 2014–2023 | 10 | 542 | 2013, 2024, 2025 |
| `opinion_discuss` | float | 4,143/5,598 | 74.0% | 2016–2023 | 8 | 542 | 2013, 2014, 2015, 2024, 2025 |
| `opinion_harmplants` | float | 4,143/5,598 | 74.0% | 2016–2023 | 8 | 542 | 2013, 2014, 2015, 2024, 2025 |
| `opinion_teachgw` | float | 4,143/5,598 | 74.0% | 2016–2023 | 8 | 542 | 2013, 2014, 2015, 2024, 2025 |
| `opinion_affectweather` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_citizens` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_congress` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_corporations` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_governor` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_localofficials` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_reducetax` | float | 3,110/5,598 | 55.6% | 2018–2023 | 6 | 541 | 7 yrs missing |
| `opinion_priority` | float | 2,117/5,598 | 37.8% | 2020–2023 | 4 | 540 | 9 yrs missing |
| `opinion_exp` | float | 1,602/5,598 | 28.6% | 2021–2023 | 3 | 539 | 10 yrs missing |
| `opinion_generaterenewable` | float | 1,086/5,598 | 19.4% | 2022–2023 | 2 | 539 | 11 yrs missing |

### Climate Policy Controls
**File:** `raw/climate/climate_policy_controls.csv`  
**Shape:** 5,598 rows × 14 columns  
**City column:** `city_name` (542 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_abb` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `muni_aaa_yield` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `c40_member` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `mayors_climate_signatory` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `iclei_member` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `climate_commitment_score` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_rps_active` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_rps_target_pct` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_carbon_pricing` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_carbon_price` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `state_climate_plan` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |

### FEMA Disasters
**File:** `raw/disasters/fema_disaster_declarations.csv`  
**Shape:** 49,408 rows × 8 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2010-2025 (16 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `fema_disaster_any` | int | 49,408/49,408 | 100.0% | 2010–2025 | 16 | None |
| `fema_disaster_count` | int | 49,408/49,408 | 100.0% | 2010–2025 | 16 | None |
| `fema_disaster_cum` | int | 49,408/49,408 | 100.0% | 2010–2025 | 16 | None |
| `fema_disaster_flood` | int | 49,408/49,408 | 100.0% | 2010–2025 | 16 | None |
| `fema_disaster_hurricane` | int | 49,408/49,408 | 100.0% | 2010–2025 | 16 | None |
| `fema_disaster_fire` | int | 49,408/49,408 | 100.0% | 2010–2025 | 16 | None |

### NFIP Flood Claims
**File:** `raw/disasters/nfip_flood_claims.csv`  
**Shape:** 2,273 rows × 9 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `nfip_repetitive_loss` | int | 2,273/2,273 | 100.0% |
| `nfip_severe_repetitive_loss` | int | 2,273/2,273 | 100.0% |
| `nfip_total_properties` | int | 2,273/2,273 | 100.0% |
| `nfip_total_losses` | int | 2,273/2,273 | 100.0% |
| `nfip_mean_losses_per_property` | float | 2,273/2,273 | 100.0% |
| `nfip_mitigated_pct` | float | 2,273/2,273 | 100.0% |
| `nfip_insured_pct` | float | 2,273/2,273 | 100.0% |
| `nfip_most_recent_loss_year` | int | 2,273/2,273 | 100.0% |

### Federal Grants
**File:** `raw/grants/federal_grants_panel.csv`  
**Shape:** 7,514 rows × 76 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2013-2025 (13 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `fips7` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_water_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_water_grant_n` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_water_grant_any` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `ira_eecbg_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `ira_eecbg_grant_n` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `ira_eecbg_grant_any` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_transit_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_transit_grant_n` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_transit_grant_any` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `fema_resil_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `fema_resil_grant_n` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `fema_resil_grant_any` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `ira_ggrf_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `ira_ggrf_grant_n` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `ira_ggrf_grant_any` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `total_federal_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `total_federal_grant_n` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `total_federal_grant_any` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_iija_water_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_ira_eecbg_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_iija_transit_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_fema_resil_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_ira_ggrf_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_total_federal_grant_amt` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `total_federal_grant_cum` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `asinh_total_federal_grant_cum` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | None |
| `iija_water_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `iija_water_grant_n_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `iija_water_grant_any_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `ira_eecbg_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `ira_eecbg_grant_n_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `ira_eecbg_grant_any_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `iija_transit_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `iija_transit_grant_n_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `iija_transit_grant_any_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `fema_resil_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `fema_resil_grant_n_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `fema_resil_grant_any_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `ira_ggrf_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `ira_ggrf_grant_n_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `ira_ggrf_grant_any_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `total_federal_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `total_federal_grant_n_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `total_federal_grant_any_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_iija_water_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_ira_eecbg_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_iija_transit_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_fema_resil_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_ira_ggrf_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_total_federal_grant_amt_lag1` | float | 6,936/7,514 | 92.3% | 2014–2025 | 12 | 2013 |
| `iija_water_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `iija_water_grant_n_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `iija_water_grant_any_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `ira_eecbg_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `ira_eecbg_grant_n_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `ira_eecbg_grant_any_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `iija_transit_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `iija_transit_grant_n_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `iija_transit_grant_any_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `fema_resil_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `fema_resil_grant_n_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `fema_resil_grant_any_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `ira_ggrf_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `ira_ggrf_grant_n_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `ira_ggrf_grant_any_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `total_federal_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `total_federal_grant_n_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `total_federal_grant_any_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `asinh_iija_water_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `asinh_ira_eecbg_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `asinh_iija_transit_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `asinh_fema_resil_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `asinh_ira_ggrf_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |
| `asinh_total_federal_grant_amt_lag2` | float | 6,358/7,514 | 84.6% | 2015–2025 | 11 | 2013, 2014 |

### State Transit Funding
**File:** `raw/grants/state_transit_funding.csv`  
**Shape:** 627 rows × 30 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2013-2025 (13 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `state_population` | int | 627/627 | 100.0% | 2013–2025 | 13 | None |
| `state_has_transit_authority` | int | 627/627 | 100.0% | 2013–2025 | 13 | None |
| `_fta_data_quality` | str | 627/627 | 100.0% | 2013–2025 | 13 | None |
| `state_fta_total` | float | 623/627 | 99.4% | 2013–2025 | 13 | None |
| `state_fta_formula_total` | float | 623/627 | 99.4% | 2013–2025 | 13 | None |
| `state_fta_per_capita` | float | 623/627 | 99.4% | 2013–2025 | 13 | None |
| `state_fta_formula_5307` | float | 617/627 | 98.4% | 2013–2025 | 13 | None |
| `state_fta_enhanced_mobility` | float | 597/627 | 95.2% | 2014–2025 | 12 | 2013 |
| `state_fta_bus_facilities` | float | 593/627 | 94.6% | 2014–2025 | 12 | 2013 |
| `state_fta_rural_5311` | float | 589/627 | 93.9% | 2013–2025 | 13 | None |
| `state_transit_ridership` | float | 576/627 | 91.9% | 2013–2024 | 12 | 2025 |
| `state_transit_ridership_per_capita` | float | 576/627 | 91.9% | 2013–2024 | 12 | 2025 |
| `_ridership_backcast` | float | 576/627 | 91.9% | 2013–2024 | 12 | 2025 |
| `state_fta_planning` | float | 538/627 | 85.8% | 2014–2025 | 12 | 2013 |
| `state_fta_capital_grants` | float | 453/627 | 72.2% | 2013–2025 | 13 | None |
| `state_fta_good_repair` | float | 397/627 | 63.3% | 2014–2025 | 12 | 2013 |
| `state_transit_pmt` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `state_transit_vrh` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `state_transit_operating_expenses` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `state_transit_fare_revenue` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `state_transit_agencies` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `state_transit_funding` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `ntd_state_funding_operations` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `ntd_state_funding_capital` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `ntd_local_funding_operations` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `ntd_local_funding_capital` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `ntd_federal_funding_operations` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |
| `ntd_federal_funding_capital` | float | 153/627 | 24.4% | 2022–2024 | 3 | 10 yrs missing |

### Federal Green Funding
**File:** `raw/grants/federal_green_funding.csv`  
**Shape:** 102 rows × 9 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2022-2023 (2 years)  
**Panel-window coverage (2013–2025):** 2/13 years  
**Missing panel years:** 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `state_abb` | str | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `iija_highway_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `iija_transit_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `iija_water_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `iija_total_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `ira_clean_energy_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `ira_total_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |
| `federal_green_total_billion` | float | 102/102 | 100.0% | 2022–2023 | 2 | 11 yrs missing |

### FOG Institutions
**File:** `raw/institutional/fog_institutions_panel_2010_2024.csv`  
**Shape:** 8,670 rows × 15 columns  
**City column:** `city_name` (548 unique cities)  
**Year column:** `year` — range 2010-2024 (15 years)  
**Panel-window coverage (2013–2025):** 12/13 years  
**Missing panel years:** 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `FIPS_7digit` | int | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `ID` | str | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `FIPS_PLACE_ID` | int | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `fog` | float | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `termlimits` | float | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `termlength` | float | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `districts` | str | 8,670/8,670 | 100.0% | 2010–2024 | 15 | 548 | 2025 |
| `partisan` | float | 8,640/8,670 | 99.7% | 2010–2024 | 15 | 546 | 2025 |
| `JURIS` | str | 8,550/8,670 | 98.6% | 2010–2024 | 15 | 541 | 2025 |
| `initiative` | float | 8,490/8,670 | 97.9% | 2010–2024 | 15 | 537 | 2025 |
| `referendum` | float | 8,490/8,670 | 97.9% | 2010–2024 | 15 | 537 | 2025 |

### TEL Data
**File:** `raw/institutional/tel.csv`  
**Shape:** 5,598 rows × 16 columns  
**City column:** `city_name` (542 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_overall_rate_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_specific_rate_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_levy_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_assessment_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_general_revenue_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_general_expenditure_limit` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_full_disclosure` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_stringency_simple` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_stringency_ads` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_stringency_normalized` | float | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `manually_verified` | int | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `verification_source` | str | 5,598/5,598 | 100.0% | 2013–2023 | 11 | 542 | 2024, 2025 |
| `tel_stringency_category` | str | 5,173/5,598 | 92.4% | 2013–2023 | 11 | 504 | 2024, 2025 |

### Bond Referenda
**File:** `raw/institutional/state_bond_referenda_requirements.csv`  
**Shape:** 50 rows × 10 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `state_abb` | str | 50/50 | 100.0% |
| `go_voter_approval_required` | int | 50/50 | 100.0% |
| `go_vote_threshold` | float | 50/50 | 100.0% |
| `go_supermajority` | int | 50/50 | 100.0% |
| `revenue_bond_voter_approval` | int | 50/50 | 100.0% |
| `has_state_bond_commission` | int | 50/50 | 100.0% |
| `has_constitutional_debt_limit` | int | 50/50 | 100.0% |
| `has_state_approval_body` | int | 50/50 | 100.0% |
| `source_notes` | str | 50/50 | 100.0% |

### Bond Banks
**File:** `raw/institutional/state_bond_banks.csv`  
**Shape:** 50 rows × 9 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `state_abb` | str | 50/50 | 100.0% |
| `has_bond_bank` | int | 50/50 | 100.0% |
| `bond_bank_name` | str | 14/50 | 28.0% |
| `bond_bank_established` | float | 14/50 | 28.0% |
| `bond_bank_active_2013_2025` | float | 14/50 | 28.0% |
| `bond_bank_rating` | str | 7/50 | 14.0% |
| `bond_bank_cumulative_billion` | float | 4/50 | 8.0% |
| `notes` | str | 3/50 | 6.0% |

### Anti-ESG Laws
**File:** `raw/political/antiesg_laws.csv`  
**Shape:** 5,609 rows × 31 columns  
**City column:** `city_name` (543 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_cum_ag_investigations` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_cum_ag_letters` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_cum_divestments` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_cum_exec_actions` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_governor_alliance_member` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_antiesg_law` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_antiesg_proposed` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_board_diversity_mandate` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_esg_disclosure_requirement` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_fossil_divestment` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_law_civil_liability` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_law_esg_score_ban_govt` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_law_esg_score_ban_private` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_law_proxy_voting` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_law_restricted_contracts` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_law_restricted_pension` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_muni_bond_law` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_proesg_contracts` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_proesg_law` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_has_underwriter_block` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_law_intensity_score` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_msrb_letter_signatory` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_num_antiesg_laws` | float | 5,609/5,609 | 100.0% | 2013–2023 | 11 | 543 | 2024, 2025 |
| `esg_first_exec_action_year` | float | 829/5,609 | 14.8% | 2018–2023 | 6 | 275 | 7 yrs missing |
| `esg_first_bill_year` | float | 749/5,609 | 13.4% | 2021–2023 | 3 | 359 | 10 yrs missing |
| `esg_first_proesg_year` | float | 519/5,609 | 9.3% | 2020–2023 | 4 | 198 | 9 yrs missing |
| `esg_first_law_year` | float | 361/5,609 | 6.4% | 2021–2023 | 3 | 209 | 10 yrs missing |
| `esg_first_underwriter_block_year` | float | 90/5,609 | 1.6% | 2018–2023 | 6 | 57 | 7 yrs missing |

### Presidential Elections
**File:** `raw/political/presidential_elections.csv`  
**Shape:** 5,653 rows × 6 columns  
**City column:** `city_name` (547 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `pres_dem_two_party_share` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `pres_dem_vote_share` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `pres_rep_vote_share` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |

### State Political
**File:** `raw/political/state_political.csv`  
**Shape:** 5,653 rows × 9 columns  
**City column:** `city_name` (547 unique cities)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `fips7` | int | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `state_dem_governor` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `state_dem_legislature` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `state_dem_trifecta` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `state_rep_trifecta` | float | 5,653/5,653 | 100.0% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `state_govt_trifecta` | str | 5,611/5,653 | 99.3% | 2013–2023 | 11 | 547 | 2024, 2025 |
| `state_legis_control` | str | 5,611/5,653 | 99.3% | 2013–2023 | 11 | 547 | 2024, 2025 |

### MSRB RFI Position
**File:** `raw/political/state_msrb_rfi_position.csv`  
**Shape:** 50 rows × 6 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `state_abb` | str | 50/50 | 100.0% |
| `signed_utah_antiesg_letter` | int | 50/50 | 100.0% |
| `msrb_rfi_position` | str | 50/50 | 100.0% |
| `source` | str | 29/50 | 58.0% |
| `signatory_role` | str | 24/50 | 48.0% |

### SRF Bond Merged
**File:** `raw/srf/srf_bond_merged.csv`  
**Shape:** 7,514 rows × 471 columns  
**City column:** `City` (548 unique cities)  
**Year column:** `year` — range 2013-2025 (13 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | # Cities | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|----------|------------|
| `geo_name` | str | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `state_abb` | str | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `county_fips5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `dwsrf_total_allotment` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `dwsrf_arra_supplement` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `cwsrf_total_allotment` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `cwsrf_arra_supplement` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `total_srf_allotment` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_n_agreements` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_total_lending` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_mean_lending` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_median_lending` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_mean_interest_rate` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_mean_repayment_years` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_cw_n_agreements` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_cw_total_lending` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_cw_mean_interest` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_dw_n_agreements` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_dw_total_lending` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `portal_dw_mean_interest` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `srf_total_principal_forgiveness` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `srf_total_pop_served` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `cwsrf_n_projects` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `cwsrf_total_amount` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `dwsrf_n_projects` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `dwsrf_total_amount` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `n_water_systems` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `srf_received_any` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `srf_ever_received` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `srf_received_any_lag1` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `total_srf_allotment_lag1` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `county_n_crosswalk_cities` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Year` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Green_Bond_Issued` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `City_Green_Amt_Issued` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `City_Green_Issuance_Count` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Total_Amt_Issued` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Total_Issuance_Count` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Govt_Amt_Issued` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `State_Govt_Issuance_Count` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `City_Share_of_State_Pct` | float | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__AMT_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__AMT_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_&_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_&_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_BQ` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_BQ` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_BQ_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_BQ_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT_ST_TAX...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT_ST_TAX...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT_ST_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT_ST_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAX-EXEMPT_ST_TAX…` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAX-EXEMPT_ST_TAX…` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAXABLE` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Tax Prov__FED_TAXABLE_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Tax Prov__FED_TAXABLE_ST_TAX-EXEMPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__NEW_MONEY` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__NEW_MONEY` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__New_Money` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__New_Money` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__REFUNDING` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__REFUNDING` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Fin Typ__REFUNDING...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Fin Typ__REFUNDING...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Education` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Education` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Financing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Financing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Financing...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Financing...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__General_Government` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__General_Government` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Public_Services` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Public_Services` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Transporta` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Transporta` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Transporta...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Transporta...` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_BICS Level 2__Utilities` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_BICS Level 2__Utilities` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Self-reported Green__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Self-reported Green__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Self-reported Green__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Self-reported Green__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Self-reported Green__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Self-reported Green__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Mgmt of Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Mgmt of Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Mgmt of Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Mgmt of Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Mgmt of Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Mgmt of Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Reporting__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Reporting__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Reporting__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Reporting__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Reporting__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Reporting__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Assurance Providers__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Assurance Providers__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Assurance Providers__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Assurance Providers__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Assurance Providers__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Assurance Providers__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Proj Sel Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Proj Sel Proc__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Proj Sel Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Proj Sel Proc__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Proj Sel Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Proj Sel Proc__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Framework__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Framework__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Framework__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Framework__No` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Framework__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Framework__Yes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__APPROP` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__APPROP` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__ARPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__ARPT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__DEV` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__DEV` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__GO` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__GO` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__GODIST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__GODIST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__LMFH` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__LMFH` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__MEL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__MEL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__MUNUTIL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__MUNUTIL` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__NFPCULT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__NFPCULT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PILOT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PILOT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PORTS` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PORTS` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PUBPWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PUBPWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__PUBTRAN` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__PUBTRAN` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__SCD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__SCD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__SOLWST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__SOLWST` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__SPLASMT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__SPLASMT` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__TXMUD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__TXMUD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__WSGTD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__WSGTD` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry__WTRSWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry__WTRSWR` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Airport` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Airport` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Appropriation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Appropriation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Development` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Development` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__General_Obligation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__General_Obligation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__General_Obligation_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__General_Obligation_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Limited_Multi-Family_Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Limited_Multi-Family_Housing` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Mello-Roos` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Mello-Roos` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Municipal_Utility` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Municipal_Utility` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Not-for-Profit_–_Cultural` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Not-for-Profit_–_Cultural` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Payment_in_Lieu_of_Taxes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Payment_in_Lieu_of_Taxes` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Ports_Marina` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Ports_Marina` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Public_Power` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Public_Power` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Public_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Public_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__School_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__School_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Solid_Waste` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Solid_Waste` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Special_Assessment` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Special_Assessment` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Texas_Municipal_Utility_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Texas_Municipal_Utility_District` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Industry_Full__Water_Sewer` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Industry_Full__Water_Sewer` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__--` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.45` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.45` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.7` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.7` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.72` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.72` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.78` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.78` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.84` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.84` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.94` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.94` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.95` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.95` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__3.97` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__3.97` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.05` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.05` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.08` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.08` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.2` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.2` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.22` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.22` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.25` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.25` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.26` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.26` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.33` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.35` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.4` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.4` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.43` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.43` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.55` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.58` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.58` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.6` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.6` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.63` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.63` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.65` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.65` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.68` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.75` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.75` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.8` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.8` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.88` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.88` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__4.93` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__4.93` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Kestrel Total ESG Impact Score__5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Kestrel Total ESG Impact Score__5` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Biodiversity,_Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Biodiversity,_Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Biodiversity,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Biodiversity,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Clean_Transportation,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Clean_Transportation,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Energy_Efficiency,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Energy_Efficiency,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Natural_Resource_Management` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Natural_Resource_Management` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control,_Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Pollution_Control,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Pollution_Control,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Renewable_Energy,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Renewable_Energy,_Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Circular_Economy` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Climate_Change_Adaptation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Energy_Efficiency` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_ESG Project Categories__Sustainable_Water,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_ESG Project Categories__Sustainable_Water,_Green_Buildings` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Circular_Design_and_Production` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Circular_Design_and_Production` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Conservation,_Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Conservation,_Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Star_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Star_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Star_Certified,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Star_Certified,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Energy_Storage,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Energy_Storage,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Hydrogen` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Hydrogen` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Circular_Value_Recovery` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Circular_Value_Recovery` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Green_House_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infastructure,_Vehicles` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infastructure,_Vehicles` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Information_Support,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Information_Support,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infrastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Infrastructure,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Infrastructure,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__LEED_Certified,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__LEED_Certified,_BREEAM_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__LEED_Certified,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__LEED_Certified,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Plumbing_System,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Plumbing_System,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Pollution_Control,_Greenhouse_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Pollution_Control,_Greenhouse_Gas_Control` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Public` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Public,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Public,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Rail_(Non_Passenger)` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Rail_(Non_Passenger)` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Soil_Remediation,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Soil_Remediation,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Bioenergy,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Bioenergy,_Plumbing_System` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Energy_Storage` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Infastructure` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Solar,_Wind,_Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Solar,_Wind,_Bioenergy,_Hydro` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Sustainable_Forestry,_Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Sustainable_Forestry,_Soil_Remediation` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Amt_Project Subcategory__Vehicles,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `Count_Project Subcategory__Vehicles,_LEED_Certified` | int | 7,514/7,514 | 100.0% | 2013–2025 | 13 | 548 | None |
| `usaspending_total` | float | 7,406/7,514 | 98.6% | 2013–2025 | 13 | 548 | None |
| `state_population_usaspending` | float | 7,406/7,514 | 98.6% | 2013–2025 | 13 | 548 | None |
| `state_srf_allotment_per_capita` | float | 7,406/7,514 | 98.6% | 2013–2025 | 13 | 548 | None |
| `portal_lending_per_capita` | float | 7,406/7,514 | 98.6% | 2013–2025 | 13 | 548 | None |
| `usaspending_dwsrf` | float | 7,381/7,514 | 98.2% | 2013–2025 | 13 | 548 | None |
| `cbsa_code` | float | 7,358/7,514 | 97.9% | 2013–2025 | 13 | 536 | None |
| `cbsa_title` | str | 7,358/7,514 | 97.9% | 2013–2025 | 13 | 536 | None |
| `cbsa_n_crosswalk_cities` | float | 7,358/7,514 | 97.9% | 2013–2025 | 13 | 536 | None |
| `usaspending_cwsrf` | float | 7,338/7,514 | 97.7% | 2013–2025 | 13 | 548 | None |
| `total_population_served` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `total_service_connections` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `n_groundwater_systems` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `n_surface_water_systems` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `n_municipal_owned` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `n_local_govt_owned` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `n_private_owned` | float | 7,176/7,514 | 95.5% | 2013–2025 | 13 | 524 | None |
| `state_srf_n_loans` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_total_lending` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_mean_loan_size` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_median_loan_size` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_mean_interest` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_median_interest` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_mean_fee_rate` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_mean_repayment` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_median_repayment` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_pct_conduit` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_pct_sponsorship` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_pct_programmatic` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_pct_cw` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_mean_upfront_fees` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_other_srf_lending` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `srf_own_state_share` | float | 1,139/7,514 | 15.2% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_mean_finance_charge` | float | 1,128/7,514 | 15.0% | 2024–2025 | 2 | 547 | 11 yrs missing |
| `state_srf_cw_mean_interest` | float | 1,089/7,514 | 14.5% | 2024–2025 | 2 | 541 | 11 yrs missing |
| `state_srf_cw_mean_repayment` | float | 1,089/7,514 | 14.5% | 2024–2025 | 2 | 541 | 11 yrs missing |
| `state_srf_cw_n_loans` | float | 1,089/7,514 | 14.5% | 2024–2025 | 2 | 541 | 11 yrs missing |
| `state_srf_cw_total_lending` | float | 1,089/7,514 | 14.5% | 2024–2025 | 2 | 541 | 11 yrs missing |
| `state_srf_dw_mean_interest` | float | 1,081/7,514 | 14.4% | 2024–2025 | 2 | 543 | 11 yrs missing |
| `state_srf_dw_mean_repayment` | float | 1,081/7,514 | 14.4% | 2024–2025 | 2 | 543 | 11 yrs missing |
| `state_srf_dw_n_loans` | float | 1,081/7,514 | 14.4% | 2024–2025 | 2 | 543 | 11 yrs missing |
| `state_srf_dw_total_lending` | float | 1,081/7,514 | 14.4% | 2024–2025 | 2 | 543 | 11 yrs missing |
| `srf_n_projects` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_total_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_mean_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_median_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_total_current_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_mean_interest_rate` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_mean_fee_rate` | float | 82/7,514 | 1.1% | 2024–2025 | 2 | 67 | 11 yrs missing |
| `srf_mean_finance_charge` | float | 83/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_mean_repayment_years` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_total_upfront_fees` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_n_cw` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_n_dw` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_any_conduit` | str | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_any_sponsorship` | str | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_any_programmatic` | str | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_cumulative_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_cumulative_projects` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `county_other_srf_n_projects` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `county_other_srf_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `cbsa_other_srf_n_projects` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `cbsa_other_srf_amount` | float | 85/7,514 | 1.1% | 2024–2025 | 2 | 68 | 11 yrs missing |
| `srf_cw_amount` | float | 72/7,514 | 1.0% | 2024–2025 | 2 | 58 | 11 yrs missing |
| `srf_cw_mean_interest` | float | 72/7,514 | 1.0% | 2024–2025 | 2 | 58 | 11 yrs missing |
| `srf_cw_mean_repayment` | float | 72/7,514 | 1.0% | 2024–2025 | 2 | 58 | 11 yrs missing |
| `srf_dw_amount` | float | 32/7,514 | 0.4% | 2024–2025 | 2 | 26 | 11 yrs missing |
| `srf_dw_mean_interest` | float | 32/7,514 | 0.4% | 2024–2025 | 2 | 26 | 11 yrs missing |
| `srf_dw_mean_repayment` | float | 32/7,514 | 0.4% | 2024–2025 | 2 | 26 | 11 yrs missing |
| `srf_total_amount_lag1` | float | 27/7,514 | 0.4% | 2025–2025 | 1 | 27 | 12 yrs missing |

### ESG AUM
**File:** `raw/market/esg_aum.csv`  
**Shape:** 11 rows × 5 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `global_esg_aum_trillion` | float | 11/11 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `us_esg_aum_trillion` | float | 11/11 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `esg_aum_growth_pct` | str | 11/11 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `esg_share_global_aum` | float | 11/11 | 100.0% | 2013–2023 | 11 | 2024, 2025 |

### State Green Bond Capacity
**File:** `raw/market/state_green_bond_capacity.csv`  
**Shape:** 550 rows × 13 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2013-2023 (11 years)  
**Panel-window coverage (2013–2025):** 11/13 years  
**Missing panel years:** 2024, 2025  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `state_abb` | str | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_count` | int | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_amt` | float | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_cum_count` | int | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_cum_amt` | float | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_ever` | int | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_cum_count_lag1` | int | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_cum_amt_lag1` | float | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_ever_lag1` | int | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `state_green_bond_issued_prior_yr` | int | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `asinh_state_green_bond_amt` | float | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |
| `asinh_state_green_bond_cum_amt_lag1` | float | 550/550 | 100.0% | 2013–2023 | 11 | 2024, 2025 |

### Municipal Electric
**File:** `raw/energy_policy/municipal_electric_utilities.csv`  
**Shape:** 578 rows × 8 columns  
**City column:** `city_name` (548 unique cities)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null | # Cities |
|----------|------|----------|------------|----------|
| `state_abb` | str | 578/578 | 100.0% | 548 |
| `has_municipal_electric` | int | 578/578 | 100.0% | 548 |
| `large_enough_for_bonds` | int | 578/578 | 100.0% | 548 |
| `utility_name` | str | 82/578 | 14.2% | 80 |
| `customers` | float | 82/578 | 14.2% | 80 |
| `revenue_thousands` | float | 82/578 | 14.2% | 80 |
| `revenue_millions` | float | 82/578 | 14.2% | 80 |

### State Building Codes
**File:** `raw/energy_policy/state_building_codes.csv`  
**Shape:** 50 rows × 12 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `state_building_code_year` | int | 50/50 | 100.0% |
| `state_building_code_residential_iecc` | str | 50/50 | 100.0% |
| `state_building_code_commercial_iecc` | str | 50/50 | 100.0% |
| `state_has_mandatory_statewide_code` | int | 50/50 | 100.0% |
| `state_building_code_stringency_aceee_rank` | int | 50/50 | 100.0% |
| `state_has_commercial_benchmarking` | int | 50/50 | 100.0% |
| `state_has_residential_disclosure` | int | 50/50 | 100.0% |
| `data_year` | int | 50/50 | 100.0% |
| `sources` | str | 50/50 | 100.0% |

### State Clean Energy
**File:** `raw/energy_policy/state_clean_energy_funds.csv`  
**Shape:** 50 rows × 12 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null |
|----------|------|----------|------------|
| `state_abb` | str | 50/50 | 100.0% |
| `state_has_green_bank` | int | 50/50 | 100.0% |
| `state_has_energy_efficiency_program` | int | 50/50 | 100.0% |
| `state_has_clean_energy_standard` | int | 50/50 | 100.0% |
| `state_has_rps` | int | 50/50 | 100.0% |
| `notes` | str | 50/50 | 100.0% |
| `state_eers_target` | float | 41/50 | 82.0% |
| `state_eers_has` | float | 34/50 | 68.0% |
| `state_green_bank_year` | float | 27/50 | 54.0% |
| `state_green_bank_name` | str | 27/50 | 54.0% |
| `state_has_resilience_fund` | float | 27/50 | 54.0% |

### State Net Metering
**File:** `raw/energy_policy/state_net_metering.csv`  
**Shape:** 800 rows × 6 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2010-2025 (16 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `state_abb` | str | 800/800 | 100.0% | 2010–2025 | 16 | None |
| `state_has_net_metering` | int | 800/800 | 100.0% | 2010–2025 | 16 | None |
| `state_has_community_solar` | int | 800/800 | 100.0% | 2010–2025 | 16 | None |
| `state_net_metering_cap_kw` | float | 667/800 | 83.4% | 2010–2025 | 16 | None |
| `state_has_municipal_utility_exemption` | float | 480/800 | 60.0% | 2010–2025 | 16 | None |

### Water Panel
**File:** `raw/geospatial/substitute_water_panel.csv`  
**Shape:** 7,501 rows × 14 columns  
**City column:** not detected (may be state-level or national)  
**Year column:** `year` — range 2013-2025 (13 years)  
**Panel-window coverage (2013–2025):** 13/13 years  

| Variable | Type | Non-Null | % Non-Null | Year Range (data) | # Years | Panel Gaps |
|----------|------|----------|------------|-------------------|---------|------------|
| `fips7` | float | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `substitute_water_25km` | float | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `substitute_water_50km` | float | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `substitute_water_any_25km` | int | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `substitute_water_n_25km` | int | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `asinh_substitute_water_25km` | float | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `asinh_substitute_water_50km` | float | 7,501/7,501 | 100.0% | 2013–2025 | 13 | None |
| `substitute_water_25km_lag1` | float | 6,924/7,501 | 92.3% | 2014–2025 | 12 | 2013 |
| `substitute_water_any_25km_lag1` | float | 6,924/7,501 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_substitute_water_25km_lag1` | float | 6,924/7,501 | 92.3% | 2014–2025 | 12 | 2013 |
| `substitute_water_50km_lag1` | float | 6,924/7,501 | 92.3% | 2014–2025 | 12 | 2013 |
| `asinh_substitute_water_50km_lag1` | float | 6,924/7,501 | 92.3% | 2014–2025 | 12 | 2013 |
| `substitute_water_n_25km_lag1` | float | 6,924/7,501 | 92.3% | 2014–2025 | 12 | 2013 |

### Crosswalk
**File:** `raw/crosswalk/Crosswalk.csv`  
**Shape:** 578 rows × 31 columns  
**City column:** `city_name` (548 unique cities)  
**Year column:** not detected (cross-sectional dataset)  

| Variable | Type | Non-Null | % Non-Null | # Cities |
|----------|------|----------|------------|----------|
| `geo_name` | str | 578/578 | 100.0% | 548 |
| `state_abb` | str | 578/578 | 100.0% | 548 |
| `GEO_ID_city` | str | 578/578 | 100.0% | 548 |
| `place_geo_id` | str | 578/578 | 100.0% | 548 |
| `NAME_city` | str | 578/578 | 100.0% | 548 |
| `county_geo_id` | str | 578/578 | 100.0% | 548 |
| `GEO_ID_county` | str | 578/578 | 100.0% | 548 |
| `NAME_county` | str | 578/578 | 100.0% | 548 |
| `state_fips2` | int | 578/578 | 100.0% | 548 |
| `state_abbrev` | str | 578/578 | 100.0% | 548 |
| `_fips7` | int | 578/578 | 100.0% | 548 |
| `_state` | str | 578/578 | 100.0% | 548 |
| `_name` | str | 578/578 | 100.0% | 548 |
| `fips7` | int | 578/578 | 100.0% | 548 |
| `city_place7` | int | 578/578 | 100.0% | 548 |
| `state_fips2_hist` | int | 578/578 | 100.0% | 548 |
| `fiscal_muni_id` | int | 578/578 | 100.0% | 548 |
| `fiscal_muni_name` | str | 578/578 | 100.0% | 548 |
| `city_place7_HIST` | int | 578/578 | 100.0% | 548 |
| `city_name_HIST` | str | 578/578 | 100.0% | 548 |
| `state_fips2_HIST` | int | 578/578 | 100.0% | 548 |
| `fiscal_muni_id_HIST` | int | 578/578 | 100.0% | 548 |
| `fiscal_muni_name_HIST` | str | 578/578 | 100.0% | 548 |
| `gid_name_2012_2016` | str | 578/578 | 100.0% | 548 |
| `pid_name_2017_2023` | str | 578/578 | 100.0% | 548 |
| `hist_fiscal_id` | int | 578/578 | 100.0% | 548 |
| `hist_fiscal_name` | str | 578/578 | 100.0% | 548 |
| `relevant_counties` | str | 90/578 | 15.6% | 89 |
| `recommended_approach` | str | 90/578 | 15.6% | 89 |

---

## 3. Panel-Window Alignment (2013–2025)

Summary of how each dataset aligns with the 13-year green bond analysis window.

| Dataset | Level | Years in Panel | Panel Coverage | Cities | Notes |
|---------|-------|---------------|----------------|--------|-------|
| Bloomberg Issuance | City-Year | 13/13 (100%) | 13/13 (100%) | 548 | Full coverage |
| Mayor Party | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | pre-panel data from 2010 |
| Mayoral Candidates | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | pre-panel data from 2001 |
| Constructed Fiscal | City-Year | 11/13 (85%) | 11/13 (85%) | 542 | missing: 2024, 2025 |
| Fiscal TEL Merged 2007-2024 | City-Year | 12/13 (92%) | 12/13 (92%) | 577 | pre-panel data from 2007; missing: 2025 |
| Fiscal TEL Merged 2013-2025 | City-Year | 12/13 (92%) | 12/13 (92%) | 548 | missing: 2025 |
| ACS Additional | State/National-Year | 12/13 (92%) | 12/13 (92%) | — | pre-panel data from 2010; missing: 2025 |
| BLS ACS Economic | City-Year | 11/13 (85%) | 11/13 (85%) | 544 | pre-panel data from 2010; missing: 2024, 2025 |
| ACS Demographics 2022 | Cross-section | N/A | N/A | — | No year dimension |
| EPA Enforcement | City-Year | 13/13 (100%) | 13/13 (100%) | 546 | pre-panel data from 2000; post-panel data to 2026 |
| EPA State Enforcement | City-Year | 11/13 (85%) | 11/13 (85%) | 542 | missing: 2024, 2025 |
| Vulcan CO2 | State/National-Year | 12/13 (92%) | 12/13 (92%) | — | missing: 2025 |
| FEMA NRI | City-Year | 11/13 (85%) | 11/13 (85%) | 542 | missing: 2024, 2025 |
| Yale Climate Opinion | City-Year | 11/13 (85%) | 11/13 (85%) | 542 | missing: 2024, 2025 |
| Climate Policy Controls | City-Year | 11/13 (85%) | 11/13 (85%) | 542 | missing: 2024, 2025 |
| FEMA Disasters | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | pre-panel data from 2010 |
| NFIP Flood Claims | Cross-section | N/A | N/A | — | No year dimension |
| Federal Grants | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | Full coverage |
| State Transit Funding | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | Full coverage |
| Federal Green Funding | State/National-Year | 2/13 (15%) | 2/13 (15%) | — | 11 panel years missing |
| FOG Institutions | City-Year | 12/13 (92%) | 12/13 (92%) | 548 | pre-panel data from 2010; missing: 2025 |
| TEL Data | City-Year | 11/13 (85%) | 11/13 (85%) | 542 | missing: 2024, 2025 |
| Bond Referenda | Cross-section | N/A | N/A | — | No year dimension |
| Bond Banks | Cross-section | N/A | N/A | — | No year dimension |
| Anti-ESG Laws | City-Year | 11/13 (85%) | 11/13 (85%) | 543 | missing: 2024, 2025 |
| Presidential Elections | City-Year | 11/13 (85%) | 11/13 (85%) | 547 | missing: 2024, 2025 |
| State Political | City-Year | 11/13 (85%) | 11/13 (85%) | 547 | missing: 2024, 2025 |
| MSRB RFI Position | Cross-section | N/A | N/A | — | No year dimension |
| SRF Bond Merged | City-Year | 13/13 (100%) | 13/13 (100%) | 548 | Full coverage |
| ESG AUM | State/National-Year | 11/13 (85%) | 11/13 (85%) | — | missing: 2024, 2025 |
| State Green Bond Capacity | State/National-Year | 11/13 (85%) | 11/13 (85%) | — | missing: 2024, 2025 |
| Municipal Electric | City (cross-section) | N/A | N/A | 548 | No year dimension |
| State Building Codes | Cross-section | N/A | N/A | — | No year dimension |
| State Clean Energy | Cross-section | N/A | N/A | — | No year dimension |
| State Net Metering | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | pre-panel data from 2010 |
| Water Panel | State/National-Year | 13/13 (100%) | 13/13 (100%) | — | Full coverage |
| Crosswalk | City (cross-section) | N/A | N/A | 548 | No year dimension |

---

## 4. Critical Gaps and Data Quality Flags

### 4a. Variables with <50% non-null rate (potential concern)

| Dataset | Variable | % Non-Null | Year Range | Cities |
|---------|----------|------------|------------|--------|
| Mayoral Candidates | `cfscore` | 38.0% | 2005–2024 | — |
| Mayoral Candidates | `flag` | 20.6% | 2001–2025 | — |
| Mayoral Candidates | `review_flag` | 15.4% | 2001–2025 | — |
| Mayoral Candidates | `review_detail` | 44.6% | 2002–2025 | — |
| Constructed Fiscal | `pension_expenditure_burden` | 13.5% | 2013–2016 | 237 |
| Constructed Fiscal | `pension_exp_own_source` | 13.5% | 2013–2016 | 237 |
| Fiscal TEL Merged 2007-2024 | `air_trans_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `air_trans_construction` | 44.2% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `air_trans_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `air_trans_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `air_trans_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `air_trans_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `alcoholic_beverage_lic` | 44.1% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `alcoholic_beverage_tax` | 33.3% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `amusement_license` | 33.6% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `amusement_tax` | 36.7% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_all_other` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_education` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_priv_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `beg_ltd_out_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `bond_fd_cash_&_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `cen_staff_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `cen_staff_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `cen_staff_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `cen_staff_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `cen_staff_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `census_region` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_air_transportation` | 47.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_elem_ed_nec` | 34.0% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_elem_ed_sch_lunch` | 33.9% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_elem_ed_tuition` | 32.2% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_hospitals` | 29.1% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_misc_com_activ` | 48.7% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_toll_highways` | 27.6% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_total_education` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_total_high_ed` | 27.0% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_total_nat_res` | 39.0% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `chg_water_transport` | 31.5% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `corp_net_income_tax` | 28.7% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `corporation_license` | 26.9% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `correct_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `correct_construct` | 29.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `correct_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `correct_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `correct_ig_to_st` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `correct_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `death_and_gift_tax` | 27.5% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `docum_and_stock_tr_tax` | 44.5% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_assistance` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_construction` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `educ_nec_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elec_util_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elec_util_construct` | 35.4% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `elec_util_inter_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elec_util_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `electric_utility_rev` | 38.1% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_construction` | 34.6% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_ig_sch_to_sch` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_benefit_paymts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_from_other_gov` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_int_rev` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_loc_emp_ctrib` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_loc_to_loc_sys` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_other_earnings` | 26.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_other_paymts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_sta_to_sta_ctr` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_total_ctrib` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_withdrawals` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_cash_&_dep` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_cash_&_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_corp_bds` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_corp_stk` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_misc_inv` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_mortgages` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_oth_nong` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_s&l_secur` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_tot_fed` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_sec_tot_nong` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_retire_total_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_sec_adm_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_sec_adm_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `emp_sec_adm_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_air_transport` | 39.9% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_education` | 31.9% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_emp_sec_adm` | 26.7% | 2007–2015 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_gen_rev_shar` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_gen_support` | 35.2% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_health_&_hos` | 38.1% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_highways` | 45.9% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_natural_res` | 30.1% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_public_welf` | 36.3% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_sewerage` | 33.1% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_transit_sub` | 39.8% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `fin_admin_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fin_admin_construction` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fin_admin_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fin_admin_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fin_admin_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fin_admin_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fips7` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fips_code_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fire_prot_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fire_prot_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fire_prot_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fire_prot_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `fyenddate` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `gas_util_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `gas_util_construct` | 29.6% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `gas_util_inter_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `gas_util_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `gas_utility_rev` | 30.7% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `gen_pub_bldg_cap_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `gen_pub_bldg_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `gen_pub_bldg_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_assist_&_sub` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_construction` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_current_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_current_oper` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_ig_to_fed` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_ig_to_st` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `general_nec_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `health_capital_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `health_construction` | 44.6% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `health_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `health_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `health_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `health_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_construct` | 26.9% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_ig_to_st` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hosp_other_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hosp_other_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hosp_other_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hosp_other_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hosp_other_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hosp_other_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hous_&_com_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hous_&_com_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hous_&_com_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hous_&_com_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `hunting_&_fishing_license` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `idchanged` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ig_exp_to_federal_govt` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ig_exp_to_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ig_exp_to_state_govt` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `imputed_record` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `individual_income_tax` | 33.1% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `insur_trust_cash_&_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `insurance_premium_tax` | 31.1% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `interest_on_gen_debt` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `jacketunit` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `judicial_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `judicial_construction` | 41.0% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `judicial_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `judicial_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `judicial_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `judicial_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `libraries_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `libraries_construction` | 49.7% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `libraries_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `libraries_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `libraries_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `liquor_stores_cap_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `liquor_stores_constr` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `liquor_stores_revenue` | 27.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `liquor_stores_tot_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_health_&_hos` | 31.0% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_highways` | 42.8% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_hous/com_dev` | 37.1% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_interschool_aid` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_oth_gen_sup` | 43.6% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_other_education` | 32.2% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_public_welf` | 31.0% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_sewerage` | 31.9% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `local_igr_transit_sub` | 33.3% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_all_other` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ffc_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_gen_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_gen_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_gen_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_ng_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_unsp_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_util_electric` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_util_gas_supply` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_util_transit` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_util_water` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_iss_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_all_other` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ffc_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_gen_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_gen_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_gen_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_ng_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_util_electric` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_util_gas_supply` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_util_transit` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_out_util_water` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_all_other` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ffc_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_gen_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_gen_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_gen_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_elec_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_ng_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_private_purp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_elec_utili` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_elem_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_gas_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_general` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_other_educ` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_other_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_trans_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_unsp_water_util` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_util_electric` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_util_gas_supply` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_util_transit` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_util_water` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `ltd_ret_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `misc_com_activ_cap_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `misc_com_activ_constr` | 34.4% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `misc_com_activ_tot_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `motor_fuels_tax` | 32.2% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `motor_veh_oper_license` | 27.2% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `motor_vehicle_license` | 38.3% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `natural_res_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `natural_res_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `natural_res_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `natural_res_ig_to_sta` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `net_lottery_revenue` | 26.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `oth_nonin_fd_cash_&_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `own_hospital_cap_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `own_hospital_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `own_hospital_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `pari_mutuels_tax` | 27.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `parking_capital_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parking_construction` | 42.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `parking_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parking_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parking_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parking_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parks_&_rec_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parks_&_rec_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parks_&_rec_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `parks_&_rec_ig_to_sta` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `police_prot_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `police_prot_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `police_prot_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `police_prot_ig_to_sta` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `police_prot_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `population` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_construction` | 43.7% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `public_utility_license` | 31.3% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `public_welf_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `public_welf_cash_asst` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `public_welf_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `public_welf_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `public_welf_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `regular_hwy_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `regular_hwy_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `regular_hwy_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `regular_hwy_ig_to_sta` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `severance_tax` | 27.5% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `sewerage_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sewerage_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sewerage_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sewerage_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sewerage_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sinking_fd_cash_&_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sortcode` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_code` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_education` | 34.4% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_health_&_hos` | 41.0% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_hous/com_dev` | 49.0% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_public_welf` | 39.6% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_sewerage` | 40.3% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_tax_relief` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `state_igr_transit_sub` | 39.9% | 2007–2021 | 547 |
| Fiscal TEL Merged 2007-2024 | `surveyyr` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sw_mgmt_capital_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sw_mgmt_construction` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sw_mgmt_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sw_mgmt_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sw_mgmt_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `sw_mgmt_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `taxes_nec` | 45.0% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `tobacco_tax` | 30.4% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `toll_hwy_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `toll_hwy_construction` | 27.8% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `toll_hwy_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `tot_assist_&_subsidies` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `tot_ins_trust_inv_rev` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `tot_ltd_out_ng` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_beg_ltd_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_cash_&_securities` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_current_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_educ_assist_&_sub` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_educ_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_educ_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_educ_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_educ_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_highways_cap_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_highways_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_highways_dir_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_highways_tot_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_hospital_cap_out` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_hospital_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_hospital_dir_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_hospital_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_hospital_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_hospital_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ig_expenditure` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_insur_trust_ctrb` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_interest_on_debt` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_iss_ffc` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_iss_ng` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_iss_unsp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_out_ffc` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_out_utility` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_ret_ffc` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_ret_ng` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_ltd_ret_unsp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_unemp_rev` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_util_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_util_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_util_inter_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `total_util_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `trans_util_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `trans_util_construct` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `trans_util_inter_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `trans_util_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `transit_sub_direct_sub` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `transit_sub_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `transit_sub_ig_to_sta` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `transit_sub_to_own_sys` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `transit_sub_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `transit_utility_rev` | 49.4% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `type_code` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_comp_bal_in_us_trs` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_comp_ben_paymts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_comp_cash_&_sec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_comp_other_balance` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_comp_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_ext_&_spec_pmts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_federal_advances` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_int_revenue` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `unemp_payroll_tax` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `vetbonus` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_trans_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_trans_construct` | 29.1% | 2007–2023 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_trans_direct_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_trans_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_trans_ig_to_sta` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_trans_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_util_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_util_inter_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `water_util_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `weight` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_cash_cash_assist` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_cash_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_cash_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_categ_cash_assist` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_categ_ig_loc_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_categ_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_categ_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_ins_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_ins_construction` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_ins_total_exp` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_nec_cap_outlay` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_nec_construction` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_nec_direct_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_nec_ig_local_govts` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_nec_ig_to_state` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_nec_total_expend` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_state_share_part_d` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_vend_pmts_medical` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `welf_vend_pmts_nec` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `year4` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `yearpop` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `zerodata` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `air_trans_curr_oper` | 21.9% | 2012–2023 | 198 |
| Fiscal TEL Merged 2007-2024 | `air_trans_fte` | 0.4% | 2012–2021 | 9 |
| Fiscal TEL Merged 2007-2024 | `air_trans_oth_cap` | 7.7% | 2012–2021 | 130 |
| Fiscal TEL Merged 2007-2024 | `air_trans_payroll` | 1.2% | 2012–2021 | 28 |
| Fiscal TEL Merged 2007-2024 | `bond_fund_cash_sec` | 43.7% | 2012–2021 | 525 |
| Fiscal TEL Merged 2007-2024 | `cen_staff_oth_cap` | 24.3% | 2012–2021 | 386 |
| Fiscal TEL Merged 2007-2024 | `central_staff_fte` | 0.4% | 2013–2021 | 9 |
| Fiscal TEL Merged 2007-2024 | `central_staff_payroll` | 2.3% | 2012–2021 | 42 |
| Fiscal TEL Merged 2007-2024 | `chg_higher_ed` | 0.5% | 2012–2023 | 5 |
| Fiscal TEL Merged 2007-2024 | `correct_constr_other` | 0.2% | 2012–2023 | 9 |
| Fiscal TEL Merged 2007-2024 | `correct_curr_oper` | 8.4% | 2012–2023 | 91 |
| Fiscal TEL Merged 2007-2024 | `correct_curr_other` | 3.5% | 2012–2023 | 47 |
| Fiscal TEL Merged 2007-2024 | `correct_oth_cap` | 2.1% | 2012–2021 | 51 |
| Fiscal TEL Merged 2007-2024 | `correct_oth_cap_other` | 0.7% | 2012–2021 | 19 |
| Fiscal TEL Merged 2007-2024 | `correction_fte` | 0.0% | 2015–2016 | 1 |
| Fiscal TEL Merged 2007-2024 | `correction_fte_other` | 0.1% | 2012–2020 | 3 |
| Fiscal TEL Merged 2007-2024 | `correction_payroll` | 3.1% | 2012–2021 | 50 |
| Fiscal TEL Merged 2007-2024 | `correction_payroll_oth` | 0.3% | 2012–2021 | 11 |
| Fiscal TEL Merged 2007-2024 | `elec_util_curr_oper` | 10.6% | 2012–2023 | 104 |
| Fiscal TEL Merged 2007-2024 | `elec_util_interest` | 7.4% | 2012–2023 | 79 |
| Fiscal TEL Merged 2007-2024 | `elec_util_oth_cap` | 3.7% | 2012–2021 | 68 |
| Fiscal TEL Merged 2007-2024 | `elec_util_payroll` | 0.3% | 2012–2021 | 12 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_assist_sub` | 0.3% | 2012–2023 | 3 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_curr_oper` | 8.5% | 2012–2023 | 87 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_fte` | 0.5% | 2012–2021 | 13 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_oth_cap` | 6.4% | 2012–2021 | 74 |
| Fiscal TEL Merged 2007-2024 | `elem_educ_payroll` | 6.7% | 2012–2021 | 98 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_contributions` | 0.1% | 2012–2023 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_from_state` | 0.0% | 2012–2015 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_interest` | 0.1% | 2012–2023 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_loc_contrib` | 0.0% | 2012–2012 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_loc_to_loc` | 0.1% | 2012–2023 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_ret_state_contrib` | 0.1% | 2013–2023 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_sec_construction` | 0.0% | 2022–2023 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_sec_curr_oper` | 0.1% | 2012–2023 | 1 |
| Fiscal TEL Merged 2007-2024 | `emp_sec_oth_cap` | 0.1% | 2012–2021 | 1 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_elec_util` | 1.1% | 2012–2021 | 32 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_gas_util` | 0.2% | 2012–2021 | 5 |
| Fiscal TEL Merged 2007-2024 | `fed_igr_water_util` | 4.5% | 2012–2021 | 121 |
| Fiscal TEL Merged 2007-2024 | `finan_adm_construction` | 7.1% | 2012–2023 | 187 |
| Fiscal TEL Merged 2007-2024 | `finan_adm_oth_cap` | 16.9% | 2012–2021 | 306 |
| Fiscal TEL Merged 2007-2024 | `financial_admin_fte` | 0.4% | 2012–2021 | 9 |
| Fiscal TEL Merged 2007-2024 | `financial_admin_payroll` | 2.9% | 2012–2021 | 52 |
| Fiscal TEL Merged 2007-2024 | `fire_prot_oth_cap` | 31.5% | 2012–2021 | 421 |
| Fiscal TEL Merged 2007-2024 | `fire_prot_payroll` | 1.6% | 2012–2021 | 52 |
| Fiscal TEL Merged 2007-2024 | `gas_util_curr_oper` | 3.3% | 2012–2023 | 39 |
| Fiscal TEL Merged 2007-2024 | `gas_util_fte` | 0.2% | 2012–2021 | 3 |
| Fiscal TEL Merged 2007-2024 | `gas_util_interest` | 2.0% | 2012–2023 | 21 |
| Fiscal TEL Merged 2007-2024 | `gas_util_oth_cap` | 1.0% | 2012–2021 | 19 |
| Fiscal TEL Merged 2007-2024 | `gas_util_payroll` | 0.1% | 2012–2020 | 5 |
| Fiscal TEL Merged 2007-2024 | `gen_bldg_construction` | 19.1% | 2012–2023 | 296 |
| Fiscal TEL Merged 2007-2024 | `gen_bldg_curr_oper` | 39.5% | 2012–2023 | 397 |
| Fiscal TEL Merged 2007-2024 | `gen_bldg_oth_cap` | 13.8% | 2012–2021 | 249 |
| Fiscal TEL Merged 2007-2024 | `health_curr_oper` | 44.8% | 2012–2023 | 440 |
| Fiscal TEL Merged 2007-2024 | `health_fte` | 0.4% | 2012–2021 | 10 |
| Fiscal TEL Merged 2007-2024 | `health_oth_cap` | 10.6% | 2012–2021 | 200 |
| Fiscal TEL Merged 2007-2024 | `health_payroll` | 4.6% | 2012–2021 | 93 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_curr_oper` | 0.5% | 2012–2023 | 5 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_fte` | 0.1% | 2012–2019 | 3 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_oth_cap` | 0.2% | 2012–2021 | 2 |
| Fiscal TEL Merged 2007-2024 | `higher_ed_payroll` | 0.2% | 2012–2018 | 9 |
| Fiscal TEL Merged 2007-2024 | `highways_fte` | 2.1% | 2012–2021 | 49 |
| Fiscal TEL Merged 2007-2024 | `highways_payroll` | 2.4% | 2012–2021 | 68 |
| Fiscal TEL Merged 2007-2024 | `hospitals_construction` | 1.4% | 2012–2023 | 13 |
| Fiscal TEL Merged 2007-2024 | `hospitals_curr_oper` | 1.7% | 2012–2023 | 23 |
| Fiscal TEL Merged 2007-2024 | `hospitals_fte` | 0.1% | 2012–2021 | 3 |
| Fiscal TEL Merged 2007-2024 | `hospitals_oth_cap` | 0.9% | 2012–2021 | 11 |
| Fiscal TEL Merged 2007-2024 | `hospitals_payroll` | 0.1% | 2012–2021 | 2 |
| Fiscal TEL Merged 2007-2024 | `hous_com_dev_construct` | 32.4% | 2012–2023 | 401 |
| Fiscal TEL Merged 2007-2024 | `hous_com_dev_oth_cap` | 18.2% | 2012–2021 | 333 |
| Fiscal TEL Merged 2007-2024 | `housing_fte` | 0.4% | 2012–2021 | 18 |
| Fiscal TEL Merged 2007-2024 | `housing_payroll` | 3.1% | 2012–2021 | 88 |
| Fiscal TEL Merged 2007-2024 | `ins_benefit_payments` | 0.1% | 2022–2023 | 7 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_air_trans` | 9.2% | 2012–2016 | 231 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_corrections` | 6.6% | 2012–2016 | 226 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_education` | 10.8% | 2012–2016 | 283 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_elem_ed` | 11.1% | 2012–2016 | 284 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_gen_support` | 8.1% | 2012–2016 | 234 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_health_hosp` | 0.4% | 2012–2016 | 19 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_higher_ed` | 8.6% | 2012–2016 | 244 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_highways` | 9.8% | 2012–2016 | 261 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_housing` | 7.2% | 2012–2016 | 212 |
| Fiscal TEL Merged 2007-2024 | `ins_trust_other_ed` | 10.6% | 2012–2016 | 278 |
| Fiscal TEL Merged 2007-2024 | `judicial_fte` | 0.6% | 2012–2021 | 16 |
| Fiscal TEL Merged 2007-2024 | `judicial_oth_cap` | 11.7% | 2012–2021 | 218 |
| Fiscal TEL Merged 2007-2024 | `judicial_payroll` | 1.5% | 2012–2021 | 44 |
| Fiscal TEL Merged 2007-2024 | `libraries_curr_oper` | 38.6% | 2012–2023 | 354 |
| Fiscal TEL Merged 2007-2024 | `libraries_fte` | 0.2% | 2012–2021 | 5 |
| Fiscal TEL Merged 2007-2024 | `libraries_oth_cap` | 12.9% | 2012–2021 | 211 |
| Fiscal TEL Merged 2007-2024 | `libraries_payroll` | 1.1% | 2012–2021 | 27 |
| Fiscal TEL Merged 2007-2024 | `liq_str_construction` | 0.0% | 2022–2023 | 2 |
| Fiscal TEL Merged 2007-2024 | `liq_str_curr_oper` | 1.1% | 2012–2023 | 10 |
| Fiscal TEL Merged 2007-2024 | `liq_str_oth_cap` | 0.2% | 2012–2021 | 4 |
| Fiscal TEL Merged 2007-2024 | `local_igr_elec_util` | 0.6% | 2012–2021 | 17 |
| Fiscal TEL Merged 2007-2024 | `local_igr_gas_util` | 0.0% | 2013–2014 | 1 |
| Fiscal TEL Merged 2007-2024 | `local_igr_water_util` | 2.4% | 2012–2021 | 71 |
| Fiscal TEL Merged 2007-2024 | `ltd_beg_pdpp` | 22.2% | 2012–2021 | 288 |
| Fiscal TEL Merged 2007-2024 | `ltd_issued_pdpp` | 3.6% | 2012–2021 | 108 |
| Fiscal TEL Merged 2007-2024 | `ltd_outstanding_pdpp` | 21.5% | 2012–2021 | 282 |
| Fiscal TEL Merged 2007-2024 | `ltd_retired_pdpp` | 18.6% | 2012–2021 | 260 |
| Fiscal TEL Merged 2007-2024 | `misc_com_curr_oper` | 16.4% | 2012–2023 | 192 |
| Fiscal TEL Merged 2007-2024 | `misc_com_oth_cap` | 4.2% | 2012–2021 | 92 |
| Fiscal TEL Merged 2007-2024 | `nat_res_construction` | 8.1% | 2012–2023 | 167 |
| Fiscal TEL Merged 2007-2024 | `nat_res_curr_oper` | 21.7% | 2012–2023 | 268 |
| Fiscal TEL Merged 2007-2024 | `nat_res_oth_cap` | 7.2% | 2012–2021 | 147 |
| Fiscal TEL Merged 2007-2024 | `nat_res_payroll` | 1.0% | 2012–2021 | 32 |
| Fiscal TEL Merged 2007-2024 | `natural_resources_fte` | 0.2% | 2013–2020 | 6 |
| Fiscal TEL Merged 2007-2024 | `other_benefit_payments` | 9.2% | 2012–2016 | 235 |
| Fiscal TEL Merged 2007-2024 | `other_gen_construction` | 46.2% | 2012–2023 | 522 |
| Fiscal TEL Merged 2007-2024 | `other_gen_fte` | 6.4% | 2012–2023 | 133 |
| Fiscal TEL Merged 2007-2024 | `other_gen_oth_cap` | 36.4% | 2012–2021 | 483 |
| Fiscal TEL Merged 2007-2024 | `other_gen_payroll` | 15.5% | 2012–2023 | 328 |
| Fiscal TEL Merged 2007-2024 | `parking_curr_oper` | 30.2% | 2012–2023 | 299 |
| Fiscal TEL Merged 2007-2024 | `parking_oth_cap` | 7.5% | 2012–2021 | 154 |
| Fiscal TEL Merged 2007-2024 | `parking_payroll` | 0.2% | 2012–2021 | 12 |
| Fiscal TEL Merged 2007-2024 | `parks_rec_construction` | 48.4% | 2012–2023 | 507 |
| Fiscal TEL Merged 2007-2024 | `parks_rec_fte` | 0.3% | 2012–2021 | 13 |
| Fiscal TEL Merged 2007-2024 | `parks_rec_oth_cap` | 33.7% | 2012–2021 | 443 |
| Fiscal TEL Merged 2007-2024 | `parks_rec_payroll` | 2.0% | 2012–2021 | 53 |
| Fiscal TEL Merged 2007-2024 | `pension_benefit_payments` | 9.6% | 2012–2016 | 259 |
| Fiscal TEL Merged 2007-2024 | `police_fte` | 0.7% | 2012–2021 | 22 |
| Fiscal TEL Merged 2007-2024 | `police_payroll` | 4.0% | 2012–2021 | 94 |
| Fiscal TEL Merged 2007-2024 | `police_prot_oth_cap` | 36.3% | 2012–2021 | 461 |
| Fiscal TEL Merged 2007-2024 | `prot_insp_oth_cap` | 11.3% | 2012–2021 | 209 |
| Fiscal TEL Merged 2007-2024 | `protective_insp_fte` | 0.0% | 2012–2018 | 4 |
| Fiscal TEL Merged 2007-2024 | `protective_insp_payroll` | 0.3% | 2012–2021 | 7 |
| Fiscal TEL Merged 2007-2024 | `public_welf_fte` | 0.1% | 2012–2021 | 2 |
| Fiscal TEL Merged 2007-2024 | `reg_hwy_oth_cap` | 29.9% | 2012–2021 | 415 |
| Fiscal TEL Merged 2007-2024 | `royalties` | 4.8% | 2012–2023 | 68 |
| Fiscal TEL Merged 2007-2024 | `sewerage_fte` | 1.5% | 2012–2021 | 30 |
| Fiscal TEL Merged 2007-2024 | `sewerage_oth_cap` | 22.2% | 2012–2021 | 360 |
| Fiscal TEL Merged 2007-2024 | `sewerage_payroll` | 3.9% | 2012–2021 | 81 |
| Fiscal TEL Merged 2007-2024 | `sinking_fund_cash_sec` | 43.3% | 2012–2021 | 506 |
| Fiscal TEL Merged 2007-2024 | `solid_waste_fte` | 0.1% | 2012–2021 | 4 |
| Fiscal TEL Merged 2007-2024 | `solid_waste_payroll` | 1.4% | 2012–2021 | 38 |
| Fiscal TEL Merged 2007-2024 | `solid_wst_construction` | 16.8% | 2012–2023 | 267 |
| Fiscal TEL Merged 2007-2024 | `solid_wst_oth_cap` | 17.0% | 2012–2021 | 283 |
| Fiscal TEL Merged 2007-2024 | `state_igr_elec_util` | 1.4% | 2012–2021 | 32 |
| Fiscal TEL Merged 2007-2024 | `state_igr_gas_util` | 0.2% | 2012–2021 | 7 |
| Fiscal TEL Merged 2007-2024 | `state_igr_water_util` | 8.5% | 2012–2021 | 202 |
| Fiscal TEL Merged 2007-2024 | `std_beg_outstanding` | 11.6% | 2012–2023 | 180 |
| Fiscal TEL Merged 2007-2024 | `std_end_outstanding` | 11.4% | 2012–2023 | 172 |
| Fiscal TEL Merged 2007-2024 | `toll_hwy_curr_oper` | 0.9% | 2012–2023 | 12 |
| Fiscal TEL Merged 2007-2024 | `toll_hwy_oth_cap` | 0.5% | 2012–2021 | 10 |
| Fiscal TEL Merged 2007-2024 | `transit_construction` | 10.6% | 2012–2023 | 164 |
| Fiscal TEL Merged 2007-2024 | `transit_curr_oper` | 25.0% | 2012–2023 | 256 |
| Fiscal TEL Merged 2007-2024 | `transit_fte` | 2.1% | 2012–2021 | 27 |
| Fiscal TEL Merged 2007-2024 | `transit_interest` | 2.0% | 2012–2023 | 46 |
| Fiscal TEL Merged 2007-2024 | `transit_oth_cap` | 9.0% | 2012–2021 | 153 |
| Fiscal TEL Merged 2007-2024 | `transit_payroll` | 3.0% | 2012–2021 | 63 |
| Fiscal TEL Merged 2007-2024 | `unemployment_benefits` | 0.7% | 2012–2021 | 13 |
| Fiscal TEL Merged 2007-2024 | `vendor_cash_med` | 0.5% | 2012–2021 | 13 |
| Fiscal TEL Merged 2007-2024 | `vendor_cash_nec` | 1.4% | 2012–2021 | 27 |
| Fiscal TEL Merged 2007-2024 | `water_trans_curr_oper` | 3.8% | 2012–2023 | 54 |
| Fiscal TEL Merged 2007-2024 | `water_trans_fte` | 0.1% | 2017–2020 | 3 |
| Fiscal TEL Merged 2007-2024 | `water_trans_oth_cap` | 0.4% | 2012–2021 | 10 |
| Fiscal TEL Merged 2007-2024 | `water_trans_payroll` | 0.1% | 2012–2021 | 3 |
| Fiscal TEL Merged 2007-2024 | `water_util_fte` | 1.1% | 2012–2021 | 27 |
| Fiscal TEL Merged 2007-2024 | `water_util_interest` | 42.5% | 2012–2023 | 410 |
| Fiscal TEL Merged 2007-2024 | `water_util_oth_cap` | 22.2% | 2012–2021 | 334 |
| Fiscal TEL Merged 2007-2024 | `water_util_payroll` | 2.7% | 2012–2021 | 75 |
| Fiscal TEL Merged 2007-2024 | `welfare_inst_construct` | 0.2% | 2017–2023 | 11 |
| Fiscal TEL Merged 2007-2024 | `welfare_inst_curr_opr` | 0.7% | 2012–2023 | 26 |
| Fiscal TEL Merged 2007-2024 | `welfare_inst_oth_cap` | 0.1% | 2012–2020 | 3 |
| Fiscal TEL Merged 2007-2024 | `welfare_nec_construct` | 2.0% | 2012–2023 | 59 |
| Fiscal TEL Merged 2007-2024 | `welfare_nec_curr_oper` | 18.0% | 2012–2023 | 231 |
| Fiscal TEL Merged 2007-2024 | `welfare_nec_fte` | 0.2% | 2012–2021 | 8 |
| Fiscal TEL Merged 2007-2024 | `welfare_nec_oth_cap` | 2.6% | 2012–2021 | 73 |
| Fiscal TEL Merged 2007-2024 | `welfare_nec_payroll` | 0.9% | 2012–2021 | 21 |
| Fiscal TEL Merged 2007-2024 | `workers_comp_benefits` | 1.3% | 2012–2021 | 27 |
| Fiscal TEL Merged 2007-2024 | `fog_change_year` | 1.0% | 2007–2024 | 6 |
| Fiscal TEL Merged 2007-2024 | `partisan_change_year` | 0.3% | 2007–2024 | 3 |
| Fiscal TEL Merged 2007-2024 | `termlimits_change_year` | 0.3% | 2007–2024 | 2 |
| Fiscal TEL Merged 2007-2024 | `termlength_change_year` | 0.5% | 2007–2024 | 3 |
| Fiscal TEL Merged 2007-2024 | `districts_change_year` | 1.2% | 2007–2024 | 9 |
| Fiscal TEL Merged 2007-2024 | `notes` | 2.9% | 2007–2024 | 20 |
| Fiscal TEL Merged 2007-2024 | `pension_expenditure_burden` | 40.9% | 2007–2016 | 547 |
| Fiscal TEL Merged 2007-2024 | `go_bond_share_outstanding` | 33.2% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `go_bond_share_issuance` | 26.5% | 2007–2012 | 538 |
| Fiscal TEL Merged 2007-2024 | `ig_exp_share` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `revenue_bonds_outstanding` | 33.3% | 2007–2012 | 547 |
| Fiscal TEL Merged 2007-2024 | `pension_exp_own_source` | 40.9% | 2007–2016 | 547 |
| Fiscal TEL Merged 2013-2025 | `relevant_counties` | 15.4% | 2013–2024 | 88 |
| Fiscal TEL Merged 2013-2025 | `recommended_approach` | 15.4% | 2013–2024 | 88 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Number of Events` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Annualized Frequency` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Exposure - Impacted Area (sq mi)` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Exposure - Building Value` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Exposure - Population` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Exposure - Population Equivalence` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Exposure - Total` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Historic Loss Ratio - Buildings` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Historic Loss Ratio - Population` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss - Building Value` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss - Population` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss - Population Equivalence` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss - Total` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss Score` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss Rate - Building` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss Rate - Population` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Expected Annual Loss Rate - National Percentile` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Hazard Type Risk Index Value` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Avalanche - Hazard Type Risk Index Score` | 32.9% | 2013–2024 | 185 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Annualized Frequency` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Exposure - Impacted Area (sq mi)` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Exposure - Building Value` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Exposure - Population` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Exposure - Population Equivalence` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Exposure - Total` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Historic Loss Ratio - Buildings` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Historic Loss Ratio - Population` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss - Building Value` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss - Population` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss - Population Equivalence` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss - Total` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss Score` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss Rate - Building` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss Rate - Population` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Expected Annual Loss Rate - National Percentile` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Hazard Type Risk Index Value` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Coastal Flooding - Hazard Type Risk Index Score` | 46.5% | 2013–2024 | 264 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Number of Events` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Annualized Frequency` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Exposure - Impacted Area (sq mi)` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Exposure - Building Value` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Exposure - Population` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Exposure - Population Equivalence` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Exposure - Total` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Historic Loss Ratio - Buildings` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Historic Loss Ratio - Population` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss - Building Value` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss - Population` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss - Population Equivalence` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss - Total` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss Score` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss Rate - Building` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss Rate - Population` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Expected Annual Loss Rate - National Percentile` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Hazard Type Risk Index Value` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Tsunami - Hazard Type Risk Index Score` | 14.0% | 2013–2024 | 81 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Number of Events` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Annualized Frequency` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Exposure - Impacted Area (sq mi)` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Exposure - Building Value` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Exposure - Population` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Exposure - Population Equivalence` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Exposure - Total` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Historic Loss Ratio - Buildings` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Historic Loss Ratio - Population` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss - Building Value` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss - Population` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss - Population Equivalence` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss - Total` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss Score` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss Rate - Building` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss Rate - Population` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Expected Annual Loss Rate - National Percentile` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Hazard Type Risk Index Value` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `Volcanic Activity - Hazard Type Risk Index Score` | 21.3% | 2013–2024 | 123 |
| Fiscal TEL Merged 2013-2025 | `exp` | 33.0% | 2021–2024 | 542 |
| Fiscal TEL Merged 2013-2025 | `generaterenewable` | 24.7% | 2022–2024 | 542 |
| Fiscal TEL Merged 2013-2025 | `priority` | 41.2% | 2020–2024 | 542 |
| Fiscal TEL Merged 2013-2025 | `avg_sufficiency` | 48.9% | 2013–2018 | 540 |
| Fiscal TEL Merged 2013-2025 | `srf_strict_count` | 5.3% | 2013–2024 | 163 |
| Fiscal TEL Merged 2013-2025 | `srf_strict_amount` | 5.3% | 2013–2024 | 163 |
| Fiscal TEL Merged 2013-2025 | `srf_incl_count` | 8.0% | 2013–2024 | 207 |
| Fiscal TEL Merged 2013-2025 | `srf_incl_amount` | 8.0% | 2013–2024 | 207 |
| Fiscal TEL Merged 2013-2025 | `srf_strict_amount_real` | 5.3% | 2013–2024 | 163 |
| Fiscal TEL Merged 2013-2025 | `srf_incl_amount_real` | 8.0% | 2013–2024 | 207 |
| Fiscal TEL Merged 2013-2025 | `ELC_total_lag1` | 48.9% | 2013–2022 | 348 |
| Fiscal TEL Merged 2013-2025 | `log_ELC_total_lag1` | 48.9% | 2013–2022 | 348 |
| Fiscal TEL Merged 2013-2025 | `ELC_share_lag1` | 48.9% | 2013–2022 | 348 |
| Fiscal TEL Merged 2013-2025 | `delta_log_flight_3yr_lag3` | 49.2% | 2016–2024 | 382 |
| Fiscal TEL Merged 2013-2025 | `log_flight_ma3_lag4` | 49.6% | 2016–2024 | 383 |
| Fiscal TEL Merged 2013-2025 | `facility_count_ma3_lag4` | 49.6% | 2016–2024 | 383 |
| Fiscal TEL Merged 2013-2025 | `delta_log_flight_3yr_lag4` | 43.8% | 2017–2024 | 378 |
| Fiscal TEL Merged 2013-2025 | `fiscal_19T` | 26.3% | 2013–2021 | 274 |
| Fiscal TEL Merged 2013-2025 | `fiscal_24T` | 3.4% | 2013–2021 | 89 |
| Fiscal TEL Merged 2013-2025 | `fiscal_34T` | 21.2% | 2013–2021 | 241 |
| Fiscal TEL Merged 2013-2025 | `fiscal_44T` | 25.6% | 2013–2021 | 267 |
| Fiscal TEL Merged 2013-2025 | `fiscal_61V` | 12.5% | 2013–2023 | 169 |
| Fiscal TEL Merged 2013-2025 | `fiscal_64V` | 12.2% | 2013–2023 | 157 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A01` | 26.2% | 2013–2023 | 181 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A03` | 23.8% | 2013–2023 | 200 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A09` | 9.4% | 2013–2023 | 63 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A10` | 6.3% | 2013–2023 | 54 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A12` | 9.1% | 2013–2023 | 67 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A16` | 0.3% | 2013–2023 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A18` | 0.7% | 2013–2023 | 5 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A36` | 2.0% | 2013–2023 | 21 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A44` | 27.9% | 2013–2023 | 291 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A45` | 1.1% | 2013–2023 | 8 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A50` | 26.7% | 2013–2023 | 277 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A59` | 10.5% | 2013–2023 | 115 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A60` | 42.3% | 2013–2023 | 312 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A87` | 4.5% | 2013–2023 | 46 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A90` | 1.5% | 2013–2023 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A92` | 13.2% | 2013–2023 | 99 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A93` | 4.4% | 2013–2023 | 37 |
| Fiscal TEL Merged 2013-2025 | `fiscal_A94` | 24.1% | 2013–2023 | 194 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B01` | 14.0% | 2013–2021 | 146 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B21` | 5.7% | 2013–2021 | 64 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B22` | 0.0% | 2013–2015 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B30` | 5.7% | 2013–2021 | 113 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B42` | 6.6% | 2013–2021 | 139 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B46` | 14.8% | 2013–2021 | 270 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B59` | 2.3% | 2013–2021 | 50 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B79` | 6.7% | 2013–2021 | 114 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B80` | 3.7% | 2013–2021 | 95 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B91` | 4.6% | 2013–2021 | 105 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B92` | 1.2% | 2013–2021 | 28 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B93` | 0.2% | 2013–2021 | 5 |
| Fiscal TEL Merged 2013-2025 | `fiscal_B94` | 12.9% | 2013–2021 | 160 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C21` | 9.2% | 2013–2021 | 85 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C42` | 13.9% | 2013–2021 | 165 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C50` | 20.3% | 2013–2021 | 281 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C79` | 10.9% | 2013–2021 | 143 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C80` | 9.8% | 2013–2021 | 180 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C91` | 8.6% | 2013–2021 | 180 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C92` | 1.4% | 2013–2021 | 31 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C93` | 0.3% | 2013–2021 | 4 |
| Fiscal TEL Merged 2013-2025 | `fiscal_C94` | 12.1% | 2013–2021 | 153 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D21` | 6.2% | 2013–2021 | 63 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D30` | 16.6% | 2013–2021 | 190 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D42` | 3.4% | 2013–2021 | 59 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D46` | 13.9% | 2013–2021 | 198 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D50` | 7.0% | 2013–2021 | 135 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D79` | 2.8% | 2013–2021 | 49 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D80` | 3.9% | 2013–2021 | 70 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D91` | 2.7% | 2013–2021 | 68 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D92` | 0.6% | 2013–2021 | 16 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D93` | 0.0% | 2013–2014 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_D94` | 4.3% | 2013–2021 | 80 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E01` | 28.0% | 2013–2023 | 192 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E03` | 20.4% | 2013–2023 | 181 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E04` | 10.1% | 2013–2023 | 79 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E05` | 4.1% | 2013–2023 | 45 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E12` | 11.2% | 2013–2023 | 85 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E16` | 0.4% | 2013–2023 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E18` | 0.7% | 2013–2023 | 5 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E22` | 0.2% | 2013–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E36` | 2.0% | 2013–2023 | 21 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E45` | 1.3% | 2013–2023 | 12 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E52` | 47.6% | 2013–2023 | 346 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E59` | 26.0% | 2013–2023 | 250 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E60` | 38.1% | 2013–2023 | 286 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E74` | 0.6% | 2013–2021 | 12 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E75` | 1.8% | 2013–2021 | 23 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E77` | 1.0% | 2013–2023 | 24 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E79` | 21.8% | 2013–2023 | 218 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E87` | 4.7% | 2013–2023 | 51 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E90` | 1.5% | 2013–2023 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E92` | 13.7% | 2013–2023 | 102 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E93` | 4.3% | 2013–2023 | 37 |
| Fiscal TEL Merged 2013-2025 | `fiscal_E94` | 30.1% | 2013–2023 | 249 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F01` | 17.9% | 2013–2023 | 161 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F03` | 2.8% | 2013–2023 | 77 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F04` | 1.8% | 2013–2023 | 31 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F05` | 0.2% | 2013–2023 | 6 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F12` | 8.2% | 2013–2023 | 70 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F18` | 0.3% | 2013–2023 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F22` | 0.0% | 2022–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F23` | 7.3% | 2013–2023 | 179 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F24` | 26.6% | 2013–2023 | 392 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F25` | 5.3% | 2013–2023 | 133 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F29` | 16.8% | 2013–2023 | 309 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F31` | 20.8% | 2013–2023 | 277 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F32` | 8.2% | 2013–2023 | 170 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F36` | 1.4% | 2013–2023 | 12 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F45` | 0.7% | 2013–2023 | 11 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F50` | 31.1% | 2013–2023 | 384 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F52` | 12.4% | 2013–2023 | 218 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F59` | 8.8% | 2013–2023 | 159 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F60` | 10.0% | 2013–2023 | 155 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F62` | 30.9% | 2013–2023 | 457 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F66` | 5.2% | 2013–2023 | 162 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F77` | 0.2% | 2019–2023 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F79` | 2.1% | 2013–2023 | 52 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F80` | 48.6% | 2013–2023 | 442 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F81` | 17.0% | 2013–2023 | 256 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F87` | 1.9% | 2013–2023 | 27 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F89` | 49.5% | 2013–2023 | 513 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F90` | 0.0% | 2022–2023 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F91` | 46.3% | 2013–2023 | 410 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F92` | 9.1% | 2013–2023 | 83 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F93` | 3.0% | 2013–2023 | 27 |
| Fiscal TEL Merged 2013-2025 | `fiscal_F94` | 10.0% | 2013–2023 | 155 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G01` | 8.2% | 2013–2021 | 121 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G03` | 4.5% | 2013–2021 | 84 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G04` | 2.0% | 2013–2021 | 40 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G05` | 0.5% | 2013–2021 | 15 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G12` | 8.2% | 2013–2021 | 72 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G18` | 0.2% | 2013–2021 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G22` | 0.1% | 2013–2021 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G23` | 17.7% | 2013–2021 | 283 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G24` | 35.6% | 2013–2021 | 399 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G25` | 12.6% | 2013–2021 | 202 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G29` | 26.0% | 2013–2021 | 366 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G31` | 14.5% | 2013–2021 | 231 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G32` | 10.5% | 2013–2021 | 181 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G36` | 1.0% | 2013–2021 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G44` | 33.2% | 2013–2021 | 394 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G45` | 0.6% | 2013–2021 | 9 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G50` | 18.3% | 2013–2021 | 308 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G52` | 13.8% | 2013–2021 | 199 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G59` | 7.6% | 2013–2021 | 133 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G60` | 7.8% | 2013–2021 | 142 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G61` | 37.8% | 2013–2021 | 429 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G62` | 41.2% | 2013–2021 | 439 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G66` | 11.4% | 2013–2021 | 199 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G77` | 0.0% | 2014–2020 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G79` | 2.6% | 2013–2021 | 64 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G80` | 23.6% | 2013–2021 | 336 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G81` | 18.3% | 2013–2021 | 268 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G87` | 0.4% | 2013–2021 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G89` | 39.7% | 2013–2021 | 465 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G90` | 0.2% | 2013–2021 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G91` | 24.8% | 2013–2021 | 322 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G92` | 4.1% | 2013–2021 | 62 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G93` | 1.2% | 2013–2021 | 19 |
| Fiscal TEL Merged 2013-2025 | `fiscal_G94` | 9.7% | 2013–2021 | 143 |
| Fiscal TEL Merged 2013-2025 | `fiscal_I92` | 9.3% | 2013–2023 | 77 |
| Fiscal TEL Merged 2013-2025 | `fiscal_I93` | 2.5% | 2013–2023 | 19 |
| Fiscal TEL Merged 2013-2025 | `fiscal_I94` | 2.3% | 2013–2023 | 42 |
| Fiscal TEL Merged 2013-2025 | `fiscal_J19` | 0.2% | 2022–2023 | 7 |
| Fiscal TEL Merged 2013-2025 | `fiscal_J67` | 0.9% | 2013–2021 | 11 |
| Fiscal TEL Merged 2013-2025 | `fiscal_J68` | 1.7% | 2013–2021 | 24 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L01` | 0.4% | 2013–2021 | 8 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L04` | 0.0% | 2015–2016 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L05` | 0.1% | 2013–2020 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L12` | 0.6% | 2013–2021 | 13 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L18` | 0.1% | 2013–2019 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L23` | 0.4% | 2013–2021 | 9 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L25` | 0.6% | 2013–2021 | 15 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L29` | 0.5% | 2013–2021 | 9 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L32` | 0.4% | 2013–2021 | 9 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L36` | 0.1% | 2013–2021 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L44` | 2.5% | 2013–2021 | 42 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L50` | 0.4% | 2013–2021 | 17 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L52` | 0.2% | 2013–2021 | 4 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L59` | 0.2% | 2013–2020 | 6 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L61` | 0.4% | 2013–2021 | 11 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L62` | 0.7% | 2013–2021 | 19 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L66` | 0.1% | 2016–2018 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L67` | 0.2% | 2013–2021 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L79` | 0.2% | 2013–2021 | 6 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L80` | 1.9% | 2013–2021 | 29 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L81` | 0.2% | 2014–2021 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L87` | 0.1% | 2017–2020 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L89` | 7.3% | 2013–2023 | 130 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L91` | 1.5% | 2013–2021 | 27 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L93` | 0.2% | 2013–2021 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_L94` | 2.8% | 2013–2021 | 27 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M01` | 1.4% | 2013–2021 | 26 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M04` | 4.1% | 2013–2021 | 47 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M05` | 0.4% | 2013–2021 | 9 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M12` | 8.6% | 2013–2021 | 91 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M18` | 0.2% | 2013–2018 | 7 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M23` | 3.4% | 2013–2021 | 50 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M24` | 1.7% | 2013–2021 | 45 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M25` | 2.0% | 2013–2021 | 42 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M29` | 2.9% | 2013–2021 | 40 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M32` | 5.8% | 2013–2021 | 87 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M36` | 0.2% | 2013–2021 | 2 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M44` | 2.8% | 2013–2021 | 64 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M50` | 3.6% | 2013–2021 | 82 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M52` | 1.3% | 2013–2021 | 24 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M59` | 1.0% | 2013–2021 | 31 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M60` | 0.3% | 2013–2021 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M61` | 2.2% | 2013–2021 | 46 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M62` | 4.3% | 2013–2021 | 88 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M66` | 0.3% | 2013–2021 | 6 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M79` | 1.1% | 2013–2021 | 18 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M80` | 4.8% | 2013–2021 | 75 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M81` | 1.6% | 2013–2021 | 34 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M87` | 0.2% | 2013–2021 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M89` | 16.2% | 2013–2023 | 317 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M91` | 3.0% | 2013–2021 | 70 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M92` | 0.4% | 2013–2021 | 10 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M93` | 0.1% | 2013–2020 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_M94` | 3.9% | 2013–2021 | 60 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T09` | 46.7% | 2013–2023 | 349 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T10` | 7.0% | 2013–2023 | 55 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T11` | 12.2% | 2013–2023 | 90 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T12` | 4.1% | 2013–2023 | 35 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T13` | 6.0% | 2013–2023 | 50 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T14` | 1.2% | 2013–2023 | 13 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T16` | 4.6% | 2013–2023 | 35 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T20` | 19.2% | 2013–2023 | 156 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T21` | 7.0% | 2013–2023 | 69 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T22` | 0.3% | 2013–2023 | 3 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T24` | 12.3% | 2013–2023 | 113 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T25` | 0.6% | 2013–2023 | 5 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T27` | 4.9% | 2013–2023 | 54 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T40` | 7.9% | 2013–2023 | 56 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T41` | 2.1% | 2013–2023 | 16 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T50` | 0.9% | 2013–2023 | 16 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T51` | 16.5% | 2013–2023 | 161 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T53` | 0.6% | 2013–2023 | 11 |
| Fiscal TEL Merged 2013-2025 | `fiscal_T99` | 13.3% | 2013–2023 | 179 |
| Fiscal TEL Merged 2013-2025 | `fiscal_U01` | 46.7% | 2013–2023 | 412 |
| Fiscal TEL Merged 2013-2025 | `fiscal_U41` | 5.5% | 2013–2023 | 64 |
| Fiscal TEL Merged 2013-2025 | `fiscal_U95` | 0.2% | 2013–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X01` | 10.3% | 2013–2016 | 212 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X05` | 7.0% | 2013–2016 | 192 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X08` | 12.4% | 2013–2016 | 258 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X11` | 12.5% | 2013–2016 | 260 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X12` | 9.5% | 2013–2016 | 224 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X21` | 12.0% | 2013–2016 | 256 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X30` | 8.5% | 2013–2016 | 203 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X42` | 0.4% | 2013–2016 | 14 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X44` | 11.2% | 2013–2016 | 242 |
| Fiscal TEL Merged 2013-2025 | `fiscal_X47` | 7.7% | 2013–2016 | 193 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Y01` | 0.2% | 2013–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Y02` | 0.2% | 2013–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Y05` | 0.2% | 2013–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Y06` | 0.0% | 2013–2015 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Y07` | 0.2% | 2013–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Y08` | 0.0% | 2019–2023 | 1 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Z77` | 10.8% | 2013–2016 | 239 |
| Fiscal TEL Merged 2013-2025 | `fiscal_Z78` | 10.2% | 2013–2016 | 215 |
| ACS Additional | `opinion_priority` | 33.3% | 2020–2024 | — |
| ACS Additional | `opinion_generaterenewable` | 20.0% | 2022–2024 | — |
| ACS Additional | `opinion_reducetax` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_congress` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_governor` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_localofficials` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_citizens` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_corporations` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_affectweather` | 46.7% | 2018–2024 | — |
| ACS Additional | `opinion_exp` | 26.7% | 2021–2024 | — |
| EPA Enforcement | `case_conclusions_unique_muni` | 1.4% | 2000–2023 | 131 |
| EPA Enforcement | `case_milestones_unique_muni` | 6.4% | 2000–2025 | 262 |
| EPA Enforcement | `case_penalty_total_muni` | 4.2% | 2000–2026 | 259 |
| EPA Enforcement | `case_conclusions_unique_locgov` | 2.0% | 2000–2025 | 164 |
| EPA Enforcement | `case_milestones_unique_locgov` | 8.0% | 2000–2025 | 301 |
| EPA Enforcement | `case_penalty_total_locgov` | 5.0% | 2000–2026 | 298 |
| EPA Enforcement | `case_conclusions_unique_private` | 12.5% | 2000–2025 | 458 |
| EPA Enforcement | `case_milestones_unique_private` | 43.0% | 2000–2025 | 529 |
| EPA Enforcement | `case_penalty_total_private` | 34.5% | 2000–2026 | 528 |
| Vulcan CO2 | `ELC_total_lag1` | 49.1% | 2013–2022 | — |
| Vulcan CO2 | `log_ELC_total_lag1` | 49.1% | 2013–2022 | — |
| Vulcan CO2 | `ELC_share_lag1` | 49.1% | 2013–2022 | — |
| Vulcan CO2 | `delta_log_flight_3yr_lag4` | 44.5% | 2017–2024 | — |
| FEMA NRI | `Volcanic Activity - Exposure - Impacted Area (sq mi)` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Coastal Flooding - Exposure - Population` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Volcanic Activity - Historic Loss Ratio - Buildings` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss - Building Value` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Tsunami - Hazard Type Risk Index Value` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss Rate - National Percentile` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Tsunami - Expected Annual Loss Rate - Population` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Annualized Frequency` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Avalanche - Exposure - Impacted Area (sq mi)` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Tsunami - Exposure - Population Equivalence` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Tsunami - Historic Loss Ratio - Population` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Avalanche - Hazard Type Risk Index Value` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Hazard Type Risk Index Value` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss - Total` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Coastal Flooding - Historic Loss Ratio - Population` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss Rate - National Percentile` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Avalanche - Exposure - Population` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Coastal Flooding - Exposure - Total` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Coastal Flooding - Exposure - Building Value` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss - Population Equivalence` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss Rate - Building` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Tsunami - Expected Annual Loss - Building Value` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Tsunami - Exposure - Impacted Area (sq mi)` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Tsunami - Expected Annual Loss Rate - National Percentile` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Avalanche - Exposure - Total` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Avalanche - Expected Annual Loss - Population Equivalence` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Coastal Flooding - Exposure - Impacted Area (sq mi)` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Tsunami - Hazard Type Risk Index Score` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Exposure - Population Equivalence` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Avalanche - Exposure - Building Value` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Tsunami - Expected Annual Loss Rate - Building` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Avalanche - Historic Loss Ratio - Buildings` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Number of Events` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Tsunami - Expected Annual Loss - Population` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss - Population` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Tsunami - Historic Loss Ratio - Buildings` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Tsunami - Annualized Frequency` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Avalanche - Expected Annual Loss Rate - Building` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Avalanche - Expected Annual Loss Score` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Exposure - Total` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss Rate - Building` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Tsunami - Expected Annual Loss - Population Equivalence` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss Score` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Tsunami - Number of Events` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Tsunami - Expected Annual Loss Score` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Historic Loss Ratio - Buildings` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss - Population Equivalence` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Volcanic Activity - Exposure - Building Value` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Avalanche - Annualized Frequency` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Avalanche - Expected Annual Loss - Total` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Avalanche - Historic Loss Ratio - Population` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Annualized Frequency` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Volcanic Activity - Exposure - Population Equivalence` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Volcanic Activity - Hazard Type Risk Index Score` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Avalanche - Expected Annual Loss Rate - National Percentile` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Avalanche - Expected Annual Loss - Population` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Tsunami - Expected Annual Loss - Total` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Hazard Type Risk Index Value` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss Rate - Population` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Avalanche - Exposure - Population Equivalence` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss Rate - Population` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Avalanche - Expected Annual Loss Rate - Population` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Avalanche - Hazard Type Risk Index Score` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss Score` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Volcanic Activity - Expected Annual Loss - Total` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Avalanche - Expected Annual Loss - Building Value` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Volcanic Activity - Historic Loss Ratio - Population` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Tsunami - Exposure - Building Value` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Coastal Flooding - Hazard Type Risk Index Score` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Avalanche - Number of Events` | 29.5% | 2013–2023 | 187 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss - Population` | 45.0% | 2013–2023 | 264 |
| FEMA NRI | `Tsunami - Exposure - Total` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Tsunami - Exposure - Population` | 10.1% | 2013–2023 | 81 |
| FEMA NRI | `Volcanic Activity - Exposure - Population` | 18.9% | 2013–2023 | 125 |
| FEMA NRI | `Coastal Flooding - Expected Annual Loss - Building Value` | 45.0% | 2013–2023 | 264 |
| Yale Climate Opinion | `opinion_exp` | 28.6% | 2021–2023 | 539 |
| Yale Climate Opinion | `opinion_generaterenewable` | 19.4% | 2022–2023 | 539 |
| Yale Climate Opinion | `opinion_priority` | 37.8% | 2020–2023 | 540 |
| State Transit Funding | `state_transit_pmt` | 24.4% | 2022–2024 | — |
| State Transit Funding | `state_transit_vrh` | 24.4% | 2022–2024 | — |
| State Transit Funding | `state_transit_operating_expenses` | 24.4% | 2022–2024 | — |
| State Transit Funding | `state_transit_fare_revenue` | 24.4% | 2022–2024 | — |
| State Transit Funding | `state_transit_agencies` | 24.4% | 2022–2024 | — |
| State Transit Funding | `state_transit_funding` | 24.4% | 2022–2024 | — |
| State Transit Funding | `ntd_state_funding_operations` | 24.4% | 2022–2024 | — |
| State Transit Funding | `ntd_state_funding_capital` | 24.4% | 2022–2024 | — |
| State Transit Funding | `ntd_local_funding_operations` | 24.4% | 2022–2024 | — |
| State Transit Funding | `ntd_local_funding_capital` | 24.4% | 2022–2024 | — |
| State Transit Funding | `ntd_federal_funding_operations` | 24.4% | 2022–2024 | — |
| State Transit Funding | `ntd_federal_funding_capital` | 24.4% | 2022–2024 | — |
| Bond Banks | `bond_bank_name` | 28.0% | — | — |
| Bond Banks | `bond_bank_established` | 28.0% | — | — |
| Bond Banks | `bond_bank_rating` | 14.0% | — | — |
| Bond Banks | `bond_bank_cumulative_billion` | 8.0% | — | — |
| Bond Banks | `bond_bank_active_2013_2025` | 28.0% | — | — |
| Bond Banks | `notes` | 6.0% | — | — |
| Anti-ESG Laws | `esg_first_bill_year` | 13.4% | 2021–2023 | 359 |
| Anti-ESG Laws | `esg_first_exec_action_year` | 14.8% | 2018–2023 | 275 |
| Anti-ESG Laws | `esg_first_law_year` | 6.4% | 2021–2023 | 209 |
| Anti-ESG Laws | `esg_first_proesg_year` | 9.3% | 2020–2023 | 198 |
| Anti-ESG Laws | `esg_first_underwriter_block_year` | 1.6% | 2018–2023 | 57 |
| MSRB RFI Position | `signatory_role` | 48.0% | — | — |
| SRF Bond Merged | `srf_n_projects` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_total_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_mean_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_median_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_total_current_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_mean_interest_rate` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_mean_fee_rate` | 1.1% | 2024–2025 | 67 |
| SRF Bond Merged | `srf_mean_finance_charge` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_mean_repayment_years` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_total_upfront_fees` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_n_cw` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_n_dw` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_cw_amount` | 1.0% | 2024–2025 | 58 |
| SRF Bond Merged | `srf_cw_mean_interest` | 1.0% | 2024–2025 | 58 |
| SRF Bond Merged | `srf_cw_mean_repayment` | 1.0% | 2024–2025 | 58 |
| SRF Bond Merged | `srf_dw_amount` | 0.4% | 2024–2025 | 26 |
| SRF Bond Merged | `srf_dw_mean_interest` | 0.4% | 2024–2025 | 26 |
| SRF Bond Merged | `srf_dw_mean_repayment` | 0.4% | 2024–2025 | 26 |
| SRF Bond Merged | `srf_any_conduit` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_any_sponsorship` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_any_programmatic` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `state_srf_n_loans` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_total_lending` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_mean_loan_size` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_median_loan_size` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_mean_interest` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_median_interest` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_mean_fee_rate` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_mean_finance_charge` | 15.0% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_mean_repayment` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_median_repayment` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_pct_conduit` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_pct_sponsorship` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_pct_programmatic` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_pct_cw` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_mean_upfront_fees` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `state_srf_cw_mean_interest` | 14.5% | 2024–2025 | 541 |
| SRF Bond Merged | `state_srf_cw_mean_repayment` | 14.5% | 2024–2025 | 541 |
| SRF Bond Merged | `state_srf_cw_n_loans` | 14.5% | 2024–2025 | 541 |
| SRF Bond Merged | `state_srf_cw_total_lending` | 14.5% | 2024–2025 | 541 |
| SRF Bond Merged | `state_srf_dw_mean_interest` | 14.4% | 2024–2025 | 543 |
| SRF Bond Merged | `state_srf_dw_mean_repayment` | 14.4% | 2024–2025 | 543 |
| SRF Bond Merged | `state_srf_dw_n_loans` | 14.4% | 2024–2025 | 543 |
| SRF Bond Merged | `state_srf_dw_total_lending` | 14.4% | 2024–2025 | 543 |
| SRF Bond Merged | `srf_cumulative_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_cumulative_projects` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `srf_total_amount_lag1` | 0.4% | 2025–2025 | 27 |
| SRF Bond Merged | `county_other_srf_n_projects` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `county_other_srf_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `cbsa_other_srf_n_projects` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `cbsa_other_srf_amount` | 1.1% | 2024–2025 | 68 |
| SRF Bond Merged | `state_other_srf_lending` | 15.2% | 2024–2025 | 547 |
| SRF Bond Merged | `srf_own_state_share` | 15.2% | 2024–2025 | 547 |
| Municipal Electric | `utility_name` | 14.2% | — | 80 |
| Municipal Electric | `customers` | 14.2% | — | 80 |
| Municipal Electric | `revenue_thousands` | 14.2% | — | 80 |
| Municipal Electric | `revenue_millions` | 14.2% | — | 80 |
| Crosswalk | `relevant_counties` | 15.6% | — | 89 |
| Crosswalk | `recommended_approach` | 15.6% | — | 89 |

### 4b. Datasets with incomplete panel-window coverage

- **Constructed Fiscal** (`constructed_fiscal.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Fiscal TEL Merged 2007-2024** (`fiscal_tel_merged_2007_2024.csv`): missing panel years **2025** — 12/13 coverage
- **Fiscal TEL Merged 2013-2025** (`fiscal_tel_merged_2013_2025.csv.gz`): missing panel years **2025** — 12/13 coverage
- **ACS Additional** (`additional_city_variables_2010_2024.csv`): missing panel years **2025** — 12/13 coverage
- **BLS ACS Economic** (`economic_bls_acs.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **EPA State Enforcement** (`epa_state_enforcement.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Vulcan CO2** (`Vulcan_data.csv`): missing panel years **2025** — 12/13 coverage
- **FEMA NRI** (`epa_nri.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Yale Climate Opinion** (`climate_opinion_ycom.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Climate Policy Controls** (`climate_policy_controls.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Federal Green Funding** (`federal_green_funding.csv`): missing panel years **2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2024, 2025** — 2/13 coverage
- **FOG Institutions** (`fog_institutions_panel_2010_2024.csv`): missing panel years **2025** — 12/13 coverage
- **TEL Data** (`tel.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Anti-ESG Laws** (`antiesg_laws.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **Presidential Elections** (`presidential_elections.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **State Political** (`state_political.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **ESG AUM** (`esg_aum.csv`): missing panel years **2024, 2025** — 11/13 coverage
- **State Green Bond Capacity** (`state_green_bond_capacity.csv`): missing panel years **2024, 2025** — 11/13 coverage

### 4c. Cross-sectional datasets (no year dimension)

These datasets have no year column and will apply as time-invariant values if merged:

- **ACS Demographics 2022** (`acs_demographics_2022.csv`): 574 observations, state/other-level
- **NFIP Flood Claims** (`nfip_flood_claims.csv`): 2273 observations, state/other-level
- **Bond Referenda** (`state_bond_referenda_requirements.csv`): 50 observations, state/other-level
- **Bond Banks** (`state_bond_banks.csv`): 50 observations, state/other-level
- **MSRB RFI Position** (`state_msrb_rfi_position.csv`): 50 observations, state/other-level
- **Municipal Electric** (`municipal_electric_utilities.csv`): 548 observations, city-level
- **State Building Codes** (`state_building_codes.csv`): 50 observations, state/other-level
- **State Clean Energy** (`state_clean_energy_funds.csv`): 50 observations, state/other-level
- **Crosswalk** (`Crosswalk.csv`): 548 observations, city-level

---

## 5. Methodology Notes

- **City detection:** columns matching `city`, `city_name`, `place_name`, `name`
- **Year detection:** columns matching `year`, `fiscal_year`
- **Non-null rate:** computed as count of non-missing values / total rows
- **Panel gaps:** years in 2013–2025 where a variable has zero non-null observations
- **No merging performed:** each dataset audited independently as instructed
- **ID columns excluded:** city, year, state, FIPS, and other identifier columns are not shown in variable tables
