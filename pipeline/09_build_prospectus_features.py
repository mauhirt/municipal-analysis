"""
Build three analysis feature sets from the prospectus corpus:

A. Use-of-Proceeds section extraction
     processed/prospectus_analysis/use_of_proceeds/*.txt
     processed/prospectus_analysis/use_of_proceeds_index.csv

C. Structured issuance metadata (regex-extracted from OS cover pages)
     processed/prospectus_analysis/issuance_metadata.csv
     One row per prospectus with: par amount, Moody's/S&P/Fitch/KBRA
     ratings, tax status (tax-exempt / taxable / AMT), dated date,
     series designation, credit enhancement (bond insurance), bond
     counsel, trustee/paying agent, and lead underwriter.

D. ESG keyword frequency table
     processed/prospectus_analysis/esg_keyword_frequencies.csv
     One row per prospectus × keyword family. Counts per-prospectus
     occurrences of climate / resilience / carbon / renewable / LEED
     / EV / sustainability / emissions / adaptation / mitigation /
     ESG / net-zero / green-jobs, etc.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_DIR = ROOT / "raw/emma/prospectuses_text"
OUT_DIR = ROOT / "processed/prospectus_analysis"


# ---------------------------------------------------------------------------
# A. Use-of-Proceeds extraction
# ---------------------------------------------------------------------------
UOP_HEADER_PATTERNS = [
    r"USE OF PROCEEDS\b",
    r"APPLICATION OF PROCEEDS\b",
    r"ESTIMATED USE OF PROCEEDS\b",
    r"PURPOSES OF THE (BONDS|REFUNDING BONDS|NOTES)\b",
    r"PURPOSE OF THE ISSUE\b",
    r"PURPOSE OF (THIS )?ISSUE\b",
    r"PLAN OF FINANCING\b",
    r"PLAN OF REFUNDING\b",
    r"THE FINANCING PLAN\b",
    r"THE REFINANCING PLAN\b",
]


def _score_is_body(raw_text: str, m: re.Match) -> tuple[int, int]:
    after = raw_text[m.end():m.end() + 200]
    is_toc = bool(re.search(r"\.{5,}|\t[0-9]+\s*$", after))
    return (0 if is_toc else 1, m.start())


def extract_section(raw_text: str, headers: list[str], max_len: int = 10000) -> tuple[str | None, str]:
    """Pick the most-body-like match of any header; trim at next section."""
    text_upper = raw_text.upper()
    best = None
    best_header = None
    for pat in headers:
        matches = list(re.finditer(pat, text_upper))
        if not matches:
            continue
        scored = sorted(matches, key=lambda m: _score_is_body(raw_text, m), reverse=True)
        if _score_is_body(raw_text, scored[0])[0] == 1:
            best = scored[0]
            best_header = scored[0].group()
            break
    if best is None:
        return None, ""
    start = best.start()
    section = raw_text[start:start + max_len]
    next_header = re.search(r"\n[A-Z][A-Z\s,&\-]{14,}(?:\n|$)", section[500:])
    if next_header:
        section = section[:500 + next_header.start()]
    return section.strip(), best_header


# ---------------------------------------------------------------------------
# C. Structured metadata regex extractors
# ---------------------------------------------------------------------------
def extract_par_amount(raw_text: str) -> str:
    """Find the main par amount, usually the largest '$NNN,NNN,NNN' near the cover."""
    # Use only the first 8000 chars (cover page area)
    cover = raw_text[:8000]
    amounts = re.findall(r"\$\s*([0-9]{1,3}(?:,[0-9]{3})+)(?:\.00)?", cover)
    if not amounts:
        return ""
    # Largest amount on cover = par amount (heuristic)
    best = max(amounts, key=lambda s: int(s.replace(",", "")))
    return best


RATING_PATTERNS = {
    # Allow quotes, colons, whitespace between agency name and rating.
    # Moody's ratings: Aaa, Aa1-Aa3, A1-A3, Baa1-Baa3, etc.
    "Moody": r"Moody['’]?s[^A-Za-z]{0,40}['\"“”]?(Aaa|Aa[1-3]|A[1-3]|Baa[1-3]|Ba[1-3]|B[1-3]|Caa[1-3]|Ca|C|NR|WR)['\"“”]?",
    # S&P: AAA, AA+/AA/AA-, A+/A/A-, BBB+/BBB/BBB-, etc.
    "SP":    r"(?:S\s*&\s*P|Standard\s*&\s*Poor['’]?s)[^A-Za-z]{0,40}['\"“”]?(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|CCC[+-]?|CC|C|D|NR)['\"“”]?",
    # Fitch: AAA, AA+, etc. (same as S&P)
    "Fitch": r"Fitch[^A-Za-z]{0,40}['\"“”]?(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|CCC[+-]?|CC|C|D|NR)['\"“”]?",
    # KBRA: same scale as S&P/Fitch
    "KBRA":  r"(?:KBRA|Kroll)[^A-Za-z]{0,40}['\"“”]?(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|CCC[+-]?|CC|C|D|NR)['\"“”]?",
}


def extract_ratings(raw_text: str) -> dict[str, str]:
    """Extract rating strings from near-cover or RATINGS section."""
    cover = raw_text[:15000]  # cover + front matter
    out = {}
    for agency, pat in RATING_PATTERNS.items():
        m = re.search(pat, cover)
        if m:
            out[agency] = m.group(1)
    return out


def extract_tax_status(raw_text: str) -> dict[str, str]:
    """Tax-exempt / taxable, AMT status."""
    head = raw_text[:20000].lower()
    out = {
        "tax_exempt": "",
        "taxable": "",
        "subject_to_amt": "",
    }
    # Tax-exempt — various phrasings in bond-counsel opinions
    if (re.search(r"interest\s+on\s+the\s+[^.]{0,80}(is|are)\s+excluded\s+from\s+gross\s+income", head) or
        re.search(r"exclu(?:ded|sion)\s+from\s+gross\s+income\s+for\s+federal\s+income\s+tax", head) or
        re.search(r"exempt\s+from\s+federal\s+income\s+tax", head)):
        out["tax_exempt"] = "Yes"
    # Taxable — often labeled on cover
    if (re.search(r"\(federally\s+taxable\)|\(taxable\)|fully\s+taxable", head) or
        re.search(r"interest\s+on\s+the\s+[^.]{0,60}(is|are)\s+(?:not\s+)?includ(?:ed|ible)\s+in\s+gross\s+income", head)):
        out["taxable"] = "Yes"
    # AMT
    if re.search(r"not\s+a\s+specific\s+preference\s+item|not\s+an\s+item\s+of\s+tax\s+preference", head):
        out["subject_to_amt"] = "No"
    elif re.search(r"(is|are)\s+a\s+specific\s+preference\s+item|subject\s+to\s+the\s+alternative\s+minimum\s+tax", head):
        out["subject_to_amt"] = "Yes"
    return out


def extract_dated_date(raw_text: str) -> str:
    head = raw_text[:10000]
    m = re.search(r"Dated\s*:?\s*(?:Date of (?:Delivery|Original Delivery)|[A-Z][a-z]+\s+\d{1,2},?\s*\d{4})",
                  head, re.IGNORECASE)
    if m:
        return m.group(0)[:80]
    return ""


def extract_series(raw_text: str) -> str:
    """Most OSs mention a 'Series 20NN[A-Z]' designation on the cover."""
    cover = raw_text[:5000]
    m = re.search(r"(Series\s+20\d{2}\s*[A-Z]?(?:[-–/]\d?)?(?:\s*\([^)]{1,60}\))?)",
                  cover, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def extract_party(raw_text: str, role_patterns: list[str]) -> str:
    """Find the entity named for a given role (e.g. 'as Trustee', 'Bond Counsel')."""
    head = raw_text[:30000]
    for pat in role_patterns:
        m = re.search(pat, head, re.IGNORECASE)
        if m:
            # For patterns without capture group, return the whole match
            name = m.group(1).strip() if m.groups() else m.group(0).strip()
            name = re.sub(r"\s+", " ", name).strip(" ,.;:")
            if 3 < len(name) < 100:
                return name
    return ""


BOND_COUNSEL_PATS = [
    # "In the opinion of [Firm Name], Bond Counsel"
    r"In the opinion of\s+([A-Z][A-Za-z&,.\s]{3,70}?),?\s+Bond Counsel\b",
    # "Bond Counsel: Firm Name"
    r"Bond Counsel:?\s+([A-Z][A-Za-z&,.\s]{3,70}?)(?:,|\.|\n)",
]
TRUSTEE_PATS = [
    r"([A-Z][A-Za-z&,.\s]{3,60}?),?\s+as\s+(?:Trustee|Fiscal Agent|Paying Agent)\b",
    r"(?:Trustee|Fiscal Agent|Paying Agent):?\s+([A-Z][A-Za-z&,.\s]{3,70}?)(?:,|\.|\n)",
]
UNDERWRITER_PATS = [
    # "The Underwriter is firm_name" or "Underwriter: firm_name"
    r"(?:^|\n)\s*Underwriter\s*:?\s*\n?\s*([A-Z][A-Za-z&,.\s]{3,80}?)(?:\n|,(?:\s+as\b|$)|\s+is\s+)",
    r"The\s+(?:Underwriter|Purchaser)\s+(?:is|for\s+the\s+Bonds\s+is)\s+([A-Z][A-Za-z&,.\s]{3,80}?)(?:,|\.|\n)",
    # "UNDERWRITING" section usually ends with firm name
    r"The\s+Underwriters?\s+have\s+agreed.{0,200}?purchase.{0,200}?from\s+the\s+(?:City|District|Authority|Department).{0,200}?at\s+a\s+price\s+of",
    # Cover-page tag like "BofA Securities" or "Piper Sandler & Co." appearing as underwriter footer
    r"(?:Morgan Stanley|Goldman Sachs|BofA Securities|Wells Fargo Securities|RBC Capital Markets|Piper Sandler|Citigroup|JPMorgan|J\.P\. Morgan|Raymond James|Stifel|Hilltop Securities|Siebert Williams Shank|Jefferies|Loop Capital Markets|Ramirez & Co|PNC Capital Markets|Barclays|Truist Securities|KeyBanc Capital Markets|Janney Montgomery Scott|Mesirow Financial|Academy Securities|Roosevelt \& Cross)(?:,?\s+(?:Inc\.?|LLC|L\.P\.?|& Co\.))?",
]
INSURER_PATS = [
    r"bond\s+insurance\s+policy.{0,100}?issued by\s+([A-Z][A-Za-z&,.\s]{3,60}?)(?:,|\.|\n)",
    r"Insured by\s+([A-Z][A-Za-z&,.\s]{3,60}?)(?:,|\.|\n)",
    r"(Assured Guaranty(?:\s+\w+)?|Build America Mutual|BAM\b|AGM|National Public Finance Guarantee)",
]


# ---------------------------------------------------------------------------
# D. ESG keyword families
# ---------------------------------------------------------------------------
ESG_KEYWORDS = {
    "climate":            r"\bclimate(?:\s+change)?\b",
    "resilience":         r"\bresilien(?:ce|cy|t)\b",
    "greenhouse":         r"\bgreenhouse\s*gas|GHG\b",
    "carbon":             r"\bcarbon(?:\s+(?:neutral|dioxide|emissions|footprint|reduction))?\b",
    "net_zero":           r"\bnet[\s-]?zero\b",
    "emissions":          r"\bemissions?\b",
    "decarbonization":    r"\bdecarboniz(?:e|ation|ing)\b",
    "renewable":          r"\brenewable\b",
    "solar":              r"\bsolar\b",
    "wind":               r"\bwind(?:\s+(?:power|energy|farm))?\b",
    "hydro":              r"\bhydro(?:electric|power)\b",
    "energy_efficiency":  r"\benergy\s+efficien(?:cy|t)\b",
    "LEED":               r"\bLEED\b",
    "ev":                 r"\bEV(?:s|[^A-Za-z])|electric\s+vehicles?|charging\s+stations?\b",
    "electrification":    r"\belectrification\b",
    "transit":            r"\bpublic\s+transit|mass\s+transit|bus\s+rapid|light\s+rail\b",
    "sustainability":     r"\bsustainab(?:ility|le)\b",
    "environmental":      r"\benvironmental(?:ly)?\b",
    "adaptation":         r"\badaptation\b",
    "mitigation":         r"\bmitigation\b",
    "ESG":                r"\bESG\b",
    "green_bond":         r"\bgreen\s+bonds?\b",
    "water_quality":      r"\bwater\s+quality|clean\s+water\b",
    "stormwater":         r"\bstormwater\b",
    "wastewater":         r"\bwastewater\b",
    "flood":              r"\bflood(?:ing|plain)?\b",
    "sea_level":          r"\bsea[\s-]?level\s+rise\b",
    "drought":            r"\bdrought\b",
    "wildfire":           r"\bwildfire\b",
    # --- Compliance / regulatory-compulsion family (H1/H4) ---
    "clean_water_act":    r"\bclean\s+water\s+act\b|\bCWA\b",
    "safe_drinking_water": r"\bsafe\s+drinking\s+water\s+act\b|\bSDWA\b",
    "cercla":             r"\bCERCLA\b|\bcomprehensive\s+environmental\s+response\b",
    "npdes":              r"\bNPDES\b|\bnational\s+pollutant\s+discharge\s+elimination\b",
    "consent_decree":     r"\bconsent\s+decree\b",
    "epa_enforcement":    r"\bEPA\s+(?:enforcement|order|administrative\s+order)\b|\benvironmental\s+protection\s+agency\s+(?:enforcement|order)\b",
    "administrative_order": r"\badministrative\s+order\s+(?:on\s+consent|for\s+compliance)?\b",
    "ms4_permit":         r"\bMS4\s+permit\b|\bmunicipal\s+separate\s+storm\s+sewer\s+system\b",
    "compliance_schedule": r"\bcompliance\s+schedule\b",
    "court_order":        r"\bcourt\s+order(?:ed)?\b|\bfederal\s+court\s+order\b",
    "regulatory_mandate": r"\b(?:regulatory|statutory)\s+mandate\b|\brequired\s+by\s+(?:law|federal\s+law|state\s+law)\b",
    "tmdl":               r"\bTMDL\b|\btotal\s+maximum\s+daily\s+load\b",
    "violation":          r"\b(?:regulatory|environmental|permit)\s+violation\b|\bnotice\s+of\s+violation\b",
    "enforcement_action": r"\benforcement\s+action\b",
}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    uop_dir = OUT_DIR / "use_of_proceeds"
    uop_dir.mkdir(parents=True, exist_ok=True)

    # Load texts once
    texts = {}
    for p in sorted(TEXT_DIR.glob("*.txt")):
        texts[p.stem] = p.read_text(errors="replace")
    print(f"Prospectus text files: {len(texts)}")

    uop_rows = []
    meta_rows = []
    kw_rows = []

    for stem, raw in texts.items():
        # --- A. Use of Proceeds ---
        section, header = extract_section(raw, UOP_HEADER_PATTERNS, max_len=12000)
        if section and len(section) >= 300:
            (uop_dir / f"{stem}.txt").write_text(section, encoding="utf-8")
            uop_rows.append({
                "prospectus_stem": stem,
                "header_matched": header,
                "section_chars": len(section),
            })

        # --- C. Structured metadata ---
        ratings = extract_ratings(raw)
        tax = extract_tax_status(raw)
        # Normalize internal whitespace for CSV-friendly values
        def _clean(s: str) -> str:
            return re.sub(r"\s+", " ", s).strip() if s else ""
        meta_rows.append({
            "prospectus_stem": stem,
            "par_amount_cover": extract_par_amount(raw),
            "series_designation": _clean(extract_series(raw)),
            "dated_date": _clean(extract_dated_date(raw)),
            "rating_Moody": ratings.get("Moody", ""),
            "rating_SP": ratings.get("SP", ""),
            "rating_Fitch": ratings.get("Fitch", ""),
            "rating_KBRA": ratings.get("KBRA", ""),
            "tax_exempt": tax["tax_exempt"],
            "taxable": tax["taxable"],
            "subject_to_amt": tax["subject_to_amt"],
            "bond_counsel": extract_party(raw, BOND_COUNSEL_PATS),
            "trustee_or_paying_agent": extract_party(raw, TRUSTEE_PATS),
            "underwriter_or_purchaser": extract_party(raw, UNDERWRITER_PATS),
            "credit_enhancement": extract_party(raw, INSURER_PATS),
        })

        # --- D. ESG keyword frequencies ---
        counts: dict[str, int] = {}
        total_words = max(1, len(re.findall(r"\b\w+\b", raw)))
        for name, pat in ESG_KEYWORDS.items():
            counts[name] = len(re.findall(pat, raw, re.IGNORECASE))
        kw_rows.append({
            "prospectus_stem": stem,
            "total_words": total_words,
            **counts,
        })

    # Write outputs
    with (OUT_DIR / "use_of_proceeds_index.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["prospectus_stem", "header_matched", "section_chars"])
        w.writeheader()
        w.writerows(uop_rows)

    with (OUT_DIR / "issuance_metadata.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(meta_rows[0].keys()))
        w.writeheader()
        w.writerows(meta_rows)

    with (OUT_DIR / "esg_keyword_frequencies.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(kw_rows[0].keys()))
        w.writeheader()
        w.writerows(kw_rows)

    print(f"\nA. Use-of-Proceeds sections : {len(uop_rows)} / {len(texts)}")
    print(f"   -> {uop_dir.relative_to(ROOT)}")
    print(f"   -> processed/prospectus_analysis/use_of_proceeds_index.csv")

    print(f"\nC. Structured metadata      : {len(meta_rows)} prospectuses")
    print(f"   -> processed/prospectus_analysis/issuance_metadata.csv")
    # Quick summary of fill rates
    cols = ["par_amount_cover", "rating_Moody", "rating_SP", "rating_Fitch",
            "tax_exempt", "bond_counsel", "trustee_or_paying_agent",
            "underwriter_or_purchaser", "credit_enhancement"]
    for c in cols:
        n = sum(1 for r in meta_rows if r[c])
        print(f"     {c:25s}: {n}/{len(meta_rows)} filled")

    print(f"\nD. ESG keyword frequencies  : {len(kw_rows)} prospectuses × {len(ESG_KEYWORDS)} keywords")
    print(f"   -> processed/prospectus_analysis/esg_keyword_frequencies.csv")
    total_kw = Counter()
    for r in kw_rows:
        for k in ESG_KEYWORDS:
            total_kw[k] += r[k]
    print("   Top keywords across corpus:")
    for k, v in total_kw.most_common(10):
        n_docs = sum(1 for r in kw_rows if r[k] > 0)
        print(f"     {k:22s} {v:7d} total, in {n_docs:3d} prospectuses")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
