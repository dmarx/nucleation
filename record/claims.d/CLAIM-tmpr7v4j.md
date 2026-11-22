---
status: Proposed
title: 'In small ReLU networks the barrier that survives alignment is set by width, by the group quotiented and by the path family, and does not sort pairs by the input cue they rely on'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-157 as a delegated
    lead worker, from the executed study CASE-tmphfmrb.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of the same design (a cue-reliance test that uses no barrier,
  pairs that share and that differ in the cue relied on, alignment over
  the full group, several path families) at greater width or depth, or on
  a real task, finds that the aligned barrier separates same-cue from
  different-cue pairs at a fixed width, with same-cue pairs connected
  wherever alignment can be searched exactly; or the toy's own result
  turns out to be an artefact of its probe set, the barrier separating
  the pairs once it is measured on inputs where the two cues disagree.
tags:
- loss-landscapes
- representation-learning
date: '2026-11-22'
line:
- learned-structure
grounds:
- CASE-tmphfmrb
bears_on:
- QUESTION-069
summary: >-
  What [CASE-tmphfmrb](../cases.d/CASE-tmphfmrb.md) measured, stated as a finding. In two-hidden-layer
  ReLU MLPs on a two-cue task, the barrier left after alignment falls with
  width for every kind of pair. At width 5, pairs that rely on the same
  cue keep barriers (0 to 0.65 in loss) that overlap those of pairs relying
  on different cues (0.15 to 0.54), even after an exhaustive search over
  permutations and rescalings. From width 64, both kinds are connected.
  Within a width, the barrier falls as the matched units' activations
  correlate more. Permutations alone leave a barrier between two copies
  of one function that differ by per-unit rescaling, and quotienting
  rescaling removes it. A trained curve joins aligned endpoints that the
  straight line does not, both across the board and in the one flat,
  poorly connected cell of a load-by-temperature grid, where the accuracy
  deficit stays. So in this toy, connectedness after alignment is a
  property of width, of the symmetry group and of the path family, more
  than of the mechanism. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmphfmrb CLAIM-tmpv22hv CLAIM-tmp46m6e — new; the study this rests on and the two readings filed with it -->
<!-- inactive-ok-file: CLAIM-263 THEORY-108 — Proposed; the claim and the reading this finding tests, open -->

# CLAIM-tmpr7v4j: In small ReLU networks the barrier that survives alignment is set by width, by the group quotiented and by the path family, and does not sort pairs by the input cue they rely on

## The claim

In [CASE-tmphfmrb](../cases.d/CASE-tmphfmrb.md)'s toy, four things set the barrier left between two
trained networks:

1. **Width.** For every kind of pair (two nets relying on cue A, two on cue
   B, two on both cues, or one on A and one on B), the best
   permutation-aligned linear barrier falls with width. From width 64 it
   is zero for all of them.
2. **Feature correspondence.** Within width 5, the pairs whose matched
   units correlate least keep the largest barrier, whichever cue they rely
   on.
3. **The group.** Two copies of one function, rescaled per unit, keep a
   barrier of 0.19 to 0.59 under permutations alone, and none once
   rescaling is quotiented. [CLAIM-263](CLAIM-263.md)'s step 1, "the group must be the full
   one", holds for ReLU MLPs as it holds for transformers ([THEORY-112](../theory.d/THEORY-112.md)).
4. **The path family.** A trained Bezier curve or polychain joins aligned
   endpoints, same cue or not, from width 8. The straight line does not.
   In the load-by-temperature grid's one flat, poorly connected cell,
   alignment plus a curve removes the barrier while the aligned line
   keeps 0.07 error, and the cell's accuracy deficit stays.

None of these sorts the pairs by the cue they rely on, as measured by a
test that uses no barrier.

## What it answers in part

[QUESTION-069](../questions.d/QUESTION-069.md) asks whether the connectedness of trained solutions belongs
to the solutions, or to the path family, the history and the regime. In
this toy it belongs to width (capacity), to the group quotiented and to
the path family. The cue relied on matters less. That is evidence for the
question's alternatives, at a scale far from [THEORY-108](../theory.d/THEORY-108.md)'s or
[THEORY-112](../theory.d/THEORY-112.md)'s.

## What it does not say

- It does not say the same holds for convolutional networks, transformers
  or real data. The defeater names the rerun that would test it.
- It does not decide what the result does to [CLAIM-263](CLAIM-263.md). That depends on
  what "share a mechanism" means there, and the two readings are filed
  as alternatives: [CLAIM-tmpv22hv](CLAIM-tmpv22hv.md) (defeated) and [CLAIM-tmp46m6e](CLAIM-tmp46m6e.md) (narrowed
  to preconditions).
- It measures barriers on inputs where the two cues agree. A probe on
  which they conflict was not run.
