"""
Build consolidated city-year state-controls panel (all 578 cities in one file).

Input:
  raw/bloomberg/cusip_with_assignment.csv
  raw/crosswalk/Crosswalk.csv

Output:
  processed/state_controls_city_year_panel.{csv,xlsx}

Structure: 578 cities x 13 years (2013-2025), keyed on FIPS.

Columns:
  FIPS, City, City_Name, State, Year
  State_Total_Amt_Annual / _Cumul            all green bonds in the state
  State_Total_Count_Annual / _Cumul
  State_Govt_Amt_Annual / _Cumul             state-jurisdiction bonds only
  State_Govt_Count_Annual / _Cumul
  State_Total_Ex_City_Amt_Annual / _Cumul    state total minus focal city
  State_Total_Ex_City_Count_Annual / _Cumul
  State_Govt_Ex_City_Amt_Annual / _Cumul     state govt minus focal city
  State_Govt_Ex_City_Count_Annual / _Cumul
  City_Own_Amt_Annual                        focal city's own issuance
  City_Own_Count_Annual
  City_Own_Govt_Amt_Annual                   focal city's state-jurisdiction subset
  City_Own_Govt_Count_Annual

NOTE: cusip_with_assignment.csv contains only green bonds.
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed"
YEARS = list(range(2013, 2026))

# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
bonds = pd.read_csv(RAW / "cusip_with_assignment.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)
bonds = bonds[bonds["State_Abb_Classified"].notna()]
bonds = bonds[~bonds["State_Abb_Classified"].str.contains("N/A", na=False)]
bonds["city_fips7"] = pd.to_numeric(bonds["city_fips7"], errors="coerce")

# ---------------------------------------------------------------------------
# State-level aggregates (all cities in a state share these)
# ---------------------------------------------------------------------------
state_total = (
    bonds.groupby(["State_Abb_Classified", "panel_year"])
    .agg(
        State_Total_Amt_Annual=("Amt Issued", "sum"),
        State_Total_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"State_Abb_Classified": "State", "panel_year": "Year"})
)

state_govt = (
    bonds[bonds["Jurisdiction_Type"] == "STATE"]
    .groupby(["State_Abb_Classified", "panel_year"])
    .agg(
        State_Govt_Amt_Annual=("Amt Issued", "sum"),
        State_Govt_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"State_Abb_Classified": "State", "panel_year": "Year"})
)

# ---------------------------------------------------------------------------
# Per-city own issuance (only 578-city-assigned bonds)
# ---------------------------------------------------------------------------
city_own = (
    bonds[bonds["is_in_578_panel"] == True]
    .groupby(["city_fips7", "panel_year"])
    .agg(
        City_Own_Amt_Annual=("Amt Issued", "sum"),
        City_Own_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"city_fips7": "FIPS", "panel_year": "Year"})
)
city_own["FIPS"] = city_own["FIPS"].astype(int)

city_own_govt = (
    bonds[(bonds["is_in_578_panel"] == True) & (bonds["Jurisdiction_Type"] == "STATE")]
    .groupby(["city_fips7", "panel_year"])
    .agg(
        City_Own_Govt_Amt_Annual=("Amt Issued", "sum"),
        City_Own_Govt_Count_Annual=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"city_fips7": "FIPS", "panel_year": "Year"})
)
city_own_govt["FIPS"] = city_own_govt["FIPS"].astype(int)

# ---------------------------------------------------------------------------
# Build single skeleton (all 578 cities x 13 years)
# ---------------------------------------------------------------------------
skel = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={
        "fips7": "FIPS", "geo_name": "City",
        "city_name": "City_Name", "state_abb": "State",
    })
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)

# Merge everything
df = (
    skel
    .merge(state_total, on=["State", "Year"], how="left")
    .merge(state_govt, on=["State", "Year"], how="left")
    .merge(city_own, on=["FIPS", "Year"], how="left")
    .merge(city_own_govt, on=["FIPS", "Year"], how="left")
)

annual_cols = [
    "State_Total_Amt_Annual", "State_Total_Count_Annual",
    "State_Govt_Amt_Annual", "State_Govt_Count_Annual",
    "City_Own_Amt_Annual", "City_Own_Count_Annual",
    "City_Own_Govt_Amt_Annual", "City_Own_Govt_Count_Annual",
]
df[annual_cols] = df[annual_cols].fillna(0)

# Ex-city
df["State_Total_Ex_City_Amt_Annual"] = df["State_Total_Amt_Annual"] - df["City_Own_Amt_Annual"]
df["State_Total_Ex_City_Count_Annual"] = df["State_Total_Count_Annual"] - df["City_Own_Count_Annual"]
df["State_Govt_Ex_City_Amt_Annual"] = df["State_Govt_Amt_Annual"] - df["City_Own_Govt_Amt_Annual"]
df["State_Govt_Ex_City_Count_Annual"] = df["State_Govt_Count_Annual"] - df["City_Own_Govt_Count_Annual"]

# Cumulative within each city across years
df = df.sort_values(["FIPS", "Year"]).reset_index(drop=True)
for annual_col in [
    "State_Total_Amt_Annual", "State_Total_Count_Annual",
    "State_Govt_Amt_Annual", "State_Govt_Count_Annual",
    "State_Total_Ex_City_Amt_Annual", "State_Total_Ex_City_Count_Annual",
    "State_Govt_Ex_City_Amt_Annual", "State_Govt_Ex_City_Count_Annual",
    "City_Own_Amt_Annual", "City_Own_Count_Annual",
    "City_Own_Govt_Amt_Annual", "City_Own_Govt_Count_Annual",
]:
    df[annual_col.replace("_Annual", "_Cumul")] = df.groupby("FIPS")[annual_col].cumsum()

# Column order
id_cols = ["FIPS", "City", "City_Name", "State", "Year"]
total_cols = [
    "State_Total_Amt_Annual", "State_Total_Count_Annual",
    "State_Total_Amt_Cumul", "State_Total_Count_Cumul",
    "State_Govt_Amt_Annual", "State_Govt_Count_Annual",
    "State_Govt_Amt_Cumul", "State_Govt_Count_Cumul",
    "State_Total_Ex_City_Amt_Annual", "State_Total_Ex_City_Count_Annual",
    "State_Total_Ex_City_Amt_Cumul", "State_Total_Ex_City_Count_Cumul",
    "State_Govt_Ex_City_Amt_Annual", "State_Govt_Ex_City_Count_Annual",
    "State_Govt_Ex_City_Amt_Cumul", "State_Govt_Ex_City_Count_Cumul",
    "City_Own_Amt_Annual", "City_Own_Count_Annual",
    "City_Own_Amt_Cumul", "City_Own_Count_Cumul",
    "City_Own_Govt_Amt_Annual", "City_Own_Govt_Count_Annual",
    "City_Own_Govt_Amt_Cumul", "City_Own_Govt_Count_Cumul",
]
df = df[id_cols + total_cols]
df = df.sort_values(["State", "City", "Year"]).reset_index(drop=True)

assert df.groupby(["FIPS", "Year"]).size().max() == 1
assert df[["FIPS", "City", "State"]].drop_duplicates().shape[0] == 578

OUT.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT / "state_controls_city_year_panel.csv", index=False)
df.to_excel(OUT / "state_controls_city_year_panel.xlsx", index=False)

print(f"Panel shape: {df.shape}")
print(f"Unique cities: {df['FIPS'].nunique()}")
print(f"Year range: {df['Year'].min()}-{df['Year'].max()}")
print(f"Written: {OUT / 'state_controls_city_year_panel.xlsx'}")
