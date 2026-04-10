"""
Build File 1: Outcome variables panel (green bond issuances at city level).

Input:
  raw/bloomberg/bonds_with_issuer_classification.xlsx
  raw/bloomberg/green_bond_issuers_assignments.csv
  raw/crosswalk/Crosswalk.csv

Output:
  processed/outcome_green_issuance_panel.xlsx (and .csv)

Structure: 578 cities x 13 years (2013-2025), keyed on FIPS (verified with city+state).
Contains ONLY green bond data:
  - Green_Bond_Issued flag + City_Green_Amt_Issued + count
  - Amt_* / Count_* pivots for all categorical fields, filtered to Self-reported Green == "Yes"
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
bonds = pd.read_excel(RAW / "bonds_with_issuer_classification.xlsx")
assign = pd.read_csv(RAW / "green_bond_issuers_assignments.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

bonds = bonds.merge(
    assign[["Issuer_Name", "city_fips7"]],
    left_on="Issuer Name",
    right_on="Issuer_Name",
    how="left",
)

# Year clean-up: prefer Year, fall back to Issue Date if Year is implausible
bonds["derived_year"] = pd.to_datetime(bonds["Issue Date"], errors="coerce").dt.year
bonds["panel_year"] = bonds["Year"].where(
    (bonds["Year"] >= 2013) & (bonds["Year"] <= 2030), bonds["derived_year"]
)
bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)

# ---------------------------------------------------------------------------
# Keep only GREEN bonds (Self-reported Green == "Yes") assigned to a city
# ---------------------------------------------------------------------------
green = bonds[bonds["Self-reported Green"].astype(str).str.strip() == "Yes"].copy()
green = green[green["city_fips7"].notna()].copy()
green["city_fips7"] = green["city_fips7"].astype(int)
print(f"Green bond rows assigned to a 578-city: {len(green)}")

# ---------------------------------------------------------------------------
# Build skeleton (578 x 13)
# ---------------------------------------------------------------------------
skeleton = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "city_name": "City_Name", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
print(f"Skeleton: {len(skeleton)} rows ({skeleton['FIPS'].nunique()} cities x {len(YEARS)} years)")

# ---------------------------------------------------------------------------
# Top-level green totals per city-year
# ---------------------------------------------------------------------------
totals = (
    green.groupby(["city_fips7", "panel_year"])
    .agg(
        City_Green_Amt_Issued=("Amt Issued", "sum"),
        City_Green_Issuance_Count=("CUSIP", "count"),
    )
    .reset_index()
    .rename(columns={"city_fips7": "FIPS", "panel_year": "Year"})
)

panel = skeleton.merge(totals, on=["FIPS", "Year"], how="left").fillna(
    {"City_Green_Amt_Issued": 0, "City_Green_Issuance_Count": 0}
)
panel["Green_Bond_Issued"] = (panel["City_Green_Issuance_Count"] > 0).astype(int)

# ---------------------------------------------------------------------------
# Categorical pivots (restricted to green bonds only)
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


def normalise_value(v):
    if pd.isna(v):
        return None
    return str(v).strip().replace(" ", "_")


def build_pivot(df, field, key_cols):
    tmp = df[df[field].notna()].copy()
    if len(tmp) == 0:
        return pd.DataFrame(columns=key_cols)
    tmp["_value"] = tmp[field].apply(normalise_value)
    amt = (
        tmp.groupby(key_cols + ["_value"])["Amt Issued"]
        .sum()
        .unstack("_value", fill_value=0)
    )
    amt.columns = [f"Amt_{field}__{v}" for v in amt.columns]
    cnt = (
        tmp.groupby(key_cols + ["_value"])["CUSIP"]
        .count()
        .unstack("_value", fill_value=0)
    )
    cnt.columns = [f"Count_{field}__{v}" for v in cnt.columns]
    return amt.join(cnt).reset_index()


green_keyed = green.drop(columns=["Year"]).rename(columns={"city_fips7": "FIPS", "panel_year": "Year"})
for field in CATEGORICAL_FIELDS:
    pivot = build_pivot(green_keyed, field, ["FIPS", "Year"])
    if len(pivot) > 0:
        panel = panel.merge(pivot, on=["FIPS", "Year"], how="left")

# Fill pivot NaNs with 0
pivot_cols = [c for c in panel.columns if c.startswith("Amt_") or c.startswith("Count_")]
panel[pivot_cols] = panel[pivot_cols].fillna(0)

# ---------------------------------------------------------------------------
# Verify: FIPS + City + State combo uniqueness
# ---------------------------------------------------------------------------
assert panel.groupby(["FIPS", "Year"]).size().max() == 1, "Duplicate (FIPS, Year) pairs"
assert panel[["FIPS", "City", "State"]].drop_duplicates().shape[0] == 578, "Not 578 unique cities"

# Column order
id_cols = [
    "FIPS", "City", "City_Name", "State", "Year",
    "Green_Bond_Issued", "City_Green_Amt_Issued", "City_Green_Issuance_Count",
]
other_cols = [c for c in panel.columns if c not in id_cols]
panel = panel[id_cols + other_cols]
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
panel.to_excel(OUT / "outcome_green_issuance_panel.xlsx", index=False)
panel.to_csv(OUT / "outcome_green_issuance_panel.csv", index=False)

print(f"\nFile 1 shape: {panel.shape}")
print(f"Cities with any green bond ever: {panel.groupby('FIPS')['Green_Bond_Issued'].max().sum()}")
print(f"City-year cells with green bond: {panel['Green_Bond_Issued'].sum()}")
print(f"Written: {OUT / 'outcome_green_issuance_panel.xlsx'}")
