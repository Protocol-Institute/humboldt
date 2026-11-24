# Supervisor review prep — 2026-11-23 (Session 42)

Prepared for the operator. Nothing here has been applied to a law record except the
mechanical `related:` backfill (§3). Every proposal below is a supervisor call.

## 1. L-012 — Intervention-Layer Displacement (review first, per TODO)

**What is new in it.** The record's one claim that L-004 (Goodhart) does not already make
is *causal-chain position*: the prediction is displaced into a terminal goal because it
sits upstream of the outcome in the protocol's own execution graph, "regardless of
optimization intensity". If that holds, it is a real law. If it doesn't hold, L-012
is a domain instance of L-004.

**Problems with the record as written:**

1. **The falsification condition tests the wrong claim.** It asks for a protocol where
   better prediction accuracy reliably improves outcomes. The statement is about where
   *institutional attention and optimization pressure* go, not about whether accuracy
   pays off. Accuracy could improve outcomes while attention is still displaced. Proposed:
   *"A deployed decision protocol whose governance cycle (oversight reviews, procurement
   renewals, vendor evaluation) is scored on the downstream outcome rather than on
   prediction metrics, sustained across 2+ cycles with no outcome-tracking mandate
   imposed from outside."*
2. **The distinguishing claim is not tested by any trigger.** "Regardless of optimization
   intensity" predicts that displacement appears even at *low* optimization pressure,
   where L-004 predicts little. Proposed `open_questions:` entry: *does displacement
   scale with optimization intensity (→ it is L-004) or appear at low intensity whenever
   the prediction is upstream in the protocol (→ distinct)?*
3. **The evidence is one seed deep.** Both examples are sourced to seed-058. The sepsis
   example is a plausible story, not a documented finding. The 58 citations from the
   session-38 backlog are triage-time *relevance* tags, not evidence. Nothing attached
   to the record came from them.
4. **No counterexample has been looked for.** Candidate to retrieve: Kaiser Permanente's
   Advance Alert Monitor deterioration-warning deployment (Escobar et al., *NEJM* 2020).
   It was a prediction protocol evaluated on mortality, not on alert metrics. If it
   holds up on reading, it fits the record's own `challenge` trigger and should be
   assessed against it. Citation is from memory, so it needs retrieval before use (M-003
   rule: read the source).

**Recommendation:** HOLD at exploration. Rewrite the falsification condition (1), add the
open question (2), and queue the Escobar paper for a deep read. Do not promote it on
citation volume.

## 2. L-022 vs L-023 — duplicates?

**No. They are distinct; the overlap is elsewhere.**

- **L-022 (Oracle Fitness Decoupling)** is about the *evaluator*: a computable oracle
  loses calibration as the outputs it scores become oracle-optimised. Its dependent
  variable is the proxy's fidelity. That makes it Goodhart-family.
- **L-023 (Informality as Novelty Sink)** is about *variance*: diversity is kept alive by
  uncomputable informal steering and collapses when that steering is formalised. Its
  dependent variable is the spread of outputs, and it says nothing about proxy fidelity.
  Its real neighbour is L-003 (Formalization Ratchet), not Goodhart. It also overlaps
  with the mode-collapse literature, which it should cite.

Both came from adjacent seeds in the same sweep (seed-473, seed-474), which explains
why they look alike. Shared vocabulary ("legible optimization") is not a shared claim.

**The real Goodhart-family question:** once `related:` was filled (§3), six laws turned
out to define themselves against L-004: **L-008, L-011, L-012, L-016, L-019, L-022**. That
cluster needs one comparative pass, asking which of them names a mechanism L-004 lacks:

| Law | Its claimed difference from L-004 |
|---|---|
| L-008 | boundary clustering under computable enforcement |
| L-012 | causal-chain position, independent of intensity |
| L-022 | calibration *decay* of the oracle under iteration (dynamic) |
| L-011 | no proxy substitution at all; semantic grounding decays while requirements stay met |
| L-016 | the algorithm's own training loop absorbs the intervention, not the participants |
| L-019 | an aggregation impossibility that holds with *no* optimization pressure |

On their own descriptions, L-019 is not Goodhart-family at all: it cites L-004 only to
say it is unlike it. L-011 and L-016 name distinct carriers. The live overlap is the
triangle **L-008 / L-012 / L-022**. All three are proxy-displacement claims, and they
differ only in what drives the displacement: boundary geometry, position in the causal
chain, or iteration.

**Recommendation:** keep L-022 and L-023 separate. Before any of L-008, L-012 or L-022 is
promoted, run one comparative pass on that triangle (an Opus `assess` or a session). The
risk is three records for one law.

## 3. Applied this session: `related:` backfill

Induction never wrote `related:` (neither `prompts/induct.md` nor `agent/induct.py` asks
for it), so all 16 induction-created laws with prose cross-references had `related: []`.
`laws.fill_related()` now derives the field from ids the record's own prose names, and
induct calls it on every new law. Backfill: 22 links across 16 laws, each with an
`edited` history entry. Additive only. `open_questions:` and `counterexamples:` are
empty for the same reason on 13 laws. That is a prompt change, not a mechanical one,
so it is left for the operator.

## 4. L-006 automation crux — the named papers were already read

The 2026-09-22 HOLD said to "retrieve and deep-read" arxiv 2402.08128, 2512.07526 and
2602.22041. All three were **already in `bibliography/deep-reads/`, with full deep-read
notes on file** (2,300–3,800 words each, whole documents). The assessor asked for work
that was already done and did not know it.

Those notes don't touch the crux. None of them mentions coordination cost, transaction
cost, or whether machine execution counts as coordination. The closest is 2402.08128
(Kovařík, Oesterheld, Conitzer), where simulating the other player is the coordination
device, so the *cost of simulation* may be the relevant quantity. That calls for a
targeted re-read of the PDF with this one question, not a fresh deep read. The other two
are about strategic preemption and responsibility attribution, and look off-target.

**Proposed next step:** (a) a targeted re-read of 2402.08128, then (b) choose sources
that actually address the crux: transaction-cost economics on automated vs. human
coordination (Williamson lineage), and before/after studies of automating a protocol
function. Then re-assess.

**Process bug behind it:** `assess` gaps can name sources without checking
`bibliography.yaml` `read_depth`. A gap that says "deep-read X" should be checked against
the bibliography before it's written. Logged in TODO.
