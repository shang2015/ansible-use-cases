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

## Prerequisites

1. Windows Server 2019, 2022 or 2025 targets with PowerShell 5.1 or later and WinRM access with an administrator account.
2. The baseline decision: CIS, DISA STIG or both, and the profile or level to apply.
3. A test group of servers with the same roles as production, and a way to restore them (snapshot or backup).
4. A place to store reports, and the owner who reviews exceptions.

## Steps

1. Run `infra.windows_ops.compliance_drift_detection` as a check-mode job to produce a baseline report from `infra.windows_ops.windows_manage_cis` without changing the servers.
2. Review the failed controls and the controls the role lists as needing manual action. Record accepted exceptions in the role's skip lists (for example `windows_manage_stig_skip_rules`).
3. Apply the baseline to the test group with the `infra.windows_ops.compliance_hardening` playbook (DISA STIG) or the `windows_manage_cis` role (CIS). Verify that applications, monitoring and remote management still work.
4. Review high-risk settings, such as NTLM restrictions and user rights, that the roles flag for manual handling because they can lock out remote administration.
5. Roll out to production in rings, with a compliance threshold (`windows_manage_stig_compliance_threshold`) and fail-on-non-compliance if the job should stop the pipeline.
6. Set audit policies with `infra.windows_ops.windows_manage_audit` or `ansible.windows.win_audit_policy_system` where the baseline needs more than the role provides.
7. Schedule `compliance_drift_detection` weekly and `infra.windows_ops.compliance_audit_report` for audit periods, writing HTML or JSON reports to a shared location.

## Success Criteria

1. Compliance percentage per server is reported and meets the agreed threshold.
2. Each accepted exception is recorded with an owner and a reason.
3. Servers remain reachable and workloads run after hardening.
4. Drift reports show settings that changed since the last run.

## Notes

- Controls that need manual verification are listed in the report as a checklist instead of being forced. Plan time for them.
- Always test hardening on a copy of each server type first. Some controls change authentication and service behaviour.
- Combine with [Patch Windows servers](patch-windows-servers.md) so patching and hardening run on the same schedule and rings.
- Generic CIS and STIG programmes across operating systems are covered by the security use cases.
