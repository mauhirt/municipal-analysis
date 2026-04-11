"""
Build water-only green bond state cumulative and nearby (regional) panels.

Purpose: the paper needs separate "water-only" versions of the state
cumulative and regional spillover controls because water infrastructure is
the federally-compelled category under NPDES enforcement. The water-only
aggregates measure the pool of similarly-compelled issuance a city is
exposed to (through state peer dynamics and geographic proximity), which
is a cleaner control for the memo's Family 1a compulsion test.

Inputs:
  raw/bloomberg/cusip_with_assignment.csv          (25,555 green bonds)
  raw/bloomberg/green_bond_issuers_assignments.csv (issuer lat/lng)
  raw/crosswalk/Crosswalk.csv                      (578 cities)
  /tmp/crosswalk_city_centroids.csv                (578 city centroids)

Outputs:
  processed/state_controls_city_year_panel_water_only.csv
  processed/nearby_by_jurisdiction_panel_water_only.csv

Water-only filter: ESG Project Categories contains "Sustainable Water"
(handles standalone and multi-category combinations like
"Sustainable_Water, Energy_Efficiency").

Variables (mirror the all-green panels exactly with _water suffix):
  State panel:
    State_Total_Water_{Amt,Count}_{Annual,Cumul}
    State_Govt_Water_{Amt,Count}_{Annual,Cumul}
    State_Total_Water_Ex_City_{Amt,Count}_{Annual,Cumul}
    State_Govt_Water_Ex_City_{Amt,Count}_{Annual,Cumul}
    City_Own_Water_{Amt,Count}_{Annual,Cumul}
    City_Own_Water_Govt_{Amt,Count}_{Annual,Cumul}

  Nearby panel:
    Nearby_NonState_Water_{Amt,Count}_{10,25,50}km_{Annual,Cumul}
    Plus per-jurisdiction splits (CITY, COUNTY, SCHOOL_DISTRICT, etc.)
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
# 1. Load and filter to water-only bonds
# ---------------------------------------------------------------------------
bonds = pd.read_csv(RAW / "cusip_with_assignment.csv", low_memory=False)
print(f"All green bonds: {len(bonds)}")

# Filter to water-related bonds: ESG Project Categories contains "Sustainable Water"
# (handles single-category, first-of-combo, last-of-combo, and middle-of-combo)
cat = bonds["ESG Project Categories"].fillna("").astype(str)
is_water = cat.str.contains("Sustainable Water", case=False, na=False)
water = bonds[is_water].copy()
print(f"Water-only bonds: {len(water)}  ({len(water)/len(bonds):.1%} of all green)")
print(f"Water-only bonds by year:")
water_year = water[water["panel_year"].between(2013, 2025, inclusive="both")].copy()
print(water_year["panel_year"].value_counts().sort_index().to_string())
print()

# Prep bonds frame (mirror pipeline/13 and pipeline/12)
water_year["panel_year"] = water_year["panel_year"].astype(int)
water_year = water_year[water_year["State_Abb_Classified"].notna()]
water_year = water_year[~water_year["State_Abb_Classified"].str.contains("N/A", na=False)]
water_year["city_fips7"] = pd.to_numeric(water_year["city_fips7"], errors="coerce")

# Load crosswalk
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

# =============================================================================
# PART A: State cumulative panel (water-only)
# =============================================================================
print("\n=== PART A: State cumulative water-only panel ===")

state_total = (
    water_year.groupby(["State_Abb_Classified", "panel_year"])
    .agg(
        State_Total_Water_Amt_Annual=("Amt Issued", "sum"),
        State_Total_Water_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"State_Abb_Classified": "State", "panel_year": "Year"})
)

state_govt = (
    water_year[water_year["Jurisdiction_Type"] == "STATE"]
    .groupby(["State_Abb_Classified", "panel_year"])
    .agg(
        State_Govt_Water_Amt_Annual=("Amt Issued", "sum"),
        State_Govt_Water_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"State_Abb_Classified": "State", "panel_year": "Year"})
)

city_own = (
    water_year[water_year["is_in_578_panel"] == True]
    .groupby(["city_fips7", "panel_year"])
    .agg(
        City_Own_Water_Amt_Annual=("Amt Issued", "sum"),
        City_Own_Water_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"city_fips7": "FIPS", "panel_year": "Year"})
)
city_own["FIPS"] = city_own["FIPS"].astype(int)

city_own_govt = (
    water_year[(water_year["is_in_578_panel"] == True) & (water_year["Jurisdiction_Type"] == "STATE")]
    .groupby(["city_fips7", "panel_year"])
    .agg(
        City_Own_Water_Govt_Amt_Annual=("Amt Issued", "sum"),
        City_Own_Water_Govt_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"city_fips7": "FIPS", "panel_year": "Year"})
)
city_own_govt["FIPS"] = city_own_govt["FIPS"].astype(int)

# Skeleton
skel = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={
        "fips7": "FIPS", "geo_name": "City",
        "city_name": "City_Name", "state_abb": "State",
    })
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)

df = (
    skel
    .merge(state_total, on=["State", "Year"], how="left")
    .merge(state_govt, on=["State", "Year"], how="left")
    .merge(city_own, on=["FIPS", "Year"], how="left")
    .merge(city_own_govt, on=["FIPS", "Year"], how="left")
)

annual_cols = [
    "State_Total_Water_Amt_Annual", "State_Total_Water_Count_Annual",
    "State_Govt_Water_Amt_Annual", "State_Govt_Water_Count_Annual",
    "City_Own_Water_Amt_Annual", "City_Own_Water_Count_Annual",
    "City_Own_Water_Govt_Amt_Annual", "City_Own_Water_Govt_Count_Annual",
]
df[annual_cols] = df[annual_cols].fillna(0)

# Ex-focal-city aggregates
df["State_Total_Water_Ex_City_Amt_Annual"] = df["State_Total_Water_Amt_Annual"] - df["City_Own_Water_Amt_Annual"]
df["State_Total_Water_Ex_City_Count_Annual"] = df["State_Total_Water_Count_Annual"] - df["City_Own_Water_Count_Annual"]
df["State_Govt_Water_Ex_City_Amt_Annual"] = df["State_Govt_Water_Amt_Annual"] - df["City_Own_Water_Govt_Amt_Annual"]
df["State_Govt_Water_Ex_City_Count_Annual"] = df["State_Govt_Water_Count_Annual"] - df["City_Own_Water_Govt_Count_Annual"]

# Cumulative within each city across years
df = df.sort_values(["FIPS", "Year"]).reset_index(drop=True)
for annual_col in [
    "State_Total_Water_Amt_Annual", "State_Total_Water_Count_Annual",
    "State_Govt_Water_Amt_Annual", "State_Govt_Water_Count_Annual",
    "State_Total_Water_Ex_City_Amt_Annual", "State_Total_Water_Ex_City_Count_Annual",
    "State_Govt_Water_Ex_City_Amt_Annual", "State_Govt_Water_Ex_City_Count_Annual",
    "City_Own_Water_Amt_Annual", "City_Own_Water_Count_Annual",
    "City_Own_Water_Govt_Amt_Annual", "City_Own_Water_Govt_Count_Annual",
]:
    df[annual_col.replace("_Annual", "_Cumul")] = df.groupby("FIPS")[annual_col].cumsum()

id_cols = ["FIPS", "City", "City_Name", "State", "Year"]
total_cols = [
    "State_Total_Water_Amt_Annual", "State_Total_Water_Count_Annual",
    "State_Total_Water_Amt_Cumul", "State_Total_Water_Count_Cumul",
    "State_Govt_Water_Amt_Annual", "State_Govt_Water_Count_Annual",
    "State_Govt_Water_Amt_Cumul", "State_Govt_Water_Count_Cumul",
    "State_Total_Water_Ex_City_Amt_Annual", "State_Total_Water_Ex_City_Count_Annual",
    "State_Total_Water_Ex_City_Amt_Cumul", "State_Total_Water_Ex_City_Count_Cumul",
    "State_Govt_Water_Ex_City_Amt_Annual", "State_Govt_Water_Ex_City_Count_Annual",
    "State_Govt_Water_Ex_City_Amt_Cumul", "State_Govt_Water_Ex_City_Count_Cumul",
    "City_Own_Water_Amt_Annual", "City_Own_Water_Count_Annual",
    "City_Own_Water_Amt_Cumul", "City_Own_Water_Count_Cumul",
    "City_Own_Water_Govt_Amt_Annual", "City_Own_Water_Govt_Count_Annual",
    "City_Own_Water_Govt_Amt_Cumul", "City_Own_Water_Govt_Count_Cumul",
]
df = df[id_cols + total_cols].sort_values(["State", "City", "Year"]).reset_index(drop=True)

assert df.shape[0] == 578 * 13
assert df.groupby(["FIPS", "Year"]).size().max() == 1

OUT.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT / "state_controls_city_year_panel_water_only.csv", index=False)
print(f"State water panel: {df.shape}")
print(f"Total water Amt Cumul at Y=2025: ${df[df.Year==2025].State_Total_Water_Amt_Cumul.sum()/1e9:.2f}B")

# =============================================================================
# PART B: Nearby (regional) water-only panel
# =============================================================================
print("\n=== PART B: Nearby (regional) water-only panel ===")

# Load issuer coordinates
issuers = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
iss_coords = issuers[["Issuer_Name", "lat", "lng"]].drop_duplicates("Issuer_Name")

# Filter to non-state water bonds with coordinates
nearby_bonds = water_year[water_year["Jurisdiction_Type"] != "STATE"].copy()
nearby_bonds = nearby_bonds.merge(iss_coords, left_on="Issuer Name", right_on="Issuer_Name", how="left")
nearby_bonds = nearby_bonds[nearby_bonds["lat"].notna() & nearby_bonds["lng"].notna()].copy()
print(f"Non-state water bonds with coords: {len(nearby_bonds)}")

bond_lat = nearby_bonds["lat"].to_numpy()
bond_lng = nearby_bonds["lng"].to_numpy()
bond_year = nearby_bonds["panel_year"].to_numpy()
bond_amt = nearby_bonds["Amt Issued"].to_numpy()
bond_jur = nearby_bonds["Jurisdiction_Type"].to_numpy()
bond_fips = nearby_bonds["city_fips7"].to_numpy()

def haversine_km(lat0, lng0, lats, lngs):
    lat0_r = np.radians(lat0)
    lng0_r = np.radians(lng0)
    lats_r = np.radians(lats)
    lngs_r = np.radians(lngs)
    dlat = lats_r - lat0_r
    dlng = lngs_r - lng0_r
    a = np.sin(dlat / 2) ** 2 + np.cos(lat0_r) * np.cos(lats_r) * np.sin(dlng / 2) ** 2
    return EARTH_RADIUS_KM * 2 * np.arcsin(np.sqrt(a))

centroids = pd.read_csv("/tmp/crosswalk_city_centroids.csv")
centroids = centroids[centroids["city_lat"].notna()].copy()
print(f"Focal cities: {len(centroids)}")

records = []
for i, row in enumerate(centroids.itertuples(index=False)):
    f_fips = row.fips7
    d = haversine_km(row.city_lat, row.city_lng, bond_lat, bond_lng)
    not_self = ~((bond_fips == f_fips) & ~np.isnan(bond_fips))

    for r_km in RADII_KM:
        mask = (d <= r_km) & not_self
        if not mask.any():
            continue
        sub_year = bond_year[mask]
        sub_amt = bond_amt[mask]
        sub_jur = bond_jur[mask]

        df_sub = pd.DataFrame({"year": sub_year, "amt": sub_amt, "jur": sub_jur})
        tot = df_sub.groupby("year").agg(amt=("amt", "sum"), cnt=("amt", "count")).reset_index()
        tot["jur_label"] = "NonState_Water_Total"
        per = df_sub.groupby(["year", "jur"]).agg(amt=("amt", "sum"), cnt=("amt", "count")).reset_index()
        per = per.rename(columns={"jur": "jur_label"})
        per["jur_label"] = "Water_" + per["jur_label"]
        long = pd.concat([tot, per], ignore_index=True)
        long["radius"] = r_km
        long["FIPS"] = f_fips
        records.append(long)

    if (i + 1) % 100 == 0:
        print(f"  {i + 1}/{len(centroids)}", flush=True)

long_df = pd.concat(records, ignore_index=True) if records else pd.DataFrame()
print(f"Long records: {len(long_df)}")

if len(long_df):
    long_df["col_amt"] = "Nearby_" + long_df["jur_label"] + "_Amt_" + long_df["radius"].astype(str) + "km_Annual"
    long_df["col_cnt"] = "Nearby_" + long_df["jur_label"] + "_Count_" + long_df["radius"].astype(str) + "km_Annual"

    amt_wide = long_df.pivot_table(index=["FIPS", "year"], columns="col_amt", values="amt", fill_value=0).reset_index()
    cnt_wide = long_df.pivot_table(index=["FIPS", "year"], columns="col_cnt", values="cnt", fill_value=0).reset_index()
    wide = amt_wide.merge(cnt_wide, on=["FIPS", "year"], how="outer").fillna(0)
    wide = wide.rename(columns={"year": "Year"})
else:
    wide = pd.DataFrame({"FIPS": [], "Year": []})

# Skeleton
skel_n = (
    centroids[["fips7", "geo_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
skel_n = skel_n.merge(
    crosswalk[["fips7", "city_name"]].rename(columns={"fips7": "FIPS", "city_name": "City_Name"}),
    on="FIPS", how="left"
)

panel_n = skel_n.merge(wide, on=["FIPS", "Year"], how="left")
num_cols = [c for c in panel_n.columns if c.startswith("Nearby_")]
panel_n[num_cols] = panel_n[num_cols].fillna(0)

# Ensure all expected columns exist
for r_km in RADII_KM:
    for label in ["NonState_Water_Total"] + [f"Water_{b}" for b in NONSTATE_BUCKETS]:
        for metric in ["Amt", "Count"]:
            col = f"Nearby_{label}_{metric}_{r_km}km_Annual"
            if col not in panel_n.columns:
                panel_n[col] = 0

panel_n = panel_n.sort_values(["FIPS", "Year"]).reset_index(drop=True)
annual_cols_n = [c for c in panel_n.columns if c.endswith("_Annual")]
for c in annual_cols_n:
    panel_n[c.replace("_Annual", "_Cumul")] = panel_n.groupby("FIPS")[c].cumsum()

id_cols_n = ["FIPS", "City", "City_Name", "State", "Year"]
ordered_n = list(id_cols_n)
for r_km in RADII_KM:
    for label in ["NonState_Water_Total"] + [f"Water_{b}" for b in NONSTATE_BUCKETS]:
        for metric in ["Amt", "Count"]:
            for suffix in ["Annual", "Cumul"]:
                col = f"Nearby_{label}_{metric}_{r_km}km_{suffix}"
                if col in panel_n.columns:
                    ordered_n.append(col)
panel_n = panel_n[ordered_n].sort_values(["State", "City", "Year"]).reset_index(drop=True)

assert panel_n.shape[0] == 578 * 13

panel_n.to_csv(OUT / "nearby_by_jurisdiction_panel_water_only.csv", index=False)
print(f"\nNearby water panel: {panel_n.shape}")
print(f"Total water Amt Cumul 25km at Y=2025: ${panel_n[panel_n.Year==2025].Nearby_NonState_Water_Total_Amt_25km_Cumul.sum()/1e9:.2f}B")
print(f"Written: {OUT / 'state_controls_city_year_panel_water_only.csv'}")
print(f"Written: {OUT / 'nearby_by_jurisdiction_panel_water_only.csv'}")
