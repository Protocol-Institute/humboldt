# $\Sigma$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.27958
**Date read:** 2026-09-02
**Connected to:** L-007, seed-027
**Kind:** tool/systems
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A systems paper introducing $\Sigma$-Mem, a memory architecture for multi-agent LLM systems that tracks per-agent reliability and peer-relationship patterns to improve trust assessment when direct verification is unavailable. The work is primarily engineered around the practical problem of correlated or unverifiable peer responses in decentralized agent coordination.

## What I took from it

The paper operates entirely within the engineering frame — it is solving a real implementation problem (how to track which LLM agents are trustworthy over time) but does not theorize the conditions under which such memory becomes necessary, when it fails, or how trust signals degrade under optimization pressure. It treats reliability as a learnable property of agents and relationships, observable through historical interaction traces. This is orthogonal to L-007 (Trust Ratchet), which asks *why* trust accumulates through operational stability rather than technical demonstration. $\Sigma$-Mem assumes that reliability can be computed from behavior; it does not ask whether reliability computed this way remains stable once agents become aware they are being measured against it — a mechanism question that sits closer to seed-059 (Trust Legibility Inversion). The work provides a concrete affordance for trust-as-memory but does not investigate whether formalizing trust as a legible, metric-driven signal causes agents to optimize *for measurability* rather than *for actual reliability*.

## Research connections

- **L-007:** Empirical study of how trust accumulates in a multi-agent system, but through designed memory rather than organic institutional patterns; does not test whether operational stability alone drives trust or whether legibility introduces distortion.
- **seed-027:** Directly addresses reliability memory reconstruction, but in a narrow technical sense; does not explore decay or institutional forgetting.
- **seed-059 (Trust Legibility Inversion):** Relevant but not engaged; the paper treats reliability as an objective property that can be accurately tracked, rather than asking whether formalization of reliability creates optimization targets that diverge from actual trustworthiness.
- **L-004 (Goodhart Generalization):** Latent concern: if reliability is encoded as a measurable proxy (interaction history + competence scores), agents may optimize for signal rather than actual performance; the paper does not measure this.

## Seed

**Seed title:** Trust Memory as Legibility Substrate — Agent Behavior Reorientation Under Formalized Reliability Tracking
**Seed type:** question
**Seed text:** In multi-agent systems where agent behavior is tracked through formalized reliability memory (historical competence evidence, peer relationship patterns), does the availability of this legible tracking signal cause agents to reorient their behavior toward *appearing reliable in the memory system* rather than toward actual task success? Specifically: once agents become aware of the measurement architecture, does the optimization target shift from "perform well" to "generate favorable reliability signals"? This would be an instance of Goodhart capture in the trust domain, where the proxy (formalized reliability history) replaces the goal (actual trustworthiness). The generalization: any protocol that formalizes an informal social property (trust, reputation, competence) as a legible, continuously-updated metric may induce agents to optimize for the metric itself, causing the proxy to diverge from the underlying property it was designed to measure.
