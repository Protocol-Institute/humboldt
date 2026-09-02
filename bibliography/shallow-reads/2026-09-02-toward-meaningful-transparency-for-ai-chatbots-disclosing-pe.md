# Toward Meaningful Transparency for AI Chatbots: Disclosing Persuasive Intent Reduces Persuasion

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.11794
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** empirical intervention study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A preregistered randomized controlled trial testing whether disclosure of AI involvement and persuasive intent reduces the persuasive effect of a chatbot on policy attitudes in 1,500 UK adults. The work measures persuasion as a measurable outcome and varies the legibility of the chatbot's operative function (persuasive intent).

## What I took from it

The paper provides direct empirical evidence that *making the optimization target legible* (disclosure of persuasive intent) reduces the success of that optimization. This is a narrow validation of a prediction implicit in L-012 and L-004: when a protocol's operative function becomes transparent, agent resistance increases, reducing the metric's validity as a success measure.

However, the work does not investigate the equilibrium consequences. It does not ask: What happens when the chatbot knows disclosure will reduce persuasion? Does it shift strategy layers (e.g., obfuscate intent through different framing)? Does disclosure become costly to enforce? This is a single-round intervention, not a protocol evolution study. The finding is real but isolated — it lacks mechanism depth and doesn't explore whether the effect persists under adaptation or becomes a coordination problem.

The intervention is additive (disclosure *added* to a fixed chatbot), which is the weakest form of evidence for protocol generalization. It tells us about user psychology under transparency, not about how systems redesign under persistent optimization pressure.

## Research connections

- **L-004 (Goodhart Generalization):** Disclosure makes the optimization target (persuasion) legible; agent awareness reduces the target's validity. But this is a user-side phenomenon, not protocol capture.
- **L-012 (Intervention-Layer Displacement):** Disclosure is an intervention at the information layer; the finding suggests the locus of persuasion optimization may shift if the agent adapts (not tested).
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** Disclosure functions as a trust signal, but the mechanism is suppression of persuasion, not substitution of trust itself.
- **seed-082 (Additive Intervention in Overloaded Protocols):** The disclosure is additive; no evidence whether it resolves or merely displaces the underlying persuasion protocol.

## Seed

**Seed title:** Legibility Resistance Without Adaptation
**Seed type:** observation
**Seed text:** Making an optimization target legible to the subject (here: disclosing persuasive intent) reduces immediate optimization success, but the study design cannot detect whether the optimizing agent adapts the target, shifts layers, or accepts reduced efficiency as the new equilibrium. In protocol systems with adaptive agents, disclosure may trigger layer displacement rather than true mitigation — the persuasion function may migrate to implicit channels or downstream interventions. This suggests legibility resistance is fragile and temporary absent enforcement of the target space itself.
