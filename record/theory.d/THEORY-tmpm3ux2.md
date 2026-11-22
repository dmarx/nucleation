---
status: Proposed
promote_when: >-
  An independent run, with the authors' code or a reimplementation,
  reproduces in the hierarchical deep-linear setting the sign flip of the
  Bayesian influence and its peaks aligned with each level of the
  hierarchy, across several training seeds and over SGLD settings not
  chosen by agreement with leave-one-out; and reproduces in a small
  transformer the timing effect of upweighting induction tokens, speeding
  in the window where the influence falls and delaying earlier, across
  seeds. Not met by a restatement that cites this paper. Not defeated by
  a showing that SGD's stages and the Bayesian posterior's differ, which
  the title does not assert.
title: "Lee, Smith, Adam and Hoogland find that the Bayesian influence of one training sample on another, estimated as a negative posterior covariance from sampling localized at each checkpoint, changes in sign and magnitude over training: in a two-layer linear network on a hierarchical dataset it flips sign and peaks as each level of the hierarchy is learned, in small language models token-class influences shift around induction-circuit formation, and upweighting induction tokens speeds induction heads in the window where that influence falls and delays them earlier"
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-11-22'
source:
- LIT-3001
bears_on:
- QUESTION-363
- QUESTION-tmphkb1w
- QUESTION-217
summary: >-
  Lee, Smith, Adam & Hoogland (2025), LIT-3001, read in NOTE-tmp1sot8.
  Influence as a susceptibility that changes at stage transitions. The
  sharp edges: the theory is for a Bayesian posterior split between two
  phases, and the link to SGD is the paper's "primary theoretical gap";
  peaks are predicted only "under some conditions"; in the toy, the order
  of the peaks is the order of the modes' strengths. A.2 names the
  "Type-B" transition, equal loss with a falling LLC, without testing it.
  Proposed until reproduced.
---

# THEORY-tmpm3ux2: Lee, Smith, Adam and Hoogland find that the Bayesian influence of one training sample on another, estimated as a negative posterior covariance from sampling localized at each checkpoint, changes in sign and magnitude over training: in a two-layer linear network on a hierarchical dataset it flips sign and peaks as each level of the hierarchy is learned, in small language models token-class influences shift around induction-circuit formation, and upweighting induction tokens speeds induction heads in the window where that influence falls and delays them earlier

## Source

Lee, Smith, Adam & Hoogland (2025), "Influence Dynamics and Stagewise
Data Attribution", ICLR 2026, arXiv 2510.12071, LIT-3001, read in
NOTE-tmp1sot8.

## What was actually shown

- **Derived:** for a posterior that is a two-phase mixture, the
  covariance of two losses has a between-phase term
  πUπV(µi,U − µi,V)(µj,U − µj,V), which can carry either sign and is
  largest at an even split (§2.3).
- **Observed, toy:** in a two-layer linear network on Saxe's eight-item
  hierarchy, the BIF, an analytic influence through Saxe's closed-form
  mode strength and leave-one-out retraining agree that influence varies
  non-monotonically, flips sign, and peaks at each branching (§3); an
  ablation's effect is largest at the influence peak (C.5).
- **Observed, language models:** token-class influences in Pythia-14M
  shift with induction-circuit formation and delimiter learning (§4,
  D.3); timed upweighting of induction tokens in a 3M-parameter
  transformer accelerates induction heads at 4k–5.5k steps and delays or
  disrupts them earlier (D.4), on one initialization and data order.

## What this does not say

- That SGD follows the Bayesian posterior's transitions (§5's gap).
- That influence peaks in any given model; "under some conditions".
- That the peaks order by dependency. In the toy they follow the modes'
  strengths, the order of THEORY-740.
- Anything measured about the LLC over training; Type-B transitions are
  named in A.2, not shown.
