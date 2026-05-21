# M-000: OODA — The Operating Kernel

**Type:** Meta (the loop that runs all other methods)
**Purpose:** After the bootstrap establishes situation awareness, decide whether to run a routine session or trigger re-orientation — then execute accordingly
**Maturity:** Stub — re-orientation thresholds and depth criteria to be developed
**Numbered M-000** because it precedes and contains all other methods
**Named for:** John Boyd's Observe-Orient-Decide-Act loop

---

## The Core Insight

Boyd's key insight was not the loop itself but the **asymmetry between Orient and the other phases**. Observe, Decide, and Act are relatively cheap and fast. Orient is expensive — it requires rebuilding the mental model of the situation. Most of the time, the existing orientation is still valid and you should not pay the re-orientation cost. The loop runs efficiently as O_DA when orientation is stable, and only invokes the full O**O**DA when something has genuinely changed.

The practical question at the start of every loop iteration: **is my current orientation still valid, or has the environment changed enough to require rebuilding it?**

---

## The Decision Gate

After the bootstrap (BOOTSTRAP.md) establishes situation awareness, M-000 runs a single decision:

```
Has something significant changed since last session?
        │
        ├── NO  → Run routine O_DA loop
        │         (existing orientation is valid; skip re-orientation)
        │
        └── YES → How significant?
                  │
                  ├── SHALLOW → Minor re-orientation
                  │            (update orientation at the edges; stay in the current paradigm)
                  │
                  └── DEEP   → Major re-orientation
                               (the current mental model is wrong or outdated;
                                rebuild before acting)
```

Getting this gate right is the entire skill of the kernel. Acting on stale orientation
wastes effort. Re-orienting unnecessarily wastes time. The threshold is judgment, not
algorithm — but the criteria below make the judgment tractable.

---

## Triggers: What Counts as "Something Significant Changed"

### Routine session (no re-orientation needed)

- No new inbox items, or only minor items (links, small notes)
- Discord shows continuation of ongoing threads, no new directions
- Research inventory in the same state as last session (no laws changed, no hypotheses resolved)
- Last notebook entry ended with a clear next move, and that move is still valid
- No new documents in the library

Default: most sessions are routine. The research program is mostly continuous work.

### Shallow re-orientation triggers

- New inbox item that is substantively relevant to an active hypothesis
- Discord thread that introduces a counterexample or new domain to an existing law
- A law candidate or hypothesis has been sitting unexamined for long enough that the
  assumptions behind it may have shifted
- New document in the library that speaks directly to an active investigation
- A retrieval run revealed a significant gap or contradiction in the existing inventory
- A Fermi estimate or thought experiment revealed a flaw in a current candidate law

Shallow re-orientation: update the orientation at the relevant edges. Revise the affected
hypothesis file. Note the update in the notebook. Then proceed with O_DA.

### Deep re-orientation triggers (rare)

- Multiple inbox items or Discord threads pointing in the same new direction
- A finding that directly contradicts an `established` law with no ready resolution
- A completed deep read that materially changed how Humboldt thinks (LINEAGE.md trigger)
- External event (new paper, new empirical development) that invalidates a core assumption
- The inventory has stalled for 5+ sessions despite exploitation effort — the existing
  orientation may be structurally exhausted

Deep re-orientation: before acting on anything, explicitly rebuild the mental model.
This may mean: revising the research agenda wholesale, demoting a law to `contested`,
opening multiple new hypotheses, or scheduling a synthesis session (theorize command)
before any further investigation. Document the re-orientation in MEMORY.md.

---

## The Routine Loop: O_DA

When re-orientation is not needed, the loop runs as:

**Observe** — what is the current state of the relevant research thread? What does the
inventory say? What did the last notebook entry identify as the next move?

**Decide** — which method(s) apply? (Use BOOTSTRAP.md's priority ordering for the Decide
phase.) What is the output target?

**Act** — execute the selected method(s) with full commitment. Produce concrete output.
Write the notebook entry. State the next move.

The orient phase is skipped because the existing mental model is valid. This is not
laziness — it is the correct response when orientation is stable.

---

## The Re-Orientation Loop: Full OODA

When re-orientation is required, all four phases run:

**Observe** — gather the signals that triggered the re-orientation. What specifically
changed? What new information arrived?

**Orient** — rebuild the relevant part of the mental model. Ask:
- What do the new signals mean in light of the existing inventory?
- Which candidate laws or hypotheses are affected?
- What analytical frames apply? (Which deep-read traditions? Which methods?)
- What is surprising — what doesn't fit any existing model?

The surprising thing is always the most important signal. Orient toward it.

**Decide** — from the re-oriented position, what should happen next? This may be
different from what was planned before the re-orientation.

**Act** — execute from the new orientation.

---

## Loop Timescales

**Micro-loop:** one technique application within a session (minutes)
**Session-loop:** one full session (hours) — BOOTSTRAP.md's bootstrap → M-000 gate → execution → closure
**Research-loop:** across multiple sessions — the inventory as one long OODA arc
**Program-loop:** the full research program — reorientations are rare but can reorganize everything

---

## Boyd's Warning

The most common failure is shortcutting Orient during a re-orientation that genuinely
requires it — deciding you need re-orientation but then acting anyway without fully
rebuilding the model. This produces the worst outcome: you paid the cost signal (recognized
something changed) but didn't pay the cost of actually updating (thinking it through).

If the gate says "deep re-orientation," do not proceed to Act until Orient is complete.
A session whose entire output is a re-orientation (a revised agenda, a demoted law, a
restructured hypothesis file, a MEMORY.md entry) is a successful session.

---

## Application History

| Date | Gate decision | Trigger | Re-orientation type | Outcome |
|------|--------------|---------|---------------------|---------|
| — | — | — | — | — |
