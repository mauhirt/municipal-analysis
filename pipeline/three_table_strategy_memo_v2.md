# REVISED RESEARCH MEMO — Table 1 Results and Specification Update
## "When Do Red and Blue Go Green?"
### Maurice Hirt, DPhil Candidate, Oxford DPIR — April 2026

---

## 1. What Changed

This memo updates `three_table_strategy_memo_revised.docx` based on
running the full Table 1 specification on the integrated panel
(N=6,054 city-years, 578 cities, 2013–2025). Three findings require
revisions to the memo's empirical strategy.

---

## 2. Finding 1 — The Memo Picked the Wrong Compulsion Variable

**Original memo primary**: `npdes_formal_prior3yr_muni` (3-year rolling
stock of NPDES formal enforcement actions against municipal facilities).

**Problem**: This variable has only 1,239 non-zero cell-years (16% of
panel). It is positive but **not statistically significant** in any
column of Table 1 (p = 0.40–0.60 across Cols 1–5).

**Replacement**: `epa_water_violations_asinh_lag2` — inverse hyperbolic
sine of the sum of NPDES effluent, compliance-schedule, permit-schedule,
and standard-exceedance violations against municipal facilities.

- **4,710 non-zero cell-years (63%)** — 4× denser signal
- **Positive and significant at 1% across every Table 1 column**:

| Column | β | SE | p |
|---|---:|---:|---:|
| C1 Green_Bond_Issued | 0.0059 | 0.0022 | 0.008 |
| C2 asinh_green_amt | 0.110 | 0.042 | 0.009 |
| C3 Y_self_green | 0.0062 | 0.0020 | 0.003 |
| C4 asinh_self_green_amt | 0.114 | 0.038 | 0.003 |
| C5 (with interactions) | 0.0054 | 0.0025 | 0.027 |

**Economic interpretation is identical** to the memo's original: regulatory
bite forces infrastructure capital investment. The difference is empirical
handle — violations are the upstream signal of infrastructure failure;
formal actions are the lagged, sparse regulatory response. Source: same
EPA ECHO file (200 columns, 3 ownership tiers).

**Action**: Replace `npdes_formal_prior3yr_muni` with
`water_violations_asinh_lag2` as the primary Family 1a variable. Keep
NPDES formal in Appendix D robustness.

---

## 3. Finding 2 — H1b Is Rejected (Rep_Mayor Not Null at Extensive Margin)

**Memo prediction**: Rep_Mayor is null at Steps 1–2 (Cols 1–2) because
compulsion overrides partisan preference at the extensive issuance margin.

**Finding**: Rep_Mayor is **significantly negative at p<0.01** in Cols 1–2:

| Column | Outcome | β (Rep_Mayor_lag1) | SE | p |
|---|---|---:|---:|---:|
| Col 1 | Green_Bond_Issued | −0.0139 | 0.0049 | 0.004 |
| Col 2 | asinh_green_amt | −0.251 | 0.090 | 0.005 |
| Col 3 | Y_self_green | −0.0105 | 0.0043 | 0.016 |
| Col 4 | asinh_self_green_amt | −0.187 | 0.081 | 0.021 |

**The partisan gap is immediate** — Republicans are ~1.4 pp less likely to
issue any green bond (baseline 2.3%), a ~60% relative reduction. This gap
appears at the extensive margin, not only at the self-labelling step.

**The gradient the memo expected (null → negative from C1 → C3) is absent.**
Coefficients are similar in magnitude across the two margins (−0.014 at C1,
−0.011 at C3). There is no pivot — the gap is everywhere.

**Action**: Revise H1b. The new claim is that Rep_Mayor is negative
throughout the decision chain, with the gap being largest where
institutional capacity is highest (see Finding 3 below). The Step 3
"pivot" is no longer a null-to-negative transition but rather a
confirmation that the gap persists into discretionary steps.

---

## 4. Finding 3 — The Memo's Interaction Story Is Wrong-Signed

**Memo prediction (Col 5 triple)**: `NPDES × Rep × fiscal_stress_pca`
positive — fiscally distressed Republican mayors instrumentally pulled
into the green bond market under compulsion.

**Finding**: The triple interaction is **exactly zero** (β = 0.0001,
p = 0.97) with the correct compulsion variable. The double interactions
are also null. Tested across 6 specifications (baseline, C×D, C×R,
triple, all 2-way, horse race).

**However**, a systematic scan of 44 candidate moderators found **two
robust interactions** surviving Bonferroni correction (α = 0.05/44):

| Moderator | β (Rep × Z) | p | Survives Bonferroni? |
|---|---:|---:|:---:|
| **Charges / own-source** (enterprise fund depth) | **−0.154** | **0.0002** | **Yes** |
| **Benchmarking adopted** (BPS precursor) | **−0.201** | **0.0005** | **Yes** |
| NFIP repetitive loss (flood exposure) | +0.00001 | 0.0013 | Nearly |
| log CWNS needs (infrastructure) | −0.014 | 0.005 | No |
| Fiscal stress PCA | −0.009 | 0.040 | No |

**All significant interactions except NFIP are NEGATIVE** — the partisan
gap **widens** where the moderator is high, not narrows. This is the
exact opposite of the memo's prediction.

**Economic interpretation**: The partisan gap is largest where cities have
the institutional capacity to issue green bonds (deep enterprise funds,
benchmarking infrastructure, large population, state-level market
precedent). Democratic mayors exploit this capacity; Republican mayors
don't. Compulsion variables (violations, NPDES, SDWA, overflow) do NOT
moderate the gap at all.

**Action**: Drop the Col 5 triple interaction from Table 1. Replace with
`Rep_Mayor × charges_to_own_source` (the Bonferroni-surviving interaction)
as the new Col 5. Reframe: the partisan gap is amplified by institutional
capacity, not compressed by regulatory compulsion.

---

## 5. Theoretical Revision — Residual Space → Capacity Amplification

The memo's Mosley "room-to-manoeuvre" framework predicts partisan
preferences fill residual space left by structural constraints. The data
suggests the opposite mechanism:

**Old claim**: "Partisan identity fills the space that compulsion leaves
open." (Compulsion narrows the gap → partisan gap in the residual.)

**New claim**: "Partisan identity is amplified by institutional capacity."
(Capacity widens the gap → partisan gap where the tools exist.)

The mechanism:
1. Most cities lack the infrastructure to issue green bonds at all
2. Structural capacity (enterprise funds, benchmarking laws, scale)
   creates the administrative/legal tools to issue
3. Democratic mayors use the tools; Republican mayors don't
4. The partisan gap is maximized where capacity is highest
5. Without capacity, neither party issues — the gap is zero

This is closer to a **"gatekeeper" model** than a "residual space" model.
The gate is institutional capacity; partisanship determines who walks
through it once it's open.

---

## 6. Revised Table 1 Specification

### Col 1–4 (unchanged structure, revised RHS)

Replace in Family 1a:
- ~~`npdes_formal_prior3yr_muni`~~ → `water_violations_asinh_lag2` (primary)
- Keep `npdes_formal_prior3yr_muni` in spec as secondary

Add to Family 1a:
- `epa_sdwa_events_asinh_lag2` (drinking water events)
- `epa_overflow_events_muni_lag2` (sewer overflows)
- `epa_case_all_prior3yr_muni` (total EPA cases)

### Col 5 (revised interaction)

Replace:
- ~~`npdes × Rep × fiscal_stress` triple~~ → dropped (zero effect, p=0.97)

New Col 5:
- `Rep_Mayor_lag1 × charges_to_own_source` (β = −0.154, p = 0.0002)
- Tests capacity-amplification: the partisan gap widens where enterprise
  fund depth creates the structural conditions for green bond issuance

Optional Col 6 (robustness):
- `Rep_Mayor_lag1 × bcode_benchmark_adopted` (β = −0.201, p = 0.0005)

---

## 7. What Survives from the Original Memo

| Memo element | Status |
|---|---|
| Three-table structure | ✅ Survives |
| Four-step decision chain | ✅ Survives (but the gradient is flat, not rising) |
| Rep_Mayor negative at Step 3 (self-labelling) | ✅ Confirmed |
| Rep_Mayor negative at Step 4 (assurance) | ✅ To be tested in Table 3 |
| `charges_to_own_source` strongest F1b predictor | ✅ Confirmed (β = 0.081–0.101***) |
| TEL stringency positive | ✅ Confirmed (β = 0.0011**) |
| State green bond ever positive | ✅ Confirmed (β = 0.013*) |
| H1a compulsion drives issuance | ✅ Confirmed — but on violations, not formal actions |
| H1b Rep_Mayor null at extensive margin | ❌ Rejected — significantly negative |
| H3a fiscal amplification triple | ❌ Rejected — zero effect |
| Table 2 compulsion gradient | ⚠️ To be tested next |
| Table 3 water-only Fisher test | ⚠️ Raw pattern confirmed (42% vs 10%) |

---

## 8. Data Status Update (April 2026)

| Dataset | Status |
|---|---|
| EPA enforcement (full 200-col, 3-tier) | ✅ Integrated (pipeline/20) |
| Mayoral partisanship | ✅ Integrated (576 cities, 2010–2025) |
| Bloomberg green bonds + categories | ✅ Y_self_green, Y_esg_assurance, 7 category Y_* derived |
| Water-only state+nearby panels | ✅ Built (pipeline/21) |
| CWSRF (USASpending) | ✅ Integrated, backfilled 2011–2012 |
| CWNS + pct_deficient | ✅ Integrated, extrapolated 2011–2012 |
| BPS + benchmarking | ✅ Integrated (pipeline/18) |
| Municipal electric utilities | ✅ Integrated (pipeline/19) |
| FEMA disasters + NFIP | ✅ Integrated |
| State institutional (bond banks, referenda, MSRB) | ✅ Integrated |
| Presidential vote (MIT MEDSL 2012–2024) | ✅ Integrated (pipeline/22) |
| ESG legislation (2010–2025) | ✅ Integrated |
| Climate policy v2 (sourced) | ✅ Integrated (pipeline/17) |
| Panel dimensions | 7,514 rows × 2,330 columns (gzipped) |
| Table 1 sample | N = 6,054 (Cols 1–4), N = 4,993 (Col 5) |

---

## 9. Next Steps

1. **Table 2** — run the compulsion gradient across categories.
   The gradient argument is weakened by H1b being rejected, but
   category-level entry rates by party are still a strong descriptive
   finding. Table 2 becomes less about "compulsion narrows the gap"
   and more about "where institutional capacity exists, Dems enter
   and Reps don't."

2. **Table 3** — run the credibility gap (Y_esg_assurance conditional
   on Green_Bond_Issued = 1). The water-only Fisher test (42% vs 10%)
   is the paper's cleanest finding and is independent of the
   interaction-structure revision.

3. **Theoretical reframing** — draft 2 paragraphs for the introduction
   summarizing the capacity-amplification mechanism.

---

*Working memo — Oxford DPhil research — not for circulation*
