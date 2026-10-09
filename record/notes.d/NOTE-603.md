---
number: 603
status: Read
formerly:
- NOTE-tmp2x9ot
paper: 'LIT-839'
title: 'Classifier-Free Diffusion Guidance'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv v1 (26 July 2022, 14 pages, text extracted
    with pdftotext): Sections 1–6, Algorithms 1–2, Tables 1–2, the
    reference list and the captions of the sample figures (Figs. 1–8; the
    images themselves were not inspected). The derivations of Section 3
    were checked line by line. The NeurIPS 2021 workshop version was not
    read.
date: '2026-10-09'
summary: >-
  Shows that guidance in diffusion models needs no classifier: one
  network trained with randomly dropped conditioning supplies conditional
  and unconditional scores, and the extrapolation (1 + w)ε(z, c) − wε(z)
  trades FID for Inception score on ImageNet as classifier guidance does.
  The paper's own argument shows the guided field is in general not the
  score of any density, so the Bayes-tilted target that motivates it is
  not what is shown to be sampled.
---

<!-- inactive-ok-file: CLAIM-123 — Proposed; named as the manuscript claim this reading bears on -->

# NOTE-603: Classifier-Free Diffusion Guidance

## Contribution

Before this paper, guidance in diffusion models needed a separate
classifier trained on noisy inputs, and it was open whether the gain in
classifier-based metrics came from samples being adversarial to
classifiers. The paper shows that the same trade-off between Inception
score and FID can be had with no classifier at all, by mixing a
conditional and an unconditional score that one network learns at once.
It is a proof of concept on class-conditional ImageNet, not a claim about
text conditioning.

## Key insight

Guidance is extrapolation between two score estimates. If the scores were
exact, ε*(z, c) − ε*(z) would be −σ times the gradient of log p(c|z) for
the classifier obtained by Bayes' rule from the generative model, and
(1 + w)ε − wε_∅ would be classifier guidance with that classifier. Because
the learned scores are arbitrary vector fields, the same arithmetic yields
a direction that need not be the gradient of anything; it works
empirically anyway.

## Assumptions

- Continuous-time variance-preserving diffusion: q(z_λ|x) = N(α_λ x,
  σ²_λ I), λ the log signal-to-noise ratio, ε-prediction trained by
  denoising score matching (Eq. 5), so ε_θ(z_λ) ≈ −σ_λ∇ log p(z_λ).
- One network for both models; the unconditional model is the
  conditional one fed a null token, trained with probability p_uncond.
- The analysis linking Eq. 6 to an implicit classifier assumes exact
  scores ε*(z, c), ε*(z); the paper is explicit that learned scores do not
  satisfy this.
- Experiments: class labels as the condition, ImageNet downsampled to
  64×64 and 128×128, hyperparameters tuned for classifier guidance
  (Dhariwal & Nichol) and reused unchanged.

## Key results

- **Classifier guidance as tilting** (Section 3.1). ε̃ = ε(z, c) −
  wσ∇ log p_θ(c|z) gives approximate samples from p(z|c)p(c|z)^w; guiding
  an unconditional model with weight w + 1 is in theory the same as
  guiding a conditional one with weight w, though Dhariwal & Nichol found
  the latter better.
- **Classifier-free guidance** (Eq. 6): ε̃(z, c) = (1 + w)ε(z, c) −
  wε(z). With exact scores this equals guidance by the implicit classifier
  p_i(c|z) ∝ p(z|c)/p(z) (Section 3.2); with learned scores it "is not in
  general the (scaled) gradient of any classifier".
- **The trade-off** (Table 1, 64×64, p_uncond = 0.1): w = 0: FID 1.80,
  IS 53.7; w = 0.1: FID 1.55, IS 66.1; w = 1: FID 12.6, IS 170.1; w = 4:
  FID 26.22, IS 260.2. *Holds when:* 400k training steps, 50,000 samples
  per point, v = 0.3.
- **p_uncond** (Table 1, Fig. 4): 0.5 worse than 0.1 and 0.2 across the
  frontier; 0.1 and 0.2 about equal.
- **128×128** (Table 2): best FID 2.43 at w = 0.3 with T = 256 or 1024
  (ADM-G 2.97, CDM 3.52); at T = 128, the setting with ADM-G's number of
  network evaluations, best FID 3.02, worse than ADM-G. At w = 4, FID 21.5
  and IS 422, better on both than BigGAN-deep at its best-IS truncation
  (25, 253).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Guidance can be performed without a classifier, by combining conditional and unconditional scores of one network | strong | Tables 1–2, Figs. 4–5 |
| C2 | Classifier-free guidance trades FID against IS in the same way as classifier guidance | moderate | own tables only; classifier guidance is not rerun, ADM-G numbers are quoted |
| C3 | The guided field is in general not the gradient of any classifier or potential | strong (argument) | non-conservative learned scores, Sections 3.2 and 5 |
| C4 | So the IS/FID gain of guidance is not explained by an adversarial attack on classifiers | moderate | follows from C3, but no classifier-robustness test is run |
| C5 | Only a small share of capacity is needed for the unconditional task | weak | p_uncond sweep at one resolution and one training length |
| C6 | Guidance works by lowering unconditional and raising conditional likelihood | weak | stated as an intuition; no likelihoods are measured |

## Concepts

- **guidance**: modifying the score at sampling time to trade diversity
  for per-sample fidelity, by analogy with GAN truncation and low
  temperature in flows.
- **implicit classifier**: p_i(c|z) ∝ p(z|c)/p(z), the classifier the
  generative model defines by Bayes' rule.
- **p_uncond**: the probability of replacing the condition by the null
  token during training.
- **conservative**: a vector field that is the gradient of a scalar
  potential; learned score networks need not be.

## Connections

It removes the classifier from Dhariwal & Nichol's classifier guidance
(held in the anthology as [ANTH-LIT-699](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-699.md)) and reuses their architectures. The
non-conservativeness argument is credited to Salimans & Ho (2021), "Should
EBMs model the energy or the score?". Composable Diffusion ([LIT-770](../literature.d/LIT-770.md))
sums several such guidance terms, one per concept, and its AND operator
reduces to Eq. 6 for one concept ([NOTE-597](NOTE-597.md)). Attend-and-Excite
([LIT-806](../literature.d/LIT-806.md)) runs on Stable Diffusion with classifier-free guidance at
scale 7.5 and describes its own method as strengthening the text
conditioning "similar to" it.

## Bearing on the record

- **[CLAIM-123](../claims.d/CLAIM-123.md).** That claim says adding scores composes conditions
  only under conditional independence at the noisy state. This paper adds
  a second, independent caveat that the claim does not state: with learned
  networks the sum of score estimates is generally not the score of any
  density, so even the one-concept case is not sampling from the tilted
  distribution p(z|c)p(c|z)^w that motivates it. The paper states this
  for its own Eq. 6; extending it to sums of several terms is my reading,
  but the argument is the same.
- No THEORY is filed. The anthology already holds the account of what the
  guidance weight does to metrics ([ANTH-LIT-693](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-693.md), with its THEORY on the
  adversarial-metric question); the probabilistic point above is stated in
  the paper and needs no separate account here.
- **The text and the tables disagree on a sign.** Section 4.1 says FID is
  "monotonically decreasing … with w"; Tables 1–2 show it rising after
  w ≈ 0.1–0.3. The tables are right. The anthology's entry says the same.
- The paper carries an instruction for machine-learning practice (how to
  train and sample with guidance, which p_uncond to use), which is
  anthology material and is held there.

## Limitations

- One task family: class-conditional ImageNet. Nothing on text
  conditioning, composition of conditions, or prompt faithfulness.
- Hyperparameters were tuned for classifier guidance; the comparison with
  ADM-G uses quoted numbers, not a rerun.
- The claim that the gain is not adversarial (C4) is argued from the form
  of the sampler; no held-out classifier or non-Inception metric is used.
- Sample fidelity is measured only by FID and IS, both Inception-based.
- Each step costs two network evaluations; at equal compute the 128×128
  model loses to ADM-G on FID.

## Open questions

- What distribution, if any, does the guided sampler draw from when the
  learned field is not conservative? A characterisation of the stationary
  law of guided sampling for non-conservative fields would answer it.
- Does the guided field become closer to conservative as the score
  estimates improve? Measuring the curl of learned score fields along the
  sampling path would show it.
- How does the trade-off behave for compositional conditions, where c is
  a prompt with several objects and attributes? The paper does not test
  it; T2I-CompBench and its successor ([LIT-783](../literature.d/LIT-783.md), [LIT-798](../literature.d/LIT-798.md)) evaluate
  guided models without varying w.
