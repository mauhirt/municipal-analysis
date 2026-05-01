# Table 2 Col 9 — Stacked Monotonicity (H2a)

Stacked panel across 8 use-of-proceeds categories, N = 47,776.
Category fixed effects included. State + year FE. State clustering.

Compulsion ordinal: water=4, pollution/transport=3, renew/adapt=2, 
energy-eff=1, green-bldg/natural-res=0.

H2a prediction (with `Dem_Mayor` coding): interaction is **negative** —
the Democratic advantage should shrink in highly-compelled categories.

| Variable | Coefficient |
|---|---|
| `Dem_Mayor` | -0.0018 (0.0012) |
| `compulsion_ord` | -0.0134*** (0.0042) |
| `Dem_Mayor × compulsion_ord` | **+0.0009 (0.0006)** |
| N | 47,776 |
| R² | 0.0269 |

## Binary-compelled variant

| Variable | Coefficient |
|---|---|
| `Dem_Mayor` | -0.0010 (0.0000) |
| `is_compelled` (ord ≥ 3) | -0.0230 (0.0000) |
| `Dem_Mayor × is_compelled` | **+0.0021 (0.0016)** |
| N | 47,776 |

Stars: * p<0.10, ** p<0.05, *** p<0.01.
