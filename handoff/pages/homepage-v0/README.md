# Homepage v0: `/` (early launch)

## 1. Tag and status
**DRAFT, not approved, not tagged.** Intended tag `homepage-v0-v1` after the owner's "go". Designed against `docs/design-constraints.md` in cleaning-sell-system (Nuxt 4, Nuxt UI v4, Tailwind v4 tokens, Lucide, light only, CSS-only motion) and `DESIGN.md` here. **No Figma** (as for the stroller page). Replaces the "Wkrótce otwieramy" placeholder at `/`. Not the full homepage (PRD S1); that gets its own brief.

**Pending brand issue [#6](https://github.com/Yariandres/cleaning-design/issues/6):** the H1, the voice line, "wkrótce", the promise line "2–3 zdjęcia wystarczą. Cenę podamy dziś." and "na WhatsApp" use the wording of `stroller-v1.2` as a placeholder. If #6 changes it, only strings in `copy.md` change.

## 2. Issues
SEO brief [cleaning-design #7](https://github.com/Yariandres/cleaning-design/issues/7) ([brief](https://github.com/Yariandres/cleaning-seo/blob/main/seo/briefs/homepage-v0.md)) · early launch #5 item 2 · developer [#8](https://github.com/Yariandres/cleaning-sell-system/issues/8), checklist [#10](https://github.com/Yariandres/cleaning-sell-system/issues/10) · PRD S1 only in part (no outcome menu, packages, proof, FAQ).

## 3. Visuals
`screens/`: `01`–`04` default at 390 / 1440 / 768 / 1024 · `05`–`06` first screen · `07`–`08` cookie banner open · `09`–`10` a second service has shipped · `11`–`12` end of page above the sticky bar / cookie banner · `13` 320 · `og-80-test.png` (the rejected 80px share image) · `checks.json`. Working reference: `prototypes/homepage-v0/index.html` (`python3 prototypes/homepage-v0/build.py`). Share image: `assets/og-nowiutko-1200x630.png`.

## 4. Sections in order
1. **Header**: the stroller page's header, unchanged (logo → `/`, phone as text, WhatsApp button from 900px). No menu.
2. **Hero** (`primary-50`): H1 as the headline, voice line, lede, WhatsApp button + outline "Zadzwoń: 736 369 704", one muted promise line. From 900px the logo badge (`mark.svg`, decorative, `alt=""`, 300–340px) sits on the right; below 900px it is hidden.
3. **Co pierzemy** (H2): the bookable card and the coming-services panel (below).
4. **Jak to działa** (H2): three steps, the stroller page's `.steps` styling.
5. **Gdzie dojeżdżamy** (H2, `neutral-100` band): one display line and one sentence.
6. **Final CTA**: the stroller page's component, unchanged (id `kontakt`).
7. **Footer**: shared component, unchanged. Sticky phone bar below 900px, cookie banner: unchanged.

**Services block.** Bookable card: Eyebrow-less white card (`rounded-2xl`, 1px `neutral-200`), chip "Dostępne teraz" (`secondary-100` / `secondary-800`, 6.7:1), H3 with the single `<a>`. A `::after` on the link stretches over the card, so the whole card is clickable while the anchor text is only the service name. Focus: the ring is drawn on the card (`:has(a:focus-visible)`, 3px `neutral-900`, 3px offset), not on the text. Hover: lift 2px + shadow, 200ms, none under reduced motion; "Cennik i szczegóły →" is a decorative line (`aria-hidden`).
**Coming panel:** `neutral-100` panel, `<ul>` of rows 56px tall: name left, text pill "wkrótce" right (`neutral-700` on white, 1px `neutral-300`). No `<a>`, no heading, no paragraph, no price, no arrow, default cursor, no hover. Not tiles, so nothing reads as clickable.
**When a counter ships** (`screens/09`–`10`): its row loses the pill and becomes one `<a>` row (`primary-600`, 700, underlined on hover, arrow); descriptive anchor text from that counter's SEO brief. Nothing else changes. (The sofa link in the state frames is an illustration only.)

## 5. Data bindings
`{business:phone}`, `{business:whatsapp}` (header, hero, final, footer, sticky); footer company keys as in `components/footer.md` (**placeholders in the prototype, never ship them**); `{zones:featured}` (see copy.md; nominative). Service rows: ideally from the services data (`bookable` flag → card/link row, otherwise "wkrótce" row), so a shipped counter needs no template change. No prices on the page.

## 6. States
Default; cookie banner open (reserves its height, as on the stroller page); a service goes live; 320–1440. Empty/loading/error: none (static page). No-JS: everything is server HTML.

## 7. Accessibility
One H1; H2 Co pierzemy / Jak to działa / Gdzie dojeżdżamy / final CTA; H3 for the card title and the steps; no headings in the footer or per coming service. Skip link "Przejdź do usług". Tab order: skip link, logo, phone, WhatsApp (header), hero WhatsApp, hero call, stroller card, final WhatsApp, call, SMS, footer rows, Prywatność, Ustawienia cookies. Automatic checks (`checks.json`, 13 frames): 0 issues; lowest text contrast 5.36:1; no horizontal scroll 320–1440; the card is the tap target (full card ≥ 44px); keyboard ring on every stop; reduced motion honoured.

## 8. Assets and licences
Only the owner's logo/mark SVGs and generated HTML text; no photos, no stock, no icons beyond Lucide `camera`, `phone`, `arrow-right`. Share image: own design (flower from the logo), PNG 61 KB.

## 9. SEO (brief §2–§9)
`<html lang="pl-PL">`, title and description as in `copy.md` (no suffix), canonical `https://nowiutko.pl/`, indexable, OG tags in the prototype's `<head>`; JSON-LD per brief §7 is the developer's (LocalBusiness + WebSite, no alternateName/SearchAction). The stroller link is a normal `<a href>` in the server HTML with the service name as text. Not present: FAQ, reviews, before/after, packages, hours, social icons, links to pages that do not exist (the checker fails on any other target).

## 10. Open questions
- Owner: registered name and NIP (footer); whether "Cenę podamy dziś" holds evenings/Sundays (brand #6).
- Developer: can the services block read a `bookable` flag, or should the template list them by hand until the next counter?
- Developer: `:has()` focus ring on the card is fine for your browser targets? (Fallback: ring on the title link.)
- Share image: static PNG for launch, as for the stroller page.

## Answers to the SEO brief §10 (draft comments for #7, not posted)
See the report to the owner; kept out of the developer README on purpose.
