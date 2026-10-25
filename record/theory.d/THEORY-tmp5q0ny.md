---
status: Active
title: 'On Stable Diffusion 2, MultiDiffusion''s 512 × 4608 panoramas had crops closer in FID to the reference model''s own samples than two outpainting baselines (10.3 against 18.4 and 45.5, fresh reference samples scoring 6.05) at equal CLIP score, over 8 prompts; and on 1,000 COCO layouts of two to four objects, the overlap of a segmenter''s output with the target layout was 0.26 IoU against 0.16–0.17 for the baselines and 0.43 for the real images, of which region fusion alone gave 0.18 and an early phase showing each region''s denoiser only its own region gave the rest'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-tmpa8ixz. Tables 1 and 2 of one paper, read in
    full; the title claims no more than they measured, and nothing in the
    record contradicts them, which meets ADR-047 v3. The attribution of
    the layout gain to bootstrapping is the paper's own ablation row.
tags:
- compositionality
date: '2026-10-25'
source:
- LIT-tmp03agp
summary: >-
  Bar-Tal, Yariv, Lipman and Dekel (2023), LIT-tmp03agp, read in
  NOTE-tmpa8ixz. Panorama quality is measured against the reference
  model's own crops, not against real panoramas, and the baselines
  extrapolate from a centre image. The layout result rests on one
  segmenter and one overlap score, with spreads whose basis is not stated.
  Comparison with models trained for region-to-image generation is
  qualitative only.
---

# THEORY-tmp5q0ny: On Stable Diffusion 2, MultiDiffusion's 512 × 4608 panoramas had crops closer in FID to the reference model's own samples than two outpainting baselines (10.3 against 18.4 and 45.5, fresh reference samples scoring 6.05) at equal CLIP score, over 8 prompts; and on 1,000 COCO layouts of two to four objects, the overlap of a segmenter's output with the target layout was 0.26 IoU against 0.16–0.17 for the baselines and 0.43 for the real images, of which region fusion alone gave 0.18 and an early phase showing each region's denoiser only its own region gave the rest

## Source

Bar-Tal, Yariv, Lipman and Dekel (2023), ICML 2023, LIT-tmp03agp, read in
full in NOTE-tmpa8ixz. Tables 1 and 2, §§5.1–5.2.

## What was actually shown

**Panoramas (Table 1).** Stable Diffusion 2, panoramas 512 × 4608 pixels
(nine times the training width) from overlapping 64 × 64 latent crops at
stride 8 with unit weights (THEORY-tmpt2q0g's fusion). For each of 8
prompts, N = 2000 reference images were sampled from the model, and one
random 512 × 512 crop was taken from each of N panoramas per method. FID
between the two sets, mean ± standard deviation over prompts: fresh
reference samples 6.05 ± 3.1, MultiDiffusion 10.3 ± 4.8, Blended Latent
Diffusion 18.4 ± 7.4, Stable Inpainting 45.5 ± 14.5. CLIP text–image
score 0.27 for all but Stable Inpainting (0.26); CLIP aesthetic 6.36 for
MultiDiffusion and the reference samples, 6.02 and 5.76 for the
baselines. Both baselines grow the panorama outward from a central image,
and the paper reports seams, repetition and drift in them (Fig. 4).

**Layouts (Table 2).** 1,000 COCO validation images with two to four
foreground objects, people excluded, every mask at least 5% of the image.
Each region is prompted "a {label}", the background by the full caption.
IoU of an off-the-shelf segmenter's output with the ground-truth
segmentation: real images 0.43 ± 0.09, Stable Inpainting 0.16 ± 0.10,
Blended Latent Diffusion 0.17 ± 0.11, MultiDiffusion without
bootstrapping 0.18 ± 0.10, with bootstrapping 0.26 ± 0.12. Bootstrapping
(Eq. 9) replaces, for the first 20% of steps, everything outside each
region's mask with a noised random constant-colour image before that
region's denoiser sees it.

What could have come out otherwise: the fused panorama could have drifted
from the reference distribution as much as outpainting does, since every
crop sees a blended state no single sample of the model would produce.
Region fusion without bootstrapping could have beaten the baselines by a
wide margin; it did not.

## What this does not say

- **Not that the fused crops are samples of the reference model.**
  10.3 against 6.05 is a measurable gap, and Proposition 3.1's guarantee
  does not apply (THEORY-tmpt2q0g).
- **Not that fusion is what gives layout control.** Without the early
  masked phase the gain over the baselines is 0.01–0.02 IoU against
  spreads of about 0.1, and the paper does not say what the spread is
  over or test the difference. Most of the gain comes from restricting
  what each denoiser sees early on, not from averaging their proposals.
- **Not parity with trained layout models.** Make-A-Scene and SpaText
  were compared only on their published examples.
- **Not "all metrics".** The paper says the method "outperforms the
  existing baselines in all metrics"; on CLIP score it ties Blended
  Latent Diffusion.

## Connections

- **QUESTION-tmpu6zq7.** The bootstrapping ablation is a case of the same
  spatial allocation used differently early in sampling changing the
  outcome. Time of action matters, not only the share of each update.
- **THEORY-522.** Open text-to-image models fail most on relative
  position. This method addresses position by explicit regions rather
  than by text.
