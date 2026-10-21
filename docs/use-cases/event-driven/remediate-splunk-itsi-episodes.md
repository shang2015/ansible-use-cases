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

## Notes

- Use `splunk.itsi.itsi_service` and `splunk.itsi.itsi_glass_table` to manage services and dashboards as code in the same repository.
- The `splunk.enterprise` collection installs and checks Splunk Universal Forwarders, which feeds the data behind ITSI.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for the common design.
