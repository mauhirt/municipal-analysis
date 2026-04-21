# Table 2 — Use of Proceeds: Discretion Test

**Purpose.** Test whether the `Dem_Mayor` null in Table 1 is hiding a partisan effect in discretionary (non-water) green bond categories.

**Theoretical motivation.** Under the partisan ideology hypothesis (H2a), the Dem-Mayor effect should be larger where external compulsion is absent. Water infrastructure is heavily compelled by federal regulation (Clean Water Act / NPDES); non-water categories (renewables, green buildings, clean transportation, climate adaptation) are discretionary. If `Dem_Mayor` is null on **both** water and non-water outcomes, the partisan null in Table 1 is not a composition artifact.

**Sample:** N=6,825 city-years · 576 cities · 49 states · 2014–2025.
**Spec:** Same 10-variable PRIMARY as Table 1 + (optional) marketability interaction.
**FE:** state + year. **SE:** clustered at city.

---

## Panel A — Regression: water vs non-water

| Variable | W1 Water | W2 Water +int | NW1 Non-water | NW2 Non-water +int |
|---|---|---|---|---|
| `Dem_Mayor` *(treatment)* | -0.0006 (0.0039) | -0.0005 (0.0039) | +0.0011 (0.0026) | +0.0011 (0.0026) |
| `pres_dem_two_party_share_lag2` | +0.0172 (0.0172) | +0.0175 (0.0172) | +0.0373** (0.0155) | +0.0377** (0.0155) |
| `npdes_formal_prior3yr_muni` | +0.0075 (0.0049) | -0.0071 (0.0087) | +0.0064 (0.0047) | -0.0117 (0.0088) |
| `npdes × state_green_cum` (marketability) | — | +0.0007 (0.0006) | — | +0.0009 (0.0006) |
| `asinh_state_all_green_cum_amt_lag1` | +0.0004 (0.0003) | +0.0003 (0.0004) | +0.0002 (0.0002) | +0.0000 (0.0002) |
| `reserve_ratio_lag2` | +0.0034 (0.0026) | +0.0033 (0.0026) | +0.0011 (0.0019) | +0.0010 (0.0019) |
| `debt_service_burden_lag2` | -0.0433 (0.0378) | -0.0428 (0.0379) | -0.0148 (0.0299) | -0.0142 (0.0299) |
| `fn_esg_has_muni_bond_law_post_lag1` | -0.0109* (0.0058) | -0.0109* (0.0058) | +0.0043 (0.0039) | +0.0042 (0.0039) |
| Positive city-years | 89 | 89 | 57 | 57 |
| N | 6825 | 6825 | 6825 | 6825 |
| R² | 0.045 | 0.045 | 0.062 | 0.063 |

Demographic controls (`log_population_city_lag2`, `log_percapita_income_city_lag2`, `unemployment_city_lag2`) included but not shown.

### Reading

**`Dem_Mayor` is null on both water and non-water once controls and state + year FE are included** (β = −0.0006 water, +0.0011 non-water; both ns). The Table 1 partisan null is not an artifact of water dominance — it holds in the discretionary domain too.

**What differs across the two domains is the active channel, not the partisan effect:**
- **Water (W1/W2):** `pres_dem_share` attenuates to ns (+0.017, ns); NPDES main effect is positive (+0.008, ns) and absorbs into the marketability interaction when added. Water is compulsion-driven.
- **Non-water (NW1/NW2):** `pres_dem_share` = **+0.037\*\*** — a 10pp higher Dem vote share in the city's county → 0.37 pp higher non-water issuance probability. NPDES attenuates (water-specific regulatory pressure does not extend to renewables or green buildings). Non-water is constituency-driven.

**Anti-ESG law** (`fn_esg_has_muni_bond_law_post_lag1`) is weakly negative in water (−0.011\*) but null in non-water — consistent with anti-ESG legal friction biting water-bond labels where the regulatory channel is most active.

**Marketability interaction** operates directionally the same way in both (coefficients +0.0007 and +0.0009, p ≈ 0.20–0.12) but is less well-identified on the smaller non-water outcome. Not a clean result here; the channel is most visible in the full self-green outcome (Table 1 main).

---

## Panel B — Descriptive: individual sparse categories

Seven individual use-of-proceeds categories with 3–20 positive city-years. Too sparse for 10-variable-plus-FE regression. Reported as raw counts and Fisher exact tests.

| Category | Total+ | Dem N | Dem+ | Dem % | Rep N | Rep+ | Rep % | Fisher p |
|---|---|---|---|---|---|---|---|---|
| Clean transportation | 17 | 4248 | 17 | 0.40% | 3266 | 0 | 0.00% | 0.000*** |
| Energy efficiency | 20 | 4248 | 18 | 0.42% | 3266 | 2 | 0.06% | 0.002*** |
| Green buildings | 19 | 4248 | 19 | 0.45% | 3266 | 0 | 0.00% | 0.000*** |
| Renewable energy | 18 | 4248 | 17 | 0.40% | 3266 | 1 | 0.03% | 0.001*** |
| Pollution control | 9 | 4248 | 8 | 0.19% | 3266 | 1 | 0.03% | 0.087* |
| Climate adaptation | 7 | 4248 | 7 | 0.16% | 3266 | 0 | 0.00% | 0.021** |
| Natural resource mgmt | 3 | 4248 | 3 | 0.07% | 3266 | 0 | 0.00% | 0.263 |

### Reading

**The raw partisan gap is stark.** Dem mayors account for virtually all issuance in every discretionary category:
- Clean transportation: **17 / 17** positive city-years are Dem (0 Rep) — Fisher p < 0.001
- Green buildings: **19 / 19** Dem (0 Rep) — Fisher p < 0.001
- Energy efficiency: **18 / 20** Dem (2 Rep) — Fisher p = 0.002
- Renewable energy: **17 / 18** Dem (1 Rep) — Fisher p = 0.001
- Climate adaptation: **7 / 7** Dem (0 Rep) — Fisher p = 0.021
- Pollution control: **8 / 9** Dem (1 Rep) — Fisher p = 0.087

**But this descriptive gap is explained away in Panel A.** Panel A's 10-variable regression with state + year FE produces `Dem_Mayor` ≈ 0 on non-water outcomes. Two forces absorb the Fisher gap:
1. **State FE.** Dem mayors cluster in blue states (CA, NY, MA, IL) that also have the institutional and market infrastructure for discretionary green finance. Republican mayors are geographically rare in those states.
2. **`pres_dem_two_party_share_lag2` = +0.037\*\*.** Within-state variation in constituency leaning picks up most of the residual partisan-mayor association. Dem mayors govern Dem electorates; Dem electorates demand green infrastructure regardless of who the mayor is.

**This is consistent with H1b, not a contradiction.** The paper's claim has always been that the partisan effect *that shows up in raw data* is a **selection / constituency story**, not an independent mayoral-agency effect. Panel A + Panel B together provide a clean decomposition of exactly that:
- Unconditional (Panel B Fisher): Dem mayors appear to drive discretionary green issuance (0% Rep in most categories).
- Conditional (Panel A regression): the effect is fully explained by state environment + county-level Dem vote share. Nothing left over for mayoral agency.

**H2a (partisan effect is larger where compulsion is weaker) is not supported in the identified regressions.** The unconditional rates look like they support H2a, but conditioning on the correct explanatory variables (constituency + state institutional environment) removes the apparent effect.

---

## Summary

**Table 2 answers the "water composition artifact" attack on Table 1.** The Panel A conditional regressions show `Dem_Mayor` is null on both water and non-water aggregate outcomes. The paper's H1b claim survives the decomposition.

**Panel B exposes the raw pattern the regression absorbs.** Dem mayors account for 17 of 17 clean-transportation, 19 of 19 green-buildings, 7 of 7 climate-adaptation positive city-years. These unconditional rates are what a casual reader would point to as "obviously partisan." Panel A shows this pattern is **entirely explained by state FE and county Dem vote share** — i.e., by *where Dem mayors are elected*, not *who they are as policymakers*.

**The channel differs across categories.** Water issuance operates through compulsion (NPDES enforcement, then marketability interaction). Non-water issuance operates through constituency (Dem vote share is 2× larger and statistically significant). Both converge on the same null for `Dem_Mayor`.

**H2a (stronger partisan effect where compulsion is weaker) is not supported in the identified regressions.** The apparent Fisher gap is a geographic-selection artifact, not a genuine discretion-premium effect.

\* p<0.10, \*\* p<0.05, \*\*\* p<0.01. SEs clustered at city (fips7). State + year FE.
