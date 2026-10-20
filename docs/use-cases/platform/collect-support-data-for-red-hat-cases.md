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

## Prerequisites

1. A Red Hat offline API token with permission to open and update cases, stored as a platform credential.
2. Platform administrator access or an API token for the platform components whose output is collected.
3. SSH access with `become` to the hosts for sos reports, or the `oc` CLI and cluster-admin rights for must-gather, in the execution environment.
4. Outbound HTTPS from the execution node to the Red Hat support APIs, and `curl` for large uploads.
5. The account, product, version and severity values to use when creating cases.

## Steps

1. Create a project with the `infra.support_assist` collection and an execution environment that contains it, `curl` and (for OpenShift) `oc`.
2. Create credentials for the Red Hat offline token and for the platform tokens, and obtain API tokens for the platform components with `infra.support_assist.aap_api_token`.
3. Create job templates for the diagnostics you need: `infra.support_assist.aap_api_gather` for the gateway, controller, hub and Event-Driven Ansible APIs, `infra.support_assist.sos_report_rhel` for RHEL hosts, and `infra.support_assist.ocp_must_gather` for an OpenShift cluster.
4. Add a survey that asks for the case number, or whether to create a new case, and the severity and summary.
5. Create the case with `infra.support_assist.rh_case_create` when none exists, and attach the archives; add comments or more files later with `infra.support_assist.rh_case_update`.
6. Chain the diagnostics and case steps in a workflow so a support engineer launches one job, and keep a copy of the archives in the job artifacts.

## Success Criteria

1. One job run produces the requested archives and attaches them to the case.
2. A case created by the job has the correct product, version and severity and a link to the job.
3. Collected archives contain no data the customer's policy forbids sharing (see notes).
4. Any engineer on the team can run the workflow without handling the offline token.

## Notes

- Review what the archives contain before uploading. sos reports and must-gather output can include host names, addresses and configuration; apply the customer's data-sharing rules.
- Run [Monitor Automation Platform health and capacity](monitor-aap-health-and-capacity.md) first: its output often shows where to collect from.
- For sos reports there is also a generic `infra.support_assist.sos_report` playbook, which carries a deprecation notice; prefer the RHEL and OpenShift variants.
- Use Event-Driven Ansible to start the diagnostics workflow when a critical alert fires, so the data is captured at the moment of failure.
