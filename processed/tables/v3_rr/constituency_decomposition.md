# Constituency Decomposition: `pres_dem_share` vs `Dem_Mayor` (Task 7)

## Discordant city-years

- `pres_dem > 0.55` but `Dem_Mayor = 0` (Rep mayor in blue city): **1126** (15.3%)
- `pres_dem < 0.45` but `Dem_Mayor = 1` (Dem mayor in red city): **332** (4.5%)
- Total city-years with both non-null: 7364

See `processed/figures/v3_rr/pres_vs_mayor_scatter.png` for the scatter.

## Regression comparison on `Y_self_green`

| Variant | β(Dem_Mayor) | SE | p | β(pres_dem_share) | SE | p | β(interaction) | SE | p | N |
|---|---|---|---|---|---|---|---|---|---|---|
| V1 (pres only) | — | — | — | +0.0585** (0.0251) | | | — | — | — | 6039 |
| V2 (Dem only) | +0.0029 (0.0039) | | | — | — | — | — | — | — | 5962 |
| C3 baseline | -0.0019 (0.0043) | | | +0.0593** (0.0280) | | | — | — | — | 5962 |
| V3 (both+int) | -0.0792** (0.0323) | | | -0.0113 (0.0268) | | | +0.1377** (0.0554) | | | 5962 |

## Reading

- **Interaction null:** No (β = +0.1377, p = 0.013). The interaction is significant — the two variables do NOT operate independently.
- **`pres_dem_share` coefficient stability:** V1 β = +0.0585, V3 β = -0.0113. Unstable — adding the interaction changes the constituency coefficient materially.
- **`Dem_Mayor` in V2 (without pres_dem):** β = +0.0029 (p = 0.461). Still null even without the constituency control — mayoral partisanship has no marginal effect.

* p<0.10, ** p<0.05, *** p<0.01.
