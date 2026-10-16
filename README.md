# vainu-plugins

Plugins that bring [Vainu](https://www.vainu.com) company data into AI agents. Each plugin
bundles the Vainu MCP connector with the [Agent Skills](https://agentskills.io) that teach the
agent when and how to use it.

## Install

| Agent | How |
|---|---|
| claude.ai, Claude desktop, Cowork | **Customize > Plugins > Add > Add marketplace**, enter `vainu-app/vainu-plugins`, add **vainu**, then connect the Vainu connector on the plugin's **Connectors** tab |
| Claude Code | `/plugin install vainu --marketplace vainu-app/vainu-plugins` (or `/plugin marketplace add vainu-app/vainu-plugins` then `/plugin install vainu@vainu-plugins`) |
| Codex CLI and ChatGPT desktop | `codex plugin marketplace add vainu-app/vainu-plugins` then `codex plugin add vainu@vainu-plugins`, then `codex mcp login vainu`; or pick it in the desktop Plugins directory |
| GitHub Copilot CLI | `copilot plugin marketplace add vainu-app/vainu-plugins` then `copilot plugin install vainu@vainu-plugins` |
| Cursor | **Customize > From GitHub Repository**, enter the repository URL, install **vainu** |
| Any agent, skills only | `npx skills add vainu-app/vainu-plugins --skill '*'` or `gh skill install vainu-app/vainu-plugins --all` |
| Manual | download `vainu.zip` from the [latest release](../../releases/latest); on claude.ai use **Customize > Plugins > Add > Upload plugin** |

Notes:

- A plugin added on claude.ai is saved to your account and also appears in Cowork and Claude
  Code. A plugin installed from the Claude Code or Codex command line stays on that machine.
- The Copilot and Cursor rows are written from those vendors' documentation and have not yet
  been verified by us.
- Codex plugins do not load in the Codex IDE extension and are undocumented for Codex cloud.
  Use the skills-only row there.
- Signing in to the Vainu connector uses your own Vainu account over OAuth. The plugin stores
  no credentials.

## Plugins

| Plugin | Skills | Details |
|---|---|---|
| `vainu` | `vainu-query-language`, `organization-field-selection`, `event-type-selection`, `finnish-purchase-invoice-explorer`, `html-report` | [plugins/vainu/README.md](plugins/vainu/README.md) |

Four skills can be called directly as `/vainu:<skill-name>`; `html-report` has no slash command
and is applied automatically when you ask for a report.

## Upgrading from vainu-skills

The earlier `vainuio/vainu-skills` repository shipped the same skills without the connector. If
you installed from it, remove the old copies first, otherwise every skill appears twice:

- On claude.ai, delete the per-skill uploads under **Organization settings > Skills** or
  **Customize > Skills**.
- For a `npx skills add vainuio/vainu-skills` install, run `npx skills remove` for those skills
  or delete them from your agent's skills directory.

Then install the plugin as described above.

## Adding a plugin

1. Create `plugins/<name>/` with a `skills/` directory of `<skill>/SKILL.md` folders.
2. Add both manifests: `plugins/<name>/.claude-plugin/plugin.json` for Claude and
   `plugins/<name>/plugin.json` in the [Agent Plugins](https://agent-plugins.org) format. Set
   `version` to the version the other plugins carry; CI fails when any manifest differs.
3. If the plugin needs the Vainu connector, copy `.mcp.json` and `mcp.json` from `plugins/vainu`.
4. Add a `README.md` of at least 40 words and a `LICENSE.txt` to the plugin folder.
5. Add an entry to `.claude-plugin/marketplace.json` and `.cursor-plugin/marketplace.json`.
6. Run `claude plugin validate .` and `python3 -I scripts/check_release_version.py`.

## Releasing

All plugins in this repository share one version. Raise `version` in both manifests of every
plugin, commit, and push a tag `v<version>`.
The release workflow validates, checks the versions against the tag, zips each plugin and
creates a GitHub release. A tag with a suffix such as `v1.0.0-rc.1` becomes a pre-release and
is the way to exercise the workflow before a real release.

