# Validity of LLMs as data annotators: AMALIA on authority

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.08731
**Date read:** 2026-09-01
**Connected to:** L-004, seed-029
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study testing whether Portugal's AMALIA (a 9B-parameter national language model) can reliably annotate coded theoretical constructs (moral foundations of authority) at scale. The paper argues that agreement metrics (F1 scores) conflate reliability with validity — AMALIA achieves near-parity with larger open models on surface-level agreement but the question of whether it measures the *intended* construct remains open.

## What I took from it

This is a clean instantiation of L-004 (Goodhart Generalization) in the annotation domain: the protocol uses agreement-with-human-coders as a proxy for validity of theoretical measurement, and optimization pressure (scaling AMALIA, fine-tuning on annotation tasks) pushes toward agreement maximization while leaving the underlying validity question untouched. The paper does not resolve whether the model is capturing linguistic authority or merely surface statistical patterns that correlate with human coding behavior.

The work also touches seed-029 (exemplar-vs-rule-as-protocol-type): AMALIA functions as a *national* exemplar of linguistic authority — it is being positioned as the community's own instrument for measuring what citizens value. This creates a closure risk: once a national model is canonized as the measurement standard, deviation from its judgments becomes interpretable as deviation from community authority rather than as disagreement about what authority *is*. The paper's hesitation about validity is sound, but it does not address the political lock-in that occurs when the exemplar becomes the rule.

## Research connections

- **L-004:** Agreement metrics drive optimization away from validity; the proxy (F1 agreement) becomes decoupled from the construct (whether the model understands moral authority) under sufficient optimization pressure.
- **seed-029:** A national model functions as both exemplar and measurement standard, conflating exemplary performance with definitional authority — once institutionalized, this becomes hard to revise.
- **seed-015:** The choice to deploy AMALIA as a national annotation standard is a taming act with political implications that the paper does not examine.

## Seed

**Seed title:** Validity-Agreement Decoupling in Canonical Measurement Models
**Seed type:** observation
**Seed text:** When a model is adopted as the official measurement instrument for a theoretical construct within a community (especially a national or institutional community), agreement with that model becomes progressively conflated with validity of the measurement itself. The closer the model approximates human coder agreement, the stronger the pressure to treat it as the canonical standard — yet agreement and validity remain independent properties. Once institutionalized, questioning the model's validity becomes institutionally costly, and communities accumulate technical debt in measurement reliability without triggering revision pressure.
