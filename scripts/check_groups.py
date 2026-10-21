#!/usr/bin/env python3
"""Validate data/groups/<fqcn>.yml against data/resources.json.

    python scripts/check_groups.py                 # every groups file
    python scripts/check_groups.py cisco.ios ...   # specific collections
Exit code 1 on any problem.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [(3, 1, 1), (8, 1, 2), (20, 2, 4), (60, 4, 8), (200, 6, 15), (500, 12, 25), (10**9, 18, 35)]


def check(fq: str, idx: dict) -> list[str]:
    p = ROOT / "data/groups" / f"{fq}.yml"
    if not p.exists():
        return ["groups file missing"]
    try:
        g = yaml.safe_load(p.read_text())
    except Exception as e:  # noqa: BLE001
        return [f"YAML error: {e}"]
    errs = []
    r = idx.get(fq)
    if r is None:
        return ["collection not in data/resources.json"]
    if g.get("fqcn") != fq:
        errs.append(f"fqcn field is {g.get('fqcn')!r}")
    if not g.get("product"):
        errs.append("product missing")
    ucs = g.get("use_cases") or []
    want = set(r["resources"]) | {f"{o['type']}:{o['name']}" for o in r["other"]}
    got = [k for uc in ucs for k in (uc.get("components") or {})]
    missing, extra = want - set(got), set(got) - want
    dup = sorted({k for k in got if got.count(k) > 1})
    if missing:
        errs.append(f"missing {len(missing)}: {sorted(missing)[:15]}")
    if extra:
        errs.append(f"unknown keys {len(extra)}: {sorted(extra)[:15]}")
    if dup:
        errs.append(f"duplicates: {dup[:15]}")
    for i, uc in enumerate(ucs):
        for f in ("title", "description", "components"):
            if not uc.get(f):
                errs.append(f"use case {i + 1} has no {f}")
        for k, v in (uc.get("components") or {}).items():
            if not isinstance(v, str) or not v.strip():
                errs.append(f"component {k} has no label")
    n = len(want)
    lo, hi = next((lo, hi) for top, lo, hi in TARGETS if n <= top)
    if not (lo <= len(ucs) <= hi):
        errs.append(f"{len(ucs)} use cases for {n} entries (target {lo}-{hi})")
    return errs


def main(argv):
    idx = json.loads((ROOT / "data/resources.json").read_text())
    fqs = argv or sorted(p.stem for p in (ROOT / "data/groups").glob("*.yml"))
    bad = 0
    for fq in fqs:
        errs = check(fq, idx)
        if errs:
            bad += 1
            print(f"FAIL {fq}: " + " | ".join(errs))
        else:
            g = yaml.safe_load((ROOT / "data/groups" / f"{fq}.yml").read_text())
            print(f"OK   {fq}: {len(g['use_cases'])} use cases")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
