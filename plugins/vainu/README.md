# Vainu

Nordic company data for your AI agent. This plugin bundles the Vainu MCP connector with the
skills that teach the agent when and how to use its tools, so you can ask about companies in
Finland, Sweden, Norway and Denmark in plain language.

## Install

In Claude Code:

```
/plugin install vainu --marketplace vainu-app/vainu-plugins
```

For claude.ai, Codex and other agents, see the [repository README](../../README.md).

## Skills

- **vainu-query-language**: build and validate VQL filters for company searches.
- **organization-field-selection**: find the right company field paths for queries and exports.
- **event-type-selection**: pick the event type IDs behind signals and lead filters.
- **finnish-purchase-invoice-explorer**: analyse Finnish public-sector purchase invoices, who
  buys from whom and for how much.
- **html-report**: turn the results into a self-contained, Vainu-styled HTML report.

## Use it

1. Connect the Vainu connector. In claude.ai and Cowork it is on the plugin's Connectors tab; in
   Claude Code run `/mcp`; in Codex run `codex mcp login vainu`. You sign in with your own Vainu
   account, and the plugin never stores credentials.
2. Ask in plain language, for example "Find Finnish software companies with over 50 employees
   that opened a new office this year". The agent picks the matching skill on its own.
3. To call a skill directly, type `/vainu:` followed by the skill name, such as
   `/vainu:vainu-query-language`. The `html-report` skill has no slash command; the agent applies
   it on its own when you ask for a report.

## Data

Your queries, company names, business IDs and list IDs are sent to `https://mcp.vainu.ai/mcp`
under your own Vainu account. Nothing is sent anywhere else, and the plugin stores nothing
itself. HTML reports are written to a file on your own machine, by default under `~/Desktop` or
at the path you give; nothing is uploaded.
