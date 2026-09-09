# Architecture v2 — Humboldt as a funnel

*Design of record for the 2026-08 redesign. Version 1 describes the system as originally
built and as it still runs in production; this describes what it is being rebuilt into.
Phases 1–3 are built, Phase 4 is in progress, Phases 5–6 are not started.*

---

## Why there is a version 2

Twenty-three sessions in, the diagnosis was not that anything was broken. It was that the
infrastructure had grown faster than the research it existed to serve. Roughly 8.6K lines
of code consumed each session on maintenance while the research pipeline sat blocked: 48
curiosity items with no route to becoming anything, no hypothesis ever created from one,
no phase advancement in months.

The deeper problem was that Humboldt had no single thing it *produced*. Output was
scattered across lab notebook entries, five separate typed-artifact directories, and a
handful of site pages. Asked "what has Humboldt made?", there was no one answer, and
therefore no way to tell whether a week had been productive.

Version 2 keeps the underlying idea from version 1 — a behavior graph organized into the
Double Freytag phase model — and rebuilds everything else around a single sentence:

> **Humboldt is a funnel that turns raw research inputs into published candidate laws.
> Everything either moves material down the funnel or gets deleted.**

The measure that follows from this is **law accumulation rate**: new law records created,
and stage advancements, per unit time. Every architectural choice below is answerable to
that number.

---

## The supervision model

The relationship is a PhD supervisor and a doctoral student, and the architecture takes
that literally. The supervisor sets direction, may read or edit anything at any time,
personally designs only the hardest behaviors, and reads analytics to tune how the system
allocates its own effort. Humboldt does the day-to-day work.

Three consequences run through the whole design:

- **Everything is supervisor-editable.** Laws, behaviors, and the transitions between
  them live in files with an editor over them. Nothing important is buried in code.
- **Nothing self-modifies silently.** Humboldt may *propose* changes to its own behavior
  graph; it may not apply them. Proposals land in an approval queue.
- **State is files in git, not a database.** Git is the audit trail and the undo. A change
  to how Humboldt thinks should be as reviewable as a change to what it thinks.

---

## The one artifact

Version 1 had five typed research artifacts — curiosity, hypothesis, candidate law,
theory, falsification monitor — one per phase of the arc, with items migrating between
directories as they matured. In practice this made the *type* carry the maturity, so
advancing an idea meant rewriting it somewhere else, and most ideas never moved.

Version 2 has **one artifact: the law record.** A single file per law, carrying a `stage`
field that moves through the phases, and a `confidence` level that moves independently.
Advancing a law is now an edit to a field plus an appended history entry, not a migration.

Two things move separately and are deliberately not collapsed:

- **Stage** — where the law is in its life: exploration → sensemaking → valley → heavy
  lift → retrospective.
- **Confidence** — how much the evidence supports it: speculative → provisional →
  supported.

There is no "established". A law that survives is *unfalsified*, which is a weaker and
more honest claim. Every law carries, from birth, both an advance trigger and a challenge
trigger — the conditions that would promote it and the conditions that would break it. A
law without a stated falsification condition is not a law yet, and the schema refuses it.

Below the law records sits a **seed pool**: fragments that are law-shaped but not yet laws.
Seeds are where the old curiosity items went, and where reading notes deposit anything
promising. Seeds are raw material, not a stage.

**The encyclopedia publishes every stage**, badged with stage and confidence rather than
filtered to the confident ones. Showing a speculative law as speculative is the point.

---

## The evidence layer

Every claim a law makes should be traceable to something read. A single canonical
bibliography holds every source, each with a **read depth** recording how seriously it has
actually been engaged:

- **listed** — known to exist, not yet read.
- **shallow** — read once for gist; a one-paragraph synthesis note exists.
- **deep** — read properly from the actual text, with full reading notes.

The distinction is load-bearing rather than decorative. A law supported entirely by
shallow reads is in a different evidential position from one grounded in deep reads, and
the record makes that visible instead of letting citation count stand in for rigour.
Deep reads are also the one place the system refuses to cut a corner: they must read the
source text, never the model's memory of it.

---

## The funnel

Eight stages, each with a scheduled consumer. The organizing rule is that **nothing
accumulates without something that eats it** — every stage boundary is a queue, queue
depth is monitored, and a growing queue is an alarm rather than a normal condition.

```
   inbox            notes + seeds           law records          the world
     │                    │                      │                   │
  intake ─→ triage ─→ shallow read ─→ induct ─→ assess ─→ publish ─→ monitor
                          │              ↑                              │
                      deep read ─────────┘         challenge ───────────┘
```

- **Intake** gathers raw material — feeds, Discord conversations, links.
- **Triage** scores it against the current law inventory and seed pool, and discards most
  of it. Everything surviving gets a bibliography entry.
- **Shallow read** produces a synthesis note, and emits a seed when it finds something
  law-shaped. It also decides whether a source deserves a deep read.
- **Deep read** is the expensive path: the full text, real reading notes.
- **Induct** is the first of two engines that actually move laws. It reads accumulated
  notes and seeds and either drafts a new candidate law, attaches evidence to an existing
  one, or returns nothing. *Returning nothing is a normal and respectable result* — most
  sweeps should not produce a law.
- **Assess** is the second engine. It takes one law and holds it against its own advance
  and challenge triggers, and returns promote, hold, or demote. Because the triggers were
  written when the law was drafted, this is a test rather than a judgement call.
- **Publish** puts law events into the world: the site, and announcements.
- **Monitor** watches published laws for counterevidence and can cycle a law backwards.

The cycle-back is what makes this a loop rather than a pipeline. A challenged law does not
get deleted; it returns to an earlier stage carrying the challenge with it.

---

## The behavior graph

Everything Humboldt does is a **behavior**: a named, file-defined unit of work with a
trigger, a model tier, and a declared list of what it produces. The funnel stages above
are behaviors; so are responding on Discord, reviewing the community's conversations, and
the supervisory sweep that analyses the graph itself.

Behaviors are nodes in a directed graph, grouped by phase, with edges representing
transitions. **Every edge carries a trigger** — the condition under which that transition
is taken. An edge without one is rejected, because an untriggered edge is a claim about
the system's behavior that nothing can check.

The registry was cut from 26 behaviors to 12 during the redesign, and the pruning
criterion was simple: a stub that had never run was deleted rather than preserved. A
thirteenth, `review`, was added when analytics revealed a daily loop that had been running
since session 9 with no registry entry to account for it.

**Graph evolution is proposal-only.** Humboldt can suggest new behaviors, retirements, and
trigger changes; each lands in the approval queue as either a *simple* change the
supervisor can wave through or a *hard* one requiring genuine design attention. Nothing
reaches the running graph without an explicit approval, and approval and application are
separate steps so an approval can itself be reviewed before it lands.

---

## The analytics overlay

The graph can only learn from traffic it can see, which makes measurement architectural
rather than incidental. Three ledgers, deliberately kept separate because they count
different things and summing them would produce a number that looks authoritative and
means nothing:

| ledger | unit | answers |
|---|---|---|
| behavior log | one invocation (one sweep or run) | how often did this behavior run? |
| law events | one law lifecycle event | is the KPI moving? |
| cost ledger | one model API call | what is this behavior costing? |

An **invocation is a sweep, not an item and not an API call.** A single shallow-read sweep
processing two thousand items is one invocation that produced two thousand outputs — the
volume lives in the output counts, so the graph's transition statistics stay about
movement between behaviors rather than item churn.

Each invocation records **what it produced, counted by type**, drawn from the behavior's
own declared outputs. This is what makes a specific kind of silent degradation visible: a
behavior that keeps running normally while one of its output types quietly drops to zero.

Cost is deliberately *not* recorded on the invocation. It is attributed by joining the
cost ledger on operation label, which stays correct even when several behaviors run
concurrently — a timestamp-based join would not.

A **run identifier** minted per sweep is carried onto the law events that sweep caused, so
"which induction run created this law?" is answerable without merging the ledgers.

From these, a weekly supervisory sweep computes utilization and raises **flags** —
candidates for pruning, splitting, or attention. Flags are proposals; they enter the
approval queue like any other graph change. The prune test compares a behavior against
*its own* history rather than an absolute floor, because behaviors legitimately run at
wildly different rates, and some — interactive deep reads, local computation — make no
model calls at all and would otherwise look permanently dead.

---

## The supervisor console

One web application over the whole system, replacing the scattered admin pages of version
1. Six views: a dashboard of KPI and queue depths, a law editor, the behavior graph with
its transition triggers, the approval queue, analytics, and the interlocutor models.

Its defining property is that **it edits the repository**. Every save is a file change
that appears in the next diff and lands as its own commit. There is no separate console
database that could disagree with the files, and no state visible in the UI that is not
also visible in git history.

Where the console *runs* is being revisited. Version 2 as originally planned put it on the
server behind an SSH tunnel; that has proved to be too much friction for the supervision
it was meant to enable, and moving it onto the authenticated web is under evaluation.

---

## Where it runs

The organizing decision is that **autonomous operation should not depend on a laptop being
awake**. Scheduled work moves to an always-on server; genuinely supervised work stays in
interactive sessions.

| | what runs there |
|---|---|
| **Server** | The daemon, all scheduled funnel behaviors, the Discord presence, batch deep reads |
| **Sessions** | Interactive deep reads, hard behavior design, anything touching the persona documents |
| **Anywhere** | The console — approvals, law edits, trigger tuning, analytics |

**Git is the synchronization fabric.** The repository is the single source of truth;
automated writes commit and push, interactive sessions push as normal, and the server
pulls. Deploys are pulls. There is no separate deployment machinery and no state that
lives outside the repo — which is what makes the whole system reviewable, and recoverable,
with ordinary version-control tools.

---

## Status

| Phase | | |
|---|---|---|
| 1 | Output layer — law records, bibliography, encyclopedia | built |
| 2 | Funnel engines — induction and assessment | built |
| 3 | Behavior graph, approval queue, supervisor console | built |
| 4 | Analytics overlay | in progress |
| 5 | Quiet-mode Discord, server cutover | not started |
| 6 | Shakedown and documentation | not started |

Version 1 remains the accurate description of what is currently deployed. The two will
converge when the redesign merges.
