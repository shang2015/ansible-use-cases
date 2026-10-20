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

## Prerequisites

1. An inventory of candidate hosts with source distribution and version, and a conversion order agreed with application owners.
2. RHEL subscriptions, an activation key, or a Satellite with the conversion content. The source distributions and versions are listed in the Convert2RHEL documentation.
3. SSH access with privilege escalation, and a backup or snapshot for every host.
4. Outbound access from hosts to the Convert2RHEL repository and the RHEL content source (Red Hat CDN or Satellite).

## Steps

1. Group the inventory by source distribution and version. Pilot with non-production hosts.
2. If hosts will use Satellite, prepare the content with the `redhat.satellite.convert2rhel` role: manifest, RHEL repositories, Convert2RHEL products and repositories, activation keys and host groups.
3. Run `infra.convert2rhel.analysis` on all hosts. It creates the pre-conversion report and sets a `conversion_inhibited` fact instead of failing, and `infra.convert2rhel.handle_c2r_report` parses the result.
4. Review the inhibitors, fix them (packages, repository configuration, kernel and driver issues) and repeat the analysis until `conversion_inhibited` is false for the batch. Fail the workflow on any host that is still inhibited.
5. Take a snapshot or backup. For hosts on LVM, `infra.lvm_snapshots.snapshot_create` can create snapshots before the change.
6. Run `infra.convert2rhel.convert` on one batch at a time, passing RHSM credentials or the activation key as automation controller credentials. Set `convert_reboot_requested` if the role should reboot the host.
7. Register converted hosts to the Satellite content views of the production environment, apply the standard configuration and update packages.
8. Remove snapshots after the application owners sign off.

## Success Criteria

1. Every converted host reports a RHEL release and is subscribed with a valid entitlement.
2. No host was converted while its analysis reported an inhibitor.
3. Application owners confirm service after the conversion for each batch.
4. The Convert2RHEL package and repository files are removed from converted hosts, as the convert role does by default.

## Notes

- The collection `infra.convert2rhel` also ships ready-made playbooks `infra.convert2rhel.analysis` and `infra.convert2rhel.convert` that can be used as job template playbooks.
- Plan a follow-up [Upgrade RHEL in place with snapshot rollback](upgrade-rhel-in-place.md) if the converted release is not the target release.
- Apply [Patch RHEL at scale](patch-rhel-at-scale.md) and [Standardise RHEL configuration](standardise-rhel-configuration.md) after conversion so the hosts join the managed estate.
- Third-party agents and kernel modules from the old distribution often cause inhibitors. Identify them from the first analysis run.
