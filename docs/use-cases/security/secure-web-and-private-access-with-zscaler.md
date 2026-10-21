---
title: Secure web and private access with Zscaler
summary: Manage Zscaler Internet Access and Private Access policy, segments and activation as code.
order: 170
personas: [Network security engineer, Zero trust architect, Security operations]
collections: [zscaler.ziacloud, zscaler.zpacloud]
key_content:
  - zscaler.ziacloud.zia_url_categories
  - zscaler.ziacloud.zia_url_filtering_rules
  - zscaler.ziacloud.zia_cloud_firewall_rule
  - zscaler.ziacloud.zia_activation_status
  - zscaler.zpacloud.zpa_application_segment
  - zscaler.zpacloud.zpa_segment_group
  - zscaler.zpacloud.zpa_policy_access_rule
---

# Secure web and private access with Zscaler

## Description

Manage cloud-delivered web security and zero trust access from the same pipeline as other infrastructure. URL filtering and cloud firewall rules in Zscaler Internet Access (ZIA) and application segments and access policies in Zscaler Private Access (ZPA) are defined in Git, reviewed, and applied with Automation Platform.

## Notes

- Zscaler policy order matters. Keep rule order explicit in the variables.
- For on-premises and data-center firewalls see [Manage firewall policy across vendors](manage-firewall-policy-across-vendors.md).
- ZIA also has IPS and DLP modules; see [Manage IDS/IPS and threat-prevention rules](manage-ids-ips-and-threat-prevention-rules.md).
