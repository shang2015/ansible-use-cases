#!/usr/bin/env python3
"""Collapse each collection's modules into resources (create/update/delete + info).

    python scripts/resource_index.py                 # all collections -> data/resources.json
    python scripts/resource_index.py azure.azcollection --print

A "resource" is a module name with the collection prefix and the read-only
suffix removed, so azure_rm_virtualmachine and azure_rm_virtualmachine_info
become one resource `virtualmachine` with operations manage + info.
Roles, playbooks and plugins are kept as their own entries.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INFO_SUFFIXES = ("_info", "_facts", "_list", "_stats", "_status", "_get")
KEEP_TYPES = ("module", "role", "playbook", "inventory", "lookup", "filter", "eda_event_source", "eda_event_filter", "connection", "callback", "test")


def module_prefix(names: list[str]) -> str:
    if len(names) < 3:
        return ""
    pre = os.path.commonprefix(names)
    return pre[: pre.rfind("_") + 1] if "_" in pre else ""


def build(col: dict) -> dict:
    items = [i for i in col.get("items", []) if i["type"] in KEEP_TYPES and not i.get("deprecated")]
    mods = [i for i in items if i["type"] == "module"]
    pre = module_prefix([m["name"] for m in mods])
    res: dict[str, dict] = defaultdict(lambda: {"manage": [], "info": [], "desc": ""})
    for m in mods:
        r = m["name"][len(pre):] if pre else m["name"]
        op = "manage"
        for suf in INFO_SUFFIXES:
            if r.endswith(suf) and len(r) > len(suf):
                r, op = r[: -len(suf)], "info"
                break
        entry = res[r]
        entry[op].append(m["name"])
        if op == "manage" or not entry["desc"]:
            entry["desc"] = m.get("short_description") or entry["desc"]
    others = [{"name": i["name"], "type": i["type"], "desc": i.get("short_description", "")}
              for i in items if i["type"] != "module"]
    return {
        "fqcn": col["fqcn"],
        "prefix": pre,
        "module_count": len(mods),
        "resources": {k: v for k, v in sorted(res.items())},
        "other": others,
    }


def main(argv):
    content = json.loads((ROOT / "data/content.json").read_text())
    wanted = [a for a in argv if not a.startswith("--")]
    out = {}
    for col in content:
        if wanted and col["fqcn"] not in wanted:
            continue
        out[col["fqcn"]] = build(col)
    if "--print" in argv:
        for fq, r in out.items():
            print(f"## {fq}  prefix={r['prefix']!r} modules={r['module_count']} resources={len(r['resources'])} other={len(r['other'])}")
            for name, e in r["resources"].items():
                ops = "+".join(o for o in ("manage", "info") if e[o])
                print(f"  {name} [{ops}] {e['desc']}")
            for o in r["other"]:
                print(f"  ({o['type']}) {o['name']} {o['desc']}")
        return
    (ROOT / "data/resources.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    n_res = sum(len(r["resources"]) + len(r["other"]) for r in out.values())
    print(f"{len(out)} collections, {n_res} resources/entries -> data/resources.json")


if __name__ == "__main__":
    main(sys.argv[1:])
