# Register Bias in Complexity-Based Large Language Model Routing

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.17542
**Date read:** 2026-09-22
**Connected to:** L-004, seed-133, seed-152
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study documenting systematic bias in LLM routing systems: complexity-estimation proxies used to allocate queries to models of differing capability misclassify non-standard English registers (AAE, L2 English) as lower-complexity than meaning-equivalent standard English. The mechanism is register-specific feature detection in the complexity estimator, not model capability difference.

## What I took from it

This is a concrete instantiation of L-004 (Goodhart Generalization) and seed-133 (Metric Formalization as Paradigm Lock), but at a narrower resolution than either predicts. The routing system optimizes on a measurable proxy (syntactic/lexical complexity) for an unmeasurable target (actual query difficulty). Under optimization pressure, the proxy drifts silently — it captures register variance orthogonal to the underlying construct, and this drift is invisible to the system operators because the routing decision itself (sending a query to a smaller model) is locally sensible and rarely escalates to visibility.

The key observation is *silent capture*: unlike Goodhart cases where the proxy itself becomes the goal and distorts behavior visibly, here the proxy misfire remains latent in allocation decisions that rarely surface as errors. The complexity estimator has formalized a construct (query difficulty) that was never fully specified, and the formalization has locked the system into a register-blind operationalization. This connects to the broader pattern in seed-133: when a safety-relevant or fairness-relevant property is replaced by a computable metric, the formalization becomes hard to revise even after bias is documented.

## Research connections

- **L-004:** Metric proxy (complexity) capturing unmeasurable target (actual difficulty); optimization pressure causing drift orthogonal to the goal; fairness property unprotected by the proxy.
- **seed-133:** Metric formalization (complexity estimation) locks the system into a paradigm that treats register variance as signal rather than noise; revising the metric requires challenging what "complexity" means operationally.
- **seed-152:** Not in inventory — triage note may indicate external reference; no connection available.
- **L-012:** Complexity signal formalized as legible input to allocation decision; optimization pressure on the router (to send queries efficiently) displaces actual optimization locus from fairness to throughput.

## Seed

**Seed title:** Register-Orthogonal Proxy Drift in Safety-Decoupled Allocation
**Seed type:** observation
**Seed text:** When a protocol allocates resources (or capability access) using a formally computable proxy for a latent construct that correlates with a protected attribute, the proxy captures variance orthogonal to its intended target. The misallocation remains invisible if the downstream outcome (allocation decision) is locally rational and rarely triggers escalation. The formalization of the construct locks the system against revision because the proxy has become the canonical definition of the target, and changing it requires retroactively re-specifying what the construct means. This pattern generalizes beyond register bias to any domain where a measurable substitute is chosen for a construct that is entangled with demographic or distributional variance.
