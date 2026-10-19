---
number: 510
status: Proposed
formerly:
- THEORY-tmpe5qsq
promote_when: >-
  A per-class analysis on ImageNet that accounts for both sources of
  noise: training runs, and the 50 validation images per class, by a
  bootstrap over validation images, with a false-discovery correction
  across the 1,000 classes. The account is supported if a corrected
  fraction of classes loses significantly as random crop or weight decay
  is strengthened while the mean rises, and if those classes are the ones
  whose label survives cropping worst. It is refuted if, after
  correction, no more classes lose than chance gives. More per-class
  curves for hand-picked classes cannot settle it.
title: "How much of an ImageNet image a crop must keep for its label to survive varies widely by class, with architectures agreeing on which classes are fragile, and strengthening random crop raises mean accuracy while some classes lose 20 points or more; how many classes lose is not established"
version: 1
tags:
- learning-theory
- anthology-candidate
date: '2026-10-16'
source:
- LIT-234
summary: >-
  Balestriero, Bottou & LeCun (2022), [LIT-234](../literature.d/LIT-234.md), read in [NOTE-845](../notes.d/NOTE-845.md). Six
  pretrained models on cropped test images keep some classes recognisable
  at an 8% crop and lose others below about 50%, and agree on which. Over
  20 ResNet-50 runs, moving the crop lower bound from 100% to 8% raises
  mean accuracy from about 70% to 76% while "academic gown" falls from
  about 62% to 40%. The classes shown are hand-picked; the per-class test
  rejects for 4.4% of classes at the 5% level, uncorrected for 1,000
  tests, which alone is not more than chance; and evaluation-set noise is
  not counted. Theorem 1 does not reach which classes pay.
---

# THEORY-510: How much of an ImageNet image a crop must keep for its label to survive varies widely by class, with architectures agreeing on which classes are fragile, and strengthening random crop raises mean accuracy while some classes lose 20 points or more; how many classes lose is not established

## Source

Balestriero, Bottou & LeCun (2022), [LIT-234](../literature.d/LIT-234.md) (NeurIPS 2022), read in full in
[NOTE-845](../notes.d/NOTE-845.md). [NOTE-845](../notes.d/NOTE-845.md) filed no THEORY, because what the paper supports for
practice (tune regularisation per class) belongs in the anthology, and its
general point is the bias–variance trade-off illustrated. This account
files the measurement the reading rates strong (C1) with the one it rates
moderate (C2), which are findings about classes and augmentations, not
instructions, and leaves the practice where the NOTE put it.

## What was actually shown

**Label preservation is class-dependent (§2.2, Figs. 2–3, 10–11).**
Pretrained models are evaluated on cropped test images. Some classes stay
recognisable down to an 8% crop. For others accuracy starts falling at
about 50%, while the average turns at about 30%. Six architectures agree
on which classes are fragile. CutOut and colour jitter behave the same.

**The average hides per-class losses (§2.3, Fig. 4).** ResNet-50 with the
random-crop lower bound τ from 100% to 8%, averaged over 20 runs. Mean test
accuracy rises from about 70% to about 76%. "Academic gown" falls from
about 62% to 40%, "barn spider" from about 68% to 46%.

**It survives transfer (§2.5, Fig. 6).** With a frozen ImageNet backbone and
a linear probe on iNaturalist, pretraining crop strength moves selected
classes by 30–60 points while the average stays near 37–40%.

**What could have come out otherwise.** The classes could have lost
recognisability at the same crop, and every class could have gained with
the mean. Neither happened for the classes shown.

## What this does not say

- **How many classes lose.** Figs. 4–6 show four pairs of classes chosen
  to illustrate divergence. A one-sided Welch test per class rejects for
  4.4% of classes at the 5% level and 2.1% at the 1% level, uncorrected
  for 1,000 tests; 4.4% at 5% is not, alone, more than chance, and 2.1%
  at 1% is about twice it. With 50 validation images per class one image
  moves a class by 2 points, a noise the test over training runs does not
  count. The printed null hypothesis is reversed ([NOTE-845](../notes.d/NOTE-845.md)).
- **That regularisation's cost must fall unevenly.** The paper asserts it
  from these figures. Theorem 1 says only that a zero-error fit to
  augmentations that leave the target's level sets is not the target, and
  it needs a group of transformations, which random crop is not.
- **That weight decay does the same.** Shown on one figure with no
  numbers or test (C3, weak).
- **That the class losses are caused by label-destroying crops.** The two
  measurements are made separately; correlating each class's crop
  fragility with its loss under training is the open test.
- **What to do about it.** Tuning or reporting per class is practice and
  belongs to the anthology.

## Connections

- **[THEORY-228](THEORY-228.md)** bounds linear-probe error by the probability that
  augmentation changes the label, divided by a spectral gap. This account
  shows that probability is far from uniform across classes, which bears
  on how that bound's error is distributed. It is a remark, not a result
  the paper draws ([NOTE-845](../notes.d/NOTE-845.md)).
- **The worst-group literature** (group DRO, spurious correlations)
  measures the same kind of per-group regression; the paper does not
  engage it, and the record holds none of it.
