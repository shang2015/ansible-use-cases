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

## Notes

- Keep device credentials and image repositories in the platform credentials and controller, not in templates.
- Related: [Upgrade network OS and firmware](upgrade-network-os.md) and [Manage scoped configuration with a source of truth](manage-scoped-configuration-with-source-of-truth.md).
- Pair with Event-Driven Ansible: a controller or DHCP event for a new device can start the onboarding workflow.
