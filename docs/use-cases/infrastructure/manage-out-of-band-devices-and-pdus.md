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

## Notes

- Use the out-of-band network for these jobs, so automation still reaches the devices during an outage.
- Server BMCs (iDRAC, iLO) are covered in [Provision bare-metal servers](provision-bare-metal-servers.md) and [Update server firmware and BIOS](update-server-firmware-and-bios.md).
- Event-Driven Ansible can trigger the power-cycle job after a monitoring alert shows a host unresponsive, with a guard that requires approval for production systems.
