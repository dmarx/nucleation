---
status: Proposed
title: 'A probe family that supplies a transformation''s training signal cannot also certify what the transformation preserves: preservation must be shown under probes that were not used to train it'
version: 1
role: thesis
defeated_if: >-
  Across documented generators trained against a pretrained feature
  family, metrics computed in that family rank and score them no
  differently from metrics in independently trained feature spaces and
  from human judgements. Evaluation under the training probes would
  then be as good a certificate as evaluation under held-out ones.
tags:
- representation-learning
- model-comparison
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-011
grounds:
- CASE-tmpp6j2b
complements:
- CLAIM-tmpd1aee
summary: >-
  The owner set the frame at U51 ("a useful case study ... the
  projected GAN work"); A184 §§3–4 argued it, with its Experiment C
  and closing maxim, and A203 §30 and A218 Study 6 keep it. It carries
  [CLAIM-011](CLAIM-011.md)'s remedy from correspondences to training objectives.
  Kynkäänniemi et al. ([CASE-tmpp6j2b](../cases.d/CASE-tmpp6j2b.md)) is a documented instance, which
  the exchange did not know of. One case, in image generation, so
  Proposed.
illustrated_by:
- CASE-tmpp6j2b
---
<!-- inactive-ok-file: CLAIM-tmpd1aee — Proposed; open, and cited as open: the claim is under test, not settled -->

# CLAIM-tmpslubp: A probe family that supplies a transformation's training signal cannot also certify what the transformation preserves: preservation must be shown under probes that were not used to train it

## The claim

A184 §4, Experiment C: "Evaluate generated samples with independent
relational probes and human judgments that were not used to train the
generator ... success under the training probes should not be taken as
sufficient evidence of preservation under independent observations". A184
§6: "What a system learns to preserve is constrained by what its training
process is able to distinguish; what we can verify it has preserved is
constrained by the observations used to evaluate it." A203 §30: "FID
measures resemblance through probes. Projected GANs trains through probes."
A218's Study 6: "Test whether matching projected feature distributions
guarantees preservation of independently measured relationships".

The reason is [CLAIM-011](CLAIM-011.md)'s, one step further. A correspondence estimated
on some tasks must be evaluated on others. A transformation trained to
satisfy some probes must be evaluated on others, because training pushes it
toward whatever the probes reward, including what they cannot see
(probe-relative equivalence, [CLAIM-tmpd1aee](CLAIM-tmpd1aee.md)). The documented case
([CASE-tmpp6j2b](../cases.d/CASE-tmpp6j2b.md)) is worse than blindness. A Projected FastGAN, trained
against ImageNet features, matches StyleGAN2's FID, which is also computed
in ImageNet features, while doing worse in CLIP space and with human
judges.

For the manuscript the application is direct. A translation or
reconstruction model tuned against a pragmatic classifier, or against an
LLM judge, cannot be certified by that classifier or judge. Its fidelity
must be shown under probes it was not tuned on. [CLAIM-085](CLAIM-085.md) makes the
neighbouring point for generation and judging with one model: that
measures the model's preferences.

## What it does not say

- It does not say metrics in the training probes are worthless. It says
  they are not a certificate.
- It does not say a generator trained against a probe family will introduce
  the differences the family cannot see. A184 §3: "This does not prove the
  generator will make that error".
- It does not say any held-out probe is neutral. Held-out probes have their
  own training data; in the case, CLIP "is not neutral either"
  ([ANTH-NOTE-304](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-304.md)).
- It does not settle [QUESTION-005](../questions.d/QUESTION-005.md). It names one way the
  operationalization can build its verdict into the measurement.
- The documented support is one case, in image generation. Hence Proposed.
