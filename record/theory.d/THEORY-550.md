---
number: 550
status: Active
formerly:
- THEORY-tmpiqm1r
title: "Unsupervised clustering is not made epistemically superior to supervised classification by the absence of labels: it is sensitive to sample bias, highly sensitive to how inputs are represented, and overfits, with the number of clusters acting as a capacity control just as parametric complexity does in supervised learning"
version: 1
tags:
- philosophy-of-science
- epistemology
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-162
summary: >-
  Søgaard (2024), [LIT-162](../literature.d/LIT-162.md), read in [NOTE-108](../notes.d/NOTE-108.md). A rebuttal of two arguments for
  clustering's superiority, the No-Bias Argument and the Simplicity-Truth
  Argument, by toy counterexample and by the technical literature on
  overfitting in unsupervised learning (Hansen & Larsen 1996). The negative
  claims are firm. The paper's positive step, that supervised
  classification is "at least as" justified, is under-argued and is not
  part of this account.
---

# THEORY-550: Unsupervised clustering is not made epistemically superior to supervised classification by the absence of labels: it is sensitive to sample bias, highly sensitive to how inputs are represented, and overfits, with the number of clusters acting as a capacity control just as parametric complexity does in supervised learning

## Source

Søgaard (2024), [LIT-162](../literature.d/LIT-162.md) (*Minds and Machines* 34:43), read in full in
[NOTE-108](../notes.d/NOTE-108.md).

## What was actually shown

**The arguments rebutted.** The No-Bias Argument (attributed to Watson 2023a
and Nelson 2020) holds that clustering escapes label bias and cheaply
mitigates sample bias. The Simplicity-Truth Argument (Rochefort-Maranda & Liu
2020) holds that parametric simplicity links to truth only in unsupervised
learning, because there is no overfitting there.

**Sample bias (§2.1.1).** Uniform data on {1,2,3,4,5,9,10,11} has its natural
boundary at x = 7. Many clustering algorithms trained on the biased subsample
{1,2,3,9,10,11} put it at x = 6. Any advantage clustering has here comes from
the larger samples it usually gets.

**Representation (§2.1.2).** Projecting the Fig. 1 data onto one axis or the
other gives "radically different" clusterings. Human choices re-enter through
the representation and through model selection against labelled test sets.

**Overfitting (§3.2).** The technical literature treats overfitting and
capacity control in unsupervised learning as in supervised learning (Hansen &
Larsen 1996). In the three-blob example the number of clusters k plays
"exactly the same" role in both.

**Function estimation (§3.1).** A clustering is a function from data to a
partition, and any clustering hypothesis lies in the hypothesis class of a
supervised classifier over the same data. Given two labelled points from two
of three blobs, 1-nearest-neighbour gives the partition 2-means converges on.

**What could have come out otherwise.** Clustering could have been immune to
the biased subsample, or free of overfitting. It is neither.

## What this does not say

- **That supervised classification is at least as justified.** That is the
  paper's conclusion, and it outruns the argument. Hypothesis-class
  containment shows a supervised learner can represent any clustering, not
  that it reaches one from comparable evidence without labels that encode it
  ([NOTE-108](../notes.d/NOTE-108.md), C6: weak).
- **That supervised learning is computationally cheaper.** The counting in
  §2.3 appears miscounted, and the "2^n clustering experiments" figure is
  underived (C7).
- **That simplicity's role is proved the same in both.** The §3.2 "proof by
  contradiction" relies on an unstated premise equivalent to its conclusion
  (C8). The point rests on the technical literature, not on that proof.
- **That Watson holds the No-Bias Argument.** The paper notes Watson warns
  against treating clustering as objective, so the attribution is partial.
- **Anything about deep clustering or large-scale representation learning.**
  Every case is a low-dimensional toy, and self-supervised learning gets three
  brief mentions.

## Connections

- Watson ([LIT-187](../literature.d/LIT-187.md)) concludes that unsupervised outputs are neither objective
  nor vacuous and should be validated by error-statistical means. That a
  clustering overfits is consistent with validating it on held-out data, so
  the two disagree less than Søgaard's framing suggests ([NOTE-108](../notes.d/NOTE-108.md)).
- The text carries technical slips (a Stirling-number sequence, a partition
  count, reversed EM step labels) that do not touch the negative arguments
  ([NOTE-108](../notes.d/NOTE-108.md), corrections).
