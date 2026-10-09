---
status: Read
paper: 'LIT-tmplnel0'
title: 'Conditional Simulation Using Diffusion Schrödinger Bridges'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v2 (26 June 2022, 29 pages, text layer), the UAI 2022
    camera-ready. Main text, Sections 1–8, read closely, with Tables 1–4
    checked against the layout text. Supplementary skimmed: Appendix B
    (unconditional DSB recalled), C (proofs of Propositions 1–3) followed
    for structure and the results they cite, not checked line by line;
    D (Proposition 4, justifying the losses), E (continuous-time CSGM and
    CDSB, evidence estimation), F (forward-backward sampling) and G
    (experimental settings, Tables 5–6) skimmed. Formulas damaged by text
    extraction (Proposition 3's 2/n factor) were read from context.
    Figures are described from captions and prose only.
date: '2026-10-09'
summary: >-
  Posterior sampling p(x|y) when only joint samples (X, Y) can be drawn,
  recast as a Schrödinger bridge on the extended space between the joint
  p(x, y) and a reference p_ref(x|y)p(y) in which y is held fixed
  (Proposition 1), and solved by iterative proportional fitting with
  learned forward and backward drifts (CDSB). Its first iteration is the
  ordinary conditional score-based model, so the rest refine it; the
  reference can be an informed guess (upsampled image, EnKF, SRFlow)
  rather than noise. Better than the conditional score model at equal,
  small numbers of steps on most but not all image metrics, and it filters
  Lorenz-63 with 20 steps where the score model diverges.
---

# NOTE-tmp2aqt4: Conditional Simulation Using Diffusion Schrödinger Bridges

## Contribution

An amortized Schrödinger-bridge formulation of conditional simulation and
an algorithm for it. Before it, De Bortoli et al. (2021) had used
Schrödinger bridges to shorten unconditional diffusion generation, and
conditional score-based models (CSGMs) sampled posteriors by running a
long noising diffusion in reverse. After it, the bridge can be posed
between a joint distribution and a reference that shares its y-marginal,
the reference can depend on y, and the same machinery samples posteriors
in super-resolution, inpainting, a Bayesian inverse problem and
sequential filtering, using only the ability to simulate (X, Y).

## Key insight

A diffusion model must run long enough to forget the data so its reverse
can start from pure noise. A Schrödinger bridge removes that requirement:
it is the process closest in KL to the noising process that hits the data
distribution at one end and the reference at the other exactly, whatever
the horizon. For conditional simulation, the bridge for one observation
cannot be built because the posterior cannot be sampled, but the bridge
between the joint p(x, y) and p_ref(x|y)p(y), with y frozen along the
path, can, and it is the average over y of the per-observation bridges.
So one network conditioned on y serves every observation, and since the
reference end is free, it can start from a cheap approximation to the
posterior rather than from noise.

## Assumptions

- **Simulation access only**: one can sample X ∼ p_data and Y ∼ g(·|X);
  g need not be evaluable.
- **Positive densities** with respect to Lebesgue measure throughout
  (footnote, Section 2.1).
- **Finite KL**: Proposition 1 needs KL(π̄*|p̄) < ∞; Proposition 2 needs
  KL(p_join ⊗ p_jref | p̄₀,N) < ∞.
- **Gaussian transitions with small steps**: the reverse kernels are
  approximated as N(x; B(k + 1, x′), 2γₖ₊₁ I), a Taylor-expansion
  approximation, with learned mean networks B and F.
- **Same y-marginal at both ends**: p_jref(x, y) = p_ref(x|y) p_obs(y).
- **Typical observations**: training never uses y_obs, so the posterior
  approximation can be unreliable when y_obs is atypical under p_obs
  (Section 8, the authors').
- **Continuous-time results** (Proposition 5) add a drift condition on a
  dominating Langevin reference; stated, not used in the experiments.

## Key results

- **Proposition 1.** The conditional SB problem (4), the average over
  Y ∼ p_obs of KL(π_Y|p_Y) under the two marginal constraints, is solved
  by the SB (5) on the extended space between p_join and p_jref with the
  y-coordinate held constant: π̄* = π^{c,*} ⊗ p̄_obs.
- **Proposition 2.** The IPF iterates for (5) factor as p̄_obs times
  conditional forward and backward Markov chains in x given y, so DSB's
  mean-matching losses carry over with y as an extra input (Eqs. 6–7).
- **Proposition 3.** For n ≥ 1, E[KL(π^{c,n}_{Y,0} | p(·|Y))] ≤ (2/n)
  E[KL(π^{c,*}_Y | p_Y)]: the IPF iterate's error at the data end falls
  as 1/n, scaled by how far the initial noising process is from the
  bridge, which is the argument for a y-dependent forward process.
- **First iteration = CSGM** (Section 8, Figure 2): with one IPF step the
  algorithm is the conditional score model; later steps correct it.
- **2D examples (Figure 2)**, from Kovachki et al.: CDSB, with about 6×
  fewer parameters than the monotone-GAN baseline and N = 50, gives
  sharper posteriors closer to the truth; more iterations correct CSGM's
  bias; forward-backward sampling helps further.
- **BOD inverse problem (Table 1):** posterior mean, variance, skewness and
  kurtosis of two parameters against 6 × 10⁶-step MCMC; CDSB variants
  closer than MGAN and inverse transport on most statistics.
- **Images (Table 2)**, PSNR/SSIM(/FID) at small N: CDSB-C is best or tied
  in most cells. CelebA 4× SR with noise, N = 20: FID 92.02 (CSGM), 57.22
  (CDSB), 44.44 (CSGM-C), 28.41 (CDSB-C). Not uniform: on CelebA
  inpainting at N = 20 CDSB's FID (19.85) is worse than CSGM's (17.62); on
  MNIST inpainting at N = 20 CDSB's SSIM (0.657) is below CSGM's (0.706);
  on CelebA inpainting CSGM-C's PSNR is slightly above CDSB-C's at both N.
- **SRFlow as reference (Table 3, CelebA 8× SR):** CDSB-C with N = 10
  lowers FID from 30.92 (SRFlow alone) to 15.00, at a lower PSNR (24.34
  against 24.83).
- **Lorenz-63 filtering (Table 4)**, RMSE to particle-filter means (10⁶
  particles), 10 runs: with N = 20 both CSGM variants diverge, while CDSB
  and CDSB-C beat the EnKF (e.g. 0.178 against 0.354 at M = 2000). With
  N = 100 the methods are close: CSGM-C (long) 0.210 against CDSB-C
  (long) 0.218 at M = 500.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Conditional simulation is a Schrödinger bridge on the joint space with y frozen | strong (proof) | Proposition 1, C.1 |
| C2 | IPF for it reduces to conditional forward/backward chains trainable by DSB's losses | strong (proof), given the Gaussian small-step approximation | Propositions 2, 4 |
| C3 | Starting the forward process near the bridge speeds IPF convergence | moderate: an upper bound, 2/n times the initial KL | Proposition 3, C.3 |
| C4 | CDSB samples posteriors better than CSGM at the same small N | moderate: most metrics on four image tasks, 2D and BOD; exceptions in Table 2 | Tables 1–2, Figure 2 |
| C5 | An informed reference p_ref(x\|y) helps, and can be non-Gaussian | moderate | Tables 2–4 |
| C6 | Score-based filtering in a state-space model is feasible from simulation alone | moderate: one model (Lorenz-63), basis-function regression, 5 IPF iterations; instability at M = 200 | Table 4, Appendix G |
| C7 | "CDSB-C achieves the lowest error consistently" in filtering | weak: CSGM-C (long) is lower at M = 500 and level at M = 1000 | Table 4 |

## Method

1. Draw (X₀, Y) from the joint by sampling X₀ from data and Y ∼ g(·|X₀),
   and run the current forward chain in x with y fixed; fit the backward
   mean network B_θ(k + 1, x, y) by the DSB mean-matching loss (Eq. 6).
2. Draw (X_N, Y) from the reference, p_ref(x|y)p_obs(y), run the backward
   chain, and fit the forward mean network F_φ(k, x, y) (Eq. 7).
3. Alternate for L IPF iterations (Algorithm 1); the first backward fit is
   the CSGM.
4. To sample p(x|y_obs): draw X_N ∼ p_ref(·|y_obs) and run the backward
   chain with y = y_obs. Variants: CDSB-C (a y-dependent reference such as
   an upsampled y, an EnKF Gaussian, or SRFlow), and CDSB-FB
   (forward-backward: push a joint sample forward to time N, then back
   with y_obs, after Spantini et al.'s error-cancelling transport).

## Concepts

- **conditional simulation**: sampling the posterior p(x|y_obs) ∝
  p_data(x)g(y_obs|x) given only the ability to simulate (X, Y).
- **Schrödinger bridge (SB)**: the path measure closest in KL to a
  reference process with both end marginals prescribed; its static form is
  entropy-regularized optimal transport, quadratic cost when the reference
  is Gaussian.
- **conditional SB (CSB)**: the averaged problem (4), equivalently the SB
  (5) on X × Y with y constant.
- **IPF**: alternating KL projections onto each marginal constraint
  (Sinkhorn in the discrete case).
- **half-bridge**: one IPF iterate's forward or backward process.

## Connections

The algorithm is De Bortoli, Thornton, Heng and Doucet's Diffusion SB
(2021) with y added as an input; IPF is Kullback's. Conditional transport
maps between joints with equal y-marginals are Marzouk et al. (2016) and
Spantini et al. (2022), the source of the forward-backward trick; CDSB is
their stochastic counterpart. Earlier SB methods for Bayesian inference
(Bernton et al. 2019, Reich 2019) need an evaluable unnormalized posterior,
which CDSB does not. Baselines are CSGMs (Saharia et al., Batzolis et al.,
Tashiro et al.), the monotone GAN of Kovachki et al., and the EnKF.

## Bearing on the record

- **No THEORY touched.** The record holds no account of Schrödinger
  bridges, diffusion generative models or optimal filtering. Its optimal-
  transport entry, [LIT-680](../literature.d/LIT-680.md) ([NOTE-543](NOTE-543.md)), uses OT to align network weights,
  an unrelated use of the same mathematics.
- **[LIT-058](../literature.d/LIT-058.md).** The record's I–MMSE reading is the information-theoretic
  side of the same Gaussian-channel calculus whose score identity drives
  the denoising losses here; neither paper cites the other.
- **[LIT-tmpdztrs](../literature.d/LIT-tmpdztrs.md) ([NOTE-tmpq1itu](NOTE-tmpq1itu.md)).** Both condition a diffusion model by
  feeding the condition to the network, and both have classifier-free-style
  null conditioning available (Appendix E.3 here, for estimating the
  evidence log p(y_obs)). Composable Diffusion composes conditions in the
  sampler; this paper changes the endpoints and the path instead.
- **THEORY candidate (not filed):** "Posterior sampling from simulation
  alone is a Schrödinger bridge between the joint and a reference sharing
  its y-marginal, so a long noising horizon is not what makes conditional
  diffusion correct; the matched endpoints are." Proposition 1 proves the
  first half; the second half is an interpretation that would need a
  source comparing horizons at fixed endpoint error.
- **Anthology.** The practical content (start the reverse process from a
  cheap posterior approximation, a pre-trained super-resolution model or
  an upsampled input, and refine with a short bridge; forward-backward
  sampling) is machine-learning practice and is anthology material, hence
  `anthology-candidate`. The filtering and BOD experiments are
  probabilistic modelling outside deep learning and belong here.

## Limitations

- The smallest usable N depends on the steepness of the IPF drifts, which
  is unknown in practice (the authors').
- Amortized over p_obs: atypical observations are poorly served, and
  neighbourhood-based fixes from ABC are not attempted (the authors').
- Each filtering step solves a new bridge; there is no amortized filter.
- Training cost roughly doubles relative to CSGM, since both F and B are
  learned (Appendix G).
- Gains over CSGM are at equal small N; there is no wall-clock comparison
  with long-horizon diffusion or with distillation and fast solvers, which
  the authors call complementary.
- Filtering instability at ensemble size M = 200 with long diffusions,
  conjectured to be overfitting (Appendix G).
- Proposition 3 bounds only the data-end marginal error of exact IPF
  iterates, not the error of the learned networks.

## Open questions

- An amortized CDSB filter that does not solve a bridge per time step.
- A conditional multi-marginal SB (the authors' suggestion).
- How to train for atypical y_obs, e.g. by local simulation around it.
- Error bounds for the learned, discretized iterates rather than exact IPF.
