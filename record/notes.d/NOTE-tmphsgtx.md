---
status: Read
paper: 'LIT-tmpuzf4t'
title: 'Probabilistic Foundations of Contextuality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv 1604.08412v4 (7 Nov 2016, 10 pages, the
    Fortschritte der Physik text with a typo corrected), extracted with
    pdftotext. Sections I–III, the definitions, Theorems II.2–II.4, the
    derivation of Theorem II.3 (Eqs. 31–35) and the reference list were
    read. The two Kochen–Specker incidence matrices of Fig. 1 came through
    as scattered stars and were not checked. The summation signs and
    absolute-value bars of Eqs. 37 and 42 were damaged in extraction and
    were restored from the cyclic criterion (LIT-777 Theorem 5.1). The
    typeset journal version was not compared.
date: '2026-10-09'
summary: >-
  In Kolmogorovian probability, joint distributedness is transitive, so
  treating a measurement as the same random variable in overlapping
  contexts already forces an overall joint distribution. A Kochen–Specker
  or Bell contradiction therefore refutes that identification, not the
  joint distribution. Contextuality is restated as the impossibility of
  a coupling of context-indexed variables whose same-content copies
  satisfy a property C. For inconsistently connected binary systems, C is
  multimaximality, characterized by adjacent pairs (Theorem II.3).
---

<!-- inactive-ok-file: THEORY-013 — Proposed; cited for what this reading adds to it -->

# NOTE-tmphsgtx: Probabilistic Foundations of Contextuality

## Contribution

The paper gives the probabilistic argument for indexing measurements by
context. It is a diagnosis of the traditional reading, not a new
theorem. It then states the CbD definition of contextuality for arbitrary
binary systems, using multimaximal couplings, and supplies the
adjacent-pairs characterization of those couplings (Theorem II.3) that
the CbD 2.0 paper ([LIT-tmpsa1qj](../literature.d/LIT-tmpsa1qj.md)) cites as its Theorem 2.

## Key insight

Within classical probability you cannot conclude "there is no joint
distribution" from a contextuality contradiction, because sharing even
one variable already puts two contexts on the same probability space.
Joint distributedness then propagates along any chain of overlapping
contexts. So what the contradiction refutes is the assumption that makes
the contexts overlap: that a measurement of q is one random variable
whatever else is measured with it. Drop that, and contextuality becomes a
question about which couplings of the now-disjoint contexts are possible.

## Assumptions

- Kolmogorovian probability with multiple domain probability spaces. A
  random variable is a triple of domain probability space, codomain and
  measurable function. Two random variables are jointly distributed if
  and only if their domain spaces coincide (Eq. 7).
- Finitely many contents and contexts. All examples and the Section II
  theory use binary measurements.
- Which conditions count as a context is part of the system's
  specification. The KS-3D example's contexts include an outcome
  condition, not just the co-measured observables.

## Key results

- **Transitivity** (Section I.3). If X, X′ are jointly distributed and so
  are X′, X″, then X, X″ are, since all three share X′'s domain space.
  An equivalent form: jointly distributed variables are functions of one
  random variable, and that representation also propagates. Hence if the
  graph of contexts linked by shared variables has a path through all
  contexts, the traditional system has an overall joint distribution.
  The paper exhibits Hamiltonian paths for KCBS, KS-4D and KS-3D.
- **Reductio** (Section I.4). The contradiction refutes Noncontextual
  Identification, not the existence of a joint distribution.
- **Definition I.1.** A system is traditionally noncontextual if it has a
  coupling in which same-content variables are equal with probability 1
  (equivalently, adjacent pairs in any ordering, Eq. 22).
- **Definition II.1.** A binary system is noncontextual if it has a
  coupling in which every set of same-content variables is equal with
  maximal possible probability. The remark credits this to the CbD 2.0
  paper and says CbD 1.0 applied the constraint only to the whole
  connection.
- **Theorem II.2** (cited to [LIT-tmpsa1qj](../literature.d/LIT-tmpsa1qj.md)). A binary connection's
  multimaximal coupling exists, is unique and has the staircase form of
  Eq. (30).
- **Theorem II.3.** A coupling of a binary connection sorted by
  p_i = Pr[R_q^i = 1] is multimaximal if and only if each adjacent pair is
  maximally coupled. Derived in Eqs. (31)–(34): adjacent maximality forces
  Pr[S^l = 1, S^{l+1} = −1] = 0, which propagates to the staircase.
- **Section II.4.** Three consequences, said to follow "trivially": (1)
  deleting measurements preserves noncontextuality; (2) consistently
  connected systems get Definition I.1; (3) for cyclic systems the theory
  is the earlier one.
- **Theorem II.4** (cited to Kujala & Dzhafarov 2016). A rank-n binary
  cyclic system is noncontextual if and only if s_odd of the n
  within-context product expectations ≤ n − 2 + Σ_i |⟨R_i^i⟩ −
  ⟨R_i^{i⊖1}⟩|.
- **Magic boxes** (Section III). Specker's three boxes, with one gem in
  each opened pair, form a rank-3 cyclic system. With consistent
  connectedness the system is contextual. Without it, the system is
  noncontextual if and only if the three marginal differences sum in
  absolute value to at least 2 (Eq. 42). In particular, any deterministic
  version is noncontextual.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | If a measurement is one random variable in all its contexts, overlapping contexts force an overall joint distribution | strong (elementary proof) | Section I.3, Eqs. 7–12 |
| C2 | Contextuality contradictions refute context-independent identification of measurements, not joint distributions | moderate (a philosophical argument resting on C1) | Section I.4 |
| C3 | A coupling of a binary connection is multimaximal if and only if its adjacent pairs, in the order of means, are maximally coupled | strong (derivation) | Theorem II.3, Eqs. 31–34 |
| C4 | Multimaximal noncontextuality is hereditary, reduces to the traditional notion under consistent connectedness, and leaves cyclic systems unchanged | strong (immediate) | Section II.4 |
| C5 | Specker's magic boxes are noncontextual exactly when the marginal discrepancies sum to at least 2 | strong (Theorem II.4 at n = 3) | Eq. 42 |
| C6 | Inconsistent connectedness is essentially universal outside physics, and non-negligible in a KCBS experiment | weak here (cited) | Section II.1, refs 20, 21, 32, 35, 36 |

## Concepts

- **Noncontextual Identification.** The assumption that the random
  variable representing a measurement is identified by the property it
  measures alone.
- **Contextual Identification; Stochastic (Un)Relatedness.** CbD's
  replacements. A variable is identified by content and context, and it
  is jointly distributed only with variables in its own context.
- **S1 / S2.** The traditional determination (existence of a joint
  distribution of all measurements) and CbD's (existence of a coupling
  whose same-content parts satisfy C).
- **consistently / inconsistently connected.** Whether same-content
  variables are identically distributed across contexts.
- **multimaximal coupling.** As in [LIT-tmpsa1qj](../literature.d/LIT-tmpsa1qj.md).

## Connections

The paper is the conceptual companion of [LIT-tmpsa1qj](../literature.d/LIT-tmpsa1qj.md). Each cites the
other for half of the binary multimaximality theory. It builds on [LIT-777](../literature.d/LIT-777.md)'s
system notation and on the earlier "Contextuality is about identity of
random variables" (2014). The transitivity point is aimed at the
Khrennikov line, which locates contextuality in variables defined on
different probability spaces. Fine and Suppes–Zanotti are cited for the
joint-distribution criterion.

## Bearing on the record

- **[LIT-016](../literature.d/LIT-016.md) and [THEORY-012](../theory.d/THEORY-012.md).** The sheaf account keeps one variable per
  measurement and asks whether overlapping marginals glue. On that
  account, the traditional "no joint distribution" is a statement about
  a global section of a presheaf over a cover, not about random variables
  on one space. This paper's transitivity argument targets the
  random-variable reading and does not engage the sheaf formulation. The
  two accounts agree under consistent connectedness ([NOTE-600](NOTE-600.md)). This
  paper does not compare them.
- **[THEORY-013](../theory.d/THEORY-013.md).** C6 restates the premise [THEORY-013](../theory.d/THEORY-013.md)'s programme rests
  on. Nothing here changes that theory.
- **[CLAIM-tmpje74v](../claims.d/CLAIM-tmpje74v.md)** (the manuscript's). This paper is the second of the
  two references the claim gives for the multimaximal version. It
  supports the claim as [LIT-tmpsa1qj](../literature.d/LIT-tmpsa1qj.md) does.
- No new THEORY. No instruction for machine-learning practice.

## Limitations

- C2 is an argument about how to read a reductio. A reader who treats
  quantum contextuality as a property of the measurement structure (the
  sheaf view) is not bound by it.
- Section II.4's three properties are asserted as trivial, without
  proofs. The first needs the subset clause of Definition II.1, which
  holds.
- The Kochen–Specker matrices are not analysed under CbD; the paper says
  only that they are not cyclic.
- Theorem II.2's citation goes to the companion paper, which in turn cites
  this one for the adjacent-pairs theorem.

## Open questions

- A CbD analysis of the KS-4D and KS-3D systems with realistic
  inconsistent connectedness, which the paper sets up and does not do.
