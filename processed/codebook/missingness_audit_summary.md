# Missingness Audit: 39 Dropped Cities — Complete Diagnosis

## Cross-Tabulation (Headline)

| Classification | Count | Recoverable? |
|---|---|---|
| **MERGE_BUG** | **6** | **Yes — crosswalk fix or reclassification** |
| **YEAR_GAP** | **5** | Yes — if overflow_events_lag2 dropped from controls |
| **GENUINE_ABSENCE** | **23** | Yes — if overflow_events_lag2 dropped from controls |
| **PRINCIPLED_DROP** | **5** | No — structurally irrecoverable or not meaningful |
| **Total** | **39** | |

**Recovery potential**: Dropping `overflow_events_lag2` from the preferred spec recovers 28 cities (5 YEAR_GAP + 23 GENUINE_ABSENCE). Fixing the 6 MERGE_BUG cities recovers 6 more. **Maximum recoverable: 34 of 39 cities**, bringing the sample from 539 to 573 cities (of 578).

---

## MERGE_BUG — 6 Cities (Highest Priority)

These cities have data available in source files but it does not reach the panel due to crosswalk or coding failures.

| FIPS | City | State | Pop | Missing Controls | Specific Fix |
|---|---|---|---|---|---|
| 1303440 | Athens-Clarke County | GA | 122,893 | pres_dem_vote_share, state_rep_trifecta, esg_has_muni_bond_law | Add FIPS 1303440 to presidential, state_political, and antiesg crosswalks. Consolidated city-county: Clarke County (13059) presidential vote = city vote. For state vars, assign GA values. |
| 1836000 | Indianapolis | IN | 858,283 | pres_dem_vote_share, state_rep_trifecta | Add to crosswalks. Marion County (18097) vote = city vote. Assign IN state vars. |
| 2148000 | Louisville | KY | 616,669 | pres_dem_vote_share, state_rep_trifecta | Add to crosswalks. Jefferson County (21111) vote = city vote. Assign KY state vars. **Has 1 green bond — only issuer among the 39.** |
| 4752006 | Nashville-Davidson | TN | 655,779 | pres_dem_vote_share, state_rep_trifecta | Add to crosswalks. Davidson County (47037) vote = city vote. Assign TN state vars. |
| 2965126 | St. Peters | MO | 56,362 | pres_dem_vote_share, state_rep_trifecta | Regular city omitted from crosswalk. Use St. Charles County (29183) vote as proxy. Assign MO state vars. |
| 2408775 | Bowie | MD | 57,595 | Rep_Mayor | Coded as "I" (Independent) in mayor_party.csv but `prob_republican=0.000`, `prob_democrat=1.000`. Effectively Democratic. `additional_candidates_6.csv` has Tim Adams as pid=D winner in 2023. Reclassify as D (Rep_Mayor=0) or use continuous `prob_republican`. |

### Merge fixes needed:
1. **Presidential crosswalk**: Add 5 FIPS codes (1303440, 1836000, 2148000, 4752006, 2965126) with county FIPS for vote allocation.
2. **State political crosswalk**: Same 5 FIPS codes — assign state-level variables for GA, IN, KY, TN, MO.
3. **Anti-ESG crosswalk**: Add 1303440 (Athens-Clarke) — assign GA state-level values.
4. **Mayor coding**: Reclassify Bowie MD as D based on prob_democrat=1.0 and additional_candidates evidence.

---

## YEAR_GAP — 5 Cities

These cities ARE in the EPA ECHO source file but only for years outside the panel window (e.g., year 2000, 2005, 2008, 2025). The overflow variable is NaN for all 2013–2025 panel years.

| FIPS | City | State | Pop | EPA Year(s) Present |
|---|---|---|---|---|
| 616532 | Costa Mesa | CA | 112,158 | 2005 |
| 655156 | Palmdale | CA | 158,850 | 2025 |
| 660620 | Richmond | CA | 110,224 | 2001 |
| 2670040 | Royal Oak | MI | 58,617 | 2008 |
| 2679000 | Taylor | MI | 62,076 | 2000 |

**Fix**: Drop `overflow_events_lag2` from the preferred control vector (as recommended in prior missingness analysis). These 5 cities are then recovered.

---

## GENUINE_ABSENCE — 23 Cities

These cities are **not in the EPA ECHO source at all** — they have no registered NPDES overflow/CSO facilities. They are served by regional sewer systems (e.g., MN Metropolitan Council, county sewer districts). The absence of overflow data is not an error — it reflects their institutional structure.

| State | Count | Cities |
|---|---|---|
| MN | 11 | Apple Valley, Blaine, Bloomington, Burnsville, Coon Rapids, Eagan, Edina, Maple Grove, Minnetonka, St. Cloud, Woodbury |
| CA | 7 | Baldwin Park, Chula Vista, El Monte, Fremont, Rancho Cucamonga, San Ramon, Union City |
| IL | 2 | Cicero, Tinley Park |
| OH | 2 | Kettering, Middletown |
| MI | 1 | Pontiac |

**Fix**: Drop `overflow_events_lag2` from the preferred control vector. All 23 cities are then recovered.

---

## PRINCIPLED_DROP — 5 Cities

These cities should remain dropped on substantive grounds.

| FIPS | City | State | Pop | Reason |
|---|---|---|---|---|
| 648914 | Monterey Park | CA | 60,700 | Council-manager government. "Mayor" is a council member selected by rotation. No mayoral election; partisanship not meaningful for theory. |
| 656924 | Pico Rivera | CA | 62,911 | Same — council-manager, rotating chair. |
| 686328 | Woodland | CA | 58,829 | Same — council-manager, rotating chair. |
| 1754885 | Oak Park | IL | 52,545 | Independent mayor (David Pope), coded as "I" for all years. `prob_republican` and `prob_democrat` are both NaN — no probabilistic fallback available. Genuinely non-partisan. |
| 3420260 | Edison | NJ | N/A | NJ township, not a Census municipality. No population, fiscal, or demographic data. Missing 10 of 14 controls. |

---

## Supplementary Files Checked

| File | Contents | Relevant to |
|---|---|---|
| `additional_candidates_6.csv` | 1,722 mayoral candidate records | Bowie MD (pid=D for Tim Adams, 2023 winner) |
| `MayoralCandidatesUnknown240326.xlsx` | 402 unknown-party candidates | None of the 5 Rep_Mayor-missing cities |
| `Unclassified_Mayors.xlsx` | 508 unclassified mayors | None of the 5 Rep_Mayor-missing cities |
| `data/clean/mayor_party/mayor_party.csv` | 576 cities × 2010–2025 | Oak Park (I), Bowie (I with prob_D=1.0) |
| `data/clean/epa_echo_authoritative/` | 554 cities × 2000–2026 | 5 overflow cities with non-panel-year data |

---

## Recommended Action Sequence

1. **Immediate (no data collection)**: Drop `overflow_events_lag2` from preferred Table 1 controls. Recovers **28 cities** (GENUINE_ABSENCE + YEAR_GAP). Report overflow only in compulsion-specific tables.

2. **Low effort (crosswalk edits)**: Fix the 5 consolidated/missing presidential crosswalk entries. Recovers **5 cities** including Louisville (1 green bond).

3. **Minimal effort (reclassification)**: Reclassify Bowie MD from I to D based on prob_democrat=1.0. Recovers **1 city**.

4. **Leave dropped**: 5 PRINCIPLED_DROP cities (3 CA council-manager, 1 IL independent, 1 NJ township).

**After all fixes: 573 of 578 cities in sample** (539 → 573, +34 cities, ~+400 city-year obs).
