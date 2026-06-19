# Deep-Read Verdicts

*Post-hoc judgment for each short-paper deep read. Training data for escalation calibration.*

**Verdict codes:** `accurate` / `over-claimed` / `under-claimed`

Each entry records:
- **(a) Escalation accuracy** — did the shallow annotation's claim match what the paper actually argued?
- **(b) What deep reading added** — what the full paper yielded beyond the shallow note
- **(c) Training signal** — the pattern to carry forward: "escalate when ___; don't when ___"

Over time, patterns in the `over-claimed` entries reveal systematic biases in the escalation criteria.

---

## arxiv-2402.08128

# Assessment of Escalation Decision

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper "introduces a genuine mechanism (simulation-induced uncertainty as cooperation device) absent from current inventory" and "directly targets AI-specific strategic dynamics."

The paper does exactly this. The core contribution is showing that recursive joint simulation — where agents run mutual simulations that themselves contain simulations, with calibrated refusal probability — creates *self-locating uncertainty* that makes agents unable to distinguish simulation from reality. This uncertainty structure is then shown to be mathematically isomorphic to infinite repetition, thereby enabling folk-theorem cooperation. This is not a standard game-theoretic mechanism; it relies specifically on the transparency and executability of AI code, making it genuinely AI-specific. The escalation annotation correctly identified the novelty and scope.

The annotation's claim held up under deep reading. No overstating; no underclaiming.

**(b) What deep reading added**

The deep read revealed the paper's true conceptual weight: the core insight is not merely that cooperation becomes possible (folk theorems already showed that for repeated games), but that *recursive joint simulation and infinitely repeated games are the same mathematical object viewed from opposite directions*. This isomorphism — Lemma 2 and Lemma 3 building toward Theorem 1 — is the paper's genuine contribution. The shallow annotation captured the mechanism but could not have discovered the equivalence structure without reading the formal argument. Additionally, deep reading showed serious engagement with the practical objection (Section 6): the authors acknowledge that indistinguishability is environment-dependent and flag this as open, rather than claiming universal applicability.

**(c) Training signal**

**Escalate when:** A paper makes a claim about a mechanism that (a) is specific to code-transparent multi-agent systems or AI-specific epistemic conditions, (b) invokes self-locating uncertainty or self-reference in a novel way, and (c) connects to established theory (here: folk theorems) in a way that requires formal argument to verify. Shallow notes mentioning "new mechanism" + "AI-specific" + "cooperation" are reliable flags for mathematical depth worth checking.

**Don't escalate when:** Papers claim mechanisms for AI cooperation that are actually just restatements of existing game-theoretic results (repeated games, correlation devices, commitment) under new names, or make AI-specific claims without showing why the mechanism wouldn't also work (perhaps more simply) for non-transparent agents. The shallow/deep boundary here is: does the paper prove a non-obvious mathematical equivalence, or just apply known theory?

---

## arxiv-2412.15707

# Assessment of Escalation Decision for arXiv-2412.15707

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper investigates "tacit collusion emergence" as a "primary theoretical source" and that the pattern "generalizes across algorithmic pricing systems" while "challenging competitive market assumptions."

The paper *does* deliver exactly this, but with a crucial inversion of the headline: rather than demonstrating that collusion emerges broadly, the paper's core theoretical contribution is showing that **most algorithms (mean-based class) converge to Nash equilibrium, not supra-competitive collusion**, while flagging UCB and Q-learning as narrow exceptions. The mechanism is real — the correlated rationalizable set as a convergence attractor — but the escalation's framing ("mechanism absent from inventory; pattern generalizes") undersells the paper's actual finding: the generalization is precisely that collusion risk *doesn't* generalize. The theoretical vocabulary (mean-based algorithms, CR set, competition constant δ) and formal apparatus (Propositions 9–11, Theorem 1) are genuinely novel to the learning-in-games literature. The annotation was accurate about novelty and mechanism, but reversed on reassurance direction — this is not a paper warning broadly of collusion, but moderately allaying that concern while isolating real hotspots (UCB, staggered entry).

**(b) What deep reading added**

Deep reading revealed the paper's true regulatory posture: a reassuring but precise narrowing of the collusion hazard, not a demonstration of its breadth. The shallow note missed the central argumentative move — the gap-filling in the learning-in-games hierarchy (CCE → CR → CE) — which is the real novelty and the reason the paper qualifies as a primary source. It also surfaced the staggered-entry finding and the non-negligible persistence of UCB collusion, which complicate the reassurance and show the authors' intellectual honesty about residual risk.

**(c) Training signal**

**Escalate when:** a paper claims to formalize a broad mechanism (collusion, coordination, non-competitive outcomes in a widespread system class) by introducing a new solution concept or algorithm-class property that partitions the design space into safe and unsafe regimes, supported by both formal proof and systematic simulation — especially if it inverts existing regulatory intuition by *narrowing* rather than broadening the risk.

**Don't escalate when:** an annotation claims a paper "generalizes across systems" or "challenges competitive assumptions" without first checking whether the generalization is assertive (collusion spreads) vs. reassuring (collusion is rare), or whether the mechanism is novel vs. a repackaging of existing learning-in-games results; also avoid escalating on mechanism claims alone if the paper's regulatory or predictive payload is already obvious from the abstract.

---

