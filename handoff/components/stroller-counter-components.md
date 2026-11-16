# Components used by the stroller counter

Nuxt UI parts restyled by tokens, plus custom components. Measurements are in the HTML reference (`prototypes/stroller/final/stroller-counter.html`, `base.css`). Colour names are Nuxt UI semantic names (`handoff/tokens/tokens.css`).

## From Nuxt UI
| Need | Component | Notes |
|---|---|---|
| Buttons | `UButton` | Primary: `color="primary" variant="solid"`; secondary: `color="neutral" variant="outline"`; on dark: white solid and white outline. Pill (`rounded-full`), weight 700, **min height 44px** (prototype 48px: 12 × 24 padding with 24px line). One solid primary per view. Hover `primary-600`; press scale .98. *v1.1:* every solid button on the stroller page is the same WhatsApp link with the same label; the outlined button on the dark final band is the call (`tel:`), with a Lucide `phone` icon |
| FAQ | `UAccordion` (or native `<details>`) | **`:unmount-on-hide="false"`**; trailing icon: plus rotating to × on open (Lucide `plus`); row min 56px; first item open |
| Cookie banner | own component from `UCard`/`UButton` parts | See README, states. Both buttons the same variant and size |

## Custom components (not in Nuxt UI)
- **`HeroPriceCard`** — white card, `rounded-2xl`, shadow `0 24px 60px -34px rgba(14,60,50,.45)`. Eyebrow + small sub-label, 2px `neutral-900` top rule, price rows (name 17px/600, price: "od" in `neutral-500` + Bricolage 800 1.7rem, tabular), optional `nextFreeSlot` strip (`secondary-50`, border `secondary-200`, text `secondary-950`), one primary button, two text links.
- **`ProofBar`** — white band, 1px `neutral-200` top and bottom. Lead fact: 44px circle `secondary-300` with Lucide clock, Bricolage 800 up to 2.3rem; three facts: 44px `primary-100` circle, label 700 + one muted line.
- **`ProblemCard`** — *v1.1: a no-photo variant (no image frame, 24px padding) in a 2 × 2 grid from 700px, used while the owner's photos are missing; all four cards switch together.*  `rounded-2xl` white card with 1px border, photo frame on top (ratios in README), eyebrow "Problem", H3, "Co robimy." line. Variants `big`, default, `wide` (horizontal; linked, with a text link and arrow). Only the linked variant lifts on hover.
- **`PriceList`** — rows with a 2px `neutral-900` top rule and 1px `neutral-200` row rules; name + optional small description left, price right (`white-space: nowrap`).
- **`PackageCard`** — `rounded-2xl`, 1px border (2px `primary-500` for the highlighted one), tag pill (`secondary-300` / `primary-100`), H3, bullets, Bricolage 800 2.2rem price + struck-through earlier price.
- **`SafetyPanel`** — `neutral-900` background, white text **including the `h3`** (v1.1 fix: it inherited `neutral-900` and was invisible), `rounded-2xl`, 28px padding; eyebrow in `primary-200`.
- **`ZoneColumn`** — 4px top border (`primary-500`, `secondary-300`, `neutral-300`), H3, fee in 700, towns muted. Text only, no map.
- **`StickyCtaBar`** — phones only, fixed bottom, white 96% opacity, top border; primary button (flex 1) + 48px outlined phone button; respects the safe-area inset. *`stroller-v1.1`:* the primary button is "Wyślij zdjęcia na WhatsApp" (the page's one action, a `wa.me` link); the label never wraps, and below 360px it drops the camera icon and uses 15px text. The phone button is a fixed 48 × 48 with the accessible name "Zadzwoń: {business:phone}". The page sets `scroll-padding-bottom: 88px` below 900px so keyboard focus is never hidden behind the bar. *Draft `stroller-v1.2`:* the space reserved under the page is `76px + env(safe-area-inset-bottom)`, not a flat 76px.
- **`SiteFooter`** — *draft `stroller-v1.2`:* the shared footer, specified in [`footer.md`](footer.md).
- **`ShareImage`** — *draft `stroller-v1.2`:* the 1200 × 630 template with a photo and a no-photo variant, specified in [`share-image.md`](share-image.md).
- **`PhotoSlot`** — fixed-ratio frame, `object-fit: cover`, `rounded-2xl` clip; placeholder style only in prototypes.
- **`Eyebrow`** — Figtree 700, 13px, uppercase, .08em, `primary-600`.
