---
title: Manage Active Directory
summary: Build domains and domain controllers, manage OUs, users, groups and GPO links, and join servers to the domain as code.
order: 30
personas: [Windows administrator, Identity engineer]
collections: [microsoft.ad]
key_content:
  - microsoft.ad.domain
  - microsoft.ad.domain_controller
  - microsoft.ad.membership
  - microsoft.ad.ou
  - microsoft.ad.user
  - microsoft.ad.group
  - microsoft.ad.computer
  - microsoft.ad.gpo_link
examples:
  - title: microsoft.ad collection
    url: https://github.com/ansible-collections/microsoft.ad
    note: certified collection for Active Directory management
---

# Manage Active Directory

## Description

Treat the directory as code. New forests, domain controllers, organizational units, accounts and group memberships are created from definitions in Git, and servers join the domain as part of their build, so joiner, mover and leaver changes run the same way each time.

## Notes

- Domain trusts (`microsoft.ad.domain_trust`), AD Certificate Services templates (`microsoft.ad.cs_template`) and AD FS trusts are available in the same collection for larger directory projects.
- Joining Linux hosts to the same domain is covered in [Manage users, sudo and SSH](../linux/manage-users-sudo-and-ssh.md).
- Test domain-controller changes in a lab forest, and keep a system-state backup before schema or topology changes.
- Pair with [Harden Windows](harden-windows.md) to apply domain-level security baselines.
