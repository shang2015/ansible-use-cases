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

## Prerequisites

1. Approved target version per platform and model, and the image files in a repository the devices or the controller can reach.
2. Write access to the devices and a maintenance window.
3. A way to reach the device if it does not come back (console or out-of-band).
4. A pre-change and post-change checklist agreed with the service owners.

## Steps

1. Group devices into waves, for example redundant pairs separately, and pass the wave as a survey variable.
2. Run pre-checks: `network.backup.backup` for the configuration, `network.healthchecks.filesystem` for free space, plus `network.healthchecks.bgp` and `network.healthchecks.interfaces` to record the baseline.
3. Copy the image to the device with `ansible.netcommon.net_put` or the vendor module, for example `arubanetworks.aoscx.aoscx_upload_firmware`.
4. Install and activate the image with the vendor module: `cisco.nxos.nxos_install_os`, `juniper.device.software` or `dellemc.enterprise_sonic.sonic_image_management`. Controller-managed devices use the controller workflow, for example `cisco.catalystcenter.swim_workflow_manager`.
5. Wait for the device to return, then re-run the health checks and compare with the baseline (see [Validate operational state and health checks](validate-operational-state-and-health-checks.md)).
6. Stop the workflow on the first failed device in a wave, and report the result per device.

## Success Criteria

1. Every device in scope reports the target version.
2. Routing adjacencies, interfaces and key services match the pre-change baseline.
3. A configuration backup taken before the change exists for every device.
4. Failed devices are listed with the failing step, and later waves did not start.

## Notes

- Use a workflow job template with an approval node between waves.
- Other options: `arista.cvp.cv_image_v3` for EOS images managed by CloudVision, `cisco.dcnm.dcnm_image_upgrade` for Nexus switches managed by NDFC, `juniper.apstra.os_upgrade` for Apstra blueprints and `f5networks.f5_bigip.bigip_software_install` for BIG-IP.
- Use [Restore configuration](restore-configuration.md) if the new release needs a configuration rollback.
