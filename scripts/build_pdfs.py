#!/usr/bin/env python3
"""Build the PDF downloads: one PDF per domain in docs/downloads/, plus
docs/downloads/index.md listing them.

    pip install playwright && playwright install chromium   # once
    python scripts/build_pdfs.py                  # all domains
    python scripts/build_pdfs.py security network # some domains

Each PDF is rendered by scripts/build_doc.py (solution use cases + product use
cases, in the Description / Collection / Key content / Notes format) and
printed with headless Chromium. Set CHROMIUM=/path/to/chrome to use a specific
browser binary instead of Playwright's own.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_pages import pdf_names  # noqa: E402

OUT = ROOT / "docs" / "downloads"
FOOTER = ('<div style="width:100%;font-size:8px;font-family:Arial,sans-serif;color:#555;text-align:center;">'
          '<span class="pageNumber"></span></div>')


def render(pairs):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM")
        browser = p.chromium.launch(**({"executable_path": exe} if exe else {}))
        page = browser.new_page()
        for html_file, pdf in pairs:
            page.goto(html_file.resolve().as_uri())
            page.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True,
                     display_header_footer=True, header_template="<div></div>", footer_template=FOOTER)
            print(f"  {pdf.name}")
        browser.close()


def write_index(domains, names):
    rows = []
    for d in domains:
        f = OUT / names.get(d["id"], "")
        if d["id"] not in names or not f.exists():
            continue
        pages = len(PdfReader(str(f)).pages)
        rows.append(f"| {d['title']} | {pages} | [{f.name}]({f.name}) ({f.stat().st_size // 1024:,} KB) |")
    text = """---
title: Downloads
---

# Downloads

The full use case catalogue as PDF, one file per domain, in the same format as the original *Ansible Automation - Use Cases* document. Every use case is one table: **Description**, **Collection** (with support level, version and last update), **Key content** and **Notes**.

Each PDF contains two kinds of use case:

- **Solution use cases**: outcome-level scenarios written by people.
- **Product use cases**: the modules of each certified or validated collection, grouped by what a customer wants to achieve, with the supported components listed.

| Domain | Pages | File |
|---|---:|---|
""" + "\n".join(rows) + "\n\nThe PDFs are rebuilt with `make pdfs` (see the [README](https://github.com/shang2015/ansible-use-cases#readme)). The website always has the latest data.\n"
    (OUT / "index.md").write_text(text)


def main(argv):
    domains = yaml.safe_load((ROOT / "data/domains.yml").read_text())
    names = pdf_names(domains)
    want = set(argv) or set(names)
    OUT.mkdir(parents=True, exist_ok=True)
    pairs = []
    for d in domains:
        if d["id"] not in names or d["id"] not in want:
            continue
        out = f"d-{d['id']}"
        subprocess.run([sys.executable, str(ROOT / "scripts/build_doc.py"), "--domains", d["id"], "--out", out], check=True)
        pairs.append((ROOT / "build" / f"{out}.html", OUT / names[d["id"]]))
    render(pairs)
    write_index(domains, names)


if __name__ == "__main__":
    main(sys.argv[1:])
