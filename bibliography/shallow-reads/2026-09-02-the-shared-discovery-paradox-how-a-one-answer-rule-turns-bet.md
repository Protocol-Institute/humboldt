# The Shared Discovery Paradox: How a One-Answer Rule Turns Better Information into Worse Search

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.18045
**Date read:** 2026-09-02
**Connected to:** L-004, L-010, seed-016
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source establishing a mechanism (pooled information as measurable proxy → coordination collapse) that directly extends L-004 and L-010 into a new domain; introduces a precise counterintuitive regularity (information accuracy vs. coverage inversion under centralized enforcement) absent from current inventory.

## What this is

A game-theoretic benchmark paper (discovery problem with 16 boxes, 1 target, 8 searchers) that models the cost of converting dispersed noisy signals into a single shared recommendation and enforcing all agents to act on it. The central finding: pooling information raises recommendation accuracy (0.20 → 0.3835) but crashes discovery coverage (0.8322 → 0.3835) because all agents now optimize the same target.

## What I took from it

This is a **direct instantiation of the proxy-capture mechanism in a coordination setting**. The paper shows that a measurable proxy (accuracy of the pooled signal) can be optimized *while the unmeasurable goal* (discovery coverage) collapses. The mechanism is precise: improved legibility of the "right" answer removes exploration incentive entirely—agents stop searching alternatives because the shared ranking is now credible enough to trust.

This extends L-004 (Goodhart Generalization) by showing the dynamic under *coordination*. When information pooling creates a single legible target, adoption pressure (L-010 nonmonotonicity) forces convergence, and that convergence is *optimally* destructive to the original objective. The paper shows a portfolio solution works, but crucially: *that requires breaking the one-answer protocol*.

This also directly challenges the implicit assumption in many coordination systems: that better shared information is always better for collective outcomes. It is not. Under enforcement of a single recommendation, better information *guarantees* worse discovery.

## Research connections

- **L-004:** Goodhart Generalization applies directly; pooled accuracy is the proxy, discovery coverage is the unmeasurable goal; metric capture occurs under "adoption pressure" (enforced one-answer rule).
- **L-010:** Coordination Adoption Nonmonotonicity; agents condition on the shared signal, creating a nonmonotonic adoption curve: better accuracy → worse outcomes.
- **seed-016:** Pooled information as measurable proxy for discovery quality—confirmed and mechanistically grounded.
- **L-006:** Coordination Cost Conservation—the paper suggests the cost moves from search effort to information pooling; mechanism worth checking.
- **seed-073:** Correlated Failure Under Proxy Consensus; all agents fail on the same target when the proxy becomes legible.
- **seed-082:** Additive Intervention in Overloaded Protocols; portfolio solution bypasses the one-answer constraint.

## Seed

**Seed title:** Legible Pooling as Coverage Collapse Under Coordination Enforcement

**Seed type:** mechanism

**Seed text:** When dispersed noisy private signals are pooled into a single measurable recommendation and agents are enforced (or incentivized) to act on that shared output, the accuracy of the pooled signal and the diversity of collective action move in inverse proportion. Specifically: as pooling improves the legibility of "the right answer," agents abandon independent exploration and concentrate optimization on the shared target, reducing coverage and discovery. This holds under coordination regimes where a single recommendation is credible and costly to ignore. The mechanism generalizes beyond discovery to any collective search problem where diversity of action is the true objective but measurable accuracy of a shared signal becomes the optimization target.
