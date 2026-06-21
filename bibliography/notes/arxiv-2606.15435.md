# Deep Read Notes: Arxiv 2606.15435

*Source: `bibliography/deep-reads/arxiv-2606.15435.pdf`*

---

## Reading session: full document (7 pages)

# Deep Read: Milzman & Maity, "On Type Deception in Linear-Quadratic Differential Games" (arXiv 2606.15435)

*Full document, 7 pages. Text complete.*

---

## 1. Gestalt

This paper asks a question that the classical theory of differential games systematically evades: what happens when one player *knows* they have an advantage and *wants to hide it*? The classical framework assumes common knowledge of system dynamics — everyone knows what everyone is capable of. Milzman and Maity strip that assumption away and find that a radically different strategic structure emerges. The informed player doesn't simply exploit their advantage; they first *perform ignorance*, mimicking behavior consistent with both possible types, then reveal at a strategically chosen moment. The paper's core contribution is making this structure tractable: it shows that the optimal deception problem decomposes cleanly into two sequential phases — a pooling phase governed by a modified Riccati equation and a complete-information phase governed by the standard one — with a single scalar (the revelation time) connecting them. The animating question is not "how do you solve games with incomplete information?" but "what does optimal deception look like when information asymmetry is itself a strategic resource?"

---

## 2. Argument and Structure

**Core claim:** In a two-player zero-sum linear-quadratic differential game where one player (P2) has a private type unknown to P1, any ex-ante Nash equilibrium decomposes into exactly two phases: a *pooling/deceptive phase* [0, s̃) in which both types of P2 play identically, and a *revelatory phase* [s̃, T] in which both players play as if the type were common knowledge. [text, p.1-2]

**How the argument builds:**

1. The problem setup introduces asymmetric type: P2's control matrix B₂(θ) depends on a private type θ ∈ {θ₁, θ₂}. P1 can observe the full state trajectory but cannot separate the control input from its type-specific modifier — the only thing P1 can infer is whether P2's behavior is *distinguishable across types*. [text, p.2-3]

2. A simplified information structure is introduced: P1's belief collapses from the prior π to certainty δ_{θ*} the moment P2's type-specific strategies become distinguishable. This is a binary belief space, not a continuous Bayesian update. The authors acknowledge this is a simplification of the full Perfect Bayesian Equilibrium framework, which remains underdeveloped for differential games. [text, p.3]

3. **Proposition 2** is the load-bearing result: any ex-ante Nash equilibrium must have (i) both P2 types playing a *common* feedback law during [0, s̃) — they are constrained to pool — and (ii) both players playing the unique complete-information feedback equilibrium during [s̃, T]. This proposition converts the search for equilibria over an infinite-dimensional strategy space into a search over a single scalar s̃ ∈ [0, T]. [text, p.4]

4. **Proposition 4** shows that Stage 1 reduces to a standard ZSLQ game with a modified effective control cost R̃₂ = π₁I + π₂Λ⊤Λ (where Λ encodes the relationship between the two types' control matrices) and a terminal cost equal to the prior-weighted average of the two complete-information Riccati solutions. The pooling constraint transforms a game of incomplete information into a game of complete information with adjusted parameters. [text, p.4-5]

5. **Proposition 5** provides an analytic gradient of the game value with respect to s̃ for time-homogeneous systems, enabling gradient-based optimization over the revelation time. [text, p.5-6]

6. The numerical example (pursuit-evasion with time-varying control advantages) demonstrates that interior optima exist: deception is most valuable not at s̃ = 0 (no deception) or s̃ = T (reveal only at the end), but at some intermediate time that tracks the crossover point where P1's advantage transitions to P2's. [text, p.6-7]

**Where the authors are most confident:** The decomposition result (Prop. 2) and the Stage 1 Riccati formulation (Prop. 4) — these are clean proofs within a well-specified framework.

**Where they are most speculative:** The ex-interim type-rationality question (will P2 *actually* want to maintain the pooling strategy once they know their type?) is explicitly deferred. The extension to off-equilibrium beliefs is acknowledged as problematic and left to future work. [text, p.3, p.4]

---

## 3. Conceptual Vocabulary

**Type** [text, p.1]: Private information about one's own capabilities — specifically, which of several possible control matrices P2 actually has. Not type in the informal sense of "character," but in the Harsanyi sense: a parameter that determines what a player *can do*, unknown to the opponent.

**Revelation time** s̃ [text, p.2]: The moment at which P2's behavior becomes distinguishable across types, causing P1's belief to collapse to certainty. A strategic variable controlled by P2 — they can choose *when* to reveal by choosing *when* to stop pooling. Equivalent to the boundary between the deceptive and revelatory phases.

**Pooling phase / concealment interval** [text, p.2-3]: The period [0, s̃) during which both P2 types play identically. Not a coincidence — a *constraint* arising at equilibrium. P2 is sacrificing some of their type-specific advantage in order to preserve P1's uncertainty.

**Ex-ante equilibrium** [text, p.3]: Equilibrium evaluated before types are assigned — both players choose strategies that are optimal in expectation over the type distribution. Contrasted implicitly with ex-interim equilibrium (after type is realized but before play) and ex-post equilibrium (after the game).

**Observational compatibility** [text, p.3]: P1's belief rule is consistent with P2's equilibrium strategy — on the equilibrium path, the belief tracks what Bayes' rule would imply. The authors' stripped-down substitute for the full PBE consistency requirement.

**Private state decomposition** [text, p.2]: A structural assumption that each player's control affects only their own state component. This simplifies observability: P1 can reconstruct B₂(θ)u₂ from the trajectory, but not separate the type-specific modifier from the control input.

**Tension with my vocabulary:** I don't have established vocabulary for this domain. The concept of "revelation time as a strategic variable" is new. The closest thing in my existing inventory is the general notion of information asymmetry as a resource, but this paper makes that precise in a way I hadn't formalized.

---

## 4. Analytical Moves

**The equilibrium decomposition move:** When a game has private information, ask whether equilibrium strategies can be decomposed into distinct phases — one governed by incomplete-information constraints, one by complete-information play. Show that the incomplete-information phase reduces to a complete-information game with modified parameters. This converts an infinite-dimensional problem (strategy over the full game) into a lower-dimensional one (strategy over a scalar parameter). [text, p.4, Prop. 2 and Prop. 4]

**The pooling-as-constraint move:** At equilibrium, the informed player's deception isn't a free choice — it's a constraint. Both types *must* play identically during the pooling phase for the equilibrium to be observationally compatible. This converts the deception problem from "how does P2 choose to deceive?" to "what is the best game P2 can play subject to the pooling constraint?" [text, p.4]

**The modified-parameter collapse:** The Stage 1 game (pooling phase) looks like a standard ZSLQ game, but with an effective control cost R̃₂ that blends the two types' capabilities weighted by the prior. The strategic complexity of incomplete information is absorbed into a parameter modification. [text, p.5, Prop. 4]

**The gradient-of-revelation-time move:** Rather than searching over all possible strategies, reduce to optimization over a single scalar (s̃) and compute its gradient analytically via variational analysis of the Riccati equation. [text, p.5-6, Prop. 5]

**The interior-optimum demonstration:** Show (numerically) that the optimal revelation time is neither 0 nor T — deception has positive value, but so does revelation. This establishes that the scalar optimization is genuinely non-trivial and has interior solutions. [text, p.6-7]

---

## 5. What It Says About the Nature of Things

**Deception as strategic resource management.** The informed player isn't simply hiding information — they're managing the *rate of information release* to maximize advantage. Information asymmetry is a depletable asset: revelation converts it into execution advantage (you can now play type-optimally), but also terminates it. The optimal policy is an interior solution between hoarding and immediate revelation. [inference]

**Pooling is sacrifice, not free concealment.** During the deceptive phase, P2 cannot play their type-optimal strategy — they're constrained to a strategy that both types could plausibly produce. This is a real cost. The deceptive player is paying for concealment by underperforming relative to what they could achieve with full revelation. The value of deception is the net of this cost against the benefit of preserving P1's uncertainty. [text, p.4]

**Equilibrium structure can be forced by information constraints.** Without any explicit coordination, the equilibrium *requires* the informed player to pool. This is a case where the information structure of the game determines the shape of equilibrium strategies — not preferences over outcomes alone. [inference from Prop. 2]

**Capability asymmetry × temporal dynamics = deception opportunity.** The numerical example is suggestive: deception is most valuable when capabilities are *changing over time* and the informed player can time revelation to exploit a transition. A static game with time-invariant capabilities might have different optimal revelation times. [inference from p.6-7]

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper — it demonstrates rather than discusses research craft. But there are implicit lessons:

**Reduce before you solve.** The authors' entire method is successive reduction of the problem: infinite-dimensional strategy space → two-phase decomposition → Stage 1 game with modified parameters → scalar optimization → gradient. Each reduction is justified by an equilibrium argument, not imposed by fiat. The discipline of finding the right reduction before attempting a solution is the central skill on display.

**Acknowledge the gap explicitly and proceed anyway.** The PBE machinery for differential games is "largely underdeveloped" [text, p.2] — the authors say this directly, adopt a simplified substitute, and continue. This is not a failure of rigor; it is a principled response to the state of the field. Relevant to M-016: knowing when to work within an incomplete framework vs. waiting for the framework to mature.

**Demonstrate existence of non-trivial optima early.** The numerical experiments don't show the optimal strategy in detail — they show that interior optima *exist*, that the scalar optimization has non-trivial solutions. This is the minimal demonstration needed to establish that the framework captures something real. Don't oversell; establish the phenomenon first.

---

## 7. Where It Touches My Research

**Direct connection to the "possible futures" thread in the inbox.** The 2026-06-17 discord idea — "protocols guard against possible futures visible in their error-correction mechanisms" — connects to what this paper is doing, but from the *other side*. The paper studies how an actor *manages* information release to control what futures the opponent can anticipate. The inbox idea studies how to *read* a protocol's defensive structure to infer what futures it was designed to guard against. These are dual questions: one is the informed player's optimization problem, the other is the uninformed player's inference problem. [inference]

**Candidate connection to protocol ossification.** If a protocol is a pooling equilibrium — a behavior that all participants can produce regardless of their underlying capabilities or intentions — then modification requires *breaking the pool*. Any participant who proposes a change reveals information about their type (their interests, capabilities, or position). The ossification pressure may partly be the cost of this revelation. This is speculative, but it's a mechanism I hadn't considered before. [inference — flag for further development]

**The revelation time as a design variable.** Protocols often have staged disclosure requirements — escrow, embargo periods, phased rollouts. These might be understood as institutionalized revelation times: rules that govern *when* participants must reveal their type-specific behavior. The optimal revelation time from this paper maps onto the design question of when to require disclosure. [inference]

---

## 8. Candidate Laws

**One candidate, weak:**

[text, p.4-6]: At equilibrium in a two-phase incomplete-information game, the deceptive phase reduces to a complete-information game with modified parameters (adjusted effective costs reflecting the prior distribution over types).

**Candidate formulation:** *In any strategic interaction where one party has private information and the optimal strategy involves a pooling phase, the optimal strategy during that phase is equivalent to a strategy for a single-type game with blended parameters weighted by the prior — even though no blending actually occurs.*

**What would falsify it:** A pooling equilibrium where the Stage 1 game cannot be expressed as a modified complete-information game — where some aspect of the incomplete-information structure has no complete-information equivalent. The authors' private-state decomposition assumption (eq. 8) does heavy lifting here; remove it and the reduction may fail.

**Confidence:** Low — this is a mathematical result within a specific framework, not an empirical regularity across domains. Worth noting but not yet a law candidate for my inventory.

---

## 9. What Surprised Me / What Doesn't Fit

**The pooling constraint is *imposed by equilibrium*, not chosen.** I expected the deception problem to be: "P2 decides how to deceive." Instead, at equilibrium, P2 *cannot* do anything but pool during the deceptive phase — any deviation would reveal their type and collapse P1's belief. The strategic freedom is only in *how long* to pool, not *how* to pool. This is a stronger result than I anticipated, and it's the source of the tractability. [text, Prop. 2]

**The ex-interim rationality problem is left open.** Once P2 knows their type (at t=0), do they actually *want* to maintain the pooling strategy? The paper defers this entirely [text, p.4]. This is a significant gap — an ex-ante equilibrium that isn't ex-interim rational for the realized type is strategically suspect. The authors know this; the deferral is honest but leaves the framework incomplete.

**The binary belief space is very special.** P1's belief jumps from π to δ_{θ*} the moment distinguishability occurs. In reality, P1 might maintain a continuously updating belief. The binary structure makes the math tractable but may miss the strategic implications of *partial* revelation — cases where P2's behavior is consistent with both types but updates the prior. [inference]

**The numerical example assumes the transition time is known.** The sigmoid crossover point t_c = 5 is part of the system dynamics, and the optimal revelation time s̃* approaches it as α increases. But in a real application, P1 might not know t_c either — creating a second layer of type uncertainty. [inference — potential extension]

---

## 10. What It Opens

**The dual inference problem.** This paper solves P2's problem (when to reveal). The dual is P1's problem: given that P2 is deceptively pooling, how should P1 update beliefs, and can P1 *force* early revelation through their own strategy choices? This is a different paper — possibly more relevant to my research on protocols, where the "uninformed" party is often the enforcer or the public.

**Protocol disclosure as institutionalized revelation time.** The design question: if revelation time is a strategic variable that actors optimize, what happens when institutions *mandate* disclosure timing? Does mandatory early disclosure destroy value that deception would have created? Does it create adverse selection (only actors with low-capability types comply)? This connects to financial disclosure regulation, clinical trial registration, and pre-registration in science — all cases where the institution is setting s̃ exogenously.

**Pooling equilibria in protocol adoption.** If protocol adoption involves actors pooling (all appearing to comply regardless of underlying capability), then the protocol itself is a pooling mechanism. The "compliant" surface hides capability variation. Regulatory inspection is P1's effort to break the pool; regulatory arbitrage is P2's effort to maintain it. This is a different framing of compliance and enforcement than I've worked with before.

**Texts to read:**
- Harsanyi (1967) — the foundational Bayesian games paper [text, ref 4] — I should read this if I pursue the pooling-in-protocols thread seriously
- Cardaliaguet & Rainer (2012) on dynamic games with incomplete information [text, ref 5]
- Fudenberg & Tirole, *Game Theory* (1991) [text, ref 13] — specifically the PBE treatment; I've encountered this before but haven't read it

**Live question:** Is protocol compliance a pooling equilibrium? If so, what are the analogs of revelation time, the modified effective cost, and the crossover point in the protocol context? This question is now running.
