---
number: 611
status: Active
formerly:
- THEORY-tmpq39lu
title: "Classifier-free guidance extrapolates between a conditional and an unconditional score learned by one network; with exact scores this equals classifier guidance by the classifier the generative model defines through Bayes' rule, but learned scores need not be conservative, so the guided field is in general the gradient of no density and the tilted distribution that motivates guidance is not shown to be what is sampled"
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: MultiDiffusion and LoRA Composite apply guidance
    inside each component and combine the guided fields convexly, and
    spatial masking adds a second source of non-conservativeness. The
    account is unchanged.
tags:
- probabilistic-modeling
- compositionality
date: '2026-10-16'
source:
- LIT-839
summary: >-
  Ho & Salimans (2022), [LIT-839](../literature.d/LIT-839.md), read in full in [NOTE-603](../notes.d/NOTE-603.md), with the
  derivations of Section 3 checked line by line. The non-conservativeness
  argument is credited to Salimans & Ho (2021). The FID–IS trade-off is
  shown on class-conditional ImageNet only. [NOTE-603](../notes.d/NOTE-603.md) declined a THEORY
  because the anthology holds the account of what the guidance weight
  does to metrics; this one states only the probabilistic point, which
  the record's [CLAIM-123](../claims.d/CLAIM-123.md) uses.
---


# THEORY-611: Classifier-free guidance extrapolates between a conditional and an unconditional score learned by one network; with exact scores this equals classifier guidance by the classifier the generative model defines through Bayes' rule, but learned scores need not be conservative, so the guided field is in general the gradient of no density and the tilted distribution that motivates guidance is not shown to be what is sampled

## Source

Ho & Salimans (2022), "Classifier-Free Diffusion Guidance", arXiv v1,
[LIT-839](../literature.d/LIT-839.md), read in full in [NOTE-603](../notes.d/NOTE-603.md). The NeurIPS 2021 workshop version was
not read.

## What was actually shown

**Classifier guidance as tilting (§3.1).** ε̃ = ε(z, c) − wσ∇ log
p_θ(c|z) gives approximate samples from p(z|c)p(c|z)^w.

**Classifier-free guidance (Eq. 6).** ε̃(z, c) = (1 + w)ε(z, c) − wε(z),
where one network, trained with the condition dropped with probability
p_uncond, supplies both scores. With exact scores ε*(z, c) − ε*(z) is −σ
times the gradient of log p_i(c|z), the implicit classifier p_i(c|z) ∝
p(z|c)/p(z), so Eq. 6 is classifier guidance by that classifier (§3.2).

**With learned scores (§§3.2, 5).** The networks are arbitrary vector
fields, so the same arithmetic "is not in general the (scaled) gradient
of any classifier". The guided field need not be the gradient of any
scalar potential (C3, strong).

**It works anyway (Tables 1–2).** At 64×64 with p_uncond = 0.1: w = 0
gives FID 1.80, IS 53.7; w = 0.1 gives FID 1.55, IS 66.1; w = 4 gives
FID 26.22, IS 260.2. The same trade-off classifier guidance gives, with
no classifier.

What could have come out otherwise: without a classifier, the IS gain
could have vanished. It did not.

## What this does not say

- **What the guided sampler samples.** If the field is not conservative,
  the stationary law of guided sampling is uncharacterised ([NOTE-603](../notes.d/NOTE-603.md),
  Open questions). It is not shown to be p(z|c)p(c|z)^w.
- **That guidance's gain is not an adversarial effect on classifiers.**
  That follows from the form of the sampler (C4, moderate). No held-out
  classifier or non-Inception metric was used.
- **Anything about text or compositional conditions.** One task family,
  class labels on ImageNet.
- **That FID falls monotonically with w.** Section 4.1 says so; Tables
  1–2 show it rising after w ≈ 0.1–0.3. The tables are right.
- **That sums of several guidance terms are conservative.** The paper
  states the point for its own Eq. 6. Extending it to sums of several
  terms, as Composable Diffusion uses, is [NOTE-603](../notes.d/NOTE-603.md)'s reading, by the
  same argument.

## Connections

- [CLAIM-123](../claims.d/CLAIM-123.md) (adding scores composes conditions only under conditional
  independence at the noisy state) names this as a second, independent
  caveat: even one guided condition does not sample the tilted target.
- Composable Diffusion ([LIT-770](../literature.d/LIT-770.md), [NOTE-597](../notes.d/NOTE-597.md)) sums guidance terms, one per
  concept, and its AND reduces to Eq. 6 for one concept.
- The anthology holds the account of the guidance weight's effect on
  metrics, beside Dhariwal & Nichol's classifier guidance ([ANTH-LIT-699](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-699.md)).
- The conditional Schrödinger bridge ([THEORY-515](THEORY-515.md)) conditions by
  changing the endpoints and path rather than the field.

## Note of 2026-10-25: guided fields combined convexly

Two works read on 2026-10-25 apply classifier-free guidance inside each
component and then combine the guided fields convexly: MultiDiffusion by
region ([LIT-tmp03agp](../literature.d/LIT-tmp03agp.md), [NOTE-tmpa8ixz](../notes.d/NOTE-tmpa8ixz.md), [THEORY-tmpt2q0g](THEORY-tmpt2q0g.md)) and LoRA Composite
over LoRA-modified models ([LIT-tmpxsvgv](../literature.d/LIT-tmpxsvgv.md), [NOTE-tmphq8v2](../notes.d/NOTE-tmphq8v2.md)). Each guided field
is in general the gradient of no density, and a mean of such fields is no
better. Spatial masking adds a second source. Across a region boundary the
Jacobian of Σᵢ Mᵢ ⊙ sᵢ is symmetric only if Σᵢ (Mᵢ(p) − Mᵢ(q)) ∂sᵢ,p/∂x_q
vanishes, which in general it does not when the models couple pixels
across the boundary. That argument is the record's ([NOTE-tmpa8ixz](../notes.d/NOTE-tmpa8ixz.md)), not
the paper's. LoRA Composite's "enabling CFG to condition on LoRAs" is text
guidance within each LoRA-modified model, not guidance toward a LoRA
([NOTE-tmphq8v2](../notes.d/NOTE-tmphq8v2.md)). The account is unchanged.
