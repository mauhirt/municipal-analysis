"""
Build nearby-issuance panel for each of the 578 cities, counting bonds
issued by NON-STATE bodies within 10/25/50 km of the city centroid.

Input:
  raw/bloomberg/cusip_with_assignment.csv           (bonds, no coords)
  raw/bloomberg/green_bond_issuers_assignments.csv  (issuer lat/lng)
  /tmp/crosswalk_city_centroids.csv                 (578 city centroids)

Output:
  processed/nearby_by_jurisdiction_panel.{csv,xlsx}

Structure: 578 cities x 13 years (2013-2025), keyed on FIPS.

For each focal city x year, count bonds issued by non-state bodies
(Jurisdiction_Type != STATE) whose issuer coordinates fall within
10/25/50 km of the focal city centroid. Excludes bonds whose issuer
is assigned to the focal city itself.

Columns per radius (10km / 25km / 50km):
  Nearby_NonState_Total_{Amt,Count}_{r}km_Annual
  Nearby_NonState_Total_{Amt,Count}_{r}km_Cumul
  Plus splits by Jurisdiction_Type:
    CITY, COUNTY, SCHOOL_DISTRICT, SPECIAL_DISTRICT,
    MULTI_JURISDICTIONAL, OTHER
  e.g. Nearby_COUNTY_Amt_25km_Annual, Nearby_COUNTY_Amt_25km_Cumul

NOTE: cusip_with_assignment.csv contains only green bonds, so all
nearby aggregates are green-bond aggregates.
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed"
YEARS = list(range(2013, 2026))
RADII_KM = [10, 25, 50]
EARTH_RADIUS_KM = 6371.0088

NONSTATE_BUCKETS = [
    "CITY", "COUNTY", "SCHOOL_DISTRICT",
    "SPECIAL_DISTRICT", "MULTI_JURISDICTIONAL", "OTHER",
]

# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
bonds = pd.read_csv(RAW / "cusip_with_assignment.csv")
issuers = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
centroids = pd.read_csv("/tmp/crosswalk_city_centroids.csv")

# Clean year
bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)
bonds["city_fips7"] = pd.to_numeric(bonds["city_fips7"], errors="coerce")

# Drop state-level bonds
bonds = bonds[bonds["Jurisdiction_Type"] != "STATE"].copy()

# Bring in issuer lat/lng
iss_coords = issuers[["Issuer_Name", "lat", "lng"]].drop_duplicates("Issuer_Name")
bonds = bonds.merge(iss_coords, left_on="Issuer Name", right_on="Issuer_Name", how="left")
bonds = bonds[bonds["lat"].notna() & bonds["lng"].notna()].copy()
print(f"Non-state bonds with coords: {len(bonds)}")
print(bonds["Jurisdiction_Type"].value_counts().to_string())

# Pre-extract numpy arrays for speed
bond_lat = bonds["lat"].to_numpy()
bond_lng = bonds["lng"].to_numpy()
bond_year = bonds["panel_year"].to_numpy()
bond_amt = bonds["Amt Issued"].to_numpy()
bond_jur = bonds["Jurisdiction_Type"].to_numpy()
bond_fips = bonds["city_fips7"].to_numpy()

# ---------------------------------------------------------------------------
# Haversine (km)
# ---------------------------------------------------------------------------
def haversine_km(lat0, lng0, lats, lngs):
    lat0_r = np.radians(lat0)
    lng0_r = np.radians(lng0)
    lats_r = np.radians(lats)
    lngs_r = np.radians(lngs)
    dlat = lats_r - lat0_r
    dlng = lngs_r - lng0_r
    a = np.sin(dlat / 2) ** 2 + np.cos(lat0_r) * np.cos(lats_r) * np.sin(dlng / 2) ** 2
    return EARTH_RADIUS_KM * 2 * np.arcsin(np.sqrt(a))

# ---------------------------------------------------------------------------
# Iterate over focal cities and accumulate long records
# ---------------------------------------------------------------------------
centroids = centroids[centroids["city_lat"].notna()].copy()
print(f"Focal cities: {len(centroids)}")

records = []
for i, row in enumerate(centroids.itertuples(index=False)):
    f_fips = row.fips7
    d = haversine_km(row.city_lat, row.city_lng, bond_lat, bond_lng)
    # exclude bonds belonging to this city
    not_self = ~((bond_fips == f_fips) & ~np.isnan(bond_fips))

    for r_km in RADII_KM:
        mask = (d <= r_km) & not_self
        if not mask.any():
            continue
        sub_year = bond_year[mask]
        sub_amt = bond_amt[mask]
        sub_jur = bond_jur[mask]

        df_sub = pd.DataFrame({"year": sub_year, "amt": sub_amt, "jur": sub_jur})
        # Total across all non-state
        tot = df_sub.groupby("year").agg(amt=("amt", "sum"), cnt=("amt", "count")).reset_index()
        tot["jur_label"] = "NonState_Total"
        # Per-jurisdiction split
        per = df_sub.groupby(["year", "jur"]).agg(amt=("amt", "sum"), cnt=("amt", "count")).reset_index()
        per = per.rename(columns={"jur": "jur_label"})
        long = pd.concat([tot, per], ignore_index=True)
        long["radius"] = r_km
        long["FIPS"] = f_fips
        records.append(long)

    if (i + 1) % 50 == 0:
        print(f"  {i + 1}/{len(centroids)}", flush=True)

long_df = pd.concat(records, ignore_index=True) if records else pd.DataFrame()
print(f"Long records: {len(long_df)}")

# ---------------------------------------------------------------------------
# Wide pivot
# ---------------------------------------------------------------------------
long_df["col_amt"] = "Nearby_" + long_df["jur_label"] + "_Amt_" + long_df["radius"].astype(str) + "km_Annual"
long_df["col_cnt"] = "Nearby_" + long_df["jur_label"] + "_Count_" + long_df["radius"].astype(str) + "km_Annual"

amt_wide = long_df.pivot_table(index=["FIPS", "year"], columns="col_amt", values="amt", fill_value=0).reset_index()
cnt_wide = long_df.pivot_table(index=["FIPS", "year"], columns="col_cnt", values="cnt", fill_value=0).reset_index()
wide = amt_wide.merge(cnt_wide, on=["FIPS", "year"], how="outer").fillna(0)
wide = wide.rename(columns={"year": "Year"})

# Skeleton (578 x 13)
skel = (
    centroids[["fips7", "geo_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
# bring City_Name from crosswalk
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")
skel = skel.merge(
    crosswalk[["fips7", "city_name"]].rename(columns={"fips7": "FIPS", "city_name": "City_Name"}),
    on="FIPS", how="left"
)

panel = skel.merge(wide, on=["FIPS", "Year"], how="left")
num_cols = [c for c in panel.columns if c.startswith("Nearby_")]
panel[num_cols] = panel[num_cols].fillna(0)

# Ensure all expected columns exist (fill missing ones with 0)
for r_km in RADII_KM:
    for label in ["NonState_Total"] + NONSTATE_BUCKETS:
        for metric in ["Amt", "Count"]:
            col = f"Nearby_{label}_{metric}_{r_km}km_Annual"
            if col not in panel.columns:
                panel[col] = 0

# ---------------------------------------------------------------------------
# Cumulative versions (running sum within FIPS over years)
# ---------------------------------------------------------------------------
panel = panel.sort_values(["FIPS", "Year"]).reset_index(drop=True)
annual_cols = [c for c in panel.columns if c.endswith("_Annual")]
for c in annual_cols:
    panel[c.replace("_Annual", "_Cumul")] = panel.groupby("FIPS")[c].cumsum()

# ---------------------------------------------------------------------------
# Column order
# ---------------------------------------------------------------------------
id_cols = ["FIPS", "City", "City_Name", "State", "Year"]
ordered = list(id_cols)
for r_km in RADII_KM:
    for label in ["NonState_Total"] + NONSTATE_BUCKETS:
        for metric in ["Amt", "Count"]:
            for suffix in ["Annual", "Cumul"]:
                col = f"Nearby_{label}_{metric}_{r_km}km_{suffix}"
                if col in panel.columns:
                    ordered.append(col)
panel = panel[ordered]
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
panel.to_csv(OUT / "nearby_by_jurisdiction_panel.csv", index=False)
panel.to_excel(OUT / "nearby_by_jurisdiction_panel.xlsx", index=False)
print(f"\nPanel shape: {panel.shape}")
print(f"Written: {OUT / 'nearby_by_jurisdiction_panel.xlsx'}")
