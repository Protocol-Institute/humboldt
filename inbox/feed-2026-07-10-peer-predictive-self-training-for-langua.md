# Peer-Predictive Self-Training for Language Model Reasoning

**Source:** cs.GT updates on arXiv.org
**URL:** https://arxiv.org/abs/2604.13356
**Date:** 2026-07-10
**Relevance:** PST's label-free self-improvement mechanism directly tests CL-002 (Coordination Cost Conservation)—whether peer prediction reduces supervision overhead while maintaining reasoning quality, a key coordination cost efficiency scenario.

## Summary

arXiv:2604.13356v3 Announce Type: replace-cross 
Abstract: Mechanisms for continued self-improvement of language models without external supervision remain an open challenge. We propose Peer-Predictive Self-Training (PST), a label-free fine-tuning framework in which multiple language models improve collaboratively by using a cross-model aggregate response as an internal training signal. Given a prompt, models generate responses sequentially; the final aggregated answer, which is often more reliable than individual responses in practice, serves as an internal reference for learning. We measure 
