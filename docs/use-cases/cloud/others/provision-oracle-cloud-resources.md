---
title: Provision Oracle Cloud (OCI) resources
summary: Create compartments, virtual cloud networks, load balancers and compute instances on Oracle Cloud Infrastructure from code.
order: 10
personas: [Cloud engineer, Platform engineer]
collections: [ansible.oci]
key_content:
  - ansible.oci.oci_identity_compartment
  - ansible.oci.oci_network_vcn
  - ansible.oci.oci_network_subnet
  - ansible.oci.oci_network_security_list
  - ansible.oci.oci_instance
  - ansible.oci.oci_loadbalancer
  - ansible.oci.oci_compute
examples:
  - title: ansible.oci certified collection
    url: https://github.com/ansible-collections/ansible.oci
    note: modules and inventory plugin for Oracle Cloud Infrastructure
---

# Provision Oracle Cloud (OCI) resources

## Description

Create an Oracle Cloud Infrastructure environment with a playbook: compartments, a virtual cloud network, subnets, security lists, compute instances and a load balancer. The same job template builds each environment the same way, and the inventory plugin finds the new instances afterwards.

## Prerequisites

1. An OCI tenancy, a user or API key with rights on the target compartment, and the configuration file or variables the OCI SDK needs.
2. An execution environment containing `ansible.oci` and the OCI Python SDK.
3. Region, CIDR, shape, image and tagging standards.
4. An SSH key for the instances.

## Steps

1. Create the compartment for the workload with `ansible.oci.oci_identity_compartment`.
2. Create the network with `ansible.oci.oci_network_vcn`, `ansible.oci.oci_network_subnet` and `ansible.oci.oci_network_internet_gateway`, then add routes with `ansible.oci.oci_network_route_table`.
3. Define access rules with `ansible.oci.oci_network_security_list` or `ansible.oci.oci_network_security_group`.
4. Launch compute instances with `ansible.oci.oci_instance`.
5. Publish traffic through `ansible.oci.oci_loadbalancer` with its listener and backend set modules.
6. Build an inventory from the new instances with the `ansible.oci.oci_compute` plugin and run configuration jobs.
7. Publish the playbook as a job template with a survey, and add a teardown job.

## Success Criteria

1. The compartment, network and instances exist with the expected settings and tags.
2. Re-running the playbook produces no changes.
3. Instances appear in the inventory and can be configured by follow-on jobs.
4. Teardown removes every resource the playbook created.

## Notes

- Protect the data with [Back up Oracle Cloud block and boot volumes](back-up-oracle-cloud-volumes.md).
- Keep the OCI API private key in an Automation Platform credential, not in the project.
- For Terraform-managed OCI estates, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
