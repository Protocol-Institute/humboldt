# Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.12895
**Date read:** 2026-09-02
**Connected to:** L-013
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary empirical source demonstrating that a foundational assumption in compositional protocol verification (conditional independence) systematically fails in practice; reveals a paradigm-locked anomaly tolerance mechanism where mathematical formalisms licensing compositional bounds persist despite empirical falsification, directly instantiating L-013 and opening a new mechanism for how formalized protocols resist correction.

## What this is

This is an empirical evaluation paper testing a foundational assumption (conditional independence of component failures) that licenses compositional reliability bounds in multi-agent systems. The authors preregistered an evaluation of 18,000 deterministic missions and discovered that two instances of a single model co-fail on 90% of missions where either fails (phi = 0.916), demolishing the independence assumption—yet the mathematical framework relying on that assumption remains in use.

## What I took from it

This is a direct instantiation of **L-013 (Paradigm-Locked Anomaly Tolerance)**: the compositional reliability framework is an established protocol system with strong mathematical foundations; the paper provides sustained, preregistered, deterministic evidence that a core assumption is empirically false; and yet the framework persists in the research and engineering inventory without triggering a paradigm-level response. The mechanism is clear: the mathematical formalism (product of component reliabilities) is decoupled from the empirical falsifiability condition (independence testing). Engineers and researchers continue to apply compositional bounds because (a) the math is elegant and (b) testing independence is not part of the standard workflow—it exists outside the formalized protocol.

This also touches **L-004 (Goodhart Generalization)**: once "compositional reliability" becomes a measurable proxy for "actual system safety," the proxy itself becomes the optimization target, allowing systems to satisfy compositional bounds while failing catastrophically in correlated ways.

The deeper insight: **formalization itself creates conditions for anomaly tolerance**. By rendering reliability as a product formula, the protocol system becomes locally legible and mathematically closed—which makes it harder, not easier, to detect when the foundational assumption breaks. This is the inverse of what transparency advocates predict.

## Research connections

- **L-013:** Direct empirical instance. Established protocol system (compositional reliability bounds) tolerating sustained, preregistered evidence of foundational assumption failure. Formal mathematical closure insulates the system from correction.
- **L-004:** Compositional reliability bounds become measurable proxy for safety; optimization toward the proxy (satisfying the formula) diverges from the unmeasurable goal (actual safety).
- **seed-062 (Formalization Opacity Collapse):** Formalizing reliability as a product formula paradoxically reduces visibility into the conditions under which that formalism applies.
- **seed-073 (Correlated Failure Under Proxy Consensus):** The paper directly documents correlated failure under a consensus-licensed proxy (the independence assumption).
- **L-005 (Gall Generalization):** The compositional framework functions correctly *as a mathematical system*; replacing it requires evolving it, not discarding it—hence the persistence despite empirical falsification.

## Seed

**Seed title:** Formalized Independence as Invisible Assumption Lock

**Seed type:** observation + mechanism

**Seed text:** In protocol systems where reliability or safety is formalized through a compositional mathematical framework (products, conditional independence, layer separation), the foundational assumptions of that framework become invisible to optimization and verification procedures that operate within the formalism. When those assumptions are empirically falsified, the system exhibits high tolerance for the anomaly because: (1) testing the assumption is not part of the protocol's legible workflow; (2) the formalism itself is mathematically self-contained and does not require external validation; (3) departure from the framework carries switching costs. This suggests that formalization creates anomaly insulation proportional to the elegance and closure of the mathematical system. The mechanism generalizes to any protocol where assumptions are baked into the formalism rather than surfaced as testable conditions.
