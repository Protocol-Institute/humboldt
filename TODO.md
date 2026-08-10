# Developer TODO — Tracks 2 and 3

Infrastructure, persona, and template work. This is the *operator* layer — managing Humboldt as a project. Humboldt's own research agenda is in `research/agenda.md`.

Priority: **[H]** urgent, **[M]** soon, **[L]** when convenient.

---

## 🎯 ON DECK — Redesign Phase 2 wrap-up (next session)

> Spec: `plans/redesign-2026-08.md`. Session 29 (2026-08-10) closed the `triage.py`/
> `reads.py` rework — the last big Phase 2 item. **Pause expires 2026-08-15** — extend
> when the daemon is next touched if Phase 5 (server cutover = "off-laptop") will slip
> past it.

~~**`triage.py` / `reads.py` rework [OPUS].**~~ **DONE (session 29, 2026-08-10).**
`agent/funnel_context.py` (new) replaces the stale `research/laws/`/`research/hypotheses/`
readers; triage tags `content`/`meta` and creates `bib-NNNN` entries; shallow-read upgrades
`read_depth`, links laws, emits seeds. Live-tested end-to-end. Reference backfill also ran
for real (11 evidence sources across 7 laws → `bib-NNNN`). Both session-28 defects
(empty triggers, transient parse error) fixed in the same pass. See `dev-log.md` 2026-08-10.

**Next — [SONNET] session:** publish hook + law-event Discord plumbing (§9 quiet mode) —
wire law create/promote/challenge → `publish-site` + one Discord law-event post.

**Also found this session, not yet fixed:** `agent/references.py` still reads the dead
`research/hypotheses/`/`research/laws/` path — same bug class as the triage/shallow-read
and daemon-presence fixes, but the module is still live (`conversation_review
.promote_inbox_links`, and `bibliography.py` itself imports it). Not urgent while the
daemon's paused; fold into the next daemon-adjacent session.

**After Phase 2:** Phase 3 (graph + console) → Phase 4 (analytics) → **Phase 5 (server
cutover + quiet-mode Discord = off-laptop)**.

**Deferred (blocked by pause until 08-15):** `humboldt ingest` of new laws/seeds/bib
(also `ingest.py` chunk types don't yet cover laws/seeds/bibliography).

**Operational:** `daemon restart` hasn't happened since this session's changes (Phase 2
funnel rework + the daemon feed-DM/law-context fixes below) — do it before or at the
08-15 unpause so the live daemon actually runs the fixed code.

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
bug in `daemon/capture.py`. None of this is live until `daemon restart`.

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

- **[M]** Update `_template/` to reflect current architecture (IDENTITY/LINEAGE/MEMORY/METHOD/BOOTSTRAP) — `SOUL-template.md` is superseded.
- **[M]** Add ingest pattern to template — augmented chunk text (title+section prefix) is the generalizable design decision; capture in `_template/`.
- **[L]** Copy M-001 through M-003 to `_template/methods/` in generic form — strip PI specifics.
- **[L]** Write `_template/CLAUDE-template.md` — generic Claude Code setup for AR projects.
- **[L]** Extract as separate repo when stable — threshold: 5+ sessions, pattern tested, reviewed.
