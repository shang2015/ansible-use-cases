#!/usr/bin/env python3
"""Render the use case catalogue in the format of the original
"Ansible Automation - Use Cases" document: per domain, "Use Case: <title>"
headings, each with a two-column table (Description, Prerequisite(s), Steps,
Success Criteria, Notes).

Two kinds of use case are rendered:
  * curated use cases from docs/use-cases/<domain>/*.md
  * product use cases: groups of a collection's modules (data/groups/<fqcn>.yml
    + data/resources.json), listing the components they support

    python scripts/build_doc.py [--only fqcn,fqcn] [--domains id,id] [--out name]
Writes build/<name>.html (+ print.css); print it to PDF with Chromium.
"""
from __future__ import annotations

import argparse
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
from build_pages import assign_domain, support  # noqa: E402

OUT = ROOT / "build"
MD = markdown.Markdown(extensions=["tables"])


def md_inline(text: str) -> str:
    MD.reset()
    out = MD.convert(text or "")
    return re.sub(r"\]\(([^)]+)\.md\)", "]", out)


def sections_of(body: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def esc(s) -> str:
    return html.escape(str(s or ""))


def strip_md_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def table(rows: list[tuple[str, str]], cls="uc") -> str:
    return f'<table class="{cls}"><tbody>' + "".join(
        f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in rows if v) + "</tbody></table>"


def curated_block(fm: dict, body: str, cols: dict, items: dict) -> str:
    s = sections_of(body)
    keys = fm.get("key_content") or []
    content_list = "".join(
        f"<li><code>{esc(k)}</code> — {esc(items.get(k, {}).get('short_description', ''))}</li>" for k in keys)
    col_list = ", ".join(
        f"<code>{esc(c)}</code> ({support(cols.get(c, {}).get('content_type'))}"
        + (f", v{esc(cols[c]['latest_version'])}" if cols.get(c, {}).get("latest_version") else "")
        + (f", updated {esc(cols[c]['last_updated'])}" if cols.get(c, {}).get("last_updated") else "") + ")"
        for c in fm.get("collections") or [])
    rows = [
        ("Description", md_inline(strip_md_links(s.get("Description", "")))),
        ("Collection", col_list),
        ("Key content", f"<ul>{content_list}</ul>" if content_list else ""),
        ("Notes", md_inline(strip_md_links(s.get("Notes", "")))),
    ]
    return f'<h3 class="uch">Use Case: {esc(fm.get("title"))}</h3>' + table(rows)


def ops_label(e: dict) -> str:
    ops = []
    if e.get("manage"):
        ops.append("manage")
    if e.get("info"):
        ops.append("query")
    return " + ".join(ops)


def product_blocks(fq: str, col: dict, group: dict, res: dict) -> str:
    out = []
    kind = support(col.get("content_type"))
    head = (f'<div class="colhead"><h3 class="colh">{esc(group.get("product") or fq)} '
            f'<span class="fq">{esc(fq)}</span></h3>'
            f'<p class="colmeta"><span class="badge {"val" if kind == "Validated" else "cert"}">{kind}</span> '
            f'{esc(col.get("provider"))} · version {esc(col.get("latest_version"))} · updated {esc(col.get("last_updated"))} · '
            f'{res["module_count"]} modules → {len(group["use_cases"])} use cases</p></div>')
    out.append(head)
    notes_common = [esc(n) for n in group.get("notes") or []]
    other = {f"{o['type']}:{o['name']}": o for o in res["other"]}
    for uc in group["use_cases"]:
        comps = []
        for key, label in (uc.get("components") or {}).items():
            if key in res["resources"]:
                e = res["resources"][key]
                mods = e["manage"] + e["info"]
                comps.append(f'<li><b>{esc(label)}</b> <span class="mods">{", ".join(f"<code>{esc(m)}</code>" for m in mods)}</span></li>')
            elif key in other:
                o = other[key]
                comps.append(f'<li><b>{esc(label)}</b> <span class="mods">{esc(o["type"].replace("_", " "))} <code>{esc(o["name"])}</code></span></li>')
        notes = [esc(uc["note"])] if uc.get("note") else []
        notes += notes_common
        rows = [
            ("Description", esc(uc.get("description"))),
            ("Collection", f"<code>{esc(fq)}</code> ({kind}, {esc(col.get('provider'))}"
                           + (f", v{esc(col['latest_version'])}" if col.get("latest_version") else "")
                           + (f", updated {esc(col['last_updated'])}" if col.get("last_updated") else "") + ")"),
            ("Key content", f'<ul class="comps{" many" if len(comps) > 16 else ""}">{"".join(comps)}</ul>'),
            ("Notes", "<ul>" + "".join(f"<li>{n}</li>" for n in notes) + "</ul>" if notes else ""),
        ]
        out.append(f'<h4 class="uch">Use Case: {esc(uc["title"])}</h4>' + table(rows, "uc prod"))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="limit product use cases to these collections")
    ap.add_argument("--domains", default="", help="limit to these domain ids")
    ap.add_argument("--out", default="use-cases-doc")
    ap.add_argument("--no-curated", action="store_true")
    a = ap.parse_args()
    only = {x for x in a.only.split(",") if x}
    want_domains = {x for x in a.domains.split(",") if x}

    cols = {c["fqcn"]: c for c in yaml.safe_load((ROOT / "data/collections.yml").read_text())}
    content = {c["fqcn"]: c for c in json.loads((ROOT / "data/content.json").read_text())}
    items = {i["fqcn"]: i for c in content.values() for i in c["items"]}
    resources = json.loads((ROOT / "data/resources.json").read_text())
    domains = yaml.safe_load((ROOT / "data/domains.yml").read_text())
    groups = {}
    for p in (ROOT / "data/groups").glob("*.yml"):
        g = yaml.safe_load(p.read_text())
        groups[g["fqcn"]] = g

    by_domain = defaultdict(list)
    for fq, c in cols.items():
        by_domain[assign_domain(c, domains)].append(fq)

    toc, body = [], []
    n_cur = n_prod = 0
    for d in domains:
        if want_domains and d["id"] not in want_domains:
            continue
        cur = []
        if not a.no_curated:
            for p in sorted((ROOT / "docs/use-cases" / d["path"]).glob("*.md")):
                if p.name == "index.md" or p.name.startswith("_"):
                    continue
                text = p.read_text()
                _, raw, b = text.split("---", 2)
                fm = yaml.safe_load(raw) or {}
                cur.append((fm.get("order", 999), fm, b))
            cur.sort(key=lambda x: x[0])
        prods = [fq for fq in sorted(by_domain.get(d["id"], [])) if fq in groups and (not only or fq in only)]
        nolist = [] if only else [fq for fq in sorted(by_domain.get(d["id"], [])) if fq not in groups]
        if not cur and not prods:
            continue
        n_cur += len(cur)
        n_prod += sum(len(groups[fq]["use_cases"]) for fq in prods)
        sub = []
        part = [f'<h1 id="d-{d["id"]}">{esc(d["title"])}</h1><p class="lead">{esc(d["summary"])}</p>']
        if cur:
            part.append('<h2>Solution use cases</h2>')
            sub.append(f'<li>Solution use cases ({len(cur)})<ul>' + "".join(f"<li>{esc(fm.get('title'))}</li>" for _, fm, _ in cur) + "</ul></li>")
            part += [curated_block(fm, b, cols, items) for _, fm, b in cur]
        if prods:
            part.append('<h2>Product use cases</h2><p class="lead">Grouped from the modules of each certified or validated collection. Key content lists the components each use case supports, with the modules that manage them (create, update, delete) and query them (_info).</p>')
            sub.append("<li>Product use cases<ul>" + "".join(
                f"<li>{esc(groups[fq].get('product') or fq)} ({len(groups[fq]['use_cases'])})</li>" for fq in prods) + "</ul></li>")
            part += [product_blocks(fq, cols[fq], groups[fq], resources[fq]) for fq in prods]
        if nolist:
            part.append('<h2>Other certified and validated collections</h2><p class="lead">Module-level content for these collections could not be read from a public source repository. Browse them on Automation Hub.</p>'
                        '<table class="uc"><tbody>' + "".join(
                            f"<tr><th><code>{esc(fq)}</code></th><td>{esc(cols[fq].get('description'))} "
                            f"<span class='ops'>({support(cols[fq].get('content_type'))}, {esc(cols[fq].get('provider'))}"
                            f"{'; ' + esc(cols[fq]['note']) if cols[fq].get('note') else ''})</span></td></tr>" for fq in nolist) + "</tbody></table>")
        toc.append(f'<li><a href="#d-{d["id"]}">{esc(d["title"])}</a><ul>{"".join(sub)}</ul></li>')
        body.append(f'<section class="domain">{"".join(part)}</section>')

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ansible Automation - Use Cases</title>
<link rel="stylesheet" href="doc.css"></head><body>
<section class="title"><h1>Ansible Automation - Use Cases</h1>
<p>A reference of the use cases by which Ansible Automation Platform is commonly implemented, by domain. Each use case is described in the same format (Description, Collection, Key content, Notes) and mapped to Red Hat Certified and Validated content.</p>
<p class="small">{n_cur} solution use cases · {n_prod} product use cases · generated {date.today().isoformat()} · community reference, not an official Red Hat publication</p></section>
<section class="toc"><h1>Contents</h1><ol>{"".join(toc)}</ol></section>
{"".join(body)}
</body></html>"""
    OUT.mkdir(exist_ok=True)
    (OUT / f"{a.out}.html").write_text(doc)
    (OUT / "doc.css").write_text(DOC_CSS)
    print(f"{n_cur} solution + {n_prod} product use cases -> {OUT / (a.out + '.html')}")


DOC_CSS = """
@page { size: A4; margin: 20mm 18mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10pt; line-height: 1.4; color: #000; margin: 0; }
h1 { font-size: 20pt; font-weight: 400; margin: 0 0 4mm; break-before: page; }
h2 { font-size: 15pt; font-weight: 400; margin: 7mm 0 3mm; }
h3, h4 { font-size: 12.5pt; font-weight: 400; margin: 7mm 0 2mm; break-after: avoid; }
.title h1 { font-size: 26pt; break-before: auto; margin-top: 60mm; }
.title { break-after: page; } .small { color: #555; font-size: 9pt; }
.toc ol, .toc ul { margin: 1mm 0; } .toc > ol > li { margin: 2mm 0; } .toc a { color: #1155cc; text-decoration: underline; }
.toc ul ul { columns: 2; font-size: 9pt; }
.lead { color: #333; }
table.uc { width: 100%; border-collapse: collapse; margin: 0 0 3mm; font-size: 9.5pt; }
table.uc th, table.uc td { border: 1px solid #999; padding: 1.8mm 2.5mm; vertical-align: top; text-align: left; }
table.uc th { width: 30mm; background: #f3f3f3; font-weight: 400; }
table.uc tr { break-inside: avoid; }
table.uc ol, table.uc ul { margin: 0; padding-left: 5mm; } table.uc p { margin: 0 0 1mm; }
code { font-family: "Courier New", monospace; font-size: 8.6pt; }
ul.comps { list-style: none; padding-left: 0; }
ul.comps.many { columns: 2; column-gap: 5mm; font-size: 8.8pt; }
ul.comps.many li { break-inside: avoid; }
ul.comps li { break-inside: avoid; margin: .3mm 0; }
.ops { color: #666; font-size: 8pt; }
.mods code { font-size: 7.6pt; color: #444; } .mods { line-height: 1.25; }
.colhead { margin-top: 9mm; border-top: 2px solid #c00; padding-top: 2mm; break-after: avoid; }
.colh { margin: 0; font-size: 14pt; } .colh .fq { font-family: "Courier New", monospace; font-size: 10pt; color: #555; }
.colmeta { margin: 1mm 0 2mm; font-size: 9pt; color: #444; }
table.uc.common th { background: #fbe9e9; }
.applies { font-size: 8.5pt; color: #666; margin: -1mm 0 2mm; font-style: italic; }
.badge { font-size: 7.5pt; border: 1px solid; border-radius: 3mm; padding: 0 1.5mm; }
.badge.cert { color: #0066cc; } .badge.val { color: #3e8635; }
"""

if __name__ == "__main__":
    main()
