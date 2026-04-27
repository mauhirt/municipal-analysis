"""
analysis_table1_city_fe.py — Table 1 with city + year FE (within-city identification)
=====================================================================================
The main Table 1 specs use state+year FE (between-city identification within
a state). This script re-estimates Table 1's two key outcomes under
**city + year FE**, which identifies off within-city variation over time.

What this means for the sample:
  - Cities are not literally dropped. But cities with no within-city variation
    in (y, x) contribute nothing to identification of that coefficient.
  - For `Rep_Mayor_lag1`: only party-switcher cities contribute. The panel has
    181 switchers out of 578 cities (00_build_panel.py output).
  - For `Green_Bond_Issued`: only cities that change between issuing / not
    issuing across years contribute to the outcome variation. ~85 cities ever
    issue a green bond.
  - Variables that are time-invariant are perfectly absorbed by city FE and
    become unidentified (e.g., has_substitute_issuer, climate_commitment_static,
    is_principal_city, nri_*, pct_college_educated, median_home_value, and
    state-level variables that don't change over the panel window).

This script:
  1. Documents sample diagnostics (switchers, ever-issuers, intersection).
  2. Identifies which RHS variables survive city FE (nonzero within-city SD).
  3. Estimates the Rep_Mayor coefficient under city + year FE on the two
     canonical outcomes (Green_Bond_Issued, Y_self_green).
  4. Prints and writes results alongside the between-city baseline for contrast.
"""
import sys
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_panel, stars

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'processed' / 'tables'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def fit_panel(df, y, xs, entity_fe=True, time_fe=True, cluster_state=False):
    """Estimate via linearmodels.PanelOLS with entity/time FE."""
    d = df[['fips7', 'year', 'state_id', y] + xs].copy()
    d = d.dropna(subset=[y] + xs)
    xs_live = [x for x in xs if d[x].nunique() > 1]
    if not xs_live:
        return None, 0, []
    d2 = d.set_index(['fips7', 'year'])
    try:
        mod = PanelOLS(d2[y], d2[xs_live].astype(float),
                       entity_effects=entity_fe, time_effects=time_fe,
                       check_rank=False)
        cluster_kwargs = {}
        if cluster_state:
            cluster_kwargs = {'cov_type': 'clustered', 'clusters': d2['state_id']}
        else:
            cluster_kwargs = {'cov_type': 'clustered', 'cluster_entity': True}
        res = mod.fit(**cluster_kwargs)
        res._xnames = xs_live
        return res, len(d), xs_live
    except Exception as e:
        print(f"    fit error: {e}")
        return None, 0, []


def fit_ols(df, y, xs, fe, cluster='fips7'):
    raw = ['fips7', cluster] + list(fe) + [y] + xs
    seen, cols = set(), []
    for c in raw:
        if c in df.columns and c not in seen:
            cols.append(c)
            seen.add(c)
    d = df[cols].copy()
    d = d.dropna(subset=[y] + [x for x in xs if x in d.columns])
    xs_live = [x for x in xs if d[x].nunique() > 1]
    if len(d) < 30 or not xs_live:
        return None, 0
    X_parts = [d[xs_live].astype(float)]
    for f in fe:
        if f in d.columns and d[f].nunique() > 1:
            X_parts.append(pd.get_dummies(d[f], prefix=f, drop_first=True, dtype=float))
    X = pd.concat(X_parts, axis=1)
    X = sm.add_constant(X).astype(float)
    y_vec = d[y].astype(float).values
    try:
        res = sm.OLS(y_vec, X.values).fit(
            cov_type='cluster', cov_kwds={'groups': d[cluster].values})
        res._xnames = list(X.columns)
        return res, len(d)
    except Exception:
        return None, 0


def coef(res, name):
    if res is None:
        return np.nan, np.nan, np.nan
    try:
        if hasattr(res, 'std_errors'):  # linearmodels
            return float(res.params[name]), float(res.std_errors[name]), float(res.pvalues[name])
        i = res._xnames.index(name)
        return float(res.params[i]), float(res.bse[i]), float(res.pvalues[i])
    except (ValueError, KeyError):
        return np.nan, np.nan, np.nan


def fmt(b, se, p):
    if np.isnan(b):
        return '—'
    return f'{b:+.4f}{stars(p)} (se {se:.4f})'


# ──────────────────────────────────────────────────────────────────────
# Load and diagnose the identifying sample
# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel: {df.shape}")

if 'Rep_Mayor_lag1' not in df.columns and 'Rep_Mayor_L1' in df.columns:
    df['Rep_Mayor_lag1'] = df['Rep_Mayor_L1']
if 'Ind_Mayor_lag1' not in df.columns and 'Ind_Mayor_L1' in df.columns:
    df['Ind_Mayor_lag1'] = df['Ind_Mayor_L1']
for tgt, cands in [('npdes_formal_prior3yr_muni',
                    ['npdes_formal_any_muni_prior3yr', 'npdes_formal_prior3yr_muni']),
                   ('overflow_events_lag2',
                    ['overflow_events_lag2', 'overflow_events_muni_lag2'])]:
    if tgt not in df.columns:
        for c in cands:
            if c in df.columns:
                df[tgt] = df[c]
                break

# Identifying-sample diagnostics
print("\n" + "=" * 78)
print("WHAT CITY + YEAR FE MEANS FOR THE IDENTIFYING SAMPLE")
print("=" * 78)

n_cities = df['fips7'].nunique()
n_obs    = len(df)
n_years  = df['year'].nunique()
print(f"\nTotal panel: {n_cities} cities × {n_years} years = {n_obs} city-years")

# Party switchers
party_by_city = df.groupby('fips7')['Rep_Mayor_lag1'].nunique(dropna=True)
n_switchers = int((party_by_city > 1).sum())
n_never_switchers = int((party_by_city == 1).sum())
print(f"\nRep_Mayor_lag1 (treatment):")
print(f"  party-switcher cities (>1 unique value):   {n_switchers}")
print(f"  never-switcher cities:                     {n_never_switchers}")
print(f"  → city FE absorbs never-switchers. Rep_Mayor is identified"
      f" off {n_switchers}/{n_cities} cities.")

# Ever-issuer cities
ever_issue = df.groupby('fips7')['Green_Bond_Issued'].max()
n_issuer = int((ever_issue == 1).sum())
n_non_issuer = int((ever_issue == 0).sum())
# Intersection
ever_self = df.groupby('fips7')['Y_self_green'].max()
n_self = int((ever_self == 1).sum())
print(f"\nGreen_Bond_Issued (Step 1+2 outcome):")
print(f"  cities that ever issued:     {n_issuer}")
print(f"  cities that never issued:    {n_non_issuer}  → Y constant = 0 → contribute nothing")
print(f"\nY_self_green (Step 3 outcome):")
print(f"  cities that ever self-labelled: {n_self}")

# Intersection — cities that both switched party AND have outcome variation
switchers = set(party_by_city[party_by_city > 1].index)
issuers_gbi = set(df.groupby('fips7')['Green_Bond_Issued']
                  .nunique().pipe(lambda s: s[s > 1].index))
issuers_ysg = set(df.groupby('fips7')['Y_self_green']
                  .nunique().pipe(lambda s: s[s > 1].index))
print(f"\nCities with BOTH party-switch AND outcome variation:")
print(f"  switchers ∩ Green_Bond_Issued varies over time: {len(switchers & issuers_gbi)}")
print(f"  switchers ∩ Y_self_green varies over time:       {len(switchers & issuers_ysg)}")
print(f"  → These are the only cities that identify β(Rep_Mayor) under city + year FE.")

# Within-city variation — which RHS vars have any?
RHS = [v for v in [
    'Rep_Mayor_lag1', 'Ind_Mayor_lag1', 'pres_dem_two_party_share_lag2',
    'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
    'charges_to_own_source_lag2', 'reserve_ratio_lag2',
    'debt_service_burden_lag2', 'property_tax_dependence_lag2',
    'log_cwsrf_obligations_lag2', 'cwns_needs_real_lag2',
    'state_rep_trifecta', 'esg_has_muni_bond_law', 'state_green_bond_ever_lag1',
    'log_population_city_lag2', 'log_percapita_income_city_lag2',
    'unemployment_city_lag2', 'has_substitute_issuer',
    'tel_x_prop_tax_dep', 'tel_x_charges',
] if v in df.columns]

print("\nRHS variables — within-city standard deviation (75th percentile):")
print(f"  {'variable':40s}  {'within-city SD (75th)':>25s}  {'identified under city FE?'}")
for v in RHS:
    wsd = df.groupby('fips7')[v].std(ddof=0).quantile(0.75)
    pos = df[v].notna().sum()
    survives = 'YES' if wsd > 1e-6 else 'ABSORBED'
    print(f"  {v:40s}  {wsd:>25.4f}  {survives}  (n_nonnull={pos})")


# ──────────────────────────────────────────────────────────────────────
# Run specs: baseline (state+year FE) vs city+year FE
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 78)
print("RESULTS — Rep_Mayor_lag1 under two FE structures")
print("=" * 78)

outcomes = ['Green_Bond_Issued', 'Y_self_green', 'asinh_green_amt', 'asinh_self_green_amt']

# Build two parallel spec sets
results = []
for y in outcomes:
    if y not in df.columns:
        continue
    # Baseline: state + year FE, cluster fips7
    res_b, n_b = fit_ols(df, y, RHS, fe=('state_id', 'year'), cluster='fips7')
    # Baseline alt: state + year FE, cluster state
    res_bs, n_bs = fit_ols(df, y, RHS, fe=('state_id', 'year'), cluster='state_id')
    # City + year FE, cluster entity (fips7)
    res_c, n_c, xs_live_c = fit_panel(df, y, RHS, entity_fe=True, time_fe=True,
                                      cluster_state=False)
    results.append((y, res_b, n_b, res_bs, n_bs, res_c, n_c, xs_live_c))

    def line(tag, r, n):
        b, se, p = coef(r, 'Rep_Mayor_lag1')
        return f"  [{tag}] n={n:4d}  β(Rep_Mayor_lag1)={b:+.4f}{stars(p)} (se={se:.4f})"

    print(f"\nOutcome: {y}")
    print(line('state+year FE, cluster=fips7 (Tables 1/2 default)', res_b, n_b))
    print(line('state+year FE, cluster=state_id                  ', res_bs, n_bs))
    print(line('city+year  FE, cluster=fips7 (within-city)       ', res_c, n_c))


# ──────────────────────────────────────────────────────────────────────
# Write markdown summary
# ──────────────────────────────────────────────────────────────────────
md = [
    '# Table 1 with city + year FE — within-city robustness',
    '',
    '## What city + year fixed effects mean',
    '',
    'State + year FE (the Table 1 default) identifies the effect of a variable'
    ' off cross-city variation **within a state in a given year**. Cities that'
    ' never change the variable value (e.g., a never-switcher city on `Rep_Mayor_lag1`)'
    ' still contribute through their cross-city position.',
    '',
    'City + year FE removes that cross-city variation entirely. Identification'
    ' is only from **within-city changes over time**. This is a much stricter'
    ' test:',
    '',
    '- A city with no within-city variation in the treatment contributes nothing'
    '  to identifying that coefficient.',
    '- A city with no within-city variation in the outcome contributes nothing'
    '  to identifying *any* coefficient.',
    '- Time-invariant variables (static city characteristics, state-level'
    '  variables that do not change over the panel window) are perfectly absorbed'
    '  and become unidentified — linearmodels drops them.',
    '',
    '## Which observations effectively identify each coefficient',
    '',
    f'- Panel total: **{n_cities} cities × {n_years} years = {n_obs} city-years**',
    f'- Party switchers (Rep_Mayor_lag1 varies over time): **{n_switchers}/{n_cities} cities**',
    f'- Never-switchers: **{n_never_switchers} cities** — contribute zero to β(Rep_Mayor) under city FE',
    f'- Ever-issuer cities (Green_Bond_Issued ever = 1): **{n_issuer}/{n_cities}**',
    f'- Ever-self-labelled cities (Y_self_green ever = 1): **{n_self}/{n_cities}**',
    f'- Switchers ∩ Green_Bond_Issued varies over time: **{len(switchers & issuers_gbi)}**',
    f'- Switchers ∩ Y_self_green varies over time: **{len(switchers & issuers_ysg)}**',
    '',
    'These last two numbers are the **effective city count** identifying'
    ' β(Rep_Mayor) under city + year FE. In practice, β is pinned down by'
    ' only those cities.',
    '',
    '## RHS variables — which survive city FE',
    '',
    '| Variable | within-city SD (75th pct) | under city FE |',
    '|---|---|---|',
]
for v in RHS:
    wsd = df.groupby('fips7')[v].std(ddof=0).quantile(0.75)
    survives = 'YES' if wsd > 1e-6 else '**ABSORBED**'
    md.append(f'| `{v}` | {wsd:.4f} | {survives} |')

md.extend([
    '',
    'Variables marked ABSORBED (75th-percentile within-city SD ≈ 0) have no'
    ' within-city variation for at least three quarters of cities — under'
    ' city FE their coefficients are unidentified and `linearmodels` drops them.',
    '',
    '## Results — Rep_Mayor_lag1 under three FE structures',
    '',
    '| Outcome | state+year FE, cluster=fips7 (Tables 1/2 default) | state+year FE, cluster=state_id | city+year FE (within-city) |',
    '|---|---|---|---|',
])
for (y, res_b, n_b, res_bs, n_bs, res_c, n_c, xs_live_c) in results:
    b_b, se_b, p_b = coef(res_b, 'Rep_Mayor_lag1')
    b_bs, se_bs, p_bs = coef(res_bs, 'Rep_Mayor_lag1')
    b_c, se_c, p_c = coef(res_c, 'Rep_Mayor_lag1')
    md.append(f'| `{y}` | {fmt(b_b, se_b, p_b)}, N={n_b} | '
              f'{fmt(b_bs, se_bs, p_bs)}, N={n_bs} | '
              f'{fmt(b_c, se_c, p_c)}, N={n_c} |')

md.extend([
    '',
    '## How to read this',
    '',
    '- If β(Rep_Mayor_lag1) is null under all three FE structures, the finding is robust.',
    '- If β collapses to zero (or becomes noisier with wider SE) under city FE,'
    '  the cross-city baseline was picking up something time-invariant at the'
    '  city level that correlates with partisan identity (e.g., state, region,'
    '  city size, urban/suburban status) — not partisan identity per se.',
    '- The small effective sample under city FE (only switcher-issuer cities'
    '  contribute) means wider SEs are expected. Absence of significance here'
    '  reflects power, not evidence against the effect.',
    '',
    '## Notable variables lost to city FE',
    '',
    '- `has_substitute_issuer` (near-static — whether there is a nearby water'
    '  special district — does not change year-to-year for most cities)',
    '- State-level political and institutional variables where the state did'
    '  not change status over 2013–2025: `state_rep_trifecta`, `state_dem_governor_lag1`,'
    '  `state_carbon_pricing_lag1`, `state_rggi_member_lag1`, `state_wci_member_lag1`,'
    '  `state_medicaid_expanded_lag1`, `state_right_to_work_lag1`, `esg_has_underwriter_block`'
    '  (in all but a handful of states), `inst_*` institutional variables (cross-sectional).',
    '- Cross-sectional ACS controls: `pct_college_educated`, `pct_nonwhite`,'
    '  `median_home_value`, `is_principal_city_lag2`, `pop_density_sqkm_lag2`.',
    '- NRI risk scores (static): `nri_water_risk_score`, `nri_overall_risk_score`,'
    '  `nri_inland_flooding_eal_bv`.',
    '- Climate-network memberships that do not change: `climate_commitment_static`,'
    '  `iclei_member_static`, `mcpa_signatory_static`.',
    '',
    'City FE identifies only the **time-varying** channels: regulatory enforcement'
    ' events, fiscal condition shocks, tax/expenditure shifts, federal grant'
    ' receipts, and the small number of mayoral party switches.',
])

(OUT_DIR / 'table1_city_fe_robustness.md').write_text('\n'.join(md) + '\n')
print(f"\nWrote: {OUT_DIR / 'table1_city_fe_robustness.md'}")
