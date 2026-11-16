# Copy: stroller counter

> **DRAFT `stroller-v1.2`:** the sections "Footer" and "Share image" below are new and await the owner's approval. Everything else is `stroller-v1.1`, unchanged.

**`stroller-v1.1` (approved by the owner on 2026-11-16): early launch without the quote form.** Changed keys are marked *(v1.1)*; everything else is as in `stroller-v1`. The one action is "Wyślij zdjęcia na WhatsApp"; the label is the same in every place.

Final Polish copy, keyed. `{...}` = comes from the database, never hard-coded. Voice: "Ty", short, concrete. **Wording of the H1 and hero is the brand strategist's call** (see README, open questions); the keys below hold the version in the approved design.

## Head
- `meta.title` — Pranie wózków i fotelików Poznań – u Ciebie, od 80 zł *(53 chars; the "80" comes from `{price:carseat}`)*
- `meta.description` — Pierzemy wózki, gondole i foteliki u Ciebie w domu, w Poznaniu i okolicach. Gotowe tego samego dnia. Cena ze zdjęć przed przyjazdem, od 80 zł. *(142 chars)*
- `meta.canonical` — https://nowiutko.pl/poznan/pranie-wozkow-i-fotelikow

## Header
- `header.phone` — `{business:phone}`, shown as **736 369 704**, link `tel:+48736369704` *(v1.1: real number)*
- `header.cta` — Wyślij zdjęcia na WhatsApp *(v1.1; the shared key `cta.whatsapp`)*

## Contact (v1.1, used by every button)
- `cta.whatsapp` — Wyślij zdjęcia na WhatsApp → `https://wa.me/{business:whatsapp}?text={whatsapp.prefill}` (`{business:whatsapp}` = `48736369704`)
- `whatsapp.prefill` — Dzień dobry, proszę o wycenę prania wózka lub fotelika. Wysyłam zdjęcia. Miejscowość:␣ *(ends with a space; URL-encoded in the link; page copy, not owner data)*
- `cta.call` — Zadzwoń: `{business:phone}` → `tel:`
- `cta.sms` — Nie masz WhatsAppa? Wyślij zdjęcia [SMS-em na ten sam numer](sms:+48736369704).

## Hero
- `hero.h1` (real `<h1>`, styled as eyebrow) — Pranie wózków i fotelików dziecięcych w Poznaniu i okolicach
- `hero.headline` (`<p class="display">`) — Wózek jak nowe. / Pod Twoim domem, tego samego dnia. *(second sentence in `primary-500`)*
- `hero.lede` — Przyjeżdżamy z własnym sprzętem. Ty nie wyjmujesz dziecka z domu, nie wozisz wózka i nie czekasz trzech dni.
- `hero.ticks` — Hipoalergiczne środki · Foteliki według instrukcji producenta · Dojazd gratis w Strefie 1
- `hero.card.eyebrow` — Cennik brutto
- `hero.card.sub` — cena ze zdjęć, przed przyjazdem
- `hero.card.rows` — Wózek spacerowy `{price:stroller-single}` · Wózek 2w1 `{price:stroller-2in1}` · Fotelik samochodowy `{price:carseat}` · Wózek 3w1 `{price:stroller-3in1}` (each "od N zł")
- `hero.card.nextslot` — Najbliższy wolny termin: `{nextFreeSlot.label}` *(v1.1: hidden for the whole early launch; never a timer)*
- `hero.card.cta` — `cta.whatsapp` *(v1.1; was "Wyślij 2–3 zdjęcia – cena dziś")*
- `hero.card.promise` — 2–3 zdjęcia wystarczą. Cenę podamy dziś. *(v1.1, new: one muted line under the button; it carries the promise the old button label had)*
- `hero.card.links` — Pełny cennik i pakiety (#cennik) · `cta.call` *(v1.1; was "Napisz na WhatsApp")*

## Proof bar (no heading)
1. **Tego samego dnia** — Rano pierzemy, po południu idziecie na spacer.
2. **U Ciebie w domu** — Własny sprzęt. Potrzebujemy wody i gniazdka.
3. **Według instrukcji producenta** — Foteliki: pasy tylko powierzchniowo.
4. **Poprawka gratis** — Jeśli coś wyjdzie po wyschnięciu, wracamy.

## Headache (H2)
- `headache.eyebrow` — Z czym przychodzą rodzice
- `headache.h2` — Dlaczego nie wyprać wózka samemu?
- `headache.lede` — Pralka i szczotka zostawiają zacieki na podszewce, a moczenie osłabia pasy. Dlatego robimy to inaczej.
- Cards (label "Problem" on each; "Co robimy." in bold):
  1. **Gondola żółta od oliwki** — Czyścimy podszewkę hipoalergicznym środkiem i odsysamy wodę, więc nic nie moczy się w pralce.
  2. **Fotelik po podróży** — Pokrowiec i skorupa według instrukcji producenta. Pasy tylko powierzchniowo.
  3. **Spacerówka po lecie** — Siedzisko, budka i szwy. Stelaż i koła są w cenie.
  4. **Drugie dziecko w drodze** — Cały zestaw po starszym rodzeństwie, gotowy na nowy początek. Link: "Pakiet Nowy Członek Rodziny od `{price:pack-new-member}`" → #cennik

## Price (H2)
- `price.eyebrow` — Cennik
- `price.h2` — Pranie wózka i fotelika – cena
- `price.lede` — Ceny brutto, z dojazdem w Strefie 1. Dokładną kwotę podajemy ze zdjęć, zanim przyjedziemy.
- Rows (name · description · price key): Wózek spacerowy · siedzisko, budka, pasy, stelaż i koła · `stroller-single` / Wózek 2w1 · gondola + spacerówka, stelaż i koła · `stroller-2in1` / Wózek 3w1 · z fotelikiem-nosidełkiem · `stroller-3in1` / Wózek bliźniaczy · `stroller-twin` / Fotelik samochodowy · pokrowiec, skorupa, baza · `carseat` / Krzesełko, leżaczek lub mata · `highchair`
- `price.note` — Minimalne zamówienie `{business:min-order}`. Przy silnych zabrudzeniach (pleśń, wymioty) wycenimy ze zdjęć przed przyjazdem. *(v1.1: the link "Pełny cennik" → `/cennik` is removed until that page exists)*
- Safety panel — eyebrow *Foteliki samochodowe*; h3 *Fotelik to sprzęt bezpieczeństwa. Tak go traktujemy.*; bullets: Pokrowiec i skorupę czyścimy według instrukcji producenta. / Pasy czyścimy tylko powierzchniowo, bo moczenie osłabia ich wytrzymałość. / Środki hipoalergiczne, bezpieczne dla niemowląt po wyschnięciu.
- Packages (price + struck-through earlier price from `{price:pack-*}` and `{price:pack-*-was}`): **Nowy Członek Rodziny** (tag *przed porodem*): Materac dwuosobowy, Wózek 2w1, Fotelik samochodowy · **Rodzinny** (tag *najczęściej wybierany*): Kanapa 3-osobowa, Wózek 2w1, Fotelik samochodowy · **Auto i Maluch** (tag *auto i maluch*): Pranie tapicerki auta, Wózek 2w1, Fotelik samochodowy. *The tag "najczęściej wybierany" is a claim: show it only if the owner's data says so (`{pack:*:badge}`).*

## Steps (H2)
- `steps.eyebrow` — Trzy kroki, zero wychodzenia z domu
- `steps.h2` — Jak to działa
- 1 **Wyślij zdjęcia** — 2–3 zdjęcia przez WhatsApp lub SMS. Napisz, gdzie mieszkasz. *(v1.1: "lub formularz" removed)*
- 2 **Dostań cenę i termin** — Zwykle w kilka minut. Wolne terminy często już na następny dzień.
- 3 **Pierzemy u Ciebie** — Przywozimy sprzęt i środki. Potrzebujemy tylko wody i gniazdka.
- `steps.cta` — `cta.whatsapp` *(v1.1; was "Wyślij 2–3 zdjęcia")*

## Before/after (hidden until real photos exist)
- `beforeafter.h2` — Wózki przed i po praniu · eyebrow *Efekty* · each pair with a one-line caption written by the owner. Data: `{beforeAfter:stroller}`.

## Car seats by brand (H2)
- `seats.eyebrow` — Foteliki według marek
- `seats.h2` — Foteliki Cybex, Maxi-Cosi, Britax i Avionaut – według instrukcji producenta *(only brands whose manuals the owner has checked: open item)*
- Bullets: Pokrowiec prany lub czyszczony tak, jak każe metka. / Skorupa i klamra przecierane łagodnym środkiem. / Pasy tylko powierzchniowo. Nigdy nie moczymy.
- Photo slot (4:3): own car-seat photo, no people.

## Reviews (hidden until real reviews exist)
- `reviews.h2` — Co mówią rodzice · eyebrow *Opinie* · data `{reviews:stroller}` (text, first name and town, only with the customer's consent). No stars or counts shown unless real.

## FAQ (H2) — `{faq:stroller}`
- `faq.eyebrow` — Pytania · `faq.h2` — Najczęstsze pytania
1. **Ile kosztuje pranie wózka dziecięcego?** — Wózek spacerowy od 90 zł, 2w1 od 120 zł, 3w1 od 160 zł, bliźniaczy od 150 zł. Dokładną cenę podajemy ze zdjęć, zanim przyjedziemy.
2. **Ile kosztuje pranie fotelika samochodowego?** — Od 80 zł. W pakietach jest taniej.
3. **Jak pierzecie foteliki Cybex czy Maxi-Cosi?** — Według instrukcji producenta: pokrowiec zgodnie z metką, skorupa i klamra łagodnym środkiem, pasy tylko powierzchniowo, bez moczenia.
4. **Czy środki są bezpieczne dla niemowlęcia?** — Tak. Używamy środków hipoalergicznych i dokładnie je odsysamy. Po wyschnięciu tapicerka jest bezpieczna dla dziecka.
5. **Kiedy wózek będzie gotowy?** — Zwykle tego samego dnia. Rano pierzemy, schnięcie trwa 3–5 godzin w ciepłym, przewietrzonym mieszkaniu.
6. **Czy usuniecie pleśń z gondoli?** — Często tak, ale stare przebarwienia po pleśni mogą nie zejść w całości. Ocenimy to uczciwie ze zdjęć, zanim przyjedziemy.
7. **Czy czyścicie też stelaż i koła?** — Tak, stelaż, koła i kosz są w cenie każdego wózka.

## Service area (H2)
- `area.eyebrow` — Obszar działania · `area.h2` — Gdzie dojeżdżamy
- `area.lede` — Poznań i okolice, tam gdzie mieszkają rodziny. W Strefie 1 dojazd jest gratis. *(v1.1: the link "Pełna lista miejscowości i stref" → `/poznan/obszar-dzialania` is removed until that page exists)*
- Zones come from `{zones}`: **Strefa 1** — dojazd gratis — Poznań, Suchy Las, Swarzędz, Luboń, Komorniki, Plewiska, Skórzewo, Tarnowo Podgórne, Rokietnica, Czerwonak · **Strefa 2** — 25 zł, gratis od 400 zł — Kórnik, Mosina, Puszczykowo, Dopiewo, Murowana Goślina, Pobiedziska, Buk, Stęszew, Kleszczewo · **Dalej** — 1,50 zł/km — Poza powiatem poznańskim wycenimy dojazd indywidualnie.

## Final CTA (master promise, PRD S9)
- `final.h2` — Wyślij 2–3 zdjęcia. Cenę podamy dziś.
- `final.text` — Przyjeżdżamy na czas. Płacisz tyle, ile podaliśmy ze zdjęć. Jeśli coś wyjdzie po wyschnięciu, wracamy za darmo.
- Buttons *(v1.1)*: `cta.whatsapp` (white solid) · `cta.call` (white outline, Lucide `phone`) · then the line `cta.sms`

## Footer *(v1.2, DRAFT: awaiting the owner's approval; shared component, `handoff/components/footer.md`)*
- `footer.logo.alt` — Nowiutko
- `footer.tagline` — Pranie tapicerki, wózków i aut u Ciebie. *(the descriptive tagline from `docs/brand.md`; the logo supplies "Nowiutko")*
- `footer.area` — Poznań i okolice.
- `footer.contact.label` — Kontakt
- `footer.contact.phone` — Telefon · `{business:phone}` → `tel:`
- `footer.contact.whatsapp` — WhatsApp · `{business:whatsapp}` shown as the number → the page's WhatsApp link (`cta.whatsapp`)
- `footer.contact.email` — E-mail · `{business:email}` → `mailto:` *(optional; no address exists yet)*
- `footer.company.label` — Dane firmy
- `footer.company.name` — `{business:legal-name}` *(not known yet)*
- `footer.company.address` — `{business:address-line1}` / `{business:address-line2}` *(optional; not known yet)*
- `footer.address-note` — To adres firmy, nie punkt przyjęć. Pierzemy u Ciebie. *(only with an address; wording for the brand strategist)*
- `footer.company.ids` — NIP `{business:nip}` · REGON `{business:regon}` *(REGON optional; neither known yet)*
- `footer.privacy` — Prywatność (privacy page, issue #47) · `cookies.settings` — Ustawienia cookies (button, reopens the cookie banner)
- **No company value is real yet.** The prototype shows bracketed placeholders such as "[nazwa firmy z CEIDG]"; they are not copy and must never ship.
- In v1.1 the footer was one line: "Nowiutko · pranie tapicerki, wózków i aut u Ciebie · Poznań". "Cookies" and "Regulamin" stay removed: those pages do not exist at the early launch.

## Share image *(v1.2, DRAFT; `handoff/components/share-image.md`)*
- `og.title` — Pranie wózków i fotelików w Poznaniu *(text inside the image; non-breaking spaces after "i" and "w"; not the H1, not the `<title>`, no price)*
- `og.line` — U Ciebie w domu · tego samego dnia
- `og.alt` — Nowiutko: pranie wózków i fotelików w Poznaniu, u Ciebie w domu.

## Cookie banner
- Title *Ciasteczka* · text *Używamy niezbędnych ciasteczek, żeby strona działała. Za Twoją zgodą także analitycznych, żeby wiedzieć, co poprawić.* · link *Szczegóły* → the cookies section of the privacy page *(v1.1; was `/cookies`)* · buttons *Akceptuję* / *Odrzucam* (identical style and size).

## Alt texts (photos supplied by the owner; plain Polish, describe the picture, no keywords lists)
- Slots: `gondola-podszewka` · `fotelik-baza` · `spacerowka-szwy` · `wozek-i-fotelik` · `fotelik-samochodowy` · before/after pairs. Example: "Gondola wózka przed praniem – żółta plama po oliwce na podszewce". Decorative stand-ins get `alt=""`. File names Polish, hyphenated (`pranie-gondoli-wozka-przed-po.webp`).
