---
number: 600
status: Read
formerly:
- NOTE-tmpybbbx
paper: 'LIT-777'
title: 'Contextuality-by-Default theory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v6 (27 May 2016, 29 pages, comment "to be published in
    Journal of Mathematical Psychology"), the last arXiv version and the
    accepted one; the typeset JMP version was not compared. Text extracted
    with pdftotext. Sections 1–7 read in full, including the footnotes that
    point to the later "multimaximal" version of the theory (footnotes 1, 7
    and 10). The worked examples of Sections 3, 4 and 6 (Figs. 9–14, 19–22)
    were followed from the prose. Their matrices and the quasi-probability
    columns of Figs. 20–21 did not survive text extraction, so individual
    entries are not reported. The cyclic-system criterion (Theorem 5.1) is
    stated here and proved elsewhere (Kujala & Dzhafarov 2016, Found. Phys.
    46:282–299), which this reading did not see. The formula for the
    criterion was recovered from a layout-preserving extraction.
date: '2026-10-09'
summary: >-
  A system is a set of stochastically unrelated bunches (one per context)
  linked by connections (one per content). It is noncontextual if some
  coupling of the bunches makes every connection a maximal coupling, which
  separates context-dependent marginals ("direct influences") from
  contextuality. The test is linear-programming feasibility (Theorem 4.1).
  Signed quasi-couplings always exist (Theorem 6.1), and the minimal total
  variation minus 1 measures the degree of contextuality.
---

<!-- inactive-ok-file: LIT-263 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together -->
<!-- inactive-ok-file: LIT-264 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together -->
<!-- inactive-ok-file: LIT-265 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together -->
<!-- inactive-ok-file: THEORY-013 — Proposed; this reading bears on it without settling its promote_when -->
<!-- inactive-ok-file: THEORY-014 — Proposed; this reading adds a third instance of its pattern -->

# NOTE-600: Contextuality-by-Default theory

## Contribution

A self-contained statement of Contextuality-by-Default (CbD) for finite
systems of categorical random variables. It covers the base-set notion of
which variables exist and which are jointly distributed, systems indexed by
content and context, and contextuality defined through maximal couplings of
connections. Three results go with it: a general linear-programming test, a
statement of the necessary and sufficient criterion for binary cyclic
systems (proved elsewhere), and a new measure of contextuality. The measure
generalizes the de Barros–Oas negative-probability measure from consistently
connected systems to arbitrary ones. The paper's own position is that CbD is
a language for describing data, not a model of anything, and "essentially
coextensive" with Kolmogorovian probability theory.

## Key insight

Give every measurement a separate random variable in every context, so that
no two contexts ever share a variable. Then ask, for each content, how often
its context-specific copies could coincide given only their own
distributions. That is the maximal coupling, and its coincidence
probability is the minimum of their probability masses, summed over values.
Finally, ask whether those coincidence probabilities can be achieved
simultaneously together with the observed joint distributions within
contexts. Differences in the marginals of a content across contexts are
"direct influences", and the theory treats them as no more puzzling than
the dependence of a response on its question. Contextuality is what is left
over: the observed within-context dependencies force the copies apart more
than their marginals require.

## Assumptions

- **Finite categorical variables** throughout. The authors say the content
  generalizes "mutatis mutandis" to arbitrary random entities, and do not
  show it here.
- **Base set** (Section 2.4). A variable exists if and only if it is a
  function of exactly one element of a base set R (P1–P2). Variables that
  are functions of different elements are stochastically unrelated. Joint
  distributions are not imposed, because they track empirical
  co-occurrence.
- **Context–content system** (Definition 2.3). The bunches are the elements
  of R, and the connections partition the union of their components. A
  bunch and a connection share at most one variable (intersection
  property), and the elements of a connection have the same set of
  possible values (comparability property).
- **What counts as content and as context is supplied from outside the
  theory** (Section 1.5, Conclusion (3)). Re-labelling them changes the
  system and can change its contextuality.
- **Maximality** is the constraint imposed on connections. Footnote 10 says
  the authors had already replaced it, in "Contextuality-by-Default 2.0"
  (arXiv 1604.04799, 1604.08412), with multimaximality, in which every
  subset of a connection is maximally coupled. The replacement changes the
  classification only for connections with more than two variables. The
  binary cyclic and consistently connected cases are unchanged, and so are
  the measure theorems.
- **Cyclic systems** (Section 5): each context has exactly two contents
  (CYC1), each content is in exactly two contexts (CYC2), and all variables
  are ±1 (CYC3).

## Key results

- **Theorem 2.2.** Variables X1, …, Xn are jointly distributed if and only
  if they are functions of one random variable. The authors attribute this
  to Suppes & Zanotti (1981) and Fine (1982), and tie it to hidden
  variables.
- **Theorem 3.3 (maximal coupling).** Every connection R_j^1, …, R_j^k has
  a coupling with Pr[T_j^1 = … = T_j^k = v] = min_i Pr[T_j^i = v] for every
  value v. This maximizes Pr[T_j^1 = … = T_j^k] (Thorisson 2000). A
  connection whose elements all have the same distribution has coincidence
  probability 1.
- **Definition 3.4.** A coupling of the bunches is maximally connected if
  its subcouplings for the connections are maximal couplings. The system is
  noncontextual if such a coupling exists, and contextual otherwise.
- **Theorem 4.1.** A system is noncontextual if and only if MQ = P has a
  nonnegative solution Q. Here Q assigns a mass to every "hidden outcome"
  (one value per variable), M is a Boolean incidence matrix, and P stacks
  the bunch probabilities and the connection coincidence probabilities from
  Theorem 3.3. This is linear programming, polynomial in the length of Q
  (Karmarkar).
- **Theorem 5.1 (Kujala & Dzhafarov 2016, not proved here).** A cyclic
  system of rank n is noncontextual if and only if
  s_odd(⟨R_i^i R_{i⊕1}^i⟩ : i = 1…n) ≤ n − 2 + Σ_i |⟨R_i^i⟩ − ⟨R_i^{i⊖1}⟩|.
  Here s_odd is the largest signed sum with an odd number of minus signs.
  The left side takes the bunches' expected products. The right side adds
  the connections' differences of expectations. With consistent
  connectedness this is s_odd(…) ≤ n − 2, the Leggett–Garg (n = 3), CHSH
  (n = 4) and KCBS (n = 5) form.
- **Examples (Section 5.2).** Rank 2 is the question-order paradigm. Moore
  (2002) found that the marginals depend on order. Wang & Busemeyer (2013)
  found that the probability of giving the same answer to both questions
  does not depend on order. To the extent that holds, the left side is 0
  and the system cannot be contextual. Rank 4 with the singlet state at
  angles 0, π/4, π/2, −π/4 gives a left side of 2√2 > 2, so it is
  contextual. The paper also describes a rank 4 psychophysical matching
  design (Dzhafarov, Ru & Kujala 2015) but does not report its outcome
  here.
- **Theorem 6.1.** If the nonnegativity constraint is dropped, an expanded
  system M*Q = P* always has a real solution, because its rows are
  linearly independent. Every solution also solves MQ = P. So a signed,
  maximally connected quasi-coupling exists for every system, consistently
  connected or not. The proof never uses maximality.
- **Measure (Section 6.3).** The set of maximally connected quasi-couplings
  attains its minimal total variation ‖S*‖ = Σ|γ(v)|, by a compactness
  argument. ‖S*‖ = 1 exactly when the system is noncontextual. ‖S*‖ − 1 is
  proposed as the degree of contextuality and is computed by linear
  programming over positive and negative parts. Take the rank-2 system of
  Fig. 14, with identical marginals, perfect agreement in one context and
  perfect disagreement in the other. One solution has total variation 3
  (Fig. 20), and the minimum is 2. Varying p = Pr[S_1^2 = 1, S_2^2 = 1]
  from 0 to ½ gives ‖S*‖ = 2(1 − p), which is noncontextual at p = ½
  (Eq. 72).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A maximal coupling exists for any connection, with coincidence mass min_i Pr[R^i = v] at each value | strong | Theorem 3.3, citing Thorisson's proof |
| C2 | Noncontextuality in CbD is exactly the feasibility of a linear program | strong | Theorem 4.1; the derivation is in the text |
| C3 | A signed maximally connected quasi-coupling exists for every finite categorical system, however inconsistently connected | strong | Theorem 6.1, proved here by linear independence of the rows of M* |
| C4 | The minimal total variation of such quasi-couplings is attained and equals 1 exactly for noncontextual systems, so ‖S*‖ − 1 is a measure of contextuality | strong for existence and the zero point; proposed, not justified axiomatically, as *the* measure | Section 6.3 |
| C5 | The binary cyclic criterion of Theorem 5.1 holds | strong but not supported here | stated with citation; proof in Kujala & Dzhafarov 2016 |
| C6 | Question-order data in which the probability of the same answer does not depend on order cannot be contextual | moderate: it follows from Theorem 5.1 for n = 2, and its empirical premise is Wang & Busemeyer's generalization | Section 5.2 |
| C7 | Direct influences respect causality, while contextuality is not constrained by it | informal argument | Conclusion (1), Leggett–Garg timing example |
| C8 | The linear-programming test and the measure carry over unchanged to any connection constraint C that every connection can satisfy taken separately | moderate: the observation is that the proofs never use maximality | Conclusion (5), and the remark after Theorem 6.1 |

## Method

To decide contextuality: (1) write the context–content matrix; (2) compute
each connection's maximal-coupling coincidence probabilities by Theorem 3.3;
(3) form MQ = P over all hidden outcomes; (4) test for a nonnegative
solution. To measure it: solve min Σ(γ⁺ + γ⁻) subject to (M | −M)(γ⁺; γ⁻)
= P with γ± ≥ 0. The optimum is ‖S*‖. Both programs have one variable per
hidden outcome, k^N of them for N variables with k values. The paper calls
the test polynomial in the length of Q and does not discuss this size,
which is exponential in the number of variables.

## Concepts

- **conteNt / conteXt.** The paper's capitalized spellings. The content is
  what a variable measures or responds to (it labels a connection). The
  context is the conditions under which it is recorded (it labels a bunch).
  Formally they are just labels; "a conteNt is, logically, merely a label
  for a connection."
- **bunch.** The jointly distributed variables of one context. A bunch is
  itself a single random variable.
- **connection.** The variables sharing a content across contexts. They are
  pairwise stochastically unrelated, so a connection is not a random
  variable.
- **stochastically unrelated.** Having no joint distribution, which is
  different from being independent. The joint probabilities are
  undefined, not zero.
- **consistently connected.** Every connection's elements have the same
  distribution. This is the paper's "ordinary" form. The strong form
  (no-signalling, no-disturbance, complete marginal selectivity) requires
  shared sets of contents to have the same joint distribution. CbD recovers
  the strong form by adding contents for those sets (system B″, Fig. 7).
- **direct influences.** Differences between the distributions of the
  elements of a connection.
- **coupling.** A jointly distributed vector with the given marginals. It
  "exists" with respect to its own base set, not the system's, and has no
  empirical meaning.
- **maximally connected coupling.** A coupling of all bunches whose
  restriction to every connection is a maximal coupling.
- **quasi-coupling.** The same object with a signed distribution summing
  to 1.
- **C-contextuality.** Contextuality defined with any constraint C on
  connection couplings in place of maximality (Conclusion (5)).

## Connections

It formalizes the CbD programme of Dzhafarov & Kujala (2014a–c), and
generalizes their Linear Feasibility Test (2012) and de Barros & Oas's
(2014) negative-probability measure. It sets itself against Abramsky &
Brandenburger ([LIT-016](../literature.d/LIT-016.md)) and Abramsky et al. (2015), which deal only with
consistently connected systems and pose contextuality as the compatibility
of overlapping groups of variables. CbD bunches never overlap. CbD poses
contextuality as compatibility between the bunches and the maximal
couplings of the connections (Conclusion (2)). The behavioural
re-analyses in Dzhafarov, Zhang & Kujala ([LIT-264](../literature.d/LIT-264.md)) apply its Theorem 5.1. Kujala
(2016, arXiv 1512.02340) is mentioned as an alternative measure that needs a
modified CbD, and is not discussed.

## Bearing on the record

- **[LIT-016](../literature.d/LIT-016.md) and [THEORY-012](../theory.d/THEORY-012.md)
  (sheaf-theoretic contextuality).** The two accounts agree on
  consistently connected systems, by my inference rather than the paper's.
  When every connection is consistent, a maximal coupling makes its
  elements equal with probability 1. A maximally connected coupling then
  collapses each connection to one variable and becomes one distribution
  over all contents whose marginals are the bunches, which is a global
  section. The CbD system has to carry the strong form (Fig. 7), since
  [LIT-016](../literature.d/LIT-016.md)'s
  no-signalling is the strong form. Where marginals differ, [LIT-016](../literature.d/LIT-016.md)'s framework
  does not apply (no-signalling is part of its definition of an empirical
  model) and CbD does. That confirms the "does not say" line of
  [THEORY-012](../theory.d/THEORY-012.md) that defers that case to CbD. There is also a sharp contrast
  with [LIT-016](../literature.d/LIT-016.md) Thm 5.9 ([NOTE-016](NOTE-016.md)
  C3), where signed global sections exist *if and only if* the model is
  no-signalling. CbD's Theorem 6.1 gives a signed maximally connected
  quasi-coupling for *every* system, signalling or not. These do not
  conflict. CbD's hidden outcomes carry a separate value for each content
  in each context, so the signed object lives on a larger space, and a
  difference in marginals is absorbed by the connection couplings instead
  of making the equations infeasible. So [THEORY-012](../theory.d/THEORY-012.md)'s conclusion, that
  negative probability does not mark contextuality, holds in CbD
  too, and more broadly.
- **[THEORY-014](../theory.d/THEORY-014.md).** CbD is a third instance of its pattern: a linear
  representation that always exists over the reals (Theorem 6.1), with
  classicality as the existence of a nonnegative solution (Theorem 4.1). A
  sentence saying so has been added to [THEORY-014](../theory.d/THEORY-014.md)'s body. As with the other
  two, the shared shape is the record's inference. This paper compares
  itself with the sheaf account only on the overlap of bunches.
- **[LIT-265](../literature.d/LIT-265.md) (contextual fraction).** Both are graded measures computed
  by linear programming, and they are different quantities. The contextual
  fraction is one minus the largest weight of a noncontextual sub-model,
  and it is defined only for no-signalling models. CbD's ‖S*‖ − 1 is the
  excess total variation of the least-negative signed maximally connected
  quasi-coupling, and it is defined for any system. On consistently
  connected systems it reduces, by the paper's account, to de Barros–Oas's
  negativity measure. The paper predates [LIT-265](../literature.d/LIT-265.md) (2017) and makes no
  comparison. The record holds no result saying whether the two order
  systems the same way.
- **[THEORY-013](../theory.d/THEORY-013.md) and [LIT-264](../literature.d/LIT-264.md).** The reading supports
  the theory's description of the CbD criterion, and it gives the
  question-order argument in compact form (C6). It does not meet
  [THEORY-013](../theory.d/THEORY-013.md)'s promote_when, which asks for a close reading of the proof of the
  cyclic criterion. That proof is in Kujala & Dzhafarov 2016, which the
  record does not hold. Note also footnote 10. The definition used in
  [LIT-264](../literature.d/LIT-264.md) and here was already being superseded by multimaximal couplings.
  For the binary cyclic systems [THEORY-013](../theory.d/THEORY-013.md) rests on, the authors say the
  results are unchanged.
- **[LIT-263](../literature.d/LIT-263.md)** (Budroni et al.'s review) is reported in [THEORY-013](../theory.d/THEORY-013.md) to treat
  the same criterion in physics. This paper adds nothing to that.
- **No new THEORY.** The paper's results are definitions, a feasibility
  equivalence and an existence theorem. The one claim about what is true
  that the record lacks is the reduction to global sections under
  consistent connectedness. It is my inference and small enough to stand
  here.

## Limitations

- **Finite categorical variables only.** Generality is asserted, not shown.
- **Theorem 5.1 is cited, not proved.**
- **The definition of contextuality was in flux at publication.** Maximal
  couplings were replaced by multimaximal ones (footnotes 1, 7, 10), which
  changes which systems with more than two variables per connection count
  as contextual.
- **The measure is offered without axioms.** No monotonicity under any
  class of operations is shown. Minimizers are generally not unique, and
  the authors mention a rival measure (Kujala 2016).
- **The LP is polynomial in the number of hidden outcomes,** which grows
  exponentially in the number of variables.
- **Results depend on the choice of contents and contexts,** which the
  theory leaves to the user (Section 1.5). The same experiment admits
  trivially noncontextual representations (systems A′, A″, A‴).

## Open questions

- How does ‖S*‖ − 1 relate to the contextual fraction ([LIT-265](../literature.d/LIT-265.md)) on
  consistently connected models? A proved inequality or a pair of
  models ordered differently would settle it.
- Is the measure monotone under some natural class of free operations on
  systems?
- Which choice of connection constraint C is right? The authors list two
  desiderata (reduce to identity under consistent connectedness, and to
  Theorem 5.1 on binary cyclic systems). Multimaximality is their later
  answer.
