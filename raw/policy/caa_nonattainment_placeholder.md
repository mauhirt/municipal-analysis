# EPA Clean Air Act Nonattainment — data-pull gap

## What this variable would measure

County-level indicator of EPA Clean Air Act (CAA) nonattainment status under
the National Ambient Air Quality Standards (NAAQS). Nonattainment designation
triggers federal Transportation Conformity requirements (40 CFR Part 93) on
state and local transportation plans, which is the most concrete
**federal-mandate compulsion channel for clean transportation** identified
in the variable audit. Unlike state-level variables, CAA nonattainment
varies *within a state* by county/MSA, which means it survives state fixed
effects and provides true within-state identifying variation.

## Why this file is a placeholder rather than actual data

Building a credible county-year nonattainment panel for 2013–2025 requires
pulling the EPA Green Book historical series for each NAAQS pollutant
(8-hour ozone 2008, 8-hour ozone 2015, PM2.5 2012 annual, PM2.5 2012
24-hour, SO2 2010, Lead 2008, CO, NO2) and reconciling the following:

1. **NAAQS revisions**: the 2015 ozone standard (70 ppb) produced a new
   wave of designations in 2018 that overlapped with the residual 2008
   ozone nonattainment areas (75 ppb). A county can be simultaneously
   nonattainment under one standard and attainment under another.

2. **Reclassification over time**: Moderate → Serious → Severe → Extreme
   reclassifications in ozone areas (e.g., Bump-Up Rule, 40 CFR § 51.903)
   happen at non-regular intervals. Final rules need to be parsed from
   the Federal Register year-by-year.

3. **Maintenance plan redesignations**: Counties that reach attainment
   enter a 20-year maintenance plan but exit "nonattainment" status. These
   transitions need date-level precision.

4. **Partial county designations**: Some counties are partially
   nonattainment. EPA's Green Book reports this as "Partial"; a county-year
   panel would need to coarsen this to a binary or share.

None of this is reconstructable from memory to peer-reviewed publication
standard. A proper data pull requires scripted download of EPA Green Book
quarterly releases and reconciliation against Federal Register publications.

## Minimum viable file (if time allows)

Extract from the EPA Green Book "Currently Designated Nonattainment Areas
for All Criteria Pollutants" downloadable at
https://www3.epa.gov/airquality/greenbook/ancl.html

Expected schema:
```
county_fips,year,naaqs_standard,classification,effective_date,attainment_date,source
```

Then construct the following derived variables for the panel:
- `caa_ozone_nonattainment_any` — 1 if county is in any ozone NAAQS
  nonattainment area in year t, 0 otherwise
- `caa_pm25_nonattainment_any` — same for PM2.5
- `caa_any_criteria_nonattainment` — union across all criteria pollutants
- `caa_nonattainment_classification` — ordinal: 0=attainment, 1=marginal,
  2=moderate, 3=serious, 4=severe, 5=extreme (ozone only)

## What the analysis cannot do without this

The clean-transportation column in Table 2 currently has no
federal-mandate compulsion variable. Without CAA nonattainment, the best
we can do is `iija_transit_grant_amt_asinh_lag1` (which reflects federal
transit funding flow, not binding mandate).

A full CAA nonattainment merge would support three pre-committed tests:

1. **T1 main spec**: add `caa_any_criteria_nonattainment × Rep_Mayor_lag1`
   to Col 5 as a compulsion × partisanship interaction, testing whether
   federal air quality mandates compress the partisan gap in transport
   bond issuance.

2. **T2-clean-transportation**: replace / augment `iija_transit_grant`
   with `caa_ozone_nonattainment_any` as the primary compulsion predictor.
   Expected positive — cities under ozone nonattainment have stronger
   mandate to shift to clean transport.

3. **Heterogeneity check**: subsample T2-clean-transport by attainment
   status; expect the partisan gap smaller in nonattainment areas if
   federal compulsion binds.

## Status

**Blocked on external data pull.** All other state-level transportation
compulsion variables (state GHG reduction laws, state ZEV mandates) have
been built from primary legislative sources in this repository. The CAA
nonattainment merge is the single largest remaining transport-compulsion
data gap.

## Next steps (if the data pull is authorised)

1. Download historical quarterly Green Book releases (data.epa.gov or
   regulations.gov); older releases via EPA FOIA.
2. Parse into county_fips × NAAQS × year panel.
3. Merge into `00_build_panel.py` on (county_fips5, year).
4. Construct the derived indicators listed above.
5. Re-run Table 2 clean-transportation column with new compulsion
   variable.
