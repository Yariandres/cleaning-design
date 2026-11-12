# References (mood board)

Snapshot of the owner's Pinterest board, saved locally so the design agent never depends on Pinterest being reachable.

- Board: <https://pin.it/6mp7nntgy> (private board "Nowiutko — design references", `https://www.pinterest.com/yshirts/nowiutko-design-references/`)
- Board description (the owner's words): *"Calm, airy, clean and warm. A light, sunny home, not a hospital or a laboratory."*
- Last synced: **2026-11-12** — 210 pins, 11 sections, all downloaded (736 px wide).

## What is in this folder

| Path | What |
|---|---|
| `<section>/NN-xxxxxx.jpg` | One image per pin. `NN` = position in the section as saved, `xxxxxx` = last 6 digits of the Pinterest pin id |
| `INDEX.md` | Every pin: image, source site, the poster's own title |
| `pins.json` | The same, plus the poster's description, alt text, Pinterest URL, and an empty `owner_note` field per pin |

Sections: `mood` 19 · `colour` 10 · `logo` 7 · `type` 10 · `landing-pages` 11 · `mobile-booking` 14 · `photo-style` 44 · `icons` 24 · `page-details` 28 · `admin` 24 · `not-this` 19. (There is no separate "print" section on the board.)

**About notes.** The owner wrote no notes on the pins (confirmed 2026-11-12). 81 pins are the owner's own uploads with no text; the other 129 carry only the original poster's description. So there is no "why I saved it" per pin. The patterns below are read from the images and the section names. If the owner wants to add a note to a pin, put it in `owner_note` in `pins.json`.

**Licensing.** These are other people's images (some stock, one with a visible Dreamstime watermark). They are for private study only. Nothing here may be copied into the site, a logo, a share image or a handover. **This repo is public**, so the image files are kept out of git until the owner decides (see the hand-over note); `INDEX.md` and `pins.json` link to the sources instead.

Rules:
- References inspire; `DESIGN.md` decides. If a reference fights the tokens, propose a DESIGN.md change instead of quietly drifting.
- Never copy a reference's logo, illustrations, photos or copy into the site.

## Patterns per section

### Mood (19)
**Sees:** sunlit rooms with sheer curtains and long window light on pale wood floors; cream, sand and warm white; a few green plants; chamomile in a pot, daisy meadow, tea with honey. Soft and uncluttered, almost no saturated colour.
**Takes:** the feeling of *light on a clean surface*. Imagery and spacing should look airy, with lots of empty space and a warm tint in the light. Chamomile and honey tea support the symbol.
**Notes:** these rooms are polished renderings (several look AI-generated, and 01 and 18 are the same image). Real customer photos will not look like this, so use the board for light and colour, not as a photo target.

### Colour (10)
**Sees:** mint and pale green; deep teal with marigold or lemon yellow; sage with cream; coastal mint with sunset yellow (10); daisies on cream (05).
**Takes:** it matches the contract: mint-to-teal as the fresh base with one warm yellow. The strongest matches are 06, 07 and 10 (teal plus yellow). Greens with a yellow-green tint (02, 04) are a good basis for the per-service accents.
**Notes:** mint and sage are used very pale on the board; DESIGN.md's teal `#0E6E5C` is darker and more serious than most of these pins. Worth a look when the 50–950 scales are built.

### Logo and symbol (7)
**Sees:** fine one-weight line drawings of single flowers (01–03); daisy with a small yellow centre and text on a curve (04–06); a chamomile with a dotted ring (07).
**Takes:** a single-line, hand-drawn chamomile with a *yellow centre as the only colour* is the clearest direction. Thin lines need care at favicon size.
**Notes:** 04–06 are one concept repeated, and 01–03 are other brands' marks. Study only; no shape or arrangement should be copied. Text on a circle (04–07) and thin strokes will not survive the small sizes needed for the favicon, app icon and Facebook avatar.

### Typography (10)
**Sees:** bold, rounded or geometric sans with friendly details (allio, kaige, freshwost, Ragick, kocha); one serif display (Reigo); a plain sans (Space Grotesk, 10); a furniture shop using chunky display type (01).
**Takes:** a friendly, slightly rounded display sans with a confident weight. Bricolage Grotesque is in that family and stays a good fit.
**Flag:** pin 10 is **Space Grotesk**, which DESIGN.md bans.

### Service landing pages (11)
**Sees:** pricing pages in tiers (01–05); cleaning-service pages with icon grids (06, 07); decor and painting sites with large rounded images and pill buttons (08–11); FAQ blocks under pricing (02, 03).
**Takes:** big headline, a visible price block directly under it, icon grid for what's included, FAQ lower down. Rounded cards and pill buttons match the contract.
**Notes:** 3-column SaaS pricing (01–05) suits our *packages* (Rodzinny and the others), not the per-item price list, which should stay a simple list as in the approved mockup.

### Mobile quote and booking flow (14)
**Sees:** photo upload zone (04–06); date and time pickers (02, 03); calculator that ends in a big "You pay" card (07–10); stepper and timeline for progress (11–14); one dark form page on purple (01).
**Takes:** upload-first form with a drop zone and thumbnail row; one clear step at a time with a visible progress bar; a result card with a large price at the end; a timeline for order status.
**Notes:** all of these exist in Nuxt UI (file upload, calendar, stepper, timeline), so they stay within the dev constraints. Pin 01's purple gradient and the blue-purple of 02, 03 do not fit the palette.

### Photo style (44)
**Sees:** warm sofas in daylight (05–12); hands doing the work in close-up: gloves, steam, vacuum nozzle, cloth on leather (02, 03, 13–24); fabric macros (33–37); strollers in real life, a baby under the hood (25–32); before and after of sofas and cars (38–44).
**Takes:** close-ups of the *work and the material*, natural light, hands rather than faces, matching before-and-after angles, fabric texture as a recurring motif.
**Flags:** 26, 27, 29, 30, 32 show people (a baby, parents). Our rules allow no photos of people we have no rights to, and no stock people, so use them only as a mood. 02, 04, 39 and 41 are advertising layouts with logos or sparkle effects, and 39 is a composite. Several before-and-after pins use a split image with BEFORE / AFTER labels, which is fine as a pattern but we use only real jobs.

### Icons and illustration (24)
**Sees:** single continuous-line drawings of dogs, cats and paws (01–13); strollers as bold outline drawings (14–17); small line icons on pastel circles (18–24).
**Takes:** icons in one thin line weight with round ends, a heart or small accent inside, a soft tinted circle behind each, one per service. The strollers at 14–17 are a useful reference for the stroller icon's silhouette (hood, basket, wheels).
**Flag:** the continuous-line animal drawings cannot be reduced to a 24 px, 2 px stroke Lucide-style icon. They fit as larger spot illustrations (SVG), not as the service icons; the service icons should follow Lucide's stroke (see "Flags" below).

### Page details (28)
**Sees:** WhatsApp button assets (01–03); pricing comparison tables (04–13); floating pill navigation bars with a blurred background (14–18, 24); testimonial and rating cards (19–23, 25, 26); FAQ accordions (27, 28).
**Takes:** floating rounded bar for the phone's sticky "Wyślij zdjęcia" action; accordion FAQ with a plus sign, as in the mockup; one green WhatsApp action next to the main button.
**Flags:** 19–26 are *reviews and star ratings*. Per the brief and SEO issue #2 they must stay hidden until real reviews exist, so we design the slot but not these contents. The WhatsApp mark (01–03) is a third-party brand icon. Lucide has none, so it needs a custom SVG or a plain "message" icon with a text label. Pills with blur (14–18) are a visual extra, not a requirement.

### Owner admin, phone (24)
**Sees:** calendars and day timelines (07–12, 15, 22); order lists with status chips (17); task lists (19, 21); service-marketplace home screens (01–05); dashboards (20, 23).
**Takes:** a "Today" screen as a vertical timeline of jobs, status as small coloured chips, a bottom tab bar, large tap targets, calm background with white cards.
**Notes:** most are pastel purple or blue and some are dark; ours stays mint/teal, light only. The admin is phone-first, so 390 px comes first.

### NOT this (19)
**Sees:** smiling cleaners in aprons and yellow gloves (01–08); bubble backgrounds (09, 12–14); loud blue gradients; "sparkle" logos and stars (15–19); a before/after promo in green (11).
**Takes:** it confirms the brief: no stock cleaners, no bubbles or sparkles, no saturated blue, no cleaning-supplies clip-art, no starburst logos.
**Notes:** pin 03 and 05 show tidy home interiors behind the cleaner. The room is fine, the posed cleaner is the problem.

## Clashes with DESIGN.md and the dev constraints

| # | Where | Clash | Suggestion |
|---|---|---|---|
| 1 | Type 10 | Space Grotesk is on the board, DESIGN.md says never use it | Keep the ban; note it in DESIGN.md as a deliberate exclusion |
| 2 | Mood vs Colour | The mood pins are warm cream, sand and wood; our paper is cool mint-white `#F5FAF8` | Keep the mint paper, allow warmth in photos and in the yellow; owner to confirm |
| 3 | Photo style | Several pins show people; brief and web-designer rules: no stock people, no photos of people without rights | Use as mood only; real photos will be hands, items, and results |
| 4 | Page details 19–26 | Reviews and star ratings | Design the slot only, hidden until real reviews exist (SEO issue #2) |
| 5 | Page details 01–03 | WhatsApp brand icon vs "Lucide only for UI icons" | Ask the developer to allow one brand SVG, or use a text-only WhatsApp button |
| 6 | Icons 01–17 | Continuous-line and bold outline drawings vs "24 px grid, single colour, 2 px stroke like Lucide" | Service icons follow Lucide's stroke; keep the line-art style for larger spot illustrations |
| 7 | Page details 14–18 | Blurred floating bars | Allowed as CSS, but must stay legible without blur and keep 44 px targets |
| 8 | Mobile booking 01–03, admin | Purple, blue and dark UIs | Take layouts only, recolour to the palette; no dark frames needed |
| 9 | Mood, photo style | Many images are AI-rendered | Do not use them as a photo target; real photos come from the owner |
| 10 | Whole folder | The images are third-party and **this repo is public** | Keep images out of git until the owner decides (see hand-over) |
