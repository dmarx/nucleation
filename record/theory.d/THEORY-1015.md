---
number: 1015
status: Active
formerly:
- THEORY-tmpz726y
title: 'Groups of objects drawn from beta processes share features only if the measure they are drawn around is discrete; in the hierarchical beta process that measure is itself a beta process draw, and at each shared feature a group''s prevalence is Beta(c_j b, c_j(1 − b)) around the shared prevalence b, so a small c_j lets groups differ and a large one pulls them together'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1171. The construction (8)–(9) and the
    argument for a discrete base are the paper's §6; the steps are
    re-derived below from its (2)–(3), which meets the condition for
    Active under ADR-047 v2. The paper's one classification experiment is
    reported, not leaned on.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
source:
- LIT-1537
summary: >-
  Thibaux and Jordan (2007), [LIT-1537](../literature.d/LIT-1537.md), read in [NOTE-1171](../notes.d/NOTE-1171.md). The
  hierarchical beta process B ~ BP(c0, B0), Aj ~ BP(cj, B) gives several
  groups one unbounded feature library at group-specific prevalences. It
  treats each object as in one group, exchangeable within it, and has no
  dynamics; its one experiment, 58% against 50% on a single text split,
  is suggestive only.
---

# THEORY-1015: Groups of objects drawn from beta processes share features only if the measure they are drawn around is discrete; in the hierarchical beta process that measure is itself a beta process draw, and at each shared feature a group's prevalence is Beta(c_j b, c_j(1 − b)) around the shared prevalence b, so a small c_j lets groups differ and a large one pulls them together

## Source

Thibaux and Jordan (2007), [LIT-1537](../literature.d/LIT-1537.md), §6, equations (8)–(9), read in
full in [NOTE-1171](../notes.d/NOTE-1171.md). The facts about beta-process draws used are its
(2)–(3).

## What was actually shown

**Why the base must be discrete.** If Aj ~ BP(cj, B) with B continuous,
then by (2) Aj = Σ pi δωi with atom locations from a Poisson process whose
intensity has B as its location part. Two independent such draws, A1 and
A2, have their atoms at independent draws from a continuous measure, so
they coincide with probability zero: the groups share no feature. If B is
discrete, B = Σ bi δωi, then by (3) every Aj has its atoms at the ωi, with
weights aj,i ~ Beta(cj bi, cj(1 − bi)). Every group then draws on the same
countable library.

**The hierarchy.** B is unknown, so it is given a prior that makes it
discrete: B ~ BP(c0, B0), with B0 continuous. Then (8):
B ~ BP(c0, B0), Aj ~ BP(cj, B) for each group, Xi,j ~ BeP(Aj).

**Shrinkage.** At an atom with baseline b, aj ~ Beta(cj b, cj(1 − b)) has
mean b and variance b(1 − b)/(cj + 1). So cj → ∞ forces every group to
the baseline prevalence and small cj lets groups depart from it, while
the library itself is shared. Given mj of the nj objects in group j
holding the feature, E[aj | b, x] = (cj b + mj)/(cj + nj), the paper's
predictive, which shrinks the group's frequency toward b rather than
toward a fixed prior mean, as Laplace smoothing does.

**Evidence the paper adds.** On 1000 unbalanced 20 Newsgroups posts in 20
categories, with cj = 10⁻⁴ chosen by cross-validation, the hBP classifier
reached 58% on one 40% test split and the best Laplace-smoothed naive
Bayes 50%. One split, no variance reported.

## What this does not say

- That groups can overlap. Each object is in exactly one group j.
- That anything changes over time. Prevalences are drawn once; there is no
  persistence or transition.
- That features within a group are correlated. Given Aj, an object's
  features are independent.
- That a small cj makes groups alike. The paper's §7 gives that reason
  for choosing cj small; by (9) it is the reverse ([NOTE-1171](../notes.d/NOTE-1171.md),
  Limitations).
- That the hBP is generally a better text classifier. The single
  experiment does not show that.
