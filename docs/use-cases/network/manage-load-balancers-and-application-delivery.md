---
title: Manage load balancers and application delivery
summary: Create virtual servers, pools and members on F5 BIG-IP, NetScaler and Avi from application requests.
order: 130
personas: [Network engineer, Application delivery engineer, Operations lead]
collections: [f5networks.f5_modules, f5networks.f5_bigip, f5networks.f5_eda_security, netscaler.adc, vmware.alb]
key_content:
  - f5networks.f5_modules.bigip_virtual_server
  - f5networks.f5_modules.bigip_pool
  - f5networks.f5_modules.bigip_pool_member
  - f5networks.f5_bigip.bigip_as3_deploy
  - netscaler.adc.lbvserver
  - netscaler.adc.servicegroup
  - vmware.alb.avi_virtualservice
---

# Manage load balancers and application delivery

## Description

Publish an application behind a load balancer from a request, rather than a manual change on the appliance. Automation creates the pools, members, health monitors and virtual servers consistently, and takes servers in and out of rotation during maintenance.

## Prerequisites

1. Management access to the load balancer or its controller with an automation account.
2. Application details: virtual IP, port, backend servers, health monitor, TLS certificate.
3. A configuration backup or device snapshot process for the appliance.
4. Change approval for production virtual servers.

## Steps

1. Capture the application request as variables: name, virtual IP, members and monitor.
2. Create the building blocks. On BIG-IP use `f5networks.f5_modules.bigip_pool` and `f5networks.f5_modules.bigip_pool_member`, then `f5networks.f5_modules.bigip_virtual_server`. For declarative deployments send an AS3 declaration with `f5networks.f5_bigip.bigip_as3_deploy`.
3. On NetScaler use `netscaler.adc.servicegroup` and `netscaler.adc.lbvserver`, and on Avi use `vmware.alb.avi_virtualservice`.
4. Verify that the virtual server is available and the members are healthy, using the device info modules or a request to the virtual IP.
5. For maintenance, run a job that disables the pool member, waits, runs the application change and enables it again.
6. Save the appliance configuration after the change.

## Success Criteria

1. The application is reachable through the virtual IP and all members show healthy.
2. The same request run twice makes no extra changes.
3. A member can be drained and restored by a job without a change on the appliance console.
4. Configuration backups exist from before and after the change.

## Notes

- Create the DNS name and address first with [Manage DNS, DHCP and IPAM](manage-dns-dhcp-and-ipam.md).
- `f5networks.f5_eda_security` provides Event-Driven Ansible playbooks that react to security events on BIG-IP, for example blocking IP addresses in an ASM policy.
- BIG-IP software and UCS archives are handled with `f5networks.f5_bigip.bigip_software_install` and `f5networks.f5_modules.bigip_ucs`.
