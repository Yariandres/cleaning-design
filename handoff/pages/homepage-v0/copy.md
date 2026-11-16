# Copy: homepage v0 (`/`)

DRAFT, not approved. Brand decisions applied 2026-11-17 (#6, #7): H1/title approved with the em dash (—) of `docs/brand.md`; "wkrótce" is gone, replaced by "Wycena na WhatsApp" (owner); "na WhatsApp" on buttons; hours line. `{...}` = data.

## Head
- `meta.title` — Nowiutko — pranie tapicerki, wózków i aut u Ciebie | Poznań *(59; no site-name suffix)*
- `meta.description` — Nowiutko: pierzemy wózki, foteliki, kanapy, materace, dywany i wnętrza aut u Ciebie w domu, w Poznaniu i okolicach. Cena ze zdjęć na WhatsApp. *(≤155)*
- `og.title` (meta tag) — Nowiutko — pranie tapicerki, wózków i aut u Ciebie · `og:description` = description · `og:image` = `https://nowiutko.pl/og-nowiutko-1200x630.png`

## Hero
- `hero.h1` (real `<h1>`, the headline itself; "Nowiutko" in `primary-500`) — Nowiutko — pranie tapicerki, wózków i aut u Ciebie w Poznaniu i okolicach
- `hero.voice` (`<p>`) — Świeżo i jak nowe — bez wychodzenia z domu.
- `hero.lede` — Przyjeżdżamy z własnym sprzętem i pierzemy u Ciebie, na miejscu: wózki, foteliki, kanapy, materace, dywany i wnętrza aut.
- **Story board (right side, decorative; whole block `role="img"`):** `story.alt` — Trzy kroki: zaplamiony wózek, zdjęcia wysłane w rozmowie na WhatsApp, wózek jak nowy.
  - `story.1` — Plama na wózku · `story.2.label` — Przykład: tak wygląda rozmowa · `story.3` — Wózek jak nowe
  - Strip below 900px (aria-hidden): `strip.1` — Plama · `strip.2` — Zdjęcia · `strip.3` — Jak nowe
  - Non-breaking spaces after single-letter words everywhere (H1: "u Ciebie", "w Poznaniu", "i okolicach")
  - Chat example (hard-coded illustration, not data; no name, no time, no rating): header *Nowiutko / WhatsApp*; customer bubble = two photo thumbnails (neutral image icons) + *Dzień dobry, proszę o wycenę wózka.*; reply bubble = *Dziękujemy! Cenę podamy dziś.* + `hours`.
  - Nothing essential lives only in the board: the same facts are in the lede, the promise line, the hours line and "Jak to działa".
- Buttons: `cta.whatsapp` (solid) · `cta.call` "Zadzwoń: {business:phone}" (outline) — both as in `stroller-v1.2` copy.md
- `hero.promise` — 2–3 zdjęcia wystarczą. Cenę podamy dziś. *(approved in voice)*
- `hours` — Odpisujemy pn–pt 9:00–17:00, sob 9:00–14:00 *(`{business:hours}`; under the promise line and under the final CTA buttons)*

## Co pierzemy (H2)
- `services.eyebrow` — Usługi · `services.h2` — Co pierzemy
- `services.lede` — Wybierz, co chcesz odświeżyć. Cenę podajemy ze zdjęć, zanim przyjedziemy.
- Page card: chip *Wózki i foteliki* · **H3 with the `<a>`**: *Pranie wózków i fotelików* → `/poznan/pranie-wozkow-i-fotelikow` · text *Wózki spacerowe, gondole, 2w1 i 3w1 oraz foteliki samochodowe. Cennik i pakiety na osobnej stronie.* · decorative line *Cennik i szczegóły →* (`aria-hidden`)
- `services.other.label` — Pozostałe usługi (a `<p>`)
- Rows, each ONE link to the WhatsApp action (no page): the link text is the service name, a separator and the label `services.wa` = **Wycena na WhatsApp**, e.g. "Kanapy, narożniki i fotele — Wycena na WhatsApp" (the dash is visually hidden text; the label is shown with a Lucide `message-circle`). Services: Kanapy, narożniki i fotele · Materace · Dywany · Tapicerka samochodowa (wnętrze auta).
- Link: `https://wa.me/{business:whatsapp}?text=` + `whatsapp.prefill.service`: *Dzień dobry, proszę o wycenę prania {object}. Wysyłam zdjęcia. Miejscowość:␣* with `{object}` per service: kanap, narożników lub foteli · materaca · dywanu · tapicerki samochodowej (wnętrza auta). The object is a data field of the service (genitive).
- No heading, paragraph or price per service row.

## Jak to działa (H2)
- `steps.eyebrow` — Trzy kroki, zero wychodzenia z domu · `steps.h2` — Jak to działa
- 1 **Wyślij zdjęcia** — 2–3 zdjęcia przez WhatsApp lub SMS. Napisz, gdzie mieszkasz.
- 2 **Dostań cenę i termin** — Zwykle w kilka minut. *(short form: the stroller page's "Wolne terminy często już na następny dzień" is left out)*
- 3 **Pierzemy u Ciebie** — Przywozimy sprzęt i środki. Potrzebujemy tylko wody i gniazdka.

## Gdzie dojeżdżamy (H2)
- `area.eyebrow` — Obszar działania · `area.h2` — Gdzie dojeżdżamy
- `area.line` (`<p>`) — Poznań i powiat poznański.
- `area.lede` — Jeździmy po całym powiecie, na przykład: `{zones:featured}`. Napisz, gdzie mieszkasz, a potwierdzimy dojazd.
- `{zones:featured}` = first 5 towns of Strefa 1 by sort order, excluding Poznań, **in the nominative**, comma separated (prototype: Swarzędz, Luboń, Suchy Las, Komorniki, Plewiska). Nominative on purpose: data holds no declined forms. No prices or zone names on the homepage.

## Final CTA, footer, sticky bar, cookie banner
Unchanged components from `stroller-v1.2`: `final.h2`, `final.text`, `cta.whatsapp`, `cta.call`, `cta.sms`; footer (`footer.*`); phone sticky bar; cookie banner. WhatsApp prefill stays the stroller one ("…wózka lub fotelika…").

## Share image
- `og.title` — Pranie tapicerki, wózków i aut u Ciebie *(non-breaking spaces after "i" and "u")*
- `og.line` — Poznań i okolice · bez wychodzenia z domu *(the homepage keeps its own line)* *(stacked on two lines in the image, no dot)*
- `og.alt` — Nowiutko: pranie tapicerki, wózków i aut u Ciebie. Poznań i okolice.
