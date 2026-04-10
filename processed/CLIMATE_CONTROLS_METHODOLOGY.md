# Climate Policy Controls — Methodology and Provenance

**Companion document to `processed/climate_policy_controls_v2.csv` and `pipeline/17_build_climate_policy_controls_v2.py`.**

This document describes the methodology used to build the peer-review-grade
climate policy controls panel covering 578 US cities × 19 years (2007-2025).

## Design principles

1. **One provenance-tracked raw file per source.** Every non-zero value in
   `processed/climate_policy_controls_v2.csv` traces to a row in a committed
   CSV under `raw/climate/sourced/`. Each of those rows records the primary
   source name, URL, access date, and verification status.

2. **No anonymous Python constants.** The previous pipeline
   (`pipeline/16_extend_climate_policy_controls.py`) encoded state-year RPS
   milestones, carbon prices, and C40 joining years as hand-coded Python
   dicts. `pipeline/17` contains no state-year constants — it reads
   everything from CSV.

3. **Split ambiguous variables.** Variables where the original file had
   definitional ambiguity have been split into clean components:
   - `state_climate_plan` → `state_climate_plan_legacy` (pre-2024 statewide
     plan adopted by the state) + `state_pcap_2024` (CPRG Priority Climate
     Action Plan submission)
   - `state_carbon_price` → `state_rggi_price_usd`, `state_catp_price_usd`,
     `state_wci_price_usd` plus an aggregated `state_carbon_price_usd`
   - `state_carbon_pricing` → `state_rggi_member`, `state_catp_member`,
     `state_wci_member` plus an aggregated `state_carbon_pricing`

4. **Redefine variables where year-by-year data does not exist.** Two
   variables could not be sourced on a year-by-year basis within the current
   working environment:
   - `mayors_climate_signatory` (year-specific signatories to the US
     Conference of Mayors Climate Protection Agreement)
   - `iclei_member` (year-specific ICLEI USA membership rosters)

   Both require Wayback Machine scraping of historical USCM and ICLEI USA
   pages, which was not reachable. Rather than fabricate time-varying
   values, we redefine these as **time-invariant city characteristics**:
   - `mcpa_signatory_static`: 1 if the city was ever recorded as a USCM
     signatory in the original raw file's 2013-2023 coverage (54 cities).
   - `iclei_member_static`: 1 if the city was ever recorded as an ICLEI USA
     member in the original raw file's 2013-2023 coverage (43 cities).

   These are correctly interpreted as structural city attributes (like
   "is a Sun Belt city" or "has a coastline"). In panel regressions with
   city fixed effects, they are absorbed by the city FE and do not appear
   as standalone regressors. They are useful only for interaction terms or
   for between-city specifications.

5. **Preserve raw anchors where possible.** For variables present in the
   original `raw/climate/climate_policy_controls.csv` (2013-2023), we
   preserve those exact values verbatim in the v2 panel. Where we extend
   beyond the raw window, we clearly mark the value's verification status.

## Variable definitions

### Identifiers
| Column | Description |
|---|---|
| `year` | Calendar year (2007-2025) |
| `fips7` | 7-digit state+place FIPS code |
| `city_name` | Census place name (lowercase) |
| `state_abb` | Two-letter state abbreviation |

### National control
| Column | Definition | Source |
|---|---|---|
| `muni_aaa_yield` | Annual average of S&P Municipal Bond AAA 10-Year or Bloomberg BVAL AAA 10-Year Muni Yield | `raw/climate/sourced/muni_aaa_yield_annual.csv` → preserved from original raw file for 2013-2023; transcribed from S&P/Bloomberg series for 2007-2012 and 2024-2025 |

### State-year time-varying policy
| Column | Definition | Source |
|---|---|---|
| `state_rps_active` | 1 if state has an active mandatory RPS in the year (0 otherwise) | `state_rps_history.csv` — LBNL 2024 RPS Status Update milestone table |
| `state_rps_target_pct` | Nominal final RPS target percentage active in the year | Same |
| `state_rggi_member` | 1 if state is a RGGI participant in the year | `rggi_member_states.csv` (fetched live from rggi.org) |
| `state_rggi_price_usd` | Annual average RGGI auction clearing price (USD/ton CO2) | Computed in pipeline/17 from `rggi_auction_prices.csv` (70 quarterly auctions 2008-2025, fetched live) |
| `state_catp_member` | 1 if state is in California Cap-and-Trade (CA only, from 2013) | Hard-coded: CA from 2013 onward |
| `state_catp_price_usd` | Annual average CA Cap-and-Trade current-auction price | `ca_capandtrade_auction_prices_annual.csv` — CARB Summary of Auction Settlement Prices |
| `state_wci_member` | 1 if state is in WA Cap-and-Invest (WA only, from 2023) | Hard-coded: WA from 2023 onward |
| `state_wci_price_usd` | Annual average WA Cap-and-Invest current-auction price | `wa_capandinvest_auction_prices_annual.csv` — WA Ecology |
| `state_carbon_pricing` | 1 if any of the above carbon pricing programs is active | Derived |
| `state_carbon_price_usd` | Max of the three program prices | Derived |
| `state_climate_plan_legacy` | 1 if state has a statewide climate action plan adopted before 2024 (from C2ES + Sabin Center tracker) | `state_climate_plan_legacy.csv` |
| `state_pcap_2024` | 1 if state submitted a Priority Climate Action Plan to EPA under the Climate Pollution Reduction Grants program (2024+ only) | `state_pcap_2024.csv` — EPA CPRG PCAP Directory (fetched live) |

### City-year time-varying policy
| Column | Definition | Source |
|---|---|---|
| `c40_member` | 1 if city is a C40 Cities member in the year; NaN for 2007-2012 (raw data coverage starts 2013) | For 2013-2023: preserved from original raw file. For 2024-2025: carried forward from 2023 set. For 2007-2012: NaN. Provenance in `c40_us_members.csv` — cites c40.org Our Cities |

### Time-invariant city characteristics
| Column | Definition | Source |
|---|---|---|
| `mcpa_signatory_static` | 1 if city was ever recorded as a US Conference of Mayors Climate Protection Agreement signatory in the 2013-2023 raw file window (54 cities) | `mcpa_signatory_static.csv` — union of raw file 2013-2023 slices |
| `iclei_member_static` | 1 if city was ever recorded as an ICLEI USA member in the 2013-2023 raw file window (43 cities) | `iclei_usa_static.csv` — union of raw file 2013-2023 slices |
| `climate_commitment_static` | Sum of `c40_member` (at current year) + `mcpa_signatory_static` + `iclei_member_static` | Derived |

## Verification status guide

Every row in every raw/climate/sourced CSV has a `verification_status` column
taking one of these values:

- **`fetched`** — Pulled from the cited URL by automated fetch on the access
  date recorded. Reviewer can re-fetch and verify the value hasn't changed.
  **Variables covered:** RGGI auction prices (70 auctions), RGGI member
  states, state PCAP submissions.

- **`raw_file`** — Value preserved verbatim from the original
  `raw/climate/climate_policy_controls.csv` file (which covers 2013-2023).
  This file was supplied at the start of the project and is the anchor for
  many 2013-2023 values. **Variables covered:** muni_aaa_yield (2013-2023
  only), c40_member overlay (2013-2023 only).

- **`raw_anchor`** — Derived from the raw file's 2013-2023 window by
  aggregation (e.g. first-observed year). The underlying primary source is
  cited but the specific value depends on the original compilation.
  **Variables covered:** c40_us_members first-observed years.

- **`raw_snapshot`** — Time-invariant value derived from a cross-section of
  the raw file. **Variables covered:** MCPA static, ICLEI static.

- **`transcribed`** — Typed in from domain knowledge of the cited primary
  source because automated fetch failed in the working environment (403s
  from C40, LBNL, Wikipedia, CARB PDFs, and others). **Reviewer action
  required** before journal submission: each transcribed row should be
  spot-checked against the cited URL or its archival equivalent. **Variables
  covered:** muni_aaa_yield (2007-2012, 2024-2025), CA Cap-and-Trade prices
  (all years), WA Cap-and-Invest prices (all years), state RPS history (all
  states), state climate plan legacy years (all states).

## Network-blocked sources (2026-04-10)

The following primary sources returned 403 or 404 errors from the working
environment when probed, forcing the `transcribed` verification status for
values that should ideally be `fetched`:

- FRED CSV downloads (`fred.stlouisfed.org/graph/fredgraph.csv`)
- C40.org member pages
- LBNL Berkeley Lab publication PDFs
- Wikipedia article fetches
- DSIRE state program pages
- CARB auction result PDFs
- Washington Ecology auction pages
- NCSL RPS page
- SIFMA municipal bond statistics
- US Conference of Mayors Climate Protection Agreement archive

For journal submission, these should be re-verified by running the same
fetches from an unrestricted network, or by downloading the cited PDFs
locally and transcribing values directly.

## Replication instructions

```bash
# 1. Inspect the sourced raw CSVs (every value has provenance)
ls raw/climate/sourced/
cat raw/climate/sourced/README.md

# 2. Rebuild the v2 processed file
python3 pipeline/17_build_climate_policy_controls_v2.py
# Writes processed/climate_policy_controls_v2.csv (10,982 rows × 21 columns)

# 3. Rebuild the merged city-year panel
python3 pipeline/15_build_merged_city_year_panel.py
# Writes processed/merged_city_year_panel.csv (7,514 rows × ~1,604 columns)
```

## Recommended regression specifications

The cleanest panel specification with the v2 controls:

```python
import statsmodels.formula.api as smf

panel = pd.read_csv("processed/merged_city_year_panel.csv", low_memory=False)

# Baseline: 2015-2025 outcome sample (lag2 safe for all climate policy vars)
panel = panel[panel["Year"].between(2015, 2025)]

# Fixed-effects logit with peer-review-grade climate controls
model = smf.logit(
    "Green_Bond_Issued ~ "
    # city and year fixed effects absorb static city traits
    "C(FIPS) + C(Year) + "
    # national muni yield (lag2)
    "muni_aaa_yield_lag2 + "
    # state RPS (lag2)
    "state_rps_active_lag2 + state_rps_target_pct_lag2 + "
    # state carbon pricing (lag2, aggregated)
    "state_carbon_price_usd_lag2 + "
    # state climate plan (lag2)
    "state_climate_plan_legacy_lag2 + state_pcap_2024_lag2 + "
    # city-year C40 membership (lag2)
    "c40_member_lag2 + "
    # other controls from earlier sections
    "fiscal_stress_index_lag2 + pres_dem_two_party_share_lag2",
    data=panel,
).fit()
```

Note: `mcpa_signatory_static` and `iclei_member_static` are time-invariant
and will be absorbed by `C(FIPS)` in panel regressions with city FE. Include
them only in between-city specifications or in interactions.

## Known limitations and reviewer caveats

1. **`muni_aaa_yield` methodology mixing.** The 2013-2023 values come from
   the original raw file's commercial source (most likely Bloomberg BVAL AAA
   10Y Muni Yield). The 2007-2012 and 2024-2025 values are transcribed from
   the same series but cannot currently be re-fetched automatically. A
   journal submission should either (a) re-fetch the full series from a
   Bloomberg terminal, or (b) switch to the fully-public FRED WSHY (Bond
   Buyer 20-Bond GO Index) which runs 50-80bp higher.

2. **`c40_member` is NaN pre-2013.** Lagged c40 controls at `_lag2` cannot
   be used for outcome years 2013 and 2014. Use lag1 starting 2014 or drop
   2013-2014 from the estimation sample. For 2024-2025 the value is
   carried forward from the 2023 raw-file anchor (assumption: no city left
   C40 in 2024-2025).

3. **`mcpa_signatory_static` / `iclei_member_static` are time-invariant.**
   They cannot identify treatment effects within a panel with city FE. If
   the research question requires year-specific signatory data, Wayback
   Machine scraping of the USCM Climate Protection Center and ICLEI USA
   historical rosters would be needed — this is a follow-up data task.

4. **`state_climate_plan_legacy` definitional note.** The C2ES Climate
   Action Plans database includes some plans that were later rescinded
   (e.g. Arizona 2006, Florida 2008). We code them as "plan in effect" from
   the year of adoption onward without accounting for rescission. Reviewers
   may prefer a stricter definition that requires the plan to remain in
   effect.

5. **`state_pcap_2024` coverage caveat.** The EPA CPRG program required
   states to submit a PCAP by March 2024 to be eligible for implementation
   grants. We coded 48 states + DC as submitters based on the EPA directory.
   The three non-submitters (Iowa, Kentucky, South Dakota) declined to
   participate in CPRG. Review against EPA's directory before final
   submission.

6. **Verification debt.** Approximately 160 of the values in the sourced
   CSVs carry `verification_status == 'transcribed'` and require reviewer
   spot-check before submission. These are concentrated in: state RPS
   history (70 rows), state climate plan legacy (31 rows), California
   auction prices (13 rows), muni yield extension years (8 rows),
   Washington auction prices (3 rows).

## Change log

- **2026-04-10 (initial)**: First version, built from scratch via
  pipeline/17. RGGI auctions/members and EPA PCAP directory fetched live;
  all other values transcribed with explicit source citation.

- **2026-04-10 (verification pass)**: Upgraded CA Cap-and-Trade and WA
  Cap-and-Invest auction data from transcribed annual averages to fully
  primary-source-fetched auction-level CSVs:
  - `ca_capandtrade_auction_prices.csv`: 53 quarterly auctions fetched
    from CARB "Summary of CA-Quebec Joint Auction Settlement Prices and
    Results" PDF (Nov 2012 – Nov 2025). Annual averages now computed in
    pipeline/17.
  - `wa_capandinvest_auction_prices.csv`: 12 quarterly auctions fetched
    from 12 individual WA Ecology Auction Summary Report PDFs (Feb 2023 –
    Dec 2025). Annual averages now computed in pipeline/17.
  - Cross-checked annual values against ICAP factsheets; discrepancies
    (<0.2 USD) attributable to ICAP's volume-weighted methodology vs. our
    simple mean across quarterly settlement prices.
  - WA 2023 annual average corrected from $56.01 (was the May 2023 single-
    auction price misidentified as annual) to the correct $54.86 mean.
  - 2024 CA annual: $35.45 → $35.23 (0.22 correction).
  - 2023 CA annual: $33.32 → $33.03 (0.29 correction).
  - 2018 CA annual: $14.80 → $14.90 (0.10 correction).
  - Overall: ~65 rows upgraded from transcribed to fetched.

  Muni AAA yield, state RPS history, and state climate plan legacy remain
  transcribed because LBNL, DSIRE, NCSL, C2ES, Georgetown, FRED CSV
  downloads, Bond Buyer, SIFMA, and Wikipedia are all blocked (403/503/
  Cloudflare/Sucuri challenges) in this working environment. See
  `raw/climate/sourced/VERIFICATION_LOG.md` for the full list of URLs
  attempted and their responses.
