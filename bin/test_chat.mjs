// Offline test for humboldt-site/functions/chat.js — mocked Voyage, Pinecone and
// Claude; no network, no cost. Run: node bin/test_chat.mjs
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
const src = join(dirname(fileURLToPath(import.meta.url)), "..", "humboldt-site", "functions", "chat.js");
const tmp = join(mkdtempSync(join(tmpdir(), "chat-test-")), "chat.mjs");
writeFileSync(tmp, readFileSync(src));
const { onRequestPost } = await import(tmp);
const kvStore = new Map();
const kv = { get: async (k, t) => { const v = kvStore.get(k); return v == null ? null : (t === "json" ? JSON.parse(v) : v); },
             put: async (k, v) => { kvStore.set(k, v); } };
let lastClaudeBody;
globalThis.fetch = async (url, init) => {
  if (url.includes("voyage")) return Response.json({ data: [{ embedding: [0.1] }] });
  if (url.endsWith("/query")) return Response.json({ matches: [{ score: 0.8, metadata: { title: "T", text: "x", type: "law" } }] });
  if (url.includes("anthropic")) {
    lastClaudeBody = JSON.parse(init.body);
    if (!lastClaudeBody.stream) return Response.json({ content: [{ type: "thinking", thinking: "" }, { type: "text", text: "Hello " }, { type: "text", text: "world" }],
      usage: { input_tokens: 1000, output_tokens: 100, cache_read_input_tokens: 5000 } });
    const evs = [
      { type: "message_start", message: { usage: { input_tokens: 1000, cache_read_input_tokens: 5000, output_tokens: 1 } } },
      { type: "content_block_delta", delta: { type: "text_delta", text: "Hel" } },
      { type: "content_block_delta", delta: { type: "text_delta", text: "lo" } },
      { type: "message_delta", usage: { output_tokens: 100 } },
      { type: "message_stop" } ];
    const body = evs.map(e => `event: ${e.type}\ndata: ${JSON.stringify(e)}\n\n`).join("");
    // split into awkward chunks to test frame reassembly
    const bytes = new TextEncoder().encode(body);
    return new Response(new ReadableStream({ start(c) { for (let i = 0; i < bytes.length; i += 37) c.enqueue(bytes.slice(i, i + 37)); c.close(); } }));
  }
  throw new Error("unexpected " + url);
};
const KEY = "k".repeat(40);
const env = { RATE_LIMIT: kv, CHAT_ADMIN_KEY: KEY, PINECONE_C3PO_HOST: "https://c", PINECONE_HUMBOLDT_HOST: "https://h", ANTHROPIC_API_KEY: "x", VOYAGE_API_KEY: "v", PINECONE_API_KEY: "p" };
const waits = [];
const mk = (body, headers = {}) => ({ request: new Request("https://x/chat", { method: "POST", headers: { "Content-Type": "application/json", ...headers }, body: JSON.stringify(body) }), env, waitUntil: p => waits.push(p) });
const assert = (c, m) => { if (!c) { console.error("FAIL", m); process.exit(1); } else console.log("ok", m); };

// seed a pre-existing day record with tokens only (old format)
const day = new Date(Date.now() - 8 * 3600e3).toISOString().slice(0, 10);
kvStore.set("stats:day:" + day, JSON.stringify({ reqs: 1, in_tok: 1e6, cache_create_tok: 0, cache_read_tok: 0, out_tok: 0, egress_bytes: 0 }));

let r = await onRequestPost(mk({ query: "what is L-003?" }));
let j = await r.json(); await Promise.all(waits);
assert(j.answer === "Hello world", "joins text blocks, skips thinking");
assert(j._model === undefined, "public request gets no admin fields");
assert(lastClaudeBody.model === "claude-sonnet-5-5" && lastClaudeBody.thinking?.type === "between_tools", "default is Sonnet 5.5, thinking off");
assert(/^Current date and time: \w+day, /.test(lastClaudeBody.messages.at(-1).content), "date line leads user message");
assert(lastClaudeBody.system.length === 2 && lastClaudeBody.system[1].cache_control, "static time rule cached in system");
let d = JSON.parse(kvStore.get("stats:day:" + day));
const expect = 3.0 /* seeded: 1M in @ $3 */ + 0.06/1e6*80 + (1000*2 + 5000*0.1 + 100*10)/1e6 + 0.06/1e6*80;
assert(Math.abs(d.usd - expect) < 1e-9, "usd seeded from old tokens then priced at write time: " + d.usd.toFixed(6));

r = await onRequestPost(mk({ query: "q2", variant: "b" }));
await r.json(); await Promise.all(waits);
assert(lastClaudeBody.model === "claude-sonnet-5-5", "variant ignored without admin key");
r = await onRequestPost(mk({ query: "q3", variant: "b", now: "2026-01-05T12:00:00Z" }, { "X-Admin-Key": "wrong" }));
await r.json(); await Promise.all(waits);
assert(lastClaudeBody.model === "claude-sonnet-5-5", "variant ignored with wrong admin key");

r = await onRequestPost(mk({ query: "q4", variant: "b", now: "2026-01-05T12:00:00Z" }, { "X-Admin-Key": KEY }));
j = await r.json(); await Promise.all(waits);
assert(lastClaudeBody.model === "claude-sonnet-5-5" && lastClaudeBody.thinking.type === "between_tools", "admin variant b");
assert(lastClaudeBody.messages.at(-1).content.startsWith("Current date and time: Monday, January 5, 2026, 12:00 UTC."), "admin now replay");
assert(j._model === "claude-sonnet-5-5" && j._usage, "admin gets _model/_usage");

r = await onRequestPost(mk({ query: "q5", mode: "sources" }, { "X-Admin-Key": KEY }));
j = await r.json();
assert(j.sources.length > 0 && j.answer === "", "sources-only mode");

const before = JSON.parse(kvStore.get("stats:day:" + day)).usd;
r = await onRequestPost(mk({ query: "q6", stream: true }));
assert(r.headers.get("Content-Type").startsWith("text/event-stream"), "stream content-type");
const text = await r.text(); await Promise.all(waits);
const events = text.trim().split("\n\n").map(f => ({ ev: f.split("\n")[0].slice(7), data: JSON.parse(f.split("\n")[1].slice(6)) }));
assert(events[0].ev === "meta" && events[0].data.sources.length, "meta first with sources");
assert(events.filter(e => e.ev === "delta").map(e => e.data.text).join("") === "Hello", "deltas reassemble across chunk splits");
assert(events.at(-1).ev === "done", "done last");
const after = JSON.parse(kvStore.get("stats:day:" + day)).usd;
assert(Math.abs((after - before) - ((1000*2 + 5000*0.1 + 100*10)/1e6 + 0.06/1e6*80)) < 1e-9, "stream usage merged and charged");

// rate limit: public requests capped; admin bypasses
for (let i = 0; i < 25; i++) kvStore.set("rl:unknown", "20");
r = await onRequestPost(mk({ query: "q7" })); assert(r.status === 429, "public rate-limited");
r = await onRequestPost(mk({ query: "q8" }, { "X-Admin-Key": KEY })); assert(r.status === 200, "admin bypasses rate limit");
// unset secret never grants admin
env.CHAT_ADMIN_KEY = "";
r = await onRequestPost(mk({ query: "q9" }, { "X-Admin-Key": "" })); assert(r.status === 429, "empty secret never grants admin");
console.log("ALL PASS");
