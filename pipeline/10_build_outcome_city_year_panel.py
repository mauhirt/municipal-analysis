"""
Build city-year outcome panel from cusip_with_assignment.csv.

NOTE: All bonds in cusip_with_assignment.csv are green bonds. The
`Self-reported Green` field just indicates whether the issuer formally
self-labeled it, not whether it counts as green. So the top-level
variables here are labelled Green_* accordingly.

Input:
  raw/bloomberg/cusip_with_assignment.csv  (CUSIP level with city_fips7 joined)
  raw/crosswalk/Crosswalk.csv              (578 target cities)

Output:
  processed/outcome_city_year_panel.xlsx  (and .csv)

Structure: 578 cities x 13 years (2013-2025), keyed on FIPS (verified city+state).

Variables per city-year:
  - Green_Bond_Issued          1 if any green bond issued in that city-year
  - City_Green_Amt_Issued      sum of Amt Issued
  - City_Green_Issuance_Count  count of CUSIPs

  For each categorical field, for every distinct value:
    Issued_{field}__{value}  1/0 flag (any bond with that attribute)
    Amt_{field}__{value}     sum of Amt Issued for those bonds
    Count_{field}__{value}   count of those bonds
"""

import pandas as pd
import re
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

# Note: cusip_duplicate_flag marks 8 rows (4 CUSIPs x 2 each) as suspected
# duplicates, but they are suspected only — could be legitimate tranches or
# Bloomberg data errors. All 4 CUSIPs have city_fips7 = NaN, so they do not
# affect this panel either way. We keep them in the input frame.
if "cusip_duplicate_flag" in bonds.columns:
    n_flagged = bonds["cusip_duplicate_flag"].sum()
    print(f"Note: {n_flagged} rows flagged as suspected duplicates (kept; none in 578-panel)")

# Keep only rows assigned to a 578-city
bonds = bonds[bonds["is_in_578_panel"] == True].copy()
bonds["city_fips7"] = bonds["city_fips7"].astype(int)
bonds = bonds[bonds["panel_year"].notna() & bonds["panel_year"].between(2013, 2025)]
bonds["panel_year"] = bonds["panel_year"].astype(int)
print(f"Bonds in 578-city panel (valid year): {len(bonds)}")

# ---------------------------------------------------------------------------
# Normalise categorical values
# ---------------------------------------------------------------------------
def clean_value(v):
    """Strip whitespace, collapse dash variants to '--'."""
    if pd.isna(v):
        return None
    s = str(v).strip()
    if s in ("", "---"):
        return "--"
    return s


def col_suffix(v):
    """Turn a value into a column-suffix-safe form (spaces -> underscores)."""
    return v.replace(" ", "_")


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

for f in CATEGORICAL_FIELDS:
    bonds[f] = bonds[f].apply(clean_value)

# ---------------------------------------------------------------------------
# Build skeleton (578 cities x 13 years)
# ---------------------------------------------------------------------------
skeleton = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={
        "fips7": "FIPS", "geo_name": "City", "city_name": "City_Name", "state_abb": "State"
    })
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
print(f"Skeleton: {len(skeleton)} rows")

# ---------------------------------------------------------------------------
# Top-level totals
# ---------------------------------------------------------------------------
totals = (
    bonds.groupby(["city_fips7", "panel_year"])
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
# Pivots: for each categorical field, for each distinct value
# ---------------------------------------------------------------------------
def build_pivot(df, field, key_cols):
    tmp = df[df[field].notna()].copy()
    if len(tmp) == 0:
        return pd.DataFrame(columns=key_cols)

    amt = (
        tmp.groupby(key_cols + [field])["Amt Issued"]
        .sum()
        .unstack(field, fill_value=0)
    )
    amt.columns = [f"Amt_{field}__{col_suffix(v)}" for v in amt.columns]

    cnt = (
        tmp.groupby(key_cols + [field])["CUSIP"]
        .count()
        .unstack(field, fill_value=0)
    )
    cnt.columns = [f"Count_{field}__{col_suffix(v)}" for v in cnt.columns]

    return amt.join(cnt).reset_index()


bonds_keyed = bonds.drop(columns=["Year"]).rename(
    columns={"city_fips7": "FIPS", "panel_year": "Year"}
)

for field in CATEGORICAL_FIELDS:
    pivot = build_pivot(bonds_keyed, field, ["FIPS", "Year"])
    if len(pivot) > 0:
        panel = panel.merge(pivot, on=["FIPS", "Year"], how="left")

# Fill pivoted numeric NaNs with 0
pivot_cols = [c for c in panel.columns if c.startswith("Amt_") or c.startswith("Count_")]
panel[pivot_cols] = panel[pivot_cols].fillna(0)

# ---------------------------------------------------------------------------
# Add Issued_* binary flags for every Count_* column
# ---------------------------------------------------------------------------
for count_col in [c for c in panel.columns if c.startswith("Count_")]:
    field_value = count_col[len("Count_"):]
    panel[f"Issued_{field_value}"] = (panel[count_col] > 0).astype(int)

# ---------------------------------------------------------------------------
# Verify FIPS + city + state combo
# ---------------------------------------------------------------------------
assert panel.groupby(["FIPS", "Year"]).size().max() == 1, "Duplicate (FIPS, Year)"
assert panel[["FIPS", "City", "State"]].drop_duplicates().shape[0] == 578, "Not 578 unique cities"

# Column order: id cols, top-level, then grouped per field
id_cols = ["FIPS", "City", "City_Name", "State", "Year"]
top_cols = ["Green_Bond_Issued", "City_Green_Amt_Issued", "City_Green_Issuance_Count"]

grouped = []
for field in CATEGORICAL_FIELDS:
    # For each field, collect Issued_ / Amt_ / Count_ columns sorted by value
    issued = sorted([c for c in panel.columns if c.startswith(f"Issued_{field}__")])
    amt = sorted([c for c in panel.columns if c.startswith(f"Amt_{field}__")])
    count = sorted([c for c in panel.columns if c.startswith(f"Count_{field}__")])
    # Interleave so Issued, Amt, Count per value stay together
    vals = sorted({c.split("__", 1)[1] for c in issued + amt + count})
    for v in vals:
        for prefix in ("Issued_", "Amt_", "Count_"):
            col = f"{prefix}{field}__{v}"
            if col in panel.columns:
                grouped.append(col)

# Any leftover columns
other = [c for c in panel.columns if c not in id_cols + top_cols + grouped]
panel = panel[id_cols + top_cols + grouped + other]
panel = panel.sort_values(["State", "City", "Year"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
panel.to_csv(OUT / "outcome_city_year_panel.csv", index=False)
panel.to_excel(OUT / "outcome_city_year_panel.xlsx", index=False)

print(f"\nPanel shape: {panel.shape}")
print(f"Cities with at least one green bond ever: {panel.groupby('FIPS')['Green_Bond_Issued'].max().sum()}")
print(f"City-year cells with green bond: {panel['Green_Bond_Issued'].sum()}")
print(f"Total columns: {len(panel.columns)}")
print(f"  Id + top-level: {len(id_cols + top_cols)}")
print(f"  Issued_/Amt_/Count_ pivots: {len(grouped)}")
print(f"Written: {OUT / 'outcome_city_year_panel.xlsx'}")
