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

## Prerequisites

1. Zscaler tenant access with API credentials for ZIA and ZPA, stored as Automation Platform credentials.
2. A policy model: URL categories, user groups, application owners and the intended access rules.
3. For ZPA, deployed app connector groups that can reach the target applications.
4. A pilot user group for testing before wide release.

## Steps

1. Read the current configuration with the `*_info` modules and commit it as the baseline.
2. Define custom URL categories with `zscaler.ziacloud.zia_url_categories` and web policy with `zscaler.ziacloud.zia_url_filtering_rules`.
3. Add network-level rules with `zscaler.ziacloud.zia_cloud_firewall_rule`.
4. Publish ZIA changes with `zscaler.ziacloud.zia_activation_status`, because ZIA applies saved changes only after activation.
5. Onboard a private application: create the segment with `zscaler.zpacloud.zpa_application_segment`, add it to a group with `zscaler.zpacloud.zpa_segment_group`, and allow access with `zscaler.zpacloud.zpa_policy_access_rule`.
6. Run the job on every merge, and a drift check on a schedule that compares the tenant with Git.

## Success Criteria

1. ZIA and ZPA settings in the tenant match the repository after each run.
2. A new private application is reachable by its user group and by no one else.
3. Changes are visible to users only after activation, and each activation maps to a reviewed change.
4. The drift check reports no unmanaged rules, or lists them for review.

## Notes

- Zscaler policy order matters. Keep rule order explicit in the variables.
- For on-premises and data-center firewalls see [Manage firewall policy across vendors](manage-firewall-policy-across-vendors.md).
- ZIA also has IPS and DLP modules; see [Manage IDS/IPS and threat-prevention rules](manage-ids-ips-and-threat-prevention-rules.md).
