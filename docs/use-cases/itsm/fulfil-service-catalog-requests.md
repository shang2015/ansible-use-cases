---
title: Fulfil service catalog requests with Automation Platform
summary: Turn ServiceNow catalog items into self-service automation that provisions, updates and closes the request.
order: 30
personas: [Service owner, Automation engineer, ITSM process owner]
collections: [servicenow.itsm, ansible.controller]
key_content:
  - servicenow.itsm.service_catalog_info
  - servicenow.itsm.service_catalog
  - servicenow.itsm.catalog_request
  - servicenow.itsm.catalog_request_info
  - servicenow.itsm.catalog_request_task
  - ansible.controller.job_template
---

# Fulfil service catalog requests with Automation Platform

## Description

Users order standard services, such as a virtual machine, a database or an access change, from the ServiceNow catalog. Automation Platform fulfils the request unattended and updates the request tasks, so the requester sees progress and the ticket closes without manual hand-offs.

## Prerequisites

1. A ServiceNow catalog item for each service, with variables for the inputs the automation needs.
2. A service account with rights on catalog requests and request tasks.
3. A job template or workflow for each service, with a survey that matches the catalog variables.
4. A way for ServiceNow to start the job: a ServiceNow flow that calls Automation Platform, or a scheduled job that polls for approved requests.

## Steps

1. List the available catalog items and their categories with `servicenow.itsm.service_catalog_info` and agree which ones to automate first.
2. Create the job template and add a survey for the same inputs. Validate input in the playbook, not only in the survey.
3. Start the job from ServiceNow when the request is approved. Alternatively poll `servicenow.itsm.catalog_request_info` and `servicenow.itsm.catalog_request_task` for approved items.
4. Fulfil the request, for example provision the resource, and write progress to the request task with `servicenow.itsm.catalog_request_task`.
5. Close the task with the result, such as host name and access details, and update the request with `servicenow.itsm.catalog_request`.
6. Use `servicenow.itsm.service_catalog` to place orders from automation when one request needs to trigger others, such as an access request that follows a server build.
7. Send a notification to the requester through a notification template when the service is ready.

## Success Criteria

1. An approved catalog request produces a finished service without manual steps.
2. The request and its tasks show the fulfilment result and the job reference.
3. Failed requests stay open and assigned, with the error captured in the task.
4. Lead time from approval to delivery is measured and falls compared with manual fulfilment.

## Notes

- Related: [Create and update ServiceNow incidents from automation](create-and-update-servicenow-incidents.md) for failures.
- Use the provisioning use cases for the target platform (VMware, AWS, Azure, OpenShift Virtualization) as the fulfilment job.
- Keep one catalog item per outcome. Free-form requests are hard to automate.
