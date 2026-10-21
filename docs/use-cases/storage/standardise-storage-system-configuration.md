---
title: Standardise storage system configuration
summary: Apply the same time, DNS, directory, monitoring, alerting, certificate and firmware settings to every storage system.
order: 50
personas: [Storage administrator, Operations lead]
collections: [netapp.ontap, dellemc.powerstore, dellemc.powerscale, everpure.flasharray, everpure.flashblade, ibm.storage_virtualize, infinidat.infinibox, netapp.storagegrid]
key_content:
  - netapp.ontap.na_ontap_ntp
  - netapp.ontap.na_ontap_dns
  - netapp.ontap.na_ontap_ldap
  - netapp.ontap.na_ontap_software_update
  - dellemc.powerstore.ntp
  - dellemc.powerscale.alert_channel
  - everpure.flasharray.purefa_ntp
  - everpure.flasharray.purefa_syslog
  - ibm.storage_virtualize.ibm_sv_manage_syslog_server
  - infinidat.infinibox.infini_notification_target
---

# Standardise storage system configuration

## Description

Storage arrays are configured one at a time by different people, and settings drift. Define the baseline once (NTP, DNS, directory service, SNMP and syslog, alert destinations, certificates, users and firmware level) and apply it to every array on a schedule. A drift report then shows which systems differ from the baseline.

## Notes

- Some arrays treat these settings as cluster-wide, others per node or per SVM; model that in the variable structure.
- Storage alerts can start Event-Driven Ansible rulebooks, for example to expand a volume or open an incident. See [Gather storage facts and capacity reports](gather-storage-facts-and-capacity-reports.md) for the reporting side.
- For switch and server firmware used with the arrays, see [Update server firmware and BIOS](../infrastructure/update-server-firmware-and-bios.md).
- Pair with [Provision block storage](provision-block-storage.md) once the baseline is in place.
