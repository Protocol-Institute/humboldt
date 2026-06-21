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

## arxiv-2508.11874

# ASSESSMENT: arxiv-2508.11874

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "demonstrates a sustained mechanism for artificial systems to discover and certify non-trivial algorithmic solutions in a formal domain, introducing automated proof synthesis as a generative capability absent from current inventory and suggesting a pattern of LLM-guided algorithm design with formal verification"

**Assessment:** The paper delivers exactly this. LegoNE is a complete LLM-in-the-loop system that:
- **Certifies** algorithms automatically via the instantiation/forgetting reduction (a genuine methodological contribution to automated proof synthesis)
- **Discovers** two-player and three-player Nash equilibrium algorithms that rediscover or improve on decades of human research
- **Scales** the discovery loop: the three-player discovery breaks the *only previously known paradigm* (extension technique), proving structural novelty, not parameter tuning

The novelty claim is sound: prior work (AlphaGeometry, FunSearch) had evaluators; LegoNE *constructs* a formal evaluator from algorithmic structure. The annotation's framing as "absent from current inventory" is precise — no prior system had automated proof synthesis for this class of problems.

**No mismatch.** The shallow annotation was conservative but accurate; it did not overstate.

---

## (b) What deep reading added

The deep read revealed the *conceptual spine* the shallow note could not: the paper's core insight is solving an infinite-dimensional proof obligation through two formally specifiable reductions (instantiation of quantifiers to only algorithm-generated strategies; forgetting of functional structure). This is not just "LLM-guided search with verification" — it's a reduction from undecidable proof space to finite-dimensional optimization. The shallow note was sufficient for triage, but it obscured what makes this mechanically novel: the instantiation/forgetting framework is reusable and domain-general in principle, even though the paper only demonstrates it on Nash equilibrium algorithms.

---

## (c) Training signal

**Escalate when:** A paper claims an automated proof or discovery method and provides both (i) a formal reduction that makes the proof obligation finite, (ii) empirical validation on known results before discovery claims, and (iii) a worked example showing structural novelty in discovered outputs (not just parameter improvement).

**Don't escalate when:** A paper describes LLM-guided search with post-hoc verification without a characterization of what the verifier computes, or when discovery results are marginal improvements within a single paradigm rather than breakouts into new design spaces.

---

## arxiv-2512.07526

# Assessment: arxiv-2512.07526

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper identifies "a novel mechanism (risk cancellation in shared catastrophe games) absent from current inventory" and demonstrates generalization to "AGI deployment dynamics."

The deep read confirms this precisely. The cancellation effect is genuinely novel within the preemption game literature—the paper proves that when catastrophic downside appears symmetrically in all players' payoff functions, the ruin term D cancels algebraically from the equilibrium indifference condition (Eq. 5, p.3/16), rendering it invisible to race timing. This is not a behavioral insight or a calibration; it is a structural property of the game form itself.

The mechanism directly generalizes: it applies wherever prizes are privatized and ruin is socialized—AGI, autonomous weapons, gain-of-function research, space weaponization. The paper is explicit about this (p.27–34) and derives the conditions under which the cancellation breaks (private liability, prize-sharing).

The escalation annotation's framing was sound. It correctly identified that this is a *primary theoretical source* (the cancellation effect is proven, not synthesized) and that it fills an inventory gap (the preemption game literature, from Weeds 2002 onward, does not contain this result).

## (b) What deep reading added

The deep read revealed the **algebraic and game-theoretic precision** of the mechanism that shallow annotation could only gesture toward. Specifically: (i) the explicit two-threshold structure (V*_P vs. V*_S), where the *suicide region widens as D grows*—the exact counterintuitive inversion of the intuitive expectation; (ii) the saviour's trap formalization, showing how asymmetric beliefs amplify preemption incentives in direct proportion to perceived catastrophe; (iii) the nested thresholds (V*_P < V*_S < V*_social) that quantify the competitive-versus-social gap; (iv) the mechanism repair conditions (Dprivate = 2D, prize-sharing thresholds S*), which are concrete and testable. The shallow annotation could not have extracted these without full engagement with the mathematical derivations and the three-part proof structure (pages 15–25).

## (c) Training signal

**Escalate when:** A paper claims to have proven a structural algebraic property in a game-theoretic model where the property contradicts intuitive expectations, generalizes across multiple policy domains, and is not present in cited prior work—*and the claim is specifically about the *non-dependence* of equilibrium outcomes on a parameter that is conventionally assumed to drive them.*

**Don't escalate when:** A paper identifies a mechanism in an existing game-theoretic framework (e.g., adding a new player type, a new information structure, or a novel safety intervention) but the mechanism is additive (increases an incentive term) rather than subtractive (causes cancellation), or when the paper's own limits section acknowledges the mechanism applies only under stringent symmetry assumptions without proof that real domains satisfy those assumptions.

---

## arxiv-2601.01279

# ESCALATION ACCURACY ASSESSMENT

**(a) Escalation accuracy** — `accurate`

The escalation annotation claimed the paper "demonstrat[es] a mechanism (emergent collusion via shared model architecture and feedback aggregation) absent from current inventory." The paper does exactly this. Specifically:
- It proves that when competing sellers use a shared AI model with (i) near-deterministic output (high fidelity ρ) and (ii) retraining on aggregated seller feedback, a phase transition occurs above a critical fidelity threshold ρ_c, past which supracompetitive pricing becomes a stable attractor (Propositions 2–4).
- Critically, this occurs *without intent, communication, or overt coordination* — purely through structural properties of shared infrastructure + performance-driven updating.
- The annotation's claim of "generalization potential beyond pricing to any multi-agent system using shared learned models" is credible given the formal structure (any domain where feedback aggregation retrains a shared decision model).

No significant mismatch. The shallow read identified the right mechanism and its novelty correctly.

---

**(b) What deep reading added**

Deep reading revealed the *mathematical specificity* that justifies the escalation: the bifurcation structure (Proposition 2, critical threshold ρ_c), the exponential concentration bounds on equilibrium selection (Proposition 4), and the phase diagram showing that "responsible" configurations (high fidelity, large batches) are precisely what triggers collusion. The shallow note captured the core claim; deep reading showed the mechanism is not merely plausible but mathematically sharp — a genuine phase transition with measurable thresholds, not a vague emergent behavior.

---

**(c) Training signal**

"Escalate when: A shallow note claims a novel *mechanism* (not just a risk or empirical observation) with a formal structure that could support a mathematical proof or tight characterization, especially if the mechanism spans a class of systems (here: any multi-agent learning system with shared infrastructure)."

"Don't escalate when: A shallow note invokes emergent collusion or unintended coordination as a conceptual warning without identifying a specific, reproducible mechanism — or when the mechanism is already well-known (e.g., 'competing agents with aligned incentives coordinate') and the paper only instantiates it in a new domain."

---

## arxiv-2602.22041

# Assessment: arxiv-2602.22041

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper "introduces a mechanism (group-level action-space reduction) for assigning causal responsibility under overdeterminism—a foundational problem absent from current inventory."

The deep read confirms this was the right call. The paper does introduce gFeAR (group Feasible Action-Space Reduction) as a formal mechanism for handling causal overdetermination—the case where no individual agent suffices to constrain an effect, but some coalition does. This is genuinely absent from standard causal responsibility frameworks (which typically assign zero responsibility to each agent in such cases, creating a "responsibility gap"). The tiering algorithm and the taxonomy of influence types (solo, mediated, coupled, mediated-coupled) are novel operationalizations that extend beyond the dyadic case.

The claim that it "generalizes beyond spatial interaction domains" is partially supported: the conceptual machinery is domain-agnostic (counterfactual action-space, minimality, tiering), though the paper only demonstrates it in grid-world spatial interactions. The secondary application (emergence detection via Kendall's τ variance) hints at broader scope but remains speculative.

No mismatch detected. The annotation's core claim is accurate and substantive.

---

## (b) What deep reading added

The shallow note captured the mechanism correctly but missed the conceptual taxonomy and rigor of the solution. Deep reading revealed three things the annotation couldn't convey: (1) the *structure* of the tiering algorithm—that it operationalizes causal priority by distinguishing mediated from direct influence, not just summing group effects; (2) the empirical validation strategy (Kendall's τ agreement between gFeAR-Tier and gFeAR-Shapley), which shows the framework is robust to ranking method; (3) the secondary emergence-detection application, which suggests the framework could serve as a complexity metric in agent-based models. The shallow note was sufficient for escalation merit, but deep reading showed this is a more technically mature and potentially multi-purpose contribution than a one-line summary allows.

---

## (c) Training signal

**Escalate when:** The annotation identifies a *specific, named problem* (overdeterminism, responsibility gap) that the paper claims to solve via a *formal mechanism* (group-level metric), and the problem is explicitly absent from the framing literature—this is a high-confidence signal that the paper has novelty and depth worth verifying.

**Don't escalate when:** The annotation invokes "generalizes beyond domain X" without the paper demonstrating that generalization (or at least sketching a clear path to it), and the validation is limited to toy scenarios with no ablation or robustness testing—this pattern suggests the mechanism may be domain-specific or fragile despite broad claims.

---

## arxiv-2603.25979

# ESCALATION ACCURACY ASSESSMENT

**(a) Escalation accuracy: `accurate`**

**Quoted escalation claim:**
> "A game-theoretic paper advocating Colonel Blotto games as a richer analytical framework than Prisoner's Dilemma for modeling adversarial resource allocation in control systems, cybersecurity, and infrastructure protection."

**Assessment:**
The escalation annotation's characterization is accurate. The paper does exactly what was claimed: it advocates for Colonel Blotto as a superior analytical framework to PD for the control systems community, with explicit applications to SCADA, cybersecurity, and critical infrastructure. The shallow read correctly identified the core positioning and intent. No material mismatch between annotation and content.

---

**(b) What deep reading added**

The shallow annotation captured the thesis but missed the paper's actual technical payload: the independence results in General Lotto (equilibrium payoffs depend only on budget ratio, not contest count); the three specific extension theorems (weakest-link scaling law, favoritism analysis showing pre-deployed resources are information-costly, coalitional games with the counterintuitive result that resource *transfers* between allies can benefit both while resource *concessions* cannot). Deep reading revealed that this is not purely a framework-advocacy paper but contains concrete structural theorems with direct engineering implications—particularly the linear scaling law for networked vulnerabilities and the inversion of intuition around what kinds of concessions help in multi-agent contests.

---

**(c) Training signal**

**Escalate when:** A game-theoretic or mechanism-design paper from the controls/cybersecurity domain claims a classical framework (Blotto, auction theory, differential games) has concrete novel theorems or negative results (impossibility, scaling laws, counterintuitive orderings) that differ from the textbook case, even if the paper frames itself as pedagogical.

**Don't escalate when:** A paper claiming a "richer framework than PD" is purely conceptual repositioning without new structural results, formal theorems with stated proofs, or quantitative scaling laws — i.e., when the depth is only in motivation, not mathematics.

---

## arxiv-2604.04193

# Assessment: arxiv-2604.04193

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "execution parallelism introduces a fundamental mechanism failure in fee mechanisms—adversarial padding becomes rational when fees respond to parallelism—which is absent from current protocol design inventory and likely generalizes beyond blockchain."

**Assessment:** The paper delivers exactly this. The deep read confirms:

1. **Fundamental mechanism failure** (not design oversight): Theorems 1–2 establish that risk tradeoffs are *structural impossibilities* rooted in P-completeness, not fixable by clever mechanism design.

2. **Adversarial padding / shill attacks** explicitly analyzed: Section 6–7 prove that mechanisms attempting to price parallelism correctly simultaneously become shill-vulnerable (Lemma 3: scheduler shill-proofness and efficiency are incompatible).

3. **Absent from current inventory**: The paper positions itself against EIP-1559 and prior gas-mechanism work, showing those mechanisms do not address contingent objects or the risk/shill interaction.

4. **Generalization beyond blockchain**: The framing in Section 1 and conclusion (p.18) explicitly positions this as a problem for "any resource-metered system with parallel execution" — MapReduce, cloud schedulers, etc.

The shallow annotation slightly underspecified the mechanism (it names "adversarial padding" but the paper's core contribution is the *impossibility tradeoff* between user risk and scheduler shill-proofness), but did not overstate. The escalation was warranted.

---

## (b) What deep reading added

The shallow note missed the paper's most load-bearing result: **the P-completeness foundation** (Theorem 2), which elevates the risk tradeoff from a game-theoretic observation to a computational-complexity statement. This explains *why* no efficient shortcut exists and places the problem in the same category as other Turing-complete intractability results. Additionally, the deep read uncovered the **incompatibility between shill-proofness and efficiency** (Lemma 3), which is the mechanism-level closure: any attempt to fix the risk tradeoff by pricing parallelism correctly opens a new, orthogonal vulnerability. The shallow note gestured at padding/adversarial incentives but did not surface that this is a *provable incompatibility*, not a clever attack.

---

## (c) Training signal

**Escalate when:** the annotation claims a new *impossibility result* or *fundamental tradeoff* (not just an attack or design flaw), especially if rooted in complexity theory, and the authors prove it with named theorems and counterexamples that show why prior mechanisms fail — this signals primary theory contribution worth verifying in full.

**Don't escalate when:** the annotation claims a mechanism is "absent from current design inventory" but the shallow read shows only that the mechanism was not the primary focus of prior work (as opposed to provably impossible), or when the generalization claim (blockchain → beyond) is stated without formal grounding in the paper's theorems.

---

## arxiv-2604.07821

# ESCALATION ASSESSMENT

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper presents "a primary source with sustained empirical argument on multi-agent coordination failure in a regime (zero-cost helping under explicit instruction) where cooperation should be trivial" and introduces "capability-cooperation decoupling absent from current inventory."

The paper delivers exactly this. The environment is maximally stripped down: zero-cost helping, explicit group-welfare instructions, no strategic complexity. The core finding—that o3 (high capability) achieves 17% of optimal while o3-mini achieves 50% (R²=0.025 across 8 models)—is a genuine inversion of the expected capability-cooperation relationship. The methodological contribution (causal decomposition via automated requesting/fulfillment) cleanly separates cooperation failures from competence failures. The instruction-utility gap is a novel concept not present in the shallow inventory of coordination failures. The annotation's claim is not overstated; the paper substantiates it across 45 runs, 8 models, and 8,807 reasoning traces.

**(b) What deep reading added**

The deep read revealed that the paper's lasting contribution is *methodological*—a diagnostic apparatus for decomposing cooperation from competence—rather than primarily behavioral. The shallow note captured the empirical surprise (capability-cooperation inversion) but missed that this inversion is intentionally *generated* by the experimental design to isolate a causal mechanism, and that the three targeted interventions (policy instructions, micro-incentives, limited visibility) are hypothesis tests validating the decomposition model, not post-hoc findings. The mechanism of "hard defection reasoning" and spontaneous market framing in o3's private thoughts—while speculative about causal direction—adds texture absent from the annotation.

**(c) Training signal**

**Escalate when:** the shallow note identifies a controlled empirical test of a specific coordination regime (costless helping, explicit instruction) where the outcome inverts intuitive predictions and the annotation explicitly claims a novel mechanism (instruction-utility gap, capability-cooperation decoupling) absent from current conceptual inventory—because this signals a paper building diagnostic infrastructure, not just reporting a surprise.

**Don't escalate when:** shallow notes describe interesting-but-aggregate behavioral findings across many models without specifying the experimental regime or causal decomposition strategy, because those often collapse under deep reading into artifacts of model scale or instruction-tuning rather than genuine mechanism discovery.

---

## arxiv-2605.18185

# Assessment of Escalation Decision

## (a) Escalation accuracy

**Annotation claim:** "Provides analytical grounding (not simulation-only) for how assortment mechanisms alter agent learning dynamics—a foundational mechanism for cooperation emergence in protocolized systems that has lacked theoretical formalization."

**Verdict:** `accurate`

The paper *does* deliver analytical grounding for how partner selection rules alter learning dynamics in multi-agent reinforcement learning. It translates empirical simulation findings into mean-field theory, deriving exact equations for population-level cooperation under policy gradient dynamics. The core mechanism—opponent distribution reshaping—is formally characterized via Markovian recursions and the Fokker-Planck equation. The variance necessity result (∆G[ρ] = bVar(ρ) − 2c) is a genuine theoretical contribution that wasn't available at simulation-only granularity. This is foundational work: it proves that population heterogeneity is *necessary*, not just empirically useful.

The annotation's framing as "protocolized systems" is slightly loose (the paper studies partner selection rules as exogenous constraints, not protocols agents design), but the substantive claim—analytical formalization of mechanism—is precisely what the paper contains.

---

## (b) What deep reading added

Deep reading revealed the paper's true architecture: it is not a novel discovery about cooperation, but a **translation of 40 years of simulation folklore into rigorous mean-field theory**. The shallow note couldn't have captured the specific mechanism (opponent distribution recursion) or the surprising symmetry between OFT and ROFT cooperation-promotion rules, nor the counterintuitive finding that *stochasticity itself can generate the variance necessary* for cooperation. The deep read also exposed the limits: the Fokker-Planck model breaks down at high learning rates, and the stationary distribution is bimodal (pure cooperators + pure defectors), not mixed-strategy equilibrium—a structure that simulation work may have missed.

---

## (c) Training signal

**Escalate when:** A shallow note claims analytical grounding for a mechanism that has only empirical (simulation) precedent, *and* cites a specific structural quantity (opponent distribution, variance requirement) that suggests the authors have isolated the causal step—not just proved cooperation occurs, but *why it must occur* given structural constraints.

**Don't escalate when:** The shallow note frames a paper as providing "theoretical formalization" but the actual contribution is a minor extension of existing analytical work (e.g., adding noise to a deterministic model that was already solved), or when the paper's own abstract or introduction already states the mechanism clearly enough that the shallow note is just paraphrasing without identifying a novel insight the deep read would uncover.

---

## arxiv-2605.18784

# ESCALATION ASSESSMENT

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed this paper "documents mechanisms of exclusion and silent exposure that are absent from current inventory and likely generalizable across financial/legal governance layers." The deep read confirms this precisely. The paper does map institutional boundary-drawing (via the 55×26 matrix), does isolate a novel mechanism ("silent AI exposure" as distinct from silent cyber), and does identify a structurally unprecedented insurability failure (foundation model concentration breaking the loss-independence assumption at portfolio level). The three-tier frontier taxonomy is genuinely absent from prior coverage — the paper is not resynthesizing existing doctrine but observing live market sorting. The annotation slightly undersold the conceptual precision: the paper doesn't just document exclusions, it distinguishes *three structurally different types* of uninsurability (architectural failure vs. intent vs. systemic correlation), which is richer than the annotation implied.

**(b) What deep reading added**

The shallow note captured the core claim (boundary-drawing + silent exposure), but missed that the paper's real contribution is a *mechanism-typing task*: it shows that "AI insurability failure" is not monolithic — some gaps (e.g., AI-washing) are familiar doctrinal problems, while one (foundation model concentration) is genuinely novel because it involves continuous cedent-base growth + no exogenous trigger + no severity scale, making it structurally unlike traditional catastrophe correlation. Deep reading also revealed the careful epistemic framing: the matrix measures "publicly claimed positioning" not executed wording, a caveat that weakens some conclusions but strengthens others (the silent exposure finding is more credible precisely because it's harder to hide). The migration hypothesis around prompt injection is speculative, not prescriptive—important for calibrating confidence.

**(c) Training signal**

"Escalate when: a paper offers a taxonomy or cartographic mapping of an institutional failure mode (here: coverage gaps) *with mechanistic differentiation* (three types of uninsurability, not one), grounded in primary-source enumeration (public carrier materials) that reveals both what's absent and why, with explicit epistemic honesty about the limits of the data source."

"Don't escalate when: the shallow note already names the finding (silent exposure, boundary-drawing) unless there's explicit signal that the paper has structural differentiation or methodological novelty beyond what the annotation states—in this case, both were present, justifying escalation, but a note that just says 'documents institutional gaps' without specifying mechanism-types or causal vocabulary would warrant skepticism."

---

## arxiv-2605.29359

# ESCALATION ACCURACY ASSESSMENT

**(a) Escalation accuracy: `accurate`**

**Escalation claim:** "Presents a sustained mechanism (algorithmic circumvention of protocol verification) that directly challenges the technical foundations of an emerging governance protocol class, and generalizes a pattern (Hardness Asymmetry) to a new domain with high policy relevance."

**Assessment:** The escalation annotation is accurate. The paper does present a sustained technical mechanism — the DiLoCo algorithmic family's reduction of inter-node bandwidth requirements from 400+ Gbps to <100 Mbps — that directly circumvents the physical detectability assumption underpinning compute governance proposals. This is not a marginal loophole but a structural vulnerability in regulatory architecture. The paper generalizes a pattern (asymmetry between what regulators can monitor and what evasion-aware adversaries can deploy) to a new domain (AI compute governance) with genuine policy stakes (Scher et al. 2025, EU AI Act, California SB 53 all targeted). The annotation's framing of "Hardness Asymmetry" maps cleanly to Rahman's core insight: regulatory architecture based on physical detectability inherits fragility as the technical requirement for detectability disappears. The paper is exactly what the escalation claim promised.

---

**(b) What deep reading added**

The deep reading clarified the *architecture* of the vulnerability in ways the shallow annotation could not have specified: the replica divergence penalty scales inversely with model size (larger models suffer less distributed training loss), which means the evasion strategy improves at frontier scale rather than degrading; the A100 80GB memory asymmetry is the load-bearing exploit, not compute thresholds themselves; and the paper's countermeasures section is not merely defensive but uses a systematic framework (which responses actually work vs. which feel responsive) that separates viable governance from theater. The shallow note captured the core claim accurately, but deep reading revealed that the paper's lasting contribution is the *framing* of regulatory fragility tied to disappearing physical assumptions, not just the numerical evasion feasibility.

---

**(c) Training signal**

**Escalate when:** The annotation identifies a mechanism that challenges foundational assumptions of a governance/verification protocol class (not just a workaround), and the paper demonstrates this mechanism scales *better* with adversary sophistication or system scale, with explicit policy-relevant threat models and countermeasures analysis.

**Don't escalate when:** The annotation claims "mechanism undermines governance" but the paper is primarily a numerical sensitivity analysis of existing attacks without identifying architectural vulnerabilities, or the evasion cost/complexity increases faster than legitimate system scale.

---

## arxiv-2605.30680

# ASSESSMENT: arxiv-2605.30680

## (a) Escalation accuracy

**`accurate`**

The escalation annotation claimed: *"introduces a generalized method (policy-as-code search + strategic response modeling) absent from current benchmarking practice and demonstrates that classical economic findings re-emerge as regime transitions in a computational system — pattern generalizes beyond healthcare."*

The paper **does** deliver on all three elements:

1. **Novel method**: Medi-Sim implements closed-loop equilibrium evaluation with inspectable policy code (DSL + LLM-guided search), which is absent from cited benchmarks that treat provider behavior as fixed. This is primary methodological contribution.

2. **Classical findings as regime transitions**: The phase diagram (α, β parameter sweep) empirically recovers DRG rent-seeking, case-mix distortion, and target gaming as adjacent regimes of a single coupled system — exactly as claimed. The audit lever sweep (p.7, p.32) is the definitive exhibit: up-coding suppression → cherry-picking doubling.

3. **Generalizability claim**: The annotation says "pattern generalizes beyond healthcare." The paper frames pressure migration as a general principle of regulated mechanism design (p.1–2) and the Stackelberg structure is domain-agnostic, but the paper itself only demonstrates it in healthcare. The claim in the annotation slightly oversells the evidence — the paper argues the principle *could* generalize, it does not show it does.

**Verdict**: The escalation was justified. The one minor overstatement (generalization beyond healthcare) is a framing choice in the annotation, not a mischaracterization of the paper's substance. The core claimed mechanism is present and load-bearing.

---

## (b) What deep reading added

Deep reading revealed the **pressure migration as substitution lattice** — the five channels (coding, selection, delay, effort, triage) are not independent levers but a coupled system where saturation of one channel forces the incentive gradient into adjacent channels. The shallow annotation captured "regime transitions" but did not expose the *structural coupling* that makes migration inevitable: Eq. (2) couples all five through a shared utility function, and the IPS decomposition makes this dependency auditable. This is the mechanism-design insight that distinguishes the paper from mere empirical phase-diagram sweeps. Deep reading also clarified the **bounded-rationality response class** (a substantial methodological limitation acknowledged on p.9 but not highlighted in the annotation) and the **warm-start dependency** of L3 search (p.22–23), which constrains how "generalizable" the policy-search method is in practice.

---

## (c) Training signal

**Escalate when:** A paper claims to close a *feedback loop* in an existing benchmark (administrator intent → provider response → measured outcome) by formalizing it as a multi-agent equilibrium problem, and demonstrates the closure reveals regime transitions or phase transitions that single-agent benchmarks systematically miss — especially if the closed-loop is *load-bearing* (i.e., the paper's diagnostic claims fail without it).

**Don't escalate when:** A paper applies equilibrium simulation to a domain but treats provider behavior as exogenous (fixed best-response or empirical data) rather than solved or modeled; or claims generalizability across domains without demonstrating the mechanism in more than one domain.

---

## arxiv-2606.00013

# Escalation Assessment: Arxiv-2606.00013

---

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper demonstrates "a novel mechanism—algorithmic conformity in moral reasoning—that operates through feedback loops between human judgment and AI outputs." The deep read confirms this is exactly what the paper delivers. The core finding—that AI-with-reasoning achieves conformity rates equivalent to human social pressure while operating through a *different mechanism* (genuine attitude change vs. public compliance)—is empirically demonstrated across 165 participants and 18 moral dilemmas. The mechanism is not speculative window-dressing; it is directly measured via the dissociation finding (56.15% public/private divergence in Human condition vs. 2.6% in AI-reasoning condition). The novelty claim is also accurate: this specific experimental demonstration of algorithmic conformity in moral judgment does not appear in the existing literature (the authors position it as extending Asch conformity paradigm to a new domain). The generalizability framing ("potentially generalizable across decision domains") is appropriately cautious—the paper tests only moral dilemmas, but the mechanism (reasoning → perceived objectivity → genuine belief shift) could plausibly apply to other high-stakes judgments.

The annotation did not oversell; it did not undersell.

---

## (b) What deep reading added

The shallow annotation captured the headline mechanism correctly, but deep reading revealed a critical theoretical refinement that the paper itself emphasizes but that a shallow note might miss: the **dissociation finding** (2.6% compliance-without-conviction in AI-reasoning vs. 56.15% in human conditions) shows that observable conformity rates can mask fundamentally different psychological processes, with asymmetric persistence implications. The deep read also surfaced that the authors' proposed neuro-evolutionary mechanism (old/new cognitive systems) is the most speculative element, not empirically tested—a meaningful qualification for downstream use.

---

## (c) Training signal

**Escalate when:** A paper reports a direct behavioral experiment (not simulation or retrospective survey) measuring a specific mechanism in a domain (moral judgment, high-stakes decisions) previously thought to be resistant to the hypothesized influence pathway (e.g., algorithmic pressure on normative reasoning), with results showing a novel dissociation or differential pathway compared to established precedents (e.g., human social conformity).

**Don't escalate when:** The shallow note describes a mechanism as "novel" but the paper only demonstrates it through correlational self-report data, qualitative interviews, or indirect proxies (e.g., behavioral outcomes without mechanism measurement), or when the claimed novelty is simply an application of an existing mechanism to a new domain without structural differentiation (e.g., "algorithmic herding in finance" that operates identically to human herding, just with a different input source).

---

## arxiv-2606.00291

# Escalation Assessment: arxiv-2606.00291

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed this paper applies "social choice impossibility results to the core aggregation mechanism in RLHF systems, identifying a fundamental structural constraint on reward model design that generalizes beyond preference learning."

The paper delivers exactly this. It transposes Arrow's impossibility theorem into the RLHF setting by proving that embedding dimensionality governs a tradeoff between two failure modes: (1) information loss from representation collapse, and (2) exposure of irreducible Condorcet cycles that no scalar reward can rationalize. The decomposition (Proposition 4.1 and Theorem 4.1) is precise and quantitative. The result is structural — not a training procedure fix, but a lower bound on achievable loss that is minimized at an intermediate dimension determined by the dataset's cycle geometry. The extension to DPO (Lemma C.1) confirms the generality claim.

No mismatch between annotation and content. The annotation was conservative if anything — it did not flag that the paper also proves joint embedding-reward training cannot find the optimal tradeoff (Propositions 5.1–5.2), a stronger negative result.

---

## (b) What deep reading added

The shallow annotation correctly identified the core insight (social choice impossibility applied to reward aggregation). Deep reading confirmed this but added two material details: (1) the exact decomposition into embedding loss and agreement cost is an identity, not a bound, which makes the lower bound derivation rigorous rather than heuristic; and (2) the joint training result showing that standard optimization has *no fixed points other than degenerate ones*, a structural failure that goes beyond the existence of a tradeoff. The paper is also more mature and careful than the annotation suggested — it acknowledges the Hölder regularity assumptions are not empirically validated and does not oversell the algorithm contribution.

---

## (c) Training signal

**Escalate when:** A paper claims to derive a *quantitative lower bound* on a standard training objective from first principles (social choice, information theory, or similar), makes that bound's dependence on a key design parameter (here: embedding dimension) explicit and non-monotonic, and proves that the standard training procedure is *structurally* unable to find the optimum. These are hallmarks of a fundamental constraint, not a tuning knob.

**Don't escalate when:** A paper applies an impossibility result (Arrow, etc.) by loose analogy, states that a tradeoff exists without quantifying it or proving it is fundamental to the objective function, or proposes a training fix without proving the constraint is truly structural. The annotation would have been over-claimed if the paper had only shown "Condorcet cycles matter in RLHF" without the exact decomposition and lower bound.

---

## arxiv-2606.01874

# Assessment: arxiv-2606.01874

## (a) Escalation accuracy

**Claim from annotation:** "Primary source modeling a fundamental tension in protocol design (decentralization vs. latency-dependent coverage) that generalizes across distributed systems; introduces geographic-temporal coupling as a mechanism absent from current inventory."

**Verdict:** `accurate` — with one refinement.

The paper does indeed model a fundamental tension: decentralization (multiple self-interested builders) vs. fair coverage (ensuring peripheral transaction sources aren't starved). This is a core protocol-design problem in blockchain and generalizes to any distributed system where geographic/network-proximity effects interact with incentive decentralization.

However, the paper does *not* introduce "geographic-temporal coupling" as an explicit named mechanism. Rather, it reveals *latency-induced location bias as an equilibrium phenomenon*: builders concentrate near high-value sources not by coordination but because the private marginal return to joining a well-covered region exceeds the social return. The "coupling" is real (builders' location choices depend on both source value and latency-to-reach), but the mechanism is framed as an *imbalance in local vs. global incentives*, not as a novel technical primitive. The annotation slightly over-labeled the conceptual novelty, but the underlying insight (that decentralization fails to guarantee fair coverage due to location-value interactions) is exactly what the paper delivers.

---

## (b) What deep reading added

The deep read revealed three dimensions the shallow annotation could not have captured: **(1)** the precise structural source of inefficiency — not information asymmetry or malice, but the *submodular returns to geographic concentration* in a stochastic game with equal-split rewards, formalized via exact potential theory; **(2)** a regime-dependent finding that welfare loss is worst in the *intermediate* latency regime (long enough to be worth routing to, short enough that high-value sources still dominate), which reframes the problem from "decentralization is bad" to "decentralization's effectiveness depends on system timescale"; and **(3)** the counter-intuitive tension between geographic dispersion and utility fairness — planner allocations may spread builders but create inequality, while equilibrium clusters builders but balances payoffs. These are not minor elaborations; they substantially deepen the strategic clarity of the result.

---

## (c) Training signal

**Escalate when:** A paper claims to model a game-theoretic or incentive-structural tension in distributed systems (decentralization vs. coverage, latency vs. fairness) *and* promises a quantitative bound (PoA, equilibrium characterization) *and* the annotation cites generalizability across system types — these are reliable signals that the paper likely contains rigorous equilibrium analysis and regime-dependent insights worth extracting.

**Don't escalate when:** A shallow annotation describes a tension or mechanism using only metaphorical or design language ("introduces coupling," "captures interaction") without citing a formal result, bound, or equilibrium prediction — the paper may be a position piece or simulation study that doesn't warrant deep structural analysis.

---

## arxiv-2606.03161

# ESCALATION ACCURACY ASSESSMENT

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper presented "a foundational mechanism (protocol-neutral trust layer for agent networks) absent from current inventory; generalizes beyond single domain to the structural problem of open multi-agent systems."

The deep read confirms this precisely. The paper does articulate a protocol-neutral trust substrate (OAN) positioned deliberately below existing agent interaction protocols (MCP, A2A, ANP). It does identify a structural gap — the "pre-connection trust problem" — that is genuinely absent from the current protocol inventory and applies across domains (Agent Services, Skills, MCP Servers, Tool endpoints). The author's framing of identity, governance, discovery, and invocation as a unified pre-connection layer is the core novelty. No misalignment detected between annotation claim and paper content.

---

**(b) What deep reading added**

The shallow annotation could not have identified that the paper's real load-bearing insight is the *separation of governance authority from protocol enforcement* (the `active governance state ∧ valid Root-issued VC` two-condition formula), nor could it have caught the deliberate deferral of cross-domain federation as an acknowledged limitation that bounds the current scope. Deep reading also revealed the OCI analogy as the primary architectural anchor — the paper's confidence is highest where it parallels container standardization (envelope-level specification without content prescription), and weakest in performance evaluation (feasibility only, not production capacity) and federation. This layered confidence map would be invisible to a shallow read.

---

**(c) Training signal**

**Escalate when:** the shallow note identifies a claimed structural gap (absent mechanism, unaddressed problem class) that spans multiple domains or protocol families, and the annotation frames it as "foundational" or "presupposed" — these signals indicate the paper is likely a design manifesto or architecture proposal where the novelty lies in problem *framing* and *role separation*, not incremental improvement to a known solution.

**Don't escalate when:** the paper is primarily a performance evaluation, empirical comparison, or implementation report of an already-defined mechanism — the shallow note will capture the main contribution, and deep reading will only confirm or refute quantitative claims rather than extend conceptual understanding.

---

## arxiv-2606.03636

# Escalation Assessment: arxiv-2606.03636

---

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper introduces "a novel equilibrium concept (CME) that formalizes endogenous semantic decoupling—a mechanism absent from game theory and present in generative agents—with explicit claims about failure modes in agentic systems."

The deep read confirms this precisely. The paper does:
- Introduce CME as a formal equilibrium concept (Definition 2, pp.5-6)
- Establish that classical equilibrium concepts (Nash, Bayesian, self-confirming, correlated, mean-field, evolutionary) are *blind* to causal decoupling because they lack a state variable tracking grounding [pp.1-4]
- Prove existence of stable equilibria where agents operate in a "mirage regime" (M_i ≥ 1 + η) — functionally coherent but causally detached from reality
- Frame this as a structural failure mode of agentic systems, distinct from model collapse or transient error

The annotation's framing was neither over-claimed nor conservative. The paper delivers exactly what was advertised: a novel formalization of a specific, previously unnamed failure mode.

---

## (b) What deep reading added

The shallow annotation could not have captured: (1) the *mathematical structure* of the bifurcation mechanism — how the mirage intensity parameter M creates a phase transition from grounded to ungrounded attractors, with an explicit critical surface M = 1 and a contractivity condition for local stability; (2) the *empirical gap* — the paper proves CME exists under regularity conditions but explicitly defers empirical estimation of M_i in real LLMs to future work, making the practical relevance currently theoretical; (3) the load-bearing role of Figure 1 as the geometric translation of the bifurcation theorem, which is the paper's most intuitable contribution.

Deep reading revealed the paper is mathematically tighter and empirically more tentative than the escalation note implied.

---

## (c) Training signal

**Escalate when:** A paper formalizes a previously *unformalized* failure mode as a stable equilibrium or attractor, introduces an explicit state variable or parameter (like Tembine's grounding functional g_i and mirage intensity M_i) that classical frameworks lack, and provides an existence proof under stated regularity conditions — even if empirical grounding is deferred.

**Don't escalate when:** The escalation note describes a novel mechanism or concept, but the deep read reveals it is speculative without a formal existence theorem, or the mechanism is already implicitly captured in classical frameworks being cited (avoid "absent from X" claims without checking whether X's generality already subsumes the proposed novelty).

---

## arxiv-2606.04056

# Escalation Accuracy Assessment

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed this paper identifies "a genuine failure class in protocolized agent systems (budget aliasing/enforcement gaps)" with "a type-theoretic mitigation absent from current inventory" that "generalizes across 21 frameworks."

The deep read confirms all three elements:
- **Failure class:** The paper documents 63 production incidents + 47 supplementary entries across 21 independently-developed frameworks showing recurring budget-overrun patterns (M-retry-loop, M-delegation-fanout, etc.). This is a structural, recurring failure mode, not an outlier.
- **Type-theoretic mitigation:** The affine-ownership approach in Rust is genuinely novel in this application domain—it enforces non-bypassability at compile time via the borrow checker, which is distinct from (and structurally superior to) runtime locking or post-hoc callbacks.
- **Generalization signal:** The eight-cluster taxonomy demonstrates the failure pattern recurs across 21 frameworks with different architectures, establishing that this is a coordination problem, not a library bug.

The annotation slightly overstated the universality of the Rust mitigation (it applies only to new Rust agents, not the Python-dominated ecosystem), but this was transparently acknowledged in the paper itself and does not undermine the primary contribution (the catalog + mechanism taxonomy).

---

## (b) What deep reading added

The deep read revealed the paper's true argumentative spine: not "here is a better defensive technique" but "here is empirical evidence that resource-constraint enforcement belongs at compile time, not runtime, because all reactive layers catch violations *after commitment*." The forgetful-operator experiment (30/30 racy overshoots vs. 0/30 affine overshoots) is categorical evidence that affine typing removes operator-discipline burden structurally—not a marginal efficiency gain. The shallow annotation could not have captured the candor about load-bearing assumptions (A1: estimator soundness; A7: provider truthfulness) or the fault-injection table showing 100% overshoot under A7 violation, which recalibrates confidence bounds on the approach's real-world applicability.

---

## (c) Training signal

**Escalate when:** the annotation identifies a cross-system failure pattern (recurrence across ≥5 independent implementations) coupled with a mechanism claim that is either structurally novel (compile-time enforcement vs. runtime) or invokes unfamiliar vocabulary (affine types, type-state protocols) that the shallow read cannot fully evaluate without formal verification sections.

**Don't escalate when:** the paper is a single-library case study, a performance optimization for an existing mitigation class, or a proposal without inter-rater-validated empirical grounding (here κ=0.837 for the core taxonomy; at κ<0.65 escalation becomes optional).

---

## arxiv-2606.04617

# Escalation Assessment

## (a) Escalation accuracy

**Claim quoted:** "formalization of rules *lowers the cost of boundary search* in strategic systems, creating a distinct class of gaming dynamics."

**Assessment: `accurate`**

The paper does establish exactly this mechanism. He demonstrates that:
- Computable rules reduce the *cost* of boundary search for firms (conduct boundary mass: 0.367 → 0.411 under computability)
- This creates a distinct behavioral class — not open violation, but systematic clustering of *formally compliant* conduct near the legal edge
- The mechanism is separable and measurable (via the conduct/signal boundary distinction)
- The dynamics persist under adaptive enforcement ("regulatory chase") rather than resolving

The shallow annotation correctly identified the novel load-bearing mechanism and its absence from standard gaming/Goodhart inventories. The paper does primary empirical work (ABM+RL) to make the mechanism inspectable. No mismatch.

---

## (b) What deep reading added

The shallow annotation captured the core novelty and mechanism claim accurately. Deep reading revealed two understated but important extensions: (1) the estimand distinction (conduct vs. signal boundary mass) is not just a measurement clarification but a *prerequisite for causal inference* — conflating them produces false inferences about whether rule changes actually change behavior — and (2) the anti-gaming design finding (randomized audits + outcome guardrails) supplies actionable regulatory direction, grounding the mechanism in a concrete design lever rather than leaving it at diagnosis.

---

## (c) Training signal

**Escalate when:** The shallow annotation identifies a *named mechanism absence* (gaming dynamic not yet in the standard inventory) + claims primary empirical construction (ABM/RL synthesis) + the mechanism is load-bearing for a policy question (Rules-as-Code reform). This combo reliably signals deep reading will yield novel vocabulary and design-relevant findings, not just confirmation.

**Don't escalate when:** A paper claims a novel mechanism but the shallow annotation lacks specificity about what exactly is absent from current theory, or when the primary source is secondary (simulation of existing phenomena with known causal structure). Also: avoid escalating on "mechanism X in novel context Y" unless the annotation indicates the context changes the mechanism's causal shape, not just its domain.

---

## arxiv-2606.05363

# ASSESSMENT: Arxiv 2606.05363

## (a) Escalation accuracy: `over-claimed`

**Escalation claim:** "Strategic obliviousness in demand modeling produces emergent collusion without explicit coordination—absent from current inventory and generalizable across price-discovery protocols."

**What the paper actually shows:** Wu & Zeevi *refute* the hypothesis that strategic obliviousness robustly produces collusion. They prove that oblivious sellers, facing structural exploration costs ("spiral-up"), must escalate to linear exploration rates. Under sufficient exploration, all-oblivious markets converge to Nash equilibrium—not collusion. Observed collusive-looking outcomes are explained as transient "excursions" (finite-time artifacts) or incomplete learning under decaying exploration, not emergent coordination.

**The mismatch:** The escalation annotation frames this as a paper identifying a collusion-producing mechanism. The paper's actual contribution is *disconfirming* that mechanism and explaining why apparent collusion is a learning artifact. This is a fundamental inversion of the claimed insight. The paper does identify a novel mechanism—the variance-dominance spiral-up—but that mechanism *prevents* collusion, not enables it. The novelty is real and the work is rigorous, but the escalation rationale mischaracterized the direction and nature of the finding.

---

## (b) What deep reading added

The shallow annotation missed the paper's core refutation: strategic obliviousness does *not* produce robust collusion. Deep reading revealed that the mechanism actually works against collusion, forcing oblivious sellers into persistent exploration that disciplines prices toward Nash. The paper also contains substantive analysis of how finite-horizon learning under diminishing exploration can *mimic* collusion (the "pseudo-equilibrium continuum"), which explains earlier empirical puzzles but does not vindicate the collusion hypothesis—a crucial distinction the shallow note's positive framing obscured.

---

## (c) Training signal

**Escalate when:** A shallow annotation claims a paper identifies a novel strategic mechanism (e.g., "strategic obliviousness produces collusion") but the mechanism is non-standard or the direction of its effects is counterintuitive—the burden to verify the actual directional claim and mechanism integrity is high, and shallow reading can easily transpose hypothesis from conclusion.

**Don't escalate when:** The annotation correctly identifies a refutation or negative result but frames it positively as a "mechanism producing X" when the paper actually proves "X does not robustly occur"—verify that the claimed mechanism's *polarity* (does it enable or constrain the outcome?) matches the paper's actual finding before escalating on novelty grounds alone.

---

## arxiv-2606.06572

# Assessment: arxiv-2606.06572

---

## (a) Escalation accuracy

**`accurate`**

The escalation annotation claimed the paper "introduces a mechanism (verification-cost collapse triggering selection for surface-feature mimicry over genuine learning accumulation) absent from current inventory; argues this generalizes across knowledge domains as a structural pressure on human epistemic practices under market conditions."

The paper *does* introduce exactly this mechanism. The core argument is a formal adverse-selection dynamic: when verification cost (cv) exceeds the expected benefit of detection (g · ∆q), evaluators stop inspecting → outputs become reward-pooled across production types → HTL producers (high-cost, high-quality) cannot compete and exit → pool composition degrades → pooled reward collapses. This is not present in standard alignment/capability literatures; it is orthogonal to them.

The generalization claim is also substantiated. The paper organizes evidence across four domains (clinical medicine, legal systems, academic publishing, content platforms) along a single dimension of verification erosion, arguing this reflects a *structural* pressure on knowledge economies under market conditions, not domain-specific failure.

No mismatch. The shallow annotation correctly identified both the novelty and scope.

---

## (b) What deep reading added

The shallow note captured the mechanism and claim correctly but omitted two load-bearing structures that only emerge from full text: (1) the formal inequality condition (`g · ∆q ≥ cv`) and the pooled-reward model that converts it to testable predictions, and (2) the distinction between two cascading mechanisms — value collapse (adverse selection proper) and pipeline compression (experiential pathway destruction) — which operate on different timescales and require different policy responses. Deep reading also revealed concrete empirical anchors (NHANES 47x growth, ICLR fabricated citations, cURL submission validation rate) that materially strengthen the otherwise abstract argument.

---

## (c) Training signal

**Escalate when:** A shallow note claims a *novel structural mechanism* (not just a new application of known dynamics) that generates a *quantifiable inequality or state-transition condition* and proposes cross-domain evidence organized along a single causal dimension—especially when the mechanism is orthogonal to current research agendas and the annotation explicitly names both the mechanism and its domain scope.

**Don't escalate when:** A shallow note proposes a generalization across domains without naming a specific mechanism that would make the generalization *testable differently* in each domain, or when the "novel" claim is actually a known adverse-selection or market-failure pattern with a new label attached.

---

## arxiv-2606.06633

# ASSESSMENT: arxiv-2606.06633

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Quoted escalation claim:** "introduces intermediary-enforcement constraints as a generative mechanism absent from current inventory; directly applicable to protocolized systems beyond blockchain."

**Assessment:** The escalation was warranted. The paper does introduce a genuinely novel mechanism — the commitment problem inherent in information disclosure under competition between sealed and open auction formats — and frames it as a delegation/intermediary-enforcement solution (Proposition 4: the seller must delegate to a credible agent to pre-commit to non-disclosure). This constraint on what intermediaries must credibly *enforce* (sealed-bid integrity against ex-post incentives to leak) is absent from standard auction theory and does generalize: any multi-channel market where a single operator controls allocation across formats faces this unraveling + commitment dynamic. The paper's application to ePBS is concrete, but the structural logic (seller, multiple auction channels, information asymmetry, fast bidders) appears in FX dealers, dark pools, and order routing — exactly as claimed. The shallow annotation correctly identified this as a foundational mechanism worth deep engagement.

---

## (b) What deep reading added

The shallow note captured the core claim (unraveling + intermediary commitment), but deep reading revealed the precise technical load-bearing move: Theorem 3 shows the seller's *ex-post incentive* to disclose is distinct from — and opposed to — the ex-ante revenue-optimal commitment (Proposition 4). This distinction between ex-post profit and ex-ante commitment value is the paper's deepest insight and is absent from the shallow summary; it reframes intermediary enforcement not as a nice-to-have but as a *binding constraint* that resolves a fundamental incentive conflict. The paper's treatment of multi-homing (Theorem 2) also adds realism beyond single-homing that the shallow note didn't surface.

---

## (c) Training signal

**Escalate when:** A mechanism design paper claims that a competing or alternative institutional channel causes existing formats to collapse (unravel), *and* attributes this to an incentive asymmetry (like information leakage, adverse selection, or commitment failure) that **prevents** the seemingly natural equilibrium from being sustained — especially if the paper resolves the tension by identifying who must enforce the constraint and why that enforcement is non-trivial.

**Don't escalate when:** A paper demonstrates that one auction format dominates another in head-to-head comparison (standard efficiency ranking) without identifying a *structural commitment or information problem* that a third party must solve — this is textbook mechanism design, not a new generative mechanism for intermediation failure.

---

## arxiv-2606.07434

# ASSESSMENT: arXiv-2606.07434

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "Introduces a genuine mechanism (evidence-coupled incentive structures with endogenous resolution) absent from prediction market design; directly addresses foundational problem in belief aggregation protocols—separating crowd consensus from causal reasoning chains."

**Assessment:** The paper delivers exactly this. The core mechanism is the dynamic liquidity parameter β(R) that decreases as evidence quality R accumulates. This couples evidence submission directly to trader payoffs via the decomposition: payoff = belief payoff + evidence payoff, where evidence payoff = [β(R_{t-1}) - β(R_t)] · H(q). This is genuinely novel in prediction market design — I found no prior work using evidence quality to modulate liquidity.

The endogenous resolution extension (resolving by softmax over evidence scores rather than external oracles) is also absent from standard designs. Theorem 1's bound on manipulation via selective evidence withholding (max shift ≤ |E_t|/τK) is what makes this feasible.

The separation of reasoning from consensus is real: the market produces both a final belief *and* a ranked corpus of evidence, not just a probability. This addresses the annotation's claim squarely. No mismatch detected.

---

## (b) What deep reading added

The shallow note captured the mechanism and motivation correctly. Deep reading revealed three layers of rigor beneath that claim: (1) Theorem 2's payoff decomposition showing how evidence reward scales with market entropy (evidence most valuable when uncertainty highest), enabling a principled microfoundation; (2) the risk-averse trader corollary, which shows how the mechanism lowers participation barriers by allowing pure evidence contribution with zero belief-taking risk; and (3) the honest treatment of three open problems (verification hardening, evidence acquisition cost, order-book implementation), which grounds the paper's scope in what remains unsolved rather than overstating completeness.

---

## (c) Training signal

**Escalate when:** A prediction market paper claims to extend the information *output* of the mechanism (e.g., producing explanations/reasoning alongside prices) and proposes a coupling between evidence quality and trader incentives with a formal decomposition showing how payoffs separate into "belief contribution" and "evidence contribution" components.

**Don't escalate when:** A prediction market paper adds a new market type or outcome space (e.g., conditional markets, continuous-outcome markets) without a novel incentive coupling, even if it solves a real design problem—these are typically incremental variants with sound but unsurprising game-theoretic properties.

---

## arxiv-2606.07873

# Assessment: arxiv-2606.07873

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper demonstrates "*adoption-level nonmonotonicity* in distributed artificial systems where increased coordination can degrade global safety outcomes" as a "generalizable pattern for partial-adoption regimes across networked autonomous agents."

The paper **does** contain exactly this mechanism. Theorem 1 proves that under fixed (non-optimal) signaling policies, increasing V2V adoption *can* increase equilibrium accident probability — a direct counterexample to the intuitive monotonicity. The mechanism is concrete: as adoption increases, the behavioral equilibrium shifts between regime regions (R₅ → R₄ → R₃...), and in intermediate regimes (R₃, R₄), the composition of signaled vs. unsignaled drivers creates a threshold effect where marginal adoption is harmful.

However, there is one important qualification the annotation did not flag: **Theorem 2 shows the perverse effect disappears under optimal signaling policy.** The nonmonotonicity is not a fundamental property of V2V systems; it's an artifact of *suboptimal disclosure design*. This narrows the generalizability claim somewhat — the pattern only manifests when the information-disclosure policy is fixed rather than optimized. The annotation's framing ("can degrade global safety") is accurate, but it undersells that optimal design recovers monotonicity. A deeper annotation would distinguish: "perverse effect occurs under fixed disclosure; vanishes under optimized disclosure."

## (b) What deep reading added

The shallow annotation could not have captured the crucial distinction between *hardware adoption* (y) and *policy optimization* (β). Deep reading revealed that the core contribution is not merely demonstrating nonmonotonicity, but identifying a tractable structure (Lemma 7's regime chain) that makes the optimal signaling policy simple and bang-bang (β ∈ {0,1}). The shallow note was sufficient to justify escalation, but the deep read showed the paper's real insight is an *information-design principle*: for V2V systems, the danger lies not in adoption itself but in fixed, non-adaptive disclosure policies; the solution is elegantly simple once the regime structure is understood.

## (c) Training signal

**Escalate when:** A paper claims a counterintuitive nonmonotonicity or perverse effect (more of something makes outcomes worse) with a concrete mechanism in a strategic/networked system, and the annotation provides parameter regions or equilibrium conditions where the effect manifests — this specificity signals the authors have actually proven the claim, not just stated it.

**Don't escalate when:** The annotation describes a paradox or failure mode (e.g., "more adoption degrades safety") without distinguishing between *fundamental* nonmonotonicity and *design-artifact* nonmonotonicity, or without noting whether the effect persists under optimization — this risks treating a design failure as a system property.

---

## arxiv-2606.08265

# ASSESSMENT: arxiv-2606.08265

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "Demonstrates a generalizable mechanism (adaptive adversarial response in learned systems to normative interventions) absent from current inventory; challenges the static-nudge model as foundational assumption across platform governance."

**Assessment:** The paper substantiates both elements. 

The mechanism is real and clearly demonstrated: a platform intervention (celebrity-endorsed sleep reminder campaign) intended to *reduce* late-night usage instead *increased* it by ~15%, with effects persisting 8 weeks post-campaign. The causal chain is: forced exposure → behavioral data generation → recommender system learns user preferences previously obscured by its own bias → policy updates durably → intervention ends but updated policy remains. This is not a simple "nudge fails" story; it's a *feedback-loop* failure where the governance action and the algorithmic learning process are in structural conflict.

The challenge to the static-nudge model is explicit and well-supported. Platform interventions are routinely evaluated as if they operate on fixed systems. This paper demonstrates they simultaneously operate as *training events* for adaptive learners. The generalizability claim is reasonable: any content intervention on a learning system faces this dual-role problem.

The only mild overstatement: the mechanism is demonstrated on *one platform* with *one intervention type* (recommendation boost). The paper doesn't yet prove this generalizes to other platforms, intervention modalities, or feedback structures—though the theoretical argument (menu-cost zones, embedding bias, durable policy updates) is general.

---

## (b) What deep reading added

Deep reading revealed the *precise theoretical scaffolding* beneath the empirical result: the menu-cost framing (inaction zones around incumbent policies), the distinction between intensive-margin (conversion) and extensive-margin (recommendation share) effects as a test of algorithmic updating versus advertising effects, and the heterogeneity pattern (strongest for middle-quintile users, near-zero for top quintile) which constrains the mechanism further. The shallow note captured the headline surprise; deep reading showed the paper had built a *transferable model* of when and why interventions produce perverse post-campaign effects—not just documented one case.

---

## (c) Training signal

**Escalate when:** a paper claims a mechanism that is *simultaneously* a platform governance action and a system-learning event, where the two operate in opposite directions, with a field-experiment or quasi-experiment that rules out simpler confounders (via placebo, reversal design, or asymmetric effect patterns across intervention scope boundaries).

**Don't escalate when:** shallow notes claim "unintended consequences" or "interventions backfire" without specifying the *dynamic feedback loop* through which the reversal occurs, or when the result could plausibly be explained by demand-side or attention effects alone (use the live-streaming placebo pattern as a template: if the mechanism is truly about algorithmic learning, it should be localized to the system under adaptive control).

---

## arxiv-2606.08457

# Assessment of Escalation Decision

## (a) Escalation accuracy: `accurate`

**Escalation claim:** "decoupling of output-level consensus from reasoning-level alignment in multi-agent systems—with direct implications for reliability signals in protocolized artificial systems."

**Assessment:** The paper precisely instantiates this claim. The core finding is that standard multi-agent debate produces answer-level consensus (output) while *actively degrading* reasoning-level alignment (the reasoning layer). The authors measure this decoupling empirically via the consistency illusion (fewer contradictions + lower semantic similarity of reasoning chains), demonstrate it occurs systematically, and show that a protocol modification (GDP) can re-couple them. The "direct implications for reliability signals" are explicit: consensus—the standard reliability proxy—becomes an unreliable signal of actual reasoning alignment, with safety implications. This is not overstated; it is the paper's central contribution and it is demonstrated with specificity (CARA metrics, effect sizes, multiple datasets).

## (b) What deep reading added

The shallow annotation correctly identified the core mechanism but missed two critical layers: (1) the *dual-decomposition* evidence that GDP's success is primarily driven by explicit reasoning-vocabulary-sharing (STANCE-mediated debate, d=+1.51) rather than format alone (d=+0.62), revealing a precise causal pathway; and (2) the striking negative result that alignment gains produce *no improvement* in accuracy, showing that standard evaluation metrics are blind to the failure mode this paper documents—a finding that reframes what "working well" means for multi-agent systems.

## (c) Training signal

**Escalate when:** A paper identifies a failure mode in a widely-used protocol (debate, consensus aggregation, etc.) by introducing a new measurement target orthogonal to existing metrics (reasoning alignment vs. answer accuracy), provides a mechanistic explanation with decomposed components, and offers a minimal intervention with large effect sizes on the new metric.

**Don't escalate when:** Shallow reads claim a "foundational mechanism" or "direct implications" without checking whether the paper actually measures the decoupling (not just proposes it) or whether the intervention produces only incremental gains on existing metrics under the authors' own evaluation framework.

---

## arxiv-2606.08998

# Assessment of Escalation Decision

---

## (a) Escalation accuracy: `accurate`

**Escalation claim:** The annotation stated the paper "systematically decompos[es] sources of variability in agentic systems—separating sampling stochasticity from state dependency—introducing a mechanism (multi-layer variability architecture) absent from our current inventory."

**Assessment:** The annotation's framing is substantially correct but requires recalibration. The paper *does* systematically decompose variability sources and *does* introduce an absent conceptual vocabulary (intrinsic vs. extrinsic variation, agentic stochasticity as distinct from model stochasticity, batch-invariance as a serving property). However, the paper is **not** introducing a novel mechanism in the discovery sense—it is a pedagogical/clarification paper that decomposes existing phenomena into precise categories. The "multi-layer variability architecture" exists in deployed systems; the paper's contribution is naming and separating layers that are routinely conflated, not proposing new architectural elements. The escalation was warranted (this paper *is* worth deep reading), but the characterization as introducing an absent *mechanism* slightly oversells what is actually a conceptual reorganization and naming act.

---

## (b) What deep reading added

The deep read revealed that this is fundamentally an **engineering clarification paper**, not an empirical discovery paper—its value lies in eliminating conceptual confusion (stochastic ≠ irreproducible; deterministic decoding ≠ zero variability in deployment) and establishing shared vocabulary across layers of agentic systems. The deep read also surfaced the load-bearing concrete example (JSON tool-call variation producing categorically different business outcomes), the critical but under-emphasized finding about batch-invariance in serving infrastructure (a protocol-layer variability independent of sampling), and the paper's own explicit epistemic boundaries (toy demonstrations on CPU/GPT-2, honest caveats about commercial API seed parameters). The shallow note captured the decomposition intent but could not have discerned that the true intellectual contribution is eliminating false confidence in deterministic decoding and misplaced alarm about stochasticity—this is a clarification that changes how systems should be *designed*, not what mechanisms are possible.

---

## (c) Training signal

**Escalate when:** A paper claims to decompose or separate confounded concepts in a high-stakes domain (systems design, safety evaluation, deployment), explicitly centers a concrete failure case (the JSON tool call), and grounds the distinction in formal vocabulary (intrinsic/extrinsic, with a state-machine model)—even if the paper is pedagogical rather than novel in mechanism.

**Don't escalate when:** A paper promises "a new architecture" or "mechanism" in the annotation but the deep read reveals it is repackaging existing phenomena with new terminology, *unless* the terminology reorganization actually changes design decisions or risk assessment for a system class (in which case it *should* escalate—this paper did meet that bar).

---

## arxiv-2606.09931

# ESCALATION ASSESSMENT

## (a) Escalation accuracy

**Claim from annotation:** "Introduces a fundamental mechanistic distinction (strategic agent coordination can decouple information capacity from harm) that [is] absent from confinement theory and directly challenges sufficiency of information-theoretic bounds in multi-agent adversarial settings."

**Assessment: `accurate`**

The paper does exactly what the annotation claims. The core mechanistic insight — that Schelling-point coordination via shared salience allows strategic agents to concentrate arbitrarily large harm into arbitrarily small channel capacity — is genuinely absent from classical confinement theory (Lampson 1973). The paper explicitly decouples information-theoretic bounds (bits through a channel) from harm-theoretic bounds (damage caused), showing the inference between them fails when senders are strategic and possess coordination resources.

The annotation's phrasing "multi-agent adversarial settings" is slightly looser than the paper's treatment (which emphasizes *cooperative* agents with aligned interests, not adversaries), but this is a minor framing choice, not a substantive mismatch. The paper does challenge the sufficiency of information-theoretic arguments in multi-agent contexts.

---

## (b) What deep reading added

Deep reading revealed the structural precision of the argument: the paper is not claiming confinement is impossible, but rather identifying *which side conditions* restore information-theoretic reasoning to harm-theoretic reasoning (condition c — reducing capacity below the entropy of the most harmful predicate — is the key one, and becomes nearly equivalent to channel removal when harm concentrates on binary predicates). The deep read also showed that the mechanism is not new (Aumann 1974's correlated equilibrium), but the *application* to learned agents and the governance implications are novel. The shallow annotation could not have caught the specificity of the side-condition analysis or the distinction between "strategic confinement is unsolved" and "here are the precise conditions under which information-theoretic bounds work."

---

## (c) Training signal

**Escalate when:** A shallow annotation claims a "fundamental mechanistic distinction" or "directly challenges" an established theoretical framework — especially if the paper rewrites the relationship between two quantities (information vs. harm, capacity vs. damage) or identifies a hidden assumption in a classical argument that fails under a naturalistic generalization (specified programs → learned agents).

**Don't escalate when:** The paper merely applies an existing mechanism (here, Aumann's correlated equilibrium) to a new domain without identifying a structural gap in prior theory, or when the annotation conflates "interesting reinterpretation" with "novel mechanism" — reinterpretation papers are often valuable, but they don't always require deep reading if the annotation already names the gap clearly.

---

## arxiv-2606.10053

# Assessment of Escalation Decision for arxiv-2606.10053

## (a) Escalation accuracy: `accurate`

**Escalation claim:** "a sustained game-theoretic argument identifying a fundamental tradeoff (diversity vs. stability) in protocolized ranking systems under strategic adaptation—a mechanism absent from current inventory that likely generalizes beyond search."

**Assessment:** The paper does exactly this. It establishes that diversity-promoting ranking functions (xQuAD, xMMR) create a genuine strategic tradeoff: coverage-based diversification produces stable equilibrium but collapses diversity at the strategic level (publishers herd); novelty-based diversification preserves diversity but often fails to produce equilibrium at all. The mechanism is the interaction between ranking incentives and publisher best responses — the ranking rule shapes which documents publishers rationally choose to publish, with downstream effects on both diversity and stability. The deep read confirms this is the paper's central contribution and that the tradeoff is demonstrated through formal results (Theorems 1–2, negative examples), not merely conjecture. The escalation's framing as "absent from current inventory" and "likely generalizing" is reasonable — this is a first systematic treatment of how diversification rules interact with strategic publisher behavior.

---

## (b) What deep reading added

Deep reading revealed the **specificity and scope of the tradeoff**: the paper doesn't just claim a tradeoff exists, but characterizes exactly which diversification method fails in which direction (xQuAD → herding; xMMR → no equilibrium for 3+ publishers), with load-bearing negative results that make the tradeoff non-trivial. It also showed that the paper proposes a constructive solution (UIR framework with existence guarantee) rather than stopping at diagnosis — this generalizable design principle wasn't captured in the shallow annotation. The shallow note was sufficient to warrant escalation but missed the constructive follow-through and the precision of the failure modes.

---

## (c) Training signal

**Escalate when:** A paper claims a structural tradeoff in a protocol-mediated game (incentive structure vs. outcome property) and supports it with multiple formal results (existence/non-existence theorems, worked counterexamples) showing the tradeoff is tight rather than an edge case, especially if a generalizable design principle (like UIR) is proposed to navigate it.

**Don't escalate when:** A shallow annotation claims a "fundamental mechanism" in a strategic system but the paper only shows it in a narrow domain (e.g., 2-player games, symmetric distributions) without counterexamples proving the failure mode generalizes, or without constructive follow-up showing how to avoid the tradeoff.

---

## arxiv-2606.10293

# Assessment: arxiv-2606.10293

## (a) Escalation accuracy

**`accurate`**

The escalation annotation claimed: "This presents a sustained formal argument about quota design in research evaluation systems that directly addresses a mechanism (cost distribution under collaboration) **absent from current inventory**, with generalizability across all evaluation protocols using submission limits."

The paper **fully delivers** on this claim:

- **Mechanism present**: Cost distribution under collaboration is indeed the core mechanism, formalized as f(a) where a is coauthor count. The paper derives why f(a) = 1/H_a is the unique solution satisfying both manipulation-resistance and collaboration-respect constraints.
- **Absent from current inventory**: Fixed quota rules (cost = 1 regardless of a) and per-capita rules (cost = 1/a) are both shown to be incoherent or gameable. The harmonic quota addresses a genuine gap.
- **Generalizability**: The framework applies to all competitive submission systems (journals, conferences, grant programs) that use author-level quotas. The generalized framework (Section 4, parameterized by exponent p) explicitly unifies fixed, per-capita, and harmonic rules as special cases, confirming cross-protocol applicability.

No material mismatch. The annotation correctly identified both the novelty (the harmonic decay mechanism) and its scope.

---

## (b) What deep reading added

The shallow annotation identified the core claim correctly but missed two dimensions that justify the escalation:

1. **The derivation structure**: Deep reading revealed that the harmonic solution is not stipulated but *derived* from two competing design axioms meeting uniquely—this is the paper's load-bearing logical architecture and explains why it generalizes (any coherent quota must lie in this space). The shallow note mentioned "mechanism" but not the principle-first methodology.

2. **The conceptual vocabulary**: The paper introduced "irreducible personal claim" (the non-transferable reviewing burden per author) as a clean decomposition of cost, which had no prior term in the evaluation-design literature. This concept extends beyond the specific quota rule and clarifies why all coherent rules have the form β + f(a).

The shallow note was sufficient for escalation decision but underclaimed the paper's theoretical depth.

---

## (c) Training signal

**Escalate when:** A paper derives an institutional protocol (not merely proposes it) from first-principles constraints, proves uniqueness or optimality within that constraint space, and the constraints map to real failure modes of existing practice (e.g., "per-capita enables author-list inflation").

**Don't escalate when:** A paper proposes a quota rule or similar institutional mechanism without either (a) deriving it from competing design axioms, or (b) proving manipulation-resistance formally, relying instead on empirical appeal or designer intuition.

---

## arxiv-2606.10907

# ASSESSMENT: arxiv-2606.10907

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "Introduces a sustained empirical mechanism for how conversational AI systems exert causal influence on human purchasing behavior through unattributed exposure, with methodological innovation to recover hidden effects."

**Assessment:** The paper delivers exactly this. The deep read confirms:
- A genuine causal mechanism (recommendation-induced search behavior among observably-unengaged users: +4.3pp same-name search, +2.4pp own-site visits)
- The mechanism is *sustained* (replicated across assistants, robust to position/familiarity confounds, verified via pre-trend event study)
- It operates through *unattributed exposure* (the effect is invisible to standard last-click attribution; the funnel is search-mediated, not direct)
- The methodological innovation is real and substantial (four-layered identification: pre-trend visualization, non-customer conditioning, stance classification, within-response same-category controls)
- It is generalizable (no cross-assistant heterogeneity; the mechanism holds across product categories)

The annotation accurately identified the paper's weight. No mismatch between claim and content.

---

## (b) What deep reading added

The shallow note captured the core finding and methodological strategy correctly. Deep reading revealed that the paper's *actual* intellectual center is not the discovery of the effect itself, but the epistemology of measuring it—the confound decomposition problem and the pre-trend event study as the load-bearing methodological contribution. It also surfaced crucial precision: the estimand is "acquisition-*like*" (behavior shift among observably-unengaged users), not transactional acquisition, and this hedging is methodologically honest, not evasive. The shallow read could not have recovered the architecture of the four-layered identification or the pre-trend event study's role as the sharpest contribution.

---

## (c) Training signal

**Escalate when:** The annotation flags a confound-decomposition mechanism (separating genuine causal effects from reverse flows and incidental exposures) paired with methodological innovation (pre-trend visualization, matched-width controls) that recovers effects invisible to standard measurement infrastructure—especially in commercial AI contexts where attribution tooling systematically mislabels channel sources.

**Don't escalate when:** The annotation claims a "mechanism for how X influences Y" but the paper only documents a pooled correlation or propensity-matched ATE without addressing whether pre-existing demand flows into X or whether X's naming is incidental rather than causal—i.e., when confound architecture is not visibly addressed in the shallow summary.

---

## arxiv-2606.11632

# ESCALATION ASSESSMENT

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed this paper proposes "a foundational mechanism (runtime admission layer with certificate binding) absent from authorization control planes" that "directly addresses the governance gap between non-deterministic reasoning and high-stakes resource mutation."

The deep read confirms this is exactly what the paper delivers. The paper's core contribution is precisely a runtime admission layer (the "assurance airlock") that interposes between untrusted agent proposals and execution, producing cryptographically bound certificates (Ω) that encode pre-execution evidence, consequence scoring, validator attestations, and scoped execution identity. The deep read confirms the paper identifies a genuine categorical gap: existing controls (IAM, audit logging, SQA) each answer part of the authorization question but none answer "when may a non-deterministic agent proposal become execution authority?" The paper's claim that "sequential individual admissibility does not guarantee joint admissibility" is the animating empirical observation.

The annotation's framing of this as addressing "the governance gap between non-deterministic reasoning and high-stakes resource mutation" is validated—the Aops example and invariants P1-P5 directly substantiate this.

**(b) What deep reading added**

The deep read revealed the paper's honest specification of its own limitations: consequence scoring R(C)—the load-bearing mechanism for routing decisions—has no principled derivation and depends entirely on empirical calibration via historical incident replay, with acknowledged risk of under-estimating hidden dependencies. The shallow note captured the mechanism and architectural contribution; deep reading exposed the paper's confidence boundaries (formal invariants vs. speculative scoring) and the 0.4% unsafe admission rate in prototype testing—data that materially affects assessment of whether this mechanism is ready for high-stakes use.

**(c) Training signal**

"Escalate when: A paper claims to identify a categorical gap in an existing control stack (not merely an extension or optimization of existing categories), proposes a new structural layer to fill it with formal invariants, and provides a concrete worked example showing why existing controls are individually insufficient." 

"Don't escalate when: The annotation claims a 'foundational mechanism' but the paper's load-bearing component relies on tuned empirical classifiers without principled grounding—in that case, flag it as a hybrid (mechanism + heuristic) rather than foundational, and note the confidence boundary in the annotation itself rather than treating the entire contribution as equally rigorous."

---

## arxiv-2606.12201

# ASSESSMENT: arxiv-2606.12201

## (a) Escalation accuracy: **accurate**

The escalation annotation claimed the paper "demonstrates a fundamental constraint on decarbonization scenarios through material physics" and "establishes that engineered energy systems obey resource-depletion laws absent from dominant planning models."

The deep read confirms this precisely. The paper *does* systematically audit 59 European energy system models and find that their least-cost decarbonization pathways exceed current global material reserves (population-allocated) for 7 of 19 materials — with DRR > 10× for Ga, In, Ir, Te. The core finding is that a methodologically rigorous modeling tradition has been collectively blind to a material feasibility constraint that is neither marginal nor easily resolved by technological roadmaps alone. The annotation's claim about "resource-depletion laws absent from dominant planning models" is substantiated: the paper shows ESMs optimize for cost while omitting material constraints entirely (only 9 of 72 prior studies even attempted material-aware modeling).

The annotation's assertion of generalizability ("across energy transitions") is slightly stronger than what the paper explicitly supports — this is a European analysis — but the structural argument (by-product materials, Ir's platinum-mining coupling, the limits of market signals on constrained supply) does suggest broader applicability.

**No mismatch detected.**

---

## (b) What deep reading added

Deep reading revealed the paper's methodological sophistication that shallow annotation could not capture: the deliberate *lower-boundary* approach (underestimating demand to create a robust finding), the four-dimensional sensitivity analysis, and the critical distinction between "technologies with feasibility issues" (Ga, In, Ir, Te — robust to reserve allocation and intensity improvements) versus "speculative constructs" (thin-film market shares, competing non-energy demand projections). The annotation also did not capture the specific mechanisms of structural bottlenecks — particularly the by-product material trap (Ir cannot be scaled independently of platinum mining) — which represents a qualitatively different constraint than simple scarcity. This mechanism-level detail is essential for understanding why technological innovation alone cannot solve the problem for materials like Ir.

---

## (c) Training signal

**Escalate when:** A paper claims to identify a *systematic omission* in a widely-cited modeling tradition (not just a marginal improvement), uses a lower-boundary methodology that reverses the burden of proof (demand-exceeds-reserves finding is robust even under conservative assumptions), and identifies materials with structural supply constraints (by-products, no primary deposit recovery) rather than mere scarcity. Papers that audit dominant frameworks for category blindness rather than incremental error.

**Don't escalate when:** Shallow notes make broad claims about "fundamental constraints" without evidence that the constraint applies robustly across sensitivity dimensions, or when the paper's scope (regional, sectoral, temporal snapshot) is presented as universal without explicit generalization argument. Avoid escalating resource-depletion papers that treat all material scarcity as equivalent without distinguishing by-product constraints from reserve constraints.

---

## arxiv-2606.12414

# Escalation Assessment: arxiv-2606.12414

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "Introduces the institutional legibility problem as a generative mechanism absent from current inventory; applies to all protocolized systems where cognition distributes across components, not just AI governance."

**Assessment:** The paper does exactly what the escalation annotation claimed. Tallam introduces "institutional legibility" — distinct from interpretability, observability, or explainability — as a failure mode where records survive but the *reading institution* decays. This is genuinely absent from standard AI governance discourse, which conflates preservation with usability.

The claim about generality also holds: the khipu framing is explicitly about *any* distributed cognitive system where interpretation requires institutional continuity, not just AI. The paper even suspends AI-specific concerns (consciousness, legal personhood) to isolate the structural governance problem. The annotation correctly identified this as a conceptual contribution with scope beyond AI governance.

No mismatch. The shallow read's claim was conservative relative to what the paper contains.

---

## (b) What deep reading added

The shallow annotation captured the core conceptual move correctly, but deep reading revealed the *architecture* underlying it: the distinction between three types of epistemic failure (missing evidence, ambiguous evidence, structurally unreadable evidence) and the proposal for "governance workspaces" as a candidate institutional form. More importantly, deep reading exposed that this is a *diagnostic paper* (strong on naming the failure) rather than a prescriptive one (the governance workspace is admittedly underdeveloped), which calibrates how to use its claims downstream.

---

## (c) Training signal

**Escalate when:** A shallow read flags a novel *conceptual primitive* (like "institutional legibility") that reframes a governance failure as a distinct category, especially if it proposes that two concepts standardly conflated (here: preservation and interpretability) are structurally separable, and especially if the move applies across domains beyond the paper's primary context.

**Don't escalate when:** The annotation claims a paper introduces a mechanism but the mechanism turns out to be an intuitive restatement of existing concepts under a new name, or when the generality claim rests on an analogy rather than on a structural argument that applies across cases.

---

## arxiv-2606.12835

# ESCALATION ASSESSMENT

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Annotation claim:** "a primary source developing a sustained theoretical vision (IoAI framework) that directly addresses foundational mechanisms of multi-agent coordination and emergent collective behavior in distributed artificial systems—a domain currently absent from our established laws inventory."

**Assessment:** The annotation's characterization is justified. The paper does:
- Develop a sustained, original framework (IoAI) organized around a coherent conceptual core (*controlled emergence*)
- Address multi-agent coordination as a primary mechanism (Sections 4–7 systematically develop communication, interoperability, resource management, trust)
- Propose emergent collective behavior as the central design challenge, distinct from single-agent capability
- Establish this as a novel domain framing (the "TCP/IP moment for agents")

The annotation does not overstate. The paper is indeed a framework paper, not an empirical contribution; this is transparent in the deep read. The claim about "absence from established laws inventory" is accurate — the paper does address a coordination/emergence domain that is distinct from alignment-of-individual-models, and that domain is underrepresented in current safety/governance research.

No significant mismatch detected. The escalation was warranted.

---

## (b) What deep reading added

The shallow annotation could not have detected (and the deep read revealed) that the paper's greatest conceptual precision lies in the *layered interoperability taxonomy* (Table 3), which operationalizes the framework into six distinct failure modes — and that this taxonomy, combined with the threat model (Table 4), represents the paper's most rigorous and actionable contribution. The shallow read also could not have surfaced the tension Zhu introduces between *autonomy* and *control* as jointly designable rather than opposed, or the subtle claim that *communication itself* (not protocol standardization alone) is the scientific frontier. The shallow annotation was correct about domain novelty but missed where the paper's own scaffolding is strongest.

---

## (c) Training signal

**Escalate when:** A paper claims to establish or substantially expand a *new domain category* (not just solve a problem within an existing domain) by proposing a novel primary mechanism (here: controlled emergence from local interactions) and backing it with a layered taxonomy or systems architecture that maps failure modes to design choices — even without empirical results, if the taxonomy is precise and the case studies illustrate the mechanism coherently.

**Don't escalate when:** A shallow read cites "emerging problem in multi-agent systems" or "framework for coordination" without evidence that the paper proposes a mechanism novel enough to warrant a new conceptual vocabulary, or without a concrete taxonomy that distinguishes failure modes — i.e., when the annotation claims novelty but the paper may just be synthesizing existing theory rather than reframing the domain itself.

---

## arxiv-2606.12848

# Escalation Assessment: arxiv-2606.12848

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper "introduces a formal decision architecture (HLER) for structuring human-machine cognitive labor that operates as a reliability mechanism independent of model capability — a novel mechanism for governance of artificial reasoning systems absent from current inventory."

The deep read confirms this precisely. The paper does introduce HLER (Human-LLM Error Reduction) as a formal architectural framework that isolates reliability as a property of *decision partitioning* rather than model quality — demonstrated empirically by the same model achieving 72% vs. 16% failure rates depending on which gates, sequencing, and commitments surround it. The mechanism is genuinely absent from prior work (which typically argues about model capability rather than workflow structure). No mismatch detected; the annotation identified the paper's actual novelty.

## (b) What deep reading added

Deep reading revealed the theoretical substrate underlying the architectural claim: a Fréchet-distributed task output model that makes a falsifiable prediction (largest reliability gains where task distance from training distribution is greatest) confirmed by the empirical data. It also clarified that the two case studies perform different epistemic work — Case 1 demonstrates *failure prevention*, Case 2 demonstrates *quality-managed degradation* — distinguishing between what the harness actively stops versus what it merely makes transparent. The shallow note could not have captured these mechanistic details or the load-bearing role of the theoretical model in converting an intuitive claim into a testable framework.

## (c) Training signal

**Escalate when:** The shallow annotation identifies a novel *partitioning mechanism* (not just a workflow) that relocates a property (reliability) from one variable (model capability) to another (architectural structure), especially if the claim includes a testable prediction or theoretical model connecting the architectural choice to measurable outcomes.

**Don't escalate when:** The paper proposes procedural best practices or "human-in-the-loop" designs without specifying the formal structure of the partition, the constraint it imposes on information flow, or the mechanism linking the partition to the claimed effect — i.e., workflow recommendations without architecture.

---

## arxiv-2606.13093

# Assessment of Escalation Decision

## (a) Escalation accuracy: `accurate`

**Escalation claim:** "primary theoretical source introducing a sustained formal extension to extensive-form games…by relaxing the implicit completeness assumption; the mechanism of exogenous stochastic action unavailability is absent from current inventory and generalizes to any protocol layer where execution is constrained by environmental uncertainty."

**Assessment:** The escalation annotation is substantially accurate. The paper does introduce a formal model (EFGSAS) that relaxes the completeness assumption in extensive-form games by making action availability stochastic rather than deterministic. However, the annotation's framing is *slightly optimistic* about generalizability: the core theoretical results (compactification via independence assumption, SI-CFR convergence) apply specifically to the ex-interim disclosure regime with independence, not to "any protocol layer." The ex-ante disclosure case remains explicitly unsolved. The mechanism is genuinely novel to the game-theoretic inventory and does generalize beyond specific domains — but with meaningful structural caveats that the annotation elides. The annotation correctly identified this as a foundational extension, not a domain-specific application.

## (b) What deep reading added

Deep reading revealed the *structural severity* of the problem: the exponential (doubly exponential in ex-ante case) representation blowup without independence, and the specific technical architecture that solves it (the DAG-plex compactification via Proposition 4.6). The shallow annotation captured the novelty claim; deep reading exposed why this extension was non-trivial — it invalidates standard regret-minimization theory and forces a new equilibrium computation concept (sleeping internal regret). The annotation's claim about generalizability is now calibrated: it holds under independence, breaks down without it.

## (c) Training signal

**Escalate when:** a shallow read identifies a formal relaxation of a foundational model assumption (e.g., removing completeness, determinism, or common knowledge) where the structural consequences—representation complexity, equilibrium properties, or algorithm design—are plausibly non-local to the specific domain.

**Don't escalate when:** the annotation claims domain-agnostic generalizability ("any protocol layer") without noting domain-specific conditions or unsolved special cases that would be visible only after checking the proof strategy and scope of the main theorems.

---

## arxiv-2606.13405

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper introduces "symbolic constraint embedding as decision-shaping substrate rather than post-hoc monitoring" — a foundational architectural shift for compliance. The deep read confirms this is exactly what the paper proposes: the core argument is that compliance must be *structurally integrated* into the agent's action space via symbolic domain artifacts (regulations, BPMN models, constraint schemas) functioning as primary architectural components, not external monitors. The paper's central conviction — that "the symbolic structures that already exist in regulated industries should function as primary architectural components that co-constitute the agent's reasoning" — directly instantiates the mechanism the annotation identified. The three-property analysis (pre-existing symbolic structure + neural reasoning demands + binary verification requirements) shows why this particular domain makes this architectural claim tractable and necessary. No material mismatch between annotation claim and paper content.

**(b) What deep reading added**

The deep read revealed the paper's load-bearing analytical move: the three-property framing that explains *why* this domain demands neuro-symbolic integration (not just benefits from it) — and critically, the precise rebuttal to the BPM objection, showing that LLM agents' probabilistic opacity reopens a problem classical BPM considered solved. It also exposed the paper's careful bounding of "compliance-by-construction" to structural (not semantic) guarantees, and documented explicit acknowledgment of the expressiveness-verifiability tradeoff that limits what formal verification can achieve. The shallow annotation was sufficient on the architectural principle but could not have surfaced the domain-specificity argument or the honest scope limitations.

**(c) Training signal**

Escalate when: a position paper claims an architectural reframing of how a structural property (compliance, security, governance) *should live* in a system, grounded in analysis of why existing approaches are architecturally insufficient for a specific high-stakes domain with pre-existing symbolic structure.

Don't escalate when: papers claim incremental improvements to monitoring or post-hoc detection mechanisms without addressing the architectural question of where domain structure belongs in the system design.

---

## arxiv-2606.13621

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper "reframes a standard safety mechanism (runtime enforcement) as a design-time analytical instrument, introducing a novel methodological lens (defensibility analysis)." This is precisely what the paper does. The deep read confirms: the core contribution is *not* a new algorithm but a reframing of the same LTL-to-DFA-to-product-game pipeline from a runtime enforcement tool (where it fails due to state explosion and deployment fragility) into a design-time analytical instrument whose output is a formal "defensibility verdict"—a provable binary certificate of whether a system is defensible under adversarial attack. The asymmetric dual-specification game is the technical enabler of this reframing, and the defensibility fingerprint extends it operationally. The annotation's claim that this "may generalize across protocolized systems" is supported by the paper's framing, though not empirically demonstrated beyond one 5-node topology family (which the authors acknowledge). No mismatch.

**(b) What deep reading added:**

The shallow note could not have captured the load-bearing role of the asymmetric specification treatment—the fact that flipping φ_A and φ_D in the attractor computation would collapse the entire state space into the attractor, making constrained adversarial analysis impossible—or the decoupling finding that topology perturbations and specification perturbations move the two-layer system (formal + MARL) coherently or independently in systematically different ways. The shallow note identified the reframing; deep reading showed *how* it works and where its boundaries lie.

**(c) Training signal:**

"Escalate when: a paper claims to reframe an established method's role or output (not improve the method itself) and the annotation explicitly names that reframing as the novelty, especially if it resolves an epistemic gap the shallow read can identify." — "Don't escalate when: the annotation emphasizes generalizability or applicability across domains but the paper's empirical work is confined to a single instance (5-node network, one topology family) and explicitly marks that scope as uncharacterized."

---

## arxiv-2606.13835

# ASSESSMENT: arxiv-2606.13835

## (a) Escalation accuracy: `accurate`

**Escalation claim:** "systematic validation framework (mobility laws, temporal rhythms, network motifs, semantic transitions, behavioral profiles) that operationalizes the plausibility-realism gap…with generalizable diagnostic value across LLM-based simulators."

**Assessment:** The paper delivers exactly this. The five-dimensional framework (spatial, temporal, motifs, behavioral profiles, semantic) is the paper's core methodological contribution. The plausibility-realism distinction is indeed load-bearing and does operationalize a foundational gap in agent simulators. The framework is presented as generalizable and is applied across two different simulators (AgentSociety, CitySim), lending credibility to portability claims. The escalation annotation correctly identified the paper's primary value: not new empirical findings about urban mobility per se, but a reusable diagnostic apparatus for comparing simulators against human behavioral regularities. No mismatch detected between annotation and paper.

## (b) What deep reading added

The deep reading revealed the paper's most interesting empirical finding—not stated prominently in the abstract—that realism dimensions are *coupled* in real data but *independent* in simulators, so improving one (e.g., spatial via richer destination-selection) can degrade another (e.g., temporal dwell time). This cross-dimensional trade-off is the mechanism that explains why simulators can appear plausible while failing realism systematically. The shallow annotation captured the framework; deep reading exposed why the framework matters methodologically.

## (c) Training signal

**Escalate when:** A paper introduces an **orthogonal diagnostic framework** (five or more independent dimensions) applied to a known plausibility problem in generative agents, with empirical instantiation across ≥2 systems and explicit framing of the measurement protocol as reusable—especially if the framework disaggregates a conflated concept (here: plausibility vs. realism) into falsifiable components.

**Don't escalate when:** A shallow note claims "systematic validation framework" but the paper offers only post-hoc criticism of one simulator or a unidimensional metric applied to a single system, or when the framework is presented as task-specific rather than generalizable.

---

## arxiv-2606.14533

# ESCALATION ASSESSMENT: Arxiv-2606.14533

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "identifies a fundamental mechanism by which statistical fidelity metrics (variance preservation) systematically decouple from decision-critical signal in protocolized systems, with catastrophic consequences for rare-event detection."

**Assessment:** The paper delivers precisely this. Theorem 1 (Information Erasure) formally proves that PCA can retain >99.9999% of variance while retaining zero mutual information about rare classes. Theorem 2 (Bayes Collapse) shows this isn't a numerical accident—the optimal classifier collapses to a constant predictor. The Risk Shadow is defined (Definition 6) as exactly the phenomenon described: a representation where conventional metrics (variance, accuracy) appear excellent while tail risk is unbounded and invisible to standard auditing.

The escalation annotation's framing of "systematic decoupling" and "catastrophic consequences for rare-event detection" matches the paper's core argument. The claim about "protocolized systems" is slightly broader than the paper's scope (which focuses on decision-theoretic consequences rather than governance specifically), but the mechanism is sound and the consequences are indeed catastrophic for any downstream system making decisions under asymmetric loss.

No mismatch detected. The annotation understated neither the rigor nor the scope.

---

## (b) What deep reading added

The deep read revealed the **hierarchy of failed alternatives** (TP-PCA, exPCA, exp2PCA) with rigorous failure analysis. Critically, Theorem 3 proves that TP-PCA fails *by design*—the centering correction μ_w μ_w^T suppresses discriminative variance regardless of sample reweighting α. This is not an implementation detail but a structural impossibility, which the annotation could not have captured. The deep read also exposed the author's epistemic boundaries: the multi-agent extension (Section VIII) and accountability framework (Section VII) are programmatic rather than developed, signaling where the paper's confidence ends. The shallow note was conceptually accurate but missed the constructive solution path and the precise locus of the alternative methods' failures.

---

## (c) Training signal

**Escalate when:** A paper claims a formal orthogonality or incompatibility between two widely-used objectives (e.g., variance maximization vs. tail-risk minimization) and proves it via construction + theorem with worked counterexamples showing the failure is invisible to standard metrics.

**Don't escalate when:** A paper demonstrates that two objectives are "different" or "trade off" without showing formal or structural incompatibility, or when the rare-event failure is predictable from existing theory (e.g., known imbalance effects) rather than arising from a hidden geometric property of the representation.

---

## arxiv-2606.14769

# ASSESSMENT: arxiv-2606.14769

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "A game-theoretic and microeconomic framework for valuing agentic AI systems as productive agents within organizational workflows, moving beyond isolated technical benchmarking to integrated [outcome measurement]."

**Assessment:** The paper delivers exactly this. Zhu proposes Agentomics as a subdiscipline grounded in Shapley-value attribution applied to workflow-level coalition surplus, explicitly rejecting benchmark scores as the valuation metric. The core contribution is the formalization of agent value as relational (determined only within coalitions relative to a human baseline), not intrinsic. The SOC case study demonstrates that economically optimal agent selection diverges from reliability-maximizing selection, supporting the paper's central diagnostic: isolated technical metrics are systematically misaligned with economic contribution.

The shallow annotation captured the essential claim accurately. No mismatch detected between annotation and content.

---

## (b) What deep reading added

Deep reading revealed the mathematical load-bearing structure: the multiplicative reliability bottleneck model ($L_F \cdot (1 - \prod_k \rho_k)$) that makes workflow value highly nonlinear in agent reliability, and the deliberate normalization of coalition value against a human baseline rather than absolute productivity. It also exposed the paper's honest acknowledgment that its own case study workflow value function is heuristically stipulated, not derived — a constraint on the framework's current applicability that the shallow note could not have captured without reading the methodology section.

The deep read confirmed the framework is primarily normative and formal rather than empirical or predictive.

---

## (c) Training signal

**Escalate when:** A paper introduces a formal framework (especially one importing tools from an adjacent discipline like game theory or mechanism design) that redefines the valuation or measurement object for a class of systems you care about, particularly if the annotation explicitly flags the definitional reframing as the core contribution rather than a technical improvement to existing measurement.

**Don't escalate when:** The shallow note describes the framework claim but doesn't signal whether it's grounded in empirical validation or remains a normative proposal; store-only papers that are framework-building exercises without significant case-study or deployment grounding often don't warrant deep reading unless they claim empirical validation they may not deliver.

---

## arxiv-2606.14818

# Escalation Assessment: arxiv-2606.14818

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper "introduces a foundational mechanistic shift from reactive to predictive dynamics" and "proposes cost-function formalism as generalizable substrate for anticipatory behavior across living and artificial collectives."

The deep read confirms this is precisely what the paper does. The core contribution is a formal mapping that treats anticipatory agents in d dimensions as equivalent to non-anticipatory chains in (d+1) dimensions, where the extra dimension encodes temporal prediction. This is not a perturbative add-on to reactive equations (the "mechanistic shift") but a categorical reconceptualization. The cost-function framework is indeed derived statistically from observed trajectory distributions rather than assumed rationality, making it a genuinely generalizable substrate tested on both pedestrian crowds and (implicitly extensible to) other active matter systems.

The annotation slightly undersold the philosophical contribution: the paper is careful to ground "cost" not in rationality but in statistical reconstruction, which is a stronger and more generalizable foundation than a shallow read might suggest. But the core claim—foundational shift + generalizable cost formalism—is borne out.

## (b) What deep reading added

The deep read revealed the internal architecture of the solution: the "shared base universe" approximation as a practical simplification that trades N-dimensional multi-agent prediction for a common field, the emergence of the anticipation horizon as a density-dependent cutoff (not a fixed parameter), and the natural decomposition of decision timescales (strategic vs. tactical vs. operational) from uncertainty structure alone. The pedestrian results section shows the formalism is not merely elegant but empirically generative—it reproduces lane formation, yielding, and static crowd crossing where existing models fail, without scenario-specific tuning. The shallow annotation captured the conceptual novelty; deep reading demonstrated it has both formal rigor and predictive teeth.

## (c) Training signal

**Escalate when:** A paper claims a categorical restructuring of a foundational concept (reaction → anticipation; individual → polymer chain) backed by formal mapping, AND applies it to a system where existing reactive models provably underperform, AND grounds universal parameters (cost function) in statistical reconstruction rather than assumed rationality.

**Don't escalate when:** A paper proposes adding a new term or parameter to existing equations, or claims "unification" across systems without demonstrating novel empirical predictions in at least one domain where baseline models fail.

---

## arxiv-2606.14819

# Escalation Assessment: arxiv-2606.14819

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper introduces "aggregate metric opacity masking concentrated harm in modular topologies" and "directly challenges sufficiency of aggregate validation as governance assurance."

The deep read confirms both. The paper's core finding is precisely that standard aggregate metrics (accuracy, F1, etc.) are arithmetically blind to position-concentrated errors: bridges comprise 12% of nodes, so their misclassifications dilute to near-zero when averaged (p.26). Experiment 1–3 establish this invariance across 15× punishment-cost sweeps. The mechanism is structural, not a weak artifact. The paper introduces a diagnostic decomposition (Lgov with separate terms for LFN, LFP, Lcontrol) that *does* register position-specific harm that aggregate metrics miss.

The annotation's claim about generalization "beyond moderation to any protocolized control on heterogeneous networks" is slightly forward of what the paper explicitly demonstrates (the model is idealized, N=240, homogeneous block structure), but the paper itself makes this theoretical case, and the scope conditions are honestly stated (p.30).

No mismatch between annotation and content.

---

## (b) What deep reading added

The shallow annotation could not have captured the *quantitative grain* of the mechanism: the specific arithmetic (12% bridge population → near-zero dilution), the ANOVA p=0.96 invariance result, or the critical finding that bridge *degree* (not betweenness) drives the effect in the base one-hop model, only shifting to betweenness under multi-hop cascades at pout=0.03 (which the author explicitly flags as a scope condition not matched to the base finding). Deep reading also revealed honest negative results (Experiment 10: bridge weighting carries *no* consequence in the base model), the adaptive bandit's specific failure mode (reward signal misalignment with Lgov), and crucially, Itkin's exceptional clarity about where directional trends remain unconfirmed (p.27) and where cascade results cannot yet claim backing at demonstrated inter-community densities. The shallow note was sufficient for *gating significance*; deep reading showed the paper's true value: a mechanism-demonstration with disciplined scope boundaries.

---

## (c) Training signal

**Escalate when:** a shallow read identifies a claimed mechanism that (a) is absent from current inventory, (b) has clear scope conditions stated, and (c) the annotation itself quotes a specific structural or arithmetic reason it should matter (e.g., "aggregate metrics arithmetically dilute position-specific harm").

**Don't escalate when:** an annotation claims a general governance or network finding without naming a specific structural mechanism, or uses terms like "challenges sufficiency" without pointing to a concrete model, metric, or trade-off that makes the challenge visible (vs. merely asserted).

---

## arxiv-2606.15376

# Assessment: arxiv-2606.15376

## (a) Escalation accuracy

**Verdict: `accurate`**

The escalation annotation claimed the paper would identify "a fundamental mismatch between classical concurrency protocols and LLM-agent dynamics—introducing a mechanism (opacity of read sets, minute-scale transactions, live-state mutation constraints) absent from current protocol theory."

The paper **fully delivers** on this claim. It explicitly diagnoses the dual failure mode:
- **Performance gap:** minute-scale transactions + broad read sets make locks and abort-retry prohibitively expensive
- **Functionality gap:** live external state (K8s clusters, production databases) cannot be forked or rolled back

The mechanism is precisely as claimed: opacity of read sets (agents reason locally about stale data), minute-scale transactions (canary example spans 6–29 seconds), and live-state mutation constraints (no buffer layer, writes apply speculatively in place). The paper grounds this in concrete infrastructure (Kubernetes) and demonstrates a protocol (MTPO) that exploits agent capabilities (semantic judgment, targeted repair, inverse actions) to sidestep classical remedies.

The shallow annotation's connection to "H-001's intuition that agent synchronization differs structurally from classical systems" is validated: the paper's core move is showing that when transacting entities can *understand their own situation and repair themselves*, the entire concurrency-control problem changes category.

---

## (b) What deep reading added

The shallow note captured the conceptual innovation (mismatch + mechanism), but deep reading revealed the full architectural insight: the protocol works by delegating *three different kinds of repair* to three different agents—LLM judgment for semantic relevance, mechanical inverse-based reordering for write ordering, and ToolSmith for tool registration. This layering (human-level reasoning + deterministic undo + online tool synthesis) is the design sophistication that makes MTPO work in practice. Deep reading also surfaced the critical load-bearing assumption (A3: self-healing accuracy at 95%) and the empirical speedup (1.43×) with concrete failure modes (canary anomaly), which the shallow read couldn't access.

---

## (c) Training signal

**Escalate when:** A paper claims a structural mismatch between classical abstractions (transactions, serializability, locking) and a new problem domain (LLM agents, continuous state, semantic repair), and grounds it in a concrete infrastructure failure mode (live state can't be rolled back, agents operate at minute scale) — especially if the proposed mechanism reverses the control flow (advisory rather than mandatory).

**Don't escalate when:** A paper claims "LLM agents need coordination" without identifying what classical theory *breaks* under agent semantics, or proposes a general "agent framework" without drilling into why existing distributed-systems solutions fail on the specific constraints of the domain (timescale, state mutability, agent reasoning).

---

## arxiv-2606.15435

# Assessment: arxiv-2606.15435

---

## (a) Escalation accuracy

**Verdict: `over-claimed`**

**Escalation claim:** "a general solution method applicable across a class of artificial systems"

**Assessment of mismatch:**

The paper does establish a decomposition structure (pooling-then-revealing) for a *specific* class of games: two-player zero-sum linear-quadratic differential games with binary incomplete information about one player's control matrix. However, the "general solution method" framing is misleading:

1. **Scope is narrow, not general.** The approach applies only to LQ games with a binary type space and a simplified information structure (belief collapse to certainty upon distinguishability). The authors explicitly acknowledge that extending to continuous type spaces or full Bayesian equilibrium remains open. [deep notes, §2, point 3]

2. **Solution method is incomplete.** Propositions 2 and 4 reduce the problem to optimizing over a single scalar (revelation time s̃), but:
   - The authors do not prove uniqueness or existence of an interior optimum — Proposition 5 only provides a gradient for *computing* s̃ once you decide to search.
   - The ex-interim incentive constraint (will P2 *want* to stick with pooling after learning their type?) is explicitly deferred as an unresolved problem. [deep notes, §2, point 5; deep notes, §3]
   - This is a reduction in dimensionality, not a closed-form or algorithmic solution.

3. **Application to "artificial systems" is vague and unsupported.** The paper offers one numerical example (pursuit-evasion) but makes no claim about scalability or robustness across different LQ problem classes.

**The shallow annotation conflates structural insight with methodological generality.** The decomposition is real and novel; the generality is overstated.

---

## (b) What deep reading added

The shallow annotation captured the core structural insight (pooling-then-revealing decomposition), but deep reading revealed: (i) the framework is much more constrained than "general solution method" suggests — limited to binary types, simplified beliefs, and incomplete analysis of incentive compatibility; and (ii) the paper's actual innovation is *conceptual* (formalizing deception as an equilibrium phenomenon in differential games), not methodological (there is no turnkey solver or unified algorithm offered). The deep read also exposed that the paper is positioned as a first step opening a research direction, not a complete solution.

---

## (c) Training signal

**Escalate when:** A paper claims a "decomposition" or "structural solution" for a class of games or optimization problems and provides a Proposition showing that equilibrium must factorize into distinct phases with analytically tractable sub-problems, even if the final step (e.g., selecting a parameter connecting the phases) remains numerical — this signals a genuine theoretical advance worth checking for overclaiming.

**Don't escalate when:** The shallow annotation uses words like "general," "applicable across," or "solution method" without specifying the problem class, boundary conditions, or whether uniqueness/existence/incentive compatibility has been verified — these are flags for projection rather than careful reading.

---

## arxiv-2606.15563

# Escalation Assessment for arxiv-2606.15563

## (a) Escalation accuracy: **accurate**

The escalation annotation claimed the paper proposes "a foundational variational principle (MSO) for autonomy allocation in delegated systems" and introduces "uncertainty-calibrated governance burden" as a mechanism absent from current inventory.

The deep read confirms both claims substantially. The MSO (Minimum Sufficient Oversight) is indeed derived as a rigorous variational principle on the Fisher information manifold, with an explicit water-filling solution (Theorem 1). The "masking index" M* = σ_corr/σ_raw is a novel, formal mechanism capturing how correctors obscure raw agent competence—this is precisely the kind of uncertainty-calibrated governance machinery the annotation anticipated. The paper does generalize across multi-agent topologies (chains, fans, diamonds) with topology-dependent masking accumulation laws.

Minor: The annotation slightly overstates generality ("multi-agent AI architectures"). The paper validates on a software-delivery pipeline and synthetic simulations, not across heterogeneous agent types or production systems. But the framework is architected to extend; this is underambition in application, not overreach in principle.

---

## (b) What deep reading added

The deep read revealed that masking is not presented as a separate pathology requiring independent motivation—it emerges *structurally* from the dual-signal framework (raw vs. corrected competence), which is the paper's genuine conceptual innovation. The shallow annotation missed the load-bearing architectural move: the paper derives not just the allocation principle but also a **capacity ceiling** (delegation capacity) and a **complexity tax** (Proposition 2: process entropy linearly erodes achievable quality), creating a complete governance geometry. The shallow note was sufficient to identify escalation-worthiness but could not have captured that the paper's real contribution is making the *dependencies between* allocation, quality, workflow complexity, and time computable—not just one of these in isolation.

---

## (c) Training signal

**Escalate when:** The paper proposes a new formal principle (variational, information-theoretic, or game-theoretic) that solves a governance or safety problem previously treated heuristically, introduces a novel primitive or measurement (masking index, effective autonomy buffer) with algebraic or information-geometric grounding, and is explicitly positioned to generalize across a family of system topologies or agent types, even if validation is limited to one domain.

**Don't escalate when:** The paper claims to formalize a heuristic but relies on empirical coefficient fitting (λ ≈ 0.02/bit) for load-bearing equations, validates only on synthetic workflows with acknowledged 20% overestimation, or uses "foundational principle" language while the core result (e.g., Proposition 2) is marked as local first-order approximation without global tightness guarantee.

---

## arxiv-2606.15960

# Assessment: arxiv-2606.15960

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "foundational mechanism (task chaining as a restructuring principle) that redefines how comparative advantage operates under AI integration, with claimed non-linear productivity implications that generalize across firm organization regardless of sector."

**Assessment:** The paper fully delivers on this claim. The deep read confirms:

1. **Task chaining as foundational mechanism**: The step/task/job hierarchy and the AI chain concept (contiguous steps bundled with a single human verification at the boundary) is indeed the paper's core theoretical contribution, not peripheral.

2. **Comparative advantage redefined**: The paper explicitly shows that standard comparative advantage fails when verification is a fixed cost of chain boundaries rather than per-step. A step optimally automated despite preferring human execution in isolation—this is a genuine reframing, not a minor caveat.

3. **Non-linear productivity**: The fragmentation index (Proposition 5) and threshold effects (Example 6, pp.24–25) directly establish that marginal AI improvements have flat, then discontinuous impact depending on sequential structure, not comparative advantage alone. This is non-linear as claimed.

4. **Generalization claim**: The theory makes no sector-specific assumptions. Empirical validation uses O*NET occupation-level data (cross-sector) and GPT workflow modeling. The micro-foundation for CES aggregation (pp.25–31) claims to explain macro patterns regardless of sector composition.

**No mismatch detected.** The escalation annotation was appropriately specific and the paper contains exactly what was flagged.

---

## (b) What deep reading added

The shallow note could not have detected that the paper's most novel theoretical result—the failure of comparative advantage due to fixed-cost verification at chain boundaries—is *localized to a specific architectural assumption* (human verification only at the final step) and that the paper's own fragmentation index is an *approximation* (guaranteed within 1/8 to 5/4 of optimal, not exact). Deep reading also revealed the paper's deliberate scope limitation: step sequencing is exogenous, and hand-off costs don't themselves respond to AI. These constraints are stated but should temper claims about "redefining" work organization—the model works within a narrower domain than a shallow annotation might assume.

---

## (c) Training signal

**Escalate when:** a paper claims to formalize a qualitative intuition (e.g., "why doesn't automation happen smoothly?") by identifying a *structural property* (e.g., sequential dependencies, cost asymmetries) that inverts a standard assumption (comparative advantage) and yields non-linear predictions testable against cross-sectional occupational or firm data.

**Don't escalate when:** a paper applies an existing mathematical model to a new domain (e.g., "CES functions apply to AI adoption") without identifying a novel mechanism that reorders which agent or dimension dominates in the model.

---

## arxiv-2606.16326

# Escalation Accuracy Assessment

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper "introduces mechanism for operator adversarialism in runtime contracts" and "formalizes five distinct attack surfaces absent from prior inventory." 

The paper substantively delivers both. The five-attack taxonomy (Definition 2: within-boundary splitting, post-toll safe-default selection, cross-boundary re-routing, interface-compliance gaming, model-identity misreporting) is genuinely inventoried here for the first time in this substrate. The mechanism design response—three new contractual clauses (common-control aggregation, interface-compliance adjudication, model-identity menu with penalty schedules)—directly addresses operator strategic behavior in a runtime pricing context that prior work (Paper A) had treated as a passive problem. The annotation's framing as "foundational gap in artificial law enforcement" is accurate: this is the layer where incentive compatibility and safety separate, and the paper does formalize that separation.

No mismatch detected. The annotation slightly undersold the technical depth (it is Myerson-grade mechanism design, not just attack cataloging), but made no false claims.

---

**(b) What deep reading added**

The deep read revealed the compositional architecture: that the five attacks are *sequentially closed* in a specific order (Lemma 21), and that this order matters because attacks (a)–(d) must be closed *uniformly* before attack (e) becomes the only remaining strategic degree of freedom. This dependency structure—and the proof that joint IC follows from sequential closure plus Myerson's binding-IC characterization—is not recoverable from the attack taxonomy alone. Deep reading also exposed the acknowledged limits (negative premiums, adversarial conformal calibration as a sixth unclosed surface, welfare non-optimality) that reframe the paper's scope as a necessary-but-incomplete step, not a complete solution.

---

**(c) Training signal**

**Escalate when:** A paper formalizes a *new attack taxonomy* on a previously-passive actor (operator, principal, deployer) in a safety-critical substrate AND proposes mechanism-design closures that exploit structure-specific leverage (e.g., super-additivity, detection probability thresholds, menu separation). The novelty is substrate + taxonomy + proof of minimality, not just cataloging.

**Don't escalate when:** A paper claims to close an attack surface but relies on unvalidated parameter assumptions (Remark 10's parameter sweep over Vθ, Cfail,θ) or defers a constraint (Assumption 18, individual rationality) to "hypothesis" status without proving feasibility. Shallow notes claiming "foundational gap" without evidence of prior work's actual scope are over-selling.

---

## arxiv-2606.16475

# ESCALATION ASSESSMENT

---

## (a) Escalation accuracy: `accurate`

**Escalation claim:** "Presents sustained empirical evidence of a fundamental asymmetry in human-AI interaction (persuasion capacity) that generalizes across multiple human skill classes and introduces a mechanism—information design under optimization—absent from current inventory."

**Assessment:** The escalation annotation is substantially accurate, though it slightly mislabels the mechanism.

The paper *does* present sustained, preregistered empirical evidence across four studies that AI systems out-persuade elite humans (debaters, selected laypeople, professional canvassers) even under conditions optimized for human performance. The effect generalizes across skill classes: +4.6 pp vs. world-champion debaters, +5.9 pp vs. professional canvassers, +10.8 pp in real-stakes donation behavior. This is exactly what the annotation claimed.

However, the mechanism is **not** "information design under optimization" in the sense of adversarial content crafting. The actual mechanism is **information throughput** — the rate at which fact-checkable claims can be produced per unit time. The paper's load-bearing result is that when AI is constrained to human word-count and response-delay, the persuasion gap collapses to zero. The mechanism is structural/quantitative (speed × volume), not qualitative design. The annotation uses the right conceptual frame (mechanism is absent from inventory) but mislabels what the mechanism is. This is a minor but meaningful mismatch: the deep read reveals the mechanism is simpler and more mechanical than "design under optimization" implies.

---

## (b) What deep reading added

The shallow annotation correctly identified the paper's core claim (asymmetry across skill classes) but omitted the critical mechanistic finding: the gap is entirely explained by **information throughput per conversation**, not by superior argument quality or persuasive sophistication. The deep read revealed the causal structure: when word-count and response-time are matched, AI's advantage vanishes (Δ = 0.0 pp, p = .96). This is a structural insight about *how* AI's persuasive advantage arises—it's not about being smarter or more empathetic, but about being faster at deploying facts—and it substantially narrows the space of possible explanations.

---

## (c) Training signal

**Escalate when:** The annotation cites a claimed mechanism (e.g., "information design," "optimization," "algorithmic advantage") that, if present and causal, would be novel to the influence/coordination literature *and* is testable via ablation or constraint experiments. Preregistration + real human comparators (expert or professional) + n > 5,000 is a reliable signal of warranted escalation.

**Don't escalate when:** The annotation claims a mechanism but either (i) the paper only demonstrates the effect, not the mechanism (no ablation/constraint tests), or (ii) the paper conflates the mechanistic label with its operationalization (e.g., calling "fact density" the mechanism rather than a trace of throughput). Papers with vague mechanism claims and n < 1,000 across condition should stay shallow.

---

## arxiv-2606.16710

# ASSESSMENT: arxiv-2606.16710

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "Identifies a novel failure mode (error propagation through agent interaction layers) absent from current inventory; empirically demonstrates that intent-agnostic systems degrade under misinformation injection; suggests generalizable mechanism of reliability collapse in coordinated protocolized systems."

**Assessment:** The paper does contain all three elements, though with important qualifications:

1. **Novel failure mode**: Yes. The "benign MAS misinformation" scenario (contaminated context, no adversarial actors, faithful protocol-following) is genuinely underexplored. The paper carves out a distinct niche between single-LLM robustness and adversarial multi-agent attacks.

2. **Intent-agnostic systems degrade under misinformation**: Partially accurate but requires refinement. Single agents do degrade (17–27% loss), but multi-agent debate *partially mitigates* this (only 2.2–10.3% loss). The system is not simply "degraded"—it's partially self-correcting. The escalation framing slightly oversells the fragility.

3. **Generalizable mechanism of reliability collapse**: This is where the escalation slightly over-claimed. The paper identifies *task- and model-dependent* thresholds for error correction (sharp jump at 3/5 misinformed agents), but stops short of proposing a generalizable formal mechanism. The finding is structural and interesting, but the paper is empirical-descriptive rather than mechanistic. The "collapse" framing is evocative but the paper shows *conditional stability*, not collapse.

**Mismatch summary:** The escalation correctly identified that this paper addresses an underexplored failure mode with solid empirical work. However, it slightly over-emphasized fragility (the partial mitigation is as important as the degradation) and over-generalized the mechanistic content (the paper maps conditions for error correction without proposing a transferable model).

---

## (b) What deep reading added

The deep read revealed that the paper's most novel contribution is not the misinformation degradation itself (which is expected) but the **sharp, threshold-dependent correction dynamic** (Figure 5: <50% misinformed agents → 8–10% self-correction; ≥60% → 77–90%). This nonlinear transition is structurally interesting and absent from the shallow annotation. Additionally, deep reading exposed important limitations (same model for MINT generation and evaluation; machine-generated misinformation; fixed debate structure) that constrain generalizability claims—the shallow note's "generalizable mechanism" framing needed this qualification. The shallow annotation captured the niche correctly but missed both the threshold finding and the honest limits that contextualize it.

---

## (c) Training signal

**Escalate when:** A paper carves out a *specific, underexplored niche* (benign MAS + misinformation, not adversarial; single-agent vulnerability already known) with careful empirical comparison (relevant vs. irrelevant misinformation, isolating semantic intent) and reports nonlinear or threshold-dependent effects (sharp correction jump at agent composition thresholds) that map conditional robustness rather than simple degradation.

**Don't escalate when:** A paper uses evocative framing ("reliability collapse," "generalizable mechanism") that conflates partial mitigation with fragility, or proposes mechanisms without grounding them in transferable formal models; also when the same model generates and evaluates artifacts (self-preference confound acknowledged but not resolved).

---

## arxiv-2606.17081

# Assessment of Escalation Decision

## (a) Escalation accuracy

**`accurate`**

The escalation annotation claimed: "First formal game-theoretic treatment of a widely-deployed inference architecture class; introduces mechanism (hierarchical resource competition with positive externalities) absent from current inventory; generalizable beyond GPU serving to any disaggregated compute substrate."

The paper **does deliver all three claims**:
1. **First formal game-theoretic treatment**: Confirmed. The paper is the first to decompose Dynamo's (NVIDIA's production disaggregated inference system) into three coupled games (prefill-decode competition, KV cache hierarchy, request routing) and derive their equilibrium structure.
2. **Mechanism absent from inventory**: Confirmed. Game 3 (routing game with positive cache-overlap externality breaking potential game structure) and Game 2's hierarchical KV caching game with O(√n) PoA bounds on sparse topologies are novel mechanistic insights. The positive externality from KV cache overlap is explicitly noted as violating standard congestion game assumptions.
3. **Generalizable beyond GPU serving**: Confirmed. The paper explicitly frames the mechanism as applicable to "any disaggregated compute substrate" and the game-theoretic vocabulary (GNEP, congestion games, hierarchical resource competition) is substrate-agnostic.

No mismatch detected between annotation claim and actual content.

---

## (b) What deep reading added

Deep reading revealed two critical insights the shallow note could not capture: (1) **methodological reframing**: the paper's core value is *analytical naming and regime diagnosis*, not algorithmic optimization—Georgiou shows that game theory's power here is in measuring equilibrium properties that production systems already compute, providing vocabulary for existing phenomena rather than new runtime algorithms. (2) **The saturation regime transition as a control signal**: the empirical discovery that PoA is stable below saturation (invariant to router parameters ±0.08–0.10) but explodes above it (37–58× variance emergence), with the transition detectable via second-derivative analysis, is the load-bearing empirical result that justifies the game-theoretic framing—it redefines what "adaptive control" should target. The shallow note's claim of "generalizable" mechanism was correct but missed that the paper's novelty is equally in *measuring when and why the mechanism matters operationally*.

---

## (c) Training signal

"Escalate when: a paper claims to apply an established mathematical framework (game theory, mechanism design, complexity theory) to a production system class, and provides evidence that the framework reveals hidden structure or regime transitions not visible to the engineering community using that system currently." 

"Don't escalate when: the annotation merely claims 'first application of X to domain Y' without specifying what novel mechanistic insight or regime-dependent behavior the framework uncovers—purely novelty-of-application claims without structural content warrant shallow confirmation only."

---

## arxiv-2606.17182

# Assessment: arxiv-2606.17182

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "formalizes a mechanism (concurrency anomalies under deterministic semantics in multi-agent LLM state-sharing) absent from the current inventory and directly addresses consistency laws in distributed artificial systems, with formal grounding in TLA+ and counterexamples."

**Assessment:** This claim is met. The paper does formalize four concurrency anomalies (A1, A2, A3, A6) specific to the multi-agent LLM state-sharing regime — a regime genuinely absent from classical database or distributed systems consistency theory. The mechanism is precisely the unbounded-latency generation phase that breaks assumptions in both hardware isolation and database snapshot models. The formal grounding is real: TLA+ specifications, TLC counterexamples (demonstrating anomalies in toy histories), Verus mechanical verification with zero unproven obligations, and Rust runtime implementations with verified sound/complete detectors. The deep read confirms the annotation was not over-claiming. However, the claim is slightly *under-precise* about what "theoretical contribution" means here: Khan explicitly disclaims that the phenomena are theoretically novel (they are structural ports of classical anomalies) or that the lattice is canonical. The novelty is the *mechanized verification chain and operational regime characterization*, not new consistency theory. The annotation's phrasing ("formalizes a mechanism") is accurate but doesn't flag that this is primarily a *verified engineering artifact* with scrupulous scope honesty.

---

## (b) What deep reading added

Deep reading revealed that the paper's most load-bearing intellectual move is the **snapshot-insufficiency observation** — that structural snapshot semantics fail for unbounded-latency operations even when individual reads are consistent, a finding that parallels write-skew under snapshot isolation but has not been formalized for this regime before. It also confirmed that the empirical findings are appropriately caveated as workload-governed sensitivity checks, not prevalence claims, and that the verification itself (274 Verus obligations, three documented stubs, zero assumes) is the substantive methodological contribution — this is not stated in the escalation annotation at all. The shallow note captured the formalization and anomaly enumeration but missed Khan's explicit self-positioning: this is *honest-scope engineering*, not theoretical novelty-hunting.

---

## (c) Training signal

**Escalate when:** A paper claims to formalize operational anomalies in a new regime (unbounded-latency state-sharing) with mechanical verification (TLA+, proof checkers, deployed runtimes) *and* explicitly disclaims theoretical novelty of the phenomena themselves — this signals mature scope honesty and a testable artifact, not overreach.

**Don't escalate when:** A paper claims to discover concurrency anomalies but only offers informal examples and pattern descriptions without either (i) mechanical verification of the detection/prevention logic or (ii) honest acknowledgment that the phenomena are regime-specific instantiations of known forms — the annotation alone will reveal over-claiming without deep read.

---

## arxiv-2606.17503

# ESCALATION ASSESSMENT

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:** "identifies settlement legibility as a mechanism governing which uncertainties become institutionally tradable — a foundational constraint on what artificial systems (prediction markets as protocols) can 'see' or operationalize"

**Assessment:** The paper does exactly this. Adegbenro develops settlement legibility as an operationalized construct (D1: template repeatability, D2: settlement determinacy, D3: closure precision) and demonstrates empirically that the inventory of prediction market contracts is steeply stratified by this property—sports and elections at ceiling (mean ~3.99), security/conflict at floor (0.67). The mechanism is not aspirational: it is instantiated in the codebook, measured across 292–4 contract pairs, and shown to correlate with contract formation even though the formation test itself narrowly missed pre-registered acceptance thresholds (p=0.056 vs. threshold α=0.05; tercile gap 10.1pp vs. 20pp target). The paper's core claim—that the market's *visible* inventory is filtered by institutional settlement properties, not just by trader demand or public interest—is directly supported. The escalation annotation correctly identified this as the load-bearing insight.

No overclaim. The paper is appropriately cautious about the formation test's failure and does not promote it post hoc. The negative value-legibility corollary among listed contracts is pre-registered and well-explained as collider bias. The mechanism is real, measurable, and consequential for understanding protocol-reality coupling.

---

## (b) What deep reading added

The deep read confirmed the escalation annotation's claim but added critical methodological specificity: the paper is *unusually well-disciplined*, with pre-registration, explicit failure-reporting on the formation test (β₁=0.433, p=0.056 vs. α=0.05), and a corollary prediction about negative value-legibility that was written down before estimation and then observed (explained as collider bias from conditioning on listing). This rigor and transparency were not captured in the shallow annotation and materially strengthen confidence in the mechanism's reality. The deep read also refined the construct itself: settlement legibility is narrower and more operational than "legibility" in my broader vocabulary—it is specifically the *administrative* legibility of an event from a dispute-resolution apparatus's perspective, not general readability. This precision is crucial for operationalization.

---

## (c) Training signal

**Escalate when:** a shallow annotation identifies a novel causal mechanism (not just correlation or noise) backed by a pre-registered empirical design on a real market or protocol, even if the focal test narrowly misses acceptance criteria—the methodological discipline and transparent failure-reporting are signals that the mechanism is real and the paper merits full technical reading.

**Don't escalate when:** a shallow annotation claims to identify a mechanism but does not specify the operational construct, measurement procedure, or pre-registered acceptance criteria, or when the annotation's language ("foundational constraint") exceeds what the paper actually operationalizes (e.g., pure conceptual work without empirical instantiation).

---

## arxiv-2606.17962

# Escalation Accuracy Assessment

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper presents "a sustained mechanism for bridging symbolic reasoning and learned inference in multi-agent protocol verification" with an "oracle-validator coupling" pattern that generalizes beyond MAS.

The deep read confirms this is precisely what the paper delivers. The generate-and-certify architecture (LLM as oracle, formal verifier as validator) is indeed a structural integration pattern—not just a performance hack. The paper demonstrates:
- **Actual mechanism**: LLM navigates exponential strategy search space; ATL pre-filter prunes infeasible cases; formal verifier certifies only sound outputs.
- **Genuinely absent pattern**: The specific pairing of bounded-rationality synthesis (NatATL) with neural generation is novel in the verification literature.
- **Generalization potential**: The deep read confirms the annotation's claim that this pattern (cheap search + cheap certification) is domain-portable—the paper explicitly frames it as applicable to other strategic logics beyond NatATL.

No mismatch detected. The annotation captured the right insight at the right level of abstraction.

---

**(b) What deep reading added**

The shallow annotation could not have discovered: (1) **NatATL as a latent theoretical substrate** — the paper's real philosophical contribution is operationalizing bounded rationality as syntactic complexity constraints, which reframes the entire problem from "exhaustive search over strategies" to "find natural (simple) strategies"; (2) **The architectural elegance of the ATL pre-filter** — a cheaper feasibility oracle that prunes before expensive verification, demonstrating a sub-pattern within the main generate-and-certify design that itself generalizes beyond this application. The shallow note captured the integration pattern but missed the theoretical grounding (boundedness) and the internal structure of the solution.

---

**(c) Training signal**

**Escalate when:** A shallow annotation identifies a novel *architectural pattern* (not just a performance result) that pairs two computational primitives with asymmetric costs—especially if it operationalizes a latent theoretical concept (bounded rationality, interpretability constraints) and the authors frame it as domain-portable beyond the immediate application.

**Don't escalate when:** The escalation rests on a claimed "integration" that is actually sequential pipeline gluing (LLM then verifier) without demonstrating that the pairing itself is the novel unit, or when the paper is primarily an empirical improvement on a single task with no architectural or theoretical lesson for other domains.

---

## arxiv-2606.17987

# ESCALATION ASSESSMENT

---

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper demonstrates "a generalizable mechanism (security-induced equilibrium collapse via resource expansion)" with "game-theoretic failure mode" applicability to "protocolized infrastructure systems." 

The paper *exactly* delivers this. It identifies a named, mechanistically precise failure mode (the Braess paradox applied to NFV/SDN orchestration) where adding a locally attractive defensive resource causes equilibrium degradation by coupling previously load-separated resources. The sufficient condition (Theorem IV.1) is formal and transportable. The mechanism is generalizable—it operates whenever load sensitivity and resource-separation structure align, not only in the specific SFC testbed. The paper does not oversell (no claim of universal applicability, properly qualifies to affine delays and Wardrop equilibria) and does not undersell (the screening algorithm and system-optimum result show both diagnosis and remedy are actionable).

No mismatch. The shallow annotation's framing was predictive.

---

**(b) What deep reading added**

The shallow note could not have predicted the *specificity of the sufficient condition*: an explicit interval on the shortcut's fixed delay where Braessian behavior occurs, coupled with the constraint that the interval is nonempty exactly when load sensitivity and distributed-inspection delay satisfy `α > 0` and `c > α`. Deep reading also revealed the system-optimum escape route—that centralized marginal-cost pricing eliminates the paradox entirely—which reframes the failure as a *coordination problem*, not a physical necessity. The shallow read captured the phenomenon; deep reading showed both the diagnostic threshold and the structural reason the paradox is recoverable.

---

**(c) Training signal**

**Escalate when:** A paper names a precise, previously-unnamed equilibrium failure mode in an engineered system (protocol, infrastructure, or market), supplies a formal sufficient condition or characterization, and demonstrates it via both stylized example and realistic topology—especially if the failure is counterintuitive and operational practice would not surface it.

**Don't escalate when:** A paper claims a "mechanism" in game-theoretic or systems language but provides only qualitative intuition, narrative examples without formal sufficiency conditions, or simulation results on a single synthetic scenario without transportable diagnostic criteria—or when the claimed failure is already well-named in the literature and the paper is primarily a replication in a new domain.

---

## arxiv-2606.18121

**(a) Escalation accuracy: `accurate`**

The escalation annotation claimed the paper applies error-correcting code theory (specifically density evolution and stopping sets) as a formal framework for multi-agent AI reliability, introducing a mechanism for analyzing failure modes in distributed verification architectures not currently in the inventory.

The paper fully delivers on this claim. It does indeed transplant the density-evolution machinery from LDPC coding theory into a model of networked AI agents solving coupled verification tasks. The authors introduce:
- A role-typed, value-conditioned density-evolution theorem (Theorem 1) generalizing classical LDPC-BEC analysis to heterogeneous agents and noisy Boolean verifiers
- A certificate-stopping-set failure mode (Theorem 3) that specializes classical LDPC stopping sets to multi-agent architectures
- A formal proof (Proposition 2–3) that the three failure tiers (agent abstention, verifier erasure, reasoning-channel loss) are *structurally non-interchangeable*—a novel insight that wouldn't arise from standard coding theory alone

This is not a loose analogy. The paper proves theorems in the coding-theoretic tradition, with concentration results and converse bounds. The mechanism—message-passing on factor graphs with typed roles—is genuinely novel in the multi-agent verification setting, and the scaffold (stopping sets, density evolution) is directly borrowed from the inventory of sparse-graph codes but extended to handle bounded-arity Boolean functions and value conditioning.

**(b) What deep reading added:**

The shallow note captured the core mechanism accurately but missed two substantive elaborations: (1) the *non-interchangeability theorems* (Propositions 2–3), which formalize why the three failure tiers cannot be collapsed into a single effective noise parameter—a result that has direct implications for architecture optimization and cost allocation; and (2) the *certificate-stopping-set* framework and its three structurally distinct failure modes (verifier-erased, combinatorial, channel-erased), each requiring a different architectural fix. The shallow read was sufficient to warrant escalation, but the deep read revealed the paper's most actionable engineering payload: separate shadow prices for each failure tier in constrained optimization.

**(c) Training signal:**

**Escalate when:** A shallow note identifies a formal transplant of a mature mathematical framework (coding theory, game theory, control-theoretic tools) from a well-understood domain into a new applied domain (multi-agent AI, distributed verification), with claims of novel theorems that specialize or extend the source theory to handle heterogeneous agents, asymmetric cost structures, or failure modes absent from the source setting.

**Don't escalate when:** A shallow note claims "applies X framework to Y problem" but the application is loose analogy, framing, or narrative borrowing without new theorems, concentration results, or formal converse bounds; or when the claimed novelty is primarily in the problem statement rather than in extending or specializing the mathematical machinery itself.

---

## arxiv-2606.18142

# Assessment of Escalation Decision

## (a) Escalation accuracy: `accurate`

The escalation annotation claimed: "Primary source introducing a mechanism absent from current inventory—the gap between declarative value alignment (text responses) and behavioral alignment (agentic action)—with empirical measurement of that gap across frontier models."

The paper **does deliver exactly this**. The core finding is that models articulate welfare reasoning in text benchmarks but fail to enact it when given purchase authority (welfare rates 26–53% vs. 64% chance baseline). The mechanism—that stated preferences and revealed preferences diverge in agentic deployment—is the paper's animating insight, and it is measured systematically across Claude, GPT, DeepSeek, and Gemini. The escalation was well-warranted.

## (b) What deep reading added

The deep read revealed the paper's second-order insight: that this alignment gap is driven by *training-data salience* (welfare reasoning tracks public discourse prevalence, ρ=+0.61, not moral category) rather than absence of capability, and that the gap is heterogeneously *remediable* via system-prompt intervention (+47–63pp for Claude vs. +7–11pp for DeepSeek). The shallow annotation captured the existence of the gap; the full paper showed *why* it exists and that it has structure.

## (c) Training signal

**Escalate when:** A paper claims a mechanism (value-action alignment gap, dormant reasoning, salience-driven behavior) that is directly measurable via a controlled behavioral benchmark where below-baseline performance disambiguates between indifference and active bias, and the mechanism has implications for deployment risk at scale.

**Don't escalate when:** Papers document welfare concerns or user harms in models without isolating a mechanistic cause or a measurement approach that rules out alternative explanations (capability failure, evaluation gaming, category ambiguity in harm classification).

---

## arxiv-2606.18392

# Assessment: Arxiv 2606.18392

## (a) Escalation accuracy

**Escalation claim:** "Introduces a genuine mechanism absent from inventory: the exploration-exploitation dilemma in human-crowdsourced information systems where individual rationality (avoiding stale-data exploration) conflicts with collective system efficiency."

**Verdict:** `accurate` — but substantially under-specified in the shallow annotation.

The paper does introduce exactly this mechanism. However, the shallow read missed the *structural precision* that makes this escalation-worthy. The annotation says "avoiding stale-data exploration" — which is true but vague. The deep read reveals that the paper formalizes *why* stale data creates the dilemma: because Age of Information (AoI) is endogenously driven (incremented by non-participation), customers face a threshold decision that couples information freshness with congestion externality. Worse, the paper proves the dilemma is *not* fixable by information mechanisms alone — a much sharper result than "conflict exists." The shallow note captured the phenomenon; deep reading revealed it has surprising structure (dual over/under-exploration, infinite PoA, mechanism-resistant design).

## (b) What deep reading added

Deep reading revealed three layers absent from the shallow claim: (1) the mathematical characterization of myopic policy failure (both directions: over- and under-exploration depending on queue state), (2) the impossibility result — that informational mechanisms fundamentally cannot bound inefficiency because customers can reverse-engineer adversarially-presented information, and (3) the constructive fix (side-payment mechanism with PoA < 2), showing the problem is not just identified but solved. The shallow note was sufficient to justify escalation but left the paper's actual contribution — mechanism design under endogenous information variation — entirely unarticulated.

## (c) Training signal

**Escalate when:** A paper claims to identify a structural conflict or coupling (incentive misalignment, externality, information-intervention entanglement) *and* provides formal proof that standard remedies (information design, disclosure, signaling) provably fail on that structure. Impossibility results paired with mechanism design are reliable signals.

**Don't escalate when:** A paper identifies a qualitative trade-off (exploration vs. exploitation, individual vs. collective) without formalizing the mechanism, proving pathology bounds (PoA, regret, welfare loss), or showing why existing tools fail. Generic tension statements are common; escalate only when the mechanism is *made precise enough to prove impossible to solve by standard means*.

---

## arxiv-2606.18479

# ASSESSMENT: Arxiv 2606.18479

---

## (a) Escalation accuracy

**Verdict: `accurate`**

**Escalation claim:**
> "identifies a structural failure mode endemic to feedback cycles in scoring protocols—where standard accuracy metrics mask deterioration in decision quality—and proposes a mechanism for diagnosing it; the pattern likely generalizes across all selection/rejection systems under retraining."

**Assessment:**
The paper delivers exactly what was claimed. The core contribution is a formally rigorous proof that in iterative model-based lending under selection bias, standard accuracy metrics structurally *improve* while decision quality on the true population *deteriorates*. The Oracle Paradox is a genuine structural inversion, not a simulation artifact—the authors prove it analytically (Propositions 1–2) and validate it empirically across three datasets and two model families. The proposed diagnostic (controlled exploration at 2–5%) is concrete and implementable.

The generalization claim ("likely generalizes across all selection/rejection systems") is explicitly flagged as speculative in the paper itself (predictive policing cited but not analyzed). This is honest framing; the escalation annotation correctly marked it as a pattern, not a proven universal law. No mismatch.

---

## (b) What deep reading added

The shallow read could not have captured the formal backbone (Lemma 1 and Propositions 1–2) or the elegance of the Oracle Paradox as a load-bearing counterexample—these require engagement with the mathematical argument and the empirical confirmation across six configurations. Deep reading also revealed the Kickout metric as a proposed escape from circularity (though with practical constraints the authors acknowledge but don't fully resolve). The shallow note was sufficient to justify escalation, but deep reading showed the work is more rigorous and the failure mode more precisely characterized than the annotation could indicate.

---

## (c) Training signal

**Escalate when:** A shallow note claims a *structural* or *formal* failure mode (not just empirical degradation) in a feedback loop or measurement system, proposes a diagnostic mechanism, and the paper appears to have the mathematical or logical apparatus to prove it, not just simulate it.

**Don't escalate when:** The annotation invokes generalization across "all systems of type X" without the paper providing either a theorem or explicit scope boundaries—especially if the paper is domain-specific (credit scoring) and generalization is only intuited, not demonstrated or formalized.

---

## arxiv-2606.18617

# ASSESSMENT: arxiv-2606.18617

## (a) Escalation accuracy: `accurate`

The escalation annotation claimed the paper presents "a sustained empirical argument about protocol-reality mismatch" and "introduces a measurement mechanism (GenAI transcription analysis) absent from current inventory."

The paper **does** deliver both. It systematically documents the gap between training-scenario performance (7.4% gains, 0.25 SD prediction of real-world quality) and authentic tutoring behavior, demonstrating that the link exists but is modest and mediated by opportunity recognition rather than execution alone. The measurement pipeline—using LLM scoring of authentic transcripts to validate training transfer—is genuinely novel as a scaling method for what would otherwise require prohibitive human annotation. The paper's honest finding (modest prediction, gradual non-causal trend, execution/opportunity decomposition) is exactly the kind of protocol-reality mismatch signal the annotation correctly identified as worth deep reading.

No significant mismatch between claim and content.

## (b) What deep reading added

The shallow note captured the mechanism correctly but missed the paper's most important conceptual move: the decomposition of transfer into *opportunity recognition* vs. *execution quality*, and the finding that training improves the former (61.1% → 68.9%) much more than the latter (65.5% → 68.1%). This reframes what "training-to-practice gaps" actually are—not uniform deficit, but skill-type-specific. Deep reading also revealed the honest causal agnosticism: the ITS design cannot distinguish training from maturation/practice effects, which the authors acknowledge rather than hide.

## (c) Training signal

**Escalate when:** Papers that propose closing a measurement gap (training↔practice validity) using a novel scaling method (GenAI/automation) applied to a concrete, protocolized domain, *and* report empirical transfer estimates (not just feasibility), *especially* when the results are modest or counterintuitive.

**Don't escalate when:** Papers claiming GenAI measurement advances without reporting predictive validity against a real-world outcome variable, or that treat the measurement tool as the primary contribution rather than what it reveals about the phenomenon.

---

