---
status: Read
paper: LIT-tmpq1fwu
title: 'Andrieu et al. — Provable state estimation with recurrent models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from
    https://arxiv.org/pdf/2611.09217 (v1, 52 pp., NeurIPS 2026), text
    extracted with pdftotext. Read in full: the main text (§§1–7, pp.
    1–10), the references, Appendix A, Appendix H, I, J and K. Read for
    their statements and structure: Appendices D, F.1, F.3 and G. Skimmed:
    the proofs in Appendices B–E and F.2/F.4. None of the proofs was
    verified, by the reader or the filer. Figures were read from their
    captions. The filer string-matched every quotation below. Status Read
    for the paper's claims; its proofs are unchecked.
date: '2026-11-15'
summary: >-
  Treats an RNN with a readout as a discretized Neural ODE and proves,
  under contraction of the latent field, differential observability and a
  generic filter-rank condition, that it is a nonlinear KKL observer whose
  error decays like κ^ℓ e^{−κt}. Adds a decoder-size bound exponential in
  latent dimension, a noise floor of order κ^ℓ, and a discrete-time
  version. The experiments use κ = 1, outside the theorems' large-gain
  regime. The claim that trained GRUs learn contraction rests on one
  trajectory-forgetting figure.
---

<!-- inactive-ok-file: THEORY-1431 — Proposed; the reservoir THEORY the reading bears on, no note filed -->

# NOTE-tmpliu98: Andrieu et al. — Provable state estimation with recurrent models

## Contribution

Before this paper, KKL observers with existence and injectivity
guarantees had linear latent filters (Kazantzis–Kravaris; Andrieu–Praly).
The one contracting nonlinear version needed a diagonal latent field.
This paper allows dense, coupled latent Jacobians such as GRU cells, at
the price of a "filter rank" condition, which it proves generic for
single-layer analytic RNNs. It adds an explicit gain κ, a bound on
decoder size, a noise bound and an Euler-discretization result. The
authors say plainly that these are existence results, not training
guarantees.

## Key insight

A contracting dynamical system driven by observations forgets its initial
state and synchronizes to a function of the driving system's state, a
generalized synchronization. If the latent space is rich enough and the
driving system observable enough, that function is injective, so the
latent state encodes the true state. Speeding the latent dynamics up by a
gain makes the encoding converge faster, but steepens it, so the decoder
must be finer and noise is amplified.

## Assumptions

- **The plant** ẋ = f(x), o = h(x) is smooth and deterministic, with
  trajectories in a compact forward-invariant set.
- **Contraction** in the Euclidean metric (Assumption 3.2): ∂g/∂z +
  (∂g/∂z)ᵀ ≤ −2I. A constant metric is covered by a change of
  coordinates; a state-dependent metric is not.
- **Differential observability of order ℓ** (Assumption 3.5): the state
  is a Lipschitz-injective function of the output and its first ℓ
  derivatives.
- **Filter rank** (Assumption 3.6): latent dimension m ≥ p(ℓ+1), and a
  left-invertibility condition on [B, AB, …, A^ℓB] at the latent
  equilibrium.
- **A large gain**: κ > 2L_f for existence, and above an unstated
  threshold for injectivity.
- **Bounded deterministic noise** for the robustness bound.

## Key results

- **Thm 3.4** (p. 5). For κ > 2L_f, a C¹ map T_κ: X → Z exists, invariant
  (T_κ(x(t)) = z(t)) and attractive (|z(t) − T_κ(x(t))| ≤
  e^{−κt}|z0 − T_κ(x0)|). Remark 3.8 characterizes it by the nonlinear
  KKL equation ∂T_κ/∂x · f = κ g(T_κ, h), and calls it "a filtered
  version" of the observability map. The proof is the paper's own, via a
  differential-inequality lemma, and does not cite a specific lemma of
  Andrieu–Praly.
- **Thm 3.7** (p. 5): c_T κ^ℓ |T_κ(x_a) − T_κ(x_b)| ≥ |x_a − x_b|. The
  authors add (p. 6) that "nothing says that a moderate gain fails; this
  is the regime our trained models operate in".
- **Thm 4.1** (p. 6): with the exact left inverse, |x̂(t) − x(t)| ≤ c′_T
  κ^ℓ e^{−κt}|z0 − T_κ(x0)|, so the error can be made smaller than any
  precision after any given time.
- **Prop. 4.3** (p. 7): with bounded disturbances, the bound gains "the
  noise floor" 2c′_T κ^ℓ L‖δ‖∞, the high-gain effect.
- **Thm 4.2** (p. 7): a ReLU MLP decoder achieving error ε after time t_o
  needs W ≤ C (κ^ℓ/ε)^m log(κ^ℓ/ε) weights, exponential in the latent
  dimension.
- **Thm 5.3** (p. 8): the Euler-discretized residual RNN is tunable for a
  small enough step. This holds for the exact decoder only; no theorem
  combines the MLP decoder with discretization.
- **Prop. K.1** (p. 48): for a single-layer analytic RNN, the filter-rank
  condition holds for almost all weights. Genericity for gated or stacked
  cells is conjectured.
- **Contracting GRU** (App. H): contracting by construction, through
  spectral normalization and a leak α = 2.5. Measured along validation
  trajectories, the largest eigenvalue of the symmetric Jacobian part
  "averages −2.18".
- **Robot task** (§6): odometry correction over 27.4 km of indoor
  driving, 5 training runs each. The contracting GRU "does outperform the
  classical GRU and … shows a far more stable training behavior". The
  experiments use κ = 1.
- **Trained GRUs** (Fig. 3): two copies of a trained vanilla GRU, started
  apart and driven by the same inputs, converge to about 10⁻⁷ relative
  distance in 300 steps over 20 trials: "The network forgets its initial
  condition under any input."
- **Simulated oscillator** (§6, App. J; 144 models): "for every fixed
  width the error decreases up to κ ≈ 2" and then grows again. The
  authors attribute this to the κ^ℓ decoder cost.

## Concepts

- **KKL observer**: a state-to-latent map T solving the KKL equation.
- **Generalized synchronization.**
- **Contraction** (uniform monotonicity) and **the echo state property**.
- **Differential observability; filter rank.**
- **Tunability**: an error below any precision after any time, by choice
  of parameters.
- **The high-gain trade-off**: transient peaking and the noise floor.

## Connections

The work lies in the nonlinear-observer tradition of Kazantzis–Kravaris
and Andrieu–Praly. For the echo state property it cites reservoir
computing: "the echo state property [21] is essentially a contraction
assumption", and it says that injectivity and tunability do not come
with it. It treats linear SSMs (S4, LRU) as special cases. Its linear
case is a Luenberger observer, solving a Sylvester equation.

## Bearing on the record

- **[LIT-051](../literature.d/LIT-051.md) / [NOTE-062](NOTE-062.md)** (control notes: Luenberger observers, rank
  tests). The paper's linear case (Remark 3.8) is the Luenberger observer
  of those notes. Its filter-rank matrix is the latent filter's
  controllability matrix. No note filed.
- **[THEORY-773](../theory.d/THEORY-773.md)** (Del Vecchio–Slotine: a contracting fast subsystem
  tracks its slow manifold, with a robustness bound). The κ-scaled latent
  field is a fast contracting subsystem, T_κ plays the slow manifold, and
  Prop. 4.3 has the same shape as that entry's robustness lemma. The
  bearing is a resemblance of method; no note filed.
- **[THEORY-1431](../theory.d/THEORY-1431.md)** (an origami metamaterial as a reservoir computer). The
  paper gives, for contracting reservoirs, a sufficient condition for the
  readout to recover the driving system's state: injectivity under
  differential observability and filter rank. The echo state property
  alone, which reservoir results usually rest on, does not give it. No
  note filed; that THEORY concerns a mechanical reservoir's computing,
  not state recovery.

## Limitations

- **Existence only.** No result says training finds such weights, and
  enforcing the filter rank "is non-trivial" (p. 10).
- **Unstated constants.** The thresholds (the minimal κ in Thm 3.7) and
  constants are not explicit. The decoder bound is exponential in m,
  with m ≥ p(ℓ+1).
- **Theory and experiment are in different regimes.** The theorems need
  a large gain, while the robot experiments use κ = 1. Tunability is
  tested only on a 3-dimensional simulation, where error grows again past
  κ ≈ 2.
- **The "GRUs learn contraction" claim is suggested, not shown.** It
  rests on one figure of trajectory forgetting, with no Jacobian check
  for the vanilla GRU, no seed count, and no untrained baseline to
  separate "learns" from "was contracting at initialization". The
  abstract's generalization goes beyond it.
- **The robot evidence is in figures**, with 5 runs and no numbers in the
  text.
- **The theory assumes an autonomous plant**, while the robot is
  controlled; the paper covers this by assuming an exosystem.
- **The proofs were not verified** here.

## Open questions

- Does an untrained GRU of the same architecture already forget its
  initial state on this task? If so, contraction is not learned.
