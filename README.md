# vainu-skills

A collection of [Agent Skills](https://agentskills.io) for working with [Vainu](https://www.vainu.com) MCP tools and Nordic company data. Skills conform to the [agentskills.io](https://agentskills.io) open standard and work with any compatible agent, including Claude Code, GitHub Copilot, Cursor, and others.

## Installation

### Organization skills for Claude

1. Download the `vainu-skills.zip` from the [latest release](../../releases/latest) and unzip it.
2. In Claude desktop navigate to `Organization settings` -> `Skills` (under `Libraries`) -> `+ Add` (under `Organization skills`)
3. Drag and drop all the individual zip files within the "release" zip file into the `Upload skill` dialog.


### Automatic installation for most 'coding' agents:

```bash
npx skills add -g vainuio/vainu-skills --skill '*'
```

### Manual installation

Clone this repository and copy (or symlink) the skills into your agent's skills directory.

#### Claude Code

For personal use across all projects, copy the skills to `~/.claude/skills/`:

```bash
git clone https://github.com/vainuio/vainu-skills.git
cp -r vainu-skills/skills/* ~/.claude/skills/
```

For a single project, copy into `.claude/skills/` at the project root instead.

#### Other agents

| Agent | Default skills path |
|---|---|
| VS Code / GitHub Copilot | `.agents/skills/` |
| Cursor | `.cursor/skills/` |
| Gemini CLI | `.gemini/skills/` |

Point your agent at the `skills/` directory in this repository, or copy its contents into the appropriate path for your tool.

## Skills

| Skill | Description | Key tools |
|---|---|---|
| [event-type-selection](skills/event-type-selection/SKILL.md) | Translate user intent into Vainu event type IDs for signals and lead filtering | `get_event_types_reference` |
| [finnish-purchase-invoice-explorer](skills/finnish-purchase-invoice-explorer/SKILL.md) | Analyse Finnish public-sector B2G purchase invoice data | `b2g_buyer`, `b2g_seller`, `b2g_search_invoices`, `search_companies` |
| [html-report](skills/html-report/SKILL.md) | Generate self-contained, Vainu-branded HTML reports from MCP output | `Write`, `Agent` |
| [organization-field-selection](skills/organization-field-selection/SKILL.md) | Discover company field paths for use in queries and exports | `list_organization_fields` |
| [vainu-query-language](skills/vainu-query-language/SKILL.md) | Build and validate VQL filters for `query_organizations` | `get_query_reference`, `search_filter_values`, `validate_query`, `query_organizations` |

## How skills work

Each skill is a directory containing a `SKILL.md` file with YAML frontmatter and markdown instructions. Agents load only the `name` and `description` at startup; the full instructions load only when a task matches the skill. Supporting reference files (examples, lookup tables, stylesheets) live alongside `SKILL.md` in the same directory.

Skills follow this frontmatter format:

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
