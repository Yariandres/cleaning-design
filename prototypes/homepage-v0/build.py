"""Builds homepage v0 (`/`) and its states. Run: python3 prototypes/homepage-v0/build.py

Early launch (owner priority cleaning-design#5, item 2). SEO mini brief: cleaning-seo seo/briefs/homepage-v0.md (cleaning-design#7).
Reuses the stroller page's header, WhatsApp button, final CTA, footer, sticky bar and cookie banner by importing them
from prototypes/stroller/build_final.py, so there is exactly one copy of each component (importing it also rebuilds
the stroller pages, which must come out identical: check `git status`)."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
STROLLER = os.path.join(HERE, "..", "stroller")
sys.path.insert(0, STROLLER)
cwd = os.getcwd(); os.chdir(STROLLER)
import build_final as F          # HEADER, STICKY, FINAL, footer(), wa_btn(), COOKIE, COOKIE_CSS, COOKIE_SPACE, FINAL_CSS
import build_og as O             # share-image template
os.chdir(cwd)
ico = F.ico

# ---------------- head (proposals from the SEO brief §2, §8; wording is the brand strategist's call, issue #6) ----------------
TITLE = "Nowiutko – pranie tapicerki, wózków i aut u Ciebie | Poznań"
DESC = "Nowiutko: pierzemy wózki dziecięce i foteliki samochodowe u Ciebie w domu, w Poznaniu i okolicach. Wkrótce także kanapy, materace, dywany i wnętrza aut."
OG_TITLE = "Nowiutko – pranie tapicerki, wózków i aut u Ciebie"
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

# ---------------- hero ----------------
# H1 is the headline itself (real text, the name first). The voice line sits under it as a normal paragraph.
HERO = f'''<section class="hh"><div class="wrap">
<div class="hh-copy">
<h1 class="hh-h1"><span class="name">Nowiutko</span> – pranie tapicerki, wózków i aut u Ciebie w Poznaniu i okolicach</h1>
<p class="voice">Świeżo i jak nowe — bez wychodzenia z domu.</p>
<p class="lede">Przyjeżdżamy z własnym sprzętem i pierzemy u Ciebie, na miejscu. Na początek: wózki i foteliki samochodowe.</p>
<div class="hh-btns">{F.wa_btn("hero")}<a class="btn btn-ghost num" href="{F.TEL}" data-bind="business:phone" data-cta="phone" data-cta-pos="hero">{ico("phone")}Zadzwoń: {F.PHONE}</a></div>
<p class="pc-promise hh-promise">2–3 zdjęcia wystarczą. Cenę podamy dziś.</p>
</div>
<div class="hh-mark" aria-hidden="true"><img src="../stroller/assets/mark.svg" alt="" width="320" height="320"></div>
</div></section>'''

# ---------------- Co pierzemy ----------------
# One bookable card: only the title is the <a> (service name in its text); a stretched ::after makes the whole card clickable.
# The other services are plain rows: no <a>, no heading, no paragraph, no price; "wkrótce" is real text.
SOON = ["Kanapy, narożniki i fotele", "Materace", "Dywany", "Tapicerka samochodowa (wnętrze auta)"]
def soon_rows(live=None):
    out = ""
    for n in SOON:
        if live and n == live[0]:
            out += f'<li class="live"><a href="{live[1]}">{live[2]}{ico("arrow-right")}</a></li>'
        else:
            out += f'<li><span class="sv-name">{n}</span><span class="sv-tag">wkrótce</span></li>'
    return out
def services(live=None):
    return f'''<section id="uslugi"><div class="wrap"><div class="sec-head"><span class="eyebrow">Usługi</span><h2>Co pierzemy</h2><p class="lede">Dziś umawiamy pranie wózków i fotelików. Kolejne usługi dodajemy po kolei.</p></div>
<div class="svc">
<div class="svc-card"><span class="svc-chip">Dostępne teraz</span>
<h3><a href="{STROLLER_URL}">Pranie wózków i fotelików</a></h3>
<p>Wózki spacerowe, gondole, 2w1 i 3w1 oraz foteliki samochodowe. Cenę podajemy ze zdjęć, zanim przyjedziemy.</p>
<span class="svc-more" aria-hidden="true">Cennik i szczegóły {ico("arrow-right")}</span></div>
<div class="soon"><p class="eyebrow">Kolejne usługi</p><ul>{soon_rows(live)}</ul></div>
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
.hh .wrap{display:grid;gap:24px;padding-block:28px 40px}
.hh-h1{font-size:clamp(1.95rem,6.4vw,3.3rem);line-height:1.08}.hh-h1 .name{color:var(--p500)}
.voice{font:700 1.15rem/1.35 var(--body);color:var(--p700);margin-top:16px}
.hh .lede{margin-top:10px;color:var(--n700);font-size:1.1rem}
.hh-btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.hh-btns .btn{flex:1 1 250px}
.hh-promise{text-align:left;margin-top:12px}
.hh-mark{display:none}
@media(min-width:700px){.hh-btns .btn{flex:0 0 auto}}
@media(min-width:900px){.hh .wrap{grid-template-columns:1fr 300px;gap:72px;align-items:center;padding-block:64px 80px}.hh-mark{display:block}.hh-mark img{width:100%;height:auto;display:block;border-radius:26%;box-shadow:0 30px 70px -36px rgba(14,60,50,.55)}}
@media(min-width:1100px){.hh .wrap{grid-template-columns:1fr 340px}}
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
.soon li{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-block:14px;border-top:1px solid var(--n200);font-weight:600;color:var(--n700);min-height:56px}
.soon li:first-child{border-top:0}
.sv-tag{flex:none;background:#fff;border:1px solid var(--n300);border-radius:999px;padding:2px 12px;font-size:.85rem;font-weight:600;color:var(--n700)}
.soon li.live{padding:0}.soon li.live a{flex:1;display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:56px;color:var(--p600);font-weight:700;text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:2px;text-decoration-color:transparent;transition:text-decoration-color .2s}.soon li.live a:hover{text-decoration-color:currentColor}
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

# state: a second counter has shipped. Its row loses "wkrótce" and becomes a link (illustration only: the sofa page does not exist yet,
# and its anchor text is the sofa brief's to decide).
write("state-service-live.html", page(live=("Kanapy, narożniki i fotele", "/poznan/pranie-kanap", "Pranie kanap i foteli")))

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
