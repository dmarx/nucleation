---
status: Proposed
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
- CLAIM-142
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

# CLAIM-tmp82c4f: Whether two systems compute the same way can be tested by quotienting the full admissible symmetry group and measuring what remains: a residual barrier marks a different mechanism, and a feature with no counterpart blocks the comparison

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
  what the probes cannot see they cannot separate ([CLAIM-tmppqir6](CLAIM-tmppqir6.md)).
