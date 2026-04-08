# DC Recovery Note and State Variable Missingness

## Key Finding: DC is NOT dropped

Washington DC (FIPS 1150000) has **full coverage** on all Table 1 control variables — `state_rep_trifecta`, `esg_has_muni_bond_law`, `pres_dem_vote_share`, and `Rep_Mayor` are all non-null for all 13 years. DC is already in the 535-city regression sample. **No `dc_special` dummy is needed.**

## What IS dropped: 4 cities with `esg_has_muni_bond_law` = NaN (processing error)

| City | State | FIPS | Population | Cause | Fix |
|---|---|---|---|---|---|
| Augusta-Richmond County | GA | 1304204 | ~200K | Processing error | Recoverable |
| Lexington-Fayette County | KY | 2146027 | ~320K | Processing error | Recoverable |
| Rio Rancho | NM | 3563460 | ~95K | Processing error | Recoverable |
| West Valley City | UT | 4983470 | ~130K | Processing error | Recoverable |

### Root Cause

`esg_has_muni_bond_law` is present in **two** data sources:
1. `fiscal_tel_merged_2013_2025.csv.gz` (the "old" fiscal supplement) — has 572 cities, missing these 4
2. `data/clean/antiesg_laws/antiesg_laws.csv` — has all 572 cities including these 4 with correct value (0.0)

The build script (`00_build_panel.py`) loads the old fiscal supplement first (step 3), which brings in `esg_has_muni_bond_law` with NaN for these 4 cities. When the anti-ESG source is merged in step 9, the column already exists in `df`, so `ae_new = [c for c in ae.columns if c not in df.columns]` skips it. The NaN values from the stale source are never overwritten.

### Fix

In `00_build_panel.py`, after the anti-ESG merge (step 9), add a targeted overwrite:

```python
# Fix: overwrite esg_has_muni_bond_law NaN values from the authoritative anti-ESG source
if 'esg_has_muni_bond_law' in df.columns and 'esg_has_muni_bond_law' in ae.columns:
    mask = df['esg_has_muni_bond_law'].isna()
    if mask.any():
        fill = ae.set_index(['fips7','year'])['esg_has_muni_bond_law']
        for idx in df[mask].index:
            key = (df.loc[idx,'fips7'], df.loc[idx,'year'])
            if key in fill.index:
                df.loc[idx, 'esg_has_muni_bond_law'] = fill.loc[key]
```

Or more simply: force the anti-ESG source to overwrite the column regardless of whether it already exists.

### Impact of Recovery

Recovering these 4 cities adds ~52 city-year observations (4 cities × 13 years, minus any other missing controls). All 4 have `state_rep_trifecta` and `pres_dem_vote_share` already, so the only barrier was `esg_has_muni_bond_law`. The value is 0 for all 4 (no state has an anti-ESG muni bond law affecting these cities), so adding them cannot change the `esg_has_muni_bond_law` coefficient — it only adds variation in other controls.

### Athens-Clarke County (GA, FIPS 1303440)

Athens-Clarke is categorised separately because it is missing from **6 different clean data sources** (anti-ESG, state_political, presidential_elections, and likely others). This is not a processing error — it is a **systematic crosswalk gap** where the consolidated city-county FIPS code was never mapped. Recovery requires manual addition to multiple crosswalks.

## Summary

| Category | Cities | Fix | Effort |
|---|---|---|---|
| DC (not dropped) | 0 | None needed | — |
| Processing error (esg stale overwrite) | 4 | Fix merge priority in build script | Low |
| Crosswalk gap (Athens-Clarke) | 1 | Manual addition to 6 crosswalks | Medium |
