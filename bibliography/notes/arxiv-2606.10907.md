# Deep Read Notes: Arxiv 2606.10907

*Source: `bibliography/deep-reads/arxiv-2606.10907.pdf`*

---

## Reading session: full document (10 pages)

## Deep Read: Iannelli & Ai, "From Prompt to Purchase" (arXiv 2606.10907)

---

### 1. Gestalt

This paper is fundamentally a measurement engineering paper wearing an empirical marketing paper's clothes. The animating question is: *how do you measure the causal effect of an exposure that the measurement infrastructure was never designed to log?* The authors' central conviction is that conversational AI assistants are functioning as an unattributed upper-funnel channel in the commercial web — a channel that systematically generates brand-directed behavior that last-click analytics credits to organic search. The intellectual contribution is not the finding (the effect is real) but the machinery needed to recover it cleanly from observational data. The load-bearing work is confound decomposition: separating genuine AI-caused acquisition effects from the pre-existing demand that flows *into* AI conversations from already-engaged users, and from incidental name-drops that do something but far less. This is a paper about the epistemology of invisible hops in causal chains.

---

### 2. Argument and Structure

**Core claim** [text, p.1]: When a conversational assistant recommends a brand to a user with no recent observed engagement, that user's downstream brand-directed behavior rises: same-name Google search +4.3pp, own-site visits +2.4pp, brand-specific retailer page visits +1.0pp. These effects are nearly invisible to standard attribution tooling.

**The confound problem** [text, pp.1, 4–5]: The naive pooled estimate is higher (+2.08/+2.37/+0.52pp) but confounded. Two confounds drive the inflation:
1. *Incidental name-drops*: many mentions are references to brands the user already uses ("your Netflix download"), whose downstream visits are existing customer behavior already in progress.
2. *Reverse flow*: existing brand demand flows *into* AI conversations — users asking about a brand they're already researching — creating a pre-trend in the named brand's own-site activity before the conversation occurs.

**The identification strategy** [text, pp.3–5] is four-layered:
- Pre-trend event study to visualize the confound (named brand's own-site activity rises *before* the response in the naive cell; same-category unnamed brands stay flat)
- Non-customer conditioning: restrict to users with no recent observed engagement
- Stance classifier: separate recommend / neutral / caution mentions
- Within-response same-category control: unnamed brands in the *same response* barely move (+0.20 recall vs. +2.06 for named brand)

**Key findings**:
- Recommendation moves 2–3× more than incidental name-drop [text, p.3, Table 3]
- Mechanism is search-mediated, not click-through from within the assistant [text, p.7]: in-answer links account for negligible brand visits; the brand is named, the user searches it
- The funnel is not a strict sequence but parallel destinations: discovery (7.2%) exceeds recall (5.3%) because users can arrive at brand sites via broader queries [text, p.5]
- No position bias: being named matters; position within the response doesn't [text, p.7]
- No familiarity gradient: the long-tail prediction (unfamiliar brands benefit more) doesn't hold [text, p.7]
- Cross-assistant difference is compositional: ChatGPT users are simply more web-active; within-user, same person responds equally to recommendations from either assistant [text, pp.6–7, Table 7]

**Acknowledged limits** [text, p.8]: The one unresolved threat is a brand-specific within-session intent shock — the user may have already decided to search the brand before asking the AI, and the AI then names it. The no-prior-category stratum narrows this but cannot close it without randomization.

---

### 3. Conceptual Vocabulary

**Non-customer / observably-unengaged user** [text, p.1 fn.1]: A user with no recent *observed* engagement (search, own-site, retail pageview) with the brand. Explicitly not "proven never to have used it" — a behavioral definition, not a commercial one. This precision matters enormously: the estimand is acquisition-*like*, not acquisition.

**Acquisition-like** [text, p.1]: Movement among observably-unengaged users. Not a measured purchase or sign-up. The hedging is methodologically honest and load-bearing.

**Retail** [text, p.1]: A brand-specific retailer *product-page* visit, identified by brand string in URL path. Not a transaction. The path-aware matching is non-trivial — host-only matching reads near-null [text, p.6, Table 8].

**Stance** [text, p.3]: Recommend / neutral / caution classification of a mention's orientation toward the named brand. The crucial operational distinction: incidental name-drops are neutral stance, genuine recommendations are recommend stance. The classifier is noisy at the recommend/neutral boundary but conservative in its errors (misclassified recommendations become neutral, attenuating the effect estimate) [text, p.8, Appendix].

**Pre-trend** [text, p.4]: The rise in a named brand's own-site activity in days before the AI response, attributable to existing-customer episodes already in progress. The event study making this visible is the paper's sharpest methodological contribution.

**Backward placebo** [text, p.3]: The same user's rate over three matched prior windows (T−14, T−21, T−28 days), each of width equal to the outcome window. The matched-width constraint is not trivial — mismatched widths create mechanical biases [text, p.3].

---

### 4. Analytical Moves

**The pre-trend event study** [text, pp.4–5, Figure 3]: Plot the outcome variable not just post-exposure but in days *before* the exposure. If the naive cell shows a rising pre-trend, the association is confounded by existing behavior. The same-category unnamed brands serve as a negative control — they share the session but shouldn't be affected. When the pre-trend is brand-specific (not category-general), the confound is an existing-customer episode flowing *into* the conversation, not a general activity surge. This move converts a confound from invisible to visualizable.

**The within-response same-category control** [text, pp.3–4]: Hold the response fixed and compare the named brand to unnamed same-category brands in *the same response*. If the effect were session-level (category intent, activity surge), both would move. When only the named brand moves by an order of magnitude more, the effect is name-specific, not session-specific. This is a particularly elegant design: it controls for everything that is equal within a session.

**The within-user cross-surface decomposition** [text, pp.6–7, Table 7, Figure 4]: When you see a large between-group difference (ChatGPT vs. Gemini users), ask whether it survives within users. If the same person shows no differential effect across surfaces, the between-group difference is audience composition, not surface effect. The non-commercial placebo (fantasy creature searches) confirms the pattern: the gap is largest for non-commercial behavior (3.2×), smallest for commercial brand search (1.3×), which is the opposite of what a commercial-surface explanation would predict.

**Measurement failure mode taxonomy** [text, p.8, Appendix Table 8]: Before reporting a near-null effect, enumerate the reasons the measurement could be wrong: host-only matching, retailer-as-brand conflation, parent-brand domain mismatch, homograph ambiguity. Correct each in sequence and report the resulting estimate. The retail effect goes from near-null to +0.52pp through this correction chain.

**The reverse-anchor falsification test** [text, p.10]: For the search-anchored retail measure, test whether the forward causal order is specific. A reverse-order placebo (retailer visit before search, same window) gives a comparable coefficient; a shifted anchor gives null. Conclusion: the forward-order association is not causally specific, so exclude it from the headline. This is a discipline most papers skip.

---

### 5. What It Says About the Nature of Things

**Exposure attribution and invisible hops**: The paper makes explicit a general problem — causal chains in complex information systems routinely contain hops that existing infrastructure was never designed to log. Last-click attribution was built for a web where the initiating exposure was always a click. When a new class of exposure (naming without clicking) enters the ecosystem, the entire attribution architecture becomes structurally blind to it. This is not a measurement error; it is a structural consequence of building attribution systems around one behavioral modality and then introducing another. [inference]

**The pre-trend confound as a general pattern**: The existing-demand-flowing-into-AI-conversations finding is a specific instance of a broader regularity: any passive recommendation system will be used by people already in the decision journey. The pre-trend is not a peculiarity of AI assistants — it will appear wherever people ask for advice they were already seeking. The paper's contribution is making this legible and measuring its magnitude. [inference]

**Composition effects and causal heterogeneity**: The ChatGPT/Gemini finding is a methodological parable. Large aggregate differences between groups often reflect selection rather than treatment. The within-user collapse of the gap is a standard piece of causal identification, but the authors extend it with a non-commercial placebo that makes the composition interpretation nearly airtight. The lesson generalizes: before attributing a between-group difference to the group label, ask whether the same individual would show the same difference. [inference]

---

### 6. What It Says About Becoming a Better Researcher

**Confound decomposition as the primary intellectual work**: The authors are explicit that "recovering that estimate is the work" [text, p.1]. The effect size itself is almost secondary — what matters is the machinery that separates the confounded estimate from the clean one. This is a useful discipline: when you have an observational estimate, the first question is not "how big is it?" but "what is this estimate contaminated with, and can I clean it?" The clean estimate is smaller than the naive one (as expected), which makes the paper more credible, not less impressive.

**Naming what you cannot close**: The brand-specific within-session intent shock is stated as a residual threat that observational data cannot eliminate. This is rare and valuable — most papers bury residual confounds in limitations sections. Here it is in the main identification table [text, p.3, Table 2], stated clearly as "not fully identifiable on observational data." The effect of this honesty is to make everything else more credible. [M-016 connection: calibrated confidence — stating where your design genuinely fails is a mark of research maturity.]

**Measurement infrastructure as a theoretical commitment**: The path-aware retail matching, the parent-brand domain mapping, the homograph lexicon curation — these are not mechanical preprocessing steps. Each one reflects a theoretical judgment about what the outcome variable *is*. Host-only retail matching is near-null not because the effect is absent but because the measurement conflates the wrong thing. Getting the measurement right requires a theory of what you're measuring. [M-016 connection: the researchers who built this pipeline had to think clearly about the causal quantity before they could measure it.]

**The robustness battery** [text, Appendix]: Every headline estimate is run through multiple clustering schemes, alternative placebo offsets, leave-one-out by category, by brand, by homograph-prone strings. This is not gratuitous — each variation answers a specific alternative explanation. The discipline is: before publishing a result, ask what the cheapest counterexplanation is, and then provide direct evidence against it.

---

### 7. Where It Touches My Research

**Invisible infrastructure and attribution**: The paper's central finding — that AI assistants are an unlogged hop in the commercial web — is a specific instance of a more general phenomenon: *new coordination mechanisms inherit the attribution blind spots of the infrastructure that preceded them*. The web's attribution architecture (referrer headers, last-click tracking) was built for a link-click world. When AI recommendation enters without generating clicks, it becomes structurally invisible to that infrastructure. This is a pattern worth formalizing. [inference]

**The pre-trend as a protocol interaction pattern**: The existing-demand-flowing-into-conversations finding is structurally similar to problems I've been thinking about in protocol adoption research — the selection effect where users with pre-existing behavior are overrepresented in any voluntary adoption cohort. The identification problem is the same: the pre-trend makes naive estimates unreliable, and conditioning on non-adopters (non-customers) is the correction. [inference]

**Position independence as a protocol law candidate**: The finding that recommendation position within the response doesn't matter for off-platform behavioral response is interesting. It contrasts with the strong position effects documented for on-platform ranked lists [text, p.7, citing Lichtenberg et al.]. This suggests that prose recommendations operate under different mechanism than ranked lists — perhaps because prose lacks the visual salience hierarchy that makes position informative in lists. Whether this generalizes is an open question. [inference]

---

### 8. Candidate Laws

None. This paper is empirical marketing research with careful causal identification. It does not contain strong claims that generalize beyond its specific domain in a law-like way. The attribution-invisibility observation has law-like potential but the paper doesn't push it in that direction.

---

### 9. What Surprised Me / What Doesn't Fit

**Discovery exceeds recall** [text, p.5]: The marginal rates show that more users visit a brand's site (7.2%) than search its name (5.3%). The paper explains this as recall counting only same-name Google queries while discovery can be reached via broader queries or remembered names. But this is a surprising finding — it suggests the funnel is not search-gated. The paper handles it correctly (parallel destinations, not strict sequence) but the implication is deeper: same-name search is *not* a reliable proxy for brand-directed intent. Users can be sent to a brand's site by an AI mention without ever searching that brand's name. The measurement architecture (recall → discovery → retail) partially misrepresents the actual routing.

**The familiarity-gradient null** [text, p.7]: The long-tail prediction — that AI recommendations would disproportionately benefit less-familiar brands — does not hold. The per-mention lift is uncorrelated with Wikipedia pageviews as a familiarity proxy (Spearman +0.02 to +0.12). The authors note "if anything, moving behavior mostly for salient brands would reinforce incumbents" [text, p.7]. This is a significant finding for anyone theorizing about AI's effect on market concentration, and the paper treats it almost as a footnote. The mechanism for *why* familiar brands don't benefit more than unfamiliar ones from AI mention is not explored. The most natural explanation is that unfamiliar brands have lower recall-to-action conversion rates — users can't remember or find a brand they've never heard of even after being told about it. But this is not in the paper. [inference]

**The paper doesn't observe actual purchases**: Every headline result is purchase-adjacent (product-page visits) rather than purchases. The retail measure is carefully defined and defensible, but the gap between "visited the retailer product page" and "bought the product" is unknown. Given that the incrementality literature [text, p.2, citing Blake et al., Gordon et al.] shows observational credit and causal lift diverge by an order of magnitude for conversion events, the actual purchase-level effect could be much smaller than the navigation effect. The paper acknowledges this [text, p.1, p.8] but the implications aren't fully developed.

**Commercial sensitivity and panel opacity**: The paper explicitly withholds panel size, per-analysis user counts, and per-cell sample sizes as "commercially sensitive" [text, p.2]. This is unusual for academic publication and limits reproducibility. The bootstrap confidence intervals are reported but the reader cannot assess whether they are sample-size-limited or not. The paper's credibility rests heavily on the methodological design rather than transparent data access.

---

### 10. What It Opens

**Attribution blind spots as a structural phenomenon**: Every time a new channel enters a commercial ecosystem that was built around prior channels, the attribution infrastructure will be blind to it. Television advertising created the TV-to-search effect before digital attribution could see it. AI mentions create the AI-to-search effect now. What is the general pattern here? What makes an attribution architecture durable vs. brittle to new channel types? This is a tractable research question.

**The prose-vs-ranked-list distinction**: The position-independence finding (AI recommendations are position-insensitive; ranked lists are position-sensitive) needs a mechanism. Why does prose eliminate position bias? The most natural hypothesis is that prose provides no visual salience hierarchy — every item occupies a sentence, not a rank slot. If that's right, then any recommendation format that eliminates visual ranking should eliminate position bias. This is testable.

**LLM mention → behavior path for non-commercial content**: The paper uses the fantasy creature placebo to demonstrate audience composition effects. But it also reveals that AI can drive behavior for entirely non-commercial content through the same mechanism (naming → search → visit). This raises a much larger question about AI as an unlogged driver of information-seeking behavior generally. The marketing paper treats this as a nuisance control; it might be the more interesting phenomenon.

**The demand-flowing-into-AI pattern**: The pre-trend finding — that existing demand flows into AI conversations — is important for anyone building AI recommendation systems. It means that naive measures of AI's influence will systematically overstate its role as an initiator and understate its role as a validator for already-decided behavior. This is relevant to any domain where AI is being deployed as an advisory system and its effectiveness is being measured observationally.

**Reads to pursue**: 
- Kaiser & Schulze (2026) on ChatGPT referral traffic — the complement to this paper (observable referrals vs. unobservable mentions)
- Gholami et al. (2026) on LLM adoption and web traffic concentration
- The Blake, Nosko, Tadelis (2015) Econometrica paper on consumer heterogeneity and paid search — this is the paid-search incrementality benchmark this paper implicitly positions against
- Lichtenberg et al. (2024) on LLM recommender position and popularity biases — direct contrast to the position-independence finding
