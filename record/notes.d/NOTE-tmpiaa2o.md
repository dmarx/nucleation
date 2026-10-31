---
status: Read
paper: LIT-tmpwzrx7
title: 'Mandt, Hoffman & Blei — SGD as approximate Bayesian inference'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 1704.04289v2 (19 January 2018),
    35 pp., which is the JMLR 18 (2017) typeset version (CC-BY 4.0), fetched
    2026-10-31. Text extracted with `pdftotext -layout`; page numbers are the
    JMLR ones. I read the abstract, §§1–8, Appendices A–G and the reference
    list. The figures' content did not survive extraction; their captions
    and Table 1 did. I checked numerically (numpy and scipy, my own scripts,
    not the authors' code): Theorem 1's optimal rate against a direct
    minimisation of the KL over ε (agreement to 10⁻⁶ relative); Corollary 4
    (the full preconditioner gives the posterior covariance exactly); that
    under Assumption 5 scalar SGD's stationary covariance is ε/(2S)·I;
    Eq. 25 for momentum against the exact stationary covariance of the
    discrete recursion (error 0.07% to 4%, falling with ε); the discrete
    SGD covariance against Eq. 13 (5% at ε = 5 × 10⁻³ by simulation); and
    Eqs. 30–31 for iterate averaging under Assumption 5 against the exact
    covariance of the mean of T stationary iterates (error about
    1/(Tελ_min), 1% at T = 50,000).
date: '2026-10-31'
summary: >-
  Constant-rate SGD, modelled near a minimum with positive-definite Hessian
  A and constant gradient-noise covariance BBᵀ as an Ornstein–Uhlenbeck
  process, has a Gaussian stationary distribution with covariance solving
  AΣ + ΣA = (ε/S)BBᵀ. Choosing the rate, batch and preconditioner to
  minimise KL to the Gaussian posterior gives closed forms, and the
  preconditioner (2S/εN)(BBᵀ)⁻¹ matches the posterior at sample size N
  exactly. The paper is about the stationary regime of a regular model in
  one basin: it sets the search phase aside, and nothing in it relates
  training time to sample size beyond iterate averaging, whose covariance
  falls as 1/(examples processed).
---
<!-- inactive-ok-file: QUESTION-tmpiir0l QUESTION-039 THEORY-209 THEORY-tmp8ggnh — Open or Proposed; the question this reading bears on, the one it refines, Kunin's deep-network reading, and a sibling filed today -->

# NOTE-tmpiaa2o: Mandt, Hoffman & Blei — SGD as approximate Bayesian inference

## Contribution

It turns the old observation that constant-rate SGD "first marches toward
an optimum ... and then bounces around its vicinity" (p. 2) into a
calculation. Under four assumptions SGD is a multivariate
Ornstein–Uhlenbeck (OU) process with an analytic Gaussian stationary
distribution, and the KL divergence from that distribution to a Gaussian
posterior can be minimised over the optimiser's tuning parameters in
closed form. Out of this come optimal constant rates and preconditioners
(Theorems 1–2, Corollary 3), a proof that full preconditioning by the
inverse noise covariance samples the posterior exactly (Corollary 4), a
variational EM scheme (§4.2), the stationary law of SGD with momentum
(§4.3), the bias of constant-rate SGLD and of diagonal SGFS (§5), and a
short proof of Polyak averaging's optimality with a sampler built on it
(§6). The 2016 ICML paper (LIT-tmpxo5z5, NOTE-tmph1our) is the first half of this one.

## Key insight

The optimiser's settings choose a distribution, not only a point. With a
quadratic loss and constant noise the stationary covariance is fixed by
AΣ + ΣA = (ε/S)BBᵀ, so Σ scales with ε/S, and the posterior's covariance
A⁻¹/N scales with 1/N. Matching the two is matching ε/S to 1/N, with the
noise covariance setting the shape. In this regime the knob that plays
the part of sample size is the noise scale, not training time.

## Assumptions

The OU model rests on four assumptions (§3.2, pp. 6–7), and the averaging
sampler on a fifth (§6.2, p. 18).

- **A1, Gaussian gradient noise.** ĝ_S(θ) ≈ g(θ) + S^(−1/2)Δg(θ), with
  Δg ~ N(0, C(θ)), by the central limit theorem.
- **A2, constant noise covariance.** C(θ) ≈ C = BBᵀ, justified "when the
  iterates of SGD are confined to a small enough region around a local
  optimum" (p. 7).
- **A3, the continuous-time limit.** The update is replaced by
  dθ = −g(θ)dt + √(ε/S) B dW, justified if "the gradients or the learning
  rates are small enough that the discretization error becomes
  negligible" (p. 7).
- **A4, a quadratic loss with positive-definite Hessian.**
  L(θ) = ½θᵀAθ, "We also assume that A is positive definite" (p. 7). The
  posterior is then the Gaussian f(θ) ∝ exp(−(N/2)θᵀAθ) (Eq. 14). This
  excludes singular models: no flat directions at the optimum, a single
  basin, and a Gaussian posterior.
- **C full rank** (p. 8), "enforced easily by adding very low-magnitude
  isotropic artificial Gaussian noise".
- **A5, Bernstein–von Mises and a well-specified model** (p. 18): the
  posterior is Gaussian and A = BBᵀ, Fisher equal to Hessian.

The paper is explicit that the assumptions fail early in training. It
describes three regimes: a search phase in which "assumptions 1–4 are
often violated and it is hard to say anything general"; a directed
approach in the quadratic region; and stationary sampling (p. 8). Its
results concern the third.

## Key results

- **Eq. 13 (stationary covariance).** The OU process dθ = −Aθdt +
  √(ε/S) B dW has stationary law N(0, Σ) with ΣA + AΣ = (ε/S)BBᵀ
  (derived in App. B).
- **Theorem 1 (constant SGD).** The KL-optimal constant rate is
  ε* = 2(S/N)·D/tr(BBᵀ) (Eq. 15). Only ε/S enters. Checked: a direct
  numerical minimisation of KL(q‖f) over ε, with a random 4 × 4 A and BBᵀ,
  agrees with the formula to 10⁻⁶ relative.
- **Theorem 2 and Corollary 4.** The KL-optimal preconditioner is
  H* = (2S/εN)(BBᵀ)⁻¹ (Eq. 17), and with it Σ = A⁻¹/N, the posterior
  covariance, so the KL is zero. Checked: |Σ − A⁻¹/N| ≤ 10⁻¹⁷.
- **Corollary 3.** The optimal diagonal preconditioner is
  H*_kk = 2S/(εN·(BBᵀ)_kk), the inverse diagonal of the noise covariance,
  which the paper relates to AdaGrad and RMSProp (p. 12).
- **Momentum (§4.3, App. D).** With damping μ, the stationary covariance
  satisfies ΣA + AΣ = (ε/(μS))BBᵀ (Eq. 25): "adding momentum only changes
  the scale of the covariance ... not its shape" (p. 3). Checked against
  the exact stationary covariance of the discrete recursion: relative
  error 3.9%, 0.65% and 0.07% at ε = 10⁻², 10⁻³, 10⁻⁴ with μ = 0.1, and
  below 0.2% for μ ≥ 0.5. With BBᵀ = σ²A it gives Σ = εσ²/(2μS)·I, which
  is THEORY-779's λ → 0 limit with μ = 1 − β.
- **SGLD at a constant rate (§5.1).** The stationary covariance
  overestimates the posterior's, by correction terms that vanish only as
  ε → 0.
- **SGFS (Theorem 5, Corollary 6).** H* = (2/εN)(BBᵀ + EEᵀ)⁻¹ samples the
  posterior exactly; the paper recommends injecting noise where gradient
  variance is small, "opposite to the advice of Ahn et al." (p. 16).
- **Iterate averaging (§6, App. G).** The average of the iterates over a
  window T has covariance D ≈ (1/T)(ΣA⁻¹ + A⁻¹Σ) = A⁻¹BBᵀA⁻¹/(TS), with T
  counted in iterations (Eqs. 30–31), the same for every constant
  preconditioner. Under A5 this is A⁻¹/(TS), so averaging over one pass,
  T = N/S, gives the posterior covariance A⁻¹/N to leading order in
  1/(TελΛ) (Eqs. 33–34). Checked: exact covariance of the mean of T
  stationary iterates against A⁻¹/(TS), relative error 23%, 4.7% and 0.9%
  at T = 2,000, 10,000 and 50,000 with ε = 0.01, λ_min = 0.2, tracking
  1/(Tελ_min).
- **An efficiency bound (§6.2).** Under A1–A5, a black-box SG-MCMC method
  producing independent posterior samples in fewer than O(N) operations
  would contradict Polyak–Juditsky optimality (pp. 20–21). The argument is
  informal and the authors call the assumptions "optimistic".
- **Experiments (§7).** On wine, protein (linear regression) and skin
  (logistic regression), the iterates' covariance matches Eq. 13 "to a
  very good extent" (p. 22); Table 1 gives KL to a Laplace posterior, e.g.
  constant SGD 18.7, 0.471, 1000.9 and full-preconditioned SGD 0.7, 0.005,
  1.8. Iterate averaging beats SGLD and NUTS from random initialisation on
  a synthetic linear regression (Figs. 4–5). Constant SGD selects L2
  hyperparameters on MNIST and covertype softmax regression comparably to
  BBVI (Fig. 6).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under A1–A4 the stationary distribution of constant SGD is N(0, Σ) with ΣA + AΣ = (ε/S)BBᵀ | strong (derivation) | App. B; standard OU result; confirmed in my check to 5% for the discrete process at small ε |
| C2 | The KL-optimal scalar rate is 2SD/(N tr BBᵀ), and the preconditioner (2S/εN)(BBᵀ)⁻¹ gives the posterior exactly | strong (derivation) | Theorems 1–2, Corollary 4; checked numerically |
| C3 | Momentum rescales the stationary covariance by 1/μ without changing its shape | strong (derivation) | Eq. 25, App. D; checked against the discrete recursion |
| C4 | The assumptions hold well enough on three small regression problems | moderate (experiment) | Figs. 1–2, Table 1; linear and logistic regression only |
| C5 | Averaging over one pass gives approximate posterior samples, and no black-box SG-MCMC can beat one sample per pass | moderate for the covariance (derivation), weak for the bound (informal, A1–A5) | Eqs. 30–34, §6.2 |
| C6 | Constant SGD can select hyperparameters as well as BBVI | weak | two datasets, one model, Fig. 6 |

## Method

Write SGD as dθ = −g dt + √(ε/S)B dW, linearise at the optimum, solve for
the stationary covariance via the Lyapunov equation, write KL(q‖f) between
two zero-mean Gaussians, and eliminate Σ by the trace identity
tr(AΣ) = (ε/2S)tr(BBᵀ) (or its preconditioned analogue) and the scaling
log|Σ| = D log(ε/S) + const. Minimise over ε, S or H.

## Concepts

- **Constant SGD** — SGD with a non-decreasing learning rate, run as a
  Markov chain with a stationary distribution.
- **Stationary distribution as variational family** — the family of OU
  stationary laws indexed by (ε, S, H), fitted by KL(q‖f) "in the spirit
  of variational inference".
- **Three regimes** — search, directed approach, stationary sampling
  (p. 8). Only the last is modelled.

## Connections

- Kunin et al.'s underdamped model (LIT-1011, THEORY-779, THEORY-209)
  is the same OU calculation with momentum, noise ∝ Hessian and weight
  decay; its isotropic stationary covariance is this paper's A5 case.
- McCandlish et al. (LIT-348, NOTE-293) use this paper's stationary
  quadratic model for their temperature ε/B (App. C there). NOTE-293
  names it without a LIT; this is that LIT.
- Hennick and De Baerdemacker (LIT-tmp107c0, NOTE-tmp5vh75) cite the 2016
  version as the non-degenerate case they generalise.
- Polyak and Juditsky (1992) for averaging; Ahn et al. (2012) for SGFS;
  Welling and Teh (2011) for SGLD. None held here.

## Bearing on the record

- **QUESTION-tmpiir0l, the three-row table.** Row 2 is right about this
  paper, and needs one sharpening. The stationary distribution "can be
  made close to" a posterior only under A1–A4, and A4 requires a
  positive-definite Hessian, so the result is about a **regular model in
  one basin**. The SLT posterior whose phase order the question asks
  about is singular by construction, and this paper says nothing about it.
  Row 3 is right that the paper does not establish the transient: it
  disclaims the search phase in so many words (p. 8). The owner's U4
  recollection was of the right paper, but it does not support "it is the
  same process". What it gives is a **map from optimiser temperature to
  sample size**, ε/S against 1/N, not from training time to sample size.
  The one place training time maps to a sample size is iterate averaging:
  after T steps of batch S, the average's covariance is that of a
  posterior from TS observations (THEORY-tmp8ggnh). That too is regular,
  single-basin and post-equilibrium, and it describes spread around a fixed
  optimum, not which region dominates.
- **THEORY-209 and THEORY-779.** Consistent. This paper is the
  general-noise, first-order antecedent of Kunin's model; THEORY-779's
  isotropy is its A5 case. No change to either.
- **NOTE-293.** Its "via Mandt–Hoffman–Blei" now has a LIT.
- **New:** THEORY-tmp7gcht (the stationary law and posterior matching, with
  their scope) and THEORY-tmp8ggnh (averaging).
- **ML practice.** The paper carries instructions: rates, batch sizes and
  preconditioners for approximate sampling, and noise injection in SGFS.
  The LIT keeps the `anthology-candidate` flag.

## Limitations

- **Regular, single-basin models only** (A4). Flat directions, degenerate
  minima and multiple basins are outside it; the paper does not discuss
  singular posteriors.
- **Constant noise covariance** (A2). For linear regression the noise
  covariance is in fact quadratic in θ (App. A, p. 27).
- **Experiments are linear and logistic regression** and softmax
  regression; no neural network is tested.
- **The search phase is not modelled**, by the authors' own statement.
- **The SG-MCMC efficiency bound** rests on A1–A5 and an informal reduction.
- Small slips: the KL in Theorem 5's proof (p. 16) is written with
  −(εN/4)tr(H(BBᵀ + EEᵀ)) where Appendix E's Eq. 46 has +. It does not
  affect the result.

## Open questions

- What replaces Eq. 13 at a degenerate minimum, where A has a null space
  and the posterior is not Gaussian? Hennick and De Baerdemacker attempt
  it (NOTE-tmp5vh75).
- Does iterate averaging's examples-to-sample-size correspondence survive
  across basins, where the posterior at sample size TS would favour a
  different region from the one the iterate sits in?
