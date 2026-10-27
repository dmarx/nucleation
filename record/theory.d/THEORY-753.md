---
number: 753
status: Active
formerly:
- THEORY-tmpeu1u4
title: 'For finite X and Y, the information bottleneck is successively refinable from budget λ₁ to λ₂ > λ₁ iff some pair of optimal encoders forms a Markov chain X → T₂ → T₁, that is, iff the coarse optimal encoder is a garbling of a fine one; when the fine optimum''s decoder points q(X|t₂) are affinely independent, this holds for that pair iff every decoder point q(X|t₁) of the coarse optimum lies in their convex hull, so a failed hull test on optima that are unique up to merging and relabelling proves that refinement fails'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-981. The equivalences are the paper's Propositions 1, 4 and 8 (Proposition 8 rests on Blackwell's theorem only for its decision-theoretic form, which this entry does not claim). Each step below is re-derived, which meets the condition for Active under ADR-047 v2. The last clause, that a failed hull test on unique optima proves non-refinability, and the convex-envelope certificate of uniqueness are the record's: the paper leaves uniqueness as its Conjecture 1 and treats its failed tests as proxies.
tags:
- information-theory
- mathematics
date: '2026-10-20'
source:
- LIT-1258
answers:
- QUESTION-tmpt5ucu
summary: >-
  Charvin, Catenacci Volpi and Polani (2023), [LIT-1258](../literature.d/LIT-1258.md), read in [NOTE-981](../notes.d/NOTE-981.md). It turns [QUESTION-220](../questions.d/QUESTION-220.md)'s Markov formulation into a finite check: nesting between two IB optima is a convex-hull inclusion of their decoder points, which a linear programme decides. The check is on given optima, and refinability asks for some pair. So a failed check settles the question only when the optima are certified globally optimal and unique. This entry adds that the information bottleneck's own convex-envelope dual can supply that certificate. Finite alphabets, two stages.
supports:
- CLAIM-392
---
# THEORY-753: For finite X and Y, the information bottleneck is successively refinable from budget λ₁ to λ₂ > λ₁ iff some pair of optimal encoders forms a Markov chain X → T₂ → T₁, that is, iff the coarse optimal encoder is a garbling of a fine one; when the fine optimum's decoder points q(X|t₂) are affinely independent, this holds for that pair iff every decoder point q(X|t₁) of the coarse optimum lies in their convex hull, so a failed hull test on optima that are unique up to merging and relabelling proves that refinement fails

## Source

Charvin, Catenacci Volpi and Polani (2023), *Entropy* 25(9):1355,
[LIT-1258](../literature.d/LIT-1258.md), read in full in [NOTE-981](../notes.d/NOTE-981.md). Definition 5, Propositions 1, 4
and 8, Appendices B.1, B.5 and B.6. The certificate in step 5 is the
record's.

## What was actually shown

**Setting.** X and Y finite, p(x) > 0 for every x. A *bottleneck at λ* is an
encoder q(t|x) on a finite T, with T → X → Y, that maximizes I(Y; T)
subject to I(X; T) ≤ λ. The problem is *(λ₁, λ₂)-refinable* (Definition 5)
if there are a bottleneck T₁ at λ₁ and a variable S such that (T₁, S), with
(T₁, S) → X → Y, is a bottleneck at λ₂. The *decoder points* of T are the
distributions q(X|t), t ∈ T.

**1. Refinable iff some pair of bottlenecks forms X → T₂ → T₁
(Proposition 1, re-derived).**
- *If refinable.* Put T₂ = (T₁, S). T₁ is a function of T₂, so
  I(X; T₁ | T₂) = 0, which is the chain.
- *Conversely.* Let T₁, T₂ be bottlenecks at λ₁, λ₂ with an extension
  q(x, t₁, t₂) under which X → T₂ → T₁. Set q(y | x, t₁, t₂) = p(y|x), so
  that Y → X → (T₁, T₂). Then I(X; T₁, T₂) = I(X; T₂) + I(X; T₁ | T₂) =
  I(X; T₂) ≤ λ₂, so (T₁, T₂) is feasible at λ₂. Also
  I(Y; T₁, T₂) ≥ I(Y; T₂), which is the optimum at λ₂, so (T₁, T₂) is a
  bottleneck at λ₂. With S = T₂, the definition is met.

**2. The chain is a garbling of encoders (Proposition 8 (iii), re-derived).**
Under X → T₂ → T₁, q(t₁|x) = Σ_{t₂} q(t₁|t₂) q(t₂|x), so
q(T₁|X) = η ∘ q(T₂|X) with η = q(T₁|T₂). Conversely, given a channel η with
q(T₁|X) = η ∘ q(T₂|X), the law p(x) q(t₂|x) η(t₁|t₂) has the right two
marginals and the chain. So "the coarse optimum is a noisy function of the
fine one" is exact, in the sense of encoders.

**3. The chain gives the hull inclusion (Proposition 4, direct part,
re-derived).** Under X → T₂ → T₁, also T₁ → T₂ → X, so
q(x|t₁) = Σ_{t₂} q(t₂|t₁) q(x|t₂). Each coarse decoder point is a convex
combination of fine ones. No condition on the decoders is needed.

**4. The hull inclusion gives the chain when the fine decoder points are
affinely independent (Proposition 4, converse, re-derived).** Suppose
q(X|t₁) = Σ_{t₂} α(t₂|t₁) q(X|t₂) with α(·|t₁) a probability vector for each
t₁. Define q̃(t₁, t₂, x) = q(t₁) α(t₂|t₁) q(x|t₂). Then:
- the (t₁, x) marginal is q(t₁) q(x|t₁), as required, and q̃ has
  T₁ → T₂ → X by construction;
- the (t₂, x) marginal is r(t₂) q(x|t₂), with r(t₂) = Σ_{t₁} q(t₁) α(t₂|t₁).
  Summing over t₂, Σ_{t₂} r(t₂) q(x|t₂) = Σ_{t₁} q(t₁) q(x|t₁) = p(x) =
  Σ_{t₂} q(t₂) q(x|t₂). So Σ_{t₂} (r(t₂) − q(t₂)) q(·|t₂) = 0. The
  coefficients sum to zero, and the q(·|t₂) are affinely independent, so
  r = q(T₂), and q̃ is an extension.

The paper states the condition as injectivity of the matrix q(X|T₂). For
probability vectors, which lie on a hyperplane missing the origin, linear and
affine independence coincide, so the two conditions are the same.
Testing whether a point lies in the convex hull of finitely many points is a
linear feasibility problem. The paper solves it as the first phase of the
simplex method (Appendix B.6), with a threshold of 10⁻⁶ on the objective.

**5. When the test proves non-refinability (the record's).**
- *Merging does not move the points.* Merging symbols with equal decoder
  points leaves the set of points unchanged and gives another bottleneck
  (the paper's Proposition A2). So if, at each budget, all bottlenecks reduce
  to one canonical bottleneck up to relabelling, every bottleneck at λᵢ has
  the same set of decoder points. Then step 3 says: if the hull inclusion
  fails for the canonical pair, no pair has the chain, and by step 1 the
  problem is not (λ₁, λ₂)-refinable.
- *The Lagrangian optimum covers the primal one.* If T minimizes
  I(X; T) − β I(Y; T), it is a bottleneck at λ = I(X; T). Any bottleneck T′
  at that λ has I(Y; T′) = I(Y; T) and I(X; T′) ≤ λ, so it also minimizes
  the Lagrangian. So uniqueness among Lagrangian minimizers gives uniqueness
  among bottlenecks at λ.
- *A certificate of global optimality and uniqueness.* Write
  F_β(r) = H(κr) − H(r)/β on the simplex Δ_X, where κ is the channel p(Y|X).
  Since q(Y|t) = κ q(X|t),
  I(X; T) − β I(Y; T) = H(X) − β H(Y) + β Σ_t q(t) F_β(q(X|t)).
  The feasible (q(t), q(X|t)) are exactly the decompositions
  p(X) = Σ_t q(t) q(X|t). So the minimum is attained exactly by decompositions
  that reach the lower convex envelope of F_β at p(X). Suppose an affine ℓ
  has ℓ ≤ F_β on Δ_X and ℓ = F_β at the decoder points of a candidate. Then
  Σ q(t) F_β(q(X|t)) = ℓ(p(X)), which is a lower bound, so the candidate is
  optimal. Any other optimum also has Σ q′(t) (F_β − ℓ)(q′(X|t)) = 0, so its
  decoder points lie in the touching set {F_β = ℓ}. If that set is a finite,
  affinely independent set of points, the weights of p(X) on it are unique,
  and the canonical optimum is unique.

What could have failed: the converse of step 4 could have needed more than
affine independence, since the hull gives the right (T₁, X) law but not
obviously the right law of T₂. Summing the decomposition of p(X) both ways
shows that affine independence is enough. Step 5 could have failed because a
second optimum with different decoder points might pass the test. The
envelope's touching set rules that out whenever it is affinely independent.

## What this does not say

- **Not that refinement holds or fails for any particular source.** It is a
  criterion. Which sources pass is [THEORY-757](THEORY-757.md)'s subject, and the
  four-state failure is in [NOTE-981](../notes.d/NOTE-981.md).
- **Not that a solver's output settles anything by itself.** The test is on
  given optima. Blahut–Arimoto iterations find stationary points, and can
  stop at non-optimal ones ([THEORY-743](THEORY-743.md), step 3). A failed test on
  uncertified optima is evidence, not proof. The paper says as much
  (Appendix D, Conjecture 1).
- **Not that the decoder points are always affinely independent.** The paper
  observed it in every run, and cites a counterexample when the information
  curve is not strictly concave. Without it, step 4's converse is unproved,
  though step 3 still holds.
- **Not more than two stages.** For n stages the chain must hold jointly.
  Pairwise garblings composed in order give it, but the paper does not state
  this and it is not claimed here.
- **Not continuous variables.** Step 4 uses finite alphabets.
- **Not partition nesting.** The chain is between stochastic encoders. For
  deterministic encoders it reduces to refinement of partitions, which
  [CLAIM-387](../claims.d/CLAIM-387.md) shows can fail.

## Connections

- **[QUESTION-220](../questions.d/QUESTION-220.md): answers in part.** It gives the exact test the
  question asked for ("a certified optimum and a test for a degrading
  channel between optima"). The four-state source of [CLAIM-387](../claims.d/CLAIM-387.md) fails it
  at β = 8 and β = 12, with certified optima ([NOTE-981](../notes.d/NOTE-981.md)).
- **[THEORY-751](THEORY-751.md).** This is the information-bottleneck form of Equitz and
  Cover's condition, single-letter. The paper's Appendix B.2 gives the
  operational coding meaning, from Tian and Chen and from Mahvari, Kobayashi
  and Zaidi, which this entry does not re-derive.
- **[THEORY-743](THEORY-743.md).** Its step 1 shows every optimum is constant on cells of
  the causal partition. So the test can be run on the quotient, as
  [NOTE-981](../notes.d/NOTE-981.md) does.
