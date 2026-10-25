---
status: Read
paper: LIT-tmpxsvgv
title: 'Zhong et al. — Multi-LoRA composition for image generation'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read in full from arXiv v2 (2402.16843, 19 November 2024), which is
    headed "Published in Transactions on Machine Learning Research
    (11/2024)" and gives the OpenReview forum of its review; text extracted
    with pdftotext. Read: abstract, §§1–6, the broader-impact statement,
    and appendix A.1 with the full GPT-4V evaluation prompt (Table 7).
    Figures 3, 4 and 5, whose numbers extraction garbled, were rendered as
    images and read from them; Figure 5's values are read off a plot and
    are approximate. The remaining appendix tables (the evaluation case
    study and the list of LoRAs) and the image figures were read from
    captions only. arXiv v1 was not compared.
date: '2026-10-25'
summary: >-
  Two training-free ways of using several LoRAs in one diffusion sampler
  without merging their weights: LoRA Switch gives each LoRA its own
  denoising steps in rotation, and LoRA Composite averages every LoRA's
  guided noise prediction at every step. On 480 sets of two to five public
  LoRAs, GPT-4V's paired judgements (and two annotators on 120 images)
  prefer both to weight merging, increasingly as LoRAs are added. In
  Switch, the switching interval and which LoRA acts first change the
  result at equal step shares. The baseline's merged adapter grows with
  the number of LoRAs, which the design does not separate from the
  decoding-time idea.
---
<!-- inactive-ok-file: CLAIM-336 CLAIM-297 CLAIM-321 THEORY-937 THEORY-927 CLAIM-278 — Proposed; the operator model, the mixture-of-experts readings and the claims this reading bears on, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-tmp6s2xi — Proposed; this reading's own account of the switching ablation, its sample unreported -->

# NOTE-tmphq8v2: Zhong et al. — Multi-LoRA composition for image generation

## Contribution

It moves the composition of several LoRA adapters from the weights to the
sampler. The prevalent method adds the adapters' low-rank updates into
one set of weights. Here every adapter stays intact and the sampler
decides, step by step, which adapters' models contribute to the update:
one at a time in rotation (LoRA Switch), or all at once by averaging
their predictions (LoRA Composite). It also supplies a testbed of 480
composition sets and a GPT-4V comparative judge, with a human check of
the judge and an analysis of its positional bias.

## Key insight

Several separately trained specialists can act on one denoising
trajectory without being merged, either by taking turns or by averaging
what each would do. The trajectory integrates their contributions. Taking
turns is sensitive to the schedule: at equal shares of steps, switching
every step distorts the image, and which specialist acts first matters
more than the order of the rest.

## Assumptions

- A text-to-image latent diffusion model ε_θ with classifier-free
  guidance at scale s (Eq. 2), and k LoRAs, each a low-rank update
  W′ = W + BA trained separately on one element (a character, clothing,
  a style, a background or an object).
- One text prompt c for all LoRAs, made of each element's manually
  annotated key features, which include the LoRAs' trigger words
  (Table 7: "kamado nezuko, black hair, pink eyes, forehead").
- LoRAs chosen to be compatible: "When composed, LoRAs from different
  categories should be compatible, preventing any conflicts in the
  resulting image composition". Every set has exactly one character and
  no repeated category.
- Experiments: Stable Diffusion 1.5 fine-tunes "Realistic_Vision_V5.1"
  (100 steps, s = 7, 1024 × 768) and "Counterfeit-V2.5" (200 steps,
  s = 10, 512 × 512), DPM-Solver++, three seeds averaged. "The weight
  scale w is consistently set at 0.8 for composing LoRAs within
  ComposLoRA", which reads as each LoRA's scale.

## Key results

- **LoRA Merge (the baseline, Eq. 3).** W′ = W + Σᵢ wᵢ BᵢAᵢ, here with
  wᵢ = 0.8 for every LoRA.
- **LoRA Switch (Eq. 4).** At step t the active LoRA is
  i = ⌊((t − 1) mod kτ)/τ⌋ + 1, with W′_t = W + wᵢBᵢAᵢ: each LoRA acts for τ
  consecutive steps in a fixed rotation, τ = 5, order character,
  clothing, style, background, object. Each LoRA gets 1/k of the steps.
- **LoRA Composite (Eq. 5).**
  ẽ(z_t, c) = (1/k) Σᵢ wᵢ [ε_θᵢ′(z_t) + s(ε_θᵢ′(z_t, c) − ε_θᵢ′(z_t))], with
  wᵢ = 1: "we set wi to 1, giving each LoRA equal importance". With unit
  weights this is ē(z_t) + s(ē(z_t, c) − ē(z_t)), classifier-free guidance
  on the mean of the k LoRA-modified models (the record's rearrangement).
  The guidance direction within each model is the text, not the LoRA:
  each model's own unconditional prediction already carries its LoRA. Cost:
  "(k − 1)× additional computational cost".
- **GPT-4V comparative scores against Merge (Fig. 3), 0–10, averaged
  over both presentation orders and three seeds; 48, 144, 192 and 96 sets
  at k = 2, 3, 4, 5.**

  | k | Switch / Merge, composition | Switch / Merge, image | Composite / Merge, composition | Composite / Merge, image |
  |---|---|---|---|---|
  | 2 | 8.69 / 8.65 | 9.53 / 9.46 | 8.85 / 8.74 | 9.72 / 9.53 |
  | 3 | 8.11 / 7.96 | 9.46 / 9.40 | 8.12 / 7.87 | 9.56 / 9.41 |
  | 4 | 7.20 / 6.68 | 9.36 / 9.27 | 7.10 / 6.68 | 9.43 / 9.15 |
  | 5 | 6.56 / 5.24 | 9.28 / 8.95 | 6.09 / 5.17 | 9.34 / 8.92 |

  Composition win/tie/loss against Merge at k = 2 → 5: Switch 43/34/23 →
  69/14/17, Composite 33/51/16 → 55/22/23 (%). Image quality at k = 5:
  Switch 46% wins, Composite 56%.
- **Human evaluation (Table 2).** Two graduate students, 120 images, 1–5
  Likert: composition Merge 3.14, Switch 3.91, Composite 3.78; image
  quality 2.94, 4.15, 4.35. Pearson correlation with the human scores:
  GPT-4V 0.454 (composition) and 0.457 (image), CLIPScore −0.006 and
  0.083. No inter-annotator agreement is reported.
- **Positional bias (Fig. 6).** Swapping the order changes Switch's
  composition win rate from 60% to 51% and Composite's from 52% to 42%;
  the bias runs the other way for image quality. Reported results average
  both orders.
- **Style (Fig. 4).** Composition wins against Merge: realistic, Switch
  58%, Composite 45%; anime, 53% and 50%. Image wins: realistic 42% and
  44%; anime 33% and 45%.
- **Switching schedule (Fig. 5, Table 3).** Composition win rate against
  Merge rises from about 38% at τ = 1 (switch every step) to about 59% at
  τ = 5; Table 3 gives 55, 57, 59, 58 for τ = 3–6 (image 29, 33, 34, 33).
  Read off Fig. 5(a), τ = 7 is about 60%, level with or above τ = 5, so
  "reaching peak performance at τ = 5" holds only within Table 3's range.
  Shrinking τ from 5 to 3 over sampling scored worst of the dynamic
  schedules (54 and 31). "the initial choice of LoRA in the activation
  sequence clearly influences overall performance, while alterations in
  the subsequent order have minimal impact": character first scores best
  (about 7.5 for composition on Fig. 5(b)), and "beginning with the style
  LoRA leads to a noticeable performance drop, even falling slightly below
  a random order". The ablation's sample (which sets, which k) is not
  stated.
- **Fewer steps (Tables 4–5).** With LCM (4 steps) or LCM-LoRA (8 steps),
  two-LoRA composition win rates against Merge stay similar (Switch
  45%/42%, Composite 39%/44%). With LCM-LoRA at k = 2, 3, 4, composition
  scores are Merge 7.52, 5.16, 3.49; Switch 8.08, 6.39, 5.08; Composite
  8.13, 6.07, 4.53.
- **ZipLoRA (Table 6),** SDXL, 10 sets each: for character + style
  ZipLoRA scores highest (9.05 composition, 9.40 image); for character +
  object Switch leads on composition (8.85) and Composite on image (9.25).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Decoding-time composition (Switch, Composite) beats weight merging, more so as LoRAs are added | moderate as measured; the cause is not isolated | Fig. 3, Table 2; Merge run at a fixed 0.8 per LoRA, so its summed update grows with k, and no Merge with weights scaled by 1/k is run |
| C2 | Switch is better at composition, Composite at image quality | weak | inferred from each method's win rate against Merge, never compared head to head by GPT-4V; human ratings agree in direction on 120 images |
| C3 | Switching every step distorts images; an interval of about five steps is best | moderate | Fig. 5(a), Table 3; sample unstated |
| C4 | Which LoRA acts first matters; the order of the rest does not | weak to moderate | Fig. 5(b); differences of a few tenths on a 0–10 scale, no spread, sample unstated |
| C5 | GPT-4V comparative judging tracks human judgement better than CLIPScore | moderate | Pearson 0.45 against −0.01 to 0.08, two annotators, 120 images |
| C6 | Both methods compose any number of LoRAs | weak | tested up to five, on LoRAs selected for compatibility, and scores fall to about 6 of 10 at five |

## Concepts

- **LoRA Merge**: adding several LoRAs' scaled low-rank updates into one
  weight matrix before sampling.
- **LoRA Switch (LoRA-s)**: one LoRA active per step, rotating every τ
  steps.
- **LoRA Composite (LoRA-c)**: the mean, at every step, of each
  single-LoRA model's guided noise prediction.
- **Decoding-centric**: the authors' term for composing in the sampler
  rather than in the weights.
- **ComposLoRA**: 22 LoRAs from civitai.com (two styles × three
  characters, two clothing, two styles, two backgrounds, two objects) and
  480 composition sets.

## Connections

It cites Composable Diffusion (Liu et al., 2022, LIT-770) and later work
as modifying classifier-free guidance to emphasize textual concepts, and
presents Composite as the same move conditioned on LoRAs. It cites
LoRAHub and ZipLoRA for learned merging coefficients, and Mixture of
LoRA Experts (Wu et al., 2024) only in passing. It does not cite
MultiDiffusion (LIT-tmp03agp, NOTE-tmpa8ixz), whose region fusion is the
spatial form of Composite's averaging.

## Bearing on the record

- **THEORY-405 and CLAIM-123.** Composite is not THEORY-405's
  conjunction. Composable Diffusion adds one guidance term per concept, so
  total guidance grows with k; Composite averages, so the total stays at s
  and each LoRA's model gets 1/k. Under THEORY-405's idealization (exact,
  conservative scores at the data distribution), an average of k scores is
  the score of the normalized geometric mean Πᵢ pᵢ^{1/k}, a product of
  experts each at temperature k, not the product itself. The noise-level
  caveat of THEORY-405 and CLAIM-123 applies unchanged. The derivation is
  the record's; the paper gives no probabilistic reading.
- **THEORY-611.** Each term is a guided field, in general the gradient of
  no density, and a mean of such fields is no better. The paper's phrase
  "enabling CFG to condition on LoRAs" overstates what Eq. 5 does: the
  guidance direction is the text within each LoRA-modified model, not the
  difference between a model with the LoRA and one without.
- **THEORY-tmpt2q0g.** Composite is MultiDiffusion's noise-prediction
  step with every mask full and the views being LoRA-modified models
  rather than prompts. Switch is the same step with a one-hot weight that
  rotates in time.
- **QUESTION-tmpu6zq7.** Switch is the owner's "number of iterations ...
  a given denoiser can apply" built and measured; Composite is A45's
  "share of one combined step". The ablation is evidence on the question's
  second half: at equal nominal budgets (each LoRA 1/k of the steps), the
  switching interval and which LoRA acts first changed the result,
  matching A33's "Authority can reside in sequence position, not just
  frequency". It is GPT-4V-judged on an unstated sample, and no per-LoRA
  counterfactual influence is measured (THEORY-tmp6s2xi). Per step, all
  three of the paper's methods and MultiDiffusion are convex weightings of
  the operators' predictions; what differs is how the weights vary over
  steps and pixels, and the ablation says that variation matters.
- **CASE-tmpjmerx.** Its operators are frozen, separately trained LoRAs
  combined per step, which is Composite with spatial grants. This paper
  is the case's prior art for the fixed-allocation arm and for
  per-step combination; it has no learned, audited or routed allocation.
  Its finding that merging degrades with k is a reason for the case's
  per-step combination, not evidence on governance.
- **CLAIM-336's note of 2026-10-25.** This paper is A45's "population
  with multiple genuinely specialized operators": distinct operators
  under one shared frame (one prompt), with uniform (Composite) or
  time-sliced (Switch) influence. The frame and the operator do not
  separate cleanly here: the shared prompt carries each LoRA's trigger
  words, so a LoRA acts partly through the frame.

ML method; it carries no instruction this record holds. Flagged
anthology-candidate on the LIT.

## Limitations

- **The baseline's scale confound.** Merge sums k updates at 0.8 each, so
  its total perturbation grows with k; Switch applies one at 0.8 and
  Composite averages. Merge's fall from 8.65 to 5.24 may owe as much to
  scale as to merging, and no rescaled Merge is run.
- **The judge.** GPT-4V with a positional bias of about ten points, told
  "Try not to let the two models end in a tie on both dimensions", and
  correlated with human ratings at 0.45. Switch and Composite are compared
  only through Merge.
- **The human check** has two annotators, 120 images and no agreement
  statistic.
- **No spread or significance** for any score; three seeds, averaged.
- **Text errors.** §5.1.1 gives "the composition quality score for LoRA-c
  with 5 LoRAs is initially 6.56 for 200 denoising steps, but with 4
  LoRAs in this setting, the score drops to 5.08"; 6.56 (Fig. 3(a)) and
  5.08 (Table 5) are LoRA Switch's scores, Composite's being 6.09 and
  4.53, and the realistic subset used 100 steps, not 200.
- **Selected LoRAs.** Compatibility was a selection criterion, so
  conflicts between adapters, the hard case, are excluded by design.

## Open questions

- Does a Merge baseline with weights scaled by 1/k close the gap? That
  separates "composing in the sampler" from "keeping the total adapter
  scale fixed".
- What is each LoRA's counterfactual effect on the image under Switch, by
  position in the order and by interval, at equal step shares? That would
  turn the ablation into a measurement for QUESTION-tmpu6zq7.
- What does Composite sample? Characterizing the target of averaged
  guided predictions would say whether it composes the LoRAs' elements in
  CLAIM-123's sense.
