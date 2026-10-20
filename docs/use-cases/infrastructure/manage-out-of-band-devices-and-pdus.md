---
title: Manage out-of-band devices and PDUs
summary: Configure, back up, monitor and control console servers and remote power distribution units, including power-cycling outlets for hung equipment.
order: 60
personas: [Data center operations, Network engineer, Infrastructure engineer]
collections: [wti.remote]
key_content:
  - wti.remote.cpm_config_backup
  - wti.remote.cpm_config_restore
  - wti.remote.cpm_firmware_update
  - wti.remote.cpm_plugcontrol
  - wti.remote.cpm_status_info
  - wti.remote.cpm_alarm_info
examples:
  - title: WTI collection
    url: https://github.com/wtinetworkgear/wti-collection
---

# Manage out-of-band devices and PDUs

## Description

Keep the access path that works when everything else is down: console servers and remote power switches. Automation applies a common configuration to every unit, monitors alarms, power and temperature, backs up settings, updates firmware, and lets other workflows power-cycle an outlet to recover a hung device.

## Prerequisites

1. WTI out-of-band (console) and PDU devices reachable on the management network, with administrative credentials stored in Automation Platform.
2. An inventory of devices with site, rack, and the mapping of outlets and serial ports to the connected equipment.
3. A baseline per site: hostname convention, time source, DNS, SNMP and syslog targets, SSH and web settings, and users.
4. Approved firmware images for the device models.

## Steps

1. Collect the current state with `wti.remote.cpm_status_info`, `cpm_hostname_info` and `cpm_firmware_info`, and store the results as a baseline.
2. Back up each device configuration with `wti.remote.cpm_config_backup` before any change.
3. Apply the baseline: `cpm_hostname_config`, `cpm_time_config`, `cpm_dnsservices_config`, `cpm_interface_config`, `cpm_snmp_config`, `cpm_syslog_client_config`, `cpm_ssh_config`, `cpm_web_config` and `cpm_user`.
4. Configure serial ports for the connected equipment with `wti.remote.cpm_serial_port_config`, and name the outlets with `wti.remote.cpm_plugconfig`.
5. Update firmware with `wti.remote.cpm_firmware_update` in batches, checking the version afterwards with `cpm_firmware_info`.
6. Monitor on a schedule with `cpm_alarm_info`, `cpm_current_info`, `cpm_power_info` and `cpm_temp_info`, and report devices outside their limits.
7. Offer a controlled power-cycle job built on `wti.remote.cpm_plugcontrol`, with an approval step, to be used by operations or called from other workflows.
8. Restore a saved configuration to a replacement unit with `wti.remote.cpm_config_restore`.

## Success Criteria

1. All devices report the baseline for time, DNS, SNMP, syslog and access settings.
2. A current configuration backup exists for each device.
3. Alarm, power and temperature data is collected on schedule and exceptions are reported.
4. A hung server can be power-cycled from a job template by an authorised user, and the action is logged.

## Notes

- Use the out-of-band network for these jobs, so automation still reaches the devices during an outage.
- Server BMCs (iDRAC, iLO) are covered in [Provision bare-metal servers](provision-bare-metal-servers.md) and [Update server firmware and BIOS](update-server-firmware-and-bios.md).
- Event-Driven Ansible can trigger the power-cycle job after a monitoring alert shows a host unresponsive, with a guard that requires approval for production systems.
