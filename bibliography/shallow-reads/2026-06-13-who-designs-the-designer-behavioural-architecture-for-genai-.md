# Who Designs the Designer? Behavioural Architecture for GenAI in Education

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.12416
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper proposing "behavioural architecture" as a design framework for educational AI systems. The work critiques binary responses to AI in education (ban vs. content-tutoring) and argues that systems must be designed to adapt to learner personality, motivation, and emotional state rather than only optimize content sequencing. The paper includes a specific proposal: student co-authorship and revocability of system records about their learning profile.

## What I took from it

The work identifies a legitimate design gap in current educational AI—the behavioral/affective dimension has been instrumentalized (tracked for optimization) rather than made transparent and negotiable. The proposal to grant students revocability and co-authorship over their behavioral profile is interesting as a *control mechanism* for protocolized systems, though the paper does not theorize what happens when student preference contradicts system-inferred learning patterns.

This is relevant to understanding how artificial systems distribute agency and authority in feedback loops, but it remains normative and domain-specific. The claim that personality and motivation "shape learning outcomes as strongly as cognitive ability" is well-established in educational psychology and is not novel. The architectural move (transparency + revocability) is pragmatic but not theoretically grounded in a general principle about how protocolized systems should handle inscribed behavioral models.

## Research connections

- none (no established laws or active hypotheses currently defined in the research inventory)

## Candidate laws or signals

- **CL-EdAI-1:** Protocolized systems that model behavioral state must make that model readable and revisable by the subject, or risk opacity-driven divergence between system-inferred and self-reported state.
- **CL-Control-1:** Revocability of historical behavioral inference appears to be a candidate control lever in systems where model adaptation depends on path-dependent behavioral records.
