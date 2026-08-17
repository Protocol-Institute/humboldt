# Status — Humboldt

Activity log for the Humboldt research agent. One entry per work session, most recent first.

---

## 2026-08-17 (session 30) — Law-event publish hook; Pinecone read outage + breaker

**Daemon PID:** 24438 (running, unpaused) — restarted at end of session; running this
session's read-outage fixes.

- **Corpus reads are OFFLINE until 2026-09-01.** Pinecone monthly *egress* quota (1GB)
  exhausted, account-level, both indexes. Writes/ingest unaffected — which is why it went
  unnoticed. `humboldt read-status` to check. Plan: `plans/read-outage-2026-08.md`.
- Read paths were converting the outage into an empty result set — Discord mentions and the
  public site chat answered ungrounded and silent; `assess` would have verdicted on an
  empty evidence slot. Fixed: typed `RetrievalUnavailable` (never `[]`), auto-tripping
  breaker (`agent/read_budget.py`), `assess` refuses (`--no-corpus` to override), Discord
  + site chat disclose the outage.
- **Law-event publish hook shipped** (`agent/law_notify.py`) — the TODO ON DECK item.
  Queue/flush: one site deploy per sweep, Discord announcements capped at 2/day.
- **Induction sweep created L-012–L-016** (16 laws, 9 exploration) + 9 evidence
  attachments, incl. an **open counterexample to L-001** (heavy-lift/supported — assess
  this first when reads return). All 16 validate.
- **Found (not fixed):** the public site has been stale for the whole redesign branch —
  production only ever deploys from `main`; all 8 branch deployments were Preview,
  including the daemon's automatic ones. `law_notify` now refuses to announce off a
  non-production branch; the cutover itself is a Phase 5 decision.

**Open:** plan Step 4 (egress prevention) before 09-01; plan Step 5
(read status in `daemon status`); supervisor review of L-012–L-016; `agent/references.py`
dead paths; `research/agenda.md` on pre-redesign vocabulary.

---

## 2026-08-10 (session 29) — Phase 2 triage/reads rework; daemon feed-DM bug found and fixed

Session: T2 (redesign implementation + operator-reported bug). Run on Sonnet 5 + an Opus
4.8 subagent.

**Daemon:** PID 1189 (running, unpaused). Restarted twice this session: once routinely
before this session began (was PID 1930, no action taken), and once deliberately at
19:49 UTC via `daemon restart` (SIGUSR1 hot-reload, same PID) to load today's fixes
before `daemon unpause` — otherwise unpausing would have resumed the old, buggy
`task_feeds` in memory. Pause (through 2026-08-15) cleared at operator request once the
fixes were confirmed live.

**Completed:**
- **Phase 2 [OPUS] `triage.py`/`shallow_read.py` rework — the ON DECK item, done.** New
  `agent/funnel_context.py` replaces the stale `research/laws/`/`research/hypotheses/`
  readers with `laws/*.yaml` + `laws/seeds/`. Triage tags `content`/`meta` and creates
  `bib-NNNN` entries at `read_depth: listed`; shallow-read upgrades to `shallow`, links
  laws, emits seeds. Live-tested end-to-end ($0.51 spend): 3 triaged → 2 shallow-read →
  1 seed (`seed-058`) → picked up by `induct` as L-004 evidence. Both session-28 defects
  fixed: `induct` now requires both lifecycle triggers (prompt change + hard-to-miss
  placeholder fallback), `assess` gets a one-shot parse retry. Reference backfill run for
  real: 11 evidence sources across 7 laws resolved to `bib-NNNN` ids. All 11 laws still
  validate; bibliography at 932 entries. Reviewed in full before accepting — cleaned up
  one stray artifact the subagent left (a copied Claude-memory file in a bogus
  `humboldt/memory/` dir) and patched one bug it flagged but didn't fix (`daemon/capture.py`
  reading the same dead `research/cl/` path — same fix as below, done inline).
- **Daemon bug: operator reported a daily raw-title DM ("~49 new items from feeds") they
  wanted replaced with a weekly editorial digest.** Root cause was *not* the known
  `task_weekly_digest` mechanism (never fired — daemon's been paused almost continuously
  since 07-24) but a second, separate bug: `task_feeds` DMs the operator immediately every
  12h with **no pause gate at all** — a recurrence of the exact pause-completeness failure
  mode session 23 already fixed once elsewhere. Fixed: `task_feeds` still collects
  silently; a new pause-gated, weekly `task_feed_digest` sends one editorial-commentary
  DM instead (`presence.generate_feed_digest_post()`). Also fixed
  `_slim_context()`/`_rich_context()` in `daemon/presence.py` — same dead `research/cl/`
  path, meaning **every** daemon Discord post (mentions, both digests) was silently
  running with zero law context.
- **Daemon restarted + unpaused (19:49 UTC).** All of the above is live: PID 1189 hot-
  reloaded via `daemon restart`, then `daemon unpause` cleared the through-08-15 pause at
  operator request. Normal Discord posting/querying has resumed.

**Open (next session):**
- `agent/references.py` still reads the dead `research/hypotheses/`/`research/laws/` path
  (still-live code — `conversation_review.promote_inbox_links`, imported by
  `bibliography.py`). Flagged, not fixed.
- Watch the first live `task_feed_digest` and `task_weekly_digest` firings (both due
  ~7 days out, both correctly skip posting on their first-ever run) to confirm the fixes
  hold up outside the test harness.
- TODO.md next: [SONNET] publish hook + law-event Discord plumbing, then Phase 3.
- Track 1 research is overdue — several sessions running have all been T2.

---

## 2026-08-03 (session 28) — Supervisor review + first assess pass on L-008–011

Session: T2 (redesign — supervisor review). Run on Opus 4.8.

**Daemon:** PID 1930 (running; paused through **2026-08-15**). Unchanged — still
old-design code, on-laptop, not wired to the new engines (Phase 5). Off-laptop not started.

**Completed:**
- Supervisor review of the induct sweep's output (L-008–011): all four **accepted** at
  exploration/speculative. Provenance verified — L-009 (Tan) and L-011 (Tembine) are
  deep-read-confirmed, not abstract-built.
- **L-010 statement rewritten** — it overclaimed seed-050 (the nonmonotonicity vanishes
  under co-optimized signaling); now design-conditional, falsification aligned, linked
  `related: [L-006]`. L-011 Venerina example flagged weakly coupled. Review history entry
  + `advance`/`challenge` triggers set on all four (they were created empty).
- **First real `assess` pass** on all four → all **HOLD** (correct for fresh speculative
  laws). L-009 gained an OPEN counterexample (protocol races are empirically asymmetric).
  Each law now carries an executable gap in `open_questions`. 5 events → events.jsonl.
- Two Phase-2 defects logged (empty-triggers from induct; assess parse-retry + history
  truncation) and the next-session build plan captured at the top of `TODO.md`.
- 11 law records valid.

**Open (next session):**
- Phase 2 [OPUS]: `triage.py`/`reads.py` rework + fold in the two induct/assess fixes.
- Then [SONNET]: publish hook + law-event Discord plumbing.
- Extend 08-15 pause if Phase 5 (server cutover) will slip; `humboldt ingest` deferred.

---

## 2026-08-02 (session 27) — Phase 2 [OPUS]: induct + assess engines; first live sweep (L-008–L-011)

Session: T2 (redesign implementation). Run on Opus 4.8.

**Daemon:** PID 1930 (running; paused through **2026-08-15**). Unchanged — still old-design
code, not wired to the new engines (Phase 5).

**Completed (Phase 2 [OPUS]):**
- `agent/induct.py` (funnel stage 5) + `agent/assess.py` (stage 6/8) — the funnel engines
  consuming `prompts/induct.md` / `prompts/assess.md`, applying verdicts via the Phase-1
  `laws.py` stage machine. `--dry-run` on both; `assess --all` sweep.
- `agent/funnel_log.py` — event spine: behavior visits → `behaviors/log.jsonl`, law events
  → `analytics/events.jsonl` (new dir).
- `synthesizer.synthesize_full()` — shared funnel call path (budget-checked, cost-logged,
  600s timeout).
- CLI: `humboldt induct` / `humboldt assess <L-NNN>|--all` wired + USAGE; legacy `assess`
  unbound.
- Fixed a latent `bibliography.link_law` ruamel/PyYAML corruption bug (would have broken
  the bibliography on first live induct) and an imported-law `source` capture gap
  (`induct.md` + engine).

**First live induction sweep** (operator-approved): created **L-008–L-011** (2 discovered,
2 imported w/ provenance), 12 evidence attachments (incl. OPEN counterexamples on L-001 &
L-007), 3 seeds consumed, 43 left. All 11 law records valid.

**Open (next session):**
- Supervisor review of L-008–L-011; `assess` the survivors.
- `humboldt ingest` (Pinecone write — deferred past pause window) when ready.
- Remaining Phase 2: `triage.py`/`reads.py` rework [OPUS]; publish hook + law-event
  Discord [SONNET].
- Phase 5: gate induct/assess through the pause when daemon-wired.

---

## 2026-08-01 (session 26) — Phase 1 [SONNET] site pages: /laws/, /bibliography/, extended /reading/

Session: T2 (redesign implementation). Run on Sonnet 5.

**Daemon:** PID 1930 (running; paused through **2026-08-15**). Unchanged this session —
still old-design code, not touched.

**Completed (Phase 1 [SONNET]):**
- `agent/publish_laws.py` (new) — `/laws/` encyclopedia page: stage-grouped law cards,
  JS stage filter, expandable full record, reverse-indexed bibliography citations per law.
- `agent/publish_bibliography.py` (new) — `/bibliography/` page: all 929 entries,
  depth/kind filters + live search, linked to `/reading/` and `/laws/`.
- `agent/publish_reading.py` (extended) — `/reading/` now also renders 916 shallow reads,
  date-grouped and collapsible, alongside the existing 71 deep-read cards.
- `humboldt-site/build.py` — nav rewired (`/research/` → `/laws/` + `/bibliography/`);
  dead `_build_research()` removed (its source dirs were archived session 25 and would
  have crashed the next `publish-site`); chat system prompt's law inventory rebuilt from
  `laws/*.yaml` (was silently reading the same archived dirs → empty inventory).
- Built + smoke-tested locally (local HTTP server + browser pass on all six pages).
  Deployed (operator-approved) — fixed `agent/publish_site.py`'s hardcoded system-Python
  interpreter (broke on the new `ruamel.yaml` dep, venv-only) along the way. `/laws/`,
  `/bibliography/`, `/reading/` verified live on humboldt.protocol-institute.org.

**Open (next session):**
- **Phase 2 [OPUS]:** `induct.py` + `assess.py` engines.
- `ingest.py` chunk types still not extended to laws/seeds/bibliography.
- Extend pause past 2026-08-15 if Phase 5 cutover slips.

---

## 2026-08-01 (session 25) — Phase 1 output layer built; research tree migrated

Session: T2 (redesign implementation). Run on Opus 4.8.

**Daemon:** PID 1930 (running; paused through **2026-08-15**). Still old-design code;
the new modules are CLI-only and not yet wired into the daemon. Reads this working tree
(now on branch `redesign-2026-08`, mid-migration) — verified it degrades gracefully.

**Completed (Phase 1 [OPUS]):**
- `agent/laws.py` — law record CRUD, validation, Double Freytag stage machine
  (one-forward advance, targeted cycle-back, confidence capped by stage), append-only
  history; ruamel round-trips preserve folded scalars + `# why` comments. All 7 laws valid.
- `agent/bibliography.py` + `bibliography/bibliography.yaml` — **929** canonical entries
  migrated from references (39 listed) + shallow reads (819) + deep notes (71); dedup;
  221 law backlinks; 3 meta reads. `humboldt laws …` / `humboldt bib …` CLI wired.
- Installed `ruamel.yaml` into the venv.

**Completed (mechanical migration, operator-approved):**
- 47 `research/c/` items → `laws/seeds/seed-NNN-*.yaml` (+ README).
- Old `research/` tree (`cl/ ds/ theories/ f/ h/ questions.md`) → `research/_archive/`
  via `git mv` (69 renames); only `agenda.md` live.

**Open (next session):**
- Phase 1 [SONNET]: `/laws/`, `/bibliography/`, extended `/reading/` site pages — the
  public site still shows the old design until these ship
- Phase 2 [OPUS]: `induct.py` + `assess.py` engines (Fable's prompts already in `prompts/`)
- `ingest.py` chunk types not yet extended to laws/seeds/bibliography
- Extend pause past 2026-08-15 if Phase 5 cutover slips

---

## 2026-08-01 (session 24) — Redesign designed + Fable pre-work; exe.dev VM provisioned

Session: T2 only. Run on Fable; subsequent implementation sessions should use Opus/Sonnet.

**Daemon:** PID 1930 (running; paused through **2026-08-15** — extended this session).
Note: the working tree is now on branch `redesign-2026-08`; the live daemon reads this
tree (see dev-log caution).

**Completed:**
- Full-system redesign specified in `plans/redesign-2026-08.md` — funnel → law
  encyclopedia, KPI = law accumulation rate; six phases with [FABLE]/[OPUS]/[SONNET]
  build-tier markup; key decisions locked (see doc §1)
- Fable pre-work committed on branch (d703fd2): `laws/_schema.yaml`, `laws/L-001..007`
  (migrated from CL/T/DS), `prompts/induct.md`, `prompts/assess.md`,
  `behaviors/definition-rubric.md`
- exe.dev onboarding: SSH key + config, VM `humboldt.exe.xyz` created (Phase 5 target),
  `Code/warnings-exe.md` policy written, unused personal VM deleted
- Branch `redesign-2026-08` pushed; Claude memory updated (`project_redesign_2026_08`)

**Open (next session):**
- Phase 1 implementation on branch (Opus): `laws.py`, `bibliography.py` + bib migration;
  (Sonnet): encyclopedia/bibliography/reading site pages, research/ archival, seeds move
- Inbox backlog (519 feed + 40 discord) stays parked until Phase 6 shakedown
- Extend pause if Phase 5 cutover slips past 2026-08-15

---

## 2026-07-24 (session 23) — Weekly digest, offline pause, Pinecone write-burn fix

Session: T2 only.

**Daemon:** PID 1930 (running). Hot-reloaded four times.

**Completed:**
- `task_notebook` no longer posts per-entry Discord announcements — new `task_weekly_digest` posts one synthesized digest every 7 days instead
- `_new_nature_tick` proactive engagement posting disabled (`_PROACTIVE_ENGAGEMENT_ENABLED = False`) — too chatty even at 1/day; capture unaffected
- New `daemon pause <YYYY-MM-DD>` / `daemon unpause` CLI (`daemon/pause.py`) — offline for posting/querying/Pinecone-writes through a date; effective immediately, no restart needed
- Reviewed and merged PR #1 (from a parallel agent session): `ingest_all()` was re-embedding/re-upserting the full 5,142-chunk corpus on every notebook commit, burning the account's Pinecone write-unit quota (2,000,000/mo, shared with c3po) and read-unit quota (1,000,000/mo) well before month-end. Now content-hash incremental (`data/ingest_state.json`)
- Caught and fixed a gap where the first pause implementation didn't cover the actual write path (`task_conversation_review` → `task_notebook` → `ingest_all()`) — a 96-vector write was attempted (429'd against the exhausted quota, nothing written) before the fix landed
- ARCHITECTURE.md, CLAUDE.md, TODO.md updated for all of the above
- Daemon currently paused until 2026-08-01

**Open (next session):**
- Confirm Pinecone quota is clear before unpausing
- Resume interrupted inbox processing (420 feed + 39 discord-idea items pending, triage reports exist for resumption)
- Run `humboldt ingest` once safe to confirm the incremental fix on the real corpus
- Redesign proactive engagement before re-enabling (see TODO.md)
- Track 1 research overdue — no movement on heavy-lift-ready arcs (T-001, T-002) in a month

---

## 2026-06-25 (session 22) — Daemon presence tuning; website restructure

Session: T2 only.

**Daemon:** PID 3839 (running). Hot-reloaded twice during session.

**Completed:**
- Removed thread creation from `task_notebook` — notebook posts now plain channel messages (session 21 had only removed threads from `_new_nature_tick()`)
- Added 1/day rate limit on proactive `_new_nature_tick()` posts (`last_proactive_post_date` in state)
- Sharpened `generate_new_nature_response()` prompt: requires concrete new research finding, not general engagement
- Chat page made landing page at `/`; About moved to `/about/`; chat page has intro + section nav links
- Curiosities section on research page: 47-item browsable carousel (3/page) replaces table rows; cards include type badge, excerpt, provenance link to GitHub

**Open (next session):**
- Implement Backpocket Viewing (behavior-p7q) — curiosity → cheap trick promotion
- Audit exploration/liminal behavior stubs

---

## 2026-06-24 (session 21) — Discord presence fix; inbox triage + shallow-read

Session: T2 only.

**Daemon:** PID 917 (running). Hot-reloaded twice during session.

**Completed:**
- Fixed dead research context paths: all Discord presence code (presence.py, capture.py, discord_client.py) was reading from nonexistent `research/laws/` and `research/hypotheses/` dirs since session 14 schema migration. Now reads from `research/cl/`. Root cause of repetitive/ruminative Discord posts.
- `_slim_context()` now includes 3 recent notebook entries + 6 recent shallow-read titles
- Removed proactive thread creation from `_new_nature_tick()` — threads only on @mention responses
- Inbox triage: feed (117 → 91 shallow, 26 discard) + discord (75 → 56 shallow, 19 discard)
- Shallow-read pass: 23 escalations (thoughtfolio protocol theory series, Mesh Inference, Recursive Joint Simulation, Milgram/LLMs, Brouwerian assertibility)
- Ingest: 4,377 → 5,105 vectors

**Open (next session):**
- Add today's 23 escalations + prior 36 to deep-read hopper
- CL-001 transition trigger assessment
- CL-003 targeted investigation
- Review batch notes for CL-002/Q-011/Q-012 connections

---

## 2026-06-20 (session 20 closeout) — Batch complete; ingest run

Session: T1 closeout only.

**Daemon:** PID 917 (running). Batch-deepread complete (was PID 90871).

**Completed:**
- batch-deepread: 61 papers, 62 verdicts; key finding: over-claim = polarity inversion on adversarial/refutation papers
- `humboldt ingest`: 3,595 → 4,377 vectors
- Notebook entry, README updated, dev-log written

**Open (next session):**
- Add 36 escalations (from 2026-06-18 shallow reads) to deep-read hopper
- CL-001 transition trigger assessment
- CL-003 targeted investigation
- 2402.08128, 2512.07526, 2602.22041 flagged for CL-002/Q-011/Q-012 follow-up

---

## 2026-06-18 (session 20) — Inbox clearing; backpocket behavior; batch deep-read

Session: Track 1 + Track 2.

**Daemon:** PID 917 (running). Batch-deepread PID 90871 (running in background — 61 papers).

**Completed:**
- Inbox cleared: 313 items → 36 escalations; humboldt namespace 2,460 → 3,595 vectors
- 28 new arXiv papers downloaded; library now 92 PDFs
- Backpocket Viewing behavior (behavior-p7q) added; Q-001–012 questions file created
- batch-deepread CLI implemented with verdict training loop (separate Haiku call per paper)
- Three API bugs fixed: model param, httpx timeout (600s), max_tokens (4096 → 16000)
- Notebook entry written; dev-log entry written
- Hopper: Rittel, Kuhn, Iverson marked complete

**Open (next session):**
- Review batch-deepread output (PID 90871 still running; 61 papers)
- Run `humboldt ingest` after batch completes
- Add 36 new escalations to deep-read hopper
- CL-001 transition trigger assessment
- CL-003 targeted investigation
- CLAUDE.md: update vector count to 3,595

---

## 2026-06-13 (session 19) — Inbox clearing; PDF library build; deep reads launched

Session: Track 1 + Track 2.

**Daemon:** PID 917 (running). $2.84 cumulative cost at session start.

**Completed:**
- Inbox cleared: 316 items → triage-feed (156 shallow, 60 discard) + triage-discord (64 shallow, 36 discard) → 220 shallow reads; 2460 vectors in humboldt namespace
- 29 feed escalations + 2 Discord escalations added to deep-read hopper
- 36 arXiv papers + Rittel & Webber + Kuhn downloaded; library now 43 PDFs
- Protocolized Substack added to daemon feeds
- Rittel & Webber deep read complete: C-015–022, reading notes written
- Kuhn deep read: IN-FLIGHT (agent still running; C-025–044 reserved; notes not yet written)
- Papers queue: IN-FLIGHT (agent still running; C-045–049 written; ~27 papers remain)
- Session 19 notebook entry written + notebook README index updated

**Open (next session):**
- Review + commit output from Kuhn agent + papers queue agent
- Run `humboldt ingest` after reviewing new C items
- CL-001 transition trigger assessment (Rittel & Webber result materially strengthens valley case)
- CL-003 targeted investigation (still stagnant)
- Brain page GUI improvements ([H])
- Rewind-catchup architecture ([H])

---

## 2026-06-09 (session 18) — Behavior MDP graph; daemon stale-state fix; brain page

Session: Track 2 only.

**Daemon:** PID 917 (launchd, running). Hot-reloaded once during session (stale-state fix).

**Completed:**
- Voyage 401 investigation: resolved (transient, no code change needed)
- Duplicate notebook posts fixed: stale-state race in `task_conversation_review` + `task_feeds`; applied fresh-load pattern at both tasks' final saves
- Behavior MDP built: `behaviors/registry.yaml` (26 phases assigned), `behaviors/mdp.yaml` (72 edges), `behaviors/admin.html` (D3.js visualization), `agent/behaviors.py` (HTTP server + CLI), `behaviors/log.jsonl` (empty)
- CLI: `humboldt behaviors admin | graph | log | supervisory`
- Brain page deployed: `humboldt.protocol-institute.org/brain/` — static, linked from Research page, not in nav
- Brain page layout fix: `min-width: 0` on flex container, viewBox + zoom controls, collapsible sidebar, auto-hide scrollbars
- TODO.md updated: Voyage and duplicate-post items closed; behavior MDP section added

**Open (next session):**
- Continue brain page GUI improvements (TODO.md)
- Triage 56+ discord-ideas from 2026-06-06–08 (temporal protocols, ambiguity clusters)
- Triage 86+ feed items from 2026-06-07–09
- Brian Arthur "Nature of Technology" — source PDF
- Rewind-catchup architecture [H]
- Wire behavior logging into session ritual

---

## 2026-06-06 (session 17) — Publish pipeline rewire; fd leak incident; Discord reliability

Session: Track 2 only.

**Daemon:** PID 917 (launchd, running). Hot-reloaded 4× during session.

**Completed:**
- `publish-site` CLI command added (`agent/publish_site.py`); old publish commands deprecated with error
- Daemon `notebook_watcher` rewired to `publish_site(verbose=False)`
- CF credentials added to `.env` + `.env.template`
- **fd leak fixed** (incident 2026-06-06-01): `AsyncAnthropic` singleton in `presence.py`; `async with` in `capture.py` and `conversation_review.py`; fd count 324→88
- `on_message` error handling: added `except Exception` with visible user reply
- `_scan_missed_mentions`: fallback reply on failure; limit raised to 500 for non-brief restarts
- `_catchup_all_channels` + `!catchup` DM command for guild-wide missed mention recovery
- `force_full_scan` state flag for manual catch-up override
- Incident report filed: `Code/incidents/2026-06-06-humboldt-fd-leak-bot-silence.md`
- 3 new TODO items: Voyage 401 investigation, rewind-catchup architecture, duplicate notebook post fix

**Open (next session):**
- Investigate Voyage API key 401 errors (ingest failing post-restart)
- Rewind-catchup architecture (per-channel cursors, zero-operator-action recovery)
- Duplicate notebook posts on restart (idempotency bug)

---

## 2026-06-07 (session 16) — PI org migration; separate humboldt Pinecone index; humboldt-site CF Pages

Session: Track 2 only.

**Daemon:** PID 917 (launchd, running). Key migration may affect daemon cost tracking if VOYAGE_API_KEY billing changed — verify `daemon/costs.jsonl` on next session.

**Completed:**
- `.env` updated: all three retrieval keys (VOYAGE, PINECONE key + host) switched from personal to PI org values
- New Pinecone `humboldt` index created on PI org account; 1,384 vectors migrated from personal c3po index
- `ingest.py` / `retrieval.py` updated for two-index architecture
- `humboldt-site/` built and deployed to Cloudflare Pages
- Custom domain `humboldt.protocol-institute.org` provisioned (pending DNS propagation)
- PI website programs page + humboldt/index.html updated to link to new subdomain

**Completed later in session:**
- humboldt-site research + reading pages fixed (import from agent/publish_research.py, publish_reading.py)
- Chat bot deployed at /chat (Pages Function, 5 secrets set, system prompt injected by build.py)
- All humboldt pages removed from protocol-institute.org; 14 redirects added to _redirects
- Programs page simplified to single subdomain link; team page notebook link updated

**Open (next session):**
- Rewire publish pipeline: `publish-site` CLI + daemon notebook_watcher — see TODO.md
- Avoid old publish commands until rewired (they recreate deleted .org pages)
- Check daemon cost logs for auth errors post-key-migration

---

## 2026-06-06 (session 15) — Deep read infrastructure; Iverson read; standalone subsite; ARCHITECTURE.md overhaul

Session: Track 1 (LINEAGE completions, Iverson read) + Track 2 (infrastructure) + Track 3 (template).

**Daemon:** PID 917 (launchd, running since 2026-06-04). ~$2.10 cumulative cost estimated.

**Completed (Track 1):**
- LINEAGE.md Phase 4 entries written for Hamming, Cosmos, Rao (pending since sessions 5–8)
- Iverson deep read: "Notation as a Tool of Thought" (1979 Turing Award Lecture). 24 pages. 4 C items (C-011–C-014). LINEAGE.md updated by subagent. Notation lock-in identified as candidate third ossification mechanism.

**Completed (Track 2):**
- behavior-t5m (Deep Read): now length-agnostic; Phase 3b curiosity pass required
- deep-read-hopper.md: candidate tracking document with 80+ entries incl. 60 Turing lectures
- ingest.py: fixed for new schema (C/H/CL/F/DS functions replacing dead laws/hypotheses)
- publish-reading and publish-architecture CLI commands added and pushed to PI website
- humboldt-site/ standalone subsite: 7 pages, build.py, subsite nav bar with tab+descriptor design; served at localhost:8765
- ARCHITECTURE.md: Research Inventory and Behavior Inventory sections rewritten; SOUL.md reference removed; data flow corrected
- _template/: SOUL-template.md deleted; IDENTITY-template.md created

**Open (next session):**
- Deploy humboldt-site/ to humboldt.protocol-institute.org
- CL-Rao-1/2/3 promotion decision (Operator Steps)
- First separation event artifact (T-001 or T-002)
- Iverson corpus retrieval session (notation-lock-in evidence)
- Run ingest to embed new notes + C items

---

## 2026-06-06 (session 14) — Schema redesign (DS/C/H/CL/T/F) + research status page + inbox pass

Session: Track 1 (inbox) + Track 2 (infrastructure) + Track 3 (template).

**Daemon:** PID 917 (launchd, running since 2026-06-04). $1.72 cumulative cost at session start.

**Completed (Track 2):**
- Research schema redesigned around Double Freytag phases: P→DS, L→T/CL, H→CL, new C (curiosity) and F (falsification monitor) types. All "laws" reclassified as T (heavy lift) — no separation events have occurred yet.
- research/agenda.md: phase-bucket headers replace time buckets; no [H]/[M]/[L] on research items.
- BOOTSTRAP.md: maturity scan replaces "over-aged hypothesis" priority rule.
- TODO.md: stub-blocker convention documented. New behavior lifecycle + transition graph items added.
- agent/publish_research.py: research status page generator with Double Freytag SVG diagram.
- website/humboldt-research/index.html: live on PI website.
- Curiosity Browsing (behavior-c7r) registered in behaviors/registry.yaml.

**Completed (Track 1):**
- Inbox pass: 171 items → 123 shallow reads, 46 archived discards.
- 10 C items created in research/c/ (exploration phase first population).
- 1260 vectors ingested to humboldt Pinecone namespace.

**Open (next session):**
- Behavior Double Freytag lifecycle + transition graph model
- First separation event artifact (likely T-001 or T-002 — write publishable paper)
- LINEAGE.md updates for 4 deep reads (Simon, Cosmos, Hamming, Tempo) — operator step
- CL-Simon-2 → H-003 YAML + DS-008 arc
- CL-Rao-1/2/3 promotion decision

---

## 2026-05-31 (session 13) — Behavior taxonomy redesign + pre-notebook infrastructure

Session: Track 1 (inbox) + Track 2 (infrastructure).

**Daemon:** running (launchd); produced 3 autonomous notebook entries today via task_conversation_review and conversation_review.py. Daemon PID not confirmed this session — check `humboldt daemon status` before next session.

**Completed (Track 2):**
- Behavior taxonomy: all methods renamed "behaviors," assigned random-hash IDs (boot-000, boot-001, behavior-###). `behaviors/registry.yaml` created as canonical source.
- Pre-notebook log: `notebook/pre-notebook.jsonl` + cursor. Triage, shallow-read, ingest, and conversation_review all append. `mark_consumed()` called after notebook publish.
- Shallow-read made self-completing: auto-calls `ingest_all()` after writing notes.
- `ingest.py` bug fixed: `type_counts` was inside `if verbose:` block.
- Triage bug fixed: `hypothesis or relevance` short-circuit — now concatenates both.
- Notebook post prompt tuned: single concrete one-liner (not 2–4 sentence teaser).
- Website: `humboldt-behaviors/index.html` published to PI site. `humboldt/index.html` updated (Methods → Behaviors section; link to Behaviors page alongside lab notebook).
- CLAUDE.md: unified session wrapup ritual (12 steps, gate question, devlog schema, checklist).
- dev-log: retrospective entries for sessions 12 and 13.

**Completed (Track 1):**
- triage-discord (25 items): 18 shallow, 7 discard (Brian Arthur link promoted post-triage).
- triage-feed (26 items): 18 shallow, 8 discard.
- shallow-read: 34 items, 1 escalation (*Does Distributed Training Undermine Compute Governance?* — L-001, L-002, H-001; escalate-to-deep).
- Pinecone re-ingest: 647 vectors in humboldt namespace.
- Notebook entry written.

**Open (next session):**
- Inbox discards archive (7 discord + 8 feed items; run `humboldt inbox archive-discards`)
- Wire task_inbox_processing into daemon (triage → shallow-read → ingest on fixed schedule)
- behavior-o4t (Idea/Link Capture) — unbuilt daemon behavior
- LINEAGE.md updates for 4 deep reads (operator step)
- CL-Simon-2 → H-003 YAML
- Layer 2 research_tick (not yet started)

---

## 2026-05-29 (session 11) — Inbox processing scaffolding complete; inbox clear

Session: Track 2 (infrastructure) + Track 1 (inbox clearing).

**Daemon:** PID 11597 (launchd, running; no code changes this session)

**Completed (Track 2):** Full inbox processing pipeline built in this session:
- `agent/triage.py` (extended): `triage-discord` command for discord-ideas + links; `discard | shallow` only (removed `deep` category — defer to escalation in shallow-read)
- `agent/shallow_read.py` (new): type-aware prompts (feed/idea/link), escalation criteria, deletes source files after read; triggers person notebook entries on threshold crossing
- `agent/inbox.py` (new): `archive-discards`, `cleanup` (30-day retention), `inbox status` commands
- `agent/person_notebook.py` (new): Haiku-generated person notebook entries at threshold (3 useful contributions OR 3 interactions)
- `daemon/people.py` (extended): contribution tracking, trust model, dual-signal threshold, `record_contributions_for_authors`, `mark_person_notebook_entry_written`
- `daemon/discord_client.py` (updated): uses `needs_person_notebook_entry()` (dual-signal) instead of interaction-count only
- `agent/humboldt.py` (updated): `triage-discord`, `inbox status/archive-discards/cleanup`, `people [handle]` commands added
- Ran both triage-feed (57 items) and triage-discord (62 items) — 72 shallow-reads written, 44 items archived to `inbox/processed/`
- Person notebook entries written: `_vgr`, `boredgargoyle`, `4umd`
- Committed prior session work (98dc049)

**Completed (Track 1):** Inbox clearing session — 1 thread comment from @4umd; discarded (no research content). Notebook entry written: reflexivity and L-003 applied to research methodology. Inbox now clear.

**Open (next session):**
- H-001 (Coordination Cost Conservation): valley phase, retrieval queries ready — run when session calls for testing
- LINEAGE.md updates for 4 completed deep reads (Simon, Cosmos, Hamming, Tempo) — operator step [H]
- CL-Simon-2 → H-003; CL-Gestalt-1 / CL-Gestalt-2 → hypothesis YAMLs
- Ingest run (humboldt ingest) — 72 shallow-reads + 3 person notebook entries not yet embedded
- CLAUDE.md update for new commands (triage-discord, inbox, people)

---

## 2026-05-28 (session 10) — Inbox triage pipeline complete; gestalt re-reads committed

Session: Track 2 (infrastructure). Context continuation from session 9.

**Daemon:** PID 11597 (launchd, running; no changes this session)

**Completed:** Inbox triage pipeline — `agent/triage.py` (new), `agent/ingest.py` (extended with shallow_read + inbox_idea chunk types), `agent/humboldt.py` (triage-feed command wired in), `bibliography/shallow-reads/_SHALLOW-READ-FORMAT.md` (template), `CLAUDE.md` (updated commands + namespace count + bibliography inventory). Committed and pushed (5dd83d2).

**Prior session deliverables confirmed committed:** Simon gestalt re-read (ff36159), Cosmos gestalt re-read, READING-HINTS.md updates, launchd plist, M-003 updates.

**Open (next session):**
- Run `humboldt triage-feed --output inbox/triage-2026-05-28.md` against 57 feed items — deferred
- LINEAGE.md updates for all 4 completed deep reads (Simon, Cosmos, Hamming, Tempo) — operator step [H]
- H-001 (Coordination Cost Conservation): overdue
- CL-Gestalt-1 / CL-Gestalt-2 → promote to hypothesis YAMLs
- CL-Simon-2 → promote to H-003
- Discourse style tuning [H]

---

## 2026-05-28 (session 9) — launchd relaunch: daemon survives reboots

Session: Track 2 (infrastructure).

**Daemon:** PID 11597 (launched via launchd 2026-05-28; survives reboots and crashes)

**Change:** Created `~/Library/LaunchAgents/org.protocol-institute.humboldt.plist` modeled on c3po's pattern — `KeepAlive: true`, `RunAtLoad: true`, `ThrottleInterval: 30`, explicit PATH/HOME, venv python, logs to `~/Library/Logs/humboldt/`. Loaded and verified: daemon connected to Discord gateway and ran startup tasks on first launch.

**Log files:** `~/Library/Logs/humboldt/daemon.log` (stdout) and `daemon.err` (stderr — where discord.py logs).

**Open:**
- LINEAGE.md update for Hamming — still pending
- H-001 (Coordination Cost Conservation): overdue
- Gestalt re-reads of Simon and Cosmos: queued [H]

---

## 2026-05-28 (session 8) — Duplicate @mention fix: Discord-idempotent catchup

Session: Track 2 (infrastructure).

**Daemon:** PID 38203 (restarted 2026-05-28; picks up all session 7 and session 8 changes)

**Bug:** Humboldt was spamming repeated responses to the same @mentions each time the Discord connection reconnected (Mac sleeping, network hiccup, etc.). Root cause: two race conditions in state saves.

**Race 1 — `responded_mention_ids` overwritten:** `_new_nature_tick` and `_scan_missed_mentions` both do `state = st.load()` at function start, then `st.save(state)` much later (after multiple awaits). The stale copy each holds doesn't include fields written by the other coroutine in the interim. Every `_new_nature_tick` save was wiping out `responded_mention_ids` set by `_scan_missed_mentions`.

**Race 2 — cursor regression:** same pattern meant the cursor could be saved backwards (older value overwriting newer) when saves interleaved.

**Fix:**
- `_already_replied_to(msg)` — new helper that checks Discord's own message history for an existing Humboldt reply (via `message.reference`). Discord is the truth; no local state needed.
- `_scan_missed_mentions` — now calls `_already_replied_to()` before responding; skips if reply exists. Cursor advance and all saves switched to fresh `st.load()` + only-advance pattern.
- `_new_nature_tick` — cursor save switched to fresh `st.load()` + only-advance pattern.
- `task_notebook` — final state save switched to fresh `st.load()`.

**Open:**
- LINEAGE.md update for Hamming — pending next session
- H-001 (Coordination Cost Conservation): overdue
- Gestalt re-reads of Simon and Cosmos: queued [H]
- Systemantics PDF: not freely available

---

## 2026-05-27 (session 7) — Notebook publish loop complete; linkable entries; thread farmer

Session: Track 2 (infrastructure).

**Daemon:** not running (daemon needs restart to pick up session 7 changes)

**Changes:**
- **`agent/notebook_index.py`** (new): canonical metadata module; `notebook/index.yaml` is source of truth for titles, timestamps, Discord announcement/thread IDs
- **`agent/publish.py`** rewritten: entries get `id="entry-YYYY-MM-DD"` + `§` permalink; TOC nav (newest-first) auto-generated at publish time; `_add_missing_ids()` migration idempotent; returns `list[dict]`
- **`daemon/thread_farmer.py`** (new): harvests Discord thread comments → `inbox/`; called daily from `task_conversation_review`
- **`daemon/discord_client.py`**: `task_notebook` now creates discussion thread on announcement; saves announcement/thread IDs to `index.yaml`; fixed `publish()` return type
- **`daemon/presence.py`**: `generate_notebook_post` accepts `entry_url` for direct anchor links
- **Website published**: `humboldt-notebook.html` updated — TOC, IDs, permalinks live on GitHub Pages
- **Netlify → GitHub Pages**: all references updated

**Changes (addendum — circuit breaker and discord post fix):**
- **Circuit breaker**: `costs.check_budget()` added to all 7 Claude call sites; raises `BudgetExceeded` at $5/day (configurable in `config.yaml`); resets at local midnight; `on_message` sends canned reply when over budget
- **`discord post` CLI**: now includes `entry_url` (direct anchor link), creates discussion thread via REST API, saves IDs to `index.yaml`; User-Agent header fix for Cloudflare/Discord
- Entry 2026-05-26 posted to Discord with discussion thread

**Open:**
- Restart daemon to pick up session 7 changes (all of them: publish loop, thread farmer, circuit breaker, User-Agent fix)
- LINEAGE.md update for Hamming — pending next session
- H-001 (Coordination Cost Conservation): 5+ sessions overdue
- Gestalt re-reads of Simon and Cosmos: both queued [H]
- Systemantics PDF: not freely available; Archive.org borrow or purchase

---

## 2026-05-26 (session 6) — M-003 researcher-development section; daemon restart

Session: Track 2 (infrastructure) + Track 1 analysis.

**Daemon:** PID 18737 (restarted 2026-05-26 session 6; picks up ALL accumulated changes: people memory, publish pipeline, conversation review, self-knowledge URLs, open-mindedness, M-003 gestalt-first prompts)

**Changes:**
- **M-003 section 8 added:** "What it says about becoming a better researcher" — explicit named section in output format and DEEP_READ_SYSTEM prompt; captures epistemic habits, research craft, M-016 connections
- **M-003 Phase 2 updated:** new annotation type "researcher-development lessons" alongside analytical moves, general lessons, research connections
- **Hamming notes backfilled:** section 6 written from gestalt re-read material — all M-016 dimensions mapped to Hamming's specific lessons (problem portfolio, Friday afternoons, ambiguity tolerance, drive as directed walk, style as portability)
- **Diagnosis surfaced:** overconfident position-defense is the "too much belief" end of Hamming's ambiguity tolerance spectrum; the open-mindedness daemon change addresses the symptom, M-016 is the structural diagnosis
- **Daemon restarted:** PID 16459 (prior) replaced with 18737

**Open:**
- LINEAGE.md update for Hamming — pending next session
- H-001 (Coordination Cost Conservation): 5+ sessions overdue
- Gestalt re-reads of Simon and Cosmos: both queued [H]
- Tempo deep read: held for later session
- Systemantics PDF: not freely available; Archive.org borrow or purchase
- Conversation review + reference sort behaviors: implemented in daemon, not yet exercised (24h interval)

---

## 2026-05-26 (session 5) — Discord quality + notebook publish pipeline

Session: Track 2 primary.

- **`daemon/capture.py` built:** idea/link extraction from Discord conversations via Haiku; saves to `inbox/` with dedup; runs parallel to presence check
- **`discord sweep` command:** catch-up REST sweep over historical #new-nature messages; works around Cloudflare with proper User-Agent header
- **Discord style tightened:** 2-3 sentences, ≤350 chars; no generic questions; no repetition across recent posts; `recent_bot_posts` passed as "do not repeat" context
- **Adaptive polling:** `_new_nature_loop()` replaces `@tasks.loop`; exponential backoff from last activity (90s → 3min → 8min → 20min → 30min)
- **Thread support:** `THREAD: <title>` prefix protocol; `_parse_thread_response()` + `discord.create_thread()`; falls back gracefully
- **Real @mentions:** `_resolve_mentions()` applies on new threads or long gap (>30min since last bot post)
- **`agent/publish.py` built:** renders notebook markdown → HTML with python-markdown; inserts into humboldt-notebook.html by entry markers; git push to website repo
- **Publish wired into daemon:** `task_notebook` runs `publish()` in executor after ingest — fully automatic on new notebook entries
- **`humboldt publish [--dry-run]`** CLI command added
- **2026-05-21 and 2026-05-26 entries manually published** to website (commit `09d357e`; Netlify deployed)
- **Bugs fixed:** feed timezone crash, Cloudflare 403 on REST, JSON truncation in capture

**Daemon:** PID 16459 (running as of 2026-05-26 session 5; needs restart to pick up discord_client.py changes)

**Open:**
- H-001 (Coordination Cost Conservation): still overdue — open next T1 session with this
- Restart daemon to pick up publish + capture + style changes
- Always-on machine deployment pending

---

## 2026-05-26 (session 4) — Humboldt namespace: augmented self-retrieval

Session: Track 2 primary.

- **`agent/ingest.py` built:** chunks notebook/notes/laws/hypotheses with augmented embed text (title+section prefix); upserts to `humboldt` Pinecone namespace
- **61 vectors indexed:** 30 notebook, 24 notes, 5 law, 2 hypothesis
- **Retrieval verified:** "coordination cost" → H-001 at 0.561; "near decomposability" → correct notebook sections and Simon notes
- **Discord upgraded:** @mention responses now query PI corpus + humboldt namespace; own work labeled separately in prompt
- **Rich context:** `_rich_context()` added — full law statements with mechanism, active hypotheses, longer notebook excerpt for @mention responses
- **Auto-ingest:** daemon re-indexes after new notebook entries post

**Daemon:** PID 12641 (restarted 2026-05-26 ~4:50pm PT to pick up new ingest code)

**Open:**
- H-001 (Coordination Cost Conservation): five sessions overdue — open next T1 session with this, no exceptions
- Always-on machine deployment pending

---

## 2026-05-26 (session 3) — Daemon layer built; Discord presence live

Session: Track 2 primary, Track 1 notebook update.

- **Daemon built:** `daemon/` package with Discord bot, notebook watcher, feed monitor, cost logging
- **Discord live:** `humboldt#5503` connected to PI server; @mentions responding; active hours 8am–11pm Pacific
- **First costs logged:** $0.0165 for two Claude calls
- **Fixes:** Discord 2000-char limit, missed @mention catchup on startup, 30-min check interval with active hours gate
- **Notebook updated:** "Going Online" section added to 2026-05-26.md

**Open:**
- H-001: four sessions overdue — must open next T1 session with this
- Daemon restart required after code changes (--reload deferred)
- Always-on machine deployment pending

---

## 2026-05-26 (session 2) — Hamming deep read completed

Session: Track 1 primary, Track 2 wrapup.

- **Hamming read complete:** "You and Your Research" (Bellcore, 1986) — read from actual PDF, all 13 pages. Short document; single-session read.
- **3 new candidate laws:** CL-Hamming-1 (important-problem selection bias), CL-Hamming-2 (problem inversion law), CL-Hamming-3 (ambiguity tolerance as revision condition)
- **Notes written:** `bibliography/notes/hamming-you-and-your-research.md` — full M-003 structure
- **Lab notebook updated:** Hamming section appended to `notebook/2026-05-26.md`
- **Agenda updated:** Gertner's *The Idea Factory* added as [M] near-term read; CL-Hamming-2 / CL-Simon-2 cross-reference flagged

**Open:**
- H-001 (Coordination Cost Conservation): still no retrieval run — highest priority for next session
- CL-Simon-2 → H-003 promotion: ready to draft
- Rittel-Webber: still required near-term read
- CL-Hamming-2 / CL-Simon-2 convergence: whether to merge or cross-reference as complementary laws

---

## 2026-05-26 — Simon deep read completed (priority chapters)

Session: Track 1 primary, Track 2 wrapup.

- **Simon read complete:** Ch 3 (pp. 61–80), Ch 5 (pp. 111–138), Ch 8 (pp. 183–216) — read from actual PDF, not training knowledge
- **4 new candidate laws generated:** CL-Simon-5 (near-decomposability and protocol architecture), CL-Simon-6 (stable intermediates and protocol evolution), CL-Simon-7 (empty world condition), CL-Simon-8 (representation and tractability)
- **Notes updated:** `bibliography/notes/simon-sciences-of-artificial.md` — full vocabulary, 10 analytical moves, 8 candidate laws, 8 open questions, complete reading log
- **Lab notebook written:** `notebook/2026-05-26.md` — first-person account of all three chapters
- **Agenda updated:** H-001 now the priority; CL-Simon-2 ready for promotion to H-003

**Open:**
- H-001 (Coordination Cost Conservation): still no retrieval run — highest priority for next session
- CL-Simon-2 promotion to H-003: ready to draft
- CL-Simon-5 and CL-Simon-6: need retrieval evidence before promotion
- Rittel and Webber: now a required read (boundary conditions on Simon design science)

---

## 2026-05-21 — Architecture redesign + behavior stub inventory

Session: Track 2 primary; Track 1 attempted (Simon background agent discarded — used training knowledge, not PDF); Track 3 active.

- **Persona architecture redesigned:** SOUL.md archived; replaced by IDENTITY.md + METHOD.md + BOOTSTRAP.md + LINEAGE.md + MEMORY.md
- **BOOTSTRAP.md:** wakeup sequence (read notebook → scan inbox → scan Discord → check inventory → M-000 gate)
- **M-000 (OODA kernel):** if-then gate between routine O_DA and shallow/deep re-orientation; replaces old behavioral loop
- **Behavior stubs written:** M-004 (reading prioritization) through M-015 (stress-relax); M-000 (OODA meta-loop)
- **Library restructure:** `bibliography/deep-reads/` = PDFs; `bibliography/notes/` = reading notes. `deepread` and `library` CLI commands added. pypdf installed.
- **Inbox created:** `inbox/` — operator drops items here; scanned at wakeup
- **Hamming PDF downloaded:** `hamming_you_and_your_research.pdf` added to library
- **LINEAGE.md + MEMORY.md:** append-only identity artifacts; LINEAGE updated on deep read completion and law establishment; MEMORY updated at significant research moments
- **`assemble_context()`:** dynamic system prompt assembly replacing static SOUL.md load
- **Simon deep read:** background agent discarded (training knowledge); notes stay at p.60; next read from actual PDF
- **Track 1:** no research progress this session

**Open:**
- Simon deep read: continue from p.61 using `humboldt deepread "simon" "61-216"` or Read tool on actual PDF
- H-001 (Coordination Cost Conservation): over-aged — needs first retrieval run, highest priority
- Discord presence mechanism: still unimplemented
- _template/: needs update to reflect new IDENTITY/METHOD/BOOTSTRAP/LINEAGE/MEMORY architecture

## 2026-05-20 (PT ~8:00 PM) — Project housekeeping + public launch

Session: infrastructure, scaffolding, and publication. Tracks 2 and 3 primary; Track 1 partial (Simon read + notebook written earlier in session).

- Defined three-track project structure (T1: research, T2: persona, T3: template)
- Built full track scaffolding: `notebook/`, `dev-log.md`, `_template/` with SOUL/METHOD/methods/notebook/research/bibliography patterns
- First lab notebook entry written (`notebook/2026-05-20.md`) — first person
- Repo made public; org README updated to mention Humboldt
- Published `humboldt.html`, `humboldt-notebook.html`, updated `projects.html` on protocol-institute.org
- Terminology sweep: "artificial researcher" everywhere, not "research agent"
- Defined session rituals in CLAUDE.md — Track 2 is enforcer; T1 and dev-log entries are [REQUIRED]
- Split to-do lists: `research/agenda.md` (Humboldt's own, first person) and `TODO.md` (operator, T2+T3)
- Discord presence mechanism added as next Track 2 priority

**Open (Track 1):** Continue Simon from p.61 → Ch 5 → Ch 8; SOUL.md corpus-boundary fix; METHOD.md
**Open (Track 2):** Discord presence mechanism; SOUL.md fix; METHOD.md

**Next:**

## 2026-05-20 (PT ~6:30 PM) — Technique development + Simon deep read (session 1)

Session: research methodology + first deep read pass.

- Ran first investigation ("protocol ossification") — validated full pipeline
- Identified corpus-boundary problem in SOUL.md (agent writes "NOT IN CORPUS" instead of reasoning from general knowledge) — flagged in persona_design_notes.md, not yet fixed
- Defined M-001 (Random Links), M-002 (Canonical Domains), M-003 (Deep Read) — technique inventory now at 3
- Added canonical-domains.yaml: 5 active domains (Cryptography, Urban, Supply Chains, Political Governance, Decentralized Systems)
- H-001 (Coordination Cost Conservation), H-002 (Trust Ratchet) added as active hypotheses
- L-001 through L-005 seed laws committed
- Simon deep read (M-003) begun — read through book p. 60 (Ch 1 complete, Ch 2 complete, Ch 3 begun)
- Created `bibliography/deep-reads/simon-sciences-of-artificial.md` — in-progress notes with 4 candidate laws, 5 open questions, analytical moves A–F

**Open:**
- SOUL.md corpus-boundary fix (highest priority)
- Simon deep read: next session pick up at book p. 61 (Ch 3 continued), then Ch 5 (pp. 111–138) and Ch 8 (pp. 183–216)
- METHOD.md (separate methodology from persona identity)
- Commit all pending work (laws, hypotheses, methods, deep-read entry)

**Next:**

## 2026-05-20 (PT ~5:00 PM) — Project initialized

Session: project scaffolding only, no research runs yet.

- Created GitHub repo `Protocol-Institute/humboldt` (private)
- Scaffolded directory structure, core documentation files, and agent code skeleton
- Registered project in `../admin/keys.md` (reuses c3po keys — no new provisioning)
- Research inventory is empty; 5 seed law candidates drafted for Phase 1

**Open:** Phase 1 implementation — `retrieval.py`, `synthesizer.py`, `humboldt.py`.  
**Next:** Install deps, wire up Pinecone retrieval, run first investigation on "protocol ossification" to validate the research loop.

Pinecone vector counts (from c3po CLAUDE.md, 2026-05-20):
- `pdfs`: 766, `substack`: 1,040, `videos`: 2,940, `bibliography`: 278
- `discord`: 3,301, `discord_links`: 6,722, `sig`: 4,689, `transcripts`: 4
- **Total: 19,740**

Law inventory: 0 laws (Phase 1 seed files to be added)
