"""
Build File 3: Geospatial reference file for spillover analysis.

Structure: one row per geographic entity with coordinates and summary outcome.
Entities:
  1. All 578 crosswalk cities (city centroid)
  2. All non-city issuers with coordinates (~840 issuer point locations)

Columns:
  entity_type           - 'large_city' | 'issuer'
  entity_id             - FIPS7 for cities, Issuer_Name for issuers
  name                  - human readable
  state                 - state abbreviation
  lat, lng              - coordinates
  city_fips7            - if entity is assigned to one of 578 (issuers only)
  jurisdiction_type     - only for issuers
  in_578_panel          - True if the entity is / is assigned to a 578 city

  Entity-level totals across 2013-2025:
    total_green_amt       - sum of Amt Issued where Self-reported Green == Yes
    total_green_count     - count of green bond CUSIPs
    total_all_amt         - sum of Amt Issued (all bonds)
    total_all_count       - all bond count
    any_green             - 1 if total_green_count > 0
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed"

bonds = pd.read_excel(RAW / "bonds_with_issuer_classification.xlsx")
assign = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
city_coords = pd.read_csv("/tmp/crosswalk_city_centroids.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

bonds["is_green"] = bonds["Self-reported Green"].astype(str).str.strip() == "Yes"

# Issuer-level totals across all years
issuer_totals = bonds.groupby("Issuer Name").agg(
    total_all_amt=("Amt Issued", "sum"),
    total_all_count=("CUSIP", "count"),
).reset_index()
green_totals = bonds[bonds["is_green"]].groupby("Issuer Name").agg(
    total_green_amt=("Amt Issued", "sum"),
    total_green_count=("CUSIP", "count"),
).reset_index()
issuer_totals = issuer_totals.merge(green_totals, on="Issuer Name", how="left").fillna(
    {"total_green_amt": 0, "total_green_count": 0}
)

# Merge with assignments / coords
issuers = assign.merge(issuer_totals, left_on="Issuer_Name", right_on="Issuer Name", how="left").drop(columns=["Issuer Name"])
issuers["any_green"] = (issuers["total_green_count"] > 0).astype(int)
issuers_rows = issuers.assign(
    entity_type="issuer",
    entity_id=issuers["Issuer_Name"],
    name=issuers["Issuer_Name"],
    state=issuers["State_Abb"],
    jurisdiction_type=issuers["Jurisdiction_Type"],
    in_578_panel=issuers["city_fips7"].notna(),
)[[
    "entity_type", "entity_id", "name", "state", "lat", "lng",
    "city_fips7", "jurisdiction_type", "in_578_panel",
    "total_green_amt", "total_green_count", "total_all_amt", "total_all_count", "any_green",
]]

# --- City rows ---
# City-level totals: aggregate across issuers assigned to that city
city_from_bonds = bonds.merge(
    assign[["Issuer_Name", "city_fips7"]], left_on="Issuer Name", right_on="Issuer_Name", how="left"
)
city_from_bonds = city_from_bonds[city_from_bonds["city_fips7"].notna()]
city_totals = city_from_bonds.groupby("city_fips7").agg(
    total_all_amt=("Amt Issued", "sum"),
    total_all_count=("CUSIP", "count"),
).reset_index()
city_green = city_from_bonds[city_from_bonds["is_green"]].groupby("city_fips7").agg(
    total_green_amt=("Amt Issued", "sum"),
    total_green_count=("CUSIP", "count"),
).reset_index()
city_totals = city_totals.merge(city_green, on="city_fips7", how="left").fillna(
    {"total_green_amt": 0, "total_green_count": 0}
)
city_totals["any_green"] = (city_totals["total_green_count"] > 0).astype(int)

# Merge with city names + coords
cities = crosswalk[["fips7", "geo_name", "city_name", "state_abb"]].merge(
    city_coords[["fips7", "city_lat", "city_lng"]], on="fips7", how="left"
).merge(city_totals, left_on="fips7", right_on="city_fips7", how="left").fillna(
    {"total_all_amt": 0, "total_all_count": 0, "total_green_amt": 0, "total_green_count": 0, "any_green": 0}
)

city_rows = cities.assign(
    entity_type="large_city",
    entity_id=cities["fips7"].astype(str),
    name=cities["city_name"],
    state=cities["state_abb"],
    lat=cities["city_lat"],
    lng=cities["city_lng"],
    jurisdiction_type="CITY",
    in_578_panel=True,
)
city_rows = city_rows.rename(columns={"fips7": "city_fips7"})[[
    "entity_type", "entity_id", "name", "state", "lat", "lng",
    "city_fips7", "jurisdiction_type", "in_578_panel",
    "total_green_amt", "total_green_count", "total_all_amt", "total_all_count", "any_green",
]]

# Combine
geo = pd.concat([city_rows, issuers_rows], ignore_index=True)
geo = geo.sort_values(["entity_type", "state", "name"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
geo.to_csv(OUT / "geospatial_entities.csv", index=False)
geo.to_excel(OUT / "geospatial_entities.xlsx", index=False)

print(f"Geospatial file shape: {geo.shape}")
print(geo["entity_type"].value_counts().to_string())
print(f"Entities with coords: {geo['lat'].notna().sum()}/{len(geo)}")
print(f"Written: {OUT / 'geospatial_entities.xlsx'}")
