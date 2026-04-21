# TEL operationalization robustness — CORRECTED

**Outcome:** `Y_self_green`. **Base spec:** 10-variable PRIMARY with the TEL variable swapped per column. State + year FE, city-clustered SE.

## Identification check (CRITICAL)

Under state FE, any variable that is **perfectly constant within state** is absorbed. The initial TEL-1 and TEL-3 (binary component) specifications produced coefficients via pseudo-inverse despite being rank-deficient. Those coefficients are **numerical artifacts and should not be interpreted**.

| Variable | Within-state variation? | Identified under state FE? |
|---|---|---|
| `tel_x_prop_tax_dep` (Mullins interaction) | Yes (via `property_tax_dependence` which varies city-to-city within state) | **Yes** |
| `has_tel_binding_lag1` (state-level binary) | No (0 of 49 states have within-state-year variation; 0 states have time variation) | **NO — rank deficient** |
| `tel_strictness_index_lag1` (state-level continuous) | Residual SD = 0.76 after FE (some within-state variation exists) | **Yes** |
| `property_tax_dependence_lag2` (city-level) | Yes | **Yes** |

## Corrected results

| Variable | TEL-0 Mullins | TEL-1 Binary | TEL-2 Strictness | TEL-3 Components |
|---|---|---|---|---|
| `tel_x_prop_tax_dep` | +0.00091 (0.00063), p=0.15 | — | — | — |
| `has_tel_binding_lag1` | — | **NOT IDENTIFIED** (rank deficient under state FE) | — | **NOT IDENTIFIED** |
| `tel_strictness_index_lag1` | — | — | -0.00071 (0.00085), p=0.40 | — |
| `property_tax_dependence_lag2` | — | — | — | +0.01543 (0.02394), p=0.52 |
| **Dem_Mayor** | -0.0002 (0.0040) | — | -0.0004 (0.0039) | — |
| N | 6,811 | 6,825 | 6,825 | 6,811 |

The spurious TEL-1 coefficient (+0.0371 with nominal "p<0.01") reported earlier reflected statsmodels' pseudo-inverse solution to a rank-deficient system. It is not a real estimate.

## Reading (revised)

- **TEL-0 Mullins (`tel_x_prop_tax_dep`)** is the only TEL specification that is both (a) identified under state FE and (b) produces a positive coefficient. But the coefficient +0.00091 (p=0.15) is **not significant** in the 10-variable PRIMARY spec. The Mullins revenue-substitution story is directionally present but not statistically distinguishable from zero.

- **TEL-1 binary and TEL-3 binary component are not identified.** The initial "TEL-1 +0.037\*\*\*" finding was a pseudo-inverse artifact of rank-deficient OLS. It cannot be used.

- **TEL-2 continuous strictness** is identified (residual SD 0.76) but null and slightly negative. No support for a continuous-TEL mechanism.

- **TEL-3 property-tax-dependence component (identified portion)** is +0.015 (ns). Property-tax dependence alone does not predict green labelling.

- **Dem_Mayor** null in all identified specifications (|β| ≤ 0.0005).

## Implication for main-table choice

If the paper wants a TEL-related variable in the main table and it must be identified under state FE, the options are:

1. **Keep `tel_x_prop_tax_dep`** (Mullins interaction) — identified, directionally positive, but not significant in this sample with the 10-variable PRIMARY. Honest reporting.
2. **Drop TEL from main, retain for robustness** — state FE already absorbs most TEL-related cross-state variation. The interaction is the only form that adds city-level identifying variation. If the result is null, demoting TEL to robustness and documenting the identification issue is cleaner.
3. **Replace state FE with region FE** — loosens identification constraint but weakens the headline. Not recommended for a main table.

My recommendation based on these results: **drop TEL from the main table, retain `tel_x_prop_tax_dep` in a fiscal-robustness column** alongside the fiscal-stress composite. The paper should note the state-level identification problem for the binary TEL indicator explicitly in the methods section.

---

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01. NOT IDENTIFIED = rank-deficient under state FE.
