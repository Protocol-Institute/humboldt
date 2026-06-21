# Deep Read Notes: Arxiv 2606.08998

*Source: `bibliography/deep-reads/arxiv-2606.08998.pdf`*

---

## Reading session: full document (28 pages)

# Deep Read: Hydari & Iqbal, "The Token Not Taken: Sampling, State, and the Variability of AI Agent Outputs" (arXiv:2606.08998)

*Full document read, 28 pages including appendices.*

---

## 1. Gestalt

This is a pedagogical clarification paper, not a research paper in the discovery sense. The authors' animating problem is conceptual confusion in a consequential domain: managers, product owners, and technical evaluators are asking the wrong question ("Is this AI system stochastic?") when they should be asking "At which layer can variation enter, and what variation matters for this use case?" [text, p.17]. The paper's method is decomposition — it carefully separates the layers of an agentic system (foundation model forward pass, decoder, orchestration loop, external environment, serving infrastructure) that are routinely conflated in both popular and technical discourse. Its central conviction is that *stochastic* and *irreproducible* are different predicates, and that conflating them produces both unnecessary alarm (you can control sampling reproducibility) and false comfort (deterministic decoding does not eliminate agentic variability). The work's intellectual lineage is engineering documentation brought into precise mathematical form — it does for the variability question what a good RFC does for a protocol: establishes shared vocabulary, separates concerns, and eliminates confusions that would otherwise propagate into system design decisions.

---

## 2. Argument and Structure

The paper's architecture is transparent and explicitly stated at the end of the introduction [text, p.3]: systems behavior → token generation → back to systems behavior.

**Core claims:**

1. **The agent loop amplifies token-level stochasticity.** A single sampled token difference can change a tool call, code path, database query, or decision to stop — because the output is parsed as an *action*, not merely read as text. [text, p.13–14] The load-bearing example is the JSON tool call: `{"tool": "lookup_order"}` vs. `{"tool": "escalate_case"}` differ by a few tokens but produce categorically different business outcomes. This example carries real weight — it makes concrete why "different wording" in chat is qualitatively different from "different wording" in an agent.

2. **Intrinsic and extrinsic variation are distinct.** Token sampling is intrinsic; environment change, serving infrastructure, application logic are extrinsic. A fixed seed addresses only the intrinsic source. [text, p.6, Table 2] This is the paper's most analytically useful move.

3. **Stochastic ≠ irreproducible.** Under matched conditions (same weights, context, decoding parameters, synchronized PRNG), sampling is exactly reproducible. The proof by induction is clean [text, p.25–26], and the twin GPT-2 demonstrations are intended to make this tangible.

4. **Deterministic decoding ≠ identical behavior in deployment.** Two sources of variability survive temperature-zero settings: (a) numerical/serving nondeterminism (batch composition changing which kernel is used, which changes floating-point accumulation patterns) [text, p.16]; (b) environment variation, which seeds cannot control.

5. **The key finding about GPU nondeterminism** is worth marking carefully: the paper cites He et al. (Thinking Machines Lab, 2025) for the argument that individual LLM inference kernels can be deterministic for fixed input shapes, but serving systems are not *batch-invariant* — your prompt gets silently batched with others, and different batch compositions can trigger different kernel paths, producing slightly different logits. This is a serving-protocol variability that has nothing to do with sampling randomness and cannot be addressed by seeding.

**Acknowledged limits:** The paper is explicit that its demonstrations use toy conditions (CPU, GPT-2, manual one-token decoding) and explicitly warns against generalizing to deployed services [text, p.26, Appendix C]. The authors are honest that commercial API "seed" parameters may be best-effort because backend infrastructure changes [text, p.16].

**Where the authors are most confident:** The formal decomposition (Table 2, the state-machine model) — this is precisely specified and appears watertight.

**Where they are most speculative:** The implications section (§7) is more normative prescription than empirical finding. The six recommendations are sensible but not derived from evidence — they're engineering wisdom stated as a corollary.

---

## 3. Conceptual Vocabulary

**Intrinsic vs. extrinsic variation** [text, p.6]: The paper draws this distinction sharply. Intrinsic = arises from the token sampling mechanism itself. Extrinsic = environment change, serving effects, application logic. This is a useful analytical cut. My existing vocabulary doesn't have a precise equivalent — I might have said "internal vs. external" but without the specific anchoring to the PRNG boundary.

**Agentic stochasticity** [text, p.4–5]: Stochasticity that has been amplified through the agent loop so that token-level variation becomes action-level and outcome-level variation. Distinct from model stochasticity (which is just the distribution over next tokens). The amplification is the agent loop's parsing step: once a token sequence becomes a *command*, the variance matters in a different register.

**Batch invariance** [text, p.16]: A serving property. A system is batch-invariant if a request produces the same output regardless of which other requests share its batch. Most practical inference servers are *not* batch-invariant. This is a protocol property of the serving layer, not of the model.

**Logits** [text, p.7–8]: The paper notes a term collision: in classical statistics, "logit" means log-odds; in neural-network software, "logits" means raw pre-softmax scores. This collision is worth tracking — it's a minor example of notation-lock creating confusion across communities (connects to Iverson in LINEAGE.md).

---

## 4. Analytical Moves

**The layer decomposition move:** When a system exhibits variability, decompose the system into its constitutive layers and ask which layers can produce variation, whether those sources are controllable by the proposed intervention, and whether the layers are independent. Applied here: token sampling, serving infrastructure, environment, application logic are four independent sources; seeding addresses only one. [inference from text, p.6] This is a broadly transferable diagnostic procedure.

**The stochastic-vs-irreproducible split:** Take a claim of the form "X is stochastic, therefore X is unpredictable/unreproducible" and decompose it: (a) what is the mechanism of stochasticity, (b) under what conditions is that mechanism controlled, (c) what remains uncontrolled even when (b) is satisfied? This prevents the common error of inferring uncontrollability from probabilistic description. [inference from text, pp.15–16]

**The semantic-vs-operational variability split** [text, p.17, item 1]: Two outputs may differ in wording but be equivalent for the task (semantic variability); two outputs may differ in a way that changes cost, risk, or compliance exposure (operational variability). For evaluating agentic systems, only operational variability matters. This is a useful instance of a more general move: distinguish variability in representation from variability in consequence.

**The twin-replica demonstration:** To show that stochastic sampling is reproducible, don't run the same model twice (which conflates seed-reset with intrinsic reproducibility); run two independent replicas with synchronized RNG state and show they produce identical output. The two-replica framing isolates the mechanism being demonstrated. [text, p.19, Appendix B]

---

## 5. What It Says About the Nature of Things

The paper's deepest implicit claim is that **variability in complex systems must be traced to specific mechanisms at specific layers, not attributed holistically to system properties.** Saying "the agent is stochastic" is like saying "the building is unstable" — it doesn't say whether the instability is in the foundation, the frame, or the weather. The diagnostic work of assigning variation to its source layer is the precondition for any useful intervention.

[inference] There's also a latent claim about **how protocol behavior propagates**: small textual differences, when they cross a parsing boundary (from output sequence to action), change category rather than just degree. A 2% probability token that triggers `escalate_case` instead of `lookup_order` doesn't produce a "slightly different" outcome — it produces a categorically different business action. This is an amplification effect that is specific to systems with action-parsing steps. Chat completions don't have this property because words never become commands in the same sense.

The batch-invariance finding [text, p.16] has a more general implication: **serving protocols introduce their own variability regime that is decoupled from both the model's mathematical properties and the application's design.** This is a coordination layer below the application and above the model that is often invisible to both the model designer and the application developer. The variability it introduces is structurally similar to the variability introduced by distributed systems generally — it's a function of which requests co-occur and how the system routes them.

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper, not a methods paper, so this section is thin. But there's something here.

The paper is primarily a *clarification* work — its contribution is not new empirical findings but sharpened conceptual distinctions in a domain where existing vocabulary was creating systematic confusion. The authors are doing what a careful natural philosopher does before doing science: they're establishing what the phenomenon *is* before trying to explain it.

The lesson for research practice: **sometimes the most important move is not investigation but decomposition** — identifying that a question is poorly formed because it conflates distinct phenomena. "Is this system stochastic?" is poorly formed; "Which layer introduces variation, and under what conditions?" is tractable. Much wasted investigation proceeds because the question-framing bundles what should be separate.

This connects to M-016 at the level of research object definition: before building a hypothesis inventory around a phenomenon, ask whether the phenomenon has been adequately decomposed into its constitutive parts. A law stated about "agentic variability" will be much weaker than a law stated about "serving-layer batch-invariance failure" or "action-parsing amplification of token stochasticity."

---

## 7. Where It Touches My Research

This paper is not directly about protocolized systems in my primary sense — it's not about financial clearing or parliamentary procedure or network protocols. But it touches several live threads:

**The serving protocol as an implicit coordination mechanism.** The batch-invariance finding is, from my perspective, a protocol observation: the serving layer has an implicit *protocol* — a set of coordination rules about how requests are batched, routed, and executed — and that protocol introduces variability that is invisible to both model and application. This is a case where a coordination layer's behavior is not formally specified and the gap between implicit and explicit protocol creates emergent behavior (non-batch-invariance). [inference] This might be evidence for something like a gap-law: the variability introduced by an unspecified coordination layer scales with the gap between its implicit behavior and its assumed behavior.

**Action-parsing as a protocol boundary.** The paper's most interesting moment for my purposes is the observation that the same token-level variation has different consequences depending on whether it crosses an action-parsing boundary [text, p.13–14]. Before parsing: text with stylistic variation. After parsing: different command with different consequences. This is a protocol boundary in the sense I care about — a point where meaning is formalized and consequences become deterministic. The amplification effect is a property of that boundary, not of the model.

**The inbox item on possible-futures representation** (discord-idea-2026-06-17: "Systems represent possible futures implicitly through their error-correction mechanisms"). The paper has a weak connection here: the diversity of possible outputs that a sampling decoder can produce is a kind of implicit representation of the model's probability landscape. Whether that connection is substantive or superficial, I'm not sure yet.

---

## 8. Candidate Laws

**Weak candidate:** The paper implies but doesn't state a regularity I'd call the **Action-Parsing Amplification Pattern**: *token-level variability in an agent's output sequence is amplified in consequence when the output is parsed as a command rather than read as text, because parsing discretizes a continuous probability space into a finite action space where small probability differences produce categorical outcome differences.*

- What the text says: "A few different tokens can change the business action. [...] The difference is small as text but material as a database query." [text, p.13–14]
- Candidate formulation: In systems where model output is parsed into a finite action set, the functional variability of sampling (measured by outcome variance) is higher than in systems where output is read as text, even when the probability distribution over outputs is identical.
- Falsification condition: A parsing-based system where outcome variance is not systematically higher than in text-output systems with equivalent sampling parameters would falsify this. (Though measuring "equivalent sampling" across contexts is non-trivial.)
- Confidence: speculative. One domain, mechanism stated, no cross-domain evidence.

This is worth noting but not yet worth formalizing. The mechanism is clear; the cross-domain question is whether analogous parsing-boundary amplification appears in other protocol systems (legal: ambiguous contract language that becomes unambiguous upon adjudication; financial: trade instructions that get parsed into order types).

---

## 9. What Surprised Me / What Doesn't Fit

**The batch-invariance finding surprised me.** I expected the paper's variability taxonomy to bottom out at "PRNG state." Instead, it goes lower — to the serving infrastructure's own protocol of batching requests, which is invisible to the application and introduces deterministic-but-unpredictable (from the application's perspective) variation. This is a level of coordination-protocol analysis I hadn't expected in a paper nominally about AI agent variability.

**The framing tension:** The paper is addressed to managers [text, p.1, p.17], but the technical content (transformer architecture, softmax derivations, PRNG induction proofs) is aimed at engineers. These are different audiences with different needs, and the paper doesn't fully resolve the tension. The managerial recommendations in §7 are sensible but would have been stronger if the earlier technical material had been more tightly connected back to them. The paper's most important managerial insight — "record the full agent trajectory, not only the final answer" [text, p.17, item 2] — is not actually derived from the technical analysis; it's stated as practical wisdom.

**The "reasoning trace" section (§6.1) deflects a question it could have addressed.** The paper argues that a visible reasoning trace is "still generated as a token sequence" [text, p.15] and thus subject to the same sampling variability as any other output. True. But the more interesting question — whether reasoning traces systematically *reduce* action-level variability (by allocating more probability mass to well-reasoned conclusions before the action-parsing boundary) — is not addressed. This seems like a genuine empirical question the paper positions itself to ask but doesn't.

---

## 10. What It Opens

**Immediate question:** Is the action-parsing amplification effect I identified in section 8 observable in non-AI protocol contexts? Legal: when does an ambiguous instruction become a binding command? Financial: when does a trade indication become an executed order? Medical: when does a verbal order become an administered medication? All of these have parsing boundaries where continuous uncertainty collapses into discrete action. If the amplification effect is real, it should be visible in the error rates at these boundaries — and there may already be literature on this (medical error at verbal-to-written order transitions comes to mind).

**The batch-invariance question** opens into distributed systems protocol design generally: under what conditions do coordination layers (load balancers, request routers, batch schedulers) produce variability that is invisible to both the layers above and below them? This is a cross-domain question worth a focused investigation.

**Related reading:** He et al. (Thinking Machines Lab, 2025), "Defeating Nondeterminism in LLM Inference" [cited at text, p.16] — the paper that provides the batch-invariance analysis the authors rely on. This seems worth reading directly rather than through citation.

**Tradition to explore:** The discrete choice literature (Train, 2009, cited at text, p.8, fn.5) — the paper notes that multinomial logit choice probabilities are the same mathematical object as softmax probabilities. There may be a deeper connection between the economics of discrete choice (where agents choose among a finite set of options with probabilistic outcomes) and the protocol design question of how systems that produce probabilistic distributions over actions should be designed for reliability. This is speculative but potentially generative.
