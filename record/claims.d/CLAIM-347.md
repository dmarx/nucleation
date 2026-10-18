---
number: 347
status: Proposed
formerly:
- CLAIM-tmp55mls
title: 'Frustration among an organization''s demands is an ordinal fact before it is a quantity: the jointly satisfiable sets of demands form a downward-closed complex whose minimal non-faces are the minimal conflicts, relief is strict enlargement of that complex for the same declared demands, reorganizations that relieve different conflicts are incomparable, and dropping or suppressing a demand is not relief'
version: 2
history:
- version: 2
  date: '2026-10-18'
  note: >-
    Acceptance conditions restated on outcomes, with structural compatibility kept apart from actual satisfaction and maintenance demands no longer forced into strict improvement, at the owner's third review. uses moves to TERM-tmp9p3s9, which supersedes TERM-060.
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
  in cost, which are strain (TERM-tmp9p3s9), nor by the existence of
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
- TERM-tmp9p3s9
summary: >-
  The owner's correction, U37 of the exchange of 2026-10-17: "We can do
  quite a lot with access to an ordering, even if it doesn't give us a
  true measure." A37 granted it ("I agree with your correction") and
  built the acceptance sets, their intersection and the compatibility
  complex. A37's acceptance set {u : u ⪰_i u₀} is corrected here: by
  reflexivity it holds the baseline for every demand and makes every
  collection compatible. Demands are stated on outcomes, in whatever form
  the demand takes, improvement only for improvement demands. The definitional facts are shown in the body, including that
  every pair of demands can be jointly improvable while the triple is
  not. The sharp edge: relief compares complexes for the same declared
  demands, so a reorganization that deletes a demand is not compared at
  all, and two reorganizations can be incomparable. It is the move
  [CLAIM-128](CLAIM-128.md) and [TERM-043](../terms.d/TERM-043.md) made for translation, in a new line.
supports:
- CLAIM-361
- CLAIM-365
---
<!-- inactive-ok-file: TERM-060 — Superseded; named in the version 2 history as the term this claim moved from -->

# CLAIM-347: Frustration among an organization's demands is an ordinal fact before it is a quantity: the jointly satisfiable sets of demands form a downward-closed complex whose minimal non-faces are the minimal conflicts, relief is strict enlargement of that complex for the same declared demands, reorganizations that relieve different conflicts are incomparable, and dropping or suppressing a demand is not relief

<!-- ref::uses-file: TERM-tmp9p3s9 — the claim is stated in the ordinal sense of frustration the term fixes -->

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

**The construction (A37 §4, corrected twice).** Let 𝒪 be the
organization, Π_𝒪 its admissible policies or transformations, and
Y_𝒪(π) the outcome or history a policy produces. Each demand i has an
acceptance condition A_i on outcomes: the outcomes that meet what i
requires. Demands live on outcomes; the available transformations belong
to the organization. That is what lets the same demands be compared
when the organization's policy space changes ([CLAIM-361](CLAIM-361.md)).

How A_i is specified is the demand's own business. A demand for
improvement on a reference y₀ is A_i = {y : y ≻_i y₀}. A maintenance
demand is a threshold or standing condition, A_i = {y : y ⪰_i t_i} or an
obligation given directly, which the present outcome may already meet. A
process that demands only maintenance is satisfied at an optimum, and
writing its demand as strict improvement would wrongly make it
frustrated there. A preference is not a demand: that a more preferred
outcome exists does not show that the present one fails a requirement
([TERM-tmp9p3s9](../terms.d/TERM-tmp9p3s9.md)).

Two corrections were made in review of the filing (workbench entries of
2026-10-18). First, A37 wrote the acceptance set as {u : u ⪰_i u₀} "(or
its strict version)". Taken as a demand that is wrong: by reflexivity
the reference meets every such condition, ⋂ A_i always holds it, and
every collection is trivially compatible. Second, the first correction
made strict improvement a canonical form. It is the right form only for
demands that are demands for improvement. Weak Pareto improvement (every
demand ⪰_i y₀, at least one ≻_i y₀) is a condition on the collection,
not an intersection of per-demand sets, so it falls outside this
construction. The worked examples below are improvement demands, with
strict or threshold sets throughout.

A set S of demands is **structurally compatible** when some admissible
policy meets them all, ∃ π ∈ Π_𝒪 with Y_𝒪(π) ∈ ⋂_{i∈S} A_i. That is a
modal fact. It is distinct from **actual satisfaction**,
Y_𝒪(π_actual) ∈ ⋂ A_i, which concerns what happened ([TERM-tmp9p3s9](../terms.d/TERM-tmp9p3s9.md)). The
compatibility complex is the structural notion:

  𝒦(𝒪) = {S ⊆ I : ∃ π ∈ Π_𝒪, Y_𝒪(π) ∈ ⋂_{i∈S} A_i},

with the empty intersection read as all outcomes. In the local model of
a learner the policy is the update d and the acceptance conditions are
read off it directly, A_i = {d : g_iᵀd < 0} or {d : −g_iᵀd ≥ ε_i} with
ε_i > 0. The facts below are stated for 𝒦 written as {S : ⋂_S A_i ≠ ∅},
with the A_i understood as the policies whose outcomes meet each demand.

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
