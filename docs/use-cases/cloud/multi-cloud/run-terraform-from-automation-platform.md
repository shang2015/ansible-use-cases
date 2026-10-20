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

## Prerequisites

1. Terraform configuration in a Git repository, and a remote state location with locking.
2. Cloud provider credentials in Automation Platform, injected into the job.
3. An execution environment containing the Terraform binary and `cloud.terraform`.
4. An agreed approval policy for production applies.

## Steps

1. Create a project for the Terraform repository, and an execution environment with the Terraform binary.
2. Create a plan job that calls `cloud.terraform.terraform` with a plan file, and pass the saved plan file between jobs with `cloud.terraform.plan_stash` so the reviewed plan is the one applied.
3. Add an approval node to the workflow so a reviewer inspects the plan.
4. Create an apply job that applies the stored plan with `cloud.terraform.terraform`, or use the `cloud.terraform.git_plan` role to clone a repository and apply a plan from it.
5. Read outputs with `cloud.terraform.terraform_output`, and build an in-memory inventory with the `cloud.terraform.inventory_from_outputs` role, or the `cloud.terraform.terraform_state` inventory plugin.
6. Run configuration playbooks against the new hosts in the next workflow node.
7. Add a destroy job, protected by approval, for temporary environments.

## Success Criteria

1. Every apply is preceded by a recorded plan and approval.
2. The applied plan is the same as the reviewed plan.
3. New hosts are configured automatically after provisioning in the same workflow.
4. Cloud credentials are not stored in the Terraform repository.

## Notes

- `cloud.terraform_ops` provides validated roles and playbooks for this integration with Automation Platform; check the collection documentation for the current content.
- For HCP Terraform or Terraform Enterprise, see [Automate HCP Terraform workspaces and policy checks](automate-hcp-terraform-workspaces-and-policy-checks.md).
- Keep Terraform state out of Automation Platform, and use a remote backend with locking.
- Compare with native modules in [Provision AWS networking and compute](../aws/provision-aws-networking-and-compute.md).
