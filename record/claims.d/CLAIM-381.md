---
number: 381
status: Active
formerly:
- CLAIM-tmppwjei
title: "Over a finite class of items with finite judgement outcomes, a constant outcome kernel fits every item only when the target readers' averaged responses do not vary with the item, an exact fit is a garbling with the item as common parameter, and Le Cam's deficiency and its restriction to finitely many decision problems are finite computations"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-228 and filed Active at the owner's direction, carrying
    out the promotion audit's decision (record/promotion-audit/decisions/CLAIM-228.yaml,
    batch 014, ADR-047). CLAIM-228 was filed as demonstrated, but its defeat
    condition is a study of whether the restated measure tells procedures
    apart, which is empirical. These are its derivations, which its own
    summary calls "elementary". CLAIM-228 keeps the proposal and rests on
    this claim.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in (1) to (3): a constant kernel that meets the across-items
  condition while the averaged target responses vary with the item; an
  exact fit that is not the kernel applied to the source family indexed by
  the item; or, for finitely many items, finite outcome sets and finitely
  many problems with finite action sets, a deficiency that is not the
  stated linear programme or a restricted deficiency not attained at a
  deterministic target rule.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-19'
line:
- pragmatic-transport
- formal-apparatus
rests_on:
- CLAIM-011
grounds:
- THEORY-717
summary: >-
  The derivational core of [CLAIM-228](CLAIM-228.md). Over a finite class of items, the
  target term is the readers' response averaged over a procedure's
  output, and one outcome kernel family is fixed across the items. Then a
  constant kernel fits only target responses that carry no information
  about the item. An exact fit is a garbling, with the item as the common
  parameter. And Le Cam's deficiency between the two finite tables is one
  linear programme. Its restriction to finitely many decision problems is a
  finite computation. It does not say the measure is informative, which is
  [CLAIM-228](CLAIM-228.md)'s empirical question.
supports:
- CLAIM-228
---
<!-- inactive-ok-file: CLAIM-228 — Proposed; the proposal this was split from, cited as open -->

# CLAIM-381: Over a finite class of items with finite judgement outcomes, a constant outcome kernel fits every item only when the target readers' averaged responses do not vary with the item, an exact fit is a garbling with the item as common parameter, and Le Cam's deficiency and its restriction to finitely many decision problems are finite computations

## The claim

**Setting.** This is [CLAIM-228](CLAIM-228.md)'s. 𝒰 is a finite class of source items. In
context C, source readers respond to u with e^o_C(· | u), on finitely many
judgement outcomes. A rendering procedure T(v | u) is a channel on texts.
The target term is ē^t_τ(C)(· | u) = Σ_v T(v | u) e^t_τ(C)(· | v), also on
finitely many outcomes. The fidelity condition asks for one kernel family
{K_C}, the same for every u, with ē^t_τ(C)(· | u) ≈ (K_C)# e^o_C(· | u).
It is scored on held-out items, which is [CLAIM-011](CLAIM-011.md)'s remedy.

**(1) Constant kernels.** If K_C(· | s) = q for every source outcome s, then
(K_C)# e = q for every distribution e. So the condition holds for every u
only if ē^t_τ(C)(· | u) = q for every u. Whenever the averaged target
responses vary with the item, a constant kernel fails the condition. On
held-out items it pays the distance between q and each item's target
response. That is what the per-pair construction of [CLAIM-207](CLAIM-207.md) lacks.

**(2) Exact fit is a garbling.** If ē^t_τ(C)(· | u) = (K_C)# e^o_C(· | u) for
every u, then the experiment u ↦ ē^t_τ(C)(· | u) is the Markov matrix K_C
applied to the experiment u ↦ e^o_C(· | u). That is the definition of a
garbling, with the item as the common parameter. No theorem is needed.

**(3) Deficiency is a finite computation.**
- Le Cam's deficiency of the source table for the target table is the
  least, over stochastic matrices M, of the largest over u of
  TV(M# e^o_C(· | u), ē^t_τ(C)(· | u)).
- It is one linear programme. Minimise t over M, slacks s_(u,y) and t,
  subject to:
  - M stochastic;
  - s_(u,y) ≥ ±[(M# e^o_C(· | u))(y) − ē^t_τ(C)(y | u)];
  - ½ Σ_y s_(u,y) ≤ t.
  M# e is linear in M, so every constraint is linear.
- For a finite family Q of problems with finite action sets, fix a target
  rule ρ_t. The inner infimum over source rules ρ_s of
  max_u [R_s(ρ_s, u) − R_t(ρ_t, u)] is a linear programme.
- As a function of (ρ_s, ρ_t) that maximum is a maximum of affine
  functions, so it is jointly convex. Minimising over ρ_s leaves a convex
  function of ρ_t.
- Its supremum over the product of simplices is therefore attained at a
  vertex, a deterministic rule, of which there are finitely many.

## What it does not say

- It does not say the restated measure tells rendering procedures apart.
  That is [CLAIM-228](CLAIM-228.md)'s defeat condition, an empirical question
  ([CASE-055](../cases.d/CASE-055.md)).
- It says nothing of the tables' estimation error. They are estimated from
  finite samples of readers, and the plug-in bias [CLAIM-235](CLAIM-235.md) shows applies.
- It does not say a fitted K_C is the translator's process, or that a
  single rendering has a fidelity under this measure.
