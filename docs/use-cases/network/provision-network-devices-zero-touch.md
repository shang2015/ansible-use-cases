---
title: Provision network devices with zero-touch onboarding
summary: Bring new switches and routers into service from factory state using DHCP/ZTP or controller onboarding workflows.
order: 110
personas: [Network engineer, Network architect, Deployment engineer]
collections: [cisco.catalystcenter, juniper.apstra, arista.cvp, arista.avd, network.base, netbox.netbox]
key_content:
  - cisco.catalystcenter.pnp_workflow_manager
  - cisco.catalystcenter.provision_workflow_manager
  - cisco.catalystcenter.template_workflow_manager
  - juniper.apstra.ztp_config
  - juniper.apstra.ztp_device
  - arista.cvp.dhcp_configuration
  - arista.avd.cv_deploy
  - network.base.deploy
---

# Provision network devices with zero-touch onboarding

## Description

Ship a device to a site, power it on and have it receive its software and configuration without an engineer on site. Automation prepares the records and templates that the onboarding service needs, then verifies that the device registered and is configured.

## Prerequisites

1. An onboarding mechanism: a controller (Catalyst Center, Apstra, CloudVision) or a DHCP/TFTP/HTTP service for ZTP.
2. Device serial numbers and roles, from procurement or a source of truth such as NetBox.
3. Configuration templates and data per site and per role.
4. Network connectivity from the new device to the DHCP and image servers.

## Steps

1. Read the planned devices (serial number, model, site, role) from the source of truth or an input file, for example with `netbox.netbox.nb_inventory`.
2. Prepare the onboarding service. For Arista, `arista.cvp.dhcp_configuration` configures DHCP as a ZTP server. For Juniper Apstra, `juniper.apstra.ztp_config` sets the ZTP server and `juniper.apstra.ztp_device` registers devices.
3. Register the devices with the controller: `cisco.catalystcenter.pnp_workflow_manager` adds and claims devices, and `cisco.catalystcenter.template_workflow_manager` and `cisco.catalystcenter.provision_workflow_manager` assign templates and provision them. For Arista designs, deploy the generated configuration with `arista.avd.cv_deploy`.
4. After the device appears, apply final configuration with the `network.base.deploy` role or the controller workflow.
5. Run health checks and add a backup (see [Back up device configuration](backup-device-configuration.md)).
6. Update the source of truth with the device status.

## Success Criteria

1. A device powered on with only a management uplink reaches the planned software version and role configuration.
2. No manual CLI configuration is needed on the device.
3. The device appears in inventory, monitoring and the backup schedule.
4. A failed onboarding is visible in the job and leaves the device in a recoverable state.

## Notes

- Keep device credentials and image repositories in the platform credentials and controller, not in templates.
- Related: [Upgrade network OS and firmware](upgrade-network-os.md) and [Manage scoped configuration with a source of truth](manage-scoped-configuration-with-source-of-truth.md).
- Pair with Event-Driven Ansible: a controller or DHCP event for a new device can start the onboarding workflow.
