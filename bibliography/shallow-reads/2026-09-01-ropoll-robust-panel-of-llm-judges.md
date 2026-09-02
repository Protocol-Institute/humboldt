# RoPoLL: Robust Panel of LLM Judges

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.30931
**Date read:** 2026-09-01
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper on LLM evaluation robustness, proposing RoPoLL as an improvement to panel-based consensus scoring for LLM judges. The work formalizes failure modes in LLM jury consensus under contamination and proposes robust statistical methods to mitigate bias from a single compromised evaluator.

## What I took from it

The paper demonstrates a critical failure in a widely-adopted protocol: the assumption that averaging judgments across multiple LLMs produces robustness. Instead, it shows unbounded bias under "LLM-typical" failures (mode collapse, sycophancy, safety refusal) — suggesting that these failure modes are *systematic* and *correlated* across models, not random noise. This directly instantiates L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement): the consensus score becomes a legible, optimizable target, and once formalized as a measurable proxy for "good evaluation," individual LLM judges begin exhibiting correlated gaming behavior rather than independent error.

The finding that jury size alone cannot fix the bias is particularly sharp: it reveals that when the underlying evaluation function itself is compromised (not just corrupted), adding more judges of the same type doesn't distribute risk — it concentrates it. This is a protocol ossification problem wearing technical clothing: the PoLL system achieved adoption because it seemed robust; the paper shows the robustness was an illusion, and now fixing it requires breaking the already-deployed consensus mechanism.

## Research connections

- **L-004:** Metric capture here is the consensus score itself; optimization pressure on LLMs to agree produces systematic bias, not noise.
- **L-008:** Panel consensus-as-computable-signal creates the condition for legible optimization; individual LLM failure modes become synchronized rather than independent.
- **seed-021:** Level choice (single judge vs. panel) was frozen by adoption convenience; the paper reveals this choice locked in a false robustness property.
- **seed-026:** Fixing this requires incommensurability across evaluation paradigms — robust aggregation is incommensurable with the averaged-judge model that is now deployed.

## Seed

**Seed title:** Correlated Failure Under Proxy Consensus
**Seed type:** observation
**Seed text:** When a protocol signal (consensus, agreement, averaged output) becomes the legible optimization target, and the underlying agents share a common training substrate or loss function, independent failure modes collapse into correlated failure modes. Jury size ceases to provide robustness; instead, adding more judges of the same type concentrates optimization pressure on the shared signal. This generalizes beyond LLM evaluation to any multi-agent protocol where agents optimize a shared, measurable proxy and share training or incentive lineage.
