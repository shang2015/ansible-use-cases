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

## Notes

- Protect the data with [Back up Oracle Cloud block and boot volumes](back-up-oracle-cloud-volumes.md).
- Keep the OCI API private key in an Automation Platform credential, not in the project.
- For Terraform-managed OCI estates, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
