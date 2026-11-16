// Screenshots + automatic checks for homepage v0 (adapted from prototypes/stroller/shots.mjs). No dependencies: drives the local Chrome over the
// DevTools protocol with Node's built-in WebSocket (Node 22+). Same approach as prototypes/quote-form/shots.mjs.
// Run: node prototypes/homepage-v0/shots.mjs [outDir]   (default: handoff/pages/homepage-v0/screens)
// Writes the PNGs and checks.json: horizontal scroll, h1 count, text contrast, tap targets, link targets,
// keyboard focus (ring + not hidden under the sticky bar), reduced motion, footer reachability.
import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.resolve(process.argv[2] || path.join(HERE, "../../handoff/pages/homepage-v0/screens"));
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
mkdirSync(OUT, { recursive: true });

// mode: full = whole page · first = the first viewport · footer = from 96px above the footer to the page end ·
// bottom = the last viewport (scrolled to the end; shows what the fixed bars cover)
const F = "";
const FRAMES = [
  ["01-default-390", F + "index.html", 390, 844, "full"],
  ["02-default-1440", F + "index.html", 1440, 900, "full"],
  ["03-hold-768", F + "index.html", 768, 1024, "full"],
  ["04-hold-1024", F + "index.html", 1024, 768, "full"],
  ["05-first-screen-390", F + "index.html", 390, 844, "first"],
  ["06-first-screen-1440", F + "index.html", 1440, 900, "first"],
  ["07-state-cookie-390", F + "state-cookie.html", 390, 844, "first"],
  ["08-state-cookie-1440", F + "state-cookie.html", 1440, 900, "first"],
  ["09-state-service-live-390", F + "state-service-live.html", 390, 844, "full"],
  ["10-state-service-live-1440", F + "state-service-live.html", 1440, 900, "full"],
  ["11-end-of-page-sticky-bar-390", F + "index.html", 390, 844, "bottom"],
  ["12-end-of-page-cookie-banner-390", F + "state-cookie.html", 390, 844, "bottom"],
  ["13-default-320", F + "index.html", 320, 640, "full"],
  ["14-hero-390", F + "index.html", 390, 844, "hero"],
  ["15-hero-1440", F + "index.html", 1440, 900, "hero"],
  ["16-hero-768", F + "index.html", 768, 1024, "hero"],
  ["17-hero-1024", F + "index.html", 1024, 768, "hero"],
  ["18-hero-320", F + "index.html", 320, 640, "hero"],
];

const proc = spawn(CHROME, ["--headless=new", "--remote-debugging-port=0", "--no-first-run", "--hide-scrollbars", "--disable-gpu",
  "--user-data-dir=" + mkdtempSync(path.join(tmpdir(), "st-")), "about:blank"], { stdio: ["ignore", "ignore", "pipe"] });
const wsUrl = await new Promise((res, rej) => {
  let buf = "";
  proc.stderr.on("data", (d) => { buf += d; const m = buf.match(/ws:\/\/[^\s]+/); if (m) res(m[0]); });
  setTimeout(() => rej(new Error("Chrome did not start: " + buf)), 15000);
});
const ws = new WebSocket(wsUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0; const pending = new Map(); const waiters = [];
ws.onmessage = (ev) => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(m.error.message)) : res(m.result); }
  else if (m.method) for (const w of [...waiters]) if (w.method === m.method && w.sessionId === m.sessionId) { waiters.splice(waiters.indexOf(w), 1); w.res(m.params); }
};
const send = (method, params = {}, sessionId) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
const once = (method, sessionId) => new Promise((res) => waiters.push({ method, sessionId, res }));
const { targetId } = await send("Target.createTarget", { url: "about:blank" });
const { sessionId: S } = await send("Target.attachToTarget", { targetId, flatten: true });
await send("Page.enable", {}, S);
const ev = async (expression) => (await send("Runtime.evaluate", { expression, returnByValue: true, awaitPromise: true }, S)).result.value;

// Pages that exist on launch day (developer #8 point 4). Everything else an <a> points at is a failure.
const LIVE = ["/", "/poznan/pranie-wozkow-i-fotelikow", "/polityka-prywatnosci", "/polityka-prywatnosci#cookies"];
const LIVE_DEMO = ["/poznan/pranie-kanap"]; // state frame 09/10 only

const CHECK = `(() => {
  const lum = (c) => { const a = c.map((v) => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * a[0] + .7152 * a[1] + .0722 * a[2]; };
  const parse = (s) => { const m = s.match(/rgba?\\(([^)]+)\\)/); if (!m) return null; const p = m[1].split(/[ ,\\/]+/).map(Number); return { c: p.slice(0, 3), a: p.length > 3 ? p[3] : 1 }; };
  const bgOf = (el) => { let stack = []; for (let n = el; n && n.nodeType === 1; n = n.parentElement) { const cs = getComputedStyle(n); if (cs.backgroundImage !== "none" && /gradient/.test(cs.backgroundImage)) { const m = cs.backgroundImage.match(/rgba?\\([^)]+\\)/g); if (m) { const ps = m.map(parse).filter((p) => p.a > 0); if (ps.length) { stack.push(ps[ps.length - 1]); if (ps[ps.length - 1].a === 1) break; } } } const b = parse(cs.backgroundColor); if (b && b.a > 0) { stack.push(b); if (b.a === 1) break; } } let c = [245, 250, 248]; for (const b of stack.reverse()) c = c.map((v, i) => v * (1 - b.a) + b.c[i] * b.a); return c; };
  const vis = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none" && !el.closest("[hidden]"); };
  const name = (el) => (el.getAttribute("aria-label") || el.innerText || el.id || el.className || el.tagName).toString().trim().replace(/\\s+/g, " ").slice(0, 60);
  const out = { horizontalScroll: document.documentElement.scrollWidth > innerWidth, h1Count: document.querySelectorAll("h1").length, headingsInFooter: document.querySelectorAll("footer.site-f :is(h1,h2,h3,h4)").length, contrastMin: 99, contrastFails: [], smallTargets: [], inlineLinksExempt: [], links: {}, deadLinks: [], placeholdersLeft: [...document.querySelectorAll(".tbd")].map((e) => e.dataset.bind) };
  for (const el of document.querySelectorAll("a,button,summary,input,select")) {
    if (!vis(el)) continue;
    const r = (el.closest(".svc-card") || el).getBoundingClientRect(); // the card is the hit area (stretched link)
    const inline = el.matches("a") && getComputedStyle(el).display === "inline" && el.closest("p");
    if (inline) out.inlineLinksExempt.push(name(el));
    else if (r.height < 43.5 || r.width < 43.5) out.smallTargets.push(name(el) + " " + Math.round(r.width) + "x" + Math.round(r.height));
    if (el.matches("a")) { const h = el.getAttribute("href"); out.links[h.replace(/\\?text=.*/, "?text=…")] = (out.links[h.replace(/\\?text=.*/, "?text=…")] || 0) + 1; }
  }
  for (const h of Object.keys(out.links)) {
    if (/^(tel:\\+48\\d{9}|sms:\\+48\\d{9}|https:\\/\\/wa\\.me\\/48\\d{9}\\?text=…)$/.test(h)) continue;
    if (h[0] === "#") { if (!document.getElementById(h.slice(1))) out.deadLinks.push(h + " (no such id)"); continue; }
    if (!(${JSON.stringify(LIVE.concat(LIVE_DEMO))}).includes(h)) out.deadLinks.push(h);
  }
  const seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n; (n = walker.nextNode());) {
    if (!n.nodeValue.trim()) continue; const el = n.parentElement; if (!vis(el) || el.closest("svg,script,style,.ph")) continue;
    const cs = getComputedStyle(el); const fg = parse(cs.color); if (!fg) continue;
    const bg = bgOf(el); const c = fg.c.map((v, i) => v * fg.a + bg[i] * (1 - fg.a));
    const l1 = lum(c), l2 = lum(bg); const ratio = (Math.max(l1, l2) + .05) / (Math.min(l1, l2) + .05);
    if (ratio < out.contrastMin) out.contrastMin = +ratio.toFixed(2);
    const big = parseFloat(cs.fontSize) >= 24 || (parseFloat(cs.fontSize) >= 18.66 && +cs.fontWeight >= 700);
    if (ratio < (big ? 3 : 4.5)) { const k = ratio.toFixed(2) + " " + n.nodeValue.trim().slice(0, 30); if (!seen.has(k)) { seen.add(k); out.contrastFails.push(k); } }
  }
  const h1 = document.querySelector("h1");
  out.h1Text = h1 ? h1.textContent.trim() : null;
  const sa = [...document.querySelectorAll('a[href="/poznan/pranie-wozkow-i-fotelikow"]')];
  out.strollerLinks = sa.map((a) => a.textContent.trim());
  const soonLis = [...document.querySelectorAll(".soon li")];
  out.comingRows = soonLis.map((li) => ({ text: li.textContent.trim().replace(/\\s+/g, " "), href: (li.querySelector("a") || {}).getAttribute ? li.querySelector("a").getAttribute("href").replace(/\\?text=.*/, "?text=…") : null, prefill: decodeURIComponent((li.querySelector("a").getAttribute("href").split("text=")[1] || "")), linkText: li.querySelector("a").textContent.trim().replace(/\\s+/g, " "), h: Math.round(li.getBoundingClientRect().height), wkrotce: /wkrótce/i.test(document.body.textContent) }));
  out.emptyHrefs = [...document.querySelectorAll("a")].filter((a) => !a.getAttribute("href") || a.getAttribute("href") === "#").length;
  out.headings = [...document.querySelectorAll("h1,h2,h3,h4")].map((e) => e.tagName + " " + e.textContent.trim().replace(/\\s+/g, " ").slice(0, 60));
  out.minBodyFontPx = Math.min(...[...document.querySelectorAll("main p, main li, main span, main a")].filter(vis).map((e) => parseFloat(getComputedStyle(e).fontSize)));
  const f = document.querySelector("footer.site-f");
  if (f) {
    const ft = [...f.querySelectorAll("p,span,a,button,b")].filter((e) => vis(e) && e.children.length === 0);
    out.footer = { height: Math.round(f.getBoundingClientRect().height), minFontPx: Math.min(...ft.map((e) => parseFloat(getComputedStyle(e).fontSize))),
      clippedText: ft.filter((e) => e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).display !== "inline").map(name),
      outsideFooter: ft.filter((e) => { const r = e.getBoundingClientRect(), fr = f.getBoundingClientRect(); return r.right > fr.right + .5 || r.left < fr.left - .5; }).map(name) };
  }
  return JSON.stringify(out);
})()`;

// Scroll to the very end and test that the footer's last controls are not under a fixed bar or the cookie banner.
const REACH = `(async () => {
  document.documentElement.style.scrollBehavior = "auto";
  const res = [];
  for (const el of document.querySelectorAll("footer.site-f a, footer.site-f button")) {
    scrollTo(0, document.documentElement.scrollHeight); el.scrollIntoView({ block: "nearest" }); await new Promise((r) => setTimeout(r, 40));
    const r = el.getBoundingClientRect(); const x = r.left + Math.min(r.width / 2, 20), y = r.top + r.height / 2;
    const top = document.elementFromPoint(x, y);
    res.push({ control: (el.innerText || "").trim().replace(/\\s+/g, " "), inViewport: r.top >= 0 && r.bottom <= innerHeight, covered: !(top && (top === el || el.contains(top))), coveredBy: top && !(top === el || el.contains(top)) ? (top.closest(".sticky,.cookie") || top).className : "" });
  }
  return JSON.stringify(res);
})()`;

// Tab through the whole page: every stop must show the 3px ring and sit clear of the sticky bar.
async function keyboard() {
  // smooth scrolling is switched off for the test only, so each stop is measured where it comes to rest
  await ev("document.documentElement.style.scrollBehavior='auto'; scrollTo(0,0); document.activeElement && document.activeElement.blur()");
  const stops = []; const bad = [];
  for (let i = 0; i < 80; i++) {
    for (const type of ["keyDown", "keyUp"]) await send("Input.dispatchKeyEvent", { type, key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 }, S);
    await ev("new Promise(r=>setTimeout(r,30))");
    const s = JSON.parse(await ev(`(() => { const el = document.activeElement; if (!el || el === document.body) return "null"; const cs = getComputedStyle(el.closest(".svc-card") || el), r = el.getBoundingClientRect(); const bar = document.querySelector(".sticky"); const br = bar && getComputedStyle(bar).display !== "none" ? bar.getBoundingClientRect() : null; const inBar = !!el.closest(".sticky"); return JSON.stringify({ n: (el.getAttribute("aria-label") || el.innerText || "").trim().replace(/\\s+/g, " ").slice(0, 44), pos: el.dataset.ctaPos || "", inFooter: !!el.closest("footer.site-f"), ring: cs.outlineStyle + " " + cs.outlineWidth + " " + cs.outlineColor, hidden: !inBar && br ? r.bottom > br.top + 1 : false, off: r.bottom < 0 || r.top > innerHeight }); })()`));
    if (!s) break;
    const key = s.n + "|" + s.pos; if (stops.length && stops[0].key === key) break;
    stops.push({ key, ...s });
    if (!/^solid 3px/.test(s.ring)) bad.push("no ring: " + s.n);
    if (s.hidden) bad.push("under sticky bar: " + s.n);
    if (s.off) bad.push("off screen: " + s.n);
  }
  return { stops: stops.length, order: stops.map((s) => s.n + (s.pos ? " [" + s.pos + "]" : "")), footerStops: stops.filter((s) => s.inFooter).map((s) => s.n + " · " + s.ring), problems: bad };
}

async function load(file, w, h) {
  await send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 2, mobile: w < 700 }, S);
  const loaded = once("Page.loadEventFired", S);
  await send("Page.navigate", { url: pathToFileURL(path.join(HERE, file)).href }, S);
  await loaded;
  await ev("document.fonts.ready.then(()=>new Promise(r=>setTimeout(r,150)))");
}
async function png(name, clip) {
  const { data } = await send("Page.captureScreenshot", { format: "png", ...(clip ? { clip: { ...clip, scale: 1 }, captureBeyondViewport: true } : {}) }, S);
  writeFileSync(path.join(OUT, name + ".png"), Buffer.from(data, "base64"));
}

const checks = { note: "Automatic checks for homepage-v0 (draft), run " + new Date().toISOString().slice(0, 10) + " in headless Chrome on prototypes/homepage-v0/*.html by prototypes/homepage-v0/shots.mjs. contrastMin is the lowest text contrast found; smallTargets lists controls under 44px (inline links in running text are exempt, WCAG 2.5.8); deadLinks lists link targets that will not exist on launch day; placeholdersLeft lists unknown company values still shown as placeholders (must be empty before launch).", frames: {} };
for (const [name, file, w, h, mode] of FRAMES) {
  await send("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: "no-preference" }] }, S);
  await load(file, w, h);
  const c = JSON.parse(await ev(CHECK)); c.width = w;
  if (mode === "full") {
    const H = await ev("Math.max(document.documentElement.scrollHeight, innerHeight)");
    await send("Emulation.setDeviceMetricsOverride", { width: w, height: H, deviceScaleFactor: 2, mobile: w < 700 }, S);
    await ev("new Promise(r=>setTimeout(r,100))"); await png(name);
  } else if (mode === "first") { await png(name); }
  else if (mode === "hero") {
    const g = JSON.parse(await ev(`(() => { const s = document.querySelector(".sticky"); if (s) s.style.display = "none"; const r = document.querySelector("section.hh").getBoundingClientRect(); const st = document.querySelector(".story"); const sr = st && getComputedStyle(st).display !== "none" ? st.getBoundingClientRect() : null; const btn = document.querySelector(".hh-btns .btn-main").getBoundingClientRect(); return JSON.stringify({ y: r.top + scrollY, h: r.height, storyTop: sr && sr.top + scrollY, btnBottom: btn.bottom + scrollY, h1Bottom: document.querySelector(".hh-h1").getBoundingClientRect().bottom + scrollY, phoneBottom: document.querySelector(".hh-btns .btn-ghost").getBoundingClientRect().bottom + scrollY, overflowX: document.documentElement.scrollWidth > innerWidth }); })()`));
    c.hero = g; c.hero.aboveFold = g.phoneBottom <= h; await png(name, { x: 0, y: g.y, width: w, height: g.h });
  } else if (mode === "footer") {
    // hide the fixed phone bar for the crop: it is not part of the footer (frame 25 shows the two together)
    const g = JSON.parse(await ev(`(() => { const s = document.querySelector(".sticky"); if (s) s.style.display = "none"; const f = document.querySelector("footer.site-f").getBoundingClientRect(); return JSON.stringify({ y: Math.max(0, f.top + scrollY - 96), h: f.height + 96 }); })()`));
    await png(name, { x: 0, y: g.y, width: w, height: g.h });
  } else if (mode === "bottom") {
    c.footerReach = JSON.parse(await ev(REACH)); await ev("scrollTo(0, document.documentElement.scrollHeight); new Promise(r=>setTimeout(r,80))"); await png(name);
  }
  if (mode === "full" && /index|state/.test(file)) {
    await load(file, w, h); c.keyboard = await keyboard();
    await send("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: "reduce" }] }, S);
    await load(file, w, h);
    c.reducedMotion = JSON.parse(await ev(`JSON.stringify({ scroll: getComputedStyle(document.documentElement).scrollBehavior, transitions: [...new Set([...document.querySelectorAll("*")].flatMap((e) => [getComputedStyle(e).transitionDuration, getComputedStyle(e, "::after").transitionDuration]))], animations: [...new Set([...document.querySelectorAll("*")].map((e) => getComputedStyle(e).animationName))] })`));
  }
  checks.frames[name] = c;
}
writeFileSync(path.join(OUT, "checks.json"), JSON.stringify(checks, null, 1));
let bad = 0;
for (const [f, c] of Object.entries(checks.frames)) {
  const issues = [...c.smallTargets.map((t) => "tap<44: " + t), ...c.contrastFails.map((t) => "contrast: " + t), ...c.deadLinks.map((t) => "dead link: " + t), ...(c.horizontalScroll ? ["horizontal scroll"] : []), ...(c.h1Count !== 1 ? ["h1 count " + c.h1Count] : []), ...(c.headingsInFooter ? ["heading in footer"] : []),
    ...((c.footer && c.footer.clippedText) || []).map((t) => "clipped: " + t), ...((c.footer && c.footer.outsideFooter) || []).map((t) => "outside footer: " + t),
    ...((c.keyboard && c.keyboard.problems) || []), ...(c.footerReach || []).filter((r) => r.covered || !r.inViewport).map((r) => "not reachable at page end: " + r.control + " " + r.coveredBy),
    ...(c.reducedMotion && (c.reducedMotion.scroll !== "auto" || c.reducedMotion.transitions.some((t) => !/^0s(, 0s)*$/.test(t))) ? ["reduced motion not honoured: " + JSON.stringify(c.reducedMotion)] : [])];
  if (issues.length) { bad += issues.length; console.log(`${f}\n  ` + issues.join("\n  ")); }
}
console.log(`${Object.keys(checks.frames).length} frames, ${bad} issue(s) → ${OUT}`);
ws.close(); proc.kill();
