---
status: Proposed
title: 'Persistence and nucleating productivity vary independently: two intermediates of an assembly can have the same expected residence time and different chances of reaching the target before failure, since the committor depends only on where a state''s exits lead and not on how fast it leaves, and an intermediate can persist while lowering the target''s chance of forming against an admissible alternative'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a continuous-time Markov chain in which two
  transient states with equal total exit rates and equal residence times
  must have equal committors, or in which scaling all of one state's exit
  rates by the same factor changes its committor. Not defeated by evidence
  about what nuclei in real organizations do, which the claim does not
  assert.
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-11-05'
line:
- realizability
- nucleating-argument
- formal-apparatus
uses:
- TERM-tmp3awsy
bears_on:
- QUESTION-038
- QUESTION-380
summary: >-
  A's candidate claim, from the third synthesis on DNA origami pasted by the
  owner on 2026-11-05 (§§2 and 10): "Persistence and nucleating
  productivity can vary independently." A's example has two intermediates,
  both with total exit rate 0.10 and so expected residence time 10; one
  exits to the target at 0.08 and to a trap at 0.02, the other the reverse.
  Their committors are 0.8 and 0.2. The assistant adds the general reason:
  a state's committor is the exit-probability-weighted average of its
  successors' committors, so its total exit rate, which sets how long it
  persists, cancels. A's second part is that "an intermediate can persist
  while reducing the target's formation probability". It is the trap of
  CLAIM-184, shown in DNA origami by Dunn et al.'s seams. The wording is
  A's, with the assistant's proof; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-184 CLAIM-185 TERM-tmp3awsy — Proposed, Skimmed or new; entries cited as open -->

# CLAIM-tmpiyvk1: Persistence and nucleating productivity vary independently: two intermediates of an assembly can have the same expected residence time and different chances of reaching the target before failure, since the committor depends only on where a state's exits lead and not on how fast it leaves, and an intermediate can persist while lowering the target's chance of forming against an admissible alternative

## The claim

Take a continuous-time Markov chain with rates Q_ij, a target set F and a
failure set K, both absorbing. For a transient state i the committor
satisfies Σ_j Q_ij q(j) = 0, which is

  q(i) = Σ_{j≠i} (Q_ij / λ_i) q(j),  with λ_i = Σ_{j≠i} Q_ij.

The expected residence time in i is 1/λ_i.

1. **Persistence and committor are separate coordinates.** Multiplying every
   exit rate of i by c > 0 changes its residence time by 1/c and leaves the
   ratios Q_ij/λ_i, and so q(i), unchanged. A state can be made as
   persistent as one likes without changing its chance of success, and two
   states of equal persistence can have any committors their exit
   probabilities allow. A's example: λ = 0.10 for both intermediates, with
   q = 0.08/0.10 = 0.8 for one and 0.02/0.10 = 0.2 for the other.
2. **Persistence can lower the target's chance.** If an intermediate N
   exits mainly to K, then forming N and holding it, rather than an
   admissible alternative from which F is likelier, lowers the chance of
   reaching F. In A's words, an intermediate "can persist while reducing
   the target's formation probability relative to an admissible
   alternative".

## The molecular instance

Dunn et al. (NOTE-tmpvgzvb): long-range seam staples that bind early and
"effectively, irreversibly" trap folding into the wrong fold. The trap
persists, and persisting is what makes it a trap.

## What it qualifies

- **CLAIM-185's anchor.** "Persistence makes anchoring possible;
  productivity requires demonstrating that the anchor improves subsequent
  development." A: "A stable anchor is not necessarily a good anchor."
  CLAIM-184 says early anchors can entrench; this claim says entrenchment
  is invisible in persistence alone.
- **QUESTION-038,** what turns a persisting structure into an anchor. This
  claim says it is not persistence.

## What it does not say

- **That a high committor shows a cause.** "The intermediate might simply
  occur along already-favorable trajectories, without being responsible
  for their success" (TERM-tmp3awsy's interventional measure).
- **Anything about organizations** beyond the logic. A: "The broader
  organizational interpretation remains to be tested."
