#!/usr/bin/env python3
"""Check use case pages: required sections, front matter, and that every
referenced collection / module / role exists in data/collections.yml and
data/content.json.

    python scripts/validate_use_cases.py                       # all use cases
    python scripts/validate_use_cases.py docs/use-cases/linux  # one folder
Exit code 1 if any problem is found.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ["Description", "Prerequisites", "Steps", "Success Criteria", "Notes"]


def main(args):
    cols = {c["fqcn"] for c in yaml.safe_load((ROOT / "data/collections.yml").read_text())}
    content = set()
    for c in json.loads((ROOT / "data/content.json").read_text()):
        content.update(i["fqcn"] for i in c["items"])
    targets = [Path(a).resolve() for a in args] or [ROOT / "docs/use-cases"]
    files = []
    for t in targets:
        files += [t] if t.is_file() else sorted(t.rglob("*.md"))
    problems = 0
    checked = 0
    for f in files:
        if f.name == "index.md" or f.name.startswith("_"):
            continue
        checked += 1
        text = f.read_text()
        errs = []
        if not text.startswith("---"):
            errs.append("missing front matter")
            fm, body = {}, text
        else:
            _, raw, body = text.split("---", 2)
            fm = yaml.safe_load(raw) or {}
        for key in ("title", "summary", "collections", "key_content"):
            if not fm.get(key):
                errs.append(f"front matter '{key}' missing or empty")
        for s in SECTIONS:
            if not re.search(rf"^## {re.escape(s)}\s*$", body, re.M):
                errs.append(f"section '## {s}' missing")
        for c in fm.get("collections") or []:
            if c not in cols:
                errs.append(f"unknown collection: {c}")
        for k in fm.get("key_content") or []:
            if k not in content:
                errs.append(f"unknown key_content: {k}")
            elif ".".join(k.split(".")[:2]) not in (fm.get("collections") or []):
                errs.append(f"key_content {k} not covered by 'collections'")
        # Fully qualified names mentioned in the body must exist too
        for ref in sorted(set(re.findall(r"`([a-z0-9_]+\.[a-z0-9_]+\.[A-Za-z0-9_.]+)`", body))):
            col = ".".join(ref.split(".")[:2])
            if col in cols and ref not in content:
                errs.append(f"unknown content in body: {ref}")
        for ref in sorted(set(re.findall(r"`([a-z0-9_]+\.[a-z0-9_]+)`", body))):
            if re.fullmatch(r"[a-z0-9_]+\.[a-z0-9_]+", ref) and ref.split(".")[0] in {c.split(".")[0] for c in cols} \
                    and ref not in cols and not ref.endswith((".yml", ".yaml", ".cfg", ".json", ".py", ".md")):
                errs.append(f"unknown collection in body: {ref}")
        for link in re.findall(r"\]\(([^)#]+\.md)", body):
            if not (f.parent / link).resolve().exists():
                errs.append(f"broken link: {link}")
        if errs:
            problems += len(errs)
            print(f"\n{f.relative_to(ROOT)}")
            for e in errs:
                print(f"  - {e}")
    print(f"\nChecked {checked} use case files, {problems} problems.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
