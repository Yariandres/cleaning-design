"""Builds homepage v0 (`/`) and its states. Run: python3 prototypes/homepage-v0/build.py

Early launch (owner priority cleaning-design#5, item 2). SEO mini brief: cleaning-seo seo/briefs/homepage-v0.md (cleaning-design#7).
Reuses the stroller page's header, WhatsApp button, final CTA, footer, sticky bar and cookie banner by importing them
from prototypes/stroller/build_final.py, so there is exactly one copy of each component (importing it also rebuilds
the stroller pages, which must come out identical: check `git status`)."""
import os, sys, re, math
HERE = os.path.dirname(os.path.abspath(__file__))
STROLLER = os.path.join(HERE, "..", "stroller")
sys.path.insert(0, STROLLER)
cwd = os.getcwd(); os.chdir(STROLLER)
import build_final as F          # HEADER, STICKY, FINAL, footer(), wa_btn(), COOKIE, COOKIE_CSS, COOKIE_SPACE, FINAL_CSS
import build_og as O             # share-image template
os.chdir(cwd)
ico = F.ico

# ---------------- head (proposals from the SEO brief §2, §8; wording is the brand strategist's call, issue #6) ----------------
TITLE = "Nowiutko — pranie tapicerki, wózków i aut u Ciebie | Poznań"
DESC = "Nowiutko: pierzemy wózki, foteliki, kanapy, materace, dywany i wnętrza aut u Ciebie w domu, w Poznaniu i okolicach. Cena ze zdjęć na WhatsApp."
OG_TITLE = "Nowiutko — pranie tapicerki, wózków i aut u Ciebie"
OG_ALT = "Nowiutko: pranie tapicerki, wózków i aut u Ciebie. Poznań i okolice."
assert len(TITLE) <= 60 and len(DESC) <= 155, (len(TITLE), len(DESC))
STROLLER_URL = "/poznan/pranie-wozkow-i-fotelikow"

HEAD_META = f'''<link rel="canonical" href="https://nowiutko.pl/">
<meta property="og:type" content="website"><meta property="og:site_name" content="Nowiutko"><meta property="og:locale" content="pl_PL">
<meta property="og:title" content="{OG_TITLE}"><meta property="og:description" content="{DESC}"><meta property="og:url" content="https://nowiutko.pl/">
<meta property="og:image" content="https://nowiutko.pl/og-nowiutko-1200x630.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{OG_ALT}">
<meta name="twitter:card" content="summary_large_image">'''

LOGO = "../stroller/assets/logo.svg"
def fix(s):
    return s.replace("../assets/logo.svg", LOGO)


# ---------------- story icons ----------------
# Custom icons on the 24px grid, currentColor, round caps/joins (DESIGN.md -> Icons). Lucide paths for frown / image (ISC licence).
STROLLER_PATHS = '<path d="M5 11a7 7 0 0 1 7-7v7"/><path d="M3 11h15a4 4 0 0 1-4 5H8a5 5 0 0 1-5-5z"/><path d="M18 11l1.5-6H22"/><circle cx="7.5" cy="19.5" r="1.8"/><circle cx="15.5" cy="19.5" r="1.8"/>'
def chamomile_paths(r1=4.6, r2=9, n=8):
    # line version: n petals as round-capped strokes around a ring, a small centre
    out = ""
    for i in range(n):
        a = math.radians(i * 360 / n)
        out += f'<path d="M{12+r1*math.sin(a):.2f} {12-r1*math.cos(a):.2f}L{12+r2*math.sin(a):.2f} {12-r2*math.cos(a):.2f}"/>'
    return out + '<circle cx="12" cy="12" r="2"/>'
def svg(inner, cls="", sw=2, size=None, extra=""):
    sz = f' width="{size}" height="{size}"' if size else ""
    return f'<svg class="ico {cls}" viewBox="0 0 24 24"{sz} fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" {extra}>{inner}</svg>'
FROWN = '<circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><path d="M9 9h.01"/><path d="M15 9h.01"/>'
IMAGE = '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>'
STAINS = '<g class="stain" stroke="none"><circle cx="9.5" cy="7.6" r="1.3"/><circle cx="12.4" cy="13.4" r="1.7"/><circle cx="7.2" cy="13.8" r="1"/><circle cx="15.2" cy="14.4" r="0.9"/><path d="M10.8 16.2c.5 1 .5 1.6 0 2.2-.5-.6-.5-1.2 0-2.2z"/></g>'
SPARK = '<g class="spark" stroke-width=".9"><path d="M20 2.2v3.2M18.4 3.8h3.2"/><path d="M3.5 3.2v3M2 4.7h3"/></g>'
FLOWER = '<g class="mini">' + "".join(f'<circle cx="{11+2.0*math.sin(math.radians(i*45)):.2f}" cy="{13.3-2.0*math.cos(math.radians(i*45)):.2f}" r="1"/>' for i in range(8)) + '<circle cx="11" cy="13.3" r="1" class="mid"/></g>'

def badge(inner_svg, cls=""):
    return f'<span class="sb {cls}">{inner_svg}</span>'

STORY = f'''<div class="story" role="img" aria-label="Trzy kroki: zaplamiony wózek, zdjęcia wysłane w rozmowie na WhatsApp, wózek jak nowy.">
<div class="sc sc1">{badge(svg(FROWN, size=22), "sb1")}
<div class="sc-art">{svg(STROLLER_PATHS + STAINS, "art-stroller", sw=1.5)}</div><p class="sc-cap"><b>1</b>Plama na wózku</p></div>
<div class="chat-card">{badge(svg('<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>', size=22), "sb2")}
<p class="ch-label">Przykład: tak wygląda rozmowa<b>2</b></p>
<div class="chat"><div class="ch-head"><img src="../stroller/assets/mark.svg" alt="" width="28" height="28"><span><b>Nowiutko</b><i>WhatsApp</i></span></div>
<div class="ch-body">
<div class="bub out"><div class="thumbs"><span class="th">{svg(IMAGE, size=24)}</span><span class="th">{svg(IMAGE, size=24)}</span></div><p>Dzień dobry, proszę o wycenę wózka.</p></div>
<div class="bub in"><p>Dziękujemy! Cenę podamy dziś.</p><small>{F.HOURS}</small></div>
</div></div></div>
<div class="sc sc3">{badge(svg(chamomile_paths(), size=24, sw=2), "sb3")}
<div class="sc-art">{svg(STROLLER_PATHS + FLOWER + SPARK, "art-stroller fresh", sw=1.5)}</div><p class="sc-cap"><b>3</b>Wózek jak nowe</p></div>
</div>'''

# ---------------- hero ----------------
# H1 is the headline itself (real text, the name first). The voice line sits under it as a normal paragraph.
HERO = f'''<section class="hh"><div class="wrap">
<div class="hh-copy">
<h1 class="hh-h1"><span class="name">Nowiutko</span> — pranie tapicerki, wózków i aut u Ciebie w Poznaniu i okolicach</h1>
<p class="voice">Świeżo i jak nowe — bez wychodzenia z domu.</p>
<p class="lede">Przyjeżdżamy z własnym sprzętem i pierzemy u Ciebie, na miejscu: wózki, foteliki, kanapy, materace, dywany i wnętrza aut.</p>
<div class="hh-btns">{F.wa_btn("hero")}<a class="btn btn-ghost num" href="{F.TEL}" data-bind="business:phone" data-cta="phone" data-cta-pos="hero">{ico("phone")}Zadzwoń: {F.PHONE}</a></div>
<p class="pc-promise hh-promise">2–3 zdjęcia wystarczą. Cenę podamy dziś.</p>
<p class="pc-promise hh-promise hh-hours" data-bind="business:hours">{F.HOURS}</p>
</div>
{STORY}
</div></section>'''

# ---------------- Co pierzemy ----------------
# One bookable card: only the title is the <a> (service name in its text); a stretched ::after makes the whole card clickable.
# The other services are plain rows: no <a>, no heading, no paragraph, no price; "wkrótce" is real text.
# Service rows. Stroller + car seats: one card linking to its page. Every other service is bookable by hand (owner decision, 2026-11-17, #7):
# its row is ONE link to the WhatsApp action (prefilled message that names the service), text "<service> — Wycena na WhatsApp".
# Never a link to a page that does not exist; no heading, paragraph or price per service.
from urllib.parse import quote
SOON = [("Kanapy, narożniki i fotele", "kanap, narożników lub foteli"), ("Materace", "materaca"), ("Dywany", "dywanu"), ("Tapicerka samochodowa (wnętrze auta)", "tapicerki samochodowej (wnętrza auta)")]
WA_LABEL = "Wycena na WhatsApp"
def wa_for(prefill_obj):
    return "https://wa.me/48736369704?text=" + quote(f"Dzień dobry, proszę o wycenę prania {prefill_obj}. Wysyłam zdjęcia. Miejscowość: ")
def soon_rows(live=None):
    out = ""
    for n, obj in SOON:
        if live and n == live[0]:
            out += f'<li><a class="sv-link sv-page" href="{live[1]}"><span class="sv-name">{live[2]}</span>{ico("arrow-right")}</a></li>'
        else:
            out += (f'<li><a class="sv-link" href="{wa_for(obj)}" rel="noopener" data-cta="whatsapp" data-cta-pos="services" data-bind="business:whatsapp">'
                    f'<span class="sv-name">{n}</span><span class="vh"> — </span><span class="sv-wa">{ico("message-circle")}{WA_LABEL}</span></a></li>')
    return out
def services(live=None):
    return f'''<section id="uslugi"><div class="wrap"><div class="sec-head"><span class="eyebrow">Usługi</span><h2>Co pierzemy</h2><p class="lede">Wybierz, co chcesz odświeżyć. Cenę podajemy ze zdjęć, zanim przyjedziemy.</p></div>
<div class="svc">
<div class="svc-card"><span class="svc-chip">Wózki i foteliki</span>
<h3><a href="{STROLLER_URL}">Pranie wózków i fotelików</a></h3>
<p>Wózki spacerowe, gondole, 2w1 i 3w1 oraz foteliki samochodowe. Cennik i pakiety na osobnej stronie.</p>
<span class="svc-more" aria-hidden="true">Cennik i szczegóły {ico("arrow-right")}</span></div>
<div class="soon"><p class="eyebrow">Pozostałe usługi</p><ul>{soon_rows(live)}</ul></div>
</div></div></section>'''

# ---------------- Jak to działa (short form of the stroller steps; same copy, v1.1) ----------------
STEPS = '''<section class="steps-s"><div class="wrap"><div class="sec-head"><span class="eyebrow">Trzy kroki, zero wychodzenia z domu</span><h2>Jak to działa</h2></div><ol class="steps">
<li><h3>Wyślij zdjęcia</h3><p>2–3 zdjęcia przez WhatsApp lub SMS. Napisz, gdzie mieszkasz.</p></li>
<li><h3>Dostań cenę i termin</h3><p>Zwykle w kilka minut.</p></li>
<li><h3>Pierzemy u Ciebie</h3><p>Przywozimy sprzęt i środki. Potrzebujemy tylko wody i gniazdka.</p></li></ol></div></section>'''

# ---------------- Gdzie dojeżdżamy: a sentence. The towns are {zones} data in the nominative (no declension needed) ----------------
AREA = '''<section class="band" id="obszar"><div class="wrap area-h"><div class="sec-head"><span class="eyebrow">Obszar działania</span><h2>Gdzie dojeżdżamy</h2></div>
<div class="ah-body"><p class="display ah-line">Poznań i powiat poznański.</p>
<p class="lede">Jeździmy po całym powiecie, na przykład: <span data-bind="zones:featured">Swarzędz, Luboń, Suchy Las, Komorniki, Plewiska</span>. Napisz, gdzie mieszkasz, a potwierdzimy dojazd.</p></div></div></section>'''

CSS = '''
/* homepage v0 */
.hh{background:var(--p50);border-bottom:1px solid var(--border);padding-block:0}
.hh .wrap{display:grid;gap:28px;padding-block:28px 40px}
.hh-h1{font-size:clamp(1.95rem,6.4vw,3.3rem);line-height:1.08}@media(min-width:900px){.hh-h1{font-size:clamp(2.3rem,3.5vw,3.1rem)}}.hh-h1 .name{color:var(--p500)}
.voice{font:700 1.15rem/1.35 var(--body);color:var(--p700);margin-top:16px}
.hh .lede{margin-top:10px;color:var(--n700);font-size:1.1rem}
.hh-btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.hh-btns .btn{flex:1 1 250px}
.hh-promise{text-align:left;margin-top:12px}.hh-hours{margin-top:2px}
.story{display:none}
/* story board: three beats in icons (problem, message, result). Zigzag like the reference: cards 1 and 3 in the left column, the chat window offset down in the right column. Badges sit on the seam. Static; no motion. */
.story{display:grid;grid-template-columns:.8fr 1.2fr;grid-template-rows:1fr 1fr;gap:16px;aspect-ratio:358/392;position:relative;--w400:#B77D44;--w500:#A15C00}
.sc{position:relative;border-radius:var(--r-2xl);display:grid;grid-template-rows:1fr auto;padding:12px 12px 12px;overflow:visible;min-height:0}
.sc1{background:var(--n100);color:var(--n500);border:1px solid var(--border)}
.sc3{background:var(--p100);color:var(--p700);border:1px solid var(--p200)}
.sc-art{display:grid;place-items:center;min-height:0}.sc-art .ico{width:min(100%,104px);height:auto;display:block;overflow:visible}
.stain{fill:var(--w400)}.fresh .mini circle{fill:#fff;stroke:var(--p700);stroke-width:.35}.fresh .mini .mid{fill:var(--s300);stroke:var(--p700);stroke-width:.35}.fresh .spark{stroke:var(--s500)}
.sc-cap{font:700 .86rem/1.2 var(--body);color:var(--n900);display:flex;gap:8px;align-items:center}
.sc-cap b,.ch-label b{flex:none;display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--n900);color:#fff;font-size:.75rem}
.sb{position:absolute;z-index:2;width:36px;height:36px;border-radius:50%;background:var(--n900);color:#fff;display:grid;place-items:center;box-shadow:0 0 0 3px var(--p50)}
.sb .ico{width:18px;height:18px}.sb3{background:var(--p500)}
.sb1{right:-26px;top:14px}.sb3{right:-26px;bottom:14px}.sb2{left:-26px;top:52%}
.chat-card{grid-column:2;grid-row:1/3;margin-top:28px;align-self:start;position:relative;display:grid;grid-template-rows:auto 1fr;gap:8px;min-height:0}
.ch-label{font:700 .8rem/1.25 var(--body);color:var(--n900);display:flex;gap:8px;align-items:center;margin:0;padding-left:24px}
.chat{background:#fff;border:1px solid var(--border);border-radius:var(--r-2xl);overflow:hidden;display:grid;grid-template-rows:auto 1fr;box-shadow:0 24px 50px -34px rgba(14,60,50,.5);min-height:0}
.ch-head{display:flex;gap:8px;align-items:center;padding:8px 10px;border-bottom:1px solid var(--border);background:var(--n50)}
.ch-head img{width:26px;height:26px;border-radius:8px}.ch-head span{display:grid;line-height:1.15}.ch-head b{font:700 .85rem var(--body);color:var(--n900)}.ch-head i{font-style:normal;font-size:.72rem;color:var(--text-muted)}
.ch-body{background:var(--p50);padding:10px;display:grid;gap:8px;align-content:start;overflow:hidden}
.bub{border-radius:14px;padding:8px 10px;max-width:92%;display:grid;gap:6px;font-size:.82rem;line-height:1.3;color:var(--n900)}
.bub.out{background:var(--p100);justify-self:end;border-bottom-right-radius:4px}.bub.in{background:#fff;justify-self:start;border-bottom-left-radius:4px;border:1px solid var(--border)}
.bub small{font-size:.74rem;line-height:1.3;color:var(--n700)}
.thumbs{display:grid;grid-template-columns:1fr 1fr;gap:4px}.th{aspect-ratio:1;border-radius:8px;background:var(--n200);color:var(--n500);display:grid;place-items:center}.th .ico{width:55%;height:55%}
@media(max-width:359px){.story{aspect-ratio:288/430}.sc-art .ico{width:72px}.sc-cap{font-size:.78rem}.sc{padding:10px}.sb3{bottom:56px}}
@media(max-width:899px){.hh .wrap{gap:36px}.story{display:grid;margin-inline:auto;width:min(100%,520px)}}
@media(min-width:900px){.hh .wrap{grid-template-columns:1fr 500px;gap:64px;align-items:center;padding-block:56px 64px}.story{display:grid;grid-template-columns:.8fr 1.2fr;aspect-ratio:500/470;gap:20px}.sc{padding:16px}.sc-art .ico{width:min(100%,128px)}.sc-cap{font-size:.95rem}.sb{width:44px;height:44px}.sb .ico{width:22px;height:22px}.sb1,.sb3{right:-32px}.sb2{left:-32px}.chat-card{margin-top:44px}.bub{font-size:.95rem}.bub small{font-size:.82rem}.ch-head b{font-size:.95rem}.ch-label{font-size:.88rem;padding-left:30px}.ch-body{padding:14px;gap:12px}.th .ico{width:50%}}
@media(min-width:1100px){.hh .wrap{grid-template-columns:1fr 540px}.story{aspect-ratio:540/500}}
/* services */
.svc{display:grid;gap:20px}
@media(min-width:900px){.svc{grid-template-columns:1.2fr 1fr;gap:28px;align-items:stretch}}
.svc-card{position:relative;background:#fff;border:1px solid var(--border);border-radius:var(--r-2xl);padding:26px 24px 24px;display:grid;gap:12px;align-content:start;transition:transform .2s ease,box-shadow .2s ease}
@media(min-width:900px){.svc-card{padding:32px}}
.svc-card:hover{transform:translateY(-2px);box-shadow:0 18px 40px -26px rgba(14,60,50,.45)}
.svc-chip{justify-self:start;background:var(--s100);color:var(--s800);font-size:12.5px;font-weight:700;padding:4px 12px;border-radius:999px}
.svc-card h3{font-size:clamp(1.5rem,3vw,1.9rem)}
.svc-card h3 a{text-decoration:none;color:inherit}
.svc-card h3 a::after{content:"";position:absolute;inset:0;border-radius:inherit}
.svc-card h3 a:focus-visible{outline:none}.svc-card:has(a:focus-visible){outline:3px solid var(--n900);outline-offset:3px}
.svc-card p{color:var(--text-muted);max-width:46ch}
.svc-more{display:inline-flex;gap:8px;align-items:center;font-weight:700;color:var(--p600);min-height:44px;margin-top:4px;text-decoration:underline;text-decoration-color:transparent;text-decoration-thickness:2px;text-underline-offset:4px;transition:text-decoration-color .2s}
.svc-card:hover .svc-more{text-decoration-color:currentColor}
.soon{background:var(--bg-muted);border-radius:var(--r-2xl);padding:22px 24px 12px;display:grid;gap:4px;align-content:start}
.soon ul{list-style:none;padding:0}
.soon li{border-top:1px solid var(--n200);min-height:56px;display:flex}.soon li:first-child{border-top:0}
.sv-link{flex:1;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:2px 16px;padding-block:10px;min-height:56px;color:var(--n700);font-weight:600;text-decoration:none}
.sv-wa{display:inline-flex;align-items:center;gap:6px;color:var(--p600);font-weight:700;text-decoration:underline;text-decoration-color:transparent;text-decoration-thickness:2px;text-underline-offset:4px;transition:text-decoration-color .2s}
.sv-link:hover .sv-wa,.sv-link:hover .ico{text-decoration-color:currentColor}.sv-link .ico{color:var(--p600)}
.sv-page{color:var(--p600);font-weight:700}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* steps */
.steps-s .steps{gap:20px}
/* area */
.area-h{display:grid;gap:20px}.area-h .sec-head{margin:0}
@media(min-width:900px){.area-h{grid-template-columns:1fr 1.5fr;gap:64px;align-items:start}}
.ah-body{display:grid;gap:14px}.ah-line{font-size:clamp(1.7rem,3.4vw,2.4rem)}
.ah-body .lede{color:var(--n700)}
'''

def page(body_extra="", extra_head="", live=None, company=F.COMPANY_DEFAULT, extra_css=""):
    main = HERO + services(live) + STEPS + AREA + F.FINAL
    html = f'''<!doctype html><html lang="pl-PL"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITLE}</title><meta name="description" content="{DESC}">{HEAD_META}
<link rel="stylesheet" href="../stroller/base.css"><style>{F.FINAL_CSS}{CSS}{extra_css}</style>{extra_head}</head><body>
<a class="skip" href="#uslugi">Przejdź do usług</a>
{F.HEADER}<main>{main}</main>{F.footer(company)}{F.STICKY}{body_extra}</body></html>'''
    return fix(html)

def write(name, html):
    open(os.path.join(HERE, name), "w").write(html)

write("index.html", page())

# state: cookie banner open (same component and reserved space as the stroller page)
cookie = page(extra_head="", body_extra=F.COOKIE + F.COOKIE_SPACE, extra_css=F.COOKIE_CSS + ".sticky{display:none!important}body{padding-bottom:var(--cookie-h,240px)!important}html{scroll-padding-bottom:calc(var(--cookie-h,240px) + 12px)!important}")
write("state-cookie.html", cookie)

# state: a second counter has shipped. Its WhatsApp row becomes a link to the new page (illustration only: the sofa page does not exist yet,
# and its anchor text is the sofa brief's to decide).
write("state-service-live.html", page(live=("Kanapy, narożniki i fotele", "/poznan/pranie-kanap", "Pranie kanap, narożników i foteli")))

# ---------------- share image (no-photo variant, same template as the stroller page) ----------------
OGDIR = HERE
og_title = "Pranie tapicerki, wózków i&nbsp;aut u&nbsp;Ciebie"
og_line = ("Poznań i okolice", "bez wychodzenia z domu")
STACK = "<style>.og .meta{flex-direction:column;align-items:flex-start;gap:4px;white-space:normal;line-height:1.2}.og .meta span{display:block;line-height:1.2}.og .meta i{display:none}</style>"
def og(name, title, line, long=False, stack=False):
    h = O.page("nophoto", title, line=line, long=long)
    h = h.replace("../assets/logo.svg", LOGO).replace("../base.css", "../stroller/base.css")
    if stack: h = h.replace("</head>", STACK + "</head>")
    write(name, h)
# FINAL: 64px title (3 lines) and the line stacked on two lines: the one-line version is 637px wide and leaves the centre-square crop (x 285-915)
og("og-homepage.html", og_title, og_line, long=True, stack=True)
# comparison only: the 80px size gives 4 lines and the single-line version of the line
og("og-homepage-80-test.html", og_title, og_line)
print("homepage-v0 built")
