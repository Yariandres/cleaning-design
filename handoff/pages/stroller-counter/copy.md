# Copy: stroller counter

Final Polish copy, keyed. `{...}` = comes from the database, never hard-coded. Voice: "Ty", short, concrete. **Wording of the H1 and hero is the brand strategist's call** (see README, open questions); the keys below hold the version in the approved design.

## Head
- `meta.title` — Pranie wózków i fotelików Poznań – u Ciebie, od 80 zł *(53 chars; the "80" comes from `{price:carseat}`)*
- `meta.description` — Pierzemy wózki, gondole i foteliki u Ciebie w domu, w Poznaniu i okolicach. Gotowe tego samego dnia. Cena ze zdjęć przed przyjazdem, od 80 zł. *(142 chars)*
- `meta.canonical` — https://nowiutko.pl/poznan/pranie-wozkow-i-fotelikow

## Header
- `header.phone` — `{business:phone}` (placeholder 500 000 000 until the owner supplies it)
- `header.cta` — Wyślij zdjęcia

## Hero
- `hero.h1` (real `<h1>`, styled as eyebrow) — Pranie wózków i fotelików dziecięcych w Poznaniu i okolicach
- `hero.headline` (`<p class="display">`) — Wózek jak nowe. / Pod Twoim domem, tego samego dnia. *(second sentence in `primary-500`)*
- `hero.lede` — Przyjeżdżamy z własnym sprzętem. Ty nie wyjmujesz dziecka z domu, nie wozisz wózka i nie czekasz trzech dni.
- `hero.ticks` — Hipoalergiczne środki · Foteliki według instrukcji producenta · Dojazd gratis w Strefie 1
- `hero.card.eyebrow` — Cennik brutto
- `hero.card.sub` — cena ze zdjęć, przed przyjazdem
- `hero.card.rows` — Wózek spacerowy `{price:stroller-single}` · Wózek 2w1 `{price:stroller-2in1}` · Fotelik samochodowy `{price:carseat}` · Wózek 3w1 `{price:stroller-3in1}` (each "od N zł")
- `hero.card.nextslot` — Najbliższy wolny termin: `{nextFreeSlot.label}` *(hidden when there is no real free slot; never a timer)*
- `hero.card.cta` — Wyślij 2–3 zdjęcia – cena dziś
- `hero.card.links` — Pełny cennik i pakiety (#cennik) · Napisz na WhatsApp (`{business:whatsapp}`, text only)

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
- `price.note` — Minimalne zamówienie `{business:min-order}`. Przy silnych zabrudzeniach (pleśń, wymioty) wycenimy ze zdjęć przed przyjazdem. [Pełny cennik](/cennik)
- Safety panel — eyebrow *Foteliki samochodowe*; h3 *Fotelik to sprzęt bezpieczeństwa. Tak go traktujemy.*; bullets: Pokrowiec i skorupę czyścimy według instrukcji producenta. / Pasy czyścimy tylko powierzchniowo, bo moczenie osłabia ich wytrzymałość. / Środki hipoalergiczne, bezpieczne dla niemowląt po wyschnięciu.
- Packages (price + struck-through earlier price from `{price:pack-*}` and `{price:pack-*-was}`): **Nowy Członek Rodziny** (tag *przed porodem*): Materac dwuosobowy, Wózek 2w1, Fotelik samochodowy · **Rodzinny** (tag *najczęściej wybierany*): Kanapa 3-osobowa, Wózek 2w1, Fotelik samochodowy · **Auto i Maluch** (tag *auto i maluch*): Pranie tapicerki auta, Wózek 2w1, Fotelik samochodowy. *The tag "najczęściej wybierany" is a claim: show it only if the owner's data says so (`{pack:*:badge}`).*

## Steps (H2)
- `steps.eyebrow` — Trzy kroki, zero wychodzenia z domu
- `steps.h2` — Jak to działa
- 1 **Wyślij zdjęcia** — 2–3 zdjęcia przez WhatsApp, SMS lub formularz. Napisz, gdzie mieszkasz.
- 2 **Dostań cenę i termin** — Zwykle w kilka minut. Wolne terminy często już na następny dzień.
- 3 **Pierzemy u Ciebie** — Przywozimy sprzęt i środki. Potrzebujemy tylko wody i gniazdka.
- `steps.cta` — Wyślij 2–3 zdjęcia

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
- `area.lede` — Poznań i okolice, tam gdzie mieszkają rodziny. W Strefie 1 dojazd jest gratis. [Pełna lista miejscowości i stref](/poznan/obszar-dzialania)
- Zones come from `{zones}`: **Strefa 1** — dojazd gratis — Poznań, Suchy Las, Swarzędz, Luboń, Komorniki, Plewiska, Skórzewo, Tarnowo Podgórne, Rokietnica, Czerwonak · **Strefa 2** — 25 zł, gratis od 400 zł — Kórnik, Mosina, Puszczykowo, Dopiewo, Murowana Goślina, Pobiedziska, Buk, Stęszew, Kleszczewo · **Dalej** — 1,50 zł/km — Poza powiatem poznańskim wycenimy dojazd indywidualnie.

## Final CTA (master promise, PRD S9)
- `final.h2` — Wyślij 2–3 zdjęcia. Cenę podamy dziś.
- `final.text` — Przyjeżdżamy na czas. Płacisz tyle, ile podaliśmy ze zdjęć. Jeśli coś wyjdzie po wyschnięciu, wracamy za darmo.
- Buttons: Wyślij zdjęcia · Napisz na WhatsApp · "Zadzwoń: `{business:phone}`"

## Footer
Nowiutko · pranie tapicerki, wózków i aut u Ciebie · Poznań — links: Prywatność, Cookies, Regulamin (pages from issue #47).

## Cookie banner
- Title *Ciasteczka* · text *Używamy niezbędnych ciasteczek, żeby strona działała. Za Twoją zgodą także analitycznych, żeby wiedzieć, co poprawić.* · link *Szczegóły* · buttons *Akceptuję* / *Odrzucam* (identical style and size).

## Alt texts (photos supplied by the owner; plain Polish, describe the picture, no keywords lists)
- Slots: `gondola-podszewka` · `fotelik-baza` · `spacerowka-szwy` · `wozek-i-fotelik` · `fotelik-samochodowy` · before/after pairs. Example: "Gondola wózka przed praniem – żółta plama po oliwce na podszewce". Decorative stand-ins get `alt=""`. File names Polish, hyphenated (`pranie-gondoli-wozka-przed-po.webp`).
