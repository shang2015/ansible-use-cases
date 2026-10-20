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

## Prerequisites

1. An Azure credential in Automation Platform with rights to create the application resources.
2. Application code or a container image, and agreed region, size and naming.
3. Target networking, see [Provision Azure networking and virtual machines](provision-azure-networking-and-virtual-machines.md).
4. An execution environment with `cloud.azure_ops` and `azure.azcollection`.

## Steps

1. Copy the `cloud.azure_ops.webapp` playbook into a project as the reference deployment and adjust variables.
2. Use `cloud.azure_ops.webapp_container` when the application is delivered as a container image.
3. Where needed, manage App Service apps directly with `azure.azcollection.azure_rm_webapp`, or scale sets with `azure.azcollection.azure_rm_virtualmachinescaleset`.
4. Run `cloud.azure_ops.validate_deployment` as the last step, and fail the workflow if it does not pass.
5. To move the application to another region, run `cloud.azure_ops.vmss_migrate` into the new region, test, then switch traffic.
6. Publish the playbooks as job templates in a workflow, with an approval before production.

## Success Criteria

1. The application responds from its Azure endpoint after the deployment job.
2. The validation job reports success, or the workflow stops.
3. A region move completes with the application running in the new region.
4. Deployments are repeatable with no manual portal changes.

## Notes

- Pair with [Manage Azure load balancers and security groups](manage-azure-load-balancers-and-security-groups.md) for traffic management.
- `cloud.azure_ops` also includes playbooks for Azure Machine Learning platform tasks, such as `cloud.azure_ops.self_service_ml_platform`.
- Keep the old region available until the new one has passed validation and traffic has been switched.
