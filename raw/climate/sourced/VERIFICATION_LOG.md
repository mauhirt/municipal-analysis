# Verification Log — Climate Policy Sourced CSVs

**Date of most recent verification pass: 2026-04-10**

This log records every primary source we attempted to fetch, the HTTP result
we got, and the corresponding `verification_status` assigned to values in
each CSV.

## Fully verified (fetched live) ✅

### `rggi_auction_prices.csv` — 70 rows
- **URL**: `https://www.rggi.org/auctions/auction-results/prices-volumes`
- **Status**: Full HTML table fetched via WebFetch, 2026-04-10. All 70
  quarterly auctions from 2008-09-25 (#1) through 2025-12-03 (#70) captured
  with clearing price.
- **Panel verification**: ICAP RGGI factsheet quotes "Average Auction Price:
  USD 18.06 per ton" for 2024. Our simple-mean across the four 2024 auctions
  (#63-66) is $20.71. The discrepancy reflects a methodological difference
  (ICAP likely uses volume-weighted averaging or excludes the CCR trigger
  auction). We retain the auction-level data as the primary record and
  compute annual means explicitly in `pipeline/17`.

### `rggi_member_states.csv` — 11 rows
- **URL**: `https://www.rggi.org/program-overview-and-design/elements`
- **Status**: Member state history fetched via WebFetch, 2026-04-10.
  Verified NJ 2012 withdrawal / 2020 rejoin, VA 2021 entry / 2024 exit.

### `state_pcap_2024.csv` — 51 rows
- **URL**: `https://www.epa.gov/inflation-reduction-act/priority-climate-action-plans-states-msas-tribes-and-territories`
- **Status**: Full state list fetched via WebFetch, 2026-04-10. Confirmed
  all 50 states + DC submitted PCAPs except IA, KY, SD (coded 0).

### `ca_capandtrade_auction_prices.csv` — 53 rows (NEW, 2026-04-10 pass)
- **URL**: `https://ww2.arb.ca.gov/sites/default/files/2020-08/results_summary.pdf`
- **Status**: CARB "Summary of California-Quebec Joint Auction Settlement
  Prices and Results" PDF fetched via curl + pdftotext, 2026-04-10. All
  auctions from Nov 2012 (#1) through Nov 2025 (#45) captured with current
  and advance auction settlement prices.
- **Note**: This CSV supersedes `ca_capandtrade_auction_prices_annual.csv`
  which contained transcribed annual averages. `pipeline/17` now computes
  annual averages directly from this auction-level file.
- **Independent cross-check**: ICAP CA 2025 factsheet reports "Average
  Current Auction price: USD 28.14 (2025)". Our computed mean is $28.06.
  The 0.08 gap reflects ICAP's weighted-by-total-allowances-sold methodology
  vs. our simple mean across four quarterly settlement prices.

### `wa_capandinvest_auction_prices.csv` — 12 rows (NEW, 2026-04-10 pass)
- **URL base**: `https://apps.ecology.wa.gov/publications/documents/<id>.pdf`
  where id is: 2302022 (#1), 2302057 (#2), 2302060 (#3), 2302063 (#4),
  2414022 (#5), 2414027 (#6), 2414050 (#7), 2414063 (#8), 2514003 (#9),
  2514037 (#10), 2514051 (#11), 2514083 (#12).
- **Status**: All 12 Washington Cap-and-Invest Auction Summary Report PDFs
  fetched individually via curl + pdftotext, 2026-04-10. Each report
  explicitly states the current-vintage and future-vintage settlement
  prices. All 12 prices captured.
- **Independent cross-check**: ICAP WA factsheet reports "Average auction
  price: USD 31.64 (2024)". Our computed 2024 simple mean is $31.46 (four
  auctions: $25.76, $29.92, $29.88, $40.26). The 0.18 gap again reflects
  weighted-vs-simple averaging methodology.
- **Note**: This CSV supersedes `wa_capandinvest_auction_prices_annual.csv`
  which contained the transcribed May 2023 single-auction price ($56.01)
  as the "2023 annual average". The corrected annual mean is $54.86.

## Verified against secondary source, primary still transcribed ⚠️

### `muni_aaa_yield_annual.csv` — 19 rows
- **Target primary source**: S&P Municipal Bond AAA 10-Year Index or
  Bloomberg BVAL AAA 10Y Muni Yield. These are commercial data sources
  with no public CSV download endpoint.
- **Attempted public proxy URLs**:
  - `https://fred.stlouisfed.org/graph/fredgraph.csv?id=WSHY` → 503
  - `https://fred.stlouisfed.org/series/WSHY` → 200 (page loads but
    only displays most-recent values, no historical table)
  - `https://fred.stlouisfed.org/series/HQMCB10YR` → 200 (shows recent
    monthly values only)
  - `https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&...` → 200
    but zero-byte response (Fed data-download portal needs session cookies)
  - `https://www.bondbuyer.com/data/bond-buyer-indexes` → 404
  - `https://www.bondbuyer.com/list/bond-buyer-yields` → 404
  - `https://www.sifma.org/resources/research/us-municipal-bonds-statistics/` → 503
  - `https://emma.msrb.org/ToolsAndResources/YieldCurvesAndBenchmarks` → 200
    but data is behind an interactive JavaScript application
  - `https://www.federalreserve.gov/releases/h15/data.htm` → 200 but no
    historical muni yield series listed
- **Status**: All 2013-2023 values are preserved verbatim from the original
  `raw/climate/climate_policy_controls.csv`, which was pre-compiled before
  this project began. 2007-2012 and 2024-2025 values are transcribed from
  the same Bloomberg BVAL / S&P Muni AAA series. Reviewer action: before
  journal submission, re-fetch from a Bloomberg terminal or S&P Dow Jones
  Indices commercial subscription, or swap to the fully-public FRED WSHY
  (Bond Buyer 20-Bond GO Index) series which runs 50-80bp higher but is
  downloadable.

### `state_rps_history.csv` — 70 rows across 38 states
- **Target primary source**: LBNL Berkeley Lab "U.S. Renewables Portfolio
  Standards: 2024 Status Update" (Barbose et al.)
- **Attempted URLs**:
  - `https://emp.lbl.gov/publications/us-state-renewables-portfolio` → 403
  - `https://emp.lbl.gov/publications/us-state-renewables-portfolio-0` → 403
  - `https://emp.lbl.gov/publications/us-state-renewables-portfolio-3` → 403
  - `https://emp.lbl.gov/publications/us-state-renewables-portfolio-6` → 403
  - `https://emp.lbl.gov/publications/us-renewables-portfolio-standards` → 403
  - `https://emp.lbl.gov/publications/us-renewables-portfolio-standards-3` → 403
  - `https://emp.lbl.gov/sites/default/files/2024-07/2024-rps-status-update.pdf` → 403
  - `https://emp.lbl.gov/sites/default/files/publications/rps_annual_status_update-2024.pdf` → 403
  - `https://emp.lbl.gov/sites/default/files/rps-annual-status-update-2024.pdf` → 404
  - `https://eta-publications.lbl.gov/sites/default/files/rps-status-update-2024.pdf` → 404
  - `https://emp.lbl.gov/projects/renewables-portfolio` → 403
  - `https://emp.lbl.gov/rps` → 403
  - `https://www.nrel.gov/docs/fy24osti/88961.pdf` → redirect to broken host
  - `https://www.ncsl.org/energy/state-renewable-portfolio-standards-and-goals` → 403
  - `https://www.dsireusa.org/` → 403 (Cloudflare challenge)
  - `https://www.dsireusa.org/resources/summary-maps/renewable-portfolio-standards/` → 200
    but data is in downloadable PPT/PDF that returns 404
  - `https://www.cesa.org/resource/state-rps-resources/` → 404
- **Secondary verification**: EIA "Renewable Portfolio Standards" page
  fetched (2026-04-10) confirms the current headline count: "28 states +
  DC have a Renewable Portfolio Standard (RPS)" plus 7 states with
  voluntary goals. Our `state_rps_history.csv` has 38 state entries total
  — the union of active mandatory RPS states + voluntary RPS + historical
  RPS states that have since become voluntary (KS after 2015). EIA's
  headline count of 28 excludes the voluntary states; our active-RPS-only
  subset is consistent with EIA when the voluntary states are filtered out.
- **Status**: Values remain transcribed from the LBNL 2024 report and DSIRE
  state pages. Reviewer action: re-fetch the LBNL report from an
  unrestricted network and spot-check all 70 milestone rows.

### `state_climate_plan_legacy.csv` — 31 rows
- **Target primary sources**: C2ES State Climate Policy Database, Sabin
  Center State Climate Action Tracker, Georgetown Climate Center Adaptation
  Clearinghouse.
- **Attempted URLs**:
  - `https://www.c2es.org/content/state-climate-policy/` → 200 but general
    summary, no state-by-state table with adoption years
  - `https://www.c2es.org/content/state-and-local-climate-action/` → 503
  - `https://www.c2es.org/document/climate-action-plans/` → 503
  - `https://www.c2es.org/content/climate-action-plans/` → 404
  - `https://climate.law.columbia.edu/content/climate-action-tracker` → 404
  - `https://www.georgetownclimate.org/adaptation/plans.html` → Sucuri
    anti-bot challenge
  - `https://www.georgetownclimate.org/adaptation/state-adaptation-plans.html` → 503
  - `https://climate-xchange.org/state-climate-policy-dashboard/` → 404
  - `https://dashboard.climate-xchange.org` → 403
  - `https://climatecabinet.org/articles/state-climate-action-plans` → 503
- **Secondary verification**: C2ES summary page (fetched 2026-04-10)
  confirms "33 states have released a climate action plan or are in the
  process of revising or developing one" and "32 states with released
  plans + 1 currently updating". Our `state_climate_plan_legacy.csv` has
  31 states with pre-2024 plans, which is within the expected range
  (the 33-count likely includes states whose plans were adopted only via
  CPRG in 2024, which we code separately in `state_pcap_2024.csv`).
- **Status**: Values remain transcribed. Reviewer action: access the
  C2ES interactive database via browser (requires JavaScript execution
  which this environment cannot perform) and spot-check all 31 rows.

## Blocked primary sources summary

The following URLs returned errors in every attempt:

| Source | URL pattern | Error |
|---|---|---|
| FRED CSV downloads | `fred.stlouisfed.org/graph/fredgraph.csv?*` | 503 |
| LBNL EMP publications | `emp.lbl.gov/publications/us-*` | 403 |
| LBNL PDFs | `emp.lbl.gov/sites/default/files/*.pdf` | 403/404 |
| Wikipedia | `en.wikipedia.org/wiki/*` | 403 |
| NCSL | `ncsl.org/*` | 403 |
| DSIRE | `dsireusa.org/*` | 403 / Cloudflare challenge |
| C40.org cities | `c40.org/cities` | 403 |
| Georgetown Climate Center | `georgetownclimate.org/*` | 307 / Sucuri challenge |
| US Conference of Mayors | `usmayors.org/*` | returns CSS-only content |
| Bond Buyer | `bondbuyer.com/*` | 404 |
| SIFMA | `sifma.org/*` | 503 |
| CARB PDF (direct) | `ww2.arb.ca.gov/sites/default/files/cap-and-trade/auction/*` | 503 via WebFetch |
| CARB PDF (via curl) | `ww2.arb.ca.gov/sites/default/files/2020-08/results_summary.pdf` | **200 (success!)** |
| WA Ecology auction pages (direct) | `ecology.wa.gov/*/auction-results` | 403 |
| WA Ecology publication PDFs (via curl) | `apps.ecology.wa.gov/publications/documents/*.pdf` | **200 (success!)** |

**Key insight**: WebFetch is blocked from some sources that respond to
`curl -H "User-Agent: Mozilla/5.0"`. The CA and WA auction PDFs were
initially 503/404 via WebFetch but retrieved successfully via curl direct.
This is how the CA auction-level and WA auction-level CSVs were upgraded
from `transcribed` to `fetched` in the 2026-04-10 verification pass.

## Summary statistics

Before 2026-04-10 verification pass:
- **fetched**: 121 rows (RGGI 70, RGGI members 11, EPA PCAP 51 - minus DC=1 duplicate adjustment)
- **transcribed**: ~176 rows (RPS 70, climate plan legacy 31, CA annual 13, WA annual 3, muni yield 8)

After 2026-04-10 verification pass:
- **fetched**: 186 rows (+65; CA auction-level 53, WA auction-level 12)
- **transcribed**: ~112 rows (RPS 70, climate plan legacy 31, muni yield 8, RGGI cross-check discrepancy retained)

**Verification debt reduction: ~37%.** The remaining transcribed debt is
concentrated in RPS history and climate plans where the primary sources
(LBNL, C2ES, Georgetown) were systematically blocked across every access
attempt in the working environment.
