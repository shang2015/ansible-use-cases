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

## Prerequisites

1. A Zabbix server with an API account and permission to configure media types and actions.
2. Event-Driven Ansible controller with the `ansible.eda.webhook` source or an event stream available to Zabbix.
3. Job templates for the fixes, and host names in Zabbix that match the inventory.

## Steps

1. Create a webhook media type and an action in Zabbix that posts problem and recovery events to the Event-Driven Ansible endpoint.
2. Write a rulebook with the `ansible.eda.webhook` source and rules on trigger name, severity and host group, then use `run_job_template` for approved problems.
3. In the job, act on the Zabbix event with `zabbix.zabbix.zabbix_event` where the use case needs it, for example to record the action taken.
4. Use `zabbix.zabbix.zabbix_inventory` to build an inventory from Zabbix hosts, or `zabbix.zabbix.zabbix_host` to create and update hosts from the automation inventory.
5. Install and maintain agents with the `zabbix.zabbix.agent` role.
6. Run a test problem, confirm recovery is reported, and enable the activation.

## Success Criteria

1. A Zabbix problem of an approved type starts one job for the right host.
2. Recovery is visible in Zabbix after the job.
3. Hosts in Zabbix match the hosts in the automation inventory.

## Notes

- The collection ships remediation examples (`zabbix.zabbix.example_oci_volume_extend`) that show the intended wiring.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) and [Roll out monitoring agents at scale](roll-out-monitoring-agents-at-scale.md).
