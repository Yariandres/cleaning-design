# Quote form — `/poznan/wycena`

## 1. Tag and status
- **Tag:** `quote-form-v1`, approved by the owner on 2026-11-15.
- Designed 2026-11-15 against `docs/design-constraints.md` in cleaning-sell-system (as read on 2026-11-15: Nuxt UI v4, Lucide, light only, 390 first, Zod forms, CSS-only motion, no map) and `DESIGN.md` in this repo.
- **No Figma for this handover** (the Figma connector was not authorised in the design session). Visuals are the PNGs in `screens/` and the HTML reference, as for `stroller-v1` and `admin-cennik-v1`.
- **No SEO brief yet** for this page; the owner said to start without it. See section 10.

## 2. Issues
- Brief: [cleaning-design #4](https://github.com/Yariandres/cleaning-design/issues/4), from `docs/design-briefs/quote-form.md` in cleaning-sell-system at `3b18544`.
- Developer issues: **#12** (quote form). Touches #9 (slots), #18 (quote page), #25 (acknowledgement e-mail), #47 (privacy page), #43 (homepage link); none of those is designed here.
- PRD: Q1, Q2, Q3 (customer side), Q4 (thank-you), Q5 (source), Q6, S3, S4, S5, P1, decision 26 and 41.

## 3. Visuals
- `screens/` (PNG, light only, 2×). File names match the HTML frames. `-390-full` is the phone frame at full height; `-390` is the 844px viewport (the first screen and the two sheets); `-1440-full` is the desktop layout; `-768`, `-1024`, `-320` show that the layout holds. `checks.json` is the automatic check output.
- **HTML reference:** `prototypes/quote-form/` (`index.html` is a board of all 42 frames; `quote.css` has every measurement; header, footer, buttons and tokens come from `prototypes/stroller/base.css`, unchanged). Static frames: each file is one state. Prototype, not production code. Regenerate with `python3 prototypes/quote-form/build.py`; re-shoot and re-check with `node prototypes/quote-form/shots.mjs`.
- Every name, price, add-on, town, postcode, slot, duration and contact detail in the frames is **sample data**.

| Frames | What |
|---|---|
| `01`–`10` | Step 1: empty · quantities and add-ons · pre-filled from the stroller page · pre-filled with a package · per-m² area and "Nie znam wymiarów" · below the 150 zł minimum · estimate sheet · error "nothing chosen" · error "no area" · package suggestion (optional) |
| `11`–`22` | Step 2: empty · list with the four groups · list while typing · postcode match · Zone 2 with fee · estimate sheet with travel · Zone 2 free from 400 zł · postcode without a match · "Inna miejscowość" · three errors |
| `23`–`34` | Step 3: default · photo states · five photos · two times chosen · three chosen with an evening slot · slots loading · slots failed to load · no free slot in 30 days · one free slot · "Żaden termin mi nie pasuje" · error "one time only" · a chosen slot was taken |
| `35`–`40` | Step 4: empty · filled (e-mail) · WhatsApp · errors · sending · sending failed |
| `41`, `42` | Thank-you: e-mail with times · WhatsApp, no photos, no time, after hours |
| `…-1440-full` | Desktop: `01`, `05`, `14`, `26`, `36`, `41` |

## 4. Sections in order
**One page, four steps, one action.** No main menu: logo + phone (same header as the stroller page, without its header button), same footer.

| # | Part | Notes |
|---|---|---|
| 0 | Header | Logo, phone (`tel:`). Not sticky |
| 1 | `<h1>` | Real text, styled as the eyebrow (same pattern as the stroller page). Stays on every step and on the thank-you state |
| 2 | Progress | "Wstecz" (from step 2), "Krok N z 4", four bars. Finished bars are links back to that step |
| 3 | Step heading | `<h2>`; receives focus on "Dalej", "Wstecz" and "Zmień" |
| 4 | Step content | See below |
| 5 | Other doors | "Wolisz inaczej? Napisz na WhatsApp · Zadzwoń" (PRD S3), quiet text links under every step |
| 6 | Footer | As on the stroller page |
| — | Estimate bar | Phones and tablets (< 900px): fixed to the bottom. Left: "Szacunkowa cena", the amount, one short note; tapping it opens the breakdown sheet. Right: the step's only solid button ("Dalej", "Wyślij zapytanie"). It replaces the counter's "Wyślij zdjęcia" bar on this page |
| — | Estimate card | From 900px: sticky card in a 360px right column with the amount and the breakdown always open; "Wstecz" and "Dalej" sit under the step |

**Step 1, "Co mamy wyczyścić?"** Six sections in one list (`UAccordion`, several may be open): the five price-list groups and "Pakiety". A closed section shows its name, a short line, its lowest price and a count of what is chosen in it. A service row has the name, the "what's included" line, "od … zł" and a 44px "+". Chosen rows are tinted `primary-50` with a 4px `primary-500` edge and show a stepper (at 1 the minus is a bin, as in the admin). Per-m² rows open a "Powierzchnia" field and "Nie znam wymiarów". Add-ons that apply to an item appear inside its chosen row as checkboxes with the amount in zł. Packages are checkbox rows with price, struck earlier price and "taniej o … zł".

**Step 2, "Gdzie mamy przyjechać?"** One field (`UInputMenu`): town, district or postcode. The list keeps the four groups with their travel message. A result card under the field states the place and the travel message; the estimate updates at once. "Inna miejscowość…" is always the last option and opens a free-text field.

**Step 3, "Zdjęcia i termin"** Photos first (optional), then times. Photos: one dashed "Dodaj zdjęcia" button (the phone offers camera or gallery itself), a list of rows with a 64px thumbnail, status and 44px actions. Times: days as rows, times as checkbox pills; area-day slots first under a heading that says why; "Pokaż późniejsze terminy" loads further days; "Żaden termin mi nie pasuje" at the end. One line states how long the visit takes.

**Step 4, "Kontakt"** Panel 1: Imię · "Jak wysłać Ci wycenę?" (E-mail / WhatsApp) · the two contact fields · Ulica i numer (optional). Panel 2: "Jak wolisz zapłacić?" (Gotówka / Karta). Then "Podsumowanie" with "Zmień" per row, the marketing checkbox, the privacy line.

**After sending** the form is replaced on the same address by the thank-you state; the estimate bar disappears.

**Behaviour the frames can't show**
- "Dalej" validates the step, then moves focus to the next step's `<h2>` and scrolls to the top of the form. Browser back and "Wstecz" go one step back; nothing typed is lost; a reload keeps the step and the data (session only). Nothing is sent before "Wyślij zapytanie", except photo files, which upload as soon as they are picked.
- "Zmień" in the summary opens that step with the button reading **"Wróć do podsumowania"** (frame `34` shows the label), so a correction costs one tap.
- The 4th photo-step rule: uploads continue while the customer moves on. If any is still running at submit, the button shows "Wysyłamy…" until they finish; a failed photo never blocks sending (the summary says how many were sent).
- After three times are chosen the other pills are disabled; unticking one frees them.
- Ticking "Żaden termin mi nie pasuje" clears and disables the pills and shows the optional free-text field.
- Evening and weekend slots carry "+15%". The surcharge is **not** added to the estimate; it is explained under the slots when such a slot is chosen (frame `27`) and applied in the quote if the visit lands there.
- Sending twice: the button is disabled and busy from the first tap; the request should carry an idempotency key so a retry after a timeout cannot create a second enquiry.
- A chosen slot taken before submit: the customer lands on step 3 with a warning naming the slot (frame `34`); the taken slot is gone, other choices stay, focus is on the warning.

**Motion (CSS only; none under `prefers-reduced-motion`):** accordion chevron rotates 180° in 200ms ease-out; buttons and pills press to scale .96–.98 in 100ms; pill and row colour 150ms ease-out; upload bar `transform: scaleX()` 200ms; estimate sheet rises 12px and fades in 250ms ease-out; skeleton shimmer 1.2s linear (flat tint when motion is reduced); spinner .8s linear. The amount in the bar does not animate.

## 5. Data bindings
Marked `data-bind` in the prototype. Never hard-code these.

| Binding | Shown as | Where |
|---|---|---|
| `{services[]}`: name, included, priceFrom, unit (piece / m²), group, order, visible | rows "od 90 zł", "od 18 zł / m²" | step 1 groups |
| group: lowest `priceFrom` of its visible services | "od 60 zł" in the section header | step 1 |
| `{packages[]}`: name, items, price, priceWas?, tag?, order, visible | "339 zł", struck "380 zł", "taniej o 41 zł" (computed; only when `priceWas` exists) | step 1 Pakiety, estimate |
| `{addons[]}`: name, kind, value, **which groups or services it applies to** | "+30% +54 zł", "+20 zł" | inside a chosen row |
| `{business:min-order}` | "150 zł" | minimum note, estimate row |
| `{estimate}`: rows[], topUp, travel, total, isFrom | "447 zł", "od 447 zł" | bar, sheet, desktop card, summary, thank-you |
| `{towns[]}` with group, zone, postcodes[]; `{zones[]}`: feeType, fee, freeOver, ratePerKm, message | list groups, "Dojazd gratis", "Dojazd 25 zł", "1,50 zł za km" | step 2 |
| `{slots[]}`: start, isAreaDay, surcharge? | "jutro, 13:30", "wt. 17 lis, 18:00 +15%" | step 3 |
| `{areaDay.label}` | "W czwartki jeździmy w Twoją okolicę" (weekday from data) | step 3, only when an area day exists for the town |
| `{visit.durationLabel}` | "3,5 godz." (rounded to half hours, never minutes) | step 3 |
| `{upload}` limits: max 5, 20 MB, JPG/PNG/WebP/HEIC | texts and errors | step 3 |
| `{business:phone}`, `{business:whatsapp}` | "500 000 000" (**placeholder**) | header, other doors |
| `{quoteEta}` | "jeszcze dziś" / "jutro rano" | thank-you |
| `{enquiry.email}`, `{source.page}` | address typed; link back to the counter the visitor came from | thank-you |
| source (counter, channel, UTM) | not shown | sent with the enquiry (Q5) |

**Pre-fill from a counter.** Proposed link format: `/poznan/wycena?z=wozki` (which section opens first) and `&pakiet=pack-family` (package to tick). The form never ticks a single item for the customer; only a package the visitor clicked is pre-selected, with a line saying so.

**Estimate rules as designed** (please confirm against the pricing tests): items × quantity + packages + add-ons → if below `min-order`, a top-up row to exactly the minimum → travel: Zone 1 free, Zone 2 fee unless the amount before travel is at least `freeOver`, other places "w wycenie". The total reads "od …" when a rug is unmeasured or travel is individual. Percent add-ons apply to their item's line; they are "do zmierzenia" for an unmeasured rug.

**Input formats** (same as `admin-cennik-v1`): area accepts whole numbers or a comma (`6`, `7,5`), a dot becomes a comma on blur, `inputmode="decimal"`, "m²" as a fixed suffix, right-aligned, tabular; postcode `00-000`, five digits typed insert the hyphen; phone `+48 000 000 000`, nine digits get "+48" and spacing on blur, `type="tel"`; all inputs 16px text.

## 6. States
| State | Frame | Notes |
|---|---|---|
| Empty | `01`, `11`, `23`, `35` | Estimate bar shows "—" and "wybierz rzeczy" |
| Pre-filled | `03`, `04` | Section order changes; one info line |
| Minimum top-up | `06`, `07` | Never hidden; neutral note, row in the breakdown |
| Travel | `14`–`19` | Text only. The 400 zł rule is one sentence of fact; no progress bar, no "brakuje tylko…" |
| Loading | `28` | Skeleton pills in the list's shape, `aria-busy`, photos usable meanwhile |
| Load error | `29` | Retry; "Żaden termin" is pre-ticked so the step never blocks |
| No slots / one slot | `30`, `31` | The customer can always continue |
| Photo states | `24`, `25` | Per-photo errors only |
| Field errors | `08`, `09`, `20`–`22`, `33`, `38` | Under the field, on blur and on submit; no summary |
| Slot taken | `34` | |
| Sending / failed | `39`, `40` | Form kept |
| Success | `41`, `42` | |
| Long text | `04`, `24` | Names wrap; prices and times never wrap |
| No JavaScript | — | Not designed: the form needs JavaScript for the estimate, uploads and slots. Without it show the heading, the "other doors" (WhatsApp, phone) and a plain link to the price list |

**Error texts**

| Case | Text |
|---|---|
| Nothing chosen | Wybierz przynajmniej jedną rzecz albo pakiet. |
| Rug without area | Wpisz powierzchnię w m² albo zaznacz „Nie znam wymiarów”. |
| No place | Wybierz miejscowość z listy albo wpisz kod pocztowy. |
| Postcode format | Wpisz kod w formacie 00-000. |
| "Inna miejscowość" empty | Wpisz nazwę miejscowości. |
| One time chosen | Wybierz jeszcze jeden termin albo zaznacz „Żaden termin mi nie pasuje”. |
| No time chosen | Wybierz 2 lub 3 terminy albo zaznacz „Żaden termin mi nie pasuje”. |
| Name empty | Wpisz imię. |
| E-mail empty / malformed | Wpisz adres e-mail. / Sprawdź adres e-mail. Powinien wyglądać tak: ty@example.com. |
| Phone empty (WhatsApp) / malformed | Wpisz numer telefonu. / Wpisz numer w formacie +48 000 000 000. (optional field: "… albo zostaw pole puste.") |
| Payment not chosen | Wybierz, jak wolisz zapłacić. |
| Consent ticked without e-mail | Podaj e-mail, żebyśmy mogli wysyłać porady. |
| Photo too big | Plik ma {size} MB. Największy, jaki przyjmiemy, to 20 MB. |
| Photo wrong type | Tego formatu nie otworzymy. Dodaj zdjęcie JPG, PNG, WebP lub HEIC. |
| Photo upload failed | Nie udało się wysłać. Sprawdź internet i spróbuj ponownie. |
| Slots failed to load | Nie udało się wczytać terminów. Sprawdź internet i spróbuj ponownie. Możesz też iść dalej bez terminu: zaproponujemy go w wycenie. |
| Slot taken | Termin {slot} właśnie zajął ktoś inny. Wybierz inny w jego miejsce. Reszta formularza została bez zmian. |
| Sending failed | Nie udało się wysłać zapytania. Sprawdź internet i spróbuj ponownie. Formularz i zdjęcia zostały, niczego nie trzeba wpisywać od nowa. |

No text uses a gendered form for the customer.

## 7. Components
**From Nuxt UI:** `UButton`, `UAccordion` (multiple, `:unmount-on-hide="false"` is not needed here), `UFormField` + `UInput` (trailing slot "m²"), `UInputMenu` (grouped), `UCheckbox`, `URadioGroup` (card variant), `UTextarea`, `UFileUpload` (button variant, list layout), `UProgress`, `UDrawer` (estimate sheet), `UAlert` (soft notes), `USkeleton`, `UStepper` if its markup can carry the four bars, otherwise custom.

**Custom:**
- **`EstimateBar`** (phones) and **`EstimateCard`** (from 900px): described in section 4. The amount carries the sun underline (the one highlight on the screen).
- **`QuoteProgress`**: "Wstecz", "Krok N z 4", four 6px bars with 44px hit areas on the finished ones.
- **`ServiceRow`** with **`QuantityStepper`** (the admin's component) and the add-on and area slots.
- **`PackageRow`**.
- **`ZoneResult`**: `primary-50` card, 40px icon circle, place line, fee in Bricolage 800, optional sentence.
- **`PhotoRow`**: thumbnail, name, status, actions; states uploading, done, failed, rejected.
- **`SlotPicker`**: day rows, checkbox pills (min 76 × 48px), optional "+15%" under the time.
- **`SummaryList`**: rows with an eyebrow label, value and "Zmień".

Heights: inputs and buttons 48px, the "Dodaj zdjęcia" button 56px, every other control at least 44px.

## 8. Accessibility
- One `<h1>`; each step's heading is the only form `<h2>` (the sheet's title is an `<h2>` inside the dialog); sub-sections are `<h3>`, slot groups `<h4>`.
- Focus moves to the step `<h2>` (`tabindex="-1"`) on every step change, to the first invalid field after a failed "Dalej", to the alert after "slot taken" and "sending failed", and to the thank-you `<h2>` after sending.
- The estimate is announced by one polite live region ("Szacunkowa cena: 447 zł"), updated at most once per second and only when the amount changes; the visible amount itself is not live.
- The bar's left half is a button (`aria-expanded`, `aria-controls`) that opens the sheet; the sheet traps focus, closes on Escape and returns focus to the bar.
- Progress is a `<nav>` with an ordered list; the current step has `aria-current="step"`; finished steps are links named "Wróć do kroku 1: Co mamy wyczyścić?".
- Accordion headers are buttons inside `<h3>` with `aria-expanded`; the count badge has a text label ("Wybrane: 2").
- Stepper buttons are named with the item ("Więcej: Fotel", "Usuń: Fotel"); the quantity is an `<output>`.
- The place field is a combobox with a grouped listbox; arrow keys, Enter and Escape work; the result card is `role="status"`.
- Photos: a real file input behind the button; no drag and drop is needed. Each row's buttons name the photo ("Usuń zdjęcie 2"). Upload progress is a `progressbar`; failures are `role="alert"` on that row.
- Slots are checkboxes in a `fieldset`; each is named in full ("wt. 17 lis, 18:00, dopłata 15%"). "Wybrane: 2 z 3" is `role="status"`.
- Required fields carry `aria-required`; optional ones say "(opcjonalnie)" in the label. Errors are linked with `aria-describedby`, fields get `aria-invalid`.
- `autocomplete`: `given-name`, `email`, `tel`, `street-address`, `address-level2`.
- Chosen, error and disabled states are never colour alone: chosen rows have the stepper or a tick, errors have an icon and text, surcharge slots have "+15%".
- Checked automatically on all 42 frames (`screens/checks.json`): no tap target under 44px, no input under 16px, no horizontal scroll (all frames at 390; 1440 on six frames, 768 and 1024 on two, 320 on one), text contrast at least 4.5:1 (3:1 for large text), exactly one `<h1>`.

## 9. Assets and licences
No photos or illustrations. The photo thumbnails in the frames are striped placeholders. Logo: `handoff/brand/logo/logo.svg` (own). Icons: Lucide (ISC) — `phone`, `chevron-left`, `chevron-down`, `chevron-up`, `arrow-right`, `plus`, `minus`, `trash-2`, `check`, `x`, `info`, `circle-alert`, `triangle-alert`, `map-pin`, `image-plus`, `rotate-cw`, `refresh-cw`, `calendar-x`, `loader-circle`, `mail`, `message-circle`, `banknote`, `credit-card`, `package`, `wifi-off`. No custom icons; the section headers have none until the service icons are drawn. Fonts and tokens: unchanged from `stroller-v1`.

## 10. SEO
- **No SEO brief exists for this page.** Designed with one real-text `<h1>` and each step heading as `<h2>`. Working title: "Wycena prania ze zdjęć – Poznań i okolice | Nowiutko". Both are placeholders for the SEO desk.
- Recommendation until the brief says otherwise: `noindex, follow`. The page has no content of its own beyond a form, and the price list and counters should rank for price searches.
- The thank-you state must not be indexable and should not have its own crawlable address.

## 11. Answers to the brief's open questions
1. **One page or four addresses?** One page, `/poznan/wycena`, with the step in the history state (for example `?krok=2`, pushed, not crawled), so browser back moves between steps and a reload keeps the step. One address is simpler for the session rule, gives one canonical page, and lets the thank-you state replace the form without a second page that could be opened cold.
2. **Sticky estimate bar or estimate inside each step?** Sticky bar on phones, holding both the estimate and the step's button. The customer's two questions ("how much so far", "what next") are answered in the thumb zone on every step, and the page keeps one solid button. From 900px it becomes a card beside the form with the breakdown open.
3. **Rugs: is "nie wiem, zmierzymy" allowed?** Yes, as "Nie znam wymiarów". A missing tape measure must not cost an enquiry. The estimate then reads "od …", the rug is listed as "do zmierzenia" with its price per m², and the photos let the owner judge the size for the quote. If the rug is the only item, the estimate is "od 150 zł" (the minimum order).
4. **Street address in step 2 or 4?** Step 4, **optional**, with the hint that it can be given when confirming the quote. It is not needed for the estimate or the slots (the town is), and a required street before the customer has seen a price is the field most likely to stop them. **Consequence for #18:** the quote page must ask for the street before "Potwierdzam" when it is missing.
5. **No free slot in 30 days?** Step 3 says so plainly, offers an optional free-text wish ("Dni i godziny, które Ci pasują") and the customer continues; the summary and thank-you say "Zaproponujemy termin w wycenie". The same applies when slots fail to load. With exactly one free slot, one is enough.
6. **Packages: tab or mixed?** Neither. "Pakiety" is a sixth section in the same list: last on a direct visit, second when arriving from a counter, first and open when the visitor clicked a package. A tab would hide half the basket, and mixing packages into groups would repeat each package in two or three groups. Optional extra (frame `10`): when the chosen items equal a package, one line offers to swap them for it at the lower price.

**Does the stroller page need a `stroller-v2`? No.** Nothing visible changes: every "Wyślij zdjęcia" button keeps its label, style and place, and "Napisz na WhatsApp" and the phone are already there as the other doors. Only link targets change, which is a build detail: the main buttons go to `/poznan/wycena?z=wozki`; the three package cards on the stroller page are not clickable in `stroller-v1`, so nothing passes a package yet. If the owner wants a "Wybierz" link on the package cards (which is what would pre-select a package here), that is a visible change and would be `stroller-v2`. One correction to note: the `stroller-v1` prototype's final button points to `/wycena`; the address is `/poznan/wycena`.

## 12. Open questions
**For the developer**
- Add-ons: the admin (`admin-cennik-v1`) has no "applies to" setting. The form needs to know which add-ons fit which groups or services, and which are customer-selectable (heavy soiling is not). The mapping in the frames is an assumption.
- "Druga strona materaca" and "SUV, 7 miejsc lub van" are shown as add-ons on mattress and car rows. Agreed?
- Evening/weekend: which slots count is data. Is the +15% decided by the confirmed slot (as designed), and is it a percent of the whole visit?
- The "Dom" package includes free travel in Zone 2 (price list). The estimate needs that rule per package.
- Does the 400 zł threshold compare the amount before travel, after add-ons and the minimum top-up (as designed)?
- How long are the chosen times held, and are all two or three held or only the first?
- `{quoteEta}`: what does the app promise after working hours ("jutro rano" in frame `42`)?
- Is "Imię" enough, or does the data model need a surname at enquiry time?
- May the form link carry `?z=` and `&pakiet=` as proposed?
- Is the package suggestion (frame `10`) in scope for v1?

**For the owner**
- Approved with the handover, unchanged (2026-11-15). Estimate wording: a plain amount ("447 zł") under the label "Szacunkowa cena", turning into "od …" only when something is unmeasured. The alternative is "od" always, since list prices are "od".
- Approved with the handover, unchanged (2026-11-15). E-mail is preselected as the channel (it gets the automatic confirmation; WhatsApp is sent by hand at launch). Payment has no default and is required.
- Still open: the privacy sentence and the consent wording need a legal read before launch.
- "Wycenę wyślemy jeszcze dziś" is a promise; it must hold on the days the owner works.
- Still open: the owner's phone number is the placeholder.
