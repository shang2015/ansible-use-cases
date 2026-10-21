---
title: Collect support data for Red Hat support cases
summary: Gather platform API output, sos reports and must-gather archives and attach them to a Red Hat support case in one job.
order: 150
personas: [Platform engineer, Operations lead, Support engineer]
collections: [infra.support_assist]
key_content:
  - infra.support_assist.aap_api_gather
  - infra.support_assist.aap_api_token
  - infra.support_assist.sos_report_rhel
  - infra.support_assist.ocp_must_gather
  - infra.support_assist.rh_case_create
  - infra.support_assist.rh_case_update
examples:
  - title: infra.support_assist validated collection
    url: https://github.com/redhat-cop/infra.support_assist
    note: playbooks and roles that gather diagnostics and manage support cases
---

# Collect support data for Red Hat support cases

## Description

Cut the time spent on the first round of questions in a support case. One job collects what Red Hat Support usually asks for (component API output, sos reports from RHEL hosts, must-gather from OpenShift), packages it, can create the case, and uploads the files to it.

## Notes

- Review what the archives contain before uploading. sos reports and must-gather output can include host names, addresses and configuration; apply the customer's data-sharing rules.
- Run [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md) first: its output often shows where to collect from.
- For sos reports there is also a generic `infra.support_assist.sos_report` playbook, which carries a deprecation notice; prefer the RHEL and OpenShift variants.
- Use Event-Driven Ansible to start the diagnostics workflow when a critical alert fires, so the data is captured at the moment of failure.
