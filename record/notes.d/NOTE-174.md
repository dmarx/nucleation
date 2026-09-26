---
number: 174
status: Read
formerly:
- NOTE-tmpw3c5d
paper: LIT-177
title: 'Rovelli — The relational interpretation (RQM)'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv:2109.09170v3 (30 Sep 2021), 9 PDF pp.:
    the abstract; unnumbered sections from "Historical roots" to
    "Perspective" (pp. 1–7); references [1]–[76] (pp. 7–9). All read. The
    PDF itself is headed "The Relational Interpretation", and page numbers
    below are the PDF's.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  Rovelli restates RQM as an ontology of sparse relative facts, which
  arise in interactions and are labelled by the interacting systems. Its
  one technical rule is that an amplitude W(b,a) gives the probability P =
  |W|² only when a and b are relative to the same system. That rule
  removes the clash between P_collapse = Σᵢ|W(c,bᵢ)|²|W(bᵢ,a)|² and
  P_unitary = |ΣᵢW(c,bᵢ)W(bᵢ,a)|² (eqs. 2–4). Decoherence makes some facts
  approximately label-independent ("stable"). ψ is a relative-state
  bookkeeping device, like a Hamilton–Jacobi function S. The price, which
  Rovelli states, is giving up "strong realism": values are not held at
  all times, may be held at different times for different systems, and
  there is no coherent global view and no quantum state of the universe.
---
<!-- inactive-ok-file: LIT-133 — Rejected on its 2026-09-26 close reading: cited as a related or contrasting view, not as a result -->

# NOTE-174: Rovelli — The relational interpretation (RQM)

## Contribution

The chapter is an authoritative, compact restatement of RQM as it stood in 2021, gathering 25 years of development (refs. [12]–[18]). It introduces nothing new technically. What it adds is a clean presentation: the measurement problem as a clash of two probability rules, the relative-labelling rule as the fix, decoherence as the source of stable facts, the Hamilton–Jacobi analogy for ψ, and an explicit list of RQM's philosophical costs.

## Key insight

Quantum theory is taken to be about facts, not states. The interference problem goes away once each fact is indexed to the system it is a fact for, and probabilities are computed only between facts indexed to the same system. What Wigner's friend sees is a fact for the friend. For Wigner it is only a correlation, which can still interfere. Macroscopic "outcomes" are the special case where decoherence makes the index practically irrelevant.

## Assumptions

- Facts are sparse: they occur only in interactions between two systems. This is attributed to Heisenberg (p. 2).
- Facts are relative: they are labelled by the interacting systems. Amplitudes W(b,a) have physical meaning only if a and b are relative to the same system. This is postulated as RQM's "core idea" (pp. 2–3).
- Any physical system can be an observer; consciousness plays no role (p. 7).
- ψ has no ontological weight. It is a relative state in Everett's sense (pp. 3–4).
- Information postulates (1996), stated for a compact classical phase space: P1, a finite maximal amount of relevant information can be obtained from a system; P2, new relevant information can always be obtained (p. 5).
- Physical information means correlation, "number of possible distinct alternatives" (p. 5).

## Key results

- **Measurement problem (pp. 2–3).** For a fact a and mutually exclusive facts bᵢ: P_collapse(c|a) = Σᵢ |W(c,bᵢ)|²|W(bᵢ,a)|² (eq. 3), while P_unitary(c|a) = |Σᵢ W(c,bᵢ)W(bᵢ,a)|² (eq. 4). These differ by interference. RQM: eq. (3) "does not hold if the bᵢ have different labels than c".
- **Stable facts (p. 3).** When decoherence makes P_collapse ≈ P_unitary, labels can be ignored. Basing the ontology on stable facts alone (Copenhagen, QBism) builds it on an approximation, and "we are all actually Wigner's friends".
- **ψ as bookkeeping (pp. 3–4).** ψ ~ e^{iS} semiclassically, so "the physical nature of ψ is the same as the physical nature of a Hamilton-Jacobi function". Spin predictions are symmetric in time: the probability cos²(φ/2) holds whichever measurement comes first. So ψ between the two measurements depends on which value is taken as known, and this shows "the state is a coding of our information; not something the particle 'has'" (p. 4, citing [15]).
- **PBR (pp. 4, 6–7).** RQM "circumvents" PBR because it posits no ontic state. PBR's hidden premise is strong realism: all properties are well-defined at all times.
- **Discreteness (p. 4).** V(R) ≥ 2πħ per degree of freedom (eq. 5). So a variable separating points in a finite region R takes at most N ≤ V(R)/2πħ values (eq. 6), and "any variable separating finite regions of phase space is discrete".
- **Postulates and formalism (pp. 5–6).** Non-commutativity (eq. 1) gives the uncertainty relation, hence discreteness, hence P1. The order-dependence of measurements corresponds to P2. Probabilistic dispositions resolve into values "when any two systems interact, provided that we label the resulting facts with the interacting systems".
- **Other considerations (p. 6).** No-go theorems for absolute facts ([57]–[59], experiment [60]). Locality ([64], [65]). Quantum gravity: system ↔ spacetime region, interaction ↔ adjacency, events on 3-d boundaries.
- **Philosophical costs (pp. 6–7).** Strong realism is given up in three respects: values not at all times; no global view; no state of the universe. The chapter also locates RQM relative to QBism, Healey's pragmatism, Zeilinger–Brukner, and Auffèves–Grangier.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Labelling facts by systems removes the collapse/unitary contradiction | moderate | argument from eqs. (2)–(4), pp. 2–3. It removes the contradiction by restricting when eq. (3) applies, and that restriction is postulated |
| C2 | Amplitudes give probabilities only between facts relative to the same system | assertion (postulate) | RQM's "core idea", p. 2 |
| C3 | Decoherence makes a subset of relative facts approximately stable | moderate | cited to Di Biagio & Rovelli [18]; not shown here |
| C4 | ψ is an information-coding device, not a property of the system | weak–moderate | Hamilton–Jacobi analogy and the time-symmetry of spin predictions, p. 4 [15]. The inference from time-symmetric predictions to "not something the particle has" is an informal argument |
| C5 | RQM circumvents PBR | moderate | posits no ontic state; cites Oldofredi & Calosi [27] |
| C6 | Any variable separating finite phase-space regions is discrete, N ≤ V(R)/2πħ | moderate | heuristic from a minimal phase-space cell (eqs. 5–6). Standard semiclassical reasoning, not a theorem |
| C7 | "The entire quantum phenomenology follows from" qp − pq = iħ | assertion | p. 5. Overstated: a representation, a composition rule and the Born rule are also needed |
| C8 | No-go theorems for absolute facts are "direct evidence in favour of RQM" | weak | p. 6. Those theorems rule out observer-independent facts under their assumptions. That is consistent with RQM but does not single it out, since QBism, Everett and others also deny the premise |
| C9 | RQM fits quantum gravity: system ↔ region, interaction ↔ adjacency | assertion | p. 6, refs. [66]–[68] |
| C10 | RQM's cost is giving up strong realism; there is no quantum state of the universe | moderate | follows from the bookkeeping definition of ψ, pp. 6–7 |
| C11 | P1 and P2 seeded the reconstruction programme; Höhn's reconstruction uses them | moderate (historical) | pp. 5, refs. [46]–[55] |

## Method

(Expository chapter: historical framing, then a statement of the interpretation's rules and their consequences.)

## Concepts

- **Fact / event.** The value of a variable (or set of variables) realised in an interaction, relative to the interacting systems (p. 2).
- **Relative fact.** A fact labelled by the systems involved in the interaction that realised it.
- **Stable fact.** A relative fact whose label can be ignored because decoherence suppresses interference (p. 3; [18]).
- **Relative state.** ψ as the state of one system relative to another (Everett). In RQM, every quantum state is of this kind (p. 7).
- **Strong realism.** The view that all physical variables have values at all times, the same for every system, and are jointly available in one global view. RQM rejects it (pp. 6–7).
- **Information.** Correlation: a system has information about another if the number of joint possible states is less than the product of the numbers of possible states of each (p. 5).

## Connections

Dorato ([LIT-176](../literature.d/LIT-176.md)) classes RQM as a ψ-antirealist ontology of events, and Rovelli cites Dorato three times, as refs. [22], [25] and [56]: for monism and becoming, a dispositionalist account of the quantum state, and "information is always information about something". Rovelli's own wording, "when … is a probabilistic disposition resolved into an actual value?" (p. 6), shows how close the two are.

PBR ([LIT-062](../literature.d/LIT-062.md)) is the ψ-ontology theorem RQM says it sidesteps. Hance et al. ([LIT-090](../literature.d/LIT-090.md)) question whether ψ-ontic and ψ-epistemic exhaust the options, which bears on whether RQM's "no ontic state" counts as a third option or falls outside the framework.

Carroll's Hilbert-space fundamentalism ([LIT-123](../literature.d/LIT-123.md)) is the direct opposite. For Carroll the universal state is everything; for Rovelli "there is no meaning in 'the quantum state of the full universe'". Cuffaro & Hartmann's open-systems view ([LIT-037](../literature.d/LIT-037.md)) shares RQM's scepticism about the closed universal system, for different reasons.

Auffèves & Grangier ([LIT-077](../literature.d/LIT-077.md), refs. [34]–[35]) are named as close in spirit. Their reading in the record contrasts their CSM, which derives quantum randomness, with RQM, which postulates it.

Elshatlawy et al. ([LIT-133](../literature.d/LIT-133.md), Rejected) claims to operationalise RQM. Gao ([LIT-121](../literature.d/LIT-121.md), §4.2 fn. 3; ref. [267]) lists Rovelli (1994) among the critics of the protective-measurement argument for ψ-reality. Gao's view, a real ψ with a preferred frame, is the opposite of RQM on both counts.

## Bearing on the record

- It can serve as the record's anchor citation for relational and perspectival quantum ontologies.
- Metaphysics: the chapter defends a relational ontology of sparse relative facts. It presupposes that ontology is fixed by what enters transition amplitudes as independent variables, and denies ontological weight to ψ.
- No ML-practice content. Nothing here bears on the Anthology of the SOTA.

## Limitations

- The core rule (C2) is postulated. The chapter gives no independent motivation beyond its resolving the contradiction.
- Inter-observer consistency, the chief objection in the philosophical literature (Laudisa [63], Brukner-type results), gets one sentence of reply ("no coherent global view"). Later attempts to strengthen RQM on this point are outside this text.
- ψ-realism is argued against mainly in its 1926 "waves in space" form and by analogy (the Hamilton–Jacobi function S). Modern ψ-realist replies (Wallace, Carroll) are not engaged.
- Several headline claims (C7, C8, C9) are stronger than the support given in the chapter.
- The chapter is a handbook overview. The substantive arguments are in the cited papers ([12], [15], [18], [64]).

## Open questions

- Does RQM need an additional postulate to guarantee that what one system records about another agrees with what it learns by later interaction, i.e. that perspectives cohere? This chapter does not say.
- Can "stable facts" be defined without an observer-relative choice of which degrees of freedom count as the environment?
- Is "no quantum state of the universe" compatible with quantum cosmology beyond the "largest-scale degrees of freedom" reading offered on p. 7?

## Corrections to the seeded skim

- Venue: the arXiv comment says "Oxford Handbook of the History of Interpretation of Quantum Physics" (the dossier follows this). The PDF header (p. 1) says "Oxford Handbook of Quantum Interpretations". arXiv also flags text overlap with arXiv:1712.02894 (Rovelli, "'Space is blue and birds fly through it'", ref. [17]). The PDF title is "The Relational Interpretation", not "… of Quantum Physics".
- The dossier's skim stops at "Other considerations (p. 6)" and misses the two sections where the metaphysics is stated: "Philosophical implications" (pp. 6–7) and "Perspective" (p. 7). There Rovelli names RQM's cost as giving up "strong realism" in three respects. First, variables do not take values at all times, and take them at different times for different systems. Second, values held relative to different systems can be compared (so there is no solipsism), but only by a physical interaction limited by ħ, so "there is no coherent global view available". Third, following Dorato's "anti-monistic" reading, "there is no meaning in 'the quantum state of the full universe'". The chapter's philosophical content is in these sections.
- On the dossier's check question: the chapter does not answer the inter-observer consistency objection beyond the comparison-by-interaction point above. It dismisses Laudisa's demand for a "deeper justification" of state reduction as resting on "a very strong realist … philosophical assumption" (p. 7). It treats the Frauchiger–Renner, Brukner and Bong et al. no-go theorems as "direct evidence in favour of RQM" (p. 6), which is more than those theorems show (see Claims C8). It does not engage Wallace- or Carroll-style ψ-realism. Its target is Schrödinger's 1926 "waves in physical space" reading and "Many-Words-like" state realism (pp. 1, 6).
- Eq. (7) prints the uncertainty relation as ∆q∆p ≤ ħ/2. It should be ≥. This is a typo, and nothing downstream uses the sign.
- The claim that "The entire quantum phenomenology follows from this one equation" (qp − pq = iħ, p. 5) is an assertion. The rest of the chapter also relies on a Hilbert-space or C*-representation, a composition rule and the Born rule |W|².
- metaphysics tag: justified. The chapter defends a relational ontology of sparse, relative events or facts: value actualisation is relational "like velocity" (p. 6). It rejects strong realism and quantum-state monism, and denies ontological weight to ψ.
