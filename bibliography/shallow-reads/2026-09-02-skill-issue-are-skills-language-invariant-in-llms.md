# Skill Issue: Are Skills Language-Invariant in LLMs?

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.25832
**Date read:** 2026-09-02
**Connected to:** none
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement paper using multilingual self-play to isolate cross-lingual skill inconsistency in LLMs from knowledge and benchmark artifacts. The work quantifies performance variance when the same model interacts with identical game states and rules through different language interfaces, treating language as an orthogonal measurement axis rather than a confound.

## What I took from it

This is primarily a methodology contribution rather than a theoretical argument about protocolized systems. However, it surfaces a measurement problem relevant to our research: **the gap between legible performance metrics and actual capability substrate**. When an LLM's skill set changes visibly depending on the language interface through which it engages with identical protocol rules and state space, this suggests that observable protocol behavior cannot be cleanly separated from the *substrate's* interface assumptions.

The deeper relevance: protocols designed with English-language benchmarks as validation may be encoding legibility assumptions rather than robust coordination properties. This touches on seed-062 (Formalization Opacity Collapse) and seed-069 (Transparency-Legibility as Trust Proxy Substitution) — the paper demonstrates that a protocol's apparent functioning depends on which language lens we measure through, raising questions about whether we are measuring the protocol or the measurability itself.

## Research connections

- **seed-062:** Formalization as applied through a single language interface may collapse when the system encounters opacity in alternative representational substrates; the paper shows this concretely.
- **seed-069:** Language-interface legibility may be substituting for actual trustworthiness in protocol evaluation — we observe consistent performance under English but not under other languages, yet still treat benchmarks as universal.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** Cross-lingual skill drift is an anomaly in the "language-universal AI" paradigm that may be tolerated without triggering paradigm review because the measurement apparatus itself enforces English-first evaluation.

## Method note

This paper exemplifies the value of *orthogonal stress testing*: by holding all protocol elements constant (opponent, rules, state, actions) and varying only the interface layer, it isolates a substrate-level artifact that conventional benchmarking obscures. For protocolized systems research, this suggests that validation frameworks should routinely test across multiple representational substrates (not just languages — also notation systems, encoding formats, mediation layers) to distinguish genuine protocol robustness from apparent robustness-under-a-specific-measurement-regime. The work also implies that "skill" and "knowledge" are not separable at measurement time — a finding that should inform how we operationalize protocol compliance.
