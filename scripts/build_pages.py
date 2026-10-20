#!/usr/bin/env python3
"""Generate the data-driven pages of the site.

Reads   data/collections.yml   catalog collections (support level, provider, repo, dates)
        data/content.json      modules/roles/plugins per collection (extract_content.py)
        data/vendors.yml       security & observability vendor collections, any source
        data/domains.yml       domain taxonomy
Writes  docs/collections/*.md, docs/vendors/**, docs/use-cases/<domain>/_collections.md,
        docs/assets/content-index.json, mkdocs.yml (base config + generated nav)
"""
from __future__ import annotations

import fnmatch
import html
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

TYPE_ORDER = ["module", "role", "playbook", "inventory", "lookup", "filter", "test",
              "eda_event_source", "eda_event_filter", "connection", "callback", "action"]
TYPE_TITLE = {
    "module": "Modules", "role": "Roles", "playbook": "Playbooks", "inventory": "Inventory sources",
    "lookup": "Lookups", "filter": "Filters", "test": "Tests", "eda_event_source": "EDA event sources",
    "eda_event_filter": "EDA event filters", "connection": "Connections", "callback": "Callbacks",
    "action": "Action plugins",
}


def load():
    cols = yaml.safe_load((DATA / "collections.yml").read_text()) or []
    content = {}
    if (DATA / "content.json").exists():
        content = {c["fqcn"]: c for c in json.loads((DATA / "content.json").read_text())}
    vendors = []
    if (DATA / "vendors.yml").exists():
        vendors = yaml.safe_load((DATA / "vendors.yml").read_text()) or []
    domains = yaml.safe_load((DATA / "domains.yml").read_text())
    return cols, content, vendors, domains


def support(kind: str | None) -> str:
    k = (kind or "").lower()
    if "validated" in k:
        return "Validated"
    if "certified" in k:
        return "Certified"
    if "galaxy" in k or "community" in k:
        return "Galaxy (community)"
    if "github" in k:
        return "Vendor GitHub only"
    return kind or "Unknown"


def badge(kind: str | None) -> str:
    s = support(kind)
    cls = {"Validated": "uc-validated", "Certified": "uc-certified",
           "Galaxy (community)": "uc-galaxy", "Vendor GitHub only": "uc-github"}.get(s, "")
    return f'<span class="uc-badge {cls}">{s}</span>'


def assign_domain(col: dict, domains: list[dict]) -> str:
    fqcn = col["fqcn"]
    for d in domains:
        if d["id"] == "other":
            continue
        if any(fnmatch.fnmatch(fqcn, p) for p in d.get("match", [])):
            return d["id"]
    cats = set(col.get("categories") or [])
    for d in domains:
        if cats & set(d.get("categories", [])):
            return d["id"]
    return "other"


def hub_url(col: dict, item: dict | None = None) -> str:
    ns, name = col["fqcn"].split(".", 1)
    repo = "validated" if support(col.get("content_type")) == "Validated" else "published"
    url = f"https://console.redhat.com/ansible/automation-hub/repo/{repo}/{ns}/{name}/"
    if item and item["type"] in ("module", "inventory", "lookup", "filter", "test", "connection", "callback"):
        url += f"content/{item['type']}/{item['name']}/"
    elif item and item["type"] == "role":
        url += f"content/role/{item['name']}/"
    return url


def src_url(col: dict, content: dict, item: dict) -> str:
    if item.get("repository"):
        return item["repository"]
    repo = (col.get("repository") or "").rstrip("/")
    m = re.match(r"(https?://(?:github|gitlab)\.com/[^/]+/[^/#?]+)", repo)
    if not m:
        return ""
    base = m.group(1).removesuffix(".git")
    sub = content.get("source_path") or ""
    path = "/".join(p for p in (sub, item["source"]) if p)
    return f"{base}/blob/HEAD/{path}" if "." in Path(item["source"]).name else f"{base}/tree/HEAD/{path}"


def anchor(name: str) -> str:
    return name.replace(".", "").replace("_", "-").lower()


def cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ")


def date_only(value: str | None) -> str:
    return (value or "")[:10]


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def collection_page(col, content, domain_title):
    fq = col["fqcn"]
    items = [i for i in content.get("items", []) if i["type"] in TYPE_ORDER]
    lines = [
        "---", f"title: {fq}", "hide: [navigation]", "---", "",
        f"# `{fq}`", "",
        f"{badge(col.get('content_type'))} &nbsp; **{col.get('provider') or 'Unknown provider'}** &nbsp;·&nbsp; domain: {domain_title}", "",
        f"{col.get('description') or content.get('galaxy', {}).get('description') or ''}", "",
    ]
    meta_rows = [
        ("Latest version (catalog)", col.get("latest_version") or "–"),
        ("Version in source repo", content.get("galaxy", {}).get("version") or "–"),
        ("Catalog last updated", col.get("last_updated") or "–"),
        ("Last commit in source repo", date_only(content.get("last_commit")) or "–"),
    ]
    links = []
    if col.get("catalog_url"):
        links.append(f"[Ecosystem Catalog]({col['catalog_url']})")
    if support(col.get("content_type")) in ("Certified", "Validated"):
        links.append(f"[Automation Hub]({hub_url(col)})")
    if col.get("repository"):
        links.append(f"[Source]({col['repository']})")
    if col.get("documentation"):
        links.append(f"[Documentation]({col['documentation']})")
    if content.get("upstream"):
        meta_rows.append(("Built from upstream", f"<code>{html.escape(content['upstream'])}</code> (module list read from the upstream source)"))
    link_html = " · ".join(re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', l) for l in links) or "–"
    meta_rows.append(("Links", link_html))
    lines += ['<table class="uc-meta"><tbody>'] + [f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in meta_rows] + ["</tbody></table>", ""]

    if items and col.get("note"):
        lines += ['!!! note', f"    {col['note']}", ""]
    if not items:
        status = content.get("status", "not extracted")
        reason = col.get("note") or {
            "no-public-repo": "The source repository is not public, so module-level detail is not listed here. Browse the content on Automation Hub.",
            "clone-failed": "The source repository listed in the catalog is not publicly readable. Browse the content on Automation Hub.",
            "not-extracted": "This collection's content is generated from a very large upstream repository, so it is not listed module by module here. Browse it on Automation Hub.",
            "repo-holds-other-collection": "The repository listed in the catalog now hosts a different (often renamed) collection, so its modules are not attributed here. Check Automation Hub for this collection's content.",
        }.get(status, "No modules, roles or plugins were found in the source repository.")
        lines += ['!!! note "Module-level use cases not available"', f"    {reason}", ""]
        return "\n".join(lines) + "\n"

    counts = defaultdict(int)
    for i in items:
        counts[i["type"]] += 1
    lines += ["## Module-level use cases", "",
              "Every module, role and plugin below is a use case in its own right. The description is the collection author's own one-line summary.", "",
              " · ".join(f"**{counts[t]}** {TYPE_TITLE[t].lower()}" for t in TYPE_ORDER if counts[t]), ""]
    for t in TYPE_ORDER:
        group = [i for i in items if i["type"] == t]
        if not group:
            continue
        lines += [f"### {TYPE_TITLE[t]}", "", '<table class="uc-items"><thead><tr><th>Name</th><th>Use case</th><th>Links</th></tr></thead><tbody>']
        for i in sorted(group, key=lambda x: x["name"]):
            desc = html.escape(i.get("short_description") or "—")
            if i.get("deprecated"):
                desc = '<span class="uc-badge uc-deprecated">Deprecated</span> ' + desc
            ilinks = []
            if support(col.get("content_type")) in ("Certified", "Validated") and t != "playbook":
                ilinks.append(f'<a href="{hub_url(col, i)}">Hub</a>')
            s = src_url(col, content, i)
            if s:
                ilinks.append(f'<a href="{s}">Source</a>')
            lines.append(f'<tr id="{anchor(i["name"])}"><td><code>{html.escape(i["name"])}</code></td><td>{desc}</td><td>{" · ".join(ilinks)}</td></tr>')
        lines += ["</tbody></table>", ""]
    return "\n".join(lines) + "\n"


def collections_table(rows, depth: int, show_domain=False, dom_titles=None):
    head = "| Collection | Support | Provider | Items | Updated |" + (" Domain |" if show_domain else "")
    sep = "|---|---|---|---:|---|" + ("---|" if show_domain else "")
    out = [head, sep]
    prefix = "../" * depth
    for col, content, dom in rows:
        n = len([i for i in content.get("items", []) if i["type"] in TYPE_ORDER]) or "–"
        upd = col.get("last_updated") or date_only(content.get("last_commit")) or "–"
        line = f"| [`{col['fqcn']}`]({prefix}collections/{col['fqcn']}.md) | {badge(col.get('content_type'))} | {cell(col.get('provider'))} | {n} | {cell(upd)} |"
        if show_domain:
            line += f" {dom_titles[dom]} |"
        out.append(line)
    return "\n".join(out) + "\n"


def vendor_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def vendor_pages(vendors, cols_by_fqcn, content):
    if not vendors:
        return []
    out_nav = []
    by_domain = defaultdict(lambda: defaultdict(list))
    for v in vendors:
        by_domain[v["domain"]][v["vendor"]].append(v)
    titles = {"security": "Security vendors", "observability": "Observability vendors"}
    index = ["# Vendor collections", "",
             "Where each security and observability vendor's Ansible content comes from, how it is supported, and how fresh it is.", "",
             '!!! info "How to read the support level"',
             "    - **Certified** — published on Red Hat Automation Hub, tested and supported jointly by Red Hat and the partner.",
             "    - **Validated** — Red Hat Validated Content on Automation Hub: opinionated, tested roles and playbooks built by Red Hat.",
             "    - **Galaxy (community)** — available on Ansible Galaxy; not supported by Red Hat (the vendor may still support it).",
             "    - **Vendor GitHub only** — published only in the vendor's own repository.", ""]
    for dom in ("security", "observability"):
        if dom not in by_domain:
            continue
        index += [f"## {titles[dom]}", "", "| Vendor | Collections | Best support level | Most recent update |", "|---|---|---|---|"]
        rank = {"Certified": 0, "Validated": 1, "Galaxy (community)": 2, "Vendor GitHub only": 3}
        for vendor in sorted(by_domain[dom], key=str.lower):
            entries = by_domain[dom][vendor]
            real = [e for e in entries if e.get("fqcn")]
            slug = vendor_slug(vendor)
            best = min((support(e.get("support_level")) for e in real), key=lambda s: rank.get(s, 9), default=None)
            latest = max((vendor_latest(e) for e in real), default="")
            index.append(f"| [{vendor}]({dom}/{slug}.md) | {len(real) or 'none found'} | {badge(best) if best else '–'} | {latest or '–'} |")
            write(DOCS / "vendors" / dom / f"{slug}.md", vendor_page(vendor, dom, entries, cols_by_fqcn, content))
            out_nav.append((dom, vendor, f"vendors/{dom}/{slug}.md"))
        index.append("")
    write(DOCS / "vendors" / "index.md", "\n".join(index) + "\n")
    return out_nav


def vendor_latest(e) -> str:
    """Most recent known activity for a vendor collection (catalog, Galaxy, commit)."""
    dates = [date_only(e.get(k)) for k in ("catalog_updated", "galaxy_updated", "last_updated", "last_commit")]
    return max((d for d in dates if re.match(r"\d{4}-\d{2}-\d{2}", d or "")), default="")


def vendor_page(vendor, dom, entries, cols_by_fqcn, content):
    sub = sorted({e.get("subcategory") for e in entries if e.get("subcategory")})
    lines = ["---", f"title: {vendor}", "hide: [toc]", "---", "", f"# {vendor}", "",
             f"*{dom.title()} vendor*" + (f" · {', '.join(sub)}" if sub else ""), ""]
    real = [e for e in entries if e.get("fqcn")]
    if not real:
        note = next((e.get("notes") for e in entries if e.get("notes")), "No Ansible collection found.")
        if any(e.get("search_complete") is False for e in entries):
            note += " (Search not exhaustive.)"
        lines += ['!!! warning "No Ansible collection found"', f"    {note}", ""]
        return "\n".join(lines) + "\n"
    for e in real:
        if e.get("status") == "deprecated":
            lines += [f'!!! danger "`{e["fqcn"]}` is deprecated"', f"    {e.get('notes', '').split('. ')[0]}.", ""]
    lines += ["| Collection | Support | Maintainer | Certified version | Galaxy latest | EDA | Status |",
              "|---|---|---|---|---|---|---|"]
    rank = {"Certified": 0, "Validated": 1, "Galaxy (community)": 2, "Vendor GitHub only": 3}
    for e in sorted(real, key=lambda x: (rank.get(support(x.get("support_level")), 9), x["fqcn"])):
        fq = e["fqcn"]
        name = f"[`{fq}`](../../collections/{fq}.md)" if fq in cols_by_fqcn else f"`{fq}`"
        if e.get("third_party") or (e.get("maintainer") == "community" and support(e.get("support_level")) != "Certified"):
            name += " <small>(third party)</small>"
        eda = {True: "Yes", False: "No"}.get(e.get("eda_event_source"), "–")
        cert = f"{e['certified_version']} ({date_only(e.get('catalog_updated')) or '–'})" if e.get("certified_version") else "–"
        gal = f"{e['galaxy_version']} ({date_only(e.get('galaxy_updated')) or '–'})" if e.get("galaxy_version") else "–"
        if not e.get("certified_version") and not e.get("galaxy_version") and e.get("latest_version"):
            gal = f"{e['latest_version']} ({date_only(e.get('last_updated')) or '–'})"
        status = e.get("status") or "–"
        if status == "deprecated":
            status = '<span class="uc-badge uc-deprecated">deprecated</span>'
        lines.append(f"| {name} | {badge(e.get('support_level'))} | {cell(e.get('maintainer') or 'unknown')} | {cell(cert)} | {cell(gal)} | "
                     f"{eda} | {status} |")
    lines += ["", "## Notes and sources", ""]
    for e in sorted(real, key=lambda x: x["fqcn"]):
        links = [f"[{lbl}]({e[k]})" for lbl, k in (("Catalog", "catalog_url"), ("Galaxy", "galaxy_url"), ("Source", "repository")) if e.get(k)]
        lines += [f"### `{e['fqcn']}`", ""]
        if e.get("notes"):
            lines += [e["notes"], ""]
        facts = []
        if e.get("last_commit"):
            facts.append(f"Last commit in source: **{date_only(e['last_commit'])}**")
        if e.get("module_count") is not None:
            facts.append(f"Modules in source: **{e['module_count']}**")
        if facts:
            lines += [" · ".join(facts), ""]
        if links:
            lines += [" · ".join(links), ""]
    return "\n".join(lines) + "\n"


def use_case_pages(domain):
    """Return (title, relative path) for hand-written use cases in a domain folder."""
    folder = DOCS / "use-cases" / domain["path"]
    pages = []
    for p in sorted(folder.glob("*.md")):
        if p.name in ("index.md",) or p.name.startswith("_"):
            continue
        text = p.read_text()
        m = re.search(r"^title:\s*(.+)$", text, re.M) or re.search(r"^#\s+(.+)$", text, re.M)
        title = m.group(1).strip().strip("'\"") if m else p.stem
        order = re.search(r"^order:\s*(\d+)", text, re.M)
        pages.append((int(order.group(1)) if order else 999, title, str(p.relative_to(DOCS))))
    return [(t, r) for _, t, r in sorted(pages)]


def main():
    cols, content, vendors, domains = load()
    dom_titles = {d["id"]: d["title"] for d in domains}
    cols_by_fqcn = {c["fqcn"]: c for c in cols}

    # Clean generated output
    shutil.rmtree(DOCS / "collections", ignore_errors=True)
    shutil.rmtree(DOCS / "vendors", ignore_errors=True)

    rows_by_domain = defaultdict(list)
    all_rows = []
    explorer = []
    for col in sorted(cols, key=lambda c: c["fqcn"]):
        dom = col.get("domain") or assign_domain(col, domains)
        c = content.get(col["fqcn"], {})
        write(DOCS / "collections" / f"{col['fqcn']}.md", collection_page(col, c, dom_titles[dom]))
        rows_by_domain[dom].append((col, c, dom))
        all_rows.append((col, c, dom))
        for i in c.get("items", []):
            if i["type"] not in TYPE_ORDER:
                continue
            explorer.append({
                "n": i["fqcn"], "t": i["type"], "d": i.get("short_description") or "",
                "c": col["fqcn"], "s": support(col.get("content_type")), "m": dom,
                "x": 1 if i.get("deprecated") else 0,
            })

    total_items = len(explorer)
    idx = ["---", "title: All collections", "hide: [navigation]", "---", "",
           "# All collections", "",
           f"**{len(cols)}** Red Hat Certified and Validated collections, with **{total_items:,}** modules, roles, playbooks and plugins.", "",
           "Use the [Module Explorer](../explorer.md) to search across all of them.", "",
           collections_table(all_rows, 1, show_domain=True, dom_titles=dom_titles)]
    write(DOCS / "collections" / "index.md", "\n".join(idx))

    for d in domains:
        rows = rows_by_domain.get(d["id"], [])
        if d["id"] == "other" and not rows:
            continue
        depth = d["path"].count("/") + 2
        text = (collections_table(rows, depth) if rows else "_No certified or validated collections are mapped to this domain yet._\n")
        write(DOCS / "use-cases" / d["path"] / "_collections.md", text)
        index = DOCS / "use-cases" / d["path"] / "index.md"
        if not index.exists():
            write(index, f"---\ntitle: {d['title']}\n---\n\n# {d['title']}\n\n{d['summary']}\n\n"
                         f"## Use cases\n\n<!-- use-case-list -->\n\n## Collections in this domain\n\n--8<-- \"use-cases/{d['path']}/_collections.md\"\n")

    # Domain grid on the use case overview page
    grid = ['<div class="uc-grid" markdown>']
    for d in domains:
        if d["id"] == "other" and not rows_by_domain.get("other"):
            continue
        n_uc = len(use_case_pages(d))
        n_col = len(rows_by_domain.get(d["id"], []))
        grid.append(f'<a class="uc-card" href="{d["path"]}/"><strong>:{d["icon"].replace("/", "-")}: {d["title"]}</strong>'
                    f'<span>{d["summary"]}<br>{n_uc} use cases · {n_col} collections</span></a>')
    grid.append("</div>")
    write(DOCS / "use-cases" / "_domain-grid.md", "\n".join(grid) + "\n")
    cloud_index = DOCS / "use-cases" / "cloud" / "index.md"
    if not cloud_index.exists():
        cards = ['<div class="uc-grid" markdown>'] + [
            f'<a class="uc-card" href="{d["path"].split("/", 1)[1]}/"><strong>{d["title"]}</strong><span>{d["summary"]}</span></a>'
            for d in domains if d["path"].startswith("cloud/")] + ["</div>"]
        write(cloud_index, "---\ntitle: Cloud\n---\n\n# Cloud\n\nPublic, private and multi-cloud automation, one folder per provider.\n\n" + "\n".join(cards) + "\n")

    write(DOCS / "assets" / "content-index.json", json.dumps(explorer, ensure_ascii=False, separators=(",", ":")))

    vnav = vendor_pages(vendors, cols_by_fqcn, content)

    # Navigation
    uc_nav = [{"Overview": "use-cases/index.md"}]
    cloud = []
    for d in domains:
        pages = use_case_pages(d)
        if d["id"] == "other" and not pages and not rows_by_domain.get("other"):
            continue
        entry = [f"use-cases/{d['path']}/index.md"] + [{t: r} for t, r in pages]
        if d["path"].startswith("cloud/"):
            cloud.append({d["title"]: entry})
        else:
            uc_nav.append({d["title"]: entry})
    # place Cloud after Security
    pos = next((i for i, n in enumerate(uc_nav) if "Security" in n), len(uc_nav) - 1) + 1
    uc_nav.insert(pos, {"Cloud": ["use-cases/cloud/index.md"] + cloud})
    vendor_nav = ["vendors/index.md"]
    for dom, title in (("security", "Security"), ("observability", "Observability")):
        items = [{v: p} for d, v, p in vnav if d == dom]
        if items:
            vendor_nav.append({title: items})
    nav = [
        {"Home": "index.md"},
        {"Use cases": uc_nav},
        {"Vendors": vendor_nav},
        {"Collections": [{"All collections": "collections/index.md"}, {"Module Explorer": "explorer.md"}]},
        {"About": ["about/how-to-use.md", "about/contributing.md", "about/methodology.md"]},
    ]
    base = (ROOT / "mkdocs.base.yml").read_text()
    write(ROOT / "mkdocs.yml", "# GENERATED by scripts/build_pages.py from mkdocs.base.yml - edit that file instead.\n"
          + base + "\n" + yaml.safe_dump({"nav": nav}, sort_keys=False, allow_unicode=True))
    print(f"{len(cols)} collections, {total_items} items, {len(vnav)} vendor pages")


if __name__ == "__main__":
    main()
