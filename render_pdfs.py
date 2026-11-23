#!/usr/bin/env python3
"""Render each review sheet to a one-page Letter PDF with headless Chrome."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHEETS = ROOT / "docs" / "printables"
PDF_DIR = SHEETS / "pdf"
CHROME = "google-chrome"

def main() -> int:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    sheets = [p for p in sorted(SHEETS.glob("*.html")) if p.name != "index.html"]
    if not sheets:
        print("no review sheets to render", file=sys.stderr)
        return 1
    failed = []
    for src in sheets:
        dest = PDF_DIR / f"{src.stem}.pdf"
        cmd = [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--no-pdf-header-footer",
            f"--print-to-pdf={dest}",
            src.resolve().as_uri(),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0 or not dest.exists():
            failed.append(f"{src.name}: {r.stderr.strip() or r.stdout.strip() or 'chrome failed'}")
            continue
        info = subprocess.run(["pdfinfo", str(dest)], capture_output=True, text=True)
        pages = ""
        for line in info.stdout.splitlines():
            if line.startswith("Pages:"):
                pages = line.split(":", 1)[1].strip()
        print(f"{dest.relative_to(ROOT)}  pages={pages or '?'}")
        if pages and pages != "1":
            failed.append(f"{dest.name}: expected 1 page, got {pages}")
    print(f"rendered {len(sheets)} pdfs into {PDF_DIR}")
    if failed:
        print("problems:", file=sys.stderr)
        for f in failed:
            print("  " + f, file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
