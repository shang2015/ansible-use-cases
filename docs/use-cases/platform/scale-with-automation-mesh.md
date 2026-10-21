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

## Notes

- Prefer control-only nodes once execution nodes exist, so job load does not slow the API.
- `ansible.receptor` configures the Receptor service and peering; the installer remains the reference for nodes it manages, so do not configure the same node both ways.
- On OpenShift, container groups run jobs as pods; combine them with the mesh for hybrid estates. See [Install Automation Platform on OpenShift](install-aap-on-openshift.md).
- Before adding nodes, check the playbooks themselves: serial execution, long fact gathering and unneeded loops cost more than missing capacity.
