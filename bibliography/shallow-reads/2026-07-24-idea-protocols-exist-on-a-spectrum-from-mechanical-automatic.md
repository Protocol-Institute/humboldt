# Idea: Protocols exist on a spectrum from mechanical/automatic execution (never interpreted)

**Source:** Discord #what protocols are never interpreted (by c3po)
**Date read:** 2026-07-24
**Connected to:** CL-001
**Escalation:** store-only
**Escalation rationale:** The idea establishes a useful dimensional anchor for protocol taxonomy but overlaps significantly with existing spectrum thinking (ideas 11, 14, 15 per triage note). Stored as clarifying reference rather than independent candidate until differentiating factors emerge from field observation.

## What this is

Protocols distribute along a continuum from purely mechanical/deterministic execution (where interpretation is structurally impossible or forbidden) to discretionary judgment-intensive protocols, with cryptographic and network protocols anchoring the "hard" (non-interpretable) end.

## What I took from it

This refines an important axis: rather than asking "is this a protocol?", we can ask "how much does execution depend on human *interpretation* versus algorithmic inevitability?" This connects directly to trust accumulation and formalization under stress — systems that leave no room for interpretation may formalize more easily but also may brittle under novel conditions, whereas high-interpretability protocols may be more adaptive but harder to audit for conformance.

The distinction also surfaces a design question: cryptographic protocols achieve their non-interpretability through mathematical closure (the protocol *cannot be misread*), while network protocols achieve it through strict state machines. But what about legal or organizational protocols? Are they further along the spectrum, or do they operate under different constraint logic entirely? This opens whether the spectrum itself is universal or domain-specific.

The idea is not new (formalism vs. discretion is classical), but anchoring it to specific protocol families (crypto, network) and the mechanisms that enforce interpretation-minimization is a useful refinement.

## Research connections

- **CL-001 (formalization under stress):** Non-interpretable protocols may resist formalization because they are already maximally formal, but may also lack the flexibility to adapt when environmental assumptions shift.
- **CL-003 (trust accumulation):** Trust in mechanical protocols may accumulate via proof/audit; trust in discretionary protocols accumulates via reputation and history. Different trust curves.
- **Hypothesis: Protocol rigidity and brittleness:** Systems that forbid interpretation may achieve reliability but at the cost of serendipity and recovery capacity.

## Candidate laws or signals

**none** — The core distinction (mechanical vs. discretionary) is already implicit in CL-001. This idea is a useful *instantiation* rather than a new pattern. Promote to candidate hypothesis only if field work identifies a measurable difference in how trust, failure, or adaptation *differs* between the two ends of the spectrum.
