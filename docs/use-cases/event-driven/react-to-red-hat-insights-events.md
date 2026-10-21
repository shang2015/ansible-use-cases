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

## Notes

- Combine with the Linux use cases for patching and remediation with Red Hat Insights.
- Review the event types delivered by the source in its documentation, and match on those fields only.
