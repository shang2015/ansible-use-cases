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

## Prerequisites

1. A SCOM management group, and a Windows management server host reachable over WinRM with the SCOM PowerShell module installed.
2. A SCOM account that can read and update alerts, stored as an automation controller credential.
3. Event-Driven Ansible controller with a decision environment that contains the `microsoft.scom` collection (the collection ships a `Containerfile` for this) and Python 3.12 or later.
4. Remediation playbooks (service restart, disk clean-up, log collection) available as job templates and tested.

## Steps

1. Build the decision environment with the SCOM event source and register it in the Event-Driven Ansible controller.
2. Write a rulebook that uses the `microsoft.scom.scom_plugin` event source, filtered by severity or by an alert criteria expression, and that matches alert names to actions.
3. Create the rulebook activation. For each alert type, have the rule run a job template that restarts the service or runs the targeted fix on the alert source.
4. Close the loop in the job: set the resolution state with `microsoft.scom.alert`, and read alert context with `microsoft.scom.alert_info`.
5. Put monitored servers into maintenance for patching with `microsoft.scom.maintenance_schedule`, and tune noisy monitors with `microsoft.scom.monitor_override`.
6. Manage notification channels, subscribers and subscriptions as code with `microsoft.scom.notification_channel` and the related notification modules, and import management packs with `microsoft.scom.management_pack`.
7. Keep SCOM groups aligned with the Ansible inventory using `microsoft.scom.group`.

## Success Criteria

1. A new alert of a covered type triggers a job within the polling interval, without operator action.
2. The alert shows as resolved in SCOM after a successful fix, and stays open with the job output linked when the fix fails.
3. Servers in a patch window do not generate alerts caused by the patching.
4. SCOM notification and override configuration matches the definitions in Git.

## Notes

- Start with a few alert types that have a safe, well-understood fix, and add a human approval for risky actions.
- Add rate limits or throttling in the rulebook so one flapping monitor does not start a flood of jobs.
- Combine with [Patch Windows servers](patch-windows-servers.md) and [Patch Windows with MECM](patch-windows-with-mecm.md) by creating the maintenance schedule at the start of the patch workflow.
- The same event-driven pattern applies to other monitoring sources; see the Event-Driven Ansible use cases.
