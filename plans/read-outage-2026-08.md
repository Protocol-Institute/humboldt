# Read Outage — Pinecone egress exhaustion, 2026-08

**Status:** Steps 1–5 COMPLETE (Steps 1–3 session 30, Steps 4–5 session 31, 2026-08-18).
Remaining work is verification: the prevention measures were built while reads were
hard-blocked, so **none of them has run against live Pinecone traffic.** First real
exercise is the 2026-09-01 reset — watch `humboldt read-status` in the days after.
**Opened:** 2026-08-17 (session 30)
**Expected clear:** 2026-09-01 (monthly quota reset)

---

## 1. What happened

Pinecone reads are hard-blocked account-wide:

```
[429] Request failed. You've reached your egress limit for the current
month (1000000000 bytes). To continue reading data, upgrade your plan.
```

Verified live 2026-08-17 against both indexes. This is an **account-level** cap, so
`c3po` (corpus) and `humboldt` (own artifacts) are both affected.

What still works, and why this went unnoticed:

| Operation | State |
|---|---|
| `upsert` (ingest) | ✅ working — daily incremental ingest ran clean 08-13…08-16 |
| `describe_index_stats` | ✅ working — reports 5,970 / 30,697 vectors |
| `query` | ❌ **blocked** — every read path |

The initial diagnosis this session was "ingest stalled." That was wrong: writes were
never affected. Vector counts and stats calls look healthy precisely because neither
consumes egress. **Any future quota check must exercise `query`, not `describe`.**

This is the second read-quota exhaustion. 2026-07-22/23 hit a *different* cap — read
units (1,000,000/month), 5 occurrences logged. Two distinct monthly quotas can each
independently take reads offline.

### Reset timing

The error says "current month", so quotas clear at the month boundary → **2026-09-01**.
Exact reset timestamp is not visible from the API error; confirm in the Pinecone console
before relying on a precise hour.

---

## 2. Why it stayed invisible for weeks — the real defect

Zero egress errors appear in `daemon.err`. Not because reads weren't attempted, but
because **the read paths swallow failures and proceed with an empty result set.** An
empty list is indistinguishable from "the corpus genuinely has nothing on this," so
degraded output looks exactly like normal output.

Full read-call-site inventory (enumerated individually — per
`feedback_pause_completeness`, gating the paths named in the request rather than every
actual side effect is the failure mode that has already recurred twice here):

| # | Call site | On failure | Consequence |
|---|---|---|---|
| 1 | `daemon/discord_client.py:242` catch-up mentions | `except Exception: pass` | answers with `chunks=[]`, **silently ungrounded** |
| 2 | `daemon/discord_client.py:345` new-nature tick mention | `except Exception: pass` | same |
| 3 | `daemon/discord_client.py:446` `on_message` mention | `logger.warning` | logged, but **still answers ungrounded** |
| 4 | `agent/assess.py:71` promotion gate | returns `"(corpus retrieval unavailable: …)"` | **runs the promotion gate blind**, still emits PROMOTE/HOLD/DEMOTE |
| 5 | `agent/humboldt.py:75` `investigate` | unhandled | crashes with a traceback (visible — acceptable) |
| 6 | `agent/humboldt.py:150` `hypothesize` | unhandled | crashes with a traceback |
| 7 | `humboldt-site/functions/chat.js:339` public chat | `console.error; return []` | **public site answers visitors ungrounded** |

The two that matter most:

- **#4 `assess`** — the promotion gate's entire value is that verdicts are evidence-tested.
  Emitting a verdict with an empty evidence slot corrupts the encyclopedia's evidentiary
  basis while looking like normal operation. This is the worst internal harm.
- **#7 public chat** — external visitors get confident, ungrounded answers attributed to a
  research agent that claims corpus provenance. This is the worst external harm and
  should ship first.

**`induct` does not retrieve.** Confirmed empirically today: a full sweep created 5 laws
during the outage. So the funnel's *creation* stage keeps running; only the *promotion*
stage needs to stop. Worth preserving as a design property.

---

## 3. Design principle

> No output that would normally be corpus-grounded may be produced ungrounded **and
> silently**. It either does not get produced, or it is produced with the epistemic
> limitation stated in the output itself.

This is a **capability outage**, deliberately distinct from `daemon/pause.py`:

| | `daemon/pause.py` | read pause (new) |
|---|---|---|
| Means | "don't speak" | "you may speak, but you have no corpus" |
| Scope | daemon posting/querying | daemon **and** CLI **and** CF Worker |
| Trigger | operator, date-based | operator **or** auto-tripped by a 429 |

They compose: pause silences, read-pause degrades-with-disclosure.

---

## 4. Plan

### Step 1 — typed failure at a single chokepoint  `agent/retrieval.py`

Every Python reader funnels through `query_pinecone`. Add there:

- `class RetrievalUnavailable(Exception)` — carries reason + expected clear date.
- Gate at entry: if a read-pause is active, raise it **before** any network call.
- Wrap the live `.query()`: on `ApiError` 429 matching `egress limit` / `read unit limit`,
  auto-trip the breaker (Step 2), then raise `RetrievalUnavailable`.

**Raise, never return `[]`.** Returning empty is what made this invisible for weeks; a
distinct type forces every caller into an explicit decision. This mirrors the existing
$5/day cost circuit breaker.

### Step 2 — auto-tripping breaker  `agent/read_budget.py` (new)

Small module over `data/read-pause.json`:
`{"until": "2026-09-01", "reason": "pinecone egress limit (1GB/month)", "tripped": "<iso>"}`

- Not in `daemon/state.json` — CLI commands need it and it is not daemon-specific.
- `is_paused()` / `set_pause(until, reason)` / `clear()`, self-clearing once the date passes
  (same shape as `daemon/pause.py`).
- Auto-trip sets `until` = first of next month.
- CLI: `humboldt read-status`, `read-pause <date>`, `read-unpause`.

Consequence: the *next* exhaustion announces itself the same day instead of being found
by accident a month later.

### Step 3 — per-call-site handling (all seven, individually)

- **#1, #2, #3 Discord mentions** — replace both bare `except: pass` with a
  `RetrievalUnavailable` catch that sets a `corpus_offline=True` flag passed into
  `presence.generate_mention_response()`. The system prompt then instructs: answer only
  from on-disk law records / notebook / lineage, and state plainly that corpus retrieval
  is offline. Humboldt stays responsive and honest rather than mute or bluffing.
- **#4 `assess`** — refuse. Abort before the model call with a clear message. Add an
  explicit `--no-corpus` opt-out for a supervisor who deliberately wants a
  records-only assessment. Never silently verdict on an empty evidence slot.
- **#5, #6 `investigate` / `hypothesize`** — fail fast with the same clear message
  instead of a traceback.
- **#7 CF Worker `chat.js`** — separate runtime, cannot read `data/read-pause.json`.
  Detect `res.status === 429` in `queryNamespace`, distinguish it from other failures,
  propagate a flag → system-prompt banner + a visible notice in the chat UI.
  **Ship this first** (external exposure, and it is independent of the Python work).

### Step 4 — prevention, before the September reset  ✅ DONE 2026-08-18 (session 31)

The confirmed driver was over-fetching: every path pulled 3–6× more matches than its
consumer formatted, and each match carries up to 2000 chars of chunk text
(`agent/ingest.py`). Egress is `namespaces × top_k × queries`, and nothing measured it.

**The one candidate that had to be dropped:** "return ids + scores, hydrate text from
disk" cannot be done via a second Pinecone call. `Index.fetch()` has no `include_values`
switch — it *always* returns the 1024-float vector, which is larger than the chunk text it
would save. Query-then-fetch would have increased egress. Disk hydration only works where
the text is already local (the `humboldt` namespace), and there it is subsumed by caching.

Landed instead:

1. **Right-sizing** — matched `top_k` to what each consumer actually formats:

   | path | before | after | consumer uses |
   |---|---|---|---|
   | Discord reply (`REPLY_TOP_K`) | 5 ns × 5 = 25 | 5 × 3 = **15** | 4 own + 4 PI |
   | site chat (`chat.js`) | 6×8 + 10 = 58 | 6×4 + 8 = **32** | 8 + 8 |
   | `assess` (`ASSESS_TOP_K`) | 2 q × 6 ns × 8 = 96 | 2 × 6 × 4 = **48** | `chunks[:10]` |

   `investigate`/`hypothesize` were left alone: human-invoked, infrequent, and breadth is
   the point of them.

2. **Caching** — `agent/read_cache.py` (disk, `data/read-cache/`) and a KV cache in
   `chat.js`. Keyed per *namespace* on the Python side so callers with different namespace
   sets share what they have in common; 30d TTL for corpus namespaces, 1d for `humboldt`
   (re-ingested daily). A full cache hit also skips the Voyage embedding. Outages are
   never cached, so a hit can never mean "reads were down when we asked".

3. **Accounting** — `agent/read_egress.py` logs bytes per query to
   `data/read-egress.jsonl`, attributed by namespace *and* by calling path (`op=`), so a
   runaway consumer is findable rather than inferable. The Worker counts its own exact
   wire bytes into KV `egress:YYYY-MM`. Python's number is an estimate and a **lower
   bound** — it cannot see the Worker, which is why the two are reported separately
   rather than summed into a false total.

Escape hatch: `humboldt read-cache clear` — a 30-day corpus TTL means a query cached
before a large c3po ingest keeps answering without the new material.

### Step 5 — monitoring  ✅ DONE 2026-08-18 (session 31)

- `humboldt read-status` — breaker state, month-to-date egress vs the 1GB cap, per-
  namespace and per-path breakdown, cache savings, and the `wrangler` command for the
  Worker's KV counter.
- `humboldt daemon status` — a "Corpus reads" section, because the daemon can be running
  and talkative while having no corpus at all.
- `task_read_budget_watch` (daemon, 24h) — DMs the operator **once per month per event**
  on crossing 70% of the egress cap, and on the breaker tripping. This is the only signal
  in the system that fires while there is still budget left to protect; everything else
  reports spend after the fact. Pause-gated like every other Discord side effect, but
  always logged at WARNING so a paused daemon still leaves the evidence.

Not addressed: the digest surface. The weekly digest is a *public* #new-nature research
post, so operator telemetry does not belong in it — the DM watcher is the right channel.

---

## 5. Sequencing

1. Step 1 + 2 (chokepoint + breaker) — everything else depends on the typed exception.
2. Step 3 #7 (public chat) — highest external exposure, independent of the rest.
3. Step 3 #4 (`assess` refusal) — highest internal risk.
4. Step 3 #1/#2/#3 (Discord disclosure), then #5/#6.
5. Step 4 prevention — must land **before** 2026-09-01 or the reset just restarts the clock.
6. Step 5 monitoring.

## 6. What keeps working during the outage

`induct` (no retrieval), `ingest` (writes fine), the laws/bibliography CRUD and CLI,
`publish-site`, and the law-event notification path added this session. The encyclopedia
keeps accumulating; newly ingested vectors simply are not searchable until 09-01.
