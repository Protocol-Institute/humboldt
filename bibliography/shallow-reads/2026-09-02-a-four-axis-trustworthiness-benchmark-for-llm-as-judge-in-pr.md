# A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.14329
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** benchmark/evaluation framework
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper proposing four evaluation axes (accuracy, paraphrase robustness, adversarial robustness, calibration) for assessing LLM-as-judge systems deployed to enforce principle-based regulatory standards. The work uses UK FCA financial-promotion principles as a test case, creating 168 scenarios with adversarial and paraphrase perturbations to stress-test LLM compliance evaluation.

## What I took from it

This is a competent benchmarking effort identifying real failure modes in the operationalization of incommensurable evaluative standards (L-004 territory). The four axes correctly identify that naive accuracy is insufficient — paraphrase robustness and adversarial robustness map onto real attack surfaces in any computable enforcement regime (L-008 relevance).

However, the work does not theorize *why* these failure modes emerge from the formalization process itself, nor does it provide evidence that the benchmark predicts real-world capture dynamics or that the four axes are exhaustive. It treats the problem as a technical evaluation challenge rather than as a case of a deeper law about what happens when unmeasurable normative standards are rendered machine-enforceable. The benchmark may be useful for debugging specific LLM judges, but it does not generalize a mechanism or challenge existing law-shaped claims.

## Research connections

- **L-004 (Goodhart Generalization):** Confirms that principle-based standards ("fair, clear, not misleading") resist reduction to computable proxies; the four-axis framing is a symptom of metric fragility rather than a solution to it.
- **L-008 (Proxy Optimization Under Computable Enforcement):** Demonstrates that once LLM evaluation becomes formalized and legible, adversarial optimization becomes predictable; the benchmark catalogs failure modes but does not theorize the equilibrium condition.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**DECISION:** This is a well-scoped evaluation paper addressing a real problem in the automation of regulatory judgment, but it remains within the domain it studies. It does not propose or test a law-shaped regularity generalizing beyond LLM-as-judge contexts, does not introduce a mechanism absent from the inventory (L-004 and L-008 already capture the core dynamics), and does not provide evidence that would shift the evidentiary status of existing open lines. Store as shallow.
