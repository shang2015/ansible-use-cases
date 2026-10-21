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

## Notes

- Run the change against a pre-production firewall or a candidate configuration first where the platform supports it.
- Back up the configuration before each change; see [Back up device configuration](../network/backup-device-configuration.md).
- For cloud-delivered policy use [Secure web and private access with Zscaler](secure-web-and-private-access-with-zscaler.md).
- For intrusion prevention and threat profiles on the same firewalls see [Manage IDS/IPS and threat-prevention rules](manage-ids-ips-and-threat-prevention-rules.md).
