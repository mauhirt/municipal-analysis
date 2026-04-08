# Diagnosis: 6 Cities Missing `pres_dem_vote_share`

## Headline

All 6 cities are missing because the presidential election crosswalk (county → city FIPS) fails for them. **4 are consolidated city-counties** where the city IS the county — the county-level presidential vote is directly usable. **1 is a regular city** (St. Peters MO) that was simply omitted from the crosswalk. **1 is a NJ township** (Edison) with no Census population data and no crosswalk entry — likely structurally unrecoverable.

**Louisville KY has 1 green bond** — it is the only issuer among the 6.

## City-by-City Diagnosis

| City | State | FIPS | Population | County FIPS | Type | Missingness Cause | Proposed Fix | Recoverable |
|---|---|---|---|---|---|---|---|---|
| Athens-Clarke County | GA | 1303440 | 122,893 | 13059 | Consolidated city-county | Missing from crosswalk AND from 5 other clean datasets (esg, state_political, presidential). No county_fips5 in panel — never linked to a county. | Add county FIPS 13059 manually. Assign Clarke County presidential vote share directly (city = county). | **Y** |
| Indianapolis | IN | 1836000 | 858,283 | 18097 | Consolidated city-county | Missing from presidential crosswalk. City IS Marion County. | Assign Marion County presidential vote share directly. | **Y** |
| Louisville | KY | 2148000 | 616,669 | 21111 | Consolidated city-county | Missing from presidential crosswalk. City IS Jefferson County. **Has 1 green bond.** | Assign Jefferson County presidential vote share directly. | **Y** |
| Nashville-Davidson | TN | 4752006 | 655,779 | 47037 | Consolidated city-county | Missing from presidential crosswalk. City IS Davidson County. | Assign Davidson County presidential vote share directly. | **Y** |
| St. Peters | MO | 2965126 | 56,362 | 29183 | Regular city | Missing from presidential crosswalk. Located entirely in St. Charles County. | Assign St. Charles County presidential vote share as proxy. Note: county includes other cities, so this is approximate. | **Y** (county proxy) |
| Edison | NJ | 3420260 | N/A | 34023 | Township/CDP | Missing from presidential crosswalk AND has no Census population data (all fiscal/demographic variables NaN). NJ townships are not municipalities in the Census of Governments. | **Not recoverable.** Edison lacks population, fiscal, and demographic data across the board. It should not be in the panel. | **N** |

## Additional Note on `state_rep_trifecta`

Indianapolis, Louisville, Nashville, St. Peters, and Athens-Clarke are also missing `state_rep_trifecta` — this comes from the same state_political source that matches on fips7. The fix is the same: add these fips7 codes to the state_political crosswalk and assign state-level values for their respective states.

## Summary

- **4 recoverable via direct county assignment** (consolidated city-counties: Athens-Clarke, Indianapolis, Louisville, Nashville)
- **1 recoverable via county proxy** (St. Peters MO — regular city, county-level vote is approximate)
- **1 structurally unrecoverable** (Edison NJ — township with no Census data)
- **Louisville is the only issuer** among the 6 — recovering it adds 1 green bond to the sample
