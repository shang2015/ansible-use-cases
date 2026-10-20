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

## Prerequisites

1. A monitoring tool that can send events by webhook or Prometheus Alertmanager format, or a vendor event source (see the vendor pages in Notes).
2. Event-Driven Ansible controller connected to automation controller, with a credential of the Red Hat Ansible Automation Platform type.
3. Tested job templates for each fix, which accept a target host as input and are safe to run twice.
4. A Git project for rulebooks and a decision environment that contains the needed event source plugins.
5. A list of alerts that are approved for automatic remediation, with an owner for each.

## Steps

1. Select a few frequent, low-risk alerts and agree on the fix and the verification for each.
2. Write the remediation as a job template, with the host or service taken from the event as `extra_vars`.
3. Write a rulebook with an event source such as `ansible.eda.alertmanager` or `ansible.eda.webhook`. Use the `ansible.eda.insert_hosts_to_meta` filter so the affected host is available to the action.
4. Add rules that match alert name, severity and environment, and use the `run_job_template` or `run_workflow_template` action. Add `throttle` or `once_within` so the same alert does not trigger repeated runs.
5. Register the decision environment (`ansible.eda.decision_environment`) and the rulebook project (`ansible.eda.project`) in the Event-Driven Ansible controller.
6. Start the rulebook activation (`ansible.eda.rulebook_activation`) and send test events from the monitoring tool.
7. Add verification and escalation to the job: check that the alert clears, and create a ticket or notify a team if it does not.
8. Review remediation results regularly, then widen the rules to further alerts.

## Success Criteria

1. A test alert causes exactly one job launch for the affected host, with the event data visible in the job.
2. The alert clears after the job, and the verification step proves it.
3. Duplicate or flapping alerts do not cause a flood of runs.
4. Failed fixes escalate to a person with the job output attached.
5. Mean time to resolve falls for the alerts in scope.

## Notes

- Use a separate rulebook activation per source, and keep rules narrow. Start in "notify only" mode, then switch the action to remediation.
- Vendor-specific versions of this pattern: [Remediate Dynatrace problems](remediate-dynatrace-problems.md), [Remediate Splunk ITSI episodes](remediate-splunk-itsi-episodes.md), [Remediate Microsoft SCOM alerts](remediate-microsoft-scom-alerts.md), [Remediate IBM Instana events](remediate-ibm-instana-events.md), [Act on LogicMonitor Edwin AI alerts](act-on-logicmonitor-edwin-ai-alerts.md), [Remediate Zabbix problems](remediate-zabbix-problems.md) and [Update BigPanda incidents from automation](update-bigpanda-incidents-from-automation.md).
- Tie each automatic fix to a ticket using [Create and update ServiceNow incidents from automation](../itsm/create-and-update-servicenow-incidents.md).
- Network alerts: Kentik and Juniper provide event sources in the network domain.
