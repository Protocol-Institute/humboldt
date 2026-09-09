# Same Facts, Different Updates: Inference Setup Shapes LLM Behavior in Medical Allocation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.18108
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Demonstrates a mechanism absent from inventory — decision-protocol behavior variance induced by inference-sequence framing rather than model weights or training data, suggesting intervention-layer displacement operates through *temporal legibility architecture* rather than just proxy capture.

## What this is

Empirical study showing that LLM allocation decisions in medical resource scenarios depend critically on the order and framing of information presentation during inference, not just on input facts or model bias. Same clinical data produces different allocation probabilities based on whether additional context arrives as update versus initial framing — a context-dependent, inference-time phenomenon orthogonal to traditional model bias axes.

## What I took from it

This is direct evidence that L-012 (Intervention-Layer Displacement) operates at the *inference architecture* level, not just at training or prompt-engineering layers. The mechanism is not model capture of a proxy metric, but rather how the sequential legibility structure of the decision context shapes the generative model's belief updating under deployment. The paper suggests that medical allocation decisions aren't determined by what facts the model "knows," but by *when and how those facts enter the inference sequence*. This implicates a deeper phenomenon: when decision protocols rely on autoregressive or sequential-update systems (LLMs), the locus of optimization pressure and artifact creation shifts to whoever controls the *ordering and framing of information arrival*. This is not Goodhart capture — it's structural: the decision-making surface becomes sensitive to inference choreography. The finding generalizes beyond medical allocation: any protocol using sequential decision systems becomes vulnerable to what we might call "inference-sequence gaming" — the optimization of when facts are presented rather than which facts are true.

## Research connections

- **L-004:** The paper does *not* show metric capture in the classical sense; instead, it shows that the decision system's behavior depends on legibility *architecture* (sequence order) rather than measurable proxy optimization.
- **L-012:** Direct support — the decision protocol's effective optimization target shifts to whichever agent controls inference-sequence framing; intervention locus is displaced to the *presentation layer*, not model parameters or data.
- **seed-063:** Latent-state coupling — the model's internal state after each update step couples to the next decision output; inference history acts as silent protocol state.
- **seed-072:** Explanation-Marker Decoupling — the "same facts" produce different outputs, suggesting the model's explanation of its decision diverges from the decision itself depending on sequence.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry — information arrival order is an upstream asymmetry; the downstream decision collapses to whoever controls that order.

## Seed

**Seed title:** Inference-Sequence Choreography as Decision Surface
**Seed type:** mechanism
**Seed text:** In decision protocols implemented via autoregressive or sequential-update systems, the temporal structure and ordering of information legibility during inference becomes a primary optimization target independent of the underlying facts or model weights. When the same factual content produces different decisions based on presentation sequence, the effective decision function is not over facts but over *legibility choreography*. This generalizes beyond LLMs to any protocol where decision output depends on accumulated state from sequential information arrival: the protocol's vulnerability shifts from data quality to *inference-sequence control*. The implications: safety interventions, fairness audits, and oversight mechanisms designed to operate at the data or model layer may be orthogonal to the actual decision-shaping surface.
