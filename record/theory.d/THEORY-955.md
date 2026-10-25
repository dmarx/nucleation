---
number: 955
status: Active
formerly:
- THEORY-tmpg6v1v
title: 'On 480 sets of two to five public LoRAs on two Stable Diffusion 1.5 checkpoints, GPT-4V''s paired judgements, averaged over both presentation orders and three seeds, scored giving each LoRA its own denoising steps in rotation (LoRA Switch) and averaging every LoRA''s guided noise prediction at every step (LoRA Composite) above merging the LoRAs'' weights at 0.8 each, at every number of LoRAs, the composition gap growing from 0.04–0.11 points of 10 at two LoRAs to 0.92–1.32 at five as merging fell from about 8.7 to 5.2; two annotators rating 120 images agreed in direction; the design does not separate composing at sampling time from the merged update''s scale growing with the number of LoRAs'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-1160. Fig. 3 and Table 2 of one paper, read
    in full; the title claims what was measured, by the judge that measured
    it, and nothing in the record contradicts it, which meets ADR-047 v3.
    The scale confound is the record's reading of the design.
tags:
- compositionality
date: '2026-10-25'
source:
- LIT-1529
summary: >-
  Zhong et al. (2024), [LIT-1529](../literature.d/LIT-1529.md), read in [NOTE-1160](../notes.d/NOTE-1160.md). The measurement
  is a GPT-4V comparison with a positional bias of about ten points,
  correlated 0.45 with two annotators, on LoRAs selected to be compatible.
  The two methods are compared with each other only through the baseline.
  It does not show that sampling-time composition is what helps: the
  baseline adds k updates at full scale, the two methods keep one
  adapter's scale.
---

# THEORY-955: On 480 sets of two to five public LoRAs on two Stable Diffusion 1.5 checkpoints, GPT-4V's paired judgements, averaged over both presentation orders and three seeds, scored giving each LoRA its own denoising steps in rotation (LoRA Switch) and averaging every LoRA's guided noise prediction at every step (LoRA Composite) above merging the LoRAs' weights at 0.8 each, at every number of LoRAs, the composition gap growing from 0.04–0.11 points of 10 at two LoRAs to 0.92–1.32 at five as merging fell from about 8.7 to 5.2; two annotators rating 120 images agreed in direction; the design does not separate composing at sampling time from the merged update's scale growing with the number of LoRAs

## Source

Zhong, Shen, Wang, Lu, Jiao, Ouyang, Yu, Han and Chen (2024), "Multi-LoRA
Composition for Image Generation", TMLR, [LIT-1529](../literature.d/LIT-1529.md), read in full in
[NOTE-1160](../notes.d/NOTE-1160.md) from arXiv v2. Fig. 3, Table 2 and Fig. 6.

## What was actually shown

**Methods.** Merge: W′ = W + Σᵢ 0.8·BᵢAᵢ. Switch: W′_t = W + 0.8·BᵢAᵢ with i
rotating every 5 steps. Composite: the mean over i of the guided
prediction of the model carrying LoRA i alone, which with unit weights is
classifier-free guidance on the mean model,
ē(z_t) + s(ē(z_t, c) − ē(z_t)).

**Testbed.** 22 LoRAs from civitai.com in two styles (realistic and
anime, each on its own SD 1.5 fine-tune), 480 sets with one character
and no repeated category: 48, 144, 192 and 96 sets of 2, 3, 4 and 5.

**Measurement.** GPT-4V sees one image from each of two methods and
scores composition and image quality from 0 to 10 by a deduction rubric,
told to "evaluate critically" and "Try not to let the two models end in a
tie on both dimensions". Swapping the order moved win rates by about ten
points (Fig. 6), so both orders are averaged. Three seeds are averaged.

**Composition scores (method / Merge), k = 2 → 5.** Switch 8.69/8.65,
8.11/7.96, 7.20/6.68, 6.56/5.24. Composite 8.85/8.74, 8.12/7.87,
7.10/6.68, 6.09/5.17. Image quality also favoured both methods at every
k, by 0.06–0.42. Composition win rates at k = 5: Switch 69%, Composite
55%.

**Humans (Table 2).** Two graduate students rated 120 images 1–5:
composition Merge 3.14, Switch 3.91, Composite 3.78; image 2.94, 4.15,
4.35. GPT-4V's scores correlated with theirs at 0.454 and 0.457,
CLIPScore at −0.006 and 0.083.

What could have come out otherwise: merging could have held up as LoRAs
were added, or the two sampling-time methods could have degraded as fast,
since every method's scores fall with k. Merging fell further.

## What this does not say

- **Not that composing in the sampler is the cause.** Merge was run at
  0.8 per LoRA, so its summed update grows with k, while Switch applies one
  adapter at a time and Composite averages k single-adapter models. A
  Merge with weights scaled by 1/k was not run, so the growing gap may
  owe as much to adapter scale as to where composition happens.
- **Not that Switch is better at composition and Composite at image
  quality.** The paper says so, from each method's win rate against Merge.
  GPT-4V never compared them directly. The human ratings agree in
  direction on 120 images with no agreement statistic.
- **Not that composition works.** At five LoRAs the best composition
  score is 6.56 of 10, and the LoRAs were selected to be compatible.
- **Not a probabilistic composition.** Composite averages guided
  predictions, which under [THEORY-405](THEORY-405.md)'s idealization would be the score
  of a geometric mean of the LoRA models' distributions, not their product
  ([NOTE-1160](../notes.d/NOTE-1160.md)).

## Connections

- **[THEORY-405](THEORY-405.md) and [CLAIM-123](../claims.d/CLAIM-123.md).** Composable Diffusion sums one guidance
  term per concept; Composite averages, keeping total guidance at s.
- **[THEORY-958](THEORY-958.md).** Composite is MultiDiffusion's noise-prediction
  step with every mask full and LoRA-modified models as the views.
- **[CASE-158](../cases.d/CASE-158.md).** Per-step combination of frozen, separately trained
  LoRA operators is the case's fixed-allocation arm without masks.
