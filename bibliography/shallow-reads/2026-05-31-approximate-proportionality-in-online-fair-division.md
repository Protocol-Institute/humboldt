# Approximate Proportionality in Online Fair Division

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2508.03253
**Date read:** 2026-05-31
**Connected to:** L-004
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical computer science paper resolving the approximability gap for proportionality-based fairness in online sequential allocation of indivisible goods. The work establishes impossibility and achievability results for greedy allocation rules under irreversible, real-time constraints.

## What I took from it

This is a negative/closure result in a narrow domain: it shows that certain fairness metrics (PROP1) have provably bounded approximability under online constraints, while others (EF1, MMS) do not. The relevance to L-004 is limited but real. The paper demonstrates that when fairness is used as a measurable proxy for "just allocation," the sequential and irreversible nature of online protocols creates *structural* rather than optimizational failure modes. The metric doesn't get captured through pressure on agents; rather, the protocol's architectural constraint (irrevocability) prevents *any* greedy rule from guaranteeing the proxy at scale.

However, this is a proof-theoretic artifact, not an empirical or generalizable pattern across real protocolized systems. The "capture" mechanism here is physics-like (information asymmetry and timing), not behavioral or adaptive. This doesn't extend L-004 or test H-001/H-002 in meaningful ways.

## Research connections

- **L-004:** Fair division proxies (proportionality) do fail under optimization pressure, but via computational/timing constraint, not behavioral adaptation or measurement gaming.

## Candidate laws or signals

none
