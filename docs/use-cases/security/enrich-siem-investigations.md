---
title: Enrich SIEM investigations and automate response
summary: Add context to SIEM alerts, manage detection content and run response actions from Splunk, QRadar or CrowdStrike NG-SIEM.
order: 50
personas: [SOC analyst, Security engineer, SOAR engineer]
collections: [splunk.es, ibm.qradar, crowdstrike.falcon, servicenow.itsm]
key_content:
  - splunk.es.splunk_correlation_searches
  - splunk.es.splunk_investigation
  - splunk.es.splunk_notes
  - splunk.es.splunk_response_plan_execution
  - ibm.qradar.offense_info
  - ibm.qradar.offense_note
  - ibm.qradar.offense_action
  - crowdstrike.falcon.ngsiem_search
---

# Enrich SIEM investigations and automate response

## Description

Give analysts the context they would otherwise collect by hand, and run the routine response steps automatically. When the SIEM raises a finding or offense, Automation Platform gathers host, user and ticket details, writes them back to the case, and starts the matching response plan. Analysts decide on the exceptions.

## Prerequisites

1. A supported SIEM with an API user for Automation Platform: Splunk Enterprise Security, IBM QRadar or CrowdStrike Next-Gen SIEM.
2. Credentials for the sources used in enrichment (inventory, CMDB, EDR, identity).
3. A list of the alert types that are worth automating, each with an agreed response.
4. A way to receive the alert: a webhook into Event-Driven Ansible, or a scheduled job that polls for open cases.

## Steps

1. Receive or poll new cases: `ibm.qradar.offense_info` for QRadar offenses, `splunk.es.splunk_finding_info` for Splunk findings, or `crowdstrike.falcon.ngsiem_search` for NG-SIEM queries.
2. Enrich the case with data from other systems, for example the asset owner from the CMDB with `servicenow.itsm.configuration_item_info`, and host details from the EDR.
3. Write the result back: `ibm.qradar.offense_note` or `splunk.es.splunk_notes`, and create an investigation with `splunk.es.splunk_investigation` where a human review is needed.
4. Start the response plan for the alert type with `splunk.es.splunk_response_plan_execution`, or run the response playbook directly.
5. Update the case state with `ibm.qradar.offense_action` after the response, for example to close a confirmed false positive.
6. Manage the detection content as code: `splunk.es.splunk_correlation_searches` and `ibm.qradar.qradar_analytics_rules`, kept in Git and applied by a job template.

## Success Criteria

1. Each automated case carries the enrichment notes without analyst effort.
2. Response plans start for the defined alert types and record their result on the case.
3. Detection rules in the SIEM match the versions in Git.
4. Cases that need a decision are handed to an analyst with the context already attached.

## Notes

- Start with read-only enrichment, then add response actions after the quality of the alerts is proven.
- Send containment actions to [Contain threats from EDR detections](contain-threats-from-edr-detections.md).
- Pair with [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md) for the trigger side.
- ibm.qradar log source and rule modules marked deprecated in the collection should be replaced by their resource-module successors, such as `ibm.qradar.qradar_log_sources_management`.
