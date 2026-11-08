# DESIGN.md — the design contract

The single source of truth for how the site and admin look. Tokens are exported to `handoff/tokens/` (and Figma variables when used); **change them together, in the same commit, with a line in the changelog below explaining why.** If a reference image or a Figma frame disagrees with this file, this file wins until it is updated on purpose.

Origin: the stroller counter mockup (`design/mockups/pranie-wozkow.html`), approved by the owner.

## Colour

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#F5FAF8` | `#0D1B19` | Page background |
| `--band` | `#E3F2EC` | `#132724` | Alternating section bands |
| `--card` | `#FFFFFF` | `#18302C` | Cards, form fields, quote panels |
| `--ink` | `#12302B` | `#E7F4EF` | Body text and headings |
| `--muted` | `#4E6B65` | `#9DBAB2` | Secondary text |
| `--line` | `#CFE3DB` | `#284540` | Borders, dividers |
| `--accent` | `#0E6E5C` | `#5FD1B5` | Primary buttons, links, eyebrows, ticks |
| `--accent-ink` | `#FFFFFF` | `#06231D` | Text on accent |
| `--sun` | `#FFD45C` | `#F3C845` | Highlight: the "wanted now" dot, headline underline, focus ring. Max one sun element per screen. |
| `--sun-ink` | `#3A2A00` | `#2A1E00` | Text on sun |
| `--bubble-in` / `--bubble-out` | `#FFFFFF` / `#D7F3E6` | `#1E3934` / `#1F4A3E` | Chat-style quote bubbles |

Why: mint/teal reads as "clean and fresh" without hospital white; the sun yellow is warm, family-friendly and reserved so it always means "look here". Dark mode follows the system setting and can be forced with `data-theme`.

## Type

| Role | Font | Notes |
|---|---|---|
| Display (h1–h3, prices, logo) | **Bricolage Grotesque** 500–800 | Friendly, characterful grotesque; h1 `clamp(2.3rem, 5.4vw, 4.1rem)` weight 800; `text-wrap: balance` |
| Body | **Figtree** 400–700 | 17px base, line-height 1.55 |
| Labels, eyebrows, phone, slots, small data | **DM Mono** 400–500 | 13px uppercase eyebrows, letter-spacing .08em |

Never use Inter, Roboto, Arial or Space Grotesk.

## Shape and space

- Radius `--r: 18px` for cards; buttons are full pills (`999px`).
- Content width `--max: 1120px`; side gutter `max(16px, safe-area)`.
- Section padding `clamp(56px, 8vw, 96px)`.
- Tap targets ≥ 44px. Buttons: 14px × 22px padding, weight 700.
- Focus: 3px `--sun` outline, 3px offset, on every interactive element.

## Components (from the mockup)

- **Buttons:** `btn-main` (accent fill) for the one action; `btn-ghost` (ink outline) for secondary like phone/WhatsApp.
- **Eyebrow:** DM Mono label above headings, accent colour.
- **Hero highlight:** key words in the h1 get a sun underline (`linear-gradient(transparent 62%, var(--sun) 62%)`).
- **Chips:** ✓-prefixed one-liners under the hero (frame and wheels included, same day, safe for babies).
- **Chat quote mock:** bubbles showing "send photos → get price" — the core interaction, shown not told.
- **Sticky bottom bar on phones:** "Wyślij zdjęcia" + phone icon.

## Imagery

Real photos of the owner's own items and jobs only (first photos: own stroller, sofa, car). Natural light, close-ups of fabric texture, honest before/after pairs at the same angle. No stock photos of people.

## Motion

Subtle and fast: 150–250 ms, ease-out for entering, no motion on load beyond a single fade. Always respect `prefers-reduced-motion`.

## Changelog

- 2026-11-08 — Created from the approved stroller mockup.
