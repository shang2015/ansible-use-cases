---
title: Respond to security events with Event-Driven Ansible
summary: Trigger containment, enrichment and remediation automatically from alerts, syslog, webhooks and ticket events.
order: 160
personas: [SOC engineer, Automation architect, Security engineer]
collections: [ansible.eda, cyberark.pas, servicenow.itsm, redhat.insights_eda, ansible.controller]
key_content:
  - ansible.eda.webhook
  - ansible.eda.kafka
  - ansible.eda.rulebook_activation
  - cyberark.pas.syslog
  - servicenow.itsm.records
  - redhat.insights_eda.insights
---

# Respond to security events with Event-Driven Ansible

## Description

Act on a security event while it is still relevant. Event-Driven Ansible listens to sources such as SIEM webhooks, message queues, syslog and ticketing systems, matches events against rules, and starts the right job template in Automation Platform with the event data as input.

## Prerequisites

1. An Event-Driven Ansible controller connected to automation controller, with a decision environment that has the needed event source plugins.
2. At least one event source that can reach the controller: a webhook from the SIEM or EDR, a Kafka topic, syslog from a vault, or Red Hat Insights events.
3. Job templates for the actions, each safe to run unattended, such as containment, enrichment or credential rotation.
4. A list of approved automatic actions with owners, and a manual-approval path for the rest.

## Steps

1. Choose the sources and build the rulebook, for example `ansible.eda.webhook` for alerts, `ansible.eda.kafka` for streams, `cyberark.pas.syslog` for privileged access events, `servicenow.itsm.records` for ticket records, or `redhat.insights_eda.insights` for Insights events.
2. Write rules that match on event fields such as severity, asset class and alert type, and map each to a job template.
3. Add safeguards: throttling, exclusion lists for critical systems, and an approval node in the target workflow.
4. Store the rulebook in a project and create the activation with `ansible.eda.rulebook_activation`.
5. Test with synthetic events and check which job templates start and with what extra variables.
6. Review activation logs and job results regularly, and tune rules that fire too often or too rarely.

## Success Criteria

1. A test event of each supported type starts the expected job template within the agreed time.
2. Events from excluded systems do not start automatic actions.
3. Every automatic action is traceable from the event to the job and its result.
4. Rule changes go through review in Git.

## Notes

- Start with notification and enrichment actions, then add containment once false positives are measured.
- Typical actions: [Contain threats from EDR detections](contain-threats-from-edr-detections.md), [Enrich SIEM investigations and automate response](enrich-siem-investigations.md) and [Rotate privileged credentials](rotate-privileged-credentials.md).
- Use [Retrieve secrets from external vaults](retrieve-secrets-from-external-vaults.md) for the credentials that rulebooks use to call back into the platform.
