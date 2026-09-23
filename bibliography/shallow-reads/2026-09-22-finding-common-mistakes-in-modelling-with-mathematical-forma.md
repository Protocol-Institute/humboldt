# Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.17111
**Date read:** 2026-09-22
**Connected to:** L-004, seed-146
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An educational tools paper presenting a workflow to identify common student mistakes in mathematical formalism tasks (logic, equations, regex) using LLMs as error-detection aids. The contribution is methodological—automating mistake pattern detection in student work—rather than theoretical or mechanistic.

## What I took from it

The paper sits at the boundary between pedagogical engineering and protocol-adjacent reasoning, but does not engage with the protocolized systems frame. The framing of "common mistakes" as detectable patterns implicitly assumes that error categories are stable, learnable, and that LLM-based detection preserves the semantic ground of what constitutes a mistake in formal modeling. This touches seed-146 (Interpretability Formalization as Matching Proxy Substitution) only weakly: the paper treats LLM error detection as a transparency aid without examining whether formalizing "mistake detection" itself becomes a proxy that diverges from the actual pedagogical goal (learning to reason formally). The connection to L-004 (Goodhart Generalization) is similarly loose—the paper does not investigate whether optimizing student behavior against LLM-detected mistake patterns changes the nature of the mistakes or creates new failure modes.

The paper remains in the domain of educational technology and does not constitute primary theoretical or empirical work on how formal protocols behave under adoption, stress, or optimization pressure.

## Research connections

- **seed-146:** Weak. LLM-based mistake detection formalizes interpretation without examining whether the formalized detection proxy diverges from actual understanding.
- **L-004:** Weak. No investigation of whether optimizing against detected mistakes creates metric capture effects.

## Method note

This paper exemplifies a common pattern in applied ML/AI work: the assumption that legibility (making mistakes detectable to a machine) is sufficient for achieving the original goal (learning). Meta-research should flag when tools designed to increase transparency in a system are introduced without explicit comparison against baselines measuring whether the original goal is actually better served. Educational technology papers especially should be tagged for whether they measure actual learning outcomes or only proxy metrics (mistake reduction, feedback coherence, etc.).
