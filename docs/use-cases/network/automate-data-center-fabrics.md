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

## Prerequisites

1. A fabric platform: Cisco ACI (APIC) or Nexus Dashboard Fabric Controller, Juniper Apstra, or an Arista EOS fabric managed with AVD and optionally CloudVision.
2. Controller API credentials in Automation Platform.
3. A design or naming standard for tenants, VRFs, VLAN/VNI ranges and policies.
4. A Git repository for the fabric data.

## Steps

1. Model the fabric intent as YAML in Git: tenants, VRFs, networks and attachments.
2. For ACI, create the objects with `cisco.aci.aci_tenant`, `cisco.aci.aci_vrf` and related modules such as `cisco.aci.aci_bd` and `cisco.aci.aci_epg`.
3. For NDFC, create VRFs and networks with `cisco.dcnm.dcnm_vrf` and `cisco.dcnm.dcnm_network`.
4. For Apstra, work in a blueprint: `juniper.apstra.blueprint` and `juniper.apstra.virtual_network`.
5. For Arista, generate structured configuration with the `arista.avd.eos_designs` role and `arista.avd.eos_cli_config_gen`, then deploy to CloudVision with `arista.avd.cv_deploy`, or to devices over eAPI with `arista.avd.eos_config_deploy_eapi`.
6. Validate after deployment, for example with `arista.avd.anta_runner`, or with the controller's own health or compliance information.
7. Take a snapshot or backup before changes, for example `cisco.aci.aci_config_snapshot`.

## Success Criteria

1. Tenants, VRFs and networks in the fabric match the data in Git.
2. Changes are reviewed as pull requests and applied by a job, not by hand in the controller.
3. Re-running the job makes no changes if the data is unchanged.
4. A pre-change snapshot exists, and post-change validation passes.

## Notes

- Multi-site ACI uses `cisco.mso` and Nexus Dashboard modules (`cisco.nd`), which have their own object models.
- Campus fabrics follow the same pattern with Catalyst Center (`cisco.catalystcenter`) and Meraki (`cisco.meraki`) collections.
- Related: [Detect configuration drift](detect-configuration-drift.md) and [Upgrade network OS and firmware](upgrade-network-os.md).
