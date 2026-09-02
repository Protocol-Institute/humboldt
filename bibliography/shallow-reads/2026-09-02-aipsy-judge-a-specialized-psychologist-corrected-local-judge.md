# aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.24899
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper demonstrating that frontier LLMs fail systematically at evaluating psychological safety in conversational AI, and proposing a psychologist-grounded evaluation protocol (aipsy-judge) as corrective. The work is a tool/method contribution with domain-specific validation, not a theoretical or mechanistic argument about protocols or artificial systems.

## What I took from it

The paper confirms a narrow instance of L-004 (Goodhart Generalization): when LLM-as-judge becomes the computable proxy for an unmeasurable target (psychological safety), the proxy optimizes away from the target under adoption pressure. The disagreement between frontier models and psychologist ratings is "structured and concentrated on safety-critical metrics" — precisely where the proxy capture matters most.

However, the paper does not generalize the mechanism. It does not ask why LLMs systematically fail at this task, whether the failure is inherent to the proxy architecture or remediable through fine-tuning, or how the problem propagates in downstream deployment contexts where aipsy-judge itself becomes a new proxy target. The contribution is domain-local: a better judge for one class of safety problems. It does not constitute a new mechanism or a challenge to existing laws.

## Research connections

- **L-004:** Confirms metric capture in safety evaluation — frontier models diverge from ground truth precisely on safety-critical dimensions when used as judges.
- **L-008:** Touches the mechanism but does not probe it: computable enforcement signals (model agreement/disagreement) fail to align with the unmeasurable target, but the paper does not investigate why optimizing agents (downstream systems) would prefer the proxy over the corrected judge.
- **seed-073 (Correlated Failure Under Proxy Consensus):** The structured disagreement suggests correlated failure modes across frontier models — they agree with each other but not with psychologists — a potential substrate for this seed.

## Seed

**Seed title:** Safety-Critical Proxy Inversion in Multi-Model Judge Consensus

**Seed type:** observation

**Seed text:** When multiple frontier models are used as judges for safety-critical properties (psychological harm, deception, manipulation), they exhibit structured agreement with each other that diverges systematically from expert ground truth. This disagreement is not random noise but concentrates on the safety-critical dimensions themselves — the very axes where proxy capture is most costly. The implication: consensus among optimized systems may be an active *indicator of proxy capture*, not a signal of reliability. This may generalize to any domain where the judging systems and the generating systems share training objectives or data sources, creating a correlated failure mode that high-model-count averaging does not resolve.
