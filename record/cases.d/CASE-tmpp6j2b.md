---
status: Active
title: 'FID and Projected GANs: one ImageNet-trained probe family used both to train a generator and to evaluate it'
version: 1
standing: documented
tags:
- representation-learning
- model-comparison
date: '2026-10-10'
line: pragmatic-transport
illustrates:
- CLAIM-tmpslubp
- CLAIM-tmpd1aee
- CLAIM-011
summary: >-
  The owner pointed to FID at U50 and proposed FID with Projected GANs
  as a paired case study at U51. A184 framed the pair: FID evaluates a
  distribution through probes, and Projected GANs learn one under
  pressure from probes. The anthology's readings supply the fact the
  exchange lacked. The Projected GAN discriminator is ImageNet-trained,
  FID's features are ImageNet class evidence, and Kynkäänniemi et al.
  show that such a generator can match FID while doing worse in an
  independent feature space and with human judges.
supports:
- CLAIM-tmpslubp
---
<!-- inactive-ok-file: CLAIM-tmpslubp CLAIM-tmpd1aee CLAIM-005 — Proposed; open, and cited as open: the claim is under test, not settled -->

# CASE-tmpp6j2b: FID and Projected GANs: one ImageNet-trained probe family used both to train a generator and to evaluate it

## The case

The owner, U50: "The Frechet Inception Distance work feels relevant". Then
U51: "yeah if anything I was thinking it might make a useful case study or
something like that. another potential case study along similar lines is
the projected GAN work." A184 §1: "FID evaluates a learned distribution
through probes; Projected GANs learn a distribution under pressure from
probes."

The works are held in the Anthology of the SOTA, and are cited here by its
codes.

- **FID** (Heusel et al. 2017, [ANTH-LIT-611](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-611.md)) compares the Inception-V3 pool3
  feature distributions of real and generated images, by the Fréchet
  (squared 2-Wasserstein) distance between Gaussian fits.
- **Projected GANs** (Sauer et al. 2021, [ANTH-LIT-562](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-562.md), read in [ANTH-NOTE-303](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-303.md);
  the practice is [ANTH-SOTA-338](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-338.md)) train the generator against discriminators
  that see a frozen ImageNet-pretrained feature network, through fixed random
  cross-channel and cross-scale mixing. They reach the previously best FIDs
  up to 40 times faster.
- **Kynkäänniemi et al. 2023** ([ANTH-LIT-563](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-563.md), read in [ANTH-NOTE-304](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-304.md); the
  practice is [ANTH-SOTA-337](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-337.md)) show two things. First, resampling a
  generator's outputs to match ImageNet class statistics lowers FID by
  63–72% on four datasets, without changing the generator, while
  non-ImageNet feature spaces barely move. Second, an ImageNet-pretrained
  Projected FastGAN matches StyleGAN2's FID on FFHQ (5.28 against 5.30),
  while its Fréchet distance in CLIP space is worse (4.67 against 2.76), and
  humans prefer StyleGAN2.

The exchange did not cite Kynkäänniemi et al. It is the decisive fact.

## What it can show

The case is A184's Experiment C, already run. A184 §4 asked to "Evaluate
generated samples with independent relational probes and human judgments
that were not used to train the generator", because "success under the
training probes should not be taken as sufficient evidence of preservation
under independent observations" ([CLAIM-tmpslubp](../claims.d/CLAIM-tmpslubp.md)). The documented result
is stronger than A184's maxim. When the evaluation probe and the training
probe share a source, the evaluation is not merely blind; it is biased in
the generator's favour.

It also shows probe-relative equivalence in a measured setting
([CLAIM-tmpd1aee](../claims.d/CLAIM-tmpd1aee.md)). Two generators equal under one probe family differ under
another and under human judgement. And it shows [CLAIM-011](../claims.d/CLAIM-011.md)'s remedy at
work: the confound was found by evaluating in a feature space the generator
was not trained against. It is a documented instance of the failure
[QUESTION-005](../questions.d/QUESTION-005.md) fears, a measurement and an objective that share a probe
family.

A181 §4 adds a second limit, which the case does not need but sits beside
it: "Even a perfect measure of the unconditional image distribution cannot
detect a generator that preserves the overall distribution while breaking
the association between prompts and images". That is a note on
[CLAIM-005](../claims.d/CLAIM-005.md).

## What it cannot show

- It does not show that Projected GANs are worse generators. The anthology
  rates the claim "moderate": one model, on one dataset, with human
  evaluation ([ANTH-NOTE-304](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-304.md), C3).
- It does not show that FID is uninformative within a fixed setup.
- It does not show that CLIP space is a neutral check. [ANTH-NOTE-304](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-304.md): "CLIP
  is not neutral either."
- It says nothing yet about pragmatic observables. It is an analogue from
  image generation.

**Boundary.** This is the nucleation reading of the works: probes in
evaluation and in training, read for the transport question. The works stay
in the anthology, and no nucleation LIT is filed. A nucleation LIT would
need a NOTE reading each work for pragmatic transport ([ADR-013](../decisions.d/ADR-013.md)), and nothing
in the exchange is such a reading.
