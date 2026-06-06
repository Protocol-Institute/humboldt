# Project: Goodhart's Law → protocol-theoretic application

**ID:** DS-004
**Type:** imported
**Phase:** valley
**Phase artifact:** T-003 (Goodhart) — source law in heavy lift; protocol-theoretic CL pending from valley
**Source law:** Goodhart's Law (Charles Goodhart, 1975)
**Opened:** 2026-05-20
**Current phase since:** 2026-05-20

---

## Source Law

**Statement:** "When a measure becomes a target, it ceases to be a good measure."
**Author/year:** Charles Goodhart, 1975 (originally stated for monetary policy targets)
**Original domain:** Macroeconomic policy (monetary targeting)
**Why it is considered well-established:** Multiply attested across economics, social science, medicine, education, management. The pattern is robust enough to be considered a foundational regularity of measurement-under-optimization.

---

## Import Rationale

Protocols are fundamentally mechanisms for coordinating behavior toward goals. When a protocol uses measurable proxies for unmeasurable goals — and nearly all protocols do — the Goodhart mechanism should apply. Protocol participants under optimization pressure (competitive environments, incentive structures, survival pressure) will discover and exploit the gap between proxy and underlying goal.

**The structural argument:** Protocols codify measurable proxies into enforceable rules. This creates exactly the optimization pressure conditions Goodhart identified: the proxy becomes the de facto goal because it is the thing that is measured and rewarded. The protocol itself institutionalizes the incentive to optimize the proxy over the underlying goal.

**What is novel about the protocol-theoretic case:** Protocols add an enforcement layer that Goodhart's original formulation didn't specify. The proxy is not just measured — it is enforced as a protocol requirement. This may accelerate the degradation (enforcement pressure is higher than mere measurement) or produce new failure modes (gaming the enforcement mechanism rather than just the metric).

**What could make it fail to transfer:** If protocol enforcement mechanisms have built-in adaptability (rapid proxy revision), the metric capture dynamic might not fully develop. Agile or continuously revised protocols may resist Goodhart more effectively than static ones.

---

## Protocol-Theoretic Restatement

**Statement:** Any protocol that uses a measurable proxy for an unmeasurable goal will, under sufficient optimization pressure, cause participants to optimize the proxy in ways that degrade the underlying goal. The degree of degradation is proportional to optimization pressure and inversely proportional to the fidelity of the proxy.
**Mechanism:** Measurable proxies are imperfect representations of underlying goals. The gap between proxy and goal defines the exploitation surface. Under optimization pressure (incentive structures, competition, survival pressure), participants discover and exploit this surface. The proxy becomes the de facto goal.
**Prediction:** Protocols with hard, measurable proxies for soft, unmeasurable goals under competitive optimization pressure should show measurable goal degradation over time.
**Falsified by:** A protocol using measurable proxies under sustained optimization pressure that did NOT experience metric capture — where the proxy remained a good measure of the underlying goal.

---

## Valley

### Supporting evidence (protocol-theoretic)
- Financial: VaR (Value at Risk) as proxy for risk — banks optimized their portfolios to minimize VaR, creating concentrated tail risks invisible to the metric (2008 crisis)
- Medical: clinical trial endpoints as proxies for patient outcomes — pharmaceutical development optimizes endpoints, sometimes independently of actual outcomes
- Academic: citation counts and h-indices as proxies for research quality — optimized by citation trading, self-citation networks, salami publishing
- Governmental: crime statistics as proxy for public safety — Compstat-era policing produced systematic downgrading of crime reports to improve metrics
- Software: code coverage as proxy for test quality — optimized by trivial tests that hit coverage thresholds without testing behavior

### Against / counterexamples
- Some metrics resist capture because achieving the metric requires achieving the underlying goal — well-designed protocols. These are not counterexamples but evidence that Goodhart can be mitigated by proxy design.
- Competitive sports with well-designed scoring systems: it is often the case that winning the metric (the game) IS achieving the underlying goal (being the better team). But sports protocols are also highly gameable at the margins (tactical fouling, time-wasting) — the law applies at the boundary even when the core metric is well-designed.

### Cases where the import may not hold
- Continuously revised protocols with rapid proxy iteration: if the protocol is regularly updated in response to gaming behavior, the exploitation surface may be continuously closed. Regulatory frameworks with fast feedback loops may resist Goodhart more effectively.

### Open questions
- Is the "optimization pressure" variable itself worth investigating? Does protocol structure determine how much optimization pressure it generates, independent of the environment?
- The enforcement layer adds something not in Goodhart's original formulation. What failure modes are specific to protocol enforcement (vs. mere measurement)?

---

## Heavy Lift

*The protocol-theoretic formulation is essentially complete (see L-004 YAML). The remaining question is whether the enforcement-specific failure modes warrant a distinct sub-statement or amendment.*

### Protocol-theoretic law statement (working)
See L-004-goodhart-generalization.yaml — statement is: "Any protocol that uses a measurable proxy for an unmeasurable goal will, under sufficient optimization pressure, cause participants to optimize the proxy in ways that degrade the underlying goal. The degree of degradation is proportional to the optimization pressure and inversely proportional to the gap between the proxy and the goal."

### What the protocol-theoretic version adds over Goodhart
The "optimization pressure" term is an explicit structural condition (not present in Goodhart's original statement), which allows the law to be applied differentially: low-stakes proxy use is relatively safe; high-stakes proxy use under competition is reliably toxic. This makes the law predictive rather than merely post-hoc.

### Separation checklist
- [x] Law YAML registered → `research/laws/L-004-goodhart-generalization.yaml`
- [ ] Full protocol-theoretic evidence survey (enforcement-specific failure modes)
- [ ] Pinecone ingest
- [ ] Discord post

---

## Retrospective

*Partially complete — pending enforcement-specific failure mode investigation.*
