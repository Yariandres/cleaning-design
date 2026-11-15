#!/usr/bin/env python3
"""Builds the static frames for the public quote form, /poznan/wycena (handover draft quote-form-v1).

Run: python3 prototypes/quote-form/build.py
Needs the Lucide icon data (same source the developer uses):
  ../cleaning-sell-system/node_modules/@iconify-json/lucide/icons.json  (or LUCIDE_JSON=/path)

Every name, price, add-on, town, postcode, slot, duration and contact detail is SAMPLE DATA (prices from
docs/source/price-list.md, towns from docs/source/customer-stories-and-copy.md). In the app they come from
the database. Frames are static: each file is one state. Header, footer, buttons and tokens come from
../stroller/base.css (stroller-v1); quote.css adds the form.
"""
import json, os, html, pathlib

HERE = pathlib.Path(__file__).parent
LUCIDE = os.environ.get("LUCIDE_JSON") or str(HERE / "../../../cleaning-sell-system/node_modules/@iconify-json/lucide/icons.json")
_d = json.load(open(LUCIDE))
_icons, _alias = _d["icons"], _d.get("aliases", {})


def ico(name, cls=""):
    n = name
    while n not in _icons:
        n = _alias[n]["parent"]
    return f'<svg class="ico {cls}" viewBox="0 0 24 24" aria-hidden="true">{_icons[n]["body"]}</svg>'


e = html.escape
NB = " "
FRAMES = []


def zl(n):
    return f"{n:,}".replace(",", NB) + NB + "zł"


def pl_photos(n):
    return f"{n} zdjęcie" if n == 1 else (f"{n} zdjęcia" if 2 <= n <= 4 else f"{n} zdjęć")


# ------------------------------------------------------------------ sample data (price-list.md)
GROUPS = [
    ("dziecko", "Dziecko", "Wózki, foteliki, krzesełka", [
        ("stroller-single", "Wózek spacerowy", "Siedzisko, budka, pasy, stelaż i koła", 90, "szt"),
        ("stroller-2in1", "Wózek 2w1", "Gondola i spacerówka, stelaż i koła", 120, "szt"),
        ("stroller-3in1", "Wózek 3w1", "Z fotelikiem-nosidełkiem", 160, "szt"),
        ("stroller-twin", "Wózek bliźniaczy", "Oba siedziska, budki, stelaż i koła", 150, "szt"),
        ("carseat", "Fotelik samochodowy", "Pokrowiec, skorupa, baza", 80, "szt"),
        ("highchair", "Krzesełko, leżaczek lub mata", "Pokrowiec i elementy z tkaniny", 60, "szt"),
    ]),
    ("meble", "Meble tapicerowane", "Kanapy, narożniki, fotele, krzesła", [
        ("armchair", "Fotel", "Siedzisko, oparcie i podłokietniki", 90, "szt"),
        ("dining-chair", "Krzesło tapicerowane", "Siedzisko i oparcie", 25, "szt"),
        ("sofa-2", "Kanapa 2-osobowa", "Odkurzanie i pranie ekstrakcyjne", 150, "szt"),
        ("sofa-3", "Kanapa 3-osobowa", "Odkurzanie i pranie ekstrakcyjne", 180, "szt"),
        ("corner-sofa", "Narożnik", "Odkurzanie i pranie ekstrakcyjne", 260, "szt"),
    ]),
    ("materace", "Materace", "Jedna strona, druga za dopłatą", [
        ("mattress-single", "Materac jednoosobowy", "Jedna strona", 100, "szt"),
        ("mattress-double", "Materac dwuosobowy", "Jedna strona", 150, "szt"),
    ]),
    ("dywany", "Dywany", "Cena za m²", [
        ("rug-synthetic", "Dywan syntetyczny", "Odkurzanie i pranie ekstrakcyjne", 18, "m2"),
        ("rug-wool", "Dywan wełniany", "Łagodny środek do wełny", 25, "m2"),
        ("carpet", "Wykładzina dywanowa", "Pranie na miejscu", 9, "m2"),
    ]),
    ("auto", "Auto", "Wnętrze auta pod Twoim domem", [
        ("car-seat-single", "Pranie jednego fotela", "Siedzisko i oparcie", 80, "szt"),
        ("car-upholstery", "Pranie tapicerki (5 miejsc)", "Fotele i kanapa", 260, "szt"),
        ("car-detail", "Kompleksowe czyszczenie wnętrza", "Tapicerka, plastiki, szyby, dywaniki", 350, "szt"),
        ("car-leather", "Czyszczenie i konserwacja skóry", "Fotele i kanapa ze skóry", 160, "szt"),
        ("car-ozone", "Ozonowanie", "Usuwanie zapachów", 80, "szt"),
    ]),
]
ITEM = {k: (n, inc, p, u, g) for g, _, _, its in GROUPS for k, n, inc, p, u in its}
# add-ons the customer can know about; which group each applies to is an ASSUMPTION (data: addon.appliesTo)
ADDONS = {
    "impreg": ("Impregnacja tkaniny", "pct", 30, {"meble", "dywany"}),
    "allergy": ("Zabieg antyalergiczny", "zl", 20, {"meble", "materace"}),
    "side2": ("Druga strona materaca", "pct", 50, {"materace"}),
    "suv": ("SUV, 7 miejsc lub van", "pct", 20, {"auto"}),
}
PACKS = [
    ("pack-new-member", "Nowy Członek Rodziny", "przed porodem", "Materac dwuosobowy · Wózek 2w1 · Fotelik samochodowy", 319, 350),
    ("pack-family", "Rodzinny", "", "Kanapa 3-osobowa · Wózek 2w1 · Fotelik samochodowy", 339, 380),
    ("pack-home-refresh", "Odświeżenie Domu", "", "Kanapa 3-osobowa · Materac dwuosobowy · 2 fotele", 450, 510),
    ("pack-car-baby", "Auto i Maluch", "", "Pranie tapicerki auta · Wózek 2w1 · Fotelik samochodowy", 409, 460),
    ("pack-whole-family", "Cała Rodzina", "", "Kanapa 3-osobowa · Materac dwuosobowy · Pranie tapicerki auta · Wózek 2w1 · Fotelik samochodowy", 699, 790),
    ("pack-home", "Dom", "", "Narożnik · Wózek 2w1 · Pranie tapicerki auta. Dojazd gratis także w Strefie 2", 569, 640),
]
PACK = {k: (n, t, inc, p, w) for k, n, t, inc, p, w in PACKS}
MIN_ORDER, FREE_OVER, Z2_FEE = 150, 400, 25
FINE = "To szacunek z cennika. Wiążącą cenę podamy w wycenie, kiedy zobaczymy zdjęcia."
STEPS = ["Co mamy wyczyścić?", "Gdzie mamy przyjechać?", "Zdjęcia i termin", "Kontakt"]


# ------------------------------------------------------------------ estimate maths (one source for every frame)
def line(key, s):
    """(amount or None, price-line html, estimate label, estimate sub)"""
    n, _, p, u, _ = ITEM[key]
    if u == "m2":
        if s.get("unknown") or not s.get("area"):
            return None, f'<i>od</i> {zl(p)} / m² <small>zmierzymy na miejscu</small>', n, f"zmierzymy na miejscu, {zl(p)} / m²"
        a = float(s["area"].replace(",", "."))
        amt = round(a * p)
        return amt, f'<i>od</i> {zl(amt)} <small>{s["area"]}{NB}m² × {zl(p)}</small>', n, f'{s["area"]}{NB}m² × {zl(p)}'
    q = s.get("qty", 1)
    amt = q * p
    small = f' <small>{q} × {zl(p)}</small>' if q > 1 else ""
    return amt, f'<i>od</i> {zl(amt)}{small}', n + (f" × {q}" if q > 1 else ""), ""


def addon_amt(akey, key, s):
    n, kind, v, _ = ADDONS[akey]
    base = line(key, s)[0]
    if kind == "zl":
        return v * s.get("qty", 1)
    return None if base is None else round(base * v / 100)


def estimate(sel=None, packs=(), travel=None):
    """travel: None (not known yet) | ("z1", place) | ("z2", place) | ("other", place)"""
    sel = sel or {}
    rows, known, unknown = [], 0, False
    for pk in packs:
        n, _, inc, p, w = PACK[pk]
        rows.append((f"Pakiet {n}", inc.split(". ")[0], f'<s>{zl(w)}</s>{zl(p)}', ""))
        known += p
    for g, _, _, its in GROUPS:
        for key, *_ in its:
            if key not in sel:
                continue
            s = sel[key]
            amt, _, lab, sub = line(key, s)
            if amt is None:
                unknown = True
                rows.append((lab, sub, "do zmierzenia", "soft"))
            else:
                known += amt
                rows.append((lab, sub, zl(amt), ""))
            for a in s.get("addons", ()):
                aa = addon_amt(a, key, s)
                an, kind, v, _ = ADDONS[a]
                if aa is None:
                    rows.append((an, f"+{v}% ceny, po zmierzeniu", "do zmierzenia", "soft"))
                else:
                    known += aa
                    rows.append((an, f"{ITEM[key][0]}, +{v}%" if kind == "pct" else f"{ITEM[key][0]}, {zl(v)} za szt.", "+" + zl(aa), "soft"))
    empty = not rows
    topup = max(0, MIN_ORDER - known) if not empty else 0
    if topup:
        rows.append((f"Dopłata do minimalnego zamówienia", f"Minimalne zamówienie to {zl(MIN_ORDER)}", "+" + zl(topup), "soft"))
    sub = known + topup
    fee, od, note = 0, unknown, ""
    if empty:
        note = "wybierz rzeczy"
    elif travel is None:
        note = "jeszcze bez dojazdu"
    else:
        kind, place = travel
        if kind == "z1":
            rows.append(("Dojazd", place, "gratis", "soft"))
            note = "dojazd gratis"
        elif kind == "z2":
            if sub >= FREE_OVER:
                rows.append(("Dojazd", f"{place}, gratis od {zl(FREE_OVER)}", "gratis", "soft"))
                note = "dojazd gratis"
            else:
                fee = Z2_FEE
                rows.append(("Dojazd", f"{place}, Strefa 2", "+" + zl(fee), "soft"))
                note = f"w tym dojazd {zl(fee)}"
        else:
            od = True
            rows.append(("Dojazd", f"{place}, wycenimy indywidualnie", "w wycenie", "soft"))
            note = "+ dojazd, wycenimy"
    if topup:
        note = f"min. zamówienie {zl(MIN_ORDER)}"
    elif unknown:
        note = "+ dywan po zmierzeniu"
    return dict(rows=rows, total=None if empty else sub + fee, od=od, note=note, sub=sub, topup=topup, empty=empty)


def amount(est):
    if est["empty"]:
        return "—"
    return ("<i>od</i>" if est["od"] else "") + zl(est["total"])


def rows_html(est):
    li = "".join(f'<li class="{c}"><span>{l}{"<small>" + s + "</small>" if s else ""}</span><b>{v}</b></li>' for l, s, v, c in est["rows"])
    return f'<ul class="rows">{li}<li class="total"><span>Szacunkowa cena</span><b data-bind="estimate.total">{amount(est)}</b></li></ul>'


def aside(est):
    if est["empty"]:
        inner = '<p class="big none" data-bind="estimate.total">—</p><p class="fine">Zaznacz rzeczy po lewej. Cenę policzymy od razu, z cennika.</p>'
    else:
        li = "".join(f'<li class="{c}"><span>{l}{"<small>" + s + "</small>" if s else ""}</span><b>{v}</b></li>' for l, s, v, c in est["rows"])
        inner = f'<p class="big hl" data-bind="estimate.total">{amount(est)}</p><ul class="rows">{li}</ul><p class="fine">{FINE}</p>'
    return f'<aside class="q-aside" aria-label="Szacunkowa cena"><div class="est"><span class="eyebrow">Szacunkowa cena</span>{inner}</div></aside>'


def ebar(est, label="Dalej", state="", expanded=False):
    v = f'<span class="v none">—</span>' if est["empty"] else f'<span class="v hl" data-bind="estimate.total">{amount(est)}</span>'
    if state == "busy":
        btn = f'<button class="btn btn-main busy" type="submit" form="q-form" aria-busy="true" disabled style="background:var(--p600);color:#fff">{ico("loader-circle", "spin")}Wysyłamy…</button>'
    else:
        arrow = "" if label != "Dalej" else ico("arrow-right")
        btn = f'<button class="btn btn-main" type="submit" form="q-form">{label}{arrow}</button>'
    return f'''<div class="ebar" role="region" aria-label="Szacunkowa cena i następny krok">
<button class="e-sum" type="button" aria-expanded="{"true" if expanded else "false"}" aria-controls="e-sheet"><span class="l">Szacunkowa cena{ico("chevron-up")}</span>{v}<span class="n">{est["note"]}</span><span class="vh">Pokaż szczegóły</span></button>
{btn}</div>
<p class="vh" role="status" aria-live="polite" aria-atomic="true">Szacunkowa cena: {"jeszcze nie policzona" if est["empty"] else html.unescape(amount(est).replace("<i>", "").replace("</i>", " "))}</p>'''


def sheet(est):
    return f'''<div class="overlay"><div class="sheet" id="e-sheet" role="dialog" aria-modal="true" aria-labelledby="e-sheet-t">
<div class="sheet-h"><h2 id="e-sheet-t">Szacunkowa cena</h2><button class="rnd plain" type="button" aria-label="Zamknij">{ico("x")}</button></div>
{rows_html(est)}<p class="fine">{FINE}</p><button class="btn-line" type="button" style="margin-top:0">Zamknij</button></div></div>'''


# ------------------------------------------------------------------ page shell (header and footer as on the stroller page)
HEADER = f'''<header class="site-h"><div class="wrap"><a href="/" aria-label="Nowiutko, strona główna"><img src="../stroller/assets/logo.svg" alt="Nowiutko" width="190" height="46"></a>
<a class="tel" href="tel:+48500000000" data-bind="business:phone">{ico("phone")}<span class="num">500 000 000</span></a></div></header>'''
FOOTER = '''<footer><div class="wrap foot"><span>Nowiutko · pranie tapicerki, wózków i aut u Ciebie · Poznań</span><nav aria-label="Informacje"><a href="/polityka-prywatnosci">Prywatność</a><a href="/cookies">Cookies</a><a href="/regulamin">Regulamin</a></nav></div></footer>'''
DOORS = f'''<p class="doors"><span>Wolisz inaczej?</span><a href="https://wa.me/48500000000" data-bind="business:whatsapp">Napisz na WhatsApp</a><a href="tel:+48500000000" data-bind="business:phone">Zadzwoń: 500{NB}000{NB}000</a></p>'''
FOOT_CSS = ".foot{display:flex;justify-content:space-between;gap:12px 24px;flex-wrap:wrap;align-items:center}.foot nav{display:flex;gap:4px 20px;flex-wrap:wrap}.foot a{min-height:44px;display:inline-grid;align-items:center}"


def prog(n, back=True):
    lis = ""
    for i, name in enumerate(STEPS, 1):
        if i < n:
            lis += f'<li class="done"><a href="#" aria-label="Wróć do kroku {i}: {name}"><i></i></a></li>'
        elif i == n:
            lis += f'<li class="cur full"><span aria-current="step"><i></i><span class="vh">Krok {i}: {name} (tu jesteś)</span></span></li>'
        else:
            lis += f'<li><span><i></i><span class="vh">Krok {i}: {name}</span></span></li>'
    b = f'<a class="back" href="#">{ico("chevron-left")}Wstecz</a>' if back and n > 1 else "<span></span>"
    return f'<nav class="prog" aria-label="Postęp formularza"><div class="prog-top">{b}<p class="where">Krok <b>{n}</b> z 4</p></div><ol>{lis}</ol></nav>'


def qnav(n, label="Dalej", state=""):
    back = f'<a class="btn-quiet" href="#">{ico("chevron-left")}Wstecz</a>' if n > 1 else "<span></span>"
    if state == "busy":
        btn = f'<button class="btn btn-main busy" aria-busy="true" disabled style="background:var(--p600);color:#fff">{ico("loader-circle", "spin")}Wysyłamy…</button>'
    else:
        btn = f'<button class="btn btn-main" type="submit">{label}{ico("arrow-right") if label == "Dalej" else ""}</button>'
    return f'<div class="q-nav">{back}{btn}</div>'


def page(fname, group, note, n, lede, body, est, label="Dalej", state="", overlay="", back=True, expanded=False):
    FRAMES.append((fname, group, note))
    busy = ' aria-busy="true"' if state == "busy" else ""
    doc = f'''<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#F5FAF8">
<title>Wycena prania ze zdjęć – Poznań i okolice | Nowiutko</title>
<link rel="stylesheet" href="../stroller/base.css"><link rel="stylesheet" href="quote.css"><style>{FOOT_CSS}</style></head>
<body>
<!-- Frame: {fname} · {e(note)} · SAMPLE DATA, static state -->
<a class="skip" href="#krok">Przejdź do formularza</a>
{HEADER}
<main class="q wrap"><div class="q-main">
<h1 class="eyebrow">Wycena prania ze zdjęć · Poznań i okolice</h1>
{prog(n, back)}
<form id="q-form" novalidate{busy}>
<div class="step-h"><h2 id="krok" tabindex="-1">{STEPS[n - 1]}</h2>{f"<p>{lede}</p>" if lede else ""}</div>
{body}
{qnav(n, label, state)}
</form>
{DOORS}
</div>
{aside(est)}
</main>
{FOOTER}
{ebar(est, label, state, expanded)}{overlay}
</body></html>'''
    (HERE / fname).write_text(doc, encoding="utf-8")


def err(msg, id_=""):
    i = f' id="{id_}"' if id_ else ""
    return f'<p class="errmsg" role="alert"{i}>{ico("circle-alert")}{msg}</p>'


def notebox(kind, icon, text, role=""):
    r = f' role="{role}"' if role else ""
    return f'<div class="note {kind}"{r}>{ico(icon)}<p>{text}</p></div>'


# ------------------------------------------------------------------ step 1
def item_row(key, s, gkey):
    n, inc, p, u, _ = ITEM[key]
    bind = f' data-bind="price:{key}"'
    if s is None:
        unit = " / m²" if u == "m2" else ""
        return f'''<li class="it"><div><span class="name">{n}</span><span class="inc">{inc}</span><span class="pr"{bind}><i>od</i> {zl(p)}{unit}</span></div>
<button class="rnd" type="button" aria-label="Dodaj: {n}">{ico("plus")}</button></li>'''
    amt, prl, _, _ = line(key, s)
    more = ""
    if u == "m2":
        bad = s.get("err")
        dis = " disabled" if s.get("unknown") else ""
        inv = ' aria-invalid="true"' if bad else ""
        more += f'''<div class="field{" err" if bad else ""}" style="margin-top:10px"><label for="a-{key}">Powierzchnia</label>
<div class="inp has-suf short"><input id="a-{key}" inputmode="decimal" autocomplete="off" value="{"" if s.get("unknown") else s.get("area", "")}" aria-describedby="h-{key}"{inv}{dis}><span class="suf">m²</span></div>
{err("Wpisz powierzchnię w m² albo zaznacz „Nie znam wymiarów”.", "h-" + key) if bad else f'<p class="hint" id="h-{key}">Długość × szerokość, np. 2 × 3 m to 6 m². Kilka dywanów? Wpisz razem.</p>'}</div>
<label class="ck"><input type="checkbox"{" checked" if s.get("unknown") else ""}><span class="tx">Nie znam wymiarów<small>Zmierzymy na miejscu. Cenę za m² znasz już teraz.</small></span></label>'''
        ctl = f'<button class="rnd plain" type="button" aria-label="Usuń: {n}">{ico("trash-2")}</button>'
    else:
        q = s.get("qty", 1)
        minus = f'<button class="rnd" type="button" aria-label="Usuń: {n}">{ico("trash-2")}</button>' if q == 1 else f'<button class="rnd" type="button" aria-label="Mniej: {n}">{ico("minus")}</button>'
        ctl = f'<div class="stp" role="group" aria-label="Ilość: {n}">{minus}<output aria-live="polite">{q}</output><button class="rnd" type="button" aria-label="Więcej: {n}">{ico("plus")}</button></div>'
    ao = [a for a, (_, _, _, gs) in ADDONS.items() if gkey in gs]
    if ao:
        more += '<p class="lbl">Dodatki</p>'
        for a in ao:
            an, kind, v, _ = ADDONS[a]
            aa = addon_amt(a, key, s)
            amt_s = f"<i>+{v}%</i>+{zl(aa)}" if kind == "pct" and aa is not None else (f"+{v}%" if aa is None else f"+{zl(aa)}")
            more += f'<label class="ck"><input type="checkbox"{" checked" if a in s.get("addons", ()) else ""}><span class="tx">{an}</span><span class="amt" data-bind="addon:{a}">{amt_s}</span></label>'
    more = f'<div class="more">{more}</div>' if more else ""
    return f'''<li class="it on"><div><span class="name">{n}</span><span class="inc">{inc}</span><span class="pr"{bind}>{prl}</span></div>{ctl}{more}</li>'''


def group_html(g, sel, open_, bad=False):
    gkey, name, meta, its = g
    cnt = sum(sel[k].get("qty", 1) if ITEM[k][3] == "szt" else 1 for k, *_ in its if k in sel)
    lo = min(p for _, _, _, p, _ in its)
    unit = " / m²" if its[0][4] == "m2" else ""
    badge = f'<span class="cnt" aria-label="Wybrane: {cnt}">{cnt}</span>' if cnt else ""
    body = f'<ul id="g-{gkey}">' + "".join(item_row(k, sel.get(k), gkey) for k, *_ in its) + "</ul>" if open_ else ""
    return f'''<section class="grp{" open" if open_ else ""}{" err" if bad else ""}"><h3><button class="grp-h" type="button" aria-expanded="{"true" if open_ else "false"}" aria-controls="g-{gkey}"><span class="t"><b>{name}</b><span>{meta} · od {zl(lo)}{unit}</span></span>{badge}{ico("chevron-down", "chev")}</button></h3>{body}</section>'''


def packs_html(pk_sel, open_, first=None):
    order = PACKS if not first else [p for p in PACKS if p[0] in first] + [p for p in PACKS if p[0] not in first]
    cnt = len(pk_sel)
    badge = f'<span class="cnt" aria-label="Wybrane: {cnt}">{cnt}</span>' if cnt else ""
    body = ""
    if open_:
        body = '<ul class="pks" id="g-pakiety">'
        for k, n, t, inc, p, w in order:
            tag = f'<span class="tag" data-bind="pack:{k}:tag">{t}</span>' if t else ""
            body += f'''<li><label class="pk"><input type="checkbox"{" checked" if k in pk_sel else ""}><span class="name">{n}{tag}</span><span class="inc">{inc}</span>
<span class="pr"><b data-bind="price:{k}">{zl(p)}</b><s data-bind="price:{k}-was">{zl(w)}</s><span>taniej o {zl(w - p)}</span></span></label></li>'''
        body += "</ul>"
    lo = min(p[4] for p in PACKS)
    return f'''<section class="grp{" open" if open_ else ""}"><h3><button class="grp-h" type="button" aria-expanded="{"true" if open_ else "false"}" aria-controls="g-pakiety"><span class="t"><b>Pakiety</b><span>Taniej w zestawie · od {zl(lo)}</span></span>{badge}{ico("chevron-down", "chev")}</button></h3>{body}</section>'''


def step1(sel=None, pk_sel=(), open_=(), order=None, top="", bottom="", bad=False, pk_first=None):
    sel = sel or {}
    order = order or ["dziecko", "meble", "materace", "dywany", "auto", "pakiety"]
    gmap = {g[0]: g for g in GROUPS}
    out = top + '<div class="groups">'
    for k in order:
        out += packs_html(pk_sel, "pakiety" in open_, pk_first) if k == "pakiety" else group_html(gmap[k], sel, k in open_, bad)
    out += "</div>" + bottom
    return out


L1 = "Zaznacz rzeczy, a od razu zobaczysz szacunkową cenę. Ceny brutto."
STROLLER_ORDER = ["dziecko", "pakiety", "meble", "materace", "dywany", "auto"]
STORY_SEL = {"rug-synthetic": dict(area="6")}
STORY_PK = ("pack-family",)
Z1 = ("z1", "Swarzędz")

page("01-krok1-pusty.html", "Step 1", "Step 1, empty (direct visit): five groups and Pakiety, all closed; estimate bar empty.", 1, L1, step1(), estimate())

s = {"armchair": dict(qty=2, addons={"impreg"}), "dining-chair": dict(qty=3)}
page("02-krok1-ilosci-dodatki.html", "Step 1", "Quantities and add-ons: 2 armchairs with impregnation, 3 chairs. Add-ons appear inside a selected row.", 1, L1,
     step1(s, open_=("meble",)), estimate(s))

page("03-krok1-z-wozkow.html", "Step 1", "Pre-filled from the stroller page: Dziecko first and open, Pakiety second; nothing ticked for the customer.", 1, L1,
     step1(open_=("dziecko",), order=STROLLER_ORDER, top=notebox("mint", "info", "Zaczynamy od wózków i fotelików. Pozostałe rzeczy znajdziesz niżej.") + '<div style="height:12px"></div>'), estimate())

page("04-krok1-z-wozkow-pakiet.html", "Step 1", "Pre-filled from the stroller page with a package clicked there: Pakiety first and open, Rodzinny selected.", 1, L1,
     step1(pk_sel=STORY_PK, open_=("pakiety",), order=["pakiety", "dziecko", "meble", "materace", "dywany", "auto"], pk_first=("pack-family", "pack-new-member", "pack-car-baby"),
           top=notebox("mint", "info", "<b>Pakiet Rodzinny jest już zaznaczony.</b> Możesz go zmienić albo coś dodać.") + '<div style="height:12px"></div>'), estimate(packs=STORY_PK))

s = {"rug-synthetic": dict(area="6"), "rug-wool": dict(unknown=True)}
page("05-krok1-dywan-m2.html", "Step 1", "Per-m² items: area typed (6 m²) and “Nie znam wymiarów” ticked; the estimate turns into “od …”.", 1, L1,
     step1(s, pk_sel=STORY_PK, open_=("dywany",)), estimate(s, STORY_PK))

s = {"carseat": dict(qty=1)}
e6 = estimate(s)
MINNOTE = '<div style="height:12px"></div>' + notebox("", "info", f"<b>Minimalne zamówienie to {zl(MIN_ORDER)}.</b> Masz teraz {zl(80)}, więc w szacunku jest dopłata {zl(70)}. Możesz też dobrać coś jeszcze w tej kwocie.")
page("06-krok1-minimum.html", "Step 1", "Basket below the 150 zł minimum: the estimate shows the top-up; a neutral note explains it.", 1, L1,
     step1(s, open_=("dziecko",), bottom=MINNOTE), e6)
page("07-krok1-szacunek-arkusz.html", "Step 1", "Estimate sheet (tap the bar): breakdown with the minimum-order top-up.", 1, L1,
     step1(s, open_=("dziecko",), bottom=MINNOTE), e6, overlay=sheet(e6), expanded=True)

page("08-krok1-blad-nic.html", "Step 1", "Error after “Dalej” with nothing chosen: text under the list, focus moves to it.", 1, L1,
     step1(bad=True, bottom=err("Wybierz przynajmniej jedną rzecz albo pakiet.")), estimate())

s = {"rug-synthetic": dict(area="", err=True)}
page("09-krok1-blad-m2.html", "Step 1", "Error: rug chosen without an area.", 1, L1, step1(s, open_=("dywany",)), estimate(s))

s = {"sofa-3": dict(qty=1), "stroller-2in1": dict(qty=1), "carseat": dict(qty=1)}
HINT = '<div style="height:12px"></div>' + f'''<div class="note mint" role="status">{ico("package")}<p><b>Te trzy rzeczy są w pakiecie Rodzinny.</b> W pakiecie kosztują {zl(339)} zamiast {zl(380)}.<br><button class="act" type="button">Zamień na pakiet</button></p></div>'''
page("10-krok1-podpowiedz-pakietu.html", "Step 1", "Recommendation (optional): chosen items match a package, one tap swaps them. True saving only.", 1, L1,
     step1(s, open_=("meble",), bottom=HINT), estimate(s))


# ------------------------------------------------------------------ step 2
L2 = "Od miejsca zależy dojazd i wolne terminy."
PLACE_LBL = "Miejscowość, dzielnica lub kod pocztowy"


def place_field(value="", hint=True, bad="", focus=False, menu=""):
    clr = f'<button class="clr" type="button" aria-label="Wyczyść">{ico("x")}</button>' if value else ""
    inv = ' aria-invalid="true"' if bad else ""
    exp = "true" if menu else "false"
    under = err(bad, "place-h") if bad else ('<p class="hint" id="place-h">Zacznij pisać albo wybierz z listy. Kod pocztowy też zadziała.</p>' if hint else "")
    return f'''<div class="field{" err" if bad else ""}"><label for="place">{PLACE_LBL}</label>
<div class="inp has-lead{" has-clr" if value else ""}">{ico("map-pin", "lead")}<input id="place" role="combobox" aria-expanded="{exp}" aria-controls="place-list" aria-autocomplete="list" autocomplete="off" placeholder="np. Winogrady albo 62-020" value="{value}" aria-describedby="place-h"{inv}{' class="focus"' if focus else ""}>{clr}</div>
{menu}{under}</div>'''


def zone(place, fee, why="", plain=False, icon="check"):
    w = f'<p class="why">{why}</p>' if why else ""
    return f'''<div class="zone{" plain" if plain else ""}" role="status"><span class="ic">{ico(icon)}</span><p class="place">{place}</p><p class="fee" data-bind="zone.message">{fee}</p>{w}</div>'''


MENU = '''<ul class="menu" id="place-list" role="listbox" aria-label="Miejscowości">
<li role="presentation" class="gh">Poznań <span>Dojazd gratis</span></li>
<li role="option" aria-selected="true"><mark>Mo</mark>rasko</li><li role="option" aria-selected="false">S<mark>mo</mark>chowice</li>
<li role="presentation" class="gh">Okolice – Strefa 2 <span>Dojazd 25 zł, gratis od 400 zł</span></li>
<li role="option" aria-selected="false"><mark>Mo</mark>sina</li>
<li role="option" aria-selected="false" class="other">Inna miejscowość…</li></ul>'''
MENU_ALL = '''<ul class="menu" id="place-list" role="listbox" aria-label="Miejscowości">
<li role="presentation" class="gh">Poznań <span>Dojazd gratis</span></li>
<li role="option" aria-selected="false">Piątkowo</li><li role="option" aria-selected="false">Winogrady</li><li role="option" aria-selected="false">Naramowice</li><li role="option" aria-selected="false">Morasko</li>
<li role="presentation" class="gh" style="color:var(--n500);letter-spacing:0;text-transform:none;font-weight:500">… i 18 kolejnych dzielnic (lista się przewija)</li>
<li role="presentation" class="gh">Okolice – bez dopłaty <span>Dojazd gratis</span></li>
<li role="option" aria-selected="false">Suchy Las</li><li role="option" aria-selected="false">Złotniki</li><li role="option" aria-selected="false">Swarzędz</li>
<li role="presentation" class="gh" style="color:var(--n500);letter-spacing:0;text-transform:none;font-weight:500">… i 9 kolejnych</li>
<li role="presentation" class="gh">Okolice – Strefa 2 <span>Dojazd 25 zł, gratis od 400 zł</span></li>
<li role="option" aria-selected="false">Kórnik</li><li role="option" aria-selected="false">Mosina</li>
<li role="presentation" class="gh" style="color:var(--n500);letter-spacing:0;text-transform:none;font-weight:500">… i 7 kolejnych</li>
<li role="option" aria-selected="false" class="other">Inna miejscowość…</li></ul>'''

E_STORY1 = estimate(STORY_SEL, STORY_PK)
E_PK1 = estimate(packs=STORY_PK)
page("11-krok2-pusty.html", "Step 2", "Step 2, empty: one field for town, district or postcode.", 2, L2, place_field(), E_STORY1)
page("12-krok2-lista-grupy.html", "Step 2", "Field focused, list open: the four groups with their travel message (list scrolls; shortened here).", 2, L2,
     place_field(focus=True, hint=False, menu=MENU_ALL), E_STORY1)
page("13-krok2-lista-szukanie.html", "Step 2", "Typing “mo”: matches from two groups, group headers kept, “Inna miejscowość…” always last.", 2, L2,
     place_field("mo", focus=True, hint=False, menu=MENU), E_STORY1)
page("14-krok2-kod-pasuje.html", "Step 2", "Postcode 62-020 typed: Swarzędz picked, zone message shown, estimate updated at once.", 2, L2,
     place_field("Swarzędz", hint=False) + zone("Kod 62-020 · okolice Poznania, bez dopłaty", "Dojazd gratis"), estimate(STORY_SEL, STORY_PK, Z1))
page("15-krok2-strefa2.html", "Step 2", "Zone 2 below 400 zł: 25 zł travel in the estimate; the 400 zł rule stated as a fact, no progress bar.", 2, L2,
     place_field("Mosina", hint=False) + zone("Okolice – Strefa 2", f"Dojazd {zl(25)}", f"Przy zamówieniu od {zl(400)} dojazd jest gratis. Twoje zamówienie ma teraz {zl(339)}.", icon="map-pin"), estimate(packs=STORY_PK, travel=("z2", "Mosina")))
e16 = estimate(packs=STORY_PK, travel=("z2", "Mosina"))
page("16-krok2-strefa2-arkusz.html", "Step 2", "Estimate sheet with the Zone 2 travel fee.", 2, L2,
     place_field("Mosina", hint=False) + zone("Okolice – Strefa 2", f"Dojazd {zl(25)}", f"Przy zamówieniu od {zl(400)} dojazd jest gratis. Twoje zamówienie ma teraz {zl(339)}.", icon="map-pin"), e16, overlay=sheet(e16), expanded=True)
page("17-krok2-strefa2-gratis.html", "Step 2", "Zone 2 at 400 zł or more: travel free.", 2, L2,
     place_field("Mosina", hint=False) + zone("Okolice – Strefa 2", "Dojazd gratis", f"W Strefie 2 dojazd kosztuje {zl(25)}, ale od {zl(400)} jest gratis. Twoje zamówienie ma {zl(447)}."), estimate(STORY_SEL, STORY_PK, ("z2", "Mosina")))


def other_field(value="", bad=""):
    inv = ' aria-invalid="true"' if bad else ""
    return f'''<div class="field{" err" if bad else ""}" style="margin-top:20px"><label for="town">Miejscowość</label>
<div class="inp"><input id="town" autocomplete="address-level2" value="{value}"{inv}></div>{err(bad) if bad else ""}</div>'''


OTHER_WHY = f"Poza powiatem poznańskim liczymy 1,50{NB}zł za km od granicy powiatu. Dokładną kwotę podamy w wycenie."
page("18-krok2-kod-nie-pasuje.html", "Step 2", "Postcode matches nothing: switches to “Inna miejscowość” with a free-text field.", 2, L2,
     place_field("64-100", hint=False) + '<div style="height:12px"></div>' + notebox("", "info", "<b>Kodu 64-100 nie mamy na liście.</b> Wpisz miejscowość, a dojazd wycenimy indywidualnie.", "status") + other_field(), estimate(STORY_SEL, STORY_PK, ("other", "inna miejscowość")))
page("19-krok2-inna-miejscowosc.html", "Step 2", "“Inna miejscowość” filled: travel quoted individually, estimate reads “od …”.", 2, L2,
     place_field("Inna miejscowość", hint=False) + other_field("Września") + zone("Września", "Wycenimy dojazd indywidualnie", OTHER_WHY, plain=True, icon="map-pin"), estimate(STORY_SEL, STORY_PK, ("other", "Września")))
page("20-krok2-blad-brak.html", "Step 2", "Error: “Dalej” with no place.", 2, L2, place_field(bad="Wybierz miejscowość z listy albo wpisz kod pocztowy."), E_STORY1)
page("21-krok2-blad-kod.html", "Step 2", "Error: postcode in the wrong format (on blur).", 2, L2, place_field("62-0", bad="Wpisz kod w formacie 00-000."), E_STORY1)
page("22-krok2-blad-inna.html", "Step 2", "Error: “Inna miejscowość” chosen, name left empty.", 2, L2,
     place_field("Inna miejscowość", hint=False) + other_field(bad="Wpisz nazwę miejscowości."), E_STORY1)


# ------------------------------------------------------------------ step 3
L3 = "Zdjęcia pomagają podać dokładną cenę. Termin wybierasz wstępnie: potwierdzimy go w wycenie."
E3 = estimate(STORY_SEL, STORY_PK, Z1)


def photo(kind, n, extra=""):
    th = '<span class="th">zdjęcie</span>'
    rm = f'<button class="rnd plain" type="button" aria-label="Usuń zdjęcie {n}">{ico("trash-2")}</button>'
    if kind == "ok":
        return f'<li class="pho ok">{th}<div><b>Zdjęcie {n}</b><span class="st">{ico("check")}Wysłane</span></div><div class="acts">{rm}</div></li>'
    if kind == "up":
        return f'''<li class="pho">{th}<div><b>Zdjęcie {n}</b><span class="st" role="status">Wysyłamy… {extra}%</span><span class="bar" role="progressbar" aria-label="Wysyłanie zdjęcia {n}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="{extra}"><i style="transform:scaleX(.{extra})"></i></span></div><div class="acts"><button class="rnd plain" type="button" aria-label="Przerwij wysyłanie zdjęcia {n}">{ico("x")}</button></div></li>'''
    if kind == "fail":
        return f'''<li class="pho bad">{th}<div><b>Zdjęcie {n}</b><span class="st" role="alert">{ico("circle-alert")}Nie udało się wysłać. Sprawdź internet i spróbuj ponownie.</span></div><div class="acts"><button class="rnd" type="button" aria-label="Wyślij ponownie zdjęcie {n}">{ico("rotate-cw")}</button>{rm}</div></li>'''
    msg = "Plik ma 31 MB. Największy, jaki przyjmiemy, to 20 MB." if kind == "big" else "Tego formatu nie otworzymy. Dodaj zdjęcie JPG, PNG, WebP lub HEIC."
    return f'''<li class="pho bad"><span class="th none">{ico("triangle-alert")}</span><div><b>{extra}</b><span class="st" role="alert">{ico("circle-alert")}{msg}</span></div><div class="acts">{rm}</div></li>'''


def photos(items=(), count=0, full=False):
    lst = f'<ul class="photos" aria-label="Twoje zdjęcia">{"".join(items)}</ul>' if items else ""
    if full:
        drop = f'<button class="drop" type="button" disabled>{ico("image-plus")}Dodaj zdjęcia</button><div class="drop-row"><span>Masz już 5 zdjęć. Usuń jedno, żeby dodać inne.</span><b class="num">5 z 5</b></div>'
    else:
        drop = f'<button class="drop" type="button">{ico("image-plus")}Dodaj zdjęcia</button><div class="drop-row"><span>Z aparatu lub galerii · JPG, PNG, WebP, HEIC</span><b class="num">{count} z 5</b></div>'
    return f'''<h3 class="sub-h">Zdjęcia <small>opcjonalnie, do 5</small></h3>
<p class="sub-p">Najbardziej pomagają trzy ujęcia: całość, plamy z bliska i metka.</p>{lst}{drop}<input class="vh" type="file" accept="image/jpeg,image/png,image/webp,image/heic,image/heif" multiple tabindex="-1" aria-hidden="true">'''


DAYS_AREA = [("czw. 19 lis", "", [("10:00", ""), ("13:30", "")]), ("czw. 26 lis", "", [("10:00", ""), ("16:00", "")])]
DAYS_REST = [("jutro", "pon. 16 lis", [("13:30", ""), ("16:00", "")]), ("wt. 17 lis", "", [("10:00", ""), ("18:00", "+15%")]),
             ("śr. 18 lis", "", [("10:00", ""), ("13:30", ""), ("16:00", "")]), ("pt. 20 lis", "", [("13:30", "")]),
             ("sob. 21 lis", "", [("10:00", "+15%"), ("13:30", "+15%")])]


def days_html(days, chosen, lock):
    out = ""
    for d, sub, ts in days:
        chips = ""
        for t, tag in ts:
            lab = f"{d}, {t}"
            on = lab in chosen
            dis = " disabled" if (lock and not on) else ""
            sm = f"<small>{tag}</small>" if tag else ""
            aria = f'{d}{" (" + sub + ")" if sub else ""}, {t}{", dopłata 15%" if tag else ""}'
            chips += f'<label class="sl"><input type="checkbox" aria-label="{aria}"{" checked" if on else ""}{dis}>{t}{sm}</label>'
        out += f'<div class="day"><p class="d">{d}{"<small>" + sub + "</small>" if sub else ""}</p><div class="ts">{chips}</div></div>'
    return out


SLOT_H = '<h3 class="sub-h">Kiedy Ci pasuje?</h3>'
SLOT_P = '<p class="sub-p">Wybierz 2 lub 3 terminy. Jeden z nich potwierdzimy w wycenie. Wizyta potrwa około <span data-bind="visit.durationLabel">3,5 godz.</span></p>'


def none_box(checked=False, text=""):
    extra = f'''<div class="field"><label for="when">Dni i godziny, które Ci pasują <span class="opt">(opcjonalnie)</span></label><div class="inp"><textarea id="when" rows="2" placeholder="np. po 17:00, najlepiej w piątki">{text}</textarea></div><p class="hint">Termin zaproponujemy w wycenie.</p></div>''' if checked else ""
    return f'<div class="none-box"><label class="ck"><input type="checkbox"{" checked" if checked else ""}><span class="tx">Żaden termin mi nie pasuje</span></label>{extra}</div>'


def slots(chosen=(), bad="", top="", none=False, evening=False):
    lock = len(chosen) >= 3 or none
    cls = ' class="dis"' if none else ""
    body = f'''<div class="slots"{' aria-disabled="true"' if none else ""}><div class="slot-g"{cls}><h4><span data-bind="areaDay.label">W czwartki jeździmy w Twoją okolicę</span></h4>{days_html(DAYS_AREA, chosen, lock)}</div>
<div class="slot-g"{cls}><h4>Pozostałe terminy</h4>{days_html(DAYS_REST, chosen, lock)}</div></div>'''
    more = "" if none else f'<button class="btn-line" type="button">Pokaż późniejsze terminy{ico("chevron-down")}</button>'
    n = len(chosen)
    picked = "" if none else f'<p class="picked" role="status"><span>Wybrane: <b class="num">{n} z 3</b></span><span>{"Możesz jeszcze dodać jeden." if n == 2 else ("To już komplet." if n == 3 else "")}</span></p>'
    ev = f'<div style="height:12px"></div>' + notebox("", "info", f"<b>Wieczorem i w weekend dopłata wynosi 15%.</b> Doliczymy ją tylko wtedy, gdy wizyta odbędzie się w takim terminie (tu: ok. {zl(67)}).", "status") if evening else '<p class="hint">Wieczorem i w weekend dopłata wynosi 15%. Takie terminy mają oznaczenie +15%.</p>'
    return f'''{SLOT_H}{SLOT_P}{top}<fieldset{' aria-invalid="true"' if bad else ""}><legend class="vh">Wolne terminy</legend>{body}</fieldset>{more}{picked}{err(bad) if bad else ""}{ev}{none_box(none, "po 17:00, najlepiej w piątki" if none else "")}'''


TWO = ("śr. 18 lis, 13:30", "czw. 19 lis, 10:00")
page("23-krok3-pusty.html", "Step 3", "Step 3, default: no photos yet, slots loaded, area-day slots first.", 3, L3, photos() + slots(), E3)
page("24-krok3-zdjecia-stany.html", "Step 3", "Photo states: two sent, one uploading (62%), one failed (retry), one too big, one wrong type. Errors sit on that photo only.", 3, L3,
     photos([photo("ok", 1), photo("ok", 2), photo("up", 3, "62"), photo("fail", 4), photo("big", 5, "Film z wakacji.jpg"), photo("type", 6, "Rachunek.pdf")], 4) + slots(), E3)
page("25-krok3-zdjecia-komplet.html", "Step 3", "Five photos: the add button is off and says why.", 3, L3,
     photos([photo("ok", i) for i in range(1, 6)], 5, full=True) + slots(), E3)
page("26-krok3-terminy-wybrane.html", "Step 3", "Two of three times chosen.", 3, L3, photos([photo("ok", 1), photo("ok", 2), photo("ok", 3)], 3) + slots(TWO), E3)
page("27-krok3-terminy-komplet-wieczor.html", "Step 3", "Three chosen (the rest switch off) including an evening slot: the +15% rule is explained, not added to the total.", 3, L3,
     photos([photo("ok", 1), photo("ok", 2), photo("ok", 3)], 3) + slots(TWO + ("wt. 17 lis, 18:00",), evening=True), E3)

PILL = '<span class="sk pill"></span>'
SK = "".join(f'<div class="day"><p class="d"><span class="sk txt"></span></p><div class="ts">{PILL * (3 if i % 2 else 2)}</div></div>' for i in range(4))
page("28-krok3-terminy-wczytywanie.html", "Step 3", "Slots loading (they depend on steps 1 and 2). Photos can be added meanwhile.", 3, L3,
     photos() + f'{SLOT_H}{SLOT_P}<div class="slots" aria-busy="true"><p class="vh" role="status">Sprawdzamy wolne terminy…</p><div class="slot-g">{SK}</div></div>' + none_box(), E3)
page("29-krok3-terminy-blad.html", "Step 3", "Slots failed to load: retry, and the enquiry is never blocked.", 3, L3,
     photos() + f'''{SLOT_H}<div class="empty bad" role="alert"><span class="big">{ico("triangle-alert")}</span><h4>Nie udało się wczytać terminów</h4><p>Sprawdź internet i spróbuj ponownie. Możesz też iść dalej bez terminu: zaproponujemy go w wycenie.</p><button class="btn-line" type="button" style="width:auto;margin-top:4px">{ico("refresh-cw")}Spróbuj ponownie</button></div>''' + none_box(True), E3)
page("30-krok3-brak-terminow.html", "Step 3", "No free slot in the next 30 days: says so, the customer can still send.", 3, L3,
     photos() + f'''{SLOT_H}<div class="empty"><span class="big">{ico("calendar-x")}</span><h4>W najbliższych 30 dniach nie mamy wolnego terminu</h4><p>Wyślij zapytanie mimo to. Termin zaproponujemy w wycenie, a Ty zdecydujesz, czy Ci pasuje.</p></div>
<div class="field" style="margin-top:16px"><label for="when">Dni i godziny, które Ci pasują <span class="opt">(opcjonalnie)</span></label><div class="inp"><textarea id="when" rows="2" placeholder="np. po 17:00, najlepiej w piątki"></textarea></div></div>''', E3)
ONE = f'''{SLOT_H}<p class="sub-p">Mamy teraz jeden wolny termin. Zaznacz go albo napisz, kiedy Ci pasuje. Wizyta potrwa około <span data-bind="visit.durationLabel">3,5 godz.</span></p>
<fieldset><legend class="vh">Wolne terminy</legend><div class="slots"><div class="slot-g">{days_html([("pt. 11 gru", "", [("13:30", "")])], ("pt. 11 gru, 13:30",), False)}</div></div></fieldset>
<div class="field" style="margin-top:16px"><label for="when">Inne terminy, które Ci pasują <span class="opt">(opcjonalnie)</span></label><div class="inp"><textarea id="when" rows="2" placeholder="np. po 17:00, najlepiej w piątki"></textarea></div></div>{none_box()}'''
page("31-krok3-jeden-termin.html", "Step 3", "Only one free slot: one is enough, plus a free-text wish.", 3, L3, photos() + ONE, E3)
page("32-krok3-zaden-nie-pasuje.html", "Step 3", "“Żaden termin mi nie pasuje” ticked: slots switch off, optional free text; never blocks.", 3, L3, photos() + slots(none=True), E3)
page("33-krok3-blad-terminy.html", "Step 3", "Error: one time chosen, “Dalej” tapped.", 3, L3,
     photos() + slots(("czw. 19 lis, 10:00",), bad="Wybierz jeszcze jeden termin albo zaznacz „Żaden termin mi nie pasuje”."), E3)
TAKEN = notebox("warn", "triangle-alert", "<b>Termin śr. 18 lis, 13:30 właśnie zajął ktoś inny.</b> Wybierz inny w jego miejsce. Reszta formularza została bez zmian.", "alert") + '<div style="height:16px"></div>'
DAYS_REST_OLD = DAYS_REST
DAYS_REST = [d if d[0] != "śr. 18 lis" else ("śr. 18 lis", "", [("10:00", ""), ("16:00", "")]) for d in DAYS_REST]
page("34-krok3-termin-zajety.html", "Step 3", "Sent back from step 4: a chosen slot was taken before submit. The taken slot is gone, the other choice stays.", 3, L3,
     photos([photo("ok", 1), photo("ok", 2), photo("ok", 3)], 3) + slots(("czw. 19 lis, 10:00",), top=TAKEN), E3, label="Wróć do podsumowania")
DAYS_REST = DAYS_REST_OLD


# ------------------------------------------------------------------ step 4
L4 = "Ostatni krok. Nic nie wysyłamy, dopóki nie klikniesz „Wyślij zapytanie”."


def tfield(id_, label, value="", opt=False, hint="", bad="", type_="text", ac="", im="", ph="", dis=False):
    o = ' <span class="opt">(opcjonalnie)</span>' if opt else ""
    attrs = f' type="{type_}"' + (f' autocomplete="{ac}"' if ac else "") + (f' inputmode="{im}"' if im else "") + (f' placeholder="{ph}"' if ph else "")
    attrs += (' aria-invalid="true"' if bad else "") + ("" if opt else ' aria-required="true"') + (" disabled" if dis else "")
    desc = f' aria-describedby="{id_}-h"' if (hint or bad) else ""
    under = err(bad, id_ + "-h") if bad else (f'<p class="hint" id="{id_}-h">{hint}</p>' if hint else "")
    return f'<div class="field{" err" if bad else ""}"><label for="{id_}">{label}{o}</label><div class="inp"><input id="{id_}" value="{value}"{attrs}{desc}></div>{under}</div>'


def radios(name, legend, opts, chosen="", bad="", hint="", dis=False):
    cards = "".join(f'<label class="rc"><input type="radio" name="{name}"{" checked" if k == chosen else ""}{" disabled" if dis else ""}>{ico(ic)}<span>{lab}{"<small>" + sm + "</small>" if sm else ""}</span></label>' for k, lab, ic, sm in opts)
    under = err(bad) if bad else (f'<p class="hint">{hint}</p>' if hint else "")
    return f'<fieldset class="{"err" if bad else ""}"{" aria-invalid=true" if bad else ""}><legend class="legend">{legend}</legend><div class="cards2">{cards}</div>{under}</fieldset>'


def summary(items, place, place_sub, nphotos, times, est, pending=0, links=True):
    def chg(what):
        return f'<a class="chg" href="#" aria-label="Zmień: {what}">Zmień</a>' if links else ""
    it = "".join(f"<span>{i}</span>" for i in items)
    ph = "Bez zdjęć" if not nphotos else pl_photos(nphotos)
    ph_sub = f"<small>{pending} jeszcze się wysyła</small>" if pending else ("<small>Wycenimy z opisu. Zdjęcia możesz dosłać.</small>" if not nphotos else "")
    tm = "".join(f"<span>{t}</span>" for t in times) if times else "<span>Bez terminu</span><small>Zaproponujemy termin w wycenie.</small>"
    return f'''<div class="sumry">
<div class="r"><div><p class="k">Rzeczy</p><p class="v">{it}</p></div>{chg("rzeczy")}</div>
<div class="r"><div><p class="k">Miejsce</p><p class="v">{place}<small>{place_sub}</small></p></div>{chg("miejsce")}</div>
<div class="r"><div><p class="k">Zdjęcia</p><p class="v">{ph}{ph_sub}</p></div>{chg("zdjęcia")}</div>
<div class="r"><div><p class="k">Terminy</p><p class="v">{tm}</p></div>{chg("terminy")}</div>
<div class="r tot"><p class="k" style="margin:0">Szacunkowa cena</p><p class="v" data-bind="estimate.total">{amount(est)}</p><small>{FINE}</small></div></div>'''


CH = [("email", "E-mail", "mail", ""), ("wa", "WhatsApp", "message-circle", "")]
PAY = [("cash", "Gotówka", "banknote", "przy wizycie"), ("card", "Karta", "credit-card", "także BLIK")]
PAY_HINT = "Karta to także BLIK, Przelewy24, Apple Pay i Google Pay. Wybór możesz zmienić później, na stronie wyceny."
STORY_ITEMS = ["Pakiet Rodzinny", f"Dywan syntetyczny, 6{NB}m²"]
LEGAL = '<p class="legal">Wysyłając formularz, przekazujesz nam dane potrzebne do przygotowania wyceny. Zdjęcia do wyceny przechowujemy 12 miesięcy. Jak dbamy o dane i zdjęcia, opisuje <a href="/polityka-prywatnosci">polityka prywatności</a>.</p>'


def consent(checked=False, dis=False):
    return f'''<label class="ck"><input type="checkbox"{" checked" if checked else ""}{" disabled" if dis else ""}><span class="tx">Chcę dostawać od Nowiutko porady i oferty e-mailem <span class="opt">(opcjonalnie)</span><small>Potwierdzisz to jednym kliknięciem w e-mailu. Możesz zrezygnować w każdej chwili.</small></span></label>'''


def step4(ch="email", v=None, bad=None, pay="", top="", dis=False, pending=0, times=TWO, nphotos=3, mk=False):
    v, bad = v or {}, bad or {}
    f = tfield("name", "Imię", v.get("name", ""), ac="given-name", bad=bad.get("name", ""), dis=dis)
    f += radios("channel", "Jak wysłać Ci wycenę?", CH, ch, hint="Na ten adres lub numer wyślemy link do wyceny.", dis=dis)
    em = tfield("email", "E-mail", v.get("email", ""), type_="email", ac="email", im="email", ph="ty@example.com", bad=bad.get("email", ""), dis=dis,
                opt=(ch == "wa"), hint="Przyślemy na niego potwierdzenie zapytania." if ch == "wa" else "")
    tel = tfield("tel", "Telefon", v.get("tel", ""), type_="tel", ac="tel", im="tel", ph="+48 000 000 000", bad=bad.get("tel", ""), dis=dis,
                 opt=(ch == "email"), hint="Przyda się w dniu wizyty, gdybyśmy musieli zadzwonić." if ch == "email" else "Numer, na którym masz WhatsApp.")
    f += (em + tel) if ch == "email" else (tel + em)
    f += tfield("addr", "Ulica i numer", v.get("addr", ""), opt=True, ac="street-address", hint="Możesz też podać przy potwierdzeniu wyceny.", dis=dis)
    p = radios("pay", "Jak wolisz zapłacić?", PAY, pay, bad=bad.get("pay", ""), hint=PAY_HINT, dis=dis)
    return f'''{top}<div class="form"><div class="panel">{f}</div><div class="panel">{p}</div></div>
<h3 class="sub-h">Podsumowanie</h3>{summary(STORY_ITEMS, "Swarzędz", "Dojazd gratis", nphotos, times, E3, pending, links=not dis)}
<div style="margin-top:16px">{consent(mk, dis)}</div>{LEGAL}'''


SEND = "Wyślij zapytanie"
FILLED = dict(name="Kasia", email="kasia@example.com", tel="", addr="")
page("35-krok4-pusty.html", "Step 4", "Step 4, empty: “E-mail” preselected, so e-mail is required and phone optional. Consent unticked.", 4, L4, step4(), E3, label=SEND)
page("36-krok4-email-wypelniony.html", "Step 4", "Filled, channel e-mail, payment chosen; summary with “Zmień” per row; one photo still uploading.", 4, L4,
     step4("email", FILLED, pay="cash", pending=1), E3, label=SEND)
page("37-krok4-whatsapp.html", "Step 4", "Channel WhatsApp: phone moves up and becomes required, e-mail becomes optional.", 4, L4,
     step4("wa", dict(name="Kasia", tel="+48 500 000 000"), pay="card"), E3, label=SEND)
page("38-krok4-bledy.html", "Step 4", "Errors after “Wyślij zapytanie”: name empty, e-mail malformed, optional phone malformed, payment not chosen.", 4, L4,
     step4("email", dict(email="kasia@example", tel="500 00"), bad=dict(name="Wpisz imię.", email="Sprawdź adres e-mail. Powinien wyglądać tak: ty@example.com.", tel="Wpisz numer w formacie +48 000 000 000 albo zostaw pole puste.", pay="Wybierz, jak wolisz zapłacić.")), E3, label=SEND)
page("39-krok4-wysylanie.html", "Step 4", "Sending: fields locked, button busy, a second tap does nothing.", 4, L4,
     step4("email", FILLED, pay="cash", dis=True), E3, label=SEND, state="busy")
FAIL = notebox("err", "wifi-off", "<b>Nie udało się wysłać zapytania.</b> Sprawdź internet i spróbuj ponownie. Formularz i zdjęcia zostały, niczego nie trzeba wpisywać od nowa.", "alert") + '<div style="height:16px"></div>'
page("40-krok4-blad-wysylki.html", "Step 4", "Sending failed (network): alert on top of the step, form kept, button becomes “Spróbuj ponownie”.", 4, L4,
     step4("email", FILLED, pay="cash", top=FAIL), E3, label="Spróbuj ponownie")


# ------------------------------------------------------------------ thank-you (same page, form replaced)
def thanks(fname, note, channel_line, times, nphotos, mail=True, eta="jeszcze dziś"):
    FRAMES.append((fname, "After sending", note))
    held = ("Wstępnie trzymamy dla Ciebie wybrane terminy." if times else "")
    conf = '<p class="fine">Potwierdzenie zapytania wysłaliśmy na <b data-bind="enquiry.email">kasia@example.com</b>. Nie widzisz go? Sprawdź spam.</p>' if mail else ""
    doc = f'''<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#F5FAF8">
<title>Dziękujemy, mamy Twoje zapytanie | Nowiutko</title>
<link rel="stylesheet" href="../stroller/base.css"><link rel="stylesheet" href="quote.css"><style>{FOOT_CSS}</style></head>
<body class="no-bar">
<!-- Frame: {fname} · {e(note)} · SAMPLE DATA, static state -->
{HEADER}
<main class="q solo wrap"><div class="q-main">
<h1 class="eyebrow">Wycena prania ze zdjęć · Poznań i okolice</h1>
<div class="ty">
<span class="big">{ico("check")}</span>
<div class="step-h" style="margin:0"><h2 id="krok" tabindex="-1">Dziękujemy. Mamy Twoje zapytanie.</h2><p class="lede">Wycenę wyślemy <b data-bind="quoteEta">{eta}</b>, {channel_line}.</p></div>
<div><h3 class="sub-h" style="margin-top:0;margin-bottom:14px">Co teraz?</h3><ol class="next">
<li><div><b>Oglądamy zdjęcia i liczymy cenę</b><span>{"Sprawdzamy rzeczy na zdjęciach i podajemy wiążącą cenę." if nphotos else "Liczymy cenę z Twojego opisu. Zdjęcia możesz jeszcze dosłać."}</span></div></li>
<li><div><b>Dostajesz wycenę z terminem</b><span>Link do wyceny przyjdzie {channel_line}.</span></div></li>
<li><div><b>Potwierdzasz jednym kliknięciem</b><span>Dopiero wtedy termin jest zarezerwowany. Do tego czasu nic nie płacisz.</span></div></li></ol></div>
<div><h3 class="sub-h" style="margin-top:0;margin-bottom:10px">Twoje zapytanie</h3>{summary(STORY_ITEMS, "Swarzędz", "Dojazd gratis", nphotos, times, E3, links=False)}{f'<p class="hint">{held}</p>' if held else ""}</div>
{conf}
<div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn btn-ghost" href="/poznan/pranie-wozkow-i-fotelikow" data-bind="source.page">Wróć na stronę o praniu wózków</a></div>
{DOORS.replace("Wolisz inaczej?", "Masz pytanie?")}
</div></div></main>
{FOOTER}
</body></html>'''
    (HERE / fname).write_text(doc.replace('.sumry .tot .v"', '.x"').replace('<p class="v" data-bind="estimate.total">', '<p class="v hl" data-bind="estimate.total">'), encoding="utf-8")


thanks("41-dziekujemy.html", "Thank-you, channel e-mail: what happens now, estimate repeated, times held, confirmation e-mail.", "e-mailem", TWO, 3)
thanks("42-dziekujemy-whatsapp-bez-terminu.html", "Thank-you variant: WhatsApp, no photos, no time, sent after working hours (“jutro rano”).", "na WhatsApp", (), 0, mail=False, eta="jutro rano")

# ------------------------------------------------------------------ review board
cards = "".join(f'<figure><iframe src="{f}" loading="lazy" title="{e(n)}"></iframe><figcaption><a href="{f}"><b>{f}</b></a><br>{e(n)}</figcaption></figure>' for f, g, n in FRAMES)
(HERE / "index.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quote form — review board</title><style>
body{{margin:0;padding:24px;font:15px/1.5 system-ui,sans-serif;background:#eef1f0;color:#12302B}}h1{{margin:0 0 4px}}p{{max-width:80ch}}
.g{{display:flex;flex-wrap:wrap;gap:28px;margin-top:24px}}figure{{margin:0;width:390px}}iframe{{width:390px;height:844px;border:1px solid #c5d3ce;border-radius:12px;background:#fff}}
figcaption{{margin-top:8px;font-size:13.5px}}</style></head><body>
<h1>Quote form, /poznan/wycena</h1><p>Draft for <code>quote-form-v1</code>. Each frame is a static state at 390 × 844; open any file at 1440 for the desktop layout (form left, estimate card right). Sample data only.</p>
<div class="g">{cards}</div></body></html>""", encoding="utf-8")
print(f"{len(FRAMES)} frames written")
