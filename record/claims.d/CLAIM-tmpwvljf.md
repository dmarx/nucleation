---
status: Active
title: 'D_obs sums over source contexts only, so a target context outside the image of τ appears in no term: a rendering that adds a relation pays nothing, and a change of cover registers only as loss'
version: 1
role: granted
tags:
- mathematics
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-076
- CLAIM-087
objects_to:
- CLAIM-005
uses:
- TERM-021
- TERM-043
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. L_obs and D_obs are sums over source
  contexts, so a target context that is not the image of one appears in
  no term. The line says interpreters add relations ([CLAIM-076](CLAIM-076.md)) and that
  a transport can add a distinction ([CLAIM-087](CLAIM-087.md)), and D_obs is the one
  component with a formula ([CLAIM-128](CLAIM-128.md)). Granted, because it is read off
  the definition. It does not say no other component could catch an
  addition, or that additions are distortions.
---
<!-- inactive-ok-file: CLAIM-005 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-076 CLAIM-087 CLAIM-128 CLAIM-034 — Proposed; the claims on added relations, the profile and adaptive translation, cited as open -->

# CLAIM-tmpwvljf: D_obs sums over source contexts only, so a target context outside the image of τ appears in no term: a rendering that adds a relation pays nothing, and a change of cover registers only as loss

## The objection

[CLAIM-005](CLAIM-005.md) gives the manuscript's L_obs(T) = Σ_C w_C d_C[(K_C)#e_C^o,
e_τ(C)^t]. [TERM-043](../terms.d/TERM-043.md) gives the profile's D_obs(T) = Σ_C w_C d_C(T_C# e_C^o,
e_τ(C)^t). Both sums run over source contexts C. A target context that is
not τ(C) for any source context C appears in no term.

A worked case. Let the source cover have one context C, in which readers
judge the speaker's stance. Let the target cover have two: τ(C), with the
same judgement, and a new context C′, in which readers judge a relation the
source does not carry, such as whether the speaker is mocking a third
party. Then D_obs = w_C d_C(K_C# e_C^o, e_τ(C)^t). Two renderings that agree
on τ(C) and differ in any way on C′ have the same D_obs.

So a relation that a rendering adds costs nothing. A change of cover
registers only as loss: a source context with no good image pays its term,
and a target context with no preimage is free.

The line says additions happen. [CLAIM-076](CLAIM-076.md): "each interpreter, such as a
captioner, may add motives and relations that were not present". [CLAIM-087](CLAIM-087.md)
is "a transport that adds a distinction". And D_obs is the one component of
the profile that can be computed. [CLAIM-128](CLAIM-128.md): "Only D_obs has a formula".
So the one computable component is blind to additions.

## What it does not say

- It does not say no other component can catch an addition. D_struct,
  "Failures to preserve restriction maps and specified relational
  constraints" ([TERM-043](../terms.d/TERM-043.md)), could, if the added relation is specified.
- It does not say additions are distortions. [CLAIM-087](CLAIM-087.md)'s improved access,
  and the deliberate adaptation of [CLAIM-034](CLAIM-034.md), may be wanted. The point is
  that D_obs cannot see them either way.
- It does not say directedness is wrong. A directed measure may weigh
  losses and additions differently. This one does not weigh additions at
  all.
