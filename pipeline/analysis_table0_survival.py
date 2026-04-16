"""
analysis_table0_survival.py — Cox proportional hazards (time-to-first-entry)
===========================================================================
Complementary analysis to Table 1 v2, directly inspired by Widmann (2026)
"When Firms Lead States". Tests whether accumulated state-level market
infrastructure accelerates city-level time-to-first-green-bond entry.

Events:
  Cox A: first Green_Bond_Issued = 1 per city (extensive margin)
  Cox B: first Y_self_green      = 1 per city (Step 3 discretion)

Data structure: start-stop format. For each city, one row per year-at-
risk. Time-varying covariates (state-market depth, fiscal, compulsion)
take year-t values. Once a city's event occurs, subsequent years are
removed (city drops out of risk set).

Primary covariates (all time-varying unless noted):
  - Dem_Mayor (Part D primary treatment)
  - pres_dem_two_party_share_lag2 (MEDSL-backed)
  - npdes_formal_prior3yr_muni (compulsion)
  - charges_to_own_source_lag2 (fiscal)
  - reserve_ratio_lag2, debt_service_burden_lag2, igr_share_lag2 (fiscal)
  - tel_x_prop_tax_dep (TEL interaction)
  - state_self_green_cum_count_lag1 (**Widmann: infrastructure accumulation**)
  - state_any_rep_self_green_lag1 (**co-partisan accumulation**)
  - fn_esg_has_muni_bond_law_post_lag1 (anti-ESG law post)
  - Controls: log pop, log income, unemployment, has_substitute_issuer

Strata: state_id (absorbs fixed state-level hazards — analogue of
Widmann's OECD stratification).

Run: TABLE0_MODULE = {a, b, all}.
"""
import os
import sys
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
from lifelines import CoxTimeVaryingFitter

warnings.filterwarnings('ignore')
sys.path.insert(0, str(Path(__file__).parent))
from helpers import load_panel

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'processed' / 'tables'
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODULE = os.environ.get('TABLE0_MODULE', 'all')
PANEL_START_YEAR = 2013
PANEL_END_YEAR = 2025


# ──────────────────────────────────────────────────────────────────────
# Covariate stack (time-varying where meaningful)
# ──────────────────────────────────────────────────────────────────────
COVARIATES = [
    # Treatment
    'Dem_Mayor',
    # Constituency
    'pres_dem_two_party_share_lag2',
    # Compulsion (F1a)
    'npdes_formal_prior3yr_muni',
    'overflow_events_lag2',
    # Fiscal (F1b)
    'charges_to_own_source_lag2',
    'reserve_ratio_lag2',
    'debt_service_burden_lag2',
    'igr_share_lag2',
    'tel_x_prop_tax_dep',
    # Widmann-style infrastructure accumulation
    'state_self_green_cum_count_lag1',          # count of prior state muni self-green bonds
    'state_any_rep_self_green_lag1',             # co-partisan indicator
    # State environment
    'state_dem_governor_lag1',
    'state_rep_trifecta_lag1',
    'fn_esg_has_muni_bond_law_post_lag1',
    # Controls
    'log_population_city_lag2',
    'log_percapita_income_city_lag2',
    'unemployment_city_lag2',
    'has_substitute_issuer',
]


def build_start_stop(df, event_col):
    """Build (start, stop, event) panel for Cox time-varying regression.

    For each city, one row per year-at-risk. Once the event occurs, the
    city is removed from subsequent rows (drops out of risk set).
    Censoring at PANEL_END_YEAR for cities that never experience the event.
    """
    work = df[['fips7', 'year', 'state_id', event_col] + COVARIATES].copy()
    work = work.dropna(subset=['fips7', 'year', event_col])
    work = work.sort_values(['fips7', 'year'])

    # For each city, find the year of first event (if any)
    ever_event = work.groupby('fips7')[event_col].max()
    first_event_year = (
        work[work[event_col] == 1].groupby('fips7')['year'].min()
    )

    out_rows = []
    for fid, grp in work.groupby('fips7'):
        grp = grp.sort_values('year')
        fey = first_event_year.get(fid, np.nan)
        for _, row in grp.iterrows():
            yr = row['year']
            # Truncate: if this city already had its event in an earlier year, skip.
            if not np.isnan(fey) and yr > fey:
                continue
            start = yr - PANEL_START_YEAR
            stop = start + 1
            # Event flag: 1 only on the year of first event
            ev = 1 if (not np.isnan(fey) and yr == fey) else 0
            out = row.to_dict()
            out['start'] = start
            out['stop'] = stop
            out['event'] = ev
            out_rows.append(out)
    out = pd.DataFrame(out_rows)
    out = out.dropna(subset=COVARIATES + ['start', 'stop', 'event'])
    return out


def fit_cox(start_stop, id_col='fips7', strata='state_id', label=''):
    """Fit CoxTimeVaryingFitter with strata, cluster SE on fips7."""
    fit_df = start_stop[[id_col, 'start', 'stop', 'event', strata] + COVARIATES].copy()
    # Drop covariates with no variation in this sample
    xs = [c for c in COVARIATES if fit_df[c].nunique() > 1]
    fit_df = fit_df.dropna(subset=xs)

    n_events = int(fit_df['event'].sum())
    n_cities = fit_df[id_col].nunique()
    n_obs = len(fit_df)
    print(f"  {label}: {n_obs} at-risk rows, {n_cities} cities, {n_events} events")
    if n_events < 15:
        print(f"  [warn] Few events — estimates may be unstable")

    try:
        ctv = CoxTimeVaryingFitter(penalizer=0.001)  # tiny penalty for stability
        ctv.fit(
            fit_df, id_col=id_col,
            event_col='event', start_col='start', stop_col='stop',
            strata=[strata], show_progress=False,
        )
        return ctv, fit_df
    except Exception as e:
        print(f"  [fit error] {e}")
        return None, fit_df


def format_summary(ctv, focus_vars):
    """Return a markdown table of hazard ratios for focus variables."""
    if ctv is None:
        return ['| (fit failed) |']
    s = ctv.summary
    lines = ['| Variable | Hazard Ratio | 95% CI | p-value |',
             '|---|---|---|---|']
    for v in focus_vars:
        if v in s.index:
            row = s.loc[v]
            hr = row['exp(coef)']
            lo = row['exp(coef) lower 95%']
            hi = row['exp(coef) upper 95%']
            pv = row['p']
            stars = ('***' if pv < 0.01 else '**' if pv < 0.05
                     else '*' if pv < 0.10 else '')
            lines.append(f'| `{v}` | **{hr:.4f}**{stars} | ({lo:.4f}, {hi:.4f}) | {pv:.4f} |')
        else:
            lines.append(f'| `{v}` | — | — | — |')
    return lines


# ──────────────────────────────────────────────────────────────────────
df = load_panel()
print(f"Panel loaded: {df.shape}\nRunning module: {MODULE}\n")


# ──────────────────────────────────────────────────────────────────────
# MODULE: a — Cox on first Green_Bond_Issued
# ──────────────────────────────────────────────────────────────────────
if MODULE in ('a', 'all'):
    print("=== Cox A — time-to-first-Green_Bond_Issued ===\n")
    ss_a = build_start_stop(df, 'Green_Bond_Issued')
    ctv_a, fit_a = fit_cox(ss_a, label='Cox A (Green_Bond_Issued)')
    if ctv_a is not None:
        print(f"\n  log-likelihood = {ctv_a.log_likelihood_:.2f}\n")
        focus = [
            'Dem_Mayor', 'pres_dem_two_party_share_lag2',
            'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
            'charges_to_own_source_lag2', 'reserve_ratio_lag2',
            'debt_service_burden_lag2', 'igr_share_lag2',
            'tel_x_prop_tax_dep',
            'state_self_green_cum_count_lag1', 'state_any_rep_self_green_lag1',
            'state_dem_governor_lag1', 'state_rep_trifecta_lag1',
            'fn_esg_has_muni_bond_law_post_lag1',
            'log_population_city_lag2', 'log_percapita_income_city_lag2',
            'unemployment_city_lag2',
        ]
        s = ctv_a.summary
        for v in focus:
            if v in s.index:
                row = s.loc[v]
                print(f"  {v:42s}  HR={row['exp(coef)']:.4f}  p={row['p']:.3f}")

        # Write md
        md = ['# Cox Proportional Hazards: Time-to-First Green_Bond_Issued',
              '', '**Event:** first city-year with `Green_Bond_Issued == 1` during 2013-2025.',
              '**Censoring:** cities that never issue are censored at 2025.',
              '**Strata:** `state_id` (state-level baseline hazards absorbed).',
              '**Time-varying covariates:** all listed in `pipeline/analysis_table0_survival.py` COVARIATES.',
              '',
              f'- At-risk rows: {len(fit_a):,}',
              f'- Cities in risk set: {fit_a["fips7"].nunique()}',
              f'- Events: {int(fit_a["event"].sum())}',
              f'- Log-likelihood: {ctv_a.log_likelihood_:.2f}',
              '']
        md.extend(format_summary(ctv_a, focus))
        md.extend([
            '',
            'HR > 1: covariate increases the instantaneous hazard of first-ever green-bond issuance.',
            'HR < 1: covariate delays first issuance.',
            '',
            '**Widmann (2026) comparison:** the `state_self_green_cum_count_lag1` hazard ratio here',
            'is directly comparable to Widmann\'s Corporate Private Cumulative (HR ≈ 1.017-1.021,',
            'each +1 corporate bond raises sovereign-entry hazard by 1.7-2.1%). Our equivalent',
            'tests whether each prior muni self-green bond in the state raises the hazard of a new',
            'muni entering.',
            '',
            'Stars: * p < 0.10, ** p < 0.05, *** p < 0.01.',
        ])
        (OUT_DIR / 'table0_cox_GBI.md').write_text('\n'.join(md) + '\n')
        print(f"\nWrote: {OUT_DIR / 'table0_cox_GBI.md'}")


# ──────────────────────────────────────────────────────────────────────
# MODULE: b — Cox on first Y_self_green
# ──────────────────────────────────────────────────────────────────────
if MODULE in ('b', 'all'):
    print("\n=== Cox B — time-to-first-Y_self_green ===\n")
    ss_b = build_start_stop(df, 'Y_self_green')
    ctv_b, fit_b = fit_cox(ss_b, label='Cox B (Y_self_green)')
    if ctv_b is not None:
        print(f"\n  log-likelihood = {ctv_b.log_likelihood_:.2f}\n")
        focus = [
            'Dem_Mayor', 'pres_dem_two_party_share_lag2',
            'npdes_formal_prior3yr_muni', 'overflow_events_lag2',
            'charges_to_own_source_lag2', 'reserve_ratio_lag2',
            'debt_service_burden_lag2', 'igr_share_lag2',
            'tel_x_prop_tax_dep',
            'state_self_green_cum_count_lag1', 'state_any_rep_self_green_lag1',
            'state_dem_governor_lag1', 'state_rep_trifecta_lag1',
            'fn_esg_has_muni_bond_law_post_lag1',
            'log_population_city_lag2', 'log_percapita_income_city_lag2',
            'unemployment_city_lag2',
        ]
        s = ctv_b.summary
        for v in focus:
            if v in s.index:
                row = s.loc[v]
                print(f"  {v:42s}  HR={row['exp(coef)']:.4f}  p={row['p']:.3f}")

        md = ['# Cox Proportional Hazards: Time-to-First Y_self_green',
              '', '**Event:** first city-year with `Y_self_green == 1` (bond self-designated green).',
              '**Censoring:** cities that never self-label are censored at 2025.',
              '**Strata:** `state_id`.',
              '',
              f'- At-risk rows: {len(fit_b):,}',
              f'- Cities in risk set: {fit_b["fips7"].nunique()}',
              f'- Events: {int(fit_b["event"].sum())}',
              f'- Log-likelihood: {ctv_b.log_likelihood_:.2f}',
              '']
        md.extend(format_summary(ctv_b, focus))
        md.extend([
            '',
            'HR > 1: covariate accelerates first self-green designation.',
            'HR < 1: covariate delays.',
            '',
            'Step-3 discretion (per memo): self-designation is the first genuinely discretionary',
            'step in the decision chain. If `Dem_Mayor` predicts timing here (HR > 1), that is a',
            'hazard-model analogue of the memo\'s expected Rep_Mayor-negative at Col 3.',
            '',
            'Stars: * p < 0.10, ** p < 0.05, *** p < 0.01.',
        ])
        (OUT_DIR / 'table0_cox_self_green.md').write_text('\n'.join(md) + '\n')
        print(f"\nWrote: {OUT_DIR / 'table0_cox_self_green.md'}")
