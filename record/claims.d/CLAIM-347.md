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
    The construction restated on attainable outcomes ℛ(𝒪), with improvement,
    maintenance and threshold demands distinguished. A weak-preference
    set is a legitimate maintenance demand; the earlier correction that
    such a set is never a demand is withdrawn. Structural frustration is
    defined as joint infeasibility, S ∉ 𝒦; relief is strict enlargement of
    𝒦 under fixed reference demands, losing no compatible collection. The
    organizational interpretation, structural frustration against
    operative thwarting, is left to QUESTION-131. At the reviews
    relayed by the owner on 2026-10-18. Status stays Proposed: the
    construction is well defined, its explanatory role is interpretive.
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
  complex. Corrected here: acceptance conditions sit on attainable
  outcomes, a demand's form depends on whether it demands improvement or
  maintenance, and A37's weak-preference sets fail only as representations
  of improvement demands. The definitional facts are shown in the body, including that
  every pair of demands can be jointly improvable while the triple is
  not. The sharp edge: relief compares complexes for the same declared
  demands, so a reorganization that deletes a demand is not compared at
  all, and two reorganizations can be incomparable. It is the move
  [CLAIM-128](CLAIM-128.md) and [TERM-043](../terms.d/TERM-043.md) made for translation, in a new line.
supports:
- CLAIM-361
- CLAIM-365
- CLAIM-tmpz8lli
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

**The construction (A37 §4, corrected).** Let 𝒪 be the organization,
ℛ(𝒪) the outcomes or histories its admissible policies can produce, and
A_i the outcomes that meet demand i's requirement. Demands are conditions
on outcomes; what is attainable belongs to the organization. So the same
demands can be compared when the organization's policy space changes
([CLAIM-361](CLAIM-361.md) is the claim that relies on this).

How A_i is specified depends on what the demand is.

- **An improvement demand** on a reference y₀ is A_i = {y : y ≻_i y₀}.
  Strict improvement may be impossible at an optimum, and then the demand
  is unmet there.
- **A maintenance demand**, "do not let this fall below its present
  level", is A_i = {y : y ⪰_i y₀}. The reference meets it, which is what a
  successfully maintained requirement should do. If every demand in a
  collection is of this form, the baseline meeting all of them is not a
  defect. It means those requirements are compatible.
- **A threshold or obligation**, A_i = {y : y ⪰_i t_i} or a set given
  directly, may or may not hold the reference.

A preference is not a demand. That a more preferred outcome exists does
not show that the present one fails a requirement.

The construction was corrected twice in review of the filing (workbench
entries of 2026-10-18). The defect in A37's version, A_i = {u : u ⪰_i
u₀} "(or its strict version)", was that it represented demands for
improvement by weak-preference sets. Those cannot exclude the unchanged
baseline, so improvement demands came out trivially compatible. The
first correction overstated this, as if a weak-preference set could never
be a demand. That is wrong for maintenance demands, as above. Weak Pareto
improvement on y₀ (every demand ⪰_i y₀, at least one ≻_i y₀) is a
condition on the collection, not an intersection of per-demand sets, so
it falls outside this construction. The worked examples below are
improvement demands with strict or threshold sets.

A set S of demands is **jointly realizable** when
ℛ(𝒪) ∩ ⋂_{i∈S} A_i ≠ ∅. That is a fact about what can be attained.
Whether the outcome the organization actually produces meets them is a
separate fact. The compatibility complex is the first:

  𝒦(𝒪; D) = {S ⊆ D : ℛ(𝒪) ∩ ⋂_{i∈S} A_i ≠ ∅},

with the empty intersection read as ℛ(𝒪). Its minimal non-faces are
minimal incompatibilities. The incompatibility belongs to the collection,
not to any one member. If A₁ = {a}, A₂ = {b}, a ≠ b, and the organization
can attain either but not both, each demand is individually realizable
and the pair is not; which one goes unmet depends on what the
organization does. In the local model of a learner the attainable set is
the set of admissible updates d, and the improvement demands are
{d : g_iᵀd < 0} or {d : −g_iᵀd ≥ ε_i}, ε_i > 0. The facts below are
stated with 𝒦 written as {S : ⋂_S A_i ≠ ∅}, the A_i read as the
attainable points that meet each demand.

**Structural frustration is defined by joint infeasibility.** Given an
organization 𝒪, a reference collection of demands D and its
compatibility complex 𝒦(𝒪; D), a collection S ⊆ D is structurally
frustrated exactly when S ∉ 𝒦(𝒪; D): no outcome attainable under the
specified constraints satisfies every demand in S simultaneously. With a
horizon H and a budget B made explicit:

  F_struct(𝒪, S; H, B)  iff  ℛ(𝒪; H, B) ∩ ⋂_{i∈S} A_i = ∅.

This is a relational property of a collection of demands, relative to an
organization, a horizon and an admissible set of transformations. It
does not require cardinal utilities, experienced distress, or an
identifiable process actively interfering with another. Minimal non-faces
of 𝒦 identify the minimal structurally frustrated collections.

The formal criterion is settled by the stated definitions. What remains
open is its broader organizational interpretation ([QUESTION-131](../questions.d/QUESTION-131.md)):
when structural incompatibility shows up as operative resistance or
thwarting, whether operative thwarting can occur without structural
incompatibility, and what evidence is needed to attribute either
condition to a particular organizational bearer. In particular, merely
failing to realize a jointly attainable set of requirements establishes
neither structural frustration nor operative thwarting.

**Relief (A37 §4C).** Relief of structural frustration is strict
enlargement of the compatibility complex under fixed reference demands
and acceptance conditions: 𝒦_before ⊊ 𝒦_after, so that at least one
previously frustrated collection becomes jointly realizable and no
previously compatible collection is lost. A37: "If the system simply deletes a difficult demand,
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
