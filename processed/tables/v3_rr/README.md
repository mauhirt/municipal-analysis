# R&R Supplementary Package (v3_rr)

Revise-and-resubmit supplementary outputs for Table 1 v3.

**Sample:** 6,825 city-years · 576 cities · 49 states · 2014–2025.
**Treatment:** `Dem_Mayor` (no lag; three-tier imputation applied — see `sample_reconciliation.md`).
**FE:** state + year. **SE:** clustered at city (fips7).

---

## Files

| File | Purpose |
|---|---|
| `sample_reconciliation.md` | Why the sample is N=6,825 and what `Dem_Mayor` imputation tiers were applied |
| `demonstration_diagnostic.md` | 4 interaction measures × 2 specs; M1 selected for Table 1 I3 |
| `appendix_alt_interactions.md` | Demoted interaction specs (M2–M4 state-cum variants, fiscal stress square) |
| `within_r2_ftest.md` | Within-R² and compulsion-block F-test (entity + time FE via PanelOLS) |
| `cluster_comparison.md` | City-clustered vs state-clustered vs two-way (Cameron-Gelbach-Miller) SE |
| `constituency_decomposition.md` | `pres_dem_share` vs `Dem_Mayor` scatter plot + 3 regression variants |
| `esg_event_study_cs.md` | Callaway-Sant'Anna event study for state anti-ESG muni bond law adoption |
| `fiscal_stress_construction.md` | Four-component fiscal-stress composite construction + party/region distributions |
| `fiscal_interactions.md` | Fiscal interactions battery (FS1–FS5) + reading section answering 4 questions |
| `tel_robustness.md` | TEL operationalization comparison with identification correction |
| `interaction_vif_diagnostics.md` | VIF + common support + marginal effects for C6 and marketability interactions |

Figures in `../../figures/v3_rr/`:
- `pres_vs_mayor_scatter.png` — constituency/mayor scatter
- `esg_event_study_cs.png` — CS-DiD event study
- `fs5_marginal_effects.png` — FS5 triple-interaction marginal effects
- `c6_marginal_effects.png` — C6 demonstration marginal effect across state market depth

---

## Headline findings

1. **H1b: `Dem_Mayor` null across every outcome and every specification.** 32 specs tested (C1–C8 main + R1–R24 robustness). Range −0.002 to +0.025; all p ≥ 0.09.

2. **Marketability is the operative compulsion channel.** Main table: NPDES is significant (+0.014\* to +0.016\*\*) when entered alone; flips null when the `npdes × state_green_cum` interaction is included (+0.0016\* to +0.0018\*). The centered-interaction VIF test confirms this is not a collinearity artifact (centered VIF 1.13, identical coefficient).

3. **Constituency drives issuance, not mayoral agency.** `pres_dem_two_party_share_lag2` = +0.053\*\* to +0.055\*\* across main columns, stable regardless of interaction inclusion.

4. **The only partisan signal is conditional: demonstration (I3).** `Dem_Mayor` = −0.024\*\*\* once the `Dem × state_green_cum` interaction is added; interaction = +0.0011\*\*\*. Dem mayors respond to existing state markets; they don't create them. VIF-robust (centered VIF 1.14).

5. **No local spatial spillover** (R13–R16). All four gravity-weighted channels (peer city, special district, county, joint) are null. The spatial-spillover story operates at the **state market-depth level**, not through local peer imitation.

6. **Anti-ESG law endogeneity matters (R17).** States with pre-existing green-bond activity before their first anti-ESG law produce significantly more self-labelled issuance (`state_pre_esg_activity` +0.064\*\*\*). CS-DiD event study shows directional but imprecise suppression after law adoption (overall ATT −0.012, ns) — rare outcome limits power.

7. **Fiscal stress does not modulate the partisan effect.** FS1–FS4 and the FS5 triple interaction are null or fragile. The labelling-incentive story (greenium-seeking) operates through debt service and fiscal stress *conditional on issuance* (Table 3 L2), not through a Dem-specific mechanism.

8. **TEL under state FE.** Binary TEL indicators are rank-deficient (no within-state variation). The Mullins interaction (`tel_x_prop_tax_dep`) is the only identified form; null (p=0.15) in the 10-variable PRIMARY spec. Dropped from main, retained as robustness.

9. **Clustering check.** Main findings are stable under city, state, and two-way clustering. No material sensitivity to the SE scheme.

10. **Two-way fixed effects (entity + time).** Within-R² for the compulsion block is near zero after city + year FE, indicating the compulsion coefficients are identified primarily off cross-sectional variation within states. This is consistent with the paper's framing; the F-test for the compulsion block is not significant (F ≈ 0.5–1.5 across C1–C6).

---

## Reproduction

```bash
# Imputation patch (one-time, idempotent)
python3 pipeline/patch_dem_mayor_imputation.py

# Main table + all robustness + F-test + clustering
TABLE1_MODULE=all python3 pipeline/analysis_table1_v3.py

# R&R sibling scripts
python3 pipeline/analysis_rr_demonstration_diagnostic.py
python3 pipeline/analysis_rr_constituency_decomp.py
python3 pipeline/analysis_rr_esg_event_study.py

# Table 3 (labelling decision on issuer subsample)
python3 pipeline/analysis_table3_labelling.py
```

## Dependencies

Python 3.11+, `pandas`, `numpy`, `scipy`, `statsmodels`, `linearmodels`, `matplotlib`, `differences` (≥0.3.0 — CS-DiD), `lifelines` (Table 0 survival).
