# Grouping guide: from modules to product use cases

Collections often have hundreds of modules that are create/update/delete/info on different resources of one product. `scripts/resource_index.py` already merges each resource's modules (create/update/delete + `_info`) into one **resource key**. The second step, described here, groups related resources into a small number of outcome-level **use cases** that a customer would recognise. The document then reads "Manage virtual networks and connectivity — components: virtual networks, subnets, peering, NAT gateways…" instead of 40 module rows.

Finished examples: `data/groups/azure.azcollection.yml`, `data/groups/cisco.ios.yml`, `data/groups/fortinet.fortios.yml`. Read at least one before starting.

## Input

```bash
python3 scripts/resource_index.py <fqcn> --print
```

Each line is `<resource_key> [manage|info|manage+info] <description>` for modules, and `(<type>) <name> <description>` for roles, playbooks and plugins.

## Output: `data/groups/<fqcn>.yml`

```yaml
fqcn: azure.azcollection
product: Microsoft Azure          # product/platform name as customers say it
notes:                            # optional, 0-2 short collection-level notes
  - ...
use_cases:
  - title: Manage virtual machines and images     # short verb phrase, customer outcome
    description: Create, resize, start, stop and delete VMs, including extensions, sizes and images.
    note: optional one-line note specific to this use case
    components:                   # resource key -> short friendly label
      virtualmachine: Virtual machines
      virtualmachineextension: VM extensions
```

(`prerequisites` and `success` fields are no longer used; omit them.)

## Rules

1. **Complete and exclusive.** Every resource key, and every role/playbook/plugin as `<type>:<name>` (for example `role:backup`, `playbook:ilab`, `inventory:azure_rm`, `eda_event_source:webhook`), appears in exactly one use case. Copy keys exactly.
2. **Number of use cases** by the collection's entry count N: N ≤ 3 → 1; 4–8 → 1–2; 9–20 → 2–4; 21–60 → 4–8; 61–200 → 6–15; 201–500 → 12–25; > 500 → 18–35.
3. **Group by customer outcome**, not alphabetically: for example "Manage firewall policy and objects", "Configure routing (BGP, OSPF, static)", "Administer the device: users, certificates, firmware", "Gather facts and inventory". For very large API-generated collections (Catalyst Center, DNA Center, FortiManager, Meraki, NetScaler), use the first token(s) of the key as a starting point, then merge small families and split oversized ones by function.
4. **Roles and playbooks** are often already outcomes; give them their own use case when they form a clear workflow (for example validated roles), otherwise put them with the resources they act on. Plugins (inventory, lookup, filter, connection, EDA sources) usually belong in an "Inventory, lookups and integrations" or similar use case, or with the function they serve.
5. **Labels** are short plural nouns ("Network security groups", "BGP", "Static routes"). Don't repeat the product name in every label.
6. **Descriptions** come from the module descriptions: one sentence, what the customer can do. Never invent features the modules don't cover. English, concise, no marketing.
7. Deprecated modules are already excluded from the index.

## Check

```bash
python3 scripts/check_groups.py <fqcn> [<fqcn> ...]      # must print OK for each
```
