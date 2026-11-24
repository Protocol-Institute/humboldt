# Peer Influence across Heterogeneous AI Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.03095
**Date read:** 2026-11-23
**Connected to:** L-017, seed-023
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement study testing how seven open-weight language models persuade or defer to one another across disagreement on three language understanding tasks. The work operationalizes "persuasion" as probabilistic shift in a receiver's decision after exposure to a peer's answer and explanation, finding that persuasion effects are substantial.

## What I took from it

This is a competent domain study documenting a real phenomenon — heterogeneous models do exhibit conformity under peer pressure — but it does not provide sustained theoretical grounding for the mechanism or generalize the pattern beyond multi-agent LLM interaction. The paper measures *that* coalescence happens, not *why* or *under what conditions* the guidance-layer effect stabilizes as a hidden coordination channel. 

The work is useful as a confirmatory data point for L-017 (Guidance-Layer Coalescence) but does not advance the mechanism inventory or challenge existing laws. It does not engage with the question of whether this persuasion effect is an artifact of training, a reflection of genuine epistemic deference, or a protocol-level vulnerability. The connection to seed-023 (Informality as Novelty Sink) is also weak — the paper does not examine whether coalition-induced conformity reduces output diversity or functional novelty over time.

## Research connections

- **L-017:** Confirms that nominally independent agents receiving shared guidance (peer explanations) exhibit conformity; does not isolate whether this is a stable equilibrium or a transient effect under repeated interaction.
- **seed-023:** No engagement with whether peer-coalescence effects suppress output diversity or novelty. Measurement is snapshot, not longitudinal.
- **seed-515 (Computable Belief as Collusion Surface):** Soft connection — if persuasion is high because explanations are legibly computable and comparable, that hints at a collusion surface, but the paper does not explore strategic conditions.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This paper is a well-executed measurement study but does not constitute a primary source presenting a sustained theoretical argument, does not challenge or extend a law, and introduces no novel mechanism absent from L-017 or seed-023. It is confirmatory evidence for an existing open line of inquiry, not a law-shaping contribution. Archive for future meta-analysis of peer influence magnitude; escalate only if follow-up work examines mechanism, strategic conditions, or long-horizon stability.
