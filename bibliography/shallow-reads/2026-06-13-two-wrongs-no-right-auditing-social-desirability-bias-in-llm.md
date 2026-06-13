# Two Wrongs, No Right: Auditing Social-Desirability Bias in LLM Annotators for Computational Social Science

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.12426
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit of social-desirability bias across three 7B instruction-tuned LLM models on text classification tasks (TweetEval), testing whether alignment-induced errors consistently skew in the same direction. The work finds that bias is *heterogeneous*: different models fail in opposite directions (leniency vs. over-labeling), undermining the assumption that a single directional correction suffices.

## What I took from it

This is a measurement-quality paper rather than a foundational one. It documents that LLM annotators exhibit *task-dependent and model-dependent* distortion patterns—Zephyr shows leniency bias (under-applies harmful labels), while others over-apply them across the same tasks. The key observation is that "two wrongs" (opposing biases in different models) produce divergent conclusions, making it unsafe to assume LLM annotators are interchangeable or that their errors can be globally corrected.

This is relevant to any research program using LLMs as measurement instruments, but it is a constraint-identification study, not a law. It shows *what fails* in proxying human annotation, but does not isolate a generalizable mechanism or present a sustained theoretical argument about protocolized system behavior. It's a tool-validation paper.

## Research connections

- none (no established laws or active hypotheses yet exist in this research agenda)

## Candidate laws or signals

**CL-LLM-Annotation-001:** Alignment-induced measurement bias in LLM annotators is heterogeneous and model-specific rather than directional; systems with different training objectives produce opposing classification errors on identical content, making ensemble or aggregation approaches unreliable without explicit per-model calibration.
