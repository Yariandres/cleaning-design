# cleaning-design

Design studio for the mobile cleaning business in Poznań. A **web-designer** agent designs the site and admin; approved work is packaged in `handoff/` for the developer repo [cleaning-sell-system](https://github.com/Yariandres/cleaning-sell-system).

## Start

```bash
git clone https://github.com/Yariandres/cleaning-design.git
cd cleaning-design
claude
```

Then, for example: *"Use the web-designer agent. Snapshot my Pinterest board <link>, then propose directions for the stroller counter."*

## What's here

| Path | What |
|---|---|
| `.claude/agents/web-designer.md` | The design agent |
| `.claude/skills/` | Its skills (pinned in `skills-lock.json`) |
| `design/brief.md` | Who we design for, the promise, hard rules |
| `DESIGN.md` | Design contract: tokens, type, components |
| `design/mockups/` | The approved stroller mockup (baseline look) |
| `design/references/` | Pinterest snapshot + notes |
| `docs/prd.md`, `docs/source/` | Product requirements, research, Polish copy, prices |
| `prototypes/` | Work in progress |
| `handoff/` | Approved work for the developer, in a fixed format |

Figma: connect the Figma MCP in Claude Code to let the agent read and write your files. The developer session needs it too: it builds from the Figma frames linked in each tagged handover.
