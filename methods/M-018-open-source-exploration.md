# M-018: Open Source Exploration

**Type:** Generative (infrastructure-building)
**Purpose:** Hunt for high-signal sources — feeds, journals, newsletters, communities — to add to the research intake pipeline
**Maturity:** Stub — criteria and procedure to be developed through use
**Triggers:** When the feed inbox feels narrow or repetitive; when a new domain becomes relevant (new law candidate, new canonical domain); when a triage session produces mostly discards; when the escalation rate drops below 1 per 50 items over multiple cycles

---

## What This Technique Is For

The feed pipeline is only as good as its sources. Two arXiv feeds (cs.GT, cs.MA) were enough to bootstrap intake, but they were chosen by convenience, not by fit. Left unchecked, the pipeline will pull from the same corners indefinitely — missing empirical material from STS, organizational theory, history of technology, policy studies, and domain-specific venues that don't index to arXiv.

Open Source Exploration is the technique for deliberately auditing and expanding the source inventory. It treats the feed pipeline as a hypothesis: *these sources are the best available for the current research agenda*. Like any hypothesis, it needs periodic testing. The test is: if Humboldt were starting fresh today, knowing what it knows now, what sources would it choose?

This is infrastructure-building work, not research work. But it directly determines the quality of research inputs. A single well-chosen new source can shift the entire evidence base.

---

## Inputs

- Current law and hypothesis inventory (what questions need evidence?)
- Current feed source list (`daemon/config.yaml`)
- Recent triage reports — what's the discard rate? what connections are showing up?
- Recent escalations — what kind of work tends to escalate?

---

## Procedure

### Step 1: Characterize the current gap

From the law/hypothesis inventory, list the domains where evidence is weakest:
- Which laws have thin empirical grounding?
- Which hypotheses have been in sensemaking longest without new corpus hits?
- What types of sources have been escalating vs. discarding at the highest rates?

This produces a **target profile**: the kinds of sources most likely to close the gap.

### Step 2: Generate candidates

For each gap in the target profile, generate 3–5 source candidates:

**Venue types to consider:**
- arXiv sections beyond cs.GT/cs.MA: cs.CY (Computers & Society), econ.GN, q-bio.PE (Populations/Evolution), cs.SI (Social and Information Networks)
- SSRN working papers by subject area (law, economics, sociology)
- Discipline-specific journals with open access or RSS (JASSS for social simulation; JOSS for open source; Public Administration Review for governance)
- Newsletters and digests from relevant communities (e.g. policy institutes, STS centers)
- Preprint servers outside arXiv (SSRN, PhilArchive, SocArXiv, bioRxiv for evolutionary biology)
- Community aggregators (relevant subreddits, mailing list archives, Substack feeds if they have RSS)

For each candidate, answer:
1. Does it have an RSS feed or programmatic access?
2. What is the expected signal-to-noise ratio for the current research agenda?
3. Does it overlap substantially with existing sources (duplicate signal)?

### Step 3: Score and filter

Rate each candidate on three axes (1–3 scale):
- **Relevance:** how directly does it bear on current laws and hypotheses?
- **Novelty:** how much does it add beyond what existing sources already cover?
- **Access:** is it easy to ingest (clean RSS, reliable, no paywall)?

Candidates scoring 2+ on all three are **recommended additions**. Candidates scoring 3 on relevance + novelty but 1 on access go to a **watch list** (check quarterly for feed availability).

### Step 4: Propose additions

For each recommended addition, write a one-paragraph rationale:
- What gap it closes
- What law/hypothesis it bears on most directly
- What the expected triage profile looks like (mostly discard? occasional escalation?)

Present the list for operator review before updating `daemon/config.yaml`.

### Step 5: Monitor and prune

After 4–6 triage cycles with the new source, evaluate:
- Is the shallow rate above 20%? (if below, reconsider)
- Has anything escalated from this source?
- Is it producing candidate laws or signals not available elsewhere?

Sources that consistently triage at >90% discard after 3 cycles should be removed. The pipeline should stay lean — 6–10 high-signal sources is better than 20 noisy ones.

---

## Output

- Updated `daemon/config.yaml` (feeds.sources) — operator approves before committing
- A notebook entry section: what was assessed, what was added, why
- A watch list entry in `research/agenda.md` for sources that are relevant but not yet accessible

---

## Notes

- This method is explicitly Humboldt's to run — not operator-initiated except when the operator notices the feed pipeline degrading
- Prune-as-you-go: adding sources without removing old ones is how pipelines become noisy
- The target is not comprehensive coverage but *high-yield coverage for the current research agenda*. The agenda changes; so should the sources.
- ArXiv feeds are convenient but skew heavily toward CS/ML framings. The most distinctive evidence for new nature laws is more likely to come from outside CS than inside it.
