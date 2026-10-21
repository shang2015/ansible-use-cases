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

## Notes

- Resource modules use `state` values such as `merged`, `replaced`, `overridden` and `deleted`. Agree on which are allowed, because `overridden` removes anything not in the data.
- Related: [Detect configuration drift](detect-configuration-drift.md) and [Manage DNS, DHCP and IPAM](manage-dns-dhcp-and-ipam.md).
- Pair with Event-Driven Ansible to start a deploy when a record in the source of truth changes.
