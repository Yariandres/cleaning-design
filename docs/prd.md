# PRD — Sell system for a mobile cleaning business, Poznań

| | |
|---|---|
| **Owner** | Yari Andres |
| **Status** | Product agreed · technical design open |
| **Date** | 8 Nov 2026 |
| **Related** | `docs/spec.md` (condensed spec) · `docs/source/` (research, prices, copy) · `docs/HANDOFF.md` (progress) |

This document says **what** we are building and **why**. It does not choose the stack; that is decided with the developer and recorded in `docs/HANDOFF.md`. Visual design comes from a separate design session as handed-over assets.

---

## 1. Problem

A one-person mobile cleaning business is launching in Poznań and the surrounding county. It cleans sofas, mattresses, rugs, strollers, car seats and car interiors at the customer's door.

The owner is on jobs most of the day. Without a system, enquiries arrive by phone, WhatsApp and Facebook and get answered late, quotes are typed by hand, the calendar lives in someone's head, payments and invoices are chased manually, and nothing tells the owner which marketing actually brings money.

Customers, meanwhile, want three things competitors do badly (from 389 local reviews and a 5-competitor audit):
1. **A clear price before anyone comes** (competitors show net prices + VAT or "wycena indywidualna").
2. **Speed** — a slot in 24–48 h, not weeks.
3. **Reliability** — the only 1-star review in the sample was a no-show.

## 2. Goal

**A sell system, not a brochure site:** one web app that turns visitors into paid, reviewed jobs with as little of the owner's time as possible, and runs the back office from a phone.

### Success metrics

| Metric | Target | Why |
|---|---|---|
| Counter page conversion (visit → enquiry) | ≥ 6.6% at launch, working toward 11% | Typical vs top-quartile landing pages |
| Enquiry → booked job | ≥ 60% | Assumption from planning; verify with real data |
| Owner time per job on admin | ≤ 5 min (quote + confirm + mark done/paid) | The point of the system |
| First reply to an enquiry | Automatic acknowledgement instantly; owner quote within working hours the same day | Speed is a top review theme |
| Revenue tracked by source | 100% of jobs carry a source | To know which collection point earns money |
| Monthly revenue | ~19,500 zł (≈ 65 jobs × 300 zł) at full solo capacity | Just under the 240,000 zł VAT-exemption limit |
| No-shows | 0 | The one thing customers punish |

## 3. Users

**Customers** (Polish-speaking, mostly on phones, arriving from Facebook groups, Google and referrals):

| Persona | Need | First counter |
|---|---|---|
| **Kasia**, parent (flagship) | Stroller / car seat / sofa clean, safe for a newborn, same day | `/poznan/pranie-wozkow` |
| **Tomek**, pet owner | Urine and smell gone, fast | pets counter |
| **Ola**, tenant / landlord | Fresh mattress after previous tenants, fixed price | mattress counter |
| **Marek**, car owner | Car interior cleaned at home, no lost day | car counter |

The suburbs (Swarzędz, Suchy Las, Luboń, Komorniki…) are the core market.

**Owner** — runs everything from a phone between jobs. One user at launch.

**Later:** partner cleaners (own businesses, pay a per-job fee), a second city (Wrocław), customers with an account.

## 4. Scope

### In v1 (launch)

- Public site: homepage + **stroller counter** first, then **sofa counter**
- Quote request flow with live estimate, photos and provisional slot
- Owner admin (6 screens), phone-first
- Quote → confirm → reminder → job → payment → invoice → review → re-clean loop
- Cash or card payment
- Automatic transactional emails, owner alerts, funnel hand-off for opted-in leads
- Cookie consent and analytics; SEO basics
- Data retention and RODO tools

### Later (designed for, not built)

- Pet, mattress and car counters (same template)
- AI booking assistant (site + WhatsApp)
- WhatsApp automation (after Meta verification)
- Customer dashboard / accounts
- Partner portal and multi-cleaner scheduling
- Second city (Wrocław)
- Online prepayment / deposits

### Out of scope

- Logo and visual design (separate work). Brand name decided: **Nowiutko** (`docs/brand.md`)
- Marketing content production (posts, ads)
- Native mobile apps

## 5. Requirements

Priority: **P0** = launch blocker · **P1** = needed soon after launch · **P2** = later.

### 5.1 Public site

| ID | Requirement | P |
|---|---|---|
| S1 | Homepage acts as a "reception desk": shows the menu (4 outcomes + 3 packages + the seasonal "wanted now" item), proof, and routes to the right counter. | P0 |
| S2 | Every counter page follows one anatomy: hero (headline, promise, one button, true urgency line) → proof bar → the headache story → what's included + gross price + matching package → 3 steps → before/after → FAQ → service area → button again. | P0 |
| S3 | Counter pages have **one action** (start a quote); no main menu (logo + phone only); sticky "Wyślij zdjęcia" bar on phones. WhatsApp and phone are alternative doors to the same action. | P0 |
| S4 | All prices shown are gross "od … zł", read from the owner-editable price list. | P0 |
| S5 | Urgency shown must be true: next real free slot, "maks. 3 wizyty dziennie", seasonal booking date. No timers, no fake scarcity. | P0 |
| S6 | Reviews, ratings and before/after photos are shown only when real and entered by the owner (with the customer's consent). Empty slots stay hidden or clearly empty. | P0 |
| S7 | Town pages (e.g. `/poznan/swarzedz`) are generated from the towns list but published only where there is real local content. | P1 |
| S8 | URLs live under the city: `/poznan/...`. | P0 |
| S9 | Master promise on every page: *Przyjeżdżamy na czas. Płacisz tyle, ile podaliśmy ze zdjęć. Jeśli coś wyjdzie po wyschnięciu, wracamy za darmo.* | P0 |

### 5.2 Quote request (customer)

| ID | Requirement | P |
|---|---|---|
| Q1 | Guest flow, no account, 4 steps: (1) items, with a live **"Szacunkowa cena"**; (2) postcode or town → zone and travel fee automatically; (3) up to 5 photos (optional) + 2–3 preferred times; (4) name, phone, email, preferred channel (email / WhatsApp), payment preference (Gotówka / Karta), unticked marketing checkbox. | P0 |
| Q2 | Estimate maths: item prices × qty, packages, **150 zł minimum order**, travel: Zone 1 free · Zone 2 25 zł (free over 400 zł) · Zone 3 1.50 zł/km or quoted. All values editable. | P0 |
| Q3 | Offered slots respect visit duration (sum of item durations + travel buffer by zone), the 3-visits-a-day cap, working hours, area days (preferred, not enforced) and the owner's Google Calendar. | P0 |
| Q4 | On submit: customer gets an instant acknowledgement; owner gets an alert; the slot is held provisionally. | P0 |
| Q5 | The form records the source (counter, channel, UTM) on the job. | P0 |
| Q6 | Town picker groups Poznań districts, Zone 1 suburbs, Zone 2 towns, and "Inna miejscowość" (free text, travel quoted individually). | P0 |

### 5.3 Quote, confirmation and visit

| ID | Requirement | P |
|---|---|---|
| V1 | Owner opens the enquiry, sees photos, adjusts items/price, taps **"Wyślij wycenę"**. | P0 |
| V2 | Customer gets a quote page: items, price, slot, guarantee, payment choice, one **"Potwierdzam"** button. Valid 30 days. | P0 |
| V3 | The quoted price is binding unless the item clearly differs on the day; any change is agreed **before** work starts. | P0 |
| V4 | Unconfirmed quotes get automatic follow-ups. | P0 |
| V5 | Reminder the day before with **"Potwierdzam / Zmieniam termin"**. Free self-service reschedule/cancel until 24 h before; later = phone call. No fees at launch. | P0 |
| V6 | Guarantee rules are encoded: late > 15 min → call ahead; owner no-show → 50% off the rescheduled visit; re-clean within 7 days. | P1 |

### 5.4 Payment and paperwork

| ID | Requirement | P |
|---|---|---|
| P1 | Customer chooses **cash or card**; can switch on the quote page or at the job. | P0 |
| P2 | Card: "Zapłać teraz" (BLIK, Przelewy24, card, Apple/Google Pay) available from confirmation onward, from the quote page, the reminder, and a QR shown on the owner's phone at the job. Marked paid automatically. | P0 |
| P3 | Cash: owner taps "Gotówka otrzymana" on the Today screen → paid. | P0 |
| P4 | Bank transfer as fallback; owner can mark paid manually. | P0 |
| P5 | Unpaid card jobs get a gentle reminder 24 h after "Wykonane". | P1 |
| P6 | Every business sale and every invoice request gets a **faktura "zw."** (VAT-exempt, art. 113) issued through the invoicing service and sent to **KSeF**. Private customers get a receipt from the cash register by default. | P0 |
| P7 | A per-job sales log matches the cash register; the Today screen reminds the owner to print the receipt when a job is marked paid. | P0 |
| P8 | Revenue is tracked against the **240,000 zł** VAT limit with a warning at 80%. | P0 |

### 5.5 After the job

| ID | Requirement | P |
|---|---|---|
| A1 | After "Opłacone": Google review request. | P0 |
| A2 | **"Coś nie tak?"** link valid 7 days: customer uploads a photo, picks a slot → free re-clean job linked to the original + owner alert. | P0 |
| A3 | Referral: −10% for both sides; opt-in discount −10%; discounts don't stack. | P1 |
| A4 | 12-month "time for a refresh" reminder to opted-in customers. | P2 |

### 5.6 Owner admin (phone-first, installable)

| ID | Screen | Requirement | P |
|---|---|---|---|
| D1 | **Dziś** | Today's visits in driving order: address, items, photos, navigation, "Gotówka otrzymana", "Wykonane", receipt reminder. | P0 |
| D2 | **Lejek** | Pipeline board: Zapytanie → Wycena wysłana → Zarezerwowane → Wykonane → Opłacone → Opinia, plus Utracone / Anulowane. Each stage triggers its message. | P0 |
| D3 | **Kalendarz** | Availability, working hours, area days, two-way Google Calendar sync. | P0 |
| D4 | **Klienci** | Search, history, addresses, one-click RODO export / delete. | P0 |
| D5 | **Cennik i ustawienia** | Prices, packages, durations, zones, towns, area days, FAQ, "wanted now" item, working hours. | P0 |
| D6 | **Raport** | Source → enquiries → bookings → revenue per counter and tagged link; VAT-limit bar. | P0 |
| D7 | Login | Passwordless (email link or code), session remembered on the phone. | P0 |
| D8 | Roles | owner / partner / customer exist in the data model from day one; only owner is used at launch. | P0 |

### 5.7 Messages and alerts

| ID | Requirement | P |
|---|---|---|
| M1 | Transactional email for: acknowledgement, quote, confirmation, reminder, payment link, paid, review request, re-clean. | P0 |
| M2 | Funnel/marketing only for people who ticked the checkbox, with **double opt-in**; the app assigns them to the group of their counter (lp-wozki, lp-zwierzeta, lp-materace, lp-auto, lp-kanapy) and updates stage tags. | P0 |
| M3 | Instant private owner alerts (new enquiry, confirmation, payment, re-clean) with a link to the job. | P0 |
| M4 | WhatsApp: manual at launch with "Napisz na WhatsApp" buttons; automated templates after Meta verification; Telegram as fallback channel. | P1 |
| M5 | Test sending from a temporary domain is fine; **customers only ever see the brand domain**. | P0 |

### 5.8 Data

| ID | Requirement | P |
|---|---|---|
| T1 | Customer identified by phone or email; many addresses; many jobs. | P0 |
| T2 | Job: line items from the price list, zone + travel fee, photos, notes, payment method, source, stage history, linked re-clean jobs. | P0 |
| T3 | Every price list, zone, town, area day and page belongs to a **city**. Only Poznań is active. | P0 |
| T4 | Prices and business data editable by the owner; never hard-coded. | P0 |

## 6. Non-functional requirements

| Area | Requirement |
|---|---|
| Performance | Main content < 2.5 s on 4G on a mid-range phone; Lighthouse mobile ≥ 90 on public pages |
| Accessibility | WCAG 2.2 AA: contrast, keyboard access, visible focus, 44 px tap targets, reduced motion respected |
| SEO | Server-rendered public pages; LocalBusiness, Service, FAQPage, Offer structured data; sitemap. Staging never indexable |
| Language | Polish UI, "Ty" voice, all strings translation-ready |
| Privacy (RODO) | Separate, unticked marketing consent; double opt-in; cookie banner with equal Accept/Reject; analytics only after consent (Consent Mode v2); no other trackers |
| Retention | Quote photos 12 months; never-booked enquiries 12 months; customers, jobs, invoices 5 years; consent until withdrawn; public photo use only with separate consent |
| Security | Secrets never in the repo; least-privilege API keys; uploads validated (type, size) |
| Reliability | Daily off-server database backups; a restore tested before launch; health check for the hosting platform |
| Hosting | EU only (owner's VPS with Dokploy) |
| Quality gate | Tests for pricing/zone maths and one end-to-end booking test must pass before every deploy |

## 7. Compliance constraints (Poland, 2026)

- **VAT exemption** while yearly revenue < 240,000 zł (prorated in the first year). The system tracks it.
- **Invoices:** VAT-exempt sales are documented with a faktura "zw.", never a "rachunek". **KSeF** applies, with penalties from 1 Jan 2027.
- **Cash register:** accepting cash removes the cashless exemption; private-customer sales above 20,000 zł/year need a register. App-only (virtual) registers are not allowed for upholstery cleaning (allowed for car washing from 1 Apr 2026). Plan: a mobile online cash register for all private-customer sales. **Accountant to confirm.**
- **RODO / ePrivacy:** see §6.
- **Consumer honesty:** no invented reviews; true urgency only.

## 8. Integrations (services chosen in planning; confirm during technical design)

| Need | Planned service |
|---|---|
| Card / BLIK / Przelewy24 payments | Stripe |
| Invoices + KSeF | Fakturownia |
| Transactional email | MailerSend |
| Funnel / marketing email | MailerLite |
| Owner alerts | Telegram bot |
| Calendar | Google Calendar (two-way) |
| Messaging | WhatsApp Business (manual → platform API) |
| Analytics | Google Analytics + Search Console |
| Reviews | Google Business Profile (link out) |

## 9. Release plan

1. **Technical setup agreed** and recorded; empty app on hidden staging.
2. **Data + settings:** price list, zones, towns, durations, area days editable.
3. **Quote request flow** (customer side).
4. **Admin core:** login, pipeline, Today, send quote, confirmation page.
5. **Money and messages:** payments (card + cash), invoicing, emails, alerts, funnel hand-off.
6. **Homepage + stroller counter** from the design handover; SEO, cookies, analytics.
7. **Sofa counter → launch** on the brand domain.

**Launch criteria:** all P0 requirements met; end-to-end booking test passing (enquiry → quote → confirm → pay by card in test mode, and the cash path); backup restore tested; brand domain live with email sending set up; accountant has confirmed the cash register setup.

## 10. Risks and open questions

| Risk / question | Mitigation / owner |
|---|---|
| Trademark not yet filed for Nowiutko | Patent attorney clearance, then UPRP filing (class 37). Owner |
| Cash register setup and PKWiU code unconfirmed | Accountant before launch. Owner |
| Meta verification delay | Manual WhatsApp at launch; Telegram fallback |
| Low early review count weakens proof | Hide empty proof; ask every customer for a review |
| Conversion and booking-rate assumptions | Measure from day one via the source report |
| Technical stack not yet decided | Agree in Claude Code before scaffolding |

---

## Appendix A — Decision log (grilling session, 7 Nov 2026)

Each line: the decision, then why. "Tech — open" marks decisions about *how* that are being revisited in technical design.

**Round 1 — scope and foundations**
1. **Launch scope:** homepage + stroller + sofa counters, quote/booking, owner admin, automatic messages; AI assistant, customer dashboard, partner portal, multi-city, prepayment later. *Why: smallest system that sells and saves the owner time.*
2. **Owner-only, phone-first admin; roles in the data from day one.** *Why: one user now, partners later without a rebuild.*
3. **Request + provisional slot, confirmed by the owner.** *Why: photos decide the real price; instant booking would break "you pay what we quoted".*
4. **Live estimate from the price list.** *Why: price is the #1 customer question.*
5. **App-managed availability with two-way Google Calendar sync.** *Why: one source of truth for slots, still visible in the owner's calendar.*
6. **EU hosting on the owner's Dokploy VPS, with backups.** *Tech — open (hosting stays EU/Dokploy).*
7. **Cashless only** — *superseded 7 Nov: customer chooses cash or card (see 42).*
8. **Polish only, translation-ready.** *Why: market is Polish; a second language later must be cheap.*
9. **Quote photos deleted after 12 months; public use only with separate consent.** *Why: RODO data minimisation.*

**Round 2 — infrastructure, money flow, messaging**

10. **One app, one deploy, daily off-server backups.** *Tech — open.*
11. **Passwordless login for everyone.** *Why: nothing to forget or leak; works on a phone.*
12. **MailerSend for transactional, MailerLite for funnel.** *Why: marketing tools are poor at one-off transactional mail; same vendor family.*
13. **Manual WhatsApp at launch, automation after Meta approval, Telegram fallback.** *Why: verification takes time; don't block launch.*
14. **Pipeline stages, each tied to a message.** *Why: the stage is what triggers automation.*
15. **One-tap quote, one-click confirm, valid 30 days, automatic follow-ups.** *Why: minimum owner time, minimum customer friction.*
16. **Payment link after the job, paid status automatic, transfer fallback.** *Why: no chasing payments.*
17. **Invoicing through an API service, not built.** *Why: KSeF and tax rules change; a specialist handles them.*
18. **Private Telegram bot for owner alerts.** *Why: free, instant, independent of Meta.*
19. **Business data editable in admin; long page copy in content files.** *Why: owner changes prices often, copy rarely.*
20. **Temporary hidden subdomain until name/domain are chosen.** *Why: build doesn't wait for branding.*

**Round 3 — day-to-day behaviour**

21. **Stripe** (BLIK, P24, card in one link). *Why: one integration, good API; P24-direct slightly cheaper but more work.*
22. **Fakturownia; an invoice for every paid job; virtual receipts for car jobs.** *Partly superseded by 42–43: register receipts for private customers, faktura for businesses and on request.*
23. **One customer, many addresses and jobs; every job tagged with its source.** *Why: repeat work and source reporting.*
24. **Visit length from items + travel, editable.** *Why: realistic slots without manual planning.*
25. **Optional area days that order slots (not hard rules).** *Why: less driving without turning customers away.*
26. **4-step guest form.** *Why: short form, no account, photos optional.*
27. **App controls MailerLite tags; only opted-in people enter it.** *Why: right sequence per counter; RODO.*
28. **Own lightweight cookie banner; GA only after consent.** *Why: compliant and fast.*
29. **Source → bookings → revenue report.** *Why: know which collection point earns money, not just traffic.*
30. **Server-rendered pages, structured data, town pages only with real content.** *Why: local SEO without thin pages.*
31. **Google review request; only real reviews shown.** *Why: trust; honesty rule.*
32. **Self-service re-clean within 7 days.** *Why: the guarantee costs the owner no admin.*
33. **Free changes up to 24 h; no fees at launch.** *Why: lower booking anxiety; revisit if abused.*
34. **Test on temporary domain; launch only on brand domain.** *Why: customers never see a placeholder address.*
35. **Private GitHub repo, auto-deploy to staging, tests before deploy.** *Tech — open (tests-before-deploy stays).*

**Round 4 — admin, growth, quality**

36. **Six admin screens; VAT-limit warning at 80%.** *Why: covers the whole day from a phone.*
37. **City in the data from day one.** *Why: Wrocław becomes a settings task.*
38. **Stroller mockup as the design system.** *Superseded: visual design now comes from the separate design session.*
39. **Quality targets checked automatically.** *Why: phone-first market; speed and accessibility are conversion.*
40. **Retention rules + one-click RODO export/delete.** *Why: legal requirement, no manual digging.*
41. **"Szacunkowa cena" first, quote binding, changes agreed before work.** *Why: protects the master promise.*

**After the session**

42. **Customer chooses cash or card** (owner, 7 Nov). *Why: many customers want to pay cash at the door.*
43. **Mobile online cash register for all private-customer sales** (proposed, accountant to confirm). *Why: cash removes the cashless exemption; virtual registers aren't allowed for upholstery cleaning.*
44. **Developer-only repo; pnpm; stack decided in Claude Code** (owner, 8 Nov).
