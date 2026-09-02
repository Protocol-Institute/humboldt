# Same Game, Different Story: A Minimal Conservative Strategic Robustness Benchmark for Large Language Model Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.19670
**Date read:** 2026-09-02
**Connected to:** L-004, L-011
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing "strategic robustness" as invariance of LLM agent action distributions under payoff-preserving narrative reframings in multi-agent settings. The work tests whether language-mediated agents maintain consistent strategies when the same game payoff is presented through different story contexts, using secondary analysis of published cooperation rates.

## What I took from it

The paper documents a real fragility in LLM agents operating under protocol-like constraints: narrative framing induces systematic action variance even when the underlying incentive structure is mathematically identical. This is a valuable *empirical observation* about a specific failure mode in formal reasoning under legibility — the agent's behavior becomes coupled to the surface syntax of the game description rather than its logical structure.

However, the work does not sustain a theoretical argument about *why* this happens, nor does it propose a mechanism that generalizes beyond LLM agent behavior. It also does not challenge or extend any of the current laws under accumulation. The observation sits near L-004 (Goodhart Generalization) and L-011 (Causal Detachment) but does not deepen either. The framing sensitivity is domain-specific to language models' susceptibility to narrative context, not a statement about protocol systems in general.

## Research connections

- **L-004:** The benchmark identifies narrative proxy capture — agents optimize for textual framing rather than the underlying game structure — but this is a special case of LLM behavior, not a generalization to all proxy-dependent protocols.
- **L-011:** Connects tangentially: causal detachment from decision structure is observed (agents decouple from logical equivalence), but the mechanism here is linguistic, not architectural misalignment as L-011 posits.
- **seed-072:** Explanation-Marker Decoupling Under Scaled Legibility — the paper shows agents respond to narrative markers independently of the actual decision logic they ostensibly support.

## Seed

**Seed title:** Narrative-Structure Decoupling in Legible Multi-Agent Protocols

**Seed type:** observation

**Seed text:** In protocol systems where agent decisions are mediated through natural language descriptions of incentive structures, action variance emerges even under payoff isomorphism — agents condition on narrative framing independent of formal equivalence. This suggests that in any protocol relying on linguistic or symbolic legibility to communicate formal constraints, the surface representation becomes an autonomous optimization target separate from the constraint it encodes. The generalization: wherever protocol obligations are rendered legible through a representational layer (natural language, formal syntax, symbolic notation), that layer itself becomes a site of causal detachment, and agents optimize the representation rather than the underlying structure.
