# NW3 — Non-Water Constituency × Partisan Interaction

**Outcome:** `Y_has_non_water` (any non-water green bond category).
**Sample:** N=6,825 · 576 cities · 49 states · 2014–2025. Positive city-years: 57.
**FE:** state + year. **SE:** clustered at city (fips7).

---

## Coefficients (NW1, NW2, NW3 side by side)

| Variable | NW1 (baseline) | NW2 (+marketability) | NW3 (+Dem×pres_dem) |
|---|---|---|---|
| `Dem_Mayor` | +0.0011 (0.0026) | +0.0011 (0.0026) | **-0.0560\*\*\*** (0.0182) |
| `pres_dem_two_party_share_lag2` | **+0.0373\*\*** (0.0155) | **+0.0377\*\*** (0.0155) | -0.0137 (0.0140) |
| **`dem_x_pres_dem`** | — | — | **+0.1014\*\*\*** (0.0323) |
| `npdes_formal_prior3yr_muni` | +0.0064 (0.0047) | -0.0117 (0.0088) | -0.0109 (0.0088) |
| `npdes_x_state_green` | — | +0.0009 (0.0006) | +0.0008 (0.0006) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0002 (0.0002) | +0.0000 (0.0002) | -0.0000 (0.0002) |
| `reserve_ratio_lag2` | +0.0011 (0.0019) | +0.0010 (0.0019) | +0.0011 (0.0018) |
| `debt_service_burden_lag2` | -0.0148 (0.0299) | -0.0142 (0.0299) | -0.0193 (0.0288) |
| `fn_esg_has_muni_bond_law_post_lag1` | +0.0043 (0.0039) | +0.0042 (0.0039) | +0.0052 (0.0040) |
| `log_population_city_lag2` | **+0.0185\*\*\*** (0.0051) | **+0.0185\*\*\*** (0.0050) | **+0.0181\*\*\*** (0.0049) |
| `log_percapita_income_city_lag2` | **+0.0183\*\*** (0.0091) | **+0.0179\*\*** (0.0091) | **+0.0160\*** (0.0085) |
| `unemployment_city_lag2` | +0.0008 (0.0008) | +0.0007 (0.0008) | +0.0008 (0.0008) |
| N | 6,825 | 6,825 | 6,825 |
| Positive city-years | 57 | 57 | 57 |
| R² | 0.062 | 0.063 | 0.067 |

---

## Diagnostics

### VIF

| Variable | Raw VIF | Centered VIF | Centered β | Centered p |
|---|---|---|---|---|
| `Dem_Mayor` | **24.28 ⚠** | **1.49** | +0.0017 | 0.505 |
| `pres_dem_two_party_share_lag2` | 3.51 | 2.11 | +0.0436\*\*\* | 0.009 |
| `dem_x_pres_dem` | **29.75 ⚠** | **1.18** | **+0.1014\*\*\*** | **0.002** |

Raw VIFs are high (24–30) due to the mechanical correlation between a binary variable and its product with a continuous moderator. Centered VIFs drop to 1.2–2.1 with identical interaction coefficient (+0.1014, p=0.002). **Not a collinearity artifact.**

### Discordant city-years (common support)

| Category | Count |
|---|---|
| Dem_Mayor=1 & pres_dem < 0.45 (Dem mayor in red city) | 324 |
| Dem_Mayor=0 & pres_dem > 0.55 (Rep mayor in blue city) | 1,026 |
| **Total discordant** | **1,350 ✓ ≥ 200** |

Common support is adequate. 1,350 city-years identify the interaction from "wrong-party" combinations.

### Marginal effect of `Dem_Mayor` across `pres_dem_share`

| Percentile | pres_dem value | Marginal effect | SE | p |
|---|---|---|---|---|
| 10th | 0.389 | **-0.0165** | 0.0061 | **0.006\*\*\*** |
| 50th | 0.566 | +0.0015 | 0.0026 | 0.567 |
| 90th | 0.750 | **+0.0201** | 0.0067 | **0.003\*\*\*** |

**Crossover:** Marginal effect of `Dem_Mayor` crosses zero at **pres_dem = 0.552** (45.5% of sample below crossover).

Plot: `processed/figures/v3_rr/nw3_marginal_effects.png`.

---

## Reading

**(a) Is the interaction significant?**

Yes. `Dem_Mayor × pres_dem_two_party_share_lag2` = **+0.1014\*\*\*** (SE 0.0323, p=0.002). This is the strongest partisan-conditional finding in the paper. It survives the centered-VIF check (identical coefficient, VIF 1.18) and has adequate common support (1,350 discordant city-years).

**(b) What is the sign and implied marginal-effect pattern?**

The interaction is positive: the marginal effect of having a Dem mayor on non-water green bond issuance increases with the Dem share of the constituency.

- In **red constituencies** (pres_dem < 0.45): Dem mayors issue **fewer** non-water green bonds than expected (ME = -0.017\*\*\*).
- In **median constituencies** (pres_dem ≈ 0.55): Dem mayors have **no effect** (ME = +0.002, ns).
- In **blue constituencies** (pres_dem > 0.75): Dem mayors issue **more** non-water green bonds (ME = +0.020\*\*\*).

The crossover at pres_dem = 0.552 means: below ~55% Dem vote share, having a Dem mayor is weakly negative for non-water issuance; above ~55%, it is positive. The median city is at the crossover — the mayoral effect is null on average (NW1: +0.001 ns) because the positive and negative tails cancel.

**(c) Does the interaction survive the fragility check?**

- VIF: 1.18 centered. ✓
- Discordant count: 1,350. ✓ ≥ 200.
- Marginal effects are significant at both tails (p<0.01 at 10th and 90th percentiles). ✓

The interaction is robust to these diagnostics. It does not collapse under the same tests that dismissed the assurance finding.

---

## Interpretation note (not editorial — for user consideration)

The NW3 finding says that `Dem_Mayor` and `pres_dem_share` are **not independent** in their effect on non-water green bond issuance. The NW1 null on `Dem_Mayor` is a pooled average of a positive effect in blue cities and a negative effect in red cities.

This is consistent with the constituency decomposition (Task 7, V3: interaction = +0.138\*\* on `Y_self_green`). The NW3 result confirms that this interaction operates specifically in the **discretionary** domain (non-water), where mayoral latitude is greatest.

Whether this constitutes a "partisan story" depends on the causal interpretation: is it the Dem mayor *responding to* constituency demand (agency), or is the interaction an artifact of Dem-mayor cities being systematically different in ways not captured by pres_dem_share alone (selection)?

---

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01. SEs clustered at city (fips7). State + year FE.
