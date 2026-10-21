---
title: Respond to Windows alerts from SCOM
summary: Turn System Center Operations Manager alerts into automated remediation, and manage maintenance schedules and SCOM configuration as code.
order: 80
personas: [Windows administrator, Monitoring engineer, Operations lead]
collections: [microsoft.scom]
key_content:
  - microsoft.scom.scom_plugin
  - microsoft.scom.alert
  - microsoft.scom.alert_info
  - microsoft.scom.maintenance_schedule
  - microsoft.scom.monitor_override
  - microsoft.scom.notification_channel
  - microsoft.scom.management_pack
  - microsoft.scom.group
---

# Respond to Windows alerts from SCOM

## Description

Connect System Center Operations Manager (SCOM) to Event-Driven Ansible so that a critical alert starts a fix immediately instead of waiting for an operator. The same collection manages SCOM itself: maintenance windows during patching, monitor overrides, notification channels and management packs.

## Notes

- Start with a few alert types that have a safe, well-understood fix, and add a human approval for risky actions.
- Add rate limits or throttling in the rulebook so one flapping monitor does not start a flood of jobs.
- Combine with [Patch Windows servers](patch-windows-servers.md) and [Patch Windows with MECM](patch-windows-with-mecm.md) by creating the maintenance schedule at the start of the patch workflow.
- The same event-driven pattern applies to other monitoring sources; see the Event-Driven Ansible use cases.
