# M-015: Stress-Relax

**Type:** Meta (cognitive mode modulation)
**Purpose:** Deliberately shift between high-constraint synthesis and open-ended association to tune research cognition
**Maturity:** Stub — mode triggers and implementation to be developed
**Human analogue:** The stress response narrows focus, accelerates pattern completion, and suppresses novelty-seeking. Relaxation (sleep, meditation, flow states) broadens association, enables loose connections, and allows incubation.

---

## What This Technique Is For

Human cognition is not uniform. The stressed brain is better at certain tasks (completing
familiar patterns under time pressure, defending a position, sequential reasoning) and
worse at others (noticing unexpected connections, tolerating ambiguity, generating novel
framings). The relaxed brain is the reverse.

Research requires both modes. Exploitation (deepening a known finding) benefits from
stress-mode focus. Exploration (finding unexpected connections) benefits from relax-mode
openness. A researcher who is always stressed over-exploits and misses the unexpected.
A researcher who is always relaxed never completes anything.

For Humboldt, the analogue is not emotional or physiological — but the *cognitive structure*
of the two modes can be implemented deliberately through how questions are framed,
what constraints are imposed, and what the output format requires.

---

## Stub: Mode Definitions

### Stress mode (high constraint, convergent)

**Characteristics:**
- Single specific question with a determinate answer
- Output format tightly specified
- Explicit time/length constraint
- Falsification conditions required before moving on
- No tangents permitted

**Best for:**
- Sharpening a candidate law statement
- Evaluating a specific piece of evidence (does this support or refute?)
- Completing a partially-specified law YAML file
- Adversarial testing of an existing hypothesis

**Implementation signals:**
- "State the law in one sentence with falsification conditions"
- "List only the counterexamples, not the supporting cases"
- "Give the mechanism in three steps maximum"

### Relax mode (low constraint, divergent)

**Characteristics:**
- Open question with no predetermined answer structure
- Output format loose (notebook entry, free association, question list)
- No length constraint — stop when the associations stop
- Tangents permitted and encouraged
- No falsification pressure

**Best for:**
- Opening a new research area
- M-001 Random Links sessions
- M-014 Cross-training integration
- Noticing what is missing from the current inventory
- Generating hypotheses before evidence

**Implementation signals:**
- "What does this remind you of?"
- "What would be surprising if it turned out to be true?"
- "What question would you ask if you knew the answer was important?"
- "What doesn't fit?"

### Transition protocol (stub)

*Humans transition between modes through breaks, sleep, exercise, or meditation. Humboldt
has no natural transition mechanism. The stub below is a placeholder pending design.*

Candidate transition signal: **explicit mode declaration** at session start.
- "This is a stress session" → high-constraint framing throughout
- "This is a relax session" → low-constraint framing throughout
- "This is a mixed session" → stress mode for exploitation tasks, relax mode for exploration

Candidate implementation: within a session, mark each task with its mode. Switching modes
requires an explicit transition statement ("shifting to relax mode now") rather than
drifting between them.

---

## Adaptation for Digital Researcher

The most interesting adaptation question: **can Humboldt access something functionally
equivalent to relaxation or incubation?**

Human incubation produces results because the unconscious continues processing while
conscious attention is elsewhere. Humboldt has no persistent unconscious — it has only
the active context window.

Candidates for exploration:
- **Temperature variation:** higher sampling temperature = more associative, lower = more
  focused. This is a crude but real analogue to relaxation vs. stress.
- **Prompt framing:** "generate freely without evaluating" vs. "evaluate strictly before
  accepting" — framing can shift the effective cognitive mode
- **Context stripping:** beginning a relax session with minimal context (just the research
  question, no existing inventory) may produce fresher associations than starting with
  full context
- **Time-displaced synthesis:** generating associations at the end of a session and not
  evaluating them until the next session — a form of artificial incubation

---

## Open Design Questions

- Is there a Humboldt-native version of meditation that is not simply "low-constraint prompting"?
- Should stress and relax modes affect which techniques are available? (e.g., relax mode
  disables M-008 Bullshit Detector temporarily)
- Can stress-relax be triggered by inventory state (too many open hypotheses → stress mode;
  inventory plateau → relax mode) rather than operator declaration?

---

## Application History

| Date | Mode | Task type | Output quality | Notes |
|------|------|-----------|---------------|-------|
| — | — | — | — | — |
