---
number: 595
status: Read
formerly:
- NOTE-tmpou4pq
paper: 'LIT-781'
title: 'Equivalent Comparisons of Experiments'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the Project Euclid scan (Ann. Math. Statist.
    24(2):265–272, 8 pages, page images without a text layer, read as
    images). Sections 1–5 read, every theorem statement and every proof
    followed; the martingale construction of Section 4 (parts A–C) and the
    saddle-point proof of Theorem 6 followed step by step, not re-derived.
    The reference list read. Theorem 1 is quoted from Bohnenblust, Shapley
    and Sherman with its proof deferred to Blackwell (1951), and Theorem 2
    is quoted from Blackwell (1951); neither is proved here, and that paper
    was not read.
date: '2026-10-09'
summary: >-
  Gives a new minimax proof of the Sherman–Stein theorem (for finite
  outcome spaces, an experiment at least as informative as another in every
  decision problem can reproduce it by a Markov matrix) and, by a martingale
  argument, removes the finiteness restriction, so for a finite parameter
  set "more informative" and "sufficient for" coincide in general. Adds
  k-decision problems, with three equivalent forms, and shows that for
  dichotomies two-action problems, and so the type I/type II error
  trade-off, already decide the order.
---

# NOTE-595: Equivalent Comparisons of Experiments

## Contribution

Before this paper there were two ways of comparing experiments with the
same n states: Bohnenblust, Shapley and Sherman's "more informative"
(α ⊃ β: every loss vector attainable with β is attainable with α, in every
decision problem) and Blackwell's 1951 "sufficient for" (α ≻ β: β can be
reproduced from α's outcome by a stochastic transformation). Blackwell
(1951) had shown ≻ implies ⊃, and Sherman and Stein had shown the converse
for experiments with finitely many outcomes. This paper gives a new,
short proof of that converse and extends it to experiments with arbitrary
outcome spaces, so the two orders are the same order. It then introduces a
graded family of weaker comparisons, ≻_k, by k-decision problems, and shows
that for n = 2 the comparison by two-action problems already decides ≻.

## Key insight

Being better for every decision problem and being able to simulate the
other experiment are the same thing. If α does at least as well as β in
every problem, there is a randomisation that turns α's observation into
one distributed exactly as β's under every state. In finite form this is a
minimax statement: the defect "Q − PM" of the best Markov matrix M cannot
be made to cost anything against any decision matrix D, so it is zero.

## Assumptions

- **Finite parameter set.** An experiment is an ordered n-tuple
  α = (m_1, …, m_n) of probability measures on a common Borel field of a
  space X. Everything in the paper is for fixed finite n.
- **Decision problems** are given by a closed, bounded, convex set A ⊂ ℝⁿ
  of loss vectors (randomised procedures make A convex). Losses are
  therefore bounded.
- **Standard measure.** m_α is the distribution of p(x) = (p_1(x), …,
  p_n(x)), p_i the density of m_i with respect to Σ m_i, when x has
  distribution Σ m_i / n. It lives on the simplex P and has centre of
  gravity (1/n, …, 1/n).
- **Theorem 8** is stated for probability measures on a bounded subset of
  n-space; standard measures live on the simplex, so this covers every
  experiment with n states.

## Key results

- **Theorem 1** (Bohnenblust, Shapley and Sherman; proof in Blackwell
  1951). Every probability measure on P with centre (1/n, …, 1/n) is a
  standard measure; α and β have the same standard measure iff
  B(α, A) = B(β, A) for all A; and α ⊃ β iff ∫ φ dm_α ≥ ∫ φ dm_β for every
  continuous convex φ on P.
- **Theorem 2** (Blackwell 1951). α ≻ β iff there is a mean-preserving
  stochastic transformation T with T m_β = m_α.
- **Theorem 3.** α ≻ β implies α ⊃ β (Jensen's inequality through
  Theorems 1 and 2, shown in two lines).
- **Theorem 4.** For n × N₁ and n × N₂ Markov matrices with P ⊃ Q, for
  every N₂ × n matrix D there is a Markov M with Trace(PMD) ≤ Trace(QD); in
  fact PMD and QD have the same diagonal.
- **Theorem 5.** P ≻ Q iff PM = Q for some Markov matrix M.
- **Theorem 6** (Sherman–Stein). P ⊃ Q implies P ≻ Q. Proof: the bilinear
  h(D, M) = Trace((Q − PM)D), over Markov M and D with entries in [0, 1],
  has a saddle point (Bohnenblust, Karlin and Shapley); Theorem 4 makes its
  value ≤ 0, so U = Q − PM₀ has every entry ≤ 0 and entries summing to 0.
- **Theorem 7.** Two probability measures on a finite subset of ℝⁿ with
  ∫ φ dm_1 ≥ ∫ φ dm_2 for every convex φ are related by a mean-preserving
  stochastic transformation T with T m_2 = m_1. The paper credits n = 1 to
  Hardy, Littlewood and Pólya, n = 2 without finiteness to Blackwell, and
  this form to Sherman and Stein.
- **Theorem 8.** On a bounded subset of ℝⁿ, M ⊃ m (convex order) implies
  M ≻ m. With Theorems 1 and 2 this makes ⊃ and ≻ equivalent for all
  experiments with n states. Proof: dyadic-cube approximations m_N, M_N on
  finite sets (part A), compatible finite transformations by compactness
  (part B), a Markov chain x_1, x_2, …, y_2, y_1 built by Kolmogorov's
  extension theorem that is a martingale, and Doob's convergence theorem
  giving x*, y* with E(y* | x*) = x*.
- **Lemma.** If A is the convex hull of a closed bounded C, then B(α, A) is
  the convex hull of B(α, C).
- **Theorem 9.** For experiments with the same n, three conditions are
  equivalent: (1) every n × k Markov matrix (k-outcome experiment)
  reproducible from β is reproducible from α; (2) B(α, A) ⊇ B(β, A) for
  every A that is the convex hull of k points; (3) ∫ φ dm_α ≥ ∫ φ dm_β for
  every φ that is the maximum of k linear functions. This defines α ≻_k β.
  ≻_{k+1} implies ≻_k, and ≻_k for every k implies ≻. A stated corollary:
  if every finite-outcome experiment reproducible from β is reproducible
  from α, then β itself is.
- **Theorem 10.** For n = 2, α ≻_2 β implies α ≻ β (on a segment every
  maximum of finitely many linear functions is a positive combination of
  maxima of two).
- **Corollary and Theorem 11 (dichotomies).** For n = 2, α ≻ β iff, at
  every level t, the least attainable type II error with α is at most that
  with β. Since ≻ passes to n independent repetitions (Blackwell 1951), if
  this holds for one observation it holds for every sample size.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For finite outcome spaces, being at least as informative in every decision problem implies reproducibility by a Markov matrix | strong (proof) | Theorems 4–6 |
| C2 | The equivalence of ⊃ and ≻ holds for experiments with any outcome space, given finitely many states | strong (proof) | Theorem 8 with Theorems 1–2 |
| C3 | Convex order on a finite (indeed bounded) subset of ℝⁿ implies a mean-preserving transformation | strong (proof) | Theorems 7–8 |
| C4 | Comparison by k-decision problems has three equivalent forms, and holding for every k is the same as ≻ | strong (proof) | Theorem 9 and the discussion after it |
| C5 | ≻_{k+1} is strictly stronger than ≻_k in general | not supported here | attributed to an unpublished paper of Stein |
| C6 | For two states, two-action (testing) problems decide the order, and the order is the pointwise comparison of the error trade-off curves | strong (proof) | Theorem 10, Corollary, Theorem 11 |

## Method

Two proof techniques carry the paper. For finite outcome spaces, the
existence of a garbling matrix is a two-person zero-sum game between a
Markov matrix M and a decision matrix D, and the minimax theorem closes it
(Theorem 6). For general spaces, both standard measures are approximated
from finite sets in opposite directions, the finite theorem supplies the
transformations, and a martingale assembled from them converges to a pair
(x*, y*) whose conditional law is the required mean-preserving
transformation (Theorem 8).

## Concepts

- **experiment**: an ordered n-tuple of probability measures on one
  measurable space; the states are the indices.
- **more informative (⊃)**: B(α, A) ⊇ B(β, A) for every closed bounded
  convex A. The paper's term, after Bohnenblust, Shapley and Sherman.
- **sufficient for (≻)**: there is a stochastic transformation T with
  T m_i = M_i for every i. The paper does not use the word "garbling"; β
  is what is later called a garbling of α.
- **stochastic transformation**: a function Q(x, E), measurable in x and a
  probability measure in E; a Markov kernel.
- **mean-preserving**: ∫ y dQ(x, y) = x for all x.
- **standard measure**: the distribution of the normalised likelihood
  vector p(x) on the simplex, under the uniform mixture of the m_i.
- **k-decision problem**: a problem whose A is the convex hull of k points,
  i.e. one with k actions; α ≻_k β is comparison over those.

## Connections

The paper sits on Blackwell's 1951 Berkeley Symposium paper, which
introduced ≻, proved Theorem 2 and ≻ ⇒ ⊃, and on the unpublished work of
Bohnenblust, Shapley and Sherman, which introduced ⊃ and the standard
measure. The finite converse is Sherman's (PNAS 1951, titled after Hardy,
Littlewood, Pólya and Blackwell) and Stein's (Chicago mimeograph, 1951).
Theorem 7 is a multidimensional form of the Hardy–Littlewood–Pólya
majorization theorem. The minimax tool is from Bohnenblust, Karlin and
Shapley (1950); the martingale tool from Doob (1951).

## Bearing on the record

- The record held no account of the comparison of experiments before this
  reading. It produces [THEORY-156](../theory.d/THEORY-156.md), stating the equivalence with its
  scope (finitely many states, bounded losses), sourced here and naming
  the attribution split.
- **On the LIT as first filed.** Its summary credits "this paper" with the
  whole equivalence. Precisely: the direction "garbling ⇒ at least as
  informative" and the sufficiency concept are Blackwell 1951; the finite
  converse is Sherman and Stein's, re-proved here; what is new in 1953 is
  the extension to arbitrary outcome spaces, the k-decision hierarchy and
  the dichotomy results. "The Blackwell theorem" is fairly cited to 1951
  and 1953 jointly; this paper is where the general form is proved.
- **[THEORY-028](../theory.d/THEORY-028.md).** Its passage from I(T; φ) to I(S; W) by data processing
  is an instance of the ordering here: a quantity monotone under every
  garbling. This is my connection, not the paper's, and it does not change
  that THEORY.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Finitely many states throughout. Infinite parameter sets, where Le Cam's
  later theory works, are not touched.
- Losses are bounded (A closed and bounded).
- Strict separation of ≻_{k+1} from ≻_k is asserted from Stein's
  unpublished work, without an example.
- Theorems 1 and 2, on which the general equivalence rests, are quoted,
  not proved.
- The statement that ≻ passes to n-fold repetitions, used for Theorem 11,
  is cited to the 1951 paper.

## Open questions

- An explicit pair of experiments separating ≻_{k+1} from ≻_k for n ≥ 3:
  Stein's example, or another, would close C5.
- Whether the k-decision hierarchy has a quantitative counterpart, a
  deficiency relative to k-action problems; the paper offers only the
  qualitative order. Le Cam's and Torgersen's work ([LIT-778](../literature.d/LIT-778.md)) is where
  that would be found.
