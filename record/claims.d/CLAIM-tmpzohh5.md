---
status: Proposed
title: 'Forcing an information-bottleneck encoder at the smaller budget to be a garbling of a bottleneck at the larger budget costs at most the concavity gap of the information curve, I(λ₁) − (λ₁/λ₂) I(λ₂), because erasing a fine bottleneck with probability 1 − λ₁/λ₂ gives a nested encoder within the smaller budget'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a finite joint distribution, budgets
  0 < λ₁ < λ₂ and a bottleneck T₂ at λ₂ with I(X; T₂) = λ₂, for which the
  erasure of T₂ with keep probability λ₁/λ₂ has I(X; ·) above λ₁ or
  I(Y; ·) below (λ₁/λ₂) I(λ₂).
tags:
- information-theory
- mathematics
date: '2026-11-22'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-220
grounds:
- THEORY-753
summary: >-
  Derived for LEAD-039, on the part of QUESTION-220 that asks how much is
  lost by forcing nesting when it fails. It generalizes the single
  computation of NOTE-980, which erased CLAIM-387's β = 12 optimum down to
  the β = 8 rate and kept 0.079 bits about Y against the optimum's 0.097.
  The bound is zero exactly where the curve is linear between the two
  budgets and shrinks to zero as the budgets approach, which fits
  CLAIM-392's report that failures cluster at nearby budgets and cost
  little. It bounds the loss; it does not give its size. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

# CLAIM-tmpzohh5: Forcing an information-bottleneck encoder at the smaller budget to be a garbling of a bottleneck at the larger budget costs at most the concavity gap of the information curve, I(λ₁) − (λ₁/λ₂) I(λ₂), because erasing a fine bottleneck with probability 1 − λ₁/λ₂ gives a nested encoder within the smaller budget

## The claim

**Setting.** X and Y finite, I the information curve, bottlenecks as in
THEORY-753. For budgets 0 < λ₁ < λ₂, define the *cost of forcing nesting*
as

  L(λ₁, λ₂) = I(λ₁) − sup { I(Y; T₁) : T₁ = η ∘ T₂ for some bottleneck T₂
  at λ₂ and channel η, with I(X; T₁) ≤ λ₁ }.

It is zero when the problem is (λ₁, λ₂)-refinable (THEORY-753, step 2).

**Bound.** Let λ₂′ = I(X; T₂) ≤ λ₂ for a bottleneck T₂ at λ₂. Then

  0 ≤ L(λ₁, λ₂) ≤ I(λ₁) − min(1, λ₁/λ₂′) I(λ₂) ≤ I(λ₁) − (λ₁/λ₂) I(λ₂).

**Proof.** If λ₂′ ≤ λ₁, T₂ itself is feasible at λ₁ and I(Y; T₂) = I(λ₂)
≥ I(λ₁), so L = 0. Otherwise let α = λ₁/λ₂′ and let T₁ equal T₂ with
probability α and an erasure symbol e otherwise, the coin independent of
everything. T₁ is a garbling of T₂. For any V independent of the coin, the
erasure scales mutual information: I(V; T₁) = α I(V; T₂), since
H(V | T₁) = α H(V | T₂) + (1 − α) H(V). So I(X; T₁) = λ₁ and
I(Y; T₁) = α I(λ₂) ≥ (λ₁/λ₂) I(λ₂). The lower bound 0 ≤ L holds since
every T₁ in the set is feasible at λ₁. ∎

## What it says and does not say

- **It is the chord gap.** By concavity of I with I(0) = 0, the bound is
  non-negative, zero where I is linear on [0, λ₂], and tends to zero as
  λ₁ → λ₂ by continuity of I. Failures of nesting between nearby budgets,
  the kind CLAIM-392's reader found most often, can therefore cost only a
  little in I(Y; T).
- **On CLAIM-387's source** (β = 8 against 12) the bound is
  0.097 − (0.546/0.952) × 0.139 ≈ 0.017 bits, NOTE-980's figure: about
  18% of the coarse optimum's relevant information. The true cost may be
  much smaller, since a better garbling than an erasure may exist.
  CLAIM-392's 4.7 × 10⁻³ bits is in a different measure (unique
  information) and is not compared here.
- **Not the size of the loss.** It is an upper bound, from one family of
  garblings. Computing L exactly means optimizing over channels from a
  fine optimum, a non-convex problem left open.
- **Only one direction.** It keeps the fine bottleneck and degrades it.
  Keeping the coarse one and extending it, (T₁, S) at λ₂, is the other way
  to force nesting, and is not bounded here.
