"""
Merge the state-controls and nearby-by-jurisdiction panels into a single
consolidated city-year controls file.

Inputs:
  processed/state_controls_city_year_panel.csv        (7,514 x 29)
  processed/nearby_by_jurisdiction_panel.csv          (7,514 x 89)

Output:
  processed/controls_city_year_panel.{csv,xlsx}
  7,514 rows (578 cities x 13 years), keyed on FIPS x Year.
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "processed"

state = pd.read_csv(OUT / "state_controls_city_year_panel.csv")
nearby = pd.read_csv(OUT / "nearby_by_jurisdiction_panel.csv")

# Drop duplicate ID columns from nearby so the merge is clean
dup_cols = ["City", "City_Name", "State"]
nearby = nearby.drop(columns=[c for c in dup_cols if c in nearby.columns])

merged = state.merge(nearby, on=["FIPS", "Year"], how="left")

assert merged.shape[0] == 7514, f"Expected 7514 rows, got {merged.shape[0]}"
assert merged.groupby(["FIPS", "Year"]).size().max() == 1
assert merged[["FIPS", "City", "State"]].drop_duplicates().shape[0] == 578

merged = merged.sort_values(["State", "City", "Year"]).reset_index(drop=True)

merged.to_csv(OUT / "controls_city_year_panel.csv", index=False)
merged.to_excel(OUT / "controls_city_year_panel.xlsx", index=False)

print(f"Merged panel shape: {merged.shape}")
print(f"  Id columns: 5")
print(f"  State-control columns: {sum(1 for c in merged.columns if c.startswith('State_') or c.startswith('City_Own'))}")
print(f"  Nearby columns: {sum(1 for c in merged.columns if c.startswith('Nearby_'))}")
print(f"Written: {OUT / 'controls_city_year_panel.xlsx'}")
