---
status: Proposed
title: 'An alternative to the floor and band of the owner''s truncated-band account: the fine end of a learned spectrum may be damped for smoothness and generalization, with discrimination growing steadily toward it, and the floor a measurement finds below it may be estimator noise rather than a class of low-signal outliers bounding a band of highly discriminating directions'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A model in which the directions below the discriminating band, once
  measured with noise controlled (a cross-validated or held-out spectrum,
  or a sample large enough that the band's edge does not move with it),
  stay less discriminating than the band above them, and the edge between
  them stays put as the sample grows, so that the floor belongs to the
  model and not to the estimator. Not met by a floor in a single
  uncontrolled measurement, which both readings predict.
tags:
- representation-learning
- neuroscience
- learning-theory
date: '2026-11-22'
line:
- learned-structure
objects_to:
- CLAIM-tmp2r6ur
grounds:
- THEORY-tmpwtoad
uses:
- TERM-tmpf5ymd
summary: >-
  A rival reading, in the assistant's voice, of two parts of the owner's
  [CLAIM-tmp2r6ur](CLAIM-tmp2r6ur.md): that the extreme bottom carries low-signal outliers and
  that the bottom of the retained band holds the most discriminating
  directions. It does not rival the stop-word half. From Stringer and
  colleagues ([THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md), [NOTE-tmp923nm](../notes.d/NOTE-tmp923nm.md)): successive principal
  components encode finer features down the spectrum; the decay rate is a
  smoothing parameter, so fine, discriminating directions are kept at low
  variance for generalization; and below the resolved range the
  cross-validated eigenvalues vanish because "the remaining eigenvectors
  correspond to or are corrupted by additive noise". On this reading there
  is no band with a floor in the model, only a continuum cut off where the
  estimator loses it. Marked as an alternative to the owner's account; the
  other alternative is [CLAIM-tmp9atj9](CLAIM-tmp9atj9.md), on the top directions. [ARG-tmptvp76](../arguments.d/ARG-tmptvp76.md)
  argues the transfer. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2r6ur THEORY-tmpwtoad CLAIM-tmp9atj9 ARG-tmptvp76 ARG-tmpabk16 — Proposed or new; the owner's claim this rivals, its grounds, the other alternative and the test -->

# CLAIM-tmpufbx6: An alternative to the floor and band of the owner's truncated-band account: the fine end of a learned spectrum may be damped for smoothness and generalization, with discrimination growing steadily toward it, and the floor a measurement finds below it may be estimator noise rather than a class of low-signal outliers bounding a band of highly discriminating directions

**Which part it rivals.** Of the owner's [CLAIM-tmp2r6ur](CLAIM-tmp2r6ur.md), the second and
third parts: the extreme bottom carries low-signal outliers, and once it
is cut the bottom of the retained band is the most discriminating. Not the
first part, on the top directions. It is **alternative (b)**;
[CLAIM-tmp9atj9](CLAIM-tmp9atj9.md) is alternative (a). The owner chooses.

**The reading.** Down a smooth code's spectrum each direction encodes finer
distinctions than the one above it, so discrimination per unit grows
toward the fine end. The fine end carries little variance not because it
is noise but because a code that put more there would generalize worse:
the decay rate is a smoothing parameter. What a measurement finds below
some rank is where the estimator stops resolving the signal, a noise floor
set by the sample and the noise, not a separate class of low-signal
outliers in the model. On this reading the owner's "band" is a monotone
continuum truncated by measurement, and its "floor" moves when the
measurement improves.

**Where it comes from.** Stringer and colleagues ([THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)):
"Successive PC dimensions encode finer stimulus features" (Extended Data
Fig. 6); "the rate of eigenspectrum decay can be seen as a smoothing
parameter: slower eigenspectrum decay means less smoothing across stimuli,
which enables representation of fine stimulus features but impairs
generalization" (SI §2.4); and the resolved power-law range "typically ...
extends to approximately half the total number of stimuli presented",
below which "the remaining eigenvectors correspond to or are corrupted by
additive noise" (SI §3.5). Cross-validated PCA removes that floor rather
than locating it in a band.

**What it does not say.** Not that Xu's near-zero directions in the Qwen
models are estimator noise: they come from normalization coordinates with
weight near zero, a property of the model ([ARG-tmpabk16](../arguments.d/ARG-tmpabk16.md)), and are the
owner's best evidence for a floor in the model. The rival reading predicts
that such floors are exceptions tied to a mechanism, not a general band
edge. Not evidence about unembeddings: the source is mouse V1 and a kernel
argument ([ARG-tmptvp76](../arguments.d/ARG-tmptvp76.md)).

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
