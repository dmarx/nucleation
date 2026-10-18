---
status: Active
title: 'frustration, of an organization''s demands: the failure of the demands it maintains to be jointly realizable under its admissible transformations and its governance'
version: 1
tags:
- self-governance
- agency
- motivation
date: '2026-10-18'
line: distributed-agency
summary: >-
  A33 of the exchange of 2026-10-17, at the owner's U33, made ordinal by
  the owner's U37 correction. The demands an organization maintains are
  frustrated when no admissible transformation meets them all (structural)
  or when one exists and the organization's governance does not select it
  (governance-induced). In its basic form it is an empty intersection of
  acceptance sets and needs no common scale. It is distinct from strain,
  where the demands are jointly realizable at a cost, and from distress, a
  possible integrated response to either. It is not [CLAIM-153](../claims.d/CLAIM-153.md)'s physics
  sense, though it shares that sense's three-demand minimal obstruction.
used_by:
- CLAIM-tmp442x9
- CLAIM-tmp55mls
- CLAIM-tmpf67p3
- CLAIM-tmpl8vsy
- CLAIM-tmpue67e
- CLAIM-tmpuia0a
- CLAIM-tmpyk3it
---

# TERM-tmp9lmlt: frustration, of an organization's demands: the failure of the demands it maintains to be jointly realizable under its admissible transformations and its governance

## Definition

Fix an organization, the set U of transformations admissible to it, and a
collection D of demands it maintains. Each demand i has an acceptance
condition, a set A_i ⊆ U of the transformations that meet what it
requires. A demand is a requirement, so its acceptance set must be able
to exclude the transformation that changes nothing when change is
demanded. In the ordinal form A_i is fixed by a preorder ⪰_i and a
requirement stated against it:

- strict improvement on a reference u₀, A_i = {u ∈ U : u ≻_i u₀};
- a required level t_i, A_i = {u ∈ U : u ⪰_i t_i}, where t_i is set by
  the demand and the baseline u₀ belongs to A_i only if it already meets
  t_i;
- or a context-indexed obligation, A_i(c) ⊆ U, given directly.

The tempting form A_i = {u : u ⪰_i u₀} is not a demand. If u₀ is
admissible, reflexivity puts u₀ in every A_i, so ⋂ A_i ⊇ {u₀} and every
collection is trivially compatible. Weak Pareto improvement on u₀ is a
requirement on the collection, not on each demand (every demand
⪰_i u₀ and at least one ≻_i u₀), so it is not an intersection of
per-demand sets and does not give a compatibility complex directly. In
the local form for a differentiable learner A_i is the set of updates d
with −g_iᵀd ≥ ε_i, with ε_i > 0 so that d = 0 is excluded, or with
g_iᵀd < 0.

- **Frustrated, structurally:** ⋂_{i∈D} A_i = ∅. No admissible
  transformation meets every demand.
- **Frustrated, by governance:** ⋂ A_i ≠ ∅, and the transformation the
  organization actually selects lies outside it.
- **Not frustrated, strained:** a jointly acceptable transformation exists
  and is selected, at a cost the organization must pay.

The ordinal form comes first. The owner at U37: "We can do quite a lot with
access to an ordering, even if it doesn't give us a true measure." A37
granted it ("I agree with your correction") and demoted the cardinal
residual of A35 to "a quantitative refinement of a more basic
order-theoretic feasibility problem, not the definition of frustration
itself". The refinements are [CLAIM-tmpue67e](../claims.d/CLAIM-tmpue67e.md) (the residual Φ and its dual)
and [CLAIM-tmpl8vsy](../claims.d/CLAIM-tmpl8vsy.md) (structural against governance-induced). The
compatibility complex of a collection of demands is [CLAIM-tmp55mls](../claims.d/CLAIM-tmp55mls.md)'s.

A33's wording, the source of the term: "Frustration: Available ways of
advancing one objective obstruct another, or the current governance cannot
jointly realize the objectives it maintains." A33 §10: "it is a failure of
joint realizability, indexed by the system's objectives, available
transformations, and governance".

The definition is relative three times over: to the demands declared, to
the transformations counted as admissible, and to the organization whose
governance selects. A change in any of the three changes the verdict.
Ordinary training is the case A33 §7 named, where the objectives are the
trainer's: "frustration in this system is primarily a property of an
externally constituted optimization problem" (and see [CLAIM-288](../claims.d/CLAIM-288.md)).

## What it is not

- **Not strain.** A33: "Strain: Achieving a set of objectives requires
  substantial regulatory effort." Strain is a cost on a realizable set. A33
  §3A marks the boundary: a budget on admissible updates can turn strain
  into frustration, because "Actual constraints on admissible updates can
  change feasibility itself." The budget then belongs to U, and the
  verdict is relative to it.
- **Not distress.** A33: "Distress: A possible persistent, integrated
  organizational response to strain or frustration, which may or may not
  have phenomenal significance." Frustration needs no integrated signal and
  no feeling. A33 §6: it "can be organizationally consequential without
  appearing as a unified internal experience or even a unified
  representation".
- **Not pairwise conflict.** Two demands conflict when their preferred
  directions disagree. Frustration is a property of the collection: every
  pair can be jointly realizable while the triple is not
  ([CLAIM-tmp55mls](../claims.d/CLAIM-tmp55mls.md)).
- **Not [CLAIM-153](../claims.d/CLAIM-153.md)'s frustration.** There, frustration is a nonzero
  monodromy of offsets around a cycle of contexts, read off a frustrated XY
  energy. Here it is an empty intersection of acceptance sets over one
  space of transformations, with no torsor and no cohomology class. They
  share the shape that pairs can be fine and a whole not, and A37 warned
  that "Not every optimization conflict has a cohomology class".
- **Not Watson's total frustration** ([THEORY-232](../theory.d/THEORY-232.md)). Watson measures
  frustration as the energy of the parts at equilibrium and compares
  totals, which is an aggregate. This term is a yes-or-no fact about a
  collection of demands before any total is formed.
- **Not low satisfaction.** [THEORY-052](../theory.d/THEORY-052.md) holds the human case apart in the
  same way: Vansteenkiste, Ryan and Soenens treat need frustration, the
  active thwarting of a need, as distinct from a mere lack of its
  satisfaction. A demand far from met but jointly realizable with the
  others is unmet, not frustrated.
- **Not a dysfunction.** A frustrated collection may be the right outcome
  of genuinely different demands. A33 §2: "A conflict may be the correct
  consequence of optimizing genuinely different objectives."
