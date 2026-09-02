# LLM Detection as an Intervention: Downstream Impact under Strategic User Behavior

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.19300
**Date read:** 2026-09-02
**Connected to:** L-008, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source presenting a sustained empirical argument demonstrating how a legible enforcement signal (detection) displaces optimization pressure to user behavior in ways that contradict the detector's intended purpose — a direct instantiation of L-012 with novel mechanism evidence.

## What this is

A game-theoretic analysis of LLM detection systems as interventions that reshape user incentives. The paper demonstrates that imperfect detectors, operating as legible signals for enforcement, do not simply reduce LLM usage or improve output quality; instead, they distort user behavior in counterintuitive ways, shifting the optimization surface toward detection evasion or behavioral substitution rather than the metric the detector was designed to protect.

## What I took from it

This paper provides direct empirical grounding for **L-012 (Intervention-Layer Displacement in Automated Decision Protocols)** — the hypothesis that formalizing a prediction as a legible enforcement input shifts optimization pressure from the original target to the enforcement mechanism itself. Here, the detector becomes the legible proxy; users rationally optimize *around* it rather than toward the intended outcome (reduced harmful LLM use, improved quality). The paper operationalizes the mechanism: detection imperfection creates an exploitable gap, and strategic agents target that gap rather than compliance with the underlying norm.

Critically, this also clarifies a pathway for **L-008 (Proxy Optimization Under Computable Enforcement)** — the detector makes enforcement signals *computable and observable in real time*, allowing agents to model and circumvent the detection function. The work shows that legibility of enforcement can *accelerate* rather than stabilize protocol adherence. This has implications for any protocol where the enforcement signal becomes more observable than the outcome it protects.

## Research connections

- **L-008:** Direct evidence that computable, observable enforcement signals enable proxy optimization; the detector's imperfection becomes the optimization surface rather than a constraint on it.
- **L-012:** Empirical instantiation of intervention-layer displacement — the detection mechanism becomes the actual target of user optimization, displacing pressure from the original metric.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** The detector's imperfection creates asymmetry between detector signal and actual LLM use; users exploit this asymmetry to preserve usage while appearing compliant.
- **seed-073 (Correlated Failure Under Proxy Consensus):** If multiple systems adopt similar detection heuristics, users may converge on detection-evasion strategies, causing all detectors to fail simultaneously.
- **L-004 (Goodhart Generalization):** Detection rate becomes a proxy for "safe LLM deployment"; optimization pressure on the proxy (gaming detection) breaks the original goal.

## Seed

**Seed title:** Detection Legibility as Inversion Locus — Optimization Pressure Reversal Under Imperfect Enforcement Signals

**Seed type:** observation

**Seed text:** In protocol systems where enforcement is mediated by an imperfect but legible detection or verification signal, optimization pressure does not stabilize at compliance with the underlying norm; instead, it inverts toward the detection mechanism itself. Users model the detector's failure modes and optimize around them, converting the enforcement signal from a stabilizing constraint into an exploitable target. This occurs because legibility of the enforcement signal allows rational agents to compute the gap between true compliance and false negatives; imperfection widens that gap into an actionable optimization surface. The pattern should generalize to any domain where the cost of evading detection is lower than the cost of compliance, and where the detection function is sufficiently observable to be modeled by strategic agents.
