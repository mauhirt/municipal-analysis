"""
Build nearby-issuance variables for the control panel.

Computes, for each focal city x year:
  - bonds issued within 10mi / 25mi / 50mi of city centroid
  - split by: OtherLargeCity / NonLargeCity / NonCity
  - for each: All bonds vs Green only, Amt + Count, Annual + Cumulative

Excludes issuers assigned to the focal city itself.
Distance = haversine(focal_city_centroid, issuer_lat_lng).

Output: /tmp/nearby_frame.parquet
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
YEARS = list(range(2013, 2026))

bonds = pd.read_excel(RAW / "bonds_with_issuer_classification.xlsx")
assign = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
city_coords = pd.read_csv("/tmp/crosswalk_city_centroids.csv")

# Merge issuer assignment + coords onto bonds
bonds = bonds.merge(
    assign[["Issuer_Name", "city_fips7", "lat", "lng", "Jurisdiction_Type"]].rename(
        columns={"Jurisdiction_Type": "issuer_jurisdiction"}
    ),
    left_on="Issuer Name",
    right_on="Issuer_Name",
    how="left",
)

# Year
bonds["derived_year"] = pd.to_datetime(bonds["Issue Date"], errors="coerce").dt.year
bonds["panel_year"] = bonds["Year"].where(
    (bonds["Year"] >= 2013) & (bonds["Year"] <= 2030), bonds["derived_year"]
)
bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)
bonds["is_green"] = bonds["Self-reported Green"].astype(str).str.strip() == "Yes"

# Drop bonds without coords (can't compute distance)
bonds = bonds[bonds["lat"].notna() & bonds["lng"].notna()].copy()
print(f"Bonds with coords: {len(bonds)}")

# ---------------------------------------------------------------------------
# Classify each bond's issuer into one of 3 buckets (from focal city's perspective):
#   OtherLargeCity : issuer_jurisdiction == CITY AND city_fips7 not null (assigned to a 578 city)
#   NonLargeCity   : issuer_jurisdiction == CITY AND city_fips7 is null (not in 578)
#   NonCity        : issuer_jurisdiction != CITY
# ---------------------------------------------------------------------------
def issuer_bucket(row):
    if row["issuer_jurisdiction"] == "CITY":
        return "OtherLargeCity" if pd.notna(row["city_fips7"]) else "NonLargeCity"
    return "NonCity"

bonds["bucket"] = bonds.apply(issuer_bucket, axis=1)
print(bonds["bucket"].value_counts().to_string())

# Save for next step (we split distance computation to avoid memory blowup)
bonds[["CUSIP", "Amt Issued", "panel_year", "is_green", "lat", "lng", "city_fips7", "bucket"]].to_parquet(
    "/tmp/bonds_for_nearby.parquet", index=False
)
city_coords.to_parquet("/tmp/city_coords.parquet", index=False)
print("Prepared data for distance computation.")
