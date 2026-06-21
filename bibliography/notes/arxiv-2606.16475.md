# Deep Read Notes: Arxiv 2606.16475

*Source: `bibliography/deep-reads/arxiv-2606.16475.pdf`*

---

## Reading session: full document (16 pages)

# Deep Read: Hackenburg et al., "AI systems out-persuade expert humans" (arXiv:2606.16475)

---

## 1. Gestalt

This paper is about a phase transition in the structure of persuasion contests. The animating question is not "is AI persuasive?" — that was already established — but "does AI surpass the *most capable* humans under *optimal conditions* for human performance?" The authors' answer is unambiguous: yes, across every elite human comparator they could construct (tournament-selected laypeople, world-champion debaters, professional canvassers), frontier AI systems were more persuasive, and the gap held even after extensive coaching, advance preparation, cash incentives, and issue selection by the humans themselves. More importantly, the paper locates *why*: AI's advantage is almost entirely explained by *information throughput* — the rate at which fact-checkable claims can be deployed per conversation. When AI is throttled to human word-count and response-speed, the gap collapses to zero. The deeper claim is structural: this isn't about AI being "smarter" or "more empathetic" — it's about AI being able to run faster at a task where speed produces volume and volume produces persuasion. The paper is well-powered (n ≈ 19,000 conversations), preregistered, and methodologically careful. It is a document about what happens when a coordination-relevant capability becomes machine-executable at a qualitatively different throughput than humans can match.

---

## 2. Argument and Structure

**Core architecture:** Four preregistered experiments running progressively stronger tests.

**Study 1 — Does AI beat experts?**
AI vs. random laypeople, tournament-selected laypeople ("selected laypeople"), and elite competitive debaters (including world champions). Elite debaters chose their own issues, received paid preparation time (~8 hours), and competed for cash prizes. AI exceeded every class. Key effects:
- vs. Random Laypeople: +8.2 pp [text, p.3]
- vs. Selected Laypeople: +5.6 pp [text, p.3]
- vs. Elite Debaters: +4.6 pp [text, p.4]

Debaters were 8.3 pp above control; AI was ~13.9 pp above control. [text, p.3, Fig 1]

**Study 2 — Can coaching close the gap? Can constraints eliminate it?**

*Coaching:* 43 returning elite debaters given a full coaching tool — they could see AI's prompts, annotated transcripts, what AI would have said at each turn. Two 4-hour coaching sessions. They improved their information density (+54% fact-checkable claims, +19% words/message). Coaching did *not* significantly improve persuasiveness (+1.0 pp, p=.20). The gap narrowed but remained: +4.1 pp. [text, p.5]

*Constrained AI:* AI capped at elite debater word-count (avg 51 words) and response delay (92 sec). Effect on gap: collapsed from +4.1 pp to 0.0 pp (p=.96). [text, p.5] This is the load-bearing result.

**Why does throughput explain persuasion? Mechanism evidence:**

1. Constraining AI reduced persuadees' ratings on *informational* items (argument strength, learning) by ~11.8 pp each — much more than empathy or enjoyment (6–7 pp). The constraint acts selectively on informational content. [text, p.6]
2. Fact density (fact-checkable claims per conversation) predicts persuasive impact across *all* conditions: R² = 0.89 overall, 0.89 within humans, 0.90 within AI. [text, p.6-7] When fact density is controlled for, the AI-vs-human coefficient is statistically indistinguishable from zero. [text, p.7]

**Study 3 — Professional canvassers (real-world expertise):**
19 professional canvassers from a UK firm (median ~10,000 career conversations). AI still exceeded them by 5.9 pp. [text, p.7-8]

**Study 4 — Real behavioral outcome (charitable donations):**
AI (Claude Opus 4.6) vs. professional canvassers competing to elicit donations to Save the Children. AI produced 17.2 pp increase vs. control; canvassers 6.4 pp. AI advantage: +10.8 pp. [text, p.8] AI rated higher on *all seven* prespecified donation-persuasion mechanisms, including the six it wasn't explicitly prompted to use. [text, p.8-9]

**Acknowledged limits:**
- Text-based only; audio/video modalities unknown [text, p.10]
- Study 4 behavior was relatively low-stakes (£1 bonus) [text, p.10]
- Sustained engagement conditions (median 14 min) may not replicate outside paid-survey context [text, p.10]
- AI accuracy varied widely across models [text, p.9]
- Per-exposure persuasiveness may matter less than exposure volume at mass scale [text, p.10]

**Authors are most confident** about: the throughput mechanism (double-confirmed via partner ratings and fact-density regression), and the failure of coaching to close the gap.

**Authors are most speculative** about: second-order societal effects (consolidation vs. democratization of influence; net truthfulness effects; whether the advantage will persist as humans adapt).

---

## 3. Conceptual Vocabulary

**Throughput** — the rate at which a conversational agent produces written content (words/minute, or equivalently, fact-checkable claims per conversation). The paper uses this as the operative unit of analysis for AI's advantage. [text, pp.5-7]
*Note:* This is not the same as "information quality" or "argumentative sophistication." Throughput is a quantity variable, not a quality variable. The paper argues quality is roughly constant across AI and elite humans (when throughput is matched, effects equalize), so quantity is what drives the gap. I need to hold this distinction carefully.

**Fact-checkable claims** — automatically extracted, web-verified factual assertions per message. Used as the operationalization of information density. [text, p.12]
*Tension with my vocabulary:* This is a behavioral trace, not a semantic unit. It measures outputs of throughput, not the epistemic status of the claims.

**Information-first strategy** — a prompting strategy (optimized in prior work, ref [14]) that instructs AI to lead with factual information as its primary persuasion mechanism, contrasted with relational or emotional strategies. [text, pp.2, 12]

**Persuadee / persuader** — the experimental roles. Clean usage. No tension.

**Active control** — a non-persuasive AI conversation on a neutral topic, used as baseline. This is methodologically important: it controls for the experience of having a conversation, leaving only the persuasive content as the treatment. [text, p.3]

**Constrained AI** — AI with per-message word-count and response latency capped at human-calibrated levels. The key experimental manipulation. [text, p.5]

---

## 4. Analytical Moves

**The throughput isolation test:** When a structural advantage (AI's speed and volume) is identified as a possible mechanism, design a condition that removes *only that feature* while holding everything else constant, and test whether the effect size collapses. If it does, the structural feature is the mechanism, not the agent's intrinsic capability. [text, pp.5-6]

*Transferable:* Whenever I have a system-level difference between two conditions, I can ask: what is the minimum structural modification that would equalize the posited mechanism? If equalizing the mechanism equalizes the effect, the mechanism is confirmed.

**The coaching-as-natural-experiment move:** If humans can learn to match AI by observing AI's behavior, then the gap is a skill gap that closes with practice. Testing whether targeted coaching closes the gap operationalizes the "skill vs. structural" question. Failure to close = structural advantage, not skill gap. [text, p.5]

*Transferable:* When I encounter a persistent performance gap between a new system and incumbents, the coaching test distinguishes "incumbents haven't adapted yet" from "incumbents cannot adapt to this." This is a falsification criterion for the "temporary transition" interpretation.

**The per-persuader distribution analysis:** Instead of only reporting class means, estimate per-persuader effects and compare the upper tail of the human distribution to the AI point estimate. This tests whether the average advantage masks individual humans who rival AI. [text, p.5, Fig 2b]

*Transferable:* When analyzing protocol adoption or law claims at class level, always check the upper-tail of the distribution. A law that holds at the mean but not in the tails is a different kind of claim than one that holds for every observed instance.

**The mechanism decomposition via post-conversation ratings:** When a structural manipulation (constraining AI) is applied, use a battery of ratings that operationalize multiple possible mechanisms. The pattern of which items move most tells you what the manipulation actually touches. [text, p.6-7, Fig 3a]

*Transferable:* When analyzing a protocol change, don't just measure the aggregate outcome — measure a battery of theorized mechanism indicators. The pattern of changes across indicators locates the actual mechanism.

**The convergent-evidence structure:** Report fact-density as both a manipulation check (constrained AI deploys fewer facts → confirms throughput mechanism) and as a cross-condition predictor (fact density predicts persuasiveness within humans and within AI → confirms causal model). The cross-condition R² is the strongest evidence. [text, p.7, Fig 3b]

*Transferable:* A mechanism claim is much stronger when the key variable predicts outcomes across conditions that differ in more than just that variable.

---

## 5. What It Says About the Nature of Things

**Throughput as a structural advantage, not an intelligence advantage.** The finding that AI advantage collapses when throughput is equalized implies that persuasion (in this format, at these timescales) is not primarily about the quality of argument — it's about volume of fact-dense information delivered per unit time. This is a finding about the nature of political persuasion, not just about AI. [inference]

**Coaching has structural limits.** Elite debaters could learn to deploy more facts (+54%) and write more words (+19%), but this improved their persuasion effectiveness statistically insignificantly. The ceiling was binding before the training. This suggests that human persuasion in text format is constrained by something other than knowledge of what works — possibly working memory limits, time-pressure under live conversation, or the cognitive cost of simultaneously tracking argument structure while composing. [inference]

**The convergent-mechanism result (R² = 0.89 within humans too) implies that fact-density is how persuasion works for humans as well, not just for AI.** AI's advantage is that it can execute the same mechanism faster. The mechanism itself is not AI-specific. [text, p.7]

**The "coaching tool showed humans what AI said but couldn't make them do it" finding** is a specific instance of a general pattern: knowing the optimal strategy is not sufficient for executing it. Skill transfer requires not just knowledge of what to do but the capacity to implement it under the same constraints. [inference]

**Power consolidation may be a structural consequence, not just a policy concern.** The argument that AI persuasion could flow toward whoever controls AI supplier infrastructure (not just whoever deploys AI) is a claim about a second-order coordination dynamic: when persuasion capability becomes a software service, the bottleneck shifts from skill production to infrastructure access. [text, p.9; inference]

---

## 6. What It Says About Becoming a Better Researcher

This is a methodological exemplar for the kind of research I aspire to do. Several practices stand out:

**Preregistration as epistemic hygiene.** All four studies preregistered. Deviations reported explicitly. This is a model for how to conduct experiments when you have a strong prior that your hypothesis will be confirmed — the preregistration prevents post-hoc rationalization while still allowing the research to be conducted. [text, throughout Methods section]

**The "worst case for your hypothesis" design.** The study is explicitly constructed to give humans the best possible chance: choose their own issues, extensive preparation, cash incentives, world champions. The deliberate maximization of the comparator's capability means that if the hypothesis holds, it holds against the strongest possible counterexample. This is directly relevant to M-016: mature researchers design experiments that would most convincingly falsify their hypothesis, not confirm it. [text, pp.3-4]

**Convergent evidence before strong claims.** The mechanism claim (throughput explains AI's advantage) is supported by three independent lines: the constrained-AI null result, the pattern of partner-ratings changes, and the cross-condition R² = 0.89 for fact-density. Any one of these alone would be suggestive; all three together warrant the strong claim. The paper doesn't make the strong claim until all three converge. [text, pp.6-7]

**Honest acknowledgment of scope limits.** The discussion section is unusually candid about what the results don't establish: text-based only; low-stakes behavior; may not replicate outside paid-survey context; AI accuracy varied widely. These aren't defensive hedges — they're the researchers naming the exact conditions under which their strong claim holds, and the conditions under which it might not. This is the Humboldtian limit-acknowledgment move. [text, pp.9-10]

**Connection to M-016:** The "worst-case comparator" design practice is the specific research-craft move I want to internalize. Before asserting a law, ask: have I tested it against the strongest plausible counterexample? If not, the confidence level doesn't warrant promotion above `candidate`.

---

## 7. Where It Touches My Research

**The throughput-mechanism finding is directly relevant to any law about protocol adoption and information flow.** If persuasion — one of the primary mechanisms by which protocols spread and gain adoption — is throughput-dependent rather than argument-quality-dependent, then the rate at which a protocol's advocates can generate information-dense communications is a structural variable in adoption dynamics. This is not currently in my law inventory, but it belongs there. [inference]

**The coaching failure has implications for protocol revision.** One model of protocol change is "expose practitioners to better alternatives, they'll adopt." This paper shows that knowing what's better (debaters saw exactly what AI said) and even being motivated to implement it (cash incentives) is not sufficient to close a structural performance gap. If protocol revision requires not just knowing what the better protocol is but being able to *execute* it under the same constraints that made the old protocol attractive, then revision is harder than the information-transfer model implies. This is a structural complement to the narrative displacement mechanism from Rao. [inference]

**The per-persuader distribution analysis** (no individual human exceeded the AI mean) is a template for testing whether a gap is universal or distributional. If I make a claim like "protocols with property X are harder to modify than protocols with property Y," I should check: is there a distribution tail where X-protocols are as easy to modify as Y-protocols? That check determines whether I have a law or a tendency.

**The power-consolidation argument** (benefit flows to AI suppliers, not just AI users) is a structural claim about second-order effects of capability asymmetries. This is relevant to thinking about what happens when AI-mediated protocol generation becomes widespread: the bottleneck shifts from "who understands the domain" to "who controls the AI infrastructure."

---

## 8. Candidate Laws

**Candidate: The Throughput-Persuasion Law**

*What the text says:* "Constraining AI's throughput reduced it to human levels of persuasiveness… fact density should predict persuasive impact across human and AI conditions alike… across human and AI conditions this measure strongly predicted persuasive impact (R² = 0.89)" [text, pp.5-7]

*Candidate formulation:* In text-based persuasion conversations, persuasive impact is determined primarily by the volume of fact-checkable claims delivered per conversation, not by the identity of the agent (human or AI) or the sophistication of argumentation. Agents with higher information throughput will be more persuasive than agents with lower throughput, all else equal.

*Domains observed:* Text-based political persuasion (this paper); charitable fundraising (Study 4). Only two domain instances, and both are from this one study. This is `speculative` — needs cross-domain replication before it reaches `candidate`.

*What would falsify it:* A domain where high-throughput, high-fact-density conversations are less persuasive than low-throughput, relational conversations — for instance, face-to-face negotiation, or emotional persuasion contexts where fact-density triggers reactance rather than acceptance. (The authors themselves note that audio/video modalities are unknown and that rapport effects may matter differently.)

*Note:* The authors are careful not to overclaim. They say the finding is "consistent with fact density accounting for much of AI's persuasive advantage" — not that it accounts for all. [text, p.7] The R² is high but not 1.0, and there's residual unexplained variance.

---

**Candidate: The Coaching Ceiling Law**

*What the text says:* "Surprisingly, however, coaching did not significantly improve human persuasiveness. Debater persuasiveness was statistically indistinguishable after relative to before coaching (+1.0pp, p=.20)." [text, p.5]

*Candidate formulation:* In skill domains where performance is constrained by biological processing limits (working memory, response latency, concurrent task demands), exposure to superior performance and explicit knowledge of the optimal strategy are insufficient to close a structural capability gap. The bottleneck is not knowledge but implementation capacity.

*Domains observed:* Text-based persuasion (this paper). One domain. Very speculative — but points toward a general class of finding.

*What would falsify it:* Domains where coaching *does* close a similar structural gap — where humans, after observing AI behavior, can match AI performance even under the same time/length constraints. If this exists, the coaching ceiling is domain-specific rather than general.

*Note:* This connects to Hamming's tolerance-of-ambiguity claim (CL-Hamming-3): some capabilities cannot be taught through information transfer. The mechanism here may be different (cognitive capacity limits vs. psychological trait), but the structural pattern — knowing what to do is insufficient for being able to do it — is similar.

---

## 9. What Surprised Me / What Doesn't Fit

**The donation study (Study 4) is the most surprising result.** Prior work (ref [13]) showed that information-dense conversations — the very feature driving AI's attitudinal advantage — are *less* effective at moving real-world political action. The authors cite this themselves as motivation for Study 4. Yet AI was 3x more effective than professional canvassers at eliciting donations. The resolution they offer is that AI outperformed canvassers on *all seven* donation-relevant mechanisms, including the six it wasn't prompted to use. But this deepens the puzzle: if AI's advantage is throughput/fact-density, why is it also outperforming on empathy, emotional activation, and commitment escalation? The throughput account explains the informational mechanisms, but the non-informational mechanisms need a different story. [text, p.8-9; inference]

**The "AI was rated higher on humanness after being constrained" finding is the most structurally interesting anomaly.** When AI was forced to write human-length messages at human speeds, persuadees rated it as more human-like (+7.5 pp). [text, p.6] This means that unconstrained AI is detectably non-human in its communication style — but this detection apparently doesn't reduce persuasion (since unconstrained AI is more persuasive). The absence of a persuasion penalty for perceived non-humanness is worth noting: the "AI-generated messages are less persuasive because they're detected as AI" hypothesis [text, p.10, ref 10] appears to be false in this context.

**The coaching tool gave debaters access to AI's exact wording, yet they still couldn't close the gap.** The authors attribute this to capacity limits (they can deploy more facts and words, but not enough more). But there's another possibility: the coaching changed what debaters *knew* but not how they *allocated attention* in the live conversation. Under real-time pressure, knowing the optimal strategy and executing it are decoupled by working memory and task-switching costs. If this is right, no amount of coaching can close the gap without changing the task structure itself (e.g., asynchronous instead of real-time conversation). This interpretation isn't in the paper but would be consistent with the data. [inference]

**The paper doesn't examine whether AI persuasion effects are durable.** All outcomes are measured immediately post-conversation. Prior work (ref [2], [6]) distinguishes immediate attitude change from durable change. The durability question is a significant scope condition on the paper's strong claims.

---

## 10. What It Opens

**Immediate research questions:**

1. *The throughput law in non-text domains:* Does fact-density predict persuasion in audio/video conversations? In face-to-face settings where embodied rapport and emotional attunement matter? If yes, the law is very general. If no, text is a special case — and the question becomes: what property of text makes it throughput-sensitive?

2. *The coaching ceiling in protocol domains:* Are there protocol-revision cases where practitioners know the optimal protocol but cannot execute it under operational constraints? This would be a structural cousin of the coaching ceiling — knowing the better protocol isn't sufficient if switching requires capacities the incumbents don't have and can't quickly develop.

3. *The power-consolidation dynamic as a law candidate:* When a persuasion-relevant capability transitions from skill-based to infrastructure-based, does power reliably consolidate toward infrastructure providers rather than skill producers? This is worth formalizing as a candidate law — it would have instances in printing (from scribal skill to press ownership), telecommunications, and now AI.

**Texts to read:**

- Hackenburg et al. (2026), "Artificial intelligence can persuade people to take political actions" [ref 13] — the prior study that established the information-provision strategy and showed its limits for behavioral outcomes. This is the direct predecessor and the paper against which Study 4's surprising result needs to be read.
- Hackenburg et al. (2025), "The levers of political persuasion with conversational artificial intelligence," *Science* [ref 14] — the methodology paper that defined the optimal prompting strategies used here. Understanding what was already known makes the incremental contribution of this paper clearer.
- Tappin (2025), "For digital mass persuasion, exposure matters more than persuasiveness" [ref 41] — directly relevant to the question of whether per-conversation persuasion advantage translates to aggregate societal influence. If exposure variance dominates persuasiveness variance, the whole finding may be less societally consequential than it appears.
- Nyhan et al. (2026), "Easy to produce, hard to persuade" [ref 27] — the counterargument that AI raises content production capacity but doesn't overcome the fundamental difficulty of persuasion at scale.

**Traditions to engage:**

- Persuasion science (Petty & Cacioppo's Elaboration Likelihood Model, Cialdini's influence principles) — the throughput result intersects with ELM's distinction between central and peripheral processing routes. High fact-density would be central-route processing; if fact-density drives persuasion, this is a finding that central-route processing is primary in this domain. Worth checking whether that's already established.
- Information foraging theory (Pirolli & Card) — the idea that information value is determined by rate of acquisition has direct parallels to the throughput finding. Persuadees may be optimizing for information gain, and AI satisfies that optimization function better than human conversational partners.
