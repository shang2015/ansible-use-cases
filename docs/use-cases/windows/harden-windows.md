---
title: Harden Windows
summary: Audit and enforce CIS and DISA STIG baselines on Windows Server, with drift detection and audit-ready reports.
order: 60
personas: [Windows administrator, Security engineer, Compliance officer]
collections: [infra.windows_ops, ansible.windows]
key_content:
  - infra.windows_ops.windows_manage_cis
  - infra.windows_ops.windows_manage_stig
  - infra.windows_ops.compliance_hardening
  - infra.windows_ops.compliance_drift_detection
  - infra.windows_ops.compliance_audit_report
  - infra.windows_ops.windows_manage_audit
  - ansible.windows.win_audit_policy_system
examples:
  - title: infra.windows_ops validated collection
    url: https://github.com/redhat-cop/infra.windows_ops
    note: CIS and DISA STIG roles and compliance playbooks
---

# Harden Windows

## Description

Bring Windows Server to a published security baseline and keep it there. The `infra.windows_ops` roles implement the CIS Benchmark and DISA STIG controls for Windows Server 2019, 2022 and 2025, report which controls pass or fail, and can run read-only so the same job serves for both enforcement and audit.

## Notes

- Controls that need manual verification are listed in the report as a checklist instead of being forced. Plan time for them.
- Always test hardening on a copy of each server type first. Some controls change authentication and service behaviour.
- Combine with [Patch Windows servers](patch-windows-servers.md) so patching and hardening run on the same schedule and rings.
- Generic CIS and STIG programmes across operating systems are covered by the security use cases.
