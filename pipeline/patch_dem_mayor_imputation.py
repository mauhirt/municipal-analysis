"""
Dem_Mayor three-tier imputation patch.

Applies the imputation directly to the existing panel.pkl, preserving all
other columns. Safe to re-run (idempotent — checks if already imputed).

Three tiers:
1. Fill from mayor_party where mayor_pid was missing (data engineering gap).
2. Within-city forward/back fill (covers single-year gaps like 2025).
3. Constituency proxy (pres_dem_share > 0.5) for nonpartisan rotating-mayor
   cities where mayor-level partisan data is unavailable.

Adds Dem_Mayor_imputed indicator (0 = original, 1/2/3 = tier).
"""

from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
PANEL_PATH = ROOT / 'processed' / 'panel' / 'panel.pkl'

df = pd.read_pickle(PANEL_PATH)
print(f"Panel shape: {df.shape}")

if 'Dem_Mayor_imputed' in df.columns and df['Dem_Mayor_imputed'].max() > 0:
    print("Imputation already applied. Nothing to do.")
else:
    n_before = df['Dem_Mayor'].notna().sum()
    df['Dem_Mayor_imputed'] = 0

    # Tier 1: mayor_party fallback
    if 'mayor_party' in df.columns:
        t1_d = df['Dem_Mayor'].isna() & (df['mayor_party'] == 'D')
        t1_r = df['Dem_Mayor'].isna() & (df['mayor_party'] == 'R')
        df.loc[t1_d, 'Dem_Mayor'] = 1.0
        df.loc[t1_r, 'Dem_Mayor'] = 0.0
        df.loc[t1_d | t1_r, 'Dem_Mayor_imputed'] = 1
        print(f"Tier 1 (mayor_party fallback): {int((t1_d|t1_r).sum())} obs "
              f"({int(t1_d.sum())} D, {int(t1_r.sum())} R)")

    # Tier 2: within-city ffill/bfill
    t2_mask = df['Dem_Mayor'].isna()
    df['Dem_Mayor'] = df.groupby('fips7')['Dem_Mayor'].transform(
        lambda x: x.ffill().bfill())
    t2_filled = t2_mask & df['Dem_Mayor'].notna()
    df.loc[t2_filled, 'Dem_Mayor_imputed'] = 2
    print(f"Tier 2 (within-city ffill/bfill): {int(t2_filled.sum())} obs")

    # Tier 3: constituency proxy for nonpartisan cities
    t3_mask = df['Dem_Mayor'].isna()
    if 'pres_dem_two_party_share_lag2' in df.columns:
        df.loc[t3_mask, 'Dem_Mayor'] = (
            df.loc[t3_mask, 'pres_dem_two_party_share_lag2'] > 0.5
        ).astype(float)
        df.loc[t3_mask & df['Dem_Mayor'].notna(), 'Dem_Mayor_imputed'] = 3
        print(f"Tier 3 (constituency proxy): {int(t3_mask.sum())} obs")

    n_after = df['Dem_Mayor'].notna().sum()
    print(f"Total: {n_before} → {n_after} (+{n_after - n_before} recovered)")

    df.to_pickle(PANEL_PATH)
    print(f"Wrote: {PANEL_PATH}")

# Verify
print(f"\nFinal: Dem_Mayor missing = {df['Dem_Mayor'].isna().sum()}")
print(f"Imputation tier distribution:")
print(df['Dem_Mayor_imputed'].value_counts().sort_index().to_string())
