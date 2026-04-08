# Municipal Green Bond Analysis — Data Repository

**Paper:** "When Do Red and Blue Go Green? Mayoral Partisanship and Municipal Green Bond Issuance"

**Author:** Maurice Hirt, University of Oxford

## Quick start

```bash
# Build the panel from raw sources
python pipeline/00_build_panel.py        # → processed/panel/panel.pkl (7,514 × 3,500+)
python pipeline/01_construct_audit_variables.py  # → adds audit vars, prunes to ~1,329 cols
```

## Repository structure

```
municipal-analysis/
├── raw/                           # All input datasets (read-only)
│   ├── bloomberg/                 # Green bond issuance skeleton (578 cities × 2013-2025)
│   ├── mayor/                     # Mayoral partisanship (576 cities × 2010-2025)
│   ├── fiscal/                    # Census ASLGF fiscal + TEL + BLS/ACS (578 × 2007-2024)
│   ├── epa/                       # EPA ECHO enforcement expanded (576 × 2000-2026)
│   ├── census_acs/                # ACS demographics, employment, raw zips
│   ├── nri/                       # FEMA National Risk Index (573 × 2013-2024)
│   ├── vulcan/                    # Vulcan CO2 emissions (577 × 2013-2024)
│   ├── political/                 # Anti-ESG laws, state political, presidential, MSRB RFI
│   ├── climate/                   # Yale Climate Opinion, climate policy controls
│   ├── institutional/             # FOG, TEL, bond referenda, bond banks
│   ├── srf/                       # State Revolving Fund data
│   ├── energy_policy/             # Building codes, EERS, net metering, municipal electric
│   ├── disasters/                 # FEMA disaster declarations, NFIP flood
│   ├── grants/                    # Federal grants (IIJA/IRA), state transit
│   ├── geospatial/                # Substitute water issuer panel
│   ├── market/                    # ESG AUM, state green bond capacity
│   └── crosswalk/                 # City-county FIPS crosswalk (578 cities)
│
├── processed/                     # Build outputs
│   ├── panel/                     # panel.pkl — the merged analysis panel
│   └── codebook/                  # Variable documentation + missingness audits
│
├── pipeline/                      # Build scripts
│   ├── 00_build_panel.py          # Merge 35 source files → panel
│   ├── 01_construct_audit_variables.py  # Derive + prune
│   └── helpers.py                 # Regression utilities
│
└── variable_list_audit.md         # Authoritative variable checklist
```

## Data sources (35 files)

| # | Folder | File | Years | Cities | Source |
|---|---|---|---|---|---|
| 1 | bloomberg | city_year_issuance_panel.xlsx | 2013-2025 | 578 | Bloomberg Terminal |
| 2 | mayor | mayor_party.csv | 2010-2025 | 576 | Harvard Dataverse + manual |
| 3 | mayor | MayoralCandidates270326.xlsx | 2001-2025 | 576 | Master candidates file |
| 4 | fiscal | fiscal_tel_merged_2007_2024.csv | 2007-2024 | 578 | Census ASLGF + ACIR TEL + BLS/ACS |
| 5 | fiscal | fiscal_tel_merged_2013_2025.csv.gz | 2013-2024 | 572 | Older build (supplement) |
| 6 | fiscal | constructed_fiscal.csv | 2013-2023 | 572 | Derived fiscal ratios |
| 7 | epa | city_year_epa_enforcement_expanded*.csv | 2000-2026 | 576 | EPA ECHO/ICIS-NPDES |
| 8 | epa | epa_state_enforcement.csv | 2013-2023 | 572 | EPA state enforcement |
| 9 | census_acs | economic_bls_acs.csv | 2010-2023 | 574 | BLS LAUS + ACS 5-Year |
| 10 | census_acs | acs_demographics_2022.csv | 2022 xsec | 574 | Census ACS API |
| 11 | census_acs | additional_city_variables_2010_2024.csv | 2010-2024 | 577 | ACS supplementary |
| 12 | census_acs | PlaceEconomic1.zip | 2010-2023 | 32K+ | Raw ACS employment |
| 13 | census_acs | PlaceEconomic2.zip | 2010-2023 | 32K+ | Raw ACS employment |
| 14 | nri | epa_nri.csv | 2013-2024 | 573 | FEMA NRI |
| 15 | vulcan | Vulcan_data.csv | 2013-2024 | 577 | Vulcan v4 |
| 16 | political | antiesg_laws.csv | 2013-2023 | 573 | State legislative tracking |
| 17 | political | state_political.csv | 2013-2023 | 577 | NCSL + Ballotpedia |
| 18 | political | presidential_elections.csv | 2013-2023 | 577 | MIT MEDSL |
| 19 | political | state_msrb_rfi_position.csv | xsec | 50 states | MSRB 2022 consultation |
| 20 | climate | climate_opinion_ycom.csv | 2014-2024 | 572 | Yale PCCC |
| 21 | climate | climate_policy_controls.csv | 2013-2023 | 572 | C40/ICLEI/DSIRE |
| 22 | institutional | fog_institutions_panel_2010_2024.csv | 2010-2024 | 578 | ICMA FOG Survey |
| 23 | institutional | tel.csv | 2013-2023 | 572 | ACIR/Lincoln Institute |
| 24 | institutional | state_bond_referenda_requirements.csv | xsec | 50 states | State statutes |
| 25 | institutional | state_bond_banks.csv | xsec | 50 states | State records |
| 26 | srf | srf_bond_merged.csv | 2013-2025 | 578 | EPA SRF + USAspending |
| 27 | energy_policy | municipal_electric_utilities.csv | xsec | 578 | EIA Form 861 |
| 28 | energy_policy | state_building_codes.csv | xsec | 50 states | DOE BECP |
| 29 | energy_policy | state_clean_energy_funds.csv | xsec | 50 states | DSIRE/ACEEE |
| 30 | energy_policy | state_net_metering.csv | 2010-2025 | 50 states | DSIRE |
| 31 | disasters | fema_disaster_declarations.csv | 2010-2025 | 3,088 counties | FEMA OpenFEMA |
| 32 | disasters | nfip_flood_claims.csv | xsec | 2,273 counties | FEMA NFIP |
| 33 | grants | federal_grants_panel.csv | 2013-2025 | 578 | USAspending |
| 34 | grants | federal_green_funding.csv | 2022-2023 | state | White House/DOE |
| 35 | grants | state_transit_funding.csv | 2013-2025 | state | FTA NTD |
| 36 | geospatial | substitute_water_panel.csv | 2013-2025 | 577 | Derived |
| 37 | market | esg_aum.csv | 2013-2023 | year-level | Morningstar/Bloomberg |
| 38 | market | state_green_bond_capacity.csv | 2013-2023 | 50 states | Bloomberg |
| 39 | crosswalk | Crosswalk.csv | xsec | 578 | Census geography |

## Output panel

- **7,514 rows** (578 cities × 13 years)
- **~1,329 columns** after construction and pruning
- **574 cities** in the regression sample (4 principled drops)
- **7,048 city-year observations** with complete preferred-spec controls

## Key variables

| Variable | Description | Coverage |
|---|---|---|
| `Y_self_green` | Primary DV: city self-labelled green bond | 2013-2025, 578 cities |
| `Y_esg_assurance` | Secondary DV: third-party assurance | 2013-2025, 578 cities |
| `Rep_Mayor` | Republican mayor (D=baseline) | 2013-2025, 576 cities |
| `Ind_Mayor` | Independent mayor indicator | 2013-2025, 576 cities |
| `npdes_formal_prior3yr_muni` | NPDES enforcement (municipal) | 2013-2025, 576 cities |
| `overflow_events_lag2` | Sewer overflow (lag-2) | 2013-2025, 578 cities |
| `charges_to_own_source_lag2` | Enterprise fund revenue share | 2013-2025, 577 cities |
| `tel_stringency_normalized` | TEL composite index | 2013-2025, 578 cities |
| `esg_has_muni_bond_law` | Anti-ESG muni bond law | 2013-2025, 573 cities |
