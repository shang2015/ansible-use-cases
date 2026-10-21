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

## Notes

- `ibm.ibm_zos_core.playbook_upgrade_validator` helps move older playbooks to a current major release of the collection.
- `ibm.ibm_eda_zos` is validated Event-Driven Ansible content for IBM Z, including an event filter for zSecure alerts, so security alerts on the mainframe can start automation.
- For a combined view with other IBM platforms, see [Manage IBM Power systems with the HMC](manage-ibm-power-systems-with-hmc.md) and [Patch and maintain AIX, VIOS and IBM i](patch-and-maintain-aix-vios-and-ibm-i.md).
- Mainframe teams usually keep their JCL and members in Git; the job template can fetch them at run time.
