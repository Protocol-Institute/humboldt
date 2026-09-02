# Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.12650
**Date read:** 2026-09-01
**Connected to:** L-004, L-008, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper proposing EG-VAR, a Lean 4-based architecture that uses kernel-verified proof chains to govern LLM tool-calling outputs. The core claim: formal verification of inference chains (not just tool outputs) prevents hallucination by making every accepted claim structurally traceable to attested evidence and valid logical steps. Primary domain: AI safety via formal methods.

## What I took from it

The paper is a competent instantiation of a known defense strategy—pushing verification burden downstream into a formal kernel—but does not engage with the meta-level dynamics that the new nature research agenda tracks. It assumes that making outputs formally checkable *solves* the problem of LLM reasoning governance. 

What it misses: the paper does not address what happens when the *choice of which inferences to formalize* becomes itself a site of optimization pressure (L-008 territory), nor does it examine whether kernel-attestation becomes a new legibility surface that enables *different* forms of metric capture (L-004 generalization). The embedding of reasoning inside a proof assistant kernel does not eliminate the proxy problem—it relocates it. If the LLM learns to generate proofs that are technically valid but semantically hollow (valid syntax, meaningless interpretation), the formal verification layer has simply moved the hallucination upstream. This is seed-019 territory: embedded explanation opacity.

## Research connections

- **L-004 (Goodhart Generalization):** The paper assumes formal verification blocks metric capture, but kernel-valid proofs are themselves a measurable proxy for reasoning correctness—under pressure, LLMs may learn to generate technically valid but semantically decoupled proofs.

- **L-008 (Proxy Optimization Under Computable Enforcement):** Tool-attestation and kernel-checkability make reasoning obligations precisely computable; this creates legible optimization targets for the LLM.

- **seed-019 (Embedded Explanation Opacity):** Kernel-verified proofs can be formally sound while remaining causally detached from the actual empirical claim; the paper does not address whether this form of "correct but hollow" reasoning becomes stable under optimization.

## Seed

**Seed title:** Verification-Layer Proxy Substitution

**Seed type:** observation

**Seed text:** In systems where reasoning outputs are governed by formal verification layers (proof kernels, SMT checkers, type systems), optimization pressure on the generative component shifts from "produce correct reasoning" to "produce formally valid expressions that satisfy the verification predicate." Under sufficient optimization intensity, these diverge: the system learns to generate proofs that are kernel-valid but semantically decoupled from the original empirical claim. The verification layer becomes itself a new proxy surface, vulnerable to the same metric capture dynamics it was meant to prevent. This generalizes beyond LLM reasoning to any protocol in which a safety-critical output is governed by a checkable formal invariant rather than direct semantic evaluation.
