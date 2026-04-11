"""
Merge the energy policy raw files into a city-year controls panel.

Inputs:
  raw/energy_policy/state_building_codes.csv        (50 x 12, 2025 snapshot)
  raw/energy_policy/state_net_metering.csv          (800 x 6, 2010-2025)
  raw/energy_policy/state_clean_energy_funds.csv    (50 x 12, 2025 snapshot)
  raw/energy_policy/municipal_electric_utilities.csv (578 x 8, city cross-section)
  raw/crosswalk/Crosswalk.csv

Output:
  processed/energy_policy_city_year_panel.csv (7,514 rows)

Namespace:
  ep_*   for all new energy-policy controls to avoid collisions

Merge logic:
  1. Skeleton: 578 cities x 13 years (2013-2025).
  2. state_building_codes.csv - only bring in ACEEE rank and disclosure flag
     (IECC vintage is superseded by pipeline/18 bcode_iecc_*).
  3. state_net_metering.csv - merge directly on (State, Year). Time-varying.
  4. state_clean_energy_funds.csv - construct ep_state_has_green_bank_active
     from state_green_bank_year (year-varying); keep other flags as static.
     DROP state_has_rps because it conflicts with climate v2 state_rps_active.
  5. municipal_electric_utilities.csv - time-invariant city characteristic.
     Merge on lowercase City + State.
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "energy_policy"
OUT = ROOT / "processed"
CROSSWALK = ROOT / "raw" / "crosswalk" / "Crosswalk.csv"

YEARS = list(range(2013, 2026))

# ---------------------------------------------------------------------------
# 1. Load all sources
# ---------------------------------------------------------------------------
bcode = pd.read_csv(RAW / "state_building_codes.csv")
nem = pd.read_csv(RAW / "state_net_metering.csv")
cef = pd.read_csv(RAW / "state_clean_energy_funds.csv")
mu = pd.read_csv(RAW / "municipal_electric_utilities.csv")
crosswalk = pd.read_csv(CROSSWALK)

print(f"state_building_codes:         {bcode.shape}")
print(f"state_net_metering:           {nem.shape}")
print(f"state_clean_energy_funds:     {cef.shape}")
print(f"municipal_electric_utilities: {mu.shape}")

# ---------------------------------------------------------------------------
# 2. 578 x 13 skeleton
# ---------------------------------------------------------------------------
skel = (
    crosswalk[["fips7", "geo_name", "city_name", "state_abb"]]
    .rename(columns={"fips7": "FIPS", "geo_name": "City", "state_abb": "State"})
    .merge(pd.DataFrame({"Year": YEARS}), how="cross")
)
skel["FIPS"] = skel["FIPS"].astype(int)
print(f"Skeleton: {skel.shape}")

# ---------------------------------------------------------------------------
# 3. state_building_codes: keep only ACEEE rank + non-overlapping flags
# ---------------------------------------------------------------------------
bcode_slim = bcode[[
    "state_abbr",
    "state_building_code_stringency_aceee_rank",
    "state_has_commercial_benchmarking",
    "state_has_residential_disclosure",
]].rename(columns={
    "state_abbr": "State",
    "state_building_code_stringency_aceee_rank": "ep_state_aceee_code_rank",
    "state_has_commercial_benchmarking": "ep_state_has_comm_benchmark_law",
    "state_has_residential_disclosure": "ep_state_has_resid_disclosure",
})
print(f"bcode_slim (static state): {bcode_slim.shape}")

# ---------------------------------------------------------------------------
# 4. state_net_metering: time-varying state-year
# ---------------------------------------------------------------------------
nem_slim = nem.rename(columns={
    "state_abb": "State",
    "year": "Year",
    "state_has_net_metering": "ep_state_net_metering",
    "state_net_metering_cap_kw": "ep_state_net_metering_cap_kw",
    "state_has_community_solar": "ep_state_community_solar",
    "state_has_municipal_utility_exemption": "ep_state_muni_util_exemption",
})
print(f"nem_slim: {nem_slim.shape}")

# ---------------------------------------------------------------------------
# 5. state_clean_energy_funds: mix of static + year-varying (green bank)
# ---------------------------------------------------------------------------
# Build year-varying green bank active flag from green_bank_year
cef_bank = cef[["state_abb", "state_green_bank_year"]].copy()
cef_bank["state_abb"] = cef_bank["state_abb"]
# Expand to state x year
state_year_grid = pd.MultiIndex.from_product(
    [cef_bank["state_abb"].unique(), YEARS],
    names=["State", "Year"],
).to_frame(index=False)
state_year_grid = state_year_grid.merge(
    cef_bank.rename(columns={"state_abb": "State"}), on="State", how="left"
)
state_year_grid["ep_state_green_bank_active"] = (
    (state_year_grid["Year"] >= state_year_grid["state_green_bank_year"])
    .fillna(False)
    .astype(int)
)
state_year_grid = state_year_grid[["State", "Year", "ep_state_green_bank_active"]]
print(f"state_year_grid (green bank active): {state_year_grid.shape}")

# Static state-level flags
cef_static = cef[[
    "state_abb",
    "state_has_green_bank",
    "state_has_resilience_fund",
    "state_has_energy_efficiency_program",
    "state_has_clean_energy_standard",
    "state_eers_target",
    "state_eers_has",
]].rename(columns={
    "state_abb": "State",
    "state_has_green_bank": "ep_state_has_green_bank_ever",
    "state_has_resilience_fund": "ep_state_has_resilience_fund",
    "state_has_energy_efficiency_program": "ep_state_has_ee_program",
    "state_has_clean_energy_standard": "ep_state_has_ces",
    "state_eers_target": "ep_state_eers_target",
    "state_eers_has": "ep_state_has_eers",
})

# Drop state_has_rps - it conflicts with climate v2's state_rps_active

# ---------------------------------------------------------------------------
# 6. municipal_electric_utilities: city cross-section
# ---------------------------------------------------------------------------
mu_slim = mu.rename(columns={
    "city_name": "_city_lower",
    "state_abb": "State",
    "has_municipal_electric": "ep_has_muni_electric",
    "customers": "ep_muni_electric_customers",
    "revenue_millions": "ep_muni_electric_rev_mil",
    "large_enough_for_bonds": "ep_muni_electric_bond_scale",
})[[
    "_city_lower", "State",
    "ep_has_muni_electric", "ep_muni_electric_customers",
    "ep_muni_electric_rev_mil", "ep_muni_electric_bond_scale",
]]
print(f"mu_slim: {mu_slim.shape}")

# ---------------------------------------------------------------------------
# 7. Assemble: merge everything onto the skeleton
# ---------------------------------------------------------------------------
panel = skel.copy()
panel["_city_lower"] = panel["City"].str.lower()

# Static state (bcode)
panel = panel.merge(bcode_slim, on="State", how="left")

# Time-varying state (net metering)
panel = panel.merge(nem_slim, on=["State", "Year"], how="left")

# Time-varying state (green bank active)
panel = panel.merge(state_year_grid, on=["State", "Year"], how="left")

# Static state (clean energy funds other flags)
panel = panel.merge(cef_static, on="State", how="left")

# Static city (muni electric)
panel = panel.merge(mu_slim, on=["_city_lower", "State"], how="left")
panel = panel.drop(columns=["_city_lower"])

# ---------------------------------------------------------------------------
# 8. Fill NaN for binary flags
# ---------------------------------------------------------------------------
binary_cols = [
    "ep_state_has_comm_benchmark_law", "ep_state_has_resid_disclosure",
    "ep_state_net_metering", "ep_state_community_solar",
    "ep_state_muni_util_exemption",
    "ep_state_green_bank_active",
    "ep_state_has_green_bank_ever", "ep_state_has_resilience_fund",
    "ep_state_has_ee_program", "ep_state_has_ces", "ep_state_has_eers",
    "ep_has_muni_electric", "ep_muni_electric_bond_scale",
]
for c in binary_cols:
    if c in panel.columns:
        panel[c] = panel[c].fillna(0).astype(int)

# ACEEE rank: fill missing with median rank (51 states + DC = 51 ranks) but
# leave NaN so regression users can decide. We'll leave NaN.

# ---------------------------------------------------------------------------
# 9. Sanity checks and summary
# ---------------------------------------------------------------------------
assert panel.shape[0] == 578 * 13
assert panel.groupby(["FIPS", "Year"]).size().max() == 1

print(f"\nPanel shape: {panel.shape}")

print(f"\n--- State Net Metering by year (cities x NM=1) ---")
print(panel.groupby("Year")["ep_state_net_metering"].sum().to_string())

print(f"\n--- State Green Bank Active by year (cities) ---")
print(panel.groupby("Year")["ep_state_green_bank_active"].sum().to_string())

print(f"\n--- Cities with municipal electric ---")
mu_cities = panel[(panel.Year == 2025) & (panel.ep_has_muni_electric == 1)]
print(f"n = {len(mu_cities)}")

# ---------------------------------------------------------------------------
# 10. Write
# ---------------------------------------------------------------------------
id_cols = ["FIPS", "City", "city_name", "State", "Year"]
other_cols = [c for c in panel.columns if c not in id_cols]
panel = panel[id_cols + other_cols].sort_values(["State", "City", "Year"]).reset_index(drop=True)
panel.to_csv(OUT / "energy_policy_city_year_panel.csv", index=False)
print(f"\nWritten: {OUT / 'energy_policy_city_year_panel.csv'}")
