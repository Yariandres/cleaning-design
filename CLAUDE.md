# Design — mobile cleaning business, Poznań

This repo is the **design studio** for a one-person mobile cleaning business in Poznań (sofas, mattresses, rugs, strollers, car seats, car interiors). It produces the visual design and hands it to a separate developer repo (`Yariandres/cleaning-sell-system`), which builds the app.

## How to work here

- All design work goes to the **web-designer** agent (`.claude/agents/web-designer.md`).
- Read first: `design/brief.md`, `DESIGN.md`, `design/references/`, `docs/prd.md`.
- Work in progress lives in `prototypes/`. Only owner-approved work goes into `handoff/`, in the format of `handoff/README.md`.
- **GitHub is the contract, Figma is the visuals.** Each approved handover is tagged (`stroller-v1`); the developer reads this repo at that tag and pulls visuals from the linked Figma frames. Nothing is copied between repos.
- **Listen to the developer.** Before every job, read `docs/design-constraints.md` in cleaning-sell-system and any open issues here labelled `dev-note`. Technical constraints (UI library, icons, fonts, breakpoints, image formats, animation, forms) are binding; if one conflicts with `DESIGN.md` or hurts the design, raise it with the owner instead of ignoring it. Apply each dev note, comment what changed, and close it.
- This repo never contains the production app, its stack or its server logic.
- Package manager, if one is ever needed for tooling here: **pnpm**.

## Rules

- Polish UI copy, "Ty" voice. English in notes and comments.
- Never invent reviews, ratings, customer names or before/after photos.
- Only true urgency; no timers or fake scarcity.
- `DESIGN.md` is the contract. Change it on purpose, with a changelog line, never by drift.
- Brand name and logo are not chosen yet: use `[Nazwa firmy]` and the placeholder mark.

## What's next

1. Snapshot the owner's **Pinterest board** into `design/references/` (one image + note per pin).
2. Connect **Figma** in Claude Code and read the owner's file, if any.
3. First job: the **stroller counter** (`/poznan/pranie-wozkow`) — directions → approved design → `handoff/pages/stroller-counter/` + `handoff/tokens/` → tag `stroller-v1`.
4. Then: counter template states, quote form, homepage, sofa counter, admin screens (order in `docs/prd.md` §9).
