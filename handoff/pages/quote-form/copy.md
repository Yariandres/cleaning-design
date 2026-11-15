# Copy: quote form (`/poznan/wycena`)

**Approved with `quote-form-v1` (2026-11-15).** Polish copy, keyed. `{...}` = comes from the database, never hard-coded. Voice: "Ty", short, concrete; no gendered forms for the customer. Service, package, add-on, town and zone names and all prices are data and are not listed here. Error texts are in the README, section 6.

## Head
- `meta.title` — Wycena prania ze zdjęć – Poznań i okolice | Nowiutko *(placeholder until the SEO brief)*
- `meta.robots` — noindex, follow *(recommendation until the SEO brief)*

## Frame
- `h1` — Wycena prania ze zdjęć · Poznań i okolice *(placeholder until the SEO brief)*
- `skip` — Przejdź do formularza
- `progress.label` — Krok {n} z 4
- `progress.back` — Wstecz
- `progress.goto` (finished step, screen readers) — Wróć do kroku {n}: {step title}
- `nav.next` — Dalej
- `nav.send` — Wyślij zapytanie
- `nav.sending` — Wysyłamy…
- `nav.retry` — Spróbuj ponownie
- `nav.backToSummary` — Wróć do podsumowania
- `doors` — Wolisz inaczej? · Napisz na WhatsApp · Zadzwoń: `{business:phone}`

## Estimate
- `estimate.label` — Szacunkowa cena
- `estimate.empty` — — *(bar note: wybierz rzeczy)*
- `estimate.empty.desktop` — Zaznacz rzeczy po lewej. Cenę policzymy od razu, z cennika.
- `estimate.from` — od `{total}` *(only when a rug is unmeasured or travel is individual)*
- Bar notes (one at a time): jeszcze bez dojazdu · dojazd gratis · w tym dojazd `{fee}` · + dojazd, wycenimy · min. zamówienie `{business:min-order}` · + dywan po zmierzeniu
- `estimate.fine` — To szacunek z cennika. Wiążącą cenę podamy w wycenie, kiedy zobaczymy zdjęcia.
- Breakdown rows: Pakiet `{name}` · `{service}` × `{qty}` · `{addon}` · Dopłata do minimalnego zamówienia (Minimalne zamówienie to `{business:min-order}`) · Dojazd (`{place}`; gratis / +`{fee}` / w wycenie) · do zmierzenia
- `estimate.sheet.close` — Zamknij
- `estimate.live` (screen readers) — Szacunkowa cena: `{total}`

## Step 1
- `s1.h2` — Co mamy wyczyścić?
- `s1.lede` — Zaznacz rzeczy, a od razu zobaczysz szacunkową cenę. Ceny brutto.
- Section lines (after the group name; the group names are data): Wózki, foteliki, krzesełka · Kanapy, narożniki, fotele, krzesła · Jedna strona, druga za dopłatą · Cena za m² · Wnętrze auta pod Twoim domem · *each followed by* "od `{lowest price}`"
- `s1.packs` — Pakiety · Taniej w zestawie · od `{lowest package price}`
- `s1.pack.saving` — taniej o `{priceWas − price}` *(only when the owner entered the earlier price)*
- `s1.count` (screen readers) — Wybrane: `{n}`
- `s1.row.add` / `more` / `less` / `remove` (button names) — Dodaj: `{name}` / Więcej: `{name}` / Mniej: `{name}` / Usuń: `{name}`
- `s1.area.label` — Powierzchnia *(suffix m²)*
- `s1.area.hint` — Długość × szerokość, np. 2 × 3 m to 6 m². Kilka dywanów? Wpisz razem.
- `s1.area.unknown` — Nie znam wymiarów — Zmierzymy na miejscu. Cenę za m² znasz już teraz.
- `s1.area.unknown.line` — zmierzymy na miejscu
- `s1.addons` — Dodatki
- `s1.prefill` — Zaczynamy od wózków i fotelików. Pozostałe rzeczy znajdziesz niżej. *(one variant per counter)*
- `s1.prefill.pack` — **Pakiet `{name}` jest już zaznaczony.** Możesz go zmienić albo coś dodać.
- `s1.min` — **Minimalne zamówienie to `{business:min-order}`.** Masz teraz `{subtotal}`, więc w szacunku jest dopłata `{topUp}`. Możesz też dobrać coś jeszcze w tej kwocie.
- `s1.packhint` (optional) — **Te trzy rzeczy są w pakiecie `{name}`.** W pakiecie kosztują `{price}` zamiast `{sum}`. · Zamień na pakiet

## Step 2
- `s2.h2` — Gdzie mamy przyjechać?
- `s2.lede` — Od miejsca zależy dojazd i wolne terminy.
- `s2.field` — Miejscowość, dzielnica lub kod pocztowy · placeholder: np. Winogrady albo 62-020
- `s2.hint` — Zacznij pisać albo wybierz z listy. Kod pocztowy też zadziała.
- `s2.clear` (button name) — Wyczyść
- List groups and messages are data (source copy): Poznań — Dojazd gratis · Okolice – bez dopłaty — Dojazd gratis · Okolice – Strefa 2 — Dojazd 25 zł, gratis od 400 zł · Inna miejscowość…
- `s2.result.free` — Dojazd gratis
- `s2.result.fee` — Dojazd `{fee}` — Przy zamówieniu od `{freeOver}` dojazd jest gratis. Twoje zamówienie ma teraz `{subtotal}`.
- `s2.result.freeOver` — Dojazd gratis — W Strefie 2 dojazd kosztuje `{fee}`, ale od `{freeOver}` jest gratis. Twoje zamówienie ma `{subtotal}`.
- `s2.result.other` — Wycenimy dojazd indywidualnie — Poza powiatem poznańskim liczymy `{ratePerKm}` za km od granicy powiatu. Dokładną kwotę podamy w wycenie.
- `s2.postcode.matched` — Kod `{postcode}` · `{group}`
- `s2.postcode.none` — **Kodu `{postcode}` nie mamy na liście.** Wpisz miejscowość, a dojazd wycenimy indywidualnie.
- `s2.other.field` — Miejscowość

## Step 3
- `s3.h2` — Zdjęcia i termin
- `s3.lede` — Zdjęcia pomagają podać dokładną cenę. Termin wybierasz wstępnie: potwierdzimy go w wycenie.
- `s3.photos.h3` — Zdjęcia · opcjonalnie, do 5
- `s3.photos.hint` — Najbardziej pomagają trzy ujęcia: całość, plamy z bliska i metka.
- `s3.photos.add` — Dodaj zdjęcia
- `s3.photos.sub` — Z aparatu lub galerii · JPG, PNG, WebP, HEIC · `{n}` z 5
- `s3.photos.full` — Masz już 5 zdjęć. Usuń jedno, żeby dodać inne.
- `s3.photo.name` — Zdjęcie `{n}` *(rejected files keep their file name)*
- `s3.photo.uploading` — Wysyłamy… `{percent}`%
- `s3.photo.done` — Wysłane
- Button names: Usuń zdjęcie `{n}` · Przerwij wysyłanie zdjęcia `{n}` · Wyślij ponownie zdjęcie `{n}`
- `s3.slots.h3` — Kiedy Ci pasuje?
- `s3.slots.lede` — Wybierz 2 lub 3 terminy. Jeden z nich potwierdzimy w wycenie. Wizyta potrwa około `{visit.durationLabel}`
- `s3.slots.area` — W `{weekday, plural}` jeździmy w Twoją okolicę *(e.g. "W czwartki…"; only when the town has an area day)*
- `s3.slots.rest` — Pozostałe terminy
- Slot format: "jutro, 13:30" (with the date under it: "pon. 16 lis"), "wt. 17 lis, 18:00"; short weekday and month, 24-hour time
- `s3.slots.more` — Pokaż późniejsze terminy
- `s3.slots.count` — Wybrane: `{n}` z 3 · Możesz jeszcze dodać jeden. · To już komplet.
- `s3.slots.surcharge.hint` — Wieczorem i w weekend dopłata wynosi `{percent}`%. Takie terminy mają oznaczenie +`{percent}`%.
- `s3.slots.surcharge.chosen` — **Wieczorem i w weekend dopłata wynosi `{percent}`%.** Doliczymy ją tylko wtedy, gdy wizyta odbędzie się w takim terminie (tu: ok. `{amount}`).
- `s3.slots.loading` (screen readers) — Sprawdzamy wolne terminy…
- `s3.slots.none.h` — W najbliższych 30 dniach nie mamy wolnego terminu
- `s3.slots.none.p` — Wyślij zapytanie mimo to. Termin zaproponujemy w wycenie, a Ty zdecydujesz, czy Ci pasuje.
- `s3.slots.one` — Mamy teraz jeden wolny termin. Zaznacz go albo napisz, kiedy Ci pasuje.
- `s3.slots.one.field` — Inne terminy, które Ci pasują (opcjonalnie)
- `s3.slots.error.h` — Nie udało się wczytać terminów · button: Spróbuj ponownie
- `s3.nofit` — Żaden termin mi nie pasuje
- `s3.nofit.field` — Dni i godziny, które Ci pasują (opcjonalnie) · placeholder: np. po 17:00, najlepiej w piątki · hint: Termin zaproponujemy w wycenie.

## Step 4
- `s4.h2` — Kontakt
- `s4.lede` — Ostatni krok. Nic nie wysyłamy, dopóki nie klikniesz „Wyślij zapytanie”.
- `s4.name` — Imię
- `s4.channel` — Jak wysłać Ci wycenę? · E-mail · WhatsApp · hint: Na ten adres lub numer wyślemy link do wyceny.
- `s4.email` — E-mail · placeholder ty@example.com · hint when optional: Przyślemy na niego potwierdzenie zapytania.
- `s4.tel` — Telefon · placeholder +48 000 000 000 · hint when optional: Przyda się w dniu wizyty, gdybyśmy musieli zadzwonić. · hint when required: Numer, na którym masz WhatsApp.
- `s4.optional` — (opcjonalnie)
- `s4.addr` — Ulica i numer (opcjonalnie) · hint: Możesz też podać przy potwierdzeniu wyceny.
- `s4.pay` — Jak wolisz zapłacić? · Gotówka (przy wizycie) · Karta (także BLIK) · hint: Karta to także BLIK, Przelewy24, Apple Pay i Google Pay. Wybór możesz zmienić później, na stronie wyceny.
- `s4.summary.h3` — Podsumowanie
- Rows: Rzeczy · Miejsce · Zdjęcia · Terminy · Szacunkowa cena · link: Zmień
- `s4.summary.photos` — `{n}` zdjęcie / zdjęcia / zdjęć · `{n}` jeszcze się wysyła · Bez zdjęć — Wycenimy z opisu. Zdjęcia możesz dosłać.
- `s4.summary.notime` — Bez terminu — Zaproponujemy termin w wycenie.
- `s4.consent` — Chcę dostawać od Nowiutko porady i oferty e-mailem (opcjonalnie) — Potwierdzisz to jednym kliknięciem w e-mailu. Możesz zrezygnować w każdej chwili. *(unticked by default; legal read needed)*
- `s4.privacy` — Wysyłając formularz, przekazujesz nam dane potrzebne do przygotowania wyceny. Zdjęcia do wyceny przechowujemy 12 miesięcy. Jak dbamy o dane i zdjęcia, opisuje [polityka prywatności](/polityka-prywatnosci). *(link placeholder, page #47; legal read needed)*

## Thank-you
- `ty.title` — Dziękujemy, mamy Twoje zapytanie | Nowiutko
- `ty.h2` — Dziękujemy. Mamy Twoje zapytanie.
- `ty.lede` — Wycenę wyślemy **`{quoteEta}`**, e-mailem. / …, na WhatsApp. *(`{quoteEta}`: jeszcze dziś / jutro rano)*
- `ty.next.h3` — Co teraz?
  1. **Oglądamy zdjęcia i liczymy cenę** — Sprawdzamy rzeczy na zdjęciach i podajemy wiążącą cenę. *(without photos: Liczymy cenę z Twojego opisu. Zdjęcia możesz jeszcze dosłać.)*
  2. **Dostajesz wycenę z terminem** — Link do wyceny przyjdzie e-mailem. / … na WhatsApp.
  3. **Potwierdzasz jednym kliknięciem** — Dopiero wtedy termin jest zarezerwowany. Do tego czasu nic nie płacisz.
- `ty.summary.h3` — Twoje zapytanie
- `ty.held` — Wstępnie trzymamy dla Ciebie wybrane terminy.
- `ty.mail` — Potwierdzenie zapytania wysłaliśmy na **`{enquiry.email}`**. Nie widzisz go? Sprawdź spam. *(only when an e-mail was given)*
- `ty.back` — Wróć na stronę o praniu wózków *(one variant per source page; "Wróć na stronę główną" for a direct visit)*
- `ty.doors` — Masz pytanie? · Napisz na WhatsApp · Zadzwoń: `{business:phone}`
