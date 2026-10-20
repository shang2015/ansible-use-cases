---
title: Update server firmware and BIOS
summary: Baseline, stage and apply firmware and BIOS updates across Dell, HPE and Cisco servers through their management controllers.
order: 10
personas: [Infrastructure engineer, Data center operations, Operations lead]
collections: [dellemc.openmanage, hpe.ilo, hpe.oneview, cisco.intersight, cisco.cvd_compute]
key_content:
  - dellemc.openmanage.idrac_firmware
  - dellemc.openmanage.ome_firmware
  - dellemc.openmanage.idrac_bios
  - hpe.ilo.ilo_firmware
  - hpe.oneview.oneview_server_profile
  - cisco.intersight.intersight_firmware_policy
  - cisco.cvd_compute.upgrade_ucs_fi_firmware
examples:
  - title: dellemc.openmanage collection
    url: https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections
  - title: cisco.intersight collection
    url: https://github.com/CiscoDevNet/intersight-ansible
---

# Update server firmware and BIOS

## Description

Bring server firmware and BIOS settings to an approved baseline without visiting each system. Automation Platform queries the out-of-band controllers (iDRAC, iLO, OneView, Intersight), reports what is out of date, stages the update and applies it in controlled batches, so fleets stay patched and consistent.

## Prerequisites

1. Network access from the execution environment to the management controllers or management platforms (iDRAC, OpenManage Enterprise, iLO, OneView, Intersight, UCS Manager), with service accounts stored in Automation Platform.
2. An approved firmware baseline per server model: a catalog, repository or bundle, hosted on a share the controllers can reach.
3. A maintenance schedule agreed with application owners, and a way to take hosts out of service (hypervisor maintenance mode, cluster drain).
4. An inventory of servers grouped by vendor, model, site and application tier.

## Steps

1. Gather the current inventory: `dellemc.openmanage.idrac_firmware_info` and `idrac_system_info`, `hpe.ilo.ilo_redfish_info`, or the OneView and Intersight inventory modules. Compare to the baseline and report the differences.
2. Back up the current configuration before changes, for example `dellemc.openmanage.idrac_server_config_profile` for iDRAC.
3. Stage the baseline:
   - Dell: `dellemc.openmanage.ome_firmware_catalog` and `ome_firmware_baseline` on OpenManage Enterprise;
   - HPE OneView: upload bundles with `hpe.oneview.oneview_firmware_bundle` and `oneview_firmware_driver`;
   - Cisco: define a `cisco.intersight.intersight_firmware_policy`.
4. Take the first batch out of service, using hypervisor or Kubernetes maintenance steps from [Operate vSphere clusters and ESXi hosts](../virtualization/operate-vsphere-clusters-and-esxi-hosts.md) or [Run Kubernetes node maintenance](../kubernetes/run-kubernetes-node-maintenance.md).
5. Apply the updates:
   - Dell: `dellemc.openmanage.idrac_firmware` per server or `dellemc.openmanage.ome_firmware` for groups, and `redfish_firmware` for a single component;
   - HPE: `hpe.ilo.ilo_firmware`, or the `hpe.ilo.flashfwpkg` role, or a server profile with a firmware baseline in `hpe.oneview.oneview_server_profile`;
   - Cisco: assign the firmware policy to server profiles, and use `cisco.cvd_compute.upgrade_ucs_fi_firmware` for UCS fabric interconnects.
6. Apply BIOS settings from the standard with `dellemc.openmanage.idrac_bios`, `hpe.ilo.ilo_redfish_config` or `cisco.intersight.intersight_bios_policy`, and reboot when the job queue requires it.
7. Wait for the controller job to finish (for Dell, `idrac_lifecycle_controller_job_status_info`), then verify versions and health and return the host to service.
8. Continue with the next batch only if the previous batch passed. Report results by host.

## Success Criteria

1. The report shows every server at, or above, the approved baseline version, or lists exceptions with reasons.
2. BIOS settings match the standard for each server model.
3. Servers are updated in batches and a failed batch stops the rollout.
4. Each server has a before and after record of versions in the job output or CMDB.

## Notes

- Always check the vendor compatibility guidance for the combination of firmware, operating system drivers and hypervisor before approving a baseline.
- Storage controllers and NICs often need a reboot; plan the order with the host maintenance step.
- Use the same pattern for storage systems in [Standardise storage system configuration](../storage/standardise-storage-system-configuration.md), and for IBM Power systems in [Manage IBM Power systems with the HMC](manage-ibm-power-systems-with-hmc.md).
- Event-Driven Ansible can start an inventory-and-compare job when a controller reports a new alert or a vendor advisory is published.
