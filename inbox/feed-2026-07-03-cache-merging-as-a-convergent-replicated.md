# Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.01308
**Date:** 2026-07-03
**Relevance:** Cache merging mechanisms that establish convergent replicated state across agents directly instantiate CL-002 (coordination overhead reduction through shared representational substrates) and CL-003 (trust requirements when delegating to composite agents).

## Summary

arXiv:2607.01308v1 Announce Type: new 
Abstract: Multi-agent latent reasoning composes agents' KV-caches into one context for a final agent. Prior work (Agent Primitives) does this by concatenating caches along the sequence axis with RoPE re-encoding, which we call BagMerge. BagMerge is non-commutative, and the best input ordering is unpredictable, shifting with the regime, the latent-step budget, and the model scale. We make this exchange a convergent replicated state. First, CanonicalMerge fixes the layout by content: ordering caches by mean K-norm at a middle layer renders the merged cache 
