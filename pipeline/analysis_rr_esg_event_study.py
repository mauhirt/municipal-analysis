"""
Task 6: Callaway-Sant'Anna DiD event study for anti-ESG muni bond laws.

Treatment: State-level adoption of first anti-ESG muni bond law (esg_first_law_year).
Outcome:   Y_self_green (city self-labelled green bond issuance).
Unit:      city (fips7). Time: year. Control: never-treated states.
Method:    Callaway & Sant'Anna (2021) via `differences.ATTgt`.

Cohorts:
  - 2021: 6 states (67 cities)
  - 2022: 4 states (21 cities)
  - 2023: 9 states (130 cities)
  - 2024: 1 state  (7 cities)
  - 2025: 1 state  (11 cities)
  - Never: 28 states (342 cities)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from pathlib import Path
from differences import ATTgt

ROOT = Path(__file__).resolve().parent.parent
OUT_TABLE = ROOT / 'processed' / 'tables' / 'v3_rr'
OUT_FIG = ROOT / 'processed' / 'figures' / 'v3_rr'
OUT_TABLE.mkdir(parents=True, exist_ok=True)
OUT_FIG.mkdir(parents=True, exist_ok=True)

df = pd.read_pickle(ROOT / 'processed' / 'panel' / 'panel.pkl')
print(f"Panel: {df.shape}")

# ── Build cohort ──
state_cohort = df.groupby('state_id')['esg_first_law_year'].max().to_dict()
df['esg_cohort'] = df['state_id'].map(state_cohort).fillna(0).astype(int)
df['esg_cohort'] = np.where(df['esg_cohort'] == 0, np.nan, df['esg_cohort'])

n_never = df.loc[df['esg_cohort'].isna(), 'fips7'].nunique()
n_treated = df.loc[df['esg_cohort'].notna(), 'fips7'].nunique()
print(f"Never-treated: {n_never} cities | Treated: {n_treated} cities")
print(f"Cohorts: {sorted(df['esg_cohort'].dropna().unique().astype(int))}")

# ── Fit CS-DiD (3 specs) ──
outcomes = [
    ('Y_self_green', 'Self-labelled green bond issuance'),
    ('Green_Bond_Issued', 'Any green bond issuance (GBI+self)'),
]

all_es = {}
all_simple = {}

for yvar, ylabel in outcomes:
    print(f"\n=== {yvar}: {ylabel} ===")
    d = df[['fips7', 'year', 'esg_cohort', yvar]].copy()
    d = d.reset_index(drop=True).set_index(['fips7', 'year'])

    att = ATTgt(data=d, cohort_column='esg_cohort', base_period='universal')
    result = att.fit(
        formula=yvar,
        est_method='reg',
        control_group='never_treated',
        boot_iterations=999,
        random_state=42,
        progress_bar=False,
    )

    # Simple ATT
    simple_df = result.aggregate('simple')
    att_val = simple_df.iloc[0, 0]
    att_se = simple_df.iloc[0, 1]
    print(f"  Overall ATT: {att_val:+.4f} (SE {att_se:.4f})")
    all_simple[yvar] = (att_val, att_se)

    # Event study aggregation
    es = result.aggregate('event')
    es_flat = es.copy()
    es_flat.columns = ['ATT', 'SE', 'lower', 'upper', 'sig']
    all_es[yvar] = es_flat.copy()

    print("  Event-study coefficients:")
    for idx, row in es_flat.iterrows():
        star = '*' if row['sig'] == '*' else ''
        se_str = f"{row['SE']:.4f}" if not np.isnan(row['SE']) else '—'
        print(f"    e={int(idx):+3d}  ATT={row['ATT']:+.4f}  SE={se_str}  {star}")

    # Cohort-level aggregation
    try:
        cohort_agg = result.aggregate('cohort')
        print("  Cohort-level ATTs:")
        cohort_flat = cohort_agg.copy()
        cohort_flat.columns = ['ATT', 'SE', 'lower', 'upper', 'sig']
        for idx, row in cohort_flat.iterrows():
            print(f"    g={int(idx)}  ATT={row['ATT']:+.4f}  SE={row['SE']:.4f}")
    except Exception as e:
        print(f"  Cohort aggregation error: {e}")

    # Pre-trend Wald test
    try:
        wald = att.wald_pre_test()
        print(f"  Pre-trend Wald: {wald}")
    except Exception as e:
        print(f"  Wald test: {e}")


# ── Event study plot ──
fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

for ax, (yvar, ylabel) in zip(axes, outcomes):
    es = all_es[yvar]
    e = es.index.values.astype(float)
    att_vals = es['ATT'].values
    se_vals = es['SE'].values.copy()
    se_vals = np.where(np.isnan(se_vals), 0, se_vals)

    ax.axhline(0, color='gray', lw=0.8, ls='--')
    ax.axvline(-0.5, color='red', lw=0.8, ls=':', alpha=0.6)

    ax.errorbar(e, att_vals, yerr=1.96 * se_vals,
                fmt='o', color='#1f77b4', capsize=3, ms=5, lw=1.5)
    ax.fill_between(e, att_vals - 1.96 * se_vals, att_vals + 1.96 * se_vals,
                    alpha=0.15, color='#1f77b4')

    att_overall, se_overall = all_simple[yvar]
    ax.set_title(f'{ylabel}\nOverall ATT = {att_overall:+.004f} (SE {se_overall:.004f})', fontsize=11)
    ax.set_xlabel('Event time (years since anti-ESG law)')
    ax.set_ylabel('ATT(e)' if ax == axes[0] else '')

    # Mark the pre-treatment range
    pre_mask = e < -0.5
    if pre_mask.any():
        ax.axvspan(e[pre_mask].min() - 0.5, -0.5, alpha=0.05, color='green')
        ax.text(e[pre_mask].mean(), ax.get_ylim()[1] * 0.9, 'Pre', ha='center',
                fontsize=9, color='green', alpha=0.6)

fig.suptitle('Callaway-Sant\'Anna Event Study: Anti-ESG Muni Bond Laws → Green Bond Issuance',
             fontsize=13, y=1.02)
plt.tight_layout()
fig_path = OUT_FIG / 'esg_event_study_cs.png'
plt.savefig(fig_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"\nSaved: {fig_path}")


# ── Write markdown table ──
lines = [
    '# Task 6: CS-DiD Event Study — Anti-ESG Laws and Green Bond Issuance',
    '',
    '**Method:** Callaway & Sant\'Anna (2021) via `differences.ATTgt`.',
    '**Treatment:** State-level adoption of first anti-ESG muni bond law.',
    '**Control group:** Never-treated states (28 states, 342 cities).',
    '**Base period:** Universal (last pre-treatment period).',
    '**Inference:** Bootstrap (999 iterations), analytic pointwise CIs.',
    '',
    '## Cohort structure',
    '',
    '| Cohort | States | Cities | Y_self_green events |',
    '|---|---|---|---|',
]

for g in sorted(df['esg_cohort'].dropna().unique().astype(int)):
    sub = df[df['esg_cohort'] == g]
    n_st = sub['state_id'].nunique()
    n_city = sub['fips7'].nunique()
    n_y = int(sub['Y_self_green'].sum())
    lines.append(f'| {g} | {n_st} | {n_city} | {n_y} |')
lines.append(f'| Never | 28 | {n_never} | {int(df.loc[df["esg_cohort"].isna(), "Y_self_green"].sum())} |')

lines.extend([
    '',
    '## Overall ATT (simple aggregation)',
    '',
    '| Outcome | ATT | SE | 95% CI |',
    '|---|---|---|---|',
])
for yvar, ylabel in outcomes:
    att_val, att_se = all_simple[yvar]
    lo, hi = att_val - 1.96 * att_se, att_val + 1.96 * att_se
    lines.append(f'| `{yvar}` | {att_val:+.4f} | {att_se:.4f} | [{lo:+.4f}, {hi:+.4f}] |')

for yvar, ylabel in outcomes:
    es = all_es[yvar]
    lines.extend([
        '',
        f'## Event-study: `{yvar}`',
        '',
        '| Event time | ATT | SE | 95% CI | Sig |',
        '|---|---|---|---|---|',
    ])
    for idx, row in es.iterrows():
        se_str = f"{row['SE']:.4f}" if not np.isnan(row['SE']) else '—'
        if np.isnan(row['SE']):
            ci = '—'
        else:
            ci = f"[{row['ATT'] - 1.96*row['SE']:+.4f}, {row['ATT'] + 1.96*row['SE']:+.4f}]"
        sig = '\\*' if row['sig'] == '*' else ''
        lines.append(f'| e={int(idx):+d} | {row["ATT"]:+.4f} | {se_str} | {ci} | {sig} |')

lines.extend([
    '',
    '## Interpretation',
    '',
    '- **Overall ATT is negative but insignificant** for both outcomes. Anti-ESG laws do not detectably '
    'suppress city-level self-labelled green bond issuance — but the point estimate is directionally negative.',
    '- **Pre-trends:** Distant leads (e = -12, -11) show positive coefficients for treated states, '
    'suggesting treated states had *higher* baseline issuance rates in the early panel. Closer leads '
    '(e = -7 through -2) are near zero, consistent with parallel trends in the relevant window.',
    '- **Post-treatment (e = 0 to +4):** Uniformly negative (-0.009 to -0.016) but none individually significant. '
    'Consistent with a small, imprecisely estimated suppression effect.',
    '- **Power caveat:** Only 28 self-labelled events across all treated cohorts. The rare outcome severely '
    'limits statistical power. The null finding should be interpreted as "too rare to detect" rather than '
    '"no effect."',
    '',
    '* = zero outside pointwise 95% confidence band.',
    '',
    f'![Event study](../../figures/v3_rr/esg_event_study_cs.png)',
])

out_path = OUT_TABLE / 'esg_event_study_cs.md'
out_path.write_text('\n'.join(lines) + '\n')
print(f"Saved: {out_path}")
