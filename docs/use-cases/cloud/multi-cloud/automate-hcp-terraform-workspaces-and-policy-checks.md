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

## Prerequisites

1. An HCP Terraform or Terraform Enterprise organization, and an API token with the needed rights, stored in Automation Platform.
2. A version-controlled repository per workload and a standard workspace baseline.
3. Defined policy sets, for example Sentinel or OPA policies, and rules for what may be applied automatically.
4. An execution environment containing `hashicorp.terraform`.

## Steps

1. Create the project and workspace for a request with `hashicorp.terraform.project` and `hashicorp.terraform.workspace`, or converge the standard baseline in one task with `hashicorp.terraform.workspace_bootstrap`.
2. Set shared and workload variables with `hashicorp.terraform.variable_sets` and `hashicorp.terraform.variable`.
3. Attach policy sets with `hashicorp.terraform.policy_set`, and give teams access with `hashicorp.terraform.team_workspace_access`.
4. Start a run with `hashicorp.terraform.run`, and read its plan with `hashicorp.terraform.view_plan`.
5. Classify the plan for drift and risky changes with `hashicorp.terraform.plan_analyze`, and use `hashicorp.terraform.promote_run` to apply it only when the policy outcomes allow.
6. Use the `hashicorp.terraform.tfc_inv` inventory plugin to bring workspace resources into Automation Platform for configuration jobs.
7. Send a notification or ticket when a run needs human approval.

## Success Criteria

1. A new workspace is available with the baseline variables, policies and access, from one request.
2. Runs that fail a mandatory policy are not applied.
3. Run results and approvals are recorded in Automation Platform and in HCP Terraform.
4. Workspace settings that drift from the baseline are corrected by the next scheduled run.

## Notes

- Combine with [Run Terraform from Automation Platform](run-terraform-from-automation-platform.md) if some configurations still run with the Terraform command line.
- Treat API tokens as secrets, and scope them to the organization or team that needs them.
- Pair with Event-Driven Ansible to start a run when a webhook reports a change in the source repository.
