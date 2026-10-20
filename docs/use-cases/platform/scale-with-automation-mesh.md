---
title: Scale and tune with automation mesh
summary: Place execution capacity close to the managed estate with execution and hop nodes, instance groups and sensible job settings.
order: 80
personas: [Platform engineer, Solution architect, Network architect]
collections: [ansible.receptor, ansible.controller, infra.aap_configuration]
key_content:
  - ansible.receptor.setup
  - ansible.receptor.podman
  - ansible.controller.instance
  - ansible.controller.instance_group
  - ansible.controller.job_template
  - infra.aap_configuration.controller_instance_groups
---

# Scale and tune with automation mesh

## Description

Run automation near the systems it manages and grow capacity without growing the control plane. Automation mesh connects control nodes to execution nodes through Receptor, optionally across firewalls and DMZs using hop nodes. Instance groups route each job template to the right nodes, and job settings keep large runs fast.

## Prerequisites

1. A measured baseline: number of managed hosts, peak concurrent jobs, average job duration and current capacity per node (see [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md)).
2. A network map showing which sites and zones the automation must reach, and which direction connections may be opened.
3. RHEL hosts for each new execution or hop node, with the required ports opened between mesh peers.
4. A decision on how nodes are installed: through the platform installer inventory, or as standalone Receptor nodes.
5. TLS certificates for mesh links if the default is not accepted.

## Steps

1. Design the mesh: control nodes, execution nodes per site, and hop nodes in front of restricted zones. Define who peers outward to whom.
2. Add execution and hop nodes to the installer inventory and re-run the installer, or set up standalone Receptor nodes with `ansible.receptor.podman` and `ansible.receptor.setup`, defining `receptor_peers` and TLS.
3. Register the nodes in the controller with `ansible.controller.instance` and check that they report as ready.
4. Create instance groups per site, zone or workload with `ansible.controller.instance_group`, set minimum and maximum capacity, and assign nodes. Keep them in Git with `infra.aap_configuration.controller_instance_groups`.
5. Attach instance groups to organizations, inventories or job templates so jobs run on the intended nodes.
6. Tune the heavy templates with `ansible.controller.job_template` settings: forks, job slicing for large inventories, timeouts and fact caching.
7. Re-run the load test and compare it with the baseline.

## Success Criteria

1. Every execution node reports ready and appears in its instance group.
2. A job for a remote site runs on the execution node in that site, not on the control plane.
3. Jobs reach hosts behind a restricted zone only through the hop node.
4. A sliced job against the largest inventory finishes within the agreed time.
5. Removing one execution node does not stop jobs for its group when capacity remains.

## Notes

- Prefer control-only nodes once execution nodes exist, so job load does not slow the API.
- `ansible.receptor` configures the Receptor service and peering; the installer remains the reference for nodes it manages, so do not configure the same node both ways.
- On OpenShift, container groups run jobs as pods; combine them with the mesh for hybrid estates. See [Install Automation Platform on OpenShift](install-aap-on-openshift.md).
- Before adding nodes, check the playbooks themselves: serial execution, long fact gathering and unneeded loops cost more than missing capacity.
