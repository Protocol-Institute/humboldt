# The Consistency Dilemma in LLMs: Generator-Evaluator Agreement and Vulnerability to Mistakes

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.30653
**Date read:** 2026-09-01
**Connected to:** L-011, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical measurement paper documenting inconsistency between LLM generation and evaluation phases across 10 frontier models and 491 concepts. The work directly tests whether models apply concepts uniformly when generating outputs versus evaluating them — a foundational assumption in agentic self-verification pipelines.

## What I took from it

The paper identifies a structural vulnerability in protocols that delegate both generation and evaluation to the same autonomous system without external arbitration. The inconsistency finding maps cleanly onto L-011 (causal detachment in autoregressive systems) and L-013 (paradigm-locked anomaly tolerance), but the mechanism here is more constrained than those laws require: the problem is not that the system achieves a stable but causally unmoored equilibrium, nor that it tolerates evidence of malfunction. Rather, it is that the same system in two operational modes (generation vs. evaluation) applies concepts differently — a form of phase-dependent incoherence.

The work is empirically competent but does not theorize *why* this inconsistency persists, nor does it explore whether it generalizes beyond LLMs to other dual-mode protocols (e.g., approval voting where the same agent both proposes and evaluates alternatives, or verification systems that both compute and audit proofs). The seed-level insight is present but underdeveloped: the paper documents a symptom of a possible broader phenomenon about inconsistency under role switching in autoregressive or iterative systems.

## Research connections

- **L-011:** Demonstrates one mechanism of causal detachment — the generation and evaluation functions are operationally decoupled (different prompts, different contexts, different sampling states), yet the system is deployed as if they are unified. A stable but internally incoherent equilibrium.
- **L-013:** Relates to paradigm-locked tolerance — these inconsistencies are likely known to model developers and systems designers, yet agentic pipelines relying on self-evaluation continue to proliferate without architectural remediation.
- **seed-049 (consensus-reasoning-decoupling):** The generator and evaluator operate on different reasoning substrates or trajectory states, suggesting a deeper pattern about mode-switching in unified systems.

## Seed

**Seed title:** Role-Switching Consistency Decay

**Seed type:** observation

**Seed text:** In autoregressive or iterative systems where the same computational substrate must perform both generation and evaluation across multiple phases, the application of abstract concepts (rules, criteria, interpretations) drifts between phases even when the concepts are semantically identical. This drift is not a bug in a single execution but a structural property of phase-dependent state: the system's internal representations, context windows, and sampling behavior differ between generation and evaluation modes. The phenomenon may generalize to any protocol where the same agent must play multiple roles sequentially without external ground truth — voting systems, approval mechanisms, self-auditing governance — suggesting a law about role incoherence in iterative protocols under unified control.
