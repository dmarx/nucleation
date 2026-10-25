---
status: Proposed
promote_when: >-
  Either the ablation's design reported (which composition sets and numbers
  of LoRAs, how many images, and the spread across seeds), with the effects
  of the switching interval and of the first LoRA exceeding that spread; or
  an independent measurement in which, at matched per-operator step
  budgets, changing the switching interval or the operator that acts first
  changes the output beyond seed variation, preferably measured as each
  operator's counterfactual effect on the image. More GPT-4V win rates on
  the same unreported sample do not meet it.
title: 'When several LoRAs take turns over one denoising trajectory, each given the same share of steps, the result depends on the schedule and not only on the shares: switching at every step scored worst (a composition win rate against weight merging near 38%, against about 59% when each LoRA kept five consecutive steps), shortening the turns late in sampling scored worse than keeping them fixed, and which LoRA acted first mattered more than the order of the rest, the character first scoring best and the style first slightly below a random order'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Proposed from NOTE-tmphq8v2. Fig. 5 and Table 3 of one paper,
    read in full, but the ablation's sample is not stated and no spread is
    given, so its own design cannot be checked to support the effects as
    stated. Fig. 5's values are read off a plot.
tags:
- compositionality
date: '2026-10-25'
source:
- LIT-tmpxsvgv
summary: >-
  Zhong et al. (2024), [LIT-tmpxsvgv](../literature.d/LIT-tmpxsvgv.md), read in [NOTE-tmphq8v2](../notes.d/NOTE-tmphq8v2.md). An ablation of
  LoRA Switch judged by GPT-4V against weight merging. It says that equal
  shares of steps do not fix the outcome; it does not say how large the
  order effect is beyond noise, or how much each LoRA contributes to the
  image, which was not measured. The authors' explanation, that core
  elements should come first, is theirs and untested.
---

# THEORY-tmp6s2xi: When several LoRAs take turns over one denoising trajectory, each given the same share of steps, the result depends on the schedule and not only on the shares: switching at every step scored worst (a composition win rate against weight merging near 38%, against about 59% when each LoRA kept five consecutive steps), shortening the turns late in sampling scored worse than keeping them fixed, and which LoRA acted first mattered more than the order of the rest, the character first scoring best and the style first slightly below a random order

## Source

Zhong et al. (2024), TMLR, [LIT-tmpxsvgv](../literature.d/LIT-tmpxsvgv.md), read in full in [NOTE-tmphq8v2](../notes.d/NOTE-tmphq8v2.md).
§4.3.2, Fig. 5 and Table 3.

## What was actually shown

LoRA Switch activates LoRA i = ⌊((t − 1) mod kτ)/τ⌋ + 1 at step t, so over
whole cycles each of k LoRAs acts on 1/k of the steps whatever τ is.

- **Interval (Fig. 5(a), Table 3).** Composition win rate against Merge,
  read off the plot: about 38% at τ = 1, rising to about 59% at τ = 5;
  Table 3 gives 55, 57, 59, 58 at τ = 3–6, and image-quality win rates
  29, 33, 34, 33. τ = 7 on the plot is about 60%. In the authors' words,
  "overly frequent switching, such as changing LoRAs at every denoising
  step, leads to distortions in generated images".
- **Dynamic intervals (Table 3).** τ rising 3 → 5 over sampling: 57 and
  33. Warm-up (rising over the first half, then 5): 58 and 34. τ falling
  5 → 3: 54 and 31, the worst.
- **Order (Fig. 5(b)).** Character first, the rest random, scores highest
  for composition (about 7.5 of 10 on the plot). Clothing, background or
  object first is comparable to a fully random order, and style first
  falls "slightly below a random order". The authors: "the initial choice
  of LoRA in the activation sequence clearly influences overall
  performance, while alterations in the subsequent order have minimal
  impact."

What could have come out otherwise: with shares held equal, the schedule
could have made no difference, as it would if the trajectory simply
summed each LoRA's contributions.

## What this does not say

- **Not how large the effects are against noise.** The ablation's sets,
  number of LoRAs and image count are not given, nor any spread. The
  order differences on Fig. 5(b) are a few tenths of a point.
- **Not that each LoRA's influence on the image depends on its position.**
  Only overall scores were measured. Whether the first LoRA's element is
  rendered better, or the others' worse, is not reported.
- **Not why.** "prioritizing core image elements in the initial stage" is
  the authors' reading. The record's diffusion literature on layout being
  set early (MultiDiffusion's "the layout is being determined early on in
  the diffusion process", [NOTE-tmpa8ixz](../notes.d/NOTE-tmpa8ixz.md)) is consistent with it and does not
  test it.
- **Not beyond this setting.** Two SD 1.5 fine-tunes, LoRAs chosen to be
  compatible, GPT-4V as judge.

## Connections

- **[QUESTION-tmpu6zq7](../questions.d/QUESTION-tmpu6zq7.md).** The owner's third mechanism counted influence as
  "the number of iterations ... a given denoiser can apply". Here the
  number of iterations is held equal and the outcome still moves with
  interval and order, as A33's "Authority can reside in sequence position,
  not just frequency" proposed. If promoted, this is evidence that the
  mechanism does not reduce to a time-averaged vector of influence
  weights.
- **[THEORY-tmp5q0ny](THEORY-tmp5q0ny.md).** MultiDiffusion's early masked phase is a second
  case of the same allocation used differently early in sampling changing
  the result.
