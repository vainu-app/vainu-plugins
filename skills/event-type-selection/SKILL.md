---
name: event-type-selection
description: Pick relevant event type tags from the canonical list for company context. Use when selecting event types for prompts, refining event filters, or matching user intent to event IDs. Filtering uses numeric IDs; each event has label, category, and databases (countries) where it applies.
allowed-tools: get_event_types_reference Read
---

# Event Type Selection

## When to use

Use this skill when you need to:

- Select relevant event types from the canonical list for a user query or prompt
- Map user intent (e.g. "companies that got funding", "CEO changes") to event type IDs
- Restrict event types by country
- Understand event categories and which databases support each event

## Data model

- **ID**: Numeric identifier. **Filtering and selection use this value**; always return or filter by ID.
- **Label**: Human-readable event name.
- **Category**: Semantic group (e.g. `finance`, `staff`, `major`, `technology`, `public`).
- **Databases**: List of country/database codes where the event is available (e.g. `FI`, `SE`, `NO`, `DK`, `NL`, `US`, `GB`, `FR`, `FI_realestate`). Empty list means the event is not restricted to specific databases in the source data.

## Selection workflow

1. **Understand intent**: From the user prompt or context, identify which kinds of events are needed (funding, staff changes, technology adoption, etc.).
2. **Match to categories**: Map that intent to one or more categories (finance, staff, major, technology, public, marketing, basic_data, other, normal, negative).
3. **Choose event types**: From the [event types reference](event-types-reference.md), pick event type **IDs** whose labels and categories match. Use the deeper descriptions to confirm relevance.
4. **Respect database scope**: If the query is limited to a country (e.g. `FI`, `NO`), only include event types whose `databases` list contains that country or is empty (when empty, treat as available everywhere in your context).

## Output format

- When returning selected events, use **numeric IDs only** (e.g. `[43543, 8000038, 8000050]`).
- The codebase expects `event_type_ids: list[int]` (the `id` field on each `EventTypeRow`);

## Source of truth

- The canonical list for this MCP service is `vainu.data.mcp.event_types_data.EVENT_TYPES_DATA` (`EventTypeRow` rows)
- For detailed meanings and use cases, see [event-types-reference.md](event-types-reference.md).

## Categories at a glance

| Category     | Typical use |
|-------------|-------------|
| finance     | Funding, turnover, bankruptcy, financial statements, earnings, layoffs, credit |
| staff       | CEO/board changes, key person appointment/departure, open positions, personnel changes |
| major       | M&A, IPO, internationalization, strategy, investments, new company, construction |
| technology  | New tools/platforms (CMS, ATS, CRM, analytics, etc.) |
| public      | Licenses, permits, patents, trademarks, government notices, minutes |
| marketing   | Domain registration, events |
| basic_data  | Company form, name, status, auxiliary name |
| normal      | Contracts, partnerships, products, relocation, real estate, stock trade |
| other       | Awards, vehicles, energy certificate, protest list, EIA, etc. |
| negative    | Legal dispute |
