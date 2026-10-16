---
status: Active
title: 'For ε between about lg^0.5001 n/√min{n, d} and 1, some n-point set in ℝ^d needs Ω(ε⁻² lg(ε²n)) dimensions under any map, linear or not, that keeps its pairwise squared distances within 1 ± ε, so a random projection with a union bound is optimal up to a constant for the worst set; nearly orthogonal sets can need fewer, and the bound says nothing about typical data'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-tmp8s1wj
extends:
- THEORY-tmpns5kz
answers:
- QUESTION-tmpa0dq9
summary: >-
  Larsen and Nelson (2017), [LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md), read in [NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md) from arXiv
  v2. Theorem 2 removes the lg(1/ε) gap that Welch, Levenshtein and Alon
  left, for arbitrary maps. The proof is an encoding argument over a family
  of k-sparse vectors with k ≈ ε⁻², ending at nm = Ω(kn lg(d/k)). It is a
  worst-case bound by existence with an untracked constant. It is not a
  phase transition, and the paper notes that ε-incoherent sets fit in
  o(ε⁻² lg n) dimensions for small enough ε.
---
<!-- inactive-ok-file: THEORY-tmp644mk — Proposed; the ℓ₁ transition account, named for what it adds beside this one -->

# THEORY-tmpfo89o: For ε between about lg^0.5001 n/√min{n, d} and 1, some n-point set in ℝ^d needs Ω(ε⁻² lg(ε²n)) dimensions under any map, linear or not, that keeps its pairwise squared distances within 1 ± ε, so a random projection with a union bound is optimal up to a constant for the worst set; nearly orthogonal sets can need fewer, and the bound says nothing about typical data

## Source

Larsen and Nelson (2017), [LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md), FOCS 2017, read in [NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md)
from arXiv 1609.02094v2.

## What was actually shown

**The lower bound (Theorem 2).** For integers n, d ≥ 2 and
lg^0.5001 n/√min{n, d} < ε < 1 there is X ⊂ ℝ^d, |X| = n, such that any
f : X → ℝ^m with (1 − ε)‖x − y‖² ≤ ‖f(x) − f(y)‖² ≤ (1 + ε)‖x − y‖² has
m = Ω(ε⁻² lg(ε²n)). The abstract states it as Ω(ε⁻² lg n) for
1/min{n, d}^0.4999 < ε < 1. The matching upper bound is
O(min{n, d, ε⁻² lg n}), by the distributional lemma with δ < 1/C(n, 2) and
a union bound ([THEORY-tmpns5kz](THEORY-tmpns5kz.md)).

**The proof.** The hard set is 0, the basis vectors e₁ … e_d and many
k-sparse vectors y_S, with k = ε⁻²/256. Any valid embedding can be encoded
in O(nm) bits by rounding to nets (Lemma 2, Corollary 1), and the encoding
determines every support S, because inner products survive to within 6ε
(Lemma 3). Counting supports gives nm = Ω(kn lg(d/k)).

**What it closes.** Earlier lower bounds fell short by lg(1/ε) (Welch,
Levenshtein, Alon) or held only for linear maps (the authors' own earlier
paper). The paper concludes that the distributional lemma plus a union
bound cannot be improved. It reports that Alon and Klartag later proved
the lower bound of its Conjecture 1, Θ(min{n, d, ε⁻² lg(2 + ε²n)}), for all
parameters.

**What could have come out otherwise.** An embedding of the hard set into
o(ε⁻² lg(ε²n)) dimensions would refute it. The counting step was read in
full; two expressions were partly garbled in extraction, and the NOTE says
where.

## What this does not say

- **That every set needs this many dimensions.** It is the worst case,
  shown by existence. Low intrinsic dimension or typical data are not
  treated.
- **The constant.** It is untracked, and k = ε⁻²/256 in the construction
  suggests it is small.
- **Anything for small ε.** Below about 1/√min{n, d} the bound is
  min{n, d}, and the conjectured form has lg(2 + ε²n) in place of lg n.
- **A sharp threshold.** There is no transition in the sense of
  [THEORY-tmp644mk](THEORY-tmp644mk.md), only matching orders.
- **A bound on how many nearly orthogonal directions fit.** ε-incoherent
  sets of n vectors exist in o(ε⁻² lg n) dimensions when
  ε < 2^{−ω(√lg n)}, by Reed–Solomon codes. Superposition, read as packing
  almost-orthogonal features ([NOTE-278](../notes.d/NOTE-278.md)), is not bounded by this result.
- **Anything about maps into more dimensions**, where the bound is vacuous.

## Connections

- [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md): on the distances thread it makes ε⁻² log n the right order on both
  sides. On the superposition thread, my observation in [NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md): the
  count the proof ends on, m = Ω(k lg(d/k)) with k ≈ ε⁻², has the form of
  the compressed-sensing bound in [NOTE-278](../notes.d/NOTE-278.md), so here the JL order arises as
  a sparse-support count.
- [THEORY-tmpns5kz](THEORY-tmpns5kz.md) is the upper bound this one matches.
