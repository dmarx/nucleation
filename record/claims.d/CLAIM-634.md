---
number: 634
status: Proposed
formerly:
- CLAIM-tmp9hy40
title: 'For demands that two contexts'' local values differ by a preferred real offset within a tolerance, the minimal sets of demands that cannot be met together are exactly the simple cycles of contexts whose holonomy exceeds their summed tolerance: without parallel overlaps every pair of demands is compatible, a minimal conflict can have any length from three to the number of contexts, Helly''s bound on its size is attained by a cycle through every context, and in this class a missing face of the compatibility complex is a failed global assignment'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a finite graph of contexts with real offsets
  and tolerances δ_e ≥ 0 in which some set of overlap demands is jointly
  unsatisfiable and contains no simple cycle whose holonomy exceeds its
  summed tolerance; or a simple cycle whose holonomy exceeds its summed
  tolerance and some proper subset of whose overlaps is jointly
  unsatisfiable. Or a premise it needs failing: CLAIM-538's cycle
  criterion failing for a graph that is not connected. Also defeated as a
  claim of its own if an entry already states that the minimal non-faces
  of this class are its violating cycles. Not defeated by demands outside
  the class, such as circle-valued offsets or acceptance sets that are not
  intervals in the offset, for which CLAIM-538's disclaimer stands.
tags:
- mathematics
- behavioral-integration
date: '2026-11-11'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-538
- CLAIM-347
complements:
- CLAIM-365
- CLAIM-153
summary: >-
  [CLAIM-538](CLAIM-538.md) gives the cycle criterion for tolerances on the overlaps of a
  graph of contexts, and lists among what it does not say "That a minimal
  non-face of [CLAIM-347](CLAIM-347.md)'s complex is a cycle obstruction." For [CLAIM-538](CLAIM-538.md)'s
  own demands the link holds exactly: applying its criterion to every set
  of overlaps, a set is jointly unsatisfiable exactly when it contains a
  simple cycle whose holonomy exceeds the cycle's summed tolerance, and
  since a cycle less one overlap is a forest, the minimal non-faces of
  [CLAIM-347](CLAIM-347.md)'s complex over the overlaps are those cycles. So pairs never
  conflict without parallel overlaps, as in [CLAIM-153](CLAIM-153.md); minimal conflicts
  run from three members to one per context, attaining the Helly bound
  [CLAIM-365](CLAIM-365.md) applies; and in this class a missing face is a failed global
  assignment, where the record's general caution keeps the two apart.
  Found at the synthesis review of the distributed-agency line's
  frustration part (2026-11-11) and checked by script. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-075 ADR-084 — Proposed; the test this claim passes and the decision that sends it here -->
<!-- inactive-ok-file: CLAIM-618 CLAIM-631 — Proposed; cited for what this claim does not cover -->

# CLAIM-634: For demands that two contexts' local values differ by a preferred real offset within a tolerance, the minimal sets of demands that cannot be met together are exactly the simple cycles of contexts whose holonomy exceeds their summed tolerance: without parallel overlaps every pair of demands is compatible, a minimal conflict can have any length from three to the number of contexts, Helly's bound on its size is attained by a cycle through every context, and in this class a missing face of the compatibility complex is a failed global assignment

## The claim

Take [CLAIM-538](CLAIM-538.md)'s setting: contexts are the vertices of a finite graph,
each context sets a local value x_v, and each overlap e = (u, v) carries a
demand that the values differ by a preferred real offset a_e within a
tolerance δ_e ≥ 0, A_e = {x : |x_v − x_u − a_e| ≤ δ_e}. These are [TERM-060](../terms.d/TERM-060.md)'s
threshold demands in additive form, as [CLAIM-538](CLAIM-538.md) reads them. [CLAIM-347](CLAIM-347.md)'s
complex over the overlaps is 𝒦 = {S : ⋂_{e∈S} A_e ≠ ∅}. For a simple cycle
C, write hol_C(a) for the signed sum of offsets around it and δ(C) for
Σ_{e∈C} δ_e; C *violates* when |hol_C(a)| > δ(C).

**The minimal non-faces of 𝒦 are exactly the violating simple cycles.**

## Derivation

1. **Faces.** A set S of overlaps is a face of 𝒦 when some x meets every
   demand in S. The demands in S constrain only the subgraph (V, S), and
   its components share no demand, so S is a face exactly when each
   component admits an assignment. By [CLAIM-538](CLAIM-538.md)'s cycle criterion, applied
   to each component, that holds exactly when no simple cycle in (V, S)
   violates.
2. **Non-faces.** So S ∉ 𝒦 exactly when S contains a violating simple
   cycle.
3. **A violating cycle is minimal.** A violating simple cycle C is a
   non-face by step 2. Removing any overlap from C leaves a path, which
   contains no cycle, so every proper subset of C is a face ([CLAIM-538](CLAIM-538.md): "on
   a forest it always holds"). So C is a minimal non-face.
4. **A minimal non-face is a violating cycle.** If S is a minimal non-face,
   it contains a violating simple cycle C by step 2, and C is a non-face,
   so C = S by minimality.

## What follows

- **Pairs are compatible.** In a graph without parallel overlaps, two
  overlaps never form a cycle, so every pair of demands is a face, and a
  minimal conflict has at least three members: [CLAIM-153](CLAIM-153.md)'s "minimal model
  of the obstruction needs three", and [CLAIM-347](CLAIM-347.md)'s fact 3, here for
  tolerances. Two overlaps between the same pair of contexts form a cycle
  of length two, the one way a pair conflicts.
- **Every length occurs.** A minimal conflict can have any length from
  three to the number n of contexts, since any simple cycle can be made to
  violate by its offsets.
- **Helly's bound is attained.** Each A_e is a closed convex slab in ℝⁿ,
  and all are invariant under adding a constant to every x_v, so the
  problem lives in ℝⁿ⁻¹. The bound [CLAIM-365](CLAIM-365.md) applies, at most p + 1
  members with p = n − 1, is n, and a violating cycle through every
  context has n members.
- **A missing face is a failed global assignment, in this class.** The
  record keeps joint infeasibility apart from the failure of local
  descriptions to glue in general ([CLAIM-347](CLAIM-347.md)'s relation to [CLAIM-153](CLAIM-153.md);
  [QUESTION-255](../questions.d/QUESTION-255.md)'s note that "infeasible demands and failure of a global
  section are different mathematical facts"). For overlap demands with
  real offsets and tolerances the two coincide: a set of demands is a
  non-face exactly when no global assignment meets them, and its minimal
  witnesses are [CLAIM-538](CLAIM-538.md)'s certifying cycles.
- **No overlap is singled out.** Every overlap of a minimal conflict is in
  it, so the incompatibility belongs to the cycle, as [QUESTION-131](../questions.d/QUESTION-131.md) says of
  collections in general; [CLAIM-538](CLAIM-538.md)'s frontier allocation decides where the
  mismatch falls.

## Admission

Admitted under [ADR-075](../decisions.d/ADR-075.md)'s derived route, as [ADR-084](../decisions.d/ADR-084.md) applies it to a claim
whose premises are claims: a valid inference from [CLAIM-538](CLAIM-538.md) and [CLAIM-347](CLAIM-347.md)
that no entry holds. [CLAIM-538](CLAIM-538.md)'s omission clause comes nearest, saying
that deleting one overlap of every witnessing cycle makes the evaluated
graph compatible; it does not identify the witnessing cycles with the
minimal non-faces, and the claim disclaims "That a minimal non-face of
[CLAIM-347](CLAIM-347.md)'s complex is a cycle obstruction." That disclaimer stands for
[CLAIM-347](CLAIM-347.md)'s complex in general; this claim holds the link for [CLAIM-538](CLAIM-538.md)'s
class only.

**Checked by script** (the reviewer's, 2026-11-11): 400 random instances
of three to six contexts and up to nine overlaps, a fifth with a parallel
overlap, offsets uniform on [−1, 1] and tolerances either 0 or uniform on
[0, 0.6], instances with a cycle within 10⁻⁶ of the bound dropped. The
faces were found by Bellman–Ford on the difference constraints, which does
not enumerate cycles, for every set of overlaps; the minimal non-faces
were compared with the violating simple cycles found by enumeration. No
mismatch. Minimal non-faces of 2 (parallel overlaps only), 3, 4, 5 and 6
members occurred, 810 in all.

No separating case is offered: a derivation has none relative to its
premises.

## What it does not say

- **Anything about circle-valued offsets.** [CLAIM-153](CLAIM-153.md) and [CLAIM-618](CLAIM-618.md) are on
  S¹, where winding enters and the convex test does not transfer.
- **Anything about acceptance sets that are not intervals in the offset.**
  [CLAIM-552](CLAIM-552.md)'s directed criteria need not be ("Not a ball around i's own
  output").
- **That [CLAIM-347](CLAIM-347.md)'s minimal non-faces are cycles in general.** [CASE-119](../cases.d/CASE-119.md)'s
  three demands and [CLAIM-347](CLAIM-347.md)'s 120° gradients are minimal conflicts with
  no graph of contexts.
- **That a minimal conflict is thwarting.** [CLAIM-631](CLAIM-631.md) and [QUESTION-131](../questions.d/QUESTION-131.md).
