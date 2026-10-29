---
number: 931
status: Proposed
formerly:
- THEORY-tmpaod5d
promote_when: >-
  The version of record (AAMAS 2018) read and found to report the same
  Table 3, with the naive learners' tit-for-tat percentage reconciled with
  their mutual-defection return (as printed the two are inconsistent), or
  an independent reproduction of the exact-gradient IPD and IMP
  experiments with the same memory-one parameterisation. ADR-047 lets an
  empirical THEORY stand on one study read in full once that inconsistency
  is resolved. It is refuted if exact-gradient LOLA pairs in that setting
  do not reach reciprocity in most runs, or do not settle at the mixed
  equilibrium of matching pennies. A result about more players, deeper
  shaping or asymmetric capacity neither promotes nor refutes it.
title: 'A learner that ascends its own return after one anticipated naive gradient step of its opponent, differentiating through that step, reached tit-for-tat-like reciprocity in 81% of fifty exact-gradient runs of the memory-one iterated prisoner''s dilemma, where pairs of naive gradient learners ended at the mutual-defection return, and settled at the mixed equilibrium of iterated matching pennies where naive learners did not converge; shown for two players, one-step shaping and access to the opponent''s parameters'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1519
summary: >-
  Foerster et al.'s LOLA (AAMAS 2018), read in full in [NOTE-1150](../notes.d/NOTE-1150.md) from
  arXiv v4, with the update rule re-derived. Empirical, in two small games
  and a grid game. Shaping here is mutual and produced cooperation, not
  capture; in matching pennies, a harmonic game, it damped the cycling of
  naive learners. Table 3's naive-learner tit-for-tat figure (20.8%) does
  not square with their return (−1.98), and the NOTE says so.
---

# THEORY-931: A learner that ascends its own return after one anticipated naive gradient step of its opponent, differentiating through that step, reached tit-for-tat-like reciprocity in 81% of fifty exact-gradient runs of the memory-one iterated prisoner's dilemma, where pairs of naive gradient learners ended at the mutual-defection return, and settled at the mixed equilibrium of iterated matching pennies where naive learners did not converge; shown for two players, one-step shaping and access to the opponent's parameters

## Source

Foerster, Chen, Al-Shedivat, Whiteson, Abbeel & Mordatch, [LIT-1519](../literature.d/LIT-1519.md),
read in [NOTE-1150](../notes.d/NOTE-1150.md) from arXiv:1709.04326v4: Eq. 4.4 (p. 3), Table 3 and
Figures 1–2 (pp. 4–6), Table 4 (p. 8).

## What was actually shown

- **The rule.** θ¹ ← θ¹ + δ∇θ¹V¹ + δη(∇θ²V¹)ᵀ∇θ¹∇θ²V², from maximising
  V¹(θ¹, θ² + η∇θ²V²) to first order with ∇θ²V¹ held fixed. Re-derived when
  filed.
- **IPD.** Memory-one policies, exact values, 50 runs: LOLA pairs played
  tit-for-tat-like policies in 81.0% (return −1.06 per step; tit-for-tat is
  −1); naive pairs returned −1.98, mutual defection being −2.
- **IMP.** LOLA pairs at the 50/50 equilibrium in 98.8% of runs, return
  standard deviation 0.02; naive pairs 0.0% and 0.37.
- **Mixed pairs.** LOLA against a naive learner −1.28 and −1.54, both above
  two naive learners (−1.99); second-order LOLA gained nothing against LOLA
  (Table 4).

What could have come out otherwise: the extra term could have made LOLA
an exploiter that drove the opponent to cooperate unilaterally; in the IPD
both sides ended better off.

## What this does not say

- **That opponent shaping yields cooperation generally.** Two players, two
  small games, one grid game, one step of look-ahead.
- **That it works without the opponent's parameters.** With a behavioural
  clone, Coin Game cooperation fell from about 80% to about 60%.
- **That shaping is benign when asymmetric.** One asymmetric pairing in
  one game.
- **What the naive learners' 20.8% counts.** As printed it contradicts
  their return and the text's "learn to defect in all states".
