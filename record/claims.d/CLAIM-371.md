---
number: 371
status: Active
formerly:
- CLAIM-tmpzk12h
title: 'Under the componentwise order on distortion profiles, two profiles are incomparable exactly when they trade off, and then positive weightings can rank them either way, while every positive weighting agrees with a dominance'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-128 under ADR-043 and filed Active at the owner's
    direction, from the owner's promotion audit of 2026-10-19, which found
    CLAIM-128 compound: a partial-order fact, demonstrated, and a thesis
    about fidelity and tasks, which is argued. This claim is the first
    part, with its proof. CLAIM-128 keeps the thesis and now rests on it.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the two-line proof below: a pair of profiles that trade off
  and are comparable, or that trade off and are ranked the same way by
  every positive weighting, or a dominance that some positive weighting
  reverses.
tags:
- mathematics
- model-comparison
date: '2026-10-19'
line: formal-apparatus
uses:
- TERM-043
summary: >-
  The order-theoretic part of [CLAIM-128](CLAIM-128.md), on its own so that it can carry its
  own warrant. It says nothing about translation, what the components
  measure, or which weighting a task fixes. Only that, under the
  componentwise order of [TERM-043](../terms.d/TERM-043.md), a trade-off is incomparability, that a
  trade-off can be resolved either way by positive weights, and that a
  dominance cannot.
supports:
- CLAIM-128
---
<!-- inactive-ok-file: CLAIM-128 — Proposed; the thesis this claim was split from and that rests on it, cited as open -->

# CLAIM-371: Under the componentwise order on distortion profiles, two profiles are incomparable exactly when they trade off, and then positive weightings can rank them either way, while every positive weighting agrees with a dominance

## The claim

Let a transport T have the distortion profile D(T) = (D₁(T), …, D_k(T)),
each component a real number, smaller meaning less distortion. Following
[TERM-043](../terms.d/TERM-043.md), T is at least as faithful as T′ when Dⱼ(T) ≤ Dⱼ(T′) for every j.
Say the two **trade off** when there are components i and j with
Dᵢ(T) < Dᵢ(T′) and Dⱼ(T) > Dⱼ(T′). For weights w with every wⱼ > 0, write
D_w = Σⱼ wⱼDⱼ.

1. T and T′ are incomparable exactly when they trade off.
2. If they trade off, some positive w gives D_w(T) < D_w(T′) and another
   gives D_w(T) > D_w(T′).
3. If T is at least as faithful as T′ and strictly less distorted on some
   component, every positive w gives D_w(T) < D_w(T′).

## Proof

Let a = D(T) − D(T′). (1) T is not at least as faithful as T′ exactly when
some aⱼ > 0, and T′ is not at least as faithful as T exactly when some
aᵢ < 0; both together are the trade-off. (2) Put weight M on a component
with aᵢ < 0 and weight 1 on the rest: w·a ≤ M aᵢ + Σ_{l≠i} |a_l|, which is
negative for M large. Putting M on a component with aⱼ > 0 instead makes
w·a positive. (3) Every aⱼ ≤ 0 and some aⱼ < 0, so w·a < 0 when every
wⱼ > 0.

## What it does not say

- It does not say any pair of translations trades off. Whether the
  components move together for the tasks studied is [QUESTION-013](../questions.d/QUESTION-013.md).
- It does not say how the components are measured ([QUESTION-005](../questions.d/QUESTION-005.md)), or
  that they are independent.
- It does not say no weighting is right. That fidelity is task-relative, and
  that the theory fixes no weighting, is [CLAIM-128](CLAIM-128.md)'s thesis, which is
  argued, not proved.
