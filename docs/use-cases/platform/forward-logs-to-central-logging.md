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

## Prerequisites

1. A logging platform with a reachable endpoint (HTTP event collector, Logstash input or syslog listener) and a token or credentials for it.
2. A decision on what to send: job events, activity stream, system logs, and the minimum log level.
3. Network access from each platform node that sends logs, and TLS trust for the endpoint.
4. Index, source type or pipeline rules prepared on the logging side, plus the dashboards and alerts to be built from the data.
5. Administrator access to the platform settings, ideally through the configuration repository.

## Steps

1. Agree the log schema and retention with the owners of the logging platform, including which fields identify the organization, template and user.
2. Set the logging aggregator type, host, port or URL, token, enabled log sources, level and certificate verification in the controller with `ansible.controller.settings`, or through the `infra.aap_configuration.controller_settings` role from code.
3. Apply the equivalent gateway and platform logging settings with `ansible.platform.settings` or `infra.aap_configuration.gateway_settings`, where the release exposes them.
4. Run a job template with `ansible.controller.job_template` that exercises success, failure and a long-running task, and confirm the events arrive.
5. Build the searches, dashboards and alerts on the logging side: failed jobs, jobs by template and team, changes by user, and failed logins.
6. Add the platform hosts' own OS and container logs to the collection agent if they are in scope.
7. Document the settings in Git, and add a check job that tests the endpoint and alerts when logs stop arriving.

## Success Criteria

1. Job events and activity entries from a test run are searchable in the logging platform within the agreed delay.
2. Fields allow filtering by organization, job template, status and user.
3. Alerts exist for failed jobs and for log silence.
4. The same settings are applied to every instance from one repository.
5. Secrets for the aggregator are stored as credentials or vault values, not in the repository.

## Notes

- Large volumes of job events can be significant. Filter at the source with the log level and enabled log types, and size the receiving side before turning on verbose output.
- Pair with [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md): logs show what happened, metrics show how loaded the platform is.
- Use Event-Driven Ansible to react to logged failures, for example to open an incident or retry a job, instead of only alerting.
- Manage the settings alongside the other configuration: [Manage Automation Platform as code](manage-aap-as-code.md).
