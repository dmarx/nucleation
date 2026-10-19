---
number: 805
status: Read
formerly:
- NOTE-tmps14xd
paper: LIT-940
title: 'Defilippis et al. — Optimal scaling laws in learning hierarchical multi-index models'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2602.05846v1, 5 February 2026,
    27 pages), text extracted with pdftotext: §§1–5 and Appendices A–C,
    with the proofs of Theorems 3.2, 3.6 and 3.8, Lemmas C.2 and C.5 and
    Corollary C.4 followed line by line, and every figure caption. The
    external theorems the proofs invoke were taken as stated: Kovačević
    et al. (2025), Theorems 4.1–4.2; Barbier et al. (2019); Rudi and
    Rosasco (2017), Theorem 1. Some displayed equations extract out of
    order and were reconstructed from context.
date: '2026-10-14'
summary: >-
  For Gaussian inputs, n = αd samples, and a target Σ_k a_k g_k(⟨w_k, x⟩)
  with even links and a_k ~ k^(−γ), direction k becomes weakly recoverable
  at α_k = Θ(a_k^(−2)) = Θ(k^(2γ)) for γ > 1/2. The Bayes-optimal weighted
  subspace error is Θ(α^(−1+1/(2γ))) before α ≍ m⋆^(2γ) and Θ(m⋆/α) after.
  A target-agnostic spectral estimator attains both, and a two-layer net
  given that estimator as its first layer, with a ridge readout, attains
  them in excess risk. The cascade is in sample size. The link to
  gradient descent is a remark.
---
<!-- inactive-ok-file: THEORY-204 THEORY-201 THEORY-180 THEORY-039 — Proposed; the account filed from this reading and the accounts of acquisition thresholds it is set beside -->

# NOTE-805: Defilippis et al. — Optimal scaling laws in learning hierarchical multi-index models

## Contribution

The paper gives exact information-theoretic rates for recovering the
relevant subspace of a hierarchical multi-index target in the
proportional high-dimensional limit. It proves that a simple spectral
estimator, which does not know the target, attains them, and that a
two-layer network built on that estimator attains them in excess risk.
Earlier heuristic results for quadratic networks become theorems for any
link of generative exponent two.

## Key insight

Each direction of the target is an independent weak signal of strength
a_k inside the label. In a label-weighted covariance matrix it becomes a
spike that leaves the bulk when α·a_k² is of order one. Because the a_k
decay as a power law, the spikes leave one at a time as data grows. The
error is the error on the directions already out plus the weight of those
still in.

## Assumptions

- **Data (Def. 2.2).** x ~ N(0, I_d/d); y = f⋆(x) + √Δ ξ, with Gaussian
  label noise.
- **Target (Def. 2.1).** f⋆(x) = Σ_(k=1)^(m⋆) a_k g_k(⟨w_k, x⟩).
  - The w_k are orthogonal with ‖w_k‖² = d.
  - a₁ > a₂ > … with Σ a_k² = 1.
  - "Scale-free" means a_k = Θ(k^(−γ)). For γ < 1/2 the coefficients
    are rescaled by m⋆^(γ−1/2).
- **Links (Assumption 2.3).**
  - Each g_k is even, so E[z | y] = 0 and no linear signal exists.
  - |g_k(z)| ≤ C(1 + |z|^b).
  - E[g_k²] and |E[g_k″]| are bounded above and below uniformly in k.
    This is generative exponent 2, which makes each index detectable at
    n = Θ(d).
- **Regime.** n, d → ∞ with α = n/d fixed, then α, m⋆ ≫ 1. m⋆ is large
  but small against n and d. The rates are Θ statements in α and m⋆.
- **Spectral estimator (Assumption 3.4).** The label preprocessing T is
  bounded, with a finite supremum τ, and is not almost surely zero.
- **Network result (Thm. 3.8).**
  - The g_k are polynomials of finite degree.
  - σ is bounded and continuous.
  - The width is p = ω(n^(1/2)) and the ridge is λ = Θ(n^(−1/2)).
  - Training is Algorithm 1, not gradient descent.

## Key results

- **Theorem 3.2 (optimal rates).** For α, m⋆ ≫ 1,
  - MMSE_γ = Θ(α^(−1+1/(2γ))) for γ > 1/2 and α ≪ m⋆^(2γ);
  - Θ(m⋆/α) for γ > 1/2 and α ≫ m⋆^(2γ), once every direction is out;
  - Θ(1) for γ < 1/2 and α ≪ m⋆;
  - Θ(m⋆/α) for γ < 1/2 and m⋆ ≪ α.

  The k-critical (weak recovery) threshold is
  α_k^Bayes = Θ_k(k^(2γ) m⋆^((1−2γ)₊)) (Eq. 13), that is, Θ(a_k^(−2)).
  - **Proof, lower bound (App. A.1).** An oracle that knows every other
    direction reduces each index to a single-index model with SNR a_k².
    Barbier et al.'s formula and Corollary C.4 then give α_IT = Θ(λ^(−1))
    and mmse = O(1/(λα)) at small SNR λ.
  - **Proof, upper bound.** The spectral method (App. A.2).
- **Theorem 3.6 (spectral estimator).** The top-r eigenvectors of
  T = Σ_i T(y_i) x_i x_iᵀ have weighted error Θ(MMSE_γ) and thresholds
  α_k^sp = Θ(α_k^Bayes). Here r is set by an eigengap cutoff C/√d,
  "reminiscent of the 'elbow' method". Because every g_k is even,
  G(y) = E[zzᵀ − I | y] is diagonal (Eq. 44). So each spike correlates
  with one w_k only, with overlap m_kk² = 1 − Θ(a_k^(−2)/α) once
  α ≫ α_k (Eq. 72).
- **Error decomposition (after Thm. 3.6).**
  - k_α ≍ min(α^(1/(2γ)), m⋆) directions are weakly learnable at α.
  - The error is k_α·Θ(α^(−1)), from the learned directions, plus
    Θ(Σ_(k>k_α) a_k²), from the unlearned ones.
- **Theorem 3.8 (two-layer network).** Algorithm 1 first computes the
  spectral estimator on one half of the data and sets W = ZŴ, with Z
  random. It then fits the readout by random-feature ridge regression on
  the other half. Its excess risk is R_NN = Θ(MMSE_γ) + O(n^(−1/2)). This
  is not shown to be the Bayes risk (Remark 3.9).
- **Experiments.** d = 1000, m⋆ = 10 or 20, γ = 1.3, three links.
  - The weighted MSE crosses from α^(−1+1/(2γ)) to the 1/α rate near
    α ≍ m⋆^(2γ) ≈ 400 (Fig. 1).
  - Spikes leave the bulk one by one at α = 5, 164, 611 and 1638 (Fig. 2).
- **Remark 3.5 (link to gradient descent).** With a "slightly modified"
  loss, T is the Hessian of the loss (Bonnaire et al. 2025). Early
  gradient descent on the first layer from a small sphere is a power
  iteration w ← (I − a_k σ″(0) T)w (Eqs. 17–18, Zhang et al. 2025). This
  is cited, not proved here.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Direction k of a scale-free hierarchical multi-index target becomes weakly recoverable at n = Θ(k^(2γ) d), for γ > 1/2 | strong | Theorem 3.2 with Theorem 3.6, App. A, C |
| C2 | The optimal weighted subspace error scales as α^(−1+1/(2γ)), crossing to 1/α once all m⋆ directions are out | strong | Theorem 3.2 |
| C3 | A target-agnostic spectral estimator attains the optimal rates and thresholds | strong | Theorem 3.6, resting on Kovačević et al. |
| C4 | A two-layer network can attain them in excess risk | moderate | Theorem 3.8, for Algorithm 1 only, polynomial links |
| C5 | Gradient descent from small initialization follows the spectral estimator | weak | Remark 3.5, cited |
| C6 | The resulting weight spectra explain heavy-tailed spectra in trained networks | weak | §5, qualitative |

## Method

The paper is theory. Its proofs combine three things:
- a Bayes-optimal analysis of single-index models, by the replica-
  symmetric free entropy of Barbier et al. (2019), expanded at small SNR
  (App. C);
- random-matrix asymptotics of spectral estimators for multi-index
  models (Kovačević et al. 2025);
- random-feature ridge regression bounds (Rudi and Rosasco 2017).

## Concepts

- **Hierarchical (scale-free) multi-index model.** A sum of single-index
  tasks with power-law weights a_k ~ k^(−γ). It is quasi-sparse for
  γ > 1/2.
- **k-critical threshold.** The smallest α at which an estimator has
  non-vanishing overlap d^(−1)|⟨ŵ_k, w_k⟩| = Θ(1) with direction k
  (Def. 2.6).
- **Weighted MSE.** MSE_γ(W) = Σ_k a_k² mse_k(w_k), with mse_k the
  matrix error ‖wwᵀ − w_kw_kᵀ‖²_F/d² (Defs. 2.5, 2.7).
- **Representation-limited.** The labels depend on an unknown
  low-dimensional subspace, and finding it is the bottleneck.

## Connections

It generalises Defilippis et al. (2025b), heuristic rates for quadratic
networks, to any link of generative exponent two. It benchmarks the
one-pass SGD analyses of Ren et al. (2025) and Ben Arous et al. (2025) on
the same targets. It notes that the rates coincide with LASSO's minimax
rates for quasi-sparse recovery (Raskutti et al. 2011). Its spectral
transitions are the multi-index form of the BBP-type weak-recovery
transitions of Mondelli and Montanari (2019) and Lu and Li (2020).

## Bearing on the record

- **[QUESTION-039](../questions.d/QUESTION-039.md).** It answers in part, in one model class. The *order*
  is the order of the target's coefficients a_k, a property of the task,
  not of the input distribution, which here is isotropic. The *moment*
  is a sample count, n_k = Θ(a_k^(−2) d). Each acquisition is a sharp
  transition in the high-dimensional limit, of one kind: a spike leaving
  a random-matrix bulk. Held as [THEORY-283](../theory.d/THEORY-283.md).
- **[THEORY-229](../theory.d/THEORY-229.md), filed today from [LIT-242](../literature.d/LIT-242.md).** Both accounts acquire the top
  eigenvectors of a data matrix one at a time, in order of signal
  strength. They differ in the axis.
  - [THEORY-229](../theory.d/THEORY-229.md) fixes the data and gives a time in training,
    τ_j ≈ −log(s_j(0)²γ_j)/(8γ_j), which depends on initialization.
  - This paper fixes nothing about training and gives a sample size at
    which direction k becomes recoverable at all, by any estimator.
  - Remark 3.5 is the only bridge: early gradient descent on the first
    layer from small initialization is a power iteration on T. That is
    the same small-initialization spectral mechanism as [THEORY-229](../theory.d/THEORY-229.md)
    (and [THEORY-187](../theory.d/THEORY-187.md)). Read together, they say the
    eigenvalue sets both when a direction can be learned and how long
    gradient descent takes once it can. Neither paper proves that
    composite.
- **[THEORY-204](../theory.d/THEORY-204.md) and [THEORY-201](../theory.d/THEORY-201.md).** The threshold has the same form as the
  horizon there: a signal of strength s is detectable once n·s² is of
  order one. With s = a_k ~ k^(−γ) that gives n_k ~ k^(2γ). With pairwise
  correlation ~ t^(−β) it gives P ~ t^(2β). Here it is a theorem, for
  Gaussian inputs and independent directions. There it is an assumption,
  for real text. This is an analogy of form, not a derivation of
  [THEORY-204](../theory.d/THEORY-204.md).
- **[THEORY-180](../theory.d/THEORY-180.md).** The same school's attention result: the trained map's
  outliers are recovered directions and its bulk is noise. This paper's
  spike-and-bulk picture is the multi-index analogue for a two-layer
  network.
- **[LIT-940](../literature.d/LIT-940.md)'s seeded claims need two corrections.**
  - The abstract and the LIT summary say the features "are learned in
    sequence through a cascade of phase transitions". The sequence is in
    *sample size*, not training time. The paper analyses no training
    trajectory.
  - The summary says the spectral estimator is read "as the
    small-learning-rate limit of gradient descent". That is Remark 3.5,
    which cites other work. The network theorem is for a spectral
    initialization followed by ridge regression, not for gradient
    descent.
- **No instruction for machine-learning practice.**

## Limitations

- The inputs are isotropic Gaussian. The directions are orthogonal, and
  their links are even and separable, so G(y) is diagonal. That
  factorisation is what lets the directions be read off one by one (§4),
  and the paper says general multi-index interactions "can be arbitrary
  complicated".
- The network result is for Algorithm 1, with a data split. Whether
  SGD without spectral initialization attains the rates is left open
  (§5).
- The risk rate is not shown to be the Bayes risk (Remark 3.9).
- The rates hold for α, m⋆ ≫ 1 after the proportional limit, with m⋆
  small against d. The regime m⋆ = O(d) of the quadratic analysis is not
  covered.
- Lemma C.2 is given as a "condensed derivation".

## Open questions

- Does gradient descent from small initialization on the full network
  reach direction k at the sample size n_k and at a training time set by
  a_k? A proof that joined Remark 3.5 to a time-to-escape analysis would
  close it.
- What happens when directions interact (non-separable link, odd
  components)? Then G(y) is not diagonal, and the order need not follow
  a_k.
