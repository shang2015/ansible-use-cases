---
title: Automate IBM Z (z/OS) operations
summary: Run job submission, data set management, operator commands, software management, partition control and CICS and IMS tasks on the mainframe from Automation Platform.
order: 30
personas: [Mainframe system programmer, Operations lead, Automation engineer]
collections: [ibm.ibm_zos_core, ibm.ibm_zosmf, ibm.ibm_zhmc, ibm.ibm_zos_cics, ibm.ibm_zos_ims, ibm.ibm_zos_sysauto, ibm.ibm_eda_zos]
key_content:
  - ibm.ibm_zos_core.zos_job_submit
  - ibm.ibm_zos_core.zos_data_set
  - ibm.ibm_zos_core.zos_operator
  - ibm.ibm_zos_core.zos_gather_facts
  - ibm.ibm_zosmf.zmf_workflow
  - ibm.ibm_zhmc.zhmc_partition
  - ibm.ibm_zos_cics.cmci_get
  - ibm.ibm_zos_ims.ims_command
examples:
  - title: ibm_zos_core collection
    url: https://github.com/ansible-collections/ibm_zos_core
  - title: ibm_zhmc collection
    url: https://github.com/zhmcclient/zhmc-ansible-modules
---

# Automate IBM Z (z/OS) operations

## Description

Extend the same automation platform used for distributed systems to the mainframe. z/OS system programmers use Ansible to submit JCL, manage data sets and files, issue operator commands, apply software updates, control partitions and manage CICS and IMS resources, and combine those steps with tasks on other platforms in a single workflow.

## Prerequisites

1. z/OS systems with the IBM Open Enterprise Python and Z Open Automation Utilities installed, and an SSH-reachable z/OS UNIX System Services environment for the core collection.
2. A z/OS user ID with the required RACF permissions for the tasks automated, and credentials in Automation Platform.
3. For z/OSMF content, a configured z/OSMF server; for HMC content, access to the IBM Z Hardware Management Console (HMC) Web Services API; for CICS, a CICSPlex SM CMCI endpoint.
4. An execution environment with the IBM collections and their Python dependencies.
5. A change process for the mainframe that matches the approvals used in Automation Platform.

## Steps

1. Verify connectivity and system information with `ibm.ibm_zos_core.zos_ping` and `ibm.ibm_zos_core.zos_gather_facts`.
2. Manage data sets and files with `ibm.ibm_zos_core.zos_data_set`, `zos_copy`, `zos_fetch`, `zos_find` and `zos_backup_restore`; edit configuration members with `zos_lineinfile` or `zos_blockinfile`.
3. Run batch work: submit JCL with `ibm.ibm_zos_core.zos_job_submit`, check status with `zos_job_query` and read results with `zos_job_output`, or call the `ibm.ibm_zos_core.job_status` role.
4. Issue operator commands and start tasks with `ibm.ibm_zos_core.zos_operator` and `zos_started_task`, and review messages needing a reply with `zos_operator_action_query`.
5. Manage users and security: `ibm.ibm_zos_core.zos_user` and `zos_user_info` for RACF profiles.
6. Automate software and workflows with z/OSMF: `ibm.ibm_zosmf.zmf_workflow` for workflows, and the `zmf_swmgmt_*` and `zmf_swupdate_*` roles to find missing updates and drive software updates.
7. Control the hardware layer with the HMC modules: `ibm.ibm_zhmc.zhmc_partition`, `zhmc_lpar`, `zhmc_storage_group` and `zhmc_cpc_capacity`.
8. Manage subsystems: CICS resources through `ibm.ibm_zos_cics.cmci_get`, `cmci_action`, `cmci_update` and region provisioning modules; IMS through `ibm.ibm_zos_ims.ims_command`, `ims_dbd_gen` and related modules; System Automation resources with the `ibm.ibm_zos_sysauto` roles.
9. Combine the steps into workflows with tasks on distributed systems, such as stopping an application tier, running a mainframe batch job and restarting the tier.

## Success Criteria

1. A batch job is submitted, monitored and its output captured by a job template, without a terminal session.
2. Data sets and configuration members are created and changed repeatably.
3. Software update status or missing fixes are reported on a schedule.
4. Mainframe steps appear in the same job history and approval trail as other platforms.

## Notes

- `ibm.ibm_zos_core.playbook_upgrade_validator` helps move older playbooks to a current major release of the collection.
- `ibm.ibm_eda_zos` is validated Event-Driven Ansible content for IBM Z, including an event filter for zSecure alerts, so security alerts on the mainframe can start automation.
- For a combined view with other IBM platforms, see [Manage IBM Power systems with the HMC](manage-ibm-power-systems-with-hmc.md) and [Patch and maintain AIX, VIOS and IBM i](patch-and-maintain-aix-vios-and-ibm-i.md).
- Mainframe teams usually keep their JCL and members in Git; the job template can fetch them at run time.
