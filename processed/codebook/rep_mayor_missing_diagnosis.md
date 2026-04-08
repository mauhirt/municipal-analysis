# Diagnosis: 5 Cities Missing `Rep_Mayor`

## Headline

3 cities are **coverage gaps** — they are not in the raw mayoral partisanship file at all (all California cities with council-manager governments where the "mayor" rotates among council members). 2 cities are **coded as Independent** (party = "I") in the raw file — they have full year coverage but `Rep_Mayor` maps to NaN because the D/R binary cannot accommodate independents.

## City-by-City Diagnosis

| City | State | FIPS | Pop (log) | In Raw File? | Raw Value | Years Coded | Classification | Recoverable |
|---|---|---|---|---|---|---|---|---|
| Monterey Park | CA | 648914 | 11.01 | **No** | — | — | Coverage gap | **Partial** — council-manager city; mayor is a council member selected by council. Party affiliation may not be meaningful. Manual coding required. |
| Pico Rivera | CA | 656924 | 11.05 | **No** | — | — | Coverage gap | **Partial** — same as above. |
| Woodland | CA | 686328 | 10.97 | **No** | — | — | Coverage gap | **Partial** — same as above. |
| Oak Park | IL | 1754885 | 10.87 | **Yes** | "I" (Independent) | 2010–2025 (all years) | Genuine unretrievability | **N** — Mayor coded as Independent for all years. Raw file has full coverage; the value is "I" not NA. The D/R binary cannot accommodate this. Coding as 0.5 on prob_republican would be an option but introduces measurement error. |
| Bowie | MD | 2408775 | 10.95 | **Yes** | "I" (Independent) | 2010–2025 (all years) | Genuine unretrievability | **N** — Same as Oak Park. Independent mayor for full period. |

## Notes on the 3 California Coverage Gaps

Monterey Park, Pico Rivera, and Woodland are all **council-manager cities** where the mayor is selected from among council members on a rotating basis. In many California cities of this type, the mayoral position is largely ceremonial and partisan affiliation is not recorded on ballots (California has a nonpartisan blanket primary). These cities are absent from the MayoralCandidates_cleaned.csv file entirely, suggesting they were excluded during the original data collection because no mayoral elections occur — the council selects the mayor.

**Recovery options:**
- Manual coding from local news sources (labor-intensive, uncertain)
- Use council majority party as a proxy (requires separate data)
- Accept as structural missingness — these are small cities (pop ~50K) with weak-mayor forms where the mayor's personal partisanship is unlikely to affect bond issuance decisions

## Notes on the 2 Independent Mayors

Oak Park IL and Bowie MD both have mayors coded as "I" (Independent) for the entire 2010–2025 period. The MayoralCandidates file has 3 entries for Oak Park and 14 for Bowie, confirming these are real elections with known candidates — the candidates are simply not affiliated with either major party.

**Recovery options:**
- Use `prob_republican` from the probabilistic model (already in the panel: Oak Park = 0.07, Bowie = 0.12 — both lean heavily Democratic)
- Create a three-category variable (D/R/I) — but this changes the regression interpretation
- Accept as structural: nonpartisan/independent mayors are theoretically distinct from D or R mayors

## Summary

| Classification | Count | Cities | Recoverable |
|---|---|---|---|
| Coverage gap (CA council-manager) | 3 | Monterey Park, Pico Rivera, Woodland | Partial (manual coding) |
| Genuine unretrievability (Independent) | 2 | Oak Park IL, Bowie MD | No (or use prob_republican) |
| Processing error | 0 | — | — |

**Recommendation**: Accept these 5 cities as structural missingness. The 3 California cities have weak-mayor forms where partisanship is not meaningful. The 2 Independent-mayor cities cannot be forced into a D/R binary. Using `prob_republican` as a continuous measure (already available for 559 of 578 cities including Oak Park and Bowie) would recover these 2 cities — but they are both very small and unlikely to move any coefficient.
