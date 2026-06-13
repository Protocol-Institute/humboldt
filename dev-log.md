# Humboldt Dev Log — Track 2

Development log for Humboldt's persona, methodology, and infrastructure. Covers Track 2 (persona evolution) and Track 3 (artificial researcher template) work. Research activity is tracked separately in `notebook/`.

Most recent entry first.

---

## 2026-06-13 (session 19) — Inbox clearing; PDF library build; deep reads launched

**Tracks active:** T1, T2
**Daemon PID:** 917 (running)

Three work streams: inbox clearing (T1), PDF library expansion (T2), and deep reads initiated (T1).

**Inbox clearing.** 316 unprocessed items (216 feed from 2026-06-08–12, 100 Discord ideas/links accumulated since session 18). Triage-feed: 156 shallow, 60 discard. Triage-discord: 64 shallow, 36 discard. All 220 shallow reads run via `shallow-read --from-triage`; 96 discards archived; humboldt namespace re-ingested to 2460 vectors. 29 feed escalations + 2 Discord escalations = 31 new deep-read candidates, all added to the hopper. Protocolized Substack added to daemon feed roster (`https://protocolizedmagazine.substack.com/feed`) — direct ingestion of PI's own magazine, previously only available indirectly via c3po corpus.

**PDF library expansion.** All 36 newly escalated arXiv papers downloaded (plus 9 previously queued = 36 total new downloads). Rittel & Webber downloaded from open-access mirror (11pp). Kuhn downloaded in 50th anniversary edition (237pp). Library: 43 PDFs (was 7 at session start). Hopper updated: all downloaded papers marked `in-library`. Remaining needs-hunting: Ostrom, Kauffman, Nelson & Winter, von Humboldt *On Language*, Gertner. Turing lectures remain Cloudflare-blocked.

**Deep reads (three parallel subagents).** Rittel & Webber: complete. 8 C items (C-015–C-022), reading notes at `bibliography/notes/rittel-webber-dilemmas-general-theory-planning.md`. Key result: wicked-problem framing reframes CL-001 — the ratchet exists because re-opening a protocol means re-entering the wicked territory the protocol was designed to escape, and that re-entry was already costly enough to settle once. Kuhn: in-flight at session close (C-025–044 reserved). Papers queue: in-flight at session close, C-045–049 written (entropy principle ×2, computable-rules boundary-search amplification, capability-cooperation inversion, consensus-reasoning decoupling). Both agents will run to completion autonomously; output lands on disk, review and commit deferred to next session. READING-HINTS.md updated with reading hints for Rittel & Webber and Kuhn.

**Open (next session):**
- Review and commit output from Kuhn agent + papers agent (C-025+ and C-050+)
- Run `humboldt ingest` after reviewing new C items
- CL-001 transition trigger assessment — Rittel & Webber result may be enough to close the valley
- CL-003 needs targeted investigation (still stagnant)
- Brain page GUI improvements still open ([H])
- Rewind-catchup architecture still open ([H])

## 2026-06-09 (session 18) — Behavior MDP graph; daemon stale-state fix; brain page

**Tracks active:** T2
**Daemon PID:** 917 (running)

Three distinct work streams this session.

**Daemon reliability fixes.** Resolved two open bugs from session 17. The Voyage 401 investigation came back clean — key is valid, ingest runs fine (1,427 vectors), the 401s were transient during the key migration window. Closed without code changes. The duplicate notebook post bug had a real root cause: `task_conversation_review` and `task_feeds` were loading state at task start, running async LLM calls (yield points), then saving the stale snapshot — clobbering `last_notebook_commit` and `notebook_entries_posted` set by concurrent `task_notebook` runs. Fixed by applying the existing fresh-load pattern to both tasks' final saves. Confirmed in the production daemon.err log: the pattern was three "Posting notebook entry 2026-06-06" events on 2026-06-06, each triggered by a different commit being visible after the cursor was rolled back by the stale save.

**Behavior MDP system.** Built the full behavior graph architecture: all 26 behaviors assigned to Double Freytag phases in `behaviors/registry.yaml`; `behaviors/mdp.yaml` defines the MDP (28 nodes including 2 virtual HL/RE placeholders, 72 edges — 34 within-phase bidirectional, 35 cross-phase, 2 cycle-back); `agent/behaviors.py` provides an HTTP admin server and CLI (graph, admin, log, supervisory); `behaviors/admin.html` is a D3.js visualization with vertical phase flow, hover tooltips, and in-graph weight editing; `behaviors/log.jsonl` is the behavior visit log. The supervisory CLI reads consecutive transitions from the log and flags divergences from MDP weights. The full MDP is connected via the retrospective → liminal cycle-back edge.

**Brain page.** Deployed the behavior graph as a static read-only page at `humboldt.protocol-institute.org/brain/` — no nav link, linked from the Research page opening blurb. `_build_brain()` in `humboldt-site/build.py` bakes registry + MDP data as inline JSON (`window.HUMBOLDT_STATIC_DATA`), injects the site nav, and writes to `dist/brain/`. Fixed a flexbox layout bug (`min-width: 0` on the graph container) that was causing the SVG to expand the flex child and suppress scrollbars. Added zoom via `viewBox` + dynamic SVG sizing (slider, +/−, keyboard shortcuts), auto-hiding scrollbars, and a collapsible right sidebar.

**Open (next session):**
- Continue brain page GUI improvements (to-do item logged in TODO.md)
- Triage 56 untriaged discord-ideas from 2026-06-06–08 (temporal protocols cluster, ossification independence, ambiguity)
- Triage 86+ untriaged feed items from 2026-06-07–09
- Brian Arthur "Nature of Technology" — two independent triage recommendations; source PDF when ready
- Rewind-catchup architecture still open ([H])
- Wire behavior logging into session wrapup ritual

## 2026-06-06 (session 17) — Publish pipeline rewire; fd leak fix; Discord reliability hardening

**Tracks active:** T2
**Daemon PID:** 917 (launchd, running)

Three independent bodies of work this session.

**Publish pipeline rewire:** The old `publish`, `publish-research`, `publish-reading`, `publish-architecture` CLI commands targeted the now-deleted `../website/` repo. Created `agent/publish_site.py` which runs `humboldt-site/build.py` then `wrangler pages deploy dist`. Old commands now exit with a deprecation error. Daemon `notebook_watcher` path updated to call `publish_site(verbose=False)`. CF credentials added to `.env` and `.env.template`. Tested live — deploy to `humboldt.protocol-institute.org` confirmed.

**File descriptor leak (incident 2026-06-06-01):** Discord bot had been silently unresponsive for ~2.5 days (Jun 4 03:19 UTC through this session). Root cause: `presence.py`'s `_client()` factory created a new `AsyncAnthropic` instance per call, each holding an httpx connection pool open indefinitely. Same pattern in `capture.py` and `conversation_review.py`. Fixed: `presence.py` converted to module-level singleton; `capture.py` and `conversation_review.py` use `async with` context manager. fd count dropped from 324 (234 leaked IPv6 sockets) to ~88 after hot-reload. No API cost overages — the leak had suppressed all costs to near zero by preventing new connections. Incident report filed at `Code/incidents/2026-06-06-humboldt-fd-leak-bot-silence.md`.

**Discord reliability hardening:** Added `except Exception` catch to `on_message` mention handler (was silently dropping all non-budget errors; users saw no reply). Added fallback reply to `_scan_missed_mentions`. Implemented `_catchup_all_channels(since_date)` for guild-wide @mention recovery covering all text channels and active threads. Added `!catchup [YYYY-MM-DD]` operator DM command. Added `force_full_scan` state flag. Raised `_scan_missed_mentions` limit to 500 for non-brief restarts. Attempted catch-up for missed mentions during blackout: Jun 4 `_vgr` mention recovered; Jun 5 `plague_year` and Jun 6 `ncc1031` (in threads/other channels) triggered via `!catchup` DM. Voyage API 401 errors appeared post-restart (ingest path only); separate investigation item.

**Open (next session):**
- Investigate Voyage API 401 (PI org key may have billing/expiry issue)
- Proper rewind-catchup architecture (per-channel cursors, no manual state edits)
- Duplicate notebook posts on restart (idempotency bug in `task_notebook`)

## 2026-06-07 (session 16, continued) — humboldt-site pages fixed; .org cleanup

**Tracks active:** T2
**Daemon PID:** 917 (running, launchd)

### humboldt-site: research and reading pages fixed

Both pages had stripped-down implementations that didn't match the PI website versions.
Fixed by importing directly from `agent/publish_research.py` and `agent/publish_reading.py`:

- `research/index.html`: now uses `_build_svg`, `_phase_rows`, `_phase_header`, `_CSS`, `_JS`
  from publish_research.py — Double Freytag arc with hover-tooltip dots + phase-grouped table
- `reading/index.html`: now uses `_render_note`, `_render_card`, `_CSS` from publish_reading.py
  — TOC, gestalt blocks, "What it opens," badges, collapsible full notes

`_page()` template gained `extra_js` parameter for per-page script injection.

### Chat bot deployed (/chat)

`humboldt-site/functions/chat.js` — CF Pages Function at POST /chat:
- Two-index Pinecone retrieval (c3po corpus + humboldt research artifacts)
- System prompt injected by `build.py` from IDENTITY.md, LINEAGE.md, CL/T/F inventory,
  recent notebook — idempotent regex replacement, refreshes on every build
- Voice: `_rich_context()` from presence.py with Discord constraints removed
- 5 secrets set on CF Pages project

### .org website cleanup

Deleted 7 humboldt pages from protocol-institute.org (3,521 lines removed).
Added 14 301 redirects in `_redirects` → `humboldt.protocol-institute.org/*`.
Programs page simplified to single subdomain link. Team page notebook link updated.

**Open (next session):**
- Rewire publish pipeline: `publish-site` CLI command replaces old per-page publishes;
  daemon notebook_watcher updated to call it. See TODO.md for full spec.
- Avoid running old publish commands until rewired (they recreate deleted .org pages).

## 2026-06-07 (session 16) — PI org migration; humboldt Pinecone index; humboldt-site subsite

**Tracks active:** T2
**Daemon PID:** 917 (running, launchd)

### Key migration — personal → PI org accounts

All three retrieval keys in humboldt `.env` were still pointing at personal accounts as of session start:
- `VOYAGE_API_KEY`: was personal (`pa-s9GiLbr…`), now PI org (`pa-Bdk7…`)
- `PINECONE_API_KEY`: was personal (`pcsk_5HhrjD…`), now PI org (`pcsk_5HqmhB…`)
- `PINECONE_C3PO_HOST`: was old personal host (`c3po-bwo39z7`), now PI org (`c3po-1os2tli`)

Keys were already present in `../.env.keys`; this was purely an `.env` update + documentation pass. `admin/keys.md` updated to reflect `VOYAGE_HUMBOLDT_API_KEY` is not needed (shared PI alias suffices). `PINECONE_C3PO_HOST` added to `.env.template`.

### Humboldt Pinecone index — separated from c3po

Problem: humboldt's research artifacts were stored in a `humboldt` namespace in the c3po Pinecone index. This created migration coupling (just seen: the PI org c3po index had no `humboldt` namespace because it was never re-ingested after c3po migrated in May). Also means humboldt's write access = write access to all c3po corpus namespaces.

Fix: created a standalone `humboldt` index (1024d, cosine, aws us-east-1) in the PI org Pinecone account. Migrated 1,384 vectors via direct fetch+upsert from the personal account's `c3po/humboldt` namespace (batch size 50; no re-ingestion, preserves all vectors including ones whose source content may no longer exist).

Code changes:
- `agent/ingest.py`: now writes to `PINECONE_HUMBOLDT_HOST` (default namespace)
- `agent/retrieval.py`: routes `humboldt` sentinel to humboldt index; all corpus namespaces still query c3po index; results merged
- `PINECONE_HUMBOLDT_HOST` added to `.env`, `.env.template`, `.env.keys`, `admin/keys.md`, `CLAUDE.md`

### humboldt-site/ — Cloudflare Pages subsite

Built `humboldt-site/` — a self-contained static site generator:
- `build.py`: generates 5 pages (About, Notebook, Research, Reading, Architecture) from source data in the repo
- `assets/style.css`: standalone CSS using PI design language (Cormorant Garamond + DM Sans, #2A6B6B teal) — no PI website dependencies
- `wrangler.toml`: CF Pages config (project: humboldt, output: dist/)
- `dist/` gitignored (generated artifact)

Deployed to PI CF account as `humboldt` Pages project. Custom domain `humboldt.protocol-institute.org` provisioned (pending DNS propagation, typically a few minutes).

Updated PI website:
- `programs/index.html`: AI Infrastructure track now links to `humboldt.protocol-institute.org`
- `humboldt/index.html`: internal links (/humboldt-notebook etc.) updated to point to new subdomain

**Open (next session):**
- Verify `humboldt.protocol-institute.org` resolves correctly after DNS propagation
- Wire `humboldt publish` / daemon auto-publish to rebuild and redeploy humboldt-site after new notebook entries
- humboldt-site/ deploy workflow: either git-connected auto-deploy or CLI command added to publish pipeline
- Verify daemon still works correctly after key migration (check `daemon/costs.jsonl` for any auth errors)

## 2026-06-06 (session 15) — Deep read infrastructure; standalone subsite; ARCHITECTURE.md overhaul; Iverson read

**Tracks active:** T1 / T2 / T3
**Daemon PID:** 917 (running, launchd)

### behavior-t5m (Deep Read) — now length-agnostic + curiosity pass required

The deep read behavior was implicitly calibrated for books. Two changes:

1. **Length-agnostic:** behavior-t5m now applies to any text length — books, papers, essays, aphorisms, koans. For shorter texts, depth comes from connections to existing inventory rather than extended structural mapping. The Phase 1 structural mapping step is now split: long texts use the table-of-contents pass; short texts form a one-sentence pre-reading hypothesis instead.

2. **Phase 3b (Curiosity Pass) added as a required phase:** After synthesis, every deep read must produce 2–5 C-NNN YAMLs capturing things the text opened that don't rise to candidate law level. `source: reading`, `source_ref` points to the notes file. These feed directly into the exploration inventory via ingest.

The Iverson read was the first test of both changes. It ran as a background subagent: 24 pages read, full 12-section notes written, 4 C items created (C-011 through C-014), LINEAGE.md updated with Iverson entry + new "Computational Epistemology / Formal Methods" tradition. Completed in ~4 minutes.

### deep-read-hopper.md — candidate tracking document

`bibliography/deep-read-hopper.md` created as the canonical queue for deep-read candidates at any stage of PDF availability. Fields: title/author, type, source of recommendation (source codes: `deep-read:X`, `shallow-read`, `discord:@handle`, `operator`, `web`), PDF status, research connections, date added.

Populated on creation with: 7 books surfaced from reading notes (Rittel-Webber, Nelson-Winter, Ostrom, Kauffman, Gertner, Kuhn, Wilhelm von Humboldt); 2 Ribbonfarm essay series; 9 arXiv escalations from shallow reads; 2 needs-operator-guidance items (Lamport, IEEE UnifiedBus); 1 web-only article. Also added the complete ACM Turing Award lecture collection (60 entries, 1966–2025), sourced from the Wikipedia laureate list after amturing.acm.org returned Cloudflare 403s. Iverson (1979) already moved from `needs-hunting` to `in-library`.

READING-HINTS.md and the M-003 source file now both reference the hopper. Download script at `bibliography/deep-reads/download-turing-lectures.sh` (requires browser cookie injection to bypass Cloudflare).

### ingest.py — new schema functions

The `_law_chunks()` and `_hypothesis_chunks()` functions pointed at `research/laws/` and `research/hypotheses/` — both directories were deleted in the session 14 schema redesign. They were silently returning empty lists and none of the new artifacts were being ingested. Fixed:

- `_law_chunks()` → removed (directory gone)
- `_hypothesis_chunks()` → removed (directory gone)  
- Added: `_curiosity_chunks()` (C items), `_cl_chunks()` (CL items), `_h_chunks()` (H items), `_f_chunks()` (F items), `_ds_chunks()` (DS arc markdown)

Confirmed counts on fix: 10 C, 3 CL, 0 H, 0 F, 52 DS chunks. Ingest pipeline now covers 9 source types.

### New publish commands

- `humboldt publish-reading` — renders `bibliography/notes/*.md` → `humboldt-reading/index.html` on PI website. Each source gets a card: gestalt paragraph highlighted, analytical moves and candidate law counts badged, full notes in a `<details>` collapsible. Pushed live this session.
- `humboldt publish-architecture` — renders `ARCHITECTURE.md` → `humboldt-architecture/index.html` on PI website. Pushed live this session.

### humboldt-site/ — standalone subsite

`protocol-institute/humboldt-site/` created as the foundation for `humboldt.protocol-institute.org`. Standalone static site: own CSS, own nav, no dependency on the PI website CSS or JS.

7 pages built from live data via `build.py`:
- **/** — research mission from IDENTITY.md, live CL inventory, latest notebook entry teaser
- **/notebook/** — all notebook entries, newest-first, TOC with permalinks
- **/reading/** — all deep-read notes with gestalt blocks and collapsible full notes
- **/research/** — research status page (adapted from PI website generated version)
- **/methods/** — all 26 behaviors from registry.yaml, grouped by classification
- **/devlog/** — all 17 dev-log sessions, TOC with permalinks
- **/architecture/** — full ARCHITECTURE.md rendered as prose

Nav redesign this session: main header is logo-only; all page navigation moves to a dedicated **subsite nav bar** — a horizontal strip below the header with tab labels and one-line descriptors (e.g., "Research / Active arcs", "Methods / Behaviors"). Active tab has teal underline. Horizontally scrollable on narrow viewports. Served at localhost:8765.

Deployment to the subdomain is deferred — standalone site confirmed working locally first.

### ARCHITECTURE.md — three sections rewritten

SOUL.md was still mentioned as "archived"; that line is gone. Three sections required complete rewrites:

- **ingest.py description** — now lists all 9 current source types
- **Research Inventory** — fully replaced with DS/C/H/CL/T/F schema, phase-to-artifact table, transition trigger explanation, explicit note that F is correctly empty
- **Methods Inventory → Behavior Inventory** — renamed, split into boot/supervised/live/daemon tables with behavior-### IDs and legacy M-0xx cross-references; `behaviors/registry.yaml` named as the canonical source

Also updated: Deep-Read Library section now includes Iverson and references `deep-read-hopper.md`; data flow diagram corrected to new artifact paths.

### _template/ — SOUL-template.md replaced

`_template/SOUL-template.md` deleted (monolithic persona model, superseded 2026-05-21).
`_template/IDENTITY-template.md` created — the new AR template lead document following the modular architecture: IDENTITY / LINEAGE / MEMORY / METHOD / BOOTSTRAP / behaviors/registry.yaml / research schema / bibliography.

### LINEAGE.md completions (T1 operator step, session 15)

Phase 4 entries written for Hamming, Cosmos, and Rao — all three had been pending since their respective reads in sessions 5–8. Combined with the Iverson entry (written by subagent), LINEAGE.md now has entries for all 5 completed reads. The "LINEAGE.md updates for 4 completed deep reads" item is removed from the Operator Steps queue.

**Open (next session):**
- CL-Rao-1/2/3 promotion decision (still in Operator Steps)
- First separation event artifact (T-001 or T-002 — write and publish)
- Deploy humboldt-site/ to humboldt.protocol-institute.org + update main PI site
- Iverson curiosities: one corpus retrieval session to check notation-lock-in evidence
- Behavior Double Freytag lifecycle model (T2 [H] item, still deferred)
- Run ingest after this session (new notes + C items need embedding)

---

## 2026-06-06 (session 14) — Schema redesign (DS/C/H/CL/T/F); research status page; inbox pass; separation event clarification

**Tracks active:** T1 / T2 / T3
**Daemon PID:** 917 (running since 2026-06-04, launchd)

### Why the schema changed

The session started with a visualization question that exposed a deeper naming problem: the research content ladder had no coherent terminology, and the existing "P/L/H/CL" naming had accumulated ad-hoc meanings across sessions. The Double Freytag phase model was already the conceptual foundation of the research process; the schema redesign simply made the naming match the model.

The five non-null phases now each have a typed artifact:
- **C** (Curiosity) — exploration. A provocation. Explicitly prohibited from being a proto-law.
- **H** (Hypothesis) — sensemaking. Post-cheap-trick working claim.
- **CL** (Candidate Law) — valley. Evidence accumulating under the organizing insight.
- **T** (Theory) — heavy lift. Synthesis committed; writing the publishable artifact.
- **F** (Falsification Monitor) — retrospective. *Only created after a separation event.*

**DS** (Deep Story) replaces P as the arc container. File renames: all `research/projects/P-NNN` → `research/ds/DS-NNN`, `research/laws/L-NNN` → `research/theories/T-NNN` or `research/cl/CL-NNN`, `research/hypotheses/H-NNN` → `research/cl/CL-NNN`. New directories: `research/c/`, `research/h/`, `research/f/`.

### The separation event correction — critical conceptual point

The most important single change: all four items previously marked as "registered laws" (L-001 Ossification, L-002 Hardness Asymmetry, L-004 Goodhart, L-005 Gall) were reclassified from F (Falsification Monitor, retrospective) to T (Theory, heavy lift). The reason: an F item only exists after a **separation event** — a published artifact available for independent review, critique, and falsification attempts. A YAML file in a GitHub repo, however detailed, is not a separation event. A notebook entry is not a separation event. None of the four laws have been published for external scrutiny.

This correction locks in a direction: the next research milestone is writing and publishing the artifact, not accumulating more private evidence. The F directory is now empty — correctly. This should be revisited after the first artifact is published.

The confidence field ("candidate" / "established") is also abolished. There are no "established" laws — only laws that have not yet been falsified or superseded. The F schema uses `status: active | superseded | refuted` instead.

### Governance scaffolding redesign

**`research/agenda.md`:** Replaced time-bucket headers (Next session / Near-term / When opportunity arises) with phase-bucket headers (Heavy Lift Ready / Valley stagnant or behavior-blocked / Valley productive / Sensemaking Needed / Cheap Trick Pending / Behavior Blockers / Operator Steps / Exploration). No `[H]/[M]/[L]` labels on research items — phase position is the temporal status. Each valley/CL item now carries a `transition_trigger` field: one specific named condition that would constitute phase-readiness, not a vague "when I know more."

**`BOOTSTRAP.md`:** Step 4 ("Any hypothesis over-aged?") replaced with a phase-position maturity scan. The Decide phase priority order rewritten: "Over-aged hypothesis" (calendar-driven) gone, replaced by "Heavy lift ready" and "Stagnant valley — diagnose." The `[H]/[M]/[L]` urgency labels remain only in TODO.md for Track 2 infrastructure work, which actually is schedule-driven.

**`TODO.md`:** Stub-blocker convention documented: when a Track 2 behavior is under-defined and blocking a Track 1 arc phase move, the flag lives in Track 2 (the behavior item gets `[BLOCKING: DS-xxx]`) and is mirrored as `blocking_behavior:` in the arc's project file. Track 1 diagnoses the block; Track 2 resolves it.

**Arc Diagnosis section** added to each active DS/CL file: `current_phase` (enum), `phase_tempo` (phenomenological description), `transition_trigger` (named condition), `blocking_behavior` (stub name or "none").

### Research status page

New `agent/publish_research.py` generates `website/humboldt-research/index.html`:
- SVG Double Freytag diagram with all research items plotted at phase position × entropy level. First peak (Cheap Trick) deliberately smaller and narrower than the second (Separation Event) — reflects entropy dynamics. Colored dots (green/yellow/red) for status. Hover tooltips.
- Phase-grouped table below the diagram.
- Published to PI website alongside lab notebook and behavior inventory.

CLI: `python3 -m agent.humboldt publish-research [--dry-run]`. Run after any session that changes the research inventory.

Schema additions: `phase_pct` field on CL and T YAMLs (fraction complete within current phase, used to position the dot on the curve); `research_status: active | stagnant | blocked` on CL YAMLs.

### Inbox pass and curiosity collection (Track 1)

171 items processed: 123 shallow reads (27 discord, 96 feed), 46 archived discards. 30 escalations flagged for potential deep reading (Arthur, Lamport, Szabo, and a range of multi-agent mechanism-design papers).

10 **C items** created in `research/c/` — first population of the exploration phase. Most structurally significant: C-001/C-002 (ossification and formalization may be independent variables; ossification as requisite-variety failure) challenge the implicit coupling assumed in CL-001 and T-001. C-006 (regulatory delay as bifurcation parameter) is the most surprising — no home in the current inventory.

**Curiosity Browsing** (behavior-c7r) registered in `behaviors/registry.yaml`: randomly samples `research/c/` when stuck or between arcs, looking for connections that might fire a cheap trick. Feeds into Random Links downstream.

### Open items (next session)

- Apply Double Freytag template to behaviors: lifecycle phases for each behavior, `behavior_phase` field in registry
- Behavior transition graph: directed graph model of which behaviors apply in which arc phase
- LINEAGE.md updates for 4 deep reads (Simon, Cosmos, Hamming, Tempo) — operator step, still pending
- CL-Rao-1/2/3 from Tempo notes — promotion decision
- CL-Simon-2 → H-003 YAML + DS-008 arc
- First separation event artifact: start writing one of the T items as a publishable paper

**Open (next session):**
- Behavior Double Freytag + transition graph
- First separation event artifact (likely T-001 or T-002)
- LINEAGE.md operator steps

---

## 2026-05-31 (session 13) — Triage bug fix; daemon notebook post tuning; session wrapup reconstruction

**Track 2 (infrastructure).**

*Note: sessions 12 and 13 had incomplete wrapups. This entry reconstructs session 12 and covers session 13.*

**Daemon notebook post prompt (presence.py):**
- `generate_notebook_post`: changed from "2–4 sentences, under 400 characters" to single-sentence with concrete-finding constraint. Snippet expanded from first-paragraph-only (500 chars) to full entry joined paragraphs (1200 chars). max_tokens reduced 300→100. Goal: posts should report the actual thing that happened, not a topic teaser.

**Triage bug fix (agent/triage.py):**
- `_triage_discord_batch`: `annotation = item["hypothesis"] or item["relevance"][:120]` was short-circuiting — when a capture file had a hypothesis tag (e.g. "H-001"), the relevance note was dropped entirely. Haiku saw only a bare ID with no context, defaulting to "methodological reference" heuristics. Fixed to concatenate both: `"Tagged: H-001 — [relevance text]"`. Brian Arthur's *The Nature of Technology* was the canary — it had H-001 tagged and a relevance note that never reached the model.

**Shallow reads in progress (background):** discord triage (18 items) and feed triage (18 items) both running via `shallow-read --from-triage`.

**Behavior taxonomy redesign (continued in same session):**
- All methods renamed "behaviors" — recurrent habits, not recipes.
- ID scheme: `boot-###` for bootstrap-triggered (2 behaviors); `behavior-###` with random 3-char hashes for all others (21 behaviors, including 5 new daemon stubs).
- `behaviors/registry.yaml`: canonical inventory with classification (supervised/live/daemon), state (stub/prototyping/production), source file, and brief implementation note for each behavior.
- Legacy M-00x IDs preserved as `legacy_id` field; methods/ files unchanged for now.
- Website Behaviors page: `humboldt-behaviors/index.html` on PI website, grouped by type with state and type badges. `humboldt/index.html` updated: "Methods" section renamed to "Behaviors," link to Behaviors page added alongside lab notebook link.
- 5 new daemon behavior stubs documented (behavior-e2h, behavior-a8r, behavior-o4t, behavior-g7u, behavior-v3c): feed intake, conversation synthesis, idea/link capture, notebook publish, thread farming.

**Pre-notebook infrastructure:**
- `agent/pre_notebook.py`: append-only JSONL queue at `notebook/pre-notebook.jsonl`. Cursor file at `notebook/.pre-notebook-cursor` tracks consumed entries. `append()`, `get_pending()`, `mark_consumed()`, `show_pending()` API.
- `daemon/conversation_review.py`: appends pre-notebook entry after each review run.
- `agent/triage.py`: appends pre-notebook entries after triage_discord + triage_feed.
- `agent/shallow_read.py`: appends pre-notebook entry after write; then calls `ingest_all()` automatically. Self-completing pipeline: triage → shallow-read → ingest requires no manual follow-up.
- `agent/ingest.py`: fix — `type_counts` dict moved outside `if verbose:` block (was undefined when verbose=False). Now appends pre-notebook entry after ingest.
- `daemon/discord_client.py`: `mark_consumed()` called after notebook publish so cursor advances.
- `agent/humboldt.py`: `pre-notebook` CLI command (show pending queue; `mark-consumed` subcommand).

**Shallow reads (background, ran in session):**
- 34 items shallow-read (discord + feed triage 2026-05-31). Notes in `bibliography/shallow-reads/`.
- 1 escalation: *Does Distributed Training Undermine Compute Governance?* → escalate-to-deep (L-001, L-002, H-001).
- Ingest ran automatically: 647 vectors in humboldt namespace (59 notebook, 46 notes, 530 shallow_read, 5 law, 2 hypothesis, 5 inbox_idea).

**CLAUDE.md:**
- Session wrapup restructured from 3 track-split sections → 1 unified ritual (12 numbered steps, gate question, devlog schema, step-level checklist template). This is session 13's wrapup format.

**Open:**
- LINEAGE.md updates (operator step — 4 deep reads unrecorded)
- CL-Simon-2 → H-003 YAML
- Inbox discards archive — 7 discord + 8 feed items still in inbox/
- Wire task_inbox_processing into daemon (triage → shallow-read → ingest on fixed schedule)
- behavior-o4t (Idea/Link Capture) — the remaining unbuilt daemon behavior

---

## 2026-05-29 (session 12) — Autonomous research daemon plan; two publish bug fixes

**Track 2 (infrastructure). Brief session, no formal wrapup written at the time.**

**Autonomous research daemon plan:**
- `plans/autonomous-research-daemon.md` written: full design for four-phase build. Phase 1: expenses log, escalation queue, M-018 stub, `research_tick.py` skeleton in dry-run. Phase 2: live hypothesis retrieval + notebook/git/Discord output. Phase 3: opportunistic (M-018) + sensemaking synthesis. Phase 4: deep read daemon (future).
- `TODO.md` updated with Phase 1–4 build order under "Autonomous research daemon — NEXT SESSION [H]."
- Note: `task_conversation_review` (already running since session 9 / commit c617bd9) constitutes the first layer of autonomous research. It synthesizes Discord conversations daily into notebook entries and promotes links to `bibliography/references.yaml`. It has already produced autonomous notebook entries on 2026-05-30 and 2026-05-31. The `research_tick` (hypothesis retrieval, escalation queue) is the unimplemented second layer.

**Notebook publish path fix:**
- `agent/publish.py`: output path changed from `humboldt-notebook.html` to `humboldt-notebook/index.html` to match website clean-URL migration.
- `agent/notebook_index.py`: URL base updated to `/humboldt-notebook/` so Discord announcement links resolve correctly.

**Person notebook entry broadcast fix:**
- `daemon/notebook_watcher.py`: now filters to `YYYY-MM-DD` stem format only and explicitly excludes `notebook/people/`. Person profiles (collaborator mental models) are private; they were previously being announced to #new-nature as if they were lab notebook entries.
- Three mistakenly-announced posts (for `_vgr`, `boredgargoyle`, `4umd`) deleted from Discord; their entries removed from `notebook/index.yaml`.

---

## 2026-05-29 (session 11) — Inbox processing pipeline complete; inbox clear

**Track 2 (infrastructure) + Track 1 (inbox clearing).**

**Inbox processing pipeline — full build:**

Continued from session 10 context. The pipeline now handles the full lifecycle from inbox to archive/delete:

- `agent/triage.py` (extended): Added `triage-discord` command for discord-idea and discord-link inbox items. Prompt uses a higher discard bar appropriate for pre-filtered community submissions. Triage output is now 2-category only (`discard | shallow`) — the `deep` category was removed so that depth decisions are made by Humboldt during reading, not at triage. Legacy `deep` items in old reports are bucketed into shallow.
- `agent/shallow_read.py` (new): Type-aware prompt dispatch — feed (evaluate as paper with escalation criteria), idea (always store-only; ideas escalate by becoming candidate laws), link (inference from description only, URL not fetched). Escalation criteria applied strictly. Source files deleted after shallow-read note is written. Triggers person notebook entry generation when contribution threshold crossed.
- `agent/inbox.py` (new): `archive-discards` (move DISCARD items to `inbox/processed/` with YYYY-MM-DD prefix, record discard contributions in people model), `cleanup` (delete processed items older than 30 days), `inbox status` (composition summary).
- `agent/person_notebook.py` (new): Haiku-generated person notebook entries. Loads full contribution history and law context. Writes to `notebook/people/{handle}.md`; appends with date header if file exists. Called by `shallow_read` (contribution threshold) and `discord_client` (interaction threshold).
- `daemon/people.py` (extended): `record_contribution()` returns True when useful_contributions just crossed NOTEBOOK_THRESHOLD=3. `record_contributions_for_authors()` parses comma-separated author strings. `needs_person_notebook_entry()` uses dual-signal trigger: useful_contributions >= 3 OR interaction_count >= 3. `mark_person_notebook_entry_written()`. `trust_score()`, `contribution_summary()`, `person_contribution_detail()` for inspection.
- `daemon/discord_client.py` (updated): `_record_interaction_and_check()` now uses `needs_person_notebook_entry()` (dual-signal) instead of `needs_notebook_entry()` (interaction count only).
- `agent/humboldt.py` (updated): CLI dispatch for `triage-discord`, `inbox status/archive-discards/cleanup`, `people [handle]`.

**Pipeline runs completed:**
- `triage-feed` against 57 feed items → 1 escalation (Short-Term Gain, Long-Term Fragility)
- `triage-discord` against 62 discord items → 6 escalations
- `shallow-read` against both triage reports → 72 notes written to `bibliography/shallow-reads/`
- Person notebook entries triggered and written: `_vgr`, `boredgargoyle`, `4umd`
- Trust model bootstrapped via one-time script (shallow-read ran before people model was wired in)

**Track 1 (inbox clearing):** 1 thread comment (44 words, no research content) discarded. Notebook entry written about reflexivity — the L-003 dynamic applied to research methodology. Notebook README index updated with 2026-05-28 and 2026-05-29 entries (both were missing).

**Pending infrastructure:**
- `humboldt ingest` — 72 shallow-reads + 3 person notebook entries not yet embedded to Pinecone humboldt namespace
- CLAUDE.md update for new commands (triage-discord, inbox, people)

---

## 2026-05-28 (session 9) — launchd relaunch; gestalt deep reads; inbox triage pipeline

**Track 2 (infrastructure).**

**launchd relaunch:** Created `~/Library/LaunchAgents/org.protocol-institute.humboldt.plist` mirroring c3po's pattern — `KeepAlive`, `RunAtLoad`, `ThrottleInterval 30`, explicit PATH/HOME, venv python, logs to `~/Library/Logs/humboldt/`. Daemon now survives reboots. Verified: daemon connected to Discord gateway on first load (PID 11597).

**Deep reads (background agents):** Launched parallel background agents for Simon and Cosmos gestalt re-reads. Both completed and committed:
- Simon (Sciences of the Artificial): all 8 chapters including previously skipped Ch 4, 6, 7. Master key: "borrowed complexity." 10 analytical moves. 2 new candidate laws: Attention Scarcity Ratchet (CL-Gestalt-1), Representation Commitment (CL-Gestalt-2).
- Cosmos Vol. 1: pp. 1–449 (prior pass stopped at p. 120). 8 analytical moves. Equilibrium-disturbance/discontinuous-restoration pattern → H-002. Aesthetic response as epistemically load-bearing. Book ends exactly where Humboldt-the-agent's domain begins.
- Reading hints updated in READING-HINTS.md: both now say "read as someone to emulate — lineage inheritance, not law extraction."
- M-003 current deep-read table updated; all 4 reads now show gestalt-complete status.
- LINEAGE.md updates still pending for all 4 reads (Simon, Cosmos, Hamming, Tempo) — operator step.
- Hamming PDF renamed from underscores to hyphens to match notes filename; library command now shows [notes exist] for all 4.

**Ingestion:** Re-ingested to Pinecone after each batch — 99 vectors total.

**Inbox triage pipeline (in progress, not yet complete):**
- Reviewed inbox: 43 discord-ideas, 16 discord-links, 57 feed items, 1 thread comment.
- `agent/triage.py` written: `humboldt triage-feed` command — Haiku scoring of inbox/feed-*.md against current laws/hypotheses, outputs ranked discard/shallow/deep report.
- `agent/ingest.py` extended: `_inbox_idea_chunks()` (discord-ideas → humboldt Pinecone) and `_shallow_read_chunks()` (bibliography/shallow-reads/ → humboldt Pinecone) added to `ingest_all()`.
- `bibliography/shallow-reads/` directory created.
- `_SHALLOW-READ-FORMAT.md` template: NOT YET WRITTEN (session interrupted).
- `humboldt.py` updated: `triage-feed` command wired, usage string updated.
- **Not yet done:** shallow-reads format template; CLAUDE.md update for new commands; running triage-feed against the actual inbox; commit + push of triage pipeline code.

**Open:**
- Complete inbox triage pipeline: write `_SHALLOW-READ-FORMAT.md`, update CLAUDE.md, run triage-feed, commit
- LINEAGE.md updates for all 4 completed deep reads (operator step)
- H-001 investigation (valley phase, retrieval queries ready)
- CL-Gestalt-1 and CL-Gestalt-2 promotion to hypotheses
- Promote CL-Simon-2 to H-003

---

## 2026-05-28 (session 8) — Duplicate @mention bug fixed; Discord-idempotent catchup

**Track 2 (infrastructure):**

**Bug diagnosed:** Humboldt was responding 3–5 times to the same @mention messages each time the Discord connection dropped and reconnected (Mac sleep/wake, network hiccup). All responses carried the "catching up from while I was offline" prefix, confirming the source was `_scan_missed_mentions` firing on every `on_ready` event.

**Root cause — two race conditions in `discord_client.py`:**

1. **Stale-state overwrite:** Both `_new_nature_tick` and `_scan_missed_mentions` do `state = st.load()` at function start, then `st.save(state)` many awaits later. In between, the other coroutine may have written new fields (notably `responded_mention_ids`). The stale save overwrites them with the loaded defaults (`[]`). Every `_new_nature_tick` cycle was wiping out the `responded_mention_ids` that `_scan_missed_mentions` had just saved, so on the next reconnect the IDs appeared untracked and were reprocessed.

2. **Cursor regression:** Same stale-save pattern meant the cursor (`last_new_nature_message_id`) could be written backwards — a later save could advance it to an older value if the coroutine's initial load captured a stale cursor.

**Fix — three changes to `discord_client.py`:**

- `_already_replied_to(msg)` — new helper method. Scans up to 50 messages after `msg` in the channel; returns True if any message is from Humboldt with `reference.message_id == msg.id`. Uses Discord's own history as the authoritative source of truth. Survives state resets, process crashes, and race conditions.

- `_scan_missed_mentions` refactored:
  - Before responding to a missed @mention, calls `_already_replied_to()`. If Discord shows a reply already exists, skips the mention and records it in `responded_mention_ids` (secondary cache); continues.
  - Cursor advance and all `st.save()` calls switched to fresh `st.load()` + only-advance pattern (compare new value against current before writing, never regress).

- `_new_nature_tick`: cursor save switched to fresh `st.load()` + only-advance pattern.

- `task_notebook`: final state save switched to fresh `st.load()`.

**Design note:** `responded_mention_ids` remains as a fast-path cache (avoids a Discord API call on repeated reconnects for the same message). Discord history is the primary guard. The combination is belt-and-suspenders.

**Daemon restarted:** PID 38203. Verified clean startup — no spurious catchup responses on first `on_ready`.

---

## 2026-05-27 (session 7 addendum) — Circuit breaker + discord post fixes

**Track 2 (infrastructure):**

**Circuit breaker (`daemon/costs.py` + all call sites):**
Added `today_usd()`, `BudgetExceeded` exception, `check_budget()`, and `configured_limit()` to `costs.py`. Every Claude API call site (5 in `presence.py`, 1 in `conversation_review.py`, 1 in `capture.py`) now calls `costs.check_budget()` before invoking the model. If today's local-date spend ≥ the configured limit ($5), `BudgetExceeded` is raised. The date boundary is local midnight — `datetime.now().strftime("%Y-%m-%d")` — so the reset is automatic with no explicit mechanism needed. UTC timestamps in costs.jsonl are converted to local time for the comparison.

For `@mention` responses (`on_message`), `BudgetExceeded` is caught specifically and sends a hardcoded canned reply ("I've hit my daily API budget and am offline until midnight. Back tomorrow.") — no model call needed, so the reply is free. All other task paths (feeds, new-nature ticking, conversation review, capture) silently skip via existing `try/except` blocks.

Limit configurable in `daemon/config.yaml` under `budget.daily_limit_usd`.

**`discord post` CLI (`agent/humboldt.py`):**
Updated `_discord_post_async` to: pass `entry_url` (anchor-linked URL) to `generate_notebook_post`; create a discussion thread on the announcement message via Discord REST API; save announcement/thread IDs to `notebook/index.yaml`. Fixed missing `User-Agent` header — Discord's Cloudflare layer was returning 403 without it.

---

## 2026-05-27 (session 7) — Notebook publish loop complete

**Track 2 (infrastructure):**

Completed the notebook → Discord → thread → harvest pipeline that was half-built at end of session 6. All four components now wired end-to-end.

**`notebook/index.yaml` + `agent/notebook_index.py`:**
New canonical metadata module. `index.yaml` is the single source of truth for entry titles, taglines, git-sourced timestamps, Discord announcement/thread IDs, and `thread_last_farmed` timestamps. `build_from_git()` bootstrapped the three existing entries from git history. All downstream consumers (publish, discord_client, thread_farmer) read/write through this module.

**`agent/publish.py` rewrite:**
The key design decisions: entries get `id="entry-YYYY-MM-DD"` (not slugified section text — dates are stable; section headers change); `§` permalink on the date line (muted grey, turns teal on hover) rather than a floating section nav (simpler, no JS); TOC is newest-first (reading order matches reverse-chronological discovery). The `_add_missing_ids()` migration runs idempotently on every publish, so the existing three entries picked up IDs and permalinks on first run. `publish()` returns `list[dict]` (not `int`) — richer return allows callers to drive downstream actions without re-reading state.

**`daemon/thread_farmer.py`:**
Harvests Discord thread comments → `inbox/` for reorientation context at next session start. Key design: uses Discord snowflake arithmetic to paginate from `thread_last_farmed` rather than fetching all history; filters bot messages; writes structured markdown with source metadata; updates `thread_last_farmed` even if zero messages (marks the baseline). Wired into `task_conversation_review` (daily). 

**`daemon/discord_client.py` `task_notebook`:**
Now uses `nbi.entry_url()` for direct anchor links in announcements; creates a 7-day auto-archive discussion thread on each announcement message; saves `discord_announcement_id` + `discord_thread_id` to index.yaml for the thread farmer to use later.

**Website:**
`humboldt-notebook.html` now has TOC (three entries, newest-first), entry IDs, and `§` permalinks. Pushed to GitHub Pages. Netlify references removed throughout (site migrated to GitHub Pages).

**Design decisions not taken:**
- Slugified section anchors within entries (e.g., `#entry-2026-05-20-first-investigation`): section headers change too easily; date-level linking is stable and sufficient for Discord sharing
- Floating section nav: requires JS, adds complexity; `§` permalink per entry is lighter and handles the primary use case (linking to a specific session from Discord)

**Open track 3:**
Thread farmer pattern (harvest external conversation → structured inbox → session reorientation) is a generalizable design worth adding to `_template/`. Not done this session.

---

## 2026-05-26 (session 6) — M-003 researcher-development section

**Track 2 (persona/methodology):**

Session began with user question: "Deep reads should also pick up on knowledge about going better researcher. Is there any of that in the notes?" The answer: yes, but it wasn't structured anywhere.

**Analysis of existing notes:**
- Hamming (gestalt re-read, complete): the *entire talk* is researcher-development material. Problem selection bias; drive as directed walk; 10-20 problem portfolio; Friday afternoons as Orient practice; ambiguity tolerance as the un-teachable prerequisite; problem inversion as local-optima escape; style as the portable core. All of this was in the gestalt re-read but had no named section.
- Simon (law-hunting only): researcher-development content exists structurally — satisficing as attention allocation model, bounded rationality as a description of the researcher's own situation, the ant's path as a caution against over-attributing to the researcher's mind — but was missed in the law-hunting pass. Will surface in gestalt re-read.
- Cosmos (law-hunting, partial): Humboldt's epistemological method is inherently researcher-development — graduated confidence, critique of observation without synthesis, the warning that accumulating disconnected facts without synthesis reinforces the conviction that there's no law. Also missed.

**What changed:**
- **M-003 output format:** section 8 "What it says about becoming a better researcher" added between "nature of things" and "research connections"; total sections now 12. Section 8 explicitly connects to M-016 dimensions. For texts primarily about research practice, this is now the most important section.
- **M-003 Phase 2:** "researcher-development lessons" added as an annotation category in close reading, alongside general lessons and research connections.
- **prompts.py DEEP_READ_SYSTEM:** section 6 added (same content as M-003 section 8); sections renumbered 6-9 → 7-10. The section is explicit about M-016 connection and notes that technical texts may have thin content here.
- **Hamming notes:** section 6 backfilled from existing gestalt re-read material. Covers all six M-016 maturity dimensions via Hamming's specific vocabulary. Key diagnostic: Humboldt's overconfident position-defense is the "too much belief" end of Hamming's ambiguity tolerance spectrum — not a behavioral tic but a structural failure of the middle state that productive revision requires.
- **Daemon restarted:** PID 18737. Picks up all changes from sessions 5-6: people memory, publish pipeline, conversation review, self-knowledge URLs, open-mindedness, M-003 gestalt-first prompts.

**Track 3 (template):** The addition of section 8 to M-003 is a potential template change — any future artificial researcher should have this section in their deep read format from the start. No template update yet; defer until pattern is exercised and stabilized across multiple reads.

---

## 2026-05-26 (session 5) — Discord quality + notebook publish pipeline

### Infrastructure changes

**New: `daemon/capture.py`** — Discord idea/link capture system:
- `extract_captures()` — Haiku call to extract ideas and external links from conversation messages relevant to active hypotheses/laws
- `save_capture()` — deduplicates (in-session URL set + file scan) and writes `inbox/discord-{type}-{date}-{time}-{slug}.md`
- `run_capture()` — chunks messages in groups of 15 before calling extract_captures; returns count saved
- max_tokens=1500 (raised from 800 to fix JSON truncation on large batches)

**New: `agent/publish.py`** — lab notebook → website publishing pipeline:
- `render_entry()` — converts `notebook/YYYY-MM-DD.md` to HTML using python-markdown; extracts tagline, title (first `##` heading or `<!-- title: ... -->` override); wraps in `<!-- ENTRY: date -->` markers
- `publish()` — diffs existing HTML by entry markers, inserts new entries chronologically, git add/commit/push to `../website` repo
- `_convert_body()` — demotes h2→h3, adds indentation, strips `<hr>` rules
- Used `markdown` library (version 3.10.2); add to `pip install` list

**Updated: `agent/humboldt.py`**:
- Added `cmd_publish(dry_run)` and `publish [--dry-run]` CLI command
- Added `discord sweep [--since DATE] [--limit N]` CLI command (catch-up capture sweep)
- Updated USAGE string

**Updated: `daemon/discord_client.py`**:
- `task_notebook` now runs `publish()` in executor after re-ingest — new notebook entries automatically appear on website
- `_new_nature_loop()` replaces `@tasks.loop` for adaptive interval checking (exponential backoff from last activity)
- `_next_check_interval()` — <4min→90s, <12min→3min, <30min→8min, <90min→20min, else 30min
- `_bot_post_context()` — single history scan returning (recent_bot_posts, last_post_age_seconds)
- `_parse_thread_response()` / `_resolve_mentions()` — THREAD: prefix protocol for thread creation; @username→<@user_id> on long gap or new thread
- Capture runs in parallel with presence check via `asyncio.gather()`

**Updated: `daemon/presence.py`**:
- Style tightened: 2-3 sentences, ≤350 chars; "do not end with a question unless you need the answer for research"
- `generate_new_nature_response()` — added `recent_bot_posts` ("do not repeat these"), participants list, THREAD: prefix instruction; max_tokens=150
- `generate_mention_response()` — added `@username` direct address, THREAD: prefix; max_tokens=200

**Updated: `daemon/state.py`** — added `last_new_nature_activity` field (ISO timestamp of last human message seen)

**Updated: `daemon/feed_monitor.py`** — fixed timezone bug: `datetime.fromtimestamp(mktime(...))` → `datetime.fromtimestamp(mktime(...), tz=timezone.utc)`

**Updated: `CLAUDE.md`** — added `markdown` to pip install; documented `publish` and `discord sweep` CLI commands

### Website

- 2026-05-21 and 2026-05-26 notebook entries manually published to `Protocol-Institute/website` (commit `09d357e`)
- Netlify auto-deployed; entries now live at humboldt-notebook.html
- Future entries will be published automatically by the daemon's `task_notebook`

### Errors resolved this session

- `ANTHROPIC_API_KEY` KeyError in smoke test → env not loaded; fixed with `set -a && source .env && set +a`
- JSON truncation in capture (`max_tokens=800` too small for 26 msgs) → raised to 1500, added chunk_size=15
- Cloudflare 403 on Discord REST calls → added `User-Agent: DiscordBot (...)` header
- Feed timezone crash (`naive vs aware` comparison) → added `tz=timezone.utc` in feed_monitor.py

---

## 2026-05-26 (session 4) — Humboldt namespace: augmented self-retrieval

### Infrastructure changes

**New: `agent/ingest.py`** — ingestion module for Humboldt's own documents:
- `_notebook_chunks()` — splits `notebook/*.md` by `##` headers; augments embed text with `"Lab Notebook YYYY-MM-DD — Section Title"` prefix
- `_notes_chunks()` — splits `bibliography/notes/*.md` by `##` headers; augments with book title
- `_law_chunks()` — embeds each `research/laws/*.yaml` in full (statement + mechanism + domains); no chunking, laws are small
- `_hypothesis_chunks()` — embeds each `research/hypotheses/*.yaml` in full (question + motivation)
- `ingest_all()` — batches and upserts to `humboldt` Pinecone namespace; deterministic IDs so re-runs update in place
- 61 vectors indexed on first run: 30 notebook, 24 notes, 5 law, 2 hypothesis

**Updated: `agent/retrieval.py`** — added `NS_HUMBOLDT = ["humboldt"]` and `NS_BROAD_PLUS` (PI corpus + humboldt namespace)

**Updated: `agent/humboldt.py`** — added `cmd_ingest()` and `ingest` CLI command

**Updated: `daemon/discord_client.py`**:
- `on_message` and `_scan_missed_mentions` now use `NS_BROAD_PLUS` — @mention responses draw from both PI corpus and Humboldt's own notebook/notes/laws
- `task_notebook` calls `ingest_all()` in executor after posting new entries, keeping namespace current

**Updated: `daemon/presence.py`**:
- `_rich_context()` — new full-depth context for @mention responses: IDENTITY + LINEAGE (truncated) + full law statements with mechanism + active hypothesis questions + longer notebook excerpt
- `_slim_context()` — unchanged, still used for notebook posts and new_nature triage
- `generate_mention_response()` now uses `_rich_context()` and separates retrieved chunks into "from own work" vs "from PI corpus" in the prompt, with `max_tokens` raised to 500

### Retrieval quality check

Test queries confirm correct retrieval:
- "coordination cost conservation" → H-001 hypothesis at 0.561, L-001 at 0.434, relevant notebook sections
- "near decomposability Simon stable intermediates" → notebook "What Ch 8 Revealed" at 0.409, Simon notes at 0.404

### Track 3: generalization candidate

The ingest pattern (augmented chunk text with document title + section prefix) is the key design decision that makes retrieval results self-identifying in Claude prompts. This is worth capturing in `_template/` as the recommended approach for any AR project that ingests its own work. Not updating the template this session — one more session to see if the retrieval quality justifies the pattern.

### Open issues updated

| Priority | Issue |
|----------|-------|
| High | H-001 (Coordination Cost Conservation): now four sessions overdue — must open next T1 session with this |
| Medium | Daemon needs manual restart after code changes |
| Low | `_template/` update: ingest pattern worth capturing |
| Low | Always-on machine deployment |

---

## 2026-05-26 (session 3) — Daemon layer built and deployed

### Infrastructure changes

**New: `daemon/` package** — full async daemon layer:
- `discord_client.py` — `HumboldtBot(discord.Client)` with three `ext.tasks` loops: notebook watcher (30 min), #new-nature presence check (30 min, active hours gated), feed monitor (12h)
- `presence.py` — Claude-powered content generation with slim context; `AsyncAnthropic`; `_discord_safe()` truncation at 1900 chars
- `notebook_watcher.py` — `git log` based detection of new notebook entries since last-seen commit
- `feed_monitor.py` — `feedparser` RSS polling + `inbox/` saving
- `state.py` — persistent `state.json` (gitignored, machine-local)
- `costs.py` — per-call cost logging to `costs.jsonl`; `totals()` by operation
- `config.yaml` — intervals, active hours, feed sources (operator-editable)

**CLI additions:** `daemon run`, `daemon status` (shows state + cost totals), `discord post [--draft]`

**Fixes during session:**
- Discord 2000-char limit: `_discord_safe()` + reduced `max_tokens` + explicit prompt instructions
- Cost logging: every Claude call logs to `costs.jsonl`; `daemon status` shows cumulative spend
- Missed @mention catchup: `_scan_missed_mentions()` runs on `on_ready`, responds to any @mentions in #new-nature since last check
- Active hours gate: `_within_active_hours()` checks Pacific time before each new-nature check; configurable in `config.yaml`
- #new-nature history limit: 25 → 100 messages

**Dependencies added:** `discord.py>=2.3`, `feedparser`

**Gitignored:** `daemon/state.json`, `daemon/costs.jsonl`, `daemon/daemon.log`

### Deployment

Bot running live on PI Discord as `humboldt#5503`. First @mention responses verified working. Daemon started with `nohup`, detached from terminal, PID tracked. Bot token and channel/guild IDs registered in `../.env.keys` and `../admin/keys.md`.

### First session costs

Two Claude calls at session start: $0.0086 (new-nature check) + $0.0079 (mention response) = $0.0165 total.

### Track 3: no template changes

The daemon pattern is PI-specific (Discord server, Pinecone index, active hours in Pacific). The general pattern of a daemon layer for an artificial researcher is worth capturing in `_template/` eventually, but too early — needs more sessions to know what generalizes.

### Open issues updated

| Priority | Issue |
|----------|-------|
| High | H-001 (Coordination Cost Conservation): four sessions overdue |
| Medium | Daemon needs manual restart after code changes — `--reload` dev mode deferred |
| Medium | Thread support: `task_new_nature` doesn't scan threads; @mention required |
| Low | Always-on machine deployment: systemd unit file, `git pull` on schedule |

---

## 2026-05-26 (session 2) — Hamming deep read completed

### Infrastructure: no changes

No persona, CLI, or infrastructure changes. Track 2 activity is this entry and the commit.

### What this session produced

Hamming's "You and Your Research" read from actual PDF (13 pages, single session). Notes at `bibliography/notes/hamming-you-and-your-research.md`. Three candidate laws generated (CL-Hamming-1 through CL-Hamming-3). Lab notebook appended.

The Hamming read introduced a distinction the Simon read didn't make explicit: there are two kinds of deep-read sources — framework sources (Simon: analytical tools for understanding what protocols are) and craft sources (Hamming: empirical wisdom about how to do research). M-004 (reading prioritization) should weight these differently. Framework sources contribute to the theory; craft sources contribute to the methodology. Both matter, but for different reasons.

CL-Hamming-2 (problem inversion) and CL-Simon-2 (local-maximum trap) are converging on the same phenomenon at different levels. This will need to be resolved before either is promoted to a hypothesis — either they merge into a single hypothesis with two contributing laws, or they remain complementary laws with explicit cross-references.

### Track 3: one generalization candidate

The framework/craft distinction in reading sources is a generalizable pattern. `_template/` should flag this in its M-004 analog: deep reads serve two functions (analytical framework acquisition, research methodology acquisition), and prioritization should consider both. Not updating the template this session — this is worth sitting with for another session before formalizing it.

---

## 2026-05-26 — Simon deep read completed; notes architecture validated

### Infrastructure: no changes

No persona, CLI, or infrastructure changes this session. The only Track 2 activity is this entry and the commit.

### What this session validated

The deep-read note-taking architecture (introduced 2026-05-20) worked as designed. The file at `bibliography/notes/simon-sciences-of-artificial.md` accumulated cleanly across multiple sessions: vocabulary, analytical moves, protocol-theoretic moments, candidate laws, and open questions are all maintained in a single structured document. The note file is now 400+ lines and covers all priority chapters. This is the intended outcome.

The M-003 deep-read rule — **always read from the actual PDF, never from training memory** — was successfully enforced. The 2026-05-21 session discarded a training-knowledge read; today's session produced the real one. The rule has now been tested under real conditions and confirmed necessary. Background agents are particularly dangerous for well-known texts: they produce plausible-sounding synthesis from training memory without any visible indication that the PDF was not read.

### Open design question: LINEAGE.md update criteria

The Simon read is complete. LINEAGE.md should be updated to acknowledge Simon as an earned lineage entry — not just a reference, but a genuinely influential source that has shaped Humboldt's analytical vocabulary. The criteria from LINEAGE.md: a deep-read source qualifies for LINEAGE entry when (a) it has been fully read, (b) its framework has been internalized and applied (analytical moves A–J, candidate laws), and (c) it has changed how Humboldt sees the research domain.

Simon qualifies on all three. I will update LINEAGE.md in this session.

### Track 3: no template updates

Nothing from this session generalizes to `_template/` in a way not already captured. The deep-read workflow is already in the template. No Track 3 changes needed.

---

## 2026-05-21 — Architecture redesign: from RAG persona to researcher OS

### The core problem resolved

The inherited SOUL.md architecture was built for c3po — a corpus assistant whose identity is defined by the corpus it inhabits and reports from. Humboldt is fundamentally different: defined by interests and skills, not by what it knows; self-directed rather than query-driven; building its own original research inventory rather than synthesizing the corpus for users. The SOUL.md pattern could not accommodate a behavioral loop where Humboldt reviews its own state and decides what to do next.

The fix required a full architecture replacement, not a patch.

### New persona architecture

**Retired:** `SOUL.md` (archived, preserved for reference)

**Replaced by:**

| Document | Purpose |
|----------|---------|
| `IDENTITY.md` | Short stable kernel: lineage telos, mission, intellectual temperament, voice |
| `LINEAGE.md` | Append-only earned lineage: grows from deep reads and established laws only |
| `MEMORY.md` | Narrative memory: how Humboldt tells itself the story of its development |
| `METHOD.md` | Epistemic standards: provenance marking, confidence levels, falsification |
| `BOOTSTRAP.md` | Wakeup sequence and Decide-phase configuration |
| `methods/M-000-ooda.md` | The OS kernel: OODA decision gate |

The key architectural insight: LINEAGE.md and MEMORY.md start nearly empty and grow slowly through research activity. Declared identity is replaced by earned identity. LINEAGE gets one entry per completed deep read and one per law promoted to `established`. MEMORY gets an entry when something significantly shifts. Both are permanent and append-only.

### Dynamic context assembly

`agent/prompts.py` now assembles the system prompt from multiple sources rather than loading a single static SOUL.md. The assembled context includes: IDENTITY + LINEAGE + MEMORY + METHOD + BOOTSTRAP + research state (loaded from research/ at runtime) + methods index (one line per M-NNN) + inbox contents + recent notebook thread. `load_soul()` is a backward-compatible wrapper around `assemble_context()`.

### Behavior stub inventory

Twelve new method stubs written (M-000 through M-015, excluding gaps):

- **M-000** — OODA meta-loop (the kernel)
- **M-004** — Reading prioritization
- **M-005** — Explore-exploit
- **M-006** — Research conversations
- **M-007** — Field trip
- **M-008** — Bullshit detector
- **M-009** — Visual thinking
- **M-010** — Fermi estimation
- **M-011** — Dyson design
- **M-012** — Thought experiments
- **M-013** — Design fictions
- **M-014** — Cross-training
- **M-015** — Stress-relax

The stubs range from immediately usable (M-010 Fermi, M-012 Thought Experiments) to requiring significant adaptation for a digital researcher (M-015 Stress-Relax, M-014 Cross-Training). The OODA stub reflects the operator's specific understanding: Orient is expensive and should only be triggered when the environment has genuinely shifted; routine sessions run as O_DA.

### Library restructure and deep-read wiring

`bibliography/` restructured:
- `bibliography/deep-reads/` — PDF source documents only
- `bibliography/notes/` — reading notes (was `bibliography/deep-reads/*.md`)

`simon_sciences.pdf` moved to `bibliography/deep-reads/simon-sciences-of-artificial.pdf`.
`simon-sciences-of-artificial.md` moved to `bibliography/notes/`.

New CLI commands: `humboldt library` (list documents) and `humboldt deepread "<name>" ["<pages>"]` (read actual PDF via pypdf, write notes to bibliography/notes/).

Critical rule enforced in M-003 and CLAUDE.md: deep reads must always use the actual PDF. Never from training knowledge. A background agent was dispatched to continue the Simon read this session and produced plausible-sounding output from training memory — it was discarded. The rule now has a concrete failure case to point to.

### Inbox

`inbox/` created. The operator drops files here; Humboldt reads them as part of the BOOTSTRAP wakeup sequence. Text and markdown files are inlined into the assembled context; PDFs and large files are listed with a pointer. `inbox/processed/` is where Humboldt moves items after acting on them.

Telegram bot integration (pointing to the existing vgr-library-code infrastructure) is the planned next step for async inbox delivery.

### Hamming PDF acquired

`hamming_you_and_your_research.pdf` downloaded to library. Reading prioritization (M-004) should evaluate it against active hypotheses before Humboldt decides when to engage it. Short document — likely a shallow-mode read alongside a primary investigation session.

### Track 3: template status

The new architecture (IDENTITY/METHOD/BOOTSTRAP/LINEAGE/MEMORY) is itself the core generalization that `_template/` should capture. The existing `SOUL-template.md` and `METHOD-template.md` are now outdated. Updating `_template/` to reflect the new architecture is the next Track 3 priority.

### Open issues

| Priority | Issue |
|----------|-------|
| High | Simon deep read: continue from p.61 using actual PDF |
| High | H-001 (Coordination Cost Conservation): over-aged, needs first retrieval run |
| High | `_template/` update: SOUL-template.md superseded; new architecture templates needed |
| Medium | Discord presence mechanism: still undesigned at implementation level |
| Medium | Telegram inbox integration: wire vgr-library-code bot to write to `inbox/` |

---

## 2026-05-20 (session 2) — Public launch + ritual definition

**Session goals:** complete project housekeeping; publish the project; define operational structure.

### Publication
- Repo made public (`Protocol-Institute/humboldt`)
- Org README (`.github/profile/README.md`) updated — Humboldt listed with description and notebook link
- PI website: `humboldt.html` (project page), `humboldt-notebook.html` (lab notebook, first entry), `projects.html` (Initiatives listing entry with both links)
- Terminology sweep across all files: "artificial researcher" replaces "research agent" / "autonomous agent" everywhere. Key distinction: Humboldt is driven by its own research interests, not by user requests.

### Three-track structure
- Track 1 (Humboldt's research), Track 2 (operator/persona), Track 3 (template) formally defined
- `notebook/` created with first entry (2026-05-20.md) — first person, Track 1 wrapup artifact
- `dev-log.md` created (this file) — Track 2 wrapup artifact
- `_template/` created — Track 3 primary artifact, v0.1

### Session rituals
- Full ritual spec written into CLAUDE.md — startup and wrapup for all three tracks
- Track 2 is enforcer: must produce wrapup checklist report before session closes
- `[REQUIRED]` designation for non-skippable items: lab notebook entry (T1) and dev-log entry (T2)

### To-do structure
- `research/agenda.md` — Humboldt's own queue, first person, lives in `research/` as a research artifact, updated at T1 wrapup [REQUIRED]
- `TODO.md` — operator queue, T2 and T3 only; Humboldt's layer cleanly separated

### Open issues updated
- Discord presence mechanism elevated to highest T2 priority
- SOUL.md corpus-boundary fix and METHOD.md creation remain high priority

---

## Open Issues (Track 2)

| Priority | Issue | Notes |
|----------|-------|-------|
| High | Discord presence mechanism for #new-nature channel | Auth, participation policy, input→inventory flow — see TODO.md |
| High | Fix SOUL.md corpus-boundary problem | Humboldt must reason from general knowledge freely; "NOT IN CORPUS" is never a research result |
| High | Create METHOD.md | SOUL = who; METHOD = how; methods/ = specific procedures |
| Medium | Update SOUL.md "Current Research State" section | Keep live at session start/end |
| Low | Periodic literature survey mechanism | Scheduled investigative move from current inventory state |

## Open Issues (Track 3)

| Priority | Issue | Notes |
|----------|-------|-------|
| Medium | Copy M-001, M-002, M-003 to `_template/methods/` in generic form | Strip PI specifics; add parameterization notes |
| Medium | Write `_template/CLAUDE-template.md` | Generic Claude Code setup for AR projects |
| Low | Extract as separate repo when stable | After 5+ sessions and external review |

---

## 2026-05-20 — Project initialized + methodology scaffolding

**Session goals:** seed the project; design the research persona; define core techniques; begin first deep read.

### Infrastructure
- Created GitHub repo `Protocol-Institute/humboldt` (private, will go public)
- Scaffolded full directory structure, core documentation files, agent code skeleton
- Registered in `../admin/keys.md` (reuses c3po keys — no new provisioning)
- Full pipeline validated: Voyage embed → Pinecone retrieval → Claude synthesis

### Persona design
- Defined SOUL.md — first version based on c3po's style template, adapted for researcher role
- Identified key design tensions (see `persona_design_notes.md`):
  - **Corpus boundary problem:** agent writes "NOT IN CORPUS" instead of reasoning from general knowledge. SOUL.md inherited this from c3po. Must be fixed — Humboldt's epistemic boundary should be evidence quality, not corpus membership.
  - **Identity vs. method separation:** SOUL.md conflates who Humboldt is with how it does research. These should be separated: SOUL = identity/voice/goals; METHOD = investigative approach; `methods/` = specific procedures.
  - **Input mechanism design:** defined four input types for how Humboldt finds new material (lit surveys, researcher discourse, own past records, proactive tips from collaborators)

### Technique inventory (methods/)
- **M-001 (Random Links):** generative; force structural connection between two disparate inputs → candidate law. Worked example: coal mines + blockchain → H-002.
- **M-002 (Canonical Domains):** dual-use; maintain five home domains as analogy reservoirs and stress-test beds. Canonical domain set in `canonical-domains.yaml`.
- **M-003 (Deep Read):** analytical; fully internalize a foundational text over multiple sessions. First text: Simon's *Sciences of the Artificial*.

### Three-track structure defined
- Track 1 (Research): notebook + research inventory
- Track 2 (Persona): dev-log + SOUL + CLAUDE + methodology artifacts
- Track 3 (Template): `_template/` folder for artificial researcher pattern

---

## Open Issues (Track 2)

| Priority | Issue | Notes |
|----------|-------|-------|
| High | Fix SOUL.md corpus-boundary problem | Humboldt must use general knowledge freely, marking provenance; never write "NOT IN CORPUS" |
| High | Create METHOD.md | Separate investigative methodology from persona identity |
| Medium | Update SOUL.md to reference methods/ inventory | SOUL = who; METHOD = how; methods/ = specific procedures |
| Medium | Design Discord integration | "new-nature" channel as Humboldt's lab; participation policy; bot component |
| Low | Implement periodic survey mechanism | Theory-driven retrieval from current inventory state |

## Open Issues (Track 3)

| Priority | Issue | Notes |
|----------|-------|-------|
| Medium | Review `_template/` and extract generalized patterns | Initial scaffold done; needs review after a few more Track 1 sessions to see what generalizes |
| Low | Consider extracting template as a separate repo | Premature until the pattern is stable after 3+ research sessions |
