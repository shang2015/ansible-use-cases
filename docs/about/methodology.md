---
title: Methodology
---

# Methodology

## Where the data comes from

| Data | Source | How it is collected |
|---|---|---|
| Collection list, support level, provider, version, last updated | [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/platform/red-hat-ansible) | Collected from the catalog listings into `data/collections.yml` |
| Modules, roles, playbooks, plugins and their descriptions | Each collection's public source repository | `scripts/extract_content.py` clones the repository and reads `short_description` from module documentation, role `argument_specs` or `meta/main.yml`, and playbook names |
| Last commit date | Source repository | `git log -1` on the default branch |
| Vendor collections outside the catalog | Ansible Galaxy and vendor GitHub organisations | Researched per vendor into `data/vendors.yml` |
| Curated (solution) use cases | Field experience | Written by hand in `docs/use-cases/` |
| Product use cases | The modules of each collection | `scripts/resource_index.py` merges each resource's create/update/delete and `_info` modules into one component (`data/resources.json`); components are then grouped by customer outcome in `data/groups/<collection>.yml` and checked by `scripts/check_groups.py` |
| PDF downloads | All of the above | `scripts/build_pdfs.py` renders one PDF per domain into `docs/downloads/` |

## How often it is refreshed

- Every Monday, a GitHub Actions workflow re-clones every collection's source repository and re-extracts its modules, roles and plugins. If anything changed it opens a pull request; the site updates when the pull request is merged.
- The collection list and support levels from the Ecosystem Catalog, the vendor data, the product use case groups and the PDFs are refreshed by hand.

## Known limits

- Some certified collections do not publish their source publicly. Their pages show catalog metadata only; browse their content on Automation Hub.
- The version in a source repository's default branch can be ahead of, or behind, the version published on Automation Hub. The catalog version is the supported one.
- Module descriptions are the authors' own words and vary in style.
- A module added to a collection after its product use cases were grouped is not part of any product use case until it is added to `data/groups/`.
- Domain assignment is rule-based (`data/domains.yml`). A collection that spans several domains appears in one; use cases in other domains still reference it.
