---
number: 637
status: Proposed
formerly:
- CLAIM-tmpol63b
title: 'The kernel fit of the restated observational distortion, and the Le Cam deficiency computed beside it, run in the garbling direction: in each context they vanish exactly when the target readers'' item tables are a garbling of the source readers'', so they bound what a rendering procedure adds about the item and charge nothing for what it loses, a procedure that renders every item alike scoring zero'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: finite item tables in one context where the
  target's experiment about the item is a garbling of the source's and yet
  no single kernel fits every item exactly, or where the target's table
  does not vary with the item and the constant kernel does not fit it; or
  a reading of the restated measure, as the record states it, on which
  the kernel family is constrained by more than fitting, such as an
  admissibility or separation condition, which would put the measure
  outside this derivation.
tags:
- mathematical-statistics
- probabilistic-modeling
- translation
date: '2026-11-11'
line:
- pragmatic-transport
rests_on:
- CLAIM-381
- CLAIM-503
summary: >-
  Over a finite class of items, the restated D_obs fits one kernel per
  context from the source readers' item tables to the target readers'
  averaged ones, and the deficiency computed beside it is the least
  worst-item distance over such kernels. Both are zero exactly when the
  target's tables are a garbling of the source's, which is the direction
  in which the rendering carries no more information about the item than
  the source. By the randomization criterion, the deficiency bounds how
  much better a receiver of the rendering can decide than a receiver of
  the source, not how much worse. So a procedure whose target readers'
  responses do not vary with the item, the extreme of loss, scores zero,
  as a faithful one does. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-228 CLAIM-005 ADR-075 — Proposed; the measure and theses this bears on, open -->

# CLAIM-637: The kernel fit of the restated observational distortion, and the Le Cam deficiency computed beside it, run in the garbling direction: in each context they vanish exactly when the target readers' item tables are a garbling of the source readers', so they bound what a rendering procedure adds about the item and charge nothing for what it loses, a procedure that renders every item alike scoring zero

## The claim

**Setting** ([CLAIM-381](CLAIM-381.md)'s, which is [CLAIM-228](CLAIM-228.md)'s). A finite class of items
u; in context C the source readers' table e^o_C(· | u) and the target
readers' averaged table ē^t_τ(C)(· | u), both on finite outcome sets; one
kernel K_C for every u.

1. **Zero exactly on garblings.** Some K_C fits every item exactly if and
   only if the experiment u ↦ ē^t_τ(C)(· | u) is a garbling of
   u ↦ e^o_C(· | u). One direction is [CLAIM-381](CLAIM-381.md)'s step (2); the other is
   the definition of a garbling. The deficiency of [CLAIM-381](CLAIM-381.md)'s step (3),
   min over K of max over u of TV(K# e^o_C(· | u), ē^t_τ(C)(· | u)), is
   then zero, and so is the held-in fit of the restated D_obs.
2. **What the deficiency bounds.** [CLAIM-503](CLAIM-503.md), with the source as M and the
   target as N: that deficiency is the least ε for which, in every
   decision problem about the item with losses in [0, 1], a receiver of
   the source can do within ε of whatever a receiver of the rendering
   does. It bounds the rendering's advantage, not its loss.
3. **Collapse scores zero.** If the procedure gives target readers
   responses that do not vary with the item, ē^t_τ(C)(· | u) = q for every
   u, the constant kernel K_C ≡ q fits every item, held-in and held-out,
   which is the "if" half of [CLAIM-381](CLAIM-381.md)'s step (1). The deficiency of the
   target relative to the source is then as large as the source's own
   information about the item allows: with two items whose source tables
   are at total-variation distance d, guessing the item under a uniform
   prior has Bayes risk (1 − d)/2 from the source and 1/2 from the
   rendering.

So the restated measure charges a rendering for target responses that
depart from every garbling of the source's, which includes responses that
distinguish items the source's do not, and charges nothing for a garbling,
however lossy. A faithful procedure whose target is the source passed
through a near-identity kernel also scores near zero, so on these two the
measure does not separate a procedure from its collapse.

Checked numerically (scratch script, numpy only): three items with source
tables (.8, .2), (.3, .7), (.5, .5) and a constant target (.6, .4) give a
constant-kernel fit of 0 to machine precision, and Bayes risks .25 from
the source and .5 from the target for guessing between the first two
items.

## What it bears on

- **[CLAIM-228](CLAIM-228.md)** (Proposed) holds that the restated D_obs separates
  procedures that receivers' task-indexed recovery separates. A procedure
  and its collapse are separated by recovery and not by the measure. Its
  defeat condition is a study ([CASE-055](../cases.d/CASE-055.md)); a collapsing or flattening arm
  in that study, such as a rendering into French that uses one address
  form for every item where the source's footing varies, would test it
  where this derivation says the measure is weakest. To the extent the
  flattened target's footing judgements vary less with the item than the
  source's, the measure scores the flattening well.
- **[CLAIM-488](CLAIM-488.md)** reads the same deficiency as "the approximate case of the
  Blackwell order for translation". Its direction is the one in which the
  rendering is approximately no more informative than the source. The
  deficiency that would bound loss, the target relative to the source, is
  the same linear programme with the roles exchanged ([CLAIM-503](CLAIM-503.md) holds for
  any finite pair), and it is the prior-free counterpart of the decision
  term [CLAIM-259](CLAIM-259.md) sets out, which "charges the rendering for its loss".
- **[CLAIM-005](CLAIM-005.md)**'s title says the match "charges for loss and not for
  addition". That is about contexts outside the image of τ ([CLAIM-256](CLAIM-256.md)).
  Within a context and about the item, the restated match runs the other
  way.

## What it does not say

- That the restated measure is useless: it excludes the constant kernel
  whenever the target varies with the item ([CLAIM-381](CLAIM-381.md)), and it bounds what
  a rendering adds.
- That fidelity should be two-sided. [TERM-008](../terms.d/TERM-008.md)'s transport is directed by
  design, and the manuscript adds a decision term to its observational
  one.
- Anything about a kernel family constrained by separation ([CLAIM-077](CLAIM-077.md)),
  which would exclude the constant kernel and is not part of the restated
  measure.

## Admission

Route: derivation ([ADR-075](../decisions.d/ADR-075.md), step 5). The steps are [CLAIM-381](CLAIM-381.md)'s (1) and (2)
read in both directions and [CLAIM-503](CLAIM-503.md)'s equivalence with M and N named.
No entry states that the fit and the deficiency vanish on every garbling,
that they bound advantage and not loss, or that a collapsing procedure
scores zero; [CLAIM-381](CLAIM-381.md) and [CLAIM-228](CLAIM-228.md) present step (1) only as an
exclusion of the constant kernel. Whether a two-line consequence is
nontrivial is the owner's call; its consequence for [CLAIM-228](CLAIM-228.md)'s study and
for the direction of [CLAIM-488](CLAIM-488.md)'s deficiency is not held anywhere. The
realistic case above (a register-flattening rendering) is not a
separating case for this claim, which is a derivation; it bears on
[CLAIM-228](CLAIM-228.md)'s defeat condition, and would contribute to meeting it only if
recovery in the study separates the flattening from a footing-sensitive
procedure while held-out D_obs does not.
