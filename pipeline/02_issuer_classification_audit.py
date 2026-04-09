"""
Issuer Classification Audit
============================
Compares jurisdiction classifications assigned in bonds_with_issuer_classification.xlsx
against the MSRB's official Issuer Type in All_US_Municipal_Bond_Issuers.csv.

Outputs:
  - processed/issuer_classification_audit.md   (narrative per-issuer analysis)
  - processed/issuer_classification_audit.csv   (machine-readable results)
"""

import pandas as pd
import re
from rapidfuzz import fuzz, process
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "bloomberg"
OUT = ROOT / "processed"

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
msrb = pd.read_csv(RAW / "All_US_Municipal_Bond_Issuers.csv")
bonds = pd.read_excel(RAW / "bonds_with_issuer_classification.xlsx")

# ---------------------------------------------------------------------------
# 2. Normalise names for fuzzy matching
# ---------------------------------------------------------------------------
def normalise(name: str) -> str:
    s = name.upper()
    s = re.sub(r"\bCUSIP:.*$", "", s)
    s = re.sub(
        r"\b(REV|REVS|REVENUE|REVENUES|BONDS|BOND|CTFS|PARTN|LEASE|LEASEREV|SER|SERIES)\b",
        "",
        s,
    )
    s = re.sub(r"\d{4,}", "", s)
    s = re.sub(r"[^A-Z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


msrb["norm_name"] = msrb["Issuer Name"].apply(normalise)

# ---------------------------------------------------------------------------
# 3. Collapse bonds to unique issuers
# ---------------------------------------------------------------------------
bond_issuers = (
    bonds.groupby("Issuer Name")
    .agg(
        Jurisdiction_Type=("Jurisdiction_Type", "first"),
        Entity_Type=("Entity_Type", "first"),
        State=("State_Abb_Classified", "first"),
        Controlling_Jurisdiction=("Controlling_Jurisdiction", "first"),
        Ultimate_Political_Jurisdiction=("Ultimate_Political_Jurisdiction", "first"),
        Independence_Level=("Independence_Level", "first"),
        Geographic_Scope=("Geographic_Scope", "first"),
        Classification_Confidence=("Classification_Confidence", "first"),
        num_bonds=("ID", "count"),
    )
    .reset_index()
)
bond_issuers["norm_name"] = bond_issuers["Issuer Name"].apply(normalise)

GENERIC_WORDS = {
    "OF", "THE", "AND", "A", "AN", "NO", "INC", "CORP", "AUTH", "AUTHORITY",
    "COUNTY", "CITY", "STATE", "DISTRICT", "SCHOOL", "BOARD", "WATER", "SEWER",
    "PUBLIC", "FINANCING", "MUNICIPAL", "DEVELOPMENT", "INDUSTRIAL", "REV", "SYS",
}

# ---------------------------------------------------------------------------
# 4. Match each bond issuer to MSRB
# ---------------------------------------------------------------------------
rows = []
for _, bi in bond_issuers.iterrows():
    state = bi["State"]
    state_msrb = msrb[msrb["State"] == state]

    if len(state_msrb) == 0:
        rows.append({
            "Issuer": bi["Issuer Name"],
            "State": state,
            "Your_Jurisdiction": bi["Jurisdiction_Type"],
            "Your_Entity_Type": bi["Entity_Type"],
            "Controlling_Jurisdiction": bi["Controlling_Jurisdiction"],
            "Ultimate_Political_Jurisdiction": bi["Ultimate_Political_Jurisdiction"],
            "Independence_Level": bi["Independence_Level"],
            "Geographic_Scope": bi["Geographic_Scope"],
            "Classification_Confidence": bi["Classification_Confidence"],
            "Num_Bonds": bi["num_bonds"],
            "MSRB_Best_Match": None,
            "MSRB_Best_Type": None,
            "Match_Score": 0,
            "Match_Quality": "NO_STATE",
            "MSRB_Type_Distribution": "",
            "Has_Matching_Type": False,
            "Comparison": "UNABLE_TO_COMPARE",
        })
        continue

    choices = state_msrb["norm_name"].tolist()
    bn = bi["norm_name"]

    # Multi-scorer matching
    all_matches = {}
    for scorer in [fuzz.token_set_ratio, fuzz.token_sort_ratio, fuzz.WRatio]:
        for name, score, idx_m in process.extract(bn, choices, scorer=scorer, limit=10):
            if idx_m not in all_matches or score > all_matches[idx_m][1]:
                all_matches[idx_m] = (name, score, idx_m)

    sorted_matches = sorted(all_matches.values(), key=lambda x: -x[1])
    best_name, best_score, best_idx = sorted_matches[0]
    best_row = state_msrb.iloc[best_idx]

    # Type distribution among good matches
    good = [(n, s, i) for n, s, i in sorted_matches if s >= 70]
    type_counts = Counter(state_msrb.iloc[i]["Issuer Type"] for _, _, i in good)

    # Match quality via specific word overlap
    bond_words = set(bn.split())
    msrb_words = set(best_row["norm_name"].split())
    specific_common = (bond_words & msrb_words) - GENERIC_WORDS

    if best_score >= 90 and specific_common:
        quality = "HIGH"
    elif best_score >= 80 and specific_common:
        quality = "MODERATE"
    elif best_score >= 70 and specific_common:
        quality = "FAIR"
    else:
        quality = "LOW"

    # Compare classifications
    expected = {"CITY": "City", "COUNTY": "County", "STATE": "State"}.get(
        bi["Jurisdiction_Type"], "Other"
    )
    has_match = expected in [state_msrb.iloc[i]["Issuer Type"] for _, _, i in good]

    if quality in ("LOW", "NO_STATE"):
        comparison = "UNABLE_TO_COMPARE"
    elif best_row["Issuer Type"] == expected:
        comparison = "AGREES"
    elif has_match:
        comparison = "AGREES_ALTERNATE_ENTRY"
    elif bi["Jurisdiction_Type"] in (
        "SCHOOL_DISTRICT", "SPECIAL_DISTRICT", "MULTI_JURISDICTIONAL"
    ) and best_row["Issuer Type"] in ("City", "County", "State"):
        comparison = "PLAUSIBLE_MSRB_USES_PARENT"
    else:
        comparison = "DISCREPANCY"

    rows.append({
        "Issuer": bi["Issuer Name"],
        "State": state,
        "Your_Jurisdiction": bi["Jurisdiction_Type"],
        "Your_Entity_Type": bi["Entity_Type"],
        "Controlling_Jurisdiction": bi["Controlling_Jurisdiction"],
        "Ultimate_Political_Jurisdiction": bi["Ultimate_Political_Jurisdiction"],
        "Independence_Level": bi["Independence_Level"],
        "Geographic_Scope": bi["Geographic_Scope"],
        "Classification_Confidence": bi["Classification_Confidence"],
        "Num_Bonds": bi["num_bonds"],
        "MSRB_Best_Match": best_row["Issuer Name"],
        "MSRB_Best_Type": best_row["Issuer Type"],
        "Match_Score": best_score,
        "Match_Quality": quality,
        "MSRB_Type_Distribution": str(dict(type_counts)),
        "Has_Matching_Type": has_match,
        "Comparison": comparison,
    })

df = pd.DataFrame(rows)

# ---------------------------------------------------------------------------
# 5. Save CSV
# ---------------------------------------------------------------------------
df.to_csv(OUT / "issuer_classification_audit.csv", index=False)

# ---------------------------------------------------------------------------
# 6. Generate Markdown report
# ---------------------------------------------------------------------------
lines = []
lines.append("# Issuer Classification Audit")
lines.append("")
lines.append("Comparison of jurisdiction types assigned in `bonds_with_issuer_classification.xlsx`")
lines.append("against the MSRB's official `Issuer Type` in `All_US_Municipal_Bond_Issuers.csv`.")
lines.append("")

# --- Summary ---
lines.append("## Summary")
lines.append("")
lines.append(f"- **Total unique issuers analysed:** {len(df)}")
lines.append(f"- **MSRB entries searched:** {len(msrb):,}")
lines.append("")

comp_counts = df["Comparison"].value_counts()
lines.append("| Comparison outcome | Count |")
lines.append("|---|---|")
for outcome in ["AGREES", "AGREES_ALTERNATE_ENTRY", "PLAUSIBLE_MSRB_USES_PARENT",
                 "DISCREPANCY", "UNABLE_TO_COMPARE"]:
    lines.append(f"| {outcome} | {comp_counts.get(outcome, 0)} |")
lines.append("")

lines.append("**Interpretation of categories:**")
lines.append("")
lines.append("- **AGREES** — Your jurisdiction type directly maps to the MSRB Issuer Type of the best match.")
lines.append("- **AGREES_ALTERNATE_ENTRY** — The best MSRB match has a different type, but another high-scoring MSRB entry for the same entity has a type that matches yours. This commonly happens because MSRB creates separate entries for different bond programs (e.g., general obligation vs revenue bonds) and sometimes labels them differently.")
lines.append("- **PLAUSIBLE_MSRB_USES_PARENT** — You classified the entity as SCHOOL_DISTRICT, SPECIAL_DISTRICT, or MULTI_JURISDICTIONAL, but MSRB uses the parent jurisdiction's type (City/County/State). The MSRB has only four categories (City, County, State, Other) and often assigns subordinate entities to their parent jurisdiction.")
lines.append("- **DISCREPANCY** — A genuine disagreement between your classification and what MSRB records suggest, warranting review.")
lines.append("- **UNABLE_TO_COMPARE** — The fuzzy match quality was too low to make a reliable comparison, or no MSRB entries exist for the state.")
lines.append("")

# --- Cross-tabulation ---
comparable = df[df["Comparison"] != "UNABLE_TO_COMPARE"]
lines.append("## Cross-tabulation (Your type vs MSRB type)")
lines.append("")
lines.append("For the {} issuers with reliable MSRB matches:".format(len(comparable)))
lines.append("")
ct = pd.crosstab(comparable["Your_Jurisdiction"], comparable["MSRB_Best_Type"], margins=True)
lines.append(ct.to_markdown())
lines.append("")

# --- Match quality ---
lines.append("## Match quality distribution")
lines.append("")
mq = df["Match_Quality"].value_counts()
lines.append("| Quality | Count | Description |")
lines.append("|---|---|---|")
lines.append(f"| HIGH | {mq.get('HIGH', 0)} | Score >= 90 with shared specific words |")
lines.append(f"| MODERATE | {mq.get('MODERATE', 0)} | Score 80-89 with shared specific words |")
lines.append(f"| FAIR | {mq.get('FAIR', 0)} | Score 70-79 with shared specific words |")
lines.append(f"| LOW | {mq.get('LOW', 0)} | Score < 70 or no shared specific words |")
lines.append(f"| NO_STATE | {mq.get('NO_STATE', 0)} | No MSRB entries for the state |")
lines.append("")

# --- Key systematic patterns ---
lines.append("## Key systematic patterns observed")
lines.append("")
lines.append("### 1. MSRB classifies bond programs (not entities)")
lines.append("")
lines.append("The MSRB database is organised around bond programs, not institutional entities. "
             "A single city may have dozens of MSRB entries — one for general obligation bonds (often typed as \"City\"), "
             "and many for revenue bonds (often typed as \"Other\"). For example, Tampa, FL has 47 MSRB entries: "
             "most are typed \"Other\" (revenue programs), not \"City\".")
lines.append("")
lines.append("### 2. MSRB uses only four categories")
lines.append("")
lines.append("The MSRB uses only **City, County, State, Other**. Your classification uses a richer taxonomy: "
             "CITY, COUNTY, STATE, SPECIAL_DISTRICT, MULTI_JURISDICTIONAL, SCHOOL_DISTRICT, OTHER. "
             "Anything that isn't cleanly a city, county, or state government in MSRB's view becomes \"Other\", "
             "including state authorities, public universities, financing authorities, transit authorities, etc.")
lines.append("")
lines.append("### 3. Louisiana parishes are classified as \"City\" by MSRB")
lines.append("")
lines.append("MSRB classifies Louisiana parishes (county-equivalents) as \"City\", not \"County\". "
             "Your classification of these as COUNTY is arguably more accurate.")
lines.append("")
lines.append("### 4. District of Columbia")
lines.append("")
lines.append("MSRB classifies DC as \"State\". Your classification as CITY is a reasonable alternative "
             "given DC functions as a city government. This is a definitional difference, not an error.")
lines.append("")
lines.append("### 5. State authorities and universities")
lines.append("")
lines.append("You classified state-created authorities (financing authorities, development corporations, "
             "public universities) as STATE. MSRB frequently classifies these as \"Other\" (e.g., MTA, "
             "NJ Infrastructure Bank, state universities). Both approaches have merit: yours reflects the "
             "controlling jurisdiction, MSRB's reflects that these are not the state government itself.")
lines.append("")

# --- Discrepancies ---
disc = df[df["Comparison"] == "DISCREPANCY"].sort_values("Match_Score", ascending=False)
lines.append(f"## Discrepancies requiring review ({len(disc)} issuers)")
lines.append("")
lines.append("These are cases where your classification and the MSRB classification clearly disagree, "
             "and no alternate MSRB entry has a matching type.")
lines.append("")

for _, r in disc.iterrows():
    lines.append(f"### {r['Issuer']} [{r['State']}]")
    lines.append("")
    lines.append(f"- **Your classification:** {r['Your_Jurisdiction']} ({r['Your_Entity_Type']})")
    lines.append(f"- **MSRB best match:** {r['MSRB_Best_Match']}")
    lines.append(f"- **MSRB type:** {r['MSRB_Best_Type']}")
    lines.append(f"- **Match score:** {r['Match_Score']:.0f} ({r['Match_Quality']})")
    lines.append(f"- **MSRB type distribution across matches:** {r['MSRB_Type_Distribution']}")

    # Add analysis
    yours = r["Your_Jurisdiction"]
    msrb_t = r["MSRB_Best_Type"]
    entity = r["Your_Entity_Type"]
    issuer = r["Issuer"]

    if "District of Columbia" in issuer:
        lines.append(f"- **Analysis:** DC is a unique jurisdiction — it functions as both a city and a state. MSRB classifies it as State; your classification as CITY reflects its municipal government role. Definitional difference, not an error.")
    elif "Parish" in issuer and r["State"] == "LA":
        lines.append(f"- **Analysis:** Louisiana parishes are county-equivalents. MSRB classifies parishes as City, likely treating them as the primary local government. Your COUNTY classification is arguably more accurate for jurisdictional analysis.")
    elif entity == "Public university" and msrb_t == "Other":
        lines.append(f"- **Analysis:** MSRB classifies universities as Other even when state-controlled. Your STATE classification reflects the controlling jurisdiction. Consider whether your analysis needs the issuing entity type or the controlling jurisdiction.")
    elif entity == "Public university" and msrb_t == "City":
        lines.append(f"- **Analysis:** MSRB sometimes classifies universities under the city where they are located. Your STATE classification reflects state control. Both are defensible depending on analytical purpose.")
    elif entity in ("State agency", "Financing authority", "Bond bank", "Development corporation") and msrb_t == "Other" and yours == "STATE":
        lines.append(f"- **Analysis:** MSRB classifies state authorities/agencies as Other rather than State. Your STATE classification reflects the controlling jurisdiction. MSRB reserves State for the state government itself.")
    elif entity == "Development corporation" and yours == "CITY" and msrb_t == "Other":
        lines.append(f"- **Analysis:** MSRB classifies this city-controlled development entity as Other. Your CITY classification reflects the controlling jurisdiction. MSRB reserves City for the city government's direct bond programs.")
    elif entity in ("State agency", "Financing authority", "Bond bank") and msrb_t == "City":
        lines.append(f"- **Analysis:** MSRB has classified this entity under City, which may reflect local rather than state control. Your STATE classification assigns it to the controlling state. Review whether this entity truly operates at the state level.")
    elif entity == "Town Government" and msrb_t == "Other":
        lines.append(f"- **Analysis:** New England towns are general-purpose local governments equivalent to cities. MSRB classifies them as Other. Your CITY classification is reasonable for jurisdictional analysis.")
    elif entity == "Tribal government" and msrb_t == "City":
        lines.append(f"- **Analysis:** MSRB classifies tribal governments as City. Your OTHER classification more accurately reflects the unique sovereign status of tribal governments.")
    elif yours == "CITY" and msrb_t == "Other":
        lines.append(f"- **Analysis:** MSRB classifies this city entity's bond programs as Other (typically used for revenue bonds). Your CITY classification reflects the actual governmental jurisdiction. The MSRB category may reflect the bond type rather than the issuer type.")
    elif yours == "CITY" and msrb_t == "County":
        lines.append(f"- **Analysis:** MSRB lists this under a county-level entry. Review whether the issuer is truly at the city level or operates at the county level.")
    elif yours == "CITY" and msrb_t == "State":
        lines.append(f"- **Analysis:** MSRB classifies this under State. Review whether this entity is controlled at the state level rather than the city level.")
    elif yours == "COUNTY" and msrb_t == "City":
        lines.append(f"- **Analysis:** MSRB lists the matched entity as City. This may be a matching artifact (matched to a city within the county) or MSRB may consider this a city-level entity.")
    elif yours == "COUNTY" and msrb_t == "Other":
        lines.append(f"- **Analysis:** MSRB classifies this county entity as Other. Your COUNTY classification reflects the jurisdictional level. The MSRB category may reflect the special-purpose nature of the entity.")
    elif yours == "STATE" and msrb_t == "City":
        lines.append(f"- **Analysis:** MSRB classifies this as City-level. Review whether this entity is truly state-controlled or operates at a local level.")
    else:
        lines.append(f"- **Analysis:** Classification disagreement. Your {yours} vs MSRB {msrb_t} warrants manual review.")
    lines.append("")

# --- Plausible differences ---
plaus = df[df["Comparison"] == "PLAUSIBLE_MSRB_USES_PARENT"]
lines.append(f"## Plausible differences — MSRB uses parent jurisdiction ({len(plaus)} issuers)")
lines.append("")
lines.append("In these cases, you used a more specific jurisdiction type (SCHOOL_DISTRICT, SPECIAL_DISTRICT, "
             "or MULTI_JURISDICTIONAL) and MSRB used the parent jurisdiction (City, County, or State). "
             "Your more granular classification is reasonable and provides richer analytical detail.")
lines.append("")

lines.append("| Issuer | State | Your Type | MSRB Type | MSRB Match | Score |")
lines.append("|---|---|---|---|---|---|")
for _, r in plaus.sort_values(["Your_Jurisdiction", "State"]).iterrows():
    lines.append(f"| {r['Issuer']} | {r['State']} | {r['Your_Jurisdiction']} | {r['MSRB_Best_Type']} | {r['MSRB_Best_Match'][:60]} | {r['Match_Score']:.0f} |")
lines.append("")

# --- Agrees with alternate entry ---
alt = df[df["Comparison"] == "AGREES_ALTERNATE_ENTRY"]
lines.append(f"## Agrees via alternate MSRB entry ({len(alt)} issuers)")
lines.append("")
lines.append("The best MSRB match had a different type, but another high-scoring MSRB entry for the same "
             "entity has a type consistent with your classification. These are not discrepancies.")
lines.append("")
lines.append("| Issuer | State | Your Type | MSRB Best Type | MSRB Match | Score |")
lines.append("|---|---|---|---|---|---|")
for _, r in alt.sort_values(["Your_Jurisdiction", "State"]).iterrows():
    lines.append(f"| {r['Issuer']} | {r['State']} | {r['Your_Jurisdiction']} | {r['MSRB_Best_Type']} | {r['MSRB_Best_Match'][:60]} | {r['Match_Score']:.0f} |")
lines.append("")

# --- Full per-issuer log (AGREES) ---
agrees = df[df["Comparison"] == "AGREES"].sort_values(["Your_Jurisdiction", "State", "Issuer"])
lines.append(f"## Direct agreement ({len(agrees)} issuers)")
lines.append("")
lines.append("Your classification directly matches the MSRB best match type.")
lines.append("")
lines.append("| Issuer | State | Your Type | MSRB Type | MSRB Match | Score |")
lines.append("|---|---|---|---|---|---|")
for _, r in agrees.iterrows():
    lines.append(f"| {r['Issuer']} | {r['State']} | {r['Your_Jurisdiction']} | {r['MSRB_Best_Type']} | {r['MSRB_Best_Match'][:60]} | {r['Match_Score']:.0f} |")
lines.append("")

# --- Unable to compare ---
unable = df[df["Comparison"] == "UNABLE_TO_COMPARE"].sort_values(["Your_Jurisdiction", "State", "Issuer"])
lines.append(f"## Unable to compare ({len(unable)} issuers)")
lines.append("")
lines.append("Match quality was too low (score < 70 or no specific word overlap) to reliably compare classifications. "
             "These issuers may use significantly different naming conventions than MSRB, or may not be in the MSRB database.")
lines.append("")
lines.append("| Issuer | State | Your Type | Best MSRB Candidate | Score | Quality |")
lines.append("|---|---|---|---|---|---|")
for _, r in unable.iterrows():
    msrb_match = r['MSRB_Best_Match'] if pd.notna(r['MSRB_Best_Match']) else 'N/A'
    lines.append(f"| {r['Issuer']} | {r['State']} | {r['Your_Jurisdiction']} | {str(msrb_match)[:60]} | {r['Match_Score']:.0f} | {r['Match_Quality']} |")
lines.append("")

report = "\n".join(lines)
(OUT / "issuer_classification_audit.md").write_text(report)

print(f"Report written to {OUT / 'issuer_classification_audit.md'}")
print(f"CSV written to {OUT / 'issuer_classification_audit.csv'}")
print(f"\nFinal summary:")
print(df["Comparison"].value_counts().to_string())
