---
number: 187
status: Proposed
formerly:
- CLAIM-tmp82c4f
title: 'Whether two systems compute the same way can be tested by quotienting the full admissible symmetry group and measuring what remains: a residual barrier marks a different mechanism, and a feature with no counterpart blocks the comparison'
version: 1
role: thesis
defeated_if: >-
  Systems that share a mechanism, by an independent test, are found
  separated by a barrier that survives full symmetry alignment, or
  systems that do not share one are found connected after alignment. Or
  the protocol cannot be posed for communicative kinds because no
  admissible group or path can be defined on their realizations.
tags:
- representation-learning
- loss-landscapes
date: '2026-10-12'
line: pragmatic-transport
rests_on:
- CLAIM-263
- CLAIM-264
grounds:
- THEORY-112
- THEORY-116
- THEORY-111
- THEORY-113
- THEORY-115
summary: >-
  The record's one fully measured case of "factor out the admissible
  symmetries, then test what survives", which the pragmatic-transport
  line's questions about invariants under admissible transformation
  ([QUESTION-027](../questions.d/QUESTION-027.md), [QUESTION-029](../questions.d/QUESTION-029.md), [QUESTION-036](../questions.d/QUESTION-036.md)) ask for in the abstract.
  From five mode-connectivity THEORYs held without links to the line. The
  carry-over from trained networks to communicative kinds is the
  filer's, and is the claim's weak point.
---
<!-- inactive-ok-file: CLAIM-263 CLAIM-264 — Proposed; the general forms of this claim's premises, filed under ADR-040, open -->

# CLAIM-187: Whether two systems compute the same way can be tested by quotienting the full admissible symmetry group and measuring what remains: a residual barrier marks a different mechanism, and a feature with no counterpart blocks the comparison

## The claim

The pragmatic-transport line asks, in several forms, what is invariant
under admissible transformations and whether a kind can be identified by
it ([QUESTION-027](../questions.d/QUESTION-027.md), [QUESTION-029](../questions.d/QUESTION-029.md), [QUESTION-036](../questions.d/QUESTION-036.md)). The mode-connectivity
results the record holds are a worked protocol for exactly that, measured:

1. **Quotient the full group.** Once the architecture's symmetries are
   factored out, most of the linear barrier between independently trained
   solutions disappears. The group must be the full one: for transformers
   it includes an orthogonal map on the residual stream, "without which a
   barrier remains" ([THEORY-112](../theory.d/THEORY-112.md)).
2. **Read the residue.** A barrier that survives the removal of
   symmetries "marks a difference in the input attributes the two models
   rely on: they compute by different mechanisms" ([THEORY-116](../theory.d/THEORY-116.md)).
3. **Inside a basin, structure interpolates.** Along a low-loss path every
   layer's features interpolate the endpoints' ([THEORY-111](../theory.d/THEORY-111.md)), so
   connectedness after alignment is sameness of feature structure.
4. **Know when the test cannot run.** Merging fails "where their features
   have no counterpart in the other model" ([THEORY-113](../theory.d/THEORY-113.md)), and connectivity
   holds only when the objectives share structure ([THEORY-115](../theory.d/THEORY-115.md)).

Read across, two communicative realizations would count as the same kind
when, after quotienting the admissible transformations, they are connected
with no residual barrier on the probes that matter. A residual barrier
would be the invariant that separates kinds. A realization with no
counterpart, [CLAIM-129](CLAIM-129.md)'s topic kept while the act is lost, is the case
where the comparison cannot be made, not one where it fails.

## What it does not say

- It does not say communicative kinds have a loss landscape. The protocol
  needs an admissible group, a path between realizations and a measure
  along it. Whether these can be defined for communicative realizations is
  open, and it is the first defeater.
- It does not answer [QUESTION-027](../questions.d/QUESTION-027.md) or [QUESTION-036](../questions.d/QUESTION-036.md). It gives them a template
  with measured examples.
- It inherits [CLAIM-142](CLAIM-142.md)'s caution. A barrier is measured on probes, and
  what the probes cannot see they cannot separate ([CLAIM-193](CLAIM-193.md)).

## Note of 2026-10-12: a case for the protocol

[THEORY-108](../theory.d/THEORY-108.md)'s phase III is a ready case for this protocol. Independently trained solutions there are poorly connected on a fitted curve, and [THEORY-108](../theory.d/THEORY-108.md) itself asks whether the barrier survives permutation alignment. If it does, the protocol reads phase III as a different mechanism from the connected phases, which [THEORY-108](../theory.d/THEORY-108.md)'s accuracy and output-similarity differences would corroborate. If it does not, the barrier was a symmetry the curve family failed to quotient. Notes on [THEORY-108](../theory.d/THEORY-108.md) and [THEORY-109](../theory.d/THEORY-109.md) record the tension this would settle.

## Note of 2026-10-12: an assessed result on the first defeater

"What it does not say" leaves open whether an admissible group can be
defined for communicative realizations. PR [#121](https://github.com/dmarx/nucleation/issues/121)'s [CLAIM-249](CLAIM-249.md), granted
and Active, assesses that point: "The transformations the line studies are
not group elements", and among stochastic maps on finite observation
spaces the invertible core is the relabellings. So the group "has to be a
symmetry group of the situation that the analyst chooses", with its action
on each medium specified independently, and [TERM-008](../terms.d/TERM-008.md)'s transport is
directed and need not be invertible. That does not show no group can be
posed; it says the group is chosen, not read off the realizations.
[CASE-057](../cases.d/CASE-057.md) is a ready case: a swap of the two persons of a dyad, a
group of order 2, which [CLAIM-249](CLAIM-249.md) notes has no automorphism to move
its characters.

## Note of 2026-10-13: the protocol is filed separately, and the premise re-pointed

Under [ADR-040](../decisions.d/ADR-040.md) the protocol for trained networks is filed on its own as
[CLAIM-263](CLAIM-263.md), the first claim in the learned-structure line, and this
claim now rests on it. What stays here is the carry-over to communicative
realizations, which the summary already calls the claim's weak point. The
claim also needed only the relativity of observational equivalence to
probes, so its `rests_on` names [CLAIM-264](CLAIM-264.md), the general form, in place
of [CLAIM-142](CLAIM-142.md). The body's citation of [CLAIM-142](CLAIM-142.md) stands.
