---
status: Proposed
promote_when: >-
  A study shows that children's or adults' second-order generalization
  from one exemplar of a novel category tracks the within-category
  variability of features in their training categories, as the
  hierarchical model's learned higher-level parameters predict, and not
  only the overall frequency of those features. A training study that
  varies within-category variability while holding feature frequency
  fixed, or the reverse, would settle it. Further qualitative fits to the
  same published data cannot, since the authors concede that a flat model
  with the right prior would mimic them.
title: "In Kemp, Perfors and Tenenbaum's account, abstract inductive constraints such as the shape bias are higher-level parameters of a hierarchical Bayesian model, here the within-category variability and population feature distribution of a Dirichlet-multinomial, learned from a few labelled exemplars per category at the same time as the categories' own feature distributions, and once learned they let a single exemplar of a new category license generalization by shape"
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-tmpazn9q, the reading of Kemp, Perfors and
    Tenenbaum (2007), registered from the owner's pasted synthesis
    "Hierarchical probabilistic models in cognitive science" of
    2026-11-04. The wording is the reader's.
tags:
- cognition
- probabilistic-modeling
- learning-and-conditioning
date: '2026-11-04'
source:
- LIT-tmplu70i
bears_on:
- QUESTION-276
summary: >-
  Kemp, Perfors & Tenenbaum (2007), LIT-tmplu70i, read in NOTE-tmpazn9q.
  Learning a constraint is inference over a hierarchy's higher-level
  parameters (α, β): low within-category variability of shape is the
  shape bias. The model reproduces Smith et al.'s first- and second-order
  generalization qualitatively, with no new experiments, and misses the
  no-name condition. Computational level; the structure and top prior are
  given. The wording is the reader's; adopting it is the owner's call.
---
# THEORY-tmpi143z: In Kemp, Perfors and Tenenbaum's account, abstract inductive constraints such as the shape bias are higher-level parameters of a hierarchical Bayesian model, here the within-category variability and population feature distribution of a Dirichlet-multinomial, learned from a few labelled exemplars per category at the same time as the categories' own feature distributions, and once learned they let a single exemplar of a new category license generalization by shape

## Source

Kemp, Perfors and Tenenbaum (2007), LIT-tmplu70i; read in NOTE-tmpazn9q.

## What was actually shown

- **The model.** Level 1, each category's feature distribution θ_i;
  level 2, (α, β); level 3, a fixed prior on α. Simulations, no new
  experiments.
- **The shape bias** (p. 314). Trained on Smith et al.'s (2002) four
  categories, two exemplars each, "shape matches are preferred in both
  cases", first- and second-order generalization, matching the children's
  choices qualitatively.
- **Against a fixed prior** (pp. 312–313). On the Barratos task, "our model
  alone accounts" for colour judged homogeneous within a tribe and obesity
  not; the model with (α, β) fixed treats them alike.
- **Predictions** (p. 314): two exemplars per category teach the bias best,
  and the abstract level can be learned faster than the concrete one.
  Neither is tested in the paper.
- **Kinds** (p. 316). A Chinese-restaurant prior over categories recovers
  objects and substances, with a shape bias for one and a material bias
  for the other.

## What this does not say

- That flat Bayesian models cannot do it. A conventional Bayesian model
  "could mimic the predictions of our model if it used the" right prior on
  the θ_i (p. 318); the case is parsimony and a learnable prior.
- That the constraint comes from nothing. The hierarchy, the generative
  process and the top prior are given (p. 318).
- Anything about mechanism: "Our contribution is entirely at the level" of
  computational theory (p. 317).
- That labels play no special role: children without labels failed
  second-order generalization, where the model predicts no impairment
  (pp. 314–315).
- That the categories themselves are learned: membership is given.
