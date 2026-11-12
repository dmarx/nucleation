---
number: 347
status: Active
formerly:
- CLAIM-tmp55mls
title: 'Frustration among an organization''s demands is an ordinal fact before it is a quantity: the jointly satisfiable sets of demands form a downward-closed complex whose minimal non-faces are the minimal conflicts, relief is strict enlargement of that complex for the same declared demands, reorganizations that relieve different conflicts are incomparable, and dropping or suppressing a demand is not relief'
version: 4
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
- version: 3
  date: '2026-10-29'
  note: >-
    Promoted at the eighth status review (ADR-057), on the owner's
    assent in the pull request. Its premises CLAIM-368 and TERM-060
    are Active, no objection is filed, and nothing meets the defeater.
    THEORY-232 moved from grounds to corroborated_by (ADR-058): the
    body cites Watson's total-frustration comparison as the measure
    this claim refines, and his criterion of agency does no work here.
    Version 2 said: "Status stays Proposed: the construction is well
    defined, its explanatory role is interpretive." The interpretive
    part is unchanged, and its relation to operative thwarting stays
    QUESTION-131's.
- version: 4
  date: '2026-11-12'
  note: >-
    After the owner's review of #485 on 2026-11-12, the dated note's account
    of CLAIM-662 is corrected to its narrowed form: expanding the
    recognized set cannot improve conjunctive compliance or lower the count
    of recognized violations, not that every score against the recognized
    set can only fall. No status change.
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
complements:
- CLAIM-128
- CLAIM-153
- CLAIM-365
- CLAIM-538
- CLAIM-564
- CLAIM-567
- CLAIM-587
- CLAIM-599
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
---
<!-- inactive-ok-file: NOTE-1793 — Skimmed; the reading filed from the same exchange -->
<!-- inactive-ok-file: CLAIM-662 — Proposed; cited in the note of 2026-11-12 from the exchange of 2026-11-11 -->
<!-- inactive-ok-file: CLAIM-618 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: THEORY-1353 — Proposed or Open; cited from the reading of Dong (2026) as open -->
<!-- inactive-ok-file: THEORY-1761 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

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

## Note of 2026-10-29: promoted

Promoted on [CLAIM-368](CLAIM-368.md) and [TERM-060](../terms.d/TERM-060.md), both Active, with no objection filed.
Watson's comparison ([THEORY-232](../theory.d/THEORY-232.md)) is the measure this claim refines, cited
as corroboration, not as a ground. [CLAIM-449](CLAIM-449.md) objects to [CLAIM-440](CLAIM-440.md)'s use of
the complex, not to this construction.

## Note of 2026-11-04: a horizon example, and the nerve-theorem reading, from "Organizational Nucleation and SLT"

**The horizon index, worked.** The claim indexes the complex to a horizon H
and a budget B. A8's Proposal C, in answer to the owner's U8, gives a
worked case:

- Two specialist capacities x₁, x₂ start at 1.
- They decay as ẋ_i = −x_i + u_i, with u_i ≥ 0 and u₁ + u₂ ≤ 1.
- Each demand requires x_i(t) ≥ 0.75 throughout the horizon.

Summing gives X ≤ 1 + e^{−t}, while both demands need X ≥ 1.5. So "no
admissible maintenance policy can satisfy both demands beyond", at H = ln 2.
The symmetric policy u = ½ attains that bound. The reader checked the
bound and A's plotted points (0.8894, 0.8033, 0.75, 0.6839, 0.6116,
0.5677).

The complex therefore holds the pair {1, 2} as a face for H ≤ ln 2 and
not beyond. A8: "Acquiring a differentiated capacity and acquiring the
capacity to maintain that differentiation are separate developmental
achievements." [CASE-189](../cases.d/CASE-189.md), [CASE-191](../cases.d/CASE-191.md) and [CLAIM-520](CLAIM-520.md) hold the maintenance side.
This example adds only the horizon dependence, so it stays here as a note
and is not filed as a CASE.

**The nerve-theorem reading.** By definition the complex is the nerve of
the cover {ℛ ∩ A_i}. A23 used this: "Because these acceptance regions and
their intersections are convex, they form a *good cover*. The nerve
theorem then tells us that their compatibility complex has the same
homotopy type as their union."

- **The example.** A23's simplex model has T_i = {g_i ≥ 0.4} on Δ². Every
  pair meets and the triple does not, so the complex is ∂Δ² and the union
  is an annulus.
- **The limit, which A23 states.** "Without the good-cover conditions, an
  abstract compatibility complex need not reproduce the topology of the
  underlying allocation space."
- **What the hole means.** "a hole in satisfactory accommodation is not
  necessarily a hole in what the organization can do". The central region
  is reachable. In it, no demand is met.

The reading holds when the acceptance sets within ℛ are closed and
convex. It is new to the record. [CLAIM-365](CLAIM-365.md)'s Helly bound is the
neighbouring convexity fact.

No status changes.

## Note of 2026-11-04: Dong, "The Kinetics of Training", read

Dong (2026; [THEORY-1353](../theory.d/THEORY-1353.md)) is related, not the same construct. Its
all-or-nothing is over the parts of one capability, an AND over attention
heads, not over the joint satisfiability of several demands. Its account
of plasticity loss is a training case of this claim's horizon. On an aged
substrate, a withheld capability and the background skills that have
taken the heads cannot both be met at fixed drive. Rescue by data
"requires c large enough to break the background's own pinning margin",
which in this claim's terms changes a demand rather than relieving the
frustration. A query–key reset reopens the heads and is a candidate for
relief. Whether it counts depends on whether the background skills
survive it, which the paper does not report. No status changes.

## Note of 2026-11-04: Chou, Chua, Teo and Zheng, "Design for Process Flexibility", read

A structural echo that qualifies the claim ([NOTE-1604](../notes.d/NOTE-1604.md)). Adding plant–product links enlarges the set of demand realisations that can be met together, and the long chain is a cheap enlargement close to the full complex. This literature measures the enlargement in expected sales, not ordinally, and its correlated-demand example shows that a sparse enlargement can be worth almost nothing when the demands that matter arrive together. So the ordinal fact depends on which realisations are likely. It leaves open whether the chain's near-completeness has an ordinal statement. No status changes.

## Note of 2026-11-04: Ratliff, Dong, Sekar and Fiez, "A Perspective on Incentive Design", read

Ratliff et al. (2019), [LIT-2097](../literature.d/LIT-2097.md), treat a misalignment between a principal's and an agent's objectives, repaired by changing the agent's payoff, not by enlarging the set of jointly satisfiable demands. That qualifies the claim loosely: incentive design is a different kind of repair from this claim's relief, closer to re-weighting than to enlarging the complex. The paper does not discuss joint feasibility, so whether an incentive change can count as relief is left open. No status changes.

## Note of 2026-11-05: the constraint-architecture readings

Several mechanical readings from the pasted synthesis on constraint architectures bear on the claim, mostly by analogy. Rocks and Mehta ([NOTE-1557](../notes.d/NOTE-1557.md)) call prestress a frustration that "cannot be relaxed away by moving the nodes", and Damavandi et al. ([NOTE-1570](../notes.d/NOTE-1570.md)) separate a self-stress, fixed by geometry, from the load it carries: existence against quantity, as here. Connelly and Whiteley ([NOTE-1588](../notes.d/NOTE-1588.md), read in part) add a cardinal layer beside the complex, not a refinement of it.

Akitaya et al. ([NOTE-1579](../notes.d/NOTE-1579.md)) fit directly: locally feasible vertex modes can admit no jointly consistent assignment, and finding one is NP-hard. In Stern et al. ([NOTE-1571](../notes.d/NOTE-1571.md)) the minimal obstruction is a closed loop of vertices, yet the designed branch is realizable: the target is hard to reach, not empty. Chen and Santangelo ([NOTE-1614](../notes.d/NOTE-1614.md)) and Berry et al. ([NOTE-1605](../notes.d/NOTE-1605.md)) show selection among, and reachability between, jointly feasible configurations, which the complex does not register.

Zang et al. ([NOTE-1569](../notes.d/NOTE-1569.md)) fit relief as strict enlargement only on the record's own reading of 56 ordered transitions as demands: prestress, supplied from outside, opens the 8 blocked ones and removes none, and the 16 needing intermediate states stay unachievable.

No status changes.

## Note of 2026-11-05: A's resource models and further distinctions

[CLAIM-586](CLAIM-586.md) shows that the complex indexed by a resource budget is monotone in the budget and contained in the unbudgeted complex, so raising a budget relieves only sets that are faces of the unbudgeted complex; [CASE-212](../cases.d/CASE-212.md) is a small instance with a hollow triangle no budget fills. [CLAIM-588](CLAIM-588.md) separates relieving a mismatch from redistributing or exploiting it. No status changes.

## Note of 2026-11-05: the resource-bounded realizability readings

Readings filed beside the pasted synthesis on resource-bounded realizability bear on the complex. The reader of Ignatov ([NOTE-1593](../notes.d/NOTE-1593.md), read in part) shows that its faces are the sets of demands with a nonempty extent in the demand–configuration formal context, the non-vacuous part of that context's closure system, so the concept lattice recovers the complex and adds implications among demands; restricted to the configurations affordable at a budget, those implications are antitone in it ([CLAIM-564](CLAIM-564.md)). [THEORY-698](../theory.d/THEORY-698.md)'s warning carries over: such a lattice is "guaranteed by construction" for any incidence, so only its shape informs.

The reading of Gopalan et al. ([NOTE-1584](../notes.d/NOTE-1584.md)) qualifies what the complex can carry. Positive 1-in-3 SAT and positive NAE-3SAT are both NP-complete to satisfy, yet st-connectivity of solutions is polynomial for the first and PSPACE-complete for the second, so an object at the level of joint satisfiability cannot carry the complexity of navigating between solutions. That is the reader's inference, for Boolean languages and single flips. [CLAIM-583](CLAIM-583.md) shows the same within one complex, and [CLAIM-578](CLAIM-578.md) that one organization's complex has no complexity at all. No status changes.

## Note of 2026-11-05: A's synthesis on the productive nucleus

From the third synthesis on DNA origami by another assistant (A), "The productive nucleus", pasted by the owner on 2026-11-05.

A's third synthesis draws an analogy with this claim: "pairwise compatibility need not settle joint compatibility", and "the effects of several candidate interventions need not be determined by their separate effects". The assistant's [CLAIM-599](CLAIM-599.md) marks where the analogy stops. The jointly satisfiable sets are closed downward, so their minimal non-faces describe them. The sets of relations that are productive nuclei are closed in neither direction, since adding a relation can turn a nucleus into a trap.

No status changes.

## Note of 2026-11-07: silencing an oscillator, from "Individuation, Possibility, and Disposition"

A9 §4 of the exchange (2026-11-06 to 07): "Silencing an oscillator is not the same as satisfying its synchronization demand." A cites [CLAIM-549](CLAIM-549.md), rightly. This claim's last clause, that dropping or suppressing a demand is not relief, is the same point, and A did not cite it. A9's "consensus produced by silencing dissent" is an illustration, not a result. [CLAIM-618](CLAIM-618.md), filed from the same exchange, rests on this claim's complex, indexed by a system's control parameters. Supports; no status change.

## Note of 2026-11-07: a product line's admissible feature combinations, from "Individuation, Possibility, and Disposition"

A, at A32 §3 of the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07), defines the admissible feature combinations of a product version, K_v, and says: "When the feature constraints are purely permissive and downward-closed, this is a simplicial complex. With mandatory features and other nonmonotonic configuration requirements, the admissible configurations are better represented directly by a constraint system rather than assuming simplicial structure." That is this claim's complex of jointly satisfiable demands, for a product line. The reader checked it on {offline, e2e, collab} with offline and collab in conflict: the faces are the empty set, the three vertices, {e2e, offline} and {collab, e2e}, so the minimal non-face is the conflict. A's caution about mandatory features is right. A does not cite this claim. No status changes.

## Note of 2026-11-12: the complex and normativity, from "Medical Ethics and Media Enshitification"

The owner asked at U19 of the exchange (2026-11-11) how the discussion
interacts with the compatibility complex. A39 §1 states the definition
accurately and says what it is not: "the compatibility complex is not itself
a moral theory". Its contribution is "to identify the structure of possible
accommodation once the demands and the relevant organization have been
specified". A39's game with three demands, revenue, accessibility and budget
protection, every pair attainable and not the triple, is [CASE-119](../cases.d/CASE-119.md)'s hollow
triangle (note there). A42 §8 turns the specification into a question, filed
as [QUESTION-456](../questions.d/QUESTION-456.md), and [CLAIM-662](CLAIM-662.md) derives from this claim's downward closure that, for a fixed arrangement,
recognizing more demands cannot improve conjunctive compliance or lower the
count of recognized violations (as narrowed after the owner's review of [#485](https://github.com/dmarx/nucleation/issues/485)
on 2026-11-12; not every score against the recognized set falls). No status change.

## Note of 2026-11-12: Fanning & Raworth (2025), read

From the reading in [NOTE-1782](../notes.d/NOTE-1782.md) ([LIT-2454](../literature.d/LIT-2454.md)), the reader's assessment as
checked by the filer: **supports, as an illustration from outside**. The
Doughnut judges each demand against its own acceptance threshold and
declines a common scale between the social and ecological domains ("no
directly traceable link"). It **qualifies** the claim's spirit in one
respect: the paper still summarises across indicators with medians and
interquartile ranges, a cross-indicator aggregate that the claim would treat
as a declared measure, not as frustration itself.

## Note of 2026-11-12: Burke et al. (2025), De-centering the (Traditional) User: Multistakeholder Evaluation of Recommender Systems, read

From the reading in [NOTE-1793](../notes.d/NOTE-1793.md) ([LIT-2400](../literature.d/LIT-2400.md)), the reader's assessment as
checked by the filer: **supports by analogy, independently.** Burke et al.
keep the multi-metric vector as a legitimate end state and allow expert
orderings with incomparable pairs, which is CLAIM-347's point that relief
need not be a quantity and that two reorganizations can be incomparable.
They do not have CLAIM-347's sharp edge: they allow converting metrics to
constraints or weights, and say nothing on comparing systems with different
stakeholder sets (CLAIM-347's "dropping or suppressing a demand is not
relief").

## Note of 2026-11-12: Rockström, Denton, Norström et al., read

From the reading in [NOTE-1796](../notes.d/NOTE-1796.md) ([LIT-2422](../literature.d/LIT-2422.md)), the reader's assessment as
checked by the filer: the recapped result that meeting minimum access for
the poorest "would cause further transgressions" under current inequality is
a case of jointly unsatisfiable demands (floor vs ceiling) for given
conditions, and the Commission's remedy is reorganization (redistribution,
technology), i.e. relief in CLAIM-347's sense, not dropping a demand.
Illustrative only; no ordinal analysis.

## Note of 2026-11-12: Davoudabadi, Makui and Rasouli, read

From the reading in [NOTE-1740](../notes.d/NOTE-1740.md) ([LIT-2429](../literature.d/LIT-2429.md)), the reader's assessment as
checked by the filer: **leaves open; serves at most as a contrast case.**
The model resolves user–organization conflict by a weighted sum whose
weights are set by "flexibility", i.e. by discounting whichever party can
bend. In CLAIM-347's terms that is suppression by weighting, not relief: the
set of jointly satisfiable demands is not enlarged, the user's demand is
down-weighted when the user is judged flexible. The paper offers no ordinal
or complex-based account, and it does not measure whether the steered user
is satisfied. It is an example of the practice the claim distinguishes from
relief, not evidence for or against the claim.

## Note of 2026-11-12: de Kleer and Williams, read

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **de Kleer and Williams** ([THEORY-1761](../theory.d/THEORY-1761.md)): **parallel construction**, not a citation: in both, a downward-closed family is determined by its minimal violating sets.

The claim is unchanged.
