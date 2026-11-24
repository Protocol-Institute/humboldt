# Prompt framing governs LLM default following in collective-action

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.03253
**Date read:** 2026-11-23
**Connected to:** L-012, L-017, seed-462
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring how default values embedded in LLM prompts shift model behavior in social-dilemma games (CPR extraction, threshold public goods). The work tests whether defaults function as mere information or as decision anchors that systematically bias agent choice distributions.

## What I took from it

This is a narrow, well-controlled experimental result: defaults do shift LLM choices in predictable directions. The work is competent within its scope but does not construct a mechanistic account of *why* defaults propagate, nor does it establish whether this effect is an artifact of training, a feature of language-model decision architecture, or a genuine coordination-capture phenomenon.

The connection to L-012 (Intervention-Layer Displacement) and L-017 (Guidance-Layer Coalescence) is real but surface-level. The paper shows that a legible decision signal (the default) displaces optimization locus *toward* compliance with that signal, but it does not investigate whether this constitutes a stable equilibrium, whether it generalizes across model families and prompt structures, or whether it scales to multi-agent scenarios where agents condition on *each other's* responses to the same default. The CPR and TPG games are one-shot and isolated — no feedback loop, no reputation, no strategic reasoning about what other agents will do given the same framing.

## Research connections

- **L-012:** Defaults render an optimization target legible and move the locus of agent pressure away from unmeasured goals toward compliance with the framed suggestion. But the mechanism is not explored: is this surface-level anchoring, or deep architectural alignment?
- **L-017:** A shared prompt default (the "guidance") is received by all agents independently. The paper does not test whether this creates *hidden coordination* — whether agents infer collective intent from the shared frame.
- **seed-462:** Related to prompt-induced behavioral alignment, but seed-462 likely tracks something about the *persistence* or *opacity* of such effects across contexts. This paper is single-context.

## Seed

**Seed title:** Default Legibility as One-Shot Coordination Externality

**Seed type:** question

**Seed text:** When a decision default is embedded in a legible prompt interface and presented uniformly to multiple agents in a symmetric game, does the agent's compliance with the default constitute coordination, and if so, does it produce better or worse outcomes than emergent coordination without shared framing? Under what conditions does uniform default framing become *strategic coordination* rather than passive anchoring — i.e., when do agents begin reasoning about the coordination signal the default carries rather than treating it as mere information? The question assumes that legibility of the default is a necessary condition; it does not establish whether sufficiency requires multi-round play, reputation, or explicit agent reasoning about other agents' responses to the same frame.
