---
number: 515
status: Active
formerly:
- THEORY-tmpes2tv
title: "Sampling a posterior p(x|y) when only joint samples (X, Y) can be drawn is solved by a Schrödinger bridge on the joint space, with y held fixed along the path, between the joint distribution and any reference sharing its y-marginal; the bridge averages the per-observation bridges, its first iterative-proportional-fitting step is the conditional score-based model, and the error of later steps at the data end falls as 1/n times the reference's distance from the bridge"
version: 1
tags:
- probabilistic-modeling
- mathematics
date: '2026-10-16'
source:
- LIT-776
summary: >-
  Shi, De Bortoli, Deligiannidis & Doucet (2022), [LIT-776](../literature.d/LIT-776.md), read in
  [NOTE-589](../notes.d/NOTE-589.md). Propositions 1–3 are proofs, read for structure and not
  checked line by line. The empirical gains over the conditional score
  model hold at equal, small step counts on most but not all image
  metrics, and in Lorenz-63 filtering at 20 steps. That a long noising
  horizon is not what makes conditional diffusion correct is [NOTE-589](../notes.d/NOTE-589.md)'s
  interpretation, not something the paper tests.
---


# THEORY-515: Sampling a posterior p(x|y) when only joint samples (X, Y) can be drawn is solved by a Schrödinger bridge on the joint space, with y held fixed along the path, between the joint distribution and any reference sharing its y-marginal; the bridge averages the per-observation bridges, its first iterative-proportional-fitting step is the conditional score-based model, and the error of later steps at the data end falls as 1/n times the reference's distance from the bridge

## Source

Shi, De Bortoli, Deligiannidis & Doucet (2022), "Conditional Simulation
Using Diffusion Schrödinger Bridges", UAI 2022, [LIT-776](../literature.d/LIT-776.md), read in
[NOTE-589](../notes.d/NOTE-589.md). Sections 1–8 closely; Appendix C (the proofs of Propositions
1–3) followed for structure only.

## What was actually shown

**The setting.** One can sample X ∼ p_data and Y ∼ g(·|X), and g need
not be evaluable. Densities are positive and the relevant KL divergences
finite. The bridge for one observation cannot be built, because its
posterior end cannot be sampled.

**Proposition 1.** The averaged problem, the expectation over Y of
KL(π_Y | p_Y) under both marginal constraints, is solved by the ordinary
Schrödinger bridge on X × Y between p(x, y) and p_ref(x|y)p(y), with the
y-coordinate held constant. So one network conditioned on y serves every
observation.

**Proposition 2.** The iterative-proportional-fitting iterates factor as
p(y) times conditional forward and backward chains in x, so the
diffusion-Schrödinger-bridge losses carry over with y as an input.

**Proposition 3.** For n ≥ 1, E[KL(π^{c,n}_{Y,0} | p(·|Y))] ≤ (2/n)
E[KL(π^{c,*}_Y | p_Y)]. The data-end error falls as 1/n, scaled by how
far the initial noising process is from the bridge.

**The first step.** With one IPF iteration the algorithm is the
conditional score-based model; later iterations correct it (Section 8,
Figure 2). The reference end is free, so it can be an informed guess:
an upsampled image, an EnKF Gaussian, or SRFlow's output.

**Empirically, at equal small step counts.** CelebA 4× super-resolution
with noise, N = 20: FID 92.02 (score model), 57.22 (bridge), 44.44
(score model with informed reference), 28.41 (bridge with informed
reference). Not uniform: on CelebA inpainting at N = 20 the bridge's FID
(19.85) is worse than the score model's (17.62). In Lorenz-63 filtering
with N = 20 both score-model variants diverge, while the bridge beats the
EnKF (0.178 against 0.354 at M = 2000).

What could have come out otherwise: the averaged problem need not have
reduced to one bridge on the extended space, and the iterates need not
have factored. Both are proved.

## What this does not say

- **That a long noising horizon is not what makes conditional diffusion
  correct.** That is [NOTE-589](../notes.d/NOTE-589.md)'s reading of Proposition 1. A source that
  compared horizons at fixed endpoint error would be needed.
- **That the learned networks achieve the bound.** Proposition 3 bounds
  exact IPF iterates, not trained, discretized ones.
- **That the method serves every observation well.** Training never uses
  y_obs, so atypical observations are poorly served (the authors'
  limitation).
- **That it is faster than diffusion in wall-clock terms.** Gains are at
  equal small N. Training costs roughly twice the score model's, and
  there is no comparison with distillation or fast solvers.
- **That adding conditions composes.** Nothing here composes several
  conditions; [CLAIM-123](../claims.d/CLAIM-123.md)'s conditional-independence point is untouched.

## Connections

- The denoising losses rest on the same Gaussian-channel calculus as the
  I–MMSE identity ([LIT-058](../literature.d/LIT-058.md), [THEORY-617](THEORY-617.md)). Neither paper cites the
  other.
- Classifier-free guidance ([LIT-839](../literature.d/LIT-839.md), [THEORY-611](THEORY-611.md)) also conditions by
  feeding y to the network; this paper changes the endpoints and the
  path instead of the sampler's field.
- [CLAIM-123](../claims.d/CLAIM-123.md) cites this paper as a path-space view of conditional
  transport.
