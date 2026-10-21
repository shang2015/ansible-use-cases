#!/usr/bin/env python3
"""Compile every curated use case into one printable HTML document (then PDF).

    python scripts/build_pdf.py            # writes build/use-cases.html
Then print it to PDF with any Chromium (see Makefile target `pdf`).
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_pages import TYPE_ORDER, assign_domain, support  # noqa: E402

DOCS = ROOT / "docs" / "use-cases"
OUT = ROOT / "build"


def read_page(p: Path):
    text = p.read_text()
    fm, body = {}, text
    if text.startswith("---"):
        _, raw, body = text.split("---", 2)
        fm = yaml.safe_load(raw) or {}
    body = re.sub(r"^# .*\n", "", body.strip(), count=1)          # title is printed from front matter
    body = re.sub(r"^## ", "### ", body, flags=re.M)               # section headings sit under the title
    body = re.sub(r"\]\(([^)]+)\.md(#[^)]*)?\)", r"](#\1)", body)    # internal links -> plain anchors
    return fm, body


def badge(kind):
    s = support(kind)
    cls = {"Validated": "val", "Certified": "cert"}.get(s, "oth")
    return f'<span class="badge {cls}">{s}</span>'


def main():
    cols = {c["fqcn"]: c for c in yaml.safe_load((ROOT / "data/collections.yml").read_text())}
    content = {c["fqcn"]: c for c in json.loads((ROOT / "data/content.json").read_text())}
    items = {i["fqcn"]: i for c in content.values() for i in c["items"]}
    domains = [d for d in yaml.safe_load((ROOT / "data/domains.yml").read_text()) if d["id"] != "other"]
    md = markdown.Markdown(extensions=["tables", "attr_list"])

    by_domain_cols = defaultdict(list)
    for c in cols.values():
        by_domain_cols[assign_domain(c, domains + [{"id": "other", "match": ["*"]}])].append(c["fqcn"])

    sections, summary, toc = [], [], []
    total_uc = total_items = 0
    for d in domains:
        folder = DOCS / d["path"]
        pages = []
        for p in folder.glob("*.md"):
            if p.name == "index.md" or p.name.startswith("_"):
                continue
            fm, body = read_page(p)
            pages.append((fm.get("order", 999), p, fm, body))
        pages.sort(key=lambda x: (x[0], x[2].get("title", "")))
        dcols = sorted(by_domain_cols.get(d["id"], []))
        n_items = sum(len([i for i in content.get(f, {}).get("items", []) if i["type"] in TYPE_ORDER]) for f in dcols)
        total_uc += len(pages)
        total_items += n_items
        summary.append((d, len(pages), len(dcols), n_items))
        if not pages:
            continue
        toc.append(f'<li><a href="#d-{d["id"]}">{html.escape(d["title"])}</a> <span class="n">{len(pages)}</span><ol>'
                   + "".join(f'<li><a href="#{d["id"]}-{p.stem}">{html.escape(fm.get("title", p.stem))}</a></li>' for _, p, fm, _ in pages)
                   + "</ol></li>")
        out = [f'<section class="domain" id="d-{d["id"]}"><h1>{html.escape(d["title"])}</h1>',
               f'<p class="lead">{html.escape(d["summary"])}</p>',
               f'<p class="meta">{len(pages)} use cases · {len(dcols)} certified/validated collections · {n_items:,} module-level use cases</p>',
               "<ol class=\"uclist\">" + "".join(f'<li>{html.escape(fm.get("title", ""))} <span>— {html.escape(str(fm.get("summary", "")))}</span></li>' for _, _, fm, _ in pages) + "</ol></section>"]
        for _, p, fm, body in pages:
            md.reset()
            body_html = md.convert(body)
            body_html = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{d["id"]}-{m.group(1).split("/")[-1]}"', body_html)
            personas = ", ".join(fm.get("personas") or [])
            rows = []
            for fq in fm.get("collections") or []:
                c = cols.get(fq, {})
                rows.append(f"<tr><td><code>{fq}</code></td><td>{badge(c.get('content_type'))}</td><td>{html.escape(c.get('provider', ''))}</td></tr>")
            krows = []
            for ref in fm.get("key_content") or []:
                it = items.get(ref, {})
                krows.append(f"<tr><td><code>{ref}</code></td><td>{it.get('type', '').replace('_', ' ')}</td><td>{html.escape(it.get('short_description', ''))}</td></tr>")
            ex = "".join(f'<li>{html.escape(e["title"])} — <span class="url">{html.escape(e["url"])}</span></li>' for e in fm.get("examples") or [])
            out.append(
                f'<article id="{d["id"]}-{p.stem}"><div class="crumb">{html.escape(d["title"])}</div>'
                f'<h2>{html.escape(fm.get("title", p.stem))}</h2>'
                + (f'<p class="persona">For: {html.escape(personas)}</p>' if personas else "")
                + body_html
                + '<h3 class="ck">Collections &amp; key content</h3>'
                + f'<table class="cols"><thead><tr><th>Collection</th><th>Support</th><th>Provider</th></tr></thead><tbody>{"".join(rows)}</tbody></table>'
                + (f'<table class="keys"><thead><tr><th>Module / role / plugin</th><th>Type</th><th>What it does</th></tr></thead><tbody>{"".join(krows)}</tbody></table>' if krows else "")
                + (f'<h4>Examples</h4><ul>{ex}</ul>' if ex else "")
                + "</article>")
        sections.append("\n".join(out))

    # Appendix: module-level use cases per collection
    appendix = ['<section class="appendix" id="appendix"><h1>Appendix: module-level use cases</h1>',
                '<p class="lead">Every module, role, playbook and plugin in a certified or validated collection is a use case in its own right. '
                'The site lists each one with its description; this appendix shows how many each collection contributes.</p>']
    for d, n_uc, n_cols, n_items in summary:
        fqcns = sorted(by_domain_cols.get(d["id"], []))
        if not fqcns:
            continue
        appendix.append(f'<h2>{html.escape(d["title"])} <span class="n">{n_items:,}</span></h2><table class="app"><thead><tr><th>Collection</th><th>Support</th><th>Provider</th><th>Items</th><th>Description</th></tr></thead><tbody>')
        for fq in fqcns:
            c = cols[fq]
            n = len([i for i in content.get(fq, {}).get("items", []) if i["type"] in TYPE_ORDER])
            appendix.append(f"<tr><td><code>{fq}</code></td><td>{badge(c.get('content_type'))}</td><td>{html.escape(c.get('provider', ''))}</td>"
                            f"<td class='num'>{n or '–'}</td><td>{html.escape((c.get('description') or '')[:140])}</td></tr>")
        appendix.append("</tbody></table>")
    appendix.append("</section>")

    srows = "".join(f'<tr><td>{html.escape(d["title"])}</td><td class="num">{u}</td><td class="num">{c}</td><td class="num">{i:,}</td></tr>'
                    for d, u, c, i in summary)
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ansible Automation Use Cases</title>
<link rel="stylesheet" href="print.css"></head><body>
<section class="cover"><div class="kicker">Reference</div><h1>Ansible Automation Use Cases</h1>
<p class="sub">By domain, each mapped to the Red Hat Certified and Validated content that delivers it.</p>
<div class="stats"><div><b>{total_uc}</b><span>curated use cases</span></div><div><b>{len(cols)}</b><span>certified &amp; validated collections</span></div><div><b>{total_items:,}</b><span>module-level use cases</span></div></div>
<p class="foot">Generated {date.today().isoformat()} · Community reference, not an official Red Hat publication · https://shang2015.github.io/ansible-use-cases/</p></section>
<section class="intro"><h1>How to read this document</h1>
<p>Every use case follows the same five parts so it can be read in a minute and reused as the outline of a delivery plan: <b>Description</b>, <b>Prerequisites</b>, <b>Steps</b>, <b>Success Criteria</b> and <b>Notes</b>. It ends with the collections and the key modules or roles that implement it.</p>
<p>There are two levels of use case. <b>Curated use cases</b> are outcome-level scenarios written by people. <b>Module-level use cases</b> are the individual modules, roles and plugins in each collection, summarised in the appendix.</p>
<h2>Coverage by domain</h2><table class="summary"><thead><tr><th>Domain</th><th>Curated use cases</th><th>Collections</th><th>Module-level use cases</th></tr></thead><tbody>{srows}
<tr class="total"><td>Total</td><td class="num">{total_uc}</td><td class="num">{len(cols)}</td><td class="num">{total_items:,}</td></tr></tbody></table></section>
<section class="toc"><h1>Contents</h1><ol>{"".join(toc)}<li><a href="#appendix">Appendix: module-level use cases</a></li></ol></section>
{"".join(sections)}
{"".join(appendix)}
</body></html>"""
    OUT.mkdir(exist_ok=True)
    (OUT / "use-cases.html").write_text(doc)
    (OUT / "print.css").write_text(PRINT_CSS)
    print(f"{total_uc} use cases, {len(cols)} collections, {total_items} items -> {OUT/'use-cases.html'}")


PRINT_CSS = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
:root { --red: #c9190b; --ink: #151515; --mute: #6a6e73; --line: #d2d2d2; --soft: #f5f5f5; }
* { box-sizing: border-box; }
body { font-family: "Red Hat Text", "Segoe UI", Helvetica, Arial, sans-serif; color: var(--ink); font-size: 9.6pt; line-height: 1.45; margin: 0; }
h1, h2, h3, h4 { font-family: "Red Hat Display", "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.2; break-after: avoid; }
code { font-family: "Red Hat Mono", Consolas, monospace; font-size: 8.4pt; background: var(--soft); padding: 0 .25em; border-radius: 2px; word-break: break-word; }
a { color: inherit; text-decoration: none; }
.cover { height: 255mm; display: flex; flex-direction: column; justify-content: center; border-left: 6mm solid var(--red); padding-left: 12mm; break-after: page; }
.cover .kicker { text-transform: uppercase; letter-spacing: .2em; color: var(--red); font-weight: 700; font-size: 9pt; }
.cover h1 { font-size: 34pt; margin: 4mm 0; }
.cover .sub { font-size: 13pt; color: var(--mute); max-width: 140mm; }
.cover .stats { display: flex; gap: 10mm; margin: 14mm 0; }
.cover .stats div { display: flex; flex-direction: column; }
.cover .stats b { font-size: 26pt; color: var(--red); font-family: "Red Hat Display", sans-serif; }
.cover .stats span { color: var(--mute); font-size: 9pt; max-width: 40mm; }
.cover .foot { margin-top: auto; color: var(--mute); font-size: 8pt; }
.intro, .toc { break-after: page; }
.intro h1, .toc h1, .domain h1, .appendix h1 { font-size: 20pt; border-bottom: 2px solid var(--red); padding-bottom: 2mm; }
table { width: 100%; border-collapse: collapse; margin: 2mm 0 3mm; font-size: 8.6pt; break-inside: auto; }
th, td { text-align: left; padding: 1.4mm 2mm; border-bottom: 1px solid var(--line); vertical-align: top; }
th { background: var(--soft); font-weight: 700; }
tr { break-inside: avoid; }
td.num { text-align: right; white-space: nowrap; }
.summary tr.total td { font-weight: 700; border-top: 2px solid var(--ink); }
.toc ol { padding-left: 5mm; } .toc > ol > li { margin: 2mm 0; font-weight: 700; break-inside: avoid; }
.toc ol ol { font-weight: 400; columns: 2; column-gap: 8mm; font-size: 8.6pt; margin-top: 1mm; }
.toc .n, h2 .n { color: var(--red); font-weight: 700; font-size: .85em; margin-left: 1mm; }
.domain { break-before: page; }
.domain .lead { font-size: 11pt; color: var(--mute); } .domain .meta { font-weight: 700; color: var(--red); }
.uclist li { margin: 1mm 0; } .uclist span { color: var(--mute); }
article { break-before: page; }
article .crumb { text-transform: uppercase; letter-spacing: .12em; color: var(--red); font-size: 7.5pt; font-weight: 700; }
article h2 { font-size: 15pt; margin: 1mm 0 1mm; }
article .persona { color: var(--mute); font-style: italic; margin-top: 0; }
article h3 { border-left: 1.2mm solid var(--red); padding-left: 2mm; margin: 4mm 0 1.5mm; font-size: 11pt; }
article h3.ck { border-left-color: var(--ink); }
article h4 { font-size: 9.5pt; margin: 2mm 0 1mm; }
article ol, article ul { padding-left: 5mm; margin: 1mm 0; } article li { margin: .6mm 0; }
.badge { font-size: 7.2pt; font-weight: 700; padding: 0 1.6mm; border: 1px solid currentColor; border-radius: 3mm; white-space: nowrap; }
.badge.cert { color: #0066cc; } .badge.val { color: #3e8635; } .badge.oth { color: var(--mute); }
.url { color: var(--mute); font-size: 8pt; word-break: break-all; }
.appendix { break-before: page; } .appendix h2 { font-size: 12pt; margin-top: 6mm; }
.app td:nth-child(5) { color: var(--mute); font-size: 8pt; }
"""

if __name__ == "__main__":
    main()
