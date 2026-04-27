"""
Panel patch: two fixes for the main specification.

1. Build effluent_muni_asinh_lag2 from raw EPA data (2000-2026) so lag2
   has pre-panel coverage (2011 values feed 2013 lag2). Replaces the
   broken in-panel lag that was missing 2013-2014.

2. Backfill fn_esg_has_muni_bond_law_post_lag1 for 2013 with 0.
   No anti-ESG muni bond law existed before 2021; the 2013 NaN is
   definitionally 0.

Combined effect: N recovers from 6,825 (2014-2025) to ~7,401 (2013-2025).
"""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
PANEL_PATH = ROOT / 'processed' / 'panel' / 'panel.pkl'

df = pd.read_pickle(PANEL_PATH)
print(f"Panel: {df.shape}")

# ── Fix 1: Build effluent_muni_asinh_lag2 from raw EPA ──
epa_path = ROOT / 'raw' / 'epa' / 'city_year_epa_enforcement_expanded_20260407_125920.csv'
epa = pd.read_csv(epa_path)
epa = epa.rename(columns={'FIPS': 'fips7', 'YEAR': 'year'})

eff = epa[['fips7', 'year', 'npdes_effluent_violations_count_muni']].copy()
eff = eff.sort_values(['fips7', 'year'])
eff['effluent_muni_lag2'] = eff.groupby('fips7')['npdes_effluent_violations_count_muni'].shift(2)
eff['effluent_muni_asinh_lag2'] = np.arcsinh(eff['effluent_muni_lag2'])

# Drop old versions if present
for col in ['effluent_muni_lag2', 'effluent_muni_asinh_lag2',
            'npdes_effluent_asinh_muni_lag2', 'npdes_effluent_violations_muni_lag2']:
    if col in df.columns:
        df = df.drop(columns=[col])

df = df.merge(
    eff[['fips7', 'year', 'effluent_muni_lag2', 'effluent_muni_asinh_lag2']],
    on=['fips7', 'year'], how='left'
)

n_2013 = df.loc[df['year'] == 2013, 'effluent_muni_asinh_lag2'].notna().sum()
print(f"Fix 1: effluent_muni_asinh_lag2 at 2013: {n_2013}/{(df['year']==2013).sum()}")

# ── Fix 2: Backfill fn_esg 2013 ──
mask = (df['year'] == 2013) & df['fn_esg_has_muni_bond_law_post_lag1'].isna()
n_fill = mask.sum()
df.loc[mask, 'fn_esg_has_muni_bond_law_post_lag1'] = 0
print(f"Fix 2: filled {n_fill} NaN fn_esg_has_muni_bond_law_post_lag1 in 2013 with 0")

# ── Verify ──
PRIMARY_NEW = [
    'Dem_Mayor', 'effluent_muni_asinh_lag2',
    'pres_dem_two_party_share_lag2', 'asinh_state_all_green_cum_amt_lag1',
    'reserve_ratio_lag2', 'debt_service_burden_lag2',
    'fn_esg_has_muni_bond_law_post_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2', 'unemployment_city_lag2',
]
cols = ['fips7', 'state_id', 'year', 'Y_self_green'] + PRIMARY_NEW
d = df[[c for c in cols if c in df.columns]].dropna()
print(f"\nNew sample: N={len(d)}, cities={d['fips7'].nunique()}")
print(f"Year range: {d['year'].min()} – {d['year'].max()}")
print(d.groupby('year').size().to_string())

df.to_pickle(PANEL_PATH)
print(f"\nPanel saved: {PANEL_PATH}")
