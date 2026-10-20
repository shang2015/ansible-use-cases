---
title: Manage scoped configuration with a source of truth
summary: Define VLANs, interfaces, routing and ACLs as data in Git or NetBox/Nautobot and apply only the resources in scope.
order: 90
personas: [Network engineer, Network architect, NetDevOps engineer]
collections: [network.base, network.interfaces, network.bgp, network.ospf, network.acls, netbox.netbox, networktocode.nautobot, ansible.netcommon, cisco.ios]
key_content:
  - network.base.persist
  - network.base.deploy
  - network.interfaces.deploy
  - network.acls.deploy
  - netbox.netbox.nb_inventory
  - networktocode.nautobot.inventory
  - ansible.netcommon.network_resource
  - cisco.ios.ios_vlans
examples:
  - title: network.base validated collection
    url: https://github.com/redhat-cop/network.base
    note: gather, persist, detect, remediate and deploy roles
---

# Manage scoped configuration with a source of truth

## Description

Describe the intended configuration of selected resources (interfaces, VLANs, BGP, OSPF, ACLs) as structured data and let automation apply it. Changes are scoped to the resources named in the change, so a VLAN update does not touch routing, and every change starts as a reviewable data change.

## Prerequisites

1. A source of truth for intended state: a Git repository of host variables, NetBox or Nautobot.
2. Write access to the devices and an approved change process.
3. Platform collections that provide resource modules for the devices in scope.
4. A baseline of the current state, so the first run produces no surprise changes.

## Steps

1. Build the baseline from the live network with `network.base.gather` and `network.base.persist`, which write resource facts as `host_vars`.
2. Load inventory and device data from the source of truth with `netbox.netbox.nb_inventory` or `networktocode.nautobot.inventory`.
3. Change the data in a branch or in the source of truth, and review it.
4. Run the `network.base.deploy` role, or a scoped role such as `network.interfaces.deploy`, `network.bgp.deploy`, `network.ospf.deploy` or `network.acls.deploy`, with the list of resources in scope. For single resources, call the vendor resource module (for example `cisco.ios.ios_vlans`) or `ansible.netcommon.network_resource`.
5. Run in check mode first and show the proposed change in the job output or a pull request.
6. After approval, apply the change in a workflow that backs up the device first and validates it afterwards.

## Success Criteria

1. Each change is traceable to a commit or a source of truth record.
2. Only the resources in scope change on the devices, and unchanged devices report no change.
3. A second run reports no change (idempotent).
4. A drift check after the run finds no difference to the data.

## Notes

- Resource modules use `state` values such as `merged`, `replaced`, `overridden` and `deleted`. Agree on which are allowed, because `overridden` removes anything not in the data.
- Related: [Detect configuration drift](detect-configuration-drift.md) and [Manage DNS, DHCP and IPAM](manage-dns-dhcp-and-ipam.md).
- Pair with Event-Driven Ansible to start a deploy when a record in the source of truth changes.
