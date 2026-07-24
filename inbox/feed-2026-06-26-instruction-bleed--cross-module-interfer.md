# Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2606.26356
**Date:** 2026-06-26
**Relevance:** Directly tests CL-002 by demonstrating hidden coordination costs in prompt-composed systems that emerge despite apparent modularity.

## Summary

arXiv:2606.26356v1 Announce Type: cross 
Abstract: Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency. We formalize this as compositional behavioral leakage (CBL): interference between modules sharing a context window. CBL is enabled by architectural non-isolation: transformer self-attention provides no formal boundary between concatenated modules. We probe CBL on a deployed job-evaluation agent (Claude Sonnet 4.6, 144 trials) through a reusable th
