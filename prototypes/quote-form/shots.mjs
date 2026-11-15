// Screenshots + automatic checks for the quote-form frames. No dependencies: drives the local Chrome over the
// DevTools protocol with Node's built-in WebSocket (Node 22+).
// Run: node prototypes/quote-form/shots.mjs [outDir]   (default: handoff/pages/quote-form/screens)
// Writes PNGs and checks.json (tap targets < 44px, inputs < 16px, horizontal overflow, text contrast < 4.5:1).
import { spawn } from "node:child_process";
import { readdirSync, mkdirSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.resolve(process.argv[2] || path.join(HERE, "../../handoff/pages/quote-form/screens"));
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
mkdirSync(OUT, { recursive: true });
const frames = readdirSync(HERE).filter((f) => /^\d\d.*\.html$/.test(f)).sort();
// desktop frames: only where 1440 differs in a way worth showing; hold frames prove 768 and 1024
const DESK = ["01", "05", "14", "26", "36", "41"];
const HOLD = { "05": [768, 1024], "36": [768] };

const proc = spawn(CHROME, ["--headless=new", "--remote-debugging-port=0", "--no-first-run", "--hide-scrollbars", "--disable-gpu",
  "--user-data-dir=" + mkdtempSync(path.join(tmpdir(), "qf-")), "about:blank"], { stdio: ["ignore", "ignore", "pipe"] });
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
await send("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: "reduce" }] }, S);

const CHECK = `(() => {
  const lum = (c) => { const a = c.map((v) => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * a[0] + .7152 * a[1] + .0722 * a[2]; };
  const parse = (s) => { const m = s.match(/rgba?\\(([^)]+)\\)/); if (!m) return null; const p = m[1].split(/[ ,\\/]+/).map(Number); return { c: p.slice(0, 3), a: p.length > 3 ? p[3] : 1 }; };
  const bgOf = (el) => { let stack = []; for (let n = el; n && n.nodeType === 1; n = n.parentElement) { const cs = getComputedStyle(n); if (cs.backgroundImage !== "none" && /gradient/.test(cs.backgroundImage)) { const m = cs.backgroundImage.match(/rgb\\([^)]+\\)/g); if (m) { const p = parse(m[m.length - 1]); stack.push(p); if (p.a === 1) break; } } const b = parse(cs.backgroundColor); if (b && b.a > 0) { stack.push(b); if (b.a === 1) break; } } let c = [255, 255, 255]; for (const b of stack.reverse()) c = c.map((v, i) => v * (1 - b.a) + b.c[i] * b.a); return c; };
  const vis = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none" && !el.closest(".vh,[hidden]"); };
  const name = (el) => (el.getAttribute("aria-label") || el.innerText || el.value || el.id || el.className || el.tagName).toString().trim().slice(0, 50);
  const out = { tap: [], input: [], contrast: [], overflow: document.documentElement.scrollWidth > innerWidth ? document.documentElement.scrollWidth : 0, h1: document.querySelectorAll("h1").length, h2: [...document.querySelectorAll("h2")].filter(vis).map((h) => h.innerText) };
  for (const el of document.querySelectorAll("a,button,input,textarea,select,summary,[role=option]")) {
    if (!vis(el) && !(el.matches("input") && el.closest("label"))) continue;
    if (el.matches(".vh")) continue;
    let box = el; if (el.matches("input[type=checkbox],input[type=radio]") && el.closest("label")) box = el.closest("label");
    const r = box.getBoundingClientRect(); if (!r.width) continue;
    const inline = el.matches("a") && getComputedStyle(el).display === "inline" && el.closest("p,.legal");
    if (!inline && (r.height < 43.5 || r.width < 43.5)) out.tap.push(name(el) + " " + Math.round(r.width) + "x" + Math.round(r.height));
    if (el.matches("input:not([type=checkbox]):not([type=radio]):not([type=file]),textarea,select") && parseFloat(getComputedStyle(el).fontSize) < 16) out.input.push(name(el));
  }
  const seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n; (n = walker.nextNode());) {
    if (!n.nodeValue.trim()) continue; const el = n.parentElement; if (!vis(el) || el.closest("svg,.overlay ~ *")) continue;
    const cs = getComputedStyle(el); const fg = parse(cs.color); if (!fg) continue;
    const dis = el.closest("[disabled],.dis,[aria-disabled=true]") || (el.closest("label") && el.closest("label").querySelector("input:disabled"));
    if (dis) continue;
    const bg = bgOf(el); const c = fg.c.map((v, i) => v * fg.a + bg[i] * (1 - fg.a));
    const l1 = lum(c), l2 = lum(bg); const ratio = (Math.max(l1, l2) + .05) / (Math.min(l1, l2) + .05);
    const big = parseFloat(cs.fontSize) >= 24 || (parseFloat(cs.fontSize) >= 18.66 && +cs.fontWeight >= 700);
    if (ratio < (big ? 3 : 4.5)) { const k = cs.color + "|" + bg.map(Math.round) + "|" + n.nodeValue.trim().slice(0, 30); if (!seen.has(k)) { seen.add(k); out.contrast.push(ratio.toFixed(2) + " " + k); } }
  }
  return JSON.stringify(out);
})()`;

async function shot(file, w, h, full, name, check) {
  await send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 2, mobile: w < 700 }, S);
  const loaded = once("Page.loadEventFired", S);
  await send("Page.navigate", { url: pathToFileURL(path.join(HERE, file)).href }, S);
  await loaded;
  await send("Runtime.evaluate", { expression: "document.fonts.ready.then(()=>new Promise(r=>setTimeout(r,120)))", awaitPromise: true }, S);
  let result = null;
  if (check) result = JSON.parse((await send("Runtime.evaluate", { expression: CHECK, returnByValue: true }, S)).result.value);
  if (full) {
    const { result: r } = await send("Runtime.evaluate", { expression: "Math.max(document.documentElement.scrollHeight, innerHeight)", returnByValue: true }, S);
    await send("Emulation.setDeviceMetricsOverride", { width: w, height: r.value, deviceScaleFactor: 2, mobile: w < 700 }, S);
    await send("Runtime.evaluate", { expression: "new Promise(r=>setTimeout(r,80))", awaitPromise: true }, S);
  }
  const { data } = await send("Page.captureScreenshot", { format: "png" }, S);
  writeFileSync(path.join(OUT, name), Buffer.from(data, "base64"));
  return result;
}

const checks = {};
for (const f of frames) {
  const base = f.replace(".html", ""), nn = f.slice(0, 2);
  const overlay = /arkusz/.test(f);
  // phone: full-height frame; the 844px viewport as well for sheets (overlay) and the first screen
  if (overlay || nn === "01") checks[f] = { 390: await shot(f, 390, 844, false, `${base}-390.png`, true) };
  if (!overlay) { const c = await shot(f, 390, 844, true, `${base}-390-full.png`, true); checks[f] = checks[f] || { 390: c }; }
  if (DESK.includes(nn)) checks[f][1440] = await shot(f, 1440, 900, true, `${base}-1440-full.png`, true);
  for (const w of HOLD[nn] || []) checks[f][w] = await shot(f, w, 1024, true, `${base}-${w}-full.png`, true);
  if (nn === "01") checks[f][320] = await shot(f, 320, 640, true, `${base}-320-full.png`, true);
}
writeFileSync(path.join(OUT, "checks.json"), JSON.stringify(checks, null, 1));
let bad = 0;
for (const [f, per] of Object.entries(checks)) for (const [w, c] of Object.entries(per)) {
  const issues = [...c.tap.map((t) => "tap<44: " + t), ...c.input.map((t) => "input<16px: " + t), ...c.contrast.map((t) => "contrast: " + t), ...(c.overflow ? ["overflow-x: " + c.overflow] : []), ...(c.h1 !== 1 ? ["h1 count " + c.h1] : [])];
  if (issues.length) { bad += issues.length; console.log(`${f} @${w}\n  ` + issues.join("\n  ")); }
}
console.log(`${frames.length} frames, ${bad} issue(s)`);
ws.close(); proc.kill();
