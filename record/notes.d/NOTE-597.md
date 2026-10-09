---
number: 597
status: Read
formerly:
- NOTE-tmpq1itu
paper: 'LIT-770'
title: 'Compositional Visual Generation with Composable Diffusion Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v6 (17 January 2023, 30 pages, text layer), the latest
    version, which carries the ECCV 2022 paper plus a later appendix on
    Point-E. Sections 1–7 read in full, with Tables 1–3 checked number by
    number against the layout text. Appendix F (the derivations of both
    operators) read; Appendices A–E (FFHQ results, classifier details,
    label encoding, baselines, training settings) read for setup; the
    figure pages (Figures 7, 9–15) skimmed. Earlier arXiv versions were
    not compared. Figures are described from captions and prose only.
date: '2026-10-09'
summary: >-
  Treats a conditional diffusion model's noise prediction as the gradient
  of an energy, so concepts compose at sampling time by adding scores:
  AND is ε(x,t) + Σ wᵢ(ε(x,t|cᵢ) − ε(x,t)), the product p(x)Πp(x|cᵢ)/p(x)
  under conditional independence of the concepts given x; NOT divides by
  the negated concept's likelihood. No retraining. On CLEVR object
  positions it beats an EBM baseline (31.36% against 7.34% at three
  components); on relations it does not (2.80% against 4.26%); on FFHQ
  attributes it trails LACE in accuracy at three components but has the
  best FID. Text composition with GLIDE and Stable Diffusion is
  qualitative only.
---

# NOTE-597: Compositional Visual Generation with Composable Diffusion Models

## Contribution

A sampling-time composition rule for diffusion models, carried over from
compositional energy-based models (Du, Li and Mordatch 2020). Before it,
probabilistic composition of concepts (conjunction, negation) had been
shown with explicitly trained EBMs, which are hard to train and give poor
images. After it, the same algebra runs on a diffusion model trained with
classifier-free-guidance-style label dropout, or on a released text model
(GLIDE, Stable Diffusion, Point-E), with no further training, and single-
concept classifier-free guidance appears as its one-term case.

## Key insight

A diffusion model's noise prediction is, up to scale, the score of the
noised data distribution, and a score is the gradient of a log-density.
Multiplying densities adds their log-densities, so it adds their scores.
If an image should satisfy several concepts at once, and the concepts are
conditionally independent given the image, the target is the unconditional
density times one likelihood ratio p(x|cᵢ)/p(x) per concept, and its score
is the unconditional score plus one guidance term per concept. Composition
moves out of the text encoder, where everything must fit one fixed-size
vector, into the sampler, where each concept keeps its own term.

## Assumptions

- **Conditional independence of concepts given the image** (Eq. 9):
  p(x, c₁, …, cₙ) = p(x) Πᵢ p(cᵢ|x). Stated once and not examined.
- **Implicit classifier**: p(cᵢ|x) ∝ p(x|cᵢ)/p(x), with both terms from
  one network trained with labels dropped to null 10% of the time
  (Appendix C, after Ho and Salimans).
- **Score as energy gradient**: ε_θ(x_t, t) is treated as ∇ₓE. The authors
  note the learned field may not be conservative, so it need not be the
  gradient of any density, and set this aside by citing Salimans and Ho's
  finding that a conservative parameterization performs similarly.
- **One model, many conditions.** All composed terms come from the same
  network. The authors report limited success composing models trained on
  different datasets.
- **Weights wᵢ are free "temperatures"** (Eq. 11). With wᵢ ≠ 1 the
  sampled distribution is no longer the product of Eq. 10.
- **The derivation is at the data distribution.** The product is derived
  for p(x|c₁, …, cₙ) and the summed scores are then used at every noise
  level t. The paper does not discuss whether the noised marginal of the
  product equals the product of the noised conditionals (in general it
  does not). This observation is mine.

## Key results

- **Conjunction (Eq. 11, F.1):** ε̂(x_t, t) = ε_θ(x_t, t) + Σᵢ wᵢ
  (ε_θ(x_t, t|cᵢ) − ε_θ(x_t, t)); with one concept and w > 1 this is
  classifier-free guidance (Eq. 20).
- **Negation (Eq. 15, F.2):** p(x|not c̃ⱼ, cᵢ) ∝ p(x) p(x|cᵢ)/p(x|c̃ⱼ),
  giving ε̂ = ε_θ(x_t, t) + w(ε_θ(x_t, t|cᵢ) − ε_θ(x_t, t|c̃ⱼ)). "Not" is
  division by the negated concept's likelihood, not the complement
  1 − p(c̃ⱼ|x), and needs a positive concept beside it to stay realistic.
- **CLEVR object positions (Table 1, 5,000 images per setting):** accuracy
  by a binary classifier trained on real images, 1/2/3 components: ours
  86.42/59.20/31.36%, EBM 70.54/28.22/7.34%, StyleGAN2, LACE and GLIDE at
  or near 0 when composing. FID (5,000 images, Clean-FID) 29.29/15.94/10.51,
  best throughout.
- **Relational CLEVR (Table 2):** ours 60.40/21.84/2.80%, EBM
  78.14/24.16/4.26%; ours has better FID (29.06/29.82/26.11 against EBM's
  44.41/55.89/58.66). Composing three relations succeeds under 3% of the
  time for every method.
- **FFHQ attributes, AND and NOT (Table 3):** ours 99.26/92.68/68.86%,
  LACE 97.60/95.66/80.88%; ours has the best FID at two and three
  components (17.22, 16.95). The authors call this "comparable".
- **Pre-trained text models (Figures 1, 3, 6, 10–13):** composed GLIDE
  renders details a single long prompt misses; no quantitative measure is
  given for this setting.
- **Failure modes (Section 6.5, Figure 6):** concepts the base model does
  not know (GLIDE and "person"); attribute confusion that survives
  composition ("a bear in a red forest" AND "a car" gives a red bear);
  fusion into a single hybrid object (bird-shaped flower, dog-furred
  couch), usually when objects are centred. Appendix A.3 shows "a dog"
  AND "the sky" giving a dog-shaped cloud.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Summing per-concept guidance terms samples images that satisfy several concepts at once, without retraining | moderate: quantitative on synthetic CLEVR and on FFHQ; qualitative on text models | Tables 1, 3; Figures 1, 3 |
| C2 | The composed score corresponds to the product distribution p(x)Πp(x\|cᵢ)/p(x) | weak as stated: exact only for conditionally independent concepts, conservative fields, wᵢ = 1, and at t = 0 | Eqs. 9–11, Appendix F |
| C3 | Composition generalizes to scenes more complex than training | moderate for object positions (up to 3 components measured, 7 shown); not supported for relations (2.80% at 3) | Tables 1–2, Figure 4 |
| C4 | Composed diffusion beats compositional EBMs | strong on image quality (FID); mixed on accuracy, losing on relations | Tables 1–3 |
| C5 | Composing prompts binds attributes that DALL-E 2 confuses | weak: selected qualitative examples, and attribute confusion is itself a listed failure mode | Figures 5, 6 |

## Method

1. Train one conditional diffusion model with labels replaced by null 10%
   of the time, so it gives both ε_θ(x_t, t|c) and ε_θ(x_t, t); or take a
   released text-conditioned model.
2. At each reverse step, evaluate the unconditional and each conditional
   prediction at the current x_t.
3. Combine them by Eq. 11 (AND) or Eq. 15 (NOT) and take the usual
   Gaussian reverse step with the combined prediction (Algorithm 1).

## Concepts

- **concept**: any conditioning label: a sentence, a 2D object position, a
  relational description, or a binary face attribute.
- **implicit classifier**: p(c|x) written as p(x|c)/p(x), so that its
  log-gradient is the difference of two diffusion predictions.
- **conjunction (AND)** and **negation (NOT)**: the two operators,
  inherited from Du, Li and Mordatch's compositional EBMs.
- **components**: the number of concepts composed at test time; training
  always used one.

## Connections

The operators and the probabilistic factorization come from Du, Li and
Mordatch (2020) and Liu et al. (2021) on composing visual relations with
EBMs; the underlying idea is Hinton's product of experts (2002), which the
paper cites for EBM composition. The score reading of diffusion follows
Vincent (2011) and Song et al. (2021); the one-concept case is Ho and
Salimans' classifier-free guidance. Baselines are StyleGAN2(-ADA), LACE
(Nie et al.: classifier energies in a GAN latent), GLIDE and the EBMs.

## Bearing on the record

- **[LIT-667](../literature.d/LIT-667.md) and [THEORY-117](../theory.d/THEORY-117.md).** The record's account of compositional
  generalization is about recognition: unseen pairs are reached when a
  learned representation is linearly factored, a pair's vector the sum of
  per-concept vectors. This paper reaches unseen combinations in
  generation by a different additive structure, imposed at sampling: a sum
  of per-concept log-likelihood-ratio gradients. Neither needs the
  combination to have been seen, and both depend on an independence or
  additivity assumption holding. The paper measures nothing about learned
  representations, so it neither supports nor contradicts [THEORY-117](../theory.d/THEORY-117.md). The
  parallel is my connection, not the paper's.
- **[LIT-058](../literature.d/LIT-058.md).** The denoising-score identity that lets a noise predictor
  stand in for an energy gradient sits beside the I–MMSE relation read
  there; neither paper cites the other.
- **Siblings.** GenEval ([LIT-782](../literature.d/LIT-782.md)) and T2I-CompBench ([LIT-783](../literature.d/LIT-783.md))
  measure the attribute-binding and multi-object failures that this paper
  addresses; its own evaluation of text composition is qualitative.
- **THEORY candidate (not filed):** "Adding per-concept classifier-free
  guidance terms samples the product of the concept likelihood ratios
  only at zero noise; at intermediate noise the summed score is not the
  score of the noised product, so composed sampling is biased even with a
  perfect model." It needs a source that states and tests this; this
  paper does not.
- **Anthology.** The paper's practical content (composing prompts as
  separate guidance terms with per-term weights, negative prompting by
  subtracting a concept's prediction) is machine-learning practice for
  generative models and is anthology material, hence `anthology-candidate`.

## Limitations

- Composed models must be the same network; composing separately trained
  diffusion models worked poorly (Section 7, the authors' own limitation).
- The correspondence to a product distribution is heuristic: the
  non-conservative field is set aside by citation, the conditional-
  independence assumption is not tested, the noise-level issue is not
  raised, and the weights are tuned rather than derived.
- Quantitative evaluation is on 128 × 128 synthetic CLEVR scenes and on
  FFHQ with classifier-assigned labels; accuracy is judged by classifiers
  trained on real images (99.05%, 99.80%, and 95.01/99.20/97.49% on
  validation). The text-to-image results have no metric.
- Relations compose badly: below 3% at three relations, and below the EBM
  baseline at two and three.
- The caption of Table 2 says EBM's FID is "much lower" than the others';
  its FID is higher (worse), as the body text says.
- FID is computed on 5,000 images rather than the usual 50,000, as the
  authors state.

## Open questions

- Does composition hold for concepts that are not conditionally
  independent given the image (relations between objects are an obvious
  case, and they are where it fails)?
- How large is the bias from applying a t = 0 product rule at every noise
  level, and does a corrected sampler (e.g. MCMC within each step) remove
  the hybrid-object failures?
- What would let separately trained diffusion models compose, as separately
  trained EBMs do? The authors suggest a conservative score field.
