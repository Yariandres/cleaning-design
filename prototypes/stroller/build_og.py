"""Builds the share-image (Open Graph) template pages, 1200 x 630. Run: python3 prototypes/stroller/build_og.py
Then render the PNGs: see the commands printed at the end (tools/render.mjs, headless Chrome).

One template, two variants (DESIGN.md -> Imagery):
  photo     light paper, logo, title, one line, the owner's photo in a 440 x 518 slot (unchanged from stroller-v1)
  no-photo  the brand badge at full size: teal ground, the chamomile bleeding off the left edge, the logo on a white label, title in white
Slots: title (og.title in copy.md: a short page name, never the H1 string and never a price), line (og.line), photo.
Text is real HTML text in the self-hosted fonts, so Polish letters are exact. No image-generation tool is involved."""
import os, math
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "final")

def flower(petals=12):
    # the logo symbol from handoff/brand/logo/mark.svg without its badge: white petals, sun centre
    e = "".join(f'<ellipse cx="50" cy="28.92" rx="3.57" ry="12.92" fill="#fff" transform="rotate({i*360/petals:.2f} 50 50)"/>' for i in range(petals))
    return f'<svg class="flower" viewBox="0 0 100 100" aria-hidden="true">{e}<circle cx="50" cy="50" r="9.18" fill="#FFD45C"/></svg>'

CSS = '''
html,body{margin:0}body{width:1200px;height:630px;overflow:hidden;padding:0!important}
.og{position:relative;width:1200px;height:630px;box-sizing:border-box;overflow:hidden;display:flex}
.og .copy{display:flex;flex-direction:column;justify-content:space-between;position:relative;z-index:1}
.og h1{font-family:var(--display);font-weight:800;letter-spacing:-.015em;margin:0;text-wrap:balance}
.og .meta{display:flex;gap:14px;align-items:center;font-family:var(--body);font-weight:700;white-space:nowrap}
.og .meta i{border-radius:50%;background:var(--s300);display:block}
/* photo variant (unchanged from stroller-v1): title max 3 lines at 64px; 54px for 4 lines */
.og.photo{background:var(--p50);padding:56px 64px;gap:48px}
.og.photo .copy{flex:1}.og.photo .logo{height:56px;width:auto;display:block;align-self:flex-start}
.og.photo h1{font-size:64px;line-height:1.04;color:var(--n900)}
.og.photo .meta{font-size:24px;color:var(--p700)}.og.photo .meta i{width:10px;height:10px}
.og.photo .slot{flex:0 0 440px;height:518px;border-radius:24px;overflow:hidden}.og.photo .slot img{width:100%;height:100%;object-fit:cover;display:block}
.og.photo .ph{height:100%;border-radius:24px;font-size:20px;box-sizing:border-box}
/* no-photo variant: the logo's own layout at full size (flower left, words right). Made to be read small (about 400px
   wide in a chat) and to survive a centre-square crop: logo, title and line all sit inside x 285-915. */
.og.nophoto{background:var(--p500);padding:52px 64px 56px}
.og.nophoto .copy{width:600px;margin-left:252px}
.og.nophoto .label{align-self:flex-start;background:#fff;border-radius:22px;padding:12px 26px 12px 12px;display:flex}.og.nophoto .logo{height:64px;width:auto;display:block}
.og.nophoto h1{font-size:80px;line-height:1;color:#fff}.og.nophoto h1.long{font-size:64px;line-height:1.04}
.og.nophoto .meta{font-size:32px;color:#fff;gap:18px}.og.nophoto .meta i{width:14px;height:14px;background:var(--p200)}
.og.nophoto .flower{position:absolute;width:860px;height:860px;left:-440px;top:-115px}
'''
def page(variant, title, line=("U Ciebie w domu", "Poznań i okolice"), long=False, photo=None):
    meta = f'<div class="meta" data-slot="line"><span>{line[0]}</span><i></i><span>{line[1]}</span></div>'
    if variant == "photo":
        slot = f'<img src="{photo}" alt="">' if photo else '<div class="ph">miejsce na własne zdjęcie<br>(przycięcie 440 × 518, bez ludzi)</div>'
        body = f'<div class="og photo"><div class="copy"><img class="logo" src="../assets/logo.svg" alt="Nowiutko"><h1 data-slot="title">{title}</h1>{meta}</div><div class="slot" data-slot="photo">{slot}</div></div>'
    else:
        body = f'<div class="og nophoto"><div class="copy"><div class="label"><img class="logo" src="../assets/logo.svg" alt="Nowiutko"></div><h1 data-slot="title"{" class=long" if long else ""}>{title}</h1>{meta}</div>{flower()}</div>'
    return f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>Share image 1200x630 ({variant})</title><link rel="stylesheet" href="../base.css"><style>{CSS}</style></head><body>{body}</body></html>\n'

STROLLER = "Pranie wózków i&nbsp;fotelików w&nbsp;Poznaniu"
FILES = {
  "og-template.html": page("photo", STROLLER),                       # photo variant, empty slot
  "og-template-no-photo.html": page("nophoto", STROLLER),            # no-photo variant = the stroller page's launch image
  "og-photo-stroller.html": page("photo", STROLLER, photo="../../../handoff/pages/stroller-counter/photos/og-photo.jpg"),  # photo variant with the owner's og-photo (stroller-v1.4 draft)
  "og-test-long-title.html": page("nophoto", "[Dłuższy tytuł strony w&nbsp;czterech wierszach – próba]", long=True),  # length test only, not a real page
}
for name, html in FILES.items():
    open(os.path.join(OUT, name), "w").write(html)
print("og built:", ", ".join(FILES))
