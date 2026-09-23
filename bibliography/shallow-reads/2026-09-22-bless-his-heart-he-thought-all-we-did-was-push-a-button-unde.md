# ''Bless his heart... he thought all we did was push a button": Understanding Worker Challenges with U.S. Election Technology

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.19233
**Date read:** 2026-09-22
**Connected to:** L-003, L-015
**Kind:** content
**Escalation:** store-only

## What this is

Qualitative empirical study (interviews + surveys, N=50 election officials across 20 U.S. states) examining how election technology creates operational friction and interpretive challenges for the workers who depend on it. The paper treats worker experience and sensemaking as primary evidence, with design gaps as the focal mechanism.

## What I took from it

This is a situated documentation of **L-015** (Interpretive Continuity Decay in Distributed Governance Protocols) in action. Election officials operate within a formalized, audited protocol system (ballot scanners, voter registration databases, chain-of-custody procedures) that is increasingly automated and legible to external oversight — but this legibility gap produces a sharp discontinuity between what the formal system *appears* to do (push a button → count votes) and what workers *know* the system requires (contextual judgment, error recovery, institutional knowledge, tacit workarounds).

The finding that "misleading narratives stem from errors that occur while using election technology" suggests that as protocols ossify and formalize (L-003: Formalization Ratchet), the informal institutional knowledge needed to *operate correctly* becomes invisible to external auditors, regulators, and public narratives. Workers develop compensatory practices, but these are not legible in the formal protocol record — so when errors occur, the audit trail appears to show protocol failure rather than worker-protocol mismatch. This is **interpretive continuity decay**: the formal record survives intact, but the meaning-making apparatus that kept it functional degrades.

## Research connections

- **L-003:** Stress and public scrutiny on election systems drove formalization of procedures; informal coordination norms (tacit knowledge, contextual judgment) are being replaced by computable, auditable steps — but the work is becoming *harder*, not easier, suggesting the ratchet is capturing necessary complexity rather than reducing it.

- **L-015:** Core example of the pattern: formal records (audit logs, machine counts, chain-of-custody documentation) remain intact and auditable, but the institutional context that made those records *meaningful* to workers (training, precedent, interpretive community) is decaying or becoming invisible to external observers.

- **seed-133:** Metric formalization as paradigm lock — election technology embeds a metric (button push → vote counted) that appears to be a complete description of the work but masks the actual decision-making labor that makes the metric faithful.

- **seed-144:** Informality as coordination cost refuge — workers likely develop informal workarounds and mutual aid structures precisely because the formal protocol does not capture the contingency and judgment the work requires.

## Seed

**Seed title:** Formalization-Legibility Inversion in Safety-Critical Worker Protocols

**Seed type:** observation

**Seed text:** In safety-critical protocol systems where worker judgment is both essential and operationally illegible (election work, medical triage, air traffic control), formalization driven by external auditing pressure does not reduce worker burden or protocol error — it displaces error into the gap between what the formal system claims to do and what workers must actually do to keep it functional. The formal system becomes more legible to regulators and auditors, but *less* legible to workers, because the formalization does not encode the conditions under which the rule applies. This creates a regime where protocol violations accumulate in the informal layer, and failures in the informal layer appear in the formal audit as protocol failures, not as evidence of formalization inadequacy.
