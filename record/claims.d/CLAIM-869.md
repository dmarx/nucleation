---
number: 869
status: Proposed
formerly:
- CLAIM-tmp3twn6
title: 'Block test misses the Life block'
statement: >-
  Read as sensitivity to one flipped cell, the coupling inside a Game of
  Life block is zero at every horizon while a single birth on its border
  destroys it, so the gap-isolated block test does not pick out the block,
  alone or in the gun; the property that keeps the block in being, its
  cells' tolerance of one another's loss, is what reads as no coupling
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A correct rerun of the computation that finds, for the lone block, a
  single flip of one of its cells changing another of its cells at some
  horizon, or inside coupling at least equal to its border's; or a
  reading of the interaction a gap test compares, for a Boolean rule,
  that is better than sensitivity to single flips and gives the block an
  inside coupling larger than its border's. A different threshold does
  not count, since the inside coupling is zero.
tags:
- individuation
- complex-systems
- mathematics
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-311
bears_on:
- QUESTION-035
- QUESTION-281
summary: >-
  From [LEAD-069](../leads.d/LEAD-069.md)'s study. [CLAIM-157](CLAIM-157.md) names a form one system when the
  coupling inside it beats the coupling across its edge by more than an
  Occam threshold. In Life, read as the fraction of cell pairs for which
  flipping one changes the other k generations later, the lone block has
  inside coupling 0 at k = 1, 2, 5 and 10, and 0.42 to 0.75 from its
  border. In Gosper's gun, over a period, it has 0.06 inside and 0.38 from
  the border. The eater's inside coupling beats its border's at one
  generation (0.24 against 0.07) and not at five. The block's members are
  coupled so that each tolerates the loss of any one other and the lost
  cell regrows, so a single deletion changes nothing a generation later.
  It is one measured case of the kind [CLAIM-157](CLAIM-157.md)'s defeated_if names, a
  form whose members compensate that does not clear the test. One case in
  a discrete rule is not the systematic failure that clause asks for. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-311 CLAIM-871 CLAIM-870 — new; the study this claim reports and the two readings filed with it -->
<!-- inactive-ok-file: CLAIM-157 — Proposed; the criterion tested and the constructions it is tested on -->

# CLAIM-869: Block test misses the Life block

## The claim

[CLAIM-157](CLAIM-157.md)'s test compares interaction inside a candidate block with
interaction across its edge. Life is a Boolean rule with no interaction
matrix, so the nearest reading is sensitivity. Flip cell j, run k
generations, and ask whether cell i differs from the unflipped run. Over
the block's four cells and its twelve-cell border ([CASE-311](../cases.d/CASE-311.md)):

| | inside | border to block | block to border |
|---|---|---|---|
| lone block, k = 1 | 0 | 0.42 | 0 |
| lone block, k = 2 | 0 | 0.58 | 0 |
| lone block, k = 5, 10 | 0 | 0.75 | 0 |
| block in Gosper's gun, k = 1, one period | 0.06 | 0.38 | 0.02 |

So the block is not a gap-isolated block for any threshold. Its border
reaches it and its own cells do not reach one another.

**Why.** Each block cell has exactly three live neighbours, the other
three. Delete one, and each remaining cell keeps two and survives, while
the deleted cell has three and is reborn. A generation later the lattice
is as it was, so the deletion has changed nothing anywhere. A birth on the
edge-adjacent border gives two block cells four neighbours, and they die.
The coupling that makes each cell's survival depend on the others is
redundant, and redundancy makes a single loss invisible. A sensitivity
reading of coupling therefore reads a form that repairs itself as
uncoupled inside.

**The eater.** Its inside coupling, 0.24 at one generation, beats its
border's, 0.07, by about 3.5 times, and by five generations the two are
equal (0.52 against 0.55). It clears the test at one generation if the
Occam threshold is below about 3.5, a threshold Life does not set, and not
at longer horizons. Its seven cells do not repair one another: none of its
single deletions returns, which is why a deletion shows up.

## What it bears on

- **[CLAIM-157](CLAIM-157.md)'s `defeated_if`.** It names "forms that do compensate and
  entrain but never clear" the threshold. The block's cells compensate:
  any three restore the fourth. It does not clear the test. That is one
  measured case of that kind, in a formal rule, with coupling read one
  way. The clause asks for systematic cases for the same target. Whether
  this case counts, or shows only that sensitivity is the wrong reading of
  coupling for a self-repairing form, is the owner's to judge.
- **[QUESTION-281](../questions.d/QUESTION-281.md).** If its "a form the record individuates" means
  [CLAIM-157](CLAIM-157.md)'s one system, this is why the block does not meet it
  ([CLAIM-870](CLAIM-870.md)).

## What it does not say

- **That the block is not an individual.** [TERM-088](../terms.d/TERM-088.md)'s other senses give
  other verdicts ([CLAIM-871](CLAIM-871.md)).
- **That no reading of coupling isolates it.** A model of a coarse
  variable, such as whether a block is present, is not built here.
- **Anything about linear systems.** The masking comes from Life's
  thresholds: a cell survives on two neighbours or three. In a linear
  model a nonzero coupling always passes a perturbation on, so the
  effect has no linear counterpart.

The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.
