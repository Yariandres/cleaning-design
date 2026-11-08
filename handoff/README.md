# Handoff format

This folder is the only thing the developer agent (repo `cleaning-sell-system`) takes from design. Everything in it is **approved by the owner** and ready to build. Work in progress stays in `prototypes/`.

## Structure

```
handoff/
  CHANGELOG.md                 one line per handover: date, what, which issues
  tokens/
    tokens.json                colours (light + dark), type, radius, spacing, motion — names match DESIGN.md
    tokens.css                 the same as CSS custom properties
    fonts.md                   font families, weights, source and licence
  components/
    <component>.md             anatomy, states, behaviour, spacing, motion, accessibility notes
  pages/
    <page>/                    e.g. stroller-counter, homepage, quote-form, admin-today
      README.md                purpose, PRD IDs and issue numbers, sections in order, states, data bindings, open questions
      prototype.html           static reference (layout and CSS to copy from, not production code)
      screens/                 PNGs: 390-light, 390-dark, 1440-light, 1440-dark, plus any extra states
      copy.md                  final Polish copy, keyed (e.g. hero.title), with which parts come from data
      assets/                  optimised images (AVIF/WebP + 2× fallback), SVG icons, alt text in copy.md
      figma.md                 link to the Figma frame(s), if any
```

## Rules for every page handover

- **Data bindings are explicit.** Anything from the database is marked, e.g. `{price:stroller-single}` → "od 90 zł", `{nextFreeSlot}`, `{faq:stroller}`, `{reviews:stroller}`. The developer wires these; nothing is hard-coded.
- **Every state is covered:** empty (no reviews or photos yet), loading, error, success, long text, phone and desktop, light and dark.
- **Accessibility is noted:** focus order, labels, alt text, reduced-motion behaviour.
- **Images are cleared for use:** owner's own, licensed (licence named), or generated (labelled).
- **Issue numbers** from `docs/prd.md`'s companion `issues.md` in the developer repo are listed (e.g. #41 counter template, #42 stroller counter).

## Delivery to the developer

Copy the approved folder(s) into the developer repo under `design-handoff/` (same structure), commit, and tell the developer which pages changed. The developer asks back in that repo if anything is missing.
