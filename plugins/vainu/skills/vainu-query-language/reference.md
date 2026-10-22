# VQL operator and syntax reference

Quick reference for VQL operators, nesting, and allowed values. For full context and examples see SKILL.md.

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
- **?MATCH** — `{"embedded_field_name": <operation>}`. The field must be an array; at least one element must match. Use for contacts, prospect_addresses, vainu_custom_industry, organization_size_indicators.

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

`prospect_addresses.types` values: `registry_main_location` (official main/HQ), `registry_other_location` (official registered branches), `other` (non-registry addresses from websites/other sources).

## Allowed values

### Field names

Use the `list_organization_fields` tool to discover valid field paths. See the organization-field-selection skill for workflow. For company name use path "name" (not "company_name").

### Enum-like and coded values

Use the `search_filter_values` tool to look up valid values for industry_codes_local (value_type="industries"), vainu_custom_industry.fact_vid (value_type="vainu_custom_industry"), legal_entity (value_type="legal_entity"; FI: locale en/sv/fi; other countries: English from FORM_OF_COMPANY), and address-related fields (value_type="address"; FI/SE/DK/NO; optional address_category). CRM filtering can use `prospectexport.target` with `Dynamics`, `HubSpot`, `Pipedrive`, `Salesforcev3`, and owner filtering can use `prospectexport.owner_email` (typically via `?STARTSWITH`; prefer combining with `prospectexport.target`). Example allowed values for common fields: titles.classifications.functional_area (CEO, Finance, HR, …), size_classes (small, medium, large, enterprise), visiting_region (e.g. FI-04, FI-11), legal_entity (jurisdiction-specific).
