"""
Build per-state control files.

Input:
  raw/bloomberg/cusip_with_assignment.csv
  raw/crosswalk/Crosswalk.csv

Output: one file per state in processed/state_controls/
  <STATE>_controls.csv  (and .xlsx)

Each file is a city x year panel for the cities in that state (from the
578-city crosswalk), 2013-2025. Columns:

  FIPS, City, City_Name, State, Year
  State_Total_Amt_Annual            Sum of Amt Issued, all bonds in the state
  State_Total_Count_Annual          Count of CUSIPs, all bonds in the state
  State_Govt_Amt_Annual             State-jurisdiction bonds only
  State_Govt_Count_Annual
  State_Total_Ex_City_Amt_Annual    State total minus the focal city
  State_Total_Ex_City_Count_Annual
  State_Govt_Ex_City_Amt_Annual     State govt minus the focal city
  State_Govt_Ex_City_Count_Annual
  ...and Cumul versions of each (running sum through year Y inclusive)

NOTE: cusip_with_assignment.csv only contains green bonds, so these are
all green bond aggregates.
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed" / "state_controls"
YEARS = list(range(2013, 2026))

# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
bonds = pd.read_csv(RAW / "cusip_with_assignment.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

# Valid year, clean state field
bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)
bonds = bonds[bonds["State_Abb_Classified"].notna()]
bonds = bonds[~bonds["State_Abb_Classified"].str.contains("N/A", na=False)]

# Fix a possible type issue
bonds["city_fips7"] = pd.to_numeric(bonds["city_fips7"], errors="coerce")

# ---------------------------------------------------------------------------
# Compute state-level aggregates per (state, year)
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
# Per-city issuance within the state (only for 578-city-assigned bonds)
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

# Also compute city-own state-government issuance (if the city hosts any
# state-jurisdiction issuer assigned to it)
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
# Build per-state files
# ---------------------------------------------------------------------------
OUT.mkdir(parents=True, exist_ok=True)
states_written = []

for state_abb, state_cities in crosswalk.groupby("state_abb"):
    # Skeleton: cities in this state x years
    skel = (
        state_cities[["fips7", "geo_name", "city_name", "state_abb"]]
        .rename(columns={
            "fips7": "FIPS", "geo_name": "City",
            "city_name": "City_Name", "state_abb": "State",
        })
        .merge(pd.DataFrame({"Year": YEARS}), how="cross")
    )

    # Bring in state totals
    df = skel.merge(state_total, on=["State", "Year"], how="left")
    df = df.merge(state_govt, on=["State", "Year"], how="left")
    df = df.merge(city_own, on=["FIPS", "Year"], how="left")
    df = df.merge(city_own_govt, on=["FIPS", "Year"], how="left")

    # Fill missing annual values with 0
    annual_cols = [
        "State_Total_Amt_Annual", "State_Total_Count_Annual",
        "State_Govt_Amt_Annual", "State_Govt_Count_Annual",
        "City_Own_Amt_Annual", "City_Own_Count_Annual",
        "City_Own_Govt_Amt_Annual", "City_Own_Govt_Count_Annual",
    ]
    df[annual_cols] = df[annual_cols].fillna(0)

    # Ex-city (state total / govt minus this city's contribution)
    df["State_Total_Ex_City_Amt_Annual"] = df["State_Total_Amt_Annual"] - df["City_Own_Amt_Annual"]
    df["State_Total_Ex_City_Count_Annual"] = df["State_Total_Count_Annual"] - df["City_Own_Count_Annual"]
    df["State_Govt_Ex_City_Amt_Annual"] = df["State_Govt_Amt_Annual"] - df["City_Own_Govt_Amt_Annual"]
    df["State_Govt_Ex_City_Count_Annual"] = df["State_Govt_Count_Annual"] - df["City_Own_Govt_Count_Annual"]

    # Cumulative versions (running sum within each city through year Y inclusive)
    df = df.sort_values(["FIPS", "Year"]).reset_index(drop=True)
    for annual_col in [
        "State_Total_Amt_Annual", "State_Total_Count_Annual",
        "State_Govt_Amt_Annual", "State_Govt_Count_Annual",
        "State_Total_Ex_City_Amt_Annual", "State_Total_Ex_City_Count_Annual",
        "State_Govt_Ex_City_Amt_Annual", "State_Govt_Ex_City_Count_Annual",
    ]:
        cumul_col = annual_col.replace("_Annual", "_Cumul")
        df[cumul_col] = df.groupby("FIPS")[annual_col].cumsum()

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
        "City_Own_Govt_Amt_Annual", "City_Own_Govt_Count_Annual",
    ]
    df = df[id_cols + total_cols]
    df = df.sort_values(["City", "Year"]).reset_index(drop=True)

    path_csv = OUT / f"{state_abb}_controls.csv"
    path_xlsx = OUT / f"{state_abb}_controls.xlsx"
    df.to_csv(path_csv, index=False)
    df.to_excel(path_xlsx, index=False)
    states_written.append((state_abb, len(df), df["FIPS"].nunique()))

print(f"Wrote {len(states_written)} per-state control files to {OUT}")
print("\nState | rows | cities")
for s, n, c in states_written:
    print(f"  {s}  | {n:>4} | {c}")
