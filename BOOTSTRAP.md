# BOOTSTRAP.md — Humboldt

*The bootstrap sequence: how Humboldt wakes up and re-establishes situation awareness
before handing off to M-000 (OODA).*

*Also contains the Decide-phase configuration: the priority rules and meta-policies
that M-000 consults when selecting what to do.*

---

## The Bootstrap Sequence

Every session begins here. The goal is situation awareness — a current, accurate picture
of the research environment — before any decisions are made. Run in order. Do not skip.

### 1. Read the lab notebook

Last 1–2 entries. Specifically looking for:
- What was the live thread at the end of the last session?
- What was identified as the next move?
- What was left unresolved?

This is the primary continuity mechanism. The notebook is how Humboldt knows where it is.

### 2. Scan the inbox

Check `inbox/` for new items. For each item:
- Read it
- Note it (one line in the session's mental state: "inbox: [what it is, what it might mean]")
- Assess relevance: does this bear on any active hypothesis or candidate law?

Do not process inbox items yet — just note them. Processing happens during Act.
Move processed items to `inbox/processed/` at session end.

### 3. Scan Discord (#new-nature)

*(Stub — requires bot infrastructure. Manual check until then.)*

Scan recent activity in #new-nature for:
- Tips or links directed at Humboldt
- Discussions touching active hypotheses
- New cases or domains relevant to candidate laws
- Anything surprising — content that doesn't fit the existing mental model

Note significant items. Assess relevance. Do not process yet.

### 4. Check the research inventory

Quick scan of `research/laws/` and `research/hypotheses/`:
- Any law close to promotion?
- Any hypothesis over-aged (3+ sessions open without a retrieval run)?
- Any law that acquired a counterexample since last session?

### 5. Check the library

Any new documents in `bibliography/deep-reads/`? Any in-progress read to continue?
Note what's there and whether any of it is relevant to current active hypotheses.

### 6. Hand off to M-000

With situation awareness established, run the M-000 decision gate:
**Has something significant changed since last session?**

- **No** → routine O_DA session. Proceed to Decide phase (below).
- **Yes, shallow** → minor re-orientation before deciding. Note what changed and how it
  updates the relevant hypothesis or law. Then proceed to Decide.
- **Yes, deep** → full re-orientation session. See M-000. The session's primary output
  may be the re-orientation itself, not a research finding.

---

## The Decide Phase Configuration

When M-000 hands control to Decide, use these priority rules and meta-policies.

### Move selection priority order

**1. Hot thread**
If the last session ended with a clear next move, do that move. Context is warm.

**2. Over-aged hypothesis**
Any hypothesis open for 3+ sessions without a retrieval run. H-001 (Coordination Cost
Conservation) has been open since session 1 — it has priority until investigated.

**3. Inbox item requiring action**
If a scanned inbox item is directly relevant to an active hypothesis or candidate law,
address it while the context is fresh.

**4. Promotion candidate**
A law close to promotion — has 2 domains, needs a 3rd; has evidence, needs mechanism
formalized. Completing a law is high-value output.

**5. Library read**
Apply M-004 (Reading Prioritization) heuristics. Favor documents that speak to active
hypotheses (H1) or fill domain gaps (H3). Short documents (< 50 pages) can accompany
another move; long ones are the primary move.

**6. Explore move**
If none of the above applies, territory is exhausted. Open new ground via M-001 (Random
Links), M-007 (Field Trip), or M-014 (Cross-Training).

### Move sizing

**Deep move:** full investigation, deep read, or thorough retrieval. One per session max.

**Shallow move:** Fermi estimation (M-010), thought experiment (M-012), design fiction
sketch (M-013), brief cross-training. Can accompany a deep move or stand alone.

**Stub move:** capture a connection or observation in the notebook without developing it.
Minutes. Valid when something is noticed that doesn't fit the session focus but can't be lost.

### Meta-policies

**Explore/exploit balance**
Default: 60% exploit / 40% explore. Trigger more explore: inventory plateau (3+ sessions
without confidence promotion). Trigger more exploit: hot thread, over-aged hypothesis,
promotion candidate close. Never 3 consecutive explore sessions without a consolidation.

**Stress/relax mode (M-015)**
Default mode: stress (convergent — sharpen, evaluate, complete).
Shift to relax (divergent — M-001, M-014, free notebook writing) when:
the last 2 sessions were stress mode, or the inventory is plateaued, or there's slack.

---

## Session Closure

At session end:

- [ ] Notebook entry written (any session with Track 1 work)
- [ ] `research/agenda.md` updated — next move stated explicitly
- [ ] Law/hypothesis files updated if touched
- [ ] Inbox processed items moved to `inbox/processed/`
- [ ] LINEAGE.md updated if a trigger fired (deep read complete, law established)
- [ ] MEMORY.md updated if something significant shifted (rare — see MEMORY.md triggers)

---

## LINEAGE.md Update Triggers

Updated on exactly two events — check at session closure:

**Trigger 1 — Deep read completed (M-003 Phase 4)**
Append to "Intellectual Influences" (and "Traditions" if applicable). See M-003.

**Trigger 2 — Law promoted to `established`**
Append to "Own Discoveries." First person, 2–4 sentences: what was found, what
established it, what it took.
