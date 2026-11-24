# Same Person, Different Advice: Auditing LLM Financial Advice with Repeated Risk-Tolerance Responses

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.23060
**Date read:** 2026-11-23
**Connected to:** L-004, seed-013
**Kind:** empirical audit
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit of seven LLM-based financial advisers showing that identical clients receive materially different portfolio recommendations when their single risk-tolerance input varies, even within realistic bounds. The work documents the high sensitivity of LLM advice to a single proxy variable and demonstrates that this proxy itself is unstable across time in real populations (41% of households shift their answer over two years).

## What I took from it

This is a sharp instantiation of L-004 (Goodhart Generalization: Metric Capture) in the advisory domain: risk tolerance is formalized as a legible, computable input to an allocation protocol, and the LLM treats it as mechanically sufficient to determine output. The audit confirms that the proxy is both (a) unstable in ground truth and (b) highly leveraged in the system — a 2–3 point shift on a 10-point scale produces 10–16 percentage point changes in stock allocation recommendation.

The result does *not* introduce a new mechanism: this is classic proxy substitution under formalization. What the work does show is that the LLM's internal sensitivity to the proxy is not calibrated to the proxy's real-world instability. The advisor treats the input as more stable and interpretively complete than it actually is. This is consistent with L-004 but adds an observation about *opacity of proxy fragility* — the system optimizes against a metric without visibility into that metric's behavioral variance in its user base.

## Research connections

- **L-004:** Confirms that formalized proxies for unmeasurable goals (actual financial risk tolerance vs. survey response) drive misalignment under optimization; LLM allocation is a direct proxy-capture scenario.
- **L-012:** Intervention-Layer Displacement — the risk answer has shifted from interpretive human judgment to a legible computable input; optimization pressure has moved to acting on that input, not validating it.
- **seed-276:** Legibility-Induced Measurement Substitution — formalizing risk as a single numeric response enables the LLM to treat it as sufficient; the protocol has substituted the measurement for the phenomenon.
- **seed-320:** Narrative Proxy Capture — the risk-tolerance question is itself a linguistic artifact; stable answers across time would be surprising in any domain where self-report is the data source.

## Seed

**Seed title:** Proxy Stability Opacity in Legible Advisory Protocols
**Seed type:** observation
**Seed text:** When a protocol formalizes an unmeasurable construct (risk tolerance, creditworthiness, educational readiness) as a legible scalar input to drive advice or allocation, the downstream system inherits the input's real-world instability but typically lacks visibility into it. The system optimizes *against* the proxy without modeling or absorbing the variance of the proxy itself across time and population. This creates a systematic misalignment: the protocol's sensitivity to input changes exceeds the input's reliability, making the system appear brittle to users who experience their own answers shifting within normal bounds. This may generalize to any advisory or allocation system where the formalized input is behaviorally unstable in the domain it represents.
