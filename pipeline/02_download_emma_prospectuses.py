"""
02_download_emma_prospectuses.py — Download bond Official Statements from MSRB EMMA
====================================================================================
Fetches Official Statement PDFs for every CUSIP flagged `is_in_578_panel == True`
in raw/bloomberg/cusip_with_assignment.csv (≈3,276 CUSIPs across ~124 issuers
mapped to the 578-city panel).

Because an Official Statement covers an entire bond issue, many CUSIPs in the
same series share a single OS PDF. The script therefore fetches the security
details page for each CUSIP, extracts the OS document ID, and deduplicates
downloads against what is already on disk.

Outputs
-------
raw/bloomberg/prospectuses/pdfs/<doc_id>.pdf       Downloaded OS PDFs (dedup'd)
raw/bloomberg/prospectuses/manifest.csv            CUSIP -> OS mapping / status
raw/bloomberg/prospectuses/fetch_log.jsonl         Append-only event log

The script is resume-safe: CUSIPs already present in manifest.csv are skipped
(unless --retry-failed is passed, in which case only `error` rows are retried).

⚠️  LEGAL / TERMS OF USE
------------------------
MSRB EMMA's Terms of Use prohibit automated collection of content without prior
written permission. Before running this script for any non-trivial batch, email
MSRBSupport@msrb.org to request research access, or obtain the MSRB's bulk data
subscription product which provides Official Statements in bulk. Running this
script without authorisation may violate MSRB's terms.

The default throttle (1.5 s between requests) is deliberately slow to minimise
impact on EMMA's public infrastructure.

Usage
-----
    python pipeline/02_download_emma_prospectuses.py                  # full run
    python pipeline/02_download_emma_prospectuses.py --limit 20       # test 20
    python pipeline/02_download_emma_prospectuses.py --cusip 544495ZK3
    python pipeline/02_download_emma_prospectuses.py --retry-failed
    python pipeline/02_download_emma_prospectuses.py --sleep 2.5
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import requests

# ───────────────────────────── paths ─────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
SRC_CSV = ROOT / "raw" / "bloomberg" / "cusip_with_assignment.csv"
OUT_DIR = ROOT / "raw" / "bloomberg" / "prospectuses"
PDF_DIR = OUT_DIR / "pdfs"
MANIFEST = OUT_DIR / "manifest.csv"
LOG_FILE = OUT_DIR / "fetch_log.jsonl"

# ─────────────────────────── constants ───────────────────────────
BASE = "https://emma.msrb.org"
SECURITY_URL = BASE + "/Security/Details/{cusip}"
DISCLAIMER_URL = BASE + "/Disclaimer.aspx"
# Known-valid CUSIP used as a stable referer when (re-)accepting the disclaimer
DISCLAIMER_REFERER_CUSIP = "544495ZK3"  # LADWP 2013 — always present on EMMA

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

MANIFEST_FIELDS = [
    "cusip",
    "issuer_name",
    "city",
    "state",
    "issue_date",
    "status",            # found | no_os | invalid_cusip | error | http_error
    "os_doc_id",         # filename stem, e.g. EA531719-EA414230-EA811102
    "os_url",            # absolute URL
    "os_display_name",   # link text e.g. "Official Statement - final os (2 MB)"
    "os_posted_date",
    "pdf_path",          # relative path under OUT_DIR, empty if not downloaded
    "pdf_bytes",
    "error",
    "fetched_at",
]

# 9-char CUSIP: 8 alphanumeric (no I/O) + 1 check digit
_CUSIP_RE = re.compile(r"^[0-9A-HJ-NP-Z]{8}[0-9]$")


def is_valid_cusip(cusip: str) -> bool:
    return bool(_CUSIP_RE.match(cusip or ""))

# ────────────────────────── HTTP helpers ─────────────────────────
def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
    )
    return s


def accept_terms_of_use(session: requests.Session, referer: str | None = None,
                        max_retries: int = 4) -> None:
    """POST the EMMA disclaimer form so subsequent requests return content.

    A known-good referer is used by default so this can be called mid-run
    without depending on the CUSIP that happens to have failed. Retries
    transient 5xx / network failures with exponential backoff.
    """
    referer = referer or SECURITY_URL.format(cusip=DISCLAIMER_REFERER_CUSIP)
    last_exc: Exception | None = None
    for attempt in range(max_retries):
        try:
            r = session.get(referer, timeout=30)
            r.raise_for_status()
            fields = {
                m.group(1): m.group(2)
                for m in re.finditer(
                    r'<input type="hidden"[^>]*name="([^"]+)"[^>]*value="([^"]*)"', r.text
                )
            }
            if not fields:
                raise RuntimeError("Disclaimer form not found on EMMA response")
            fields["ctl00$mainContentArea$disclaimerContent$yesButton"] = "Accept"
            r2 = session.post(
                DISCLAIMER_URL,
                data=fields,
                headers={"Referer": referer, "Origin": BASE},
                allow_redirects=True,
                timeout=30,
            )
            r2.raise_for_status()
            return
        except Exception as exc:
            last_exc = exc
            wait = 2 ** (attempt + 1)  # 2, 4, 8, 16 s
            print(f"  accept_terms_of_use attempt {attempt+1}/{max_retries} failed "
                  f"({type(exc).__name__}: {exc}); sleeping {wait}s")
            time.sleep(wait)
    assert last_exc is not None
    raise last_exc


def is_disclaimer_page(html: str) -> bool:
    return "Terms of Use" in html and "officialStatementContainer" not in html


# ──────────────────────── parsing helpers ────────────────────────
_OS_ANCHOR_RE = re.compile(
    r'<a[^>]*data-doctype="OS"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', re.S
)
_POSTED_DATE_RE = re.compile(r"<td[^>]*>\s*(\d{1,2}/\d{1,2}/\d{4})\s*</td>")


@dataclass
class OSRecord:
    doc_id: str
    url: str
    display_name: str
    posted_date: str


def extract_os_records(html: str) -> tuple[list[OSRecord], bool]:
    """Return (records, no_os_flag). Empty list + False ⇒ parse failure."""
    start = html.find('id="officialStatementContainer"')
    if start == -1:
        return [], False
    end = html.find('id="continuingDisclosureContainer"', start)
    section = html[start:end] if end != -1 else html[start : start + 6000]
    no_os = "No OS has been submitted" in section

    records: list[OSRecord] = []
    for m in _OS_ANCHOR_RE.finditer(section):
        href = m.group(1).strip()
        display = re.sub(r"\s+", " ", m.group(2)).strip()
        # Posted date lives in the <td> right after the anchor's <td>.
        tail = section[m.end() : m.end() + 400]
        pd_match = _POSTED_DATE_RE.search(tail)
        posted = pd_match.group(1) if pd_match else ""
        # Derive a stable doc ID from the filename
        doc_id = href.rsplit("/", 1)[-1]
        if doc_id.lower().endswith(".pdf"):
            doc_id = doc_id[:-4]
        url = href if href.startswith("http") else BASE + href
        records.append(OSRecord(doc_id=doc_id, url=url, display_name=display, posted_date=posted))
    return records, no_os


# ─────────────────────── manifest / log I/O ──────────────────────
def load_manifest() -> dict[str, dict]:
    if not MANIFEST.exists():
        return {}
    with MANIFEST.open() as f:
        return {row["cusip"]: row for row in csv.DictReader(f)}


def write_manifest(rows: Iterable[dict]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def append_log(event: dict) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    event["ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with LOG_FILE.open("a") as f:
        f.write(json.dumps(event) + "\n")


# ───────────────────────────── core ──────────────────────────────
def load_panel_cusips() -> list[dict]:
    """Return in-panel CUSIP rows with minimal fields, preserving file order."""
    rows: list[dict] = []
    seen: set[str] = set()
    with SRC_CSV.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("is_in_578_panel") != "True":
                continue
            cusip = (row.get("CUSIP") or "").strip()
            if not cusip or cusip in seen:
                continue
            seen.add(cusip)
            rows.append(
                {
                    "cusip": cusip,
                    "issuer_name": row.get("Issuer Name", ""),
                    "city": row.get("city_name_crosswalk", "") or row.get("City_Name", ""),
                    "state": row.get("State_Abb_Classified", ""),
                    "issue_date": row.get("Issue Date", ""),
                }
            )
    return rows


def download_pdf(session: requests.Session, url: str, dest: Path, timeout: int = 120) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with session.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        ct = r.headers.get("Content-Type", "")
        if "pdf" not in ct.lower():
            raise RuntimeError(f"Unexpected Content-Type {ct!r} for {url}")
        n = 0
        with tmp.open("wb") as f:
            for chunk in r.iter_content(64 * 1024):
                if chunk:
                    f.write(chunk)
                    n += len(chunk)
    tmp.rename(dest)
    return n


def fetch_security_page(session: requests.Session, cusip: str, max_retries: int = 4) -> str:
    url = SECURITY_URL.format(cusip=cusip)
    last_exc: Exception | None = None
    for attempt in range(max_retries):
        try:
            r = session.get(url, timeout=45)
            # Back off longer on 5xx (EMMA under load)
            if r.status_code >= 500:
                raise requests.HTTPError(f"{r.status_code} server error", response=r)
            r.raise_for_status()
            if is_disclaimer_page(r.text):
                # Session timed out — re-accept via a known-good referer.
                accept_terms_of_use(session)
                r = session.get(url, timeout=45)
                r.raise_for_status()
            return r.text
        except Exception as exc:
            last_exc = exc
            wait = 2 ** (attempt + 2)  # 4, 8, 16, 32 s
            print(f"  {cusip}: fetch attempt {attempt+1}/{max_retries} failed "
                  f"({type(exc).__name__}: {exc}); sleeping {wait}s")
            time.sleep(wait)
    assert last_exc is not None
    raise last_exc


def process_cusip(
    session: requests.Session,
    row: dict,
    pdf_dir: Path,
) -> dict:
    cusip = row["cusip"]
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    base = {**row, "status": "", "os_doc_id": "", "os_url": "", "os_display_name": "",
            "os_posted_date": "", "pdf_path": "", "pdf_bytes": "", "error": "", "fetched_at": now}
    if not is_valid_cusip(cusip):
        base["status"] = "invalid_cusip"
        base["error"] = "CUSIP failed format validation"
        return base
    try:
        html = fetch_security_page(session, cusip)
    except requests.HTTPError as e:
        base["status"] = "http_error"
        base["error"] = f"HTTP {e.response.status_code if e.response else '?'}"
        return base
    except Exception as e:
        base["status"] = "error"
        base["error"] = f"{type(e).__name__}: {e}"
        return base

    records, no_os = extract_os_records(html)
    if not records:
        base["status"] = "no_os" if no_os else "error"
        if not no_os:
            base["error"] = "OS container not found / unexpected page"
        return base

    # Prefer the first OS record (typically the final OS). Record additional
    # records via the log; manifest stores the primary one.
    primary = records[0]
    pdf_path = pdf_dir / f"{primary.doc_id}.pdf"
    try:
        if not pdf_path.exists():
            size = download_pdf(session, primary.url, pdf_path)
        else:
            size = pdf_path.stat().st_size
    except Exception as e:
        base["status"] = "error"
        base["os_doc_id"] = primary.doc_id
        base["os_url"] = primary.url
        base["os_display_name"] = primary.display_name
        base["os_posted_date"] = primary.posted_date
        base["error"] = f"download failed: {type(e).__name__}: {e}"
        return base

    base.update(
        status="found",
        os_doc_id=primary.doc_id,
        os_url=primary.url,
        os_display_name=primary.display_name,
        os_posted_date=primary.posted_date,
        pdf_path=str(pdf_path.relative_to(OUT_DIR)),
        pdf_bytes=size,
    )
    if len(records) > 1:
        append_log({"cusip": cusip, "extra_os_records": [r.__dict__ for r in records[1:]]})
    return base


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None, help="process only first N CUSIPs")
    ap.add_argument("--cusip", type=str, default=None, help="process a single CUSIP (bypasses panel filter)")
    ap.add_argument("--sleep", type=float, default=1.5, help="seconds between requests (default 1.5)")
    ap.add_argument("--retry-failed", action="store_true", help="re-attempt rows whose status is 'error' or 'http_error'")
    ap.add_argument("--force", action="store_true", help="re-process CUSIPs already in manifest")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    print(f"Manifest: {len(manifest)} existing rows")

    # Build target list
    if args.cusip:
        targets = [{"cusip": args.cusip.strip(), "issuer_name": "", "city": "",
                    "state": "", "issue_date": ""}]
    else:
        targets = load_panel_cusips()
        print(f"Panel CUSIPs: {len(targets)}")

    # Filter by resume rules
    filtered: list[dict] = []
    for row in targets:
        existing = manifest.get(row["cusip"])
        if existing and not args.force:
            if args.retry_failed and existing.get("status") in {"error", "http_error"}:
                filtered.append(row)
            else:
                continue
        else:
            filtered.append(row)

    if args.limit:
        filtered = filtered[: args.limit]
    print(f"To fetch: {len(filtered)}")

    if not filtered:
        print("Nothing to do.")
        return 0

    session = make_session()
    print("Accepting EMMA Terms of Use …")
    accept_terms_of_use(session)

    counters = {"found": 0, "no_os": 0, "invalid_cusip": 0, "error": 0, "http_error": 0}
    try:
        for i, row in enumerate(filtered, 1):
            result = process_cusip(session, row, PDF_DIR)
            manifest[result["cusip"]] = result
            counters[result["status"]] = counters.get(result["status"], 0) + 1
            append_log({"cusip": result["cusip"], "status": result["status"],
                        "os_doc_id": result["os_doc_id"], "error": result["error"]})
            if i % 10 == 0 or i == len(filtered):
                print(
                    f"[{i}/{len(filtered)}] {result['cusip']} -> {result['status']}"
                    + (f" ({result['os_doc_id']})" if result["os_doc_id"] else "")
                    + (f"  {result['error']}" if result["error"] else "")
                )
                # Flush manifest periodically so a crash doesn't lose work
                write_manifest(manifest.values())
            time.sleep(args.sleep)
    except KeyboardInterrupt:
        print("\nInterrupted — flushing manifest.")
    finally:
        write_manifest(manifest.values())

    print("\n── summary ──")
    for k, v in counters.items():
        print(f"  {k:12s} {v}")
    print(f"  manifest rows: {len(manifest)}")
    unique_pdfs = len({p.name for p in PDF_DIR.glob('*.pdf')})
    print(f"  unique PDFs on disk: {unique_pdfs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
