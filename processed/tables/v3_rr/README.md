# R&R Response Package (v3_rr)

Revise-and-resubmit supplementary outputs for Table 1 v3.

**Sample:** 5,962 city-years, 572 cities, 49 states, 2013–2025.
**Treatment:** `Dem_Mayor` (no lag). **FE:** state + year. **SE:** clustered at city (fips7).

---

## Files

| File | Task | Purpose |
|---|---|---|
| `demonstration_diagnostic.md` | 2 | 4 measures × 2 specs; selects M1 for main table, M2–M4 to appendix |
| `appendix_alt_interactions.md` | 3 | Demoted interaction specs: Dem×stress, stress², M2–M4 demonstration |
| `within_r2_ftest.md` | 8 | Within-R² (entity+time FE) and compulsion-block joint F-test |
| `cluster_comparison.md` | 4 | City-clustered vs state-clustered vs two-way (Cameron-Gelbach-Miller) |
| `constituency_decomposition.md` | 7 | `pres_dem_share` vs `Dem_Mayor` decomposition; scatter + 3 regressions |
| `esg_event_study_cs.md` | 6 | Callaway-Sant'Anna event study for anti-ESG muni bond law adoption |

Figures: `../../figures/v3_rr/` (`pres_vs_mayor_scatter.png`, `esg_event_study_cs.png`).

---

## Headline findings across the R&R package

1. **H1b (Dem_Mayor null at extensive margin) holds** across all 27 specifications in Table 1 v3 (main C1–C5 + R1–R21) and survives every robustness check in this package.
2. **Partisan margin exists only via demonstration (H3)** — C6 Demonstration shows `Dem_Mayor` = -0.034\*\*, `dem_x_state_green_cum` = +0.0015\*\*. Dem mayors respond to existing state markets, do not autonomously initiate them.
3. **Constituency ≠ mayoral agency** — `pres_dem_two_party_share_lag2` is robustly positive (+0.059\*\*) across all specs, while `Dem_Mayor` is null. The constituency–mayor interaction (V3 in decomposition) = +0.137\*\*: pres-dem-share and Dem_Mayor are *not independent*; their effects are entangled.
4. **Compulsion story rests on NPDES formal enforcement** — +0.018\*\* consistently, generalises to `_locgov` (+0.014\*\*), clean placebo on `_private` (null). Overflow variable was scrapped due to rarity (9 nonzero city-years, all 2024–2025 due to EPA's electronic SSO reporting only starting ~2022).
5. **Pre-ESG-law market matters** — R17: `state_pre_esg_activity` +0.064\*\*\*. CS-DiD event study (Task 6): overall ATT of anti-ESG laws on self-labelled issuance is -0.012 (SE 0.011, ns), with post-treatment coefficients uniformly negative (-0.009 to -0.016) but imprecise. Suppression direction is right; power is limited by rare outcome.
6. **Two-way clustering check (Task 4):** Most results are stable; `overflow_events_lag2` lost significance under two-way clustering (p=0.002 → p=0.211) — which was one signal that led to scrapping overflow entirely.

---

## Reproduction

```bash
# All Table 1 v3 modules
TABLE1_MODULE=all python3 pipeline/analysis_table1_v3.py

# Individual R&R outputs
python3 pipeline/analysis_rr_demonstration_diagnostic.py     # Task 2
python3 pipeline/analysis_rr_constituency_decomp.py          # Task 7
python3 pipeline/analysis_rr_esg_event_study.py              # Task 6
TABLE1_MODULE=ftest python3 pipeline/analysis_table1_v3.py   # Task 8
TABLE1_MODULE=cluster_check python3 pipeline/analysis_table1_v3.py  # Task 4
```

## Dependencies

Python 3.11+, `pandas`, `numpy`, `statsmodels`, `linearmodels`, `matplotlib`, `scipy`, `differences` (CS-DiD, ≥0.3.0), `lifelines` (survival in Table 0).
