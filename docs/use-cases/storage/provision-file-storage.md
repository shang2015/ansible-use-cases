---
title: Provision file storage
summary: Create NFS exports, SMB shares and filesystems with access rules and quotas on NAS platforms.
order: 20
personas: [Storage administrator, Infrastructure engineer]
collections: [netapp.ontap, dellemc.powerscale, dellemc.powerstore, dellemc.unity, everpure.flashblade, infinidat.infinibox]
key_content:
  - netapp.ontap.na_ontap_volume
  - netapp.ontap.na_ontap_export_policy_rule
  - netapp.ontap.na_ontap_cifs
  - netapp.ontap.na_ontap_quotas
  - dellemc.powerscale.nfs
  - dellemc.powerscale.smb
  - dellemc.powerscale.smartquota
  - dellemc.powerstore.filesystem
  - everpure.flashblade.purefb_fs
---

# Provision file storage

## Description

Deliver NFS exports and SMB shares from enterprise NAS systems through a repeatable request: create the filesystem or volume, publish it through the right protocol, restrict access, and apply a quota. Application and virtualization teams get file storage in minutes, while storage teams keep the naming, security and capacity standards.

## Notes

- For Kubernetes persistent storage, create the backend storage with these modules, then claim it from the cluster with the Kubernetes tooling in [Deploy applications to Kubernetes and OpenShift](../kubernetes/deploy-applications-to-kubernetes.md).
- Dell PowerScale supports access zones (`dellemc.powerscale.accesszone`) and SmartConnect network pools, which are useful for multi-tenant designs.
- Use the vendor info modules to check for name clashes before creating a share.
- Pair with [Decommission storage safely](decommission-storage-safely.md).
