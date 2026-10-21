---
title: Build self-healing infrastructure from monitoring alerts
summary: Turn a monitoring alert into an automatic, controlled fix by letting Event-Driven Ansible launch a job template or workflow.
order: 10
personas: [Operations lead, SRE, Automation engineer]
collections: [ansible.eda, ansible.controller]
key_content:
  - ansible.eda.alertmanager
  - ansible.eda.webhook
  - ansible.eda.insert_hosts_to_meta
  - ansible.eda.decision_environment
  - ansible.eda.project
  - ansible.eda.rulebook_activation
  - ansible.controller.job_template
---

# Build self-healing infrastructure from monitoring alerts

## Description

When monitoring raises a known alert, such as a stopped service, a full file system or an unresponsive node, Event-Driven Ansible receives the event, checks it against rules and starts the matching job template or workflow in Automation Platform. The common failures are fixed in seconds, without a person being paged first, and everything is logged.

## Notes

- Use a separate rulebook activation per source, and keep rules narrow. Start in "notify only" mode, then switch the action to remediation.
- Vendor-specific versions of this pattern: [Remediate Dynatrace problems](remediate-dynatrace-problems.md), [Remediate Splunk ITSI episodes](remediate-splunk-itsi-episodes.md), [Remediate Microsoft SCOM alerts](remediate-microsoft-scom-alerts.md), [Remediate IBM Instana events](remediate-ibm-instana-events.md), [Act on LogicMonitor Edwin AI alerts](act-on-logicmonitor-edwin-ai-alerts.md), [Remediate Zabbix problems](remediate-zabbix-problems.md) and [Update BigPanda incidents from automation](update-bigpanda-incidents-from-automation.md).
- Tie each automatic fix to a ticket using [Create and update ServiceNow incidents from automation](../itsm/create-and-update-servicenow-incidents.md).
- Network alerts: Kentik and Juniper provide event sources in the network domain.
