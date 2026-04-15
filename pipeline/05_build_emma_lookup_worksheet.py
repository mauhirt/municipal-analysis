"""
Build a lookup worksheet for uncovered issuances so the user can find the
missing Official Statement URLs on EMMA.

Groups 'included == 0' rows in cusip_with_assignment_matched.csv by
(Issuer Name, Issue Date) and, for each group, writes one row with:
  - Issuer, Issue Date, # CUSIPs, first few CUSIPs, total face amount
  - A clickable EMMA Security Details URL for the lead CUSIP
  - A clickable EMMA Search URL (criteria = CUSIP)
  - A Google site-restricted search URL as a fallback

Output: processed/codebook/emma_lookup_uncovered_issuances.csv
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
MATCHED = ROOT / "raw" / "bloomberg" / "cusip_with_assignment_matched.csv"
OUT = ROOT / "processed" / "codebook" / "emma_lookup_uncovered_issuances.csv"


def money(v: str) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def main() -> int:
    with MATCHED.open(newline="") as fh:
        rows = list(csv.DictReader(fh))

    uncov = [r for r in rows if r["included"] == "0"]
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in uncov:
        groups[(r["Issuer Name"], r["Issue Date"])].append(r)

    out_rows = []
    for (iss, date), group in sorted(groups.items(),
                                     key=lambda x: (x[0][1], x[0][0])):
        group_sorted = sorted(group, key=lambda r: r["CUSIP"])
        lead = group_sorted[0]["CUSIP"]
        cusip_list = ";".join(r["CUSIP"] for r in group_sorted)
        total_face = sum(money(r["Amt Issued"]) for r in group_sorted)
        green = "Yes" if any(r["Self-reported Green"] == "Yes"
                             for r in group) else "No"
        out_rows.append({
            "Issuer_Name": iss,
            "Issue_Date": date,
            "n_CUSIPs": len(group),
            "Self_reported_Green": green,
            "Total_Face_Value": f"{total_face:.0f}",
            "lead_CUSIP": lead,
            "all_CUSIPs": cusip_list,
            # EMMA Security Details page (ToS-gated; opens in browser fine)
            "emma_security_details":
                f"https://emma.msrb.org/Security/Details/{lead}",
            # EMMA Search page by CUSIP
            "emma_search":
                f"https://emma.msrb.org/Search/Search.aspx?criteria={lead}",
            # Google fallback
            "google_site_search":
                "https://www.google.com/search?q=" + quote(
                    f"site:emma.msrb.org {lead} \"Official Statement\""),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    n_green = sum(1 for r in out_rows if r["Self_reported_Green"] == "Yes")
    print(f"Uncovered CUSIPs              : {len(uncov)}")
    print(f"Unique uncovered issuances    : {len(out_rows)}")
    print(f"  of which Self-reported Green: {n_green}")
    print(f"Worksheet written to          : {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
