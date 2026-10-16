# VQL examples

Example VQL queries. Use with the Vainu MCP tools: validate_query, query_organizations. See SKILL.md for syntax and workflow.

### 1. Simple ?ALL with ?IN and ?RANGE

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

Helsinki addresses from official main registry location only.

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

### 11. Filter by business IDs

```json
{"?ALL": [{"?IN": {"business_id": ["FI12345678", "FI87654321"]}}]}
```

### 12. Include/exclude by connected CRM target

```json
{"?ALL": [{"?EQ": {"prospectexport.target": "HubSpot"}}]}
```

```json
{"?ALL": [{"?NOT": {"?EQ": {"prospectexport.target": "HubSpot"}}}]}
```

### 13. Filter by CRM owner email

```json
{
  "?ALL": [
    {"?EQ": {"prospectexport.target": "HubSpot"}},
    {"?STARTSWITH": {"prospectexport.owner_email": ["test@example.com"]}}
  ]
}
```
