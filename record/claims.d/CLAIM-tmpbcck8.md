---
status: Proposed
title: 'A family of probes that supplies an optimized system''s training signal
  cannot also certify what the system preserves: optimization pushes toward
  whatever the probes reward, including what they cannot see, so preservation
  must be shown under probes not used to train it'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-149 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-149 rests on; CLAIM-149
    now rests on this claim.
role: thesis
defeated_if: Across systems optimized against a probe family, evaluation in
  that family is found to rank and score them no differently from evaluation
  under independent probes and from independent human judgement, so that the
  training probes certify as well as held-out ones.
tags:
- model-comparison
- representation-learning
- philosophy-of-science
date: '2026-10-13'
line:
- formal-apparatus
grounds:
- CASE-041
summary: 'The general content of [CLAIM-149](CLAIM-149.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  it does not rest on [CLAIM-011](CLAIM-011.md)''s account of correspondences in translation.
  Training against a probe family pushes a system toward whatever the family
  rewards, including differences it cannot see, so the family is not a certificate
  of what was preserved. [CASE-041](../cases.d/CASE-041.md) is a documented instance: a Projected FastGAN
  trained against ImageNet features matches StyleGAN2''s FID, also computed
  in ImageNet features, while doing worse in CLIP space and with human judges.'
supports:
- CLAIM-149
- CLAIM-190
---
<!-- inactive-ok-file: CLAIM-149 CLAIM-190 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-tmpbcck8: A family of probes that supplies an optimized system's training signal cannot also certify what the system preserves: optimization pushes toward whatever the probes reward, including what they cannot see, so preservation must be shown under probes not used to train it

## The claim

What a system learns to preserve is constrained by what its training
signal can distinguish. What can be verified that it preserved is
constrained by the observations used to evaluate it. When the two are the
same probe family, evaluation measures fit to the training signal, not
preservation. Optimization moves the system toward whatever the probes
reward, and that includes differences the probes cannot see. So
preservation has to be shown under probes the system was not trained
against.

The documented case ([CASE-041](../cases.d/CASE-041.md)) is worse than blindness. A generator
trained against ImageNet features matches a stronger generator's FID,
computed in the same features, while doing worse in an independently
trained feature space and with human judges.

## Where the record applies it

[CLAIM-149](CLAIM-149.md) applies it to translation and reconstruction models tuned
against pragmatic classifiers or judges. [CLAIM-190](CLAIM-190.md) applies it to a
record's anchoring measures. Both now rest on this claim for the general
point.

## What it does not say

- It does not say metrics in the training probes are worthless, only that
  they are not a certificate.
- It does not say a system trained against a family will introduce the
  differences the family cannot see. It says the family cannot show that
  it did not.
- It does not say held-out probes are neutral. They have their own
  training data.
- The documented support is one case, in image generation. Hence
  Proposed.
