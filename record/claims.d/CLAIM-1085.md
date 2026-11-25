---
number: 1085
status: Proposed
formerly:
- CLAIM-tmpeno57
title: 'Seed findings reappear out of sample'
statement: >-
  In a kinetic constraint-growth system unlike self-folding sheets, adding a
  seed already in its target state to a seed set can roughly halve the
  chance of exact assembly although the larger set is still compatible with
  the target, and coverage by the seeds' islands predicts that chance better
  than the number of seeds, so both of the self-folding sheets' findings on
  where intervention sits reappear out of sample
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23 from the executed study
    CASE-389.
role: thesis
warrant: empirical
defeated_if: >-
  An error in the code or the analysis of CASE-389; or a rerun of its
  model in which, with at least 3000 runs per set, the confirmed decreases
  vanish (no addition of a target-state seed lowers V by more than its
  sampling error), or the number of seeds ranks seed sets as well as island
  coverage does. Not defeated by systems in which adding seeds always helps,
  nor by the observation that the harmful seeds have large islands rather
  than the small ones of Stern et al.'s example, both of which the claim
  allows.
tags:
- complex-systems
- probabilistic-modeling
- natural-sciences
date: '2026-11-23'
line:
- realizability
- formal-apparatus
grounds:
- CASE-389
corroborates:
- CLAIM-562
- CLAIM-599
uses:
- TERM-117
bears_on:
- QUESTION-380
summary: >-
  [CLAIM-562](CLAIM-562.md) holds, from Stern, Pinson and Murugan's self-folding sheets,
  that where an intervention acts predicts success better than how much
  there is, and that adding one can make a successful set fail. In a kinetic
  constraint-growth model of another kind ([CASE-389](../cases.d/CASE-389.md)), 38 of 40
  significant decreases from adding a target-state seed are confirmed with
  3000 runs, typically halving the chance of exact assembly, and island
  coverage outranks the seed count (Spearman 0.54 against 0.14, and 0.48
  against 0.26 on fresh architectures). Every set is compatible with the
  target, so [CLAIM-599](CLAIM-599.md)'s upward non-closure arises here without an
  incompatibility built in. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-389 — new; the executed study this claim is grounded in, filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CASE-374 — Proposed; the earlier assembly study, cited for contrast -->

# CLAIM-1085: Seed findings reappear out of sample

## The claim

[CASE-389](../cases.d/CASE-389.md) grows a random constraint architecture on an 8 × 8 lattice
in the threshold-2 regime of the kinetic tile assembly model, from seed
sets established in their target states, and estimates V(S), the chance of
exact assembly. Two things hold there.

1. **More can be worse.** Adding one target-state seed lowered V
   significantly in 40 of the additions tested; rerun with 3000 runs, 38 are
   confirmed at z < −2, on the sensitivity architectures with a median fall
   of 0.07 (for example from 0.16 to 0.07). Each larger set is still
   compatible with the target: nothing in the architecture forbids the
   target it lowers the chance of. In [TERM-117](../terms.d/TERM-117.md)'s sense, the added seed is
   not productive relative to the smaller set.
2. **Placement beats count.** Coverage by the seeds' islands ranks seed
   sets by V far better than their number (Spearman 0.54 against 0.14 on
   five architectures; 0.48 against 0.26 on five fresh ones).

## What it adds

[CLAIM-562](CLAIM-562.md)'s two findings come from one 4 × 4 crease pattern; [CLAIM-599](CLAIM-599.md)
draws the general point, that productive sets need not be closed upward,
from them and a stipulated table. [CASE-374](../cases.d/CASE-374.md) showed two seams combining into
a trap, but there the pair is incompatible by construction. Here both
findings recur in a system with different physics (stochastic attachment
with a binding threshold, not energy descent with torques), with every set
compatible with the target.

## What it does not say

- That the harm has the sheets' mechanism. The harmful seeds here have
  large islands; the errors are order effects at the binding threshold
  ([CASE-389](../cases.d/CASE-389.md), "Why").
- That adding seeds usually hurts. Most additions help or do nothing; V
  rises on average.
- Anything about DNA origami, whose rates the model does not take.
