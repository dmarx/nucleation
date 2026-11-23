---
status: Proposed
title: 'A non-monotone generalisation of folding-island coverage, counting a component as covered only when the first seed front to reach it forces it, does not transfer to a kinetic constraint-growth system: it ranks seed sets worse than the monotone island union and flags many times more harmful additions than occur, because the seeds that hurt there have large islands and act through the order in which components reach the binding threshold'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23 from the executed study
    CASE-tmp2a9lm, whose pre-registration fixed the predictor and the
    criterion of transfer before the test.
role: thesis
warrant: empirical
defeated_if: >-
  An error in the code or the analysis of CASE-tmp2a9lm; or a rerun of the
  pre-registered test, with more runs per set or more architectures of the
  same model, in which Voronoi-island coverage meets the registered
  criterion (AUC at least 0.7, recall at least 0.5, and a rank correlation
  with V no more than 0.05 below the best monotone baseline's). Not
  defeated by the predictor's success in self-folding sheets or in any
  system with coherent alternative branches, which the claim does not test,
  nor by the success of a different predictor in the same system.
tags:
- complex-systems
- probabilistic-modeling
- mathematics
date: '2026-11-23'
line:
- realizability
- formal-apparatus
grounds:
- CASE-tmp2a9lm
bears_on:
- QUESTION-380
summary: >-
  [QUESTION-380](../questions.d/QUESTION-380.md) asks for a predictor of productive nuclei from the
  constraint architecture, tested in a system other than its own, and its
  note of 2026-11-07 records that UFI, the folding-island predictor, is
  monotone. The race reading of folding islands (VIC), pre-registered as
  the non-monotone replacement, fails the registered test in
  [CASE-tmp2a9lm](../cases.d/CASE-tmp2a9lm.md): Spearman 0.22 against the island union's 0.54, 193
  additions flagged of which 2 are significant decreases, and on five fresh
  architectures 0.21 against 0.48. Its own first form, built on static
  arc consistency, was constant there. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp2a9lm — new; the executed study this claim is grounded in, filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-tmpzi0ri — new; the post hoc predictor's claim, filed by the lead run of 2026-11-23 -->

# CLAIM-tmpzo914: A non-monotone generalisation of folding-island coverage, counting a component as covered only when the first seed front to reach it forces it, does not transfer to a kinetic constraint-growth system: it ranks seed sets worse than the monotone island union and flags many times more harmful additions than occur, because the seeds that hurt there have large islands and act through the order in which components reach the binding threshold

## The claim

Stern, Pinson and Murugan ([THEORY-1418](../theory.d/THEORY-1418.md)) explain an added actuator "with a
very small folding island" stopping a successful fold as competition
between actuators, the sheet misfolding just outside the small island
([CLAIM-562](CLAIM-562.md)'s reading). Voronoi-island
coverage (VIC) writes that as a race: each component is credited only if
the nearest seed's own island forces it, so a small-island seed placed in
a larger island's territory lowers the score. VIC is computed from the
constraints and the graph alone, and is not monotone in the seed set.

In [CASE-tmp2a9lm](../cases.d/CASE-tmp2a9lm.md), pre-registered before any run, VIC fails the criterion
of transfer:

- **Ranking.** Its rank correlation with the chance of exact assembly is
  0.22 on five architectures and 0.21 on five fresh ones, against 0.54 and
  0.48 for the monotone island coverage it was meant to improve on.
- **Flags.** It predicts a fall for 193 additions, of which 2 are
  significant decreases (precision 0.01), and catches 2 of the 8 there are;
  on the fresh architectures 22 of 251 flags (recall 0.58, precision 0.09).
- **Mechanism.** Post hoc, the seeds that hurt on average have islands of
  25, 62 and 62 of 64 components; the failures they cause fall inside
  islands, on components bound at threshold with two states still open. A
  seed changes when and from which side components reach threshold, which
  VIC, like any island-based score, does not see.

The first registered form, with islands by static arc consistency, was
constant on the test system, because the constraints there have the target
as their only solution and arc consistency finds it from any seed.

## What it does not say

- That VIC fails in self-folding sheets. It was not run there.
- That no non-monotone predictor works here: a post hoc one does
  ([CLAIM-tmpzi0ri](CLAIM-tmpzi0ri.md)).
- That the test system is like DNA origami.
