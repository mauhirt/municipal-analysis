"""
Build a city-year presidential vote share panel from the MIT Election Data
and Science Lab (MEDSL) County Presidential Election Returns 2000-2024.

Input:
  raw/political/mit_countypres_2000_2024.csv   (94,151 rows, 2000-2024)
  raw/crosswalk/Crosswalk.csv                  (578 cities with county mapping)

Output:
  processed/presidential_vote_city_year_panel.csv

Logic:
  1. Filter MIT data to DEMOCRAT + REPUBLICAN candidates, 2012/2016/2020/2024
     election cycles (covers the full 2013-2025 panel window).
  2. For each county x election, compute:
       dem_votes, rep_votes, total_votes, dem_two_party_share
  3. Map cities to their primary county via the crosswalk (county_geo_id).
     Where a city spans multiple counties, weight by the crosswalk's
     relevant_counties field or fall back to the first county listed.
  4. Expand to annual frequency 2013-2025 using the most recent prior
     election:
       Outcome year 2013-2016 <- 2012 election
       Outcome year 2017-2020 <- 2016 election
       Outcome year 2021-2024 <- 2020 election
       Outcome year 2025      <- 2024 election

Why "most recent prior": municipal capital planning reflects the political
environment the mayor took office under, not a future election. This also
matches the memo's `pres_dem_vote_share_lag2` intent — by the time a
decision is observed at year Y, the applicable vote share is from the most
recent election that occurred strictly before Y+1 (so 2025 outcomes use
the Nov 2024 results).
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "processed"
YEARS = list(range(2013, 2026))

# ---------------------------------------------------------------------------
# 1. Load and reshape MIT data
# ---------------------------------------------------------------------------
mit = pd.read_csv(RAW / "political" / "mit_countypres_2000_2024.csv",
                  dtype={"county_fips": str})
print(f"MIT county pres rows: {len(mit)}")

# Keep only elections we need for the 2013-2025 panel (2012, 2016, 2020, 2024)
mit = mit[mit.year.isin([2012, 2016, 2020, 2024])]
# Keep DEM + REP only for two-party share computation
mit = mit[mit.party.isin(["DEMOCRAT", "REPUBLICAN"])]
print(f"After filter to DEM/REP 2012-2024: {len(mit)}")

# Some rows have NaN candidatevotes — drop them
mit = mit[mit["candidatevotes"].notna()].copy()

# County-year-party pivot
piv = mit.pivot_table(
    index=["year", "county_fips", "state_po", "county_name"],
    columns="party",
    values="candidatevotes",
    aggfunc="sum",
).reset_index()
piv.columns.name = None
piv = piv.rename(columns={"DEMOCRAT": "dem_votes", "REPUBLICAN": "rep_votes"})
piv["dem_votes"] = piv["dem_votes"].fillna(0)
piv["rep_votes"] = piv["rep_votes"].fillna(0)
piv["total_2party"] = piv["dem_votes"] + piv["rep_votes"]
# Two-party share and raw shares
piv["pres_dem_two_party_share"] = np.where(
    piv["total_2party"] > 0, piv["dem_votes"] / piv["total_2party"], np.nan
)
# For raw vote share, also need total votes (using candidatevotes + other parties)
totals = mit.groupby(["year", "county_fips"])["totalvotes"].max().reset_index()
piv = piv.merge(totals, on=["year", "county_fips"], how="left")
piv["pres_dem_vote_share"] = np.where(
    piv["totalvotes"] > 0, piv["dem_votes"] / piv["totalvotes"], np.nan
)
piv["pres_rep_vote_share"] = np.where(
    piv["totalvotes"] > 0, piv["rep_votes"] / piv["totalvotes"], np.nan
)
print(f"County-year records: {len(piv)}")
print(f"Elections covered: {sorted(piv.year.unique())}")
# Ensure county_fips is 5-digit integer
piv["county_fips_int"] = piv["county_fips"].astype(int)

# ---------------------------------------------------------------------------
# 2. Map 578 cities to primary county via crosswalk
# ---------------------------------------------------------------------------
cw = pd.read_csv(RAW / "crosswalk" / "Crosswalk.csv")
print(f"Crosswalk cities: {len(cw)}")

def extract_county_fips5(val):
    if pd.isna(val):
        return None
    s = str(val)
    if "US" in s:
        s = s.split("US")[-1]
    try:
        return int(s[-5:]) if s.strip() else None
    except ValueError:
        return None

cw["county_fips5"] = cw["county_geo_id"].apply(extract_county_fips5)
# Also handle relevant_counties for multi-county cities
cw["primary_county_fips5"] = cw["county_fips5"]

# For cities where county_fips5 is None, try to parse relevant_counties
def first_county_from_relevant(s):
    if pd.isna(s):
        return None
    parts = str(s).split(";")
    for p in parts:
        try:
            return int(p.strip()[-5:])
        except (ValueError, IndexError):
            continue
    return None

mask = cw["primary_county_fips5"].isna()
if mask.any():
    cw.loc[mask, "primary_county_fips5"] = cw.loc[mask, "relevant_counties"].apply(first_county_from_relevant)

print(f"Cities with primary county: {cw.primary_county_fips5.notna().sum()}")
city_county = cw[["fips7", "geo_name", "state_abb", "primary_county_fips5"]].rename(
    columns={"fips7": "FIPS", "geo_name": "City", "state_abb": "State",
             "primary_county_fips5": "county_fips_int"}
)
city_county["FIPS"] = city_county["FIPS"].astype(int)
city_county["county_fips_int"] = pd.to_numeric(
    city_county["county_fips_int"], errors="coerce"
).astype("Int64")

# ---------------------------------------------------------------------------
# 3. Build city-election panel (one row per city per election cycle)
# ---------------------------------------------------------------------------
city_elec = city_county.merge(
    piv[["year", "county_fips_int", "dem_votes", "rep_votes", "total_2party",
         "totalvotes", "pres_dem_two_party_share", "pres_dem_vote_share",
         "pres_rep_vote_share"]],
    on="county_fips_int", how="left"
)
print(f"City-election rows: {len(city_elec)}")
matched = city_elec[city_elec.pres_dem_two_party_share.notna()]
print(f"Cities matched to a county in MIT data: {matched.FIPS.nunique()}")

# ---------------------------------------------------------------------------
# 4. Expand to city-year by applying the most-recent-prior-election rule
# ---------------------------------------------------------------------------
def applicable_election(outcome_year):
    """Return the election year whose results apply at outcome_year."""
    if outcome_year <= 2016:
        return 2012
    if outcome_year <= 2020:
        return 2016
    if outcome_year <= 2024:
        return 2020
    return 2024

rows = []
for _, row in city_county.iterrows():
    fips = row["FIPS"]
    county = row["county_fips_int"]
    city = row["City"]
    state = row["State"]
    for y in YEARS:
        elec_year = applicable_election(y)
        sub = city_elec[(city_elec.FIPS == fips) & (city_elec.year == elec_year)]
        if len(sub):
            r = sub.iloc[0]
            rows.append({
                "FIPS": fips,
                "City": city,
                "State": state,
                "Year": y,
                "applicable_election_year": elec_year,
                "county_fips_int": county,
                "pres_dem_two_party_share": r["pres_dem_two_party_share"],
                "pres_dem_vote_share": r["pres_dem_vote_share"],
                "pres_rep_vote_share": r["pres_rep_vote_share"],
                "pres_dem_votes": r["dem_votes"],
                "pres_rep_votes": r["rep_votes"],
                "pres_total_votes": r["totalvotes"],
            })
        else:
            rows.append({
                "FIPS": fips,
                "City": city,
                "State": state,
                "Year": y,
                "applicable_election_year": elec_year,
                "county_fips_int": county,
                "pres_dem_two_party_share": np.nan,
                "pres_dem_vote_share": np.nan,
                "pres_rep_vote_share": np.nan,
                "pres_dem_votes": np.nan,
                "pres_rep_votes": np.nan,
                "pres_total_votes": np.nan,
            })

panel = pd.DataFrame(rows)
print(f"Panel: {panel.shape}")
print(f"Non-null pres_dem_two_party_share: {panel.pres_dem_two_party_share.notna().sum()}")

# ---------------------------------------------------------------------------
# 5. Year-by-year coverage check
# ---------------------------------------------------------------------------
print("\nCoverage by outcome year:")
for y in YEARS:
    sub = panel[panel.Year == y]
    nn = sub.pres_dem_two_party_share.notna().sum()
    elec = sub.applicable_election_year.iloc[0]
    print(f"  Y={y} (elec={elec}): {nn}/578 cities with vote share")

# ---------------------------------------------------------------------------
# 6. Save
# ---------------------------------------------------------------------------
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)
panel = panel[[
    "FIPS", "City", "State", "Year", "applicable_election_year",
    "county_fips_int",
    "pres_dem_two_party_share", "pres_dem_vote_share", "pres_rep_vote_share",
    "pres_dem_votes", "pres_rep_votes", "pres_total_votes",
]]
OUT.mkdir(parents=True, exist_ok=True)
panel.to_csv(OUT / "presidential_vote_city_year_panel.csv", index=False)
print(f"\nWritten: {OUT / 'presidential_vote_city_year_panel.csv'}")
