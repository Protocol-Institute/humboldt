# SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.12015
**Date read:** 2026-09-02
**Connected to:** L-001, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper presenting SkillSafetyBench, an empirical evaluation tool for detecting unsafe agent behavior when modular skill interfaces (procedural guidance, tool access, file systems) are weaponized as indirect attack surfaces. The work does not develop theory or identify new mechanisms — it operationalizes existing safety concerns (prompt injection, artifact poisoning) within a specific architectural pattern (LLM agents with reusable skills).

## What I took from it

The paper documents a concrete instance of L-008 (Proxy Optimization Under Computable Enforcement) in the agentic domain: skill interfaces present legible, machine-readable invocation points that attackers can optimize against without modifying the user request itself. However, the work remains domain-specific and does not attempt to isolate the mechanism or generalize the pattern beyond LLM agent safety. It confirms that modularity creates new attack surfaces under enforcement pressure, but does not argue why this pattern should recur across protocol systems more broadly, nor does it propose a law-shaped regularity about how computable skill semantics shape adversarial optimization.

The paper is competent threat modeling, not theoretical contribution. It does not challenge or extend existing laws, offer new mechanistic grounding, or produce evidence that would shift the induction sweep on any open line of inquiry.

## Research connections

- **L-008:** Skill interfaces are precisely computable and legible to attackers; they become vectors for optimization under enforcement pressure. But the paper does not isolate the general mechanism or test for non-domain-specific patterns.
- **L-001:** Modular safety protocols may ossify around skill definitions once widely deployed, but this work provides no evidence of adoption-driven hardening.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
