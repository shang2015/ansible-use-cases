---
title: Run Terraform from Automation Platform
summary: Plan and apply Terraform configurations as controlled jobs, then configure the resulting infrastructure in the same workflow.
order: 10
personas: [Cloud engineer, Platform engineer, Automation architect]
collections: [cloud.terraform, cloud.terraform_ops]
key_content:
  - cloud.terraform.terraform
  - cloud.terraform.terraform_output
  - cloud.terraform.plan_stash
  - cloud.terraform.git_plan
  - cloud.terraform.inventory_from_outputs
  - cloud.terraform.terraform_state
examples:
  - title: cloud.terraform certified collection
    url: https://github.com/ansible-collections/cloud.terraform
    note: modules, roles and inventory plugins for Terraform
  - title: cloud.terraform_ops validated collection on the Ecosystem Catalog
    url: https://catalog.redhat.com/en/software/collection/cloud/terraform_ops
    note: roles and playbooks for Terraform integration with Automation Platform
---

# Run Terraform from Automation Platform

## Description

Organizations that already describe infrastructure in Terraform can run it from Automation Platform and keep one place for credentials, approvals and audit. Terraform creates the cloud resources, and Ansible configures what Terraform built, in a single workflow.

## Notes

- `cloud.terraform_ops` provides validated roles and playbooks for this integration with Automation Platform; check the collection documentation for the current content.
- For HCP Terraform or Terraform Enterprise, see [Automate HCP Terraform workspaces and policy checks](automate-hcp-terraform-workspaces-and-policy-checks.md).
- Keep Terraform state out of Automation Platform, and use a remote backend with locking.
- Compare with native modules in [Provision AWS networking and compute](../aws/provision-aws-networking-and-compute.md).
