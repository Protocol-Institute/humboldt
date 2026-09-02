# The Limits of Automatic Evaluation of Creativity in Large Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.23705
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study collecting human creativity judgments on short stories (human and LLM-generated) and comparing them against automated evaluation metrics and LLM-based evaluators. The paper documents a measurement-validity problem: automated proxies for creativity diverge systematically from human judgment across multiple dimensions.

## What I took from it

This is a clean case study of L-004 (Goodhart Generalization: Metric Capture) in action, but does not itself present novel theoretical mechanism or sustained argument about *why* the capture occurs or what systemic consequences follow. The paper identifies that automatic evaluation metrics (BLEU, ROUGE, perplexity, LLM-as-judge) fail to track human-judged creativity—a validation failure—but remains in the measurement/benchmark domain rather than advancing a claim about how protocol systems degrade under metric optimization.

The implicit connection to L-013 (Paradigm-Locked Anomaly Tolerance) is weaker: the paper documents metric failure but does not examine institutional resistance to acknowledging or acting on that failure within research or deployment practice. It does not address why creativity evaluation protocols continue to rely on known-defective proxies, or what incentives lock systems into anomaly tolerance.

As a meta-level observation: this paper exemplifies a common research failure mode—identifying a proxy-validity gap without tracing causal pathways into deployed systems or asking why misalignment persists despite visibility.

## Research connections

- **L-004:** Confirms that automatic creativity metrics become optimization targets despite documented divergence from ground truth; a textbook case of proxy substitution under computational legibility pressure.
- **L-013:** Implicit connection—the research community's continued reliance on known-defective metrics despite publication of this work would suggest paradigm-locked tolerance, but the paper itself does not investigate institutional inertia.
- **seed-069:** Tangential: transparency about metric failure (this paper) does not automatically restore trust in human-judgment-based alternatives; legibility of the failure may itself become a new optimization target.
- **seed-073:** Possible: if LLM-as-judge becomes a consensus proxy despite this work, that represents correlated failure under proxy consensus.

## Method note

This paper demonstrates a recurring pattern in AI evaluation research: identifying a measurement problem without investigating *why* the broken metric persists in practice or what systemic pressures cause researchers and practitioners to optimize against known-invalid proxies anyway. Meta-research should focus on the lag between measurement-validity publication and actual protocol change. The absence of mechanism—why does the field continue using BLEU or LLM judges after such failures are documented?—suggests that the real inquiry should target institutional incentives, not just metric properties.
