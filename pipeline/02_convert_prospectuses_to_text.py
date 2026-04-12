"""
Convert EMMA municipal bond prospectus PDFs to plain text.

Source : raw/emma/prospectuses/*.pdf
Output : raw/emma/prospectuses_text/*.txt  (+ _manifest.csv with per-file status)

Pages are separated by a form-feed (\\f) to preserve page boundaries for
downstream chunking / search.
"""

from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "raw" / "emma" / "prospectuses"
OUT_DIR = ROOT / "raw" / "emma" / "prospectuses_text"
MANIFEST = OUT_DIR / "_manifest.csv"

PAGE_SEPARATOR = "\f"  # form-feed; standard page separator in pdftotext output


def extract_pdf(pdf_path: Path) -> tuple[str, int]:
    """Return (full_text, page_count) for a single PDF."""
    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception as exc:  # noqa: BLE001 — keep going on per-page failures
            pages.append(f"[PAGE EXTRACTION ERROR: {exc!r}]")
    return PAGE_SEPARATOR.join(pages), len(reader.pages)


def main() -> int:
    if not SRC_DIR.exists():
        print(f"ERROR: source directory not found: {SRC_DIR}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(SRC_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"ERROR: no PDFs found in {SRC_DIR}", file=sys.stderr)
        return 1

    print(f"Found {len(pdfs)} PDFs in {SRC_DIR}")
    print(f"Writing text to      {OUT_DIR}")

    rows: list[dict] = []
    t_start = time.time()

    for i, pdf_path in enumerate(pdfs, 1):
        out_path = OUT_DIR / (pdf_path.stem + ".txt")
        status = "ok"
        pages = 0
        chars = 0
        err = ""
        t0 = time.time()
        try:
            text, pages = extract_pdf(pdf_path)
            out_path.write_text(text, encoding="utf-8")
            chars = len(text)
        except (PdfReadError, Exception) as exc:  # noqa: BLE001
            status = "error"
            err = repr(exc)
        elapsed = time.time() - t0

        rows.append({
            "pdf": pdf_path.name,
            "txt": out_path.name,
            "pages": pages,
            "chars": chars,
            "seconds": round(elapsed, 2),
            "status": status,
            "error": err,
        })

        print(
            f"[{i:3d}/{len(pdfs)}] {pdf_path.name:50s} "
            f"pages={pages:4d}  chars={chars:8d}  {elapsed:5.2f}s  {status}"
        )

    with MANIFEST.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["pdf", "txt", "pages", "chars", "seconds", "status", "error"],
        )
        writer.writeheader()
        writer.writerows(rows)

    ok = sum(1 for r in rows if r["status"] == "ok")
    bad = len(rows) - ok
    total_chars = sum(r["chars"] for r in rows)
    total_pages = sum(r["pages"] for r in rows)
    print(
        f"\nDone in {time.time() - t_start:.1f}s — "
        f"{ok} ok, {bad} errored; {total_pages:,} pages, {total_chars:,} chars."
    )
    print(f"Manifest written to {MANIFEST}")
    return 0 if bad == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
