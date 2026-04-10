# Codebook: Green Bond City-Year Analysis Panels

This folder contains the processed panels used in the municipal green bond
analysis. All panels are keyed on `FIPS × Year` (578 cities × 13 years,
2013–2025) unless noted otherwise.

**Important scope note:** Every bond in the source file
(`raw/bloomberg/cusip_with_assignment.csv`) is a green bond. The
`Self-reported Green` field is a subcategory indicating whether the
issuer formally self-labeled; it is not a filter.

---

## 1. Inputs used

| File | Description |
|---|---|
| `raw/bloomberg/cusip_with_assignment.csv` | CUSIP-level green bond data with city assignments, 25,555 rows. Columns include `Issuer Name`, `Amt Issued`, `Issue Date`, `panel_year`, `Jurisdiction_Type`, `State_Abb_Classified`, `city_fips7`, `is_in_578_panel`, plus ~14 categorical bond attributes. |
| `raw/bloomberg/green_bond_issuers_assignments.csv` | Issuer-level metadata: `Issuer_Name`, `lat`, `lng`, `city_fips7`, `Jurisdiction_Type`, etc. Used to bring issuer coordinates onto bond rows. |
| `raw/crosswalk/Crosswalk.csv` | 578 large US cities with `fips7`, `geo_name`, `city_name`, `state_abb`. Defines the panel universe. |
| `/tmp/crosswalk_city_centroids.csv` | Geocoded centroids for the 578 cities (Nominatim/OSM, one-time lookup). Used for nearby-distance calculations. |

**Filters applied throughout:**
- Valid `panel_year ∈ [2013, 2025]`
- 8 CUSIPs flagged by `cusip_duplicate_flag` are retained but none belong to a 578-city, so they have no effect on the panels.
- Whitespace/dash variants in categorical values are normalized (`"Yes "` → `"Yes"`, `"---"` → `"--"`).

**Coverage:** The 578-city panel covers **49 states + DC**. WV and VT have no cities in the crosswalk and therefore no rows.

---

## 2. Panel files

### 2.1 `outcome_city_year_panel.{csv,xlsx}`

**Purpose:** City-level green bond issuance outcomes.

**Script:** `pipeline/10_build_outcome_city_year_panel.py`

**Shape:** 7,514 rows × 560 columns.

**Key design:** Only bonds where `is_in_578_panel == True` are aggregated. Every city-year not in the data is filled with zeros.

**Column groups:**

| Columns | Description |
|---|---|
| `FIPS`, `City`, `City_Name`, `State`, `Year` | Identifiers. FIPS is the unique key; City+State is the verification combo. |
| `Green_Bond_Issued` | 1 if any green bond was issued in this city-year, else 0. |
| `City_Green_Amt_Issued` | Sum of `Amt Issued` for that city-year. |
| `City_Green_Issuance_Count` | Number of CUSIPs issued in that city-year. |
| `Issued_{field}__{value}` | 1 if any bond with that attribute was issued in the city-year. |
| `Amt_{field}__{value}` | Sum of `Amt Issued` for bonds with that attribute. |
| `Count_{field}__{value}` | Number of CUSIPs with that attribute. |

**Categorical fields that get Issued/Amt/Count triples:**
1. `Tax Prov` — federal/state tax treatment
2. `Fin Typ` — new money vs refunding
3. `BICS Level 2` — Bloomberg industry classification
4. `Self-reported Green` — whether the issuer self-labeled (Yes/No/--)
5. `Mgmt of Proc` — management of proceeds disclosed
6. `ESG Reporting` — ESG reporting provided
7. `ESG Assurance Providers` — third-party assurance
8. `Proj Sel Proc` — project selection process disclosed
9. `ESG Framework` — ESG framework used
10. `Industry` — short industry code
11. `Industry_Full` — long industry name
12. `Kestrel Total ESG Impact Score` — Kestrel score bucket
13. `ESG Project Categories` — project category (often comma-separated)
14. `Project Subcategory` — sub-category

**Summary stats:** 91 of 578 cities have at least one green bond 2013–2025; 170 city-year cells are non-empty.

---

### 2.2 `controls_city_year_panel.{csv,xlsx}` ⭐ (unified controls file)

**Purpose:** All control variables in one file.

**Script:** `pipeline/14_merge_controls.py` (merges outputs of scripts 13 and 12).

**Shape:** 7,514 rows × 113 columns.

**Column groups:**

#### State-level controls (24 cols) — from `pipeline/13_build_state_controls_city_year.py`

For each variable below, both `_Annual` (year Y only) and `_Cumul` (running sum through Y inclusive) are provided.

| Variable | Description |
|---|---|
| `State_Total_{Amt,Count}` | All green bonds issued in the focal city's state in year Y. |
| `State_Govt_{Amt,Count}` | Subset where `Jurisdiction_Type == STATE` (state-government issuers). |
| `State_Total_Ex_City_{Amt,Count}` | `State_Total` **minus** the focal city's own issuance. This is the "rest of the state" aggregate, specific to each city. |
| `State_Govt_Ex_City_{Amt,Count}` | `State_Govt` minus the focal city's own state-jurisdiction subset. |
| `City_Own_{Amt,Count}` | The focal city's own issuance (provided for reference / sanity check). |
| `City_Own_Govt_{Amt,Count}` | Focal city's state-jurisdiction subset. |

**Note:** State totals include **all** bonds in the state (including ones not assigned to a 578-city), so `State_Total` captures the full state-level green bond market. `Ex_City` is computed as `State_Total − City_Own` and will equal `State_Total` for cities that did not issue anything in that year.

#### Nearby controls (84 cols) — from `pipeline/12_build_nearby_by_jurisdiction.py`

For each focal city, nearby green bonds are those whose **issuer coordinates** (lat/lng from `green_bond_issuers_assignments.csv`) fall within a radius of the city centroid (from `/tmp/crosswalk_city_centroids.csv`).

**Rules:**
- Only non-state bonds (`Jurisdiction_Type != STATE`) are counted.
- Bonds whose issuer is assigned to the focal city itself are **excluded** (no double-counting with the focal city's own issuance).
- Distance = haversine kilometers between centroid and issuer lat/lng.

**Columns per radius (10 / 25 / 50 km), each in `_Annual` and `_Cumul`, each in `Amt` and `Count`:**

| Variable | Description |
|---|---|
| `Nearby_NonState_Total` | All non-state green bonds within the radius. |
| `Nearby_CITY` | City-level issuers (other 578 cities and small cities not in the panel) within radius. |
| `Nearby_COUNTY` | County-level issuers. |
| `Nearby_SCHOOL_DISTRICT` | School district issuers. |
| `Nearby_SPECIAL_DISTRICT` | Special district issuers (water, sewer, transit authorities, etc.). |
| `Nearby_MULTI_JURISDICTIONAL` | Multi-jurisdictional bodies (regional councils, joint authorities). |
| `Nearby_OTHER` | Catch-all for other non-state issuers. |

**Verification:** For each radius, `Nearby_NonState_Total` equals the sum of the six subcategory columns. Radii are monotonic: 10km ⊆ 25km ⊆ 50km.

**⚠️ Known limitation — the 10 km radius is too tight for large cities.**
The nearby-distance is computed from the focal city's **centroid** to the issuer's lat/lng. For geographically small cities this works fine, but for large-footprint cities (LA, SF, Chicago, Houston, Phoenix, etc.) a 10 km ring from the centroid falls well inside the city limits and misses nearby same-metro entities.

Concrete example: for **Los Angeles**, the 10 km ring has **0 non-state bonds in every year**, while 25 km picks up 138 and 50 km picks up 385. Key LA-area entities sit at these distances from the LA centroid:

| Entity | Distance from LA centroid |
|---|---|
| Monterey Park Financing Authority | 10.8 km |
| LA County Sanitation Districts Financing Authority | 20.5 km |
| LA County Metropolitan Transportation Authority | 39.0 km |
| LA County Public Works Financing Authority | 39.0 km |

**Practical implication:** Use the **25 km or 50 km** variables as the working diffusion/learning controls. The 10 km variable is retained in the panel for completeness and for small-to-medium cities where it is meaningful, but it will be near-zero for the largest cities and should not be used as the primary control for them.

A more principled fix would be to compute the distance from the focal city's **boundary polygon** (TIGER shapefile) rather than the centroid, so that any bond inside the city + within 10 km of the boundary counts. That change requires adding geopandas + TIGER place boundaries and has not been implemented. Let me know if you want me to add it.

---

### 2.3 Component files (kept for provenance)

These are the building blocks of the unified controls file. They have the same `FIPS × Year` key and can be joined back if needed.

| File | Rows × Cols | Source script | Contents |
|---|---|---|---|
| `state_controls_city_year_panel.{csv,xlsx}` | 7,514 × 29 | `13_build_state_controls_city_year.py` | State-level variables only (first 24 cols above). |
| `nearby_by_jurisdiction_panel.{csv,xlsx}` | 7,514 × 89 | `12_build_nearby_by_jurisdiction.py` | Nearby variables only (84 cols above). |
| `state_controls/{STATE}_controls.{csv,xlsx}` | 49 files | `11_build_per_state_controls.py` | Per-state breakdown of section 2.2's state-level controls. One file per state. Redundant with `state_controls_city_year_panel` but useful if you want to work state-by-state. |

---

## 3. Outcome variable vs control variable design

- **Outcomes** (`outcome_city_year_panel.csv`): What the focal city itself did. Use these as LHS variables.
- **Controls** (`controls_city_year_panel.csv`): The environment around the focal city — state-level activity minus the focal city, and nearby activity by other bodies. Use these as RHS variables to capture spillovers and the broader green bond market.

The `Ex_City` construction is the key mechanism that keeps controls **predetermined relative to the focal city's own outcome**: if you regress `Green_Bond_Issued` on `State_Total_Ex_City_Amt_Annual`, the RHS cannot include the LHS by construction.

---

## 4. Methodology notes

### 4.1 Year field
`panel_year` is the cleaned year field from the input CSV. It was originally derived by preferring `Year` when in [2013, 2030], otherwise falling back to the year of `Issue Date`.

### 4.2 City centroids
All 578 crosswalk cities were geocoded via Nominatim/OpenStreetMap using "City, State, USA" queries. Centroids are used for distance calculations only; they are the approximate center of the named place returned by the geocoder.

### 4.3 Issuer coordinates
Most issuers were geocoded by Google (from the original `FinalEntities_with_coords` file). A subset (~131) were re-geocoded via Nominatim after the file was rebuilt keyed on `Issuer Name`. 39 issuers with wrong-state coordinates (e.g., Bloomington IN that had Bloomington MN coords) were re-geocoded and fixed.

### 4.4 Cities with same name in different states
FIPS is the primary key throughout. Bloomington IN (1805860), Bloomington MN (2706616), and Bloomington IL (1706613) are three distinct rows in every panel.

### 4.5 Suspected duplicate CUSIPs
8 rows (4 CUSIPs × 2) are flagged in the input via `cusip_duplicate_flag`. They are **retained** in all aggregates because:
1. Whether they are true duplicates or legitimate tranches is ambiguous.
2. All 4 CUSIPs have `city_fips7 = NaN`, so they do not affect the 578-city panels either way.

### 4.6 WV and VT
West Virginia and Vermont have no cities in the 578-city crosswalk. They appear in state-level aggregates (e.g., there may be WV bonds in the state-level totals) but they produce no panel rows.

---

## 4a. Merged city-year panel with all independent variables

### `merged_city_year_panel.{csv,xlsx}` ⭐ main analysis file

**Script:** `pipeline/15_build_merged_city_year_panel.py`

**Shape:** 7,514 rows × 1,583 columns. Same `FIPS × Year` key.

**Contents:**
- Identifiers (FIPS, City, City_Name, State, Year)
- The **outcome panel** (Green_Bond_Issued + 552 Issued/Amt/Count pivots)
- The **green bond controls** (State_Total, State_Govt, State_Total_Ex_City, State_Govt_Ex_City, City_Own, Nearby_* at 10/25/50 km)
- **Fiscal + TEL** (from `fiscal_tel_merged_2007_2024.csv`, 54 vars) with lag1 and lag2 computed from **pre-2013** data (2011/2012) — so 2013 outcome rows have legitimate lags, not NaN.
- **Census additional city variables** (20 vars including state political control, YCOM climate opinion subset, presidential vote shares)
- **YCOM climate opinion** (24 vars, `ycom_*` prefix)
- **Climate policy controls** (10 vars: C40 membership, muni yield, RPS, carbon pricing)
- **Anti-ESG laws** (28 vars, `esg_*` prefix)
- **Other state political** (non-overlapping vars)
- **Federal grants** (IIJA/IRA/EECBG/GGRF/FEMA resilience, 24 base vars)
- **NRI hazard risk** (432 vars, `nri_*` prefix, time-invariant — merged once)

All time-varying vars have `{var}`, `{var}_lag1`, and `{var}_lag2` triples.

### Lag strategy (Option B — predetermined controls, no carry-forward)

For each variable, `lag1` and `lag2` are computed from the **raw data frame** (which may extend back to 2007 for fiscal, 2010 for census) **before** filtering to the 2013–2025 outcome window. This means:

| Outcome year | Fiscal lag1 source | Fiscal lag2 source |
|---|---|---|
| 2013 | raw 2012 (real) | raw 2011 (real) |
| 2014 | raw 2013 (real) | raw 2012 (real) |
| … | … | … |
| 2024 | raw 2023 (real) | raw 2022 (real) |

**No artificial carry-forward is applied.** Where the raw file does not
contain year Y, the contemporaneous `X` column at Y is **NaN**. The user
should rely on `X_lag1` or `X_lag2` instead.

### Verified availability matrix (number of cities with non-null data out of 578)

The lag logic does a proper **cross-year merge**: `{var}_lag1` at outcome year Y pulls `raw[fips, Y-1]`, and `{var}_lag2` at Y pulls `raw[fips, Y-2]`. So when the raw data has year Y-1 or Y-2, the panel is populated for that outcome year.

**Fiscal — core economic variables** (`population_city`, `percapita_income_city`, `total_revenue_pc`, `own_source_rev_pc`, `debt_pc`, `property_tax_share`, `fiscal_stress_index`, `debt_to_revenue`, etc.). Raw ends at **2023** (Census of Governments publishing lag).

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | **0** | **0** |
| **lag1** | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | **0** |
| **lag2** | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | **577** |

**Fiscal — `fiscal_stress_pca`**. Raw ends at **2021**.

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 577 | 577 | 577 | 576 | 574 | 573 | 575 | 575 | 574 | 0 | 0 | 0 | 0 |
| lag1 | 577 | 577 | 577 | 577 | 576 | 574 | 573 | 575 | 575 | 574 | 0 | 0 | 0 |
| lag2 | 577 | 577 | 577 | 577 | 577 | 576 | 574 | 573 | 575 | 575 | 574 | 0 | 0 |

**TEL variables** (`tel_stringency_*`, `tel_levy_limit`, etc.). Raw ends at **2024**.

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 0 |
| **lag1** | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | **578** |
| **lag2** | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | **578** |

**Census additional — presidential vote share, state political, opinion subset** (`pres_dem_two_party_share`, `state_dem_governor`, `opinion_happening`, etc.). Raw ends at **2024**.

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 576 | 0 |
| **lag1** | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | **576** |
| **lag2** | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | 577 | **577** |

**YCOM climate opinion** (`ycom_*`). Raw file has years 2013–2023 but the opinion variables start at **2014** (2013 rows exist but are NaN).

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | **0** | 470 | 475 | 477 | 556 | 484 | 509 | 515 | 516 | 569 | 517 | 0 | 0 |
| lag1 | 0 | 0 | 470 | 475 | 477 | 556 | 484 | 509 | 515 | 516 | 569 | 517 | 0 |
| **lag2** | 0 | 0 | 0 | 470 | 475 | 477 | 556 | 484 | 509 | 515 | 516 | 569 | **517** |

**Climate policy controls** (`c40_member`, `mayors_climate_signatory`, `muni_aaa_yield`, state RPS/carbon). Raw ends at **2023**; some vars start at 2013, others at 2014.

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 510 | 470 | 475 | 477 | 556 | 484 | 509 | 515 | 516 | 569 | 517 | 0 | 0 |
| lag1 | 0 | 510 | 470 | 475 | 477 | 556 | 484 | 509 | 515 | 516 | 569 | 517 | 0 |
| **lag2** | 0 | 0 | 510 | 470 | 475 | 477 | 556 | 484 | 509 | 515 | 516 | 569 | **517** |

**Anti-ESG laws** (`esg_*`). Raw ends at **2023**.

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 511 | 471 | 476 | 478 | 557 | 485 | 510 | 516 | 517 | 570 | 518 | 0 | 0 |
| lag1 | 0 | 511 | 471 | 476 | 478 | 557 | 485 | 510 | 516 | 517 | 570 | 518 | 0 |
| **lag2** | 0 | 0 | 511 | 471 | 476 | 478 | 557 | 485 | 510 | 516 | 517 | 570 | **518** |

**Federal grants** (IIJA/IRA/EECBG/GGRF/FEMA resilience). Raw ends at **2025** — contemporaneous and all lags available throughout.

| Outcome year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| contemp | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 |
| lag1 | 0 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 |
| lag2 | 0 | 0 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 | 578 |

**Green bond outcomes, state controls, and nearby controls** — all 578 cities × all 13 years, no missing.

**NRI hazards** — time-invariant, merged once across the panel.

### Summary: is `_lag2` sufficient for 2013–2025?

| Variable group | Can use `_lag2` 2013–2025? | Notes |
|---|---|---|
| Fiscal core economic vars | ✅ **YES** (577 at Y=2025) | lag2 = raw 2023 |
| `fiscal_stress_pca` | ❌ No (ends at 2023 outcome) | raw ends 2021 |
| `pension_expenditure_burden` | ❌ No (ends at 2018 outcome) | raw ends 2016 |
| `go_bond_share_*` | ❌ No | raw ends 2012 |
| TEL variables | ✅ YES (578 at Y=2025) | |
| Presidential vote share, state political (census add) | ✅ YES (577 at Y=2025) | |
| YCOM climate opinion | ⚠️ YES from **2016** onward; 2013–2015 NaN | raw starts 2014 |
| Climate policy (C40, RPS, etc.) | ⚠️ YES from **2015** onward; 2013–2014 NaN | raw starts 2013 but lag2 needs 2013 for 2015 |
| Anti-ESG laws | ⚠️ YES from **2015** onward; 2013–2014 NaN | same |
| Federal grants | ⚠️ YES from **2015** onward; 2013–2014 NaN | raw starts 2013 |
| Green bond outcomes/controls/nearby | ✅ YES all 2013–2025 | |

For a regression using `_lag2` on the full 2013–2025 sample:
- **Fiscal economic, TEL, presidential, state political** → no dropped observations.
- **YCOM / climate policy / anti-ESG / federal grants** → rows 2013–2014 (or 2013–2015 for YCOM) will have NaN on those lags. Either drop those years from the regression or impute with constant "no information" values.
- **`fiscal_stress_pca`, `pension_expenditure_burden`, `go_bond_share_*`** → avoid unless you're willing to lose substantial sample on the right tail.

### Recommendation for 2013–2025 analysis

Use **`_lag2`** as the default lag for control variables. With lag2:
- **2013** outcomes use control values from raw **2011** (real, pre-sample).
- **2025** outcomes use control values from raw **2023** (real, the last complete year for most Census data).
- No NaN rows are produced by the lag operation for any 2013–2025 outcome year.
- Controls are predetermined by 2 years, which strengthens the causal interpretation.

Alternative (mixed-depth lags):
- `fiscal_*_lag2` (economic vars)
- `tel_*_lag1` (TEL vars — have 2024)
- `federal_grants_*_lag1` (grants — have 2024)
- `esg_*_lag2`, `ycom_*_lag2`, `cpol_*_lag2` (2023-ending)
- Green bond controls: contemporaneous is fine (raw ends 2025)

### Usage

```python
import pandas as pd
panel = pd.read_csv("processed/merged_city_year_panel.csv", low_memory=False)
# 7,514 rows x 1,583 cols, covering 578 cities x 13 years (2013-2025)

# Regression with t-2 lags (recommended - works for all 2013-2025)
import statsmodels.formula.api as smf
model = smf.logit(
    "Green_Bond_Issued ~ "
    "fiscal_stress_index_lag2 + debt_to_revenue_lag2 + "
    "pres_dem_two_party_share_lag2 + esg_num_antiesg_laws_lag2 + "
    "State_Total_Ex_City_Amt_Cumul + "
    "Nearby_NonState_Total_Amt_25km_Cumul",
    data=panel,
).fit()
```

---

## 5. Pipeline scripts (in `pipeline/`)

| Script | Purpose |
|---|---|
| `02_issuer_classification_audit.py` | Compares issuer jurisdiction types against MSRB (produces audit report). |
| `_geocode_cities.py` | One-time helper to geocode the 578 crosswalk city centroids via Nominatim. |
| `10_build_outcome_city_year_panel.py` | Builds `outcome_city_year_panel`. |
| `11_build_per_state_controls.py` | Builds the per-state files in `state_controls/`. |
| `12_build_nearby_by_jurisdiction.py` | Builds `nearby_by_jurisdiction_panel`. |
| `13_build_state_controls_city_year.py` | Builds `state_controls_city_year_panel` (all 578 cities in one file). |
| `14_merge_controls.py` | Merges 12 + 13 into `controls_city_year_panel`. |

Scripts `03`–`09` are earlier iterations whose outputs were deleted. They are retained for reference but should not be re-run; the current production flow is 10 → 11 → 12 → 13 → 14.

---

## 6. Typical usage example

```python
import pandas as pd

outcomes = pd.read_csv("processed/outcome_city_year_panel.csv")
controls = pd.read_csv("processed/controls_city_year_panel.csv")

panel = outcomes.merge(controls, on=["FIPS", "City", "City_Name", "State", "Year"])
# Now you have 7,514 rows with outcomes + controls joined.

# Example: regress green bond issuance on state ex-city activity and nearby activity
import statsmodels.formula.api as smf
model = smf.logit(
    "Green_Bond_Issued ~ State_Total_Ex_City_Amt_Cumul + "
    "Nearby_NonState_Total_Amt_25km_Cumul",
    data=panel,
).fit()
```
