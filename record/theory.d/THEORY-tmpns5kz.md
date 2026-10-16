---
status: Active
title: 'A random linear map into k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n dimensions keeps every pairwise squared distance of a fixed set of n points in ℓ₂ within 1 ± ε, because each difference vector''s squared length concentrates with tails exp(−(k/2)(ε²/2 − ε³/3)) and a union bound over the pairs costs only ln n; the proofs cover a random subspace, Gaussian entries and independent zero-mean ±1 or √3·{+1, 0, −1} entries, and no matrix with nonnegative entries'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-tmpjy3gf
- LIT-tmp7skui
- LIT-tmppzjx6
answers:
- QUESTION-tmpa0dq9
summary: >-
  Dasgupta and Gupta (2003), [LIT-tmpjy3gf](../literature.d/LIT-tmpjy3gf.md), read in [NOTE-tmpve6z2](../notes.d/NOTE-tmpve6z2.md), give the
  explicit bound for a projection onto a random subspace; Johnson and
  Lindenstrauss (1984), [LIT-tmp7skui](../literature.d/LIT-tmp7skui.md), read in [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md), prove the lemma
  with k = [K(τ) log n] and K ≥ (10/τ)² by Lévy's isoperimetric inequality;
  Achlioptas, [LIT-tmppzjx6](../literature.d/LIT-tmppzjx6.md), read in [NOTE-tmp4oub5](../notes.d/NOTE-tmp4oub5.md) from a 2002 draft, carries
  the same k₀ to independent ±1 and sparse three-valued entries. The guarantee
  is for a fixed finite set, on squared distances, and it rests on entries
  being zero-mean. It says nothing about maps that go up in dimension or are
  followed by a threshold.
extended_by:
- THEORY-tmpfo89o
presupposed_by:
- THEORY-tmp4mezl
- THEORY-tmp7nqd6
- THEORY-tmpbseab
- THEORY-tmpi8kfq
---
<!-- inactive-ok-file: LIT-tmpokc0j — Unavailable; the fly paper, named as the case this account does not cover -->

# THEORY-tmpns5kz: A random linear map into k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n dimensions keeps every pairwise squared distance of a fixed set of n points in ℓ₂ within 1 ± ε, because each difference vector's squared length concentrates with tails exp(−(k/2)(ε²/2 − ε³/3)) and a union bound over the pairs costs only ln n; the proofs cover a random subspace, Gaussian entries and independent zero-mean ±1 or √3·{+1, 0, −1} entries, and no matrix with nonnegative entries

## Source

Dasgupta and Gupta (2003), [LIT-tmpjy3gf](../literature.d/LIT-tmpjy3gf.md), read in [NOTE-tmpve6z2](../notes.d/NOTE-tmpve6z2.md) from the
published version. Johnson and Lindenstrauss (1984), [LIT-tmp7skui](../literature.d/LIT-tmp7skui.md), read in
[NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md) from a scan of the published article. Achlioptas,
[LIT-tmppzjx6](../literature.d/LIT-tmppzjx6.md), read in [NOTE-tmp4oub5](../notes.d/NOTE-tmp4oub5.md) from a 2002 journal draft, not the JCSS
text.

## What was actually shown

**The original lemma.** For each 0 < τ < 1 there is K(τ) such that any n
points of ℓ₂ⁿ map into ℓ₂ᵏ, k = [K log n], with ‖f‖_lip‖f⁻¹‖_lip ≤
(1+τ)/(1−τ). The map is a Haar-random rank-k orthogonal projection. The
proof concentrates the projected norm about its median by Lévy's
isoperimetric inequality, with tail 4exp(−nε²/2), and takes a union bound
over the normalized differences: failure ≤ 2n(n+1)exp(−τ²k/18), positive
success once K ≥ (10/τ)². The statement carries no τ⁻²; the proof does.
The lemma was a tool for Theorem 1, Lipschitz extension from n-point sets
into ℓ₂ with constant K√(log n).

**The explicit bound (Dasgupta and Gupta, Theorem 2.1).** For 0 < ε < 1 and
k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n, any n points in ℝᵈ have f into ℝᵏ with
(1 − ε)‖u − v‖² ≤ ‖f(u) − f(v)‖² ≤ (1 + ε)‖u − v‖². f is √(d/k) times a
projection onto a random k-subspace. Lemma 2.2 bounds both tails of the
squared length of a random unit vector's first k coordinates by
exp((k/2)(1 − β + ln β)); at β = 1 ± ε each is at most 1/n². A union bound
over C(n, 2) pairs gives success with probability at least 1/n.

**Other ensembles (Achlioptas, Theorem 1.1).** With
k₀ = (4 + 2β)/(ε²/2 − ε³/3) · log n and E = (1/√k)AR, entries of R either
±1 with probability 1/2 each or √3 × {+1, 0, −1} with probabilities 1/6,
2/3, 1/6, all pairwise squared distances stay within 1 ± ε with
probability at least 1 − n^−β. The proof needs only independent,
zero-mean, unit-variance entries and a per-vector tail of 2/n^{2+β}
(Eq. 3). Lemma 6.1 makes (1, …, 1)/√d the worst vector and Lemma 6.2
bounds its even moments by a Gaussian's. The sparse case of Lemma 6.3 is
omitted in the copy read, and the claim that more than two thirds zeros
breaks it is made without proof.

**What could have come out otherwise.** A fixed n-point set and an
ensemble above for which the stated k fails with more than the stated
probability would refute it. The arguments are short and were checked line
by line in the readings, except Achlioptas's omitted sparse case.

## What this does not say

- **Anything about unsquared distances directly.** Dasgupta–Gupta and
  Achlioptas bound squared distances; the unsquared factor is √(1 ± ε).
- **That this k is necessary.** That is [THEORY-tmpfo89o](THEORY-tmpfo89o.md)'s, and only up to
  a constant and for the worst set.
- **Anything about a set that is not fixed in advance**, such as all
  k-sparse vectors. That needs a net and a further union bound
  ([THEORY-tmp4mezl](THEORY-tmp4mezl.md)).
- **Anything about nonnegative or {0, 1} matrices**, like the fly's
  projection into the mushroom body ([LIT-tmpokc0j](../literature.d/LIT-tmpokc0j.md)). Every ensemble here is
  zero-mean, which the unbiasedness step E‖f(α)‖² = ‖α‖² uses.
- **Anything about maps into more dimensions, or followed by a
  threshold.** For k ≥ d the statement is trivial, and no threshold
  appears.
- **That the guarantee helps a learner.** It keeps a fixed set's geometry.
  Whether a random-features regressor interpolates well is a different
  question ([THEORY-106](THEORY-106.md)).

## Connections

- [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md): the distances thread. The threshold is the log of the family's
  size, here about 2 ln n for n² pairs, over a squared tolerance, which is
  the shape the question proposes.
- [THEORY-388](THEORY-388.md): Indyk and Motwani use a random projection of this kind
  before bucketing ([NOTE-905](../notes.d/NOTE-905.md), Proposition 3), and prove a Gaussian version
  in their Appendix A.
