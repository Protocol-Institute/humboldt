# Detecting Deceptive Recruitment: A Signal-theoretic Machine Learning Framework for Early Identification of Labour Exploitation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.20336
**Date read:** 2026-09-22
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An applied machine learning classification study that formalizes labour exploitation signal detection using signalling theory over a dataset of 464 job advertisements (164 deceptive, 300 legitimate). The work treats exploitative recruitment as a costless-signal mimicry problem and develops multimodal classifiers across text, visual, and structural features.

## What I took from it

The paper engages with the proxy formalization problem at the boundary of L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement), but remains trapped in a single-domain applied setting without mechanism insight into how the protocol itself changes under detection pressure.

The core vulnerability: the paper assumes deceptive signals remain stable features once formalized as classifier inputs. It does not model what happens when exploiters observe that certain textual, visual, or structural patterns trigger detection — i.e., it builds a static classifier without modeling the adversarial co-evolution loop. This is precisely the domain where L-008 lives: once a proxy becomes legible and computable, optimizing agents shift the optimization target away from the proxy. The paper has no account of this migration.

There is latent relevance to L-004 (metric capture under optimization pressure): if this detector were deployed and enforced at scale, exploiters would not abandon deceptive recruitment; they would learn to generate signals that evade the classifier while remaining functionally deceptive to human targets. The paper does not theorize this equilibrium.

## Research connections

- **L-004:** The paper formalizes deception detection as a measurable proxy, but does not examine what happens when that proxy becomes an enforcement target under adversarial optimization.
- **L-008:** The detection protocol creates a computable, legible signal space; the paper lacks a model of how agents respond once that legibility becomes actionable.
- **seed-128 (Legibility-Driven Agent Convergence Under Computable Audit):** If the classifier becomes auditable and enforced, exploiters may converge on evasion strategies that satisfy the proxy while preserving deception capability — a coordination phenomenon the paper does not address.
- **seed-133 (Metric Formalization as Paradigm Lock in Safety Protocols):** Once deception is operationalized as a classification problem, the protocol may lock into a feature-based paradigm that misses functional deception modes the classifier was not trained to detect.

## Seed

**Seed title:** Proxy Stability Collapse Under Adversarial Co-evolution in Harm-Detection Protocols

**Seed type:** motif

**Seed text:** In protocols designed to detect harmful agent behavior through formalized, computable proxies (textual patterns, structural markers, visual features), the stability of the proxy-as-classifier depends critically on whether optimizing agents observe the detection rule and can modify their input generation process. Once a harm-detection proxy becomes legible and enforced, the agent population does not remain stable; exploiters migrate toward signal-generation strategies that preserve functional harm intent while evading the proxy. This creates a fundamental non-monotonicity: increasing detector accuracy and enforcement legibility can accelerate proxy capture and migration, rather than reducing harm. The mechanism is not specific to labour exploitation; it should generalize to any detection protocol where the target population is adaptive and the proxy is computable.
