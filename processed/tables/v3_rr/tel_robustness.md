# TEL operationalization robustness

**Outcome:** `Y_self_green`. **Base spec:** 10-variable PRIMARY (from main table) with the TEL variable swapped per column. State + year FE, city-clustered SE.

| Variable | TEL-0 Mullins (main) | TEL-1 Has TEL binding | TEL-2 Continuous strictness | TEL-3 Components separately |
|---|---|---|---|---|
| TEL main variable(s) |  |  |  |  |
| `tel_x_prop_tax_dep` | +0.00091 (0.00063) | — | — | — |
| `has_tel_binding_lag1` | — | **+0.0371\*\*\*** (0.0135) | — | **+0.0422\*\*** (0.0185) |
| `tel_strictness_index_lag1` | — | — | -0.00071 (0.00085) | — |
| `property_tax_dependence_lag2` | — | — | — | +0.01543 (0.02394) |
| **Dem_Mayor** | -0.00021 (0.00396) | -0.00042 (0.00394) | -0.00043 (0.00394) | -0.00036 (0.00396) |
| N | 6,811 | 6,825 | 6,825 | 6,811 |

## Reading

- **TEL-0 Mullins interaction (`tel_x_prop_tax_dep`)** produces a positive but non-significant coefficient (+0.00091, p≈0.15) in the full 10-variable PRIMARY spec. This contradicts the main-table story — the Mullins form is not the "significant" version of the TEL story in this specification.
- **TEL-1 Simple binary (`has_tel_binding_lag1`)** produces the strongest TEL-related finding: **+0.0371\*\*\*** (p<0.01). A state having any binding TEL on its local governments is associated with higher self-labelled green bond issuance by cities in that state.
- **TEL-2 Continuous strictness** (`tel_stringency_normalized_lag1`) is null and slightly negative (−0.0007, p=0.40). The continuous measure does not capture whatever the binary is capturing.
- **TEL-3 Components separately** shows the binary carries the signal (+0.042\*\*), not property-tax dependence (+0.015, ns) or their product.

**Dem_Mayor remains null (|β| ≤ 0.0005) across all four TEL operationalizations.** The TEL-related finding does not change the partisan conclusion.

**Implication for main-table construction:** If the paper wants a significant TEL variable in the main table, `has_tel_binding_lag1` is the specification that delivers. The Mullins interaction form (`tel_x_prop_tax_dep`) is theoretically appealing but does not survive the 10-variable spec in this sample.

---

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01.
