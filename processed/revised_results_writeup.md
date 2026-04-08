# Revised Results: When Do Red and Blue Go Green?

## Mayoral Partisanship and Municipal Green Bond Issuance

*Based on 578 U.S. municipalities, 2013–2025 | N = 6,422 | Preferred spec: state+year FE, city-clustered SEs*

---

## I. The Headline Finding: Partisanship Operates on Credibility, Not Issuance

The central empirical result is a **selective null**. Republican mayors are no less likely than Democratic mayors to issue green bonds (β = −0.002, p = 0.633). They are, however, significantly less likely to invest in **third-party assurance** — the costliest credibility signal available to municipal issuers (β = −0.006, p = 0.033).

This pattern is stable across specifications. Under city+year fixed effects, the assurance gap persists at marginal significance (β = −0.004, p = 0.099). It survives subsample restrictions (pre-2020: p = 0.093; drop top-5 cities: p = 0.038), continuous party measurement (prob_republican: p = 0.052), and the inclusion of CWNS infrastructure controls on the 2015–2025 subsample.

The composition of green bonds among the 113 issuing city-years with known mayor party reinforces this:

| Dimension | D mayors (N=95) | R mayors (N=18) | p (Fisher exact) |
|---|---|---|---|
| Water-only | 51.6% | 83.3% | 0.018** |
| Has non-water category | 48.4% | 16.7% | 0.018** |
| Third-party assurance | 61.1% | 16.7% | 0.001*** |
| ESG framework | 63.2% | 55.6% | 0.601 |

Republican mayors who issue green bonds issue **water-only** bonds without credibility certification. Democratic mayors issue across categories and invest in verification. The partisan gap is not about whether to enter the green bond market — it is about how visibly green to be once there.

---

## II. What Drives Cities into the Green Bond Market

### A. Enforcement compulsion is the primary push factor

Federal environmental enforcement is the strongest and most robust predictor of green bond issuance. Cities with NPDES formal enforcement actions in the prior three years are 1.5 percentage points more likely to self-label a green bond (p = 0.013) and 1.2 percentage points more likely to seek assurance (p = 0.017). This is a large effect against a 1.6% base rate.

Combined sewer overflow events show an even sharper pattern. Overflow at lag-2 predicts self-labelled issuance at β = +0.016 (p < 0.001) and is precisely zero on non-water outcomes (p = 0.889 for non-water, p = 0.169 for clean transportation). This falsification passes cleanly: sewer overflows predict sewer revenue bonds and nothing else.

On the 2015–2025 subsample where the green bond market is established, the enforcement lag structure reveals timing: overflow events become significant at lag-1 (p = 0.053), peak at lag-2 (p < 0.001), and reverse at lag-3 (p < 0.001) — consistent with a 2-year compliance timeline from violation to bond issuance.

### B. The enterprise fund channel

85.8% of green bond dollars are revenue bonds, predominantly water/sewer (59.1% WTRSWR alone). Only 6.5% is GO-backed. This means the relevant fiscal channel is not general fund taxation but enterprise fund user charges.

The variable `charges_to_own_source` — the share of own-source revenue derived from user charges rather than taxes — predicts green bond issuance across all outcomes: Bloomberg (p = 0.031), self-labelled (p = 0.089), assurance (p = 0.003), water-only (p = 0.063). In the tax effort vs. user charges horse race, **user charges win and tax effort is null**:

| Variable | → WTRSWR revenue bond | → Water-only |
|---|---|---|
| charges_to_own_source | p = 0.017** | p = 0.002*** |
| tax_effort_pc | p = 0.167 | p = 0.269 |

Cities whose revenue structure is skewed toward user charges have larger, more autonomous enterprise funds. These funds issue their own revenue bonds secured by charge streams — and those bonds are classified as green.

### C. The TEL → enterprise fund → revenue bond mechanism

Tax and expenditure limitations are strongly associated with green bond issuance on the post-2015 subsample (β = +0.002, p < 0.001 for self-labelled). The mechanism works through the enterprise fund channel, not through taxation:

1. **TEL → higher charge dependence** (p < 0.001): TEL-constrained cities compensate by relying more on enterprise fund user charges.
2. **Charge dependence → WTRSWR revenue bonds** (p = 0.021): cities with charge-heavy revenue structures issue more water revenue bonds.
3. **TEL partly works through charges**: adding `charges_to_own_source` attenuates the TEL coefficient by **41%** on WTRSWR and **31%** on self-labelled.

The remaining TEL effect (59% unmediated) likely captures the general fund squeeze that prevents cross-subsidisation of water infrastructure, forcing enterprise funds to access bond markets independently.

**Important qualification**: TEL is strongly positive on 2015–2025 (p < 0.001) but reverses sign on the full 2013–2025 panel (β = −0.001, p = 0.23). The years 2013–2014 contain 0 and 1 green bonds respectively — essentially a structural zero period before the market existed. The TEL finding should be presented as a post-market-establishment effect.

### D. Revenue structure confirms the financing channel

Three fiscal federalism variables tell a consistent story. Cities with higher vertical fiscal imbalance — spending more than they raise from own sources — issue more green bonds (vfi: β = +0.036, p = 0.049). Its mirror, tax autonomy ratio (taxes/total revenue), is negative (β = −0.041, p = 0.092): cities that *can* self-fund via taxation issue fewer green bonds because they don't need the bond market. Higher debt affordability (existing debt stock relative to revenue) also predicts issuance (β = +0.005, p = 0.058) — cities already active in bond markets are more likely to issue green.

None of these fiscal variables interact with partisanship (0 of 52 tests at p < 0.10). Fiscal structure pushes both parties into the bond market equally.

---

## III. State Institutional Environment

### A. Anti-ESG legislation constrains labelling

The `esg_has_muni_bond_law` variable — states with laws specifically regulating ESG criteria in municipal bond issuance — is negative on self-labelled (β = −0.014, p = 0.019) and marginally on assurance (β = −0.009, p = 0.053). These laws, which emerged after 2020, appear to suppress green labelling directly. The effect is on the self-labelling decision (Level 2), not on infrastructure investment (Level 1: p = 0.163).

### B. State green bond market capacity

The direct effect of state green bond market depth is absorbed by state fixed effects. However, the **interaction with mayoral partisanship** reveals a significant differential:

| Outcome | Cap × Rep_Mayor β | p | FE |
|---|---|---|---|
| Assurance | −0.00073 | 0.009*** | city+year |
| Self-labelled | −0.00076 | 0.076* | city+year |
| Self-labelled | −0.00135 | 0.004*** | state+year |
| Assurance | −0.00113 | 0.003*** | state+year |

As the state green bond market deepens (more cumulative issuance by all issuers — state government, municipalities, authorities), **Democratic mayors increase their issuance but Republican mayors do not**. Market depth is a permissive institutional condition that only translates into green bond issuance when a willing mayor meets available infrastructure.

This is the cleanest evidence for the political economy story: the *opportunity* to issue green bonds is created by material conditions (enforcement, infrastructure need, enterprise fund capacity, market depth). The *choice* to label bonds as green and invest in credibility is where partisanship enters.

---

## IV. What Partisanship Does Not Explain

The 882 tests across five political variable groups (systematic Family 2 analysis) and the 52 fiscal × partisanship interaction tests establish clear boundaries:

- **No partisan gap on the extensive margin**: Bloomberg-observed issuance (p = 0.60), self-labelled (p = 0.63), water-only (p = 0.88), dollar amount (p = 0.62).
- **No partisan gap conditional on fiscal stress**: reserve_ratio × Rep (p = 0.47), debt_service_burden × Rep (p = 0.62), days_cash × Rep (p = 0.38), operating_deficit × Rep (p = 0.71). Fiscal pressure pushes both parties into the bond market equally.
- **No partisan gap conditional on enforcement**: npdes_formal × Rep (p = 0.41 under state+year FE). Enforcement compels compliance regardless of the mayor's party.
- **No partisan differential on TEL effects**: TEL pushes both parties through the enterprise fund channel without partisan differentiation.

---

## V. The Refined Argument

The paper's contribution is a three-level decomposition of municipal green bond issuance:

**Level 1 — Project supply (Bloomberg-observable).** Determined by material conditions: enforcement compulsion, infrastructure need, enterprise fund capacity, city size, and (on the post-2015 panel) TEL-driven revenue structure. Partisanship plays no role. Both D and R mayors issue at the same rate when facing the same economic pressures.

**Level 2 — Green labelling (self-reported).** Weakly constrained by anti-ESG muni bond laws (p = 0.019) but not by partisanship per se. The composition differs: R mayors label only water bonds; D mayors label across categories. But the *rate* of labelling conditional on issuance does not differ.

**Level 3 — Credibility investment (third-party assurance).** This is where partisanship bites. R mayors are 0.6 percentage points less likely to seek assurance (p = 0.033) — a 46% reduction relative to the D-mayor assurance rate of 1.3%. The effect is amplified in states with deeper green bond markets (Cap × Rep: p = 0.009): D mayors in deep-market states invest in credibility; R mayors in the same states do not.

The political economy logic: green bond assurance is costly, visible, and has no direct fiscal benefit — it signals environmental commitment to ESG-aligned investors. For Republican mayors, this signal carries a political cost (constituent backlash, state-level anti-ESG pressure) without a clear electoral benefit. For Democratic mayors, it carries a political benefit (climate-conscious constituency, alignment with party platform). The decision to issue a green bond is driven by pipes and enforcement; the decision to certify it is driven by politics.

### What TEL and enterprise funds add

The TEL finding enriches the Level 1 story with a specific institutional mechanism. States with stringent tax and expenditure limitations push cities toward charge-financed enterprise funds, which access the revenue bond market for water infrastructure. This is not a green choice — it is a fiscal-structural pathway that happens to produce bondable water assets. The channel runs: TEL → tax constraint → enterprise fund autonomy → user-charge-backed revenue bonds → Bloomberg classifies as green.

This mechanism explains why 86% of green bond dollars are revenue bonds and why water/sewer dominates: the fiscal architecture of American municipal finance channels infrastructure investment through enterprise funds and their associated bond markets, regardless of any environmental intent.

### What state capacity adds

The state market depth interaction shows that institutional readiness matters — but asymmetrically. A deeper state green bond market (more cumulative issuance by all issuers) creates a permissive environment: bond counsel familiarity, underwriter experience, investor appetite. Democratic mayors exploit this environment; Republican mayors leave the opportunity on the table. The green premium and reputational benefits of certification are worth the political cost only for mayors whose constituents value environmental commitment.

---

## VI. Summary Table of Key Results

| Variable | → Self-labelled | → Assurance | → Water-only | Note |
|---|---|---|---|---|
| **Rep_Mayor** | −0.002 (p=0.63) | **−0.006 (p=0.033)** | −0.001 (p=0.88) | Selective on credibility |
| npdes_formal_prior3yr | +0.015 (p=0.013) | +0.012 (p=0.017) | +0.008 (p=0.066) | Primary push factor |
| overflow_events_lag2 | +0.016 (p<0.001) | — | +0.016 (p<0.001) | Water-specific |
| log_population_lag2 | +0.023 (p<0.001) | +0.013 (p=0.009) | +0.012 (p<0.001) | Scale |
| esg_has_muni_bond_law | −0.014 (p=0.019) | −0.009 (p=0.053) | — | Anti-ESG chills labelling |
| charges_to_own_source_lag2 | +0.038 (p=0.089) | +0.052 (p=0.003) | +0.029 (p=0.063) | Enterprise fund channel |
| vfi_lag2 | +0.036 (p=0.049) | — | — | Fiscal imbalance → bonds |
| tax_autonomy_ratio_lag2 | −0.041 (p=0.092) | −0.044 (p=0.033) | — | Tax capacity substitutes |
| tel_stringency (2015–25) | +0.002 (p<0.001) | +0.001 (p=0.009) | +0.001 (p<0.001) | Enterprise fund mechanism |
| Cap × Rep_Mayor | −0.001 (p=0.076) | **−0.001 (p=0.009)** | — | D mayors exploit depth |

*Panel: 578 cities, 535 with complete controls, 2013–2025. State+year FE except Cap×Rep (city+year FE). City-clustered standard errors throughout.*
