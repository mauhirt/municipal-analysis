# Third-Party Assurance Robustness Check

**Outcome:** `Y_esg_assurance` (third-party ESG assurance on city green bonds).
**Purpose:** Assess whether the marginal Dem_Mayor +0.004* (p=0.08) finding is robust or fragile.

## Baseline

| Spec | Dem_Mayor | SE | p | N | n+ |
|---|---|---|---|---|---|
| Table 1 PRIMARY + state+year FE | +0.0044 | 0.0025 | 0.080\* | 6,825 | 61 |
| Year FE only (no state FE) | +0.0066 | 0.0021 | 0.002\*\*\* | 6,825 | 61 |
| Drop pres_dem_share | +0.0057 | 0.0025 | 0.020\*\* | 6,825 | 61 |

The finding strengthens substantially without state FE or constituency — indicating it is a **between-state** pattern (Dem mayors are in states where assurance is common), not a within-state mayoral-agency effect.

## Leave-one-state-out

| Dropped state | Dem_Mayor | p | N | n+ |
|---|---|---|---|---|
| California (22 assurance events) | **+0.0031** | **0.239** | 5,786 | 39 |
| Wisconsin (6 events) | +0.0056 | 0.015\*\* | 6,717 | 55 |
| Washington (6 events) | +0.0047 | 0.051\* | 6,657 | 54 |
| Georgia/Arizona (4 events) | +0.0036 | 0.132 | 6,705 | 57 |
| Florida (3 events) | +0.0040 | 0.133 | 6,334 | 58 |

**Dropping California kills the finding.** California accounts for 22 of 61 assurance events (36%). San Francisco alone contributes 10 Dem-mayor assurance city-years; LA contributes 6. The baseline +0.0044\* is a California effect.

## City concentration

Only **33 cities** in the entire 576-city panel ever have a third-party assurance event. The top contributors:

| City | State | Dem-assurance years |
|---|---|---|
| San Francisco | CA | 10 |
| Los Angeles | CA | 6 |
| Milwaukee | WI | 6 |
| Atlanta | GA | 4 |
| Seattle | WA | 3 |
| Tacoma | WA | 3 |
| Minneapolis | MN | 2 |
| Tampa | FL | 2 |

These 8 cities account for 36 of 58 Dem-assurance city-years (62%).

## Conditional on issuing (N=118 issuers)

| Group | Assured | Total | Rate |
|---|---|---|---|
| Dem issuers | 58 | 98 | 59.2% |
| Rep issuers | 3 | 20 | 15.0% |

Fisher exact p < 0.001. But the conditional LPM with `Dem_Mayor + pres_dem_share + log_population` (no FE, N=118) gives Dem_Mayor = +0.37\*\*\* — this is essentially documenting that SF/LA issue high-volume assured bonds, not that Dem partisanship causes assurance procurement.

## Between vs within state decomposition

| Level | Correlation (assurance rate × Dem_Mayor rate) |
|---|---|
| Between-state (state means) | +0.123 |
| Within-state (demeaned) | +0.066 |

Most of the association is between-state (Dem-mayor states are assurance states), not within-state variation.

## Verdict

**Not robust.** The +0.0044\* finding is:
1. Driven by California (drops to +0.003, p=0.24 without it)
2. Concentrated in 8 large coastal Democratic cities
3. A between-state pattern, not within-state mayoral agency
4. Consistent with a **sophistication/scale** story (SF and LA can afford Kestrel verification), not partisan ideology

**Recommendation:** do not report as a partisan finding. If a reviewer asks, the response is: *"Among six credibility dimensions, only third-party assurance showed a marginal positive Dem coefficient (+0.004, p=0.08). That coefficient is not robust to dropping California (β=+0.003, p=0.24), which accounts for 36% of all assurance events. The pattern reflects the concentration of high-volume green issuance in a handful of large coastal cities with sophisticated finance departments, not partisan mayoral agency."*

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01.
