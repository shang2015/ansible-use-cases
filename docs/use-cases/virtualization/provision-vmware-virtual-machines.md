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

## Prerequisites

1. A vCenter Server (or ESXi host) reachable from the execution environment, and a service account with rights to create VMs in the target folders, clusters and datastores.
2. The vCenter credential stored in Automation Platform as a custom credential type, with certificate validation settings agreed with the security team.
3. An execution environment that includes `vmware.vmware`, `cloud.vmware_ops` and their Python dependencies.
4. Golden templates, content library items or OVF files, plus guest customisation specifications for Linux and Windows.
5. A naming, folder, datastore and network standard that the variable file can reference.

## Steps

1. Build or import the VM images: use `vmware.vmware.folder_template_from_vm` or `vmware.vmware.content_template` to turn a prepared VM into a template, and `vmware.vmware.import_content_library_ovf` to load vendor appliances into a content library.
2. Create the folder layout with `vmware.vmware.folder`, or the `cloud.vmware_ops.manage_folder` playbook, so new VMs land in the right place.
3. Deploy the VM with `vmware.vmware.deploy_content_library_template`, `vmware.vmware.deploy_content_library_ovf` or `vmware.vmware.deploy_folder_template`. The `cloud.vmware_ops.provision_vm` role wraps this flow, and `cloud.vmware_ops.deploy_custom_windows_template` covers Windows templates that need customisation.
4. Adjust the VM to the request with `vmware.vmware.vm`, including CPU, memory, disks and networks, and apply guest customisation with `vmware.vmware.vm_apply_customization`.
5. Power the VM on with `vmware.vmware.vm_powerstate` and wait for VMware Tools and an IP address before handing over.
6. Tag the VM and set custom attributes with `vmware.vmware.tag_associations` and `vmware.vmware.vm_custom_attributes` so ownership, environment and backup policy are recorded.
7. Add the new host to the inventory, for example with the `vmware.vmware.vms` inventory plugin, and run a follow-up job template for OS configuration.
8. Expose the job template as a survey or through a service catalog so requesters supply only name, size and environment.

## Success Criteria

1. A requested VM is created in the correct folder, cluster, datastore and network without manual vSphere work.
2. The VM boots with the intended hostname, IP configuration and guest customisation.
3. Tags and custom attributes are present and match the request.
4. Re-running the job with the same variables reports no changes.

## Notes

- `vmware.vmware_rest` is an alternative that talks to the vSphere REST API. Its `vcenter_vm_*` modules are mainly used for information and hardware settings, and several of its older modules are marked deprecated. Prefer `vmware.vmware` for new VM lifecycle work.
- Pair with [Manage VMware snapshots and VM lifecycle](manage-vmware-snapshots-and-vm-lifecycle.md) for day-2 operations and with [Operate vSphere clusters and ESXi hosts](operate-vsphere-clusters-and-esxi-hosts.md) for the platform underneath.
- To use vSphere as an inventory source, see the `vmware.vmware.vms` and `vmware.vmware.esxi_hosts` inventory plugins.
- Event-Driven Ansible: the `vmware.vmware.vcenter_event_manager` event source can start follow-up automation when a VM is created or changed in vCenter.
