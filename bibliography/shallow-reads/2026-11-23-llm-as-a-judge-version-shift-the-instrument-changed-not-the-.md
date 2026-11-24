# LLM-as-a-Judge Version Shift: The Instrument Changed, Not the Standard

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.32986
**Date read:** 2026-11-23
**Connected to:** L-013, L-015
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary empirical source demonstrating a sustained mechanism — interpretive instability under formal legibility — that directly instantiates L-015 and extends L-013 with concrete evidence of paradigm-locked tolerance for measurement discontinuity in automated evaluation protocols.

## What this is

An empirical preregistered study measuring whether LLM judge replacements preserve evaluation standards across model transitions (Qwen, Gemma, Mistral). The paper finds that version shifts do not simply increase harshness; instead, they introduce directional, non-monotonic reranking of research proposals under different information conditions—suggesting the judge's evaluation logic has drifted rather than merely calibrated.

## What I took from it

This work provides concrete instantiation of **L-015 (Interpretive Continuity Decay in Distributed Governance Protocols)**: formal audit traces (frozen proposals, evaluation records) remain intact while the institutional and interpretive substrate (the LLM's decision logic) shifts undetected. The governance system (automated research filtering) continues to operate under the assumption of stable measurement, but the instrument itself has become incommensurable.

The paper also strengthens **L-013 (Paradigm-Locked Anomaly Tolerance)**: the research community tolerates the replacement of evaluation judges without systematic verification that the standard has been preserved. The anomaly—that the instrument changed—is visible in retrospect but was not flagged during deployment. This suggests that systems locked into a paradigm (automated evaluation as neutral, versioning as transparent improvement) systematically fail to trigger alarm until the drift becomes large enough to produce contradictions.

The mechanism is generalizable: any protocol system that delegates legible judgment to an adaptive component and treats version updates as monotonic improvements will accumulate interpretive drift while maintaining formal continuity of records.

## Research connections

- **L-013:** Direct evidence that established protocol systems (automated research evaluation) tolerate accumulating measurement divergence without triggering recalibration, because the paradigm treats judge updates as improvements rather than potential discontinuities.
- **L-015:** Shows how formal audit trails (frozen proposals, scores) survive intact while the interpretive machinery (judge reasoning) decays; institutional memory of *what the standard was* becomes unrecoverable even as records remain.
- **L-023 (Informality as Novelty Sink Under Legible Optimization):** LLM judge drift may systematically downrank novel proposals under newer versions, as adaptive judges converge on higher-reward-density regions of the proposal space.
- **seed-544 (Metalinguistic Displacement Under Formalization Pressure):** The formal score remains stable-looking while the judge's metalinguistic reasoning has shifted; the protocol assumes transparency but achieves only apparent consistency.
- **seed-554 (Formal Risk Category Lag Under Operational Capability Adoption):** Newer judge versions implement capability shifts (better reasoning, different training) that create new risk categories (bias toward certain proposal types) not yet formalized in the evaluation protocol.

## Seed

**Seed title:** Measurement Drift Invisibility Under Formal Update Cycles

**Seed type:** observation

**Seed text:** In protocol systems where the measurement instrument is itself an adaptive component subject to routine versioning, discontinuities in what is measured are systematically invisible until comparison with frozen baselines reveals non-monotonic reranking. The formal continuity of records (scores, decisions) masks interpretive discontinuity in the standard itself. This drift remains undetected because version transitions are treated as improvements to precision rather than potential changes to what is being evaluated. The mechanism generalizes to any system coupling formal legibility with adaptive measurement: recommendation systems, credit scoring under model updates, safety evaluation under capability shifts—anywhere the standard is delegated to an updatable agent.
