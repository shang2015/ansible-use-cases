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

## Prerequisites

1. Recovery targets agreed with the business: recovery point and recovery time objectives for the platform.
2. A backup destination outside the platform hosts, with retention and access controls.
3. The installation inventory and the secret key and password material used at install time, held securely, because a restore needs the original secrets.
4. A standby environment for restore tests, with the same version as production.
5. For high availability, a load balancer for the gateway, multiple nodes per component and a database design (external PostgreSQL with its own replication and failover is the customer's responsibility).

## Steps

1. Review the current design and list single points of failure: gateway, controller, hub storage, database, Receptor links, load balancer, DNS.
2. Take a backup with `infra.aap_utilities.aap_backup`, written to a destination such as `aap_backup_dest`, and copy it off the host.
3. Run the backup from a job template in the platform that has the installer directory and inventory available, and schedule it with `ansible.controller.schedule` (or run it from a separate management instance so the backup does not depend on the system being backed up).
4. For migrations and cold standbys, additionally export a portable artifact with `ansible.aap_snapshot.artifact_export`.
5. Test the restore on the standby with `infra.aap_utilities.aap_restore`, using the backup file, then validate sign-in, a project sync and a job run.
6. Stop and start the platform around maintenance with `infra.aap_utilities.aap_manage_containerized_services` (`svc_action: stop`, `start`, `status`), using tags for single components.
7. Write the DR runbook: who declares a disaster, which backup to restore, DNS or load balancer changes, and how to verify.
8. Rehearse the failover and restore on a schedule, and record timings against the objectives.

## Success Criteria

1. Backups run on schedule, are stored off-host and are retained per policy.
2. A restore on the standby brings the platform up with its data in the agreed recovery time.
3. Loss of one node of any redundant component does not interrupt job execution.
4. The DR runbook exists, is reviewed and was exercised this year.
5. Failed backups raise a notification.

## Notes

- Restore into the same Automation Platform version, and keep the installation inventory and its secrets safe, because a restore uses them.
- On OpenShift, backups are taken with the operator's backup custom resource and cluster tools, not with the installer-based roles. See [Install Automation Platform on OpenShift](install-aap-on-openshift.md).
- Execution nodes hold no platform data, so they can be rebuilt from automation. See [Scale and tune with automation mesh](scale-with-automation-mesh.md).
- Back up before any rotation or upgrade: [Rotate secrets and credentials](rotate-secrets-and-credentials.md).
- Pair with [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md) and Event-Driven Ansible to restart failed services automatically.
