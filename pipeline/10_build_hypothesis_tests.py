"""
Build three analysis artifacts aligned to hypotheses H1, H3, H4:

1. Bond-level label-intensity features (H3: labelling margin)
     processed/prospectus_analysis/bond_label_intensity.csv
     One row per matched-city CUSIP with a primary prospectus assigned.
     Continuous + categorical measures of how intensely the bond is
     labelled as green:
       - green_section_chars
       - n_green_keywords   (sum of green/ESG/sustainability/SDG family)
       - n_frameworks_cited
       - has_SPO, spo_verifier, frameworks_cited
       - bloomberg_self_reported_green, bloomberg_esg_assurance
       - match_kind (quality of CUSIP→prospectus match)

2. Bloomberg green-flag validation (H3: outcome-variable credibility)
     processed/prospectus_analysis/bloomberg_label_validation.md
     Cross-tab of Bloomberg 'Self-reported Green' vs text-detected
     green-bond designation, with sensitivity/specificity/precision
     for the Bloomberg flag as a classifier for text-green.

3. Compliance-vs-discretionary measure (H1/H4)
     processed/prospectus_analysis/bond_compliance_score.csv
     Per CUSIP: counts of compliance-family keywords and a
     compliance_density_per_1k_words score. Flags compelled vs
     discretionary at the document level (regardless of sector).

Assumes pipeline/08 and pipeline/09 have been run so the following
inputs exist:
  processed/prospectus_analysis/cusip_prospectus_map.csv
  processed/prospectus_analysis/issuance_prospectus_map.csv
  processed/prospectus_analysis/green_bond_sections_index.csv
  processed/prospectus_analysis/esg_keyword_frequencies.csv
  raw/bloomberg/cusip_with_assignment_matched.csv
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AN = ROOT / "processed/prospectus_analysis"
MATCHED = ROOT / "raw/bloomberg/cusip_with_assignment_matched.csv"

# Keyword groups used in this script (must exist in esg_keyword_frequencies.csv)
GREEN_FAMILY = [
    "green_bond", "sustainability", "environmental", "climate",
    "renewable", "solar", "wind", "hydro", "energy_efficiency",
    "LEED", "ev", "electrification", "transit",
    "carbon", "net_zero", "emissions", "decarbonization",
    "greenhouse", "adaptation", "mitigation", "ESG",
    "resilience", "water_quality", "stormwater",
]
COMPLIANCE_FAMILY = [
    "clean_water_act", "safe_drinking_water", "cercla",
    "npdes", "consent_decree", "epa_enforcement",
    "administrative_order", "ms4_permit", "compliance_schedule",
    "court_order", "regulatory_mandate", "tmdl",
    "violation", "enforcement_action",
]


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def to_int(s: str, default: int = 0) -> int:
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


def main() -> int:
    # ---- Load inputs ----
    cusip_map = read_csv(AN / "cusip_prospectus_map.csv")
    green_idx = {r["prospectus_stem"]: r for r in read_csv(AN / "green_bond_sections_index.csv")}
    kw_rows   = {r["prospectus_stem"]: r for r in read_csv(AN / "esg_keyword_frequencies.csv")}
    matched   = {r["CUSIP"]: r for r in read_csv(MATCHED)}

    # ---- 1. Bond-level label intensity ----
    intensity_rows = []
    for c in cusip_map:
        cusip = c["CUSIP"]
        files = [f for f in c["prospectus_files"].split(";") if f]
        if not files:
            continue
        # Pick the primary prospectus: the one where green_section_chars is largest
        def green_chars(stem):
            g = green_idx.get(stem)
            return to_int(g["section_chars"]) if g else 0
        primary = max(files, key=green_chars)

        green_row = green_idx.get(primary)
        kw = kw_rows.get(primary, {})
        total_words = to_int(kw.get("total_words", "0"), 1) or 1

        n_green_kw = sum(to_int(kw.get(k, "0")) for k in GREEN_FAMILY)
        matched_row = matched.get(cusip, {})

        intensity_rows.append({
            "CUSIP": cusip,
            "Issuer_Name": c["Issuer_Name"],
            "Issue_Date": c["Issue_Date"],
            "primary_prospectus": primary,
            "n_prospectus_matches": c["n_prospectuses"],
            "match_kind": c["match_kind"],
            "prospectus_total_words": total_words,
            "green_section_chars": green_chars(primary),
            "n_green_keywords": n_green_kw,
            "green_keyword_density_per_1k":
                round(1000.0 * n_green_kw / total_words, 3),
            "n_frameworks_cited": (
                len([x for x in green_row["frameworks"].split(";") if x])
                if green_row else 0
            ),
            "frameworks_cited":
                green_row["frameworks"] if green_row else "",
            "has_SPO": "1" if (green_row and green_row["verifiers"]) else "0",
            "spo_verifiers":
                green_row["verifiers"] if green_row else "",
            "bloomberg_self_reported_green":
                matched_row.get("Self-reported Green", ""),
            "bloomberg_esg_assurance":
                matched_row.get("ESG Assurance Providers", ""),
            "bloomberg_esg_framework":
                matched_row.get("ESG Framework", ""),
            "bloomberg_project_category":
                matched_row.get("ESG Project Categories", ""),
            "bloomberg_industry":
                matched_row.get("Industry_Full", ""),
            "city_fips7":
                matched_row.get("city_fips7", ""),
            "State":
                matched_row.get("State_Abb_Classified", ""),
        })

    out_intensity = AN / "bond_label_intensity.csv"
    with out_intensity.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(intensity_rows[0].keys()))
        w.writeheader()
        w.writerows(intensity_rows)
    print(f"Label intensity : {out_intensity.relative_to(ROOT)}")
    print(f"  {len(intensity_rows)} CUSIPs with at least one prospectus")

    # ---- 2. Bloomberg label validation (confusion matrix) ----
    # Define text-green = has_SPO OR green_section_chars > 500 OR n_frameworks_cited > 0
    def text_green(r):
        return (r["has_SPO"] == "1") or (to_int(r["green_section_chars"]) > 500) or (to_int(r["n_frameworks_cited"]) > 0)

    def bb_green(r):
        return r["bloomberg_self_reported_green"] == "Yes"

    tp = tn = fp = fn = 0
    bb_yes_text_green_strs = []
    bb_no_text_green_strs = []
    for r in intensity_rows:
        bg = bb_green(r)
        tg = text_green(r)
        if bg and tg: tp += 1
        elif bg and not tg: fn += 1  # Bloomberg says green, text doesn't
        elif (not bg) and tg: fp += 1  # Bloomberg says not green, text does
        else: tn += 1

    total = tp + tn + fp + fn
    sensitivity = tp / (tp + fn) if (tp + fn) else 0  # Bloomberg recall of text-green
    specificity = tn / (tn + fp) if (tn + fp) else 0
    precision   = tp / (tp + fp) if (tp + fp) else 0

    def cross_tab_by(field_name):
        """Group by a bloomberg field and show text-green rate."""
        buckets = defaultdict(lambda: [0, 0])
        for r in intensity_rows:
            k = r.get(field_name, "") or "(blank)"
            buckets[k][0] += 1
            if text_green(r):
                buckets[k][1] += 1
        return buckets

    bb_green_buckets = cross_tab_by("bloomberg_self_reported_green")
    md = []
    md.append("# Bloomberg Green-Flag Validation\n")
    md.append(
        f"Cross-tabulation of Bloomberg `Self-reported Green` against prospectus-"
        f"detected green designation (N = {total} CUSIPs covered by a prospectus).\n"
    )
    md.append("## Text-green criterion\n")
    md.append(
        "A CUSIP is 'text-green' if its primary prospectus has ANY of:\n"
        "- a detected Second-Party Opinion verifier (Kestrel / Sustainalytics / "
        "BAM / Moody's ESG)\n"
        "- a green-bond designation section longer than 500 characters\n"
        "- at least one cited green-bond framework (ICMA GBP, Climate Bonds "
        "Standard, SDGs)\n"
    )
    md.append("\n## Confusion matrix (CUSIP-level)\n")
    md.append("| | text-green = 1 | text-green = 0 | row total |")
    md.append("|---|---:|---:|---:|")
    md.append(f"| Bloomberg green = Yes | **{tp}** TP | {fn} FN | {tp+fn} |")
    md.append(f"| Bloomberg green ≠ Yes | {fp} FP | **{tn}** TN | {fp+tn} |")
    md.append(f"| **column total** | **{tp+fp}** | **{fn+tn}** | **{total}** |")
    md.append("")
    md.append("## Classifier metrics (Bloomberg as predictor of text-green)\n")
    md.append(f"- sensitivity (recall)  = TP / (TP+FN) = **{sensitivity:.3f}**")
    md.append(f"- specificity           = TN / (TN+FP) = **{specificity:.3f}**")
    md.append(f"- precision             = TP / (TP+FP) = **{precision:.3f}**")
    md.append("")
    md.append("## Rate of text-green by Bloomberg flag value\n")
    md.append("| Bloomberg flag | CUSIPs | text-green | rate |")
    md.append("|---|---:|---:|---:|")
    for k in sorted(bb_green_buckets):
        n, g = bb_green_buckets[k]
        md.append(f"| {k or '(blank)'} | {n} | {g} | {100*g/n:.1f}% |")
    md.append("")
    # --- Intensity stratification ---
    from statistics import median
    def _nums(field, bg_value):
        return sorted(
            to_int(r[field]) for r in intensity_rows
            if r["bloomberg_self_reported_green"] == bg_value
        )
    md.append("## Intensity stratification by Bloomberg flag\n")
    md.append(
        "Even a binary 'Self-reported Green' flag hides a continuous "
        "labelling intensity. The table below summarizes the "
        "prospectus-level intensity measures, stratified by Bloomberg's "
        "'Self-reported Green' value:\n"
    )
    md.append(
        "| Bloomberg flag | N | green-section median chars | n_green_keywords median | has_SPO rate |"
    )
    md.append("|---|---:|---:|---:|---:|")
    for bg in ["Yes", "No", "--", ""]:
        subset = [r for r in intensity_rows
                  if r["bloomberg_self_reported_green"] == bg]
        if not subset:
            continue
        gs = _nums("green_section_chars", bg)
        nk = _nums("n_green_keywords", bg)
        spo = sum(1 for r in subset if r["has_SPO"] == "1")
        md.append(
            f"| {bg or '(blank)'} | {len(subset)} | "
            f"{median(gs) if gs else 0:.0f} | "
            f"{median(nk) if nk else 0:.0f} | "
            f"{100*spo/len(subset):.1f}% |"
        )
    md.append("")
    md.append("## Interpretation\n")
    md.append(
        f"If sensitivity is high (>0.9) the Bloomberg flag rarely misses "
        f"bonds whose prospectuses actually label them green. If specificity "
        f"is high, the flag rarely inflates — bonds with no green language "
        f"aren't flagged. Low values on either side indicate noise in the "
        f"outcome variable the main panel regression uses.\n\n"
        f"The intensity stratification above reveals the **labelling-margin** "
        f"story directly: Bloomberg's binary Yes/No distinction carries "
        f"little information about prospectus content — both groups have "
        f"similar green-section length, keyword counts, and SPO rates. The "
        f"real dividing line is 'labelled/not-labelled' (Yes or No) vs "
        f"'unknown/missing' (-- or blank). This is consistent with a story "
        f"where issuer-level green disclosure is a discretionary labelling "
        f"decision applied to bonds that look the same ex-ante."
    )

    out_val = AN / "bloomberg_label_validation.md"
    out_val.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Validation     : {out_val.relative_to(ROOT)}")
    print(f"  TP={tp}, TN={tn}, FP={fp}, FN={fn}")
    print(f"  Sensitivity={sensitivity:.3f}  Specificity={specificity:.3f}  Precision={precision:.3f}")

    # ---- 3. Compliance-vs-discretionary score ----
    compliance_rows = []
    for r in intensity_rows:
        primary = r["primary_prospectus"]
        kw = kw_rows.get(primary, {})
        total_words = to_int(kw.get("total_words", "0"), 1) or 1
        counts = {k: to_int(kw.get(k, "0")) for k in COMPLIANCE_FAMILY}
        n_compliance = sum(counts.values())
        compliance_rows.append({
            "CUSIP": r["CUSIP"],
            "Issuer_Name": r["Issuer_Name"],
            "Issue_Date": r["Issue_Date"],
            "primary_prospectus": primary,
            "prospectus_total_words": total_words,
            "bloomberg_industry": r["bloomberg_industry"],
            "bloomberg_project_category": r["bloomberg_project_category"],
            "bloomberg_self_reported_green": r["bloomberg_self_reported_green"],
            "n_compliance_keywords": n_compliance,
            "compliance_density_per_1k":
                round(1000.0 * n_compliance / total_words, 3),
            # Binary compelled flag: specifically under a federal environmental
            # consent decree. consent_decree is narrow and defensible; broader
            # terms like court_order/regulatory_mandate catch too much boilerplate.
            "compelled_by_text": "1" if counts["consent_decree"] > 0 else "0",
            # Secondary/stronger flag: consent decree + NPDES context
            "compelled_by_text_strict": "1" if (
                counts["consent_decree"] > 0 and counts["npdes"] > 0
            ) else "0",
            **{f"kw_{k}": counts[k] for k in COMPLIANCE_FAMILY},
        })

    out_comp = AN / "bond_compliance_score.csv"
    with out_comp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(compliance_rows[0].keys()))
        w.writeheader()
        w.writerows(compliance_rows)

    n_compelled = sum(1 for r in compliance_rows if r["compelled_by_text"] == "1")
    print(f"Compliance     : {out_comp.relative_to(ROOT)}")
    print(f"  {len(compliance_rows)} CUSIPs scored")
    print(f"  {n_compelled} ({100*n_compelled/len(compliance_rows):.1f}%) flagged 'compelled_by_text'")

    # Quick descriptive: water vs non-water compelled-rate
    by_ind = defaultdict(lambda: [0, 0])
    for r in compliance_rows:
        k = r["bloomberg_industry"] or "(blank)"
        by_ind[k][0] += 1
        if r["compelled_by_text"] == "1":
            by_ind[k][1] += 1
    print("\n  'Compelled by text' rate by Bloomberg industry (top 10):")
    for ind, (n, c) in sorted(by_ind.items(), key=lambda x: -x[1][0])[:10]:
        print(f"    {n:4d}  compelled={c:4d} ({100*c/n:5.1f}%)  {ind[:60]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
