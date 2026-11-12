"""Generates the Nowiutko logo directions as SVG files (design tool, not production code).

Run:  python3 prototypes/logo/build.py <path-to-bricolage-latin-wght-normal.woff2>
The wordmark is outlined from Bricolage Grotesque (SIL OFL), so the SVGs need no font.
Colours are the DESIGN.md scales: primary-500 #0E6E5C, primary-700 #0B473B, primary-800 #09342C,
primary-100 #D7F3E6, secondary-300 #FFD45C, neutral-50 #F5FAF8, neutral-900 #12302B.
"""
import io, math, os, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

TEAL, TEAL7, TEAL8, MINT = "#0E6E5C", "#0B473B", "#09342C", "#D7F3E6"
SUN, PAPER, INK, WHITE = "#FFD45C", "#F5FAF8", "#12302B", "#FFFFFF"
OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- wordmark outlines -------------------------------------------------
_woff = sys.argv[1]
_tt = TTFont(_woff); _tt.flavor = None
_buf = io.BytesIO(); _tt.save(_buf)
_face = hb.Face(_buf.getvalue()); _upem = _face.upem
_os2 = _tt["OS/2"]
XH, CAP = _os2.sxHeight / _upem, _os2.sCapHeight / _upem


def shape(text, size, wght, tracking=0.0):
    """Returns (path d, advance width, [glyph (x_left, x_right) in px], glyph infos) with baseline at y=0, y down."""
    f = hb.Font(_face); f.set_variations({"wght": wght})
    b = hb.Buffer(); b.add_str(text); b.guess_segment_properties()
    hb.shape(f, b, {"kern": True})
    s = size / _upem; x = 0.0; parts = []; boxes = []
    for info, pos in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(None, ntos=lambda v: f"{v:.2f}")
        f.draw_glyph_with_pen(info.codepoint, TransformPen(pen, (s, 0, 0, -s, x + pos.x_offset * s, 0)))
        parts.append(pen.getCommands())
        ext = f.get_glyph_extents(info.codepoint)
        boxes.append((x + ext.x_bearing * s, x + (ext.x_bearing + ext.width) * s))
        x += pos.x_advance * s + tracking * size
    return " ".join(p for p in parts if p), x - tracking * size, boxes


# ---------- chamomile ---------------------------------------------------------
def flower(cx, cy, R, n=12, style="solid", sw=2.6, petal=WHITE, line=TEAL, centre=SUN, small=False):
    """Chamomile head: n petals round a sun centre. style 'solid' (filled) or 'line' (outlined)."""
    if small:
        dp, rx, ry, rc = 0.60 * R, 0.19 * R, 0.40 * R, 0.36 * R
    else:
        dp, rx, ry, rc = 0.62 * R, 0.105 * R if n >= 12 else 0.14 * R, 0.38 * R, 0.27 * R
    out = []
    for i in range(n):
        a = 360 / n * i
        st = f'fill="{petal}"' + (f' stroke="{line}" stroke-width="{sw}"' if style == "line" else "")
        out.append(f'<ellipse cx="{cx}" cy="{cy - dp:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" {st} transform="rotate({a:.2f} {cx} {cy})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{rc:.2f}" fill="{centre}"/>')
    return "".join(out)


def svg(w, h, body, vb=None, title=""):
    vb = vb or f"0 0 {w} {h}"
    t = f"<title>{title}</title>" if title else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" role="img" aria-label="Nowiutko">{t}{body}</svg>\n'


def write(path, content):
    os.makedirs(os.path.dirname(os.path.join(OUT, path)), exist_ok=True)
    open(os.path.join(OUT, path), "w").write(content)


def square_icon(inner, bg, rounded=True):
    r = 22 if rounded else 0
    return svg(512, 512, f'<rect width="100" height="100" rx="{r}" fill="{bg}"/>{inner}', vb="0 0 100 100", title="Nowiutko")


# ========== A  LINIA — line chamomile on a stem, ink-teal wordmark ============
def a_mark_full():
    stem = f'<path d="M50 64 C50 76 46 86 46 98" fill="none" stroke="{TEAL}" stroke-width="3" stroke-linecap="round"/>'
    leaf = f'<path d="M47.5 86 C47 77 55 72 65 72 C65 81 58 86 47.5 86 Z" fill="{MINT}" stroke="{TEAL}" stroke-width="3" stroke-linejoin="round"/>'
    return stem + leaf + flower(50, 34, 30, n=12, style="line", sw=2.6)


def a_mark_small():
    return flower(50, 50, 44, n=8, style="line", sw=6.5, small=True)


d, wA, _ = shape("Nowiutko", 46, 700, 0.0)
write("a-linia/mark.svg", svg(100, 100, a_mark_full(), title="Nowiutko symbol"))
write("a-linia/mark-small.svg", svg(100, 100, a_mark_small(), title="Nowiutko symbol, small sizes"))
write("a-linia/logo.svg", svg(round(112 + wA), 100,
      a_mark_full() + f'<path d="{d}" fill="{INK}" transform="translate(112 68)"/>', title="Nowiutko"))
write("a-linia/app-icon.svg", square_icon(f'<g transform="translate(50 50) scale(0.62) translate(-50 -50)">{a_mark_small()}</g>', PAPER))
write("a-linia/app-icon-maskable.svg", square_icon(f'<g transform="translate(50 50) scale(0.52) translate(-50 -50)">{a_mark_small()}</g>', PAPER, rounded=False))

# ========== B  ODZNAKA — white chamomile on a teal badge, teal wordmark =======
def b_badge(inner_scale=1.0, bg=TEAL, rounded=True, small=False):
    f = flower(50, 50, 34 * inner_scale, n=8 if small else 12, style="solid", small=small)
    return f'<rect width="100" height="100" rx="{26 if rounded else 0}" fill="{bg}"/>{f}'


d, wB, _ = shape("Nowiutko", 50, 800, -0.005)
write("b-odznaka/mark.svg", svg(100, 100, b_badge(), title="Nowiutko symbol"))
write("b-odznaka/mark-small.svg", svg(100, 100, b_badge(small=True), title="Nowiutko symbol, small sizes"))
write("b-odznaka/logo.svg", svg(round(116 + wB), 100,
      b_badge() + f'<path d="{d}" fill="{TEAL7}" transform="translate(116 67)"/>', title="Nowiutko"))
write("b-odznaka/app-icon.svg", square_icon(flower(50, 50, 33, n=8, small=True), TEAL))
write("b-odznaka/app-icon-maskable.svg", square_icon(flower(50, 50, 27, n=8, small=True), TEAL, rounded=False))

# ========== C  KROPKA — wordmark whose i-dot is a chamomile; N monogram ========
SIZE = 56
d_left, w1, _ = shape("Now", SIZE, 800, -0.005)
_, wi, bi = shape("ı", SIZE, 800)
d_i, _, _ = shape("ı", SIZE, 800)
d_right, w3, _ = shape("utko", SIZE, 800, -0.005)
x_i = w1 + 0.01 * SIZE
stem_cx = x_i + (bi[0][0] + bi[0][1]) / 2
R_dot = 0.215 * SIZE
cy_dot = -(XH * SIZE + 0.07 * SIZE + R_dot)
x_r = x_i + wi
word_w = x_r + w3
pad = 6
body = (f'<g transform="translate({pad} {pad + 70})"><path d="{d_left}" fill="{INK}"/>'
        f'<path d="{d_i}" fill="{INK}" transform="translate({x_i:.2f} 0)"/>'
        f'<path d="{d_right}" fill="{INK}" transform="translate({x_r:.2f} 0)"/>'
        f'<g transform="translate({stem_cx:.2f} {cy_dot:.2f})">{flower(0, 0, R_dot, n=8, style="line", sw=1.9, petal=WHITE, line=TEAL, small=True)}</g></g>')
write("c-kropka/logo.svg", svg(round(word_w + 2 * pad), 88, body, title="Nowiutko"))

dN, wN, bN = shape("N", 52, 800)
def c_monogram(bg=TEAL8, rounded=True, k=1.0, small=False):
    ox = 50 - wN / 2 - 4
    f = flower(0, 0, 11.5, n=8, small=True, petal=WHITE)
    return (f'<rect width="100" height="100" rx="{26 if rounded else 0}" fill="{bg}"/>'
            f'<g transform="translate(50 50) scale({k}) translate(-50 -50)">'
            f'<path d="{dN}" fill="{WHITE}" transform="translate({ox:.2f} {50 + CAP * 52 / 2 + 4:.2f})"/>'
            f'<g transform="translate({ox + wN + 1:.2f} {50 - CAP * 52 / 2 - 1:.2f})">{f}</g></g>')
write("c-kropka/mark.svg", svg(100, 100, c_monogram(), title="Nowiutko monogram"))
write("c-kropka/mark-small.svg", svg(100, 100, c_monogram(), title="Nowiutko monogram, small sizes"))
write("c-kropka/app-icon.svg", square_icon(c_monogram(rounded=False, k=1.0)[0:0] + c_monogram(rounded=False).split("/>", 1)[1], TEAL8))
write("c-kropka/app-icon-maskable.svg", square_icon(c_monogram(rounded=False, k=0.78).split("/>", 1)[1], TEAL8, rounded=False))
print("done; wordmark widths", round(wA), round(wB), round(word_w), "xh", XH, "cap", CAP)
