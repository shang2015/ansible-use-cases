---
title: Contributing
---

# Contributing

Use cases grow out of real engagements and new product features. Add one with a pull request.

## Add a use case

1. Pick the domain folder under `docs/use-cases/` (for example `docs/use-cases/security/`).
2. Copy the template below into a new file named after the outcome, such as `rotate-privileged-credentials.md`.
3. Fill in the five sections, keep each one short, and write steps as delivery tasks.
4. List the collections and the key modules, roles or playbooks in the front matter, using their fully qualified names. The site renders the table for you, with support level and descriptions, and the build fails if a name does not exist.
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

## Prerequisites

1.

## Steps

1.

## Success Criteria

1.

## Notes

-
```

## Refresh the generated pages

```bash
make data     # clone collection repos and re-extract modules (data/content.json)
make pages    # regenerate collection, vendor and domain pages
make serve    # preview at http://127.0.0.1:8000
```

`data/collections.yml` is the list of Certified and Validated collections, taken from the Red Hat Ecosystem Catalog. `data/vendors.yml` tracks security and observability vendor collections from every source. Both are plain YAML and can be edited by hand.
