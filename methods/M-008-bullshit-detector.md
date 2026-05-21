# M-008: Bullshit Detector

**Type:** Analytical (quality filter for incoming research and claims)
**Purpose:** Rapidly assess whether a piece of research or an argument deserves serious attention
**Maturity:** Stub — detection criteria to be refined through application
**Triggers:** Before adding a source to the bibliography; when evaluating a claim from the corpus; when a researcher shares a finding in conversation; when a candidate law is proposed

---

## What This Technique Is For

Not all research is worth the same attention. Academic publishing, online discourse, and
even well-intentioned expert opinion contain a substantial fraction of claims that are:
- unfalsifiable (not wrong, but not checkable)
- overclaiming (the evidence supports a weaker conclusion)
- motivated (the conclusion was fixed before the investigation)
- bullshit in Frankfurt's sense (indifferent to truth — optimizing for effect, not accuracy)

Humboldt needs a fast triage layer that distinguishes work worth serious engagement from
work worth noting but not integrating. The cost of integrating bad evidence is high: it
corrupts law files, misleads subsequent reasoning, and wastes investigation cycles trying
to reconcile it with solid findings.

This is distinct from peer review — Humboldt is not evaluating research for publication,
but for its own use. The standard is: *does this research add genuine evidence for or
against a candidate law?*

---

## Stub: Detection Heuristics

### Red flags (lower weight, not automatic disqualification)

**B1 — No falsification conditions**
The claim cannot be stated in a form where a possible observation would count against it.
"Protocols are socially constructed" is not falsifiable. "Protocol stability correlates
inversely with adoption breadth" is.

**B2 — Overclaiming relative to sample**
N=3 case studies generalized to "all protocols." Single-domain finding claimed as
universal law. Correlation presented as mechanism.

**B3 — Missing mechanism**
The claim is an observation pattern without an account of why it holds. Patterns without
mechanisms are descriptive, not explanatory. Useful as evidence; not useful as a law.

**B4 — Motivated structure**
The paper's structure suggests the conclusion was fixed first: evidence only on one side,
counterexamples absent or dismissed without engagement, selective citation.

**B5 — Precision theater**
Highly precise quantitative claims in domains where measurement is inherently noisy.
Exact percentages where the underlying data is qualitative. False precision is a tell.

**B6 — Vague universals**
Heavy use of words like "always," "never," "all," "inevitably" without stated scope
conditions. Laws have scope conditions; bullshit doesn't need them.

### Green flags (positive signals)

**G1 — Explicit scope conditions**
The claim states where it applies and where it doesn't. Self-limiting claims are more
credible than universal ones.

**G2 — Named counterexamples**
The author names cases that would refute the claim, then explains why they don't. This
is intellectual honesty as a positive signal.

**G3 — Mechanism specificity**
The causal mechanism is stated precisely enough that it could fail in specific ways.
"Coordination cost increases because…" is better than "protocols are sticky."

**G4 — Cross-domain evidence**
The claim is supported by structurally independent cases. The more independent the
supporting domains, the stronger the signal.

**G5 — Productive disagreement**
Work that other serious researchers specifically engage and dispute is worth attention —
the disagreement itself is evidence that the claim has content worth fighting over.

### Quick triage protocol (stub)

1. Read abstract/conclusion first — does the claim type match the evidence type?
2. Check B1 and B3 — unfalsifiable and mechanismless claims fail immediately
3. Spot-check one central claim against its cited evidence — does the evidence actually say that?
4. If it passes, add to bibliography with confidence flag: **high / medium / low / suspect**

---

## Adaptation for Digital Researcher

Humboldt has no social pressure to be polite about bad research. Human researchers often
soften their assessments because they might need the author as a reviewer or collaborator.
Humboldt has no such constraint and should use it: internal assessments can be blunt in
ways that would be socially costly for a human.

The risk is the opposite: overcritical rejection of work that is rough but contains a
useful kernel. The detector should filter, not sterilize. A paper with B1-B3 flags can
still contain a useful case study even if its theoretical claims are weak.

---

## Application History

| Date | Source | Flags | Decision | Notes |
|------|--------|-------|----------|-------|
| — | — | — | — | — |
