# It is not enough to give your moderation rules to ChatGPT: Policy-as-Prompt Moderation and Its Potential Impacts on Community Governance

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.12149
**Date read:** 2026-09-01
**Connected to:** L-003, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical case study examining how AI language models (specifically ChatGPT) fail to faithfully execute community moderation policies when policies are encoded as natural language prompts. The paper observes drift between stated policy intent and AI-mediated enforcement outcomes in both centralized and decentralized moderation contexts.

## What I took from it

The paper documents a specific instantiation of L-003 (Formalization Ratchet) and L-015 (Interpretive Continuity Decay): when informal moderation norms are formalized into prompts for AI systems, two failure modes emerge. First, the act of formalization itself changes the policy's meaning — what was tacit practitioner judgment becomes a brittle specification. Second, the AI's interpretation of the formal policy diverges from the community's original interpretive consensus, creating a lag between the recorded policy text and its operative effect. The paper treats this as a technical robustness problem (how to make ChatGPT follow rules better), but the underlying pattern is institutional: formalization + delegation to a system without shared interpretive history = loss of coherence.

This is less about AI capability and more about what happens when you extract governance from a community of practice and encode it for execution by a black-box agent. The policy doesn't travel cleanly; it decays in translation.

## Research connections

- **L-003 (Formalization Ratchet):** The paper shows formalization of informal norms into prompts as a stress response (scaling pressure), confirming the ratchet direction, but does not generalize the mechanism beyond the specific AI moderation case.
- **L-015 (Interpretive Continuity Decay):** The paper demonstrates loss of interpretive consensus when policy text survives but institutional memory of *how to apply it* does not. This is the core mechanism L-015 posits.
- **seed-018 (Revision Implicates Responsibility):** The paper hints at resistance to policy revision when AI systems are involved — changing the prompt is no longer a community discussion, but a technical intervention with opaque consequences.

## Seed

**Seed title:** Policy-Prompt Opacity as Norm Decay Accelerant

**Seed type:** observation

**Seed text:** When governance rules are encoded as natural language prompts to AI systems, the interpretive gap between formal policy text and operative enforcement widens faster than in human-mediated systems. This occurs because: (1) the AI has no access to the historical reasoning or edge-case discussions that shaped the norm, (2) communities cannot easily audit or reverse-engineer the AI's interpretation, and (3) attempted corrections to the prompt often produce second-order drift. The mechanism generalizes beyond content moderation to any protocol system where formalized rules are delegated to optimizing agents without shared institutional memory — regulatory systems, resource allocation, audit protocols. The decay rate depends on both the complexity of the policy and the opacity of the enforcement system.
