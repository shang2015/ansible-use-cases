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

## Notes

- Expose the job as a survey or service catalog item so other automation can call it, for example during [Provision network devices with zero-touch onboarding](provision-network-devices-zero-touch.md).
- Both Infoblox collections can also act as inventory sources, for example `infoblox.nios_modules.nios_inventory`.
- Related: [Manage scoped configuration with a source of truth](manage-scoped-configuration-with-source-of-truth.md).
