---
number: 940
status: Proposed
formerly:
- CLAIM-tmplxbtx
title: 'IB refinability is closed under products'
statement: >-
  Successive refinability of the information bottleneck at every pair of
  budgets is closed under independent products: if (X₁, Y₁) and (X₂, Y₂) are
  independent and each is refinable at every pair of budgets, so is ((X₁,
  X₂), (Y₁, Y₂)), because the product's information curve is the
  sup-convolution of the factors' curves and the split of the budget can be
  chosen nondecreasing in both factors
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: two independent finite pairs, each
  refinable at every pair of budgets, whose product has budgets
  λ₁ < λ₂ at which no bottleneck at λ₁ is a garbling of a bottleneck at
  λ₂; or an encoder T of the product with I(Y; T) above
  max over λ₁ + λ₂ = I(X; T) of I₁(λ₁) + I₂(λ₂).
tags:
- information-theory
- mathematics
- learning-theory
date: '2026-11-22'
line:
- learned-structure
- formal-apparatus
answers:
- QUESTION-220
grounds:
- THEORY-753
- THEORY-757
complements:
- CLAIM-939
summary: >-
  Derived for [LEAD-039](../leads.d/LEAD-039.md), with the tensorization checked on grid envelopes
  of twelve random products ([CASE-360](../cases.d/CASE-360.md)). Combined with [CLAIM-939](CLAIM-939.md)
  and [THEORY-757](../theory.d/THEORY-757.md), it gives a structural condition on P(X, Y) of the kind
  [QUESTION-220](../questions.d/QUESTION-220.md) asks for: a source that is, after merging inputs with equal
  p(Y|x), an independent product of pairs each of which has two distinct
  rows or has Y a function of X, is refinable at every pair of budgets,
  with any number of distinct rows. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-939 CASE-360 — new; filed with this claim from LEAD-039 -->

# CLAIM-940: IB refinability is closed under products

## The claim

**Setting.** (X₁, Y₁) and (X₂, Y₂) are finite pairs, independent of each
other, with X = (X₁, X₂) and Y = (Y₁, Y₂). I, I₁ and I₂ are the information
curves: I(λ) is the largest I(Y; T) over encoders T → X → Y with
I(X; T) ≤ λ. Bottlenecks and refinability are as in [THEORY-753](../theory.d/THEORY-753.md). "Refinable
at every pair of budgets" means (λ, λ′)-refinable for all 0 ≤ λ ≤ λ′.

**Theorem.** If each pair is refinable at every pair of budgets, so is the
product. By induction, so is any finite independent product of such pairs.

## Proof

**1. The product's curve is the sup-convolution.**
I(λ) = max over λ₁ + λ₂ = λ, λᵢ ≥ 0, of I₁(λ₁) + I₂(λ₂).
- *At least.* If Tᵢ is a bottleneck of pair i at λᵢ, the product encoder
  q(t₁, t₂ | x) = q₁(t₁|x₁) q₂(t₂|x₂) makes (X₁, Y₁, T₁) and (X₂, Y₂, T₂)
  independent, so I(X; T) = λ₁′ + λ₂′ ≤ λ and I(Y; T) = I₁(λ₁) + I₂(λ₂).
- *At most.* Take any T, and put U₁ = T and U₂ = (T, X₁). The joint law is
  p(x₁, y₁) p(x₂, y₂) q(t | x₁, x₂), so Y₁ is independent of
  (X₂, Y₂, T) given X₁, and Y₂ of (X₁, Y₁, T) given X₂. Hence
  U₁ → X₁ → Y₁ and U₂ → X₂ → Y₂ are Markov chains. By the chain rule and
  X₁ ⊥ X₂,
  I(X; T) = I(X₁; T) + I(X₂; T | X₁) = I(X₁; U₁) + I(X₂; U₂).
  And, using Y₁ ⊥ Y₂ and then Y₁ ⊥ (Y₂, T) given X₁,
  I(Y; T) = I(Y₁; T) + H(Y₂) − H(Y₂ | T, Y₁)
  ≤ I(Y₁; T) + I(Y₂; T, Y₁, X₁) = I(Y₁; U₁) + I(Y₂; U₂).
  So I(Y; T) ≤ I₁(λ₁′) + I₂(λ₂′) with λ₁′ + λ₂′ = I(X; T) ≤ λ, and the
  curves are nondecreasing.

**2. A monotone split.** Each Iᵢ is concave, nondecreasing and continuous
on [0, ∞), with Iᵢ(0) = 0 and Iᵢ(λ) ≤ λ. Let g(λ₁, λ) = I₁(λ₁) + I₂(λ − λ₁)
on 0 ≤ λ₁ ≤ λ. The constraint sets [0, λ] rise with λ, and g has increasing
differences in (λ₁, λ): for λ₁ < λ₁′ and λ < λ′, concavity of I₂ gives
I₂(λ − λ₁) − I₂(λ − λ₁′) ≥ I₂(λ′ − λ₁) − I₂(λ′ − λ₁′), an increment over an
interval of fixed length shifted right being smaller. By Topkis's
monotonicity theorem the sets of maximizers rise in the strong set order,
so the least maximizer λ₁(λ) is nondecreasing in λ. The same argument
applied to the problem written in λ₂ shows that its greatest maximizer,
which is λ − λ₁(λ), is nondecreasing too.

**3. Refinability.** Let λ ≤ λ′, with splits (λ₁, λ₂) ≤ (λ₁′, λ₂′) from
step 2. By hypothesis there are bottlenecks Tᵢ at λᵢ and Tᵢ′ at λᵢ′ of pair
i, and channels ηᵢ with q(Tᵢ | Xᵢ) = ηᵢ ∘ q(Tᵢ′ | Xᵢ) ([THEORY-753](../theory.d/THEORY-753.md), steps 1
and 2; for λᵢ = λᵢ′ take Tᵢ = Tᵢ′ and ηᵢ the identity). The product
encoders T = (T₁, T₂) and T′ = (T₁′, T₂′) are bottlenecks of the product at
λ and λ′ by step 1, and q(T | X) = (η₁ ⊗ η₂) ∘ q(T′ | X). By [THEORY-753](../theory.d/THEORY-753.md) the
product is (λ, λ′)-refinable. ∎

## What follows

- **A structural condition on P(X, Y).** Call a pair *elementary* if p(Y|x)
  takes at most two distinct values ([CLAIM-939](CLAIM-939.md), with [THEORY-757](../theory.d/THEORY-757.md)'s
  binary case inside it) or Y is a function of X ([THEORY-757](../theory.d/THEORY-757.md), case 1).
  Every source that is, after merging inputs with equal p(Y|x)
  ([THEORY-743](../theory.d/THEORY-743.md), step 1), an independent product of elementary pairs, up to
  relabelling, is refinable at every pair of budgets. Two independent
  noisy binary channels already give four distinct rows and four outputs,
  outside both [THEORY-757](../theory.d/THEORY-757.md) and [CLAIM-939](CLAIM-939.md).
- **Independent noise.** Adding an input coordinate independent of
  everything, or an output coordinate independent of everything, is the
  product with a pair of zero information, which is trivially refinable.

## What it does not say

- **Not a characterization.** The condition is sufficient. Sources that
  are not products of elementary pairs may nest; whether one with three
  distinct rows and no product structure always fails, or sometimes nests
  at every pair, is open ([CASE-360](../cases.d/CASE-360.md) found sources of both kinds on a
  coarse grid of budgets, uncertified).
- **Not the converse.** It is not shown that a product with a
  non-refinable factor fails to nest, though it is likely: the
  product's bottlenecks need not all be products, so the factor's failure
  does not transfer directly.
- **Not the Lagrangian path alone.** The statement is for the primal
  problem at every pair of budgets, which includes budgets on linear
  stretches of the curve. That is why step 2 is needed.
- **Whether the closure is in the literature was not checked.**
  Tensorization of the bottleneck's information curve for independent
  pairs is of a familiar kind (the argument of step 1 is standard). The
  record holds no reading that states it, or the closure of refinability.
