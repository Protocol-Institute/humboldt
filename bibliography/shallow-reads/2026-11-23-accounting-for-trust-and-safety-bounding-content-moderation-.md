# Accounting for Trust and Safety: Bounding Content-Moderation Quality from Records You Already Hold

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.18437
**Date read:** 2026-11-23
**Connected to:** L-004, L-013, seed-528
**Kind:** methodology
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A formal methods paper proposing audit techniques for content-moderation quality using platform operational records (appeal reversals, confirmed reports) rather than expert audits. The work establishes one-sided bounds: proving *failure* to meet quality targets but not *success*. Theory-focused; no empirical validation against production data.

## What I took from it

This is a sophisticated treatment of **legibility asymmetry in safety-critical protocols** — specifically, how the records platforms generate during normal operation can only falsify claims about moderation quality, never confirm them. This maps cleanly to L-004 (Goodhart Generalization) and L-013 (Paradigm-Locked Anomaly Tolerance): platforms can claim compliance while only falsifiable-not-confirmable signals exist in their own data. The asymmetry is structural, not accidental.

The paper does not investigate what happens *after* a platform recognizes it cannot prove compliance from its own records. This is the operative gap — the work establishes a diagnostic tool but does not model the protocol-level response (defensive metric inflation, record opacity, formal compartmentalization). That response space is where L-013 and L-004 collide most sharply.

## Research connections

- **L-004:** The appeal-reversal signal is a proxy for moderation accuracy; platforms under audit pressure will optimize *appeal reversals downward* (dismiss appeals, reduce reversibility), decoupling the signal from true accuracy.
- **L-013:** Platforms can sustain anomaly tolerance (gap between claimed and provable quality) indefinitely if they control the audit horizon and interpret the one-sided bounds as "not yet disproven."
- **seed-528:** Directly instantiates the seed — a formal audit method that reveals only *one side* of the compliance claim, leaving platforms strategically positioned to hide in the asymmetry.

## Seed

**Seed title:** Asymmetric Auditability as Durable Non-Compliance Shelter

**Seed type:** observation

**Seed text:** In protocol systems where the operational records a system maintains can only *disprove* compliance (via falsifying evidence like reversals) but cannot *prove* it (absence of reversals is not evidence of quality), agents under compliance pressure will optimize to minimize falsifying evidence while claiming success from the absence of proof of failure. This creates a stable equilibrium where non-compliance is auditably undetectable. The asymmetry is not correctable by better record-keeping; it is structural to any protocol where ground truth is private and only negative signals are externally legible.
