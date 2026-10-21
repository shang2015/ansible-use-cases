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

## Notes

- Start with read-only enrichment, then add response actions after the quality of the alerts is proven.
- Send containment actions to [Contain threats from EDR detections](contain-threats-from-edr-detections.md).
- Pair with [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md) for the trigger side.
- ibm.qradar log source and rule modules marked deprecated in the collection should be replaced by their resource-module successors, such as `ibm.qradar.qradar_log_sources_management`.
