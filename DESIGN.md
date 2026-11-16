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
- **Sticky bottom bar on phones:** "Wyślij zdjęcia" plus a phone icon. **Until the quote form is live (early launch)** the button reads "Wyślij zdjęcia na WhatsApp" and is a `wa.me` link with a prefilled message; the label never wraps (below 360px it drops its icon). Pages with the bar set `scroll-padding-bottom` so keyboard focus is never hidden behind it.
- **Footer** (spec `handoff/components/footer.md`): one footer on every public page, on the page background, in 0.9rem `neutral-500`. Logo (not a link) with the descriptive tagline and the area; "Kontakt" (phone and WhatsApp as 44px rows, value in 700 `neutral-900`); "Dane firmy" (legal name, NIP; REGON, address and e-mail optional, all from data); a 1px rule; then "Prywatność" and "Ustawienia cookies". **No solid button, no headings, no page navigation, no link to a page that does not exist.** An empty optional value removes its line; without a legal name and NIP the company block is left out. The end of the page stays clear of the sticky bar (`76px + safe-area inset` reserved) and of the open cookie banner (its height reserved while it is open).
- **The one action before the quote form exists:** every solid button on a counter is the same WhatsApp link with the same label; the phone call is the second action (outline button or text link, number always visible as text); SMS is a one-line fallback. No WhatsApp brand mark: the button uses the Lucide camera. When the quote form ships, the solid buttons go back to it and WhatsApp and phone return to `neutral` outline.
- **Headings on dark surfaces** (`primary-800` final band, `neutral-900` safety panel) are white; they do not inherit the default `neutral-900` heading colour.
- **Service area and zones:** text only (postcode field, grouped town picker, list of towns). No map.

## Admin patterns

The owner's admin uses the same tokens, fonts and components as the site; it is quieter (no bands, no photos, no highlight underline). Added with the "Cennik i ustawienia" design (reference: `prototypes/admin-cennik/`).

- **Shell:** below 1024px a bottom tab bar with five items (Dziś, Lejek, Kalendarz, Klienci, Więcej); "Więcej" is a sheet with Cennik i ustawienia, Raport and Wyloguj. From 1024px a 248px left sidebar with all six. Edit screens replace the tab bar with the save bar.
- **Screens:** `neutral-50` page, white `rounded-xl` cards and panels with a 1px `neutral-200` border. Screen title in Bricolage 800 at 28px; everything else Figtree. Fields always sit on white panels.
- **List → edit:** rows at least 64px tall, the whole row is the link; edit forms are stacked white panels.
- **Saving:** explicit "Zapisz" in a fixed bottom save bar with a status line (clean, unsaved, invalid, saving, failed). After saving: back to the list, the row tinted `success-50`, and a `neutral-900` toast saying the change is live. Only reorder moves save at once. Leaving with unsaved changes asks first.
- **Off, not deleted:** hidden entries stay in place with muted text and an "Ukryta" badge. Delete only for never-used entries, with a confirmation; solid `error` is used only on that confirm button.
- **Order:** a reorder mode with 44px up and down buttons. No drag and drop.
- **Live prices in text:** a price token is shown as a chip (`primary-100` / `primary-800`, Lucide `tag`), never as code.
- **Sun** in admin: only the "Teraz w sezonie" marker, once per screen. The package-tag colour sample is a swatch, not a highlight.
- **Status colours:** soft notes use the status 50 background, 200 border and 700 text; the unsaved dot is `warning-500` and always has text next to it.
- **Controls:** inputs and buttons 48px, 16px text in inputs (no zoom on iOS); every other control at least 44px, including the switch's hit area.

## Quote form patterns

The public quote form (`/poznan/wycena`) looks like the counters: same header (logo + phone), footer, type, buttons and tokens. Added with the quote-form design (reference: `prototypes/quote-form/`).

- **Estimate bar replaces the "Wyślij zdjęcia" bar** on this page. Below 900px a fixed white bottom bar holds "Szacunkowa cena" with the amount (left, a button that opens the breakdown in a `UDrawer`) and the step's one solid button (right). From 900px the estimate is a sticky white `rounded-2xl` card in a 360px right column, and the buttons sit under the step.
- **Sun on the form:** only the highlight underline under the estimate amount, once per screen. Package tags inside the form are `primary-100` / `primary-800`, not sun.
- **Chosen things** (service rows, packages, radio cards): `primary-50` background with a 4px `primary-500` left edge or a 2px `primary-500` border, always together with a non-colour sign (stepper, tick).
- **Steps:** four 6px bars (`primary-500` done and current, `neutral-200` ahead) with "Krok N z 4"; one `h1` (styled as the eyebrow) and the step title as the only `h2`.
- **Status colours on the public site** follow the admin rule: soft notes use the status 50 background, 200 border and 700 text; field errors are `error-500` text with a Lucide `circle-alert`, under the field.
- **Fields sit on white panels or directly on the `neutral-50` page**, never on a `neutral-100` band. Inputs and buttons 48px, 16px input text, every other control at least 44px (slot pills 48px).
- **Never pressure:** the minimum order and the "free travel from 400 zł" rule are stated as one neutral sentence with the customer's current amount. No progress bars toward a threshold, no "only … left".

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
- **Share image (Open Graph):** one template, 1200 × 630, with slots for the page title and one photo. Designed with the first page. **Two variants** (spec `handoff/components/share-image.md`): *photo* (light paper, logo, title, photo slot 440 × 518) and *no photo* (the logo's layout at full size: `primary-500` ground, the chamomile bleeding off the left edge, the logo on a white label, the title in white). A page without a share photo uses the no-photo variant; a placeholder is never published. The no-photo variant keeps logo, title and line inside the middle 630px, so a centre-square crop still shows a whole card, and its smallest text is 32px so it reads at about 400px wide.
- No H1 or prices as text inside images. For the share image this means: its title is a short page name with its own copy key (`og.title`), never the H1 string, never the `<title>` and never a price.

## Motion

CSS only: **opacity and transform**, 150–250 ms, ease-out for entering, no motion on load beyond a single fade. Every animation has a `prefers-reduced-motion` version (usually none). Content must be readable in the HTML without JavaScript, and nothing essential may appear only after an animation (the chat mock's bubbles are in the HTML from the first paint and only slide).

## Brand and per-service accents

Brand: **Nowiutko** (`docs/brand.md`). Symbol: chamomile flower — white petals around a sun-yellow centre on mint.

**Logo (owner-approved 2026-11-13): direction B, "Odznaka".** A white chamomile with a sun-yellow centre on a `primary-500` rounded-square badge (12 petals; 8 bolder petals at 48px and below), with the wordmark "Nowiutko" set in Bricolage Grotesque 800 in `primary-700`. Source SVGs and generator: `prototypes/logo/b-odznaka/`. Favicon, admin app icon (512 plus maskable) and Facebook avatar use the small-size badge. Paper stays the cool mint `neutral-50` (owner-approved). **One look across all services**; each service varies only inside the system, using the existing scales (no extra palettes):

| Service | Accent scale | Icon (one consistent style) | Icon on tinted circle |
|---|---|---|---|
| Strollers and car seats (flagship) | `secondary` (sun) | stroller | `secondary-800` on `secondary-100` (6.7:1) |
| Sofas, armchairs, rugs | `primary` (teal) | sofa | `primary-700` on `primary-100` (9.0:1) |
| Car interiors | `primary-800`, deeper teal (confirmed 2026-11-13) | car | `primary-800` on `primary-100` (11.6:1) |
| Pets (urine, hair, smell) | `neutral-700` calm grey-green (no new colour) | paw | `neutral-700` on `neutral-100` (8.0:1) |
| Mattresses | `primary-600`, a lighter teal than sofa | mattress | `primary-700` on `primary-50` (9.8:1) |

Accent use is limited to small surfaces (icon, eyebrow, highlight underline, illustration tint). Buttons, type, layout and components never change per service. No sub-brands.

## Changelog

- 2026-11-08 — Created from the approved stroller mockup.
- 2026-11-09 — Brand Nowiutko: chamomile symbol, one look with per-service accents (accent values for pets, mattresses and car still to define).
- 2026-11-12 — Dev note #1 (Nuxt UI, Lucide, light only): **removed dark mode**; colours rebuilt as Nuxt UI semantic names with 50–950 scales (old `--paper/--band/--card/--ink/--muted/--line/--accent/--sun` map onto them, same values at the anchors); **fonts cut from three to two** (DM Mono dropped for Figtree) and self-hosted; radius is one base value (6px) that reproduces the 12/18/24px sizes; spacing on a 4px grid; 44px minimum control height; icons Lucide plus custom 24px 2px-stroke SVGs; share-image, image-ratio and motion rules added. **Contrast fixes:** focus ring changed from sun yellow (1.3:1) to ink or white, field borders from `--line` (1.3:1) to `neutral-400` (3.4:1). FAQ accordion must not unmount closed answers (SEO). Pets and mattress accents still open (Job C).
- 2026-11-13 — Logo B (Odznaka) chosen; paper stays cool mint. Accents defined: pets `neutral-700`, mattress `primary-600`; car `primary-800` confirmed. All reuse existing scales, no new colours.
- 2026-11-14 — **Admin patterns added** (shell navigation, list → edit, explicit save with a save bar and "live on the site" toast, off-not-deleted, reorder mode, live price chips), from the "Cennik i ustawienia" design. No new tokens or colours. Draft until the owner approves `admin-cennik-v1`.
- 2026-11-15 — **Quote form patterns added** (estimate bar in place of the "Wyślij zdjęcia" bar on the form, sun only on the estimate amount, chosen-row style, step bars, status colours on the public site, no-pressure rule), from the quote-form design. No new tokens or colours. Draft until the owner approves `quote-form-v1`.
- 2026-11-16 — **Early launch without the quote form** (owner priority #5): the sticky-bar rule and the "one action" rule gain a temporary WhatsApp version ("Wyślij zdjęcia na WhatsApp", same link on every solid button; call second; SMS fallback), because the stroller page goes live before the form. Two rules written down after defects found in `stroller-v1`: headings on dark surfaces are white (they were `neutral-900` on dark, about 1:1), and pages with a sticky bar set `scroll-padding-bottom`. No new tokens or colours. Approved by the owner with `stroller-v1.1` (2026-11-16).
- 2026-11-16 — Approved by the owner with `stroller-v1.2` (2026-11-16). **Footer** rule added under Components (one shared footer: brand line, contact, company details from data, legal row; no button, headings or navigation; rules for missing values; the end of the page stays clear of the sticky bar and the cookie banner). **Share image** gains a no-photo variant, and the "no H1 or prices in images" rule is spelled out for it (`og.title` is its own key). The sticky bar's reserved space now includes the safe-area inset. No new tokens or colours.
- 2026-11-17 — **Homepage v0 draft** (not yet approved): "Services block" pattern (one bookable card with a stretched title link and a card-level focus ring; coming services as plain text rows with a real-text "wkrótce" pill, no link/heading/price; a shipped service turns its row into one link row). No new tokens or colours.
- 2026-11-17 — **Homepage v0 hero: story board** (draft): three beats in icons (problem, message, result) in a zigzag with round badge chips on the seam, plus a labelled, aria-hidden chat example (HTML/CSS, no name/time/rating). Custom stroller and line-chamomile icons on the 24px grid (stroke 1.5 when used large). Stains use `warning-400`; no new tokens.
- 2026-11-17 — Homepage v0 hero story board revised (draft): vertical timeline from 900px (chips on a dashed line), a 3-tile strip under the voice line below 900px; non-breaking spaces after single-letter Polish words and `text-wrap: balance/pretty` on hero text. No new tokens.
