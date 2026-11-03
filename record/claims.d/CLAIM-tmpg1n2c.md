---
status: Active
title: 'An organization that acts on what it observes has a policy acceptable in every circumstance exactly when, for each observation, the circumstances it cannot tell apart share an acceptable action; so every circumstance having an acceptable action does not give a policy, a finer observation never removes one, and where acceptable actions overlap the coarsest observations that suffice are several and incomparable, so which distinctions must be made legible depends on which acceptable action the organization commits to'
version: 1
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
- CLAIM-tmpkogzd
bears_on:
- QUESTION-285
- QUESTION-133
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
<!-- inactive-ok-file: CLAIM-354 CLAIM-523 — Proposed, Open or new; cited as open -->

# CLAIM-tmpg1n2c: An organization that acts on what it observes has a policy acceptable in every circumstance exactly when, for each observation, the circumstances it cannot tell apart share an acceptable action; so every circumstance having an acceptable action does not give a policy, a finer observation never removes one, and where acceptable actions overlap the coarsest observations that suffice are several and incomparable, so which distinctions must be made legible depends on which acceptable action the organization commits to

## The claim

Circumstances w ∈ W, an observation map h: W → O, and for each w a set A(w) of
acceptable actions. A policy π: O → actions is acceptable everywhere when
π(h(w)) ∈ A(w) for every w.

- **Criterion.** Such a π exists exactly when ∩_{w ∈ h⁻¹(o)} A(w) ≠ ∅ for every
  o. If each such intersection is nonempty, pick π(o) in it. If one is empty,
  any π(o) fails some w in that class.
- **Possibility is not enough.** A(w) ≠ ∅ for every w does not give a policy,
  as in [CLAIM-tmpkogzd](CLAIM-tmpkogzd.md)'s triangle.
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
