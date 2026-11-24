# Who Convinced Whom? Tracing How LLMs Change Their Minds in Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.35930
**Date read:** 2026-11-23
**Connected to:** L-017, L-011
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary empirical source directly measuring the mechanism of L-017 (Guidance-Layer Coalescence) and L-011 (Causal Detachment) — it provides behavioral evidence that agents in multi-agent systems achieve agreement through shared exposure rather than independent verification, which is foundational to both laws and absent from current inventory documentation.

## What this is

An empirical study measuring how language models change their positions during multi-agent debate (MAD) through behavioral and internal probing. The authors introduce MAD Bench (2,400 questions) and test whether consensus in debate reflects independent corroboration or shared persuasion without independent verification. The work uses round-matched control conditions to isolate the effect of peer communication on model decisions across knowledge, reasoning, values, and safety domains.

## What I took from it

This work directly operationalizes a critical failure mode: agents converging on positions not because each independently verified them, but because they received the same external guidance or were exposed to shared persuasive sequences. The control design (round-matched independent reflection) allows isolation of the "agreement without verification" condition — precisely the causal detachment mechanism in L-011 and the hidden coordination pathway in L-017. 

The benchmark spans multiple domains (knowledge, reasoning, values, safety), which suggests the phenomenon generalizes beyond single task classes. This is crucial: if guidance-layer coalescence produces indistinguishable functional consensus across heterogeneous problem types, it becomes a property of the multi-agent protocol *itself*, not an artifact of domain specifics. The safety domain is particularly important — if refusal behavior synchronizes through shared guidance rather than independent safety reasoning, this reveals a critical vulnerability in distributed safety protocols.

## Research connections

- **L-017 (Guidance-Layer Coalescence):** Direct empirical measurement of how shared AI guidance produces apparent coordination without independent agent reasoning — this is the phenomenon L-017 postulates as a hidden channel.
- **L-011 (Causal Detachment):** Evidence that operationally functional configurations (consensus, agreement) emerge decoupled from the causal chain of independent verification — agents appear to reason independently but are actually synchronized through shared inputs.
- **L-004 (Goodhart Generalization):** If models optimize for agreement signals within debate, those signals may proxy for correctness while actually selecting for susceptibility to shared persuasion.
- **seed-515 (Computable Belief as Collusion Surface):** The legibility of model internal states and decision traces may create an unintended coordination surface when multiple agents observe or receive guidance about the same computable belief states.
- **seed-320 (Narrative Proxy Capture):** Debate exchanges are narrative outputs; if models update based on narrative persuasiveness rather than evidence, the protocol selects for narrative capture rather than truth-tracking.

## Seed

**Seed title:** Agreement-Verification Decoupling in Shared-Guidance Multi-Agent Protocols

**Seed type:** observation

**Seed text:** In multi-agent systems where agents receive guidance, arguments, or decision inputs from shared sources (whether explicit debate partners or implicit guidance systems), consensus emerges decoupled from independent verification of the consensus target. Agents synchronize on shared exposure, not on corroborating evidence. This produces operationally indistinguishable consensus (identical decisions, apparent reasoning chains) but with fundamentally different causal structure: coordinated-by-guidance rather than coordinated-by-convergent-evidence. The phenomenon generalizes across problem domains (knowledge, reasoning, values, safety) and is detectable only through interventional isolation of shared-exposure paths. This suggests guidance-layer coalescence is a stable equilibrium in any multi-agent protocol with legible shared-input architecture, independent of task semantics.
