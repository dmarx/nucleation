---
status: Proposed
title: 'Structural frustration of a set of demands forces, under every attainable arrangement, some member whose demand is unmet while it acts toward it, the precondition of operative thwarting, exactly when no attainable arrangement leaves each member either met or quiet; lying outside both the requirement complex and the quiescent complex does not suffice, the requirement complex is the test when every member acts whenever its demand is unmet, and in a minimal such conflict each member is the unmet, acting one under some arrangement and none is under all'
version: 1
history:
- version: 1
  date: '2026-11-08'
  note: >-
    Filed at the decision that a SYNTHESIS is an account (ADR-tmp72iro),
    as its demonstration: SYNTHESIS-008, version 1, was a derived
    result, one claim, and returns to CLAIM under a code of its own.
    Title, body, defeater, role, warrant, lines and bears_on are the
    synthesis's; its premises are `rests_on`; its standing, Proposed, is
    kept.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: attainable arrangements, acceptance sets and
  quiet regions for which a set outside the met-or-quiet complex has an
  arrangement leaving no member both unmet and acting, or a set inside it
  has none; or a minimal non-face of two or more members one of which is
  unmet and acting under every arrangement. Or a premise it needs failing:
  a reading of operative thwarting the record adopts on which a
  constituent's demand can be thwarted while it does not act toward it, as
  in self-determination theory's environmental thwarting. Also defeated as
  a claim of its own if it only restates CLAIM-347's compatibility
  complex, CLAIM-549's quiescent complex and QUESTION-131's two-demand
  example, adding no criterion beyond them. Not defeated by an unmet,
  acting member that no countervailing process blocks: it gives a
  necessary condition of thwarting, not thwarting.
tags:
- mathematics
- self-governance
- agency
date: '2026-11-08'

# REQUIRED: the line or lines of inquiry, from `lines` in luria.yaml. The
# claims index is grouped by it, and the `argument` chain reports a
# `rests_on` step that crosses from one line to another (ADR-032). A general
# result that rests on no claim may also hold `formal-apparatus`, so that
# setting its first line aside does not retire it (ADR-040).
line:
- distributed-agency
- formal-apparatus
- will-organization
rests_on:
- CLAIM-347
- CLAIM-549
bears_on:
- QUESTION-131
summary: >-
  QUESTION-131 asks when structural frustration among jointly incompatible
  demands shows up as operative thwarting, and which member is thwarted.
  Thwarting needs a member that acts toward its demand while the demand
  goes unmet. Putting CLAIM-347's requirement complex beside CLAIM-549's
  quiescent complex shows that neither decides when frustration forces
  such a member. A third complex decides it: the sets that some attainable
  arrangement leaves each member met or quiet. The result is derived and
  checked exhaustively on small instances. It is a necessary condition of
  thwarting, not an identification of thwarting, which still needs the
  causal evidence CLAIM-357 and QUESTION-131 ask for. Filed at the
  synthesis review of 2026-11-07 (ADR-078). The integration's wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: ADR-075 ADR-078 — Proposed; the audit applied and the review that filed this entry -->
<!-- inactive-ok-file: CLAIM-553 — Proposed, the owner's; used only for the scalar corollary -->

# CLAIM-tmpt8x7l: Structural frustration of a set of demands forces, under every attainable arrangement, some member whose demand is unmet while it acts toward it, the precondition of operative thwarting, exactly when no attainable arrangement leaves each member either met or quiet; lying outside both the requirement complex and the quiescent complex does not suffice, the requirement complex is the test when every member acts whenever its demand is unmet, and in a minimal such conflict each member is the unmet, acting one under some arrangement and none is under all

*Returned to CLAIM from SYNTHESIS-008 on 2026-11-08 (ADR-tmp72iro). The notes below that speak of a synthesis are the synthesis's own.*

*Filed at the synthesis review of 2026-11-07 (ADR-078) as an opportunity: QUESTION-131 had several in-force answers and no entry stating what they add up to.*

## The integration

Operative thwarting needs a member whose demand is unmet while it acts
toward it. QUESTION-131 puts it as "a process acts to meet its requirement
and another blocks or overrides it", and CLAIM-554 as a constituent whose
"attempted realization is causally blocked". Whether structural frustration
forces such a member is decided by neither of the record's two complexes,
but by a third.

- **CLAIM-347** (Active; the owner's correction at U37, built by A37) gives
  the requirement complex 𝒦: the sets of demands some attainable
  arrangement r ∈ ℛ meets jointly, r ∈ Aᵢ for every member. Structural
  frustration of S is S ∉ 𝒦. Premise.
- **CLAIM-549** (Active, demonstrated; A's, sharpened by the reader) gives
  the quiescent complex 𝒬, and says "a perspective can be quiet while its
  requirement is unmet and active while it is met". Here Tᵢ is the region
  where member i does not act toward its demand: the owner's U17
  intervention threshold, which CLAIM-553 (Proposed, the owner's) separates
  from activation. Premise.
- **CLAIM-357** (Active; A's) gives realized violation inside 𝒦, and the
  caution that neither of its measures identifies "an obstructing
  mechanism, a governance failure or active thwarting".
- **CLAIM-554** (Active) gives the table of relations that come apart.
- **CLAIM-586** (Active, demonstrated): everything below holds at any
  budget b, taking ℛ as the arrangements affordable at b.
- **CLAIM-361** and **CLAIM-368** (Active), the fixed reference set and
  strain, are untouched.

**Definition.** The met-or-quiet complex 𝓛 is the set of S such that some
r ∈ ℛ lies in Aᵢ ∪ Tᵢ for every i ∈ S. A member is unmet and acting at r
exactly when r ∉ Aᵢ ∪ Tᵢ.

## Admission

Admitted under ADR-075's derived route: a valid, nontrivial inference from
the components that no entry holds. The reader's script checked items 1 to
5 exhaustively on 20,000 random instances (three members, up to four
arrangements, 2,404 minimal non-faces) and the scalar corollary on 5,000
more; all passed. The filer checked each step by hand.

1. 𝓛 is a complex (closed under subsets) and contains 𝒦 ∪ 𝒬, since
   Aᵢ ⊆ Aᵢ ∪ Tᵢ and Tᵢ ⊆ Aᵢ ∪ Tᵢ.
2. Every attainable arrangement leaves some member of S unmet and acting
   exactly when S ∉ 𝓛.
3. **Lying outside both 𝒦 and 𝒬 is not enough.** Take ℛ = {x, y},
   A₁ = {x}, A₂ = {y}, T₁ = {y}, T₂ = {x}. Then {1, 2} ∉ 𝒦 and
   {1, 2} ∉ 𝒬, but {1, 2} ∈ 𝓛: at x, member 1 is met and member 2 is
   unmet and quiet.
4. **When each complex is the test.** If every member acts whenever its
   demand is unmet (Tᵢ ⊆ Aᵢ on ℛ), 𝓛 agrees with 𝒦, and S ∉ 𝒦 forces an
   unmet, acting member. If every member is quiet whenever met
   (Aᵢ ⊆ Tᵢ), 𝓛 = 𝒬. In CLAIM-553's scalar form, Aᵢ = {dᵢ ≤ τᵢ^acc} and
   Tᵢ = {dᵢ ≤ τᵢ^int}, so 𝓛 is the requirement complex at the tolerances
   max(τᵢ^acc, τᵢ^int). The band τᵢ^acc < dᵢ ≤ τᵢ^int, where a demand is
   unmet and quiet, can hide a structural frustration completely.
5. **Which member.** Let S be a minimal non-face of 𝓛 with |S| ≥ 2. Since
   S∖{i} ∈ 𝓛, some arrangement leaves every other member met or quiet, and
   since S ∉ 𝓛, i is unmet and acting there. Since {i} ∈ 𝓛, i is not unmet
   and acting under every arrangement. This carries QUESTION-131's "An
   incompatibility can obstruct joint satisfaction without singling out any
   demand as the obstructed one" from unmet demands to demands that are
   unmet and acted on.
6. Conversely, S ∈ 𝒦 does not exclude an unmet, acting member: that is
   CLAIM-357's realized violation with the member acting. So the
   precondition can occur where joint satisfaction is possible.

Items 1, 2 and 4 are close to definitional once 𝓛 is written down: 𝓛 is
CLAIM-347's construction applied to Aᵢ ∪ Tᵢ. What is not held anywhere, and
makes the inference nontrivial, is that this union, and neither component's
complex, is the one operative thwarting needs: item 3 refutes the natural
guess, item 4 says when the guess is right and names the band that hides
frustration, and item 5 answers "which member" for acted-on demands.

## What it does not say

- **That an unmet, acting member is thwarted.** Thwarting also needs, in
  QUESTION-131's words, an identified constraint or "countervailing
  mechanism, ideally shown by counterfactual intervention".
- **That acting is observed.** In CLAIM-553, observation also needs a
  channel.
- **Which Tᵢ to use** beyond what the definition of thwarting fixes. The
  criterion holds for any Tᵢ, so Tᵢ is a declared input, not a free
  parameter adjusted case by case.
- **That a frustration hidden in the unmet-and-quiet band has been
  relieved.** It has only gone unvoiced (CLAIM-549, CLAIM-361).
