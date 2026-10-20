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

## Prerequisites

1. Administrator credentials for each array or management server, stored in Automation Platform.
2. A baseline per platform: time servers, DNS servers and domains, directory server and bind account, monitoring targets, alert recipients, banner text and certificate authority.
3. An inventory that groups systems by vendor, site and environment.
4. For firmware, a maintenance window, the approved firmware image and the vendor's compatibility matrix.

## Steps

1. Capture each system's current settings with the info modules and store them as the starting baseline.
2. Set time and name resolution:
   - ONTAP `na_ontap_ntp` and `na_ontap_dns`;
   - PowerStore `dellemc.powerstore.ntp` and `dns`;
   - FlashArray `purefa_ntp` and `purefa_dns`, FlashBlade `purefb_ntp` and `purefb_dns`;
   - StorageGRID `na_sg_grid_ntp` and `na_sg_grid_dns`.
3. Configure directory services and roles: ONTAP `na_ontap_ldap` and `na_ontap_ldap_client`, PowerStore `ldap_domain`, PowerScale `dellemc.powerscale.ldap`, FlashArray `purefa_ds` and `purefa_dsrole`.
4. Configure monitoring and alerting:
   - ONTAP `na_ontap_snmp`, `na_ontap_ems_destination` and `na_ontap_autosupport`;
   - PowerStore `snmp_manager` and `smtp_config`;
   - PowerScale `snmp_settings`, `alert_channel` and `alert_rule`;
   - FlashArray `purefa_syslog`, `purefa_smtp` and `purefa_alert`;
   - Storage Virtualize `ibm_sv_manage_syslog_server` and `ibm_svc_manage_callhome`;
   - Infinidat `infini_notification_target` and `infini_notification_rule`.
5. Install certificates and set the login banner: ONTAP `na_ontap_security_certificates`, FlashArray `purefa_certs` and `purefa_banner`, PowerStore `dellemc.powerstore.certificate`, StorageGRID `na_sg_grid_certificate`.
6. Where the collection supports it, upgrade firmware in a controlled workflow, for example ONTAP `na_ontap_software_update` and `na_ontap_firmware_upgrade`. Check cluster health before and after each step and stop on failure.
7. Run the playbook in check mode on a schedule and send the differences from the baseline to the storage team.

## Success Criteria

1. Every storage system reports the baseline NTP, DNS, directory and monitoring settings.
2. Alerts from each system reach the monitoring or ticketing tool, confirmed by a test event.
3. Drift reports are produced on schedule and exceptions are tracked.
4. Firmware levels are within the approved list, and upgrades have before and after health checks.

## Notes

- Some arrays treat these settings as cluster-wide, others per node or per SVM; model that in the variable structure.
- Storage alerts can start Event-Driven Ansible rulebooks, for example to expand a volume or open an incident. See [Gather storage facts and capacity reports](gather-storage-facts-and-capacity-reports.md) for the reporting side.
- For switch and server firmware used with the arrays, see [Update server firmware and BIOS](../infrastructure/update-server-firmware-and-bios.md).
- Pair with [Provision block storage](provision-block-storage.md) once the baseline is in place.
