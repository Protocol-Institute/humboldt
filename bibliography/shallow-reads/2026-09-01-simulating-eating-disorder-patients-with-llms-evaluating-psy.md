# Simulating Eating Disorder Patients with LLMs: Evaluating Psychological Persona Stability in Multi-Turn Conversations

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.26109
**Date read:** 2026-09-01
**Connected to:** L-013, seed-015
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical validation study of LLM clinical simulation stability using eating disorder personas grounded in published case vignettes, dual-assessment framework, and psychometric instruments. The work evaluates whether LLM-based patient simulants maintain coherent psychological profiles across multi-turn conversations—a prerequisite for clinical validity.

## What I took from it

This is a methodological paper documenting a failure mode: LLMs assigned stable clinical personas drift or contradict their assigned profiles under multi-turn interaction, even when grounded in validated case vignettes and measured against known psychometric ground truth. The paper does not theorize this failure; it documents and measures it.

The relevance to L-013 (Paradigm-Locked Anomaly Tolerance) is tangential. The work itself does not exhibit tolerance of malfunction—it explicitly detects and reports the instability. What *would* be theoretically interesting is if clinical training and research communities continued deploying these simulants *despite* known persona instability, or rationalized the drift as acceptable for certain training purposes. The paper provides the diagnostic substrate for that question but does not itself investigate institutional adoption or anomaly tolerance post-detection.

## Research connections

- **L-013:** The paper surfaces a failure mode (persona drift) that clinical protocols *using* LLM simulants might tolerate if deployment pressure and training scalability incentives are strong enough; the paper is a precondition for observing whether L-013 applies here, but does not itself observe it.
- **seed-015 (C-015-taming-as-political-act):** The framing of "taming" LLMs for clinical use involves boundary-setting around what drift is acceptable; the paper's ground-truth measurement framework is itself a taming mechanism, but does not interrogate the politics of where the boundary gets drawn post-publication.

## Method note

This work demonstrates the value of dual-assessment frameworks and validated psychometric ground truth in detecting protocol degradation in synthetic systems. It establishes a diagnostic practice that *should* precede deployment decisions, but the paper does not investigate whether such diagnostics actually gate deployment or are decoupled from adoption. The research design itself is sound; the open question is whether this kind of validation becomes a ritual that generates the appearance of scrutiny without constraining adoption—a meta-protocol concern worth tracking across domains where synthetic systems are deployed in safety-sensitive contexts.
