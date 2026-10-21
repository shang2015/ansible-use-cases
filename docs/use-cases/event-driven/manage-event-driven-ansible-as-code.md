---
title: Manage Event-Driven Ansible as code
summary: Define projects, decision environments, credentials, event streams and activations in Git and apply them with playbooks.
order: 120
personas: [Platform administrator, Automation engineer]
collections: [ansible.eda, infra.eda_configuration, infra.aap_configuration]
key_content:
  - ansible.eda.project
  - ansible.eda.decision_environment
  - ansible.eda.credential
  - ansible.eda.event_stream
  - ansible.eda.rulebook_activation
  - infra.eda_configuration.dispatch
  - infra.aap_configuration.eda_rulebook_activations
---

# Manage Event-Driven Ansible as code

## Description

Rulebook activations, credentials and decision environments are configured in the Event-Driven Ansible controller. Defining them in Git as variable files, and applying them with a pipeline, gives review, history and a repeatable setup across development, test and production.

## Notes

- Related: [Manage Automation Platform as code](../platform/manage-aap-as-code.md) for the same approach on controller, gateway and hub.
- Restart an activation when its rulebook changes, so the new rules are loaded.
