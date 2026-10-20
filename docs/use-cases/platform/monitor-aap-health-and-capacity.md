---
title: Monitor Automation Platform health and capacity
summary: Watch service status, job capacity and queue depth of the platform and alert or self-heal before users notice.
order: 130
personas: [Platform engineer, Operations lead, SRE]
collections: [infra.aap_configuration, infra.aap_utilities, ansible.controller, infra.automation_development_office, ansible.eda]
key_content:
  - infra.aap_configuration.get_stats
  - infra.aap_utilities.aap_manage_containerized_services
  - ansible.controller.instance
  - ansible.controller.instance_group
  - infra.automation_development_office.grafana_upload_dashboards
  - infra.automation_development_office.grafana_upload_alerts
  - ansible.eda.alertmanager
---

# Monitor Automation Platform health and capacity

## Description

Know whether the automation platform is healthy and has room to run the next job. Ansible collects metrics and service status from every component, feeds them to the monitoring tool the operations team already uses, installs dashboards and alerts, and can restart failed services on its own.

## Prerequisites

1. A monitoring stack, for example Prometheus with Grafana, Zabbix or an enterprise tool, that can scrape or receive the data.
2. Credentials for the platform API, with the permissions needed to read metrics and instances.
3. Access to the platform hosts or the OpenShift namespace for service status.
4. Agreed service levels: acceptable queue time, job success rate and capacity headroom.

## Steps

1. Pick the signals: component service status, database health, disk and memory on each node, node capacity and instance state, jobs waiting and running, and failed job ratio.
2. Collect controller metrics with `infra.aap_configuration.get_stats`, which reads the controller metrics endpoint, or scrape the same endpoint from the monitoring tool, and read node capacity with `ansible.controller.instance` and `ansible.controller.instance_group`.
3. Check the status of the containerized services on every node with `infra.aap_utilities.aap_manage_containerized_services` using `svc_action: status`.
4. Load dashboards and alert rules into Grafana as code with `infra.automation_development_office.grafana_upload_dashboards` and `infra.automation_development_office.grafana_upload_alerts`, or build the equivalent in the existing tool.
5. Alert on node loss, services down, capacity below a threshold, jobs queued beyond the agreed time and a falling success rate.
6. Optional: forward alerts to Event-Driven Ansible with the `ansible.eda.alertmanager` source and run a remediation job that restarts a service or adds capacity.
7. Review the trends monthly to decide when to add execution nodes or move workloads.

## Success Criteria

1. A dashboard shows service status, capacity and queue depth for every component.
2. A stopped service or an offline node raises an alert within the agreed time.
3. Capacity trend data supports the next sizing decision.
4. Auto-remediation, where configured, restarts a failed service and records what it did.
5. Monitoring configuration is stored in Git.

## Notes

- Combine with [Forward logs to a central logging platform](forward-logs-to-central-logging.md) for the full picture.
- Capacity numbers come from instance and instance group settings; see [Scale and tune with automation mesh](scale-with-automation-mesh.md) for acting on them.
- Keep remediation jobs conservative: restart services and re-sync, but leave database or storage failures to people.
- The `get_stats` playbook expects to run on or against the platform with an administrator account attached to the job template.
