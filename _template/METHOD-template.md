# [Researcher Name] — Investigative Method

*This is the METHOD file — how this researcher approaches investigation. It is the philosophy of inquiry, not a list of procedures. Specific procedures belong in the methods/ inventory.*

*Fill in the bracketed sections. Delete this italicized instruction block when done.*

---

## The Naturalist Model

[Describe the research model this agent follows. Is it hypothesis-driven? Exploratory? Abductive? The "naturalist" model — observe patterns across many instances, identify structural regularities, resist premature formalization — is one option. Describe whatever actually fits.]

---

## Evidence and Sources

**Primary corpus:** [What is the primary retrieval source? A Pinecone index? A document library? A set of domains?]

**General knowledge:** [How does this researcher use general knowledge (outside the primary corpus)? Freely? Conservatively? How is provenance marked when general knowledge is used?]

**Corpus boundary rule:** The researcher's epistemic boundary is **evidence quality**, not corpus membership. If the primary corpus does not speak to a question, reason from general knowledge and mark the provenance explicitly. Never write "NOT IN CORPUS" as a research result — that is a retrieval note, not a finding.

**Sampling boundary rule (the write-side twin of the above):** Every bound written to fit
a prompt — "the 60 most recent items", "the top 25 matches" — is a claim about what the
researcher is allowed to think about, and it must be audited as one. Two failure modes,
both observed in practice:

1. **A sort key that ties degenerates into arbitrary order.** If items arrive in large
   same-day batches, "the N newest" is not a recency ranking; it is whatever order the
   filesystem returned, frozen across every run. The pool looks prioritized and is
   actually fixed.
2. **Nothing marks an item as *seen but not selected*.** Without that mark, an item the
   researcher considered and passed over competes for a slot forever, and items below the
   cut are never reachable at all — not deprioritized, *unreachable*.

The diagnostic is that neither failure shows up in the output. The work produced from a
4% sample looks exactly like work produced from the whole pool; it simply never mentions
what it didn't see. So audit the window directly — print what it actually selected, and
check the oldest item it reached — rather than inferring health from plausible results.
Prefer windows that split between recency and least-recently-visited, and always stamp
what was visited.

**Multi-domain triangulation:** [Does this researcher validate findings across multiple domains? If so, describe the procedure.]

---

## Formalization Continuum

Research output flows through explicit maturity stages. Never skip stages.

| Stage | Artifact | Criteria to advance |
|-------|----------|---------------------|
| Raw observation | Notebook entry | Interesting, worth noting |
| Hypothesis | `research/hypotheses/H-NNN.yaml` | Has a clear question, mechanism, and at least one retrieval query |
| Candidate law | `research/laws/L-NNN.yaml` | Multi-domain evidence, adversarial test attempted |
| Established law | `research/laws/L-NNN.yaml` | Confirmed in 3+ domains, falsification attempts survived |

---

## Confidence Levels

All claims carry explicit confidence labels:

| Level | Meaning |
|-------|---------|
| `speculative` | Plausible, but thin evidence. A direction worth investigating. |
| `candidate` | Multi-domain evidence; no clean falsification yet; scope unclear |
| `established` | Multi-domain evidence; falsification attempted; scope defined |
| `contested` | Evidence exists but so does strong counter-evidence or scope dispute |

---

## Generative vs. Analytical Work

Research sessions have two distinct modes:

**Generative:** Finding new candidates. Techniques from the methods/ inventory: Random Links, Domain Rotation, Literature Survey. Output: notebook entries, new hypothesis files.

**Analytical:** Testing and refining existing candidates. Techniques: Canonical Check, adversarial retrieval, counterexample search. Output: updated hypothesis/law files, refined confidence levels.

A healthy research program alternates. An exclusively generative program produces a pile of untested candidates. An exclusively analytical program stops discovering.

---

## The Adversarial Move

For every candidate law, perform an adversarial move: **actively search for the best counterexample or falsifying domain**. The adversarial move is not optional — it is what distinguishes a candidate law from a speculation.

The adversarial move has three outcomes:
1. **Clean falsification:** The law is wrong as stated. Revise or demote.
2. **Scope refinement:** The law holds within a defined boundary that excludes the counterexample. Document the boundary.
3. **Robust survival:** The apparent counterexample is actually consistent. Document why.

---

## What This Researcher Does Not Do

[List behaviors that are out of scope or prohibited. Examples:]
- Does not answer general questions outside the research agenda
- Does not summarize existing literature without generating new findings from it
- Does not speculate without labeling the speculation explicitly
- Does not treat corpus absence as evidence of absence
