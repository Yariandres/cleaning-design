# Footer (shared: counters, homepage v0, quote form)

> **DRAFT — awaiting the owner's approval (2026-11-16).** Part of the draft `stroller-v1.2`. Do not build from this until it is tagged.

One footer for every public page. It replaces the one-line footer of `stroller-v1.1`. Owner priority [cleaning-design #5](https://github.com/Yariandres/cleaning-design/issues/5), scope item 4 ("company details, privacy link, Ustawienia cookies").

- **Reference:** `prototypes/stroller/final/stroller-counter.html` (`<footer class="site-f">`), styles in `prototypes/stroller/build_final.py` (`FINAL_CSS`, the block marked "footer (v1.2)").
- **Screens** (`handoff/pages/stroller-counter/screens/`): `15`–`18` default at 390 / 1440 / 768 / 1024 · `19`–`22` and `28` every field present and long at 390 / 1440 / 768 / 1024 / 320 · `23`–`24` no company details · `25` end of the page above the phone sticky bar · `26`–`27` end of the page above the open cookie banner.
- No new tokens, colours or icons.

## What it is for
A quiet place for who runs the site and how to reach them. It is **not navigation** and it has **no button**: counters have one action and no menu, and the footer must not compete with it. It contains no link to another page of the site except the privacy page.

## Anatomy

| Part | Content | Source |
|---|---|---|
| Brand | Logo (`handoff/brand/logo/logo.svg`, 36px tall, **not a link**: the header logo already goes home) and two short lines: the descriptive tagline and the area | copy `footer.tagline`, `footer.area` |
| Kontakt | Label (Eyebrow) + rows "Telefon", "WhatsApp", optional "E-mail". Each row is one link, 44px tall: a muted key and the value in 700 `neutral-900` | `{business:phone}`, `{business:whatsapp}`, `{business:email}` |
| Dane firmy | Label (Eyebrow) + legal name (700), optional address (1–2 lines) with one note line, then "NIP …" and optional "REGON …" | `{business:legal-name}`, `{business:address-line1}`, `{business:address-line2}`, `{business:nip}`, `{business:regon}` |
| Legal row | Above it a 1px `neutral-200` rule. "Prywatność" (link) and "Ustawienia cookies" (`<button>`, reopens the cookie banner, as already built for #46). Only links whose pages exist | copy `footer.privacy`, `cookies.settings` |

No copyright line, no social icons, no service links, no opening hours (none are decided; see open questions).

## Data
The company keys are **new**. The admin "Firma" screen (`admin-cennik-v1`, frame 26) holds only `phone`, `whatsapp`, `minOrder`, `maxVisitsPerDay`, `minNoticeHours`; these follow the same naming.

| Binding (page) | Field name (suggested) | Required | Shown as |
|---|---|---|---|
| `{business:phone}` | `phone` | yes (exists) | "736 369 704", `tel:+48…` |
| `{business:whatsapp}` | `whatsapp` | yes (exists) | the number, link = **the page's own WhatsApp link** (same `wa.me` link and prefill as the page's buttons) |
| `{business:email}` | `email` | no | `mailto:` |
| `{business:legal-name}` | `legalName` | yes, for the block to show | one text line, may wrap to 2–3 lines |
| `{business:nip}` | `nip` | yes, for the block to show | "NIP 0000000000" (owner's formatting, never broken across lines) |
| `{business:regon}` | `regon` | no | "REGON …" after the NIP, wraps under it when narrow |
| `{business:address-line1}`, `{business:address-line2}` | `addressLine1`, `addressLine2` | no | two lines, plus the note `footer.address-note` |

**The values are not known yet.** In the prototype every unknown is a bracketed, dashed placeholder (class `.tbd`). That style is prototype-only. **A placeholder never ships.**

## Rules for missing values
- An optional value that is empty removes its own line (e-mail row, REGON, address **together with its note**).
- If the legal name **or** the NIP is empty, the whole "Dane firmy" block is left out (`23`, `24`) and the grid closes up. The footer is still complete without it.
- "Prywatność" follows the developer's existing rule: left out while the page does not exist. "Ustawienia cookies" is left out if the banner cannot be reopened.
- With WhatsApp on the same number as the phone, both rows still show: the second row says that WhatsApp works on this number.

## Layout
| Width | Grid |
|---|---|
| < 640 | one column: brand, Kontakt, Dane firmy, legal row; 28px between blocks |
| 640–899 | brand across the top; Kontakt and Dane firmy side by side (1fr 1fr, 40px gap) |
| ≥ 900 | three columns 1.25fr / 1fr / 1.25fr, 56px gap; without company details 1.25fr / 2.25fr |

- Background: the page (`neutral-50`), 1px `neutral-200` top border (visible when the section above is light). Padding 40px top / 20px bottom below 900px, 56px / 24px from 900px. Legal row: 28px above, the rule, 8px, then the 44px controls.
- Type: Figtree, 0.9rem (14.4px at 390, 15.3px from 640), `neutral-500`; values 700 `neutral-900`; legal name 700 `neutral-700`; legal controls 600 `neutral-700`, underlined. Labels are the Eyebrow component, written as `<p>`, **not headings** (the page's heading outline and the SEO brief's H2 order stay untouched).
- Long values wrap inside their column (`overflow-wrap: anywhere`, `min-width: 0`); nothing is truncated. NIP and REGON never break inside the number.
- Contact key column: fixed 5.5rem, so the values line up.

## Behaviour
- Row hover: the value gets a 2px underline in 200ms (same as text links elsewhere); none under reduced motion. No other motion.
- Focus: the standard ring (3px `neutral-900`, 3px offset) on the two contact rows, the privacy link and the cookies button.
- **The last line must always be reachable.**
  - Phone sticky bar: the page reserves `76px + env(safe-area-inset-bottom)` below 900px. **Changed from v1.1** (was a flat 76px; the bar itself grows by the inset, so on a phone with a home indicator the last line could sit under it).
  - Cookie banner open: the page reserves the **banner's height** at the bottom (the prototype sets `--cookie-h` from the banner with a few lines of script and uses it as `padding-bottom` and in `scroll-padding-bottom`). In `stroller-v1.1` the open banner covered the end of the page. Frames `26`, `27`.
- Tab order: Telefon → WhatsApp → (E-mail) → Prywatność → Ustawienia cookies, after the page's last control and before the sticky bar.
- Click hooks as on the page: `data-cta="phone|whatsapp"`, `data-cta-pos="footer"`.

## Accessibility
- `<footer>` landmark; contact block in `<address>`; legal row in `<nav aria-label="Informacje">`.
- Logo `alt="Nowiutko"` (it starts the tagline sentence); not focusable.
- Contrast: `neutral-500` on `neutral-50` 5.5:1, `neutral-700` 8.7:1, `neutral-900` 13.4:1, Eyebrow `primary-600` on `neutral-50` 7.7:1.
- All four controls ≥ 44px tall at 320–1440 (`checks.json`).

## On other pages
- **Homepage v0:** the same component, unchanged. Its WhatsApp row uses the homepage's own WhatsApp link. No extra columns for v0.
- **Quote form:** the same component; the estimate bar reserves its own space the same way the sticky bar does.
- When more pages exist (price list, service area, terms), they join the **legal row** or get a "Usługi" column in a new version of this component. Not now: no dead links.

## Open
See the stroller README, section 10 (which company fields the owner wants public; the address; the note wording; where the company fields are edited).
