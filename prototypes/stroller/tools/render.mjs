// Renders local HTML or SVG files to PNG at an exact pixel size with headless Chrome (DevTools protocol, no dependencies).
// Run: node prototypes/stroller/tools/render.mjs <file> <width> <height> <out.png> [transparent] [-- more jobs...]
// Several jobs can be chained, separated by "--". Used for the share image and the favicon / app-icon PNGs.
import { spawn } from "node:child_process";
import { writeFileSync, readFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const jobs = []; let cur = [];
for (const a of process.argv.slice(2)) { if (a === "--") { jobs.push(cur); cur = []; } else cur.push(a); }
if (cur.length) jobs.push(cur);
const proc = spawn(CHROME, ["--headless=new", "--remote-debugging-port=0", "--no-first-run", "--hide-scrollbars", "--disable-gpu", "--user-data-dir=" + mkdtempSync(path.join(tmpdir(), "rd-")), "about:blank"], { stdio: ["ignore", "ignore", "pipe"] });
const wsUrl = await new Promise((res, rej) => { let b = ""; proc.stderr.on("data", (d) => { b += d; const m = b.match(/ws:\/\/[^\s]+/); if (m) res(m[0]); }); setTimeout(() => rej(new Error("Chrome did not start")), 15000); });
const ws = new WebSocket(wsUrl); await new Promise((r) => (ws.onopen = r));
let id = 0; const pending = new Map(); const waiters = [];
ws.onmessage = (ev) => { const m = JSON.parse(ev.data); if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(m.error.message)) : res(m.result); } else if (m.method) for (const w of [...waiters]) if (w.method === m.method && w.sessionId === m.sessionId) { waiters.splice(waiters.indexOf(w), 1); w.res(m.params); } };
const send = (method, params = {}, sessionId) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
const once = (method, sessionId) => new Promise((res) => waiters.push({ method, sessionId, res }));
const { targetId } = await send("Target.createTarget", { url: "about:blank" });
const { sessionId: S } = await send("Target.attachToTarget", { targetId, flatten: true });
await send("Page.enable", {}, S);
for (const [file, w, h, out, transparent] of jobs) {
  await send("Emulation.setDeviceMetricsOverride", { width: +w, height: +h, deviceScaleFactor: 1, mobile: false }, S);
  await send("Emulation.setDefaultBackgroundColorOverride", transparent ? { color: { r: 0, g: 0, b: 0, a: 0 } } : {}, S);
  const svg = /\.svg$/.test(file);
  // an SVG is inlined into a blank page, so it scales to the exact size and keeps a transparent background
  const url = svg ? "data:text/html;charset=utf-8," + encodeURIComponent(`<body style="margin:0;background:transparent"><div style="width:${w}px;height:${h}px">` + readFileSync(file, "utf8").replace(/<svg /, '<svg style="display:block;width:100%;height:100%" ') + "</div>") : pathToFileURL(path.resolve(file)).href;
  const loaded = once("Page.loadEventFired", S); await send("Page.navigate", { url }, S); await loaded;
  await send("Runtime.evaluate", { expression: "document.fonts.ready.then(()=>new Promise(r=>setTimeout(r,200)))", awaitPromise: true }, S);
  const { data } = await send("Page.captureScreenshot", { format: "png", clip: { x: 0, y: 0, width: +w, height: +h, scale: 1 } }, S);
  writeFileSync(out, Buffer.from(data, "base64")); console.log(out, w + "x" + h);
}
ws.close(); proc.kill();
