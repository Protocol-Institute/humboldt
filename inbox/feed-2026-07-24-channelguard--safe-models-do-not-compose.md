# ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.19430
**Date:** 2026-07-24
**Relevance:** Directly validates CL-002 (Coordination Cost Conservation)—demonstrates that safety properties don't compose across agent boundaries, forcing explicit monitoring costs at each channel rather than relying on endpoint guarantees.

## Summary

arXiv:2607.19430v1 Announce Type: cross 
Abstract: Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary (IBProtector, Llama Guard, perplexity filters, SmoothLLM) or run outside the application as opaque, stochastic provider-side filters. We show this gap carries a consequence rarely measured: on a 2,100-trace evaluation across eight attack families, five defenses, and three model backends, an undefende
