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

## Notes

- Always check the vendor compatibility guidance for the combination of firmware, operating system drivers and hypervisor before approving a baseline.
- Storage controllers and NICs often need a reboot; plan the order with the host maintenance step.
- Use the same pattern for storage systems in [Standardise storage system configuration](../storage/standardise-storage-system-configuration.md), and for IBM Power systems in [Manage IBM Power systems with the HMC](manage-ibm-power-systems-with-hmc.md).
- Event-Driven Ansible can start an inventory-and-compare job when a controller reports a new alert or a vendor advisory is published.
