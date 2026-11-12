# DESIGN.md — the design contract

The single source of truth for how the site and admin look. Tokens are exported to `handoff/tokens/` (and Figma variables when used); **change them together, in the same commit, with a line in the changelog below explaining why.** If a reference image or a Figma frame disagrees with this file, this file wins until it is updated on purpose.

Origin: the stroller counter mockup (`design/mockups/pranie-wozkow.html`), approved by the owner. The mockup is kept as the first approved *look*; where this file now differs from it (light only, two fonts, focus ring, field borders, Nuxt UI structure) this file wins.

## Built on Nuxt UI

The app uses Nuxt UI v4 with Tailwind CSS v4 (dev note [#1](https://github.com/Yariandres/cleaning-design/issues/1), source: `docs/design-constraints.md` in cleaning-sell-system at a73ee34). Consequences for every design:

- **Components come from Nuxt UI** (Figma kit: https://ui.nuxt.com/figma), restyled only through the tokens below. Anything Nuxt UI doesn't cover is listed as a **custom component** in the handover README.
- **Colours use Nuxt UI's semantic names** (`primary`, `secondary`, `success`, `info`, `warning`, `error`, `neutral`), each a 50–950 scale. No raw hex in components.
- **Light mode only.** No dark frames, no dark tokens. Keep every colour on a semantic name so dark could be added later without redesigning components.
- **Frames at 390 and 1440**; layouts must also hold at 768 and 1024 (Tailwind breakpoints 640 / 768 / 1024 / 1280 / 1536).
- Motion CSS only, fonts self-hosted, forms and the cookie banner built from Nuxt UI components (see the sections below).

## Colour

### Roles

| Nuxt UI name | Brand role | Anchor (shade 500) |
|---|---|---|
| `primary` | Teal. The one action: solid buttons, links, active states, eyebrows, ticks | `#0E6E5C` |
| `secondary` | Sun yellow. The one highlight per screen: the "wanted now" dot, headline underline. Never a solid button | `#E4A400` (the sun itself is `secondary-300` `#FFD45C`) |
| `success` | Confirmation, "sent", done | `#2E7D32` |
| `info` | Neutral notices | `#2C6E91` |
| `warning` | Needs attention, pending | `#A15C00` |
| `error` | Validation errors, destructive | `#B3372B` |
| `neutral` | Mint-tinted grey: text, surfaces, borders | `#4E6B65` |

Shade 500 of each status colour is deep enough for white text on it and for text on white. Status colours carry meaning only; never decoration.

### Scales

| | `neutral` | `primary` | `secondary` | `success` | `info` | `warning` | `error` |
|---|---|---|---|---|---|---|---|
| 50 | `#F5FAF8` | `#EEF8F4` | `#FFF8E1` | `#EFF8EC` | `#EEF5F9` | `#FFF4E0` | `#FDEEEC` |
| 100 | `#E3F2EC` | `#D7F3E6` | `#FFF1C9` | `#DAEAD7` | `#D8E5ED` | `#F5E3CA` | `#F7DAD6` |
| 200 | `#CFE3DB` | `#A0E2CD` | `#FFE398` | `#AFCEAD` | `#ADC7D6` | `#E1C09D` | `#E9B3AA` |
| 300 | `#A2B9B2` | `#5FD1B5` | `#FFD45C` | `#86B384` | `#83A8BF` | `#CC9E71` | `#D98B80` |
| 400 | `#77918A` | `#399E87` | `#F2BC3C` | `#5C985B` | `#598BA8` | `#B77D44` | `#C76356` |
| **500** | `#4E6B65` | `#0E6E5C` | `#E4A400` | `#2E7D32` | `#2C6E91` | `#A15C00` | `#B3372B` |
| 600 | `#3F5C56` | `#0D5A4B` | `#BB8700` | `#26692A` | `#255C7A` | `#874D00` | `#962D23` |
| 700 | `#304D47` | `#0B473B` | `#946A00` | `#1F5622` | `#1D4C64` | `#6E3F00` | `#7A241C` |
| 800 | `#213E39` | `#09342C` | `#6E5000` | `#17441B` | `#163B4F` | `#553100` | `#601B14` |
| 900 | `#12302B` | `#06231D` | `#4B3600` | `#103214` | `#0F2C3B` | `#3E2300` | `#46120D` |
| 950 | `#0A1F1C` | `#031511` | `#3A2A00` | `#0D2A10` | `#0C2431` | `#331D00` | `#3A0E0A` |

Exact anchors (the values from the approved mockup): `neutral-50` paper, `-100` band, `-200` line, `-500` muted, `-900` ink; `primary-100` chat bubble, `-300` the old dark-mode teal, `-500` brand teal, `-900` text on accent; `secondary-300` sun, `-950` text on sun. Every other step is interpolated in OKLCH between anchors.

### Surfaces and text (Nuxt UI variables set in `:root`)

Nuxt UI's defaults use white as the page. Ours is the mint paper, so override these:

| Old token | Nuxt UI variable | Value | Use |
|---|---|---|---|
| `--paper` | `--ui-bg` | `neutral-50` | Page background |
| `--band` | `--ui-bg-muted` | `neutral-100` | Alternating section bands |
| `--card` | `--ui-bg-elevated` | `#FFFFFF` | Cards, form fields, quote panels |
| `--ink` | `--ui-text-highlighted`, `--ui-bg-inverted` | `neutral-900` | Headings, the dark "safety" panel |
| (body) | `--ui-text` | `neutral-700` | Body text |
| `--muted` | `--ui-text-muted` | `neutral-500` | Secondary text, placeholders |
| `--line` | `--ui-border`, `--ui-border-muted` | `neutral-200` | Dividers, card borders |
| — | `--ui-border-accented` | `neutral-300` | Hover/active borders |
| `--accent` | `--ui-primary` | `primary-500` | Buttons, links, ticks |
| `--accent-ink` | `--ui-text-inverted` | `#FFFFFF` | Text on primary |
| `--sun` | `secondary-300` | `#FFD45C` | The one highlight |
| `--sun-ink` | `secondary-950` | `#3A2A00` | Text on sun |
| `--bubble-in` / `--bubble-out` | custom chat component | `#FFFFFF` / `primary-100` | Chat-style quote bubbles |

`--ui-text-dimmed` (`neutral-400`) is for disabled text only; it does **not** pass contrast as a placeholder, so placeholders use `text-muted`.

### Contrast (WCAG 2.2 AA, checked 2026-11-12)

| Pair | Ratio | Needs |
|---|---|---|
| `neutral-700` body on paper | 8.7 | 4.5 |
| `neutral-500` muted on paper / white / band | 5.5 / 5.8 / 5.0 | 4.5 |
| white on `primary-500` (button) / `primary-600` (hover) | 6.2 / 8.1 | 4.5 |
| `primary-500` text on paper / band | 5.9 / 5.3 | 4.5 |
| `secondary-950` on `secondary-300` | 9.8 | 4.5 |
| white on success / info / warning / error 500 | 5.1 / 5.6 / 5.2 / 6.0 | 4.5 |
| status 700 text on its 50 (soft alerts) | 8.0–8.9 | 4.5 |
| `neutral-400` field border on white / paper | 3.4 / 3.2 | 3 |
| focus ring `neutral-900` on paper | 13.4 | 3 |
| white focus ring on `primary-500` / `neutral-900` | 6.2 / 14.1 | 3 |

Two things in the approved mockup **failed** and are changed (changelog 2026-11-12): the sun-yellow focus ring (1.3:1 against the page) and the `--line` field borders (1.3:1).

### Using colour

- **One solid primary button per view.** Everything else is `neutral` with `outline` or `ghost`. Solid `secondary` is not used; if a `secondary` surface needs text, use `secondary-950`.
- **Sun** appears at most once per screen and never carries meaning alone (the "wanted now" dot always has a text label). The headline underline is decoration.
- Hover on solid buttons uses `primary-600`; disabled is Nuxt UI's default.
- **Focus:** 3px outline, 3px offset, `neutral-900` on light surfaces and white on `primary` or ink surfaces, on every interactive element. Nuxt UI's own solid-button focus ring (the colour at 25% opacity) is too faint and must be overridden.
- **Field borders:** `neutral-400` (not `neutral-200`), on white cards. Fields do not sit directly on a `neutral-100` band.

## Type

**Two families only**, self-hosted through `@nuxt/fonts` (no requests to Google at runtime). Both are variable fonts under the SIL Open Font License 1.1, and both contain every Polish letter (ą ć ę ł ń ó ś ź ż and capitals), „ ” – — … and tabular figures. Checked on the Fontsource files, 2026-11-12.

| Role | Font | Weights | Notes |
|---|---|---|---|
| Display: h1–h3, big prices, logo wordmark | **Bricolage Grotesque** | 500–800 (variable `wght`) | h1 `clamp(2.3rem, 5.4vw, 4.1rem)` weight 800; `text-wrap: balance`; line-height 1.08 |
| Body, UI, labels, numbers | **Figtree** | 400–700 (variable `wght`) | 17px base on desktop, 16px at 390; line-height 1.55 |

- **Eyebrows** (previously DM Mono): Figtree 600, 13px, uppercase, letter-spacing .08em, `primary-500`.
- **Phone numbers, time slots, small data, list prices:** Figtree 600 with `font-variant-numeric: tabular-nums`. Big package prices: Bricolage 800.
- Load only the Latin and Latin-Extended subsets (Polish needs Latin-Extended): about 87 KB of WOFF2 for both families.
- The optical-size axis of Bricolage (used by the Google build in the mockup) is not loaded, to keep files small; headings may look very slightly different from the mockup.

Never use Inter, Roboto, Arial or Space Grotesk (it appears on the owner's board, and stays excluded). Dropping DM Mono was needed to stay within two families.

## Shape and space

- **Radius is one base value:** `--ui-radius: 0.375rem` (6px). Nuxt UI derives the rest, which reproduces the approved look exactly: `rounded-lg` 12px (fields, small panels) · `rounded-xl` 18px (cards, the old `--r`) · `rounded-2xl` 24px (packages, form panel, safety panel, and the chat mock, which moves from 28px to 24px). **Buttons and chips are full pills** (`rounded-full`).
- **4px spacing grid** (Tailwind's default). Off-grid values from the mockup move to the nearest step: button padding 14×22 → 12×24 (with 24px text this makes 48px tall), card padding 18/22/28 → 16/24/28, gaps 18 → 16 or 20.
- Content width `--ui-container: 70rem` (1120px); side gutter `max(16px, safe-area)`.
- Section padding `clamp(56px, 8vw, 96px)`.
- **Tap targets ≥ 44px.** Nuxt UI's tallest default button (`xl`) is only 40px, so set a global minimum height of 44px (`min-h-11`) on buttons, inputs, selects, checkboxes' labels and tab/nav items, and verify it in the handover.

## Components

Nuxt UI components, restyled through tokens (the mockup's hand-made versions are the visual reference):

- **Buttons** (`UButton`): primary = `color="primary" variant="solid"` for the one action; secondary = `color="neutral" variant="outline"` (phone, WhatsApp). Pill shape, weight 700, `size="xl"` plus the 44px minimum.
- **FAQ** (`UAccordion`): **must set `:unmount-on-hide="false"`.** Nuxt UI removes closed answers from the HTML by default, which breaks the SEO brief (real text in the HTML, [#2](https://github.com/Yariandres/cleaning-design/issues/2)). Native `<details>` is an acceptable alternative. Trailing icon: Lucide chevron.
- **Forms** (`UForm`, `UFormField`, `UInput`, `USelectMenu`, `UCheckbox`, `UFileUpload`): states default, focus, error, disabled, loading. Error text sits under the field and appears on blur and on submit. No error summaries in modals.
- **Cookie banner** (own component, Nuxt UI parts): "Akceptuję" and "Odrzucam" with equal visual weight.
- **Custom components** (not in Nuxt UI): hero highlight underline, chat-style quote mock, price list rows, proof bar, zone list, sticky bottom bar on phones. Listed again in each handover README.
- **Eyebrow:** label above headings (see Type).
- **Hero highlight:** key words in the h1 get a `secondary-300` underline (`linear-gradient(transparent 62%, var(--ui-color-secondary-300) 62%)`).
- **Chips:** one-liners under the hero, each with a Lucide `check` icon (replaces the ✓ character).
- **Sticky bottom bar on phones:** "Wyślij zdjęcia" plus a phone icon.
- **Service area and zones:** text only (postcode field, grouped town picker, list of towns). No map.

## Icons

- **Interface icons: Lucide only** (`i-lucide-*` in Nuxt UI). No other set, and no emoji or text characters standing in for icons (the mockup's ✓ and ★ become `check` and, later, `star`).
- **Custom icons:** chamomile, stroller, sofa, paw, mattress, car. SVG on a **24px grid, one colour via `currentColor`, 2px stroke, round caps and joins**, to sit next to Lucide. They are drawn in Job C with the logo.
- **Chamomile:** two versions. The *icon* is the single-colour 24px line version. The *logo* symbol is full-colour (white petals, sun centre) and is a separate asset; it is not an icon.
- **Open question:** the WhatsApp button needs a brand mark, and Lucide has none. Either one custom brand SVG is allowed, or the button is text only. Asked of the owner and developer in the Job B hand-over.
- Larger illustrations (for example the continuous-line style on the board) are SVG spot illustrations, not icons.

## Imagery

Real photos of the owner's own items and jobs only (first photos: own stroller, sofa, car). Natural light, close-ups of fabric texture, honest before/after pairs at the same angle. No stock photos of people.

- **Photos as JPG at 2× the largest displayed size**; icons and illustrations as SVG. The tool serves AVIF/WebP.
- **Every image slot has a fixed aspect ratio** (stated in the handover README, to avoid layout shift) and alt text that describes the picture in plain Polish.
- **Share image (Open Graph):** one template, 1200 × 630, with slots for the page title and one photo. Designed with the first page.
- No H1 or prices as text inside images.

## Motion

CSS only: **opacity and transform**, 150–250 ms, ease-out for entering, no motion on load beyond a single fade. Every animation has a `prefers-reduced-motion` version (usually none). Content must be readable in the HTML without JavaScript, and nothing essential may appear only after an animation (the chat mock's bubbles are in the HTML from the first paint and only slide).

## Brand and per-service accents

Brand: **Nowiutko** (`docs/brand.md`). Symbol: chamomile flower — white petals around a sun-yellow centre on mint. **One look across all services**; each service varies only inside the system, using the existing scales (no extra palettes):

| Service | Accent scale | Icon (one consistent style) | Icon on tinted circle |
|---|---|---|---|
| Strollers and car seats (flagship) | `secondary` (sun) | stroller | `secondary-800` on `secondary-100` (6.7:1) |
| Sofas, armchairs, rugs | `primary` (teal) | sofa | `primary-700` on `primary-100` (9.0:1) |
| Car interiors | `primary-800`, deeper teal (provisional) | car | `primary-800` on `primary-100` (11.6:1) |
| Pets (urine, hair, smell) | to define with the logo (Job C) | paw | |
| Mattresses | to define with the logo (Job C) | mattress | |

Accent use is limited to small surfaces (icon, eyebrow, highlight underline, illustration tint). Buttons, type, layout and components never change per service. No sub-brands.

## Changelog

- 2026-11-08 — Created from the approved stroller mockup.
- 2026-11-09 — Brand Nowiutko: chamomile symbol, one look with per-service accents (accent values for pets, mattresses and car still to define).
- 2026-11-12 — Dev note #1 (Nuxt UI, Lucide, light only): **removed dark mode**; colours rebuilt as Nuxt UI semantic names with 50–950 scales (old `--paper/--band/--card/--ink/--muted/--line/--accent/--sun` map onto them, same values at the anchors); **fonts cut from three to two** (DM Mono dropped for Figtree) and self-hosted; radius is one base value (6px) that reproduces the 12/18/24px sizes; spacing on a 4px grid; 44px minimum control height; icons Lucide plus custom 24px 2px-stroke SVGs; share-image, image-ratio and motion rules added. **Contrast fixes:** focus ring changed from sun yellow (1.3:1) to ink or white, field borders from `--line` (1.3:1) to `neutral-400` (3.4:1). FAQ accordion must not unmount closed answers (SEO). Pets and mattress accents still open (Job C).
