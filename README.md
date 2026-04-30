# vainu-skills

A collection of Claude Code skills for working with [Vainu](https://www.vainu.com) MCP tools and Nordic company data.

## Skills

| Skill | Description | Key tools |
|---|---|---|
| [event-type-selection](skills/event-type-selection/SKILL.md) | Translate user intent into Vainu event type IDs for signals and lead filtering | `get_event_types_reference` |
| [finnish-purchase-invoice-explorer](skills/finnish-purchase-invoice-explorer/SKILL.md) | Analyse Finnish public-sector B2G purchase invoice data | `b2g_buyer`, `b2g_seller`, `b2g_search_invoices`, `search_companies` |
| [html-report](skills/html-report/SKILL.md) | Generate self-contained, Vainu-branded HTML reports from MCP output | `Write`, `Agent` |
| [organization-field-selection](skills/organization-field-selection/SKILL.md) | Discover company field paths for use in queries and exports | `list_organization_fields` |
| [vainu-query-language](skills/vainu-query-language/SKILL.md) | Build and validate VQL filters for `query_organizations` | `get_query_reference`, `search_filter_values`, `validate_query`, `query_organizations` |

## How skills work

Each skill is a markdown file (`SKILL.md`) that instructs Claude how and when to use Vainu's MCP tools. Claude Code loads skills automatically as conversation context. Supporting reference files (examples, lookup tables, stylesheets) live alongside `SKILL.md` in the same directory.

Skills follow a standard frontmatter format:

```yaml
---
name: skill-name
description: When and why to invoke this skill.
allowed-tools: mcp__claude_ai_Vainu__some_tool Read Write
---
```

## Directory layout

```
skills/
  event-type-selection/           SKILL.md + event-types-reference.md
  finnish-purchase-invoice-explorer/  SKILL.md
  html-report/                    SKILL.md + assets/vainu-report.css
  organization-field-selection/   SKILL.md + organization-fields-reference.md
  vainu-query-language/           SKILL.md + reference.md + examples.md
```

## Adding a skill

1. Create `skills/<name>/SKILL.md` with the required frontmatter (`name`, `description`, `allowed-tools`).
2. Add supporting reference files (`.md`, assets) in the same directory as needed.
3. Follow the section structure used by existing skills: **When to use**, **Workflow**, **Output format**.
