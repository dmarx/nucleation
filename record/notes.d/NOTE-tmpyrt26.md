---
status: Read
paper: 'LIT-tmpmghyl'
title: 'Single-Head Attention in High Dimensions'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v2 PDF (2 February 2026, 42 pp.), text extracted
    with pdftotext. Main text (Sections 1–6, pp. 1–12) read in full, with
    Claims 3.1 and 4.1, Corollary 3.2 and Eqs. (24)–(25) (re-extracted
    in raw mode to read the exponents). Appendix A (the nuclear-norm
    identities) followed line by line. Appendix B read through the
    proof-sketch steps, the generic multi-token matrix-sensing setting
    and the AMP algorithm; the state-evolution equations not re-derived.
    Appendices C (reduction to linear attention) and D (non-factorized
    attention) read for their results, the algebra skimmed. Appendices E
    and F (error decomposition, power-law phases) skimmed: Conjecture E.1,
    the sharp/flat-minimum split and the phase list read, the
    expansions not followed. Appendix G and Figures 6–11 read. The v1
    PDF (29 September 2025, 28 pp.) was compared for title, authors and
    section structure only.
date: '2026-10-09'
summary: >-
  In a solvable model, one tied softmax attention layer trained by
  ridge-penalized ERM on Gaussian sequences with n ∝ d² samples, derives
  (non-rigorously, by AMP and random-matrix theory) the test error,
  interpolation and recovery thresholds, and the spectrum of the learned
  query–key map, η·ReLU(S0 + δZ − ε): outliers are recovered target
  directions, the bulk is finite-sample noise, and weight decay acts as a
  nuclear norm. Power-law targets are recovered mode by mode, giving
  heavy-tailed spectra and LASSO-rate scaling laws.
---

<!-- inactive-ok-file: THEORY-tmpjhj8u — Proposed; the account this reading produces -->
<!-- inactive-ok-file: THEORY-106 — Proposed; its scope is compared with this paper's interpolation peak -->
<!-- inactive-ok-file: THEORY-085 — Proposed; named as an analogous outlier-and-bulk account -->

# NOTE-tmpyrt26: Single-Head Attention in High Dimensions

## Contribution

Before this paper, high-dimensional theory of attention covered Bayes-
optimal inference in attention-indexed models and low-rank (O(1)) attention;
there was no sharp account of what empirical risk minimization finds when
the query–key map has extensive rank. This paper gives one for a tied,
single-head softmax layer: the test error, the training loss, the
interpolation and perfect-recovery thresholds, and the full singular-value
law of the trained weights, all from one low-dimensional variational
problem. It ties the spectrum to the error term by term, and shows that
power-law targets give heavy-tailed learned spectra and power-law learning
curves.

## Key insight

With square-penalized factor weights, training one attention layer is
nuclear-norm-penalized matrix sensing in disguise, and the solution of that
problem is a spectral soft-threshold: take the target, add a semicircle of
noise whose width shrinks with the data, subtract a threshold set by the
penalty, and keep the positive part. Everything visible in trained
spectra in this model (a spike at zero, a bulk, outliers, heavy tails) is
the position of that threshold relative to the target's eigenvalues and
the noise.

## Assumptions

- **Architecture.** f(x) = σ_β((x W Wᵀ xᵀ − E_tr[·])/√(dp)) x (seq2seq) or the
  attention matrix itself (seq2lab): one head, query and key tied (W = W_Q =
  W_K), value the identity, row-wise softmax at inverse temperature β, a
  batch-centring term. The authors expect untied attention to behave
  similarly but do not treat it.
- **Data.** Each of T tokens i.i.d. N(0, I_d); universality beyond Gaussian
  data is asserted by analogy with cited results, not shown.
- **Target.** Inside the model class: softmax_β0 of
  (x_aᵀ S0 x_b − δ_ab Tr S0)/√d plus symmetric Gaussian noise of variance
  Δ/(2 − δ_ab); higher-order dependencies are modelled as that noise.
- **Loss.** Square loss plus λ‖W‖²_F (Claim 3.1 extends to losses
  depending bilinearly on the data and to spectral penalties, Appendix
  B.2.1).
- **Limit.** d, n, p → ∞ with α = n/d², κ = p/d, κ₀ = rank(S0)/d fixed, T
  finite, the spectral law of S0 converging with finite first two moments.
- **Replicon condition** (Eq. 11) at the global minimum, which licenses the
  AMP fixed point as the global minimizer; checked numerically for the
  plotted cases, not proved.
- **Sections 4–5 go beyond the limit.** The error decomposition and the
  scaling laws assume Claims 3.1 and 4.1 remain valid for any large n, d
  with λ depending on d (Conjecture E.1), and that the learned weights are
  well aligned with the target.

## Key results

- **Claim 3.1** (train and test error). With λ̃ = √κ·λ, μ_δ = μ0 ⊞ μ_sc,δ and
  J(δ, ε) = ∫_ε^∞ μ_δ(dx)(x − ε)², the global minimizer of
  Φ = (q̂Σ + 2m̂m − Σ̂q)/4 + (n/d²)·M(Σ, m, q) − (m̂²/4Σ̂)·J(√q̂/m̂, 2λ̃/m̂)
  gives lim E e_test = E Σ_ab [σ̃_β0(z0)_ab − σ̃_β(z)_ab]² and
  lim d⁻² E L = Φ*, with (z0, z) jointly Gaussian with covariance
  [[Q + Δ/2, m], [m, q]]. Holds for all α, λ > 0, Δ ≥ 0 and
  κ ≥ 1 − F_{√q̂/m̂}(2λ̃/m̂).
- **Corollary 3.2.** For λ → 0⁺, α_interp = ∂₁J(δ̄, 0)/(2δ̄(T² + T − 2)) with
  δ̄ solving Q0 + Δ/2 = J(δ̄, 0) − (δ̄/2)∂₁J(δ̄, 0); for Δ = 0, α_perf from
  Eqs. (16)–(18). Proved by reduction to linear single-token attention
  below interpolation (Appendix C), where softmax's invariance to a
  constant shift per row leaves T² + T − 2 effective constraints per
  sample.
- **Appendix A** (exact). ‖W‖²_F = ‖WᵀW‖_* for tied weights;
  ‖M‖_* = min over UVᵀ = M of (‖U‖²_F + ‖V‖²_F)/2, attained by the balanced
  SVD factorization, with no convexity needed for equality of optimal
  values.
- **Claim 4.1** (spectrum). WᵀW/√(pd) has, in law, η·ReLU(S0 + δZ − εI),
  Z ∼ GOE(d), η = m̂/Σ̂, δ = √q̂/m̂, ε = 2λ̃/m̂; its spectral density converges
  to a deterministic limit fixed by (η, δ, ε) and the law of S0.
- **Factorized against direct.** Training a symmetric S with a Frobenius
  penalty (Eq. 20) does worse at every α, at cross-validated λ for both
  (Figure 2). Noiseless, ridgeless, κ₀ → 0: ‖Ŝ − S0‖²_F = Q0(1 − 2α), so
  recovery needs α = 1/2, n = O(d²), against n = O(d·p0) factorized.
- **Error decomposition** (Eq. 23). e_test = e0 + e1, e1 = c1·E_over +
  E_under + E_approx + c2·E_mismatch, with E_over set by the bulk, E_under
  by target eigenvalues still in the bulk, E_approx by error along the
  outliers. Compared with the full theory in Figure 8 (right) and called
  "qualitative in nature" away from small error.
- **Scaling laws** (Eqs. 24–25). For S0 eigenvalues √d·i^(−γ), γ > 1/2:
  e_test = e0 + Θ((n/d)^(−1+1/(2γ)) + …) for d ≪ n ≪ d², λ ≪ √(n/d²);
  further regimes in λ with rates d²/n, (λd^(3/2)/n)^(2−1/γ) and (λd²/n)²
  (Figure 5's phase diagram). The paper says these coincide with the LASSO
  and matrix compressed-sensing rates of Defilippis et al. and, at optimal
  λ, the LASSO minimax rate n^(−1+1/(2γ)).
- **Numerics.** Adam on the loss, d = 100–400, p = d or 3d/4, 8–64 runs:
  test error, train loss and spectra match the theory (Figures 1, 4, 6, 9);
  seq2seq and seq2lab coincide; lower β gives lower error; T rescales α.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Weight decay on tied (or balanced untied) factors equals a nuclear-norm penalty on the query–key product | strong | Appendix A, proof |
| C2 | In the stated limit, the global ERM minimum's test error and train loss are given by the six-parameter variational problem | moderate | Claim 3.1: AMP/replica derivation with proof sketch, replicon checked numerically, Adam simulations agree |
| C3 | The learned query–key spectrum is η·ReLU(S0 + δZ − ε) | moderate | Claim 4.1, same derivation; histograms from Adam agree (Figures 1, 4) |
| C4 | Gradient methods reach the predicted global minima despite non-convexity | weak to moderate | Adam runs only, at d ≤ 400; no landscape argument |
| C5 | Factorized training beats direct training of the product when the target is low-rank, and needs O(d·p0) rather than O(d²) samples | moderate | Figure 2 at cross-validated λ; Appendix D for the unfactorized rate |
| C6 | Spectral outliers are learned target features and the bulk is noise; adding outliers lowers error | moderate | error decomposition (Section 4), resting on Conjecture E.1 |
| C7 | Power-law targets yield sequential mode recovery, heavy-tailed learned spectra and LASSO-rate power-law learning curves | weak to moderate | Appendix F under Conjecture E.1; Figure 4 at d = 200–400 |
| C8 | The derived spectra explain those of trained transformers | not supported here | "qualitative agreement" with cited empirical studies only |

## Method

Replace each quadratic form x_aᵀSx_b by a GOE sensing matrix (Gaussian
universality, assumed), turning ERM into multi-token generalized matrix
sensing over PSD S with penalty dλ̃·Tr S. Write an AMP whose fixed points
are the loss's stationary points: the matrix denoiser is
ϕ(ODOᵀ, Λ) = O·diag(ReLU(D_ii − 2λ̃)/Λ)·Oᵀ, a spectral soft-threshold, and
the sample-side step is a T(T+1)/2-dimensional proximal operator through the
softmax. State evolution reduces it to scalar order parameters; among its
fixed points the one of lowest training loss is taken, legitimate where
the replicon condition holds (citing Vilucchio et al.'s proof for
generalized linear models). Equations are solved by iteration with
Monte-Carlo expectations (about 60,000 CPU hours in all).

## Concepts

- **attention-indexed model**: a target whose output is a softmax of
  bilinear forms x_aᵀS0x_b of the tokens, with S0 of rank κ₀d.
- **tied attention**: query and key matrices equal, so the score matrix is
  x WWᵀ xᵀ and the effective map S = WWᵀ/√(pd) is PSD.
- **interpolation threshold α_interp**: the largest α at which the λ → 0⁺
  minimizer fits the training set exactly.
- **perfect-recovery threshold α_perf**: the smallest α at which, noiseless,
  the minimizer has zero test error.
- **replicon condition**: the stability inequality (Eq. 11) under which the
  AMP fixed point is the global ERM minimum.
- **rank collapse, bleed-out, outliers**: the paper's names for the
  stages of the learned spectrum as α grows: a delta at zero, bulk mass
  spreading, eigenvalues detached from the bulk.

## Connections

The paper extends the authors' "nuclear route" analysis of ERM in
overparameterized quadratic networks (Erba et al. 2025, the single-token
linear case, T = 1) to T tokens and a softmax, using the multi-token AMP of
Cui et al. (2024) for dot-product attention, and the Bayes-optimal analysis
of attention-indexed models (Boncoraglio et al. 2025) as its target model
and its lower bound (Figure 8, left). The nuclear-norm identity is the
standard one (Srebro and colleagues, Gunasekar et al.), applied to
attention after Kobayashi et al. (2024). Its scaling-law exponents are
taken over from Defilippis et al. (2025) for shallow networks. Empirical
targets are Martin and Mahoney's heavy-tailed spectra and Staats, Thamm and
Rosenow's random-matrix analysis of transformers (arXiv 2410.17770).

## Bearing on the record

- **Produces [THEORY-tmpjhj8u](../theory.d/THEORY-tmpjhj8u.md)**: the spectral law and the nuclear-norm
  identity, stated with their scope (one tied layer, Gaussian data,
  target in the model class, non-rigorous derivation).
- **[THEORY-106](../theory.d/THEORY-106.md)** (double-descent peak as a ridgeless divergence in
  random-features regression). This paper has an interpolation peak too, at
  an analytically located α_interp, which shrinks as λ grows (Figure 6). It
  calls the peak "oddly asymmetric", "distinct from the usual cusp-like
  shape", and, in Appendix G, says the simulations "suggest a large but
  finite interpolation peak at small regularization". Its model learns
  features, so it is outside [THEORY-106](../theory.d/THEORY-106.md)'s random-features scope and
  neither meets nor fails its promote_when. But if a finite ridgeless
  peak held up, that would be a peak at the interpolation threshold that is
  not a divergence, which is worth noting beside [THEORY-106](../theory.d/THEORY-106.md). The paper
  does not derive the λ → 0⁺ height; "finite" rests on simulations down to
  λ = 10⁻⁵ and a solver it says performs poorly near the threshold.
- **[LIT-672](../literature.d/LIT-672.md)** (Martin and Mahoney). This paper derives, in one solvable
  model, the kind of spectrum the Martin–Mahoney line measures, and its
  heavy tails come from accumulated recovered modes of a power-law target,
  not from a self-regularization mechanism. It cites their later papers,
  not [LIT-672](../literature.d/LIT-672.md).
- **The outlier-and-bulk accounts of the information-geometry line**
  ([THEORY-085](../theory.d/THEORY-085.md), [LIT-617](../literature.d/LIT-617.md), [LIT-619](../literature.d/LIT-619.md)) explain Fisher and Hessian outliers by
  class structure. Here outliers in the *weights* are recovered target
  directions and the bulk is finite-sample noise. The analogy is mine,
  not the paper's, and the matrices differ.
- **[THEORY-169](../theory.d/THEORY-169.md)** (attention as an in-context learner) concerns what a
  fixed attention layer does with a context. This paper is about training
  the layer's weights across samples, and does not bear on it.
- The factorized-versus-direct comparison and the scaling-law regimes are
  material for ML practice; hence `anthology-candidate` on the LIT. No
  practice is drawn here.

## Limitations

- Claims, not theorems. The authors list the proof steps still needed
  (multi-token Gaussian universality, the multi-token AMP upper and lower
  bounds) and expect no roadblock, but they are not done.
- Isotropic Gaussian tokens, one tied head, identity values, a target
  inside the model class with higher-order structure modelled as noise:
  the paper names these as its main simplifications.
- Sections 4–5 rest on Conjecture E.1 (validity outside the strict
  scaling limit), supported only by numerics; Appendix E.1 leaves the
  excess risk in one regime "as future work".
- Agreement with real transformer spectra is qualitative and unquantified.
- Global minima are checked against Adam only at d ≤ 400.

## Open questions

- Is the ridgeless interpolation peak finite in this model, as Appendix G
  suggests? A λ → 0⁺ limit of Φ at α_interp would settle it, and would say
  whether [THEORY-106](../theory.d/THEORY-106.md)'s divergence is special to random features.
- Does untied attention, or more than one head, keep the ReLU-thresholded
  law? The untied nuclear-norm identity (Appendix A, Case 2) suggests so,
  but the spectral claim is only for tied weights.
- A rigorous proof of Claims 3.1 and 4.1 for T ≥ 2, extending the T = 1
  results it builds on.
