# Ansible Automation Use Cases

A domain-by-domain reference of what Red Hat Ansible Automation Platform automates. Every use case is mapped to the Red Hat **Certified** and **Validated** content collections, modules and roles that deliver it, in one simple format.

**Site:** https://shang2015.github.io/ansible-use-cases/ · **PDFs:** [Downloads](https://shang2015.github.io/ansible-use-cases/downloads/)

## At a glance

| | |
|---|---|
| Domains | 21 (platform, Linux, Windows, network, security, AWS, Azure, Google Cloud, other clouds, multi-cloud, virtualization, Kubernetes, servers and mainframe, storage, ITSM, event-driven, applications, edge, AI, reporting, developer) |
| Solution use cases | 165, written by hand |
| Product use cases | 1,354, grouped from 18,279 module components across 238 collections |
| Collections | 264 Certified and Validated collections from the Red Hat Ecosystem Catalog, with 20,470 modules, roles, playbooks and plugins |
| Vendors | Security and observability vendors, with support level, source and last update |

## The format

Every use case, on the site and in the PDFs, is one table in the format of the original *Ansible Automation - Use Cases* document:

| Row | What it holds |
|---|---|
| **Description** | What the customer wants to achieve, in one paragraph. |
| **Collection** | The collections that deliver it, with support level (Certified or Validated), provider, version and last update date. |
| **Key content** | The key modules, roles and plugins. For a product use case, the components it supports with the modules that manage (create, update, delete) and query (`_info`) them. |
| **Notes** | Variations, pitfalls, related use cases and example repositories. |

There are two kinds of use case:

1. **Solution use cases**: outcome-level scenarios such as *Harden RHEL to CIS and DISA STIG baselines* or *Back up device configuration*, often combining several collections.
2. **Product use cases**: the modules of one collection grouped by customer outcome. For example, the 449 `azure.azcollection` modules become 24 use cases such as *Manage virtual networks and connectivity*, listing virtual networks, subnets, peering, route tables and NAT gateways as components, instead of one row per create/update/delete module.

## What's inside

| Path | Content |
|---|---|
| `docs/use-cases/<domain>/` | One folder per domain. `index.md` is the domain page: at-a-glance counts and the PDF link, every solution use case as a table, the product use cases per collection, and the collections in the domain. Each other `.md` file is one solution use case. |
| `docs/collections/` | One page per collection: version and last update, product use cases, then every module, role and plugin. Generated. |
| `docs/vendors/` | Security and observability vendor collections from every source (Certified, Validated, Galaxy, vendor GitHub). Generated from `data/vendors.yml`. |
| `docs/downloads/` | One PDF per domain, and `index.md` listing them. Built by `make pdfs`. |
| `docs/explorer.md` | Searchable Module Explorer across all collections. |
| `docs/about/` | How to use the site, contributing, methodology. |
| `data/collections.yml` | Certified and Validated collections from the Red Hat Ecosystem Catalog: support level, provider, version, last updated, repository. |
| `data/collection_overrides.yml` | Corrections to the catalog data (repositories, renamed collections, notes). |
| `data/content.json` | Modules, roles, playbooks and plugins extracted from each collection's source repository. |
| `data/resources.json` | Modules merged into resources (create/update/delete + `_info` of the same resource). |
| `data/groups/<collection>.yml` | Product use cases: the resources of a collection grouped by outcome, with friendly component labels. |
| `data/vendors.yml`, `data/domains.yml` | Vendor collections; domain taxonomy and the rules that map collections to domains. |
| `hooks/use_case_tables.py` | MkDocs hook that renders each solution use case as its table. |
| `scripts/` | See below. |

### Scripts

| Script | What it does |
|---|---|
| `extract_content.py` | Clones every collection's source repository and extracts its modules, roles and plugins into `data/content.json` (`make data`). |
| `resource_index.py` | Builds `data/resources.json` from `data/content.json` (`make resources`). |
| `check_groups.py` | Checks that every resource of a collection is in exactly one product use case (`make resources`). |
| `build_pages.py` | Generates the collection, vendor and domain pages and the navigation (`make pages`). |
| `validate_use_cases.py` | Checks solution use cases: required sections, and that every referenced collection, module and link exists. |
| `build_doc.py` | Renders one domain in the document format as HTML. |
| `build_pdfs.py` | Prints every domain to PDF into `docs/downloads/` and rewrites `docs/downloads/index.md` (`make pdfs`). |
| `digest.py` | Lists the content of a domain or collection, for writers. |

## Run locally

```bash
pip install -r requirements.txt
make serve        # generate pages and preview at http://127.0.0.1:8000
make build        # strict build into site/, fails on any broken reference
```

Rebuild the PDFs:

```bash
pip install -r requirements-pdf.txt && playwright install chromium
make pdfs
```

## How the content is kept up to date

| What | How often | How |
|---|---|---|
| Modules, roles and plugins of every collection (`data/content.json`) | Weekly, Mondays 03:17 UTC | The **Refresh module data** workflow re-clones every source repository and opens a pull request when something changed. Merge it to update the site. |
| Site | On every push to `main` | The **Build and deploy site** workflow builds with `--strict` and publishes to GitHub Pages. |
| Collection list, support level, version and last update (`data/collections.yml`), vendor data | By hand | Re-collected from the Red Hat Ecosystem Catalog and vendor sources. |
| Product use cases (`data/groups/`) | By hand, after a module refresh | Run `make resources`. New modules show up as `missing` in `check_groups.py`; add them to a use case following [GROUPING_GUIDE.md](GROUPING_GUIDE.md). |
| PDFs | By hand | `make pdfs`, then commit `docs/downloads/`. |

## Contribute

- **A solution use case:** copy the template in [docs/about/contributing.md](docs/about/contributing.md) into the right domain folder, write the **Description** and **Notes**, list the collections and key content by fully qualified name in the front matter, and open a pull request. See [WRITING_GUIDE.md](WRITING_GUIDE.md). The build checks that every referenced collection and module exists.
- **Product use cases:** edit `data/groups/<collection>.yml` following [GROUPING_GUIDE.md](GROUPING_GUIDE.md) and run `python3 scripts/check_groups.py <collection>`.

## Disclaimer

Community reference maintained by Red Hat field staff; not an official Red Hat publication. Confirm support status on [Automation Hub](https://console.redhat.com/ansible/automation-hub) and the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/platform/red-hat-ansible). Ansible and Red Hat are trademarks of Red Hat, Inc.
