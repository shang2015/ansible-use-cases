---
title: Provision bare-metal servers
summary: "Prepare new servers from template: BIOS, boot, RAID, firmware, profile and operating system installation through their management controllers."
order: 20
personas: [Infrastructure engineer, Data center operations, Platform engineer]
collections: [dellemc.openmanage, hpe.ilo, hpe.oneview, cisco.intersight, cisco.cvd_compute]
key_content:
  - dellemc.openmanage.idrac_server_config_profile
  - dellemc.openmanage.idrac_storage_volume
  - dellemc.openmanage.idrac_boot
  - dellemc.openmanage.idrac_os_deployment
  - hpe.ilo.ilo_storage
  - hpe.oneview.oneview_server_profile_template
  - cisco.intersight.intersight_server_profile_template
  - cisco.cvd_compute.deploy_ucs_server_profile
---

# Provision bare-metal servers

## Description

Take a rack-mounted or blade server from racked and cabled to ready for an operating system. A template defines the BIOS, boot order, storage layout, firmware and network identity. The automation applies it to each new server, installs the operating system and hands the host over to configuration management.

## Prerequisites

1. Servers racked, cabled and reachable on the out-of-band management network, with initial controller credentials.
2. A hardware standard per role: BIOS profile, RAID layout, boot mode, firmware baseline, NIC and storage connectivity.
3. A boot source for the operating system, such as an ISO on a web server, PXE, or a Satellite provisioning setup.
4. An IP address plan and an inventory source (CMDB, NetBox) that lists new servers and their controller addresses.
5. Service accounts for the management controllers or management platforms in Automation Platform.

## Steps

1. Discover the new servers and register them in the inventory, for example from OpenManage Enterprise (`dellemc.openmanage.ome_discovery`), OneView (`hpe.oneview.oneview_server_hardware`) or Intersight.
2. Apply the hardware profile:
   - Dell iDRAC: `dellemc.openmanage.idrac_server_config_profile` (import a standard profile), or the finer-grained `idrac_bios`, `idrac_attributes` and `idrac_network_attributes`;
   - HPE iLO: `hpe.ilo.ilo_redfish_config`, with the `hpe.ilo.changbiosattr` role for BIOS attributes;
   - HPE OneView: `hpe.oneview.oneview_server_profile_template` and `oneview_server_profile`;
   - Cisco: `cisco.intersight.intersight_server_profile_template`, derived to servers with `intersight_server_profile_derive` and `intersight_server_profile`, or the `cisco.cvd_compute.deploy_ucs_server_profile` role for UCS Manager.
3. Create the RAID layout: `dellemc.openmanage.idrac_storage_volume` or `idrac_redfish_storage_controller`, `hpe.ilo.ilo_storage` (or the `create_logical_drives` role), or storage policies in Intersight and OneView profiles.
4. Set the boot mode and order: `dellemc.openmanage.idrac_boot`, `hpe.ilo.ilo_boot`, or a boot order policy in `cisco.intersight.intersight_boot_order_policy`.
5. Install the operating system:
   - mount an installer ISO with `dellemc.openmanage.idrac_virtual_media` and boot it with `dellemc.openmanage.idrac_os_deployment`;
   - or boot from the network, with a provisioning tool such as Satellite (see the Linux use cases) taking over.
6. Wait for the operating system to come up, add the host to the inventory and launch a follow-up job template for the standard OS configuration.
7. Record the serial number, firmware versions and controller address in the CMDB.

## Success Criteria

1. A new server goes from first power-on to a reachable operating system without manual console work.
2. BIOS, RAID, boot and firmware settings match the hardware standard for the server's role.
3. The server appears in the inventory and the CMDB with its hardware details.
4. Two servers of the same role show identical hardware configuration when compared.

## Notes

- Keep hardware profiles in Git and compare them to live settings regularly to detect drift.
- Apply the firmware baseline before the operating system install; see [Update server firmware and BIOS](update-server-firmware-and-bios.md).
- Servers from other vendors are supported by their own certified collections, such as `inspur.ispim` for Inspur BMCs.
- For remote power control of servers without a BMC, see [Manage out-of-band devices and PDUs](manage-out-of-band-devices-and-pdus.md).
- Event-Driven Ansible can launch this job when a new server is added to the CMDB or discovered by the management platform.
