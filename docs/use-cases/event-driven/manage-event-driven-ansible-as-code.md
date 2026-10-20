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

## Prerequisites

1. An Event-Driven Ansible controller (AAP 2.5 or later) and an account or token with administrator rights.
2. A Git repository for the configuration variables, with a branch strategy and reviewers.
3. An execution environment that includes `ansible.eda` and either `infra.eda_configuration` or `infra.aap_configuration`.

## Steps

1. Export or write the current configuration: projects, decision environments, credentials, credential types, event streams, rulebook activations and teams.
2. Store the objects as variables in Git, with one file per environment, and keep secrets in credentials or a vault, not in the repository.
3. Apply the configuration with the `ansible.eda` modules, for example `ansible.eda.project`, `ansible.eda.decision_environment`, `ansible.eda.credential` and `ansible.eda.rulebook_activation`.
4. Or use the validated roles: `infra.eda_configuration.dispatch` loads all object types, and `infra.aap_configuration.eda_rulebook_activations` and related roles manage them with the other platform objects.
5. Create event streams with `ansible.eda.event_stream` and publish the resulting endpoint to the sender.
6. Run the apply job from a pipeline on merge, with a check mode run on pull requests.
7. Use `ansible.eda.role_team_assignment` to give teams their roles.

## Success Criteria

1. A new environment can be configured from the repository with no manual console steps.
2. Every change to an activation or a credential is a reviewed commit.
3. A scheduled run reports no difference between Git and the controller.

## Notes

- Related: [Manage Automation Platform as code](../platform/manage-aap-as-code.md) for the same approach on controller, gateway and hub.
- Restart an activation when its rulebook changes, so the new rules are loaded.
