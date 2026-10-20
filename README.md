# Ansible Automation Use Cases

A domain-by-domain reference of what Red Hat Ansible Automation Platform automates, with every use case mapped to the Red Hat **Certified** and **Validated** content collections, modules and roles that deliver it.

**Site:** https://shang2015.github.io/ansible-use-cases/

## What's inside

| Section | Content |
|---|---|
| `docs/use-cases/<domain>/` | Curated use cases, one folder per domain (platform, Linux, Windows, network, security, cloud/aws, cloud/azure, cloud/gcp, virtualization, storage, ITSM, event-driven...). Each use case follows the same format: **Description · Prerequisites · Steps · Success Criteria · Notes**, plus the collections and key modules. |
| `docs/vendors/` | Security and observability vendor collections: support level (Certified, Validated, Galaxy, vendor GitHub), maintainer, last update. Generated from `data/vendors.yml`. |
| `docs/collections/` | One page per Certified or Validated collection, listing every module, role, playbook and plugin as a module-level use case. Generated. |
| `docs/explorer.md` | Searchable Module Explorer across all collections. |
| `data/` | `collections.yml` (from the Red Hat Ecosystem Catalog), `content.json` (extracted from source repos), `vendors.yml`, `domains.yml` (taxonomy). |
| `scripts/` | `extract_content.py` (clone repos, extract modules), `build_pages.py` (generate pages and nav). |

## Run locally

```bash
pip install -r requirements.txt
make data    # optional: re-extract modules from every collection repo (a few minutes)
make serve   # generate pages and preview at http://127.0.0.1:8000
```

## Contribute a use case

Copy the template in [docs/about/contributing.md](docs/about/contributing.md) into the right domain folder, list the collections and key content by fully qualified name, and open a pull request. The build checks that every referenced collection and module exists.

## Disclaimer

Community reference maintained by Red Hat field staff; not an official Red Hat publication. Confirm support status on [Automation Hub](https://console.redhat.com/ansible/automation-hub) and the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/platform/red-hat-ansible). Ansible and Red Hat are trademarks of Red Hat, Inc.
