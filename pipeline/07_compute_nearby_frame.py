"""
Compute nearby-issuance aggregates for each focal city x year.

For each of 578 focal cities:
  1. Compute haversine distance from focal city centroid to every bond's issuer location
  2. Filter to bonds within 10/25/50 mi
  3. Exclude bonds where the focal city is the issuer's assigned city
  4. Aggregate by (year, bucket, green/all) -> sum Amt, count CUSIPs
  5. Compute annual + cumulative versions

Output: /tmp/nearby_frame.parquet  (long format: FIPS, Year, <many cols>)
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEARS = list(range(2013, 2026))
RADII = [10, 25, 50]  # miles

bonds = pd.read_parquet("/tmp/bonds_for_nearby.parquet")
city_coords = pd.read_parquet("/tmp/city_coords.parquet")
city_coords = city_coords[city_coords["city_lat"].notna()].copy()
print(f"Focal cities with coords: {len(city_coords)}")
print(f"Bonds to evaluate: {len(bonds)}")

# Haversine distance in miles between one point (lat0, lng0) and arrays of points
EARTH_RADIUS_MI = 3958.8

def haversine_miles(lat0, lng0, lats, lngs):
    lat0_r = np.radians(lat0)
    lng0_r = np.radians(lng0)
    lats_r = np.radians(lats)
    lngs_r = np.radians(lngs)
    dlat = lats_r - lat0_r
    dlng = lngs_r - lng0_r
    a = np.sin(dlat / 2) ** 2 + np.cos(lat0_r) * np.cos(lats_r) * np.sin(dlng / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return EARTH_RADIUS_MI * c

# Pre-extract arrays
bond_lat = bonds["lat"].to_numpy()
bond_lng = bonds["lng"].to_numpy()
bond_year = bonds["panel_year"].to_numpy()
bond_amt = bonds["Amt Issued"].to_numpy()
bond_green = bonds["is_green"].to_numpy()
bond_bucket = bonds["bucket"].to_numpy()
bond_fips = bonds["city_fips7"].to_numpy()  # may be NaN

# For each focal city, produce annual sums by (year, bucket, greenflag, radius)
records = []
for i, row in enumerate(city_coords.itertuples(index=False)):
    f_fips = row.fips7
    f_lat = row.city_lat
    f_lng = row.city_lng

    d = haversine_miles(f_lat, f_lng, bond_lat, bond_lng)

    # Mask: exclude bonds assigned to this focal city itself
    not_self = ~((bond_fips == f_fips) & ~np.isnan(bond_fips))

    for radius in RADII:
        mask = (d <= radius) & not_self
        if not mask.any():
            continue
        sub_year = bond_year[mask]
        sub_amt = bond_amt[mask]
        sub_green = bond_green[mask]
        sub_bucket = bond_bucket[mask]

        df_sub = pd.DataFrame({
            "year": sub_year, "amt": sub_amt, "green": sub_green, "bucket": sub_bucket
        })
        # Annual sums: all bonds
        g_all = df_sub.groupby(["year", "bucket"]).agg(amt=("amt", "sum"), cnt=("amt", "count")).reset_index()
        g_all["greenflag"] = "All"
        # Annual sums: green only
        g_green = (
            df_sub[df_sub["green"]]
            .groupby(["year", "bucket"]).agg(amt=("amt", "sum"), cnt=("amt", "count")).reset_index()
        )
        g_green["greenflag"] = "Green"
        g = pd.concat([g_all, g_green], ignore_index=True)
        g["radius"] = radius
        g["FIPS"] = f_fips
        records.append(g)

    if (i + 1) % 50 == 0:
        print(f"  Focal city {i+1}/{len(city_coords)}", flush=True)

long = pd.concat(records, ignore_index=True) if records else pd.DataFrame()
print(f"Long records: {len(long)}")

# Pivot to wide: one column per (bucket, greenflag, radius, metric)
if len(long) > 0:
    long["col_amt"] = "Nearby_" + long["bucket"] + "_" + long["greenflag"] + "_Amt_" + long["radius"].astype(str) + "mi_Annual"
    long["col_cnt"] = "Nearby_" + long["bucket"] + "_" + long["greenflag"] + "_Count_" + long["radius"].astype(str) + "mi_Annual"

    amt_wide = long.pivot_table(index=["FIPS", "year"], columns="col_amt", values="amt", fill_value=0).reset_index()
    cnt_wide = long.pivot_table(index=["FIPS", "year"], columns="col_cnt", values="cnt", fill_value=0).reset_index()
    wide = amt_wide.merge(cnt_wide, on=["FIPS", "year"], how="outer").fillna(0)
    wide = wide.rename(columns={"year": "Year"})
else:
    wide = pd.DataFrame(columns=["FIPS", "Year"])

# Build full 578 x 13 skeleton so cells with zero nearby activity are present
focal_skeleton = city_coords[["fips7"]].rename(columns={"fips7": "FIPS"}).merge(
    pd.DataFrame({"Year": YEARS}), how="cross"
)
wide = focal_skeleton.merge(wide, on=["FIPS", "Year"], how="left").fillna(0)
wide = wide.sort_values(["FIPS", "Year"])

# Cumulative: running sum within each FIPS across years for every Annual column
annual_cols = [c for c in wide.columns if c.endswith("_Annual")]
for c in annual_cols:
    cumul_col = c.replace("_Annual", "_Cumul")
    wide[cumul_col] = wide.groupby("FIPS")[c].cumsum()

print(f"Nearby wide shape: {wide.shape}")
wide.to_parquet("/tmp/nearby_frame.parquet", index=False)
print("Saved nearby frame.")
