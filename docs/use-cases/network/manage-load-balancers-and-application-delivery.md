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

## Notes

- Create the DNS name and address first with [Manage DNS, DHCP and IPAM](manage-dns-dhcp-and-ipam.md).
- `f5networks.f5_eda_security` provides Event-Driven Ansible playbooks that react to security events on BIG-IP, for example blocking IP addresses in an ASM policy.
- BIG-IP software and UCS archives are handled with `f5networks.f5_bigip.bigip_software_install` and `f5networks.f5_modules.bigip_ucs`.
