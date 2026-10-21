---
title: Upgrade network OS and firmware
summary: Stage, install and verify software images on switches, routers and controllers in controlled waves.
order: 60
personas: [Network engineer, NetOps lead]
collections: [ansible.netcommon, network.backup, network.healthchecks, cisco.nxos, juniper.device, dellemc.enterprise_sonic, arubanetworks.aoscx, cisco.catalystcenter]
key_content:
  - network.backup.backup
  - network.healthchecks.filesystem
  - ansible.netcommon.net_put
  - cisco.nxos.nxos_install_os
  - juniper.device.software
  - dellemc.enterprise_sonic.sonic_image_management
  - arubanetworks.aoscx.aoscx_upload_firmware
  - cisco.catalystcenter.swim_workflow_manager
---

# Upgrade network OS and firmware

## Description

Move a fleet of network devices to an approved software release without manual device-by-device work. Automation backs up the device, checks space, stages and installs the image, reboots when needed and proves that the device is healthy afterwards.

## Notes

- Use a workflow job template with an approval node between waves.
- Other options: `arista.cvp.cv_image_v3` for EOS images managed by CloudVision, `cisco.dcnm.dcnm_image_upgrade` for Nexus switches managed by NDFC, `juniper.apstra.os_upgrade` for Apstra blueprints and `f5networks.f5_bigip.bigip_software_install` for BIG-IP.
- Use [Restore configuration](restore-configuration.md) if the new release needs a configuration rollback.
