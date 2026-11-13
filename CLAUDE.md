# Design — mobile cleaning business, Poznań

This repo is the **design studio** for a one-person mobile cleaning business in Poznań (sofas, mattresses, rugs, strollers, car seats, car interiors). It produces the visual design and hands it to a separate developer repo (`Yariandres/cleaning-sell-system`), which builds the app.

## How to work here

- All design work goes to the **web-designer** agent (`.claude/agents/web-designer.md`).
- Read first: `docs/brand.md`, `design/brief.md`, `DESIGN.md`, `design/references/`, `docs/prd.md`.
- Work in progress lives in `prototypes/`. Only owner-approved work goes into `handoff/`, in the format of `handoff/README.md`.
- **GitHub is the contract, Figma is the visuals.** Each approved handover is tagged (`stroller-v1`); the developer reads this repo at that tag and pulls visuals from the linked Figma frames. Nothing is copied between repos.
- **Listen to the developer.** Before every job, read `docs/design-constraints.md` in cleaning-sell-system and any open issues here labelled `dev-note`. Technical constraints (UI library, icons, fonts, breakpoints, image formats, animation, forms) are binding; if one conflicts with `DESIGN.md` or hurts the design, raise it with the owner instead of ignoring it. Apply each dev note, comment what changed, and close it.
- **Work from the SEO brief.** Each page starts with an "SEO brief: <page>" issue from the SEO desk ([cleaning-seo](https://github.com/Yariandres/cleaning-seo)). Its headings, FAQ questions and layout needs (visible price, real-text H1 and FAQ) are requirements; wording stays in the brand voice. Ask questions on that issue. Don't start a page without its brief unless the owner says so.
- This repo never contains the production app, its stack or its server logic.
- Package manager, if one is ever needed for tooling here: **pnpm**.

## How we work: one job at a time, owner reviews

1. Work on **one job** at a time (from "What's next" below, or what the owner asks).
2. Design it in `prototypes/` (and Figma), screenshot and run the checks; commit locally.
3. **Stop and hand over for review:** screenshots, what you decided and why, open questions.
4. **Don't push, tag, mark Figma frames "Ready for dev" or open issues until the owner says "go".** If they ask for changes, make them and hand over again.
5. After approval: push, tag the handover, open "Handoff ready" in cleaning-sell-system, close the issues you resolved, update "What's next". Then propose the next job.

- **Brand problems** (name, tagline, voice, offers, prices, messaging, leftover placeholders): open a "Brand: …" issue with label `brand` in this repo, as described in `docs/brand.md` → "Raising a brand issue". The owner takes them to the brand strategist.

## Rules

- Polish UI copy, "Ty" voice. English in notes and comments.
- Never invent reviews, ratings, customer names or before/after photos.
- Only true urgency; no timers or fake scarcity.
- `DESIGN.md` is the contract. Change it on purpose, with a changelog line, never by drift.
- Brand: **Nowiutko** — chamomile symbol, freshness voice, one look across all services with a light accent per service. Source of truth: `docs/brand.md`. The logo is now in scope (from the chamomile symbol), with the owner's approval.

## What's next

1. ~~Snapshot the owner's Pinterest board~~ (done 2026-11-12).
2. Connect **Figma** in Claude Code and read the owner's file, if any (read tools only so far; no write tools).
3. ~~Logo~~ — direction B approved 2026-11-13; per-service accents and icon set in DESIGN.md. Custom icons (chamomile, stroller, sofa, paw, mattress, car) still to draw.
4. First page: the **stroller counter** (`/poznan/pranie-wozkow-i-fotelikow`, per the SEO brief, issue #2) — **handed over as `stroller-v1` (2026-11-13)**; waiting for the developer's questions and the owner's photos, phone number and brand-list checks.
5. Next: quote form, then counter template states, homepage, sofa counter, admin screens (order in `docs/prd.md` §9). Custom service icons (chamomile, stroller, sofa, paw, mattress, car) still to draw.
