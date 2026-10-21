---
title: Automate HCP Terraform workspaces and policy checks
summary: Create workspaces, variables and policy sets in HCP Terraform or Terraform Enterprise, and gate runs on policy results.
order: 40
personas: [Cloud engineer, Platform engineer, Cloud governance lead]
collections: [hashicorp.terraform]
key_content:
  - hashicorp.terraform.workspace
  - hashicorp.terraform.variable_sets
  - hashicorp.terraform.run
  - hashicorp.terraform.policy_set
  - hashicorp.terraform.plan_analyze
  - hashicorp.terraform.promote_run
  - hashicorp.terraform.tfc_inv
examples:
  - title: hashicorp.terraform certified collection
    url: https://github.com/hashicorp/terraform-ansible-collection
    note: modules for HCP Terraform and Terraform Enterprise
---

# Automate HCP Terraform workspaces and policy checks

## Description

For teams that use HCP Terraform or Terraform Enterprise, Ansible can manage the platform itself: projects, workspaces, variables and policies, and can start runs and decide whether to apply them. Application teams get a ready workspace on request, and governance rules are enforced consistently.

## Notes

- Combine with [Run Terraform from Automation Platform](run-terraform-from-automation-platform.md) if some configurations still run with the Terraform command line.
- Treat API tokens as secrets, and scope them to the organization or team that needs them.
- Pair with Event-Driven Ansible to start a run when a webhook reports a change in the source repository.
