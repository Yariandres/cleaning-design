"""Builds the three stroller-counter directions (prototypes, not production). Run: python3 build.py"""
import re, os
L = "/home/claude/scratch-lucide/package/icons/"
def ico(name):
    s = open(L + name + ".svg").read()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", s, re.S).group(1).strip()
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{inner}</svg>'

PRICES = [("Wózek spacerowy", "siedzisko, budka, pasy, stelaż i koła", 90),
          ("Wózek 2w1", "gondola + spacerówka, stelaż i koła", 120),
          ("Wózek 3w1", "z fotelikiem-nosidełkiem", 160),
          ("Wózek bliźniaczy", "", 150),
          ("Fotelik samochodowy", "pokrowiec, skorupa, baza", 80),
          ("Krzesełko, leżaczek lub mata", "", 60)]

def price_list():
    rows = "".join(f'<li><span>{n}{"<small>"+d+"</small>" if d else ""}</span><b><i>od</i>{p}&nbsp;zł</b></li>' for n, d, p in PRICES)
    return f'<ul class="plist">{rows}</ul>'

HEADER = f'''<header class="site-h"><div class="wrap"><a href="#" aria-label="Nowiutko, strona główna"><img src="assets/logo.svg" alt="Nowiutko" width="190" height="46"></a>
<div style="display:flex;gap:20px;align-items:center"><a class="tel" href="tel:+48500000000">{ico("phone")}<span class="num">500 000 000</span></a><a class="btn btn-main" href="#wycena">Wyślij zdjęcia</a></div></div></header>'''
STICKY = f'<div class="sticky"><a class="btn btn-main" href="#wycena">{ico("camera")}Wyślij zdjęcia</a><a class="btn btn-ghost" href="tel:+48500000000" aria-label="Zadzwoń">{ico("phone")}</a></div>'

PROOF = f'''<div class="proof"><div class="wrap"><ul>
<li>{ico("clock")}Gotowe tego samego dnia</li><li>{ico("house")}Pierzemy u Ciebie w domu</li>
<li>{ico("shield-check")}Foteliki według instrukcji producenta</li><li>{ico("badge-check")}Wrócimy za darmo, jeśli coś wyjdzie po wyschnięciu</li></ul></div></div>'''

HEADACHE = f'''<section class="{{band}}"><div class="wrap"><div class="sec-head"><span class="eyebrow">Z czym przychodzą rodzice</span><h2>Dlaczego nie wyprać wózka samemu?</h2><p class="lede">Pralka i szczotka zostawiają zacieki na podszewce, a moczenie osłabia pasy. Dlatego robimy to inaczej.</p></div>
<div class="cards4"><div class="card"><h3>Gondola żółta od oliwki</h3><p>Tłuste plamy na podszewce, których pralka nie rusza.</p></div>
<div class="card"><h3>Fotelik po podróży</h3><p>Choroba lokomocyjna, okruchy w bazie, sok wsiąknięty w piankę.</p></div>
<div class="card"><h3>Spacerówka po lecie</h3><p>Krem z filtrem, lody i piasek w każdym szwie.</p></div>
<div class="card"><h3>Drugie dziecko w drodze</h3><p>Cały zestaw po starszym rodzeństwie gotowy na nowy początek.</p></div></div></div></section>'''

PRICE = f'''<section id="cennik" class="{{band}}"><div class="wrap"><div class="sec-head"><span class="eyebrow">Cennik</span><h2>Pranie wózka i fotelika – cena</h2><p class="lede">Ceny brutto, z dojazdem w Strefie 1. Dokładną kwotę podajemy ze zdjęć, zanim przyjedziemy.</p></div>
<div class="price-wrap"><div>{price_list()}<p class="pnote">Minimalne zamówienie 150 zł. Przy silnych zabrudzeniach (pleśń, wymioty) wycenimy ze zdjęć przed przyjazdem.</p></div>
<aside class="safety on-dark"><span class="eyebrow">Foteliki samochodowe</span><h3>Fotelik to sprzęt bezpieczeństwa. Tak go traktujemy.</h3><ul><li>Pokrowiec i skorupę czyścimy według instrukcji producenta.</li><li>Pasy czyścimy tylko powierzchniowo, bo moczenie osłabia ich wytrzymałość.</li><li>Środki hipoalergiczne, bezpieczne dla niemowląt po wyschnięciu.</li></ul></aside></div>
<div class="packs"><div class="pack"><span class="tag">przed porodem</span><h3>Nowy Członek Rodziny</h3><ul><li>Materac dwuosobowy</li><li>Wózek 2w1</li><li>Fotelik samochodowy</li></ul><div class="pr"><b class="num">319&nbsp;zł</b><s class="num">350&nbsp;zł</s></div></div>
<div class="pack hot"><span class="tag">najczęściej wybierany</span><h3>Rodzinny</h3><ul><li>Kanapa 3-osobowa</li><li>Wózek 2w1</li><li>Fotelik samochodowy</li></ul><div class="pr"><b class="num">339&nbsp;zł</b><s class="num">380&nbsp;zł</s></div></div>
<div class="pack"><span class="tag" style="background:var(--p100);color:var(--p800)">auto i maluch</span><h3>Auto i Maluch</h3><ul><li>Pranie tapicerki auta</li><li>Wózek 2w1</li><li>Fotelik samochodowy</li></ul><div class="pr"><b class="num">409&nbsp;zł</b><s class="num">460&nbsp;zł</s></div></div></div></div></section>'''

STEPS = '''<section><div class="wrap"><div class="sec-head"><span class="eyebrow">Jak to działa</span><h2>Trzy kroki, zero wychodzenia z domu</h2></div><ol class="steps">
<li><h3>Wyślij zdjęcia</h3><p>2–3 zdjęcia przez WhatsApp, SMS lub formularz. Napisz, gdzie mieszkasz.</p></li>
<li><h3>Dostań cenę i termin</h3><p>Zwykle w kilka minut. Wolne terminy często już na następny dzień.</p></li>
<li><h3>Pierzemy u Ciebie</h3><p>Przywozimy sprzęt i środki. Potrzebujemy tylko wody i gniazdka.</p></li></ol></div></section>'''

SEATS = f'''<section class="{{band}}"><div class="wrap seat"><div><div class="sec-head" style="margin-bottom:20px"><span class="eyebrow">Foteliki według marek</span><h2>Cybex, Maxi-Cosi, Britax Römer, Avionaut – według instrukcji producenta</h2></div>
<ul><li>Pokrowiec prany lub czyszczony tak, jak każe metka.</li><li>Skorupa i klamra przecierane łagodnym środkiem.</li><li>Pasy tylko powierzchniowo. Nigdy nie moczymy.</li></ul></div>
<div class="ph" style="aspect-ratio:4/3" role="img" aria-label="Miejsce na własne zdjęcie fotelika">miejsce na własne zdjęcie fotelika<br>(4:3, bez ludzi)</div></div></section>'''

FAQ_Q = [("Ile kosztuje pranie wózka dziecięcego?", "Wózek spacerowy od 90 zł, 2w1 od 120 zł, 3w1 od 160 zł, bliźniaczy od 150 zł. Dokładną cenę podajemy ze zdjęć, zanim przyjedziemy."),
 ("Ile kosztuje pranie fotelika samochodowego?", "Od 80 zł. W pakietach jest taniej."),
 ("Jak pierzecie foteliki Cybex czy Maxi-Cosi?", "Według instrukcji producenta: pokrowiec zgodnie z metką, skorupa i klamra łagodnym środkiem, pasy tylko powierzchniowo, bez moczenia."),
 ("Czy środki są bezpieczne dla niemowlęcia?", "Tak. Używamy środków hipoalergicznych i dokładnie je odsysamy. Po wyschnięciu tapicerka jest bezpieczna dla dziecka."),
 ("Kiedy wózek będzie gotowy?", "Zwykle tego samego dnia. Rano pierzemy, schnięcie trwa 3–5 godzin w ciepłym, przewietrzonym mieszkaniu."),
 ("Czy usuniecie pleśń z gondoli?", "Często tak, ale stare przebarwienia po pleśni mogą nie zejść w całości. Ocenimy to uczciwie ze zdjęć, zanim przyjedziemy."),
 ("Czy czyścicie też stelaż i koła?", "Tak, stelaż, koła i kosz są w cenie każdego wózka.")]
FAQ = '<section><div class="wrap"><div class="sec-head"><span class="eyebrow">Pytania</span><h2>Najczęstsze pytania</h2></div><div class="faq">' + "".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ_Q)) + '</div></div></section>'

AREA = '''<section class="{band}"><div class="wrap"><div class="sec-head"><span class="eyebrow">Obszar działania</span><h2>Gdzie dojeżdżamy</h2><p class="lede">Poznań i okolice, tam gdzie mieszkają rodziny. W Strefie 1 dojazd jest gratis.</p></div><div class="area">
<div class="zone"><h3>Strefa 1</h3><span class="fee">dojazd gratis</span><p>Poznań, Suchy Las, Swarzędz, Luboń, Komorniki, Plewiska, Skórzewo, Tarnowo Podgórne, Rokietnica, Czerwonak</p></div>
<div class="zone z2"><h3>Strefa 2</h3><span class="fee">25 zł, gratis od 400 zł</span><p>Kórnik, Mosina, Puszczykowo, Dopiewo, Murowana Goślina, Pobiedziska, Buk, Stęszew, Kleszczewo</p></div>
<div class="zone z3"><h3>Dalej</h3><span class="fee">1,50 zł/km</span><p>Poza powiatem poznańskim wycenimy dojazd indywidualnie.</p></div></div></div></section>'''

FINAL = f'''<section id="wycena" class="final on-dark"><div class="wrap"><h2>Wyślij 2–3 zdjęcia. Cenę podamy dziś.</h2><p>Przyjeżdżamy na czas. Płacisz tyle, ile podaliśmy ze zdjęć. Jeśli coś wyjdzie po wyschnięciu, wracamy za darmo.</p><a class="btn btn-main" href="#">{ico("camera")}Wyślij zdjęcia</a></div></section>
<footer><div class="wrap">Nowiutko · pranie tapicerki, wózków i aut u Ciebie · Poznań</div></footer>'''

def lower(alt):
    # alt: which sections sit on the mint band, so each direction keeps its rhythm
    a, b = alt
    return (PROOF + HEADACHE.replace("{band}", a) + PRICE.replace("{band}", b) + STEPS + SEATS.replace("{band}", a) + FAQ + AREA.replace("{band}", a) + FINAL)

# ---------- hero 1: Rozmowa ----------
H1_B = "Wózek i fotelik jak nowe – pranie u Ciebie w domu, w Poznaniu i okolicach"
def mini_prices():
    items = [("Wózek", 90), ("Wózek 2w1", 120), ("Fotelik", 80)]
    return '<ul class="mini">' + "".join(f'<li><span>{n}</span><b class="num">od&nbsp;{p}&nbsp;zł</b></li>' for n, p in items) + '</ul>'

HERO1 = f'''<section class="hero1"><div class="wrap">
<div class="h1-copy"><span class="eyebrow">Pranie wózków i fotelików · Poznań</span>
<h1>{H1_B.replace("jak nowe","<em>jak nowe</em>")}</h1>
<p class="lede">Gondole, spacerówki i foteliki pierzemy pod Twoim domem. Hipoalergiczne środki, foteliki według instrukcji producenta. Wózek gotowy tego samego dnia.</p>
{mini_prices()}
<div class="ctas"><a class="btn btn-main" href="#wycena">{ico("camera")}Wyślij 2–3 zdjęcia – cena dziś</a><a class="btn btn-ghost" href="#cennik">Zobacz cennik</a></div>
<p class="free">{ico("map-pin")}Dojazd gratis: Poznań, Suchy Las, Swarzędz, Luboń, Komorniki</p></div>
<div class="chat" role="img" aria-label="Przykładowa rozmowa o wycenie"><div class="chat-top"><img src="assets/mark.svg" alt="" width="40" height="40"><div><b>Nowiutko</b><small>zwykle odpowiada w kilka minut</small></div></div>
<div class="msgs"><div class="msg in">Dzień dobry, gondola zrobiła się żółta od oliwki, a fotelik jest po wakacjach. Ile za całość?<span class="time">09:12</span></div>
<div class="phs"><div class="ph">zdjęcie<br>gondoli</div><div class="ph">zdjęcie<br>fotelika</div></div>
<div class="msg out">Wózek 2w1 ze stelażem i kołami + fotelik: <b class="num">200 zł</b>. Dojazd do Suchego Lasu gratis.<span class="time">09:16</span></div>
<div class="msg out">Mogę jutro o 10:00. Wózek będzie gotowy na popołudniowy spacer.<span class="time">09:16</span></div></div>
<p class="chat-note">Przykładowa rozmowa, nie opinia klienta.</p></div></div></section>'''
CSS1 = '''
.hero1 .wrap{display:grid;gap:32px;padding-block:20px 48px}
.hero1 h1{font-size:clamp(2.1rem,6.4vw,3.3rem);margin-block:12px 16px}
.hero1 h1 em{font-style:normal;background:linear-gradient(transparent 64%,var(--s300) 64%);padding-inline:2px}
.mini{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 0}
.mini li{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:10px 14px;display:grid;line-height:1.2}
.mini span{font-size:.85rem;color:var(--text-muted)}.mini b{font-size:1.2rem}
.ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.ctas .btn{flex:1 1 260px}@media(min-width:900px){.ctas .btn{flex:0 0 auto}}
.free{margin-top:18px;display:flex;gap:8px;color:var(--text-muted);font-size:.95rem;align-items:flex-start}.free .ico{color:var(--p500);margin-top:2px}
.chat{background:#fff;border:1px solid var(--border);border-radius:var(--r-2xl);padding:18px;box-shadow:0 24px 60px -30px rgba(14,60,50,.4);max-width:430px;width:100%;justify-self:center}
.chat-top{display:flex;gap:12px;align-items:center;padding-bottom:12px;border-bottom:1px solid var(--border);margin-bottom:14px}.chat-top img{border-radius:12px}
.chat-top small{display:block;color:var(--text-muted);font-size:.8rem}
.msgs{display:grid;gap:10px}.msg{max-width:86%;padding:10px 14px;border-radius:16px;font-size:.95rem;line-height:1.4}
.in{background:#fff;border:1px solid var(--border);border-bottom-left-radius:4px}.out{background:var(--p100);justify-self:end;border-bottom-right-radius:4px}
.time{display:block;font-size:11px;color:var(--text-muted);margin-top:4px;text-align:right}
.phs{display:grid;grid-template-columns:1fr 1fr;gap:6px;width:68%;justify-self:end}.phs .ph{aspect-ratio:1;padding:6px;font-size:11px;border-radius:12px}
.chat-note{font-size:.8rem;color:var(--text-muted);margin-top:12px;text-align:center}
@media(min-width:900px){.hero1 .wrap{grid-template-columns:1.1fr .9fr;gap:64px;align-items:center;padding-block:40px 80px}.chat{justify-self:end}}
'''

# ---------- hero 2: Cennik pierwszy ----------
def card_rows():
    rows = [("Wózek spacerowy", 90), ("Wózek 2w1", 120), ("Fotelik samochodowy", 80), ("Wózek 3w1", 160)]
    return "".join(f'<li><span>{n}</span><b class="num"><i>od</i> {p}&nbsp;zł</b></li>' for n, p in rows)
HERO2 = f'''<section class="hero2"><div class="wrap">
<div class="h2-copy"><h1 class="eyebrow">Pranie wózków i fotelików dziecięcych w Poznaniu i okolicach</h1>
<p class="display">Wózek jak nowe. <span>Pod Twoim domem, tego samego dnia.</span></p>
<p class="lede">Przyjeżdżamy z własnym sprzętem. Ty nie wyjmujesz dziecka z domu, nie wozisz wózka i nie czekasz trzech dni.</p>
<ul class="ticks"><li>{ico("check")}Hipoalergiczne środki</li><li>{ico("check")}Foteliki według instrukcji producenta</li><li>{ico("check")}Dojazd gratis w Strefie 1</li></ul></div>
<div class="pcard"><div class="pc-head"><span class="eyebrow">Cennik brutto</span><span class="pc-sub">cena ze zdjęć, przed przyjazdem</span></div>
<ul class="pc-rows">{card_rows()}</ul>
<a class="btn btn-main" href="#wycena">{ico("camera")}Wyślij 2–3 zdjęcia – cena dziś</a>
<a class="pc-link" href="#cennik">Pełny cennik i pakiety</a></div></div></section>'''
CSS2 = '''
.hero2{background:var(--p50);border-bottom:1px solid var(--border)}
.hero2 .wrap{display:grid;gap:28px;padding-block:24px 40px}
.hero2 h1.eyebrow{font-size:12.5px;margin:0}
.hero2 .display{font-size:clamp(2.2rem,7vw,3.7rem);margin-block:12px 14px}.hero2 .display span{color:var(--p500)}
.ticks{list-style:none;padding:0;display:grid;gap:8px;margin:20px 0 0;font-weight:600}.ticks li{display:flex;gap:10px;align-items:center}.ticks .ico{color:var(--p500)}
.pcard{background:#fff;border:1px solid var(--border);border-radius:var(--r-2xl);padding:22px;display:grid;gap:16px;box-shadow:0 24px 60px -34px rgba(14,60,50,.45)}
.pc-head{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}.pc-sub{color:var(--text-muted);font-size:.85rem}
.pc-rows{list-style:none;padding:0;border-top:2px solid var(--n900)}
.pc-rows li{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding-block:14px;border-bottom:1px solid var(--border);font-weight:600}
.pc-rows b{font:800 1.7rem/1 var(--display);white-space:nowrap}.pc-rows b i{font:500 .9rem var(--body);font-style:normal;color:var(--text-muted)}
.pc-link{text-align:center;font-weight:700;color:var(--p600);min-height:44px;display:grid;place-items:center}
@media(min-width:900px){.hero2 .wrap{grid-template-columns:1fr 480px;gap:72px;align-items:center;padding-block:56px 72px}.hero2 .pcard{padding:30px}}
'''

# ---------- hero 3: Dzień ----------
TL = [("09:12", "Wysyłasz 2–3 zdjęcia", "camera"), ("09:16", "Dostajesz cenę i termin", "message-circle"), ("10:00", "Jesteśmy u Ciebie i pierzemy", "droplets"), ("15:00", "Wózek suchy, czas na spacer", "sun")]
def timeline():
    return '<ol class="tl">' + "".join(f'<li><time class="num">{t}</time><span class="dot">{ico(i)}</span><span>{s}</span></li>' for t, s, i in TL) + '</ol>'
HERO3 = f'''<section class="hero3"><div class="wrap">
<div><span class="eyebrow">Pranie wózków i fotelików · Poznań i okolice</span>
<h1>Pranie wózków i fotelików u Ciebie w domu – <em>gotowe tego samego dnia</em></h1>
<p class="lede">Rano wysyłasz zdjęcia, my pierzemy pod Twoim domem, po południu idziecie na spacer. Hipoalergiczne środki, foteliki według instrukcji producenta.</p>
<div class="rowp"><div><small>Wózek</small><b class="num">od 90 zł</b></div><div><small>Wózek 2w1</small><b class="num">od 120 zł</b></div><div><small>Fotelik</small><b class="num">od 80 zł</b></div></div>
<div class="ctas"><a class="btn btn-main" href="#wycena">{ico("camera")}Wyślij 2–3 zdjęcia – cena dziś</a><a class="btn btn-ghost" href="#cennik">Zobacz cennik</a></div></div>
<div class="day"><span class="eyebrow">Przykładowy dzień</span><p class="display dh">Od zdjęć do spaceru</p>{timeline()}<p class="chat-note">Godziny orientacyjne. Schnięcie trwa zwykle 3–5 godzin.</p></div></div></section>'''
CSS3 = '''
.hero3 .wrap{display:grid;gap:36px;padding-block:20px 52px}
.hero3 h1{font-size:clamp(2.05rem,6.2vw,3.4rem);margin-block:12px 16px}.hero3 h1 em{font-style:normal;color:var(--p500)}
.rowp{display:grid;grid-template-columns:repeat(3,1fr);margin-top:22px;border-block:2px solid var(--n900)}
.rowp div{padding:12px 10px;display:grid;line-height:1.15}.rowp div+div{border-left:1px solid var(--border)}.rowp small{color:var(--text-muted);font-size:.8rem}.rowp b{font:800 1.25rem/1.2 var(--display)}
.ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.ctas .btn{flex:1 1 260px}@media(min-width:900px){.ctas .btn{flex:0 0 auto}}
.day{background:var(--p800);color:#fff;border-radius:var(--r-2xl);padding:26px;display:grid;gap:14px;align-content:start}.day .eyebrow{color:var(--p200)}.day .dh{font-size:1.7rem}
.tl{list-style:none;padding:0;margin:6px 0 0;display:grid}
.tl li{display:grid;grid-template-columns:56px 40px 1fr;align-items:center;gap:12px;padding-block:12px;position:relative}
.tl li+li::before{content:"";position:absolute;left:calc(56px + 12px + 19px);top:-14px;height:26px;border-left:2px dashed rgba(255,255,255,.35)}
.tl time{font-weight:700;color:var(--p200)}.tl .dot{width:40px;height:40px;border-radius:50%;background:var(--p700);display:grid;place-items:center;position:relative}
.tl li:last-child .dot{background:var(--s300);color:var(--s950)}.tl span:last-child{font-weight:600}
.day .chat-note{color:var(--p200);text-align:left;margin:0}
@media(min-width:900px){.hero3 .wrap{grid-template-columns:1.1fr .9fr;gap:64px;align-items:center;padding-block:40px 80px}.day{padding:36px}}
'''

PAGES = {"direction-1-rozmowa": (HERO1, CSS1, ("", "band")), "direction-2-cennik": (HERO2, CSS2, ("band", "")), "direction-3-dzien": (HERO3, CSS3, ("", "band"))}
for name, (hero, css, alt) in PAGES.items():
    html = f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Pranie wózków i fotelików Poznań – u Ciebie, od 80 zł</title><link rel="stylesheet" href="base.css"><style>{css}</style></head><body>
{HEADER}<main>{hero}{lower(alt)}</main>{STICKY}</body></html>'''
    open(os.path.join(os.path.dirname(__file__), name + ".html"), "w").write(html)
print("built", list(PAGES))
