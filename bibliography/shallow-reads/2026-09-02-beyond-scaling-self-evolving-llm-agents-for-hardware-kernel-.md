# Beyond Scaling: Self-Evolving LLM Agents for Hardware Kernel Optimization via an Experience-Driven Workflow and Experience Graph Memory

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.25570
**Date read:** 2026-09-02
**Connected to:** L-005, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A systems paper describing an LLM-agent architecture for iterative hardware kernel optimization, where agents retain and reuse "experience graphs" — structured records of past optimization decisions, their execution outcomes, and downstream revisions — to avoid redundant search. The work is primarily a tool/architecture contribution demonstrating that memory-augmented agents outperform stateless scaling on a specific domain task.

## What I took from it

The paper confirms the practical intuition behind L-005 (working systems resist restructuring): even when an agent has capacity to rewrite kernel code from scratch, it preferentially learns and reuses local modifications to prior working configurations rather than wholesale replacement. The experience graph is a formalization that *retains the prior system as the base* — suggesting that in agentic optimization systems, path-dependence is not just an artifact of human reluctance but emerges from the computational economics of verification and testing.

However, the work does not theorize this regularity or test it across domains. It also does not probe L-012 (intervention-layer displacement): the experience graph is itself a new legible optimization surface — the agent learns to *select* from past decisions rather than to modify the kernel directly. This is a layer shift, not examined. The paper remains local to hardware optimization and does not generalize the mechanism.

## Research connections

- **L-005:** Confirms that self-modifying agents prefer incremental revision over restructuring; suggests verification cost (testing/profiling) creates a functional lock favoring prior configurations.
- **L-012:** Introduces experience graph as intermediate optimization target; agent learns to select/reweight prior decisions rather than generate new code — a potential instance of intervention-layer displacement, but not theorized.
- **seed-063:** Experience graph as latent-state coupling — the formalized history becomes a silent protocol constraint on future decisions; agent cannot escape prior category structure without full retraining.

## Seed

**Seed title:** Experience Graph as Irreversible Coordination Lock

**Seed type:** observation

**Seed text:** In self-evolving agentic systems that formalize and retain execution history (via experience graphs, audit logs, or learned priors), the agent becomes progressively unable to discover solutions that violate the categorical or causal assumptions embedded in prior records, even when such violations would improve global outcome. The formalization of "what worked" becomes a constraint on "what can be tried." This is distinct from Gall's resistance to restructuring: it is active optimization *toward* the shape of the past, mediated through legibility.
