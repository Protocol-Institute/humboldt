# Deep Read Notes: Arxiv 2606.10293

*Source: `bibliography/deep-reads/arxiv-2606.10293.pdf`*

---

## Reading session: full document (12 pages)

# Deep Read: Shah, "How Many Submissions May an Author Make?" (arXiv 2606.10293)

---

## 1. Gestalt

This paper is a piece of mechanism design applied to a specific coordination problem: how should scientific institutions ration submission slots when authorship is collaborative? The animating observation is that existing fixed-quota rules are incoherent — they treat a solo submission and a fifty-author submission identically for each named author, ignoring that collaborative work dilutes both credit and reviewing burden. Shah's project is to derive, from first principles, a quota function that simultaneously (a) respects the economics of collaboration and (b) resists strategic manipulation via author list inflation. The result — that the harmonic number is the natural decay rate for per-author submission cost — is elegant because it falls out of an empirically validated credit model rather than being stipulated. The paper matters not primarily for its specific rule but as a demonstration that institutional protocols can be derived rather than merely chosen: that there exist principled constraints on what quota rules are coherent, analogous to how thermodynamic constraints limit what heat engines can do.

---

## 2. Argument and Structure

**Core problem:** Fixed quota rules ignore coauthorship. Per-capita rules (cost = 1/a) are gameable because adding spurious coauthors lets a lead author accumulate unbounded total credit. The question is: what cost function f(a) is simultaneously manipulation-resistant and maximally generous to genuine collaborations?

**The key derivation (Section 3):**

Shah imports an empirically validated credit model [Hodge-Greenberg 1981, Hagen 2008/10/13]: the rank-i author of an a-author paper receives credit share 1/(i · H_a), where H_a = Σ(1/j) for j=1 to a is the a-th harmonic number. This is presented as empirical, not stipulated [text, p.6].

The manipulation-resistance condition requires that padding author lists not increase a lead author's total accumulated credit. This yields the inequality f(a) ≥ f(1)/H_a [text, p.6]. The per-capita rule f(a) = 1/a violates this because 1/a decays faster than 1/H_a for large a, enabling unbounded credit accumulation by padding.

The two design principles — respect collaboration, resist manipulation — push f in opposite directions and meet uniquely at f(a) = 1/H_a. This is the load-bearing logical move of the paper. The harmonic quota is not chosen for being natural; it is derived as the unique solution satisfying both constraints simultaneously [text, p.6].

A second component, β, represents an "irreducible personal claim" — the part of reviewing burden that doesn't vanish even with infinite coauthors (your name is still on the submission, you still consume pipeline resources). This lifts f(a) above the manipulation boundary: f(a) = β + 1/H_a [text, p.7]. The two free parameters (N₁, N∞) are set by organizers to calibrate the rule's stringency.

**Theorem 1** proves the manipulation resistance formally in three cases: lead authors, fractional submissions, and integer submissions. The integer case allows at most one additional paper's worth of credit from padding — tight and provably minimal [text, p.6-7, proof p.12].

**Generalized framework (Section 4):** The Generalized Harmonic Rule adds a third parameter (A, N_A) and a free exponent p on the harmonic series. When p=1, you recover the manipulation-resistant harmonic rule. When p=0, you get per-capita. Intermediate p values allow organizers to trade off manipulation resistance against generosity to large collaborations. The unifying insight: fixed, per-capita, and harmonic rules are all special cases of a single family parameterized by p [text, pp.3-4, 8-9].

**Acknowledged limits:**
- The paper makes no assumptions about whether author ordering reflects contribution [text, p.9]
- Author exchange gaming (mutual authorship inflation) is noted and checked but not fully analyzed [text, p.9]
- Quota restoration for accepted papers or reviewing service is left for future work [text, p.9]
- Randomized desk rejection creates complications for quota consumption [text, p.9]

---

## 3. Conceptual Vocabulary

**Fixed quota rule** [text, p.1]: Each submission counts as 1 against every author's budget, regardless of coauthor count. The current default. Treats collaboration as irrelevant.

**Per-capita quota rule** [text, p.1]: Submission with a authors costs 1/a per author. Respects collaboration but is gameable.

**Harmonic Quota Rule** [text, p.2]: Per-author cost decays at rate 1/H_a. Manipulation-resistant and maximally collaboration-generous.

**Harmonic number H_a** [text, p.2]: Σ(1/j) for j=1 to a. Grows logarithmically. Key property: decays slower than 1/a, which is what makes it manipulation-resistant.

**Irreducible personal claim** [text, p.7]: The portion of submission cost that does not vanish as coauthors increase — the non-transferable burden on each named author regardless of list size. This is a decomposition of cost into collective and individual components. I had no prior term for this; it's a useful concept.

**Generalized harmonic number H_{a,p}** [text, p.3]: Σ(1/j^p) for j=1 to a. Generalizes the harmonic number. At p=0, it equals a (giving per-capita); at p=1, it gives the ordinary harmonic number.

**Manipulation resistance** [text, p.5-6]: A quota rule is manipulation-resistant if adding spurious coauthors cannot increase a lead author's total accumulated credit. This is the key design constraint, and it's the one the fixed rule satisfies trivially (by over-restricting) while per-capita fails.

---

## 4. Analytical Moves

**Shah's unique-solution move:** Identify two design constraints that push a free parameter in opposite directions, then show they meet at a unique value. Here: respect-collaboration pushes f(a) down; manipulation-resistance provides a floor. The harmonic number is where the floor meets the ceiling. This move yields a derivation rather than a stipulation — the rule is forced, not chosen. Transferable to any mechanism design problem with two opposing constraints.

**Shah's two-component decomposition:** Decompose a quantity into a collective component (shared across agents, vanishes at scale) and an individual component (non-transferable, irreducible). Here applied to submission cost: f(a) = β + 1/H_a. This structure appears wherever individual and collective burdens must be separated. The irreducible personal claim component is the part that resists substitution.

**Shah's empirical-model anchoring:** Import an empirically validated external model (Hodge-Greenberg credit model) as the normative foundation for a mechanism design choice. This converts a question of values ("how much should we discount collaborative submissions?") into a question of facts ("how does the community actually apportion credit?"). The normative weight of the rule derives from its empirical grounding. Transferable wherever design choices can be anchored in documented behavioral patterns rather than stipulated preferences.

**Shah's unified-framework move:** Show that apparently disparate rules (fixed, per-capita, harmonic) are all special cases of a single parameterized family. This converts a choice between incommensurable options into navigation of a parameter space. Organizers can now choose p rather than choosing a named rule, and the space is navigable with interpretable coordinates.

**The proof-by-feasible-region move (Theorem 1, Part b):** Show that padding reduces the feasible region for the optimization (f(a') ≤ f(a) means the constrained set shrinks), so maximum credit cannot increase. Elegant because manipulation resistance falls out of the geometry of the linear program rather than requiring case analysis.

---

## 5. What It Says About the Nature of Things

**Protocols can be derivable rather than chosen.** The deepest implicit claim of this paper is that institutional rules are not merely conventional — they have principled forms that follow from constraints. The harmonic quota is not a design choice; it is the unique solution to a well-posed problem. This suggests that many institutional protocols that look arbitrary are actually either coherent solutions to their implicit constraint structure, or incoherent violations of it. The question to ask of any institutional rule is: what constraints is it satisfying? And is it the most coherent solution to those constraints, or could it be derived from first principles?

**Manipulation resistance and generosity are genuinely in tension, and the tension has a unique resolution.** This is not a finding specific to quota rules — it is a general feature of allocation mechanisms. Any rule that respects collaborative dilution of cost will, to some degree, enable gaming; the question is whether the decay rate falls inside or outside the manipulation boundary. The harmonic number turns out to be that boundary. Whether analogous boundaries exist in other allocation mechanisms is an open question.

**The irreducible personal claim generalizes.** Many protocols involve costs that cannot be fully socialized — costs that stick to named individuals regardless of how many others share the action. The separation of collective from individual components is a structure that shows up in legal liability, in insurance, in academic citation practice. The concept of a "floor" contribution that doesn't vanish at scale is undertheorized in mechanism design literature.

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper, so this section is thin — but one observation is pointed.

**Derivation over stipulation as a research habit.** Shah's method throughout is to ask: is there a principled constraint that forces the answer, rather than a design choice that permits it? This is a specific epistemic habit — hunting for uniqueness proofs rather than optimal solutions. The research practice: when you find yourself choosing between several options, ask whether the design constraints, properly formulated, select one of them uniquely. If they do, you have not made a choice — you have made a discovery.

**External empirical grounding as a way to resolve normative debates.** The choice of the harmonic credit model isn't defended as fair; it's defended as empirically validated. This moves the argument from a philosophical dispute (what counts as fair credit?) to an empirical one (what does the community's behavior reveal about perceived credit?). This is a methodological move: ground normative mechanism design in behavioral evidence wherever possible, because empirical grounding transfers normative weight from stipulation to discovery.

---

## 7. Where It Touches My Research

**Protocol design as constraint satisfaction.** The finding that the harmonic quota is derivable — not chosen — from first principles is directly relevant to the question of what makes institutional protocols stable and legitimate. A protocol that is the unique solution to its constraint structure has a different stability profile than one that is conventional. Conventions can be changed by choosing differently; derived rules can only be changed by changing the underlying constraints. This is a mechanism-level distinction worth noting for any hypothesis about protocol ossification.

**The irreducible personal claim as a candidate mechanism.** The concept of a non-vanishing individual cost component — one that resists socialization — is structurally interesting. In the protocol ossification context: are there protocol features that are "irreducibly personal" in the sense that they cannot be distributed across more participants? If so, those features may be sites of particular resistance to modification, because modification would require reassigning the irreducible claim, not just redistributing a collective one.

**The manipulation-generosity tension as a general law candidate.** [inference] Any allocation mechanism that discounts individual burden based on group size faces a manipulation boundary: discount too fast, and the rule enables gaming; too slow, and collaboration is penalized. The harmonic number appears to be the manipulation boundary in this specific setting. Whether analogous boundaries exist in other allocation protocols is worth investigating.

---

## 8. Candidate Laws

**Candidate: The Manipulation Boundary Principle**

[text, pp.5-6]: "The inequality f(a) ≥ f(1)/H_a is a necessary condition for resistance to manipulation: any cost that decays faster than f(1)/H_a as coauthors are added would let an author inflate their total accumulated credit by padding author lists."

**Candidate formulation:** In any collective action protocol that allocates individual burden as a function of group size, there exists a minimum decay rate for per-member cost below which the protocol becomes gameable through artificial group inflation. The harmonic number defines this boundary in protocols where individual credit decays according to the Hodge-Greenberg model.

**What would falsify it:** A protocol where per-member cost decays faster than 1/H_a without enabling credit accumulation through author padding — i.e., a faster-decaying rule that is nonetheless manipulation-resistant, which would require either a different credit model or a different gaming mechanism not considered here.

**Note:** This candidate is narrow — it inherits the specific credit model assumption. Generalization to other domains would require showing that analogous manipulation boundaries exist under different credit functions. Marking as `speculative` pending cross-domain investigation.

---

## 9. What Surprised Me / What Doesn't Fit

**The irreducible personal claim is asserted, not derived.** Shah introduces β as an "irreducible personal claim" [text, p.7] and offers intuitive justification (your name is attached, you consume pipeline resources), but there is no principled derivation of what fraction of the cost is irreducible. The parameter N∞ is left to organizers to set. This is the soft joint in the argument — the harmonic component is derived, but the floor β is stipulated. The paper is more honest about this than it initially appears: the derivation determines the form of f, not its magnitude.

**The generalized framework sacrifices manipulation resistance.** The generalized rule (Algorithm 2) with p < 1 is explicitly not manipulation-resistant [text, p.4]. Shah notes this as a tradeoff: organizers can choose faster-growing rules but lose the guarantee. This is an honest acknowledgment, but it means the unified framework is not a unified derivation — the manipulation-resistance derivation only covers p=1. The generalization is a parameterization, not a principled extension.

**The credit model itself is not examined.** The Hodge-Greenberg model is cited as "empirically validated" [text, p.6], but no detail is given about the validation conditions, the fields covered, or potential domain-specificity. The harmonic quota rule's principled grounding depends entirely on this model's generality. If the credit model is field-specific (e.g., different in mathematics with alphabetical authorship vs. biology with contribution-ordered authorship), the derived rule may not generalize across scientific communities. This is not acknowledged.

**Author ordering as an unresolved assumption.** Shah explicitly notes [text, p.9] that the paper makes no assumptions about whether author order reflects contribution. But the Hodge-Greenberg credit model assigns credit by rank — lead author gets the most. If author ordering in a given venue doesn't track contribution rank, the model's empirical grounding is broken. The paper identifies this as future work rather than a current limitation, which may understate the problem.

---

## 10. What It Opens

**Immediate questions:**
- Does the harmonic number as manipulation boundary generalize to non-academic allocation protocols? The paper studies submission quotas; the mechanism seems domain-independent if the credit model is. Worth a field trip to other scarce-resource allocation systems (telescope time is mentioned; what about compute cluster time, ICU bed allocation, spectrum licensing?).
- Are there institutional protocols that function like the fixed quota rule — ignoring collaboration effects — that would be improved by the harmonic substitution? The regulatory domain seems likely.

**Related texts:**
- Hagen (2008, 2010, 2013) — the empirical credit model this paper depends on. If I'm going to use the Harmonic Quota finding in cross-domain analysis, I need to understand the credit model directly, not through Shah's summary.
- Ostrom's work on commons governance — Ostrom designed allocation rules for common-pool resources with analogous manipulation-resistance requirements. The harmonic quota may be a special case of a more general class of manipulation-resistant allocation rules that she characterizes.
- The 2025 paper cited [CLL+25] on "Dissecting submission limits in desk-rejections: A mathematical analysis of fairness in AI conference policies" — directly in the same problem domain, likely to contain counterexamples or complications.

**Live thread opened:** The concept of the "irreducible personal claim" — cost components that don't vanish as group size increases — is a structural feature that may appear across many protocol types. I want to run a field trip examining where this structure appears outside academic submission systems: environmental permits, criminal liability, debt obligations, professional licensing. If it's general, it deserves its own formalization.
