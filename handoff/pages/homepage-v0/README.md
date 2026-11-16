# Homepage v0: `/` (early launch)

## 1. Tag and status
Tag `homepage-v0`, approved by the owner on 2026-11-17. Designed against `docs/design-constraints.md` in cleaning-sell-system (Nuxt 4, Nuxt UI v4, Tailwind v4 tokens, Lucide, light only, CSS-only motion) and `DESIGN.md` here. **No Figma** (as for the stroller page). Replaces the "Wkrótce otwieramy" placeholder at `/`. Not the full homepage (PRD S1); that gets its own brief.

**Brand decisions applied 2026-11-17** ([#6](https://github.com/Yariandres/cleaning-design/issues/6), [#7](https://github.com/Yariandres/cleaning-design/issues/7)): H1 and title approved (em dash as in `docs/brand.md`); the owner replaced "wkrótce" with **"Wycena na WhatsApp"** (sofas, mattresses, rugs and car interiors are taken by hand; no page link); buttons "na WhatsApp"; hours line "Odpisujemy pn–pt 9:00–17:00, sob 9:00–14:00" under the hero promise and the final CTA buttons.

## 2. Issues
SEO brief [cleaning-design #7](https://github.com/Yariandres/cleaning-design/issues/7) ([brief](https://github.com/Yariandres/cleaning-seo/blob/main/seo/briefs/homepage-v0.md)) · early launch #5 item 2 · developer [#8](https://github.com/Yariandres/cleaning-sell-system/issues/8), checklist [#10](https://github.com/Yariandres/cleaning-sell-system/issues/10) · PRD S1 only in part (no outcome menu, packages, proof, FAQ).

## 3. Visuals
`screens/`: `01`–`04` default at 390 / 1440 / 768 / 1024 · `05`–`06` first screen · `07`–`08` cookie banner open · `09`–`10` a second service has shipped · `11`–`12` end of page above the sticky bar / cookie banner · `13` 320 · `og-80-test.png` (the rejected 80px share image) · `checks.json`. Working reference: `prototypes/homepage-v0/index.html` (`python3 prototypes/homepage-v0/build.py`). Share image: `assets/og-nowiutko-1200x630.png`.

## 4. Sections in order
1. **Header**: the stroller page's header, unchanged (logo → `/`, phone as text, WhatsApp button from 900px). No menu.
2. **Hero** (`primary-50`): H1 as the headline, voice line, lede, WhatsApp button + outline "Zadzwoń: 736 369 704", one muted promise line. The right side is the **story board** (below): three beats in icons, from 900px on the right (500–540px wide), below the text on phones and tablets.
3. **Co pierzemy** (H2): the bookable card and the coming-services panel (below).
4. **Jak to działa** (H2): three steps, the stroller page's `.steps` styling.
5. **Gdzie dojeżdżamy** (H2, `neutral-100` band): one display line and one sentence.
6. **Final CTA**: the stroller page's component, unchanged (id `kontakt`).
7. **Footer**: shared component, unchanged. Sticky phone bar below 900px, cookie banner: unchanged.

**Story board** (`screens/14`–`18` hero at 390 / 1440 / 768 / 1024 / 320). Three beats in icons, no photos, read **1 → 2 → 3**:
- **From 900px: a vertical timeline** in the right column (500px, 540px from 1100px; fixed aspect ratio 500/640 and 540/640): card 1 "Plama na wózku" (stroller icon in `neutral-500` with `warning-400` stain dots, on `neutral-100`), the chat window (card 2, label "Przykład: tak wygląda rozmowa"), card 3 "Wózek jak nowe" (the stroller in `primary-700` with a small chamomile and two `secondary-500` sparkles, on `primary-100`). Round chips (44px, `neutral-900`, 4px `primary-50` ring: `frown`, `camera`, custom chamomile on `primary-500`) sit on a dashed 2px `neutral-300` line at the left edge, which links the beats. Why not three in a row: the column is 500px, so a chat window would be about 150px wide and unreadable; a vertical stack keeps the chat at full width and matches the height of the text column at 1024 and 1440.
- **Below 900px: a slim strip** (3 tiles + `arrow-right` connectors, about 96px tall, max 520px) directly under the voice line, so the story shows early: "Plama" → "Zdjęcia" → "Jak nowe" (stain stroller, a chat bubble, fresh stroller). Captions are one line, 12.8px bold (11.5px below 360px). The chat window itself comes after the hours line, so the H1, the WhatsApp button and the phone end at y 655 of 844 at 390 (above the sticky bar). Trade-off: the strip is decorative and aria-hidden, and the chat is further down; the first screen is a little longer than before (+~100px).
- Chat window: plain HTML/CSS, header with the logo mark ("Nowiutko / WhatsApp"), an outgoing `primary-100` bubble (two neutral image thumbnails, one line), an incoming white bubble ("Dziękujemy! Cenę podamy dziś." and the hours line). No name, time, ticks, rating or input field; labelled as an example.
- Whole board = one `role="img"` with `story.alt`; the strip is `aria-hidden`; no essential text only inside. Static, no motion. Custom icons (stroller, line chamomile) on the 24px grid, `currentColor`, round caps, drawn at stroke 1.5 when large.
- **Line breaks:** `text-wrap: balance` on the H1 and voice line, `pretty` on the lede; non-breaking spaces after single-letter words (u, w, i, z, a, o) in all body text, and between "wnętrza" and "aut." Wording unchanged. The prototype adds them in `build.py` (`nb()`); in Nuxt do it in the strings (or a small text filter).
- **Deviations:** card 3 uses `primary` instead of the stroller accent (`secondary`, which looked dirty beside the stains); stains use `warning-400`; at 320 wide (frame size 320×640) the phone button ends at 679px, below that small frame's fold.

**Services block.** Page card: white card (`rounded-2xl`, 1px `neutral-200`), chip "Wózki i foteliki" (`secondary-100` / `secondary-800`, 6.7:1), H3 with the `<a>` to `/poznan/pranie-wozkow-i-fotelikow`; a `::after` on the link stretches over the card, so the whole card is clickable while the anchor text is only the service name. Focus ring on the card (`:has(a:focus-visible)`, 3px `neutral-900`, 3px offset). Hover: lift 2px + shadow, 200ms, none under reduced motion; "Cennik i szczegóły →" is decorative (`aria-hidden`).
**Other services panel** (`neutral-100`): `<ul>` of rows, each row **one `<a>`** to the WhatsApp action with the service in the prefilled message. Link text = service name + (visually hidden " — ") + "Wycena na WhatsApp", so it is never a bare "Wycena". The label is `primary-600` 700 with a Lucide `message-circle`, underlined on hover; the name is `neutral-700` 600. Rows are ≥ 56px tall (≥ 72px when the name wraps to two lines at 390px, label under the name) and span the whole panel width, so the tap target is the whole row. Contrast `primary-600` on `neutral-100` 7.2:1. No heading, paragraph or price per row.
**When a counter ships** (`screens/09`–`10`): its row becomes a link to the new page (`primary-600`, 700, arrow) with that counter's descriptive anchor text from its SEO brief; the WhatsApp label goes. The sofa link in the state frames is an illustration only.

## 5. Data bindings
`{business:phone}`, `{business:whatsapp}` (header, hero, final, footer, sticky, and the service rows), `{business:hours}`; footer company keys as in `components/footer.md` (**placeholders in the prototype, never ship them**); `{zones:featured}` (see copy.md; nominative). Service rows: ideally from the services data (has a page → card/link row to it, otherwise a WhatsApp row with the genitive `{object}` for the prefilled message), so a shipped counter needs no template change. No prices on the page.

## 6. States
Default; cookie banner open (reserves its height, as on the stroller page); a service goes live; 320–1440. Empty/loading/error: none (static page). No-JS: everything is server HTML.

## 7. Accessibility
One H1; H2 Co pierzemy / Jak to działa / Gdzie dojeżdżamy / final CTA; H3 for the card title and the steps; no headings in the footer or per coming service. Skip link "Przejdź do usług". Tab order: skip link, logo, phone, WhatsApp (header), hero WhatsApp, hero call, stroller card, final WhatsApp, call, SMS, footer rows, Prywatność, Ustawienia cookies. Automatic checks (`checks.json`, 13 frames): 0 issues; lowest text contrast 5.36:1; no horizontal scroll 320–1440; the card is the tap target (full card ≥ 44px); keyboard ring on every stop; reduced motion honoured.

## 8. Assets and licences
Only the owner's logo/mark SVGs and generated HTML text; no photos, no stock, no icons beyond Lucide `camera`, `phone`, `arrow-right`. Share image: own design (flower from the logo), PNG 61 KB.

## 9. SEO (brief §2–§9)
`<html lang="pl-PL">`, title (`Nowiutko — pranie tapicerki, wózków i aut u Ciebie | Poznań`, em dash) and description as in `copy.md` (no suffix); the description no longer says "wkrótce", canonical `https://nowiutko.pl/`, indexable, OG tags in the prototype's `<head>`; JSON-LD per brief §7 is the developer's (LocalBusiness + WebSite, no alternateName/SearchAction). The stroller link is a normal `<a href>` in the server HTML with the service name as text. Not present: FAQ, reviews, before/after, packages, hours, social icons, links to pages that do not exist (the checker fails on any other target; the service rows link to WhatsApp, not to pages).

## 10. Open questions
- Owner: registered name and NIP (footer); whether "Cenę podamy dziś" holds evenings/Sundays (brand #6).
- Developer: can the services block read "has a page" and a genitive `{object}` per service from the services data, or should the template list them by hand until the next counter?
- Developer: `:has()` focus ring on the card is fine for your browser targets? (Fallback: ring on the title link.)
- Share image: static PNG for launch, as for the stroller page.

## Answers to the SEO brief §10 (posted on #7)
1. H1 is the headline itself (em dash, "Nowiutko" in teal), voice line under it in a `<p>`. 2. Whole card clickable via a stretched title link; anchor text is "Pranie wózków i fotelików". 3. Counter header reused unchanged. 4. Area: a sentence with five towns from `{zones}` (nominative). 5. Share image: 80px gives 4 lines and the one-line `og.line` leaves the crop, so 64px with a two-line, dot-less line (final). 6. **Changed by the owner's decision (#7, 2026-11-17):** the other services are not "plain text, nothing clickable" any more. They are one-link rows to the WhatsApp action ("<service> — Wycena na WhatsApp"), in one muted panel. Still no link to a page that does not exist, no heading/paragraph/price per service, no Service/Offer structured data for them.
