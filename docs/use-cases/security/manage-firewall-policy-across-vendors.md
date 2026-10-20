---
title: Manage firewall policy across vendors
summary: Create, review and publish firewall rules on Palo Alto, Fortinet, Check Point and Cisco ASA from one request-driven workflow.
order: 40
personas: [Network security engineer, Security architect, Change manager]
collections: [paloaltonetworks.panos, paloaltonetworks.panos_policy_automation, fortinet.fortios, fortinet.fortimanager, check_point.mgmt, cisco.asa, servicenow.itsm]
key_content:
  - paloaltonetworks.panos_policy_automation.policy_creation
  - paloaltonetworks.panos.panos_security_rule
  - fortinet.fortios.fortios_firewall_policy
  - fortinet.fortimanager.fmgr_securityconsole_install_package
  - check_point.mgmt.cp_mgmt_access_rule
  - check_point.mgmt.cp_mgmt_install_policy
  - cisco.asa.asa_acls
---

# Manage firewall policy across vendors

## Description

Handle firewall rule requests the same way on every platform. A request supplies source, destination and service, the automation checks whether the traffic is already allowed, adds the objects and rule on the right firewall, commits the change and records it. Teams with several vendors get one process instead of one per console.

## Prerequisites

1. API or SSH access to the firewalls or their managers (Panorama, FortiManager, Check Point management server), with a service account that has policy rights.
2. Credentials stored in Automation Platform as machine or custom credentials, not in playbooks.
3. A request source: ServiceNow catalog item, a Git pull request, or a survey on a job template.
4. A naming and tagging standard for address objects, services and rules.

## Steps

1. Normalize the request into variables: source, destination, service, action, business owner and ticket number.
2. Check the current policy first. On Palo Alto, use the `paloaltonetworks.panos_policy_automation.lookup_policy` role to test whether the traffic is already permitted.
3. Create the objects and rule with the platform modules: `paloaltonetworks.panos_policy_automation.policy_creation` or `paloaltonetworks.panos.panos_security_rule` for PAN-OS, `fortinet.fortios.fortios_firewall_policy` for FortiGate, `check_point.mgmt.cp_mgmt_access_rule` for Check Point, `cisco.asa.asa_acls` for Cisco ASA.
4. For manager-based platforms, push the change to devices: `fortinet.fortimanager.fmgr_securityconsole_install_package`, `check_point.mgmt.cp_mgmt_install_policy` (after `check_point.mgmt.cp_mgmt_publish`), or `paloaltonetworks.panos.panos_commit_panorama`.
5. Add an approval node to the workflow so that a security reviewer accepts the rule before it is committed.
6. Update the ticket with `servicenow.itsm.change_request` or the equivalent, with the rule details and the job link.

## Success Criteria

1. A request produces the same rule structure on every platform, using the agreed names and tags.
2. Traffic that is already permitted creates no duplicate rule.
3. Every rule change maps to an approved ticket and a job run.
4. A failed commit or policy install leaves the previous policy active and is reported in the job output.

## Notes

- Run the change against a pre-production firewall or a candidate configuration first where the platform supports it.
- Back up the configuration before each change; see [Back up device configuration](../network/backup-device-configuration.md).
- For cloud-delivered policy use [Secure web and private access with Zscaler](secure-web-and-private-access-with-zscaler.md).
- For intrusion prevention and threat profiles on the same firewalls see [Manage IDS/IPS and threat-prevention rules](manage-ids-ips-and-threat-prevention-rules.md).
