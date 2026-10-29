---
number: 156
status: Active
formerly:
- THEORY-tmpl07kz
title: 'For experiments on a finite parameter set whose outcome spaces are standard Borel, being at least as informative for every decision problem is the same as being able to simulate the other by a randomisation'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, from the second pass of the owner's
    promotion audit of 2026-10-19, the finite-outcome case is filed apart
    as THEORY-717, Active. The 1953 paper proves it in full
    (Theorems 4–6, followed step by step in NOTE-595), and the
    promote_when, which concerns the quoted 1951 results and the
    arbitrary-outcome case, does not bear on it. This THEORY extends it
    and keeps the general case. The promote_when and the claim are
    unchanged; the status stays Proposed.
- version: 3
  date: '2026-10-29'
  note: >-
    Promoted and narrowed by the twelfth status review (ADR-057; ADR-047's
    ruling that a checked re-derivation meets a request for a proof). The
    promote_when asked that "A second, independent proof of the general
    (arbitrary outcome space) case is read and checked, such as the
    treatment in Torgersen's book or Le Cam's deficiency theory specialised
    to deficiency zero, or the 1953 proof is checked together with the
    1951 proofs of the two results it quotes." The note of this date gives
    one, checked numerically by the reviewing session. Its last step needs
    a regular conditional distribution, so the title is narrowed to
    standard Borel outcome spaces. The old title: 'For experiments on a
    finite parameter set, being at least as informative for every decision
    problem is the same as being able to simulate the other by a
    randomisation'. Arbitrary spaces go to QUESTION-tmpeep5e.
tags:
- mathematical-statistics
- information-theory
- mathematics
date: '2026-10-09'
source:
- LIT-781
summary: >-
  Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorem 8 with Theorems 1–3: for
  experiments with finitely many states and decision problems with bounded
  losses, α attains every loss vector β attains, in every problem, exactly
  when a Markov kernel turns α's observation into β's under every state.
  The direction from simulation to informativeness is Blackwell (1951); the
  finite converse is Sherman and Stein (1951); the general converse is
  proved in 1953. It is a qualitative order and says nothing about how much
  worse an incomparable experiment is. The record re-derived the converse
  for standard Borel outcome spaces (note of 2026-10-29); arbitrary spaces,
  which the paper claims through a quoted 1951 result, are QUESTION-tmpeep5e.
extends:
- THEORY-717
supports:
- CLAIM-259
- CLAIM-326
bears_on:
- QUESTION-tmpeep5e
---

# THEORY-156: For experiments on a finite parameter set whose outcome spaces are standard Borel, being at least as informative for every decision problem is the same as being able to simulate the other by a randomisation

## Note of 2026-10-27: the easy direction split off

The status review of this date ([ADR-057](../decisions.d/ADR-057.md)) split the definitions and the
easy direction into [THEORY-1096](THEORY-1096.md), Active, with its proof. Ten of
this account's twelve dependents used nothing more and moved there.
[CLAIM-259](../claims.d/CLAIM-259.md) and [CLAIM-326](../claims.d/CLAIM-326.md) use the converse and stay grounded here. The
blocker is unchanged: a second proof of the general converse.

## Source

Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorems 1–8, as read in [NOTE-595](../notes.d/NOTE-595.md).

## What was actually shown

An experiment is an n-tuple of probability measures on a common space, one
per state. α is "more informative" than β (α ⊃ β) if, for every closed
bounded convex set A of loss vectors, every risk vector attainable with β
is attainable with α. α is "sufficient for" β (α ≻ β) if there is a
stochastic transformation T with T m_i = M_i for every state i: β is a
garbling of α.

≻ implies ⊃ by Jensen's inequality (Theorem 3, from Blackwell 1951). For
finite outcome spaces the converse is a minimax argument: the defect
Q − PM of the best Markov matrix M costs nothing against any decision
matrix, so it vanishes (Theorem 6, Sherman–Stein, new proof). For arbitrary
outcome spaces, both orders reduce to a comparison of standard measures on
the simplex (Theorems 1 and 2, quoted), where ⊃ is the convex order and ≻
is a mean-preserving transformation; Theorem 8 proves convex order implies
such a transformation on any bounded subset of ℝⁿ by finite approximation
and martingale convergence. The support is proof, not experiment: what
could show it wrong is an error in a step, so the promotion condition asks
for a checked second proof, and for the two quoted results to be checked
at their source.

For two states the order is decided by testing problems alone: α ≻ β iff
α's least type II error at every level t is at most β's (Theorem 10 and its
Corollary).

## What this does not say

- **Not a measure.** Most pairs of experiments are incomparable; the
  theorem says nothing about how much information is lost when neither
  simulates the other. That quantitative question is Le Cam's deficiency
  ([LIT-778](../literature.d/LIT-778.md), not read).
- **Not for infinitely many states**, and not for unbounded losses, as
  proved here.
- **Not, as re-derived here, for outcome spaces that are not standard
  Borel.** The 1953 paper claims them through Theorem 2, quoted from
  Blackwell (1951), which the record has not read (QUESTION-tmpeep5e).
- **Not "finitely many decision problems suffice".** The k-action
  comparisons ≻_k are weaker than ≻ in general (asserted from Stein's
  unpublished work); only for two states does k = 2 suffice.
- **Not that the simulating kernel is constructive or unique**; Theorem 8's
  kernel comes from a compactness and limit argument.
- **Not a statement about any particular informativeness functional.**
  That a quantity such as mutual information or an f-divergence is
  monotone under garbling is a consequence one may draw, but the paper
  states only the convex-function criterion of Theorem 1.

## Note of 2026-10-19: the finite case filed apart

The finite-outcome case is [THEORY-717](THEORY-717.md), Active. The paper proves it
without the quoted results: Theorems 4–6 for the converse, and a one-line
matrix argument for the direct implication. Claims that cite this THEORY
for experiments with finitely many outcomes can cite that one instead.
This one is Proposed only for the arbitrary-outcome extension.

The citing claims were checked the same day. [CLAIM-323](../claims.d/CLAIM-323.md), whose case is
finite, now rests on that THEORY alone. [CLAIM-237](../claims.d/CLAIM-237.md) and [CLAIM-326](../claims.d/CLAIM-326.md) cite
both, each with a note saying when the finite case suffices. The other ten
use the definition or the order for unrestricted renderings, and they
stay here.

## Note of 2026-10-29: the general converse, re-derived

The twelfth status review re-derived the converse for any α and a β whose
outcome space is standard Borel, without the 1951 results the 1953 paper
quotes. Write μ and ν for the standard measures of α and β, the laws of the
posterior p under the uniform prior, on the simplex Δ.

1. **Bayes risks give the convex order on max-affine functions.** For a
   finite problem with losses L(a, i) and the uniform prior, the Bayes risk
   is ∫ min_a ⟨L_a, p⟩ dμ(p). If α does at least as well as β in every such
   problem, then ∫ φ dμ ≥ ∫ φ dν for every φ = max_j (⟨c_j, p⟩ + d_j).
2. **A martingale coupling exists** (the content of Theorem 8). Discretize ν
   by conditional expectation on a finite partition of Δ into cells of
   diameter at most 1/k: ν_k = Σ_j w_j δ_{y_j}, with ν_k ≤cx ν by Jensen's
   inequality and ν_k → ν. Then μ splits as Σ_j w_j μ_j with the barycentre
   of μ_j equal to y_j. The splittings, densities f_j ≥ 0 summing to 1 in
   L∞(μ), form a weak* compact convex set; their image under
   f ↦ (∫ f_j dμ, ∫ p f_j dμ)_j is compact and convex in finite dimensions;
   and a functional (c_j, d_j) separating the target from it would give
   Σ_j w_j (⟨c_j, y_j⟩ + d_j) > ∫ max_j (⟨c_j, p⟩ + d_j) dμ
   ≥ ∫ max_j (⟨c_j, p⟩ + d_j) dν_k ≥ Σ_j w_j (⟨c_j, y_j⟩ + d_j), a
   contradiction. So there are couplings π_k of ν_k and μ with
   ∫ g(y)(x − y) dπ_k = 0 for every continuous g. On the compact Δ × Δ a
   subsequence converges, the condition passes to the limit, and the limit
   π couples ν and μ with E[X | Y] = Y.
3. **The coupling gives a garbling.** Under state i, α's posterior has law
   n x_i μ(dx), and β's has law n y_i ν(dy). Let K be π's conditional law of
   Y given X, and C(q, ·) the conditional law of β's outcome given its
   posterior q, which exists as a kernel because β's outcome space is
   standard Borel, and is the same under every state because the posterior
   is sufficient. Then T(x, E) = ∫ K(p_α(x), dq) C(q, E) satisfies
   ∫ T(x, E) m_i(dx) = n ∫ q_i C(q, E) ν(dq) = M_i(E), using
   E[X_i | Y = q] = q_i.

Step 3 is where standard Borel is used; arbitrary spaces are
QUESTION-tmpeep5e. The check (numpy, run by the reviewing session, on
three-state Gaussian experiments on a 400-point grid, with β a Gaussian
garbling of α): step 3's identities hold to 3 × 10⁻¹⁵, with T built from the
coupling alone; step 2's splitting residual falls from 8.3 × 10⁻³ at 10³
Frank–Wolfe iterations to 1.1 × 10⁻³ at 6.4 × 10⁴, while a pair not in
convex order stays at 5.5 × 10⁻²; and the discretization error falls from
0.208 at 4 cells to 0.008 at 120. The proof is the evidence; the numbers
check its finite steps.
