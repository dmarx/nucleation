---
number: 2045
status: Proposed
formerly:
- THEORY-tmpsiaty
title: 'Settles''s survey reports that letting a learner choose which instances to have labelled usually reduces the labels needed for a given accuracy, but not reliably: actively gathered data are biased toward the model that chose them, active learning has sometimes needed more labels than passive sampling, approaches that ignore variable labelling costs can do no better than random selection, and greedy guarantees hold only for submodular objectives, which active-learning criteria generally are not'
version: 1
source:
- LIT-2799
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-494
promote_when: >-
  A second reading of the survey (§§4.1, 6.3, 6.6, 6.7, 7.3) confirming
  that it reports each of these four caveats as stated, with the cited
  sources (Schein and Ungar 2007; Settles et al. 2008a; the submodularity
  remark citing Nemhauser et al. 1978 and Krause 2008).
summary: >-
  From the reading of [LIT-2799](../literature.d/LIT-2799.md) in [NOTE-2118](../notes.d/NOTE-2118.md). Settles (2009;
  revised 26 January 2010), Active Learning Literature Survey, Computer
  Sciences Technical Report 1648, University of Wisconsin–Madison,
  https://burrsettles.com/pub/settles.activelearning.pdf. The standard
  survey of active learning: query scenarios, query strategies
  (uncertainty sampling, query-by-committee, expected error reduction,
  variance reduction), and the evidence for them. It also covers practical
  issues such as variable labelling costs, unknown model classes and
  stopping criteria. It reports that active learning usually saves labels
  but can fail: the data are biased toward the model that chose them,
  cost-blind selection can do no better than random, and greedy guarantees
  need submodularity, which active-learning criteria generally lack. Here
  because the owner said at U30 that the exchange was entering active-
  learning territory. It bears on [CLAIM-572](../claims.d/CLAIM-572.md)'s greedy-stopping result and
  on the feedback premise of [QUESTION-494](../questions.d/QUESTION-494.md). Read in its NOTE
  (skimmed).
---
<!-- inactive-ok-file: NOTE-2118 — Skimmed; cited in this filing of 2026-11-19 -->

# THEORY-2045: Settles's survey reports that letting a learner choose which instances to have labelled usually reduces the labels needed for a given accuracy, but not reliably: actively gathered data are biased toward the model that chose them, active learning has sometimes needed more labels than passive sampling, approaches that ignore variable labelling costs can do no better than random selection, and greedy guarantees hold only for submodular objectives, which active-learning criteria generally are not

## The account

In the survey's framing, active learning lets the learner pose queries, usually unlabeled instances for an oracle to label, to reach high accuracy with few labels. Most published results show fewer labels needed, though publication bias may play a part. In a noiseless one-dimensional threshold task the saving is exponential. The caveats: the labelled set is a biased sample tied to the model class that chose it; Schein and Ungar found cases needing more labels than passive learning; ignoring variable labelling costs can erase the gain; stopping rules in use are intrinsic stability heuristics, while in practice stopping is economic; and the (1 − 1/e) greedy guarantee needs submodularity, which active-learning criteria lack in general.

## What it does not show

- No new results. A survey up to 2010.
- Little on agents whose queries are actions in a world, or on interventional or structural queries.
- It does not quantify how often active learning fails.

## Note of 2026-11-19: Howard and Ruder, read
A parallel ([NOTE-2141](../notes.d/NOTE-2141.md)): Howard and Ruder use the same measure of labels needed to reach a level, by transfer rather than by choosing which examples to label.
