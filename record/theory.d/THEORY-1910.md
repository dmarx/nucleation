---
number: 1910
status: Proposed
formerly:
- THEORY-tmpysvtc
promote_when: >-
  An independent reproduction, or a run of the released code, on the same
  GloVe gender setup gives linear classifier accuracy near chance after
  INLP and a one-hidden-layer MLP's accuracy well above chance.
title: 'INLP guards only against linear readers'
statement: >-
  On Ravfogel and colleagues, iterating "train a linear classifier for an
  attribute, then project the representations onto its nullspace" makes the
  attribute linearly undecodable, gender in GloVe falling from 100% to 49.3%
  linear accuracy, while a one-hidden-layer MLP still recovers it at 85.0%,
  so the method guards only against linear readers
version: 1
tags:
- representation-learning
date: '2026-11-15'
source:
- LIT-2619
summary: >-
  Ravfogel, Elazar, Gonen, Twiton & Goldberg (2020), [LIT-2619](../literature.d/LIT-2619.md), read in
  [NOTE-1991](../notes.d/NOTE-1991.md). INLP's composed projection is linearly guarding for the
  attribute; the MLP result is the paper's own measurement of what it
  leaves. The wording is the reader's; adopting it is the owner's call.
---

# THEORY-1910: INLP guards only against linear readers

## Source

Ravfogel et al. (2020), [LIT-2619](../literature.d/LIT-2619.md); read in [NOTE-1991](../notes.d/NOTE-1991.md).

## The result

- On GloVe vectors labelled for gender, a linear SVM's accuracy falls from
  100% to 49.3% after 35 iterations of INLP (§6.1.1).
- "The MLP recovers gender with accuracy of 85.0%. This is expected, as
  the INLP method is only meant to achieve linear guarding" (§6.1.1).
- The authors state the limit: "the attributes are not protected under
  non-linear classifiers" (§7).

## What it does not show

- That any erasure method fails against nonlinear readers: the result is
  INLP's, on one embedding and one attribute.
- Anything about perfect erasure (independence of representation and
  attribute), which INLP does not attempt; [THEORY-281](THEORY-281.md) is about that.
- What a downstream model trained on the guarded vectors does with the
  nonlinear residue; the MLP was trained as a probe for gender.
