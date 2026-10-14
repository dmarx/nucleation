---
status: Read
paper: LIT-934
title: 'Aerts — Quantum structure in cognition'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arXiv:0805.3850v2, 12 March 2009,
    58 pp.), text extracted with pdftotext: the introduction, §§1–4
    (there is no concluding section), Tables 1–4 and Appendices A–E (the
    proofs of Theorems 1, 4, 7, 8 and 9). The tables were read as data;
    rows quoted below were checked against them. The Hawaii computation
    (eqs. 27–32) and the claim that the §3.3 conjunction model reads the
    complements through the orthocomplement (eqs. 119–125, with 69–70)
    were checked by hand. Several slips in the text are noted under
    Limitations.
date: '2026-10-14'
summary: >-
  Hampton's membership weights for conjunctions and disjunctions of
  concepts fail a single Kolmogorovian model, item by item, in two ways:
  over- or underextension (∆-type) and a negative Kolmogorovian factor
  (k-type). A subspace lattice with meet and join can fit the k-type
  items, but provably never the ∆-type ones. Those need an emergent
  concept state in a second sector of Fock space. Negation appears only
  as the orthocomplement used to reach conjunction from disjunction, and
  is never measured.
---
<!-- inactive-ok-file: THEORY-tmpajs5h — Proposed; the theory filed from this reading -->
<!-- inactive-ok-file: CLAIM-119 THEORY-013 — Proposed; the claim and account this reading bears on, open -->

# NOTE-tmpsgugb: Aerts — Quantum structure in cognition

## Contribution

The paper turns Hampton's (1988a,b) data on membership weights for pairs
of concepts and their conjunctions and disjunctions into a test of
classical representability. It gives exact conditions for an item's three
weights to come from one Kolmogorovian probability space, and finds two
distinct ways the data fail them. It then builds an explicit vector-space
model in ℝ⁸ that fits every item, with fixed angles per pair of concepts.
It shows, by a short proof, that the dominant failure (overextension of
"and", underextension of "or") cannot come from representing concepts as
subspaces combined by the lattice meet and join.

## Key insight

There are two kinds of non-classicality in these data, and only one of
them is a matter of the lattice. The k-type, where the weights are
monotone but do not add up, can be had by tilting two subspaces so their
lattice is not Boolean. The ∆-type, the guppy effect proper, violates
monotonicity, and no lattice meet or join can violate monotonicity.
Aerts therefore models "A and B" and "A or B" as a superposition of the
logical combination with a new, emergent concept, which lives in a
second sector of the space.

## Assumptions

- **A conjunction query measures the intersection event.** "Classical
  conjunction data" are weights with a Kolmogorovian space and events
  E_A, E_B such that P(E_A) = µ(A), P(E_B) = µ(B) and
  P(E_A ∩ E_B) = µ(A and B) (eq. 3); for disjunction, P(E_A ∪ E_B) =
  µ(A or B) (eq. 8). The non-classicality results hold relative to this
  identification. One space is asked for per item, not per experiment.
- **Membership weights are relative frequencies.** Subjects rated items
  on −3 … +3; the weight is positive ratings over non-zero ratings (§1.1).
- **Measurement is a projector.** In §1.5 a concept is a unit vector
  |A⟩ and the membership test for item X is a projector M, so
  µ(A) = ⟨A|M|A⟩. In §§2–3 the roles swap: the item is a unit vector x
  and each concept a subspace, with µ the squared length of the
  projection ("Quantum Rule", §2.1). The two representations are not
  reconciled in the paper.
- **"A or B" as a one-particle state** is (|A⟩ + |B⟩)/√2 with
  ⟨A|B⟩ = 0, by analogy with the double slit (§§1.5–1.6), and, in Fock
  space, as m e^{iθ}|A⟩⊗|B⟩ + n e^{iφ}(|A⟩ + |B⟩)/√2 with m² + n² = 1
  (eq. 19).
- **Weights 0 or 1** are excluded from the ℂ³ model and "call for a
  specific approach" (§1.5).

## Key results

- **Theorem 1 and 3 (conjunction).** µ(A), µ(B), µ(A and B) are classical
  iff 0 ≤ µ(A and B) ≤ µ(A), µ(B) ≤ 1 and
  k_c = 1 − µ(A) − µ(B) + µ(A and B) ≥ 0 (eqs. 4–7). *Holds when:* one
  Kolmogorovian space per item, with the identification above. Proof by
  an explicit four-point space (Appendix A).
- **Theorems 4 and 6 (disjunction).** Classical iff
  µ(A), µ(B) ≤ µ(A or B) ≤ 1 and k_d = µ(A) + µ(B) − µ(A or B) ≥ 0
  (eqs. 9–12). Appendix B.
- **Theorems 2 and 5.** Overextension, ∆_c = µ(A and B) −
  min(µ(A), µ(B)) > 0, and underextension, ∆_d = max(µ(A), µ(B)) −
  µ(A or B) > 0, are each sufficient for non-classicality. Examples:
  Cuckoo for Bird and Pet, 1, 0.575, 0.842 (§1.1); Ashtray for Home
  Furnishings or Furniture, 0.7, 0.3, 0.25. Almond for Fruits or
  Vegetables, 0.2, 0.1, 0.425, is k-type with k_d = −0.125 (§1.6).
- **Interference model (eqs. 13–17).** µ(A or B) = ½(µ(A) + µ(B)) +
  Re⟨A|M|B⟩, realised in ℂ³ with an explicit phase β. *Holds when:* the
  interference term can reach the data; it is bounded by the smaller of
  √(µ(A)µ(B)) and √((1−µ(A))(1−µ(B))), so items with one weight near 0
  and the other near 1 (Cave, Apple, Gardening) have no such model
  (§1.7, Tables 1–2).
- **Fock-space weights (eqs. 23, 26).**
  µ(A and B) = m²µ(A)µ(B) + n²(½(µ(A)+µ(B)) + Re⟨A|M|B⟩);
  µ(A or B) = m²(µ(A)+µ(B)−µ(A)µ(B)) + n²(½(µ(A)+µ(B)) + Re⟨A|M|B⟩).
  With zero interference these are convex mixtures of the product rule
  and the average, which fit the items the ℂ³ model cannot.
- **Hawaii problem (§1.8).** Tversky and Shafir's 0.54, 0.57 and 0.32 are
  reproduced in ℂ³ with β = 121.8967°: 0.555 + 0.4447 cos β = 0.32.
- **Theorems 7 and 8.** Every classical item is represented in ℝ⁴ with A
  and B coordinate subspaces meeting in one axis (eqs. 35–46).
- **k-type items (§2.2).** Tilting A and B by an angle θ (eqs. 47–48)
  replaces k_c by a "quantum logic factor"
  q_conj(A, B, θ) = 1 − µ(A and B) − (a + b − 2√a√b cos θ)/sin²θ, with
  a = µ(A) − µ(A and B), b = µ(B) − µ(A and B) (eq. 54), and
  q_conj(A, B, π/2) = k_c. An item is representable iff q_conj ≥ 0, which
  holds for cos θ between the roots of eq. 56. Horse Cart and Dishwasher
  (Machine and Vehicle) are fitted together at θ = 80.9026°. The paper
  attributes this kind of non-classicality to "the non Boolean nature of
  the set of closed subspaces".
- **Theorem 9 (§2.3, Appendix E).** If concepts are subspaces of ℝⁿ,
  "A and B" is A ∩ B and "A or B" is A + B, then ∆_c ≤ 0 and ∆_d ≤ 0 for
  every item. The proof is monotonicity of ‖P_S x‖² in S. So ∆-type items
  have no such model.
- **The ℝ⁸ = ℝ⁴ ⊕ ℝ⁴ model (§§2.3–3.3).** A and B get a component in a
  second ℝ⁴ (eqs. 57–58), and the combination adds a fixed 2-dimensional
  "emergent concept" subspace C there (eqs. 61–62), parametrised by θ
  and φ per pair. With 8 coordinates, 4 equations and C fixed per pair,
  each item has one free degree of freedom (§2.3). It is fixed by a
  "modularity condition", µ(A)·µ_c(B) = µ(B)·µ_c(A) (eq. 117), and, for
  classical items, by setting the relative classical disjunction weight
  halfway between the measured and the maximal value (§3.4). Tables 3–4
  give a vector for every item.
- **Conjunction through complements (§3.3).** For "A and B" the paper
  introduces "hypothetical concepts" A′, B′ with µ(A′) = 1 − µ(A),
  µ(B′) = 1 − µ(B), µ(A′ or B′) = 1 − µ(A and B), and uses the
  disjunction model for them (eqs. 119–125). A′ is the orthogonal
  complement of A in ℝ⁸, and the emergent subspace for "A′ or B′" is the
  orthogonal complement of C within the second ℝ⁴. So the conjunction
  model is the De Morgan dual of the disjunction model under the
  orthocomplement.
- **Two layers of thought (§§1.6, 3.4).** The first sector's weights are
  read as "classical logical thought" and the second's as "quantum
  conceptual thought". For Sugar under Spices or Herbs (0, 0, 0.2), the
  relative classical disjunction weight is 0 and the relative quantum
  one is 1.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Weights for a pair and its conjunction (disjunction) have a Kolmogorovian model iff ∆ ≤ 0 and k ≥ 0 | strong | Theorems 1–6, proofs in Appendices A–B |
| C2 | Many of Hampton's items fail it, mostly by over- or underextension, and several disjunction items by k_d < 0 | strong | Tables 1–4, computed from Hampton's published weights |
| C3 | No subspace model with conjunction as meet and disjunction as join can fit ∆-type items | strong | Theorem 9, Appendix E |
| C4 | k-type items can be fitted by tilting subspaces, so their non-classicality is of "quantum logic nature" | moderate | §2.2, worked for Machine and Vehicle only; the general claim is asserted |
| C5 | An ℝ⁸ model with one emergent subspace per pair fits all of Hampton's items | moderate | Tables 3–4; one free parameter per item and two angles per pair, fixed by stipulated conditions |
| C6 | Thought has two superposed layers, classical logical and quantum conceptual | weak | an interpretation of the two sectors, illustrated, not tested |
| C7 | The disjunction effect, conjunction fallacy and sure-thing violations are the same effects as under- and overextension | weak | one ℂ³ fit (Hawaii) and one transposed item (Diving Mask); analogy otherwise |

## Method

Compute ∆ and k for each item from Hampton's weights. Classify items as
classical, ∆-type or k-type. Fit ℂ³ interference models where the
interference term can reach the data, Fock-space convex weights where it
cannot (Tables 1–2). Then build a single real model per pair in ℝ⁸: the
first ℝ⁴ holds the classical part (Theorems 7–8, tilted by θ for k-type
items), the second holds the emergent concept C, obtained by rotating
the canonical basis by 90° in the (e₆, e₈) plane and by φ in the plane of
e₅ and the bisector of e₆, e₇ (eqs. 79–86). Solve eqs. 108–111 by a
graphical search followed by iteration to 10⁻¹⁵ (Figure 1).

## Concepts

- **Membership weight µ(A).** The proportion of positive among non-zero
  ratings of an item for concept A.
- **∆-type non-classical item.** Overextended for a conjunction or
  underextended for a disjunction: monotonicity fails.
- **k-type non-classical item.** Monotone, but k_c < 0 (conjunction) or
  k_d < 0 (disjunction): the weights cannot be partitioned into four
  non-negative cells.
- **Emergent concept.** The 2-dimensional subspace C of the second ℝ⁴,
  representing "A or B" (or "A and B") as a new concept, not as a
  logical combination.
- **One-particle and two-particle ways.** Judging membership in "A or B"
  as one new concept, or as two parallel judgements combined by truth
  table. They are the two sectors of Fock space.
- **Modularity condition.** Eq. 117: classical weights proportional to
  measured weights. It has nothing to do with the modular law of
  lattices.

## Connections

The paper continues Gabora and Aerts (2002) and Aerts and Gabora
(2005a,b, held here as [LIT-340](../literature.d/LIT-340.md) and [LIT-312](../literature.d/LIT-312.md), [NOTE-294](NOTE-294.md) and [NOTE-299](NOTE-299.md)), and
Aerts (2007a,b), which it summarises. Its data are Hampton (1988a,b), and
its classical criterion is related to Pitowsky's correlation polytopes
through Aerts, Aerts and Gabora (2009). It cites Busemeyer, Matthew and
Wang (2006), Franco (2007) and Khrennikov (2008) for quantum models of
the disjunction effect, and Widdows and Peters (2003) and van Rijsbergen
(2004, [LIT-262](../literature.d/LIT-262.md)) for orthogonal negation in retrieval. None of these
lineages is declared on the LIT.

## Bearing on the record

- **[QUESTION-055](../questions.d/QUESTION-055.md) (the negation of a category).** The paper does not
  answer it and does not ask it.
  - Negation of a concept appears in only two places. One is the "no"
    outcome of a membership test, 1 − M. The other is the device of
    §3.3, where hypothetical complements A′, B′ with weights 1 − µ let
    the conjunction model be read off the disjunction model through the
    orthocomplement. No negated concept is measured.
  - In §1.5 a concept is a state vector, which has no complement at all.
  - The subspace lattice it does use (§2) is orthocomplemented and,
    being finite-dimensional, modular. But Theorem 9 shows that this
    lattice's meet and join cannot represent the main data. What carries
    the guppy effect is the emergent subspace, which is not a lattice
    operation on A and B.
  - The record's inference: Theorem 9 needs only that membership is
    order-preserving and that "and" is a meet. So the same holds for a
    Boolean, orthomodular or Heyting lattice. If communicative
    categories show guppy-type effects, the choice among the three
    negations of [QUESTION-055](../questions.d/QUESTION-055.md) cannot by itself account for them. This is
    filed as [THEORY-tmpajs5h](../theory.d/THEORY-tmpajs5h.md).
- **[LIT-934](../literature.d/LIT-934.md)'s own body and status note** say the paper models the data
  "with quantum, orthocomplemented structure", one of the "candidate
  negations". That holds only weakly. The orthocomplement appears in
  §3.3 as a calculational device, and the lattice whose negation it is
  fails for the ∆-type data.
- **[NOTE-294](NOTE-294.md)'s open question** names "Aerts 2009" as where tests of a
  non-distributive concept lattice are "said to appear". In part they
  do. §2.2 uses non-commuting subspaces (θ ≠ 90°), whose lattice is not
  distributive, and needs them for the k-type items. But no identity such
  as e ∧ (f ∨ g) = (e ∧ f) ∨ (e ∧ g) is tested directly, and the main
  effect is placed outside the lattice.
- **[THEORY-041](../theory.d/THEORY-041.md).** Aerts's "modularity condition" (eq. 117) is a
  proportionality constraint on weights, not Birkhoff and von Neumann's
  modular law. A citation that runs the two together would be wrong.
- **[CLAIM-041](../claims.d/CLAIM-041.md) and [THEORY-013](../theory.d/THEORY-013.md).** Non-classicality here means "no single
  Kolmogorovian space in which 'A and B' is the intersection event". That
  is not contextuality in the Contextuality-by-Default sense of [LIT-264](../literature.d/LIT-264.md),
  and the paper does not claim it is. It is consistent with [CLAIM-041](../claims.d/CLAIM-041.md):
  the paper's evidence for quantum structure is that a quantum model
  fits where a classical one, so defined, cannot.
- **[CLAIM-119](../claims.d/CLAIM-119.md).** If communicative categories behave like Hampton's
  concepts, a concept lattice with meet as conjunction cannot model
  their overextended blends. That is a constraint on [CLAIM-119](../claims.d/CLAIM-119.md)'s lattice
  that the record had not stated.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **Fit, not test.** Each item has one free parameter after the per-pair
  angles are chosen, and the extra conditions that fix it are stipulated
  (eq. 117, and the halfway rule for classical items). The angles were
  found by search, and for two pairs only "a very narrow window" worked
  (§3.2). No held-out prediction is made.
- **Classical items are recast as non-classical** "in reality" (§3.4).
  That is a modelling choice, made because the data allowed a purely
  classical fit.
- **The two-layer hypothesis and the decision-theory transfer are not
  tested**; the paper says further experiments are needed (§1.8).
- **Feature-linked quantities are not modelled**, which the paper itself
  names as a limitation (Introduction).
- **Slips in the text.** After Theorem 4 the text writes
  "µ(A and B) ≤ min" where the disjunction condition is meant. Discus
  Throwing's weights are attributed to Hampton (1988a) though they are
  disjunction data, and its measured µ(A or B) is given as 0.75 and then
  as "the original weight of 0.7" (§3.2). For MSG, µ(B) is written
  "µ(A) = µ_2c(A) = µ_rq(A) = 0.1" (§3.4).

## Open questions

- Does any lattice-theoretic semantics, with conjunction a meet and a
  non-monotone membership function, reproduce overextension? Theorem 9
  rules out monotone ones only.
- What would data on negated concepts ("not a Pet") show? Whether
  µ(not A) = 1 − µ(A) holds, and whether "not A or not B" mirrors
  "A and B", would test the orthocomplement that §3.3 assumes.
