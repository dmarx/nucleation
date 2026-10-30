---
number: 227
status: Active
formerly:
- THEORY-tmp7q33x
title: "Mutual information between an input and its representation does not fix the representation's quality: invertible encoders all preserve it exactly, yet under a linear probe some do better than the raw input and some worse"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active under ADR-065, at the status review's ruling (the
    owner delegated these rulings). The title asserts an existence result,
    and one instance of each half settles it: invertible encoders all keep
    the true mutual information, and under a linear probe some score above
    raw pixels ("some give rise to improved linear classification
    performance over raw pixels", §3.1, checked by the reviewer against the
    arXiv v2 text NOTE-749 read) and one scores "significantly worse than
    using raw pixels" (Fig. 1c). NOTE-749 read the paper in full, and
    nothing in the record contradicts it. The old promote_when read: "A
    replication outside MNIST and CIFAR-10, or with a second probe family
    (for example a regularized nonlinear readout), showing that encoders
    constrained to preserve the input's information exactly still span a
    range of downstream quality that includes worse than the raw input. The
    invertibility argument already makes the true MI equal across them, so
    what needs settling is the generality of the quality spread, not the MI.
    It is refuted by a showing that, among exactly information-preserving
    encoders, downstream quality under the probes in use is constant, or is
    ordered by some information quantity of the encoder alone. What cannot
    settle it: comparisons of MI estimates, since the account is about true
    MI, which the estimators do not measure." Its demand for generality
    beyond MNIST, CIFAR-10 and the linear probe asks for more than the title
    claims, and moves to QUESTION-357.
tags:
- representation-learning
- information-theory
date: '2026-10-14'
source:
- LIT-247
summary: >-
  Tschannen, Djolonga, Rubenstein, Gelly & Lucic (2020), [LIT-247](../literature.d/LIT-247.md), read in
  [NOTE-749](../notes.d/NOTE-749.md). Invertible RealNVP encoders on MNIST halves keep the true
  MI constant, yet trained with an MI estimator they gain linear-probe
  accuracy, and one trained adversarially against a linear probe ends
  "significantly worse than using raw pixels". At matched bound values the
  encoder architecture decides quality. What makes MI-trained
  representations good must therefore come from somewhere other than MI.
  The paper's alternative, that InfoNCE works as metric learning, is argued,
  not tested.
---
<!-- inactive-ok-file: THEORY-001 CLAIM-193 — Proposed; cited for context, nothing here rests on them -->

# THEORY-227: Mutual information between an input and its representation does not fix the representation's quality: invertible encoders all preserve it exactly, yet under a linear probe some do better than the raw input and some worse

## Source

Tschannen et al. (2020), [LIT-247](../literature.d/LIT-247.md), read in [NOTE-749](../notes.d/NOTE-749.md): §3.1 (Fig. 1,
App. B), §3.2 (Fig. 3), §3.3 (Fig. 4a–b, Fig. 9) and §4.

## What was actually shown

**The argument.** An invertible map preserves all the information in its
input, so every invertible encoder of each half of an MNIST image
maximizes the MI between the two halves' representations. MI cannot
prefer one invertible encoder to another. The paper adds a thought
experiment: a PNG-compressed image keeps the information and loses the
geometry. "The information content alone is not sufficient to guarantee
a useful geometry in the representation space."

**Accuracy rises at constant MI (§3.1, Fig. 1a–b).** RealNVP encoders
trained with I_NCE or I_NWJ stay invertible. The estimate and linear-probe
accuracy both rise during training while the true MI does not change.

**Accuracy falls at constant MI (§3.1, Fig. 1c, App. B).** An encoder of
the same architecture, trained adversarially against a linear classifier
with no MI estimator involved, stays invertible and ends with
classification "significantly worse than using raw pixels".

**The encoder decides at a matched bound (§3.3).** Training MLP and
ConvNet encoders to the same bound value (|I_EST − t| for t = 2, 4), the
ConvNet encoders give "clearly superior classification accuracy, for both
I_NCE and I_NWJ", though both architectures reach about 94% when trained
supervised.

**A tighter bound can do worse (§3.2).** For I_NWJ, a higher-capacity MLP
critic gives a higher bound value and worse features. For I_NCE all
critics saturate near log K, and only accuracy differs.

What could have come out otherwise: the adversarial invertible encoder
could have been unable to fall below raw pixels, which would have left
open that information preservation sets a floor on linear-probe quality.

## What this does not say

- **Not that MI is irrelevant.** A representation that discards the
  information a task needs cannot support it. The claim is that, once the
  information is kept, MI does not order representations.
- **Not that InfoNCE is metric learning.** InfoNCE with an inner-product
  critic is algebraically the multi-class K-pair loss (App. C), but that
  this explains its success is argued from the experiments, not tested.
- **Not a general result about probes.** Quality here is linear-probe
  accuracy on MNIST halves, and CIFAR-10 for two experiments.
- **Not that tighter InfoNCE bounds give worse features.** That is shown
  for I_NWJ only.
- **Not advice.** The paper's recommendations to co-design critic, encoder
  and evaluation are machine-learning practice and belong in the anthology.

## Connections

- **[THEORY-006](THEORY-006.md)** summarizes these experiments under the InfoNCE bound, as
  evidence that the bound's value is not what the objective's success
  tracks. This account states the stronger, estimator-free point beneath
  it, about true MI.
- **[THEORY-001](THEORY-001.md).** The optimal critic is a function of the density ratio
  alone, so the optimum says nothing about which encoder is good. At
  matched bound values the encoder's inductive bias decides.
- **[CLAIM-193](../claims.d/CLAIM-193.md).** Linear-probe quality depends on geometry that an
  invertible map can change while it keeps the information. That fits the
  claim that a linear probe family separates only what differs in the
  normalized kernel.
