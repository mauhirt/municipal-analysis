"""
Generate clean worksheets of CUSIPs that are not yet covered by any prospectus.

Inputs:
  raw/bloomberg/cusip_with_assignment_matched.csv  (must have up-to-date 'included')

Outputs:
  processed/codebook/cusips_needing_prospectuses.csv
      Per-CUSIP. One row per uncovered CUSIP.
      Columns: CUSIP, Issuer_Name, Issue_Date, Maturity, Amt_Issued,
               Self_reported_Green, State

  processed/codebook/issuances_needing_prospectuses.csv
      Per-issuance. One row per (Issuer_Name, Issue_Date) group.
      This is the file the coworker should use — one EMMA lookup per row.
      Columns: Issuer_Name, Issue_Date, n_CUSIPs, Self_reported_Green,
               Total_Face_Value, lead_CUSIP, all_CUSIPs, emma_search
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATCHED = ROOT / "raw" / "bloomberg" / "cusip_with_assignment_matched.csv"
OUT_CUSIPS = ROOT / "processed" / "codebook" / "cusips_needing_prospectuses.csv"
OUT_ISSUANCES = ROOT / "processed" / "codebook" / "issuances_needing_prospectuses.csv"


def money(v: str) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def main() -> int:
    with MATCHED.open(newline="") as fh:
        rows = list(csv.DictReader(fh))

    uncov = [r for r in rows if r.get("issuance_covered", r["included"]) == "0"]

    # --- Per-CUSIP file ---
    OUT_CUSIPS.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CUSIPS.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["CUSIP", "Issuer_Name", "Issue_Date", "Maturity",
                    "Amt_Issued", "Self_reported_Green", "State"])
        for r in sorted(uncov, key=lambda x: (x["Issuer Name"],
                                              x["Issue Date"], x["CUSIP"])):
            w.writerow([r["CUSIP"], r["Issuer Name"], r["Issue Date"],
                        r.get("Maturity", ""), r.get("Amt Issued", ""),
                        r.get("Self-reported Green", ""),
                        r.get("State_Abb_Classified", "")])

    # --- Per-issuance file ---
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in uncov:
        groups[(r["Issuer Name"], r["Issue Date"])].append(r)

    with OUT_ISSUANCES.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Issuer_Name", "Issue_Date", "n_CUSIPs",
                    "Self_reported_Green", "Total_Face_Value",
                    "lead_CUSIP", "all_CUSIPs", "emma_search"])
        for (iss, date), grp in sorted(groups.items(),
                                       key=lambda x: (x[0][0], x[0][1])):
            cusips = sorted(r["CUSIP"] for r in grp)
            total = sum(money(r.get("Amt Issued", "")) for r in grp)
            green = "Yes" if any(r.get("Self-reported Green") == "Yes"
                                 for r in grp) else "No"
            w.writerow([iss, date, len(cusips), green, f"{total:.0f}",
                        cusips[0], ";".join(cusips),
                        f"https://emma.msrb.org/Search/Search.aspx?criteria={cusips[0]}"])

    print(f"Uncovered CUSIPs      : {len(uncov)}")
    print(f"Uncovered issuances   : {len(groups)}")
    print(f"  -> {OUT_CUSIPS.relative_to(ROOT)}")
    print(f"  -> {OUT_ISSUANCES.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
