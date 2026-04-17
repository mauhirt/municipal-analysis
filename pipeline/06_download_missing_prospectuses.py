"""
Download Official Statement PDFs listed in raw/bloomberg/Missing_Green_Prospectuses_URLS.csv
into raw/emma/prospectuses/.

Skips files already present on disk (non-zero size) and rows marked
"NO OS SUBMITTED". Polite 0.5s delay between requests.

Writes a small download log CSV with per-file status.
"""

from __future__ import annotations

import csv
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL_CSV = ROOT / "raw" / "bloomberg" / "Missing_Green_Prospectuses_URLS.csv"
OUT_DIR = ROOT / "raw" / "emma" / "prospectuses"
LOG = OUT_DIR / "_download_log.csv"

UA = "Mozilla/5.0 (compatible; muni-analysis-research/1.0)"
DELAY = 0.5  # seconds between requests


def parse_urls_csv(path: Path) -> list[dict]:
    raw = path.read_text(encoding="utf-8-sig")
    lines = raw.splitlines()
    header = lines[0].strip('"').split(",")
    rows = []
    for line in lines[1:]:
        s = line.strip().strip('"')
        parts = s.split(",", len(header) - 1)
        if len(parts) == len(header):
            rows.append(dict(zip(header, parts)))
    return rows


def download(url: str, dst: Path) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    dst.write_bytes(data)
    return len(data), "ok"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = parse_urls_csv(URL_CSV)

    url_rows = [r for r in rows if r["prospectus_url"].startswith("http")]
    no_os = [r for r in rows if not r["prospectus_url"].startswith("http")]
    print(f"URL rows         : {len(url_rows)}")
    print(f"NO OS SUBMITTED  : {len(no_os)}")

    # Deduplicate by filename
    seen = {}
    for r in url_rows:
        fname = r["prospectus_url"].rsplit("/", 1)[-1]
        seen.setdefault(fname, (r["prospectus_url"], r))

    existing_ok = {p.name for p in OUT_DIR.glob("*.pdf") if p.stat().st_size > 0}

    log_rows = []
    to_download = [(f, u, r) for f, (u, r) in seen.items() if f not in existing_ok]
    print(f"Unique PDFs      : {len(seen)}")
    print(f"Already on disk  : {len(seen) - len(to_download)}")
    print(f"To download      : {len(to_download)}\n")

    for i, (fname, url, meta) in enumerate(to_download, 1):
        dst = OUT_DIR / fname
        t0 = time.time()
        try:
            size, status = download(url, dst)
            err = ""
        except urllib.error.HTTPError as e:
            size, status, err = 0, "http_error", f"{e.code} {e.reason}"
        except urllib.error.URLError as e:
            size, status, err = 0, "url_error", repr(e.reason)
        except Exception as e:  # noqa: BLE001
            size, status, err = 0, "error", repr(e)
        elapsed = time.time() - t0
        print(f"[{i:3d}/{len(to_download)}] {fname:55s} "
              f"{size:10d} B  {elapsed:5.2f}s  {status}"
              f"{'  ' + err if err else ''}")
        log_rows.append({
            "filename": fname,
            "url": url,
            "bytes": size,
            "seconds": round(elapsed, 2),
            "status": status,
            "error": err,
            "lead_CUSIP": meta.get("lead_CUSIP", ""),
            "Issuer_Name": meta.get("Issuer_Name", ""),
            "Issue_Date": meta.get("Issue_Date", ""),
        })
        time.sleep(DELAY)

    if log_rows:
        with LOG.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(log_rows[0].keys()))
            w.writeheader()
            w.writerows(log_rows)
        print(f"\nDownload log: {LOG.relative_to(ROOT)}")

    ok = sum(1 for r in log_rows if r["status"] == "ok")
    bad = len(log_rows) - ok
    print(f"\n{ok} ok, {bad} failed out of {len(log_rows)} attempted")
    return 0 if bad == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
