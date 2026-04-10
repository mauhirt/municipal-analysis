"""
Merge state-level aggregates + nearby-issuance frame into the full control panel.
Produces processed/control_variables_panel.{xlsx,csv}
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "processed"
YEARS = list(range(2013, 2026))

state_frame = pd.read_parquet("/tmp/state_frame.parquet")
nearby_frame = pd.read_parquet("/tmp/nearby_frame.parquet")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

skeleton = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "city_name": "City_Name", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)

panel = (
    skeleton
    .merge(state_frame, on=["State", "Year"], how="left")
    .merge(nearby_frame, on=["FIPS", "Year"], how="left")
)

# Fill numeric NaNs with 0
num_cols = panel.select_dtypes(include="number").columns
panel[num_cols] = panel[num_cols].fillna(0)

assert panel.groupby(["FIPS", "Year"]).size().max() == 1
assert panel[["FIPS", "City", "State"]].drop_duplicates().shape[0] == 578

# Column order
id_cols = ["FIPS", "City", "City_Name", "State", "Year"]
state_cols = [c for c in panel.columns if c.startswith("State_")]
nearby_cols = [c for c in panel.columns if c.startswith("Nearby_")]
other = [c for c in panel.columns if c not in id_cols + state_cols + nearby_cols]
panel = panel[id_cols + state_cols + nearby_cols + other]
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
panel.to_csv(OUT / "control_variables_panel.csv", index=False)
panel.to_excel(OUT / "control_variables_panel.xlsx", index=False)

print(f"Control panel shape: {panel.shape}")
print(f"State columns: {len(state_cols)}")
print(f"Nearby columns: {len(nearby_cols)}")
print(f"Written: {OUT / 'control_variables_panel.xlsx'}")
