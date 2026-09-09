# Rules Before Oracles: Auditable, User-Configurable Argument Selection for Deliberative Polling

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.23979
**Date read:** 2026-09-02
**Connected to:** L-015, seed-021
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A design paper proposing rule-based, auditable argument selection mechanisms for deliberative polling as an alternative to opaque learned rankers. The work formalizes argument filtering over recomputable evidence with voter-held parameters, treating legibility as a hard constraint rather than an accuracy trade-off. Primarily a tool/mechanism contribution to deliberative AI systems rather than a primary theoretical argument.

## What I took from it

The paper demonstrates a real instance of L-015 (Interpretive Continuity Decay) in action: even when voting outputs remain stable and formally recorded, the *upstream selection mechanism* that shapes exposure — and therefore cognition — can decay into illegibility, creating a hidden locus of preference formation that voters cannot reconstruct or contest. The framing explicitly rejects the standard accuracy-vs-interpretability framing and instead treats auditability as a prerequisite for protocol legitimacy.

This is instrumentally relevant but not theoretically novel. The paper does not investigate *why* opacity persists despite legitimacy costs, nor does it probe what happens when rule-based auditable systems themselves degrade under optimization pressure (e.g., when voters game parameter-setting, or when rule complexity grows beyond auditability). It is a design response to a known problem, not an exploration of a generative mechanism.

## Research connections

- **L-015:** Directly instantiates the core claim: formal records of outcomes survive while the institutional interpretation apparatus (argument exposure) becomes unmapped and uncontestable.
- **seed-021:** Relates to the hypothesis that "level-choice-as-frozen-politics" — i.e., the choice of *what layer to make legible* becomes itself a frozen political act.
- **seed-072:** Peripherally connected: the paper addresses explanation-marker decoupling (what was shown vs. what shaped judgment) but does not investigate how markers diverge under scaled use.

## Seed

**Seed title:** Auditability as Prerequisite vs. Auditability as Target

**Seed type:** motif

**Seed text:** Deliberative polling systems that delegate argument selection to learned rankers face a legitimacy crisis not because outcomes are wrong but because the selection mechanism is unreconstructible — voters cannot contest what shaped their cognition. Rule-based auditable selection restores legitimacy by making the filtering function recomputable. However, this does not investigate whether auditability itself becomes a target under optimization (voters learning to exploit rule parameters; rule complexity creeping beyond effective auditability). A generalized law might hold: *Systems that elevate auditability from a side property to a hard constraint inadvertently create a new optimization surface — the parameters and structure of the audit mechanism itself.* This mirrors L-014 (Strategic Boundary Concentration Under Computable Legality) but inverted: legibility as the prize rather than the boundary.
