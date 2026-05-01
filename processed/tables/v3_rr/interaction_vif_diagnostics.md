# Interaction-term VIF and support diagnostics

**Purpose:** Verify that the two significant interaction terms in Table 1 are not collinearity-driven artifacts. **Sample:** reconciled N=6,825, 10-variable PRIMARY spec, state + year FE, city-clustered SE.

## Diagnostic A — Demonstration (C6/I3: `Dem_Mayor × asinh_state_all_green_cum_amt_lag1`)

### VIF — raw interaction

| Variable | β | SE | p | VIF |
|---|---|---|---|---|
| `Dem_Mayor` | -0.02438 | 0.00916 | **0.008\*\*\*** | **13.04 ⚠** |
| `asinh_state_all_green_cum_amt_lag1` | -0.00033 | 0.00043 | 0.443 | 4.39 |
| `dem_x_state_green_cum` | +0.00121 | 0.00045 | **0.008\*\*\*** | **14.13 ⚠** |

### VIF — mean-centered interaction (definitive test)

After demeaning `Dem_Mayor` and `asinh_state_all_green_cum_amt_lag1`, then forming `Dem_c × state_green_c`:

| Variable | β | SE | p | VIF |
|---|---|---|---|---|
| `Dem_Mayor_c` | -0.00224 | 0.00387 | 0.563 | 1.55 |
| `state_green_c` | +0.00036 | 0.00034 | 0.297 | 3.00 |
| `dem_x_state_green_cum_c` | **+0.00121** | 0.00045 | **0.008\*\*\*** | **1.14** |

**Reading.** The interaction coefficient is identical in raw and centered forms (+0.00121, p=0.008). VIFs collapse from 13-14 to ~1-3 when variables are centered. This is the canonical signature of **mechanical interaction-term correlation** (X and X·Z are correlated by construction), not collinearity between distinct regressors. The finding is robust.

### Common support

| Group | N | Mean | Median | p25 | p75 | Count at zero | Count above median |
|---|---|---|---|---|---|---|---|
| Dem mayor | 3,859 | 19.89 | 21.40 | 19.90 | 22.57 | **284** | 1,922 |
| Rep / Ind | 2,966 | 19.45 | 21.16 | 19.59 | 22.39 | 246 | 1,441 |

Dem-mayor count at zero state_green_cum = **284 > 200 threshold**. Common support requirement met.

### Marginal-effects crossover

Marginal effect of `Dem_Mayor` on P(Y_self_green) crosses zero at **asinh_state_green_cum ≈ 20.07**. The 10th, 50th, 90th percentiles of state_green_cum in the sample are {≈19.0, 21.40, 22.84}. **Roughly 28% of sample observations fall below the crossover** (Dem effect negative), 72% above (Dem effect positive). Plot: `processed/figures/v3_rr/c6_marginal_effects.png`.

---

## Diagnostic B — Marketability (`npdes × asinh_state_all_green_cum_amt_lag1`)

### VIF — raw interaction

| Variable | β | SE | p | VIF |
|---|---|---|---|---|
| `npdes_formal_prior3yr_muni` | -0.01533 | 0.01334 | 0.251 | **13.30 ⚠** |
| `asinh_state_all_green_cum_amt_lag1` | +0.00010 | 0.00039 | 0.792 | 3.21 |
| `npdes_x_state_green` | +0.00160 | 0.00090 | **0.074\*** | **13.25 ⚠** |

### VIF — mean-centered interaction

| Variable | β | SE | p | VIF |
|---|---|---|---|---|
| `npdes_c` | +0.01378 | 0.00593 | **0.020\*\*** | 1.25 |
| `state_green_c` | +0.00037 | 0.00034 | 0.288 | 3.00 |
| `npdes_x_state_green_c` | **+0.00160** | 0.00090 | **0.074\*** | **1.13** |

**Reading.** Same pattern: interaction coefficient identical across raw and centered forms (+0.00160, p=0.074). Centered VIFs are ~1.1-3.0. The raw VIFs are mechanical. The NPDES main-effect coefficient flips from -0.015 (ns) to +0.014\*\* (p=0.020) between raw and centered — this is the expected identification shift (raw interprets NPDES at state_green_cum=0; centered interprets at mean). Both are consistent: compulsion increases issuance, amplified at higher market depth.

### Correlation structure

| Pair | Correlation |
|---|---|
| `npdes_formal_prior3yr_muni` ↔ `asinh_state_all_green_cum_amt_lag1` (city-year) | -0.011 |
| `npdes_formal_prior3yr_muni` ↔ `npdes_x_state_green` (mechanical) | 0.901 |
| `asinh_state_all_green_cum_amt_lag1` ↔ `npdes_x_state_green` | 0.170 |
| State-year averages of NPDES ↔ state_green_cum | 0.088 |

The 0.901 correlation between NPDES and the interaction is mechanical (any X·Z will correlate ~0.9 with X when Z has low variation). The underlying constituents are essentially uncorrelated (-0.011 at city-year, 0.088 at state-year). No substantive collinearity problem.

---

## Verdict

Both interaction findings survive the VIF diagnostic:

| Interaction | Raw VIF | Centered VIF | Coefficient (both) | p (both) |
|---|---|---|---|---|
| `Dem × state_green_cum` (C6/I3 Demonstration) | 14.1 ⚠ | **1.14** | +0.00121 | 0.008 |
| `npdes × state_green_cum` (Marketability) | 13.3 ⚠ | **1.13** | +0.00160 | 0.074 |

Neither is a collinearity artifact. The C6 demonstration interaction is robust at the 1% level; the marketability interaction is robust at the 10% level. Both have adequate common support: 284 Dem-mayor city-years at zero state_green_cum exceeds the 200-observation threshold.

---

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01. VIF > 10 flagged with ⚠. SEs clustered at city (fips7).
