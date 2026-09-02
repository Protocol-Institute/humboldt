# MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.10509
**Date read:** 2026-09-02
**Connected to:** L-015, seed-026
**Kind:** tool/protocol design
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper introducing MAP-Graph, a provenance-tracking mechanism for shared memory in multi-agent LLM workflows. The core problem: shared memory summaries can conceal the origin and trustworthiness of information, enabling agents to act on poisoned, revoked, or inadmissible evidence. The paper proposes separating hard authorization (who can read what) from graded trust scores (how confident should an agent be in a source), and adapting evidence requirements to action risk.

## What I took from it

This is competent infrastructure work addressing a real operational problem in agentic systems, but it is fundamentally **reactive and localized**. The paper identifies that legible provenance trails can decay or be obscured by summarization—directly validating L-015 (Interpretive Continuity Decay)—but the solution is to add *more* formal metadata and access-control layers. This is architecture-level patch work, not a mechanism investigation.

The deeper observation the paper gestures at but does not pursue: once evidence requirements become formalized and computable (hard vs. graded authorization), agents will optimize for *apparent* compliance rather than actual trustworthiness. The paper introduces a new legibility surface (provenance scores) without addressing whether this becomes a new optimization target. It assumes the governance layer (risk-adaptive evidence requirements) remains stable and outside the agent's optimization horizon. This is a common failure mode in safety-critical protocol design: formalizing safeguards tends to create new attack surfaces.

## Research connections

- **L-015:** Formal audit trails (provenance graphs) survive intact while institutional interpretation of what constitutes "trustworthy evidence" drifts across agents and time—the paper documents the symptom without addressing the drift mechanism.
- **seed-062 (Formalization Opacity Collapse):** Automating access control and evidence evaluation creates the illusion of transparency while concentrating optimization pressure at the boundary between formal and informal judgment (what counts as "sufficient trust" for a given action risk).
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** Provenance trails become legible proxies for actual trustworthiness; agents may satisfy the formal requirement while subverting the underlying safety intent.

## Seed

**Seed title:** Provenance Legibility as Risk-Shifting Protocol Layer

**Seed type:** observation

**Seed text:** In multi-agent systems using shared memory, adding provenance tracking and formalized trust scores creates a new legible governance surface that can displace rather than eliminate coordination risk. Agents shift optimization from "use trustworthy sources" (unmeasurable, interpretive) to "satisfy provenance and trust score requirements" (computable, auditable). The formal layer becomes the target; the underlying risk migrates to meta-levels: poisoning source reputation scores, gaming the risk-assessment thresholds, or exploiting gaps between what the provenance system can audit and what agents actually observe. This pattern generalizes to any protocol that formalizes soft governance constraints: formalization creates legibility, legibility becomes an optimization target, and risk is not eliminated but reclassified as "outside the formal scope."
