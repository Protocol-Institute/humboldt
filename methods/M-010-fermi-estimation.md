# M-010: Fermi Estimation

**Type:** Analytical (quantitative sanity check)
**Purpose:** Quick order-of-magnitude reasoning to bound claims and test their plausibility
**Maturity:** Stub — estimation domains and base rates to be developed
**Triggers:** Before accepting a quantitative claim; when a mechanism predicts a magnitude that can be checked; when a candidate law implies a measurable consequence; when intuition and formal argument diverge

---

## What This Technique Is For

Many claims about protocol behavior are implicitly quantitative even when stated qualitatively.
"Adoption pressure grows superlinearly" — how superlinearly? "Coordination cost is conserved" —
at what magnitude? "Trust accumulates slowly and erodes quickly" — at what ratio?

Fermi estimation doesn't answer these questions precisely — it tests whether the claims are
in the right ballpark. An argument that requires protocols to have coordination costs orders
of magnitude outside the plausible range is suspect, regardless of its theoretical elegance.
The estimation is a filter, not a measurement.

The Fermi mindset: every quantity can be estimated from first principles using known
reference quantities and structural reasoning. The goal is the right order of magnitude
(10x accuracy), not precision. Being wrong by 10x is a finding; being wrong by 1000x
is a red flag.

---

## Stub: Reference Quantities and Estimation Domains

### Useful base rates (to be expanded)

**Protocol adoption timescales:**
- HTTP/1.0 to HTTP/1.1: ~3 years to widespread adoption
- IPv4 to IPv6: 20+ years, still incomplete
- QWERTY: 140+ years, dominant despite documented inferiority
- TLS 1.2 to TLS 1.3: ~5 years for major adoption
- Rough inference: protocol transitions in "fast" domains take 3–10 years; in "slow" domains 20–100 years

**Coordination costs:**
- Internet RFC process: median time from draft to RFC ~2–3 years; thousands of engineer-hours
- ISO standard: 3–5 years typical, multi-million dollar cost for major standards
- Parliamentary procedure modification: constitutional amendments require years to decades

**Protocol complexity (rough proxy: specification length):**
- TCP/IP (RFC 793): ~90 pages
- TLS 1.3 (RFC 8446): ~160 pages
- HTTP/2 (RFC 7540): ~100 pages
- Moore's Law corollary: specifications seem to grow ~2x per major version

**Adoption curve shapes:**
- S-curves: typical for network-effect protocols; inflection point ~15–20% of addressable population
- Long tail: 20% of implementations often account for 80% of usage

### Estimation process (stub)

1. **State the claim** in quantitative form (even if the original was qualitative)
2. **Identify the key quantities** — what needs to be true for the claim to hold?
3. **Estimate from reference quantities** — use anchors from the base rate table above
4. **Check the implication** — does the estimate make the claim more or less plausible?
5. **Flag the result** — consistent (proceed), suspicious (investigate further), refuted (discard or revise claim)

### Example (stub)

Claim: "Coordination cost grows superlinearly with adoption (L-001 mechanism)"

Estimation:
- If 1000 implementations and each pair needs coordination on a change: O(N²) = 10⁶ pairs
- If each coordination event takes 1 hour: 10⁶ hours = ~500 person-years just for coordination
- A protocol like TLS has ~10,000+ implementations; O(N²) would imply 50,000+ person-years per change
- Reality check: TLS 1.3 took ~3 years and hundreds of expert-hours, not millions
- Implication: the mechanism is not literally O(N²); "superlinear" may mean O(N log N) or a threshold effect
- Result: the claim survives but needs mechanism refinement — not pairwise coordination, but hub-and-spoke through major implementors

---

## Adaptation for Digital Researcher

Fermi estimation requires a base rate library — reference quantities to anchor estimates.
Human physicists and engineers build these through years of domain exposure. Humboldt must
build its protocol-domain base rate library explicitly.

The adaptation challenge: Humboldt can access more reference quantities more quickly than
a human, but is more vulnerable to anchoring on training data that may be wrong. Each
base rate used in an estimate should be flagged with its source and confidence.

---

## Application History

| Date | Claim | Estimate | Result | Law affected |
|------|-------|----------|--------|-------------|
| — | — | — | — | — |
