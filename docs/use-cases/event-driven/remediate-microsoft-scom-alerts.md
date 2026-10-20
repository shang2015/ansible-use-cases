---
title: Remediate Microsoft SCOM alerts
summary: Start Windows remediation from System Center Operations Manager alerts and manage SCOM maintenance windows from Ansible.
order: 40
personas: [Windows administrator, Operations lead]
collections: [microsoft.scom, ansible.eda, ansible.controller]
key_content:
  - microsoft.scom.scom_plugin
  - microsoft.scom.alert
  - microsoft.scom.alert_info
  - microsoft.scom.maintenance_schedule
  - ansible.eda.rulebook_activation
---

# Remediate Microsoft SCOM alerts

## Description

Organizations that monitor Windows servers and applications with System Center Operations Manager (SCOM) can react to alerts automatically. Event-Driven Ansible receives new SCOM alerts, runs the fix, and the playbook closes the alert and puts servers in maintenance while work is done.

## Prerequisites

1. A SCOM management group and an account that can read alerts and change their state.
2. Event-Driven Ansible controller with a decision environment that includes `microsoft.scom`.
3. A Windows execution environment and job templates for the fixes, with WinRM or SSH credentials in Automation Platform.
4. A list of SCOM alerts approved for automatic remediation, with the matching fix.

## Steps

1. Configure the `microsoft.scom.scom_plugin` event source in a rulebook with the SCOM connection details taken from a credential.
2. Write rules on alert name, severity, monitored object and path, and map the object to an inventory host.
3. Use `run_job_template` to start the fix, for example restart a Windows service or clear a disk, and pass the alert details as extra variables.
4. Put the server into a maintenance window with `microsoft.scom.maintenance_schedule` before disruptive work, so that the change does not raise further alerts.
5. Review the alert afterwards with `microsoft.scom.alert_info`, and close or update it with `microsoft.scom.alert`.
6. Use other modules of the collection, such as `microsoft.scom.monitor_override` or `microsoft.scom.notification_subscription`, to tune SCOM as code.

## Success Criteria

1. An approved alert starts one remediation job for the correct Windows host.
2. The alert is closed from the playbook once the fix is verified.
3. Planned work is covered by maintenance schedules and creates no noise.

## Notes

- Pair with the Windows use cases for patching and service configuration, which provide the fixes.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for the general design and guard rails.
