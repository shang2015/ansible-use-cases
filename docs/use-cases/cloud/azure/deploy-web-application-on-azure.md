---
title: Deploy and migrate a web application on Azure
summary: Bootstrap a web app on Azure, validate the deployment and move it to another region.
order: 50
personas: [Cloud engineer, Application owner, DevOps engineer]
collections: [cloud.azure_ops, azure.azcollection]
key_content:
  - cloud.azure_ops.webapp
  - cloud.azure_ops.webapp_container
  - cloud.azure_ops.validate_deployment
  - cloud.azure_ops.vmss_migrate
  - azure.azcollection.azure_rm_webapp
  - azure.azcollection.azure_rm_virtualmachinescaleset
---

# Deploy and migrate a web application on Azure

## Description

Deliver an application to Azure with a repeatable playbook, check that the deployment works, and move it to another region when needed. Application teams run the workflow as a service; operations teams own the playbooks.

## Notes

- Pair with [Manage Azure load balancers and security groups](manage-azure-load-balancers-and-security-groups.md) for traffic management.
- `cloud.azure_ops` also includes playbooks for Azure Machine Learning platform tasks, such as `cloud.azure_ops.self_service_ml_platform`.
- Keep the old region available until the new one has passed validation and traffic has been switched.
