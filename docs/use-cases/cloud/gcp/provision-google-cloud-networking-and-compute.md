---
title: Provision Google Cloud networking and compute
summary: Create VPC networks, firewall rules, load balancers and Compute Engine instances from code.
order: 10
personas: [Cloud engineer, Platform engineer]
collections: [google.cloud, cloud.gcp_ops]
key_content:
  - google.cloud.gcp_compute_network
  - google.cloud.gcp_compute_subnetwork
  - google.cloud.gcp_compute_firewall
  - google.cloud.gcp_compute_address
  - google.cloud.gcp_compute_instance
  - google.cloud.gcp_http_lb
  - cloud.gcp_ops.manage_machine_image
examples:
  - title: google.cloud certified collection
    url: https://github.com/ansible-collections/google.cloud
    note: modules for Google Cloud resources
---

# Provision Google Cloud networking and compute

## Description

Build a Google Cloud environment with a playbook: a VPC network, subnets, firewall rules, IP addresses and Compute Engine instances. Projects can be rebuilt consistently in development, test and production, and removed when finished.

## Notes

- Dynamic discovery of the resulting instances is covered in [Use Google Cloud as a dynamic inventory source](use-gcp-as-dynamic-inventory.md).
- Resource creation order matters: create networks before subnets, and delete in reverse.
- If Terraform is the standard provisioner, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
