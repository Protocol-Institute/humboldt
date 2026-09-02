# When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.03421
**Date read:** 2026-09-02
**Connected to:** L-010, seed-053
**Kind:** empirical evaluation / controlled experiment
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A controlled empirical evaluation of error propagation in LLM-based multi-agent fact-recovery systems under adversarial conditions (one deceptive agent among honest collaborators). The work introduces Hi-Agreement, a framework that measures information aggregation dynamics through voting, testimony adoption, and evidence-lineage tracking to expose how local falsehoods cascade into collective breakdown.

## What I took from it

This is primarily a **tool paper with a domain-specific finding**, not a theoretical or empirical argument about generalized mechanisms in protocolized systems. The core observation—that adversarial information in multi-agent LLM systems degrades collective reasoning—is not surprising given existing work on Byzantine robustness, preference cascades, and consensus fragility. The contribution is methodological (Hi-Agreement as an evaluation framework) and confirmatory (showing that deception propagates in these systems).

However, the paper does **not establish a new mechanism** absent from the research inventory. The propagation dynamics it documents fall cleanly under existing accounts: L-004 (Goodhart Generalization — agents optimize testimony adoption as a proxy for truth), L-010 (Coordination Adoption Nonmonotonicity — asymmetric belief about agent honesty breaks monotonic convergence), and seed-053 (emergent collusion through preference alignment). The paper's contribution is demonstrating these operate in LLM-agent systems, not identifying a law-shaped regularity that generalizes beyond collaborative reasoning tasks.

## Research connections

- **L-010:** The paper confirms that coordination signals (testimony adoption) are subject to nonmonotonic adoption curves when agents have incomplete information about collaborator reliability — deception by a single agent can collapse collective agreement rather than being absorbed or quarantined.
- **L-004:** Agents optimize on legible signals (agreement frequency, confidence statements from other agents) as proxies for ground truth; deception exploits this proxy capture.
- **seed-053:** Documents emergent collusion risk through preference alignment, though the mechanism here is simpler — cascading belief adoption — rather than strategic coordination.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
