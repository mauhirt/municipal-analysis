# Climate Policy Controls — Sourced Raw Data

This directory contains the provenance-tracked raw source files used to build
`processed/climate_policy_controls_v2.csv` via `pipeline/17_build_climate_policy_controls_v2.py`.

The goal is **peer-review replicability**: every non-zero value in the
processed panel must be traceable to a row in one of the files here, and
every row cites a primary source (`source_name`, `source_url`, `access_date`,
`verification_status`).

## File inventory

| File | Variables produced | Coverage | Primary source | Verification |
|---|---|---|---|---|
| `rggi_auction_prices.csv` | `state_rggi_price_usd` | 2008-01 to 2025-12, 70 quarterly auctions | RGGI Auction Results page | **fetched live** 2026-04-10 |
| `rggi_member_states.csv` | `state_rggi_member` | 10 founding states + VA/NJ transitions | RGGI Program Overview and Design | **fetched live** 2026-04-10 |
| `state_pcap_2024.csv` | `state_pcap_2024` | 50 states + DC | EPA CPRG PCAP Directory | **fetched live** 2026-04-10 |
| **`ca_capandtrade_auction_prices.csv`** (NEW) | `state_catp_price_usd` | 53 auctions, Nov 2012 to Nov 2025 | CARB Summary of CA-Quebec Joint Auction Settlement Prices and Results PDF | **fetched live** 2026-04-10 via curl+pdftotext |
| **`wa_capandinvest_auction_prices.csv`** (NEW) | `state_wci_price_usd` | 12 auctions, Feb 2023 to Dec 2025 | WA Ecology Auction Summary Report PDFs (12 individual reports) | **fetched live** 2026-04-10 via curl+pdftotext |
| `muni_aaa_yield_annual.csv` | `muni_aaa_yield` | 2007-2025 | S&P Muni AAA 10Y / Bloomberg BVAL AAA 10Y | 2013-2023 preserved from original raw file; 2007-2012 and 2024-2025 **transcribed**. FRED WSHY blocked in environment (503). See VERIFICATION_LOG.md |
| `state_rps_history.csv` | `state_rps_active`, `state_rps_target_pct` | 1983-2025 enactment milestones across 38 states | LBNL Berkeley Lab 2024 RPS Status Update (Barbose) + DSIRE | **transcribed** — LBNL/NCSL/DSIRE all blocked (403/Cloudflare). EIA "28 states + DC" headline count verified as consistent. See VERIFICATION_LOG.md |
| `state_climate_plan_legacy.csv` | `state_climate_plan_legacy` | 31 states with pre-2024 statewide climate action plans | C2ES State Climate Policy Database | **transcribed** — C2ES interactive database requires JavaScript. C2ES "33 states" summary count verified as consistent. See VERIFICATION_LOG.md |
| `c40_us_members.csv` | `c40_member` | 25 US C40 member cities with first-observed year | c40.org Our Cities + original raw file | **raw_anchor** — first-observed year from raw 2013-2023 |
| `mcpa_signatory_static.csv` | `mcpa_signatory_static` | 54 US Conference of Mayors Climate Protection Agreement signatories (static) | Original raw/climate/climate_policy_controls.csv 2013-2023 snapshot | **raw_snapshot** — time-invariant |
| `iclei_usa_static.csv` | `iclei_member_static` | 43 ICLEI USA member cities (static) | Original raw/climate/climate_policy_controls.csv 2013-2023 snapshot | **raw_snapshot** — time-invariant |

**Superseded (kept for reference):**
- `ca_capandtrade_auction_prices_annual.legacy.csv` — previous transcribed annual averages, now replaced by auction-level CSV
- `wa_capandinvest_auction_prices_annual.legacy.csv` — same

See `VERIFICATION_LOG.md` in this directory for the full per-source log of
every URL we attempted to fetch, the HTTP results, and the verification
pass summary (2026-04-10).

## Verification status codes

- **`fetched`** — Value was pulled from the cited URL by automated fetch on the
  access_date recorded. Independently re-fetchable.
- **`raw_file`** — Value was preserved exactly from `raw/climate/climate_policy_controls.csv`
  which is the original compiled file supplied at the start of the project.
- **`raw_anchor`** — Derived from the raw file's 2013-2023 window (e.g. union or
  first-observed); the underlying primary source is cited but the specific value
  depends on the original compilation.
- **`raw_snapshot`** — Time-invariant variable derived from the raw file's
  2013-2023 window; treated as a city-level or state-level characteristic.
- **`transcribed`** — Value was typed in from the assistant's domain knowledge
  of the cited primary source because automated fetch from that source failed
  in the working environment (403/404 from LBNL, Wikipedia, C40, DSIRE, CARB
  PDFs, WA Ecology). **Reviewer action required**: each transcribed row must
  be spot-checked against the cited URL before submission to a journal.

## Known fetch blockers (as of 2026-04-10)

The following primary sources returned 403 or 404 from this working environment:

- FRED CSV downloads (`fred.stlouisfed.org/graph/fredgraph.csv` endpoints)
- C40.org pages (c40.org/cities, c40.org/our-cities, c40.org/about-c40)
- LBNL Berkeley Lab publication PDFs (emp.lbl.gov/publications/...)
- Wikipedia article fetches (403 for all)
- DSIRE state program pages (programs.dsireusa.org, dsireusa.org/resources/summary-maps/...)
- CARB Summary of Auction Settlement Prices PDFs (ww2.arb.ca.gov/sites/default/files/...)
- Washington Ecology auction results direct URLs (apps.ecology.wa.gov/...)
- NCSL RPS page (ncsl.org/energy/state-renewable-portfolio-standards...)
- SIFMA municipal bond statistics (sifma.org/...)

For final journal submission the `transcribed` rows should be refreshed by
re-running the fetch from a less-restricted network (or by downloading the
cited PDFs locally and transcribing).

## How to verify independently

1. For each row in any CSV where `verification_status == 'transcribed'`, open
   the `source_url` in a browser and cross-check the value.
2. For `fetched` rows, the same URL should still return the same data (RGGI's
   auction results and EPA's PCAP directory are stable publications).
3. For `raw_file` and `raw_snapshot` rows, the anchor is `raw/climate/climate_policy_controls.csv`
   which is committed to this repository.

## Version

Initial commit: 2026-04-10. Generated alongside `pipeline/17_build_climate_policy_controls_v2.py`.
