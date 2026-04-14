"""
Repair malformed CUSIPs in raw/bloomberg/cusip_with_assignment_matched.csv
and recompute the 'included' coverage flag against the prospectus texts.

Strategy
--------
A valid CUSIP is 9 alphanumeric characters with a self-checking 9th digit
(modulus-10 algorithm — alternate weights 1,2,…, sum-the-digits if the
weighted value exceeds 9). We treat a row as malformed if its CUSIP is not
9-char alnum.

For each malformed CUSIP we:
  1. Anchor the issuer prefix using the most common 6-char prefix among the
     same issuer's other CUSIPs in the *full* cusip_with_assignment.csv.
  2. Generate single-edit candidates (drop char, replace underscore, insert
     a missing char so the prefix matches the anchor).
  3. Keep only candidates that (a) pass the CUSIP check-digit validator,
     (b) match the issuer prefix anchor, and (c) are not already present
     among the issuer's known sibling CUSIPs (avoid duplicates).
  4. If exactly one candidate survives, apply it. Otherwise log and skip.

Outputs
-------
Updates raw/bloomberg/cusip_with_assignment_matched.csv in place
(corrected CUSIP, recomputed 'included', plus a new 'cusip_repaired' flag).
Writes processed/codebook/cusip_repairs.csv with original→corrected mapping.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULL_CSV = ROOT / "raw" / "bloomberg" / "cusip_with_assignment.csv"
MATCHED_CSV = ROOT / "raw" / "bloomberg" / "cusip_with_assignment_matched.csv"
TEXT_DIR = ROOT / "raw" / "emma" / "prospectuses_text"
REPAIR_LOG = ROOT / "processed" / "codebook" / "cusip_repairs.csv"

CUSIP_RE = re.compile(r"[0-9A-Z]{9}")
ALPHANUM = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ---------------------------------------------------------------------------
# CUSIP check-digit
# ---------------------------------------------------------------------------
def _char_value(c: str) -> int | None:
    if c.isdigit():
        return int(c)
    if "A" <= c <= "Z":
        return ord(c) - ord("A") + 10
    return None


def cusip_check_digit(eight: str) -> int | None:
    """Return the modulus-10 check digit for the 8-char CUSIP body."""
    if len(eight) != 8:
        return None
    total = 0
    for i, c in enumerate(eight):
        v = _char_value(c)
        if v is None:
            return None
        if i % 2 == 1:  # 0-indexed; even positions (1-indexed) get weight 2
            v *= 2
        total += (v // 10) + (v % 10)
    return (10 - total % 10) % 10


def is_valid_cusip(cusip: str) -> bool:
    if not CUSIP_RE.fullmatch(cusip):
        return False
    expected = cusip_check_digit(cusip[:8])
    return expected is not None and str(expected) == cusip[8]


# ---------------------------------------------------------------------------
# Repair candidate generation
# ---------------------------------------------------------------------------
def candidates(bad: str, prefix_anchor: str) -> set[str]:
    """Generate plausible 9-char alnum corrections from `bad`."""
    out: set[str] = set()
    bad = bad.upper()

    # 1. If bad has an underscore: replace it with each alnum char
    if "_" in bad:
        for ch in ALPHANUM:
            cand = bad.replace("_", ch, 1)
            # may still be wrong length; iterate further below
            if len(cand) == 9:
                out.add(cand)
            elif len(cand) > 9:
                # also try dropping the underscore entirely
                pass
        # also try dropping the underscore
        dropped = bad.replace("_", "", 1)
        if len(dropped) == 9:
            out.add(dropped)
        elif len(dropped) == 8:
            # then insert any alnum at any position
            for i in range(9):
                for ch in ALPHANUM:
                    out.add(dropped[:i] + ch + dropped[i:])

    # 2. If too long (10 chars), drop any one char
    if len(bad) == 10:
        for i in range(10):
            cand = bad[:i] + bad[i + 1:]
            if len(cand) == 9:
                out.add(cand)

    # 3. If too short (8 chars), insert any alnum at any position
    if len(bad) == 8:
        for i in range(9):
            for ch in ALPHANUM:
                out.add(bad[:i] + ch + bad[i:])

    # Filter to alphanumeric and prefix-anchored
    return {c for c in out
            if CUSIP_RE.fullmatch(c) and c.startswith(prefix_anchor)}


# ---------------------------------------------------------------------------
# Repair driver
# ---------------------------------------------------------------------------
def main() -> int:
    # Build anchor map: for each issuer, find the dominant 6-char prefix
    with FULL_CSV.open(newline="") as fh:
        full_rows = list(csv.DictReader(fh))

    issuer_prefix: dict[str, str] = {}
    issuer_known: dict[str, set[str]] = {}
    iss_pref_count: dict[str, Counter] = {}
    for r in full_rows:
        iss = r["Issuer Name"]
        c = (r["CUSIP"] or "").strip().upper()
        if CUSIP_RE.fullmatch(c):
            iss_pref_count.setdefault(iss, Counter())[c[:6]] += 1
            issuer_known.setdefault(iss, set()).add(c)
    for iss, ctr in iss_pref_count.items():
        issuer_prefix[iss] = ctr.most_common(1)[0][0]

    # Load matched file
    with MATCHED_CSV.open(newline="") as fh:
        matched_rows = list(csv.DictReader(fh))
    fieldnames = list(matched_rows[0].keys())
    if "cusip_repaired" not in fieldnames:
        fieldnames.append("cusip_repaired")

    # Repair pass
    repairs = []
    for row in matched_rows:
        row.setdefault("cusip_repaired", "0")
        cusip = (row["CUSIP"] or "").strip().upper()
        if CUSIP_RE.fullmatch(cusip):
            continue  # well-formed; skip
        iss = row["Issuer Name"]
        anchor = issuer_prefix.get(iss, "")
        if not anchor:
            print(f"NO ANCHOR for issuer {iss!r}; skipping CUSIP {cusip!r}")
            continue

        cands = candidates(cusip, anchor)
        valid = {c for c in cands if is_valid_cusip(c)}
        new_only = valid - issuer_known.get(iss, set())  # avoid existing dups

        if len(new_only) == 1:
            chosen = next(iter(new_only))
        elif len(valid) == 1:
            chosen = next(iter(valid))
        else:
            print(f"AMBIGUOUS for {cusip!r} (issuer={iss!r}): {sorted(valid)}")
            continue

        repairs.append({
            "ID": row["ID"],
            "Issuer Name": iss,
            "Issue Date": row.get("Issue Date", ""),
            "original_CUSIP": cusip,
            "corrected_CUSIP": chosen,
            "anchor_prefix": anchor,
            "n_candidates_valid": len(valid),
        })
        row["CUSIP"] = chosen
        row["cusip_repaired"] = "1"

    # Recompute 'included' against prospectus texts
    blobs = []
    for p in sorted(TEXT_DIR.glob("*.txt")):
        up = p.read_text(encoding="utf-8", errors="replace").upper()
        blobs.append(re.sub(r"\s+", "", up))
    n_inc = 0
    for row in matched_rows:
        c = (row["CUSIP"] or "").strip().upper()
        if CUSIP_RE.fullmatch(c) and any(c in b for b in blobs):
            row["included"] = "1"
            n_inc += 1
        else:
            row["included"] = "0"

    # Write back
    with MATCHED_CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(matched_rows)

    # Write repair log
    REPAIR_LOG.parent.mkdir(parents=True, exist_ok=True)
    with REPAIR_LOG.open("w", newline="") as fh:
        if repairs:
            w = csv.DictWriter(fh, fieldnames=list(repairs[0].keys()))
            w.writeheader()
            w.writerows(repairs)

    print()
    print(f"Repaired CUSIPs: {len(repairs)}")
    for r in repairs:
        print(f"  {r['original_CUSIP']:>11s} -> {r['corrected_CUSIP']:9s}  "
              f"({r['Issuer Name']})")
    print()
    print(f"Total matched rows : {len(matched_rows)}")
    print(f"included == 1      : {n_inc} ({100*n_inc/len(matched_rows):.1f}%)")
    print(f"Repair log         : {REPAIR_LOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
