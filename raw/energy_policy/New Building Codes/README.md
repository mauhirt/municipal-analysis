# Building Codes & Building Performance Standards Data

**Purpose.** Hand-curated panel of (a) state-level new-construction energy-code
stringency ("Tier 1") and (b) city-/county-/state-level Building Performance
Standards ("BPS") for existing buildings, plus the benchmarking-ordinance
precursor panel, to be merged into the green-bond city-year dataset.

This directory was built on branch `claude/state-level-building-data-hkmGc`
in response to the request to collect Tier 1 + BPS data per the research-design
memo ("Block A", "Block B", "Block C").

## TL;DR — the two files you want to merge

**Time span: 2010 – 2025 (16 years).**

| File | Rows | Unit | What it's for |
|---|---|---|---|
| **`master_city_year_panel_2010_2025.csv`** | **816** | jurisdiction × year | Primary merge target. 51 unique jurisdictions (39 cities + 9 states + 2 counties + DC) × 16 years. All Block A + B + C fields + state-level BPS rollup + derived convenience columns (`years_since_bps`, `any_policy_active`). |
| **`master_state_year_panel_2010_2025.csv`** | **816** | state × year | Supplementary merge target. All 51 states/DC × 16 years. Block A (state IECC Tier 1), state-level BPS rollup, and counts of city-level BPS / benchmarking jurisdictions active in each state-year. Use this to carry state-level policy context onto cities that are NOT in the city-year master (i.e. the never-treated majority in a ~578-city green-bond panel). |

The city-year master has **48 columns**. The state-year master has **23 columns**. Both are plain CSV, no external dependencies.

### Where to download / where the files live

On branch `claude/state-level-building-data-hkmGc` of `mauhirt/municipal-research`, in the folder `data/building_codes_bps/`. Full paths:

- `data/building_codes_bps/master_city_year_panel_2010_2025.csv`
- `data/building_codes_bps/master_state_year_panel_2010_2025.csv`
- `data/building_codes_bps/README.md` (this file)

Clone the branch to get everything:

```bash
git clone -b claude/state-level-building-data-hkmGc \
    https://github.com/mauhirt/municipal-research.git
cd municipal-research/data/building_codes_bps/
```

Or pull the branch if you already have the repo:

```bash
git fetch origin claude/state-level-building-data-hkmGc
git checkout claude/state-level-building-data-hkmGc
ls data/building_codes_bps/
```

### Recommended merge pattern

Your green-bond dataset is assumed to have at minimum `jurisdiction`, `state_abbr`, and `year` columns.

```python
import pandas as pd

gb = pd.read_csv("green_bond_city_year.csv")

city_master  = pd.read_csv("data/building_codes_bps/master_city_year_panel_2010_2025.csv")
state_master = pd.read_csv("data/building_codes_bps/master_state_year_panel_2010_2025.csv")

# Step 1 — state-level context for ALL cities (Block A Tier 1 + state BPS rollup)
gb = gb.merge(state_master, on=["state_abbr", "year"], how="left")

# Step 2 — jurisdiction-level fields for cities that are in the master panel
city_only_cols = [
    "jurisdiction", "state_abbr", "year",
    "bps_adopted", "bps_effective", "bps_year_enacted", "bps_first_compliance_year",
    "years_since_bps", "bps_metric", "bps_covered_threshold_comm_sqft",
    "bps_covers_municipal", "bps_ratchet",
    "bps_penalty_per_sqft", "bps_penalty_per_tco2e",
    "bps_law_name", "bps_law_id",
    "bps_coalition_member", "bps_coalition_launch_day", "bps_coalition_joined_year",
    "benchmarking_adopted", "benchmarking_effective",
    "benchmarking_year_enacted", "benchmarking_first_reporting_year",
    "years_since_benchmarking", "benchmarking_threshold_sqft", "audit_tuneup_req",
    "any_policy_active", "any_policy_effective",
]
gb = gb.merge(city_master[city_only_cols],
              on=["jurisdiction", "state_abbr", "year"], how="left")

# Step 3 — fill NaN for never-treated cities (binary indicators → 0)
for col in ["bps_adopted", "bps_effective",
            "benchmarking_adopted", "benchmarking_effective",
            "bps_coalition_member", "bps_coalition_launch_day",
            "any_policy_active", "any_policy_effective"]:
    gb[col] = gb[col].fillna(0).astype(int)
```

After this, for a city like **Baltimore, MD** (not in my city-year master but in Maryland which has a state-level BPS), you'll have:
- `state_bps_adopted = 0` for 2010–2021, `1` from 2022 onward (Maryland SB 528)
- `bps_adopted = 0` in every year (Baltimore has no city-level BPS)
- `iecc_comm_vintage` following Maryland's code transitions (2009 → 2012 → 2015 → 2019)
- `state_any_city_has_bps = 0` pre-2022, `1` from 2022 (Montgomery County Bill 16-21)

For a city like **New York City, NY** (which IS in the master):
- Full jurisdiction-level BPS fields from LL97 (enacted 2019, effective 2024)
- `years_since_bps = 0,1,2,3,4,5,6` across 2019–2025
- `bps_penalty_per_tco2e = 268`
- NY state IECC vintage following the NY transitions

---


## Files

| File | Rows | Unit | Description |
|---|---|---|---|
| `state_iecc_current.csv` | 51 | state | Cross-section of the current commercial IECC/ASHRAE 90.1 vintage in force in each US state + DC (Block A) |
| `state_code_transitions.csv` | ~140 | state-transition | Historical commercial energy code transitions (effective year + vintage) for each state, sourced from DOE BECP state portal pages |
| `state_iecc_panel_2010_2025.csv` | 816 | state-year | Long-format state-year panel (51 × 16 yrs) with vintage carried from transitions, plus `lag_model_code_yrs` (years behind frontier) |
| `bps_jurisdictions.csv` | 16 | jurisdiction | Cross-section of every US jurisdiction that has enacted a Building Performance Standard, per IMT BPS Matrix Jan 2026 (Block B). Includes quantitative penalty columns (`bps_penalty_per_sqft`, `bps_penalty_per_tco2e`). |
| `bps_coalition_members.csv` | 45 | jurisdiction | States/cities/counties in the National BPS Coalition. Includes `launch_day_member = 1` for the 33 original members from the Biden White House fact sheet of Jan 21 2022, plus `joined_year` for post-launch additions. |
| `bps_city_panel_2015_2025.csv` | 506 | jurisdiction-year | Long-format BPS panel (46 jurisdictions × 11 yrs); includes adopters and Coalition-only members, penalty fields, and launch-day flag |
| `benchmarking_ordinances.csv` | 28 | jurisdiction | Cross-section of mandatory building-energy benchmarking ordinances (Block C) |
| `benchmarking_city_panel_2008_2025.csv` | 504 | jurisdiction-year | Long-format benchmarking panel (28 × 18 yrs) |
| `build_panels.py` | — | — | Script that expands the four cross-sections into the three long panels |

## Variable dictionary — keyed to the codebook

### Block A: New-Construction Stringency (Tier 1, state-level)

From `state_iecc_current.csv` and `state_iecc_panel_2010_2025.csv`:

| Codebook var | CSV column | Notes |
|---|---|---|
| `iecc_comm_vintage` | `iecc_comm_vintage` | Year of IECC edition (or ASHRAE 90.1 year-equivalent) in force **in that specific state-year**, computed by walking `state_code_transitions.csv`. Blank when `pre_first_transition = 1` (state had no documented transition before that year) or the state has no statewide code. |
| `iecc_comm_code_type` | `iecc_comm_code_type` | "IECC", "ASHRAE", "TITLE24", "ICC", etc. — model-code family of the vintage in force. |
| `iecc_effective_year` | `iecc_comm_effective_year` | In `state_iecc_current.csv`, the effective year of the **current** vintage (cross-section convenience field). |
| `home_rule` | `home_rule` | 1 if the state has no mandatory statewide code and delegates to localities (AZ, KS, MS, MO, ND, SD, TN, WV are coded 1). |
| `preemption` | `preemption_of_stricter_local` | 1 if the state prohibits localities from exceeding the state code (NC, OH, TN, UT are coded 1). |
| `local_stretch_permitted` | `stretch_code_available` | 1 if the state permits localities to adopt a stretch code (CA, CO, DC, MA, ME, MD, NM, NY, OR, RI, WA are coded 1). |
| `weakening_amendments` | `weakening_amendments` | 1 if the state has amended the model code in ways that reduce stringency (MI, OH are coded 1 per ACEEE). |
| `no_statewide` | `no_statewide_code` | 1 if the state has no mandatory statewide commercial energy code (AK, SD coded 1; AZ mostly home-rule). |
| `lag_model_code_yrs` | `lag_model_code_yrs` | Frontier vintage in that year minus the state's own vintage. `0` = up to the frontier; higher = more behind. Computed per year so "frontier" shifts as states upgrade. |

**Historical vintages are now backfilled.** The panel walks
`state_code_transitions.csv` — a hand-built table of every commercial code
transition sourced from the DOE Building Energy Codes Program state portal
pages (`energycodes.gov/status/states/<state>`) — and carries the
most-recent-prior vintage into each state-year cell. Coverage:

| Year | States with known vintage |
|---|---|
| 2010 | 38/51 |
| 2015 | 41/51 |
| 2020 | 42/51 |
| 2025 | 43/51 |

The ~8 states with no vintage in any year are the no-statewide-code states
(AK, AZ, KS, MS, MO, ND, SD, WY), which is expected. For them,
`iecc_comm_vintage` is blank and `no_statewide_code = 1`.

**Not yet built.** `zepi_commercial` — ACEEE zEPI continuous stringency score.
The ACEEE Commercial Code page does not expose zEPI numerically in the public
database view; obtaining the scored values requires either the ACEEE State
Scorecard PDFs (one per year) or the New Buildings Institute Comm. Energy
Code Scorecard. The ordinal `iecc_comm_vintage` + `lag_model_code_yrs`
variables here serve as a reasonable substitute until zEPI is added.

### Block B: Building Performance Standards (jurisdiction-level)

From `bps_jurisdictions.csv` and `bps_city_panel_2015_2025.csv`:

| Codebook var | CSV column | Notes |
|---|---|---|
| `bps_adopted` | `bps_adopted` | 1 from `bps_year_enacted` onward, else 0. |
| `bps_effective_year` | `bps_first_compliance_year` | First year a covered building must actually comply with a numeric target. Distinct from `bps_year_enacted`. |
| `bps_metric` | `bps_metric` | EUI, GHG/carbon intensity, or ENERGY STAR score. |
| `bps_covered_sqft` | `bps_covered_threshold_comm_sqft`, `_mf_sqft`, `_public_sqft` | Threshold square footage varies by building type. Three columns preserve the per-type threshold. |
| `bps_ratchet` | `bps_ratchet` | 1 if the ordinance tightens targets on a scheduled cycle. All 16 current adopters code as 1. |
| `bps_penalty_strength` | `bps_penalty_type` | All 16 adopters impose monetary fines or alternative compliance payments. |
| `bps_penalty_per_sqft` | `bps_penalty_per_sqft` | **Quantitative $/sqft penalty where specified in the ordinance.** Washington State $1/sqft/yr Tier 1; DC max $10/sqft (capped $7.5M/property); Denver $10/sqft for never-benchmarked. Blank if the ordinance uses a different unit. |
| `bps_penalty_per_tco2e` | `bps_penalty_per_tco2e` | **Quantitative $/metric ton CO2e penalty where specified.** NYC LL97 $268/tCO2e; Boston BERDO $234/tCO2e alternative compliance payment; Maryland $230/tCO2e from 2030 (tied to EPA social cost of carbon). |
| `bps_covers_municipal` | `bps_covers_municipal` | 1 if the ordinance explicitly covers city-owned buildings. NYC (LL97) coded 0 because municipal buildings are subject to LL97 via separate pathway; all others coded 1. |
| `bps_compliance_deadline_1` | `bps_first_compliance_year` | Same column — first compliance target year. |
| `bps_coalition_member` | `bps_coalition_member` | From `bps_coalition_members.csv`. 1 from `bps_coalition_joined_year` onward. |
| `bps_coalition_launch_day` | `bps_coalition_launch_day` | 1 if the jurisdiction was one of the 33 original members of the White House BPS Coalition announced January 21, 2022 (2 states + 31 cities/counties per the Biden White House fact sheet). |

**Coalition membership as an anticipation proxy.** The launch-day cohort is
now coded distinctly from later joiners. The 33 launch-day members are the
cohort the White House fact sheet explicitly names (Colorado, Washington
state + 31 cities/counties: Ann Arbor, Annapolis, Aspen, Atlanta, Boston,
Cambridge, Chicago, Chula Vista, Columbus, Denver, Evanston, Fort Collins,
Grand Rapids, Ithaca, Kansas City, Los Angeles, Milwaukee, Montgomery
County, New York City, Orlando, Philadelphia, Pittsburgh, Portland, Prince
George's County, Reno, Sacramento, St. Louis, San Francisco, Savannah,
Seattle, Washington DC). Use `bps_coalition_launch_day == 1 AND bps_adopted == 0`
to identify cities that publicly committed to BPS without having enacted one
— a clean anticipation indicator.

### Block C: Benchmarking & Audit Requirements (precursors)

From `benchmarking_ordinances.csv` and `benchmarking_city_panel_2008_2025.csv`:

| Codebook var | CSV column | Notes |
|---|---|---|
| `benchmarking_adopted` | `benchmarking_adopted` | 1 from `benchmarking_year_enacted` onward. |
| `benchmarking_year` | `benchmarking_year_enacted` | Year the ordinance was enacted. Earliest is DC 2008 (Clean & Affordable Energy Act). |
| `benchmarking_threshold_sqft` | `benchmarking_threshold_sqft` | Building size threshold in square feet. |
| `audit_tuneup_req` | `audit_tuneup_req` | 1 if the ordinance (or a companion ordinance) requires periodic audits or retro-commissioning. NYC (via LL87), Boston, Atlanta, Berkeley, Salt Lake City, Austin, Montgomery County, Boulder, Orlando, SF are coded 1. |
| `eers_state` | *not here* | State Energy Efficiency Resource Standard — already flagged in `variable_list_audit.md` as C12 (ACEEE state scorecard). Out of scope for this folder. |

**The BPS-is-grown-from-benchmarking pattern.** Several jurisdictions in
`benchmarking_ordinances.csv` also appear in `bps_jurisdictions.csv` with
`also_has_bps = 1`. These are the cases where a benchmarking ordinance was
later amended or superseded by a BPS (Boston 2013→2021, NYC 2009→2019, DC
2008→2018, Montgomery County 2014→2022, Cambridge 2014→2023, St. Louis
2017→2020, Colorado 2021 combined, Washington State 2019 combined, Evanston
2016→2025). The benchmarking ordinance typically precedes the BPS by 3–7
years and builds the data infrastructure that makes the BPS enforceable.
This is the sequencing you want to exploit in an event study.

## Sources

Every field is traceable to one of the following:

1. **IMT BPS Matrix, January 2026.** `https://imt.org/wp-content/uploads/2021/01/BPS-Matrix-January-2026.pdf` — the authoritative cross-section of all US BPS jurisdictions with year enacted, law ID, metric, thresholds, compliance cycle, and enforcement info. Block B and the `source` column of `bps_jurisdictions.csv` point to this. Extracted via pypdf.
2. **DOE Building Energy Codes Program — State Portal Pages.** `https://www.energycodes.gov/status/states/<state>` — historical commercial and residential code adoption timelines for every US state and DC. This is the primary source for `state_code_transitions.csv`. Each state's page lists every code transition back to the 1970s with effective and adoption dates.
3. **ACEEE State Commercial Energy Code Database.** `https://database.aceee.org/state/commercial-code` — current commercial code vintage and qualitative flags (home-rule, preemption, stretch code availability, weakening amendments). Block A cross-section (`state_iecc_current.csv`).
4. **Biden White House Fact Sheet on BPS Coalition, January 21, 2022.** `https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2022/01/21/fact-sheet-biden-harris-administration-launches-coalition-of-states-and-local-governments-to-strengthen-building-performance-standards/` — the authoritative list of the 33 launch-day members (Colorado, Washington + 31 cities/counties). Used to code `launch_day_member`.
5. **National BPS Coalition participating jurisdictions.** `https://nationalbpscoalition.org/` — list of states, cities, and counties participating in the Coalition as of 2025. Post-launch additions are coded with approximate `joined_year`.
6. **Primary ordinance records for BPS penalty amounts.** DC DOEE BEPS rules (max $10/sqft, $7.5M cap); WA HB 1257 (Tier 1 $5000+$1/sqft/yr); NYC LL97 ($268/tCO2e); Boston BERDO 2.0 ($234/tCO2e ACP); Maryland COMAR 26.28 ($230/tCO2e); Colorado HB21-1286 ($2000/$5000 monthly civil penalties); Denver Office of Climate Action Energize Denver Rules ($0.35-0.70/kBtu over target + $10/sqft for never-benchmarked); Montgomery County Bill 16-21 (Class A violation max $1000 + 6 months jail).
7. **Primary ordinance records for benchmarking ordinances.** Each row is traced to either the municipal code citation (e.g. `§9-3402 Philadelphia Code`, `SMC 22.920.010 Seattle`, `DC Law 17-250`) or the IMT news release on passage. The `source` column in `benchmarking_ordinances.csv` records the specific citation.

## How to merge into the green-bond city-year dataset

The existing green-bond dataset is city-year. Recommended merges:

```python
# Tier 1 (state-level, merged via city's state):
merge_key = city.state_abbr + year
panel = city_year.merge(state_iecc_panel, on=['state_abbr','year'], how='left')

# BPS (direct city-level merge):
panel = panel.merge(bps_city_panel, on=['jurisdiction','state_abbr','year'], how='left')
# Fill NaN bps_adopted with 0 for cities NOT in bps_city_panel (never-treated)

# Benchmarking (same treatment):
panel = panel.merge(benchmarking_city_panel, on=['jurisdiction','state_abbr','year'], how='left')
panel['benchmarking_adopted'] = panel['benchmarking_adopted'].fillna(0)
```

`jurisdiction` and `state_abbr` in the two city panels should match the city
identifier in the green-bond dataset. Spot-check any name mismatches (e.g.
"St. Louis" vs "Saint Louis", "Washington" vs "District of Columbia").

## Known gaps / next steps

Originally this folder had six open gaps; four are now filled. What remains:

1. **ACEEE zEPI commercial continuous scores** — the ordinal
   `iecc_comm_vintage` and the derived `lag_model_code_yrs` are now in place
   and should serve as a good substitute. A continuous zEPI score would still
   require parsing ACEEE State Scorecard PDFs (one per year). Lower priority
   now that the ordinal measure is clean.
2. **No-statewide-code states** — 8 states (AK, AZ, KS, MS, MO, ND, SD, WY)
   have no mandatory statewide commercial code and therefore `iecc_comm_vintage`
   is blank in every year. For cities in these states the relevant stringency
   measure is the local adoption, which is not covered in this panel. If a
   green-bond analysis includes cities in those states, treat them as a
   separate risk-set and use `home_rule = 1` as the analytic control.
3. **DSIRE EERS state panel** — not built here; tracked in
   `variable_list_audit.md` as C12.

### Gaps now filled (2026-04 update)

- ✅ **Historical IECC vintages** — backfilled from DOE BECP state portal
  pages for all 50 states + DC via `state_code_transitions.csv`. Vintage
  coverage is now 38/51 states in 2010 rising to 43/51 by 2025.
- ✅ **BPS per-sqft and per-tCO2e penalty amounts** — now coded as two
  quantitative columns (`bps_penalty_per_sqft`, `bps_penalty_per_tco2e`)
  for the 6 jurisdictions whose ordinances specify dollar figures: DC ($10/sqft),
  Washington State ($1/sqft/yr), Denver ($10/sqft non-reporters, $0.35-0.70/kBtu
  over target), NYC ($268/tCO2e), Boston ($234/tCO2e ACP), Maryland ($230/tCO2e).
- ✅ **BPS Coalition launch-day flag** — the 33 original members from the
  Biden White House fact sheet of January 21, 2022 are now flagged via
  `launch_day_member = 1`, with later joiners coded with their estimated
  `joined_year`. Use the launch-day flag as a clean anticipation indicator.
- ✅ **Audit / tune-up ordinance detail** — NYC LL87 detail (10-year cycle by
  tax-block last digit, $3k first-year / $5k subsequent missed-year penalty)
  and Boston BERDO 1.0 detail (5-year energy action requirement, 2013-2021)
  are now captured in `benchmarking_ordinances.csv` notes.
