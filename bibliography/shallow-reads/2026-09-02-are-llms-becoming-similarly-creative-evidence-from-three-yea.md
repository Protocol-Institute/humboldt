# Are LLMs becoming similarly creative? Evidence from three years of models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.19437
**Date read:** 2026-09-02
**Connected to:** L-001, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmarking and trend analysis paper measuring creative output diversity across three years of LLM releases using the Infinity-Chat100 dataset. The work tracks whether LLMs are converging or diverging in their creative performance on open-ended tasks.

## What I took from it

The paper appears to document an empirical pattern — convergence toward similarity in creative outputs across successive model generations — but does not propose a mechanism or develop a sustained theoretical argument about *why* this occurs. The triage note connects this to L-001 (protocol ossification under adoption) and L-013 (paradigm-locked anomaly tolerance), but the paper itself does not engage with protocol dynamics, governance structures, or institutional blindness. It is primarily a descriptive trend measurement.

The observation that LLMs converge in creative behavior *could* reflect ossification pressures (adoption-driven constraints on model design freedom, training data homogenization, RLHF standardization) or paradigm lock (a stable configuration that resists deviation despite evidence it produces less diverse outputs). However, the paper does not examine these mechanisms. It measures the phenomenon but not the causal substrate.

## Research connections

- **L-001:** Possible evidence that widespread adoption of LLM architectures and training paradigms constrains creative diversity, but the paper does not examine whether this is due to protocol-level ossification or other factors (scaling laws, data saturation, optimization pressure).
- **L-013:** The convergence *could* reflect paradigm lock — an established approach (transformer + RLHF) that is retained despite accumulating evidence of reduced creative diversity — but this requires inferential work the paper does not perform.
- **seed-077 (Metric-Induced Preference Ratcheting):** If training metrics or evaluation criteria systematically favor certain output distributions, this could drive convergence; the paper does not examine training objectives.

## Seed

**Seed title:** Creativity-Diversity Divergence Under Legibility Pressure

**Seed type:** observation + question

**Seed text:** LLM creative outputs may converge toward similarity not because of architectural constraints, but because verifiable evaluation of "good" creative work is harder than verifiable evaluation of correctness, and under adoption pressure, systems migrate toward measurable proxies (fluency, coherence, safety compliance) that are more amenable to automated optimization and ranking. If true, this would reflect a more general pattern: open-ended tasks remain diverse only when evaluation is informal or decentralized; formalization of evaluation criteria under scaling pressure drives convergence toward the legible dimensions. Worth tracking whether this holds across other generative domains (image, music, design).
