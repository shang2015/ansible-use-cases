---
title: React to Red Hat Insights events
summary: Start automation from Red Hat Insights events, such as new findings on registered RHEL systems.
order: 110
personas: [Linux administrator, Security engineer, Operations lead]
collections: [redhat.insights_eda, redhat.insights, ansible.eda, ansible.controller]
key_content:
  - redhat.insights_eda.insights
  - redhat.insights.insights_client
  - redhat.insights.insights
  - ansible.eda.rulebook_activation
  - ansible.controller.job_template
---

# React to Red Hat Insights events

## Description

Red Hat Insights analyses registered RHEL systems and reports findings. The Insights event source brings those events to Event-Driven Ansible, so a new finding can open a ticket, run a remediation playbook or start a patch workflow, instead of waiting for someone to review a console.

## Prerequisites

1. RHEL systems registered with Red Hat Insights, with the Insights client installed.
2. Red Hat Insights credentials for the event source (for example service account details) stored as an Event-Driven Ansible credential.
3. Event-Driven Ansible controller with a decision environment that includes `redhat.insights_eda`.
4. Job templates for the remediation or notification actions.

## Steps

1. Register systems with the `redhat.insights.insights_client` role, and make sure the Insights inventory is available through the `redhat.insights.insights` inventory plugin.
2. Add the `redhat.insights_eda.insights` source to a rulebook and test which events arrive.
3. Write rules on event type, severity and affected system. Map the system to an inventory host.
4. Run a job template for events that have an approved fix, such as a configuration change or a patch, and for the others open a ticket.
5. Start the rulebook activation with `ansible.eda.rulebook_activation` and check one event end to end.
6. Report the job result so the finding is not raised again after it is resolved.

## Success Criteria

1. A new finding of an approved type starts one job against the right system.
2. Systems return to a clean state in Insights after the fix.
3. Findings without an automated fix create a ticket or notification.

## Notes

- Combine with the Linux use cases for patching and remediation with Red Hat Insights.
- Review the event types delivered by the source in its documentation, and match on those fields only.
