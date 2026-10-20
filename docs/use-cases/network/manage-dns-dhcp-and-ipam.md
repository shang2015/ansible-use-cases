---
title: Manage DNS, DHCP and IPAM
summary: Allocate addresses and create DNS and DHCP records in Infoblox or NetBox as part of every provisioning request.
order: 120
personas: [Network engineer, DDI administrator, Cloud engineer]
collections: [infoblox.nios_modules, infoblox.universal_ddi, netbox.netbox, networktocode.nautobot]
key_content:
  - infoblox.nios_modules.nios_next_ip
  - infoblox.nios_modules.nios_host_record
  - infoblox.nios_modules.nios_network
  - infoblox.universal_ddi.ipam_subnet
  - infoblox.universal_ddi.dns_record
  - infoblox.universal_ddi.dhcp_fixed_address
  - netbox.netbox.netbox_prefix
  - netbox.netbox.netbox_ip_address
---

# Manage DNS, DHCP and IPAM

## Description

Take the manual tickets out of address management. Automation reserves the next free address, creates the DNS record and DHCP reservation and records the result in the IPAM, so servers, devices and applications get consistent names and addresses the moment they are requested.

## Prerequisites

1. An IPAM or DDI platform: Infoblox NIOS, Infoblox Universal DDI, NetBox or Nautobot, with an API account that has the needed permissions.
2. Network containers, views, zones and naming rules defined in the platform.
3. Credentials stored in Automation Platform and reachable from the execution environment.

## Steps

1. Look up free space: `infoblox.nios_modules.nios_next_ip` returns the next available address in a network, and `netbox.netbox.netbox_prefix` and `netbox.netbox.netbox_ip_address` manage prefixes and addresses in NetBox.
2. Create or update networks or subnets with `infoblox.nios_modules.nios_network` or `infoblox.universal_ddi.ipam_subnet`.
3. Create the DNS records with `infoblox.nios_modules.nios_host_record` or `infoblox.universal_ddi.dns_record`.
4. Create DHCP reservations with `infoblox.universal_ddi.dhcp_fixed_address` where hosts use DHCP.
5. Return the address and name to the caller, for example a provisioning workflow or the requesting ticket.
6. For decommissioning, run the same job with `state: absent` to release addresses and delete records.

## Success Criteria

1. A request returns a unique address and a resolving name without manual steps.
2. Running the job again for the same host does not create duplicates.
3. DNS, DHCP and IPAM show the same data.
4. Released addresses return to the pool and their records are removed.

## Notes

- Expose the job as a survey or service catalog item so other automation can call it, for example during [Provision network devices with zero-touch onboarding](provision-network-devices-zero-touch.md).
- Both Infoblox collections can also act as inventory sources, for example `infoblox.nios_modules.nios_inventory`.
- Related: [Manage scoped configuration with a source of truth](manage-scoped-configuration-with-source-of-truth.md).
