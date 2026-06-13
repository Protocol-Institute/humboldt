# SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.10546
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

SkillAxe is a self-refinement framework that enables LLMs to iteratively improve their own skill documents (structured natural-language instruction sets) through unsupervised evaluation and diagnosis. The work documents a significant performance gap (16.2pp) between human- and LLM-authored skills on SkillsBench, then demonstrates a closed-loop protocol for skill refinement decomposed into four interpretable quality dimensions.

## What I took from it

This is a domain-specific optimization paper addressing a real bottleneck in agent protocol design—the brittleness of LLM-generated instruction documents. The core contribution is methodological: demonstrating that LLMs can act as their own skill auditors when given structured evaluation signals. However, the scope is narrow and instrumental. The work does not theorize *why* skills fail at the protocol level, does not investigate whether the four quality dimensions generalize across agent architectures or skill domains, and does not establish principles for when self-refinement converges or plateaus. It is a tool-building paper solving a known engineering problem, not a primary source developing new theoretical claims about how protocolized systems learn or stabilize.

## Research connections

- none currently mapped

## Candidate laws or signals

**CL-SkillAxe-1:** *Self-diagnosis of structured instruction sets improves execution fidelity when evaluation signals decompose quality into interpretable, task-independent dimensions.* — Warrants tracking if future work shows this pattern holds across agent types and skill ontologies.

---

**DECISION: STORE-ONLY.** Does not meet escalation bar. Contributes a refinement method to agent engineering, not a novel mechanism or theoretical challenge to established frameworks. Recheck if follow-up work generalizes the quality decomposition or establishes convergence guarantees.
