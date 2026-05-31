# Developer TODO — Tracks 2 and 3

Infrastructure, persona, and template work. This is the *operator* layer — managing Humboldt as a project. Humboldt's own research agenda is in `research/agenda.md`.

Priority: **[H]** urgent, **[M]** soon, **[L]** when convenient.

---

## Track 2 — Persona and Infrastructure

### Autonomous research daemon — Layer 1 RUNNING; Layer 2 next [H]

Full plan at `plans/autonomous-research-daemon.md`.

**Layer 1 (COMPLETE — running since session 9):** `task_conversation_review` — daily Discord synthesis into notebook + reference promotion to `bibliography/references.yaml`. Has produced autonomous notebook entries on 2026-05-30 and 2026-05-31.

**Layer 2 — research_tick (NOT YET BUILT):** Build in this order:

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

### Discord presence quality (next cluster)

- **[H]** **Conversation style tuning** — review actual #new-nature transcripts and identify what's off. Current symptoms: likely too formal / too long / too eager. Tune `_slim_context()` and `_rich_context()` prompts based on observed output. May require a dedicated prompt-tuning session with real examples.

- ~~**[H]** **Graceful shutdown + restart**~~ — **COMPLETE 2026-05-27.** `responded_mention_ids` prevents duplicate @mention responses across restarts; `last_clean_shutdown` / `last_startup` markers enable brief-restart detection; `close()` override saves clean-shutdown marker; `daemon restart` CLI sends SIGUSR1 for hot-reload; DM `!reload` from operator triggers same; feed DMs suppressed on restarts < 5 min offline; `daemon.pid` file tracks live PID.

- **[H]** **Idea and reference capture from Discord** — when Humboldt participates in a conversation, it should notice and save: (1) ideas or arguments that bear on its research hypotheses, (2) external papers/articles/links that participants cite. Save to `inbox/` as structured items. This is the "input → inventory" flow that was deferred at Discord launch. Design: detect in `on_message` and `task_new_nature` response path; use a lightweight extraction call (Haiku) to decide if anything is worth saving before responding.

- **[H]** **Discord user models + person notebook entries** — track recurring interlocutors persistently. Store interaction history in `daemon/people.json` (gitignored). When someone crosses a threshold (3+ interactions), write a notebook entry treating them as a research conversation: what they keep bringing up, how their thinking connects to active research. Use in `generate_mention_response` to personalize and acknowledge history.

- **[M]** **Richer self-context in Discord responses** — current `_rich_context()` includes laws and hypotheses but not the research agenda, LINEAGE.md in full, or recent open questions. Humboldt should be able to situate a conversation within its actual current thinking, not just inventory. Add agenda summary and current open questions to rich context.

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

---

## Track 3 — Artificial Researcher Template

- **[M]** Update `_template/` to reflect current architecture (IDENTITY/LINEAGE/MEMORY/METHOD/BOOTSTRAP) — `SOUL-template.md` is superseded.
- **[M]** Add ingest pattern to template — augmented chunk text (title+section prefix) is the generalizable design decision; capture in `_template/`.
- **[L]** Copy M-001 through M-003 to `_template/methods/` in generic form — strip PI specifics.
- **[L]** Write `_template/CLAUDE-template.md` — generic Claude Code setup for AR projects.
- **[L]** Extract as separate repo when stable — threshold: 5+ sessions, pattern tested, reviewed.
