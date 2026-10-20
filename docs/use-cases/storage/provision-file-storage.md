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

## Prerequisites

1. Administrative access to the NAS system or its management server, stored as an Automation Platform credential.
2. A prepared file service on the array: an SVM or NAS server with network interfaces, DNS and, for SMB, an Active Directory join.
3. A standard for protocol, security style, export policies, snapshot policy and quota tiers.
4. The list of client hosts, subnets or AD groups allowed to use each share.

## Steps

1. Capture the request: name, size, protocol (NFS, SMB or both), client list and quota.
2. Create the filesystem or volume:
   - ONTAP `netapp.ontap.na_ontap_volume` (or the `na_ontap_nas_create` role for shares in one pass);
   - PowerScale `dellemc.powerscale.filesystem`;
   - PowerStore `dellemc.powerstore.filesystem` on a `dellemc.powerstore.nasserver`;
   - Unity `dellemc.unity.filesystem` on a `dellemc.unity.nasserver`;
   - FlashBlade `everpure.flashblade.purefb_fs`;
   - Infinidat `infinidat.infinibox.infini_fs`.
3. Publish over NFS:
   - ONTAP `na_ontap_export_policy`, `na_ontap_export_policy_rule` and `na_ontap_nfs`;
   - PowerScale `dellemc.powerscale.nfs`;
   - PowerStore `dellemc.powerstore.nfs`, Unity `dellemc.unity.nfs`;
   - FlashBlade `purefb_export`;
   - Infinidat `infini_export` and `infini_export_client`.
4. Publish over SMB: ONTAP `na_ontap_cifs` and `na_ontap_cifs_acl`, PowerScale `dellemc.powerscale.smb`, PowerStore `dellemc.powerstore.smbshare`, Unity `dellemc.unity.smbshare`.
5. Apply quotas: ONTAP `na_ontap_qtree` with `na_ontap_quotas`, PowerScale `dellemc.powerscale.smartquota`, PowerStore `dellemc.powerstore.quota`, Unity `dellemc.unity.tree_quota` and `user_quota`, FlashBlade `purefb_userquota` and `purefb_groupquota`.
6. Attach the standard snapshot policy (see [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md)).
7. Mount or map the share on a test client, write a file, and publish the mount path to the requester.

## Success Criteria

1. The share is reachable by the requested clients over the requested protocol and not by others.
2. The quota is enforced, and usage can be reported.
3. Security style, export rules and share permissions match the standard.
4. The share has the standard snapshot policy attached.

## Notes

- For Kubernetes persistent storage, create the backend storage with these modules, then claim it from the cluster with the Kubernetes tooling in [Deploy applications to Kubernetes and OpenShift](../kubernetes/deploy-applications-to-kubernetes.md).
- Dell PowerScale supports access zones (`dellemc.powerscale.accesszone`) and SmartConnect network pools, which are useful for multi-tenant designs.
- Use the vendor info modules to check for name clashes before creating a share.
- Pair with [Decommission storage safely](decommission-storage-safely.md).
