# Design brief

Read this before designing anything. Full sources are in `docs/source/`; product requirements are in `docs/prd.md`.

## The business in one line

*We clean what your family lives on (sofa, mattress, stroller, car seat and car) at your door in Poznań and the suburbs, at the price quoted from your photos, and usable the same day.*

One-person, mobile cleaning business. Launching in Poznań; built to add partner cleaners and a second city (Wrocław) later. Brand name: **Nowiutko** (nowiutko.pl). Symbol: a **chamomile flower**; voice: **freshness**; one look across all services with a light accent per service. Everything is in `docs/brand.md` — read it first.

## Who we design for

| Persona | Who | Headache (their words) | Our promise |
|---|---|---|---|
| **Kasia**, the parent (flagship) | Mum on Winogrady, second baby due | "Boję się chemii przy noworodku i zacieków na podszewce." | Wózek gotowy na popołudniowy spacer, bezpieczny dla niemowlęcia. |
| **Tomek**, the pet owner | Rents on Rataje, puppy + cat | "Plama znika, ale zapach wraca." | Zapach znika, a nie jest maskowany, albo wracamy za darmo. |
| **Ola**, the tenant | Just moved into a rented flat | "Nie chcę spać na cudzym materacu i nie mam Karchera." | Świeży materac jeszcze dziś, za stałą cenę od 150 zł. |
| **Marek**, the car owner | Dad on Grunwald, selling the car in spring | "Nie mam całego dnia, żeby odstawić auto." | Czyste wnętrze auta pod Twoim domem, bez straconego dnia. |

The suburbs (Swarzędz, Suchy Las, Luboń, Komorniki…) are the core market: young families, free travel in Zone 1.

**Master promise, on every page:** *Przyjeżdżamy na czas. Płacisz tyle, ile podaliśmy ze zdjęć. Jeśli coś wyjdzie po wyschnięciu, wracamy za darmo.*

## How it should feel

- **A friendly, competent neighbour.** Warm, calm, clean, trustworthy — never corporate, never "cheap cleaning flyer".
- **Fresh, not clinical.** Mint and teal for clean; a sunny yellow for the one thing that matters on a screen.
- **Family-safe.** Soft corners, generous space, real photos of real items. No stock-photo smiling cleaners, no sparkle emojis, no bubbles clip-art.
- **Phone first.** Most visitors arrive on a phone from a Facebook group or Google. Thumb-reachable buttons, sticky bottom bar.

## What competitors get wrong (we do the opposite)

- Walls of keyword-stuffed text → we use short, plain Polish in the customer's words.
- Net prices + 23% VAT, "wycena indywidualna" → we show **gross "od" prices** everywhere.
- Strollers and pets buried in a price list → each gets its **own counter page**.
- Suburbs treated as an extra cost → **"Dojazd gratis"** is a feature.
- Vague drying times → stated per item, up front.
- Only one competitor shows a guarantee → ours is in the proof bar.

## The site structure

- **Homepage = reception desk.** Offers choices, proves we're legit, points people to the right counter. Never the best seller.
- **Counters = landing pages**, one per persona: `/poznan/pranie-wozkow` (build first), `/poznan/pranie-kanap`, pets, mattresses, car.
- **Every counter has the same anatomy:**
  1. Hero: headline matching the ad/search, one promise line, one button, urgency line under it
  2. Proof bar: rating + review count, "Ubezpieczenie OC", "Gwarancja poprawki 7 dni"
  3. The headache: headache → why it hasn't gone away → aspirin → proof → next step
  4. What's included and the price (gross), matching package
  5. How it works: three steps
  6. Before and after: real photos of this service only
  7. FAQ: the 4–6 questions people actually ask
  8. The area: zones and "dojazd gratis"
  9. The button again, with the guarantee line
- **Conversion rules:** one action only (every button does the same thing); no main menu on counters (logo + phone only); headline matches the source; sticky "Wyślij zdjęcia" bar on phones; short form; price always visible; real proof only.

## Hard rules

- **Never invent reviews, ratings, review counts, customer names or before/after photos.** Leave an empty, clearly marked slot until real ones exist.
- **Urgency must be true.** No countdown timers, no "only 2 left". Allowed: real next free slot, "maks. 3 wizyty dziennie", the Christmas booking date.
- **Polish UI, "Ty" voice.** English only in code and comments.
- **Accessibility and speed are part of the design:** WCAG AA contrast, visible focus, 44px tap targets, main content under 2.5 s on 4G, Lighthouse mobile 90+.
- **Prices come from data** (the owner edits them in the admin), so mark them as data bindings in every handover. Use `docs/source/price-list.md` for realistic sample data.
