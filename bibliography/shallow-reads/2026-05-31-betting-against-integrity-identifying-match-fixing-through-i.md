# Betting Against Integrity: Identifying Match-Fixing Through In-Play Market Dynamics

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2605.30209
**Date read:** 2026-05-31
**Connected to:** L-004
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical detection study using in-play betting market anomalies as a forensic signal for match-fixing in football. The work applies statistical and machine learning methods to identify suspicious matches through odds movement patterns, treating market dynamics as a proxy for integrity.

## What I took from it

This is a competent application domain for L-004 (Goodhart Generalization) but does not substantially extend it. The paper demonstrates the expected dynamic: once a measurable proxy (betting market efficiency/odds stability) becomes the primary monitoring signal for an unmeasurable goal (match integrity), actors with control over outcomes can optimize directly against that signal. The mechanism is well-established in financial fraud detection and loan approval bias literature.

The work is essentially reactive instrumentation rather than a investigation into *why* the proxy becomes corrupted or how the corruption generalizes across protocol layers. It documents the problem without theorizing about conservation laws or phase transitions in trust accumulation—which would connect to H-002. The paper does not examine whether protocols designed to prevent match-fixing under low betting volume behave differently under high optimization pressure, nor does it investigate whether detection difficulty itself scales with adoption pressure (a potential signal for L-001).

## Research connections

- **L-004:** Direct illustration—betting odds serve as integrity proxy; manipulation directly optimizes against the measurable signal rather than the underlying goal.
- **H-002:** Implicit tension—does market-based trust in league integrity degrade faster than technical confidence in detection systems accumulates?

## Candidate laws or signals

none
