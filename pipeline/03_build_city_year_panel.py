"""
Build city-year issuance panel from CUSIP-level bonds data.

Input:
  raw/bloomberg/bonds_with_issuer_classification.xlsx  (CUSIP level, 25,555 rows)
  raw/bloomberg/green_bond_issuers_assignments.csv     (issuer -> city_fips7 bridge)
  raw/crosswalk/Crosswalk.csv                          (578 target cities)

Output:
  processed/city_year_issuance_panel.xlsx             (city x year panel)
  processed/city_year_issuance_panel.csv

Group by: city_fips7 x Year (2013-2025)
Panel includes all 578 cities x 13 years (zeros for no-issuance cells).
Produces Amt_* and Count_* columns for each categorical field value.
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed"
YEARS = list(range(2013, 2026))  # 2013..2025 inclusive

# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------
bonds = pd.read_excel(RAW / "bonds_with_issuer_classification.xlsx")
assign = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

# Merge bonds with city assignment
bonds = bonds.merge(
    assign[["Issuer_Name", "city_fips7", "city_geo_name", "city_name_crosswalk"]],
    left_on="Issuer Name",
    right_on="Issuer_Name",
    how="left",
)

# Use Year field, fall back to Issue Date year if Year is missing or > 2030 (bad data)
bonds["derived_year"] = pd.to_datetime(bonds["Issue Date"], errors="coerce").dt.year
# Prefer derived_year when Year is implausible (> 2030 - before any maturity)
bonds["panel_year"] = bonds["Year"].where(
    (bonds["Year"] >= 2013) & (bonds["Year"] <= 2030), bonds["derived_year"]
)
bonds = bonds[bonds["panel_year"].notna()]
bonds["panel_year"] = bonds["panel_year"].astype(int)

# ---------------------------------------------------------------------------
# Normalise categorical value -> column suffix
# ---------------------------------------------------------------------------
def normalise_value(v):
    """Replace spaces with underscores; leave other chars alone."""
    if pd.isna(v):
        return None
    return str(v).strip().replace(" ", "_")


# ---------------------------------------------------------------------------
# Compute state-level totals (across ALL issuers in the state, no city filter)
# ---------------------------------------------------------------------------
state_totals = (
    bonds.groupby(["State_Abb_Classified", "panel_year"])
    .agg(
        State_Total_Amt_Issued=("Amt Issued", "sum"),
        State_Total_Issuance_Count=("CUSIP", "count"),
    )
    .reset_index()
)

state_govt = (
    bonds[bonds["Jurisdiction_Type"] == "STATE"]
    .groupby(["State_Abb_Classified", "panel_year"])
    .agg(
        State_Govt_Amt_Issued=("Amt Issued", "sum"),
        State_Govt_Issuance_Count=("CUSIP", "count"),
    )
    .reset_index()
)

state_frame = state_totals.merge(
    state_govt, on=["State_Abb_Classified", "panel_year"], how="left"
).fillna({"State_Govt_Amt_Issued": 0, "State_Govt_Issuance_Count": 0})

# ---------------------------------------------------------------------------
# Filter to only city-assigned rows for the panel
# ---------------------------------------------------------------------------
city_bonds = bonds[bonds["city_fips7"].notna()].copy()
city_bonds["city_fips7"] = city_bonds["city_fips7"].astype(int)
print(f"Bonds assigned to a city: {len(city_bonds)}/{len(bonds)}")
print(f"Unique city-year combinations with bonds: {len(city_bonds.groupby(['city_fips7','panel_year']))}")

# Build the full 578 x YEARS skeleton so every city appears every year
city_skeleton = crosswalk[["fips7", "geo_name", "city_name", "state_abb"]].copy()
city_skeleton.columns = ["city_fips7", "city_geo_name", "city_name_crosswalk", "State_Abb_Classified"]
skeleton = city_skeleton.merge(pd.DataFrame({"panel_year": YEARS}), how="cross")
print(f"Full skeleton: {len(skeleton)} rows ({skeleton['city_fips7'].nunique()} cities x {len(YEARS)} years)")

# ---------------------------------------------------------------------------
# Top-level city-year totals
# ---------------------------------------------------------------------------
city_agg = (
    city_bonds.groupby(["city_fips7", "panel_year"])
    .agg(
        City_Total_Amt_Issued=("Amt Issued", "sum"),
        City_Total_Issuance_Count=("CUSIP", "count"),
    )
    .reset_index()
)
# Start with the full skeleton and left-merge the aggregates
top_level = skeleton.merge(city_agg, on=["city_fips7", "panel_year"], how="left").fillna(
    {"City_Total_Amt_Issued": 0, "City_Total_Issuance_Count": 0}
)

green_mask = city_bonds["Self-reported Green"].astype(str).str.strip() == "Yes"
green_totals = (
    city_bonds[green_mask]
    .groupby(["city_fips7", "panel_year"])
    .agg(
        City_Green_Amt_Issued=("Amt Issued", "sum"),
        City_Green_Issuance_Count=("CUSIP", "count"),
    )
    .reset_index()
)

top_level = top_level.merge(green_totals, on=["city_fips7", "panel_year"], how="left").fillna(
    {"City_Green_Amt_Issued": 0, "City_Green_Issuance_Count": 0}
)
top_level["Green_Bond_Issued"] = (top_level["City_Green_Issuance_Count"] > 0).astype(int)

# Merge state totals
top_level = top_level.merge(state_frame, on=["State_Abb_Classified", "panel_year"], how="left")
top_level["City_Share_of_State_Pct"] = (
    top_level["City_Total_Amt_Issued"] / top_level["State_Total_Amt_Issued"].replace(0, pd.NA) * 100
).round(4)
# Fill state totals with 0 for cells where the state has no activity that year
for col in ["State_Total_Amt_Issued", "State_Total_Issuance_Count",
            "State_Govt_Amt_Issued", "State_Govt_Issuance_Count"]:
    top_level[col] = top_level[col].fillna(0)
top_level["City_Share_of_State_Pct"] = top_level["City_Share_of_State_Pct"].fillna(0)

# ---------------------------------------------------------------------------
# Categorical pivots: produce Amt_* and Count_* per value per field
# ---------------------------------------------------------------------------
CATEGORICAL_FIELDS = [
    "Tax Prov",
    "Fin Typ",
    "BICS Level 2",
    "Self-reported Green",
    "Mgmt of Proc",
    "ESG Reporting",
    "ESG Assurance Providers",
    "Proj Sel Proc",
    "ESG Framework",
    "Industry",
    "Industry_Full",
    "Kestrel Total ESG Impact Score",
    "ESG Project Categories",
    "Project Subcategory",
]


def build_pivot(df, field, key_cols):
    """For each distinct value of `field`, produce Amt_field__value and Count_field__value."""
    tmp = df[df[field].notna()].copy()
    if len(tmp) == 0:
        return pd.DataFrame(columns=key_cols)

    tmp["_value"] = tmp[field].apply(normalise_value)

    # Pivot: sum of Amt Issued
    amt = (
        tmp.groupby(key_cols + ["_value"])["Amt Issued"]
        .sum()
        .unstack("_value", fill_value=0)
    )
    amt.columns = [f"Amt_{field}__{v}" for v in amt.columns]

    # Pivot: count of CUSIP
    cnt = (
        tmp.groupby(key_cols + ["_value"])["CUSIP"]
        .count()
        .unstack("_value", fill_value=0)
    )
    cnt.columns = [f"Count_{field}__{v}" for v in cnt.columns]

    return amt.join(cnt).reset_index()


key_cols = ["city_fips7", "panel_year"]
panel = top_level.copy()

for field in CATEGORICAL_FIELDS:
    pivot = build_pivot(city_bonds, field, key_cols)
    if len(pivot) > 0:
        panel = panel.merge(pivot, on=key_cols, how="left")

# Fill NaN in pivoted numeric columns with 0
pivot_cols = [c for c in panel.columns if c.startswith("Amt_") or c.startswith("Count_")]
panel[pivot_cols] = panel[pivot_cols].fillna(0)

# ---------------------------------------------------------------------------
# Final column order
# ---------------------------------------------------------------------------
panel = panel.rename(
    columns={
        "city_geo_name": "City",
        "city_name_crosswalk": "City_Name",
        "State_Abb_Classified": "State",
        "city_fips7": "FIPS",
        "panel_year": "Year",
    }
)

id_cols = [
    "City",
    "City_Name",
    "State",
    "FIPS",
    "Year",
    "Green_Bond_Issued",
    "City_Total_Amt_Issued",
    "City_Total_Issuance_Count",
    "City_Green_Amt_Issued",
    "City_Green_Issuance_Count",
    "State_Total_Amt_Issued",
    "State_Total_Issuance_Count",
    "State_Govt_Amt_Issued",
    "State_Govt_Issuance_Count",
    "City_Share_of_State_Pct",
]
other_cols = [c for c in panel.columns if c not in id_cols]
panel = panel[id_cols + other_cols]

panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
panel.to_excel(OUT / "city_year_issuance_panel.xlsx", index=False)
panel.to_csv(OUT / "city_year_issuance_panel.csv", index=False)

print(f"\nPanel shape: {panel.shape}")
print(f"Unique cities: {panel['FIPS'].nunique()}")
print(f"Year range: {panel['Year'].min()}-{panel['Year'].max()}")
print(f"\nWritten: {OUT / 'city_year_issuance_panel.xlsx'}")
print(f"Written: {OUT / 'city_year_issuance_panel.csv'}")
