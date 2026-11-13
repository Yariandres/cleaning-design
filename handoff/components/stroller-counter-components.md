# Components used by the stroller counter

Nuxt UI parts restyled by tokens, plus custom components. Measurements are in the HTML reference (`prototypes/stroller/final/stroller-counter.html`, `base.css`). Colour names are Nuxt UI semantic names (`handoff/tokens/tokens.css`).

## From Nuxt UI
| Need | Component | Notes |
|---|---|---|
| Buttons | `UButton` | Primary: `color="primary" variant="solid"`; secondary: `color="neutral" variant="outline"`; on dark: white solid and white outline. Pill (`rounded-full`), weight 700, **min height 44px** (prototype 48px: 12 × 24 padding with 24px line). One solid primary per view. Hover `primary-600`; press scale .98 |
| FAQ | `UAccordion` (or native `<details>`) | **`:unmount-on-hide="false"`**; trailing icon: plus rotating to × on open (Lucide `plus`); row min 56px; first item open |
| Cookie banner | own component from `UCard`/`UButton` parts | See README, states. Both buttons the same variant and size |

## Custom components (not in Nuxt UI)
- **`HeroPriceCard`** — white card, `rounded-2xl`, shadow `0 24px 60px -34px rgba(14,60,50,.45)`. Eyebrow + small sub-label, 2px `neutral-900` top rule, price rows (name 17px/600, price: "od" in `neutral-500` + Bricolage 800 1.7rem, tabular), optional `nextFreeSlot` strip (`secondary-50`, border `secondary-200`, text `secondary-950`), one primary button, two text links.
- **`ProofBar`** — white band, 1px `neutral-200` top and bottom. Lead fact: 44px circle `secondary-300` with Lucide clock, Bricolage 800 up to 2.3rem; three facts: 44px `primary-100` circle, label 700 + one muted line.
- **`ProblemCard`** — `rounded-2xl` white card with 1px border, photo frame on top (ratios in README), eyebrow "Problem", H3, "Co robimy." line. Variants `big`, default, `wide` (horizontal; linked, with a text link and arrow). Only the linked variant lifts on hover.
- **`PriceList`** — rows with a 2px `neutral-900` top rule and 1px `neutral-200` row rules; name + optional small description left, price right (`white-space: nowrap`).
- **`PackageCard`** — `rounded-2xl`, 1px border (2px `primary-500` for the highlighted one), tag pill (`secondary-300` / `primary-100`), H3, bullets, Bricolage 800 2.2rem price + struck-through earlier price.
- **`SafetyPanel`** — `neutral-900` background, white text, `rounded-2xl`, 28px padding; eyebrow in `primary-200`.
- **`ZoneColumn`** — 4px top border (`primary-500`, `secondary-300`, `neutral-300`), H3, fee in 700, towns muted. Text only, no map.
- **`StickyCtaBar`** — phones only, fixed bottom, white 96% opacity, top border; primary button (flex 1) + 48px outlined phone button; respects the safe-area inset.
- **`PhotoSlot`** — fixed-ratio frame, `object-fit: cover`, `rounded-2xl` clip; placeholder style only in prototypes.
- **`Eyebrow`** — Figtree 700, 13px, uppercase, .08em, `primary-600`.
