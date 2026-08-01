# Humboldt Redesign — August 2026

**Status:** DRAFT — under supervisor review
**Supersedes:** the session-14 typed-artifact schema (C/H/CL/T/F), the 26-behavior registry, and the current daemon presence design once implemented.

---

## 1. Purpose and diagnosis

Twenty-three sessions in, the infrastructure layer (~8.6K LOC) consumes every session on
maintenance while the research funnel is blocked: 48 curiosities with no promotion path,
zero H items ever created, no phase advancement since June. Output is scattered across
notebook entries, five artifact directories, and site pages — there is no single thing
Humboldt *produces*.

This redesign keeps the basic architecture — an MDP-style behavior graph organized in
Double Freytag phases (Tempo) — and rebuilds everything around one principle:

> **Humboldt is a funnel that turns raw research inputs into published candidate laws.**
> Everything either moves material down the funnel or gets deleted.

**KPI: law accumulation rate** — new law records created, and stage-advancement events,
per unit time.

Supervision model: the operator is a **PhD supervisor** — sets direction, reviews and
edits anything at any time, designs only the hardest behaviors, and reads analytics to
tune the graph. Humboldt does the day-to-day work.

### Decisions locked 2026-08-01

1. **Unified law record** replaces C/H/CL/T/F typed artifacts. One YAML per law, `stage`
   field cycles through the Double Freytag phases; cycle-back on challenge.
2. **Encyclopedia publishes all stages**, clearly badged with stage + confidence.
3. **Discord: law events only.** Proactive posts fire only on law created / promoted /
   challenged. @mentions get replies gated by a relevance threshold. Digest and
   conversation-review posting retire.
4. **Existing 48 C items become the seed pool** — no batch extraction pass; routine
   induction sweeps consume them gradually.
5. **Comprehensive bibliography published on the site**, along with shallow- and
   deep-read summaries.
6. **Autonomous operations move to the exe.dev server** (§12): the daemon and all
   scheduled funnel behaviors run there, unblocked from laptop sessions. The supervisor
   console is server-hosted, reached over an SSH tunnel. Interactive deep reads stay
   session work, but batch deep reads may run on the server on remote trigger.

---

## 2. Design principles

1. **Single output format.** The law record is the only research artifact type. Notes,
   seeds, and bibliography entries exist to feed and support law records.
2. **Unblocked funnel.** Every pipeline stage has a scheduled default consumer. Nothing
   accumulates without something that eats it. Queue depth is monitored; a growing queue
   is an alarm, not a norm.
3. **Files in git, no database.** All state is YAML/JSONL/Markdown in the repo. The
   console UI reads and writes these files; git is the audit trail and undo.
4. **Everything supervisor-editable.** Laws, behaviors, transition triggers — all live
   in files with a UI editor over them. Nothing is buried in code.
5. **Model-tier economy.** Haiku for triage/routing, Sonnet for routine synthesis, Opus
   for deep reads and hard synthesis, supervisor only for what Claude can't do.
6. **Delete what didn't earn its keep.** Stubs, empty directories, and disabled code
   paths are removed, not preserved.

---

## 3. The law record and the encyclopedia

### 3.1 Law record schema — `laws/L-NNN.yaml`

```yaml
id: L-007
title: Formalization Ratchet
slug: formalization-ratchet
stage: valley            # exploration | sensemaking | valley | heavy-lift | retrospective
status: active           # active | challenged | falsified
origin: discovered       # discovered | imported
confidence: provisional  # speculative | provisional | supported | unfalsified
statement: >
  One-to-three crisp sentences. The law itself.
justification: >
  Prose: why believe this. Mechanism, argument, provenance of the idea.
examples:
  - domain: urban planning
    description: ...
    source: bib-0042          # bibliography id
counterexamples: []           # same shape; challenges live here
references: [bib-0042, bib-0107]   # bibliography ids
seeds: [seed-031]             # seed items that fed this law
triggers:                     # supervisor-editable, plain language + optional check
  advance: "Evidence from 3+ independent domains; mechanism stated falsifiably"
  challenge: "A counterexample survives one assessment pass"
history:                      # append-only
  - {date: 2026-06-05, event: created, detail: "from CL-001"}
  - {date: 2026-06-13, event: evidence, detail: "Rittel & Webber deep read"}
  - {date: 2026-08-xx, event: promoted, detail: "sensemaking → valley"}
```

Rules:

- **Stage** retains Double Freytag semantics. `retrospective` = published-and-monitored;
  never "established," only unfalsified (METHOD.md unchanged on this).
- **Challenge/falsification cycle-back:** a surviving challenge demotes the stage (with
  history entry) rather than deleting the law. `falsified` status archives it in place —
  falsified laws stay in the encyclopedia, labeled, as negative results.
- **History is append-only** and is the narrative record — the DS arc files retire; their
  content folds into the corresponding law's history and the notebook.
- The supervisor may edit any field at any time (console UI or directly in the YAML).

### 3.2 Seeds — `laws/seeds/`

A holding pen of law-shaped fragments not yet worth a record: one small YAML or MD file
per seed (idea, observation, motif, question). The 48 existing C items migrate here
unchanged in content. Shallow and deep reads emit new seeds. Induction sweeps sample
seeds and either promote them into exploration-stage laws, attach them to existing laws
as evidence, or leave them. Seeds are cheap and unmanaged — no schema ceremony beyond
id/title/text/source.

### 3.3 Encyclopedia — published on humboldt-site

- `/laws/` — index of all law records, filterable by stage, status, confidence; sorted
  by recency of last event. Each law gets an anchor/page rendering: statement,
  stage+confidence badges, justification, examples, counterexamples, references (linked
  into the bibliography), and history timeline.
- The KPI chart (law events over time) renders at the top of the index.
- Rebuilt by the publish step (§5, stage 7) from `laws/*.yaml`. No hand-edited HTML.

### 3.4 Migration of existing artifacts

| Current | Becomes |
|---|---|
| `research/cl/CL-001..003` | `laws/L-001..003`, stage `valley` |
| `research/theories/T-001..002` | laws, stage `heavy-lift` |
| `research/theories/T-003..004` (imported Goodhart/Gall) | laws, stage `heavy-lift`, origin `imported` |
| `research/c/*` (48) | `laws/seeds/` |
| `research/ds/*` | history entries on the corresponding laws; files archived |
| `research/h/`, `research/f/` | deleted (never held an item) |
| `research/agenda.md` | kept — Humboldt's own queue, now organized by funnel stage |

Archived files move to `research/_archive/` in one commit so history stays browsable.

---

## 4. Bibliography and reads — the evidence layer

### 4.1 Canonical bibliography — `bibliography/bibliography.yaml`

One entry per source Humboldt has ever engaged with past triage-discard:

```yaml
- id: bib-0042
  title: "Dilemmas in a General Theory of Planning"
  authors: [Rittel, Webber]
  year: 1973
  url: ...
  encountered: feed          # feed | discord | operator | citation-chase
  read_depth: deep           # listed | shallow | deep
  kind: content              # content | meta  (meta = how-to-do-research reads)
  notes: bibliography/notes/rittel-webber.md      # if deep
  summary: bibliography/shallow-reads/2026-06-13-....md  # if shallow
  laws: [L-003]              # laws citing this source
```

Triage-in creates the entry (`listed`); shallow/deep reads upgrade `read_depth` and link
their outputs; law references point at `bib-` ids. Existing `references.yaml`, reading
notes, and shallow-read files migrate in.

### 4.2 Published on the site

- `/bibliography/` — full bibliography, filterable by read depth / kind / year, each
  entry linking to its read summary or notes and to the laws citing it.
- `/reading/` — extended: deep-read notes (as now) **plus shallow-read summaries**,
  grouped by date, each cross-linked to its bibliography entry.

The bibliography count and read-depth breakdown become secondary dashboard metrics
(input side of the funnel, complementing the law-rate output side).

---

## 5. The funnel

Eight stages. Each is one production behavior with an owner (daemon schedule or
session), a model tier, and an editable trigger. **This table is the spine of the whole
system.**

| # | Stage | Behavior | Runs | Model | Consumes → Produces |
|---|-------|----------|------|-------|---------------------|
| 1 | Intake | `intake` | daemon, continuous | code | feeds + Discord capture + operator drops → `inbox/` items |
| 2 | Triage | `triage` | daemon, daily | Haiku | inbox items → discard / shallow / deep, tagged `content` or `meta`; bibliography entries created |
| 3 | Shallow read | `shallow-read` | daemon, daily | Haiku | shallow queue → summary + embed + seeds/evidence + bibliography update |
| 4 | Deep read | `deep-read` | session or batch | Opus | deep queue → notes + seeds/evidence + bibliography update. **Meta deep reads → graph-change proposals (§7.4)** |
| 5 | Induction | `induct` | daemon, weekly + session | Sonnet | new seeds + recent reads + existing laws → new exploration-stage laws, evidence attachments |
| 6 | Assessment | `assess` | daemon, weekly + session | Sonnet/Opus | each active law vs its `advance` trigger → promotion, or a recorded gap ("what's missing"). Retrospective laws get periodic challenge attempts |
| 7 | Publish | `publish` | daemon, on law event | code | laws + bibliography + reads → site rebuild + Discord law-event post |
| 8 | Monitor | `monitor` | daemon, weekly | Haiku→Sonnet | retrospective laws vs new corpus material → challenge flags → cycle-back via `assess` |

Unblocked-funnel guarantees:

- Stages 2, 3, 5, 6, 8 run on schedule regardless of session activity — the funnel
  advances while the supervisor is away. "Daemon" here means the exe.dev server (§12),
  not a laptop process.
- Deep reads (stage 4) are the one intentionally session-gated stage (quality over
  throughput); the batch-deepread path remains for clearing queues and can run
  server-side on remote trigger (§12).
- Queue depths at every stage boundary are logged and surfaced in analytics; a queue
  growing for N consecutive weeks flags the consuming behavior for attention.

The **content/meta distinction** enters at triage: `meta` reads (research methodology,
epistemics, how-great-researchers-work) route down the same shallow/deep paths but their
terminal output is different — instead of seeds/evidence for laws, they produce
**graph-change proposals** that feed the behavior-evolution loop (§7.4).

---

## 6. Behavior graph — pruned and specified

### 6.1 The pruned registry

The 26-behavior registry reduces to the funnel behaviors (§5) plus:

| Behavior | Phase | Purpose |
|---|---|---|
| `orient` | liminal | Session bootstrap: read state, pick focus (replaces boot-000/001 + BOOTSTRAP ceremony) |
| `respond` | any | Discord @mention response, relevance-gated |
| `graph-evolve` | retrospective (meta) | Turn meta-read proposals + analytics flags into registry/transition changes via the approval queue |
| `supervisory` | retrospective (meta) | Weekly analytics sweep: utilization, queue depths, prune/split flags, KPI report |

Everything else — the ~14 unbuilt stubs (backpocket viewing, curiosity browsing, field
trip, bullshit detector, cross-training, …) — is **deleted from the registry**. The good
ideas among them are re-expressible later as behavior requests through the new
definition pipeline (§6.3); they are not carried as dead weight.

### 6.2 Behavior spec — `behaviors/registry.yaml`

Every behavior entry must be complete enough to run or to hand to a definition session:

```yaml
- id: induct
  name: Law Induction Sweep
  phase: sensemaking
  status: active            # active | proposed | retired
  defined_by: claude-sonnet # claude-sonnet | claude-opus | supervisor
  trigger: "Weekly; or ≥10 unconsumed seeds; or on session request"
  action:
    entrypoint: agent/induct.py
    model: claude-sonnet-5
    prompt: prompts/induct.md     # prompts live in files, editable in console
  produces: [law-created, evidence-attached]
  utilization: auto         # filled by analytics from the event log
```

Transitions in `behaviors/mdp.yaml` keep the same shape but every edge now requires a
`trigger` — a plain-language condition, supervisor-editable, optionally backed by a
programmatic check:

```yaml
- from: induct
  to: assess
  trigger: "A new law was created or ≥3 evidence attachments accumulated"
  weight: 0.8
```

### 6.3 Behavior definition triage — the supervisor bottleneck fix

New behaviors enter through **behavior requests** (filed by meta reads, analytics flags,
the supervisor, or a session). Each request gets a complexity classification:

- **Simple** (clear inputs/outputs, precedent exists in the registry, no new epistemic
  judgment): Claude drafts the full behavior spec — trigger, prompt, entrypoint sketch —
  at Sonnet level, Opus for borderline cases. Draft lands in the **approval queue**;
  supervisor approves/edits/rejects in the console. Target: the large majority of
  behaviors take this path.
- **Hard** (new epistemic standards, changes what counts as evidence or a law, touches
  identity/METHOD, or irreversible external behavior): routed to the **supervisor design
  queue** with a structured brief — the problem, why it's hard, what Claude would try.
  Supervisor designs it (or answers the brief's questions, demoting it to simple).

Classification rubric lives in `behaviors/definition-rubric.md`, itself
supervisor-editable.

### 6.4 Meta reads → graph evolution

Meta deep/shallow reads terminate in **graph-change proposals**: new-behavior requests,
trigger redefinitions, prompt amendments, prune suggestions — each citing the source
read. Proposals land in the same approval queue. This is the concrete mechanism by which
"meta reads drive the evolution of the behavior graph": Hamming teaches Humboldt how to
work → a proposal to change how `assess` weighs important-problem selection → supervisor
approves → registry changes, with the bibliography entry as provenance.

---

## 7. Supervisor console — the web UI

One web app replacing `behaviors/admin.html` + `agent/behaviors.py`. Same
implementation philosophy as now — Python stdlib HTTP server + a single-page static
frontend on port 7878 — but redesigned around supervisor workflows. It reads and writes
the repo's YAML directly; every save is a file edit the next `git diff` shows, and the
console commits+pushes its own writes (one commit per save, tagged `[console]`).

It runs on the exe.dev server against the server's live checkout, bound to localhost and
reached via SSH tunnel (§12) — so approvals, law edits, and trigger tuning happen from
any device without a laptop session. It can also run locally against the laptop checkout
(same code, `humboldt console`) when working offline; git is the reconciliation fabric.

Views:

1. **Dashboard** — KPI chart (law events over time), funnel queue depths (bar per stage
   boundary), last-7-days activity feed, daemon status/pause state.
2. **Laws** — table of all law records (stage, status, confidence, last event) → full
   editor: every schema field editable, stage override with required history note,
   challenge button. Seeds browsable in a side tab.
3. **Graph** — the D3 phase-flow visualization (kept from the brain page), nodes colored
   by utilization; click node → behavior editor (trigger, prompt file, model tier,
   status); click edge → transition trigger editor.
4. **Queue** — the approval queue: Claude-drafted behavior specs, graph-change proposals
   from meta reads, prune/split suggestions from analytics. Approve / edit-then-approve /
   reject, each with a one-line rationale that goes into the log.
5. **Analytics** — per-behavior utilization (invocations, outputs, cost), queue-depth
   trends, flags list (§8).
6. **People** — the interlocutor models (§9): view/edit trust and model text.

The console does not need the daemon running — it operates on files; the daemon picks
changes up on its next tick (registry/laws are re-read per task, no restart requirement
for content changes).

---

## 8. Analytics overlay

Event spine: `behaviors/log.jsonl` — every behavior invocation (already partially in
place) plus every law event and queue snapshot, appended by the behaviors themselves.

The weekly `supervisory` behavior computes and writes `analytics/weekly-YYYY-MM-DD.yaml`:

- **KPI**: law events this week / trailing 4 weeks (created, promoted, challenged).
- **Funnel throughput**: items in/out per stage, current queue depths, depth trend.
- **Per-behavior utilization**: invocations, outputs produced, API cost.
- **Flags:**
  - *Prune candidate* — active behavior, zero invocations in 4 weeks, or invocations but
    zero outputs in 6 weeks → proposal to retire or trigger-redefine (into approval queue).
  - *Split candidate* — behavior consuming an outsized share of invocations/cost, or its
    queue persistently growing → proposal to fork into sub-behaviors, with a suggested
    split (into approval queue, usually a *hard* definition → supervisor).
  - *Stalled law* — no history event in 6 weeks on an active non-retrospective law →
    surfaced on dashboard for `assess` prioritization.

Flags are proposals, never auto-applied — the graph changes only through the approval
queue.

---

## 9. Discord persona — quiet mode

**Posting policy: law events only.**

- Proactive posts fire solely on law lifecycle events: created (exploration entry into
  the encyclopedia), promoted a stage, challenged, falsified. One short post, linking to
  the law's encyclopedia page. Naturally rate-limited by the actual KPI; quiet weeks are
  silent. A per-day cap (default 2) guards against migration/burst noise.
- **@mentions**: always answered, but through a relevance gate — if Humboldt has nothing
  research-grounded to add, it says so briefly rather than synthesizing engagement.
  Response length bias: short.
- **Retired**: `task_weekly_digest`, conversation-review *notebook writing* (the daily
  synthesis entries were the chattiness source), proactive `_new_nature_tick` posting
  (currently disabled — code now deleted), thread farming as a separate task,
  person notebook entries.
- **Kept, silent**: idea/link capture from channels (feeds the funnel), a weekly
  conversation sweep replacing the daily review — output goes to `inbox/` only, never to
  the notebook or the channel.

**Social model — clean but limited.** `daemon/people.json` (gitignored) slims to:

```json
{"handle": "@x", "first_seen": "...", "last_seen": "...", "interactions": 14,
 "trust": 0.7, "model": "≤3 sentences: what they know, what they keep raising,
 how their thinking relates to active laws.", "contributions": 3}
```

Trust rises with contributions that survive triage into the funnel; it modulates how
much weight `respond` and `triage` give to their suggestions. No further person
machinery. Cap the store at ~50 people, least-recently-seen evicted.

---

## 10. Persona documents and notebook

- **Keep**: `IDENTITY.md`, `LINEAGE.md`, `MEMORY.md` — the identity spine, unchanged in
  role. `METHOD.md` — updated for the law-record confidence/stage rules.
- **Simplify**: `BOOTSTRAP.md` collapses to the `orient` behavior's spec (read state →
  check flags/queues → pick focus). `methods/M-*.md` files retire; anything still live
  moves into behavior registry entries or METHOD.md. `SOUL.md` (already archived),
  `persona_design_notes.md`, `ROADMAP.md` → `_archive/`.
- **Notebook**: unchanged as Humboldt's first-person journal, written at sessions and by
  significant daemon events (law promotions, not daily reviews). Pre-notebook queue stays.

---

## 11. Codebase restructure

Target: cut total LOC meaningfully while adding the console. Everything grouped by
funnel role.

```
agent/
  humboldt.py      CLI — regrouped subcommands: funnel (triage/read/induct/assess),
                   laws, bib, publish, console, daemon, discord
  retrieval.py     keep (two-index Pinecone + Voyage)
  ingest.py        keep (incremental); extend chunk types to laws/seeds/bibliography
  laws.py          NEW — law record CRUD, stage machine, validation, history
  bibliography.py  NEW — canonical bib CRUD, migration from references.yaml
  triage.py        rework — unified feed+discord triage, content/meta tagging, bib entry creation
  reads.py         rework — merges shallow_read.py + deepread paths; emits seeds/evidence/bib updates
  induct.py        NEW — induction sweep
  assess.py        NEW — trigger evaluation, promotion, challenge handling
  publish_site.py  rework — adds /laws/, /bibliography/, extended /reading/
  console.py       NEW — supervisor console server (replaces behaviors.py admin)
  analytics.py     NEW — event log aggregation, flags, weekly report
  synthesizer.py   keep, slimmed to shared Claude-call plumbing
  costs / notebook_index / pre-notebook   keep

daemon/
  runner.py, state.py, pause.py, costs.py   keep
  discord_client.py   slimmed — mentions + law-event announcer + capture + schedule ticks
  capture.py          keep (silent capture; absorbs thread_farmer + weekly sweep)
  feed_monitor.py     keep
  presence.py         slimmed — respond() and law_event_post(); digest/proactive code deleted
  people.py           slimmed to §9 model
  RETIRED: thread_farmer.py, conversation_review.py, notebook_watcher.py
           (publish moves to a post-law-event hook), person_notebook.py

laws/           L-NNN.yaml + seeds/
bibliography/   bibliography.yaml + notes/ + shallow-reads/ + deep-reads/ (PDFs)
behaviors/      registry.yaml, mdp.yaml, log.jsonl, definition-rubric.md, prompts/
analytics/      weekly-*.yaml
research/       agenda.md + _archive/ (everything else migrates out)
```

---

## 12. Deployment — exe.dev server

Autonomous operation moves off the laptop onto the supervisor's exe.dev server. The
laptop stops being a dependency for anything that doesn't actually need supervision.

> **Provisioned 2026-08-01:** VM `humboldt.exe.xyz` (2 vCPU · 4 GB · 20 GB, Ubuntu
> 24.04, systemd, Python 3.12), dedicated to this project per the one-VM-per-project
> policy in `Code/warnings-exe.md`. SSH key, config stanzas, and the
> `humboldt-console` tunnel alias (`ssh humboldt-console` → localhost:7878) are in
> place on the laptop. Phase 5 cutover deploys onto this box.

### 12.1 Topology

| Where | What runs | Why |
|---|---|---|
| **exe.dev server** | Daemon (all scheduled funnel behaviors §5: intake, triage, shallow reads, induction, assessment, publish, monitor, supervisory sweep), Discord bot, console server, on-demand batch deep reads | Always-on; the funnel advances continuously |
| **Laptop sessions** | Interactive deep reads, hard behavior design, migration/dev work, anything touching METHOD/IDENTITY | The genuinely supervised work |
| **Any device** | Console via SSH tunnel — approvals, law edits, trigger tuning, analytics review, pause/unpause | Supervision without a session |

### 12.2 Git as the sync fabric

The GitHub repo (`Protocol-Institute/humboldt`) is the single source of truth. The
server runs a plain clone (not Dropbox — which also sidesteps the Dropbox/working-tree
gotchas the laptop copy lives with).

- **Server writes:** automated behaviors commit and push their outputs (notes, seeds,
  law events, bibliography, analytics, log) — as the daemon already does for notebook
  entries. Every automated commit is prefixed `[daemon]` or `[console]` for a clean
  audit trail. `git pull --rebase` before every write cycle; on conflict, the behavior
  skips its write, logs the failure, and retries next tick (conflicts should be rare:
  server writes are additive files or designated YAML paths).
- **Laptop sessions** push as normal; the server picks changes up on its next pull.
  A systemd timer also does a plain `git pull` every few minutes so supervisor edits
  (from console or laptop) reach the running daemon quickly.
- **Deploys are pulls:** code changes reach the server via the same pull path + daemon
  hot-reload (SIGUSR1) or systemd restart. No separate deploy machinery.

### 12.3 Process management and access

- **systemd units** replace the Mac launchd plist: `humboldt-daemon.service` and
  `humboldt-console.service`, both `Restart=always`, logs to journald. The launchd
  plist on the laptop is unloaded and deleted at cutover.
- **Console access:** console binds to `localhost:7878` on the server; supervisor
  reaches it with an SSH tunnel (`ssh -L 7878:localhost:7878 <exe-host>`, wrapped in an
  SSH config alias so it's one command). No public exposure, no auth code to maintain.
- **Remote control:** `daemon pause/unpause`, `daemon restart`, `batch-deepread`, and
  `console` are all invocable over SSH; the console gets pause/unpause and
  batch-deepread trigger buttons so routine control needs no terminal at all.

### 12.4 Secrets and safety rails

- `.env` provisioned on the server by copying the needed keys from the PI key store
  (registered in `../admin/keys.md` per PI security policy, with the server listed as a
  deployment location). Standard file permissions (`chmod 600`); never committed —
  same policy as the laptop, minus the Dropbox xattr concerns.
- **Cost circuit breaker** ($/day cap in `daemon/config.yaml`) matters more on an
  always-on box — it stays on every Claude call site, and the daily spend is surfaced
  on the console dashboard.
- **Pause is global:** the pause state lives in the repo-adjacent `state.json` on the
  server; pausing from the console or SSH gates every posting/querying/writing call
  site there, exactly as designed in session 23.

### 12.5 Relationship to the public site (humboldt.protocol-institute.org)

The exe.dev VM does **not** host the public site. Hosting stays exactly where it is:
static pages + the chat Pages Function on **Cloudflare Pages**, at
humboldt.protocol-institute.org. What changes is *who runs the build-and-deploy step*:
today the laptop daemon runs `publish-site` (build.py + `wrangler pages deploy`); after
cutover, the `publish` behavior runs it on the VM, using CF credentials in the VM's
`.env`. The VM is the factory; Cloudflare is the storefront.

The VM's own `https://humboldt.exe.xyz` endpoint is unrelated to the public site — it
stays private (exe.dev-authenticated) and unused; the console is reached only via the
SSH tunnel, and nothing else on the VM serves HTTP.

### 12.6 What this changes elsewhere

- The long-standing TODO "[L] always-on machine deployment" closes.
- Batch deep reads (stage 4) become remotely triggerable: queue clearing no longer
  waits for laptop time; results land as commits for later supervised review.
- The laptop checkout remains fully functional for sessions — nothing becomes
  server-only except the always-on scheduling.

---

## 13. Migration plan

Work happens on a branch (`redesign-2026-08`); the daemon stays paused (through
2026-08-15, extend if needed) until Phase 5 lands. Each phase is one or two sessions and
ends in a working state.

### Build-tier legend

Which model implements each workstream. (Distinct from the *runtime* tiers in §5 —
those are what the behaviors call in operation; these are who builds them.)

- **[FABLE]** — supervisor-session work with Fable: architecture judgment, the
  epistemic core (what counts as a law, evidence, promotion), content-bearing
  migrations of research artifacts, anything touching METHOD/identity, high-blast-radius
  cross-cutting refactors.
- **[OPUS]** — complex engineering against a clear spec: multi-file code, async/daemon
  work, persona-voice prompts (with supervisor review), failure triage.
- **[SONNET]** — well-scoped implementation from spec: page templates, CRUD forms,
  charts, scripts, mechanical migrations, doc updates.

Fable's irreplaceable share is concentrated in Phases 1–3; most of the LOC is
Opus/Sonnet work.

> **Fable pre-work: COMPLETE (2026-08-01, on branch `redesign-2026-08`).** All
> [FABLE]-tagged deliverables are done and committed, so the remaining phases can run
> in Opus/Sonnet sessions with this doc as the spec:
> - `laws/_schema.yaml` — final schema + definitive stage-machine rules (§3.1).
> - `laws/L-001..L-007` — all seven laws migrated with content, counterexamples,
>   triggers, and histories folded from CL/T/DS (mapping per §3.4; original L-numbers
>   restored). Old `research/` files left in place; moving them to `_archive/` is the
>   Phase 1 [SONNET] cleanup, along with `research/c/` → `laws/seeds/`.
> - `prompts/induct.md` + `prompts/assess.md` — the epistemic core (Phase 2 engines
>   consume these as templates; slots documented in each file).
> - `behaviors/definition-rubric.md` — SIMPLE/HARD classification + brief format
>   (Phase 3 approval-queue machinery consumes this).
> - Registry prune decisions are fully specified in §6.1 (keep-list + delete-list);
>   executing the rewrite of `registry.yaml`/`mdp.yaml` is Phase 3 [OPUS] work.
> Remaining Fable involvement is review-only (heuristics in Phase 4, persona prompts
> in Phase 5) — no further Fable-blocking work in the plan.

### Phases

- **Phase 1 — Output layer.** *The encyclopedia exists.*
  - **[FABLE]** Final law-schema semantics + stage-machine rules; the content-bearing
    migration of CL/T/DS artifacts (interpreting and folding research content into law
    records and histories per §3.4).
  - **[OPUS]** `laws.py` (CRUD, validation, history); `bibliography.py` + migration of
    references.yaml, reading notes, shallow-reads into the canonical bibliography.
  - **[SONNET]** Site pages: /laws/, /bibliography/, extended /reading/; C-items →
    seeds file move.
- **Phase 2 — Funnel engines.** *The funnel flows end-to-end, manually driven.*
  - **[FABLE]** `induct` and `assess` prompt + logic design — the epistemic heart:
    law-worthiness criteria, evidence attachment standards, promotion/challenge
    evaluation.
  - **[OPUS]** `triage.py`/`reads.py` rework (content/meta tagging, bib wiring, seed
    emission).
  - **[SONNET]** Publish hook + law-event plumbing.
- **Phase 3 — Graph + console.** *The supervisor can steer.*
  - **[FABLE]** Registry prune decisions; behavior-spec and transition-trigger
    semantics; the definition-triage rubric (`definition-rubric.md`).
  - **[OPUS]** Console server; laws/graph/queue editor logic; approval-queue format
    and application of approved changes.
  - **[SONNET]** UI polish: forms, dashboard, D3 view refresh, styling.
- **Phase 4 — Analytics.** *The graph is observable.*
  - **[OPUS]** Flag heuristics (prune/split/stall thresholds) + weekly supervisory
    report design (supervisor reviews the heuristics before they ship).
  - **[SONNET]** Event logging in all behaviors; `analytics.py` aggregation; console
    analytics view.
- **Phase 5 — Daemon quiet mode + server cutover.** *Humboldt is live again — quiet,
  and off the laptop.*
  - **[OPUS]** Discord rework per §9 (respond relevance gate, law-event posts — persona
    voice, supervisor reviews prompts); daemon task schedule per §5; dead-code
    deletion; people.json slimming.
  - **[SONNET]** exe.dev deployment per §12: clone, `.env` provisioning, systemd units,
    tunnel alias verification, launchd plist retirement. Unpause **on the server**.
- **Phase 6 — Shakedown + docs.**
  - **[OPUS]** Run the 519-item backlog through the new funnel on the server as the
    acceptance test; triage and fix what breaks; notebook entry in Humboldt's voice on
    the reorganization.
  - **[SONNET]** ARCHITECTURE.md, CLAUDE.md, `_template/` updates.

Rollback safety: migration commits are mechanical and separate from code commits;
`research/_archive/` preserves every retired artifact; the branch merges only after
Phase 5.

---

## 14. What gets deleted

For the record, the simplification ledger: research/h/, research/f/, research/ds/ (after
history fold), ~14 stub behaviors, methods/M-*.md, BOOTSTRAP ceremony, SOUL/ROADMAP/
persona_design_notes (archived), weekly digest, daily conversation-review notebook
entries, proactive engagement code, thread farmer, person notebook entries, old
per-page publish commands, behaviors/admin.html (superseded by console), and the laptop
launchd plist (`org.protocol-institute.humboldt.plist` — superseded by systemd on the
exe.dev server).
