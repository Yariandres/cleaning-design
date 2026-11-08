# Handoff format

How approved design reaches the developer agent (repo [cleaning-sell-system](https://github.com/Yariandres/cleaning-sell-system)).

**GitHub is the contract, Figma is the visuals.** This folder says *what* is approved, for which issues, with which states and data; Figma holds the exact layout and assets. Nothing is copied between repos: the developer reads this repo directly at a version tag. Work in progress stays in `prototypes/` and Figma pages marked WIP.

## Structure

```
handoff/
  CHANGELOG.md                 one line per handover: date, tag, what, issues
  tokens/
    tokens.json                colours (light + dark), type, radius, spacing, motion — names match DESIGN.md and Figma variables
    tokens.css                 the same as CSS custom properties
    fonts.md                   families, weights, source and licence
  components/
    <component>.md             anatomy, states, behaviour, spacing, motion, accessibility; Figma link to the component
  pages/
    <page>/                    e.g. stroller-counter, homepage, quote-form, admin-today
      README.md                the brief for the developer (see below)
      screens/                 PNGs: 390-light, 390-dark, 1440-light, 1440-dark, plus extra states
      copy.md                  final Polish copy, keyed (e.g. hero.title), alt texts, which parts are data
      assets/                  optimised images (AVIF/WebP + 2× fallback), SVG icons — also exportable from Figma
      prototype.html           optional static reference when Figma isn't used for this page
```

## Page README (required sections)

1. **Tag and status** — e.g. `stroller-v1`, approved by the owner on YYYY-MM-DD, designed against `design-constraints.md` at commit `<sha>`
2. **Issues** — developer issue numbers and PRD IDs it covers (e.g. #41, #42 · S2–S6, S9)
3. **Figma** — direct links to the exact frames (one per section and state), not just the file
4. **Sections in order** — with notes the frames can't show (behaviour, sticky bar, scroll, motion with durations and easing)
5. **Data bindings** — everything from the database marked, e.g. `{price:stroller-single}` → "od 90 zł", `{nextFreeSlot}`, `{faq:stroller}`, `{reviews:stroller}`. Never hard-coded.
6. **States** — empty (no reviews/photos yet), loading, error, success, long text, phone/desktop, light/dark — each with its frame or screenshot
7. **Accessibility** — focus order, labels, alt text, reduced-motion behaviour
8. **Assets and licences** — owner's own, licensed (named), or generated (labelled)
9. **SEO** — link to the SEO brief; title, meta description, H1 and structured-data notes as agreed
10. **Open questions** — anything the developer must decide with the owner

## Talking to each other

| Direction | Where | Title / label |
|---|---|---|
| Design → dev: handover ready | issue in cleaning-sell-system | "Handoff ready: `<tag>`" · `handoff` |
| Dev → design: question about a handover | comment on that issue | — |
| SEO → design: page brief | issue in **this** repo, brief in cleaning-seo | "SEO brief: `<page>`" · `seo-brief` |
| Dev → design: technical change (UI library, icons, fonts, breakpoints…) | issue in **this** repo, plus `docs/design-constraints.md` in cleaning-sell-system | "Dev note: `<topic>`" · `dev-note` |

## Delivery flow

1. Owner approves the design.
2. Designer completes the page folder, updates `tokens/` if anything changed, adds a CHANGELOG line, commits and pushes.
3. Designer tags the commit: `git tag <page>-v<n>` (e.g. `stroller-v1`) and pushes the tag. Later edits get a new tag (`stroller-v2`); a published tag is never moved.
4. Figma: the approved frames are marked "Ready for dev" (or moved to a "Handoff" page) and must match the tag. Changes after the tag go to a new version, not over the approved frames.
5. Notify the developer — either the owner says *"Build stroller-v1 from cleaning-design"*, or, if this session has GitHub access to both repos, the designer opens an issue in cleaning-sell-system titled **"Handoff ready: stroller-v1"** with the tag, the README link, the issue numbers and the Figma links.
6. The developer fetches the tag, reads the README, pulls visuals from Figma, builds, and asks back (in that issue, or via the owner) if anything is missing.
