---
title: Remediate Splunk ITSI episodes
summary: Act on Splunk IT Service Intelligence episodes with Event-Driven Ansible and write progress back to the episode.
order: 30
personas: [SRE, Operations lead, Splunk administrator]
collections: [splunk.itsi, splunk.enterprise, ansible.eda, ansible.controller]
key_content:
  - splunk.itsi.aap_eda_rulebook
  - splunk.itsi.itsi_episode_details_info
  - splunk.itsi.itsi_add_episode_comments
  - splunk.itsi.itsi_update_episode_details
  - splunk.itsi.itsi_aggregation_policy
  - ansible.controller.job_template
---

# Remediate Splunk ITSI episodes

## Description

Splunk ITSI groups related alerts into episodes. Event-Driven Ansible reads those episodes, starts a fix when the episode matches a known pattern and records what it did on the episode itself. Operators then see the automation result next to the alert history.

## Prerequisites

1. Splunk ITSI with correlation searches and aggregation policies that produce episodes for the services in scope.
2. A Splunk account or token with rights to read and update episodes.
3. Event-Driven Ansible controller and a decision environment that includes `splunk.itsi`.
4. Job templates for the approved fixes and an inventory that matches the entities named in the episodes.

## Steps

1. Review episode grouping with `splunk.itsi.itsi_aggregation_policy` and `splunk.itsi.itsi_correlation_search` (or their `_info` modules), so one real incident produces one episode.
2. Use the Splunk ITSI source plugin in a rulebook, with the connection details in an Event-Driven Ansible credential.
3. Write rules on episode title, severity, service and affected entity, and use `run_job_template` to start the matching fix.
4. In the job, read the episode with `splunk.itsi.itsi_episode_details_info`.
5. Add comments with `splunk.itsi.itsi_add_episode_comments` at the start and the end of the run.
6. Update the status, owner or severity with `splunk.itsi.itsi_update_episode_details`, for example set the episode to resolved after verification.
7. Test with a replayed episode, then enable the activation.

## Success Criteria

1. An episode of an approved pattern starts exactly one job.
2. The episode shows the job comments and the final status.
3. Episodes that automation cannot fix remain open and assigned to people.

## Notes

- Use `splunk.itsi.itsi_service` and `splunk.itsi.itsi_glass_table` to manage services and dashboards as code in the same repository.
- The `splunk.enterprise` collection installs and checks Splunk Universal Forwarders, which feeds the data behind ITSI.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for the common design.
