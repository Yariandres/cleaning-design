"""Builds the final stroller counter (Direction 2) and its states board. Run: python3 build_final.py

stroller-v1.1 (early launch, owner priority cleaning-design#5): no quote form yet. The one action is
"Wyślij zdjęcia na WhatsApp" (wa.me with a prefilled message); the phone call is the second action; SMS is the fallback.
stroller-v1 (quote-form version) stays reproducible from the tag `stroller-v1`."""
import os, sys
from urllib.parse import quote
sys.argv = [sys.argv[0]]
import build as B   # reuses helpers/sections; importing also regenerates the three direction pages
ico = B.ico
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "final")

TITLE = "Pranie wózków i fotelików Poznań – u Ciebie, od 80 zł"
DESC = "Pierzemy wózki, gondole i foteliki u Ciebie w domu, w Poznaniu i okolicach. Gotowe tego samego dnia. Cena ze zdjęć przed przyjazdem, od 80 zł."

# Contact: all three come from data ({business:phone}, {business:whatsapp}); the prefilled text is page copy (copy.md: whatsapp.prefill)
PHONE = "736 369 704"
TEL = "tel:+48736369704"
SMS = "sms:+48736369704"
WA_PREFILL = "Dzień dobry, proszę o wycenę prania wózka lub fotelika. Wysyłam zdjęcia. Miejscowość: "
WA = "https://wa.me/48736369704?text=" + quote(WA_PREFILL)
WA_LABEL = "Wyślij zdjęcia na WhatsApp"
def wa_btn(pos, cls="btn btn-main"):
    return f'<a class="{cls}" href="{WA}" rel="noopener" data-bind="business:whatsapp" data-cta="whatsapp" data-cta-pos="{pos}">{ico("camera")}{WA_LABEL}</a>'

HEADER = f'''<header class="site-h"><div class="wrap"><a href="/" aria-label="Nowiutko, strona główna"><img src="../assets/logo.svg" alt="Nowiutko" width="190" height="46"></a>
<div style="display:flex;gap:20px;align-items:center"><a class="tel" href="{TEL}" data-bind="business:phone" data-cta="phone" data-cta-pos="header">{ico("phone")}<span class="num">{PHONE}</span></a>{wa_btn("header")}</div></div></header>'''
STICKY = f'<div class="sticky">{wa_btn("sticky")}<a class="btn btn-ghost" href="{TEL}" aria-label="Zadzwoń: {PHONE}" data-bind="business:phone" data-cta="phone" data-cta-pos="sticky">{ico("phone")}</a></div>'

def hero_rows():
    rows = [("Wózek spacerowy", 90, "stroller-single"), ("Wózek 2w1", 120, "stroller-2in1"), ("Fotelik samochodowy", 80, "carseat"), ("Wózek 3w1", 160, "stroller-3in1")]
    return "".join(f'<li><span>{n}</span><b class="num" data-bind="price:{k}"><i>od</i> {p}&nbsp;zł</b></li>' for n, p, k in rows)

HERO = f'''<section class="hero2"><div class="wrap">
<div class="h2-copy"><h1 class="eyebrow">Pranie wózków i fotelików dziecięcych w Poznaniu i okolicach</h1>
<p class="display">Wózek jak nowe. <span>Pod Twoim domem, tego samego dnia.</span></p>
<p class="lede">Przyjeżdżamy z własnym sprzętem. Ty nie wyjmujesz dziecka z domu, nie wozisz wózka i nie czekasz trzech dni.</p>
<ul class="ticks"><li>{ico("check")}Hipoalergiczne środki</li><li>{ico("check")}Foteliki według instrukcji producenta</li><li>{ico("check")}Dojazd gratis w Strefie 1</li></ul></div>
<div class="pcard"><div class="pc-head"><span class="eyebrow">Cennik brutto</span><span class="pc-sub">cena ze zdjęć, przed przyjazdem</span></div>
<ul class="pc-rows">{hero_rows()}</ul>
<p class="nextslot" data-bind="nextFreeSlot" hidden>{ico("calendar-check")}<span>Najbliższy wolny termin: <b data-bind="nextFreeSlot.label">jutro, 10:00</b></span></p>
{wa_btn("hero")}
<p class="pc-promise">2–3 zdjęcia wystarczą. Cenę podamy dziś.</p>
<div class="pc-links"><a class="ulink" href="#cennik">Pełny cennik i pakiety</a><a class="ulink num" href="{TEL}" data-bind="business:phone" data-cta="phone" data-cta-pos="hero">Zadzwoń: {PHONE}</a></div></div></div></section>'''

PRICE_ROWS = [("Wózek spacerowy", "siedzisko, budka, pasy, stelaż i koła", 90, "stroller-single"),
              ("Wózek 2w1", "gondola + spacerówka, stelaż i koła", 120, "stroller-2in1"),
              ("Wózek 3w1", "z fotelikiem-nosidełkiem", 160, "stroller-3in1"),
              ("Wózek bliźniaczy", "", 150, "stroller-twin"),
              ("Fotelik samochodowy", "pokrowiec, skorupa, baza", 80, "carseat"),
              ("Krzesełko, leżaczek lub mata", "", 60, "highchair")]
PACKS = [("przed porodem", "Nowy Członek Rodziny", ["Materac dwuosobowy", "Wózek 2w1", "Fotelik samochodowy"], 319, 350, "pack-new-member", False),
         ("najczęściej wybierany", "Rodzinny", ["Kanapa 3-osobowa", "Wózek 2w1", "Fotelik samochodowy"], 339, 380, "pack-family", True),
         ("auto i maluch", "Auto i Maluch", ["Pranie tapicerki auta", "Wózek 2w1", "Fotelik samochodowy"], 409, 460, "pack-car-baby", False)]

def price_section(band):
    rows = "".join(f'<li><span>{n}{"<small>"+d+"</small>" if d else ""}</span><b data-bind="price:{k}"><i>od</i>{p}&nbsp;zł</b></li>' for n, d, p, k in PRICE_ROWS)
    packs = ""
    for tag, name, items, p, was, k, hot in PACKS:
        style = '' if tag != "auto i maluch" else ' style="background:var(--p100);color:var(--p800)"'
        packs += f'<div class="pack{" hot" if hot else ""}"><span class="tag"{style}>{tag}</span><h3>{name}</h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + f'</ul><div class="pr"><b class="num" data-bind="price:{k}">{p}&nbsp;zł</b><s class="num" data-bind="price:{k}-was">{was}&nbsp;zł</s></div></div>'
    return f'''<section id="cennik" class="{band}"><div class="wrap"><div class="sec-head"><span class="eyebrow">Cennik</span><h2>Pranie wózka i fotelika – cena</h2><p class="lede">Ceny brutto, z dojazdem w Strefie 1. Dokładną kwotę podajemy ze zdjęć, zanim przyjedziemy.</p></div>
<div class="price-wrap"><div><ul class="plist">{rows}</ul><p class="pnote">Minimalne zamówienie <span data-bind="business:min-order">150&nbsp;zł</span>. Przy silnych zabrudzeniach (pleśń, wymioty) wycenimy ze zdjęć przed przyjazdem.</p></div>
<aside class="safety on-dark"><span class="eyebrow">Foteliki samochodowe</span><h3>Fotelik to sprzęt bezpieczeństwa. Tak go traktujemy.</h3><ul><li>Pokrowiec i skorupę czyścimy według instrukcji producenta.</li><li>Pasy czyścimy tylko powierzchniowo, bo moczenie osłabia ich wytrzymałość.</li><li>Środki hipoalergiczne, bezpieczne dla niemowląt po wyschnięciu.</li></ul></aside></div>
<div class="packs">{packs}</div></div></section>'''

STEPS = B.STEPS.replace("przez WhatsApp, SMS lub formularz", "przez WhatsApp lub SMS").replace('</ol></div></section>', '</ol><div style="margin-top:32px">' + wa_btn("steps") + '</div></div></section>')
assert "formularz" not in STEPS

# hidden slots: present in the HTML for the developer, shown only when real content exists
BEFORE_AFTER = '''<section id="przed-po" hidden data-slot="before-after" data-show-when="real before/after photos with customer consent exist (PRD S6)"><div class="wrap"><div class="sec-head"><span class="eyebrow">Efekty</span><h2>Wózki przed i po praniu</h2></div>
<div class="ba-grid"><figure class="ba"><div class="ph ratio43" role="img" aria-label="Przed">przed</div><div class="ph ratio43" role="img" aria-label="Po">po</div></figure></div></div></section>'''
REVIEWS = '''<section id="opinie" hidden data-slot="reviews" data-show-when="real Google reviews entered by the owner exist"><div class="wrap"><div class="sec-head"><span class="eyebrow">Opinie</span><h2>Co mówią rodzice</h2></div></div></section>'''

AREA = B.AREA  # v1.1: no link to /poznan/obszar-dzialania until that page exists (restore with it; SEO brief §4)

FINAL = f'''<section id="kontakt" class="final on-dark"><div class="wrap"><h2>Wyślij 2–3 zdjęcia. Cenę podamy dziś.</h2><p>Przyjeżdżamy na czas. Płacisz tyle, ile podaliśmy ze zdjęć. Jeśli coś wyjdzie po wyschnięciu, wracamy za darmo.</p>
<div class="fin-btns">{wa_btn("final")}<a class="btn btn-ghost-light num" href="{TEL}" data-bind="business:phone" data-cta="phone" data-cta-pos="final">{ico("phone")}Zadzwoń: {PHONE}</a></div>
<p class="fin-note">Nie masz WhatsAppa? Wyślij zdjęcia <a href="{SMS}" data-bind="business:phone" data-cta="sms" data-cta-pos="final">SMS-em na ten sam numer</a>.</p></div></section>'''

# ---------------- footer (stroller-v1.2 draft; shared component: handoff/components/footer.md) ----------------
# Company details are NOT known yet (asked of the owner, 2026-11-16). Nothing here is a real or realistic value:
# every unknown is a bracketed, dashed placeholder (.tbd) and a data key. Never ship a placeholder; a missing
# optional key removes its line, and a missing legal name or NIP removes the whole "Dane firmy" block.
def tbd(key, text):
    return f'<span class="tbd" data-bind="business:{key}">[{text}]</span>'
COMPANY_DEFAULT = dict(name=tbd("legal-name", "nazwa firmy z CEIDG"), nip=tbd("nip", "NIP"))
COMPANY_LONG = dict(name=tbd("legal-name", "Imię Nazwisko Nazwa Firmy – pełna nazwa z CEIDG, także gdy jest długa"),
                    address=[tbd("address-line1", "ulica, numer domu i numer lokalu"), tbd("address-line2", "kod pocztowy i miejscowość")],
                    nip=tbd("nip", "NIP: 10 cyfr"), regon=tbd("regon", "REGON: 9 cyfr"), email=tbd("email", "adres e-mail na nowiutko.pl"))
def footer(company=COMPANY_DEFAULT):
    c = company or {}
    email = f'<div class="f-row"><span class="k">E-mail</span><span class="v">{c["email"]}</span></div>' if c.get("email") else ""
    firm = ""
    if c.get("name") and c.get("nip"):
        addr = ""
        if c.get("address"):
            addr = "<p>" + "<br>".join(c["address"]) + '</p><p class="f-note">To adres firmy, nie punkt przyjęć. Pierzemy u Ciebie.</p>'
        ids = f'<span class="nw">NIP {c["nip"]}</span>' + (f' <span class="nw">REGON {c["regon"]}</span>' if c.get("regon") else "")
        firm = f'<div class="f-col f-firm"><p class="eyebrow">Dane firmy</p><p class="f-name">{c["name"]}</p>{addr}<p class="f-ids num">{ids}</p></div>'
    return f'''<footer class="site-f"><div class="wrap">
<div class="f-grid{"" if firm else " no-firm"}">
<div class="f-brand"><img src="../assets/logo.svg" alt="Nowiutko" width="128" height="36"><p>Pranie tapicerki, wózków i aut u Ciebie.<br>Poznań i okolice.</p></div>
<address class="f-col f-contact"><p class="eyebrow">Kontakt</p>
<a class="f-row" href="{TEL}" data-bind="business:phone" data-cta="phone" data-cta-pos="footer"><span class="k">Telefon</span><span class="v num">{PHONE}</span></a>
<a class="f-row" href="{WA}" rel="noopener" data-bind="business:whatsapp" data-cta="whatsapp" data-cta-pos="footer"><span class="k">WhatsApp</span><span class="v num">{PHONE}</span></a>{email}</address>
{firm}</div>
<nav class="f-legal" aria-label="Informacje"><a href="/polityka-prywatnosci">Prywatność</a><button type="button" data-action="open-cookie-settings">Ustawienia cookies</button></nav>
</div></footer>'''

def page(extra_head="", body_extra="", company=COMPANY_DEFAULT):
    main = (HERO + B.PROOF2 + B.HEADACHE2.replace("{band}", "band") + price_section("") + STEPS + BEFORE_AFTER + B.SEATS.replace("{band}", "band") + REVIEWS + B.FAQ + AREA.replace("{band}", "band") + FINAL)
    return f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITLE}</title><meta name="description" content="{DESC}"><link rel="canonical" href="https://nowiutko.pl/poznan/pranie-wozkow-i-fotelikow">
<link rel="stylesheet" href="../base.css"><style>{B.CSS2}{FINAL_CSS}</style>{extra_head}</head><body>
{HEADER}<main>{main}</main>{footer(company)}{STICKY}{body_extra}</body></html>'''

FINAL_CSS = '''
.pc-links{display:flex;justify-content:center;gap:0 24px;flex-wrap:wrap}
.ulink{font-weight:700;color:var(--p600);text-decoration:underline;text-decoration-color:transparent;text-decoration-thickness:2px;text-underline-offset:4px;transition:text-decoration-color .2s;min-height:44px;display:inline-grid;align-items:center}
.nextslot{display:flex;gap:10px;align-items:center;background:var(--s50);border:1px solid var(--s200);border-radius:var(--r-lg);padding:10px 14px;color:var(--s950);font-size:.95rem;margin:0}.nextslot .ico{color:var(--s800)}
.ulink:hover{text-decoration-color:currentColor}
.pnote .ulink,.lede .ulink,.cookie .ulink{display:inline;min-height:0;text-decoration-color:currentColor}
.final .fin-btns{display:flex;gap:12px;flex-wrap:wrap;width:100%}.final .fin-btns .btn{flex:1 1 240px}@media(min-width:700px){.final .fin-btns .btn{flex:0 0 auto}}
.btn-ghost-light{border-color:#fff;color:#fff;background:transparent}.btn-ghost-light:hover{background:rgba(255,255,255,.12)}
.fin-note{color:var(--p100)}.fin-note a{font-weight:700;color:#fff}
/* footer (v1.2): brand line, contact, company details, legal row. Quiet: no solid button, no page navigation. */
.site-f{padding-block:40px 20px;color:var(--text-muted);font-size:.9rem;border-top:1px solid var(--border)}
.f-grid{display:grid;gap:28px}
.f-brand{display:grid;gap:12px;align-content:start}.f-brand img{height:36px;width:auto;display:block}
.f-col{display:grid;align-content:start;font-style:normal;min-width:0}.f-col .eyebrow{margin-bottom:4px}
.f-row{display:flex;align-items:center;gap:12px;min-height:44px;text-decoration:none}
.f-row .k{flex:0 0 5.5rem}.f-row .v{font-weight:700;color:var(--n900);min-width:0;overflow-wrap:anywhere}
a.f-row .v{text-decoration:underline;text-decoration-color:transparent;text-decoration-thickness:2px;text-underline-offset:4px;transition:text-decoration-color .2s}a.f-row:hover .v{text-decoration-color:currentColor}
.f-firm{gap:4px}.f-firm .eyebrow{margin-bottom:9px}.f-firm p{overflow-wrap:anywhere}.f-name{font-weight:700;color:var(--n700)}.f-note{font-size:.84rem}
.f-ids{display:flex;flex-wrap:wrap;gap:0 16px}.nw{white-space:nowrap}
.f-legal{display:flex;flex-wrap:wrap;gap:0 24px;margin-top:28px;padding-top:8px;border-top:1px solid var(--border)}
.f-legal a,.f-legal button{min-height:44px;display:inline-grid;align-items:center;font-weight:600;color:var(--n700)}
.f-legal button{font:inherit;font-weight:600;background:none;border:0;padding:0;cursor:pointer;text-decoration:underline}
@media(min-width:640px){.f-grid{grid-template-columns:1fr 1fr;gap:32px 40px}.f-brand{grid-column:1/-1}.f-grid.no-firm .f-brand{grid-column:auto}}
@media(min-width:900px){.site-f{padding-block:56px 24px}.f-grid{grid-template-columns:1.25fr 1fr 1.25fr;gap:56px}.f-brand{grid-column:auto}.f-grid.no-firm{grid-template-columns:1.25fr 2.25fr}}
/* prototype only: an unknown value. Never ships. */
.tbd{display:inline;padding:1px 6px;border:1.5px dashed var(--n400);border-radius:6px;background:repeating-linear-gradient(135deg,var(--n100) 0 6px,var(--n50) 6px 12px);color:var(--n700);font-weight:600;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.nextslot[hidden]{display:none}
.pc-promise{text-align:center;color:var(--text-muted);font-size:.93rem;margin-top:-6px}
.sticky .btn-main{white-space:nowrap}.sticky .btn-ghost{flex:0 0 48px;padding-inline:0}@media(max-width:359px){.sticky .btn-main .ico{display:none}.sticky .btn-main{padding-inline:8px;font-size:.94rem}}
.ratio43{aspect-ratio:4/3}.ba-grid .ba{display:grid;gap:12px;grid-template-columns:1fr 1fr;margin:0}
.btn:hover{background-color:var(--p600)}.btn-ghost:hover{background:var(--n100)}
.btn-main:hover{transform:translateY(-1px)}
.plist li{padding-block:18px}
.skip{position:absolute;left:12px;top:-60px;background:#fff;color:var(--n900);padding:12px 16px;border-radius:12px;z-index:50;font-weight:700}.skip:focus{top:12px}
@media (prefers-reduced-motion:reduce){.btn-main:hover,a.pc:hover,a.pc:hover .pic{transform:none}}
'''

os.makedirs(OUT, exist_ok=True)
html = page().replace("<body>\n", '<body>\n<a class="skip" href="#cennik">Przejdź do cennika</a>\n', 1)
open(os.path.join(OUT, "stroller-counter.html"), "w").write(html)

# ---------------- states board ----------------
COOKIE = '''<div class="cookie" role="dialog" aria-labelledby="ck-t" aria-describedby="ck-d"><div class="ck-in"><div><h2 id="ck-t" class="display">Ciasteczka</h2><p id="ck-d">Używamy niezbędnych ciasteczek, żeby strona działała. Za Twoją zgodą także analitycznych, żeby wiedzieć, co poprawić. <a class="ulink" href="/polityka-prywatnosci#cookies">Szczegóły</a></p></div><div class="ck-btns"><button class="btn btn-main" type="button">Akceptuję</button><button class="btn btn-main" type="button">Odrzucam</button></div></div></div>'''
COOKIE_CSS = '''
.cookie{position:fixed;inset:auto 0 0 0;z-index:40;background:#fff;border-top:1px solid var(--border);box-shadow:0 -12px 40px -20px rgba(14,60,50,.35);padding:16px max(16px,env(safe-area-inset-left)) calc(16px + env(safe-area-inset-bottom))}
.ck-in{max-width:var(--container);margin:0 auto;display:grid;gap:14px}.cookie h2{font-size:1.25rem}.cookie p{color:var(--text-muted);font-size:.95rem;margin-top:4px}
.ck-btns{display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(min-width:900px){.ck-in{grid-template-columns:1fr auto;align-items:center;gap:32px}.ck-btns{grid-template-columns:auto auto}}
'''
# Both cookie buttons: same variant, same size (equal weight, per dev constraint). Stacked above the sticky phone bar on mobile.
open(os.path.join(OUT, "cookie.css"), "w").write(COOKIE_CSS)
# v1.2: while the banner is open the page reserves the banner's height at the bottom, so the footer's last line
# ("Prywatność", "Ustawienia cookies") can always be scrolled into view above it. The script is prototype-only.
COOKIE_SPACE = """<script>(function(){var b=document.querySelector('.cookie'),r=document.documentElement;function f(){r.style.setProperty('--cookie-h',b.offsetHeight+'px')}f();if(window.ResizeObserver)new ResizeObserver(f).observe(b);addEventListener('resize',f)})()</script>"""
cookie_page = page(extra_head='<link rel="stylesheet" href="cookie.css">', body_extra=COOKIE + COOKIE_SPACE)
open(os.path.join(OUT, "state-cookie.html"), "w").write(cookie_page.replace("</style>", ".sticky{display:none!important}body{padding-bottom:var(--cookie-h,240px)!important}html{scroll-padding-bottom:calc(var(--cookie-h,240px) + 12px)!important}</style>", 1))

# footer states (v1.2): every company field present and long; and no company details at all (the block is left out)
SKIP = '<body>\n<a class="skip" href="#cennik">Przejdź do cennika</a>\n'
open(os.path.join(OUT, "state-footer-long.html"), "w").write(page(company=COMPANY_LONG).replace("<body>\n", SKIP, 1))
open(os.path.join(OUT, "state-footer-no-company.html"), "w").write(page(company=None).replace("<body>\n", SKIP, 1))

# before/after + reviews live (wireframe: labelled placeholders, never real-looking content)
live = page().replace('id="przed-po" hidden', 'id="przed-po"').replace('id="opinie" hidden', 'id="opinie"').replace('data-bind="nextFreeSlot" hidden', 'data-bind="nextFreeSlot"')
assert 'data-bind="nextFreeSlot">' in live
live = live.replace('<div class="ba-grid"><figure class="ba"><div class="ph ratio43" role="img" aria-label="Przed">przed</div><div class="ph ratio43" role="img" aria-label="Po">po</div></figure></div>',
  '<div class="ba-grid3">' + "".join('<figure class="ba"><div class="ph ratio43" role="img" aria-label="Zdjęcie przed">przed<br>(zdjęcie własne)</div><div class="ph ratio43" role="img" aria-label="Zdjęcie po">po<br>(zdjęcie własne)</div><figcaption>Gondola, plama po oliwce</figcaption></figure>' for _ in range(3)) + '</div>')
live = live.replace('<div class="wrap"><div class="sec-head"><span class="eyebrow">Opinie</span><h2>Co mówią rodzice</h2></div></div>',
  '<div class="wrap"><div class="sec-head"><span class="eyebrow">Opinie</span><h2>Co mówią rodzice</h2></div><div class="rv-grid">' + "".join('<blockquote class="rv"><p class="rv-t">[tekst opinii wpisany przez właścicielkę]</p><footer>[imię i miejscowość, za zgodą]</footer></blockquote>' for _ in range(3)) + '</div></div>')
live = live.replace("</style>", ".ba-grid3{display:grid;gap:20px}@media(min-width:900px){.ba-grid3{grid-template-columns:repeat(3,1fr)}}.ba figcaption{grid-column:1/-1;color:var(--text-muted);font-size:.9rem}.rv-grid{display:grid;gap:16px}@media(min-width:900px){.rv-grid{grid-template-columns:repeat(3,1fr)}}.rv{margin:0;background:#fff;border:1px solid var(--border);border-radius:var(--r-2xl);padding:22px;display:grid;gap:12px}.rv-t{font-size:1.05rem;color:var(--text-muted)}.rv footer{font-weight:700;color:var(--text)}</style>")
open(os.path.join(OUT, "state-live-slots.html"), "w").write(live)

# FAQ all open + long text price row
longp = page().replace("<details>", "<details open>").replace("<details open", "<details open")
longp = longp.replace("Wózek bliźniaczy</span>", "Wózek bliźniaczy lub tandem z dwoma gondolami i dużym koszem na zakupy</span>")
open(os.path.join(OUT, "state-faq-open-long.html"), "w").write(longp)

# No photos yet (the likely early-launch state): no placeholder ever ships. Problem cards become text cards in a 2 x 2 grid,
# the car-seat section becomes one text column. Same copy, same order, same links.
import re
nop = page()
nop, n1 = re.subn(r'<div class="ph pic" role="img"[^>]*>.*?</div>', '', nop)
nop, n2 = re.subn(r'<div class="ph" style="aspect-ratio:4/3" role="img"[^>]*>.*?</div>', '', nop)
assert (n1, n2) == (4, 1), (n1, n2)
nop = nop.replace('<div class="bento">', '<div class="bento nophoto">').replace('<div class="wrap seat">', '<div class="wrap seat nophoto">')
nop = nop.replace("</style>", """.bento.nophoto .pc-body{padding:24px}
@media(min-width:700px){.bento.nophoto{grid-template-columns:1fr 1fr;grid-template-rows:none;gap:20px}.bento.nophoto .pc.big{grid-row:auto;grid-template-rows:none}.bento.nophoto .pc.big h3{font-size:1.3rem}.bento.nophoto .pc.wide{grid-column:auto;grid-template-columns:1fr}.bento.nophoto .pc.wide .pc-body{align-content:start}}
.seat.nophoto{grid-template-columns:1fr}.seat.nophoto>div{max-width:760px}
</style>""", 1)
open(os.path.join(OUT, "state-no-photos.html"), "w").write(nop.replace("<body>\n", '<body>\n<a class="skip" href="#cennik">Przejdź do cennika</a>\n', 1))
print("final built")
