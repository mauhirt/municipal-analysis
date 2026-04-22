"""
Build analysis-ready artifacts from the prospectus text corpus.

Outputs:
  processed/prospectus_analysis/cusip_prospectus_map.csv
      One row per matched-city CUSIP. Columns: CUSIP, Issuer, Issue_Date,
      Self_reported_Green, n_prospectuses, prospectus_files, match_kind.

  processed/prospectus_analysis/issuance_prospectus_map.csv
      One row per (Issuer, Issue_Date). Columns: Issuer_Name, Issue_Date,
      n_CUSIPs, n_CUSIPs_covered, Self_reported_Green_any, Total_Face_Value,
      Primary_State, prospectus_files.

  processed/prospectus_analysis/green_bond_sections/*.txt
      Extracted "Designation as Green Bonds" / "Green Bonds" sections from
      each prospectus. One file per prospectus that has a detectable green
      section.

  processed/prospectus_analysis/green_bond_sections_index.csv
      Index of which prospectuses have green-section extractions and their
      detected framework/verifier.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATCHED = ROOT / "raw/bloomberg/cusip_with_assignment_matched.csv"
TEXT_DIR = ROOT / "raw/emma/prospectuses_text"
OUT_DIR = ROOT / "processed/prospectus_analysis"

CUSIP_RE = re.compile(r"[0-9A-Z]{9}")

# Manual overrides for prospectuses that cover an issuance but can't be
# detected via text matching (scanned PDFs, no CUSIP column).
MANUAL_OVERRIDES = {
    ("St Louis Municipal Finance Corp", "2016-05-04"): "ES790334-ES618314-ER1154135",
    ("City of Little Rock AR Water Reclamation System Revenue", "2020-12-03"): "P21406465-P21093323-P21502152",
}


def cusip_match(cusip: str, blob: str, raw: str) -> str | None:
    """Return match kind if the CUSIP is present in this text, else None."""
    if cusip in blob:
        return "full"
    prefix = cusip[:6]
    if prefix not in raw:
        return None
    suffix = cusip[6:]
    if suffix in raw:
        return "prefix+suffix"
    split_aab = f"{suffix[:2]} {suffix[2]}"
    if split_aab in raw:
        return "prefix+split_suffix"
    return None


# ---------------------------------------------------------------------------
# Green bond section extraction
# ---------------------------------------------------------------------------
GREEN_HEADER_PATTERNS = [
    # match on their own line or followed by punctuation
    r"DESIGNATION AS GREEN BONDS?",
    r"GREEN BONDS? DESIGNATION",
    r"GREEN BOND DESIGNATION",
    r"GREEN BONDS?\b",           # loose — only used as fallback
    r"USE OF PROCEEDS[\s\-—–]+GREEN",
    r"THE GREEN BONDS?\b",
]
VERIFIER_PATTERNS = {
    "Kestrel": r"\bKESTREL\b",
    "Sustainalytics": r"\bSUSTAINALYTICS\b",
    "S&P ESG": r"S&P GLOBAL RATINGS.*(ESG|SHADES OF GREEN)",
    "Moody's ESG": r"MOODY'S.*(ESG|GREEN)",
    "Climate Bond Initiative": r"CLIMATE BONDS? (INITIATIVE|STANDARD|CERTIFIED)",
    "ICMA GBP": r"(ICMA|INTERNATIONAL CAPITAL MARKET ASSOCIATION).{0,60}GREEN BOND PRINCIPLES",
    "Green Bond Principles": r"GREEN BOND PRINCIPLES",
    "Build America Mutual": r"BUILD AMERICA MUTUAL",
    "Kroll/KBRA": r"KROLL|KBRA",
}
FRAMEWORK_PATTERNS = {
    "ICMA Green Bond Principles": r"GREEN BOND PRINCIPLES",
    "Climate Bonds Standard": r"CLIMATE BONDS? STANDARD",
    "EU Taxonomy": r"EU TAXONOMY",
    "Sustainable Development Goals": r"(SDGS?|SUSTAINABLE DEVELOPMENT GOALS)",
}


def extract_green_section(raw_text: str) -> tuple[str | None, dict]:
    """Extract the green-bonds section and metadata (framework, verifier).

    Picks the match that looks like a real section body (followed by prose),
    not a table-of-contents entry (followed by dot leaders and page numbers).
    """
    text_upper = raw_text.upper()

    # Try each header pattern; for each, iterate all matches and score them.
    # A TOC entry is recognizable by dot-leader sequences like '......' within
    # the next ~120 chars. Real sections are followed by sentences.
    def score_match(m: re.Match) -> tuple[int, int]:
        after = raw_text[m.end():m.end() + 150]
        is_toc = bool(re.search(r"\.{5,}|\t[0-9]+\s*$", after[:200]))
        # prefer non-TOC; among ties, prefer later matches (body usually after TOC)
        return (0 if is_toc else 1, m.start())

    best = None
    best_header = None
    for pat in GREEN_HEADER_PATTERNS[:-1]:
        matches = list(re.finditer(pat, text_upper))
        if not matches:
            continue
        # Pick the highest-scoring (non-TOC, latest)
        scored = sorted(matches, key=score_match, reverse=True)
        candidate = scored[0]
        if score_match(candidate)[0] == 1:  # found a non-TOC match
            best = candidate
            best_header = candidate.group()
            break
    if best is None:
        for pat in GREEN_HEADER_PATTERNS[-2:]:
            matches = list(re.finditer(pat, text_upper))
            if matches:
                scored = sorted(matches, key=score_match, reverse=True)
                if score_match(scored[0])[0] == 1:
                    best = scored[0]
                    best_header = best.group()
                    break
    if best is None:
        return None, {}

    start = best.start()
    matched_header = best_header
    section = raw_text[start:start + 8000]

    next_header = re.search(r"\n[A-Z][A-Z\s,&\-]{14,}(?:\n|$)", section[500:])
    if next_header:
        section = section[:500 + next_header.start()]

    # Detect framework/verifier mentions
    meta: dict[str, str] = {"header_matched": matched_header}
    section_upper = section.upper()
    for name, pat in VERIFIER_PATTERNS.items():
        if re.search(pat, section_upper):
            meta.setdefault("verifiers", []).append(name)
    for name, pat in FRAMEWORK_PATTERNS.items():
        if re.search(pat, section_upper):
            meta.setdefault("frameworks", []).append(name)

    return section.strip(), meta


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def money(v: str) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sections_dir = OUT_DIR / "green_bond_sections"
    sections_dir.mkdir(exist_ok=True)

    # Load text blobs
    blobs = {}
    raws = {}
    for p in sorted(TEXT_DIR.glob("*.txt")):
        raws[p.stem] = p.read_text(errors="replace")
        blobs[p.stem] = re.sub(r"\s+", "", raws[p.stem].upper())
    print(f"Prospectus text files: {len(blobs)}")

    # Upper-case raw texts for matching
    raws_upper = {k: v.upper() for k, v in raws.items()}

    # --- 1. Per-CUSIP prospectus map ---
    with MATCHED.open(newline="") as fh:
        rows = list(csv.DictReader(fh))

    cusip_out = []
    for r in rows:
        cu = (r["CUSIP"] or "").strip().upper()
        matches: list[tuple[str, str]] = []  # (stem, kind)
        if CUSIP_RE.fullmatch(cu):
            for stem in blobs:
                kind = cusip_match(cu, blobs[stem], raws_upper[stem])
                if kind:
                    matches.append((stem, kind))
        kinds = sorted(set(k for _, k in matches))
        cusip_out.append({
            "CUSIP": cu,
            "Issuer_Name": r["Issuer Name"],
            "Issue_Date": r["Issue Date"],
            "Self_reported_Green": r.get("Self-reported Green", ""),
            "Amt_Issued": r.get("Amt Issued", ""),
            "State": r.get("State_Abb_Classified", ""),
            "n_prospectuses": len(matches),
            "match_kind": ";".join(kinds),
            "prospectus_files": ";".join(s for s, _ in matches),
        })

    out_cusip = OUT_DIR / "cusip_prospectus_map.csv"
    with out_cusip.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cusip_out[0].keys()))
        w.writeheader()
        w.writerows(cusip_out)
    covered = sum(1 for r in cusip_out if r["n_prospectuses"] > 0)
    print(f"\nPer-CUSIP map : {out_cusip.relative_to(ROOT)}")
    print(f"  {covered} / {len(cusip_out)} CUSIPs matched to ≥1 prospectus")

    # --- 2. Per-issuance map ---
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in cusip_out:
        groups[(r["Issuer_Name"], r["Issue_Date"])].append(r)

    issuance_out = []
    for (iss, date), grp in sorted(groups.items()):
        cusips = [r["CUSIP"] for r in grp]
        covered = [r for r in grp if r["n_prospectuses"] > 0]
        # Union of prospectus files across all CUSIPs
        all_stems = set()
        for r in grp:
            for s in r["prospectus_files"].split(";"):
                if s:
                    all_stems.add(s)
        if not all_stems and (iss, date) in MANUAL_OVERRIDES:
            all_stems.add(MANUAL_OVERRIDES[(iss, date)])

        issuance_out.append({
            "Issuer_Name": iss,
            "Issue_Date": date,
            "n_CUSIPs": len(cusips),
            "n_CUSIPs_covered": len(covered),
            "Self_reported_Green_any": (
                "Yes" if any(r["Self_reported_Green"] == "Yes" for r in grp) else "No"
            ),
            "Total_Face_Value": f"{sum(money(r['Amt_Issued']) for r in grp):.0f}",
            "Primary_State": grp[0]["State"],
            "n_prospectuses": len(all_stems),
            "prospectus_files": ";".join(sorted(all_stems)),
        })

    out_iss = OUT_DIR / "issuance_prospectus_map.csv"
    with out_iss.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(issuance_out[0].keys()))
        w.writeheader()
        w.writerows(issuance_out)
    covered_iss = sum(1 for r in issuance_out if r["n_prospectuses"] > 0)
    print(f"\nPer-issuance map : {out_iss.relative_to(ROOT)}")
    print(f"  {covered_iss} / {len(issuance_out)} issuances with ≥1 prospectus")

    # --- 3. Green bond section extraction ---
    section_index = []
    for stem, raw in raws.items():
        section, meta = extract_green_section(raw)
        if section is None or len(section) < 200:
            continue
        (sections_dir / f"{stem}.txt").write_text(section, encoding="utf-8")
        section_index.append({
            "prospectus_stem": stem,
            "header_matched": meta.get("header_matched", ""),
            "section_chars": len(section),
            "frameworks": ";".join(meta.get("frameworks", [])),
            "verifiers": ";".join(meta.get("verifiers", [])),
        })

    out_idx = OUT_DIR / "green_bond_sections_index.csv"
    with out_idx.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "prospectus_stem", "header_matched", "section_chars",
            "frameworks", "verifiers",
        ])
        w.writeheader()
        w.writerows(section_index)
    print(f"\nGreen-bond sections extracted: {len(section_index)} files")
    print(f"  index: {out_idx.relative_to(ROOT)}")
    print(f"  sections: {sections_dir.relative_to(ROOT)}/<prospectus>.txt")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
