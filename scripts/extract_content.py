#!/usr/bin/env python3
"""Clone every collection listed in data/collections.yml and extract its content.

For each collection we record every module, plugin (inventory, lookup, filter,
connection, callback, action...), EDA event source / filter, role and playbook,
together with the one-line description the authors wrote for it. Those
one-liners are what the site turns into "use cases" at module level.

Usage:
    python scripts/extract_content.py                # all collections
    python scripts/extract_content.py cisco.ios ...  # only these
Output: data/content.json
"""
from __future__ import annotations

import ast
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = Path(os.environ.get("CONTENT_CACHE", tempfile.gettempdir())) / "collection-src"

UPSTREAM: dict[str, str] = {}

PLUGIN_TYPES = [
    "modules", "inventory", "lookup", "filter", "test", "connection", "callback",
    "action", "become", "cache", "cliconf", "httpapi", "netconf", "terminal", "vars",
    "strategy", "shell",
]


def clone(repo: str, dest: Path) -> bool:
    if (dest / ".git").exists():
        return True
    if dest.exists():
        shutil.rmtree(dest)
    url = repo.rstrip("/")
    # Normalise browse URLs like https://github.com/org/repo/tree/main/sub
    m = re.match(r"(https?://(?:github|gitlab)\.com/[^/]+/[^/#?]+)", url)
    if m:
        url = m.group(1)
    if url.endswith(".git"):
        url = url[:-4]
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--quiet", url + ".git", str(dest)],
            check=True, timeout=240, capture_output=True,
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        )
        return True
    except Exception:
        return False


def find_collection_root(repo_dir: Path, fqcn: str):
    """Locate the directory holding galaxy.yml for this collection (may be nested)."""
    ns, name = fqcn.split(".", 1)
    candidates = []
    for gy in list(repo_dir.rglob("galaxy.yml")) + list(repo_dir.rglob("galaxy.yaml")):
        if any(p in gy.parts for p in (".git", "tests", "node_modules")):
            continue
        try:
            meta = yaml.safe_load(gy.read_text(errors="ignore")) or {}
        except Exception:
            meta = {}
        score = 0
        if str(meta.get("namespace", "")).strip() == ns and str(meta.get("name", "")).strip() == name:
            score = 10
        elif "{{" in gy.read_text(errors="ignore"):  # templated galaxy.yml
            score = 1
        candidates.append((score, -len(gy.parts), gy.parent))
    if candidates:
        candidates.sort(reverse=True)
        if candidates[0][0] == 0:
            # galaxy.yml names a different collection. Usually this is the upstream
            # project that Red Hat or the partner rebuilds under the certified
            # namespace (awx.awx -> ansible.controller). Known renames that are
            # *not* the same content are excluded in collection_overrides.yml.
            gy = candidates[0][2] / "galaxy.yml"
            try:
                meta = yaml.safe_load(gy.read_text(errors="ignore")) or {}
                UPSTREAM[fqcn] = f"{meta.get('namespace')}.{meta.get('name')}"
            except Exception:
                UPSTREAM[fqcn] = "unknown"
        return candidates[0][2]
    if (repo_dir / "plugins").exists() or (repo_dir / "roles").exists():
        return repo_dir
    return None


def _first_line(value) -> str:
    if isinstance(value, list):
        value = value[0] if value else ""
    text = str(value or "").strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[ILMBCOUV]\(([^)]*)\)", r"\1", text)  # Ansible doc markup
    return text


def parse_doc_string(source: str) -> dict | None:
    """Return the parsed DOCUMENTATION yaml from a python plugin file."""
    try:
        tree = ast.parse(source)
    except Exception:
        tree = None
    if tree is not None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "DOCUMENTATION":
                        try:
                            value = ast.literal_eval(node.value)
                        except Exception:
                            continue
                        if isinstance(value, str):
                            try:
                                return yaml.safe_load(value)
                            except Exception:
                                return None
    m = re.search(r"DOCUMENTATION\s*=\s*r?(['\"]{3})(.*?)\1", source, re.S)
    if m:
        try:
            return yaml.safe_load(m.group(2))
        except Exception:
            return None
    return None


def plugin_entry(path: Path, ptype: str, fqcn: str, root: Path) -> dict | None:
    name = path.stem
    if name.startswith("_") and name != "__init__":
        name = name[1:]
    if name == "__init__":
        return None
    doc = None
    if path.suffix == ".py":
        doc = parse_doc_string(path.read_text(errors="ignore"))
    elif path.suffix in (".yml", ".yaml"):
        try:
            loaded = yaml.safe_load(path.read_text(errors="ignore")) or {}
            doc = loaded.get("DOCUMENTATION", loaded)
            if isinstance(doc, str):
                doc = yaml.safe_load(doc)
        except Exception:
            doc = None
    if not isinstance(doc, dict):
        doc = {}
    short = _first_line(doc.get("short_description")) or _first_line(doc.get("description"))
    if path.suffix != ".py":
        # .yml docs (filters, tests, Windows modules) carry the plugin name; for
        # .py plugins Ansible loads them by file name, so the file name wins.
        name = str(doc.get("module") or doc.get("name") or name)
    deprecated = bool(doc.get("deprecated")) or "deprecated" in short.lower()
    return {
        "name": name,
        "fqcn": f"{fqcn}.{name}",
        "type": "module" if ptype == "modules" else ptype,
        "short_description": short,
        "deprecated": deprecated,
        "source": str(path.relative_to(root)),
    }


def extract_plugins(root: Path, fqcn: str) -> list[dict]:
    items: dict[tuple, dict] = {}
    for ptype in PLUGIN_TYPES:
        pdir = root / "plugins" / ptype
        if not pdir.is_dir():
            continue
        files = sorted(pdir.rglob("*"))
        for path in files:
            if not path.is_file() or path.suffix not in (".py", ".yml", ".yaml", ".ps1"):
                continue
            if path.suffix == ".ps1":
                continue  # docs live in the sibling .py/.yml for Windows modules
            if ptype in ("filter", "test") and path.suffix == ".py":
                # filter/test .py files hold code for many plugins; docs are in .yml
                if any(path.with_suffix(s).exists() for s in (".yml", ".yaml")):
                    continue
                if parse_doc_string(path.read_text(errors="ignore")) is None:
                    continue
            entry = plugin_entry(path, ptype, fqcn, root)
            if entry is None:
                continue
            key = (entry["type"], entry["name"])
            if key not in items or (not items[key]["short_description"] and entry["short_description"]):
                items[key] = entry
    # Event-Driven Ansible content
    for sub, ptype in (("event_source", "eda_event_source"), ("event_filter", "eda_event_filter")):
        edir = root / "extensions" / "eda" / "plugins" / sub
        if edir.is_dir():
            for path in sorted(edir.glob("*.py")):
                entry = plugin_entry(path, ptype, fqcn, root)
                if entry:
                    entry["type"] = ptype
                    items[(ptype, entry["name"])] = entry
    # Action plugins usually back a module of the same name; keep only documented,
    # stand-alone ones. Drop undocumented connection plumbing.
    module_names = {n for (t, n) in items if t == "module"}
    plumbing = {"terminal", "cliconf", "netconf", "httpapi", "shell", "strategy", "become", "cache"}
    cleaned = []
    for (t, n), e in items.items():
        if t == "action" and (n in module_names or not e["short_description"]):
            continue
        if t in plumbing and not e["short_description"]:
            continue
        cleaned.append(e)
    return cleaned


def extract_roles(root: Path, fqcn: str) -> list[dict]:
    out = []
    rdir = root / "roles"
    if not rdir.is_dir():
        return out
    for role in sorted(p for p in rdir.iterdir() if p.is_dir() and not p.name.startswith(".")):
        short = ""
        for spec in ("meta/argument_specs.yml", "meta/argument_specs.yaml"):
            sp = role / spec
            if sp.exists():
                try:
                    specs = (yaml.safe_load(sp.read_text(errors="ignore")) or {}).get("argument_specs", {})
                    main = specs.get("main") or next(iter(specs.values()), {})
                    short = _first_line(main.get("short_description")) or _first_line(main.get("description"))
                except Exception:
                    pass
            if short:
                break
        if not short:
            mp = role / "meta" / "main.yml"
            if mp.exists():
                try:
                    gi = (yaml.safe_load(mp.read_text(errors="ignore")) or {}).get("galaxy_info", {}) or {}
                    short = _first_line(gi.get("description"))
                except Exception:
                    pass
        placeholder = re.fullmatch(r"(the )?[\w.-]+ role\.?|your (role )?description|role description", short.strip().lower()) if short else True
        if not short or placeholder:
            readme = next((role / n for n in ("README.md", "README.rst", "readme.md") if (role / n).exists()), None)
            if readme:
                short = readme_summary(readme.read_text(errors="ignore"))
        out.append({
            "name": role.name,
            "fqcn": f"{fqcn}.{role.name}",
            "type": "role",
            "short_description": short,
            "deprecated": "deprecated" in short.lower(),
            "source": str(role.relative_to(root)),
        })
    return out


def readme_summary(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "=", "-", "[!", "!", "<", "|", "```", ":", "..", "*")):
            continue
        if len(s) < 15:
            continue
        return _first_line(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s))[:300]
    return ""


def extract_playbooks(root: Path, fqcn: str) -> list[dict]:
    out = []
    pdir = root / "playbooks"
    if not pdir.is_dir():
        return out
    for pb in sorted(pdir.rglob("*.y*ml")):
        if any(part in ("vars", "group_vars", "host_vars", "templates", "files", "tasks") for part in pb.relative_to(pdir).parts[:-1]):
            continue
        try:
            plays = yaml.safe_load(pb.read_text(errors="ignore"))
        except Exception:
            continue
        if not isinstance(plays, list) or not plays or not isinstance(plays[0], dict):
            continue
        if not any(k in plays[0] for k in ("hosts", "import_playbook", "ansible.builtin.import_playbook")):
            continue
        title = plays[0].get("name") or ""
        rel = pb.relative_to(pdir).with_suffix("")
        name = ".".join(rel.parts)
        out.append({
            "name": name,
            "fqcn": f"{fqcn}.{name}",
            "type": "playbook",
            "short_description": _first_line(title),
            "deprecated": False,
            "source": str(pb.relative_to(root)),
        })
    return out


def process_role_repos(col: dict, result: dict) -> dict:
    """Collections assembled from one repository per role (e.g. RHEL System Roles)."""
    spec = col["role_repos"]
    fqcn = col["fqcn"]
    items, dates = [], []
    for role in spec["roles"]:
        dest = CACHE / fqcn / role
        if not clone(spec["base"].rstrip("/") + "/" + role, dest):
            continue
        out = subprocess.run(["git", "-C", str(dest), "log", "-1", "--format=%cI"], capture_output=True, text=True)
        dates.append(out.stdout.strip())
        tmp = CACHE / f"{fqcn}.__roles"
        (tmp / "roles").mkdir(parents=True, exist_ok=True)
        link = tmp / "roles" / role
        if not link.exists():
            link.symlink_to(dest)
        for r in extract_roles(tmp, fqcn):
            if r["name"] == role:
                published = spec.get("rename", {}).get(role, role)
                r["name"], r["fqcn"] = published, f"{fqcn}.{published}"
                r["source"] = ""
                r["repository"] = spec["base"].rstrip("/") + "/" + role
                items.append(r)
    result["items"] = items
    result["last_commit"] = max(dates) if dates else ""
    result["status"] = "ok" if items else "empty"
    return result


def process(col: dict) -> dict:
    fqcn = col["fqcn"]
    repo = col.get("repository") or ""
    result = {"fqcn": fqcn, "status": "ok", "items": [], "galaxy": {}}
    if col.get("role_repos"):
        return process_role_repos(col, result)
    if col.get("extract") is False:
        result["status"] = "not-extracted"
        return result
    if not re.match(r"https?://(github|gitlab)\.com/", repo):
        result["status"] = "no-public-repo"
        return result
    dest = CACHE / fqcn
    if not clone(repo, dest):
        result["status"] = "clone-failed"
        return result
    try:
        result["last_commit"] = subprocess.run(
            ["git", "-C", str(dest), "log", "-1", "--format=%cI"],
            capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        pass
    root = find_collection_root(dest, fqcn)
    if root == "mismatch":
        result["status"] = "repo-holds-other-collection"
        return result
    if root is None:
        result["status"] = "no-collection-found"
        return result
    for gyname in ("galaxy.yml", "galaxy.yaml"):
        gy = root / gyname
        if gy.exists():
            try:
                meta = yaml.safe_load(gy.read_text(errors="ignore")) or {}
                result["galaxy"] = {
                    k: meta.get(k) for k in ("version", "description", "tags", "repository", "documentation")
                }
            except Exception:
                pass
    result["source_path"] = str(root.relative_to(dest)) if root != dest else ""
    if fqcn in UPSTREAM:
        result["upstream"] = UPSTREAM[fqcn]
    items = extract_plugins(root, fqcn) + extract_roles(root, fqcn) + extract_playbooks(root, fqcn)
    result["items"] = sorted(items, key=lambda i: (i["type"] != "module", i["type"], i["name"]))
    if not items:
        result["status"] = "empty"
    return result


def main(argv: list[str]) -> None:
    cols = yaml.safe_load((DATA / "collections.yml").read_text())
    if argv:
        cols = [c for c in cols if c["fqcn"] in argv]
    CACHE.mkdir(parents=True, exist_ok=True)
    existing = {}
    out_file = DATA / "content.json"
    if argv and out_file.exists():
        existing = {c["fqcn"]: c for c in json.loads(out_file.read_text())}
    with cf.ThreadPoolExecutor(max_workers=int(os.environ.get("WORKERS", "12"))) as pool:
        for res in pool.map(process, cols):
            existing[res["fqcn"]] = res
            print(f"{res['status']:>20}  {len(res['items']):4d}  {res['fqcn']}", flush=True)
    ordered = [existing[k] for k in sorted(existing)]
    out_file.write_text(json.dumps(ordered, indent=1, ensure_ascii=False) + "\n")
    total = sum(len(c["items"]) for c in ordered)
    print(f"\n{len(ordered)} collections, {total} content items -> {out_file}")


if __name__ == "__main__":
    main(sys.argv[1:])
