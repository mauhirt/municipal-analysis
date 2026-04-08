# Ind_Mayor Implementation Note

## Cities Recovered

| City | State | FIPS | I-years | Mechanism |
|---|---|---|---|---|
| **Oak Park** | **IL** | **1754885** | **2013–2025 (all 13)** | **Previously dropped; now recovered with Ind_Mayor=1** |
| **Bowie** | **MD** | **2408775** | **2013–2025 (all 13)** | **Reclassification to D reversed; now Ind_Mayor=1** |

12 additional cities already in the panel now contribute their I-coded years (previously dropped as NaN):
Antioch CA (1yr), Cathedral City CA (1yr), Encinitas CA (2yr), Gilroy CA (1yr), Des Plaines IL (8yr), Waukegan IL (4yr), Quincy MA (2yr), Waltham MA (11yr), Sterling Heights MI (4yr), Plymouth MN (7yr), Syracuse NY (8yr), Elyria OH (4yr).

## New Sample Size

| Metric | Before | After | Change |
|---|---|---|---|
| Cities | 573 | **574** | +1 (Oak Park) |
| City-year obs | 6,941 | **7,004** | +63 |
| Ind_Mayor=1 city-years in regression | 0 | **69** (12 cities) | New |

Bowie was already in the panel (counted among 573) but is now coded correctly as Ind_Mayor=1 rather than the manual D reclassification.

## Remaining 4 Dropped Cities

| City | State | FIPS | Reason |
|---|---|---|---|
| Monterey Park | CA | 648914 | Council-manager, not in raw mayor file at all |
| Pico Rivera | CA | 656924 | Council-manager, not in raw mayor file at all |
| Woodland | CA | 686328 | Council-manager, not in raw mayor file at all |
| Edison | NJ | 3420260 | NJ township, no Census data |

## Coefficient Comparison

| DV | Metric | Without Ind_Mayor (573 cities) | With Ind_Mayor (574 cities) |
|---|---|---|---|
| **Y_esg_assurance** | **Rep_Mayor β** | **−0.00581, p=0.023** | **−0.00578, p=0.023** |
| Y_esg_assurance | Ind_Mayor β | — | −0.00332, p=0.440 |
| Y_esg_assurance | N | 6,941 | 7,004 |
| Y_self_green | Rep_Mayor β | −0.00166, p=0.667 | −0.00161, p=0.676 |
| Y_self_green | Ind_Mayor β | — | −0.00491, p=0.390 |
| Green_Bond_Issued | Rep_Mayor β | −0.00233, p=0.583 | −0.00249, p=0.565 |
| Green_Bond_Issued | Ind_Mayor β | — | −0.00665, p=0.314 |

All Rep_Mayor coefficients stable within 0.1 SE. The headline assurance result is unchanged at p=0.023.

## Sanity Check: Ind_Mayor Power

69 city-years with Ind_Mayor=1 from 12 cities. This exceeds the 20 city-year threshold. However, the coefficient is estimated off a small number of independent-mayor cities, most of which (Bowie, Waltham, Oak Park) lean heavily Democratic (prob_republican ≈ 0). The Ind_Mayor coefficient on assurance (β=−0.003, p=0.44) is negative but noisy — consistent with independent mayors behaving like Democrats on this margin, but underpowered.

## Continuous Robustness

`prob_republican` on the expanded sample (N=6,942): β=−0.007, p=0.016 on assurance (stable from prior p=0.017). This specification is unchanged by the Ind_Mayor addition since it already accommodates intermediacy.

## Bowie MD Reclassification Reversal

The prior D reclassification of Bowie MD (FIPS 2408775) has been reversed. The raw mayor_party.csv retains the original `mayor_pid='I'` coding. Bowie is now handled via `Ind_Mayor=1` for all 2013–2025 years, with `Rep_Mayor=0` (Democrats are the omitted baseline, and Bowie's mayor has prob_democrat=1.0).
