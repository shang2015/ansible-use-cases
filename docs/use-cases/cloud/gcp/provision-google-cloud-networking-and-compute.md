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

## Prerequisites

1. A Google Cloud project and a service account with Compute Admin and Network Admin roles, stored as a Google Compute Engine credential in Automation Platform.
2. An execution environment containing `google.cloud` and `cloud.gcp_ops`, and the Google authentication libraries.
3. Region, zone, CIDR, machine type and image standards.
4. Labels or naming conventions for ownership and environment.

## Steps

1. Define the design as variables: project, region, subnets, firewall rules, machine types and labels.
2. Create the network and subnets with `google.cloud.gcp_compute_network` and `google.cloud.gcp_compute_subnetwork`.
3. Add firewall rules with `google.cloud.gcp_compute_firewall` and reserve addresses with `google.cloud.gcp_compute_address`.
4. Create the Compute Engine instances with `google.cloud.gcp_compute_instance`, on a base image or a prepared machine image from the `cloud.gcp_ops.manage_machine_image` role.
5. Publish traffic through an HTTP load balancer using the `google.cloud.gcp_http_lb` role where the application needs one.
6. Publish the playbook as a job template with a survey, and add a teardown job that deletes resources in reverse order.

## Success Criteria

1. The network, firewall rules and instances exist with the expected addresses, labels and machine types.
2. Re-running the job reports no changes.
3. Instances can be reached on the allowed ports only.
4. A teardown run removes the resources it created.

## Notes

- Dynamic discovery of the resulting instances is covered in [Use Google Cloud as a dynamic inventory source](use-gcp-as-dynamic-inventory.md).
- Resource creation order matters: create networks before subnets, and delete in reverse.
- If Terraform is the standard provisioner, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
