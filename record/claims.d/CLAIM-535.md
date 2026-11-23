---
number: 535
status: Active
formerly:
- CLAIM-tmpg1n2c
title: 'An organization that acts on what it observes has a policy acceptable in every circumstance exactly when, for each observation, the circumstances it cannot tell apart share an acceptable action; so every circumstance having an acceptable action does not give a policy, a finer observation never removes one, and where acceptable actions overlap the coarsest observations that suffice are several and incomparable, so which distinctions must be made legible depends on which acceptable action the organization commits to'
version: 5
history:
- version: 2
  date: '2026-11-10'
  note: >-
    Carries distributed-agency as well, at the sweep of ADR-085's
    rule (2026-11-10): the entry takes part in that line's argument,
    through the first line of an entry it names: distributed-agency,
    since it bears on QUESTION-285, bears on QUESTION-133. No other
    change.
- version: 3
  date: '2026-11-11'
  note: >-
    A dated note corrects the note of 2026-11-04, which calls CLAIM-559
    Proposed; it has been Active since 2026-11-06. Found at the
    synthesis review of the formal-apparatus line. No other change.
- version: 4
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-097, from the reading review of 2026-11-11, by
    question. The question asks when a distinction an organized agent
    can observe corresponds to an intervention it can perform. The
    claim states a condition joining them: a policy acceptable in
    every circumstance exists "exactly when, for each observation, the
    circumstances it cannot tell apart share an acceptable action", so
    "which distinctions must be made legible depends on which
    acceptable action the organization commits to". It already carries
    the question's line. No other change.
- version: 5
  date: '2026-11-17'
  note: >-
    A dated note: A106 §7 of the exchange "Assess Depp Heard Abuse"
    re-derives the claim's disjoint case as a "formal obstruction"
    without citing it, and the filer adds the bound for randomized
    policies, checked. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An observation map and acceptable sets for which a policy acceptable in
  every circumstance exists while some observation's circumstances share
  no acceptable action, or the converse; or overlapping acceptable sets
  for which the coarsest sufficient observation is unique in every case.
tags:
- agency
- information-theory
date: '2026-11-03'
line:
- will-organization
- formal-apparatus
- distributed-agency
- learning-and-inquiry
rests_on:
- CLAIM-350
grounds:
- THEORY-1096
uses:
- TERM-064
complements:
- CLAIM-523
- CLAIM-354
- CLAIM-152
- CLAIM-537
- CLAIM-559
bears_on:
- QUESTION-285
- QUESTION-133
- QUESTION-097
summary: >-
  A33 §4 of the exchange "Assess SDT Coverage" (2026-11-02), at the
  owner's U33 request for positive accounts, with A30 §2's example and
  A32's Claim B. Its second appearance in the exchange, so it gets a code.
  The criterion is elementary, and its monotonicity is Blackwell's easy
  direction ([THEORY-1096](../theory.d/THEORY-1096.md)). What it adds to [CLAIM-350](CLAIM-350.md), its single-valued
  case, is found by the reader of U32–U33: with overlapping acceptable
  sets, legibility is relative to policy. A positive characterization of
  what legibility must supply for action.
---
<!-- inactive-ok-file: ARG-060 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-620 — filed from the same exchange, Proposed -->

# CLAIM-535: An organization that acts on what it observes has a policy acceptable in every circumstance exactly when, for each observation, the circumstances it cannot tell apart share an acceptable action; so every circumstance having an acceptable action does not give a policy, a finer observation never removes one, and where acceptable actions overlap the coarsest observations that suffice are several and incomparable, so which distinctions must be made legible depends on which acceptable action the organization commits to

## The claim

Circumstances w ∈ W, an observation map h: W → O, and for each w a set A(w) of
acceptable actions. A policy π: O → actions is acceptable everywhere when
π(h(w)) ∈ A(w) for every w.

- **Criterion.** Such a π exists exactly when ∩_{w ∈ h⁻¹(o)} A(w) ≠ ∅ for every
  o. If each such intersection is nonempty, pick π(o) in it. If one is empty,
  any π(o) fails some w in that class.
- **Possibility is not enough.** A(w) ≠ ∅ for every w does not give a policy,
  as in [CLAIM-537](CLAIM-537.md)'s triangle.
- **Refinement.** If h = g ∘ h′, any policy π for h gives π ∘ g for h′, so a
  finer observation never removes an acceptable policy (Blackwell's easy
  direction, [THEORY-1096](../theory.d/THEORY-1096.md)).
- **Policy-relativity.** With W = {1, 2, 3}, A(1) = {a}, A(2) = {a, b},
  A(3) = {b}, the partitions {1, 2} | {3} and {1} | {2, 3} both suffice, neither
  refines the other, and the trivial partition does not. So there is no unique
  coarsest sufficient observation. Which distinctions the organization must
  make legible depends on which acceptable action it commits to where it has
  a choice. [CLAIM-350](CLAIM-350.md)'s unique coarsest partition is the case with one
  acceptable action per circumstance.

So legibility, in [TERM-064](../terms.d/TERM-064.md)'s sense, has a positive job here: to make legible
the distinctions that separate circumstances with no common acceptable
action, under the policy the organization adopts.

## What it does not say

- **Anything about memory, the cost of observing, or limits on action.** One
  step only. A32's "bounded actuation" half is unproved and not filed.
- **That the acceptable sets are the right ones.**
- **That choosing what to observe under cost is covered.** That is active
  sensing and dual control (Feldbaum), not registered because its citation
  could not be checked.

## Note of 2026-11-04: Guigues, Kleywegt and Nascimento, "Policies for the Operation of an Ambulance Fleet", read

Ambulance selection in their policies ([LIT-2066](../literature.d/LIT-2066.md)) acts on the emergency type as the dispatcher classifies it: one dispatch policy whose observation is coarser than the circumstances, which qualifies the claim by analogy. It does not test the claim. No status changes.

## Note of 2026-11-04: U.S. Fire Administration, "Dispatched and Canceled en Route", read

The page's Scenario 2 ([LIT-2084](../literature.d/LIT-2084.md)) dispatches "Based on information provided by dispatch" and cancels two units once the first-arriving engine finds a false alarm: a coarse observation refined, which supports the claim by analogy. The page does not say whether the initial dispatch was acceptable in every circumstance consistent with the call. No status changes.

## Note of 2026-11-04: Ratliff, Dong, Sekar and Fiez, "A Perspective on Incentive Design", read

The moral-hazard case Ratliff et al. (2019), [LIT-2097](../literature.d/LIT-2097.md), review is a principal who "is unable to observe the action u ∈ U chosen by the agent" (p. 10) and must condition incentives on a coarser signal. This claim is the same observation-limited design problem without a strategic agent, so it is the natural baseline, and the reading qualifies it there. The paper does not say how strategic response changes which distinctions must be made legible. No status changes.

## Note of 2026-11-04: observations that arrive in sequence

A's [CLAIM-559](CLAIM-559.md) (Proposed) carries this claim to two stages: as the first unit's report arrives, the acceptable action changes from dispatch to cancel under one objective, so a reversal is not by itself evidence of error. The claim is unchanged.

## Note of 2026-11-07: what follows for will and for perspectives, from the second share of "Individuation, Possibility, and Disposition"

A57 reads this claim rightly: "the **distinctions needed for adequate action depend on which acceptable policy is chosen**". A58 §3 adds that the theorem "doesn't justify those sets, and whoever controls that standard can influence which distinctions the organization is required to recognize". That is this claim's "That the acceptable sets are the right ones" joined to [TERM-064](../terms.d/TERM-064.md)'s caution on the loss and [CLAIM-404](CLAIM-404.md)'s evaluative route. A58 §8's route of changing what the organization can do is [CLAIM-572](CLAIM-572.md)'s hedge, and it is open only where a hedge exists ([ARG-060](../arguments.d/ARG-060.md)). Two consequences are filed: for comparing perspectives, [CLAIM-622](CLAIM-622.md); for the synthesis of meaning, perspective and will, layer 6 of [CLAIM-620](CLAIM-620.md), version 2. The claim is unchanged.

**Note (2026-11-11).** The note of 2026-11-04 above calls [CLAIM-559](CLAIM-559.md)
Proposed; it has been Active since the status review of 2026-11-06.

## Note of 2026-11-17: the disjoint case re-derived as a formal obstruction, with a bound for randomized policies, from "Assess Depp Heard Abuse"

A106 §7 of the exchange "Assess Depp Heard Abuse" (https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b, 2026-11-17) states "A minimal impossibility result": if Λ(s₀) = Λ(s₁) and R_N(s₀) ∩ R_N(s₁) = ∅, no deterministic policy acting on Λ alone selects a permitted response in both states. That is this claim's criterion in the case of one observation class whose acceptable sets are disjoint. A presents it as derived "from Nucleation's legibility research" and cites [CLAIM-523](CLAIM-523.md), not this claim, which already gives the general condition. A's caption states the assumptions correctly ("a common observation-dependent deterministic decision rule, with no additional information or action that distinguishes the states").

Two additions. First, A's moral reading, which the claim's text does not draw: "**no amount of sincere commitment to those requirements can guarantee appropriate conduct under those informational constraints**", so "better institutional motivation is not always an adequate remedy". With A's qualification: "Not every failure of discrimination is wrongful", and "The independent normative question is which distinctions an institution has sufficient responsibility to acquire and preserve." Second, a bound A does not state, which supports A105's "reliably": a randomized policy assigns one distribution p over actions to the shared observation, so its success probabilities in the two states are p(R_N(s₀)) and p(R_N(s₁)); the sets are disjoint, so the two sum to at most 1 and the worse is at most 1/2, attained by a fair mixture of one action from each set. The claim's "acceptable in every circumstance" is the deterministic case; for randomized policies the disjoint case caps worst-case reliability at 1/2. Checked by the filer (Claude, in this session).

No status changes.

## Note of 2026-11-22: the reverse swipe, from the exchange "Explain First Contact RL"
<!-- inactive-ok-file: CASE-419 — Proposed; filed 2026-11-22 from the exchange "Explain First Contact RL" -->

A8 §3A of that exchange applies this claim to an adaptive scroll interface
([CASE-419](../cases.d/CASE-419.md), which illustrates it): a quick reverse swipe can mean
overshoot, deliberate rereading or searching back, circumstances the
interface cannot tell apart from the gesture and that call for different
adjustments (more friction, or none). "The system cannot solve missing
information merely by making its classifier more sophisticated." A's
conclusion is to keep the interface task-agnostic and learn from patterns
over many gestures rather than decode intent per gesture, which is this
claim's lesson that the coarsest sufficient observation depends on the
action committed to: an interface committed to adjusting only physics
needs no distinction among the three intents. No status change.
