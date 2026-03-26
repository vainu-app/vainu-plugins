# Organization fields reference

Canonical list: **list_organization_fields** (data from `/api/v3/organizations_fields/?api_versions=v3`).  
Use the returned **path** (api.v3.path) in `fields` for `query_organizations` and `get_company_context`, and for VQL filter keys.

## Categories at a glance

Use these with `list_organization_fields(main_category=..., sub_category=...)` to narrow results. Exact values come from the API; below are examples from the tool descriptions.

| main_category | sub_category (examples) | Typical use |
|---------------|--------------------------|-------------|
| basic         | identification, …        | Core company identifiers, name, business_id, status |
| financials   | —                        | Turnover, staff number, financial statement fields |
| main_location| —                        | Address, region, postal code, city |

Call **list_organization_fields** without category filters to see all available main_category and sub_category values for your user.

## Common paths

- **Company name**: `name` (do not use `company_name`)
- **Business ID**: `business_id`
- **Filterable fields**: Use `list_organization_fields(filterable_only=True)` to get only fields that can be used in VQL filters.

## application_availability

- **export**, **profile**, **connector**: Field is available in those contexts.
- **filter**: Field can be used in VQL query filters. Use `filterable_only=True` to restrict to these.
