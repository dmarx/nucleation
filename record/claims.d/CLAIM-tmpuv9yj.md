---
status: Proposed
title: 'Because establishing more relations can lower the chance of forming a target, the sets of relations that are productive nuclei need not be closed upward: two productive nuclei can combine into a trap, so the minimal productive sets describe the productive ones only where adding relations never hurts'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a proof that for every assembly the value
  V(S) = Pr(τ_F ≤ T | do(S)) is non-decreasing in the set S of established
  relations; or an assembly in which V is monotone and some superset of a
  set reaching the threshold falls below it. Not defeated by assemblies in
  which V happens to be monotone, which the claim allows.
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-11-05'
line:
- realizability
- formal-apparatus
uses:
- TERM-tmp3awsy
rests_on:
- CLAIM-562
complements:
- CLAIM-tmpiyvk1
- CLAIM-347
bears_on:
- QUESTION-380
summary: >-
  The assistant's, on A's third synthesis on DNA origami, pasted by the
  owner on 2026-11-05, §5. A defines a minimal productive nucleating set:
  a set S of established relations with Δ_S ≥ η, no proper subset reaching
  η, and possibly several incomparable ones. The productive sets are then
  described by these minimal ones only if V is monotone, that is, if
  establishing more relations never lowers the chance of the target. The
  record already holds that it can (CLAIM-562, from Stern, Pinson and
  Murugan's actuators), and in DNA origami Dunn et al.'s early long-range
  seams trap the fold.
  With V(∅) = 0.2, V({a}) = V({b}) = 0.6 and V({a, b}) = 0.1, two productive
  nuclei combine into a trap. The productive sets therefore form no
  complex of either kind, unlike [CLAIM-347](CLAIM-347.md)'s jointly satisfiable sets,
  which are closed downward. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-562 CLAIM-tmpiyvk1 TERM-tmp3awsy — Proposed, Skimmed or new; entries cited as open -->

# CLAIM-tmpuv9yj: Because establishing more relations can lower the chance of forming a target, the sets of relations that are productive nuclei need not be closed upward: two productive nuclei can combine into a trap, so the minimal productive sets describe the productive ones only where adding relations never hurts

## The claim

Let R be the relations that can be established and V(S) the chance of
reaching the target by the horizon after establishing S ⊆ R. Call S
productive at threshold η when V(S) − V(∅) ≥ η (A's Δ_S ≥ η against
establishing nothing).

1. **If V is monotone, minimal sets suffice.** If S ⊆ S′ implies
   V(S) ≤ V(S′), the productive sets are closed upward. Every productive
   set contains a minimal one, and every set containing a minimal one is
   productive. A's minimal productive nucleating sets, an antichain,
   describe them all.
2. **V need not be monotone.** A relation can be productive alone and
   harmful in company. Take V(∅) = 0.2, V({a}) = V({b}) = 0.6 and
   V({a, b}) = 0.1, with η = 0.3. Then {a} and {b} are minimal productive
   sets and {a, b}, which contains both, is a trap. This is the shape of
   two nuclei for incompatible folds.
3. **So the productive sets form no complex.** They are not closed upward
   (point 2). They are not closed downward either, since a productive set's
   subsets include ∅, which is not productive. A family with neither
   closure is not determined by its minimal members, and finding the
   productive sets needs V on more than the minimal ones.

## What is demonstrated and what is evidence

The demonstration is the numerical example in point 2, which suffices to
refute upward closure. The readings are evidence for the mechanism, not
for that factorial proposition. Dunn et al. ([NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md)) show that
long-range seam staples that bind early and "effectively, irreversibly"
force particular folds and trap others, and that weakening the seams
helps. That is competing early commitment. They do not test two
separately productive nuclei established together. Majikes et al. 2026
([NOTE-tmppwpd0](../notes.d/NOTE-tmppwpd0.md)) found that replacing medium folds with more short ones
raised defects, again a design change and not a factorial test of nuclei.

## What it adds

- **Beyond [CLAIM-562](CLAIM-562.md),** which holds the non-monotonicity itself, from
  mechanical origami: this claim draws what follows for A's minimal
  nucleating sets, and that productive sets have no closure. The
  assistant's first filing missed [CLAIM-562](CLAIM-562.md), and this version rests on it.

- **To A's minimal nuclei** ([TERM-tmp3awsy](../terms.d/TERM-tmp3awsy.md)): they suffice only under a
  monotonicity that assembly often lacks.
- **Beside [CLAIM-347](CLAIM-347.md):** pairwise compatibility does not settle joint
  compatibility, and the jointly satisfiable sets are closed downward.
  Productivity does not combine either, and its sets have no closure at
  all.
- **To [CLAIM-tmpiyvk1](CLAIM-tmpiyvk1.md):** a nucleus is target-relative and context-relative.
  So whether a set is a nucleus depends on what else is
  established.

## What it does not say

- **That nucleation in organizations is non-monotone.** Whether adding
  relations to an organizational core can lower its chance of forming
  needs a model of its own.
