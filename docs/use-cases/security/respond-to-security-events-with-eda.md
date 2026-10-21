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

## Notes

- Start with notification and enrichment actions, then add containment once false positives are measured.
- Typical actions: [Contain threats from EDR detections](contain-threats-from-edr-detections.md), [Enrich SIEM investigations and automate response](enrich-siem-investigations.md) and [Rotate privileged credentials](rotate-privileged-credentials.md).
- Use [Retrieve secrets from external vaults](retrieve-secrets-from-external-vaults.md) for the credentials that rulebooks use to call back into the platform.
