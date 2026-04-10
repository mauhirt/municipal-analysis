"""
Build File 2: Control variables panel.

Inputs:
  raw/bloomberg/bonds_with_issuer_classification.xlsx  (CUSIP level)
  raw/bloomberg/green_bond_issuers_assignments.csv     (issuer -> city bridge)
  raw/crosswalk/Crosswalk.csv                          (578 target cities)
  /tmp/crosswalk_city_centroids.csv                    (geocoded city centroids)

Output:
  processed/control_variables_panel.xlsx (and .csv)

Structure: 578 cities x 13 years (2013-2025), keyed on FIPS.

Variables:
  STATE-LEVEL:
    State_All_Total_{Amt,Count}_Annual  - all bonds in state, year Y
    State_All_Total_{Amt,Count}_Cumul   - all bonds in state, cumulative through Y
    State_All_Govt_{Amt,Count}_Annual   - state-jurisdiction bonds, year Y
    State_All_Govt_{Amt,Count}_Cumul    - state-jurisdiction bonds, cumulative
    State_Green_Total_{Amt,Count}_Annual - green bonds in state, year Y
    State_Green_Total_{Amt,Count}_Cumul  - green bonds in state, cumulative
    State_Green_Govt_{Amt,Count}_Annual  - state-jurisdiction green bonds, year Y
    State_Green_Govt_{Amt,Count}_Cumul   - state-jurisdiction green bonds, cumulative

  NEARBY ISSUANCES (10mi / 25mi / 50mi of city centroid):
    Distance measured from focal city centroid to issuer lat/lng
    Excludes issuers assigned to the focal city itself
    Split by:
      - OtherLargeCity: other 578 cities (city-assigned issuers, different fips7)
      - NonLargeCity:   jurisdiction_type == CITY but not in 578
      - NonCity:        jurisdiction_type != CITY
    For each split: Amt + Count x All + Green x Annual + Cumulative
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed"
YEARS = list(range(2013, 2026))

# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
bonds = pd.read_excel(RAW / "bonds_with_issuer_classification.xlsx")
assign = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")
city_coords = pd.read_csv("/tmp/crosswalk_city_centroids.csv")

bonds = bonds.merge(
    assign[["Issuer_Name", "city_fips7", "lat", "lng"]],
    left_on="Issuer Name",
    right_on="Issuer_Name",
    how="left",
)

# Year clean-up
bonds["derived_year"] = pd.to_datetime(bonds["Issue Date"], errors="coerce").dt.year
bonds["panel_year"] = bonds["Year"].where(
    (bonds["Year"] >= 2013) & (bonds["Year"] <= 2030), bonds["derived_year"]
)
bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)
bonds["is_green"] = bonds["Self-reported Green"].astype(str).str.strip() == "Yes"

# ---------------------------------------------------------------------------
# Skeleton
# ---------------------------------------------------------------------------
skeleton = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "city_name": "City_Name", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)

# ---------------------------------------------------------------------------
# STATE-LEVEL AGGREGATES
# ---------------------------------------------------------------------------
def state_agg(df, label):
    g = (
        df.groupby(["State_Abb_Classified", "panel_year"])
        .agg(**{
            f"State_{label}_Amt_Annual": ("Amt Issued", "sum"),
            f"State_{label}_Count_Annual": ("CUSIP", "count"),
        })
        .reset_index()
        .rename(columns={"State_Abb_Classified": "State", "panel_year": "Year"})
    )
    return g

all_state = state_agg(bonds, "All_Total")
govt_state = state_agg(bonds[bonds["Jurisdiction_Type"] == "STATE"], "All_Govt")
green_state = state_agg(bonds[bonds["is_green"]], "Green_Total")
green_govt_state = state_agg(
    bonds[bonds["is_green"] & (bonds["Jurisdiction_Type"] == "STATE")], "Green_Govt"
)

state_frame = (
    skeleton[["State", "Year"]].drop_duplicates()
    .merge(all_state, on=["State", "Year"], how="left")
    .merge(govt_state, on=["State", "Year"], how="left")
    .merge(green_state, on=["State", "Year"], how="left")
    .merge(green_govt_state, on=["State", "Year"], how="left")
    .fillna(0)
)

# Cumulative within state over years
state_frame = state_frame.sort_values(["State", "Year"])
for col in [
    "State_All_Total_Amt", "State_All_Total_Count",
    "State_All_Govt_Amt", "State_All_Govt_Count",
    "State_Green_Total_Amt", "State_Green_Total_Count",
    "State_Green_Govt_Amt", "State_Green_Govt_Count",
]:
    state_frame[f"{col}_Cumul"] = state_frame.groupby("State")[f"{col}_Annual"].cumsum()

print(f"State frame built: {state_frame.shape}")
state_frame.to_parquet("/tmp/state_frame.parquet", index=False)
print("Saved state frame to /tmp/state_frame.parquet")
