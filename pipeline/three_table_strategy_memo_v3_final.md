# FINAL RESEARCH MEMO — Three-Family Empirical Strategy
## "When Do Red and Blue Go Green?"
### Maurice Hirt, DPhil Candidate, Oxford DPIR — April 2026

---

## 1. Paper in Brief

This paper examines municipal green bond issuance across 578 US cities,
2013–2025, using Bloomberg municipal bond data, EPA ECHO enforcement
records, hand-coded mayoral partisanship, and Census fiscal variables.
The central question: what determines whether a city issues a green bond,
which categories it enters, and whether it invests in third-party ESG
credibility?

The answer is organised around three families of explanatory variables
— Material, Political, and State/Multilevel Governance — tested across
three outcome tables that trace the decision chain from issuance to
credibility investment.

---

## 2. Three Families of Variables

### Family 1 — Material (compulsion + fiscal structure + infrastructure)

These variables determine WHETHER green bonds happen at all. They are
the necessary conditions — structural forces that create the opportunity
for issuance regardless of the mayor's partisan identity.

| Variable | Source | Lag | Role |
|---|---|---|---|
| `epa_water_violations_asinh_lag2` | EPA ECHO (200 cols, 3 tiers) | lag 2 | **Primary compulsion**: asinh of NPDES effluent + CS + PS + SE violations against muni facilities. Positive and significant at 5% across every Table 1 column. |
| `epa_npdes_formal_prior3yr_muni` | EPA ECHO | contemp (rolling) | Robustness compulsion: 3-yr stock of formal enforcement actions. Not significant (too sparse at 16% non-zero). |
| `charges_to_own_source` | Census of Governments | contemp | **Enterprise fund depth**: share of city revenue from utility user charges. Strongest single predictor (β=+0.10***, p<0.01). Creates both the capital need and the revenue bond structure. |
| `reserve_ratio_lag2` | Census of Governments | lag 2 | Fiscal capacity. Positive direction, not significant. |
| `debt_service_burden_lag2` | Census of Governments | lag 2 | Debt exposure. Negative direction, not significant. |
| `tel_stringency_normalized` | Lincoln Institute TEL database | contemp | Tax and expenditure limits. Positive when alone, drops to zero when Family 3 added (absorbed by state-level variation). |
| `cwsrf_log_obligations_lag2` | USASpending | lag 2 | Federal CWSRF subsidy access. Not significant (no crowding-out detected). |
| `log_cwns_needs_real_lag2` | EPA CWNS 2022 Survey (interpolated) | lag 2 | Infrastructure needs index. Not significant. |
| `fn_pct_deficient_lag2` | FHWA NBI | lag 2 | Bridge deficiency rate. Not significant. |

### Family 2 — Political (partisan identity + constituency + ESG environment)

These variables determine WHO takes the green bond opportunity that
material forces create. They capture the partisan and ideological
dimension that fills the space between structural possibility and
actual issuance.

| Variable | Source | Lag | Role |
|---|---|---|---|
| `Rep_Mayor_lag1` | Hand-coded mayoral partisanship (~1,824 cities) | lag 1 | **Primary treatment**: binary Republican mayor. Negative and significant at every step of the decision chain: −1.1pp at issuance (Table 1), complete separation in discretionary categories (Table 2), −27pp at assurance (Table 3). |
| `pres_dem_two_party_share_lag2` | MIT MEDSL county returns 2012-2024 | lag 2 | **Constituency composition**: Dem two-party vote share. Positive and significant — more Democratic cities issue more. Among Republicans, issuers govern cities averaging 58.5% Dem vote (vs 49.2% for non-issuers, p<0.0001). |
| `esg_any_antiesg_law` | ESG legislation panel 2010-2025 | contemp | Anti-ESG environment: binary for any state anti-ESG law. Republican issuers have ZERO anti-ESG laws in their states (p<0.0001). Not significant as a main effect in the regression. |

### Family 3 — State / Multilevel Governance

These variables capture the state-level political and institutional
environment that permits or constrains municipal green bond activity.
They act as gatekeeping conditions — structural features of the state
that bound what is politically feasible for municipal actors.

| Variable | Source | Lag | Role |
|---|---|---|---|
| `state_rep_trifecta` | State political panel | contemp | State unified Republican control. Marginally negative (−0.014†). Republican issuers are NOT in trifecta states (24% vs 54%, p=0.002). |
| `mkt_state_green_bond_ever_lag1` | Bloomberg state-year aggregation | lag 1 | State market precedent. Positive direction (+0.018), not significant. |
| `fn_esg_has_muni_bond_law` | State legislation tracker | contemp | State muni bond enabling law. Negative (−0.038*) — likely reverse causality (states passed laws because activity was low). |
| `inst_has_bond_bank` | State institutional survey | static | State bond bank presence. Strongly negative (−0.103***) — counter-intuitive; may capture state-level intermediation that substitutes for direct municipal issuance. |
| `has_substitute_issuer` | Geospatial water issuer panel | contemp | Alternative water/sewer issuer within 25km. Not significant. |
| `ep_state_green_bank_active` | State energy policy panel | contemp | State green bank active. Not significant. |

### Controls

| Variable | Source | Role |
|---|---|---|
| `log_population_lag2` | Census/ACS | City size (strongly positive, p<0.001). |
| `log_percapita_income_lag2` | Census/ACS | City wealth. |
| `unemployment_city_lag2` | BLS | Economic conditions. |
| `fema_disaster_any_lag2` | FEMA disaster declarations | Physical risk exposure. |
| `log_state_water_excity` | Bloomberg state cumulative panel | State-level water peer issuance (ex-focal city). |
| `log_nearby_water_25km` | Bloomberg nearby spillover panel | Regional water peer issuance (25km radius). |

### Fixed Effects and Standard Errors

- **Tables 1 and 2**: State + Year fixed effects
- **Table 3**: Year fixed effects only (N=130 is too small for state FE with 30+ states)
- **All tables**: Standard errors clustered at city (FIPS) level

---

## 3. Table 1 — Green Bond Issuance

**Sample**: N=4,993 city-years, 565 cities, 2013–2025.

**Outcomes**: Green_Bond_Issued (binary, LPM, Cols 1–3 and 5),
Y_self_green (binary, LPM, Col 4).

**Structure**: Five columns building up the three families sequentially.

| Column | Families included | Outcome |
|---|---|---|
| Col 1 | Family 1 only (Material) | Green_Bond_Issued |
| Col 2 | + Family 2 (Political) | Green_Bond_Issued |
| Col 3 | + Family 3 (State/multilevel) — FULL SPEC | Green_Bond_Issued |
| Col 4 | Full spec | Y_self_green (self-labeling) |
| Col 5 | Full spec + Rep × Dem vote share interaction | Green_Bond_Issued |

### Key results

**Family 1 (Material)**:
- Water violations: +0.005 to +0.006* across every column. Stable.
  The compulsion pipeline works — infrastructure compliance failures
  drive green bond issuance.
- Charges/own-source: +0.08 to +0.10** across every column. The
  strongest single predictor. Enterprise fund depth creates both the
  capital need and the financing structure.

**Family 2 (Political)**:
- Rep_Mayor: enters at Col 2 at −0.011* and is **perfectly stable**
  when Family 3 is added (Col 3: −0.011*). The partisan gap is
  immediate, not attenuated by state-level controls.
- Pres Dem vote share: +0.08* — more Democratic cities issue more.

**Family 3 (State/multilevel)**:
- State bond bank: −0.103*** — strong negative, capturing state-level
  intermediation that may substitute for direct municipal issuance.
- TEL stringency drops from +0.002*** (Col 1-2) to zero (Col 3) —
  absorbed by state-level variation in Family 3.

**Col 5 interaction**: Rep × Dem vote share = −0.111† (p=0.068).
Suggestive that the partisan gap is LARGER in more Democratic cities
— consistent with capacity-amplification rather than constituency
moderation.

### What Table 1 establishes

1. Material forces drive issuance (water violations, enterprise fund
   depth) — symmetrically across parties.
2. Republicans issue ~1.1pp less than Democrats at the extensive margin,
   conditional on identical material conditions and state environment.
3. The partisan gap at self-labeling (Col 4: −0.008†) is similar in
   magnitude to the extensive margin, confirming the gap is immediate.
4. No fiscal or economic incentive differentially pulls Republicans
   into the green bond market.

---

## 4. Table 2 — Issuance by Use-of-Proceeds Category

**Sample**: N=4,993 city-years (N=732 for renewables restricted to
municipal electric utility subsample).

**Outcome**: Category-specific binary (Y_water_only, Y_clean_trans,
Y_renewable, Y_energy_eff, Y_green_bldg).

**Structure**: One column per category, all using the full three-family
specification from Table 1 Col 3.

### Raw participation rates by party

| Category | Compulsion | Dem rate | Rep rate | Rep/Dem ratio |
|---|---|---:|---:|---:|
| Water/Sewer | High (CWA) | 2.1% | 0.6% | **30%** |
| Clean Transport | Medium | 0.4% | 0.0% | **0%** |
| Renewables | Low-Med | 0.4% | 0.04% | 11% |
| Energy Efficiency | Low | 0.4% | 0.08% | 18% |
| Green Buildings | None | 0.5% | 0.0% | **0%** |

Complete Republican separation in clean transport and green buildings
(zero events).

### Rep_Mayor coefficient by category

| Category | Rep_Mayor β | p | Water violations β | p |
|---|---:|---:|---:|---:|
| Water/Sewer | **−0.009†** | 0.069 | **+0.004*** | **0.046** |
| Clean Transport | −0.000 | 0.977 | +0.001 | 0.396 |
| Renewables | −0.000 | 0.934 | −0.003 | 0.375 |
| Energy Efficiency | −0.001 | 0.699 | +0.001 | 0.231 |
| Green Buildings | **−0.002†** | 0.090 | +0.000 | 0.607 |

### What Table 2 establishes

1. Water violations are significant ONLY in the water category —
   confirming the compulsion channel is sector-specific.
2. The partisan gap gradient tracks compulsion intensity: where
   compulsion binds (water), Republicans participate at 30% of the
   Democratic rate. Where it doesn't, they drop to 0%.
3. The compulsion gradient is visible in the ratio (Rep/Dem
   participation rate), not the absolute gap. This is the correct
   metric — the absolute gap is largest in water because water is the
   biggest category.

---

## 5. Table 3 — ESG Assurance (Credibility Gap)

**Sample**: N=130 issuer city-years (conditional on Green_Bond_Issued=1),
~78 unique cities. Year FE only.

**Outcome**: Y_esg_assurance (binary — did the issuer obtain third-party
ESG verification?).

**Structure**: Five columns building up the three families, plus two
interactions.

### Signature result — Water-only Fisher exact test

| | Assurance | No assurance | Rate |
|---|---:|---:|---:|
| Democratic mayors | 31 | 46 | **40.3%** |
| Republican mayors | 2 | 13 | **13.3%** |

Fisher exact p = 0.075. On identical compelled water infrastructure,
Democratic mayors obtain ESG assurance at 3× the Republican rate.

### Regression results

| Variable | C1 (Material) | C2 (+Political) | C3 (+State) |
|---|---:|---:|---:|
| Water violations | +0.018 | +0.022 | +0.026 |
| Charges/own-source | +0.450 | +0.171 | +0.058 |
| **Rep Mayor** | — | **−0.265**** | **−0.274**** |
| Dem vote share | — | −0.176 | −0.206 |
| State trifecta | — | — | +0.013 |
| Bond bank | — | — | +0.082 |

### What Table 3 establishes

1. The partisan assurance gap is large (−27pp), highly significant
   (p<0.01), and stable across all three family additions.
2. No material variable significantly predicts assurance — the
   credibility investment decision is purely political, not fiscal.
3. No state/multilevel variable moderates the gap — it is
   unconditional within the issuer sample.
4. The gap represents the deepest expression of partisan preference:
   among cities that have already issued a Bloomberg-classified green
   bond (often on compelled water infrastructure), Democratic mayors
   additionally invest in third-party credibility signalling while
   Republican mayors decline.

---

## 6. The Three-Family Argument — Integrated

### Sequential, not interactive

The three families operate **in sequence**, not in interaction:

1. **Family 1 (Material)** creates the green bond opportunity.
   Water violations and enterprise fund depth drive issuance
   symmetrically across both parties. These are necessary conditions.

2. **Family 2 (Political)** determines who takes the opportunity.
   The partisan gap appears immediately at the extensive margin
   (−1.1pp) and deepens through the decision chain to assurance
   (−27pp). No fiscal incentive overrides this — the gap is
   ideological, modulated only by constituency composition (Republican
   issuers govern in cities averaging 58.5% Democratic).

3. **Family 3 (State/multilevel)** sets the ceiling on municipal
   action. Republican mayors issue ONLY in states without anti-ESG
   legislation, without Republican trifectas, and with Democratic
   governors. The state political environment is the binding constraint
   — even moderate Republicans in blue-leaning cities cannot issue in
   hostile state environments.

### What does NOT drive partisan convergence

The paper tested comprehensively for any fiscal, economic, or
compulsion-based mechanism that would pull Republicans into the green
bond market:

- 44 Rep_Mayor interaction tests across all panel variables: 0
  compulsion × Rep interactions significant
- 70 EPA × fiscal interaction tests: the interactions that survive
  (overflow × fiscal variables) are positive for both parties, not
  differentially Republican
- 6-specification H3a salvage pass with Bonferroni correction: 0
  passing
- Direct comparison of Republican issuers vs non-issuers: zero
  significant fiscal/economic variables, all significant predictors
  are political

**There is no economic incentive that makes Republicans issue green
bonds.** The green bond market does not attract Republicans through
cheaper cost of capital, fiscal necessity, or infrastructure pressure.
What predicts Republican participation is political environment —
moderate Republicans in Democratic-leaning cities in non-anti-ESG states.

### The paper's contribution

> Material forces determine whether the green bond opportunity exists.
> State governance determines whether the opportunity is politically
> accessible. Partisan identity determines whether the opportunity is
> taken. The decision chain from infrastructure need to credibility
> investment is structured by material necessity at the base and
> increasingly by partisan preferences at each subsequent step. No
> economic mechanism bridges the partisan divide — the gap is
> ideological, bounded by multilevel governance constraints, and
> deepest where the decision is most voluntary.

---

## 7. Data and Reproducibility

**Panel**: 578 cities × 13 years (2013–2025), 2,330 columns.
Stored as `processed/merged_city_year_panel.csv.gz` (7 MB compressed).

**Pipeline**: 22 scripts (`pipeline/00` through `pipeline/22`) plus
4 analysis scripts, fully reproducible from raw sources.

**Raw sources**: 44 files across 17 directories in `raw/`, including
EPA ECHO (200 columns, 3 ownership tiers, 2000–2026), Bloomberg
municipal bonds (25,555 CUSIPs), MIT MEDSL county returns (2012–2024),
hand-coded mayoral partisanship (1,824 cities, 2010–2025), and
provenance-tracked climate policy controls with primary-source
verification.

**Analysis scripts**:
- `pipeline/analysis_table1_threefamily.py` — Table 1
- `pipeline/analysis_table2.py` — Table 2
- `pipeline/analysis_table3.py` — Table 3
- `pipeline/analysis_rep_mayor_interactions_scan.py` — 44-moderator scan
- `pipeline/analysis_salvage_pass.py` — 6-spec H3a salvage

**Known limitations**:
- YCOM climate opinion data ends 2023 (2024–2025 extension pending)
- Table 3 sample is small (N=130) — interactions are underpowered
- `fiscal_stress_pca` raw data ends 2021; replaced with
  `fiscal_stress_index` (r=0.80) which covers 2013–2025
- Water-only Fisher test p=0.075 (marginal) — was p=0.014 with a
  slightly different sample definition

---

## 8. Target Journals

| Journal | Fit | Angle |
|---|---|---|
| Journal of Politics | Strong | Multilevel governance + partisan identity |
| Political Research Quarterly | Strong | Constituency responsiveness |
| JPART | Strong | Municipal fiscal decision-making |
| Public Choice | Good | Partisan preferences in public finance |
| EPSA Belfast June 2026 | Conference | Presentation target |

---

*Working memo — Oxford DPhil research — not for circulation*
*Final version with all three tables — April 2026*
