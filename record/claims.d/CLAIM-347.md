---
number: 347
status: Proposed
formerly:
- CLAIM-tmp55mls
title: 'Frustration among an organization''s demands is an ordinal fact before it is a quantity: the jointly satisfiable sets of demands form a downward-closed complex whose minimal non-faces are the minimal conflicts, relief is strict enlargement of that complex for the same declared demands, reorganizations that relieve different conflicts are incomparable, and dropping or suppressing a demand is not relief'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A kind of demand the frustration account needs that has no acceptance
  condition except through a common scale or rate of exchange with other
  demands, so that its frustration cannot be stated as an empty
  intersection of acceptance sets at all: for example, if demands of the
  form "improve as much as possible" cannot be given thresholds without
  importing the cardinal comparison the ordinal form avoids. Not
  defeated by cases where demands are jointly realizable and differ only
  in cost, which are strain (TERM-060), nor by the existence of
  useful cardinal refinements (CLAIM-365).
tags:
- mathematics
- self-governance
- agency
date: '2026-10-18'
line:
- distributed-agency
- will-organization
rests_on:
- CLAIM-368
grounds:
- THEORY-232
complements:
- CLAIM-128
- CLAIM-153
uses:
- TERM-060
summary: >-
  The owner's correction, U37 of the exchange of 2026-10-17: "We can do
  quite a lot with access to an ordering, even if it doesn't give us a
  true measure." A37 granted it ("I agree with your correction") and
  built the acceptance sets, their intersection and the compatibility
  complex. A37's acceptance set {u : u ⪰_i u₀} is corrected here: by
  reflexivity it holds the baseline for every demand and makes every
  collection compatible, so a demand's set is stated as strict
  improvement, a required level or an obligation. The definitional facts are shown in the body, including that
  every pair of demands can be jointly improvable while the triple is
  not. The sharp edge: relief compares complexes for the same declared
  demands, so a reorganization that deletes a demand is not compared at
  all, and two reorganizations can be incomparable. It is the move
  [CLAIM-128](CLAIM-128.md) and [TERM-043](../terms.d/TERM-043.md) made for translation, in a new line.
supports:
- CLAIM-361
- CLAIM-365
---

# CLAIM-347: Frustration among an organization's demands is an ordinal fact before it is a quantity: the jointly satisfiable sets of demands form a downward-closed complex whose minimal non-faces are the minimal conflicts, relief is strict enlargement of that complex for the same declared demands, reorganizations that relieve different conflicts are incomparable, and dropping or suppressing a demand is not relief

<!-- ref::uses-file: TERM-060 — the claim is stated in the ordinal sense of frustration the term fixes -->

## The claim

A36 §2D had said that the cardinal residual of A35 is not defined "if each
process supplies only an ordinal ranking over outcomes". The owner, at
U37: "I think this is why some parts of our research have leaned on the
machinery of posets, lattices, presheafs, etc. We can do quite a lot with
access to an ordering, even if it doesn't give us a true measure." A37:
"I agree with your correction. My earlier discussion treated the absence
of cardinal utilities as primarily a limitation. But for much of our
argument, an ordering is sufficient, and sometimes it is the more
appropriate structure."

**The construction (A37 §4, corrected).** Let U be the organization's
admissible transformations, ⪰_i a preorder for demand i, and A_i ⊆ U
the transformations that meet demand i's requirement. A37 wrote the
acceptance set as A_i = {u ∈ U : u ⪰_i u₀} for a reference u₀ "(or its
strict version)". As the primary definition that is wrong. If u₀ is
admissible, reflexivity puts u₀ in every A_i, so ⋂ A_i ⊇ {u₀} ≠ ∅ and
every collection of demands is trivially compatible. A demand is a
requirement, so its acceptance set must be able to exclude the
unmodified baseline when change is demanded. The owner pointed this out
in review of the filing (workbench entries of 2026-10-18). The admissible
forms are those of [TERM-060](../terms.d/TERM-060.md): strict improvement, A_i = {u : u ≻_i u₀};
a required level, A_i = {u : u ⪰_i t_i}, which holds u₀ only if u₀ already
meets t_i; or a context-indexed obligation given directly. Weak Pareto
improvement on u₀ (every demand ⪰_i u₀, at least one ≻_i u₀) is a
condition on the collection, not an intersection of per-demand sets, so
it falls outside this construction. The worked examples below use strict
or threshold sets throughout. The demands are jointly satisfiable when
⋂ A_i ≠ ∅. The compatibility complex of a demand set I is

  𝒦 = {S ⊆ I : ⋂_{i∈S} A_i ≠ ∅},

with the empty intersection read as U.

**Relief (A37 §4C).** For the same declared demands I and the same
acceptance conditions, a reorganization relieves frustration when
𝒦_before ⊊ 𝒦_after. A37: "If the system simply deletes a difficult demand,
it has changed the comparison problem rather than shown an expansion of
its ability to realize the original demands." And: "two reorganizations
may relieve different conflicts, with neither compatibility complex
containing the other. They would be incomparable rather than ranked by a
universal success metric." Suppressing a demand's evidence, or lowering its
weight, leaves its A_i where it was, so it leaves 𝒦 unchanged; it is not
relief (A35 §4: "suppression, not necessarily resolution").

The claim is that this is the basic form of frustration and of its relief,
and that scalar measures are refinements of it ([CLAIM-365](CLAIM-365.md)), not
definitions.

## The definitional facts

These follow from the definitions and are checked here.

1. **𝒦 is downward closed.** If S ∈ 𝒦 and T ⊆ S, then ⋂_T A_i ⊇ ⋂_S A_i ≠
   ∅. So, when U ≠ ∅, 𝒦 is an abstract simplicial complex on the
   individually satisfiable demands.
2. **Its minimal non-faces are the minimal conflicts.** A set S ∉ 𝒦 all of
   whose proper subsets are in 𝒦 is a collection that is jointly
   unsatisfiable while no smaller collection explains it. By downward
   closure, every jointly unsatisfiable set contains one.
3. **Pairwise compatibility does not give joint compatibility.** A37's
   example: three binary variables with the demands a = b, b = c, c ≠ a.
   Each pair is satisfiable, the triple is not. The same holds for local
   improvement demands on a learner, which is the point G5 worked and
   A33–A37 did not make. Take three unit gradients at 120° in a plane,
   g₁, g₂, g₃ with g₁ + g₂ + g₃ = 0, and A_i = {d : g_iᵀd < 0}. Any two
   are not antiparallel, so −(g_i + g_j) lowers both: g_iᵀ(−g_i − g_j) =
   −1 + ½ < 0. All three cannot be lowered at once, since Σ g_iᵀd = 0 for
   every d. So 𝒦 is the boundary of a triangle, and the minimal conflict
   has three members.
4. **Pairwise non-conflict does rule frustration out.** If every
   g_iᵀg_j ≥ 0 and no g_i is zero, then |Σλ_i g_i|² ≥ Σλ_i²|g_i|² > 0 for
   every λ in the simplex, so 0 ∉ conv{g_i} and a common descent direction
   exists ([CLAIM-366](CLAIM-366.md)). With nonzero demands, a minimal conflict of
   two is an antiparallel pair. Among non-antiparallel demands the
   minimal obstruction needs three, which is [CLAIM-153](CLAIM-153.md)'s "the minimal
   model of the obstruction needs three" in the update setting. For
   convex acceptance sets in ℝᵖ, Helly's theorem bounds it above by p + 1
   ([CLAIM-365](CLAIM-365.md)).

The claim's interpretive part is the rest: that these sets are the right
representation of an organization's demands, that "relief" should mean
enlargement for fixed demands, and that the comparison should be left
partial.

## Later versions of the same construction

- **Indexed to an organization, horizon and budget.** A38 §2:
  𝒦(𝒪_t; D₀, H, B) = {S ⊆ D₀ : ℛ(𝒪_t; H, B) ∩ ⋂_{i∈S} A_i ≠ ∅}, where ℛ
  is what organization 𝒪_t can attain within horizon H and budget B. In
  A38's words, the possibilities "belong to a particular organization
  with a particular developmental history". Fixing D₀ across time, and saying what
  happens to a demand when the organization changes, is
  [CLAIM-361](CLAIM-361.md)'s, not this claim's.
- **Robust to compromised constituents.** A41 §5 defines 𝒦_f^rob(𝒪), the
  sets S for which one admissible policy meets every demand in S against
  every allowed insider behaviour. It is the same complex with a ∃∀
  condition in place of ∃.
- **A flexibility order.** A42 orders governance policies by inclusion of
  the contexts in which they respond acceptably: π₁ ⪰_flex π₂ iff
  ℛ(π₂) ⊆ ℛ(π₁). It is the same inclusion construction, applied to
  contexts instead of demands.

## Relations

- **[CLAIM-128](CLAIM-128.md) and [TERM-043](../terms.d/TERM-043.md).** Translations whose distortion profiles trade
  off are incomparable until a task fixes weights. This claim is the same
  move for organizations: a partial order by inclusion, a scalar only
  once weights are fixed.
- **[CLAIM-153](CLAIM-153.md).** The contextual version has torsors and a cycle class,
  which plain set incompatibility does not supply. A39: "ordinary set
  incompatibility doesn't automatically supply the torsors, transition
  maps, or cohomological obstruction used there."
- **[THEORY-232](../theory.d/THEORY-232.md).** Watson compares the parts' total frustration under two
  organizations. Inclusion of complexes refines that comparison: it does
  not credit an organization that lowers the total by sacrificing a
  demand, and it leaves two organizations unranked when each relieves a
  conflict the other does not.
- **A37 §5 on Arrow.** The unanimity relation ⋂⪰_i of preorders is a
  preorder, so the organization's evaluative state can be kept partial and
  selection of one action treated as a separate governance step.

## What it does not say

- **That cardinal measures are useless.** A37: "We need cardinal
  quantities only when we want to distinguish how far one outcome is from
  another, how much improvement is required, or what resources a
  transformation costs."
- **That a partial order chooses.** A37: weakening the output to a partial
  order "does not eliminate the practical problem of selecting an action
  when alternatives remain incomparable".
- **That demands have acceptance conditions.** A37: "It does require each
  demand to have a well-defined acceptance condition." Where they have
  none, the construction does not apply, which is the defeater.
- **That every revision of a demand is a failure.** Constitutive revision
  may be legitimate transformation (A38). It is simply not relief of the
  original demands.
