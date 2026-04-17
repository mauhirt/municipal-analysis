# Claude Code Task: DOT Discretionary Grant Panel for the 578-City Green Bond Dataset

## Objective

Build a city-year panel of USDOT discretionary grant receipts (2009–2025) merged to the existing 578-city green bond panel. The output feeds into the "When Do Red and Blue Go Green?" paper as (a) a control for federal capital inflows in the fiscal-necessity variable family, and (b) a robustness check for the Republican mayor / ESG assurance coefficient.

**Scope discipline:** This is a *targeted* integration, not a comprehensive DOT scrape. Stay within the programs listed below. Do not expand scope without checking back.

---

## Data source

USAspending.gov bulk download API (no key required).

- API base: `https://api.usaspending.gov/api/v2/`
- Bulk download endpoint: `POST /api/v2/download/awards/`
- Search endpoint (for paginated fetch): `POST /api/v2/search/spending_by_award/`
- Award-level detail: `GET /api/v2/awards/{award_id}/`

Docs: https://api.usaspending.gov/ and https://github.com/fedspendingtransparency/usaspending-api

Prefer the **bulk download endpoint** for fiscal years. It returns a CSV ZIP with one row per prime award transaction. For diagnostics/spot-checks, use the search endpoint.

---

## Programs to pull

Use the `program_activities` / `assistance_listings` (CFDA) filter where possible. Scope:

| Program | CFDA / Notes |
|---|---|
| RAISE / BUILD / TIGER (National Infrastructure Investments) | 20.933 |
| INFRA / Mega / Nationally Significant Freight & Highway | 20.934, 20.942 |
| Safe Streets and Roads for All (SS4A) | 20.939 |
| Reconnecting Communities Pilot (RCP) | 20.940 |
| Charging and Fueling Infrastructure (CFI) — community track | 20.942 discretionary / check current listing |
| Low or No Emission Vehicle Program (Low-No) | 20.526 |
| Bus and Bus Facilities competitive | 20.526 |
| Pilot Program for TOD Planning | 20.500 |

If a CFDA code returns nothing or is ambiguous, fall back to keyword filtering on `award_description` + `awarding_sub_agency_name` (FHWA, FTA, FRA, MARAD, OST). Log any program where CFDA coverage is uncertain.

**Time period:** FY2009–FY2025 (action_date between 2008-10-01 and 2025-09-30).

**Award types:** Prime awards, type codes `02`, `03`, `04`, `05` (grants and direct payments / cooperative agreements).

---

## Pipeline

Build it in a new directory under the existing project repo, e.g. `data/dot_grants/`. Reuse existing project conventions (Python, pandas, logging). Match the EPA ECHO script structure if one exists in the repo.

### Step 1 — Fetch

`fetch_dot_awards.py`

- Loop over the program list above. For each program, POST to `/api/v2/download/awards/` with:
  - `prime_award_types`: `["02","03","04","05"]`
  - `time_period`: `[{"start_date":"2008-10-01","end_date":"2025-09-30","date_type":"action_date"}]`
  - `agencies`: `[{"type":"awarding","tier":"toptier","name":"Department of Transportation"}]`
  - Program filter via `program_activities` or `assistance_listings` as applicable
- Poll the returned `status_url` until `status == "finished"`, then download `file_url`.
- Unzip to `data/dot_grants/raw/{program}/`.
- Rate limit: one concurrent download request at a time; the API is slow (2–10s per page on search, minutes for bulk).
- Idempotency: skip refetch if the program's raw CSV exists and is newer than 30 days. Add a `--refresh` CLI flag.
- Log each request's row count, date range, and file size to `data/dot_grants/logs/fetch.log`.

### Step 2 — Clean and normalize

`clean_dot_awards.py`

Reduce to the columns we actually need:

- `award_id_fain` (grant) / `award_id_uri`
- `assistance_listing_number` (CFDA)
- `awarding_agency_name`, `awarding_sub_agency_name`
- `recipient_name`, `recipient_uei`, `recipient_duns`
- `recipient_city_name`, `recipient_state_code`, `recipient_zip_5`
- `primary_place_of_performance_city_name`, `primary_place_of_performance_state_code`, `primary_place_of_performance_zip_5`, `primary_place_of_performance_county_fips`
- `action_date`, `period_of_performance_start_date`, `period_of_performance_current_end_date`
- `federal_action_obligation`, `total_obligated_amount`, `total_outlayed_amount`
- `award_description`
- `business_types_description` (to flag "city or township government")

Then:

1. Parse `action_date` → `fiscal_year` (Oct–Sep).
2. Deduplicate on `award_id_fain` keeping the max `total_obligated_amount` per fiscal year.
3. Tag `program` (RAISE/INFRA/SS4A/RCP/CFI/Low-No/BBF/TOD) via CFDA + keyword rules. Store the rule that matched in a `program_match_method` column for audit.
4. Filter to recipients where `business_types_description` contains "City", "Township", "Municipal", or "Local Government" — OR where `recipient_name` matches a city in the 578-city crosswalk (next step). Keep a separate file for state DOTs, MPOs, transit authorities, and ports for possible later use, but do not merge those into the main city panel.

Write outputs to `data/dot_grants/clean/dot_awards_clean.parquet`.

### Step 3 — Merge to the 578-city panel

`merge_to_578.py`

**Deterministic matching only. No fuzzy matching.** USAspending recipient and place-of-performance strings are noisy, so the match key is FIPS codes, not names.

USAspending returns `primary_place_of_performance_county_fips` and a state code on each award. The 578-city panel already has city FIPS codes (Census Place GEOID, 7 digits: 2-digit state + 5-digit place). The challenge: USAspending does not consistently populate Census Place GEOID — place of performance gives county FIPS + city name, not place FIPS directly.

Three-tier deterministic strategy:

**Tier 1 — exact Place GEOID match (preferred).** USAspending *does* return `primary_place_of_performance_code` for some records, which is a 7-digit Census Place code (state FIPS + place FIPS). When present, join directly on Place GEOID to the 578-city panel. This is exact and unambiguous.

**Tier 2 — (state FIPS, normalized city name) exact match.** When Place GEOID is missing:
- Normalize: lowercase, strip "city of", "town of", "township of", "village of", trailing state abbreviations, and all punctuation.
- Build the same normalized key for the 578-city panel.
- Require **exact** string equality after normalization, within the same state FIPS.
- If a normalized name maps to multiple cities in the same state (e.g. "Springfield" in a state with multiple Springfields — unlikely within a single state but check), flag to the review queue, do not match.

**Tier 3 — recipient-name match, city-government entities only.** Some awards list a municipal department as recipient without a clean place of performance (e.g. "Chicago Department of Aviation"). For these:
- Require `business_types_description` to contain "City", "Township", "Municipal", or "County" government.
- Require recipient state + recipient city (normalized) to exactly match a 578-city record.
- Apply the governance standard already used for green bond issuers: only assign if the entity is a unit of the city government (not an independent authority with its own board). Use the existing issuer classification file as the authority — if the entity is flagged NOT_IN_578 there, it stays out here.

**Everything that doesn't match one of these three tiers goes to a review queue, not the panel.** No fuzzy fallback. The review queue is a CSV with columns: `award_id`, `recipient_name`, `place_of_performance_city`, `place_of_performance_state`, `total_obligated_amount`, `program`, `award_description`, `reason_unmatched`. Sort descending by obligated amount so manual review time goes to the dollars that matter.

Expectation: tiers 1+2 should capture ≥95% of dollars on their own. The review queue is for the long tail, and I will decide case-by-case whether to add manual overrides to a crosswalk file (`data/dot_grants/manual_overrides.csv`) that the merge script consumes on the next run.

### Step 4 — Aggregate to city-year

`aggregate_city_year.py`

For each (city_id, fiscal_year), produce:

- `dot_total_obligated` — sum across all programs
- `dot_total_outlayed`
- `dot_n_awards`
- One column per program: `dot_{program}_obligated`, `dot_{program}_n_awards`
- `dot_any_award` (0/1 flag)
- Three-year rolling sum: `dot_total_obligated_3yr`

Left-join this onto the existing city-year panel. Zero-fill missing years (city had no awards, not missing data).

Output: `data/dot_grants/clean/dot_city_year_panel.parquet` and a copy integrated into the master panel.

### Step 5 — Audit and sanity checks

`audit_dot_panel.py`

Report:

1. Total obligated by fiscal year vs. FHWA's published TIGER/BUILD/RAISE totals (should be in the ~$14.4B ballpark cumulative through FY2024 across RAISE alone).
2. Top 20 cities by cumulative receipts — spot check these are plausible (expect NYC, Chicago, LA, Seattle, Philadelphia, etc. near the top).
3. Share of 578 cities with at least one DOT award over the panel period (expect 60–80%).
4. Coverage by program: how many awards per program, median award size.
5. **Match diagnostics**: rows matched via Tier 1 (Place GEOID), Tier 2 (state + normalized name), Tier 3 (recipient entity); rows sent to review queue; share of *dollars* captured by each tier. Flag if tiers 1+2 capture less than 95% of dollars — that would signal a data problem worth investigating before trusting the merge.
6. Flag any fiscal year with zero awards (likely a fetch failure).

Write a short markdown report to `data/dot_grants/audit/summary.md` with the above, plus the top 50 rows of the review queue by obligated amount.

---

## Deliverables

```
data/dot_grants/
├── raw/                          # untouched API pulls, one subdir per program
├── clean/
│   ├── dot_awards_clean.parquet  # award-level after Step 2
│   ├── dot_city_year_panel.parquet  # city-year after Step 4
│   └── review_queue.csv          # unmatched awards for manual review
├── manual_overrides.csv          # my hand-curated award_id → city_id mappings (populated by me, read by merge script)
├── logs/
│   └── fetch.log
├── audit/
│   └── summary.md
└── scripts/
    ├── fetch_dot_awards.py
    ├── clean_dot_awards.py
    ├── merge_to_578.py
    ├── aggregate_city_year.py
    └── audit_dot_panel.py
```

Plus: a one-page summary in the paper's methods appendix describing the pipeline, match rate, and the sample of awards covered.

---

## Do not

- Do not pull state DOT, MPO, transit authority, or port authority awards into the main city panel. Keep them in a separate file for later.
- Do not add programs beyond the list above without flagging it.
- Do not use fuzzy string matching anywhere in the pipeline. Exact deterministic matches only.
- Do not use recipient_name as the primary match key — place of performance is cleaner.
- Do not scrape the USAspending website HTML. The API is sufficient.

## Check back with me before

- Running the full fetch if the first program's pull exceeds 500k rows (likely a filter error).
- Expanding beyond the listed programs.
- Integrating the aggregated panel into the master city-year file — I want to review the audit report first.
- Adding anything to `manual_overrides.csv` — that file is populated by me, not by the script.

## Time budget

Target: one working day for a clean v1. Two days if the merge gets messy. If you're over two days, stop and write up what's blocking.
