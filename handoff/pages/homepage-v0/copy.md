# Copy: homepage v0 (`/`)

DRAFT, not approved. Wording of the H1, hero lines, "wkrótce" and the promise line is **pending brand issue [#6](https://github.com/Yariandres/cleaning-design/issues/6)** (placeholder: the wording of `stroller-v1.2`). `{...}` = data.

## Head
- `meta.title` — Nowiutko – pranie tapicerki, wózków i aut u Ciebie | Poznań *(59; no site-name suffix)*
- `meta.description` — Nowiutko: pierzemy wózki dziecięce i foteliki samochodowe u Ciebie w domu, w Poznaniu i okolicach. Wkrótce także kanapy, materace, dywany i wnętrza aut. *(152)*
- `og.title` (meta tag) — Nowiutko – pranie tapicerki, wózków i aut u Ciebie · `og:description` = description · `og:image` = `https://nowiutko.pl/og-nowiutko-1200x630.png`

## Hero
- `hero.h1` (real `<h1>`, the headline itself; "Nowiutko" in `primary-500`) — Nowiutko – pranie tapicerki, wózków i aut u Ciebie w Poznaniu i okolicach
- `hero.voice` (`<p>`) — Świeżo i jak nowe — bez wychodzenia z domu.
- `hero.lede` — Przyjeżdżamy z własnym sprzętem i pierzemy u Ciebie, na miejscu. Na początek: wózki i foteliki samochodowe.
- Buttons: `cta.whatsapp` (solid) · `cta.call` "Zadzwoń: {business:phone}" (outline) — both as in `stroller-v1.2` copy.md
- `hero.promise` — 2–3 zdjęcia wystarczą. Cenę podamy dziś. *(same line as stroller `hero.card.promise`)*

## Co pierzemy (H2)
- `services.eyebrow` — Usługi · `services.h2` — Co pierzemy
- `services.lede` — Dziś umawiamy pranie wózków i fotelików. Kolejne usługi dodajemy po kolei.
- Bookable card: chip *Dostępne teraz* · **H3 with the only `<a>`**: *Pranie wózków i fotelików* → `/poznan/pranie-wozkow-i-fotelikow` · text *Wózki spacerowe, gondole, 2w1 i 3w1 oraz foteliki samochodowe. Cenę podajemy ze zdjęć, zanim przyjedziemy.* · decorative line *Cennik i szczegóły →* (`aria-hidden`, not a link of its own; the whole card is clickable through the title link)
- `services.soon.label` — Kolejne usługi (a `<p>`, not a heading)
- Coming rows, text only: Kanapy, narożniki i fotele · Materace · Dywany · Tapicerka samochodowa (wnętrze auta); each followed by the text pill `services.soon.tag` = **wkrótce**

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
- `og.line` — Poznań i okolice · bez wychodzenia z domu *(stacked on two lines in the image, no dot)*
- `og.alt` — Nowiutko: pranie tapicerki, wózków i aut u Ciebie. Poznań i okolice.
