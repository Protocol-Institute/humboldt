# Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.31498
**Date read:** 2026-09-01
**Connected to:** L-006, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A taxonomy and gap analysis paper examining six agent interoperability protocols against a governance requirements framework (membership, deliberation, voting, enforcement, transparency, adaptation). The work is primarily diagnostic—identifying what existing task-coordination protocols fail to express when deployed in governed communities—rather than presenting sustained theory or a novel mechanism.

## What I took from it

The paper confirms L-006 (Coordination Cost Conservation) by showing explicit displacement: governance functions that cannot be expressed *within* the protocol layer migrate upward to enterprise policy, human oversight committees, or external governance layers. The coordination cost doesn't vanish; it moves. This is clean observational support.

The work also touches L-015 (Interpretive Continuity Decay) tangentially: as agent systems scale and governance becomes distributed, the audit trail of decisions (who voted, why, under what rules) survives in formal records while the *institutional context* that made those records meaningful decays. The paper notes this indirectly when discussing "transparency without interpretation" in async agent systems. However, this is not the paper's main thrust, and the connection is inferred rather than explicit.

The paper does not present a new mechanism, foundational argument, or theoretical challenge. It is a competent engineering diagnosis of an interoperability gap—a problem statement, not a law candidate.

## Research connections

- **L-006:** Confirms displacement of coordination cost upward when protocols cannot express governance constraints; the work is an applied case of the conservation principle.
- **L-015:** Tangential touch on survival of formal records without institutional interpretability in distributed agent governance; underdeveloped in the paper.
- **seed-026 (incommensurability-as-deformalization-cost):** Implicit: protocols that cannot express governance norms force governance concerns back into natural language and informal human mediation, raising deformalization cost.

## Seed

**Seed title:** Expressiveness Floor in Coordination Protocols — Governance as Irreducible Residual

**Seed type:** observation

**Seed text:** Coordination protocols that are task-sufficient (message passing, capability discovery, identity) become governance-insufficient when deployed in contexts requiring collective binding decisions. The gap is not incidental but structural: governance functions (membership rules, deliberation norms, enforcement legitimacy) require expressiveness that pure task protocols systematically lack. This suggests a lower bound: protocols designed for efficiency in one layer (task coordination) cannot be extended to adjacent layers (governance coordination) without either redesign or cost displacement. The regularity may generalize: any protocol optimized for narrow functional expressiveness will fail to accommodate contextual or normative constraints that emerge only under multi-agent deployment at scale.
