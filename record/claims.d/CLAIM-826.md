---
number: 826
status: Proposed
formerly:
- CLAIM-tmpjbee7
title: "Near a critical point a system becomes harder to separate into levels and easier to classify: fluctuations stay collectively consequential across scales, so no separation of levels holds, while the details of the microscopic interactions become irrelevant to the scaling exponents, so systems fall into a few universality classes"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A continuous transition at which the two come apart the other way: a
  system whose critical exponents depend on the details of its
  microscopic interactions beyond the few relevant parameters and the
  symmetry and dimension that fix a universality class, or one at which
  the correlation length stays finite, so that blocks larger than it are
  nearly independent and a block description is closed. Marginal cases,
  where exponents vary along a line of fixed points, limit the claim
  rather than defeat it, and the claim says so.
tags:
- complex-systems
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
uses:
- TERM-139
complements:
- CLAIM-478
grounds:
- THEORY-777
summary: >-
  A17 §5 of the exchange "Rich Get Richer Power Laws" (2026-11-21), on
  "continue" at U11: "Critical systems become harder to separate but
  easier to classify". At criticality "Microscopic fluctuations remain
  collectively consequential", so the levels of description stop being
  separable, and "Microscopic details become less important to the
  universal scaling laws", so the system is "extraordinarily complex in
  its instantaneous configuration but mathematically simple in its
  statistical description". The two halves are about different things,
  which is why they do not conflict. The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A17); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: TERM-139 THEORY-777 CLAIM-478 CLAIM-820 — Proposed or new, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or Proposed entries the record already held -->

# CLAIM-826: Near a critical point a system becomes harder to separate into levels and easier to classify: fluctuations stay collectively consequential across scales, so no separation of levels holds, while the details of the microscopic interactions become irrelevant to the scaling exponents, so systems fall into a few universality classes

## The claim

A17 §5 poses it as a paradox. Ordinarily a macroscopic theory works
because fluctuations average out over large regions. "Near criticality,
however, fluctuations can remain correlated across increasingly large
distances", with ξ ∝ |T − T_c|^(−ν) and τ ∝ ξ^z, so "The distinction
between microscopic and macroscopic behavior becomes less clean. Yet, at
precisely the same time, the system can become *more universal*." A's
resolution:

> **Microscopic fluctuations remain collectively consequential.**
>
> **Microscopic details become less important to the universal scaling
> laws.**

"This is why a critical system can be extraordinarily complex in its
instantaneous configuration but mathematically simple in its statistical
description." A's example is the 2D Ising model, with ν = 1, η = 1/4 and
β = 1/8 (the exact exponents, standard).

## Why the two halves do not conflict

They are said of different objects. Separation is about the system's
states: whether blocks larger than some scale are nearly independent, so
that a description of block sums is closed. Classification is about the
renormalization flow: whether perturbations away from the fixed point
grow or shrink under coarse-graining. In the terms of [TERM-139](../terms.d/TERM-139.md), a
critical system sits at a fixed point with a few relevant directions and
many irrelevant ones. Its fluctuations are scale-free, so no block size
gives independence; and the irrelevant directions shrink, so systems that
differ only along them share the fixed point's exponents. The record's
reading of the coarse-grained Fisher information on the critical Ising
model shows the second half directly: two stiff directions survive
decimation while the irrelevant ones fall by up to six decades
([THEORY-777](../theory.d/THEORY-777.md)).

## Where it sits

- **[CLAIM-478](CLAIM-478.md) and its note of this date.** That claim has rate
  differences making levels: where some degrees of freedom settle faster
  than others, their relation is a constraint over the window between the
  rates. The note adds the spatial window a finite correlation length
  gives, and that criticality removes it, in space and, through τ ∝ ξ^z,
  in time. This claim is the other side of that loss: what goes at
  criticality is the separation of levels, and what remains, and
  sharpens, is the classification by universality class. It complements
  [CLAIM-478](CLAIM-478.md) rather than objecting to it.
- **Sloppiness.** "Easier to classify" is the parametric face of
  [CLAIM-820](CLAIM-820.md): many microscopic models give nearly the same large-scale
  predictions.

## What it does not say

- Not that every critical system is fully classified by a few numbers.
  Marginal directions give logarithmic corrections or lines of fixed
  points with varying exponents ([TERM-139](../terms.d/TERM-139.md)).
- Not that universality needs criticality. Irrelevant directions shrink
  under coarse-graining at any fixed point, including the trivial ones of
  ordered and disordered phases; what is special at a critical one is that
  the fixed point is nontrivial and the separation of levels fails at the
  same time.
