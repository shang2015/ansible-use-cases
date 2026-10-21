---
title: Remediate Zabbix problems
summary: Send Zabbix problems to Event-Driven Ansible, run the fix and keep Zabbix hosts in step with the inventory.
order: 70
personas: [Operations lead, Linux administrator, Monitoring engineer]
collections: [zabbix.zabbix, ansible.eda, ansible.controller]
key_content:
  - zabbix.zabbix.zabbix_event
  - zabbix.zabbix.zabbix_host
  - zabbix.zabbix.zabbix_inventory
  - zabbix.zabbix.agent
  - ansible.eda.webhook
  - ansible.controller.job_template
---

# Remediate Zabbix problems

## Description

Zabbix triggers raise problems for hosts and services. A webhook from Zabbix delivers them to Event-Driven Ansible, which starts the remediation job for known problems. The same collection deploys agents and registers hosts so that monitoring follows the automation inventory.

## Notes

- The collection ships remediation examples (`zabbix.zabbix.example_oci_volume_extend`) that show the intended wiring.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) and [Roll out monitoring agents at scale](roll-out-monitoring-agents-at-scale.md).
