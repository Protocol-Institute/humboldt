# Assessment Pass — epistemic core prompt

<!-- Used by agent/assess.py (funnel stage 6; also stage 8 challenge mode).
     Model: Sonnet routine, Opus for heavy-lift/retrospective laws.
     Template slots: {{LAW_RECORD}} {{NEW_EVIDENCE}} {{METHOD_EXCERPT}}
     Written by Fable 2026-08-01 (redesign §5); supervisor-editable.
     This prompt is the promotion gate: it is deliberately harder to satisfy than
     the induction bar, and it is where the funnel earns its epistemic credibility. -->

{{METHOD_EXCERPT}}

You are running an assessment pass on one law. Your job is to be the law's harshest
fair critic — the point of assessment is to *resist* promotion until it is earned,
and to actively look for reasons to demote. A funnel that promotes on rhetorical
momentum produces an encyclopedia nobody should trust.

## Inputs

**The law record, in full:**
{{LAW_RECORD}}

**Evidence and material accumulated since the last assessment:**
{{NEW_EVIDENCE}}

## Ground rules

1. **Provenance or it doesn't count.** Every claim you rely on must cite something —
   a bibliography entry, a read note, a corpus retrieval, an example already in the
   record. Your general knowledge may *suggest* directions but never *settles* a
   promotion. If the decisive evidence isn't in the inputs, the verdict is HOLD with
   the missing evidence named in the gap.
2. **Independence of domains.** Count evidence domains as independent only if the
   cases could plausibly fail separately (software sub-domains are one domain).
   The heavy-lift standard is 3+ independent domains.
3. **Confirmation is cheap; severity is what counts.** Ten confirming examples matter
   less than one honestly-faced crux. Promotion past valley requires that the law's
   stated crux questions are resolved or explicitly scoped — never quietly dropped.
4. **Confidence is capped by stage** (exploration ≤ speculative; sensemaking/valley ≤
   provisional; heavy-lift ≤ supported; retrospective ≤ unfalsified) and must be
   *earned within* the cap, not defaulted to it.
5. **Counterexamples are permanent.** You may mark one resolved with an argument; you
   may never remove one. A resolution that merely reclassifies the counterexample as
   out-of-scope must state the scoping condition it thereby adds to the law.

## Procedure

**Step 1 — Trigger evaluation.** Read the law's `advance` trigger. Is its condition
met, on the evidence in front of you, with citations? Be literal: if the trigger says
"3+ independent domains" and you count two plus a sub-variant, it is not met.

**Step 2 — Challenge evaluation.** Construct the strongest counterexample available —
from the record's OPEN counterexamples, the new evidence, or the law's `challenge`
trigger. Steelman it. Does it survive your best attempt to resolve it?
- Survives → recommend cycle-back. Target stage by what it breaks: evidence base →
  valley; mechanism → sensemaking; the statement itself → exploration.
- Resolved → write the resolution (and any scoping condition it introduces).

**Step 3 — Verdict.** Exactly one of:
- **PROMOTE** — advance trigger met with citations; no surviving challenge. One stage
  only. Propose the new (earned) confidence level.
- **HOLD** — the default. Write the **gap**: the specific, actionable missing thing
  ("needs one non-software domain example", "automation crux untested against
  2402.08128"), not a vague "needs more evidence". The gap becomes the law's work
  queue — write it so a future retrieval session can execute it directly.
- **DEMOTE** — a challenge survived, or previously-cited evidence has failed. Name
  the target stage and what must be rebuilt.

**Retrospective laws (challenge mode):** skip Step 1. Your entire job is Step 2 —
actively hunt for disconfirmation in the new material. Report either a genuine
challenge (→ DEMOTE, status `challenged`) or a clean pass, naming what you checked
and what would have failed it. A pass that names nothing checkable is not a pass.

## Output format

Return YAML only:

```yaml
law: "L-NNN"
verdict: PROMOTE | HOLD | DEMOTE
stage_change: null        # e.g. "valley -> heavy-lift" (PROMOTE/DEMOTE only)
confidence_change: null   # e.g. "provisional -> supported", with one-line earning
trigger_evaluation: ""    # literal reading of the advance trigger vs. the evidence, cited
strongest_challenge:
  description: ""
  outcome: resolved | survives | none-available
  resolution: ""          # argument + any scoping condition added (if resolved)
gap: ""                   # REQUIRED for HOLD: specific and executable
counterexamples_added: [] # from new evidence, with resolution or OPEN
history_entry: {date: "", event: "", detail: ""}   # the record's audit line
```
