---
title: Convert CentOS and Oracle Linux to RHEL
summary: Analyse and convert CentOS and Oracle Linux hosts to Red Hat Enterprise Linux in place with convert2rhel.
order: 90
personas: [Linux administrator, Migration lead]
collections: [infra.convert2rhel, redhat.satellite, infra.lvm_snapshots]
key_content:
  - infra.convert2rhel.analysis
  - infra.convert2rhel.handle_c2r_report
  - infra.convert2rhel.convert
  - redhat.satellite.convert2rhel
  - infra.lvm_snapshots.snapshot_create
examples:
  - title: infra.convert2rhel validated collection
    url: https://github.com/redhat-cop/infra.convert2rhel
    note: analysis and conversion roles with example playbooks
---

# Convert CentOS and Oracle Linux to RHEL

## Description

Move CentOS and Oracle Linux systems to supported RHEL without reinstalling them. The Convert2RHEL tool changes the operating system packages in place; Ansible runs a pre-conversion analysis on every host, fixes what blocks the conversion and then converts the hosts in controlled batches.

## Notes

- The collection `infra.convert2rhel` also ships ready-made playbooks `infra.convert2rhel.analysis` and `infra.convert2rhel.convert` that can be used as job template playbooks.
- Plan a follow-up [Upgrade RHEL in place with snapshot rollback](upgrade-rhel-in-place.md) if the converted release is not the target release.
- Apply [Patch RHEL at scale](patch-rhel-at-scale.md) and [Standardise RHEL configuration](standardise-rhel-configuration.md) after conversion so the hosts join the managed estate.
- Third-party agents and kernel modules from the old distribution often cause inhibitors. Identify them from the first analysis run.
