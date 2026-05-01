# Marketability Interaction Decision

## Decision

The `npdes_formal_prior3yr_muni × asinh_state_all_green_cum_amt_lag1` (marketability) interaction is **dropped from Table 1 main** and retained only in **Table 3 L3** (labelling margin, conditional on bond issuance), where it is separately identified on a different sample.

Table 1 main reverts to four columns (C1–C4) with the 10-variable PRIMARY and NPDES main effect in its non-interacted form.

## Diagnostic evidence (Task 10)

**10a VIF.** Raw VIF flagged at 13.3 on the interaction term. Centered VIF = 1.13 with identical coefficient — canonical mechanical-correlation pattern, same as the constituency interaction. VIF alone would not motivate the drop.

**10b Leave-one-state-out.** Three of ten single-state exclusions dropped the coefficient below p < 0.10:
- California: β fell 53% (from +0.00160 to +0.00074), p = 0.232.
- State_id=9: p = 0.109.
- State_id=10: p = 0.113.
California alone accounts for the fragility. The remaining seven exclusions preserved marginal significance.

**10c Domain subsample check.** The interaction was not significant in either water-only (p = 0.19) or non-water (p = 0.12) when estimated on subsamples. The pooled-sample significance (p = 0.074) derives from combining two individually-insignificant subsamples.

## Comparison with I2

The constituency × partisan interaction (`Dem_Mayor × pres_dem_two_party_share_lag2`) passes the same diagnostics cleanly:
- Centered VIF 1.18 (same scale).
- No single-state LOSO exclusion drops the interaction below p < 0.05 on non-water (coefficient +0.101, p = 0.002).
- The interaction strengthens — rather than weakens — in the discretionary subdomain.

The two interactions are not comparable in robustness.

## Where the marketability interaction is retained

Table 3 L3 estimates the marketability interaction on the **issuer subsample** (city-years with `total_ltd_issued > 0`, N = 3,888). On this sample, `npdes × state_green_cum` = +0.0022\*\* (p < 0.05). The issuer-conditional sample is a different identification population and the coefficient is separately estimated. The labelling-margin finding does not depend on the fragile full-sample result.

## Preserved files

- `table1_v3_main_eightcol.md` — previous 8-column main table with paired marketability interaction.
- `table1_v3_main_eightcol_full.md` — same, all controls visible.
- `v3_rr/marketability_interaction_diagnostics.md` — full Task 10 diagnostics.
