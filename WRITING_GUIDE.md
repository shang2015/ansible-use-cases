# Writing guide for use case pages

This guide is for anyone (human or AI) adding use cases under `docs/use-cases/`.

## Audience and purpose

Readers are Red Hat sellers, solution architects and partners who get asked "what are the use cases for Ansible in X?". A use case must be readable in one minute and usable as the outline of a delivery plan or statement of work.

## The format (do not change it)

Every use case file has YAML front matter and exactly these five `##` sections, in this order:

1. `## Description`: one short paragraph, the customer's goal in plain words.
2. `## Prerequisites`: numbered list of what must exist first (access, credentials, systems, inventory source).
3. `## Steps`: numbered list of delivery tasks, in order, each starting with a verb. Mention the key module or role inline in backticks where it does the work.
4. `## Success Criteria`: numbered list of observable outcomes everyone can agree on.
5. `## Notes`: bullets for variations, pitfalls, related use cases (link sibling files with relative links), and when to pair with Event-Driven Ansible.

Front matter:

```yaml
---
title: Patch RHEL servers at scale        # outcome as a short verb phrase
summary: One sentence shown in the domain list.
order: 10                                  # 10, 20, 30... position in the list
personas: [Linux administrator, Operations lead]
collections: [redhat.satellite, redhat.rhel_system_roles]   # every collection used below
key_content:                               # 2-8 most important modules/roles/playbooks, by FQCN
  - redhat.satellite.content_view_version
  - redhat.rhel_system_roles.timesync
examples:                                  # optional, only real URLs you have verified exist
  - title: ...
    url: https://github.com/...
---
```

The site renders a **Collections & key content** table from `collections` and `key_content` automatically. Do not write that table yourself.

## Rules

- **Only reference content that exists.** Every FQCN in `collections` and `key_content` must exist in `data/collections.yml` / `data/content.json`. Find content with:
  - `python3 scripts/digest.py --domain <domain-id>` (collections mapped to a domain, with every module and role)
  - `python3 scripts/digest.py <fqcn> <fqcn>` (specific collections)
  - `python3 scripts/digest.py --grep <word>` (search all modules, roles and plugins)
- Every collection of a `key_content` entry must also be listed in `collections`.
- Prefer **Certified** and **Validated** content. Validated collections (roles and playbooks such as `network.backup`, `infra.leapp`, `cloud.aws_ops`) are the best fit for outcome-level use cases; certified modules are the building blocks.
- Never invent module names, options, product features, version numbers or URLs. If unsure, leave it out.
- Product names: Ansible Automation Platform (AAP) 2.5+; "automation controller", "Event-Driven Ansible controller", "platform gateway", "automation hub", "execution environment". Do not use "Ansible Tower" except when describing migration from it.
- English, concise, no marketing language. No first person. Keep each section short: Steps usually 4-8 items.
- File names: lowercase-hyphenated outcome, e.g. `patch-rhel-at-scale.md`.
- Only link to sibling use cases that you are also creating, or that already exist.

## Check your work

```bash
python3 scripts/validate_use_cases.py docs/use-cases/<your-domain-folder>
```

It must report `0 problems`. Fix every problem it lists before finishing.
