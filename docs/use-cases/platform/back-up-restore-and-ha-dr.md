---
title: Back up, restore and design HA and DR
summary: Schedule platform backups, prove restores, and design high availability and disaster recovery around the gateway, database and execution capacity.
order: 110
personas: [Platform engineer, Operations lead, Solution architect]
collections: [infra.aap_utilities, ansible.aap_snapshot, ansible.controller]
key_content:
  - infra.aap_utilities.aap_backup
  - infra.aap_utilities.aap_restore
  - infra.aap_utilities.aap_manage_containerized_services
  - ansible.aap_snapshot.artifact_export
  - ansible.controller.schedule
  - ansible.controller.job_template
---

# Back up, restore and design HA and DR

## Description

Make the automation platform itself recoverable. Ansible takes regular backups of the platform database and settings, stores them off-host, and runs restore tests on a standby. The same exercise records which components have to be redundant (gateway, controller, hub, database, execution nodes) and what the recovery steps are.

## Notes

- Restore into the same Automation Platform version, and keep the installation inventory and its secrets safe, because a restore uses them.
- On OpenShift, backups are taken with the operator's backup custom resource and cluster tools, not with the installer-based roles. See [Install Automation Platform on OpenShift](install-aap-on-openshift.md).
- Execution nodes hold no platform data, so they can be rebuilt from automation. See [Scale and tune with automation mesh](scale-with-automation-mesh.md).
- Back up before any rotation or upgrade: [Rotate secrets and credentials](rotate-secrets-and-credentials.md).
- Pair with [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md) and Event-Driven Ansible to restart failed services automatically.
