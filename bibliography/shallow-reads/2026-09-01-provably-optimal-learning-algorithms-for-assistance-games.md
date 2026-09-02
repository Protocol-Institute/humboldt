# Provably Optimal Learning Algorithms for Assistance Games

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.08012
**Date read:** 2026-09-01
**Connected to:** none
**Kind:** content
**Escalation:** store-only

---

## What this is

A game-theoretic paper analyzing repeated interaction between an informed principal (human) and an uninformed agent (assistant) optimizing a shared reward function. The work provides regret bounds for learning algorithms when the agent must infer latent state from observed human actions alone.

## What I took from it

The paper is technically clean but operates in the classical game-theoretic sandbox: agents with fixed utility functions, well-defined state spaces, and explicit reward signals. It does not examine what happens when the shared reward function itself becomes contested, when the latent state becomes non-stationary due to the learning process itself, or when the assistant's inference procedure begins to shape what the human believes about the state (feedback into observation).

The "assistance" framing is suggestive—it implies an asymmetry in knowledge and agency—but the execution treats this as a parameter in a cooperative game rather than a *protocol under adoption pressure*. The assistant does not face the kind of pressure that arises when its inferences become actionable across populations, when humans adjust their signaling in response to being read, or when the cost of verification (whether the assistant's inference is correct) diverges sharply from the cost of execution. None of these are present in the model.

## Research connections

- **L-012 (exploration):** The paper formalizes inference from human actions but does not model how legibility of that inference shifts optimization pressure—e.g., once humans realize they are being read, does the signaling protocol itself change?
- **L-015 (exploration):** No discussion of interpretive continuity as the shared reward function or latent state definition drifts across repeated interaction cycles.
- **seed-049:** The paper assumes reasoning and consensus are tightly coupled (both agents optimize the same reward); it does not explore what happens when they decouple.

## Seed

**Seed title:** none
