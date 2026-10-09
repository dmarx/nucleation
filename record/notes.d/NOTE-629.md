---
number: 629
status: Read
formerly:
- NOTE-tmpjllrs
paper: 'LIT-813'
title: 'Sheaf-theoretic structure of definite causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the EPTCS 343 PDF (QPL 2021, pp. 301–324, 24 pages
    with the proofs appendix), extracted with pdftotext: Sections 1–9,
    all definitions and propositions, the proofs of Propositions 5, 8, 9,
    15, 16, 21 and 22, and the reference list. The empirical-model tables
    of Sections 8 and 9 lost part of their layout in extraction and were
    followed from the prose. Proposition 5 was checked by hand against a
    two-event example, given below. The arXiv v3 withdrawal notice (3 April
    2024) was read on the abstract page. The successor papers it names
    were not read.
date: '2026-10-09'
summary: >-
  Extends the Abramsky–Brandenburger sheaf framework from non-locality
  (discrete order) to any finite causal order of events. Sections are
  causal functions over families of inputs on lower sets. Empirical models
  are causal conditional distributions forming a polytope. Locality is a
  global section, equivalently a mixture of deterministic causal functions.
  The authors withdrew the paper in 2024 because its "locale of inputs" is
  not fit for purpose. This reading finds that Proposition 5's meet can
  leave the poset and that distributivity fails.
---

<!-- inactive-ok-file: LIT-813 — Rejected: the paper this note reads, withdrawn by its authors -->
<!-- inactive-ok-file: THEORY-014 THEORY-165 — Proposed; cited for what this reading does or does not add to them -->

# NOTE-629: Sheaf-theoretic structure of definite causality

## Contribution

It is the first attempt to put definite causal order into the
sheaf-theoretic framework of [LIT-016](../literature.d/LIT-016.md). In [LIT-016](../literature.d/LIT-016.md) every event is causally
unrelated to every other. Here an output may depend on inputs in its causal
past. Locality becomes the existence of a classical model built from
deterministic *causal* functions, and the no-signalling condition becomes a
family of causality equations, one per lower set. It reduces exactly to
[LIT-016](../literature.d/LIT-016.md)'s construction on the discrete order. It also sketches pre-orders
for indefinite causal order and a causal-fraction analysis of the
Baumeler–Feix–Wolf model.

## Key insight

Replace "measurements that can be performed together" by "inputs at events
closed under the past". On a lower set, a function from joint inputs to
joint outputs that respects the causal order can be restricted to a smaller
lower set, because nothing in the smaller set depends on what was cut away.
So causal functions form a sheaf, and the whole Abramsky–Brandenburger
apparatus (distributions, compatible families, global sections) can be
reused with causality in the sections rather than in a no-signalling
condition.

## Assumptions

- Ω a finite poset; finite, nonempty input and output sets at each event.
- Non-determinism valued in a commutative semiring R: R₊ for probabilities,
  ℝ for signed, 𝔹 for possibilistic.
- An empirical model is a compatible family over the cover induced by all
  joint inputs I_Σ (Definition 11). Every event's input is chosen in every
  run. There is no notion of measuring only some events.

## Key results

- **Definition 3, Proposition 5 (the locale of inputs).** L_Σ is the
  disjoint union over lower sets λ of the products over ω ∈ λ of nonempty
  subsets of I_ω, ordered componentwise. Its meet is given as
  (U_ω ∩ V_ω) on λ_{U∩V} = {ω ∈ λ_U ∩ λ_V : U_ω ∩ V_ω ≠ ∅}. **This fails.**
  Take Ω = {C < A} and I_C = I_A = {0, 1}. Let U = ({0}, {0}) and
  V = ({1}, {0}), both on {C, A}. Then λ_{U∩V} = {A}, which is not a
  lower set, so U ∩ V is not in L_Σ. The true greatest lower bound is the
  bottom ∅. With a = U, b = ({0}) on {C} and c = V: b ∨ c = ({0, 1}, {0}),
  so a ∧ (b ∨ c) = a, while (a ∧ b) ∨ (a ∧ c) = ({0}) on {C} ≠ a.
  Distributivity fails, so L_Σ is not a locale. This is the reader's
  check, and it agrees with the authors' withdrawal of Definition 3.
- **Definition 6.** f on a lower set is causal if f(i)_ω depends only on
  i restricted to ω's down-set.
- **Proposition 8.** Restriction of causal sections is well defined, and
  E_Σ is a sheaf. The gluing argument assumes U ∩ V as in Proposition 5,
  so it inherits that defect.
- **Proposition 9.** For a discrete Ω, L_Σ ≅ P(X) and E_Σ is the original
  sheaf of sections. Here every subset of Ω is a lower set, and the
  defect above cannot arise.
- **Proposition 15.** Empirical models over the joint-input cover are
  exactly causal conditional distributions e(o | i). Causality means that
  the marginal on each lower set λ is independent of inputs outside λ.
- **Proposition 16.** Probabilistic empirical models form a polytope: the
  product of |I_Σ| simplices intersected with the linear causality
  equations (35). Remark 17 notes that they are redundant.
- **Proposition 21.** e is local (has a global section) if and only if
  ê = Σ_ξ p(ξ) δ_{f(ξ)} for causal functions f(ξ) and p ∈ D_R. This is the
  causal analogue of [LIT-016](../literature.d/LIT-016.md)'s Theorem 8.1. The proof here is short
  because local sections are already functions on all joint inputs.
- **Proposition 22.** Diagrams over a framed multigraph in an
  R-probabilistic theory (the authors' earlier formalism) with normalised
  processes yield R-valued empirical models. The proof discards maximal
  events one at a time.
- **Section 9** (stated, proofs deferred). For the Baumeler–Feix–Wolf
  model, the Ω-causal fraction (the largest λ with λ·e ≤ e_BFW for an
  Ω-causal e) is 0 for every partial order on three events and 1 for four
  pre-orders. Fixing the first party's input leaves a no-signalling model
  for the other two.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | On a discrete order the construction is exactly Abramsky–Brandenburger's | strong (proof; unaffected by the defect) | Proposition 9 |
| C2 | Empirical models are exactly causal conditional distributions, and they form a polytope | strong (proof) | Propositions 15–16 |
| C3 | Locality is the same as a mixture of deterministic causal functions | strong (proof, given the sheaf of sections) | Proposition 21 |
| C4 | L_Σ is a locale and E_Σ a sheaf over it | fails as stated | Proposition 5; counterexample above; authors' withdrawal |
| C5 | Physical diagrams respecting the causal order yield empirical models | moderate (proof sketch in another formalism) | Proposition 22 |
| C6 | The BFW model has causal fraction 0 for every definite order and 1 for exactly four pre-orders | not supported here (proof deferred) | Section 9 |

## Concepts

- **definite causal scenario.** (Ω, I, O) with Ω a finite poset.
- **lower set.** A set of events closed under the past. Λ(Ω) is the set
  of all of them.
- **locale of inputs L_Σ.** Families of nonempty input sets indexed by
  lower sets (Definition 3). Defective, as above.
- **causal function.** Its output at ω depends only on inputs at events
  ≤ ω.
- **local / non-local.** A global section of the presheaf of R-distributions
  exists or does not. Here this means "explained by classical causal
  functions", which generalizes Bell locality.
- **Ω-causal fraction.** The largest weight of an Ω-causal sub-model, by
  analogy with [LIT-265](../literature.d/LIT-265.md)'s non-contextual fraction.

## Connections

It builds on [LIT-016](../literature.d/LIT-016.md) and cites [LIT-277](../literature.d/LIT-277.md) (cohomology) and [LIT-265](../literature.d/LIT-265.md)
(contextual fraction) in its literature review. It also builds on the
authors' process-theoretic causal frameworks (Pinzani & Gogioso 2020;
Gogioso & Scandolo 2018). It contrasts itself with Mansfield's 2017
presentations, which impose a causal order on the powerset of measurements
and, the authors argue, cannot handle Bell scenarios or classify causal
classical functions as local. Fritz's correlation scenarios and Henson,
Lal and Pusey's generalized Bayesian networks are named as the other
traditions. Contextuality-by-Default (Dzhafarov, Kujala and Cervantes) is
cited once, for the idea that context changes "the very conditions" of
prediction.

## Bearing on the record

- **[LIT-016](../literature.d/LIT-016.md) and [THEORY-012](../theory.d/THEORY-012.md).** Proposition 21 extends [THEORY-012](../theory.d/THEORY-012.md)'s
  criterion: noncontextual (local) exactly when there is a global section,
  equivalently a classical model, with "classical" now meaning causal
  functions on a causal order. Within this paper the extension rests on a
  construction the authors withdrew. On the discrete order it is
  [LIT-016](../literature.d/LIT-016.md)'s result unchanged. No edit to [THEORY-012](../theory.d/THEORY-012.md) follows.
- **[THEORY-014](../theory.d/THEORY-014.md).** The R-valued generality (ℝ for signed distributions) is
  set up but not used. The paper proves no "signed global sections always
  exist" result for causal scenarios, so it adds no instance to
  [THEORY-014](../theory.d/THEORY-014.md).
- **[LIT-265](../literature.d/LIT-265.md) and [THEORY-165](../theory.d/THEORY-165.md).** The Ω-causal fraction of Section 9 is
  the contextual fraction's construction with causality in place of
  locality. Its properties are not proved here.
- **The manuscript.** The reading supplies no premise for the claims
  around `what-survives-translation`. Its relevance would be the idea of
  restricting the admissible covers by an order, and that is the
  withdrawn part.
- No new THEORY. No instruction for machine-learning practice.

## Limitations

- The central construction (Definition 3, Proposition 5) is defective, as
  the authors acknowledge. Propositions 8 and 21 inherit it outside the
  discrete case.
- Empirical models are defined only over the cover of all joint inputs.
  Scenarios in which some events are not run are not represented.
- The indefinite-causality section states results without proof.
- No example is analysed for locality. The quantum diamond model is
  constructed but not tested.

## Open questions

- Whether the successor's "spaces of input histories" (arXiv 2206.08911)
  repair Propositions 5 and 8 while keeping Propositions 15–21. Settling
  that means filing and reading the successor.
- The status of the BFW causal-fraction results, proved only in later
  work.
