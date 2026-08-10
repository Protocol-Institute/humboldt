# The Asymmetric Effects of Knowledge Distillation on Bias in Small Language Models

**Source:** cs.CY updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.28639
**Date:** 2026-08-03
**Relevance:** Directly addresses bias and fairness properties in language models, relevant to understanding robustness and safety of smaller LLMs.

## Summary

arXiv:2607.28639v1 Announce Type: cross 
Abstract: We show that knowledge distillation in small instruction-tuned language models has asymmetric effects on bias. On unambiguous tasks (BBQ-disambig), response-based distillation from a Gemma-2-9B teacher improves context-following: for the most biased baseline (SmolLM2-1.7B-Instruct), it cuts the context-overriding error rate from 44% to 24%. On ambiguous tasks (BBQ-ambig), the same distillation destroys per-item refusal calibration: 15% of items where the baseline correctly abstained instead receive stereotype answers, even when overall refusal
