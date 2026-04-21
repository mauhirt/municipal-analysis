# Fiscal interactions with partisanship (FS1–FS5)

**Outcome:** `Y_self_green` across all specifications.
**Sample:** Reconciled N=6,825 (576 cities, 2014–2025). Sample drops to N=6,811 where `fiscal_stress_composite_lag2` is required (14 obs missing on composite), to N=6,680–6,691 where `Rep_Mayor_lag1` is required (additional ~130 obs missing on lagged mayor).
**Base spec:** 10-variable PRIMARY (`Dem_Mayor`, `npdes_formal_prior3yr_muni`, `pres_dem_two_party_share_lag2`, `asinh_state_all_green_cum_amt_lag1`, `reserve_ratio_lag2`, `debt_service_burden_lag2`, `fn_esg_has_muni_bond_law_post_lag1`, `log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`). State + year FE. SE clustered at city.

---

## Step 2 — Baseline Dem interactions (FS1–FS4)

Each spec adds one Dem × fiscal interaction to PRIMARY.

| Spec | Added regressor | Fiscal main effect | Dem × fiscal interaction | N |
|---|---|---|---|---|
| FS1 Dem × Composite | `fiscal_stress_composite_lag2` + `dem_x_fs_composite` | -0.0026 (0.0044) | -0.0025 (0.0039) | 6,811 |
| FS2 Dem × Debt Service | `dem_x_debt_service` | -0.0660 (0.0446) | +0.0451 (0.0703) | 6,825 |
| FS3 Dem × Reserve Ratio | `dem_x_reserve_ratio` | +0.0007 (0.0025) | +0.0057 (0.0038) | 6,825 |
| FS4 Dem × TEL×PropTax | `tel_x_prop_tax_dep` + `dem_x_tel_prop_tax` | +0.0005 (0.0005) | **+0.0009\*** (0.0006) | 6,811 |

### Delta-method slopes (Dem vs Rep mayor slope on each fiscal variable)

| Spec | Dem slope (β_fiscal + β_interaction) | Rep slope (β_fiscal only) |
|---|---|---|
| FS1 Composite | -0.0051 (0.0040) | -0.0026 (0.0044) |
| FS2 Debt Service | -0.0209 (0.0700) | -0.0660 (0.0446) |
| FS3 Reserve Ratio | +0.0064 (0.0045) | +0.0007 (0.0025) |
| FS4 TEL × PropTax | **+0.0014\*** (0.0008) | +0.0005 (0.0005) |

`Dem_Mayor` coefficient (in each Step 2 spec):
- FS1: -0.0010 (0.0039)  ·  FS2: -0.0026 (0.0055)  ·  FS3: -0.0051 (0.0043)  ·  FS4: -0.0152 (0.0095)

---

## Step 3 — Symmetric check (Dem and Rep interactions jointly)

Reference category: independent / nonpartisan mayors (neither Dem_Mayor=1 nor Rep_Mayor_lag1=1).

| Spec | Fiscal main | Dem interaction | Rep interaction | N |
|---|---|---|---|---|
| FS1-sym Composite | -0.0029 (0.0052) | -0.0015 (0.0040) | +0.0003 (0.0042) | 6,680 |
| FS2-sym Debt Service | -0.0034 (0.0699) | -0.0013 (0.0722) | -0.0726 (0.0772) | 6,691 |
| FS3-sym Reserve | -0.0022 (0.0056) | +0.0078 (0.0055) | +0.0030 (0.0054) | 6,691 |
| FS4-sym TEL×PropTax | +0.0008 (0.0008) | +0.0007 (0.0006) | -0.0003 (0.0007) | 6,680 |

The Step 2 FS4 Dem × interaction attenuates from +0.0009\* to +0.0007 (ns, p≈0.24) when `Rep_Mayor_lag1` is added. Neither Dem nor Rep interactions reach significance in the symmetric spec across FS1-sym–FS4-sym.

---

## Step 4 — Triple interaction (FS5)

`Y_self_green ~ PRIMARY + fiscal_stress_composite_lag2 + dem×fs + dem×market + fs×market + dem×fs×market`

N=6,811, R²=0.095.

| Term | β | SE | p |
|---|---|---|---|
| `Dem_Mayor` | **-0.0271\*\*\*** | 0.0097 | 0.0050 |
| `fiscal_stress_composite_lag2` | -0.0014 | 0.0050 | 0.7838 |
| `asinh_state_all_green_cum_amt_lag1` | -0.0004 | 0.0005 | 0.4103 |
| `dem_x_fs` | -0.0037 | 0.0049 | 0.4536 |
| `dem_x_market` | **+0.0013\*\*\*** | 0.0005 | 0.0052 |
| `fs_x_market` | -0.00001 | 0.0002 | 0.9346 |
| `dem_x_fs_x_market` | **-0.00002** | 0.0004 | **0.9588** |

### Marginal effect of `Dem_Mayor` across fiscal-stress × market-depth

| Market depth | Fiscal stress | ME | SE | p |
|---|---|---|---|---|
| Low (10th) | 10th pct | +0.00017 | 0.00631 | 0.979 |
| Low (10th) | 50th pct | -0.00482 | 0.00403 | 0.232 |
| Low (10th) | 90th pct | **-0.00963\*** | 0.00494 | 0.051 |
| Median (50th) | 10th pct | +0.00611 | 0.00745 | 0.412 |
| Median (50th) | 50th pct | +0.00102 | 0.00412 | 0.805 |
| Median (50th) | 90th pct | -0.00388 | 0.00577 | 0.501 |
| High (90th) | 10th pct | +0.00918 | 0.00826 | 0.267 |
| High (90th) | 50th pct | +0.00403 | 0.00455 | 0.376 |
| High (90th) | 90th pct | -0.00091 | 0.00675 | 0.892 |

Plot: `processed/figures/v3_rr/fs5_marginal_effects.png`.

Only one of 9 cells reaches p<0.10 (Dem in shallow-market + high-stress states: -0.0096\*). The triple interaction itself is -0.00002 (p=0.96). The `dem_x_market` two-way interaction (+0.0013\*\*\*) carries the partisan signal; fiscal stress does not modulate it.

---

## Reading

**1. Does fiscal stress modulate the mayoral-partisanship effect on green-bond issuance?**

Marginally, in Step 2 FS4 only: `Dem × (TEL × property-tax dependence)` = +0.0009\* (p=0.10). The delta-method Dem slope on the Mullins interaction is +0.0014\*, while the Rep slope is +0.0005 (ns). All other fiscal interactions (FS1 composite, FS2 debt service, FS3 reserve ratio) are null. Once `Rep_Mayor_lag1` is added symmetrically (Step 3), the FS4 Dem interaction attenuates to +0.0007 (p≈0.24) and neither partisan group differs from the nonpartisan-mayor reference. The Step 2 FS4 finding is thus fragile — present in the base-reference spec, absent in the symmetric spec.

**2. Is the effect Democratic-specific or general?**

The Step 2 FS4 result is nominally Dem-specific (Dem slope +0.0014\*, Rep slope +0.0005 ns). But the Step 3 symmetric spec shows neither partisan group has a slope on TEL × PropTax distinguishable from independents. The asymmetry in Step 2 reflects the baseline comparison (effectively Rep/Ind pooled) rather than a Dem-specific mechanism.

**3. Does the fiscal-stress mechanism require a mature state green-bond market (Step 4 FS5)?**

No. The triple interaction `Dem × fiscal_stress × state_green_cum` = -0.00002 (p=0.96). The two-way `Dem × market_depth` interaction is independently significant (+0.0013\*\*\*, p=0.005), but fiscal stress does not amplify it. The marginal-effects table shows only 1 of 9 cells reaches p<0.10 (Dem in shallow-market, high-stress states: -0.010\*), consistent with noise rather than a systematic conditional effect.

**4. Is the TEL-related result robust to alternative TEL operationalizations?**

No — the results flip. In the 10-variable PRIMARY + TEL spec:

| Spec | TEL coefficient | Sig |
|---|---|---|
| TEL-0 Mullins (`tel_x_prop_tax_dep`) | +0.00091 (0.00063) | p=0.15 |
| TEL-1 Simple binary (`has_tel_binding_lag1`) | **+0.0371\*\*\*** (0.0135) | p<0.01 |
| TEL-2 Continuous strictness (`tel_strictness_index_lag1`) | -0.0007 (0.0009) | p=0.40 |
| TEL-3 Components separately (binary + prop_tax_dep) | binary **+0.042\*\*** (0.019); prop_tax_dep +0.015 (0.024) | — |

The simple binary "has any TEL binding" (TEL-1) produces the strongest TEL-related coefficient (**+0.037\*\*\***). The Mullins interaction form (TEL-0) is not significant in the full 10-variable spec, and the continuous-strictness form (TEL-2) is null with the wrong sign. Decomposing into components (TEL-3) assigns the effect entirely to the binary TEL indicator, not to property-tax dependence or their product. `Dem_Mayor` is null (≤ |0.0005|) in all four TEL specs.

Implication for the main table: the Mullins interaction is not the uniquely productive form of the TEL variable. A main-table specification that uses `has_tel_binding_lag1` as the TEL variable would produce a stronger and more readily interpretable result than `tel_x_prop_tax_dep`, and would not depend on Property tax dependence to carry the signal.

---

## Files

- `fiscal_stress_construction.md` — composite component details
- `fiscal_interactions.md` — this file (Steps 2–4)
- `tel_robustness.md` — Step 5 TEL alternatives
- `processed/figures/v3_rr/fs5_marginal_effects.png` — Dem marginal effect × fiscal stress × market depth

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01. SEs in parentheses, clustered at city (fips7).
