# Transportation Compulsion — what's built, what's blocked

Clean-transportation outcomes (`Y_Clean_Transportation`, `Y_Renewable_Energy`
after muni-electric restriction, and any interaction with mayoral
partisanship) historically had no federal-mandate compulsion variable
analogous to EPA NPDES for water. This file documents what has now been
built from authoritative sources and what genuinely requires an external
data pull (CAA nonattainment from EPA Green Book).

## What's built (from peer-review-grade sources)

### 1. `state_ghg_law_active` / `state_ghg_law_active_lag1`

**What it is:** state-year indicator that a binding statutory economy-wide
GHG reduction target has been enacted by year *t*.

**Source file:** `raw/policy/state_ghg_reduction_laws.csv` — one row per
distinct statute with full citation (statute code + session-law link) in
the `source` column. Cross-referenced against Georgetown Climate Center
State Climate Policy Maps and LSE Grantham Climate Change Laws of the
World Database.

**Panel coverage:** 2,447 city-years (states with any binding statute
in effect).

**States covered:** CA (2006/2016), CT (2008/2022), CO (2019/2021), HI
(2007/2022), IL (2021), MA (2008/2021), MD (2009/2022), ME (2019), MN
(2023), NJ (2007), NY (2019), OR (2007/2021), RI (2021), VT (2020),
WA (2021).

**Why this is a "compulsion" for municipal transportation:** Economy-wide
GHG reduction statutes create a top-down obligation that reduces state
regulatory tolerance for business-as-usual transportation investment.
While the statutes themselves do not directly bind municipal bond
issuance, they do obligate state transportation agencies (e.g. CalTrans
under AB 32/SB 32) to implement reductions, which flow through state
transportation funding formulas to the municipalities that depend on
them. The mechanism is therefore indirect but statutorily binding at
the state level.

**Caveat for peer review:** This is not a *federal* mandate compulsion
analogous to NPDES. It is a state-level mandate. Whether it constitutes
compulsion for a *city* within the state depends on whether the state
implements the statute through municipal channels. Under state fixed
effects, `state_ghg_law_active` is identified from state-years where
enactment shifts the variable within a state (enactment-year only) —
limited identifying variation, so this variable is best used in no-FE
or state-clustered specs, or as an interaction term (see §3).

### 2. `state_zev_mandate_active` / `state_zev_mandate_active_lag1`

**What it is:** state-year indicator that the state has adopted
California's ZEV standards under § 177 of the Clean Air Act (42 U.S.C.
§ 7507).

**Source file:** `raw/policy/state_zev_mandate.csv` — one row per state,
with adoption year, first compliance model year, regulatory citation,
and source URL. Cross-referenced against CARB Section 177 tracking, ICCT
US ZEV Regulation Tracker, and NESCAUM.

**Panel coverage:** 2,666 city-years (states with active ZEV rule).

**States covered (with adoption year):**
- CA (1990 original), NY (2005), NJ (2004), MA (1991), VT (2005),
  ME (2005), CT (2004), RI (2005), OR (2007), WA (2005), MD (2007),
  DE (2010), CO (2019), MN (2021), NM (2022), NV (2021), VA (2021).

**Why this is a "compulsion" for municipal transportation:** Section 177
states create state-backed pressure for municipal fleet / transit
procurement to shift toward ZEVs. State ZEV rules typically include
provisions for fleet procurement (government vehicles), which creates
direct bond-financing demand for:
- Electric transit bus replacement
- Charging-infrastructure bonds
- Electric municipal fleet conversion

**Identification:** Within-state temporal variation from adoption
(CO 2019, MN 2021, NM 2022, VA 2021) is sharp. Early-adopting states
(CT, NJ, MA, NY, etc.) are pre-panel; no within-state variation for
them.

## What's blocked — EPA Clean Air Act Nonattainment

See `raw/policy/caa_nonattainment_placeholder.md` for full details.

**Why it matters:** CAA nonattainment is the sharpest federal-mandate
transportation compulsion channel, and it varies at the **county-MSA
level within a state** — so it identifies under state fixed effects,
unlike state GHG / ZEV rules.

**What's required:** A structured pull of EPA Green Book historical
quarterly releases, reconciled against Federal Register publications for
classification changes over 2013-2025. Minimum output:

```
county_fips,year,caa_ozone_nonattainment_any,caa_pm25_nonattainment_any,
  caa_classification,effective_date,attainment_date,source
```

**Alternative (lower-cost):** EPA Clean Air Markets Division publishes
county-level annual air quality design value data. Could be used as a
proxy: designate a county as "nonattainment-pressure" if its 3-year
design value for 8-hour ozone exceeds the current NAAQS. This is
coarser than actual nonattainment designation but retrievable.

**Until this is done:** The clean-transportation column in Table 2
continues to use `iija_transit_grant_amt_asinh_lag1` as the best available
compulsion proxy, with state GHG + state ZEV as new supplementary
variables. The caveat in the paper must acknowledge that CAA compulsion
is not directly measured.

## Proposed specification updates

### Table 1 — add transportation-compulsion × partisanship interaction

Once all three transportation-compulsion variables are built (GHG, ZEV,
CAA), test:

```
rep_x_ghg_law = Rep_Mayor_lag1 × state_ghg_law_active_lag1
rep_x_zev     = Rep_Mayor_lag1 × state_zev_mandate_active_lag1
rep_x_caa     = Rep_Mayor_lag1 × caa_ozone_nonattainment_any  [blocked]
```

Predictions (from the compulsion-compresses-gap theory):
- Positive interactions on `Green_Bond_Issued` / `Y_self_green`:
  compulsion pulls Republican mayors into issuance.
- Null interaction with `Y_esg_assurance`: compulsion stops at Step 4.

### Table 2 — replace clean-transport column RHS

Current: NPDES (water-specific) as compulsion predictor.

Proposed: `iija_transit_grant_amt_asinh_lag1` + `state_ghg_law_active_lag1`
+ `state_zev_mandate_active_lag1` as the compulsion block, with
`caa_ozone_nonattainment_any` added once retrievable.

## Summary

| Variable | Source | Coverage | Ready? |
|---|---|---|---|
| `state_ghg_law_active_lag1` | `raw/policy/state_ghg_reduction_laws.csv` (23 laws, 15 states) | 2,447 city-years | ✅ |
| `state_zev_mandate_active_lag1` | `raw/policy/state_zev_mandate.csv` (17 states) | 2,666 city-years | ✅ |
| `caa_ozone_nonattainment_any` | EPA Green Book (pending pull) | county-year | ❌ blocked |
