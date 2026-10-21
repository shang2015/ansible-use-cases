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

## Notes

- Begin with non-production accounts and recommendations that scale down idle instances.
- Pair with the cloud use cases for tagging and cost hygiene.
