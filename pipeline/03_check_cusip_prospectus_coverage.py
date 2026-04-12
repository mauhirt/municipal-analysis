"""
Check whether every CUSIP issued by a matched city (is_in_578_panel == True)
in raw/bloomberg/cusip_with_assignment.csv is covered by at least one of the
extracted prospectus texts in raw/emma/prospectuses_text/.

A CUSIP is 'covered' if its 9-char code appears in at least one prospectus
text after collapsing all whitespace (so 'XXXXXX XX1' and 'XXXXXX\\nXX1' on
PDF cover pages also match the compact 'XXXXXXXX1' form).

Outputs
-------
processed/codebook/cusip_prospectus_coverage.csv
    One row per matched CUSIP with Issuer, City, Issue Date, green flag,
    coverage flag, and the list of prospectus files that contain the code.
Stdout: summary counts (overall, green-only, per-issuer).
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CUSIP_CSV = ROOT / "raw" / "bloomberg" / "cusip_with_assignment.csv"
TEXT_DIR = ROOT / "raw" / "emma" / "prospectuses_text"
OUT_CSV = ROOT / "processed" / "codebook" / "cusip_prospectus_coverage.csv"

CUSIP_RE = re.compile(r"[0-9A-Z]{9}")


def norm(s: str | None) -> str:
    return (s or "").strip().upper()


def main() -> int:
    with CUSIP_CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))

    matched = [r for r in rows if r.get("is_in_578_panel", "").strip().lower() == "true"]
    matched_cusips = {norm(r["CUSIP"]) for r in matched if norm(r["CUSIP"])}
    matched_by_cusip: dict[str, list[dict]] = defaultdict(list)
    for r in matched:
        matched_by_cusip[norm(r["CUSIP"])].append(r)

    malformed = {c for c in matched_cusips if not CUSIP_RE.fullmatch(c)}

    # Build compact (whitespace-stripped) uppercase blob per prospectus
    blobs: dict[str, str] = {}
    for p in sorted(TEXT_DIR.glob("*.txt")):
        up = p.read_text(encoding="utf-8", errors="replace").upper()
        blobs[p.name] = re.sub(r"\s+", "", up)

    found: dict[str, list[str]] = defaultdict(list)
    for c in matched_cusips:
        if not CUSIP_RE.fullmatch(c):
            continue
        for name, blob in blobs.items():
            if c in blob:
                found[c].append(name)

    covered = {c for c in matched_cusips if found[c]}
    uncovered = matched_cusips - covered

    # Green subset
    def is_green(c: str) -> bool:
        return any(rr["Self-reported Green"] == "Yes" for rr in matched_by_cusip[c])

    green_matched = {c for c in matched_cusips if is_green(c)}
    green_covered = green_matched & covered

    # Issuer-level coverage for green
    iss_total: Counter[str] = Counter()
    iss_cov: Counter[str] = Counter()
    for c in green_matched:
        iss = matched_by_cusip[c][0]["Issuer Name"]
        iss_total[iss] += 1
        if c in covered:
            iss_cov[iss] += 1

    fully   = [i for i in iss_total if iss_cov[i] == iss_total[i]]
    none_   = [i for i in iss_total if iss_cov[i] == 0]
    partial = [i for i in iss_total if 0 < iss_cov[i] < iss_total[i]]

    print(f"Prospectus text files scanned          : {len(blobs)}")
    print(f"Matched-city CUSIPs (578-panel, unique): {len(matched_cusips)}")
    print(f"  malformed (not 9-char alnum)         : {len(malformed)}")
    print(f"Covered by at least one prospectus     : "
          f"{len(covered)} ({100*len(covered)/len(matched_cusips):.1f}%)")
    print(f"Not covered                            : {len(uncovered)}")
    print()
    print(f"Self-reported Green matched CUSIPs     : {len(green_matched)}")
    print(f"  covered                              : "
          f"{len(green_covered)} ({100*len(green_covered)/max(1,len(green_matched)):.1f}%)")
    print(f"  uncovered                            : {len(green_matched - green_covered)}")
    print()
    print(f"Green-bond issuers in 578 panel        : {len(iss_total)}")
    print(f"  fully covered                        : {len(fully)}")
    print(f"  partially covered                    : {len(partial)}")
    print(f"  not covered at all                   : {len(none_)}")
    print()
    print("Top 15 green-bond issuers with uncovered CUSIPs:")
    missing: Counter[str] = Counter()
    for i, total in iss_total.items():
        missing[i] = total - iss_cov[i]
    for iss, n in missing.most_common(15):
        if n == 0:
            continue
        print(f"  {iss_cov[iss]:4d}/{iss_total[iss]:<4d}  "
              f"({100*iss_cov[iss]/iss_total[iss]:5.1f}%)  {iss}")

    # Per-CUSIP detail CSV
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "CUSIP", "Issuer_Name", "City", "Issue_Date", "Amt_Issued",
            "Self_reported_Green", "ESG_Assurance_Providers",
            "covered", "n_prospectus_matches", "prospectus_filenames",
        ])
        for c in sorted(matched_cusips, key=lambda x: (x in covered, x)):
            rr = matched_by_cusip[c][0]
            files = sorted(found.get(c, []))
            w.writerow([
                c, rr["Issuer Name"], rr.get("city_name_crosswalk", ""),
                rr.get("Issue Date", ""), rr.get("Amt Issued", ""),
                rr.get("Self-reported Green", ""),
                rr.get("ESG Assurance Providers", ""),
                c in covered, len(files), ";".join(files),
            ])
    print()
    print(f"Per-CUSIP detail written to {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
