---
title: Build and validate VPN tunnels
summary: Create site-to-site VPN tunnels between on-premises devices and cloud gateways and verify that they are up.
order: 150
personas: [Network engineer, Cloud network engineer]
collections: [network.vpn, ansible.netcommon]
key_content:
  - network.vpn.deploy
  - network.vpn.validate
  - network.vpn.azure_rm_localnetworkgateway
  - network.vpn.azure_rm_virtualnetworkgatewayconnection
  - ansible.netcommon.net_ping
examples:
  - title: network.vpn validated collection
    url: https://github.com/redhat-cop/network.vpn
    note: build, maintain and validate VPN tunnels across cloud providers and network appliances
---

# Build and validate VPN tunnels

## Description

Connect a data center or branch to a cloud network with an IPsec VPN, and prove that it works. Both ends of the tunnel are configured from the same data, so peer addresses, pre-shared keys and routes cannot drift apart.

## Notes

- Check the collection documentation for the providers and appliances supported by each role.
- Related: [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
- Pair with Event-Driven Ansible to re-run validation, or open a ticket, when a tunnel-down alert arrives from monitoring.
