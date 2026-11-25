---
number: 970
status: Proposed
formerly:
- CLAIM-tmpzdcl1
title: 'Best buffer variable is not the gap block'
statement: >-
  In a non-lattice coupled-agent system the variable most informative about
  the far environment across a buffer is generically not the gap-isolated
  block: it is a boundary mode and the block is the spread collective mode,
  and they coincide only under a homogeneous boundary or one-way drive
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A demonstration that across generic non-lattice coupled-agent systems with
  heterogeneous, two-way boundaries the variable most informative about the
  far environment across a buffer coincides with the gap-isolated block's
  joint mode whenever the region clears the block test — so that the
  divergence found here is an artefact of the operationalization (equal-time
  canonical correlation for informativeness, the leading mode of the
  region's restricted dynamics for the block) rather than of boundary
  structure. A single model in which they happen to agree does not satisfy
  it; nor does the homogeneous-boundary or one-way-drive case, which this
  claim already excepts.
tags:
- individuation
- complex-systems
- information-theory
date: '2026-11-22'
line:
- distributed-agency
answers:
- QUESTION-065
grounds:
- CASE-375
complements:
- CLAIM-157
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; the block criterion this claim bounds, its joint-mode unit, and the readings the study operationalizes -->

# CLAIM-970: Best buffer variable is not the gap block

## The claim

[QUESTION-065](../questions.d/QUESTION-065.md) asks whether a system's own locality can fix the target a
sufficiency boundary serves — as informativeness about the far environment
across a buffer — so that the coarse variables kept are the system's and not
the analyst's, and whether those variables are [CLAIM-157](../claims.d/CLAIM-157.md)'s gap-isolated
block. For a lattice the record already has a yes: the variable most
informative across a buffer is the leading transfer-matrix eigenvector
([THEORY-205](../theory.d/THEORY-205.md)), which is the slow collective mode. [CASE-375](../cases.d/CASE-375.md) ran the
comparison in coupled-agent systems that are not lattices — communities on a
path, random within — and found that the yes does not carry over.

In such a system, for a region `R` separated from a far environment `E` by a
buffer, the direction of `R` most informative about `E` (the top
canonical-correlation direction) and the gap-isolated block mode (the leading
mode of `R`'s own dynamics, the projector of [CLAIM-164](../claims.d/CLAIM-164.md)) generically
differ. The informative variable concentrates on the few boundary nodes that
bridge to the environment — it is a *boundary mode* — while the gap-isolated
block is the *collective mode* spread over the whole region. The two coincide
only in two special cases: a **homogeneous boundary**, where every node of
`R` couples alike across the edge, which is what a lattice slab has and what
makes the lattice result hold; and **one-way drive**, where `R` is a pure
source with no incoming boundary coupling to localize the informative
direction. Over heterogeneous, two-way boundaries — the generic non-lattice
case — they come apart, sometimes to near-orthogonality.

This answers [QUESTION-065](../questions.d/QUESTION-065.md) the other way for a generic local system, and so
bounds [CLAIM-157](../claims.d/CLAIM-157.md): clearing the near-decomposability and gap test does
identify a block, and does so robustly here (the region clears it by two to
three orders of magnitude), but the block's joint mode is not in general the
variable the system's own locality would keep as most informative about its
far environment. Locality does not, on its own, hand the block criterion its
target. The match that holds on a lattice is a property of the lattice's
homogeneous boundary, not of coupled agents as such.

## What it does not say

- **That [CLAIM-157](../claims.d/CLAIM-157.md)'s block criterion is wrong.** [CLAIM-157](../claims.d/CLAIM-157.md) names the unit
  relative to a *stated* target and never claims the target is the one
  locality supplies; that identification is [QUESTION-065](../questions.d/QUESTION-065.md)'s hypothesis, and
  it is that hypothesis this claim bounds. The block test still picks out the
  block it is defined to pick out.
- **That informativeness and the block never coincide.** They coincide under
  a homogeneous boundary and under one-way drive, both demonstrated here.
  The claim is about the generic heterogeneous two-way case.
- **That the result transfers beyond the model.** It is shown for a linear
  Gaussian VAR(1) on a path of random communities, with informativeness read
  as equal-time canonical correlation and the block as the leading mode of
  the region's restricted dynamics. A conditional-information reading of
  "across a buffer", a time-lagged transfer operator, or a nonlinear system
  could behave differently; the claim's warrant is this demonstration.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
