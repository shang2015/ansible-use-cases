---
title: Forward logs to a central logging platform
summary: Send job, activity and system logs from Automation Platform to Splunk, Elastic or another aggregator, and keep the setting in code.
order: 120
personas: [Platform engineer, Security analyst, Operations lead]
collections: [ansible.controller, ansible.platform, infra.aap_configuration]
key_content:
  - ansible.controller.settings
  - ansible.platform.settings
  - infra.aap_configuration.controller_settings
  - infra.aap_configuration.gateway_settings
  - ansible.controller.job_template
---

# Forward logs to a central logging platform

## Description

Give the security and operations teams the platform's logs in the tools they already use. Automation Platform can stream structured job events, activity stream entries and system logs to an external aggregator such as Splunk, Logstash or a generic HTTP or syslog target. Ansible applies and verifies the logging settings so every instance sends the same data to the same place.

## Notes

- Large volumes of job events can be significant. Filter at the source with the log level and enabled log types, and size the receiving side before turning on verbose output.
- Pair with [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md): logs show what happened, metrics show how loaded the platform is.
- Use Event-Driven Ansible to react to logged failures, for example to open an incident or retry a job, instead of only alerting.
- Manage the settings alongside the other configuration: [Manage Automation Platform as code](manage-aap-as-code.md).
