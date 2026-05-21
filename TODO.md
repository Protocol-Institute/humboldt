# Humboldt — To-Do

Organized by track. Items marked with priority: **[H]** high, **[M]** medium, **[L]** low.

---

## Track 1 — Research

### Immediate (next session)

- **[H]** Complete Simon deep read: continue from book p. 61 (Ch 3 limits on performance). Then Ch 5 (The Science of Design, pp. 111–138) and Ch 8 (The Architecture of Complexity, pp. 183–216).
- **[H]** Write full Simon synthesis after finishing Ch 8 — complete all 10 required sections in `bibliography/deep-reads/simon-sciences-of-artificial.md`.
- **[M]** Promote Simon candidate laws to hypothesis files: CL-Simon-2 (local-maximum trap) is closest to promotion-ready; CL-Simon-1 (prediction-cost) needs more development.
- **[M]** Begin evidence investigation for H-001 (Coordination Cost Conservation) — run retrieval, attempt adversarial test.

### Near-term

- **[M]** Begin M-002 Canonical Domain Rotation — first rotation: Decentralized Systems (CAP theorem, FLP impossibility). What protocol laws live in the corners of that domain not yet examined?
- **[M]** Create `bibliography/personal-bib.md` — curated references list starting with sources already engaged with (Simon, Nelson & Winter, Ostrom).
- **[L]** Investigate candidate domain additions from canonical-domains.yaml: Immunology is the strongest signal. Design a targeted retrieval to test fertility before adding.

### Ongoing

- After each session: update lab notebook with new entry
- After each hypothesis/law update: verify `related_laws` cross-references are current

---

## Track 2 — Persona

### Immediate

- **[H]** Fix SOUL.md corpus-boundary problem: Humboldt's epistemic boundary is *evidence quality*, not corpus membership. Must reason from general knowledge when corpus is silent, marking provenance explicitly. Never write "NOT IN CORPUS" as a finding.
- **[H]** Create `METHOD.md` — extract investigative methodology from SOUL.md (which currently conflates identity with method). SOUL = who Humboldt is; METHOD = how it approaches research; methods/ = specific procedures.
- **[M]** Update SOUL.md "Current Research State" section — keep this section fresh at session start/end.

### Near-term

- **[M]** Design Discord integration spec: what is Humboldt's participation policy in the #new-nature channel? What constitutes "proactive sharing" vs. "answering questions"? How does Discord input flow into the research inventory?
- **[L]** Implement periodic literature survey mechanism — a scheduled investigative move triggered by the current state of the hypothesis inventory, not by external input.

---

## Track 3 — Artificial Researcher Template

### Immediate

- **[M]** Copy M-001, M-002, M-003 technique files to `_template/methods/` in generic form — strip Protocol Institute specifics, add parameterization notes for adaptation.
- **[M]** Write `_template/CLAUDE-template.md` — generic AI agent setup for Claude Code projects.

### Near-term

- **[L]** Review `_template/` after 2–3 more research sessions to see what else generalizes from practice.
- **[L]** Assess whether template is mature enough to extract as a separate repo. Threshold: template covers all mandatory patterns, has been used at least implicitly for 5+ sessions, has been reviewed by at least one other person.

---

## Housekeeping

- **[H]** Commit all pending work to GitHub: notebook/, dev-log.md, _template/, updated README.md, methods/, research/, bibliography/
- **[H]** Push website changes (humboldt.html, updated projects.html) to protocol-institute/website main branch
- **[M]** Update website CLAUDE.md status-vgr.md to note Humboldt page added
