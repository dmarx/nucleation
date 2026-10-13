---
number: 711
status: Read
formerly:
- NOTE-tmpq7q6s
paper: LIT-1011
title: 'The Limiting Dynamics of SGD'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read from arXiv v4 (28 December 2023) through the PDF text layer:
    §§1–9 in full, and Appendices A (the SDE model), B (noise covariance),
    C (the quadratic assumption) and H (oscillation rates). The solutions
    and expectations derived in Appendices D–G were not checked, and
    plotted values were read from captions and text only.
date: '2026-10-13'
summary: >-
  SGD with momentum β, learning rate η, batch size S and weight decay λ is
  modelled as (η/2)(1 + β)θ̈ + (1 − β)θ̇ + λθ = −g(θ) + √(η/S) √Σ ξ(t). For
  linear regression with Σ = σ²H this is an OU process in phase space.
  Its stationary state is Gibbs on a modified loss, with inverse
  temperature κ = S(1 − β²), in broken detailed balance. Under a
  quadratic loss at the end of training the same holds for deep networks,
  and a ResNet-18 on ImageNet shows the predicted isotropy, velocity
  regularization, oscillations and speed.
---
<!-- inactive-ok-file: THEORY-108 THEORY-114 THEORY-209 — Proposed; readings this one connects to and the account filed from it, open -->

# NOTE-711: The Limiting Dynamics of SGD

## Contribution

Earlier SDE models of the end of training were first-order, assumed the
learning rate vanishes while keeping its square root finite, or argued for
a modified loss and probability currents without writing them down. This
paper lifts the dynamics into phase space, position and velocity, models
finite learning rate and batch noise together, solves linear regression
exactly, and gives explicit expressions for the modified loss, the current
and the speed. It then tests their qualitative and quantitative
consequences on a pre-trained ResNet-18.

## Key insight

Where gradient noise is anisotropic, a Langevin process does not settle
into the Gibbs distribution of the potential that drives it. It settles
into the Gibbs distribution of a different potential, and it keeps
circulating. For SGD the noise covariance tracks the Hessian, so the
modified potential undoes the Hessian's anisotropy, and the circulation
runs through the Hessian's eigen-planes. A trained network is therefore not
at a point, and not wandering the training loss. It is moving isotropically
on a different landscape, at a speed and with correlations set by the
optimizer.

## Assumptions

- **Assumption 1 (CLT).** The batch gradient minus the full gradient is
  Gaussian with covariance Σ(θ)/S. Appendix A notes that sampling without
  replacement and heavy-tailed noise both strain this.
- **Assumption 2 (SDE).** The underdamped Langevin equation, Eq. (6),
  tracks SGD: θ(ηk) ≈ θ_k, v(ηk) ≈ v_k. The finite-learning-rate
  correction is the second-order "artificial diffusion" term (η/2)(1 + β)θ̈.
- **Assumption 3 (covariance).** Σ(θ) = Σ = σ²H. It holds approximately
  for data from a noisy linear teacher (Appendix B). For deep networks it
  is an assumption.
- **Assumption 4 (quadratic loss).** At the end of training
  L(θ) = (θ − µ)⊺(H/2)(θ − µ) with H ⪰ 0. Appendix C concedes that real
  Hessians have negative eigenvalues at the end of training, "at odds with
  our assumption", and that the Hessian is low-rank. The analysis is
  restricted to the Hessian's image space, which the noise covariance
  shares.

## Key results

- **Phase-space SDE (Eq. 6).** Mass (η/2)(1 + β), friction (1 − β),
  potential L(θ) + (λ/2)‖θ‖², and fluctuating force from the gradient
  noise.
- **Linear regression is an OU process (Eqs. 7–11).** The mean is a sum
  of damped harmonic oscillators in the Hessian's eigenbasis, which matches
  CIFAR-10 linear regression closely (Fig. 2). The stationary distribution
  is N((µ, 0), κ⁻¹B), with κ = S(1 − β²) and µ = (H + λI)⁻¹b.
- **Modified loss and current (Eqs. 13–14).** Using the decomposition
  A = (D + Q)U, with Q skew-symmetric, the stationary state is Gibbs on
  Ψ = ½ x⊺Ux, and J_ss = −QUx·p_ss ≠ 0. Detailed balance is broken in phase
  space. The marginals in position alone, or velocity alone, are in
  detailed balance.
- **Isotropy (Eq. 15, Fig. 4).** Ψ_θ ∝ (θ − µ)⊺H⁻¹(H + λI)(θ − µ)/(η(1 + β)),
  which for λ ≈ 0 is isotropic on the column space of H. The ResNet-18
  trajectory, projected on the top and 30th Hessian eigenvectors
  (eigenvalue ratio about 6), covers both directions equally while the
  train and test losses are anisotropic in that plane.
- **Velocity regularization (Eq. 16, Fig. 5).** Ψ_v ∝ v⊺H⁻¹v. The projected
  velocity trajectory follows the inverse Hessian's contours.
- **Oscillations (Eq. 17, Fig. 6, App. H).** Noisy clockwise rotations in
  each eigen-plane, at rates that differ between eigenvectors, checked by
  the amplitude-weighted FFT frequency. With incommensurate rates the
  integral curves of the current fill the level sets of Ψ. The paper
  takes this to contradict the limit cycles proposed by Chaudhari and
  Soatto (2018).
- **Speed (Eq. 18, Fig. 7).** E‖δ‖² = η²σ²tr(H)/(S(1 − β²)). σ²tr(H) is
  fitted once from one run, then the formula predicts the speed across
  sweeps of η, S and β. The paper reads this as evidence the model stays in
  one quadratic basin when hyperparameters change.
- **Diffusion exponent (Eq. 19, Fig. 7).** Global displacement is a
  Brownian term plus oscillator corrections with damping ratio
  ζ_l = (1 − β)/√(2η(1 + β)(ρ_l + λ)). Overdamped modes give persistent
  velocity correlations and superdiffusion. Underdamped modes give
  anticorrelations and slower transport. Larger η lowers c. Batch size
  leaves ζ unchanged but affects c non-monotonically.

## Claims

- The anomalous limiting dynamics of deep networks have "a mechanistic
  origin": the interaction of hyperparameters, gradient-noise structure
  and the Hessian (§9). Supported for one architecture under Assumptions
  3–4, with the speed matched quantitatively and the exponent's trends
  matched qualitatively.
- "No matter how anisotropic the original training loss … the limiting
  trajectory of the network will behave isotropically" (§1). Shown in one
  two-dimensional projection of one network.

## Concepts

- **Modified loss:** the potential whose Gibbs distribution is the
  stationary state, which differs from the driving potential when the
  noise is anisotropic.
- **Broken detailed balance:** stationarity with a divergence-free but
  non-zero probability current.
- **Anomalous diffusion:** E‖Δ_t‖² ∝ t^c with c ≠ 1.
- **Phase space:** position and velocity together. Several of the results
  exist only there.

## Connections

- The anthology's [ANTH-NOTE-202](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-202.md) reads the same paper for practice, and
  [ANTH-THEORY-031](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-031.md) uses it as one way the loss curve hides training.
- [THEORY-108](../theory.d/THEORY-108.md) varies a "temperature" (learning rate, batch size, weight
  decay) and finds that connectivity predicts generalization. This paper
  gives that temperature a meaning at the end of training: κ = S(1 − β²)
  is the inverse temperature of the stationary state, and η sets the
  modified loss's scale and the damping.
- [THEORY-114](../theory.d/THEORY-114.md)'s copies spawned from a shared state differ only in SGD noise.
  This paper describes what that noise does once a run has converged.

## Bearing on the record

It bears on [QUESTION-069](../questions.d/QUESTION-069.md)'s "regime" alternative. A converged run is a
stationary distribution, not a point, and its spread, shape and
correlations depend on η, β and S. So a trained "solution" is partly a
property of the regime that produced it. It says nothing about the
connectivity between different runs. The account filed from it is
[THEORY-209](../theory.d/THEORY-209.md).

## Limitations

- **One network for the deep-learning tests.** The isotropy, velocity and
  oscillation results are a ResNet-18 with batch norm on ImageNet, in one
  two-dimensional projection on eigenvectors 1 and 30. The diffusion
  exponents of Fig. 1 cover five convnets.
- **The two assumptions that carry the result are the ones least checked
  for deep networks:** Σ ∝ H, and a positive semidefinite quadratic loss.
- **Flat directions are outside the model.** Noise and drift both vanish
  on the Hessian's null space, so the model describes motion only in its
  image. It is silent on travel along flat or symmetric directions.
- **The model's account of displacement was not checked here.** The OU
  stationary variance is bounded, so how Eq. (19) yields sustained
  power-law growth over the observed horizon depends on the slow modes.
  The derivation in Appendix G was not read.
- **The speed is fitted.** σ²tr(H) is estimated from one run and then
  held fixed, so Fig. 7 tests the scaling with η, S and β, not the
  absolute value.

## Open questions

- Does the isotropy hold in the bulk of near-zero eigenvalues, or only
  across the top thirty?
- What drives motion along the Hessian's null space, where symmetries put
  most of a network's flat directions?
- Do the same dynamics hold for adaptive optimizers, whose noise is
  preconditioned?

## Corrections

None.
