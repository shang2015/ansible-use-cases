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

## Notes

- Combine with [Forward logs to a central logging platform](forward-logs-to-central-logging.md) for the full picture.
- Capacity numbers come from instance and instance group settings; see [Scale and tune with automation mesh](scale-with-automation-mesh.md) for acting on them.
- Keep remediation jobs conservative: restart services and re-sync, but leave database or storage failures to people.
- The `get_stats` playbook expects to run on or against the platform with an administrator account attached to the job template.
