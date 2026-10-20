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

## Prerequisites

1. Windows Server hosts for domain controllers, or an existing domain, with WinRM access from the execution environment.
2. An account with rights to create the objects (domain admin or a delegated account) stored as an automation controller credential.
3. A directory design: OU structure, naming conventions, group model and the GPOs that exist.
4. A source of truth for people and groups, for example an HR export or an ITSM request.

## Steps

1. For a new forest, create the domain on the first server with `microsoft.ad.domain`. Add further controllers with `microsoft.ad.domain_controller`.
2. Define sites, subnets and links for replication with `microsoft.ad.site`, `microsoft.ad.site_subnet` and `microsoft.ad.site_link`.
3. Create the OU tree with `microsoft.ad.ou`. Keep service accounts, servers and users in separate OUs.
4. Manage identities with `microsoft.ad.user` and `microsoft.ad.group`, and application accounts with `microsoft.ad.service_account`. Use `microsoft.ad.pso` for fine-grained password policy.
5. Link existing Group Policy Objects to OUs with `microsoft.ad.gpo_link`.
6. Join servers with `microsoft.ad.membership`, after pre-creating the computer object in the right OU with `microsoft.ad.computer`. Use `microsoft.ad.offline_join` to produce the blob for hosts that cannot reach a controller during the build.
7. Query the current state with `microsoft.ad.object_info`, or use the `microsoft.ad.ldap` inventory plugin to build inventories from directory data.
8. Run joiner, mover and leaver jobs from ITSM requests, with a survey for the details.

## Success Criteria

1. The OU, group and account structure in the directory matches the definitions in Git.
2. Newly built servers are joined to the domain in the intended OU on first boot.
3. Leavers are disabled within the agreed time, and the job record shows who requested it.
4. Domain controllers show healthy replication after changes to sites or links.

## Notes

- Domain trusts (`microsoft.ad.domain_trust`), AD Certificate Services templates (`microsoft.ad.cs_template`) and AD FS trusts are available in the same collection for larger directory projects.
- Joining Linux hosts to the same domain is covered in [Manage users, sudo and SSH](../linux/manage-users-sudo-and-ssh.md).
- Test domain-controller changes in a lab forest, and keep a system-state backup before schema or topology changes.
- Pair with [Harden Windows](harden-windows.md) to apply domain-level security baselines.
