"""
Discretionary-bond validity check (for H4).

Problem: Bonds flagged as 'not federally compelled' (no consent_decree
keyword) may still be driven by *state* regulation — green building
codes (CALGreen/Title 24), Renewable Portfolio Standards, state climate
acts, LEED requirements, voter-approved bond measures, etc.

This script searches the primary prospectus text for state-level
regulatory drivers and produces:

  processed/prospectus_analysis/discretionary_validity_check.csv
    One row per CUSIP currently classified as 'discretionary'
    (compelled_by_text == 0), with counts of state-compulsion
    keywords and a binary 'state_compelled' flag.

  processed/prospectus_analysis/discretionary_validity_summary.md
    Narrative with the fraction of 'discretionary' bonds that
    actually disclose state-level compulsion.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AN = ROOT / "processed/prospectus_analysis"
TEXT_DIR = ROOT / "raw/emma/prospectuses_text"

# State-level regulatory drivers that could make a bond *project*
# legally required even without federal enforcement.
# Patterns are case-insensitive. Each matches a phrase that implies
# "the project had to be done this way" or "we're required to do this".
STATE_COMPULSION = {
    # Green building codes
    "calgreen":           r"\bCALGreen\b|California\s+Green\s+Building\s+Standards?",
    "title_24":           r"\bTitle\s+24\b",
    "energy_code":        r"\bstate\s+energy\s+code|state\s+building\s+code.{0,60}(?:energy|green)",
    "leed_required":      r"LEED.{0,80}(?:required|mandated|certified|standard)|required.{0,30}LEED",
    "energy_star":        r"\bENERGY\s*STAR\b",
    "ashrae":             r"\bASHRAE\s+(?:90\.1|189)\b",

    # State climate/GHG mandates (mostly California)
    "sb_32":              r"\bSB\s*32\b|Senate\s+Bill\s+32",
    "ab_32":              r"\bAB\s*32\b|Assembly\s+Bill\s+32|California\s+Global\s+Warming\s+Solutions\s+Act",
    "cap_and_trade":      r"\bcap[\s\-]and[\s\-]trade\b",
    "state_ghg_target":   r"(?:state|California|New York|Oregon|Washington|Massachusetts).{0,40}(?:greenhouse\s+gas|GHG|emissions)\s+(?:reduction|target|mandate)",

    # Renewable Portfolio Standards
    "rps":                r"\bRenewable\s+Portfolio\s+Standard|\bRPS\b",
    "renewable_mandate":  r"required\s+(?:by\s+law\s+)?to\s+(?:procure|purchase|generate).{0,40}renewable",
    "clean_energy_mandate": r"\bclean\s+energy\s+standard\b|clean\s+energy\s+mandate",

    # Executive orders and state statutes that drive spending
    "executive_order":    r"\b(?:state|governor['’]?s|presidential)?\s*executive\s+order\s+(?:no\.?\s*)?\d",
    "state_statute":      r"pursuant\s+to\s+(?:state\s+)?(?:statute|law|code\s+section)\s+[A-Z\d]",
    "state_law_required": r"required\s+by\s+(?:state\s+law|California\s+law|[A-Z][a-z]+\s+[A-Z][a-z]+\s+law)",

    # Voter-approved bond mandates (not regulation but political compulsion)
    "voter_approved":     r"(?:voter[\s\-]approved|approved\s+by\s+(?:the\s+)?voters|ballot\s+measure|general\s+obligation\s+bond\s+measure)",
    "measure_prop":       r"\b(?:Measure|Proposition)\s+[A-Z0-9]{1,3}\b",

    # Rate covenants / fiscal compulsion
    "rate_covenant":      r"rate\s+covenant|required\s+to\s+(?:set|establish).{0,40}rates",

    # Seismic / disaster mandates (often trigger state-required retrofits)
    "seismic_retrofit":   r"seismic\s+(?:retrofit|upgrade|safety)\s+(?:required|mandated|law)",
    "unsafe_building":    r"unsafe\s+(?:structure|building)\s+ordinance",

    # General "required by" patterns near project descriptions
    "required_by_law":    r"required\s+by\s+(?:federal\s+or\s+)?(?:state|local)\s+law",
    "statutory_mandate":  r"statutory\s+mandate|legislative\s+mandate",
}


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def to_int(s: str, default: int = 0) -> int:
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


def main() -> int:
    intensity = read_csv(AN / "bond_label_intensity.csv")
    compliance = {r["CUSIP"]: r for r in read_csv(AN / "bond_compliance_score.csv")}

    # Load raw prospectus texts (not whitespace-collapsed — we want context)
    raws = {}
    for p in sorted(TEXT_DIR.glob("*.txt")):
        raws[p.stem] = p.read_text(errors="replace")

    # Count state-compulsion keyword hits for each prospectus
    state_counts: dict[str, dict[str, int]] = {}
    for stem, text in raws.items():
        counts = {}
        for name, pat in STATE_COMPULSION.items():
            counts[name] = len(re.findall(pat, text, re.IGNORECASE))
        state_counts[stem] = counts

    # Build output: one row per discretionary (compelled_by_text=0) CUSIP
    out_rows = []
    for r in intensity:
        cusip = r["CUSIP"]
        comp = compliance.get(cusip)
        if not comp:
            continue
        # Only examine bonds NOT flagged as federally compelled
        if comp["compelled_by_text"] == "1":
            continue
        primary = r["primary_prospectus"]
        counts = state_counts.get(primary, {k: 0 for k in STATE_COMPULSION})
        total_state_hits = sum(counts.values())

        # SUBSTANTIVE state regulatory compulsion: external mandate that
        # requires the specific project to be green. Excludes procedural
        # items (voter approval, rate covenants) that are standard bond
        # structures, not evidence of external compulsion.
        substantive_green_mandate = [
            # State green building codes
            "calgreen", "title_24", "leed_required", "ashrae", "energy_code",
            # State climate / GHG laws
            "sb_32", "ab_32", "cap_and_trade", "state_ghg_target",
            # Renewable Portfolio Standards
            "rps", "renewable_mandate", "clean_energy_mandate",
        ]
        # Direct statutory compulsion (broader, but still external)
        state_legal_mandate = [
            "state_law_required", "required_by_law", "statutory_mandate",
        ]
        state_compelled = "1" if any(counts[k] > 0 for k in substantive_green_mandate) else "0"
        state_legal_compelled = "1" if any(counts[k] > 0 for k in state_legal_mandate) else "0"
        # Voter-approved is procedural, reported separately
        voter_compelled = "1" if (counts["voter_approved"] > 0
                                   or counts["measure_prop"] > 0) else "0"

        out_rows.append({
            "CUSIP": cusip,
            "Issuer_Name": r["Issuer_Name"],
            "Issue_Date": r["Issue_Date"],
            "primary_prospectus": primary,
            "bloomberg_self_reported_green": r["bloomberg_self_reported_green"],
            "bloomberg_industry": r["bloomberg_industry"],
            "federally_compelled": "0",  # by definition here
            "state_compelled_substantive": state_compelled,
            "state_legal_compelled": state_legal_compelled,
            "voter_compelled": voter_compelled,
            "n_state_compulsion_hits": total_state_hits,
            **{f"kw_{k}": counts[k] for k in STATE_COMPULSION},
        })

    out_csv = AN / "discretionary_validity_check.csv"
    with out_csv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    # Summary stats
    n_disc = len(out_rows)
    n_state = sum(1 for r in out_rows if r["state_compelled_substantive"] == "1")
    n_legal = sum(1 for r in out_rows if r["state_legal_compelled"] == "1")
    n_voter = sum(1 for r in out_rows if r["voter_compelled"] == "1")
    n_substantive_any = sum(1 for r in out_rows
                             if r["state_compelled_substantive"] == "1"
                             or r["state_legal_compelled"] == "1")
    n_truly_disc_narrow = n_disc - n_state  # excludes only substantive green mandates
    n_truly_disc_strict = n_disc - n_substantive_any  # excludes legal mandates too

    # Breakdown by Bloomberg industry
    from collections import defaultdict
    by_ind = defaultdict(lambda: [0, 0, 0])  # total, state_substantive, voter
    for r in out_rows:
        ind = r["bloomberg_industry"] or "(blank)"
        by_ind[ind][0] += 1
        if r["state_compelled_substantive"] == "1":
            by_ind[ind][1] += 1
        if r["voter_compelled"] == "1":
            by_ind[ind][2] += 1

    # Which specific state-compulsion keywords are most common?
    kw_totals = Counter()
    for r in out_rows:
        for k in STATE_COMPULSION:
            if to_int(r[f"kw_{k}"]) > 0:
                kw_totals[k] += 1

    # Write markdown summary
    md = []
    md.append("# Discretionary-Bond Validity Check (H4)\n")
    md.append(
        f"Among the **{n_disc} CUSIPs** currently classified as 'discretionary' "
        f"(no consent-decree / EPA-enforcement language in the prospectus), "
        f"how many actually disclose **state-level regulatory compulsion**?\n"
    )
    md.append("## Headline\n")
    md.append("**Definitions:**\n"
              "- *Substantive green mandate*: state green building code (CALGreen, Title 24, "
              "LEED requirement, ASHRAE), state GHG/climate statute (AB 32, SB 32, cap-and-trade, "
              "state GHG target), or Renewable Portfolio Standard.\n"
              "- *State legal mandate (broader)*: prospectus uses phrases like "
              "'required by state law', 'statutory mandate'.\n"
              "- *Voter-approved*: prospectus describes the bond as authorized by ballot "
              "measure/proposition. **Not external regulatory compulsion**, but political "
              "commitment constrained by voter mandate.\n")
    md.append(f"- {n_state} / {n_disc} ({100*n_state/n_disc:.1f}%) disclose a **substantive state green mandate**.")
    md.append(f"- {n_legal} / {n_disc} ({100*n_legal/n_disc:.1f}%) invoke a **general state legal mandate** ('required by state law').")
    md.append(f"- {n_substantive_any} / {n_disc} ({100*n_substantive_any/n_disc:.1f}%) have **either** type of state compulsion.")
    md.append(f"- {n_voter} / {n_disc} ({100*n_voter/n_disc:.1f}%) were **voter-approved** (procedural, not regulatory).")
    md.append("")
    md.append(f"- **{n_truly_disc_strict} / {n_disc} ({100*n_truly_disc_strict/n_disc:.1f}%) appear truly discretionary** "
              "with neither substantive nor broad legal state compulsion disclosed.\n")
    md.append("")
    md.append("## Breakdown by Bloomberg industry (substantive state mandate rate)\n")
    md.append("| Industry | N discretionary | substantive state mandate | voter-approved |")
    md.append("|---|---:|---:|---:|")
    for ind, (n, s, v) in sorted(by_ind.items(), key=lambda x: -x[1][0]):
        md.append(f"| {ind[:60]} | {n} | {s} ({100*s/n:.0f}%) | {v} ({100*v/n:.0f}%) |")
    md.append("")
    md.append("## Most-common state-compulsion keyword hits\n")
    md.append("| Keyword | # discretionary CUSIPs with ≥1 hit |")
    md.append("|---|---:|")
    for k, n in kw_totals.most_common():
        md.append(f"| `{k}` | {n} ({100*n/n_disc:.1f}%) |")
    md.append("")
    md.append("## Interpretation for H4\n")
    md.append(
        f"- If the 'truly discretionary' fraction is high (>70%), H4's "
        f"compelled-vs-discretionary distinction is clean and the main panel "
        f"result on discretionary green bonds genuinely identifies voluntary "
        f"environmental commitment.\n"
        f"- If the 'state-compelled' fraction is high (>30%), the "
        f"`compelled_by_text` flag undercounts compulsion — many bonds "
        f"the panel treats as 'voluntary green' are actually issued to "
        f"comply with state-level regulation. The paper should either "
        f"(a) expand the compelled flag to include state compulsion, or "
        f"(b) acknowledge in the paper that 'discretionary' in the "
        f"federal-enforcement sense includes state-mandated projects.\n"
    )
    md.append(
        f"- **Current result: {100*n_truly_disc_strict/n_disc:.1f}% of 'discretionary' "
        f"bonds show no state compulsion** ({n_truly_disc_strict} CUSIPs). "
        f"{'Supports' if n_truly_disc_strict/n_disc > 0.7 else 'Qualifies' if n_truly_disc_strict/n_disc > 0.5 else 'Substantially weakens'} "
        f"the H4 interpretation of a meaningful discretionary channel.\n"
    )

    out_md = AN / "discretionary_validity_summary.md"
    out_md.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"Output: {out_csv.relative_to(ROOT)}")
    print(f"Output: {out_md.relative_to(ROOT)}\n")
    print(f"Discretionary CUSIPs                       : {n_disc}")
    print(f"  substantive state green mandate          : {n_state} ({100*n_state/n_disc:.1f}%)")
    print(f"  general state legal mandate              : {n_legal} ({100*n_legal/n_disc:.1f}%)")
    print(f"  any state compulsion (substantive+legal) : {n_substantive_any} ({100*n_substantive_any/n_disc:.1f}%)")
    print(f"  voter-approved (procedural)              : {n_voter} ({100*n_voter/n_disc:.1f}%)")
    print(f"  truly discretionary (no state signal)    : {n_truly_disc_strict} ({100*n_truly_disc_strict/n_disc:.1f}%)")
    print("\nTop state-compulsion keywords in discretionary bonds:")
    for k, n in kw_totals.most_common(10):
        print(f"  {k:25s} {n} ({100*n/n_disc:.1f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
