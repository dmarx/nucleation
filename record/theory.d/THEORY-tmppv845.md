---
status: Proposed
promote_when: >-
  A proof, read and checked, that the lower bound ∏(rᵢ+1) for one hidden
  layer holds for uniform approximation on a box and not only for Taylor
  matching at the origin, and either that it survives hidden-layer
  biases or a statement of what replaces it with them. Against it: a
  family of one-hidden-layer networks with fewer neurons converging
  uniformly to a monomial, or a bias-free construction beating the
  bound. More trained-network experiments on products cannot settle it,
  since they measure what training finds, not what exists.
title: 'For networks of smooth units without biases, one hidden layer needs exactly ∏(rᵢ+1) neurons to approximate the monomial x₁^r₁⋯xₙ^rₙ and a deep network O(Σ log rᵢ), so the cost of flattening a polynomial grows exponentially with its degree in distinct variables and not with the number of inputs: products of many inputs separate depths, bounded-degree polynomials do not'
version: 1
tags:
- mathematics
- learning-theory
date: '2026-10-09'
source:
- LIT-tmpbq8zx
- LIT-887
summary: >-
  Rolnick and Tegmark (2017), [LIT-tmpbq8zx](../literature.d/LIT-tmpbq8zx.md), Theorems 4.1 to 4.3,
  extending Lin, Tegmark and Rolnick's 2ⁿ for a product ([LIT-887](../literature.d/LIT-887.md)). Proved
  for Taylor matching at the origin with bias-free units; the uniform
  version's lower bound rests on an unproved step. The flip side, that a
  polynomial of degree d with c monomials costs one layer at most c·2ᵈ
  however many inputs it has, is the edge: the separation does not reach
  the low-order polynomials [LIT-887](../literature.d/LIT-887.md) calls natural.
---


# THEORY-tmppv845: For networks of smooth units without biases, one hidden layer needs exactly ∏(rᵢ+1) neurons to approximate the monomial x₁^r₁⋯xₙ^rₙ and a deep network O(Σ log rᵢ), so the cost of flattening a polynomial grows exponentially with its degree in distinct variables and not with the number of inputs: products of many inputs separate depths, bounded-degree polynomials do not

## Source

Rolnick and Tegmark (2017), [LIT-tmpbq8zx](../literature.d/LIT-tmpbq8zx.md): Proposition 3.3, Theorems 4.1 to
4.3 and Proposition 4.6, with the appendix proofs, as read in
[NOTE-tmp5dcxw](../notes.d/NOTE-tmp5dcxw.md). Lin, Tegmark and Rolnick (2016), [LIT-887](../literature.d/LIT-887.md), Appendix A, for
the case rᵢ = 1 and the sign-pattern construction, as read in [NOTE-688](../notes.d/NOTE-688.md).

## What was actually shown

For N(x) = A_k σ(⋯σ(A₀x)⋯) with no biases and σ smooth with nonzero
Taylor coefficients up to the degree d of the monomial:

- **Lower bound, one hidden layer.** If Σⱼ wⱼ σ(aⱼ·x) has the monomial as
  its degree-d Taylor polynomial at 0, the matrix ∏_{h∈S} a_{hj}, indexed
  by the ∏(rᵢ+1) sub-multisets S of the monomial's variables, has full
  row rank, so there are at least ∏(rᵢ+1) units. Checked.
- **Matching upper bound** from summing σ(±x₁ ± ⋯) over sign patterns,
  and a deep bound Σ(7⌈log₂ rᵢ⌉+4) by repeated squaring and a tree of
  product gates. Both transfer to uniform approximation by rescaling
  (Proposition 3.3).
- **Sparse polynomials.** With c monomials, one layer costs at least 1/c
  of the dearest monomial and at most the sum over monomials.

What could have come out otherwise: the lower bound could have been
polynomial in n (sums of powers of linear forms can be economical; any
univariate polynomial of degree d needs only d+1), and it is not.

## What this does not say

- **Not that depth helps on bounded-degree functions.** Each monomial of
  degree d costs one layer at most 2ᵈ, so a polynomial with c monomials
  costs at most c·2ᵈ for any n. For the quadratic-to-quartic Hamiltonians
  that [LIT-887](../literature.d/LIT-887.md) argues physics supplies, this separation gives nothing;
  any depth advantage there must come from elsewhere, such as [LIT-887](../literature.d/LIT-887.md)'s
  composition argument, which nothing proves.
- **Not a uniform-approximation lower bound.** The paper claims one
  (Theorem 4.1), but its proof assumes that uniform closeness forces the
  Taylor coefficients close, which fails for networks in general
  (ε·tanh(x/ε²) is within ε of 0 with first coefficient 1/ε).
- **Not about standard networks.** No biases, smooth σ with nonzero
  low-order coefficients; ReLU and tanh fall outside. Neuron counts are
  finite only because weights are unbounded.
- **Not about intermediate depth.** At depth k only the upper bound
  O(n^((k−1)/k)·2^(n^(1/k))) for a product is proved; 2^Θ(n^(1/k)) is a
  conjecture.
- **Not about learning,** nor about binary inputs, where a conjunction of
  k bits is one threshold unit ([LIT-887](../literature.d/LIT-887.md), Eq. 13); so it says nothing for
  [QUESTION-025](../questions.d/QUESTION-025.md)'s lattices of binary attributes. And no instruction for
  machine learning: the paper's depth rule of thumb is not part of this
  account.
