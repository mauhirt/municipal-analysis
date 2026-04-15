# Pre-2013 presidential election data — data-pull gap

## Status

**Pending external data pull.** The user noted in the Part D variable audit
that earlier presidential election data (2008 onwards) is available and
should be merged into the panel. The current `raw/political/presidential_elections.csv`
covers 2013-2023 only, with the 2012 Obama/Romney results forward-filled from
2013-2015 and the 2016/2020 results filling later years.

This file documents the gap and how to close it when the data becomes
accessible.

## What needs to be pulled

The authoritative source for city-level presidential vote shares matched to
`fips7` city identifiers is the **MIT Election Data and Science Lab
(MEDSL) County Presidential Election Returns 2000-2020 dataset**
(`countypres_2000-2020.csv`), available at:

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ

Specifically, the 2008 and 2012 county-level presidential returns are what
we need. They can be aggregated to `fips7` via `raw/crosswalk/Crosswalk.csv`
(`county_geo_id` → county FIPS → MEDSL `county_fips`).

## Expected impact on the panel

Adding 2008 and 2012 presidential data means:

| Year range | Current panel value | After extension |
|---|---|---|
| 2013-2015 | 2012 Obama/Romney (fwd-filled) | 2012 Obama/Romney |
| 2012 row (if added) | MISSING (panel starts 2013) | 2012 Obama/Romney |
| 2009-2011 rows (if added) | MISSING | 2008 Obama/McCain |
| 2008 row (if added) | MISSING | 2008 Obama/McCain |

**Effect on lag-2 coverage:** The current lag-2 presidential variables
(`pres_dem_two_party_share_lag2`, `pres_rep_minus_dem_share_lag2`) are NaN
for panel years 2013-2014 because the lag-2 window reaches 2011-2012 which
isn't in the panel. If we extend the panel back to 2008, the lag-2 for 2013
becomes the 2011 value (= 2008 Obama/McCain), and lag-2 for 2014 becomes
the 2012 value (= 2012 Obama/Romney), recovering 1,154 city-years of
currently-missing constituency data.

## What's blocked until the pull

- Full-coverage `pres_dem_two_party_share_lag2` for panel years 2013-2014
  (currently NaN)
- Full-coverage `pres_rep_minus_dem_share_lag2` for 2013-2014
- Full-coverage `rep_x_pres_dem_share` interaction for 2013-2014
- A cleaner T3 Col 4 electoral-discipline test (more pre-2016 observations
  with meaningful lag-2 variation)

Until the pull is done, the affected robustness columns will run on the
2015-2025 subsample. Report the N difference in any paper table.

## How to complete the pull

1. Download `countypres_2000-2020.csv` from MIT MEDSL Dataverse to
   `raw/political/countypres_2000_2020_MEDSL.csv`.
2. Filter to years {2008, 2012}.
3. Aggregate from county to city via `raw/crosswalk/Crosswalk.csv`:
   - Read `county_geo_id` (format `0500000US<county_fips>`) and parse the
     5-digit county FIPS.
   - Multi-county cities (e.g., NYC) aggregate population-weighted vote
     shares across their listed counties (see `relevant_counties` column
     in the crosswalk).
4. Build `pres_dem_vote_share_{2008,2012}`, `pres_rep_vote_share_{2008,2012}`,
   `pres_dem_two_party_share_{2008,2012}` at the city level.
5. Extend the panel skeleton in `00_build_panel.py` §1 to cover 2008-2012
   (add synthetic rows for those years with presidential data only — do
   NOT extend other data sources that are 2013+).
6. Apply the existing forward-fill convention (election-year value
   persists until next election) so 2009-2011 rows get 2008 data, 2013-2015
   rows get 2012 data.
7. Rebuild the panel; verify `pres_dem_two_party_share_lag2` has
   full 2013-2025 coverage.

## Until then

The panel currently has 2013-2025 coverage with the following presidential
variables already built:

| Variable | Coverage | N nonnull |
|---|---|---|
| `pres_dem_vote_share` | 2013-2023 | 6,088 |
| `pres_dem_two_party_share` | 2013-2023 | 6,088 |
| `pres_rep_vote_share` | 2013-2023 | 6,088 |
| `pres_rep_minus_dem_share` | 2013-2023 | 7,248 (2024-2025 via fwd-fill) |
| `pres_dem_two_party_share_lag2` | 2015-2025 | 6,088 |
| `pres_rep_minus_dem_share_lag2` | 2015-2025 | 6,094 |
