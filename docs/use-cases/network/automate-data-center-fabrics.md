---
title: Automate data center fabrics
summary: Define tenants, VRFs and networks once and deploy them through ACI, NDFC, Apstra or Arista AVD.
order: 140
personas: [Network architect, Data center engineer, NetDevOps engineer]
collections: [cisco.aci, cisco.dcnm, juniper.apstra, arista.avd, arista.cvp]
key_content:
  - cisco.aci.aci_tenant
  - cisco.aci.aci_vrf
  - cisco.dcnm.dcnm_vrf
  - cisco.dcnm.dcnm_network
  - juniper.apstra.blueprint
  - juniper.apstra.virtual_network
  - arista.avd.eos_designs
  - arista.avd.cv_deploy
---

# Automate data center fabrics

## Description

Manage a data center fabric through its controller or design model, not box by box. Teams describe tenants, VRFs, networks and policies as data, review the change, and automation pushes it to the fabric in a repeatable way.

## Notes

- Multi-site ACI uses `cisco.mso` and Nexus Dashboard modules (`cisco.nd`), which have their own object models.
- Campus fabrics follow the same pattern with Catalyst Center (`cisco.catalystcenter`) and Meraki (`cisco.meraki`) collections.
- Related: [Detect configuration drift](detect-configuration-drift.md) and [Upgrade network OS and firmware](upgrade-network-os.md).
