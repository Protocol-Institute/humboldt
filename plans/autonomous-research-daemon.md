# Plan: Autonomous Research Daemon

*Drafted: 2026-05-29. Implement in next session.*

Track 1 research work (retrieval runs, hypothesis testing, sensemaking synthesis,
opportunistic investigation) moves into the daemon. The daemon runs a research OODA
loop every 30 minutes, budget-gated at $5/day. Deep reads stay in Claude Code sessions
for now; the architecture leaves a clear slot for them in Phase 4.

---

## New Files

### `daemon/research_tick.py`

The research OODA loop. Entry point: `research_tick(client)`, called by
`discord_client.task_research_tick` via `run_in_executor`.

**Orient — `_orient() → ResearchState`**

Reads:
1. All `research/projects/*.md` — extract `phase:` and the `retrieval_queries` block
   (lives under the `## Sensemaking` or `## Valley` section). Candidate if:
   - phase is `valley` AND file contains a `retrieval_queries:` block → type `hypothesis_retrieval`
   - phase is `sensemaking` AND file has ≥3 bullet observations under `### Observations` → type `sensemaking_synthesis`
2. `bibliography/shallow-reads/` (last 14 days) — files containing `**Escalation:** escalate-to-deep`
   that are NOT already in `daemon/escalation-queue.json` → add to that file, add as candidate type `escalation_precursor`
3. Most recent `notebook/YYYY-MM-DD.md` — first 400 chars as live-thread context
4. Law + hypothesis inventory — IDs + one-line summaries from YAML files

Returns `ResearchState` dict:
```python
{
    "candidates": [
        {
            "type": "hypothesis_retrieval" | "escalation_precursor" | "sensemaking_synthesis" | "opportunistic",
            "target": "H-001" | "P-006" | "path/to/shallow-read.md" | None,
            "context": str,   # ≤200 char excerpt from project file or shallow-read
            "queries": [str], # retrieval queries if available; empty for opportunistic
        }
    ],
    "recent_notebook": str,
    "law_summary": str,
    "date": str,  # today ISO
}
```

**Decide — `_decide(state) → ResearchAct | None`**

```
1. candidates = state["candidates"]
2. if empty:
     add one synthetic {"type": "opportunistic", "target": None, "context": "", "queries": []}
3. if len == 1: return candidates[0]
4. if len > 1:
     prompt = build_interestingness_prompt(state, candidates)
     response = haiku_call(prompt)  # cheap: ~$0.001
     parse index from response → return candidates[index]
     on parse failure: return random.choice(candidates)
```

Interestingness prompt (Haiku): pass compressed state (law summary + recent notebook)
and numbered candidate list (type + target + context). Ask: "Which is most interesting
to investigate right now? Reply with just the number and one sentence of reasoning."

**Act — `_execute(act, client) → ActResult`**

*hypothesis_retrieval*: call `agent.investigate.run_investigation(act["queries"])` or
direct Pinecone query via VoyageAI embed + top-10 retrieval + Sonnet synthesis. Write
synthesis with explicit framing: "Testing [hypothesis]. Queries: [...]. Findings: [...]."

*escalation_precursor*: run retrieval on the shallow-read title as query. Write
"Preparing context for deep read: [title]. Retrieval findings: [...]." Mark entry in
`escalation-queue.json` as `retrieval_run: True, retrieval_date: today`.

*sensemaking_synthesis*: pass project file `### Observations` bullets to Sonnet.
Ask: "Given these observations about [question], what patterns emerge? What is the
simplest candidate law you can state?" Append result to project file's sensemaking
section. Write to notebook.

*opportunistic* (M-018): Sonnet call with full state context:
"Given this research state, propose one investigation question and one retrieval query.
Be specific — sharp enough that retrieval will either confirm or surprise you."
Then run that query. Label notebook section `[opportunistic]`.

Returns `ActResult`:
```python
{
    "notebook_section": str,   # markdown to append; includes header with timestamp
    "cost_usd": float,
    "act_type": str,
    "act_target": str | None,
    "candidate_laws": [str],   # any CL-xxx strings found in output
    "escalation_queued": str | None,
}
```

**Close — `_close(result)`**

1. Append to `notebook/YYYY-MM-DD.md`:
   - Header format: `## Research session — autonomous [ISO timestamp UTC]\n*Act: {act_type} | {target or "opportunistic"}*`
   - If file exists: append `\n\n---\n\n{header}\n\n{notebook_section}`
   - If not: create file with that as sole content
2. Log to `daemon/research-expenses.jsonl`
3. Git commit + push (scoped paths; see below)
4. Discord post: only if `notebook_section` contains a research finding or CL — skip pure
   housekeeping (e.g., escalation_precursor with no new content)

**Git commit in close:**

```python
_SAFE_PATHS = [
    "notebook/",
    "research/projects/",
    "research/laws/",
    "research/hypotheses/",
    "bibliography/shallow-reads/",
]
# subprocess: git add {paths} && git commit -m "Autonomous: {act_type} [{target}]" && git push
# On non-zero exit: log error + set state["pending_research_push"] = True
# On next tick: if pending_research_push, attempt push before running new act
```

---

### `daemon/research_expenses.py`

Separate from `costs.py` (which tracks all daemon API calls). Research expenses are the
record of research *sessions* — start/end time, what was worked on, how much it cost, and
what notebook entry it produced. This is the operator-facing log.

Functions:
- `log_expense(ts_start, ts_end, cost_usd, act_type, act_target, notebook_entry, candidate_laws_surfaced)` → appends to `daemon/research-expenses.jsonl`
- `today_research_usd() → float` — sum of today's research session costs
- `check_research_budget(limit=5.0)` — raises `BudgetExceeded` if today >= limit
- `summary(days=7) → str` — human-readable table for CLI

**`daemon/research-expenses.jsonl`** (committed; grows slowly — one line per research act):
```json
{"ts_start":"2026-05-30T09:00:00Z","ts_end":"2026-05-30T09:03:12Z","cost_usd":0.23,"act_type":"hypothesis_retrieval","act_target":"H-001","notebook_entry":"notebook/2026-05-30.md","candidate_laws_surfaced":0}
```

CLI output format (`humboldt research-expenses`):
```
Research sessions — last 7 days
────────────────────────────────────────────────────────────────
2026-05-30  hypothesis_retrieval   H-001       $0.23  09:00–09:03  notebook/2026-05-30.md
2026-05-29  opportunistic          —           $0.18  08:31–08:34  notebook/2026-05-29.md

Total 7d: $0.41   avg/day: $0.06   budget remaining today: $4.77
```

---

### `daemon/escalation-queue.json`

Local state file (gitignored). Tracks shallow-read escalations awaiting deep-read or
precursor retrieval.

```json
{
  "2026-05-29-short-term-gain-long-term-fragility.md": {
    "queued_date": "2026-05-29",
    "retrieval_run": false,
    "retrieval_date": null,
    "retrieval_summary": null
  }
}
```

Populated by `_orient()` on first seeing an escalated shallow-read.
Updated by `_execute_escalation_precursor()`.

---

### `methods/M-018-opportunistic-investigation.md`

When: no hypothesis, escalation, or sensemaking candidate is ready.

Process:
1. Assemble context: law/hypothesis inventory (one line each) + shallow-read titles from
   last 14 days + most recent notebook excerpt
2. Sonnet prompt: "You are Humboldt. Given this research state, what is the most interesting
   thread to pull right now? Propose: (1) one specific investigation question, (2) one
   retrieval query to pursue against the corpus, (3) one sentence on why this is interesting
   given your current state. Be specific enough that retrieval will either confirm or surprise you."
3. Run the proposed query via corpus retrieval
4. Synthesize findings
5. Write notebook section labeled `[opportunistic]`
6. If synthesis suggests a candidate law: note it as `CL-Opportunistic-N: statement`

Constraint: M-018 acts are labeled `[opportunistic]` in the notebook and expenses log.
They are lower-confidence than directed retrieval — they follow curiosity, not a
hypothesis under test.

---

## Modified Files

### `daemon/costs.py`

Add `category` parameter to `log_call()`:
```python
def log_call(operation, model, input_tokens, output_tokens, category="daemon") -> float:
    # add "category": category to the JSONL record
```

Add `today_usd(category=None)`: if category provided, filter records by that category.

The research budget check lives in `research_expenses.py` (separate concerns: costs.py
tracks API calls, research_expenses.py tracks research sessions).

### `daemon/discord_client.py`

Add alongside `task_notebook`:

```python
@tasks.loop(minutes=30)
async def task_research_tick(self):
    from daemon import research_tick as rt
    try:
        await self.loop.run_in_executor(None, lambda: rt.research_tick(self.client))
    except BudgetExceeded:
        logger.info("Research budget reached for today — skipping tick")
    except Exception as e:
        logger.error(f"Research tick failed: {e}", exc_info=True)

@task_research_tick.before_loop
async def before_task_research_tick(self):
    await self.wait_until_ready()
```

Start in `on_ready`: `self.task_research_tick.start()`

### `agent/humboldt.py`

Add two CLI commands:

- `research-tick [--dry-run]` — run one research tick manually; dry-run logs what it would
  do without executing the act or spending budget
- `research-expenses [--days N]` — print expense summary table

---

## Implementation Order

### Phase 1 — Infrastructure + dry run (implement next session)

1. `daemon/research_expenses.py` — expense logger, `check_research_budget()`, `summary()`
2. `daemon/research-expenses.jsonl` — empty file, committed
3. `daemon/escalation-queue.json` — empty `{}`, gitignored (add to `.gitignore`)
4. `methods/M-018-opportunistic-investigation.md` — method definition
5. `daemon/research_tick.py` skeleton:
   - `_orient()` — reads project files, detects escalations, returns state
   - `_decide()` — candidate selection + Haiku interestingness call
   - `_execute()` — **dry-run only**: logs what it would do, no API call, no write
   - `_close()` — **dry-run only**: logs notebook section it would write
   - `research_tick(client, dry_run=True)` — main entry, dry-run default
6. `discord_client.py` — wire `task_research_tick`, starts in dry-run mode
7. `humboldt.py` — add `research-tick --dry-run` and `research-expenses` commands
8. Run dry-run for a few cycles, verify orient/decide looks sane

### Phase 2 — Live execution

9. `_execute_hypothesis_retrieval()` — corpus retrieval + Sonnet synthesis
10. `_execute_escalation_precursor()` — retrieval + queue update
11. `_close()` — notebook append + git commit/push + Discord post
12. `research_tick(client, dry_run=False)` — enable live mode
13. Update `discord_client.py` to pass `dry_run=False`

### Phase 3 — Scavenging + sensemaking

14. `_execute_opportunistic()` — M-018 Sonnet call + retrieval
15. `_execute_sensemaking_synthesis()` — project file observation synthesis

### Phase 4 — Deep reads (future, separate design)

16. PDF text extraction cache (extend `agent/ingest.py` pre-processing)
17. M-003 daemon adaptation
18. `_execute_deep_read()`

---

## Design Decisions Captured

**Readiness inference**: no explicit `readiness:` field in project files. Inferred from
phase + presence of retrieval_queries block. Revisit if selection quality is poor.

**Supervised vs. unsupervised labeling**: daemon-written notebook sections carry explicit
header `## Research session — autonomous [timestamp]`. Operator-written entries have no
such header (or a different format). This makes the distinction visible in the notebook
without requiring a separate file.

**Budget throttle**: `check_research_budget()` in `research_expenses.py` is the sole
throttle. The 30-min loop is cheap to check (orient + decide ≈ $0.002 in Haiku); the
act is where budget is consumed. A day with nothing interesting to do will spend ~$0.01
total on orient/decide skips.

**Git safety**: commit is scoped to `_SAFE_PATHS` only. On push failure, set
`state["pending_research_push"] = True` and retry on next tick before running new act.
The daemon's existing `state.json` holds this flag.

**Discord post gate**: post only if notebook section contains substantive findings or
a candidate law. Escalation precursors and pure orient/decide runs do not post.

**$5/day budget**: separate from the existing daemon $5/day budget (Discord responses,
triage, shallow-reads). Total daily ceiling is therefore $10 until we reassess. Revisit
after a few weeks of data.
