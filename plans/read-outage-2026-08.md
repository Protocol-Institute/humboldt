# Read Outage — Pinecone egress exhaustion, 2026-08

**Status:** PLAN — awaiting supervisor approval
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

### Step 4 — prevention, before the September reset

1GB/month is a lot to burn; without a root-cause fix this recurs. Suspected driver:
`multi_retrieve` with `include_metadata=True` returns **full chunk text** on every match,
multiplied across namespaces × `top_k_each` × queries-per-call, on every composed Discord
reply and every daily review.

Already mitigated by the operator this session (`ce7f838`): `NS_BROAD_PLUS` trimmed 6→5
namespaces, dropping `bibliography` and `discord_links` from the per-reply path.

Remaining candidates, cheapest first:
- Stop shipping full text through metadata — return ids + scores, hydrate text from disk
  (the shallow-reads/notes are local files anyway). Likely the single largest win.
- Lower `top_k_each` on the high-frequency reply path (currently 5).
- Cache retrieval results per query hash — Discord threads re-query near-identical text.
- Add egress accounting to `daemon/costs.py` so spend is visible before it is exhausted,
  and surface it in the weekly digest.

### Step 5 — monitoring

Add read-availability to the weekly digest and `daemon status`, so the operator sees
"corpus reads: OFFLINE until 2026-09-01" rather than inferring it from odd output.

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
