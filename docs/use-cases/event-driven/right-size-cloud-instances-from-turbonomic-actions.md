---
title: Right-size cloud instances from Turbonomic actions
summary: Apply Turbonomic resize recommendations to AWS EC2 and Azure virtual machines through Event-Driven Ansible.
order: 80
personas: [Cloud engineer, FinOps lead, Operations lead]
collections: [ibm.turbonomic_eda, ansible.eda, ansible.controller]
key_content:
  - ibm.turbonomic_eda.eda_webhook
  - ibm.turbonomic_eda.resize_ec2_instance
  - ibm.turbonomic_eda.resize_azure_instance
  - ibm.turbonomic_eda.resize_ec2
  - ibm.turbonomic_eda.resize_azure
  - ansible.eda.webhook
---

# Right-size cloud instances from Turbonomic actions

## Description

Turbonomic recommends resizing cloud instances to match actual demand. Instead of copying each recommendation into a ticket, Turbonomic sends the approved action to Event-Driven Ansible, and a playbook resizes the EC2 instance or Azure virtual machine.

## Prerequisites

1. IBM Turbonomic managing the AWS or Azure accounts in scope, with permission to define webhook workflows.
2. Cloud credentials in Automation Platform that can resize instances.
3. Event-Driven Ansible controller and a decision environment that includes `ibm.turbonomic_eda`.
4. A change policy that says which resize actions may be applied without a ticket, and when.

## Steps

1. Create the Turbonomic webhook workflow with `ibm.turbonomic_eda.eda_webhook`, or in the Turbonomic interface, and attach it to the action policy.
2. Write a rulebook that receives the action with `ansible.eda.webhook` and filters by cloud, account, entity type and action type (resize).
3. Launch a job template that runs `ibm.turbonomic_eda.resize_ec2` or `ibm.turbonomic_eda.resize_azure`, which call the `resize_ec2_instance` and `resize_azure_instance` roles.
4. Use approval and maintenance-window checks before stopping production instances, because resizing normally needs a restart.
5. Report the result to Turbonomic and the change record, then verify the instance runs and meets the new size.

## Success Criteria

1. An approved Turbonomic resize action changes the instance type with no manual steps.
2. Disruptive actions run only in the approved window.
3. Every resize has a record of the old and new size.

## Notes

- Begin with non-production accounts and recommendations that scale down idle instances.
- Pair with the cloud use cases for tagging and cost hygiene.
