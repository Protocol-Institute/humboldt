# Not Birds of a Feather: Personality-Based Partner Selection in LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.19785
**Date read:** 2026-09-02
**Connected to:** L-010, seed-033
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of partner selection in multi-agent LLM systems, testing whether personality archetypes (Big Five traits) influence agent choice when capability is held constant. The work runs 375 trials across five task categories, varying personality profiles while controlling information asymmetry about actual competence.

## What I took from it

The paper is a competent behavioral study but remains narrowly scoped to personality-signaling effects in a controlled laboratory setting. It documents that LLM agents do condition partnership choice on personality cues when capability information is unavailable — a finding consistent with L-010 (Coordination Adoption Nonmonotonicity: agents do condition on coordination signals from others). However, the study does not probe the mechanism by which personality becomes a *proxy* for unobserved capability, nor does it investigate what happens when personality signals decouple from actual performance under real task stress, or how agents revise personality-based priors after failure. The paper provides a data point on signal utilization but does not generalize to the broader pattern: how legible but decoupled attributes become coordination anchors in systems with incomplete capability information.

The work touches seed-033 (partner selection under incomplete information) but does not advance the mechanistic question: *under what deployment pressures does personality-as-proxy stabilize or collapse?* There is no indication whether this effect scales, competes with other signals, or produces systematic miscoordination when personality diverges from competence.

## Research connections

- **L-010:** Confirms that agents do use legible signals (personality) to condition adoption/partnership decisions when capability is opaque; consistent with coordination nonmonotonicity under signal-dependence.
- **seed-033:** Documents personality as a partner-selection proxy under incomplete information, but does not examine stability or failure modes.
- **seed-069:** Tangent: personality markers may function as trust proxies in asymmetric-knowledge protocols, but paper does not theorize this as substitution mechanism.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Store rationale:** This is a well-executed single-variable study that documents a behavioral effect but does not introduce a mechanism absent from the inventory, does not challenge or extend a law, and does not provide foundational grounding for an open line. It is a behavioral measurement within an already-identified pattern (signal-dependent coordination) rather than a new regularity. File as supporting evidence for L-010 and seed-033, but do not escalate.
