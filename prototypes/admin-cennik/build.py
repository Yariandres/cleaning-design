#!/usr/bin/env python3
"""Builds the static frames for the admin shell + "Cennik i ustawienia" (handover draft admin-cennik-v1).

Run: python3 prototypes/admin-cennik/build.py
Needs the Lucide icon data (same source the developer uses):
  ../cleaning-sell-system/node_modules/@iconify-json/lucide/icons.json  (or LUCIDE_JSON=/path)
All names, prices, minutes and counts are SAMPLE DATA from docs/source/price-list.md; in the app they come
from the database. Frames are static: each file is one state.
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
INV = ' aria-invalid="true"'
OTC = ' autocomplete="one-time-code"'
FRAMES = []  # (file, group, note)

# ------------------------------------------------------------------ shell
NAV = [("Dziś", "list-checks", "dzis"), ("Lejek", "square-kanban", "lejek"), ("Kalendarz", "calendar-days", "kalendarz"),
       ("Klienci", "users", "klienci"), ("Cennik i ustawienia", "sliders-horizontal", "cennik"), ("Raport", "chart-column", "raport")]


def tabbar(active="wiecej"):
    out = ['<nav class="tabbar" aria-label="Główna nawigacja">']
    for label, icon, key in NAV[:4]:
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'<a href="#"{cur}><span class="pill">{ico(icon)}</span>{label}</a>')
    cur = ' class="cur"' if active == "wiecej" else ""
    out.append(f'<a href="02-shell-wiecej.html"{cur} aria-haspopup="dialog"><span class="pill">{ico("menu")}</span>Więcej</a>')
    out.append("</nav>")
    return "".join(out)


def sidebar(active="cennik"):
    out = ['<nav class="sidebar" aria-label="Główna nawigacja"><div class="brandline"><img src="../stroller/assets/mark.svg" alt="">Nowiutko</div>']
    for label, icon, key in NAV:
        cur = ' aria-current="page"' if key == active else ""
        href = "03-index.html" if key == "cennik" else "#"
        out.append(f'<a href="{href}"{cur}>{ico(icon)}{label}</a>')
    out.append(f'<a href="#" class="end">{ico("log-out")}Wyloguj</a></nav>')
    return "".join(out)


def savebar(state="dirty", label="Zapisz"):
    st = {
        "clean": ('<p class="st">Brak zmian do zapisania.</p>', f'<button class="btn-main" disabled>{label}</button>'),
        "dirty": ('<p class="st dirty">Niezapisane zmiany. Zapis od razu zmienia stronę.</p>', f'<button class="btn-main">{label}</button>'),
        "saving": ('<p class="st" role="status">Zapisuję…</p>', f'<button class="btn-main busy" aria-busy="true" disabled style="background:var(--p600);color:#fff">{ico("loader-circle","spin")}Zapisuję…</button>'),
        "invalid": (f'<p class="st bad" role="alert">Popraw zaznaczone pola, żeby zapisać.</p>', f'<button class="btn-main">{label}</button>'),
        "failed": (f'<p class="st bad" role="alert">Nie zapisano. Na stronie jest nadal stara wersja.</p>', f'<button class="btn-main">{ico("refresh-cw")}Spróbuj ponownie</button>'),
    }[state]
    return f'<div class="savebar"><div class="in">{st[0]}{st[1]}</div></div>'


def toast(strong="Zapisano.", text="Zmiana jest już na stronie.", link="Zobacz"):
    a = f'<a href="#">{link}</a>' if link else ""
    return f'<div class="toast" role="status">{ico("circle-check")}<p><b>{strong}</b>{text}</p>{a}</div>'


def page(fname, group, note, title, body, bottom="tabs", save="dirty", overlay="", extra="", active="wiecej", shell=True, raw=False):
    FRAMES.append((fname, group, note))
    if raw:
        inner = body
    else:
        cls = "screen has-save" if bottom == "save" else "screen"
        inner = f'<main class="{cls}">{body}</main>'
    bar = ""
    if bottom == "tabs":
        bar = tabbar(active)
    elif bottom == "save":
        bar = savebar(save)
    elif bottom == "save+split":
        bar = savebar(save)
    doc = f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#F5FAF8">
<title>{e(title)} · Nowiutko admin</title>
<link rel="stylesheet" href="admin.css"></head>
<body>
<!-- Frame: {fname} · {e(note)} · SAMPLE DATA, static state -->
{sidebar() if shell else ""}{inner}{extra}{bar}{overlay}
</body></html>"""
    (HERE / fname).write_text(doc, encoding="utf-8")


def top(back=None, back_href="03-index.html", act=""):
    left = f'<a class="back" href="{back_href}">{ico("chevron-left")}{back}</a>' if back else f'<div class="brandline"><img src="../stroller/assets/mark.svg" alt="">Nowiutko</div>'
    return f'<header class="top">{left}{act}</header>'


def head(title, sub="", eyebrow=""):
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    sb = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<div class="head">{eb}<h1 class="title">{title}</h1>{sb}</div>'


_id = [0]


def field(label, value="", suffix=None, hint=None, error=None, optional=False, placeholder="", inputmode=None, short=False,
          kind="input", options=None, disabled=False, count=None, rows=3, autocomplete="off", type_="text"):
    _id[0] += 1
    i = f"f{_id[0]}"
    opt = ' <span class="opt">(opcjonalnie)</span>' if optional is True else ""
    if optional == "hint":
        hint = "Opcjonalnie." + (" " + hint if hint else "")
    cnt = f'<span class="count num">{count}</span>' if count else ""
    dis = " disabled" if disabled else ""
    desc = []
    if hint: desc.append(f"{i}h")
    if error: desc.append(f"{i}e")
    aria = (f' aria-describedby="{" ".join(desc)}"' if desc else "") + (' aria-invalid="true"' if error else "")
    cls = "inp" + (" has-suf" if suffix else "") + (" short" if short else "") + (" sel" if kind == "select" else "")
    if kind == "select":
        opts = "".join(f'<option{" selected" if o == value else ""}>{e(o)}</option>' for o in options)
        ctl = f'<select id="{i}"{aria}{dis}>{opts}</select>'
    elif kind == "textarea":
        ctl = f'<textarea id="{i}" rows="{rows}"{aria}{dis}>{e(value)}</textarea>'
    else:
        im = f' inputmode="{inputmode}"' if inputmode else ""
        ph = f' placeholder="{e(placeholder)}"' if placeholder else ""
        ctl = f'<input id="{i}" type="{type_}" value="{e(value)}"{im}{ph}{aria}{dis} autocomplete="{autocomplete}">'
    suf = f'<span class="suf">{suffix}</span>' if suffix else ""
    h = f'<p class="hint" id="{i}h">{hint}</p>' if hint else ""
    er = f'<p class="errmsg" id="{i}e" role="alert">{ico("circle-alert")}{error}</p>' if error else ""
    return f'<div class="field{" err" if error else ""}"><label for="{i}">{label}{opt}{cnt}</label><div class="{cls}">{ctl}{suf}</div>{er}{h}</div>'


def switch(label, small="", on=True, disabled=False):
    _id[0] += 1
    return (f'<label class="sw-row"><span class="t"><b>{label}</b>{f"<small>{small}</small>" if small else ""}</span>'
            f'<input class="sw" type="checkbox" role="switch"{" checked" if on else ""}{" disabled" if disabled else ""}></label>')


def seg(legend, name, options, checked, error=None):
    labs = "".join(f'<label><input type="radio" name="{name}"{" checked" if o == checked else ""}>{o}</label>' for o in options)
    er = f'<p class="errmsg" role="alert">{ico("circle-alert")}{error}</p>' if error else ""
    return f'<fieldset><legend class="legend">{legend}</legend><div class="seg">{labs}</div>{er}</fieldset>'


def note(text, kind="", icon="info"):
    return f'<p class="note {kind}">{ico(icon)}<span>{text}</span></p>'


def row(name, meta="", val="", href="#", cls="", badge="", icon=None, icon_cls="", go=True):
    ic = f'<span class="ic {icon_cls}">{ico(icon)}</span>' if icon else ""
    m = f'<span class="meta">{meta}</span>' if meta else ""
    v = f'<span class="val num">{val}</span>' if val else ""
    g = ico("chevron-right", "go") if go else ""
    return f'<li><a class="row {cls}" href="{href}">{ic}<span class="main"><span class="name">{name}{" " + badge if badge else ""}</span>{m}</span>{v}{g}</a></li>'


def card(rows):
    return f'<ul class="card">{"".join(rows)}</ul>'


def group(title, right=""):
    return f'<div class="group-h"><h2>{title}</h2><span>{right}</span></div>'


HIDDEN = f'<span class="badge">{ico("eye-off")}Ukryta</span>'
PROTO = '<p class="proto">Prototyp: dane przykładowe z cennika. W aplikacji pochodzą z bazy.</p>'

# ------------------------------------------------------------------ sample data (docs/source/price-list.md)
SERVICES = [
    ("Dziecko", [
        ("Wózek spacerowy", "Siedzisko, budka, kosz, stelaż i koła", "90", "szt.", 45),
        ("Wózek 2w1 (gondola i spacerówka)", "Gondola, spacerówka, stelaż i koła", "120", "szt.", 60),
        ("Wózek 3w1 (z fotelikiem)", "Gondola, spacerówka, fotelik, stelaż", "160", "szt.", 80),
        ("Wózek bliźniaczy", "Oba siedziska, budki, stelaż i koła", "150", "szt.", 80),
        ("Fotelik samochodowy", "Pokrowiec i skorupa, pasy powierzchniowo", "80", "szt.", 40),
        ("Krzesełko, leżaczek lub mata", "Pokrowiec i elementy z tkaniny", "60", "szt.", 30),
    ]),
    ("Meble tapicerowane", [
        ("Fotel", "Siedzisko, oparcie i podłokietniki", "90", "szt.", 30),
        ("Krzesło tapicerowane", "Siedzisko i oparcie", "25", "szt.", 10),
        ("Kanapa 2-osobowa", "Odkurzanie i pranie ekstrakcyjne", "150", "szt.", 60),
        ("Kanapa 3-osobowa", "Odkurzanie i pranie ekstrakcyjne", "180", "szt.", 75),
        ("Narożnik", "Odkurzanie i pranie ekstrakcyjne", "260", "szt.", 100),
    ]),
    ("Materace", [
        ("Materac pojedynczy", "Jedna strona", "100", "szt.", 40),
        ("Materac podwójny", "Jedna strona", "150", "szt.", 50),
    ]),
    ("Dywany", [
        ("Dywan syntetyczny", "Odkurzanie i pranie ekstrakcyjne", "18", "m²", 6),
        ("Dywan wełniany", "Łagodny środek do wełny", "25", "m²", 8),
        ("Wykładzina dywanowa", "Pranie na miejscu", "9", "m²", 4),
    ]),
    ("Auto", [
        ("Pranie jednego fotela", "Siedzisko i oparcie", "80", "szt.", 30),
        ("Pranie tapicerki (5 miejsc)", "Fotele i kanapa", "260", "szt.", 120),
        ("Kompleksowe czyszczenie wnętrza", "Tapicerka, plastiki, szyby, dywaniki", "350", "szt.", 180),
        ("Czyszczenie i konserwacja skóry", "Fotele i kanapa ze skóry", "160", "szt.", 90),
        ("Ozonowanie", "Usuwanie zapachów", "80", "szt.", 30),
    ]),
]
OFF = {"Wykładzina dywanowa"}
PACKS = [
    ("Nowy Członek Rodziny", "319", "350", ["Materac podwójny", "Wózek 2w1", "Fotelik samochodowy"], ("przed porodem", "mint"), False),
    ("Rodzinny", "339", "380", ["Kanapa 3-osobowa", "Wózek 2w1", "Fotelik samochodowy"], None, True),
    ("Odświeżenie Domu", "450", "510", ["Kanapa 3-osobowa", "Materac podwójny", "Fotel × 2"], None, False),
    ("Auto i Maluch", "409", "460", ["Pranie tapicerki (5 miejsc)", "Fotelik samochodowy", "Wózek 2w1"], ("auto i maluch", "mint"), False),
    ("Cała Rodzina", "699", "790", ["Kanapa 3-osobowa", "Materac podwójny", "Pranie tapicerki", "Wózek 2w1", "Fotelik"], None, False),
    ("Dom", "569", "640", ["Narożnik", "Wózek 2w1", "Pranie tapicerki (5 miejsc)"], None, False),
]
ADDONS = [
    ("Impregnacja tkaniny", "+30%", "procent ceny pozycji"),
    ("Mocne zabrudzenia, sierść lub mocz", "+20–30%", "wyceniane ze zdjęć"),
    ("Druga strona materaca", "+50%", "procent ceny pozycji"),
    ("SUV, 7 miejsc lub van", "+20%", "procent ceny pozycji"),
    ("Zabieg antyalergiczny", "+20 zł", "za pozycję"),
    ("Wieczór lub weekend", "+15%", "procent ceny wizyty"),
]
Z1 = [("Poznań", "60-001 … 61-896"), ("Suchy Las", "62-002"), ("Swarzędz", "62-020"), ("Luboń", "62-030"), ("Komorniki", "62-052"),
      ("Plewiska", "62-064"), ("Skórzewo", "60-185"), ("Tarnowo Podgórne", "62-080"), ("Rokietnica", "62-090"), ("Czerwonak", "62-004")]
Z2 = [("Kórnik", "62-035"), ("Mosina", "62-050"), ("Puszczykowo", "62-040, 62-041"), ("Dopiewo", "62-070"), ("Murowana Goślina", "62-095"),
      ("Pobiedziska", "62-010"), ("Buk", "64-320"), ("Stęszew", "62-060"), ("Kleszczewo", "63-005")]
FAQ = [
    "Ile kosztuje pranie wózka dziecięcego?", "Ile kosztuje pranie fotelika samochodowego?", "Jak pierzecie foteliki Cybex czy Maxi-Cosi?",
    "Czy środki są bezpieczne dla niemowlęcia?", "Kiedy wózek będzie gotowy?", "Czy usuniecie pleśń z gondoli?", "Czy czyścicie też stelaż i koła?",
]


def pchip(v, sel=False):
    return f'<span class="pchip{" sel" if sel else ""}" contenteditable="false">{ico("tag")}{v}</span>'


# ------------------------------------------------------------------ 01–03 shell + index
def index_body():
    b = top() + head("Cennik i ustawienia", "Każda zmiana po zapisaniu jest od razu na stronie.", "Poznań")
    b += card([row(f'Teraz w sezonie', 'Wózek 2w1 · „Przed wiosennymi spacerami”', href="30-sezon.html", icon="sun", icon_cls="sun")])
    b += group("Oferta")
    b += card([
        row("Usługi", "21 pozycji w 5 grupach · 1 ukryta", href="04-uslugi-lista.html", icon="tag"),
        row("Pakiety", "6 pakietów · 1 wyróżniony", href="14-pakiety-lista.html", icon="package"),
        row("Dopłaty", "6 dopłat", href="17-doplaty-lista.html", icon="percent"),
    ])
    b += group("Dojazd")
    b += card([
        row("Strefy", "3 strefy · Strefa 1 gratis", href="19-strefy-lista.html", icon="route"),
        row("Miejscowości", "19 miejscowości", href="21-miejscowosci-lista.html", icon="map-pin"),
    ])
    b += group("Czas pracy")
    b += card([
        row("Godziny pracy", "Pon.–sob. · niedziela zamknięte", href="25-godziny.html", icon="clock"),
        row("Dni rejonowe", "Jeszcze nie ustawione", href="23-dni-rejonowe-puste.html", icon="calendar-range"),
    ])
    b += group("Strona i firma")
    b += card([
        row("FAQ", "1 strona · 7 pytań", href="27-faq-lista.html", icon="message-circle-question-mark"),
        row("Firma", "Telefon, WhatsApp, minimum zamówienia, limity", href="26-firma.html", icon="store"),
    ])
    return b


page("01-shell-tabbar.html", "Shell", "Shell on a phone: 4 daily tabs + Więcej. Content area of Dziś is out of scope (placeholder).",
     "Dziś", top() + head("Dziś", "", "") + '<p class="proto">Ekran „Dziś” jest poza zakresem tego projektu. Ta ramka pokazuje tylko nawigację: cztery codzienne ekrany i „Więcej”.</p>',
     active="dzis")

more = f"""<div class="overlay"><div class="sheet" role="dialog" aria-modal="true" aria-labelledby="mt"><h2 id="mt">Więcej</h2>
<ul>{row("Cennik i ustawienia", "Ceny, pakiety, dojazd, godziny, FAQ", href="03-index.html", icon="sliders-horizontal")}
{row("Raport", "Źródła, zapytania, przychód", icon="chart-column")}</ul>
<div class="acts"><a class="btn-text" href="#">{ico("log-out")}Wyloguj</a></div></div></div>"""
page("02-shell-wiecej.html", "Shell", "Więcej sheet (UDrawer): Cennik i ustawienia, Raport, Wyloguj.",
     "Więcej", top() + head("Dziś") + '<p class="proto">Ekran „Dziś” jest poza zakresem tego projektu.</p>', overlay=more, active="dzis")
page("03-index.html", "Index", "Section index: 9 sections in 4 groups + Teraz w sezonie on top (the one sun highlight).", "Cennik i ustawienia", index_body())


# ------------------------------------------------------------------ 04–13 services
def services_list(reorder=False, flash=None, loading=False):
    act = (f'<a class="act on" href="04-uslugi-lista.html">Gotowe</a>' if reorder
           else f'<a class="act" href="05-uslugi-kolejnosc.html">{ico("arrow-up-down")}Kolejność</a>')
    b = top("Cennik i ustawienia", act=act)
    b += head("Usługi", "Kolejność tutaj to kolejność na stronie." if reorder else "20 na stronie · 1 ukryta")
    if reorder:
        b += f'<p class="status" role="status">{ico("circle-check")}Kolejność zapisana. Już widać ją na stronie.</p>'
    for g, items in SERVICES:
        b += group(g, f"{len(items)}")
        rows = []
        for n, (name, inc, price, unit, mins) in enumerate(items):
            off = name in OFF
            if reorder:
                up = f'<button aria-label="Przesuń wyżej: {e(name)}"{" disabled" if n == 0 else ""}>{ico("arrow-up")}</button>'
                dn = f'<button aria-label="Przesuń niżej: {e(name)}"{" disabled" if n == len(items) - 1 else ""}>{ico("arrow-down")}</button>'
                rows.append(f'<li class="row{" off" if off else ""}"><span class="pos num">{n + 1}</span><span class="main"><span class="name">{name}{" " + HIDDEN if off else ""}</span></span><span class="ord">{up}{dn}</span></li>')
            else:
                u = "m²" if unit == "m²" else "szt."
                meta = f"{mins} min / m²" if unit == "m²" else f"{mins} min"
                href = "06-usluga-edycja.html" if name == "Wózek spacerowy" else ("12-usluga-ukryta-usun.html" if off else "#")
                val = f'<small>od</small> {price} zł<small> / {u}</small>' if unit == "m²" else f'<small>od</small> {price} zł'
                if flash == name:
                    val = '<small>od</small> 95 zł'
                rows.append(row(name, meta, val, href=href, cls=("off" if off else "") + (" flash" if flash == name else ""), badge=HIDDEN if off else ""))
        b += card(rows)
    if not reorder:
        b += f'<a class="add" href="#" style="margin-top:20px">{ico("plus")}Dodaj usługę</a>'
    return b + PROTO


page("04-uslugi-lista.html", "Usługi", "List: 21 items in 5 groups, hidden entry stays in place (dimmed + badge). Full height.", "Usługi", services_list())
page("05-uslugi-kolejnosc.html", "Usługi", "Reorder mode: up/down buttons per row, saved on each move, 'Gotowe' leaves the mode.", "Kolejność usług", services_list(reorder=True))


def service_edit(name="Wózek spacerowy", inc="Siedzisko, budka, kosz, stelaż i koła", price="95", mins="45", errors=False, disabled=False,
                 used='<b>Używane w:</b> FAQ wózków (1 odpowiedź), 12 wycen.', grp="Dziecko", unit="sztukę", on=True, hide_warn=False, deletable=False, fail=False):
    b = top("Usługi", "04-uslugi-lista.html")
    b += head(name if not errors else "Wózek spacerowy", "", "Usługi · " + grp)
    if fail:
        b += note("<b>Nie udało się zapisać.</b> Na stronie jest nadal stara cena. Sprawdź internet i spróbuj ponownie. Twoje zmiany zostają w formularzu.", "err", "triangle-alert").replace('class="note', 'role="alert" class="note') + '<div style="height:16px"></div>'
    f = '<div class="panel">'
    f += field("Nazwa", "" if errors else name, error="Wpisz nazwę." if errors else None, disabled=disabled)
    f += field("Grupa", grp, kind="select", options=[g for g, _ in SERVICES], disabled=disabled)
    f += field("Co jest w cenie", inc, count=f"{len(inc)}/60", hint="Jedna krótka linijka pod nazwą w cenniku.", disabled=disabled)
    f += '<div class="pair">'
    f += field("Cena od", "0" if errors else price, suffix="zł", inputmode="decimal", error="Cena musi być większa niż 0 zł." if errors else None, disabled=disabled)
    f += field("Czas wizyty" if unit == "sztukę" else "Czas na 1 m²", mins, suffix="min", inputmode="numeric", disabled=disabled)
    f += '</div>'
    f += seg("Cena liczona za", "unit", ["sztukę", "m²"], unit)
    f += '</div><div class="panel" style="gap:12px">'
    f += switch("Widoczna na stronie", "Wyłączona znika z cennika i formularza wyceny. Stare wyceny jej nie tracą.", on=on, disabled=disabled)
    if hide_warn:
        f += note("<b>Ta usługa jest w 5 pakietach.</b> Po ukryciu zniknie z cennika pojedynczych usług. Pakiety zostają na stronie bez zmian.", "warn", "triangle-alert")
    f += note(used, "", "link")
    f += '</div>'
    if deletable:
        f += f'<a class="btn-text danger" href="13-usun-potwierdzenie.html">{ico("trash-2")}Usuń usługę</a>'
    else:
        f += '<p class="hint" style="margin:0 4px">Tej usługi nie można usunąć, bo jest w wycenach. Możesz ją ukryć.</p>'
    return b + f'<form class="form">{f}</form>'


page("06-usluga-edycja.html", "Usługi", "Edit a service: price changed 90 → 95, dirty save bar, 'Używane w' hint, off-not-delete.", "Wózek spacerowy", service_edit(), bottom="save")
page("07-usluga-bledy.html", "Usługi", "Errors after tapping Zapisz: required name empty, price 0.", "Wózek spacerowy", service_edit(errors=True), bottom="save", save="invalid")
page("08-usluga-zapisywanie.html", "Usługi", "Saving: fields locked, button busy.", "Wózek spacerowy", service_edit(disabled=True), bottom="save", save="saving")
page("09-uslugi-zapisano.html", "Usługi", "Saved: back on the list, row flashes with the new price, toast says it is live with a link to the page.", "Usługi",
     services_list(flash="Wózek spacerowy"), extra=toast("Zapisano.", "Nowa cena jest już na stronie."))
page("10-usluga-blad-zapisu.html", "Usługi", "Save failed (server/network): alert on top, form keeps the changes, retry in the bar.", "Wózek spacerowy", service_edit(fail=True), bottom="save", save="failed")
unsaved = f"""<div class="overlay"><div class="sheet" role="alertdialog" aria-modal="true" aria-labelledby="ut" aria-describedby="ud"><h2 id="ut">Masz niezapisane zmiany</h2>
<p class="lead" id="ud">Cena „Wózek spacerowy” jest zmieniona z 90 zł na 95 zł, ale jeszcze nie zapisana. Na stronie jest nadal 90 zł.</p>
<div class="acts"><button class="btn-main">Zapisz zmiany</button><button class="btn-sec">Odrzuć zmiany</button><button class="btn-text">Wróć do edycji</button></div></div></div>"""
page("11-niezapisane-zmiany.html", "Usługi", "Leaving with unsaved changes (back, tab, browser back): Zapisz / Odrzuć / Wróć.", "Wózek spacerowy", service_edit(), bottom="save", overlay=unsaved)
page("12a-usluga-ukrywanie-uzywana.html", "Usługi", "Switching off an item used in packages: warning before saving; delete not offered.", "Wózek 2w1",
     service_edit("Wózek 2w1 (gondola i spacerówka)", "Gondola, spacerówka, stelaż i koła", "120", "60", on=False, hide_warn=True,
                  used="<b>Używane w:</b> 5 pakietów (Rodzinny, Nowy Członek Rodziny, Auto i Maluch, Cała Rodzina, Dom), FAQ wózków, 31 wycen."), bottom="save")
page("12-usluga-ukryta-usun.html", "Usługi", "Hidden, never-used entry: delete is offered.", "Wykładzina dywanowa",
     service_edit("Wykładzina dywanowa", "Pranie na miejscu", "9", "4", grp="Dywany", unit="m²", on=False, deletable=True,
                  used="<b>Jeszcze nieużywana:</b> nie ma jej w żadnej wycenie, pakiecie ani odpowiedzi FAQ."), bottom="save", save="clean")
delete = f"""<div class="overlay"><div class="sheet" role="alertdialog" aria-modal="true" aria-labelledby="dt" aria-describedby="dd"><h2 id="dt">Usunąć „Wykładzina dywanowa”?</h2>
<p class="lead" id="dd">Usługa zniknie z cennika na stałe. Tego nie da się cofnąć. Jeśli chcesz ją tylko schować, zostaw ją ukrytą.</p>
<div class="acts"><button class="btn-danger">{ico("trash-2")}Usuń na stałe</button><button class="btn-text">Anuluj</button></div></div></div>"""
page("13-usun-potwierdzenie.html", "Usługi", "Delete confirmation (UModal/UDrawer), only for never-used entries.", "Wykładzina dywanowa",
     service_edit("Wykładzina dywanowa", "Pranie na miejscu", "9", "4", grp="Dywany", unit="m²", on=False, deletable=True,
                  used="<b>Jeszcze nieużywana.</b>"), bottom="save", save="clean", overlay=delete)

# ------------------------------------------------------------------ 14–16 packages
b = top("Cennik i ustawienia", act=f'<a class="act" href="#">{ico("arrow-up-down")}Kolejność</a>') + head("Pakiety", "6 na stronie")
rows = []
for name, price, was, items, tag, hi in PACKS:
    badges = ""
    if hi: badges += f'<span class="badge ok">{ico("star")}Wyróżniony</span> '
    if tag: badges += f'<span class="badge {tag[1]}">{tag[0]}</span>'
    rows.append(row(name, f'{len(items)} pozycje{" · " if badges else ""}{badges}' if len(items) < 5 else f'{len(items)} pozycji', f'{price} zł<s>{was} zł</s>',
                    href="15-pakiet-edycja.html" if name == "Rodzinny" else "#"))
b += '<div style="height:4px"></div>' + card(rows) + f'<a class="add" href="#">{ico("plus")}Dodaj pakiet</a>' + PROTO
page("14-pakiety-lista.html", "Pakiety", "Packages list: price, struck 'was' price, tag, highlighted badge.", "Pakiety", b)


def pack_edit(no_items=False):
    b = top("Pakiety", "14-pakiety-lista.html") + head("Rodzinny", "", "Pakiety")
    f = '<div class="panel">' + field("Nazwa", "Rodzinny")
    f += '<div class="pair">' + field("Cena pakietu", "339", suffix="zł", inputmode="decimal")
    f += field("Cena przed", "380", suffix="zł", inputmode="decimal", optional="hint") + '</div>'
    if not no_items:
        f += f'<p class="hint" style="margin-top:-8px">Na stronie „Cena przed” jest przekreślona. Suma pozycji osobno: <b class="num">380 zł</b>. Klient oszczędza 41 zł (11%).</p>'
    f += '</div><fieldset class="panel" style="gap:8px"><legend class="vh">Pozycje w pakiecie</legend><h2 aria-hidden="true">Co jest w pakiecie</h2>'
    if no_items:
        f += f'<p class="errmsg" role="alert" style="margin:0">{ico("circle-alert")}Dodaj co najmniej jedną pozycję.</p>'
    else:
        f += '<div>'
        for n, p, q in [("Kanapa 3-osobowa", "180", 1), ("Wózek 2w1 (gondola i spacerówka)", "120", 1), ("Fotelik samochodowy", "80", 1)]:
            f += (f'<div class="item"><span class="main"><span class="name">{n}</span><span class="meta num">{p} zł za szt.</span></span>'
                  f'<span class="step"><button type="button" aria-label="Mniej: {n}">{ico("trash-2") if q == 1 else ico("minus")}</button><output aria-label="Ilość">{q}</output>'
                  f'<button type="button" aria-label="Więcej: {n}">{ico("plus")}</button></span></div>')
        f += '</div><p class="sum"><span>Osobno razem</span><span class="num">380 zł</span></p>'
    f += f'<a class="add" href="#" style="margin-top:8px">{ico("plus")}Dodaj pozycję</a></fieldset>'
    f += '<div class="panel">' + field("Etykieta", "", optional=True, placeholder="np. przed porodem", count="0/24", hint="Krótki napis nad nazwą pakietu.")
    f += ('<fieldset><legend class="legend">Kolor etykiety</legend><div class="seg"><label><input type="radio" name="tc" checked><span class="dot"></span>Słońce</label>'
          '<label><input type="radio" name="tc"><span class="dot mint"></span>Mięta</label></div></fieldset>')
    f += '</div><div class="panel" style="gap:4px">' + switch("Wyróżniony", "Pogrubiona ramka na stronie. Najlepiej jeden pakiet naraz.", on=True)
    f += switch("Widoczny na stronie", "Wyłączony znika ze strony. Stare wyceny go nie tracą.", on=True) + '</div>'
    f += '<p class="hint" style="margin:0 4px">Tego pakietu nie można usunąć, bo jest w wycenach. Możesz go ukryć.</p>'
    return b + f'<form class="form">{f}</form>'


page("15-pakiet-edycja.html", "Pakiety", "Edit a package: price, typed 'was' price with the computed sum shown next to it, items with quantity, tag + colour, highlighted, visible.",
     "Pakiet Rodzinny", pack_edit(), bottom="save", save="clean")
page("16-pakiet-blad-brak-pozycji.html", "Pakiety", "Error: package with no items.", "Pakiet Rodzinny", pack_edit(no_items=True), bottom="save", save="invalid")

# ------------------------------------------------------------------ 17–18 add-ons
b = top("Cennik i ustawienia", act=f'<a class="act" href="#">{ico("arrow-up-down")}Kolejność</a>') + head("Dopłaty", "6 na stronie")
b += card([row(n, m, v, href="18-doplata-edycja.html" if "Mocne" in n else "#") for n, v, m in ADDONS]) + f'<a class="add" href="#">{ico("plus")}Dodaj dopłatę</a>' + PROTO
page("17-doplaty-lista.html", "Dopłaty", "Add-ons list.", "Dopłaty", b)
b = top("Dopłaty", "17-doplaty-lista.html") + head("Mocne zabrudzenia, sierść lub mocz", "", "Dopłaty")
f = '<div class="panel">' + field("Nazwa", "Mocne zabrudzenia, sierść lub mocz")
f += seg("Rodzaj dopłaty", "kind", ["Procent", "Kwota w zł"], "Procent")
f += '<div class="pair">' + field("Od", "20", suffix="%", inputmode="numeric") + field("Do", "30", suffix="%", inputmode="numeric", optional="hint") + '</div>'
f += '<p class="hint" style="margin-top:-8px">Całe procenty. Zostaw „Do” puste, jeśli dopłata ma jedną wartość. Na stronie: <b class="num">+20–30%</b>.</p></div>'
f += '<div class="panel" style="gap:12px">' + switch("Widoczna na stronie", "", on=True) + note("<b>Używane w:</b> 9 wycen.", "", "link") + '</div>'
page("18-doplata-edycja.html", "Dopłaty", "Edit an add-on: percent (single or range) or fixed zł.", "Dopłata", b + f'<form class="form">{f}</form>', bottom="save", save="clean")

# ------------------------------------------------------------------ 19–22 zones + towns
b = top("Cennik i ustawienia") + head("Strefy", "3 strefy dojazdu")
b += card([
    row("Strefa 1", "10 miejscowości · +0 min dojazdu", "Gratis", href="#"),
    row("Strefa 2", "9 miejscowości · +20 min dojazdu", "25 zł<s style='text-decoration:none'>gratis od 400 zł</s>", href="20-strefa-edycja-blad.html"),
    row("Dalej", "Wszystko poza listą miejscowości · +40 min", "1,50 zł / km", href="#"),
]) + note("Miejscowości przypisujesz do stref w sekcji <a href='21-miejscowosci-lista.html'>Miejscowości</a>.") + PROTO
page("19-strefy-lista.html", "Strefy", "Zones list (3): fee type and value at a glance.", "Strefy", b)
b = top("Strefy", "19-strefy-lista.html") + head("Strefa 2", "", "Strefy")
f = '<div class="panel">' + field("Nazwa", "Strefa 2")
f += seg("Opłata za dojazd", "fee", ["Gratis", "Stała opłata", "Za kilometr"], "Stała opłata")
f += '<div class="pair">' + field("Opłata", "", suffix="zł", inputmode="decimal", error="Podaj opłatę za dojazd.") + field("Gratis od kwoty", "400", suffix="zł", inputmode="decimal", optional="hint") + '</div>'
f += field("Dodatkowy czas dojazdu", "20", suffix="min", inputmode="numeric", short=True, hint="Doliczamy go do wizyty w kalendarzu.")
f += field("Notatka", "Reszta powiatu poznańskiego", optional=True, hint="Widoczna pod nazwą strefy na stronie.") + '</div>'
f += '<div class="panel" style="gap:12px">' + note("<b>Używane w:</b> 9 miejscowości, 6 wycen.", "", "link") + '</div>'
page("20-strefa-edycja-blad.html", "Strefy", "Edit a zone: fee type changes the fields. Error: flat-fee zone without a fee.", "Strefa 2", b + f'<form class="form">{f}</form>', bottom="save", save="invalid")

b = top("Cennik i ustawienia", act=f'<a class="act" href="#">{ico("arrow-up-down")}Kolejność</a>') + head("Miejscowości", "19 miejscowości w 2 strefach")
b += group("Strefa 1 · dojazd gratis", "10") + card([row(n, pc, href="#") for n, pc in Z1])
b += group("Strefa 2 · 25 zł", "9") + card([row(n, pc, href="22-miejscowosc-bledy.html" if n == "Puszczykowo" else "#") for n, pc in Z2])
b += f'<a class="add" href="#">{ico("plus")}Dodaj miejscowość</a>' + PROTO
page("21-miejscowosci-lista.html", "Miejscowości", "Towns list (19) grouped by zone, postcodes as the second line.", "Miejscowości", b)
b = top("Miejscowości", "21-miejscowosci-lista.html") + head("Nowa miejscowość", "", "Miejscowości")
f = '<div class="panel">' + field("Nazwa", "Kostrzyn")
f += field("Strefa", "Wybierz strefę", kind="select", options=["Wybierz strefę", "Strefa 1 · gratis", "Strefa 2 · 25 zł", "Dalej · 1,50 zł / km"], error="Wybierz strefę.")
f += '<fieldset><legend class="legend">Kody pocztowe</legend><div class="chips">'
f += f'<span class="chip num">62-025<button type="button" aria-label="Usuń kod 62-025">{ico("x")}</button></span></div>'
f += f'<div class="addline"><div class="inp"><input aria-label="Nowy kod pocztowy" value="6202" inputmode="numeric" placeholder="00-000" aria-invalid="true" style="border-color:var(--err500);border-width:2px"></div><button type="button" class="btn-sec">Dodaj kod</button></div>'
f += f'<p class="errmsg" role="alert">{ico("circle-alert")}Wpisz kod w formacie 00-000.</p></fieldset></div>'
page("22-miejscowosc-bledy.html", "Miejscowości", "New town: errors for missing zone and a malformed postcode; postcodes as removable chips.", "Nowa miejscowość",
     b + f'<form class="form">{f}</form>', bottom="save", save="invalid")

# ------------------------------------------------------------------ 23–24 area days
b = top("Cennik i ustawienia") + head("Dni rejonowe")
b += f"""<div class="card"><div class="empty"><span class="big">{ico("calendar-range")}</span><h2>Nie masz jeszcze dni rejonowych</h2>
<p>Wybierz dzień tygodnia i miejscowości. W formularzu klienci z tych miejscowości zobaczą ten dzień jako pierwszy. Inne dni zostają dostępne.</p>
<a class="btn-main" href="24-dzien-rejonowy-edycja.html">{ico("plus")}Dodaj dzień rejonowy</a></div></div>"""
page("23-dni-rejonowe-puste.html", "Dni rejonowe", "Empty state (real launch state: 0 area days).", "Dni rejonowe", b)
b = top("Dni rejonowe", "23-dni-rejonowe-puste.html") + head("Nowy dzień rejonowy", "", "Dni rejonowe")
f = '<div class="panel">' + field("Dzień tygodnia", "Wtorek", kind="select", options=["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"])
f += field("Twoja nazwa", "Południe: Luboń, Mosina", hint="Tylko dla Ciebie. Klient jej nie widzi.")
f += '<fieldset><legend class="legend">Miejscowości</legend><div class="chips">'
for t in ["Luboń", "Mosina", "Puszczykowo"]:
    f += f'<span class="chip">{t}<button type="button" aria-label="Usuń: {t}">{ico("x")}</button></span>'
f += f'</div><a class="add" href="#" style="margin-top:10px">{ico("plus")}Dodaj miejscowość</a></fieldset></div>'
f += note("Dzień rejonowy tylko ustawia kolejność terminów dla tych miejscowości. Nie blokuje innych dni.", "info")
page("24-dzien-rejonowy-edycja.html", "Dni rejonowe", "Add an area day: weekday, own label, towns as chips (picker = UDrawer with the grouped town list).", "Nowy dzień rejonowy",
     b + f'<form class="form">{f}</form>', bottom="save")

# ------------------------------------------------------------------ 25 hours, 26 business
b = top("Cennik i ustawienia") + head("Godziny pracy", "Z tych godzin powstają wolne terminy w formularzu.")
f = '<fieldset class="panel" style="gap:0"><legend class="vh">Godziny pracy</legend>'
for d, o, a, z in [("Poniedziałek", True, "08:00", "18:00"), ("Wtorek", True, "08:00", "18:00"), ("Środa", True, "08:00", "18:00"), ("Czwartek", True, "08:00", "18:00"),
                   ("Piątek", True, "08:00", "18:00"), ("Sobota", True, "14:00", "09:00"), ("Niedziela", False, "", "")]:
    bad = d == "Sobota"
    f += f'<div class="day{" err" if bad else ""}"><span class="dn">{d}{"" if o else "<small>Zamknięte</small>"}</span><input class="sw" type="checkbox" role="switch" aria-label="{d}: otwarte"{" checked" if o else ""}>'
    if o:
        f += (f'<div class="times"><div class="inp"><input type="time" aria-label="{d}: od" value="{a}"></div><span>do</span>'
              f'<div class="inp"><input type="time" class="{"bad" if bad else ""}" aria-label="{d}: do" value="{z}"{INV if bad else ""}></div></div>')
    if bad:
        f += f'<p class="errmsg" role="alert">{ico("circle-alert")}Godzina zamknięcia musi być późniejsza niż otwarcia.</p>'
    f += '</div>'
f += '</fieldset>'
page("25-godziny.html", "Godziny pracy", "Working hours: 7 days on one screen, one save. Error: closing before opening. Closed day collapses.", "Godziny pracy",
     b + f'<form class="form">{f}</form>', bottom="save", save="invalid")

b = top("Cennik i ustawienia") + head("Firma", "Kontakt na stronie i zasady przyjmowania zleceń.")
f = '<div class="panel"><h2>Kontakt</h2>' + field("Telefon", "+48 500 000 000", inputmode="tel", type_="tel", autocomplete="tel", hint="Numer w nagłówku strony i w przycisku „Zadzwoń”.")
f += switch("WhatsApp na tym samym numerze", "", on=False)
f += field("Numer WhatsApp", "+48 500 000 00", inputmode="tel", type_="tel", error="Wpisz numer w formacie +48 000 000 000.") + '</div>'
f += '<div class="panel"><h2>Zlecenia</h2>' + field("Minimalne zamówienie", "150", suffix="zł", inputmode="decimal", short=True)
f += field("Maksymalnie wizyt dziennie", "3", inputmode="numeric", short=True, hint="Na stronie pokazujemy to jako „maks. 3 wizyty dziennie”.")
f += field("Najkrótszy czas do wizyty", "24", suffix="godz.", inputmode="numeric", short=True, hint="Klient nie zarezerwuje wcześniejszego terminu.") + '</div>'
f += '<p class="proto">Prototyp: numer telefonu to przykład. Prawdziwy numer poda właściciel.</p>'
page("26-firma.html", "Firma", "Business settings: one form, one save. Error: malformed phone. Phone is a placeholder.", "Firma", b + f'<form class="form">{f}</form>', bottom="save", save="invalid")

# ------------------------------------------------------------------ 27–29 FAQ
b = top("Cennik i ustawienia", act=f'<a class="act" href="#">{ico("arrow-up-down")}Kolejność</a>') + head("FAQ", "Pytania i odpowiedzi na stronach usług.")
b += field("Strona", "Wózki i foteliki · 7 pytań", kind="select", options=["Wózki i foteliki · 7 pytań"], hint="Kolejne strony pojawią się tu, gdy powstaną.")
b += '<div style="height:16px"></div>'
b += card([row(q, f'{pchip("90 zł")}{pchip("120 zł")}{pchip("160 zł")}{pchip("150 zł")} 4 ceny na żywo' if n == 0 else (f'{pchip("80 zł")} 1 cena na żywo' if n == 1 else ""),
               href="28-faq-edycja.html" if n == 0 else "#") for n, q in enumerate(FAQ)])
b += f'<a class="add" href="#">{ico("plus")}Dodaj pytanie</a>'
page("27-faq-lista.html", "FAQ", "FAQ list for one counter page (page picker ready for 5 more). Rows show which answers carry live prices.", "FAQ", b)


def faq_edit():
    b = top("FAQ", "27-faq-lista.html") + head("Pytanie", "", "FAQ · Wózki i foteliki")
    f = '<div class="panel">' + field("Pytanie", "Ile kosztuje pranie wózka dziecięcego?", kind="textarea", rows=2)
    f += f"""<div class="field"><span class="legend" id="al">Odpowiedź</span>
<div class="rich" role="textbox" aria-multiline="true" aria-labelledby="al" contenteditable="true">Wózek spacerowy od {pchip("90 zł", True)}, 2w1 od {pchip("120 zł")}, 3w1 od {pchip("160 zł")}, bliźniaczy od {pchip("150 zł")}. Dokładną cenę podajemy ze zdjęć, zanim przyjedziemy.</div>
<div class="richbar"><button type="button" class="btn-sec sm">{ico("tag")}Wstaw cenę</button><button type="button" class="btn-sec sm" style="color:var(--err500)">{ico("x")}Usuń cenę</button></div>
<p class="hint">Zaznaczona: <b>Wózek spacerowy</b>. Zielona cena bierze się z cennika. Gdy zmienisz cenę usługi, zmieni się też tutaj.</p></div></div>"""
    f += f"""<div class="preview"><span class="lbl">Tak to wygląda na stronie</span><b>Ile kosztuje pranie wózka dziecięcego?</b>
Wózek spacerowy od 90 zł, 2w1 od 120 zł, 3w1 od 160 zł, bliźniaczy od 150 zł. Dokładną cenę podajemy ze zdjęć, zanim przyjedziemy.</div>"""
    f += f'<button type="button" class="btn-text danger">{ico("trash-2")}Usuń pytanie</button>'
    return b + f'<form class="form">{f}</form>'


page("28-faq-edycja.html", "FAQ", "Edit an answer: live prices are chips (never raw code); a chip is selected, so its item name and 'Usuń cenę' show; preview below.",
     "FAQ: pytanie", faq_edit(), bottom="save", save="clean")
pick = f"""<div class="overlay"><div class="sheet" role="dialog" aria-modal="true" aria-labelledby="pt"><h2 id="pt">Wstaw cenę</h2>
<p class="lead">Wybierz pozycję. W odpowiedzi pojawi się jej aktualna cena.</p>
<div class="field"><label class="vh" for="ps">Szukaj</label><div class="inp"><input id="ps" type="search" placeholder="Szukaj usługi lub pakietu" style="padding-left:44px">{ico("search").replace('class="ico "', 'class="ico" style="position:absolute;left:14px;color:var(--n500)"')}</div></div>
<p class="gh">Dziecko</p><ul>
{"".join(row(n, "", f"{p} zł", go=False) for n, _, p, _, _ in SERVICES[0][1])}</ul>
<p class="gh">Meble tapicerowane</p><ul>{"".join(row(n, "", f"{p} zł", go=False) for n, _, p, _, _ in SERVICES[1][1][:2])}</ul>
</div></div>"""
page("29-faq-wstaw-cene.html", "FAQ", "'Wstaw cenę' picker (UDrawer): search, grouped items and packages with current prices; tap inserts a chip at the cursor.",
     "Wstaw cenę", faq_edit(), bottom="save", save="clean", overlay=pick)

# ------------------------------------------------------------------ 30 wanted now
b = top("Cennik i ustawienia") + head("Teraz w sezonie", "Jedna usługa lub pakiet, który teraz polecasz na stronie.")
f = '<div class="panel">' + switch("Pokazuj na stronie", "", on=True)
f += f"""<div class="field"><span class="legend">Co polecasz teraz</span>
<a class="row" href="#" style="border:1.5px solid var(--n400);border-radius:var(--r-lg);padding-left:14px" aria-label="Zmień: Wózek 2w1 (gondola i spacerówka), od 120 zł"><span class="main"><span class="name">Wózek 2w1 (gondola i spacerówka)</span><span class="meta num">Usługa · od 120 zł</span></span><span style="font-weight:700;color:var(--p600)">Zmień</span></a></div>"""
f += field("Krótka linijka", "Przed wiosennymi spacerami", optional=True, count="26/60", hint="Bez dat i liczników. Tylko to, co jest prawdą.") + '</div>'
f += f"""<div class="preview"><span class="lbl">Podgląd etykiety</span><span class="wanted"><i></i>Teraz w sezonie: Wózek 2w1 od 120 zł</span><br>Przed wiosennymi spacerami</div>"""
f += note("Miejsce tej etykiety na stronie nie jest jeszcze ustalone (strona główna, #43). Cena w etykiecie zawsze bierze się z cennika.", "info")
page("30-sezon.html", "Teraz w sezonie", "Wanted now: pick one item or package + optional line, on/off, label preview. Where it shows publicly is open.", "Teraz w sezonie",
     b + f'<form class="form">{f}</form>', bottom="save", save="clean")

# ------------------------------------------------------------------ 31–32 loading + load error
b = top("Cennik i ustawienia") + head("Usługi", '<span class="sk" style="width:150px;margin-top:6px"></span>')
b += '<div aria-busy="true" aria-label="Wczytuję usługi">'
for n in (6, 5):
    b += '<div class="group-h"><span class="sk" style="width:90px"></span></div><div class="card">'
    b += "".join(f'<div class="row"><span class="main"><span class="sk" style="width:{w}%"></span><span class="sk" style="width:22%;height:10px;margin-top:10px"></span></span><span class="sk" style="width:56px"></span></div>' for w in (48, 62, 55, 40, 58, 50)[:n])
    b += '</div>'
b += '</div>'
page("31-wczytywanie.html", "States", "Loading (every list): skeleton rows in the list's real shape. Title and back link render at once.", "Usługi", b)
b = top("Cennik i ustawienia") + head("Usługi")
b += f"""<div class="card"><div class="empty bad" role="alert"><span class="big">{ico("triangle-alert")}</span><h2>Nie udało się wczytać usług</h2>
<p>Sprawdź internet i spróbuj ponownie. Na stronie nic się nie zmieniło.</p><button class="btn-main">{ico("refresh-cw")}Spróbuj ponownie</button></div></div>"""
page("32-blad-wczytywania.html", "States", "Load error (every section): what happened, that the site is unaffected, retry.", "Usługi", b)

# ------------------------------------------------------------------ 33–35 login (optional)
LOGO = '<div class="logo"><img src="../stroller/assets/mark.svg" alt="">Nowiutko</div>'
page("33-logowanie-email.html", "Login", "Login step 1: email.", "Logowanie", f"""<main class="login">{LOGO}<div><h1>Zaloguj się</h1><p>Wpisz swój e-mail. Wyślemy na niego 6-cyfrowy kod.</p></div>
<form class="form">{field("E-mail", "", placeholder="ty@nowiutko.pl", inputmode="email", type_="email", autocomplete="email")}<button class="btn-main">Wyślij kod</button></form></main>""",
     bottom=None, shell=False, raw=True)


def code_step(err=False):
    digits = "482913" if err else "48"
    inputs = "".join(f'<input inputmode="numeric" maxlength="1" aria-label="Cyfra {i + 1} z 6" value="{digits[i] if i < len(digits) else ""}"{OTC if i == 0 else ""}>' for i in range(6))
    er = f'<p class="errmsg" role="alert">{ico("circle-alert")}Kod jest nieprawidłowy albo wygasł. Wpisz go jeszcze raz lub wyślij nowy.</p>' if err else ""
    return f"""<main class="login">{LOGO}<div><h1>Wpisz kod</h1><p>Wysłaliśmy 6-cyfrowy kod na <b>ty@nowiutko.pl</b>. Jest ważny 10 minut.</p></div>
<form class="form"><fieldset><legend class="vh">Kod z e-maila</legend><div class="code{" err" if err else ""}">{inputs}</div>{er}</fieldset>
<button class="btn-main">Zaloguj</button><button type="button" class="btn-text">Wyślij kod jeszcze raz</button><a class="btn-text" href="33-logowanie-email.html" style="color:var(--n500);margin-top:-12px">Zmień e-mail</a></form></main>"""


page("34-logowanie-kod.html", "Login", "Login step 2: 6-digit code (one-time-code autofill).", "Kod", code_step(), bottom=None, shell=False, raw=True)
page("35-logowanie-blad.html", "Login", "Login error: wrong or expired code.", "Kod", code_step(True), bottom=None, shell=False, raw=True)

# ------------------------------------------------------------------ 40 desktop split (only place 1440 really differs)
lst = services_list().replace('<a class="row " href="06-usluga-edycja.html">', '<a class="row " href="06-usluga-edycja.html" aria-current="true">', 1)
det = service_edit()
split = f'<div class="split"><main class="screen list-pane" aria-label="Lista usług">{lst}</main><section class="screen detail" aria-label="Edycja usługi">{det}</section></div>'
page("40-desktop-uslugi.html", "Desktop", "1440: sidebar with all six sections replaces the tab bar; list and edit side by side; save bar across the bottom.", "Usługi", split,
     bottom="save+split", raw=True)

# ------------------------------------------------------------------ review board
cards = "".join(f'<figure><iframe src="{f}" loading="lazy" title="{e(n)}"></iframe><figcaption><a href="{f}"><b>{f}</b></a><br>{e(n)}</figcaption></figure>' for f, g, n in FRAMES if not f.startswith("40"))
(HERE / "index.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin: Cennik i ustawienia — review board</title><style>
body{{margin:0;padding:24px;font:15px/1.5 system-ui,sans-serif;background:#eef1f0;color:#12302B}}h1{{margin:0 0 4px}}p{{max-width:80ch}}
.g{{display:flex;flex-wrap:wrap;gap:28px;margin-top:24px}}figure{{margin:0;width:390px}}iframe{{width:390px;height:844px;border:1px solid #c5d3ce;border-radius:12px;background:#fff}}
figcaption{{margin-top:8px;font-size:13.5px}}</style></head><body>
<h1>Admin: shell + Cennik i ustawienia</h1><p>Draft for <code>admin-cennik-v1</code>. Each frame is a static state at 390 × 844. Sample data only. Desktop: <a href="40-desktop-uslugi.html">40-desktop-uslugi.html</a> (open at 1440).</p>
<div class="g">{cards}</div></body></html>""", encoding="utf-8")
print(f"{len(FRAMES)} frames written")
