# When benchmark inferences do not compose: Projectibility in AI evaluation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.26159
**Date read:** 2026-09-02
**Connected to:** seed-026
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A meta-methodological paper identifying a specific epistemic failure in AI evaluation: the assumption that valid individual benchmark claims chain together into valid composite claims. The paper argues that projectibility—the ability to transport inference across systems, populations, tasks, and sites—is not guaranteed even when each link in the chain is individually warranted.

## What I took from it

This is primarily a cautionary note on evaluation methodology rather than a source for law induction. It documents a real failure mode in how we accumulate evidence about protocolized systems, particularly AI evaluation protocols. The core insight—that compositionality of valid inferences is not automatic—is relevant to **L-013 (Paradigm-Locked Anomaly Tolerance)** in that it describes how systemic misevaluation can persist even under valid local reasoning, and to the broader question of **how we detect protocol failure when measurement systems themselves are epistemically brittle**.

However, the paper does not propose a mechanism explaining *why* projectibility breaks down in protocolized systems, nor does it generalize the failure mode as a law-like pattern. It functions as a corrective to research practice rather than as evidence for or against a standing hypothesis about protocol behavior.

## Research connections

- **seed-026:** Confirmed—benchmark compositionality failures are indeed instances of incommensurability cost; projectibility deficits mark the boundary where formalization breaks down under transport.
- **L-004 (Goodhart Generalization):** Tangential—benchmark results are often proxies, but the paper's concern is structural (composition) rather than optimization-driven capture.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** Indirect—shows how valid local reasoning can coexist with systemic invalidity, relevant to understanding why anomalies in composite claims go undetected.

## Method note

This paper flags a critical blind spot in evidence accumulation: we validate individual steps but not the chain. For protocolized system research, this suggests we need explicit protocols for verifying projectibility *before* scaling up from local findings. The implication is that meta-level audit of inference chains—not just validity of individual claims—should be a standard stage in research synthesis, particularly when building arguments that cross domains or populations.
