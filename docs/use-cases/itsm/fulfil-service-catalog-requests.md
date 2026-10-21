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

## Notes

- Related: [Create and update ServiceNow incidents from automation](create-and-update-servicenow-incidents.md) for failures.
- Use the provisioning use cases for the target platform (VMware, AWS, Azure, OpenShift Virtualization) as the fulfilment job.
- Keep one catalog item per outcome. Free-form requests are hard to automate.
