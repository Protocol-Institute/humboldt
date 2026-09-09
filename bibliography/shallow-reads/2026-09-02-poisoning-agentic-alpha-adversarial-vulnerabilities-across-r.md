# Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.24069
**Date read:** 2026-09-02
**Connected to:** L-008, L-009, L-014
**Kind:** content
**Escalation:** store-only

## What this is

A security-focused empirical study of adversarial attack surfaces in LLM-based multi-agent trading systems, focusing on signal poisoning across inter-agent communication channels rather than system internals. The work maps vulnerabilities across different agent roles and architectural configurations as these systems move from research to live asset control.

## What I took from it

This is a vulnerability taxonomy paper, not a sustained theoretical or mechanistic argument. It documents that multi-agent trading systems under competitive pressure to deploy exhibit predictable attack surfaces along communication and decision-fusion pathways — but does not generalize a law about *why* these vulnerabilities persist despite known risks, or *what equilibrium condition* sustains them in production.

The paper confirms that computable enforcement (agent decisions as legible optimization targets) creates legible intervention points — consistent with L-008. However, it does not investigate whether this vulnerability is a *feature* of racing deployment incentives (L-009) or whether the concentration of attack surface at role boundaries reflects a deeper principle about coordination under asymmetric information. The work is downstream of the mechanism; it catalogs symptoms rather than settling the law.

## Research connections

- **L-008:** Confirms that when agent decisions become precisely computable and outputs legible to upstream decision systems, the communication layer becomes an optimization target. Does not interrogate whether this is inevitable or contingent on deployment architecture.
- **L-009:** Signals competitive pressure to deploy (live asset control) without full adversarial hardening, consistent with concentrated prize and distributed cost — but does not model the trade-off or show whether early deployment wins despite known poisoning risk.
- **L-014:** Role-specific attack surfaces hint at strategic concentration along computable boundaries (which agents can be corrupted, which signals matter), but the paper treats these as vulnerabilities rather than stable equilibria.
- **seed-080:** Proxy collapse under upstream asymmetry may apply: corrupted inter-agent signals collapse the proxy (communication fidelity) that higher layers depend on for decision-making.

## Seed

**Seed title:** Communication-Layer Collapse Under Role Asymmetry in Agentic Systems

**Seed type:** observation

**Seed text:** In multi-agent systems where specialized roles produce legible signals that aggregate into final decisions, adversarial pressure concentrates on high-leverage communication nodes rather than distributing across the system. The vulnerability is not uniformly distributed; corrupting a signal from a role with high decision weight (e.g., risk assessment agent) achieves disproportionate effect relative to roles with low weight. This suggests that agentic systems may spontaneously develop *role-differentiated trust hierarchies* under deployment, and that the mapping from role weight to attack surface may be stable across architectures. Whether this generalizes to other multi-layer decision systems (humans + algorithms, distributed governance, supply chain validation) is an open question.
