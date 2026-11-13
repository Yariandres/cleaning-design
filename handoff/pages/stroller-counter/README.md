# Stroller counter — `/poznan/pranie-wozkow-i-fotelikow`

## 1. Tag and status
- **Tag:** `stroller-v1` (proposed; created only after the owner's "go"). Direction 2 ("Cennik pierwszy") chosen by the owner on 2026-11-13; the full design is awaiting the owner's review.
- Designed against `docs/design-constraints.md` in cleaning-sell-system at commit `85dee45`, and `DESIGN.md` in this repo at the tag.
- **No Figma for this handover** (owner decision, 2026-11-13). The visuals are the PNGs in `screens/` and the working HTML reference below.

## 2. Issues
- Developer issues: **#40** (build from a tagged handover), **#41** (counter template), **#42** (stroller counter content), **#44** (reviews and before/after slots, kept hidden), **#46** (cookie banner)
- PRD: S2, S3, S4, S5, S6, S8, S9
- SEO: [cleaning-design #2](https://github.com/Yariandres/cleaning-design/issues/2) and `seo/briefs/stroller-counter.md` in cleaning-seo. Title, meta description, H2 order and the seven FAQ questions follow it.

## 3. Visuals (instead of Figma frames)
- `screens/` (PNG, light only): `01`/`02` full page at 390 and 1440 · `03`/`04` the same layout held at 768 and 1024 · `05`/`06` the first screen · `07`/`08` cookie banner · `09`/`10` reviews, before/after and next-slot **live** states · `11`/`12` FAQ open with a long price-row label.
- **Working HTML reference** (the source of truth for measurements, spacing, hover states and breakpoints): `prototypes/stroller/final/stroller-counter.html` at this tag, with `prototypes/stroller/base.css`. Open it in a browser and inspect it. It is a prototype, not production code; recreate it with Nuxt UI components and the tokens in `handoff/tokens/`. States: `state-cookie.html`, `state-live-slots.html`, `state-faq-open-long.html`. Share image: `assets/og-template.html`.
- Regenerate the prototype: `python3 prototypes/stroller/build_final.py` (needs the Lucide icon folder; not needed to read the HTML).

## 4. Sections in order
Counter pages have **no main menu**: logo + phone only (PRD S3). One action: start a quote.

| # | Section | Heading | Notes |
|---|---|---|---|
| 0 | Header | — | Logo left; phone (tel link) and "Wyślij zdjęcia" button right (button hidden below 900px) |
| 1 | Hero | `<h1>` as eyebrow + big headline | 2 columns from 900px (copy / price card 480px), 1 column below. The **price card is the hero's main object**: the price is visible on the first phone screen. The big headline is a `<p class="display">`, not a heading, so the page has one H1 |
| 2 | Proof bar | none | First fact ("Tego samego dnia") large with the sun-yellow icon; three smaller facts with `primary-100` icon circles. 4 columns from 900px (1.3fr 1fr 1.15fr 1fr), lead fact on top at phone width |
| 3 | Headache | H2 | Bento from 900px: large card (spans 2 rows), two small, one wide linked card; stacked on phone |
| 4 | Price | H2 | Price list (left) + dark safety panel (right) from 1000px; three package cards below |
| 5 | Steps | H2 | 3 columns from 800px; one button below |
| 6 | Before/after | H2 | **Hidden** until real photos exist (`hidden` attribute and `data-slot="before-after"` in the prototype) |
| 7 | Car seats by brand | H2 | Text + 4:3 photo from 900px; band background |
| 8 | Reviews | H2 | **Hidden** until real reviews exist (`data-slot="reviews"`) |
| 9 | FAQ | H2 | `UAccordion` with **`:unmount-on-hide="false"`** (answers must be in the HTML), first item open |
| 10 | Service area | H2 | Text only, three zone columns; link to `/poznan/obszar-dzialania` |
| 11 | Final CTA | H2 | Dark `primary-800` band; master promise (S9); primary white button + outlined "Napisz na WhatsApp" (text only) + phone |
| 12 | Footer | — | One line of text + three links |
| — | Sticky bar | — | Phones only (<900px): "Wyślij zdjęcia" + phone icon, 76px reserved at the page bottom |
| — | Cookie banner | — | See states |

Alternating backgrounds: the headache, car-seat and area sections sit on `neutral-100`; the rest on `neutral-50`; proof bar on white.

**Behaviour and motion (CSS only; every one is removed under `prefers-reduced-motion`):** buttons step on hover (`primary-600`, 1px up) and press (scale .98); text links draw an underline in 200ms; the linked headache card lifts 2px with a shadow and its photo scales 1.03 inside the frame (350ms); FAQ plus sign rotates 45° in 200ms; smooth scroll for in-page anchors. No fade-in on scroll, no parallax, no timers.

## 5. Data bindings
Everything from the database is marked `data-bind` in the prototype. Never hard-code these.

| Binding | Shown as | Where |
|---|---|---|
| `{price:stroller-single}` `{price:stroller-2in1}` `{price:stroller-3in1}` `{price:stroller-twin}` `{price:carseat}` `{price:highchair}` | "od 90 zł" … | hero card (4 rows), price list (6 rows), FAQ answers 1–2, meta title/description |
| `{price:pack-new-member}` `{price:pack-family}` `{price:pack-car-baby}` and `…-was` | "319 zł" with struck-through "350 zł" | package cards, headache card 4 |
| `{business:min-order}` | "150 zł" | price note |
| `{business:phone}` | "500 000 000" (**placeholder**, owner to supply) | header, final CTA, sticky bar `tel:` |
| `{business:whatsapp}` | `wa.me` link | hero card, final CTA (text button, no brand icon) |
| `{nextFreeSlot}` / `.label` | "jutro, 10:00" | hero card line, **hidden when there is no real slot** (S5: true urgency only; no timers) |
| `{faq:stroller}` | 7 Q&A | FAQ and FAQPage JSON-LD (same text) |
| `{reviews:stroller}` | review cards | hidden until entries exist |
| `{beforeAfter:stroller}` | photo pairs + caption | hidden until entries exist |
| `{zones}` | towns per zone, fees | service area |
| `{pack:*:badge}` | "najczęściej wybierany" | package tag; show only if the owner marks it |

## 6. States
- **Default** — `screens/01`–`06`.
- **Hold at 768 and 1024** — `03`, `04`: layout was checked at 390, 768, 1024, 1440 and 320; no horizontal scroll at any.
- **Cookie banner** — `07`, `08`. Fixed bottom, white, top shadow. Title + one short paragraph + two buttons of **identical** size and style (both `primary` solid; equal weight, per constraint). Stacks above the sticky bar until a choice is made; on phones the buttons share a row. Built from Nuxt UI parts (issue #46).
- **Reviews / before-after / next-slot live** — `09`, `10`. The review and photo contents in these screenshots are **wireframe placeholders**, never real-looking quotes. Real data replaces them.
- **Empty (default)** — photo slots show a striped `neutral-100` placeholder with a dashed `neutral-400` border and a label. In production an empty slot must not ship as a placeholder: either the owner's photo is there, or the slot is hidden or replaced by the plain layout (headache cards without a photo: drop the image frame and keep the text card).
- **FAQ open + long text** — `11`, `12`: all items open; a long price-row label wraps and keeps the price right-aligned and unbroken (`white-space: nowrap` on the price).
- **Loading / error / success:** none on this page. The quote form is a separate job and handover.
- **No JavaScript:** all content, headings and FAQ answers are in the HTML; the FAQ also works as native `<details>`.

## 7. Accessibility
- Focus: 3px solid `neutral-900`, 3px offset; white on dark surfaces (`primary-800` final CTA, `neutral-900` safety panel). Never `outline: none`.
- Skip link first in the tab order: "Przejdź do cennika".
- Tab order = visual order: logo → phone → header button → hero card button and links → proof bar (no focus) → linked headache card → price link → steps button → FAQ summaries → area link → final CTA buttons → phone → footer links.
- All tap targets ≥ 44px (inline links in running text are exempt). Phone number is a `tel:` link; WhatsApp is a normal link.
- One `<h1>`; H2s in the order of the SEO brief; headache/price card titles are H3. Decorative icons `aria-hidden`; photo slots get the owner's alt text.
- Text contrast (WCAG AA): body `neutral-700` on `neutral-50` 8.7:1, muted `neutral-500` on `primary-50` 5.4:1, `primary-200` on `primary-800` 9.3:1, white on `primary-500` 6.2:1, `secondary-950` on `secondary-50` 13:1.
- Reduced motion: no transforms or transitions, no smooth scroll.
- Page language `pl`; `lang` on nothing else.

## 8. Assets and licences
- **Logo and icons (generated by us from the owner's approved direction B):** `handoff/brand/logo/` — `logo.svg`, `mark.svg`, `mark-small.svg` (favicon at 48px and below), `app-icon.svg`, `app-icon-maskable.svg` (admin app icon, 512 with safe padding). The wordmark is outlined from Bricolage Grotesque (SIL OFL).
- **Photos: none yet.** Every photo slot is a placeholder awaiting the owner's own photos. No stock photos, no people. Slots and sizes (hand over JPG at 2× the displayed size; the tool serves AVIF/WebP; keep the ratio fixed to avoid layout shift):

| Slot | Ratio | Displayed (desktop) | Source to supply |
|---|---|---|---|
| Headache card 1 (large) | 4:5 (frame fills the card, `object-fit: cover`) | ~392 × 560 | 1200 × 1500 |
| Headache cards 2, 3 | 16:10 desktop, **2:1 at 390** | ~327 × 204 | 1200 × 750 |
| Headache card 4 (wide) | fills the left 40% of the card (~4:3) | ~270 × 200 | 800 × 600 |
| Car seat | 4:3 | ~516 × 387 | 1200 × 900 |
| Before / after (each image) | 4:3 | ~350 × 262 | 1200 × 900 |
| Share image | 1200 × 630 (`assets/og-template-1200x630.png`, source `og-template.html`) | — | slot for page title (≤3 lines at 64px; 54px for 4) and one photo, 440 × 518 |

- Icons: Lucide only (`i-lucide-camera`, `phone`, `clock`, `house`, `shield-check`, `badge-check`, `check`, `calendar-check`, `arrow-right`; FAQ sign is a CSS plus). No custom icons are used on this page.
- Fonts: see `handoff/tokens/fonts.md`.

## 9. SEO
- Brief: `seo/briefs/stroller-counter.md` in cleaning-seo (approved by the owner 2026-11-10); design issue #2.
- Title: option 1 of the brief (53 chars). Meta description: option 1 (142 chars). Canonical `https://nowiutko.pl/poznan/pranie-wozkow-i-fotelikow`.
- H1 follows the brief's **option (a)**: the search phrase as the real `<h1>`, styled small as an eyebrow, with the hero line as the large visual headline. Option (b) (reworded big H1) would be a copy change only; the layout holds either.
- H2 order is exactly the brief's anatomy; before/after and reviews are absent from the rendered HTML while hidden (use `v-if`, not just CSS, so empty headings never reach crawlers).
- Structured data (rendered server-side): Service + Offer per item (from `{price:*}`), FAQPage (same text as visible), BreadcrumbList (Strona główna → Pranie wózków i fotelików). **No AggregateRating or Review** until real reviews exist.
- Prices are the real "od" prices in the HTML; none is inside an image. The hero has no image.
- In-content links: `/cennik`, `/poznan/obszar-dzialania`, anchors; descriptive anchor text.

## 10. Open questions (for the developer with the owner)
1. **Phone number** is still the placeholder 500 000 000; WhatsApp is `wa.me/48500000000`. Both come from `{business:*}`.
2. **WhatsApp** is a text-only button, no brand icon (owner decision). Revisit if the developer allows one brand SVG.
3. **H1 wording** (brief options a or b) and hero line are the brand strategist's call; the design holds either.
4. **Brand list** in the car-seat H2 (Cybex, Maxi-Cosi, Britax, Avionaut): only brands whose manuals the owner has checked; the SEO brief lists this as open.
5. **"najczęściej wybierany"** on the Rodzinny package is a claim; show it only if the owner's data supports it.
6. **Headache copy** ("Co robimy.") was written from the price list and mockup; the owner should confirm the gondola line ("odsysamy wodę") matches the real method.
7. **Cookie banner** does not appear in the hero screens; it shows on first visit until a choice is made. Whether the sticky bar hides under it is the developer's call (design shows it hidden).
8. **Package "…-was" prices** (struck-through) are shown only when the owner enters them.
