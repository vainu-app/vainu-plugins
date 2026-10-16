---
name: organization-field-selection
description: Discover and choose company (organization) field paths for queries and context. Use when building query_organizations or get_company_context and you need valid field names. Selection uses the path (api.v3.path) from list_organization_fields; filter by category, search, or availability.
allowed-tools: list_organization_fields
---

# Organization Field Selection

## When to use

Use this skill when you need to:

- Discover which company fields exist and their metadata
- Choose fields for `query_organizations` or `get_company_context`
- Map user intent (e.g. "company name and turnover", "contact info", "financials") to field paths
- Restrict to filterable fields (for VQL) or to specific countries

## Data model

- **path**: The api.v3.path string. **Use this value** in the `fields` parameter of `query_organizations` and `get_company_context`; also use for filter field names in VQL. Do not invent paths.
- **type**: Field data type from the API.
- **description**: Human-readable description of the field.
- **main_category**: Semantic group (e.g. `basic`, `financials`). Use to narrow the list.
- **sub_category**: Finer grouping (e.g. `main_location`, `identification`).
- **countries**: List of country codes where the field is available (e.g. `FI`, `SE`, `NO`, `DK`).
- **application_availability**: Where the field can be used: `"export"`, `"profile"`, `"connector"`, **`"filter"`** (field can be used in VQL query filters). Use `filterable_only=True` in `list_organization_fields` when building filters.
- **requires_permission**: If set, the current user must have at least one of these permissions; the tool returns only allowed fields.

## Selection workflow

1. **Understand intent**: From the user prompt or context, identify which kinds of company data are needed (name, financials, location, contacts, industry, etc.).
2. **Call list_organization_fields**: Use the tool with optional filters:
   - **search**: Free-text match on description and translated labels.
   - **main_category** / **sub_category**: Narrow by category (e.g. `basic`, `financials`, `main_location`, `identification`).
   - **countries**: Restrict to fields available in the relevant databases (e.g. `["FI", "SE"]`).
   - **application_availability**: e.g. `["filter"]` for fields usable in VQL filters.
   - **filterable_only**: Set to `true` when you need field paths for query filters.
3. **Pick path values**: From the returned list, collect the **path** values you need. Use exactly those strings in `fields` or in VQL filter keys.
4. **Company name**: Use path **`"name"`** for company name (not `"company_name"`).

## Output format

- When passing fields to tools, use **path strings only** (e.g. `["name", "business_id", "facts_numeric.turn_over_c"]`).
- The `fields` parameter expects `list[str]` of api.v3.path values.

## Source of truth

- Field metadata comes from **list_organization_fields** (backed by GET `/api/v3/organizations_fields/?api_versions=v3`). Only fields the user is allowed to access are returned.
- For a short reference of categories and common paths, see [organization-fields-reference.md](organization-fields-reference.md).
