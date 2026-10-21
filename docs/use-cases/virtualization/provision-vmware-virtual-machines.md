---
title: Provision VMware virtual machines
summary: Deploy standardised VMs on vCenter from templates, content library items or OVF, with customisation and tags applied on the way in.
order: 10
personas: [Virtualization administrator, Cloud platform engineer]
collections: [vmware.vmware, cloud.vmware_ops, vmware.vmware_rest]
key_content:
  - vmware.vmware.vm
  - vmware.vmware.deploy_content_library_template
  - vmware.vmware.deploy_content_library_ovf
  - vmware.vmware.vm_apply_customization
  - vmware.vmware.tag_associations
  - cloud.vmware_ops.provision_vm
  - cloud.vmware_ops.deploy_custom_windows_template
examples:
  - title: cloud.vmware_ops validated collection
    url: https://github.com/redhat-cop/cloud.vmware_ops
    note: roles and playbooks for VM, template, ESXi and snapshot operations
  - title: vmware.vmware collection
    url: https://github.com/ansible-collections/vmware.vmware
---

# Provision VMware virtual machines

## Description

Replace manual vSphere clicks and ticket-driven VM builds with a repeatable job that creates a virtual machine from an approved template, content library item or OVF. Sizing, placement, networking, guest customisation and tags come from a variable file or a service catalog request, so every VM is built the same way.

## Notes

- `vmware.vmware_rest` is an alternative that talks to the vSphere REST API. Its `vcenter_vm_*` modules are mainly used for information and hardware settings, and several of its older modules are marked deprecated. Prefer `vmware.vmware` for new VM lifecycle work.
- Pair with [Manage VMware snapshots and VM lifecycle](manage-vmware-snapshots-and-vm-lifecycle.md) for day-2 operations and with [Operate vSphere clusters and ESXi hosts](operate-vsphere-clusters-and-esxi-hosts.md) for the platform underneath.
- To use vSphere as an inventory source, see the `vmware.vmware.vms` and `vmware.vmware.esxi_hosts` inventory plugins.
- Event-Driven Ansible: the `vmware.vmware.vcenter_event_manager` event source can start follow-up automation when a VM is created or changed in vCenter.
