---
name: vainu-query-language
description: Build and understand VQL (Vainu Query Language) queries for organization search via the Vainu MCP tools.
allowed-tools: get_query_reference search_filter_values validate_query query_organizations list_organization_fields get_user_lists get_user_list
---

# Vainu Query Language (VQL) Reference

## Syntax rules

- **Top-level structure**: Queries use a single `?ALL` at the root wrapping an array of conditions (AND semantics).
- **Operator prefix**: Every operator key is prefixed with `?` (e.g. `?EQ`, `?IN`, `?RANGE`).
- **Single key per object**: Each operator object has exactly one key (the operator name). The value is `{ "field_name": value }` for field operators or a nested operation for logical operators.
- **JSON format**: Field operators: `{"?OPERATOR": {"field_name": value}}`. Logical: `{"?ALL": [{...}, {...}]}` or `{"?ANY": [{...}, {...}]}`.

## Operators

### Logical / structural

- **?ALL** — Array of operations. All must match (AND). Used at root.
- **?ANY** — Array of operations. At least one must match (OR).
- **?NOT** — Single operation. Matches if that operation does NOT match.
- **?MATCH** — `{"embedded_field_name": <operation>}`. The field must be an array; at least one element must match. Use for contacts, prospect_addresses, vainu_custom_industry, organization_size_indicators, leads.

### Field comparison

- **?EQ** — `{"field": value}`. Equality.
- **?IN** — `{"field": [value1, value2, ...]}`. At least one value must match.
- **?GT / ?GTE / ?LT / ?LTE** — `{"field": value}`. Numeric or date comparison.
- **?RANGE** — `{"field": [low, high]}`. Closed interval. Use `null` for open-ended: `[min, null]` or `[null, max]`.
- **?IEXACT** — Case-insensitive equality.
- **?YEAR** — `{"field": year_number}`. Field's year equals given year.

### Text / list-of-strings

- **?STARTSWITH** — `{"field": ["prefix1", "prefix2"]}`. Must start with one of the strings.
- **?CONTAINS** — `{"field": ["substring1", "substring2"]}`. Must contain one of the strings.
- **?ICONTAINS** — Case-insensitive CONTAINS.
- **?ENDSWITH** — `{"field": ["suffix1", ...]}`. Must end with one of the strings.

### Presence

- **?EXISTS** — `{"field": true}` or `{"field": false}`. Checks presence/absence.
- **?ISNULL** — Field is null/absent.

### Geo

- **?GEO_WITHIN** — Polygon: `{"field": [[lat, lng], ...]}`.
- **?GEO_WITHIN_BOX** — Bounding box: `{"field": [[lat1, lng1], [lat2, lng2]]}`.
- **?GEO_WITHIN_SPHERE** — Center + radius: `{"field": {"#coordinates": [lat, lng], "#radius": number}}`.

## Nesting rules

1. **Root**: One `?ALL` containing an array of conditions.
2. **?MATCH**: Value is exactly one key (the array field name) whose value is one operation. That operation is usually `?ALL` or `?ANY` on subdocument fields.
3. **?NOT**: Wraps exactly one operation. Use `?ALL` inside if you need multiple negated conditions.
4. **?RANGE**: Always a two-element array `[low, high]`. Use `null` for open end.
5. **Dot notation**: Use dots for nested fields (e.g. `facts_numeric.staff_number`). Only the top-level array is named in `?MATCH`, then use dotted paths inside.

## Common embedded fields for ?MATCH

| Field | Typical inner conditions |
|-------|--------------------------|
| contacts | titles.classifications.functional_area, titles.classifications.is_decision_maker, EXISTS email/phone |
| prospect_addresses | visiting_region, visiting_postal, visiting_city, types |
| vainu_custom_industry | fact_vid (?EQ) AND (confidence_score (?RANGE) OR confidence_class (?EQ)) |
| organization_size_indicators | size_classes (?IN), indicator_type (?EQ) |
| leads | vainu_date (**always** ?GTE/?LTE/?RANGE for performance), content (?ICONTAINS), tags (?IN), title (?CONTAINS) |

### leads (signals / events)

Filter companies where at least one lead/event matches conditions. Use `?MATCH` on `leads` with inner conditions.

**Important:** Always include a **timeframe** on `leads.vainu_date` (e.g. `?GTE`, `?LTE`, or `?RANGE`) to make the database query faster.

| Field | Type | Description |
|-------|------|-------------|
| leads.content | str | Lead/event content (text). Use ?CONTAINS / ?ICONTAINS. |
| leads.link | str | Link URL. |
| leads.title | str | Lead/event title. Use ?CONTAINS / ?ICONTAINS. |
| leads.vainu_date | datetime or "n months ago" | When the event happened. **Always filter by this** (e.g. ?GTE, ?LTE, ?RANGE) for performance. |
| leads.tags | list of IDs | Event type IDs. Get valid IDs from `get_event_types_reference` or the event-type-selection skill. Use ?IN. |

Searching in both title and content (match if either contains the text). Use inside `?MATCH.leads`; field names are `title` and `content`:

```json
{"?ANY": [
  {"?CONTAINS": {"title": "look for this in title"}},
  {"?CONTAINS": {"content": "look for this in content"}}
]}
```

### prospect_addresses.types values

When filtering by `prospect_addresses`, combine location fields (`visiting_city`, `visiting_region`, etc.) with `types` to target the right source/type of address:

- `registry_main_location`: Official main registered location (often HQ).
- `registry_other_location`: Other official registered branch locations.
- `other`: Non-registry addresses discovered from websites/other sources.

## Allowed values

### Field names

Use the `list_organization_fields` tool to discover valid field paths (use the returned "path" / api.v3.path in "fields" lists). See the organization-field-selection skill for workflow. Do not invent field names. For company name use path "name" (not "company_name").

### Enum-like and coded values

Use the `search_filter_values` tool to look up valid values for:
- **industry_codes_local**: Country-specific industry codes (e.g. "62", "63", "J"). Search with value_type="industries".
- **vainu_custom_industry.fact_vid**: Custom industry taxonomy IDs. Search with value_type="vainu_custom_industry".
- **legal_entity** (form_of_company): Jurisdiction-specific legal form codes (e.g. "OY", "AB"). Search with value_type="legal_entity". For FI use locale en/sv/fi (better labels); other countries use English from FORM_OF_COMPANY.
- **visiting_city**, **visiting_municipality**, **visiting_postal**, **visiting_region**: value_type="address" with country FI/SE/DK/NO; optional address_category cities, municipalities, postal_codes, or regions.
- **prospectexport.target**: CRM export target values when CRM integration is connected: `Dynamics`, `HubSpot`, `Pipedrive`, `Salesforcev3`.
- **prospectexport.owner_email**: CRM owner email attached to exported company records (string; typically filtered with `?STARTSWITH`). Prefer combining with `prospectexport.target`.

Example allowed values (verify via search_filter_values):

| Field | Example values |
|-------|----------------|
| titles.classifications.functional_area | CEO, Finance, HR, Technology, Operations, Strategy, Board, Administration, Logistics, Ecommerce, Entrepreneur |
| titles.classifications.is_decision_maker | true, false |
| organization_size_indicators.size_classes | small, medium, large, enterprise |
| organization_size_indicators.indicator_type | company_size_indicator_model |
| industry_codes_local | Country-specific codes (e.g. "62", "63", "J", "851") |
| visiting_region | Region codes (e.g. "FI-04", "FI-11") |
| legal_entity | Jurisdiction-specific (e.g. "Osakeyhtiö") |
| prospectexport.target | Dynamics, HubSpot, Pipedrive, Salesforcev3 |
| prospectexport.owner_email | e.g. test@example.com |

## Workflow

1. Call `get_query_reference` (or read this skill) to understand VQL syntax.
2. Call `search_filter_values` to find valid codes/IDs for industry, custom industry, legal_entity, technology, and address fields (value_type="address") as needed.
3. Construct the VQL JSON query using the syntax and values.
4. Call `validate_query` to check the query is valid.
5. Call `query_organizations` with the validated query to get results.

## Common Formatting Pitfalls (CRITICAL)

When passing the query to `query_organizations` or `validate_query`, the payload must be a standard JSON object.
- **DO NOT** stringify the object before passing it to the tool.
- **DO NOT** escape the quotation marks around the keys.
- The server will reject keys containing literal quotes (e.g., `Invalid op_name: "?ALL"`).

**RIGHT (Standard JSON keys):**
```json
{
  "?ALL": [
    { "?IN": { "visiting_city": ["Turku"] } }
  ]
}
```

## Examples

### 1. Simple ?ALL with ?IN and ?RANGE

Industry codes, staff range, and turnover range (all must match).

```json
{
  "?ALL": [
    {"?IN": {"industry_codes_local": ["62", "63"]}},
    {"?RANGE": {"facts_numeric.staff_number": [10, 50]}},
    {"?RANGE": {"turn_over_local_c": [500000, 4000000]}}
  ]
}
```

### 2. Including or Excluding a target group (user list)

You can query companies that belong to a specific user list (target group) using its list ID. You can find list IDs using the `get_user_lists` or `get_user_list` tools.

Include companies from a specific target group:
```json
{
  "?ALL": [
    {"?EQ": {"target_group._id": "69c39e7f4df2cfa1b2d02765"}}
  ]
}
```

Exclude a target group with `?NOT ?IN`:
```json
{
  "?ALL": [
    {"?IN": {"industry_codes_local": ["62"]}},
    {"?RANGE": {"turn_over_local_c": [500000, 4000000]}},
    {"?NOT": {"?IN": {"target_group._id": ["<target_group_id>"]}}}
  ]
}
```

### 3. ?MATCH on contacts

At least one contact: functional area, decision maker, has email or phone.

```json
{
  "?ALL": [
    {
      "?MATCH": {
        "contacts": {
          "?ALL": [
            {"?IN": {"titles.classifications.functional_area": ["CEO", "Finance"]}},
            {"?EQ": {"titles.classifications.is_decision_maker": true}},
            {"?ANY": [
              {"?EXISTS": {"email": true}},
              {"?EXISTS": {"phone": true}}
            ]}
          ]
        }
      }
    }
  ]
}
```

### 4. ?MATCH on prospect_addresses

Companies with a Helsinki address that is specifically the official main registry location.

```json
{
  "?ALL": [
    {
      "?MATCH": {
        "prospect_addresses": {
          "?ALL": [
            {"?IN": {"visiting_city": ["Helsinki"]}},
            {"?IN": {"types": ["registry_main_location"]}}
          ]
        }
      }
    }
  ]
}
```

### 5. ?MATCH on vainu_custom_industry

Custom industry filtering must combine `fact_vid` with either `confidence_score` or `confidence_class` (where 1 = high confidence).

```json
{
  "?ALL": [
    {
      "?ANY": [
        {
          "?MATCH": {
            "vainu_custom_industry": {
              "?ALL": [
                {"?EQ": {"fact_vid": 9572932}},
                {"?RANGE": {"confidence_score": [0.3, 1]}}
              ]
            }
          }
        },
        {
          "?MATCH": {
            "vainu_custom_industry": {
              "?ALL": [
                {"?EQ": {"fact_vid": 9573091}},
                {"?EQ": {"confidence_class": 1}}
              ]
            }
          }
        }
      ]
    }
  ]
}
```

### 6. ?MATCH on organization_size_indicators

Company size classes.

```json
{
  "?ALL": [
    {
      "?MATCH": {
        "organization_size_indicators": {
          "?ALL": [
            {"?IN": {"size_classes": ["small", "medium"]}},
            {"?EQ": {"indicator_type": "company_size_indicator_model"}}
          ]
        }
      }
    }
  ]
}
```

### 7. ?STARTSWITH and ?CONTAINS

```json
{
  "?ALL": [
    {"?STARTSWITH": {"company_keywords": ["medicin", "pharma"]}},
    {"?STARTSWITH": {"urls_keywords": ["health"]}}
  ]
}
```

```json
{"?ALL": [{"?CONTAINS": {"company_name_l": ["nokia"]}}]}
```

### 8. ?ANY of multiple ?MATCH (custom industries)

Either custom industry A or B.

```json
{
  "?ALL": [
    {
      "?ANY": [
        {
          "?MATCH": {
            "vainu_custom_industry": {
              "?ALL": [
                {"?EQ": {"fact_vid": 9572932}},
                {"?EQ": {"confidence_class": 1}}
              ]
            }
          }
        },
        {
          "?MATCH": {
            "vainu_custom_industry": {
              "?ALL": [
                {"?EQ": {"fact_vid": 9573018}},
                {"?EQ": {"confidence_class": 1}}
              ]
            }
          }
        }
      ]
    }
  ]
}
```

### 9. Open-ended ?RANGE

Use `null` for one-sided bounds.

```json
{"?ALL": [{"?RANGE": {"turn_over_c": [500000, null]}}, {"?RANGE": {"staff_number_c": [10, null]}}]}
```

```json
{"?ALL": [{"?RANGE": {"turn_over_c": [null, 1000000]}}]}
```

### 10. Combined: industry, turnover, address, and contact

```json
{
  "?ALL": [
    {"?IN": {"industry_codes_local": ["62", "63"]}},
    {"?RANGE": {"turn_over_c": [500000, 4000000]}},
    {
      "?MATCH": {
        "prospect_addresses": {
          "?ALL": [{"?IN": {"visiting_region": ["FI-04"]}}]
        }
      }
    },
    {
      "?MATCH": {
        "contacts": {
          "?ALL": [{"?EXISTS": {"email": true}}]
        }
      }
    }
  ]
}
```

### 11. Filter by business IDs (e.g. from document_search)

Restrict results to a known list of companies. Use the same **country** as the business_id prefix when calling `query_organizations` (e.g. `"FI"` for Finnish IDs).

```json
{"?ALL": [{"?IN": {"business_id": ["FI12345678", "FI87654321"]}}]}
```

### 12. Include/exclude companies by connected CRM target

Include only companies already in HubSpot:

```json
{"?ALL": [{"?EQ": {"prospectexport.target": "HubSpot"}}]}
```

Exclude companies already in HubSpot:

```json
{"?ALL": [{"?NOT": {"?EQ": {"prospectexport.target": "HubSpot"}}}]}
```

### 13. Filter by CRM owner email

Limit results to companies owned by a specific CRM owner email. Prefer combining owner filter with CRM target.

```json
{
  "?ALL": [
    {"?EQ": {"prospectexport.target": "HubSpot"}},
    {"?STARTSWITH": {"prospectexport.owner_email": ["test@example.com"]}}
  ]
}
```

### 14. ?MATCH on leads (signals/events) — timeframe required

Filter companies where some lead/event happened in a timeframe and matches content and event type. **Always include a timeframe** on `leads.vainu_date` (e.g. `?GTE`, `?LTE`, or `?RANGE`) to keep the query fast. Event type IDs come from `get_event_types_reference` or the event-type-selection skill.

```json
{
  "?ALL": [
    {
      "?MATCH": {
        "leads": {
          "?ALL": [
            {"?GTE": {"vainu_date": "2026-11-01"}},
            {"?ICONTAINS": {"content": ["Expansion"]}},
            {"?IN": {"tags": ["77883"]}}
          ]
        }
      }
    }
  ]
}
```

### 15. Search leads by title OR content (?ANY)

Match companies that have at least one lead where either the title or the content contains the text (use inside `?MATCH` on `leads`).

```json
{
  "?ALL": [
    {
      "?MATCH": {
        "leads": {
          "?ALL": [
            {"?GTE": {"vainu_date": "2025-01-01"}},
            {
              "?ANY": [
                {"?CONTAINS": {"title": "look for this in title"}},
                {"?CONTAINS": {"content": "look for this in content"}}
              ]
            }
          ]
        }
      }
    }
  ]
}
```
