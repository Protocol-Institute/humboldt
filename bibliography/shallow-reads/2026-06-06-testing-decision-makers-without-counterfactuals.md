# Testing Decision Makers without Counterfactuals

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.02095
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper studying inference of agent rationality and information quality in bandit environments where an outside observer has access only to chosen actions and their realized payoffs—never counterfactual outcomes. The work addresses whether one can distinguish informed from uninformed decision-makers when recommendations and their consequences are partially unobservable.

## What I took from it

This is a technical contribution to revealed-preference inference and strategic information asymmetry, operating within classical economic/game-theoretic assumptions (rationality, optimization, equilibrium). The core problem—inferring agent quality without counterfactuals—is operationally relevant to any system where we audit decision-making in bandit-like settings (e.g., recommendation systems, trading agents, medical protocols).

However, the framing remains within standard decision theory. The adviser-decisionmaker setup assumes both agents are optimizing agents with stable preferences; the question is epistemic (what can we infer?), not about how protocols reshape rationality itself or how observational structure constrains what *kinds* of decisions become legible. It does not address how partial observability creates new forms of agency or decision logic peculiar to artificial systems—it treats observability as an inference problem, not a constitutive feature of the system's nature.

## Research connections

- none identified; no existing laws or hypotheses yet defined in context.

## Candidate laws or signals

**CL-2606-01:** Partial observability of counterfactuals makes agent-quality inference identifiable only under specific correlation structures between choice and information—suggests that legibility of decision-maker rationality depends critically on the *topology* of what remains hidden.
