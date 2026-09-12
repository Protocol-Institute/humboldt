# Developer TODO — Tracks 2 and 3

Infrastructure, persona, and template work. This is the *operator* layer — managing Humboldt as a project. Humboldt's own research agenda is in `research/agenda.md`.

Priority: **[H]** urgent, **[M]** soon, **[L]** when convenient.

---

## ⏸ RESUME HERE — session 35 paused 2026-09-12

**1. [H] Talk voice.** Blocked on one operator action: download macOS Premium/Enhanced
voices (System Settings → Accessibility → Spoken Content → System Voice → Manage Voices).
Full detail in `plans/talk-2026-09-23.md` §5.8. **Content changed since that note was
written** — the talk was rebuilt and deployed session 35 (§5.9): 15 slides → 14, old
audio deleted as mismatched. This is now a full re-voice of the new track from scratch,
not a resume of the old 12:12 render. **11 days to the talk as of this pause.**

**2. [H] Phase 4 — instrumentation. DONE (session 35, 2026-09-12).** All 13 registry
behaviors now call `funnel_log.behavior_visit` (the 7 previously-uninstrumented active
behaviors, plus a new 13th, `review`, for `daemon/conversation_review.py` +
`agent/person_notebook.py` — decision 4); `outputs` dict + `run_id` added per decisions
2–3; `mdp.yaml` edge `review → orient`; `analytics/op-behavior-map.yaml` remapped off
`behavior: null`. Verified live via `humboldt analytics utilization`. Drive-by finding,
not fixed: `daemon/presence.py:generate_person_notebook_entry` appears to be dead code
(no caller found) — left unmapped rather than silently deleted.
**Still open:** the flag heuristics (prune/split/stall) — the [OPUS] half of Phase 4 —
and the one number they need: the collapse threshold for the self-relative prune test.
Now calibratable against real data via `humboldt analytics utilization` once a few weeks
of `visits` accumulate under the new instrumentation; don't guess it before then.

**3. [M] Phase 5.** `plans/phase5-vm-cutover.md` is the runbook. §4.2 corrected
2026-09-09: deploy keys are **disabled org-wide** on Protocol-Institute, so it specifies a
scoped fine-grained PAT instead (matching what c3po landed on).

**4. [M] Reading page follow-up.** Six slugs still have two shallow-read files each, both
referenced, by two *different* bibliography entries — Discord ideas re-triaged later and
given a second entry. A duplicate-records question, not a duplicate-files one; laws may
cite either id, so which id survives is a supervisor call.

**5. [L] Site.** The 49 `read_depth: listed` sources are a real backlog signal — registered
but never read — now visible on `/reading/`.

---

## ⚠ Found + fixed (session 35, 2026-09-12): law records were invisible to corpus retrieval

While fixing the `research/laws/`/`research/hypotheses/` stale-path bugs above, found that
`agent/ingest.py` never got a `_law_chunks()` equivalent when the 2026-08 redesign retired
the old `_cl_chunks()`/`_h_chunks()`/`_f_chunks()` (and `_curiosity_chunks()`,
`_ds_chunks()`) — their source directories are archived, so they'd been silently
contributing zero chunks. **Every law created since the redesign merge (all 20) has been
absent from the `humboldt` Pinecone namespace** — `agent/induct.py`'s own comment
("the ingest embedded it") and its post-sweep "run `humboldt ingest`" instruction were
describing behavior that had quietly stopped. This means `respond`'s and `assess`'s
retrieval against the `humboldt` namespace has been searching notebook/notes/shallow-reads
only, never the law statements/mechanisms/examples themselves, since the merge.

**Fixed:** `_law_chunks()` added (one chunk per law, via `agent/laws.py`), wired into
`ingest_all()`; the five dead functions deleted rather than kept as always-empty dead
weight. Ran `humboldt ingest` — 43 upserted (20 new law chunks + 23 changed notebook/notes),
0 deleted. **Verified live**: a `multi_retrieve` query for "protocol ossification adoption
pressure" now returns an `L-001` law-type hit alongside the pre-existing notebook/shallow-
read hits.

**Not chased further:** the same query also returned a `deep_story` (`DS-001-ossification`)
hit — a vector embedded before the redesign, whose id isn't in `data/ingest_state.json`
(so the incremental cleanup can't see it to delete it). There may be other pre-redesign
orphan vectors (old `curiosity`/`candidate_law`/`hypothesis`/`falsification_monitor`/
`deep_story` types) sitting in the live `humboldt` index with no corresponding source file.
Not harmful — just redundant — but cleaning it up means enumerating the index directly
(`index.list()`) and deleting by id, which is a production-data operation worth doing
deliberately rather than as a side effect of a bug fix.

---

## 🎯 ON DECK — Redesign Phase 4 (analytics)

> Spec: `plans/redesign-2026-08.md` §8, §13.
>
> **Phase 3 [OPUS] work DONE 2026-09-01 (session 33).** Registry pruned 26 → 12
> behaviors; `mdp.yaml` v2 (22 directional edges, every one triggered); approval queue
> (`agent/approval_queue.py`, `behaviors/queue.yaml`); supervisor console
> (`agent/console.py` + `behaviors/console.html`, all six views, browser-verified).
> `humboldt console` / `humboldt queue …`; `behaviors admin` retired.
> **[SONNET] UI polish is the one Phase 3 item still open** — the console works; this is
> styling and form refinement, not completion.
>
> **[H] Phase 4 must start with instrumentation, not aggregation.** Only `induct` and
> `assess` call `funnel_log.behavior_visit` — the other 7 active behaviors have logged
> zero visits ever, so utilization, prune/split flags, and the supervisory loop are all
> reasoning from a 2-of-9 sample. Wire `behavior_visit` into intake, triage, shallow-read,
> deep-read, publish, respond, supervisory *before* building `analytics.py`, or Phase 4
> ships confident numbers computed from nothing.
>
> **Target dates set 2026-09-01** (operator decision — don't skip phases, but land Phase 5
> by the conference talk since the VM cutover gets demoed alongside it):
> Phase 3 by **09-06** → Phase 4 by **09-10** → Phase 5 (cutover + merge to `main` + first
> production deploy) by **09-16**, coinciding with `plans/talk-2026-09-23.md` Phase D. See
> `plans/redesign-2026-08.md` §13 for why that date is shared, not coincidental — the merge
> is also the talk's persistent-page production deploy (talk plan risk 3).
>
> Daemon unpaused 2026-08-10; normal Discord posting/querying has resumed. Re-pause
> manually if Phase 5 (server cutover = "off-laptop") work needs the daemon quiet again.

~~**`triage.py` / `reads.py` rework [OPUS].**~~ **DONE (session 29, 2026-08-10).**
`agent/funnel_context.py` (new) replaces the stale `research/laws/`/`research/hypotheses/`
readers; triage tags `content`/`meta` and creates `bib-NNNN` entries; shallow-read upgrades
`read_depth`, links laws, emits seeds. Live-tested end-to-end. Reference backfill also ran
for real (11 evidence sources across 7 laws → `bib-NNNN`). Both session-28 defects
(empty triggers, transient parse error) fixed in the same pass. See `dev-log.md` 2026-08-10.

~~**Next — [SONNET] session:** publish hook + law-event Discord plumbing.~~
**DONE (session 30, 2026-08-17).** `agent/law_notify.py` — queue/flush: one site deploy
per sweep, Discord announcements capped at 2/day, pause-gated, and gated on
`publish_site.is_production_deploy()`.

---

## 🎤 ON DECK — conference talk, 2026-09-23 (hard external deadline)

**Plan: `plans/talk-2026-09-23.md`.** "Some Candidate Laws of New Nature" — 20 min
available, 15 min targeted (separate 10-min Q&A slot), live deck + per-slide `say`-voiced
audio, track generated by Humboldt from `laws/*.yaml` and supervisor-edited. Covers the 7
tier-1 laws (L-001–L-007, with L-001/L-002 as expanded case studies) plus two new
metacognition slides; L-008–L-016 excluded as too speculative to present as candidate laws.

**Freeze-immune** — composition from law records is not retrieval, so Phase A proceeded now.

0. **[H] NEXT SESSION — Phase B′: publish the talk publicly, then refine it in public.**
   Operator decision 2026-09-02 (`plans/talk-2026-09-23.md` §5.6). Two priorities:
   (a) put the talk on the **live** site at `/talks/2026-09-23-new-nature/`, real domain;
   (b) iterate it over **multiple rounds of public review and comment**, replacing the
   single private supervisor edit pass that has been pending since session 32.
   **This reopens risk 3.** The production URL was scheduled to arrive with the Phase 5
   merge on 09-16 — too late for multiple rounds before 09-23. The talk deploy must be
   decoupled from the Phase 5 merge; recommendation is to cherry-pick the page onto
   `main` rather than merge the untested redesign early. Decide that first: it determines
   which branch `_build_talk_page()` targets. Also: build the page **text-first, without
   audio** (inverts §5.5's dependency chain), and pick a comment channel before round one.

1. ~~**[H] Phase A (by 08-25):**~~ **DONE (session 32, 2026-08-18)**, ahead of target.
   `brief.md`, `slides.yaml` (15 slides), `prompts/talk.md`, `agent/talk.py`
   (`draft`/`check`/`voice`/`time`) all built; `track.md` v1 generated and `check`-clean.
   **Operator's real edit pass (voice/substance, not mechanics) is next session** — what
   landed this session is budget-compliant but not yet reviewed for content.
2. **[M] Phase B (after 09-01):** evidence refresh; find a non-software example for L-006.
3. **[H] Phase C (by 09-13):** `_build_talk()` deck, voice audition, `talk voice`/`time`,
   trim to ≤ 15:00 (soft cap), design the Q&A-ingest step (new scope — see plan risk 7:
   live Q&A will run through the site chat, so the talk content needs to be in Humboldt's
   retrievable context before 09-23, timed so it doesn't leak early).
4. **[H] Phase D (by 09-16):** full rehearsal from the real URL. **Resolve the deploy
   question** — the deliverable is a URL and this branch has only ever deployed to Preview
   (see below); decide merge-to-main vs folder handoff vs preview alias.

---

## 🚨 ON DECK — corpus reads offline until 2026-09-01

**Plan: `plans/read-outage-2026-08.md`.** Pinecone's monthly *egress* cap is exhausted
(account-level, both indexes). Steps 1–3 landed session 30; **Steps 4–5 landed session 31
(2026-08-18)** — right-sizing (`REPLY_TOP_K`, `ASSESS_TOP_K`, `chat.js` top-Ks),
`agent/read_cache.py` + a KV cache in the Worker, `agent/read_egress.py` accounting, and
`task_read_budget_watch` (DMs the operator at 70% of the cap and on a trip).

**[H] Remaining: verify at the 2026-09-01 reset.** Every prevention measure was built
while reads were hard-blocked, so **none has run against live Pinecone traffic.** In the
days after the reset: run `humboldt read-status` and confirm (a) the ledger is actually
accumulating, (b) per-path attribution looks sane, (c) cache hits are non-zero once a
Discord thread runs. Also read the Worker's own counter — Python accounting cannot see it:
`npx wrangler kv key get --binding=RATE_LIMIT 'egress:2026-09' --remote`.

**[M] Watch for:** stale cache after a big c3po ingest (30d corpus TTL) — the fix is
`humboldt read-cache clear`. And the Worker's KV counter is read-modify-write, so it
undercounts under concurrency.

**Also found session 30 — public site is stale [H].** Production only ever deploys from
`main` (17 deployments); the whole `redesign-2026-08` branch has produced 8, **all
Preview** — including every automatic `publish_site` the daemon runs after a notebook
entry. So humboldt.protocol-institute.org has not reflected the redesign at any point, and
the session-26 note claiming otherwise is wrong. Deciding when to cut production over is a
Phase 5 call, not a bug fix.

**Track 1 queue:** supervisor review of L-012–L-016 (session-28 shape); assess the **open
counterexample on L-001** first when reads return — it is heavy-lift/supported, so it
outranks the five new exploration laws.

**FIXED (session 35, 2026-09-12):** `agent/references.py` read the dead
`research/hypotheses/`/`research/laws/` path — same bug class as the triage/shallow-read
and daemon-presence fixes. While fixing that, found and fixed three more live instances
of the same bug, all silently degrading to empty context rather than crashing:
`daemon/conversation_review.py:_load_slim_context()` (feeds the daily notebook-synthesis
prompt), `agent/person_notebook.py:generate_person_notebook_entry()` (feeds the
person-notebook prompt — the exact path Phase 4 just instrumented under `review`), and
`agent/humboldt.py:_load_inventory()`/`cmd_inventory()` (the `humboldt inventory` CLI
command, which had been silently printing "Law inventory is empty." regardless of the 20
real laws on file — `cmd_inventory` now delegates to `agent/laws.py:cmd_list`, the
already-correct replacement). All four now read live `laws/L-*.yaml` records via
`agent/laws.py`, matching `agent/funnel_context.py`'s pattern. Also corrected two stale
`research/laws/`/`research/hypotheses/` mentions in `cmd_investigate`/`cmd_deepread`'s
"next step" print statements. `agent/humboldt.py:cmd_assess_evidence` still references
the dead path but is explicitly marked LEGACY/unbound/not wired into the CLI dispatcher —
left alone. Not touched: the same stale paths in `README.md`, `ROADMAP.md`, `SOUL.md`,
`methods/M-*.md`, `_template/METHOD-template.md` — these are docs the redesign plan §10
already schedules for archival/rewrite, not a quick grep-fix.

**A fifth live instance, found after the above:** `daemon/discord_client.py:_active_hypotheses()`
read the dead `research/cl/` (Candidate Law) path and fed the result straight into
`task_feeds`'s relevance scoring — the single largest line in the cost ledger (`feed_triage`,
5,614 calls). Feed-relevance scoring has been running with an empty hypotheses list since
the redesign merged, silently, for the same reason as the rest of this bug class. Fixed
the same way: reads exploration/sensemaking-stage laws via `agent/laws.py` now.

**And the big one, same session:** `agent/ingest.py` had the identical bug at index-write
time, not just at prompt-read time — see the dedicated section below ("law records were
invisible to corpus retrieval"). All fixes in this bug class are now believed exhaustive
for `.py` files (confirmed via repo-wide grep for `research/(laws|hypotheses|cl|c|h|f|ds)`
outside `research/_archive/`); the remaining hits are documentation files, listed above.

**After Phase 2:** Phase 3 (graph + console) → Phase 4 (analytics) → **Phase 5 (server
cutover + quiet-mode Discord = off-laptop)**.

**No longer deferred:** the daemon is unpaused, so `task_notebook`'s incremental
Pinecone re-index and manual `humboldt ingest` are both live again. Watch cost/write-unit
usage for a session or two given the session-23 quota-exhaustion history, though the
incremental-ingest fix from that session should hold.

---

## Daemon bug fixed this session (2026-08-10, not in the redesign spec)

Operator reported a daily raw-title DM from feed monitoring; investigation found
`task_feeds` had **no pause gate at all** — a second live instance of the same
pause-completeness failure mode session 23 already fixed once elsewhere (a pause that
gates the paths named in the request, not every actual side effect).
Fixed: `task_feeds` still collects to inbox silently; a new pause-gated weekly
`task_feed_digest` sends one editorial-commentary DM instead. Along the way, found
`daemon/presence.py`'s `_slim_context()`/`_rich_context()` reading the same dead
`research/cl/` path as the funnel modules — every daemon Discord post (mentions, both
digests) was silently running with zero law context. Fixed; also patched the identical
bug in `daemon/capture.py`. **Live as of 19:49 UTC** — `daemon restart` (hot-reload, same
PID) then `daemon unpause`, both run this session.

**Stub-blocker convention:** When a Track 2 behavior is a stub and its absence is
preventing a specific Track 1 arc from advancing phase, annotate the item here with
`[BLOCKING: P-xxx — what move is blocked]` and mirror the signal in the arc's project
file (`blocking_behavior:` field) and in the *Behavior Blockers* bucket of
`research/agenda.md`. The urgency of building the behavior lives entirely in Track 2;
Track 1 diagnoses and records the block but does not re-label the arc as urgent.

---

## Track 2 — Persona and Infrastructure

### Autonomous research daemon — Layer 1 RUNNING; Layer 2 next [H]

Full plan at `plans/autonomous-research-daemon.md`.

**Layer 1 (COMPLETE — running since session 9):** `task_conversation_review` — daily Discord synthesis into notebook + reference promotion to `bibliography/references.yaml`. Has produced autonomous notebook entries on 2026-05-30 and 2026-05-31.

**Layer 2 — research_tick (NOT YET BUILT):** Build in this order.
*Pre-blocker:* orientation phase must use arc-position / phase-tempo scanning (see
`research/agenda.md` bucket structure), not queue-age. Will block autonomous heavy-lift
and valley investigation once P-006/P-007 are heavy-lift-ready. Not yet `[BLOCKING]`.*

**Phase 1 — Infrastructure + dry run:**
- `daemon/research_expenses.py` + `daemon/research-expenses.jsonl`
- `daemon/escalation-queue.json` (gitignored)
- `methods/M-019-opportunistic-investigation.md` (M-018 slot taken by Open Source Exploration)
- `daemon/research_tick.py` skeleton (orient + decide + dry-run act/close)
- Wire `task_research_tick` into `discord_client.py` (dry-run mode)
- Add `research-tick --dry-run` + `research-expenses` CLI commands

**Phase 2 — Live execution:** hypothesis_retrieval + escalation_precursor + notebook/git/Discord

**Phase 3:** opportunistic (M-019) + sensemaking_synthesis

**Phase 4 (future):** deep read daemon

---

### Curiosity promotion behaviors — stub → production

The curiosity collection (research/c/) accumulates fast and has no automated pathway toward Cheap Trick transitions. The exploration-phase stub behaviors address this but none are production yet.

- **[M]** **Backpocket Viewing (behavior-p7q)** — randomly sample 3–5 curiosities (weighted toward recently added and unconnected items), cross-reference with 1–2 active CL items, check for structural connections that could qualify as a cheap trick. Implementation sketch in registry: Haiku triage → escalate to Sonnet if cheap-trick-level. Output: connection note in notebook, new C item (connection only), or cheap-trick trigger opening a new DS arc. Start here — it's the primary curiosity → hypothesis promotion path.

- **[M]** **Curiosity Browsing (behavior-c7r)** — audit and implement alongside Backpocket Viewing; they share the curiosity-sampling logic.

- **[L]** **Audit remaining exploration/liminal stubs** — behavior-f8p (Canonical Domains), behavior-h4v (Field Trip), behavior-j6d (Bullshit Detector), behavior-w3x (Reading Prioritization), behavior-k7r (Explore-Exploit), behavior-s5j (Open Source Exploration), behavior-m7v (Cross-Training) are all liminal/exploration stubs. Review each: promote to production, defer, or descope. Do not build all at once — prioritize by what Track 1 actually needs next.

---

### Discord presence quality (next cluster)

- **[M]** **Proactive #new-nature engagement — disabled 2026-07-24, needs redesign before re-enabling** — `_new_nature_tick`'s self-initiated jump-into-conversation posting (`generate_new_nature_response`) was too chatty/redundant even at its 1/day cap; operator turned it off (`_PROACTIVE_ENGAGEMENT_ENABLED = False` in `daemon/discord_client.py`; capture still runs silently). Same underlying symptom as the notebook-announcement chattiness fixed the same session (per-entry → weekly digest). Before flipping back on: sharper judgment on whether Humboldt genuinely has something to add vs. generic engagement, probably corpus-grounded content requirements similar to `task_weekly_digest`, and a much longer natural gap between posts than 1/day.

- **[H]** **Conversation style tuning** — review actual #new-nature transcripts and identify what's off. Current symptoms: likely too formal / too long / too eager. Tune `_slim_context()` and `_rich_context()` prompts based on observed output. May require a dedicated prompt-tuning session with real examples.

- ~~**[H]** **Graceful shutdown + restart**~~ — **COMPLETE 2026-05-27.** `responded_mention_ids` prevents duplicate @mention responses across restarts; `last_clean_shutdown` / `last_startup` markers enable brief-restart detection; `close()` override saves clean-shutdown marker; `daemon restart` CLI sends SIGUSR1 for hot-reload; DM `!reload` from operator triggers same; feed DMs suppressed on restarts < 5 min offline; `daemon.pid` file tracks live PID.

- **[H]** **Idea and reference capture from Discord** — when Humboldt participates in a conversation, it should notice and save: (1) ideas or arguments that bear on its research hypotheses, (2) external papers/articles/links that participants cite. Save to `inbox/` as structured items. This is the "input → inventory" flow that was deferred at Discord launch. Design: detect in `on_message` and `task_new_nature` response path; use a lightweight extraction call (Haiku) to decide if anything is worth saving before responding.

- **[H]** **Discord user models + person notebook entries** — track recurring interlocutors persistently. Store interaction history in `daemon/people.json` (gitignored). When someone crosses a threshold (3+ interactions), write a notebook entry treating them as a research conversation: what they keep bringing up, how their thinking connects to active research. Use in `generate_mention_response` to personalize and acknowledge history.

- **[M]** **Richer self-context in Discord responses** — current `_rich_context()` includes laws and hypotheses but not the research agenda, LINEAGE.md in full, or recent open questions. Humboldt should be able to situate a conversation within its actual current thinking, not just inventory. Add agenda summary and current open questions to rich context.

### Daemon reliability — catch-up and restart safety

- **[H]** **Proper rewind-catchup architecture** — current approach (manual `state.json` cursor rollback + `force_full_scan` flag + daemon restart) is brittle and operator-heavy. The `_catchup_all_channels` method added 2026-06-06 works for one-off recovery but is not a design. Proper architecture: (1) per-channel cursor tracking in state (not a single `last_new_nature_message_id`), so catch-up is automatic across all channels on any restart; (2) `discord catch-up [--since DATE]` CLI command that runs a one-shot catch-up session without touching the live daemon cursor; (3) outage detection on startup — if offline > N hours, automatically run full scan rather than relying on operator to notice. The `!catchup` DM command is a stopgap; this should be zero-operator-action for ordinary restarts.

- ~~**[H]** **Duplicate notebook posts on restart**~~ — **FIXED 2026-06-09.** Root cause: `task_conversation_review` and `task_feeds` were saving stale state snapshots (loaded at task start, saved at task end) after async LLM calls, clobbering `last_notebook_commit` and `notebook_entries_posted` set by concurrent `task_notebook` runs. Fixed by applying the fresh-load pattern to both tasks' final saves.

- ~~**[H]** **Investigate Voyage API key 401 errors**~~ — **RESOLVED 2026-06-09.** Key is valid and ingest runs cleanly (1,427 vectors). The 401s were transient during the session 16/17 key migration window, not a persistent bug.

### Daemon infrastructure

- **[M]** **Daemon auto-restart on code changes** — currently requires manual kill + restart after every code change. Add `--reload` dev mode or use `watchdog` to restart on file change. Low priority for always-on deployment, higher priority during active development.

- **[L]** **Always-on machine deployment** — move daemon to a machine that doesn't sleep. Write systemd unit file; add `git pull` + restart on schedule so code updates deploy automatically.

- **[L]** **Thread support** — `task_new_nature` only reads main channel, not threads. Threads require explicit @mention currently. Decide whether to extend the proactive check to threads or leave @mention as the thread entry point.

---

### Notebook formatting

- ~~**[M]** **Linkable notebook entries**~~ — **COMPLETE 2026-05-27.** Each entry has `id="entry-YYYY-MM-DD"`, a `§` permalink on the date line, and a TOC nav block (newest-first) auto-generated at publish time. `notebook/index.yaml` is the canonical metadata store. Discord announcements now link directly to `humboldt-notebook.html#entry-YYYY-MM-DD` and create a discussion thread on the announcement message. Thread comments are harvested daily by `daemon/thread_farmer.py` → `inbox/`.

---

### Research time management (M-017)

- **[H]** **Wire M-017 secondary orientation fork into BOOTSTRAP.md** — M-017 defines a phase-position check ("what arc phase is this research thread in?") that should sit below the primary Bootstrap orientation. Add the reorientation question and phase vocabulary to `BOOTSTRAP.md` so Humboldt applies arc-position diagnosis before selecting session behavior. The specific question and its position in the Bootstrap sequence needs operator design.

- **[M]** **Promote Tempo candidate laws to hypothesis/law YAMLs** — CL-Rao-1 (Narrative Displacement), CL-Rao-2 (Doctrine Lock-In), CL-Rao-3 (Temporal Misalignment Failure) are in `bibliography/notes/rao-tempo.md` section 10. Review and decide which warrant promotion to `research/laws/` or `research/hypotheses/`.

- **[M]** **LINEAGE.md update for Tempo** — M-003 Phase 4 required after first read complete. Operator step.

---

### Deep reading methodology (M-003)

- **[H]** **Looser deep reading — exploration before extraction** — current M-003 prompt filters too aggressively for law candidates, producing narrow output. Deep reading should start with genuine open-ended engagement: what is the author's central problem? what is surprising? what doesn't fit? Candidate laws should *emerge* from engagement, not be the frame that organizes the reading. Revise M-003 prompt structure to lead with exploration, end with extraction.

- **[H]** **Synthesis behaviors — cross-read and cross-law reasoning** — no current mechanism for Humboldt to synthesize *across* deep reads (e.g., Cosmos + Simon + Hamming together) or to notice when candidate laws from different sources converge, conflict, or imply a more general law. Design: a `synthesize` CLI command that takes a set of reading notes and existing laws and runs a synthesis pass; also a periodic scheduled synthesis in the daemon.
  *Pre-blocker:* will block CL-Humboldt-3 (Substitution Invariance) and CL-Simon-5/6 sensemaking once those arcs open project files. Not yet `[BLOCKING]` — no project arc exists yet — but implement before those arcs reach valley.

---

### Behavior MDP — lifecycle and transition model

~~**[H]** **Behavior transition graph**~~ — **BUILT 2026-06-09 (session 18).**
- All 26 behaviors assigned to Double Freytag phases in `behaviors/registry.yaml`
- `behaviors/mdp.yaml`: 28 nodes (26 real + 2 virtual), 72 edges (34 within-phase bidir, 35 cross-phase, 2 cycle-back)
- `behaviors/admin.html`: D3.js admin visualization (vertical phase flow, hover tooltips, in-graph weight editor, supervisory analysis panel)
- `behaviors/log.jsonl`: behavior visit log (timestamp, behavior_id, phase, arc_id, note)
- `agent/behaviors.py`: HTTP admin server + CLI (graph, admin, log, supervisory)
- CLI: `humboldt behaviors admin | graph | log <id> | supervisory`
- Admin server: http://localhost:7878 — live weight editing → POST saves to mdp.yaml

**Remaining items (Track 2):**

- **[H]** **Brain page GUI improvements** — continue from session 18. Specific items to consider: pan-by-drag within the SVG (currently only scroll); edge label positioning cleanup (labels sometimes overlap nodes); phase band labels could be clickable to filter view; fit-to-screen button; URL hash to restore selected node/edge across refreshes. Evaluate after seeing it in use.

- **[M]** **Wire behavior logging into research sessions** — currently logging is manual (`humboldt behaviors log <id>`). Integrate into session wrapup checklist: log the behaviors actually used in the session. Eventually, BOOTSTRAP.md decision gate (boot-001) should log its output automatically.

- **[M]** **Apply Double Freytag to behavior lifecycle** — add `behavior_phase` field tracking the behavior's own maturation arc (design-uncertainty → prototype → production → monitoring). Assess each behavior in the registry. Connects to session 14 schema redesign.

- **[L]** **Wire behavior graph into BOOTSTRAP.md** — replace flat priority list with phase-position check: given current arc phase, which behaviors are applicable? Use MDP to recommend next behavior from current position. Requires boot-001 to be implemented.

- **[L]** **Heavy Lift and Retrospective behaviors** — design concrete behaviors for phases 4 and 5 to replace placeholders. Heavy Lift likely needs a synthesis behavior (cross-read + cross-law reasoning, see TODO synthesis behaviors item). Retrospective likely needs a monitoring + challenge behavior.

- **[L]** **Humboldt self-manages supervisory loop** — currently operator reviews `humboldt behaviors supervisory` output and applies suggestions manually. Eventually: daemon runs supervisory analysis weekly, writes suggestions to notebook, Humboldt reviews and applies on Track 1.

---

~~### humboldt-site publish pipeline [H]~~ **COMPLETE 2026-06-08**

`publish-site` CLI command added (`agent/publish_site.py`): runs `build.py` then
`wrangler pages deploy`. Old per-page publish commands (`publish`, `publish-research`,
`publish-reading`, `publish-architecture`) deprecated with error message directing to
`publish-site`. Daemon `notebook_watcher.py` task updated to call `publish_site(verbose=False)`.
CF credentials (`CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`) added to `.env` and
`.env.template`. `CLAUDE.md` CLI docs updated.

---

## Track 3 — Artificial Researcher Template

- **[M]** **Capability-outage pattern → template (from session 30).** Generalizable beyond
  Humboldt: any artificial researcher with a retrieval dependency needs (a) a typed
  outage exception that is *never* an empty result — an empty list reads as "nothing
  found" and hides the failure; (b) a breaker that trips itself on the provider's quota
  error and records the reset date; (c) a distinction between "don't speak" (operator
  pause) and "speak without grounding, and disclose it"; (d) refusal for the one operation
  whose whole value is evidence-testing. See `agent/read_budget.py` +
  `plans/read-outage-2026-08.md`.

- **[M]** **Metered-dependency accounting → template (from session 31).** Companion to the
  capability-outage item above: an outage needs a breaker, but *not recurring* needs
  metering. Three generalizable parts, none provider-specific: (a) right-size every
  automated fetch to what its consumer actually formats — the default failure is
  retrieving 3–6× what gets used, because breadth is tuned for recall by someone who
  cannot see the bill; (b) account for spend attributed by *calling path*, not just total,
  so a runaway consumer is findable rather than inferable; (c) alert while budget remains
  (threshold crossing), since every other signal reports spend after the fact. Also the
  reporting rule: when a second runtime spends from the same quota and you cannot see it,
  report the two separately — a combined number is confidently wrong. See
  `agent/read_egress.py` + `plans/read-outage-2026-08.md` §4.

- **[L]** **Researcher-presents-own-work pipeline → template (from session 31).** An
  artificial researcher eventually has to address a room. The generalizable shape:
  narration generated from the *records* rather than hand-written (so it regenerates when
  findings change and cannot drift from them), slides and script kept as separate
  artifacts (the slide is not the script), a lint pass for what a synthetic voice reads
  badly, and runtime *measured* from rendered audio rather than estimated. Revisit after
  the 2026-09-23 talk ships — do not templatize before it has survived a real audience.
  See `plans/talk-2026-09-23.md`.

- **[M]** Update `_template/` to reflect current architecture (IDENTITY/LINEAGE/MEMORY/METHOD/BOOTSTRAP) — `SOUL-template.md` is superseded.
- **[M]** Add ingest pattern to template — augmented chunk text (title+section prefix) is the generalizable design decision; capture in `_template/`.
- **[L]** Copy M-001 through M-003 to `_template/methods/` in generic form — strip PI specifics.
- **[L]** Write `_template/CLAUDE-template.md` — generic Claude Code setup for AR projects.
- **[L]** Extract as separate repo when stable — threshold: 5+ sessions, pattern tested, reviewed.
