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

## Notes

- Pair with the Windows use cases for patching and service configuration, which provide the fixes.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for the general design and guard rails.
