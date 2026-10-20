#!/usr/bin/env python3
"""Print a compact digest of collections and their content, for writing use cases.

    python scripts/digest.py --domain network          # collections mapped to a domain
    python scripts/digest.py cisco.ios network.backup  # specific collections
    python scripts/digest.py --grep snapshot           # search all items
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_pages import TYPE_ORDER, assign_domain, support  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fqcns", nargs="*")
    ap.add_argument("--domain")
    ap.add_argument("--grep")
    ap.add_argument("--max", type=int, default=400, help="max items per collection")
    a = ap.parse_args()
    cols = yaml.safe_load((ROOT / "data/collections.yml").read_text())
    domains = yaml.safe_load((ROOT / "data/domains.yml").read_text())
    content = {c["fqcn"]: c for c in json.loads((ROOT / "data/content.json").read_text())}
    if a.grep:
        g = a.grep.lower()
        for c in cols:
            for i in content.get(c["fqcn"], {}).get("items", []):
                if i["type"] in TYPE_ORDER and (g in i["fqcn"].lower() or g in (i["short_description"] or "").lower()):
                    print(f"{i['fqcn']}  [{i['type']}, {support(c.get('content_type'))}]  {i['short_description']}")
        return
    for c in sorted(cols, key=lambda c: c["fqcn"]):
        dom = c.get("domain") or assign_domain(c, domains)
        if a.fqcns and c["fqcn"] not in a.fqcns:
            continue
        if a.domain and dom != a.domain:
            continue
        items = [i for i in content.get(c["fqcn"], {}).get("items", []) if i["type"] in TYPE_ORDER]
        print(f"\n## {c['fqcn']}  [{support(c.get('content_type'))}] by {c.get('provider')} (domain: {dom})")
        print(f"   {c.get('description') or ''}")
        for i in items[: a.max]:
            dep = " (DEPRECATED)" if i.get("deprecated") else ""
            print(f"   - {i['type']}: {i['fqcn']}{dep} — {i['short_description']}")
        if len(items) > a.max:
            print(f"   ... {len(items) - a.max} more")


if __name__ == "__main__":
    main()
