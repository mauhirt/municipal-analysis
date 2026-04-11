"""
Build city-year Building Codes + BPS + Benchmarking controls panel from
raw/energy_policy/New Building Codes/ master files.

Inputs:
  raw/energy_policy/New Building Codes/master_state_year_panel_2010_2025.csv
  raw/energy_policy/New Building Codes/master_city_year_panel_2010_2025.csv
  raw/crosswalk/Crosswalk.csv

Output:
  processed/building_codes_city_year_panel.csv (7,514 rows x ~30 cols)

Merge logic:
  1. Start with the 578-city x 13-year skeleton (keyed FIPS x Year).
  2. Left-merge the state-year master on (state_abb, year) to attach state-
     level IECC vintage, state-level BPS rollup, and state-level counts of
     city-level BPS/benchmarking adoption.
  3. Left-merge the city-year master on (city_name_normalized, state, year)
     to attach city-level BPS and benchmarking for the 32 of 39 city-type
     jurisdictions that match the 578-city panel.
  4. Fill NaN for non-BPS / non-benchmarking cities (binary flags -> 0; year
     and penalty numbers kept as NaN).

Variable namespace (to avoid clashes with existing climate v2 columns):
  - State IECC stringency: bcode_iecc_* (from state_year master)
  - State BPS rollup: bcode_state_bps_*
  - City BPS: bcode_bps_*
  - City benchmarking: bcode_benchmark_*
  - Derived: bcode_any_policy_active, bcode_any_policy_effective
"""

import pandas as pd
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "energy_policy" / "New Building Codes"
OUT = ROOT / "processed"
CROSSWALK = ROOT / "raw" / "crosswalk" / "Crosswalk.csv"

YEARS = list(range(2013, 2026))  # Align with main panel window


def norm_name(s: str) -> str:
    """Normalize city names for cross-source matching."""
    s = str(s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("saint ", "st. ")
    return s


# ---------------------------------------------------------------------------
# 1. Load master panels and crosswalk
# ---------------------------------------------------------------------------
state_master = pd.read_csv(SRC / "master_state_year_panel_2010_2025.csv")
city_master = pd.read_csv(SRC / "master_city_year_panel_2010_2025.csv")
crosswalk = pd.read_csv(CROSSWALK)

print(f"state_master: {state_master.shape}")
print(f"city_master:  {city_master.shape}")
print(f"crosswalk:    {len(crosswalk)} cities")

# ---------------------------------------------------------------------------
# 2. Build 578 x 13 skeleton
# ---------------------------------------------------------------------------
skel = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
skel["FIPS"] = skel["FIPS"].astype(int)
print(f"Skeleton: {skel.shape}")

# ---------------------------------------------------------------------------
# 3. Prepare state-year master for merge
# ---------------------------------------------------------------------------
state_keep = [
    "state_abbr", "year",
    # State IECC
    "iecc_comm_vintage", "lag_model_code_yrs",
    "no_statewide_code", "home_rule", "preemption_of_stricter_local",
    "stretch_code_available", "weakening_amendments",
    # State BPS rollup
    "state_bps_adopted", "state_bps_effective",
    "state_bps_year_enacted", "state_bps_first_compliance_year",
    "state_bps_penalty_per_sqft", "state_bps_penalty_per_tco2e",
    # State counts of city-level policy in that state
    "state_n_city_bps_adopted", "state_n_city_benchmarking_adopted",
    "state_any_city_has_bps", "state_any_city_has_benchmarking",
]
state_slim = state_master[state_keep].rename(
    columns={
        "state_abbr": "State",
        "year": "Year",
        "iecc_comm_vintage": "bcode_iecc_vintage",
        "lag_model_code_yrs": "bcode_iecc_lag_yrs",
        "no_statewide_code": "bcode_no_statewide_code",
        "home_rule": "bcode_home_rule",
        "preemption_of_stricter_local": "bcode_state_preemption",
        "stretch_code_available": "bcode_state_stretch_code",
        "weakening_amendments": "bcode_state_weakening_amendments",
        "state_bps_adopted": "bcode_state_bps_adopted",
        "state_bps_effective": "bcode_state_bps_effective",
        "state_bps_year_enacted": "bcode_state_bps_year_enacted",
        "state_bps_first_compliance_year": "bcode_state_bps_compliance_year",
        "state_bps_penalty_per_sqft": "bcode_state_bps_pen_sqft",
        "state_bps_penalty_per_tco2e": "bcode_state_bps_pen_tco2e",
        "state_n_city_bps_adopted": "bcode_state_n_city_bps",
        "state_n_city_benchmarking_adopted": "bcode_state_n_city_bench",
        "state_any_city_has_bps": "bcode_state_any_city_bps",
        "state_any_city_has_benchmarking": "bcode_state_any_city_bench",
    }
)
print(f"state_slim: {state_slim.shape}")

# ---------------------------------------------------------------------------
# 4. Prepare city-year master for merge
# ---------------------------------------------------------------------------
# Filter to city-level rows: "city" + "district" (DC is coded as district
# but is in the 578-city panel and has a real city-level BPS from 2018).
# State and county rows are excluded here - those are captured via the
# state_slim merge above.
city_type = city_master[
    city_master["jurisdiction_type"].isin(["city", "district"])
].copy()

# Remap NYC jurisdiction name to match panel's "new york"
city_type.loc[city_type["jurisdiction"] == "New York City", "jurisdiction"] = "New York"
city_type["_key"] = city_type["jurisdiction"].apply(norm_name)

city_keep = [
    "_key", "state_abbr", "year",
    # City BPS
    "bps_adopted", "bps_effective",
    "bps_year_enacted", "bps_first_compliance_year",
    "years_since_bps",
    "bps_penalty_per_sqft", "bps_penalty_per_tco2e",
    "bps_covers_municipal", "bps_ratchet",
    "bps_coalition_member", "bps_coalition_launch_day", "bps_coalition_joined_year",
    # City benchmarking
    "benchmarking_adopted", "benchmarking_effective",
    "benchmarking_year_enacted", "benchmarking_first_reporting_year",
    "years_since_benchmarking", "benchmarking_threshold_sqft", "audit_tuneup_req",
    # Derived
    "any_policy_active", "any_policy_effective",
]
city_slim = city_type[city_keep].rename(
    columns={
        "state_abbr": "State",
        "year": "Year",
        "bps_adopted": "bcode_bps_adopted",
        "bps_effective": "bcode_bps_effective",
        "bps_year_enacted": "bcode_bps_year_enacted",
        "bps_first_compliance_year": "bcode_bps_compliance_year",
        "years_since_bps": "bcode_bps_years_since",
        "bps_penalty_per_sqft": "bcode_bps_pen_sqft",
        "bps_penalty_per_tco2e": "bcode_bps_pen_tco2e",
        "bps_covers_municipal": "bcode_bps_covers_municipal",
        "bps_ratchet": "bcode_bps_ratchet",
        "bps_coalition_member": "bcode_bps_coalition_member",
        "bps_coalition_launch_day": "bcode_bps_coalition_launch_day",
        "bps_coalition_joined_year": "bcode_bps_coalition_joined_year",
        "benchmarking_adopted": "bcode_benchmark_adopted",
        "benchmarking_effective": "bcode_benchmark_effective",
        "benchmarking_year_enacted": "bcode_benchmark_year_enacted",
        "benchmarking_first_reporting_year": "bcode_benchmark_first_reporting_year",
        "years_since_benchmarking": "bcode_benchmark_years_since",
        "benchmarking_threshold_sqft": "bcode_benchmark_threshold_sqft",
        "audit_tuneup_req": "bcode_benchmark_audit_req",
        "any_policy_active": "bcode_any_policy_active",
        "any_policy_effective": "bcode_any_policy_effective",
    }
)
print(f"city_slim: {city_slim.shape}  (city-type rows only)")

# ---------------------------------------------------------------------------
# 5. Merge state-level context onto skeleton
# ---------------------------------------------------------------------------
panel = skel.merge(state_slim, on=["State", "Year"], how="left")
print(f"After state merge: {panel.shape}")

# ---------------------------------------------------------------------------
# 6. Merge city-level BPS/benchmarking using normalized city name
# ---------------------------------------------------------------------------
panel["_key"] = panel["City"].apply(norm_name)
panel = panel.merge(city_slim, on=["_key", "State", "Year"], how="left")
panel = panel.drop(columns=["_key"])
print(f"After city merge: {panel.shape}")

# ---------------------------------------------------------------------------
# 7. Fill NaN for non-treated cities
# ---------------------------------------------------------------------------
# Binary flags: fill with 0 (city does not have a BPS / benchmarking)
binary_cols = [
    "bcode_bps_adopted", "bcode_bps_effective",
    "bcode_bps_covers_municipal", "bcode_bps_ratchet",
    "bcode_bps_coalition_member", "bcode_bps_coalition_launch_day",
    "bcode_benchmark_adopted", "bcode_benchmark_effective",
    "bcode_benchmark_audit_req",
    "bcode_any_policy_active", "bcode_any_policy_effective",
    "bcode_state_bps_adopted", "bcode_state_bps_effective",
    "bcode_state_any_city_bps", "bcode_state_any_city_bench",
    "bcode_no_statewide_code", "bcode_home_rule",
    "bcode_state_preemption", "bcode_state_stretch_code",
    "bcode_state_weakening_amendments",
]
for c in binary_cols:
    if c in panel.columns:
        panel[c] = panel[c].fillna(0).astype(int)

# Count columns: fill with 0 (no cities in that state have adopted)
count_cols = [
    "bcode_state_n_city_bps", "bcode_state_n_city_bench",
]
for c in count_cols:
    if c in panel.columns:
        panel[c] = panel[c].fillna(0).astype(int)

# years_since: fill with NaN (city never adopted - no meaningful duration)
# year_enacted, first_compliance_year: keep NaN (city never adopted)
# penalty amounts: keep NaN (no penalty applicable)

# ---------------------------------------------------------------------------
# 8. Sanity checks
# ---------------------------------------------------------------------------
assert panel.shape[0] == 578 * 13, f"Expected 7514 rows, got {panel.shape[0]}"
assert panel.groupby(["FIPS", "Year"]).size().max() == 1

# How many cities end up with city-level BPS adoption by 2025?
city_bps_2025 = panel[(panel.Year == 2025) & (panel.bcode_bps_adopted == 1)]
print(f"\nCities with city-level BPS adopted by 2025: {len(city_bps_2025)}")
if len(city_bps_2025):
    print(city_bps_2025[["City", "State", "bcode_bps_year_enacted",
                         "bcode_bps_compliance_year"]].to_string(index=False))

# State-level BPS by year
print(f"\nState-level BPS adoption cities (via state rollup) by year:")
print(panel.groupby("Year")["bcode_state_bps_adopted"].sum().to_string())

# Benchmarking adopters by year
print(f"\nCity-level benchmarking adopters by year:")
print(panel.groupby("Year")["bcode_benchmark_adopted"].sum().to_string())

# Any policy active
print(f"\nAny BPS/benchmarking policy active by year:")
print(panel.groupby("Year")["bcode_any_policy_active"].sum().to_string())

# ---------------------------------------------------------------------------
# 9. Write
# ---------------------------------------------------------------------------
# Put identifiers first
id_cols = ["FIPS", "City", "city_name", "State", "Year"]
other_cols = [c for c in panel.columns if c not in id_cols]
panel = panel[id_cols + other_cols].sort_values(["State", "City", "Year"]).reset_index(drop=True)

OUT.mkdir(parents=True, exist_ok=True)
panel.to_csv(OUT / "building_codes_city_year_panel.csv", index=False)
print(f"\nWritten: {OUT / 'building_codes_city_year_panel.csv'}")
print(f"Shape: {panel.shape}")
