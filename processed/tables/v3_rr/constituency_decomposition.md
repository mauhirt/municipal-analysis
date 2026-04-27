# Constituency Decomposition: `pres_dem_share` vs `Dem_Mayor` (Task 7)

## Discordant city-years

- `pres_dem > 0.55` but `Dem_Mayor = 0` (Rep mayor in blue city): **1162** (15.5%)
- `pres_dem < 0.45` but `Dem_Mayor = 1` (Dem mayor in red city): **347** (4.6%)
- Total city-years with both non-null: 7514

See `processed/figures/v3_rr/pres_vs_mayor_scatter.png` for the scatter.

## Regression comparison on `Y_self_green`

| Variant | β(Dem_Mayor) | SE | p | β(pres_dem_share) | SE | p | β(interaction) | SE | p | N |
|---|---|---|---|---|---|---|---|---|---|---|
| V1 (pres only) | — | — | — | +0.0596** (0.0265) | | | — | — | — | 6052 |
| V2 (Dem only) | +0.0030 (0.0040) | | | — | — | — | — | — | — | 6052 |
| C3 baseline | -0.0019 (0.0044) | | | +0.0624** (0.0289) | | | — | — | — | 6052 |
| V3 (both+int) | -0.0763** (0.0319) | | | -0.0050 (0.0256) | | | +0.1324** (0.0546) | | | 6052 |

## Reading

- **Interaction null:** No (β = +0.1324, p = 0.015). The interaction is significant — the two variables do NOT operate independently.
- **`pres_dem_share` coefficient stability:** V1 β = +0.0596, V3 β = -0.0050. Unstable — adding the interaction changes the constituency coefficient materially.
- **`Dem_Mayor` in V2 (without pres_dem):** β = +0.0030 (p = 0.450). Still null even without the constituency control — mayoral partisanship has no marginal effect.

* p<0.10, ** p<0.05, *** p<0.01.
