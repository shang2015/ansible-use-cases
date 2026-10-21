---
title: Provision bare-metal servers
summary: "Prepare new servers from template: BIOS, boot, RAID, firmware, profile and operating system installation through their management controllers."
order: 20
personas: [Infrastructure engineer, Data center operations, Platform engineer]
collections: [dellemc.openmanage, hpe.ilo, hpe.oneview, cisco.intersight, cisco.cvd_compute]
key_content:
  - dellemc.openmanage.idrac_server_config_profile
  - dellemc.openmanage.idrac_storage_volume
  - dellemc.openmanage.idrac_boot
  - dellemc.openmanage.idrac_os_deployment
  - hpe.ilo.ilo_storage
  - hpe.oneview.oneview_server_profile_template
  - cisco.intersight.intersight_server_profile_template
  - cisco.cvd_compute.deploy_ucs_server_profile
---

# Provision bare-metal servers

## Description

Take a rack-mounted or blade server from racked and cabled to ready for an operating system. A template defines the BIOS, boot order, storage layout, firmware and network identity. The automation applies it to each new server, installs the operating system and hands the host over to configuration management.

## Notes

- Keep hardware profiles in Git and compare them to live settings regularly to detect drift.
- Apply the firmware baseline before the operating system install; see [Update server firmware and BIOS](update-server-firmware-and-bios.md).
- Servers from other vendors are supported by their own certified collections, such as `inspur.ispim` for Inspur BMCs.
- For remote power control of servers without a BMC, see [Manage out-of-band devices and PDUs](manage-out-of-band-devices-and-pdus.md).
- Event-Driven Ansible can launch this job when a new server is added to the CMDB or discovered by the management platform.
