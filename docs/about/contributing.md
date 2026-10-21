---
title: Contributing
---

# Contributing

Use cases grow out of real engagements and new product features. Add one with a pull request.

## Add a use case

1. Pick the domain folder under `docs/use-cases/` (for example `docs/use-cases/security/`).
2. Copy the template below into a new file named after the outcome, such as `rotate-privileged-credentials.md`.
3. Write the two prose sections, **Description** and **Notes**, and keep each one short.
4. List the collections and the key modules, roles or playbooks in the front matter, using their fully qualified names. The site renders the use case as one table (**Description · Collection · Key content · Notes**), the same format as the PDF downloads, and the build fails if a name does not exist.
5. Run `make serve` and check the page.

## Template

```markdown
---
title: <Outcome, as a short verb phrase>
summary: <One sentence shown in the domain list>
order: 100                      # position in the domain list
personas: [<who asks for this>]
collections: [<namespace.name>, ...]
key_content:                    # modules, roles, playbooks (FQCN)
  - <namespace.name.module_or_role>
examples:                       # optional demos and repos
  - title: <name>
    url: <https://...>
    note: <optional>
---

# <Title>

## Description

<One short paragraph: the customer's goal in plain words.>

## Notes

- <Variations, pitfalls, related use cases, when to pair with Event-Driven Ansible>
```

## Refresh the generated pages

```bash
make data     # clone collection repos and re-extract modules (data/content.json)
make pages    # regenerate collection, vendor and domain pages
make serve    # preview at http://127.0.0.1:8000
make pdfs     # rebuild the 21 domain PDFs in docs/downloads/
```

`data/collections.yml` is the list of Certified and Validated collections, taken from the Red Hat Ecosystem Catalog. `data/vendors.yml` tracks security and observability vendor collections from every source. Both are plain YAML and can be edited by hand.

## Product use cases

Product use cases group a collection's modules by outcome (for example *Manage virtual networks and connectivity*) and list the components each one supports. They live in `data/groups/<collection>.yml`. When a collection adds modules, add the new resource keys to a use case there, following [GROUPING_GUIDE.md](https://github.com/shang2015/ansible-use-cases/blob/main/GROUPING_GUIDE.md), and run `python3 scripts/check_groups.py <collection>`.
