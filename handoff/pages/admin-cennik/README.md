# Admin: shell navigation + "Cennik i ustawienia"

## 1. Tag and status
- **DRAFT. Not approved by the owner, not tagged.** Planned tag: `admin-cennik-v1`. Do not build from this until the tag exists.
- Designed 2026-11-14 against `docs/design-constraints.md` in cleaning-sell-system (as read on 2026-11-14: Nuxt UI v4, Lucide, light only, 390 first, online only, installable) and `DESIGN.md` in this repo.
- **No Figma for this handover** (no Figma write access in the design session). Visuals are the PNGs in `screens/` and the HTML reference below, as for `stroller-v1`.

## 2. Issues
- Brief: [cleaning-design #3](https://github.com/Yariandres/cleaning-design/issues/3) (developer issue #11).
- Developer issues: **#11** (Cennik i ustawienia), **#15** (admin shell navigation), **#10** (login, optional frames). Related, not designed here: #20 (Kalendarz), #43 (homepage), #44 (reviews/photos).
- PRD: D5, T4, D7 (login frames), shell for D1–D6.

## 3. Visuals
- `screens/` (PNG, light only). File names match the HTML frames. `-390` is the phone viewport (390 × 844); `-390-full` is the same frame at full height; `-768` and `-1440` show that the layout holds; `40-desktop-uslugi-1440` is the only desktop-specific layout.
- **HTML reference:** `prototypes/admin-cennik/` (`index.html` is a board of all frames; `admin.css` has every measurement). Static frames: each file is one state. It is a prototype, not production code. Regenerate with `python3 prototypes/admin-cennik/build.py`.
- All names, prices, minutes, counts and the phone number in the frames are **sample data**.

| Frames | What |
|---|---|
| `01`, `02` | Shell on a phone: tab bar, "Więcej" sheet |
| `03` | Section index |
| `04`–`13` | Usługi: list, reorder, edit, field errors, saving, saved, save failed, unsaved-changes dialog, hide a used item, never-used item with delete, delete confirmation |
| `14`–`16` | Pakiety: list, edit, error "no items" |
| `17`, `18` | Dopłaty: list, edit |
| `19`, `20` | Strefy: list, edit with error "flat fee without a fee" |
| `21`, `22` | Miejscowości: list, new town with errors "no zone" and "postcode format" |
| `23`, `24` | Dni rejonowe: empty state, new area day |
| `25` | Godziny pracy, with error "closing before opening" |
| `26` | Firma, with error "phone format" |
| `27`–`29` | FAQ: list, edit with live price chips, "Wstaw cenę" picker |
| `30` | Teraz w sezonie |
| `31`, `32` | Loading skeleton, load error (same pattern in every section) |
| `33`–`35` | Login: email, code, wrong/expired code (optional) |
| `40` | Desktop 1440: sidebar + list and edit side by side |

## 4. Sections in order

### Shell navigation (#15)
- **Phones and tablets (< 1024px): bottom tab bar with five items**: Dziś, Lejek, Kalendarz, Klienci, **Więcej**. "Więcej" opens a bottom sheet (`UDrawer`) with Cennik i ustawienia, Raport and Wyloguj. While the owner is inside Cennik i ustawienia or Raport, the "Więcej" tab is the active one.
- **From 1024px: left sidebar (248px)** with all six sections and Wyloguj at the bottom; no tab bar, no "Więcej".
- Why: six tabs at 390px leave 65px each and "Cennik i ustawienia" cannot be a readable label. The four daily screens keep one tap; the two occasional ones cost two.
- Tab bar: white, 1px top border, items 52px tall, label 12.5px/600, active item `primary-600` with a `primary-100` pill behind the icon, `aria-current="page"`. It respects the bottom safe-area inset. Icons (Lucide): `list-checks`, `square-kanban`, `calendar-days`, `users`, `menu`, `sliders-horizontal`, `chart-column`, `log-out`.
- **Edit screens replace the tab bar with the save bar** (see Saving). List and index screens show the tab bar.
- One city at launch: the index shows the city as an eyebrow ("Poznań"). A city switcher can later take that place; nothing else moves.

### Cennik i ustawienia: index (`03`)
Nine sections in four groups, plus "Teraz w sezonie" on top (the one sun-yellow highlight on the screen). Each row shows a one-line summary from data, so the owner can check state without opening it.

| Group | Section | Summary line (data) |
|---|---|---|
| — | Teraz w sezonie | promoted item + line, or "Wyłączone" |
| Oferta | Usługi · Pakiety · Dopłaty | counts, hidden count, highlighted count |
| Dojazd | Strefy · Miejscowości | counts |
| Czas pracy | Godziny pracy · Dni rejonowe | open days · count or "Jeszcze nie ustawione" |
| Strona i firma | FAQ · Firma | pages and question count |

### List → edit pattern (all sections)
- **List:** back link to the index, title, one-line count, rows (min 64px, whole row is the link), dashed "Dodaj …" button at the end. Grouped where the data is grouped (Usługi by the five groups, Miejscowości by zone).
- **Edit:** back link to the list, eyebrow (section · group), title = entry name, white panels of fields, then visibility switch and "Używane w", then delete or the reason delete is not offered. Fixed save bar at the bottom.
- **Single-form sections** (Godziny pracy, Firma, Teraz w sezonie) open straight into the form: one screen, one save.
- **Desktop (`40`):** list (440px) and edit (560px) side by side; the open row is marked; the save bar spans the content area with the button on the right. Sheets become centred `UModal`s.

### Saving
- **Explicit save per entry** for anything typed. The save bar has a status line and one solid "Zapisz" button:
  - clean: "Brak zmian do zapisania." + disabled button
  - dirty: amber dot + "Niezapisane zmiany. Zapis od razu zmienia stronę."
  - invalid (after tapping Zapisz): red "Popraw zaznaczone pola, żeby zapisać."; focus moves to the first invalid field
  - saving: fields disabled, button "Zapisuję…" with a spinner (`aria-busy`)
  - failed: red "Nie zapisano. Na stronie jest nadal stara wersja." + "Spróbuj ponownie"; an alert on top repeats it; the form keeps the changes
- **Saved:** return to the list. The saved row is tinted `success-50` with a 4px `success-500` left edge for about 2s, and a toast says "Zapisano. Nowa cena jest już na stronie." with a "Zobacz" link that opens the public page in a new tab. Toast: `role="status"`, stays 5s, sits above the tab bar. For a hidden entry the text is "Zapisano. Pozycja jest ukryta na stronie."
- **Saved at once, without the save bar** (single gestures with nothing half-typed): each reorder move, and nothing else. The visibility switch is part of the form and is saved with "Zapisz", because hiding a live item is a decision worth one deliberate tap.
- **Unsaved changes (`11`):** leaving a dirty form by the back link, a tab, the sidebar or the browser's back opens a dialog naming what is unsaved: "Zapisz zmiany" (primary), "Odrzuć zmiany", "Wróć do edycji". On page close or reload use the browser's own `beforeunload` prompt.

### Off, not deleted
- Switch "Widoczna na stronie" in the edit form. A hidden entry **stays in its place in the list**, with muted text and an "Ukryta" badge (Lucide `eye-off`), so it keeps its position when switched back on. The list header counts them ("20 na stronie · 1 ukryta").
- **Used entries cannot be deleted.** In place of the delete button: "Tej usługi nie można usunąć, bo jest w wycenach. Możesz ją ukryć."
- **Never-used entries** show "Usuń usługę" (text button, `error-500`) → confirmation (`13`): "Usuń na stałe" (solid error) / "Anuluj".
- Hiding an item that is in packages (`12a`) shows a warning before saving. Proposed rule, to confirm: packages stay on the site unchanged; the item only leaves the single-item price list and the quote form.

### "Używane w"
A neutral note in the edit form: "Używane w: 5 pakietów (names), FAQ wózków, 31 wycen." or "Jeszcze nieużywana: …". Needs from the API, per entry: package names, FAQ pages and answer count, quote count.

### Order
- Lists that have an order (Usługi, Pakiety, Dopłaty, Miejscowości, FAQ) have a "Kolejność" action in the top bar. It switches the list into **reorder mode (`05`)**: position number, name, and two 44px buttons (up, down) per row; prices and links are hidden. The first row's "up" and the last row's "down" are disabled. "Gotowe" leaves the mode.
- Each move saves at once; a status line confirms "Kolejność zapisana. Już widać ją na stronie." (`role="status"`). After a move, focus stays on the same button of the moved row.
- Usługi reorder within their group. Group order is fixed (not editable in v1).
- No drag and drop.

### Section notes
- **Usługi (`04`, `06`):** list row = name, visit length, "od 90 zł" (per m² items: "od 18 zł / m²", "6 min / m²"). Form: Nazwa · Grupa (select) · Co jest w cenie (max 60) · Cena od · Czas wizyty (label becomes "Czas na 1 m²" for m² items) · Cena liczona za: sztukę / m².
- **Pakiety (`14`, `15`):** list row = name, item count, tag, "Wyróżniony" badge, price with the struck-through earlier price. Form: Nazwa · Cena pakietu · Cena przed (optional, typed; the computed sum of items and the saving are shown under it) · items with a quantity stepper (at quantity 1 the minus button is a bin and removes the item) · "Dodaj pozycję" (opens the same picker as "Wstaw cenę", services only) · Etykieta (optional, max 24) + Kolor etykiety: Słońce / Mięta · Wyróżniony · Widoczny na stronie.
- **Dopłaty (`17`, `18`):** Rodzaj: Procent / Kwota w zł. Procent shows "Od" and optional "Do" (range); Kwota shows one zł field.
- **Strefy (`19`, `20`):** Opłata za dojazd: Gratis / Stała opłata / Za kilometr. Gratis: no money fields. Stała opłata: Opłata + optional "Gratis od kwoty". Za kilometr: "Stawka" in zł/km. Always: Dodatkowy czas dojazdu (min), Notatka (optional). Zones are not added, deleted or reordered here (three fixed rows); say if they should be.
- **Miejscowości (`21`, `22`):** grouped by zone. Form: Nazwa · Strefa (select) · Kody pocztowe as removable chips with an add field.
- **Dni rejonowe (`23`, `24`):** empty state first. Form: Dzień tygodnia · Twoja nazwa (owner-only label) · Miejscowości as chips, added from a picker sheet. A note states that area days only reorder slots and never block other days.
- **Godziny pracy (`25`):** seven rows on one screen: day, open switch, start and end time (`type="time"`). A closed day collapses to "Zamknięte".
- **Firma (`26`):** Telefon · switch "WhatsApp na tym samym numerze" (hides the second field when on) · Numer WhatsApp · Minimalne zamówienie · Maksymalnie wizyt dziennie · Najkrótszy czas do wizyty (godz.).
- **FAQ (`27`–`29`):** page select on top (one page now; five more appear in the same select). List rows show the question and which answers carry live prices. Form: Pytanie · Odpowiedź (see the custom component below) · preview "Tak to wygląda na stronie" · "Usuń pytanie" (FAQ entries can always be deleted, with the same confirmation).
- **Teraz w sezonie (`30`):** switch "Pokazuj na stronie" · the chosen item or package ("Zmień" opens the picker, services and packages) · Krótka linijka (optional, max 60) · label preview. The label reads "Teraz w sezonie: {name} od {price}" with the sun dot; the price is always live.

### Login (`33`–`35`, optional)
No shell. Logo, heading, one field, one button. Code step: six 56px boxes, first box `autocomplete="one-time-code"`, pasting a full code fills all six; "Wyślij kod jeszcze raz" and "Zmień e-mail". The email shown is a placeholder.

## 5. Data bindings
Nothing in these screens is fixed text except labels, hints and errors.

| Binding | Where |
|---|---|
| `{services[]}`: name, included, priceFrom, unit (piece / m²), minutes, group, visible, order, usedIn | Usługi list and form; pickers |
| `{packages[]}`: name, price, priceWas?, items[{service, qty}], tag?{text, colour: sun/mint}, highlighted, visible, order | Pakiety |
| computed: sum of items, saving in zł and % | under "Cena przed" (display only) |
| `{addons[]}`: name, kind (percent / amount), from, to?, amount, visible, order | Dopłaty |
| `{zones[]}`: name, feeType (free / flat / perKm), fee, freeOver?, ratePerKm, extraMinutes, note? | Strefy |
| `{towns[]}`: name, zone, postcodes[], order | Miejscowości; area-day picker |
| `{areaDays[]}`: weekday, label, towns[] | Dni rejonowe |
| `{hours[7]}`: open, from, to | Godziny pracy |
| `{business}`: phone, whatsapp, minOrder, maxVisitsPerDay, minNoticeHours | Firma |
| `{faq:<page>[]}`: question, answer with `{price:<id>}` tokens, order | FAQ. Tokens render as chips in the editor and as plain text in the preview and on the site |
| `{wantedNow}`: target (service or package), line?, visible | Teraz w sezonie; index row |
| counts and summaries on the index and list headers | from the lists above |

**Input formats** (show and accept; store as the developer prefers):
- Money: whole zł or with a comma (`90`, `89,50`); also accept a dot and turn it into a comma on blur. `inputmode="decimal"`, "zł" as a fixed suffix inside the field, right-aligned, tabular figures.
- Minutes, visits, hours: whole numbers, `inputmode="numeric"`, suffix "min" / "godz.".
- Percent: whole numbers, suffix "%".
- Postcode: `00-000`; typing five digits inserts the hyphen.
- Phone: `+48 000 000 000`; nine digits typed without the prefix get "+48" and spacing on blur. `type="tel"`.
- All inputs use 16px text so iOS does not zoom the page.

## 6. States
| State | Frame | Notes |
|---|---|---|
| Loading | `31` | Title and back link at once; skeleton rows in the list's real shape; `aria-busy`. Same in every section; forms use the same skeleton blocks in a panel |
| Empty | `23` | Dni rejonowe starts empty. Other lists use the same block with their own sentence and "Dodaj …" |
| Load error | `32` | "Nie udało się wczytać …" + "Na stronie nic się nie zmieniło." + retry |
| Saving | `08` | |
| Saved | `09` | Row tint + toast |
| Save failed | `10` | |
| Field errors | `07`, `16`, `20`, `22`, `25`, `26` | Under the field, on blur and on submit (constraint: no error summary) |
| Unsaved changes | `11` | |
| Hidden entry | `04` (Wykładzina dywanowa), `12` | |
| Delete | `12`, `13` | |
| Long names | `04`, `12a`, `18` | Names wrap to two lines; prices never wrap |

**Error texts**

| Case | Text |
|---|---|
| Required field empty | "Wpisz nazwę." (per field: "Wpisz pytanie.", "Wpisz odpowiedź.", "Wpisz cenę.") |
| Price 0 | "Cena musi być większa niż 0 zł." |
| Closing before opening | "Godzina zamknięcia musi być późniejsza niż otwarcia." |
| Flat-fee zone without a fee | "Podaj opłatę za dojazd." |
| Package with no items | "Dodaj co najmniej jedną pozycję." |
| Town without a zone | "Wybierz strefę." |
| Postcode format | "Wpisz kod w formacie 00-000." |
| Phone format | "Wpisz numer w formacie +48 000 000 000." |
| Range "Do" not above "Od" | "„Do” musi być większe niż „Od”." |
| Save failed | "Nie udało się zapisać. Na stronie jest nadal stara cena. Sprawdź internet i spróbuj ponownie. Twoje zmiany zostają w formularzu." |
| Load failed | "Nie udało się wczytać usług. Sprawdź internet i spróbuj ponownie. Na stronie nic się nie zmieniło." |
| Login: wrong or expired code | "Kod jest nieprawidłowy albo wygasł. Wpisz go jeszcze raz lub wyślij nowy." |

Copy has no gendered forms for the owner.

## 7. Components
**From Nuxt UI:** `UButton` (solid primary = Zapisz only; neutral outline; ghost text; solid error only in the delete dialog), `UFormField` + `UInput` (trailing slot for zł / min / %), `USelect`, `UTextarea`, `USwitch`, `URadioGroup` shown as pills, `UDrawer` (sheets on phones), `UModal` (the same dialogs from 1024px), `UToast`, `USkeleton`, `UBadge`, `UAlert` (the notes), `UPinInput` (login code), `UNavigationMenu` or plain links (sidebar).

**Custom (not in Nuxt UI):**
- **`AdminTabBar`**: see Shell.
- **`SaveBar`**: fixed bottom bar, status line + one button; five states above.
- **`ListRow`** and **`ReorderRow`**.
- **`QuantityStepper`**: two 44px round buttons and the number.
- **`ChipInput`**: removable chips (towns, postcodes); each remove button is 44px and labelled "Usuń: {name}".
- **`PriceChipEditor`** (FAQ answer): a text area in which a `{price:<id>}` token is one atomic chip showing the **current price** with a Lucide `tag` icon (`primary-100` background, `primary-800` text). The raw code is never shown. "Wstaw cenę" opens the picker and inserts a chip at the cursor. Tapping a chip selects it (2px `primary-500` ring); the hint then names its item and "Usuń cenę" appears. Backspace next to a chip removes the whole chip. If a chip's item is later hidden or deleted, the chip turns `warning` and the answer cannot be saved until it is replaced; the "Używane w" hint on that item warns first.
- **`ItemPicker`** (sheet): search field, items grouped as in the price list, current price on the right; one tap picks and closes.

Minimum heights: inputs and buttons 48px, every other control at least 44px (the 52 × 32 switch has a 44px-tall hit area).

Motion (CSS only): switch 150ms ease-out; toast rises 8px and fades in over 200ms ease-out; button press scale .98 over 100ms; skeleton shimmer 1.2s linear. With `prefers-reduced-motion`: none of these move; the skeleton is a flat tint.

## 8. Accessibility
- One `h1` per screen (the title); group names are `h2`.
- Focus order follows the visual order; the save bar comes last. Focus ring as in DESIGN.md (3px `neutral-900`, 3px offset; white on the dark toast).
- Every field has a visible label; hints and errors are linked with `aria-describedby`; invalid fields have `aria-invalid`; errors use `role="alert"`.
- Sheets and dialogs trap focus, close on Escape, and return focus to the control that opened them. Destructive and unsaved-changes dialogs are `alertdialog`.
- Reorder buttons are labelled "Przesuń wyżej: {name}" / "Przesuń niżej: {name}".
- Hidden entries are marked by a text badge, not by colour alone. The unsaved state is marked by text plus the dot.
- Contrast: every text pair in the frames is at least 4.5:1 (measured in the rendered frames, see the checks in the design report).
- Install: the app icon and maskable icon from `handoff/brand/logo/` (unchanged since `stroller-v1`); `theme-color` `#F5FAF8`.

## 9. Assets and licences
No photos or illustrations. Logo symbol: `handoff/brand/logo/mark.svg` (own). Icons: Lucide (ISC licence). Fonts: Bricolage Grotesque and Figtree (SIL OFL 1.1), as in `handoff/tokens/fonts.md`. Tokens: unchanged from `stroller-v1`.

## 10. SEO
Not applicable. The admin and login must be `noindex`.

## 11. Answers to the brief's open questions
1. **Save per entry or auto-save?** Explicit save per entry; only reorder moves save at once. A half-typed price ("9" on the way to "95") must never reach the public site, and one deliberate tap gives a clear moment to say "saved and live".
2. **Tab bar or menu?** Both: five-item tab bar with "Więcej" on phones, sidebar with all six from 1024px.
3. **"Teraz w sezonie": where, and an image?** For the owner to decide (offer). Recommendation: one text label with the sun dot, on the homepage hero and at the top of the price list; on a counter page only when the promoted item belongs to that counter. No image: the promoted item's own photo slot on the page is enough, and a separate image would need a new photo for every change.
4. **Package "was" price: computed or typed?** For the owner to decide (pricing). Recommendation: keep it typed and optional, and show the computed sum of the items next to it, so the two cannot drift apart unnoticed. If the typed value is lower than the package price, block the save.

## 12. Open questions for the developer
- Is "group" an editable field of a service (designed as a select), and are groups themselves fixed?
- What exactly counts as "used" for delete (quotes only, or also packages and FAQ tokens)?
- Rule when a hidden item is still inside a visible package (proposed above).
- Can zones be added or removed, or are there always three?
- Does "Zobacz" in the toast have one target per section (price list, counter page, service-area page)?
- Poznań's postcodes are a range in the sample data; how are ranges stored and shown?
