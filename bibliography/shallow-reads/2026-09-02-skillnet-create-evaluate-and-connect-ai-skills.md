# SkillNet: Create, Evaluate, and Connect AI Skills

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2603.04448
**Date read:** 2026-09-02
**Connected to:** L-001, L-005
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper describing an infrastructure (SkillNet) for consolidating, organizing, and transferring learned skills across AI agents through a unified ontology. The work addresses fragmentation in agent capability accumulation—agents repeatedly solving problems independently rather than leveraging prior solutions—by proposing a structured skill marketplace and discovery mechanism.

## What I took from it

The paper is a competent infrastructure contribution but lacks theoretical depth on *why* skill fragmentation persists or *what mechanisms prevent* consolidation. The triage flags L-001 and L-005 (ossification and resistance to restructuring) are superficially relevant—one might expect that successful, widely-adopted skills would become difficult to modify, or that replacing skill subsystems is risky—but the paper does not engage with these dynamics. It treats skill consolidation as a technical coordination problem (ontology design, evaluation metrics, discovery interface) rather than investigating whether protocol or system-level laws resist accumulation. The paper confirms that agents do "reinvent the wheel" but does not ask whether this is a symptom of deeper coordination constraints or whether a unified infrastructure would itself ossify under adoption pressure. No mechanistic investigation of the boundary conditions under which consolidation succeeds or fails.

## Research connections

- **L-001:** Superficial match—assumes unified skill infrastructure solves reuse; does not investigate whether adopted skills become harder to modify or whether the ontology itself ossifies.
- **L-005:** Superficial match—does not examine whether replacing or restructuring skill subsystems in a mature SkillNet system would be constrained by operational dependency or drift risk.
- **L-004 (Goodhart):** Latent connection—if skill value is measured by evaluation metrics, optimization pressure on those metrics could decouple learned skills from actual task success; not explored.
- none (others)

## Seed

**Seed title:** Skill Reuse Resistance as Coordination Cost Displacement

**Seed type:** question

**Seed text:** SkillNet assumes that making skills legible, evaluable, and discoverable via unified ontology removes barriers to reuse. But if agents "reinvent the wheel" despite access to prior solutions, the barrier may not be *legibility* but *integration cost*: adapting a skill learned in one context to a new one may require more computation, debugging, or causal understanding than learning anew. The paper does not distinguish between "skills are invisible" (legibility problem) and "skills are costly to integrate" (coordination cost problem). If the latter is primary, SkillNet reduces *search* cost but may not reduce *adaptation* cost, and the infrastructure itself becomes a new coordination overhead. Worth tracking whether unified skill infrastructures reduce or merely *displace* the work of capability transfer.
