---
status: Read
paper: 'LIT-tmp6gimq'
title: 'Chorin and Lu — Discrete stochastic parametrization by NARMAX'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the published text on PubMed Central (PMC4538664,
    HTML, extracted to plain text) and from the arXiv v1 PDF (12 pages,
    references included), extracted with pdftotext. The two were
    compared section by section: equations, Tables 1–3 and the figures
    agree, and the published text adds a Significance statement, renames
    the exogenous functions P_i to Q_i and softens one phrase of the
    conclusion. The PMC page did not carry the figures as text, so Figs. 1
    and 2 were read from the rendered arXiv pages, Fig. 2's left panels
    re-rendered at 250 dpi. Read: the introduction, the NARMAX section with
    its likelihood, structure selection and Mori–Zwanzig discussion, the
    Lorenz 96 set-up, all numerical results and the conclusions. The paper
    has no proofs and no appendix. The record's checks on the linear
    Gaussian class were run in numpy from scripts in the session
    scratchpad, not from anything in the paper.
date: '2026-10-20'
summary: >-
  Model reduction done wholly in discrete time: advance the resolved
  variables by a fixed integrator and fit the exact one-step discrepancy as
  a NARMAX series, so memory lives in a few lags of the discrepancy, the
  resolved variable and the innovations. On Lorenz 96 with ε = 0.5 one or
  two lags reproduce x₁'s statistics and double forecast lead time at
  δ = 0.05. The link to Mori–Zwanzig is analogy, not derivation; nothing is
  proved and no error is bounded. The record's check: a partially observed
  linear Gaussian VAR(1) is exactly ARMA, with order 1 + the rank of its MZ
  memory kernels, so a memory non-zero at every lag is carried exactly by
  finitely many history-measurable coordinates.
---
<!-- inactive-ok-file: THEORY-tmpdjsgt THEORY-747 THEORY-257 CLAIM-327 — Proposed; the account this reading files, its turbulence analogue, and the record's criteria it is set beside, nothing here rests on their being settled -->

# NOTE-tmpejcu2: Chorin and Lu — Discrete stochastic parametrization by NARMAX

## Contribution

It moves stochastic parametrization out of continuous time. Instead of
estimating the unresolved tendency z = R(x, y) − R₀(x) by differentiating
data, and then discretizing a stochastic differential system with memory,
it fixes one discretization of the resolved equations and fits the
discrepancy between the data and one step of it. That discrepancy is
computed from the data without approximation. It is fitted as a NARMAX
time series whose lags carry the memory, and the result is tested on
two-scale Lorenz 96 without time-scale separation, against Wilks's
polynomial-plus-AR(1) closure.

## Key insight

A closure need not reproduce the continuous unresolved tendency. It only
needs to make the sampled resolved variable come out right, so it can be
built for the sampled process directly, step size and integrator error
included. In that discrete setting, memory is a few lags of three
sequences: the discrepancy, the resolved variable and the past
innovations. The moving-average lags matter most. They let a finite state
carry a dependence on the past that never cuts off.

## Assumptions

- The full system dx/dt = R(x, y), dy/dt = S(x, y) is ergodic, and its
  long-run statistics are stationary. For Lorenz 96 this is taken from
  earlier numerical work, not verified.
- x is observed at spacing δ "with negligible observation errors".
- A solvable approximation R₀ and a fixed integrator R_δ for it are chosen
  in advance. The paper does not discuss how to choose R₀.
- The innovations ξ are iid Gaussian with mean zero, independent of the
  past. The paper notes that the exogenous input x is not independent of
  the noise, unlike in standard NARMAX.
- The fitted model is judged by the long-run statistics of x and by short
  forecasts. Whether z_δ approximates the continuous z is declared "not
  relevant".

## Key results

- **The discrete reduction (Eq. 5).** z_δ^{n+1} = (x^{n+1} − x^n)/δ − R_δ(x^n),
  and x^{n+1} = x^n + δR_δ(x^n) + δz_δ^{n+1}. This is exact by construction.
- **The NARMAX form (Eqs. 6–7).** z^{n+1} = Φ^{n+1} + ξ^{n+1}, with
  Φⁿ = μ + Σ_{j≤p} a_j z^{n−j} + Σ_{j≤r} Σ_{i≤s} b_{i,j} Q_i(x^{n−j}) + Σ_{j≤q} c_j ξ^{n−j}.
  Substituting zⁿ from Eq. 5 gives a NARMA form for x alone.
- **Estimation.** Given the structure, the conditional log-likelihood
  l(θ | ξ¹…ξ^q) = −Σ|zⁿ − Φⁿ|²/(2σ²) − ((N − q)/2) ln σ² is quadratic in the
  parameters other than σ², so maximum likelihood is least squares. It is
  consistent if the reduced system is ergodic (cited, not shown).
- **Structure selection** is "by trial and error" against three criteria:
  fit to the long-run mean and autocorrelation, convergence of the
  estimates as data grow, and respect for symmetries. Orthogonal least
  squares and error-reduction ratios "do not work" here, because the
  exogenous input is correlated with the noise.
- **Lorenz 96 (Eq. 10, Tables 2–3, Figs. 1–2).** At ε = 0.5, K = 18,
  J = 20, F = 10:
  - δ = 0.01: (p, r, s, q) = (1, 2, 0, 1), d_x = 1: a₁ = 0.9782, lag-1 and
    lag-2 coefficients of x equal to −0.1271 and 0.1132, MA d₁ = 0.9997,
    σ² = 0.0004.
  - δ = 0.05: (p, r, s, q) = (1, 1, 1, 0), (d_x, d_R) = (3, 1): a₁ = 0.8879,
    a cubic in x^{n−1} and a term in R_δ(x^{n−1}), σ² = 0.0284.
  - The KS distance of x₁'s distribution is 0.0055 and 0.0049 for NARMAX,
    against 0.0183 and 0.0747 for POLYAR.
  - At δ = 0.05, POLYAR's pdf is bimodal and its autocorrelation and
    cross-correlation drift in amplitude and phase; NARMAX tracks all three
    over 10 time units. With 20 members the anomaly correlation stays above
    0.6 to lead time 4, against 2 for POLYAR. Filed as [THEORY-tmpdjsgt](../theory.d/THEORY-tmpdjsgt.md).
- **Mori–Zwanzig (the NARMAX section's last paragraphs).** R₀ = E[R | x] is
  MZ's choice, and MZ writes z as memory plus noise, which the paper
  matches with Φ and ξ. "The MZ expressions are exact, and prove the need
  for the representation of z to take the memory into account." MZ follows
  one sample path. NARMAX asks only for a stationary process with the
  right statistics, a "less ambitious and more feasible task".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The discrete discrepancy z_δ is available from data without approximation, and fitting it avoids numerical differentiation | strong | by construction (Eq. 5) |
| C2 | A NARMAX model of z_δ, fitted by least squares, reproduces the long-run statistics of x₁ in Lorenz 96 at ε = 0.5 better than POLYAR | strong for this system | Table 3, Fig. 1 |
| C3 | It forecasts better than POLYAR, by a lead time of 2 at δ = 0.05 | strong at δ = 0.05; overstated at δ = 0.01 | Fig. 2; see Limitations |
| C4 | The Mori–Zwanzig memory and noise correspond to Φ and ξ | weak | asserted by analogy; no derivation |
| C5 | The MZ expressions "prove the need" for memory in the representation of z | moderate | true generically, but the memory can vanish ([CLAIM-389](../claims.d/CLAIM-389.md)) |
| C6 | The approach "generalizes the MZ formalism to a broader class of approximations" | weak, overstated | no argument; see Limitations |
| C7 | The advantages will grow with the complexity of the problem | weak | expectation only |

## Method

1. Choose R₀ and an integrator R_δ at the observation spacing δ (here
   RK4 on the Lorenz 96 resolved equations with the coupling dropped).
2. From the data, compute zⁿ⁺¹ = (xⁿ⁺¹ − xⁿ)/δ − R_δ(xⁿ).
3. Choose a structure (p, r, s, q) and exogenous functions (powers of x and
   of R_δ(x)). Estimate the parameters by conditional least squares, with
   ξ¹ = … = ξ^q = 0 and ξⁿ = zⁿ − Φⁿ recursively.
4. Simulate by drawing ξⁿ⁺¹, forming zⁿ⁺¹ and stepping x. For forecasts,
   initialize from n₀ = max{1, p, r, s, 2q} + 1 observed steps, which also
   set the initial ξ.

## Concepts

- **Discrete stochastic parametrization** — Eq. 5: the resolved variable
  advanced by a fixed scheme plus a discrete stochastic correction fitted
  for that scheme and step.
- **Noise** — the paper's word for the whole unresolved tendency z, with
  its memory, not only its random part.
- **NARMAX** — nonlinear autoregression with moving average and exogenous
  inputs; here the exogenous input is the resolved variable itself, so
  input and noise are correlated.
- **POLYAR** — Wilks's closure: a polynomial in x_k fitted to
  finite-difference estimates of z, plus an AR(1) noise independent of x.

## Connections

It descends from Chorin, Hald and Kupferman's Mori–Zwanzig optimal
prediction ([LIT-1245](../literature.d/LIT-1245.md), [LIT-1253](../literature.d/LIT-1253.md)) and from Chorin and Hald (2014), which was
"not yet fully discrete". Its data-driven neighbours are Wilks (2005),
Arnold, Moroz and Palmer (2013), Crommelin and Vanden-Eijnden's
conditional Markov chains (2008) and Kwasniok (2012). Majda and Harlim's
physics-constrained regression (2013) and Kondrashov, Chekroun and Ghil's
non-Markovian closures (2015) are cited as related. The line continues in
Lu, Lin and Chorin's Kuramoto–Sivashinsky reduction (arXiv:1509.09279), in
their comparison of continuous and discrete-time modelling for hypoelliptic
systems (arXiv:1605.02273), and in Lin and Lu's derivation linking NARMAX
to a discrete Mori–Zwanzig formalism through Wiener projections
(arXiv:1908.07725). None of these is in the record.

## Bearing on the record

- **[QUESTION-222](../questions.d/QUESTION-222.md), the paper's part.** A NARMAX closure is a
  finite-dimensional Markovian augmentation: the coarse variable plus a few
  lags of x, z and ξ is a Markov state. On a chaotic system with no scale
  gap, one or two lags and one moving-average term suffice for the
  statistics and improve forecasts ([THEORY-tmpdjsgt](../theory.d/THEORY-tmpdjsgt.md)). There is no error
  bound, the orders are tuned, and they change with δ. So the paper shows
  that a short discrete memory can be enough in practice. It does not show
  when, or with what error.
- **[QUESTION-222](../questions.d/QUESTION-222.md), the record's check on the linear class.** Take a
  stable VAR(1) X_{t+1} = AX_t + ε_t in ℝⁿ with Gaussian ε and a scalar
  Y = LX. The NARMAX idea is then exact:
  1. **Y is ARMA(n, n − 1).** From (I − AB)X_t = ε_t, multiplying by the
     adjugate gives det(I − AB)X_t = adj(I − AB)ε_t, whose entries are
     polynomials in the backshift B of degree at most n − 1. So
     φ(B)Y_t, with φ(B) = det(I − AB), is a moving average of order at most
     n − 1, and a stationary process whose autocovariance vanishes beyond
     lag n − 1 is an MA(n − 1) in its own innovations. Checked on a random
     n = 3 model: the autocovariances of φ(B)Y are 1.643, 0.837 and 0.516
     at lags 0–2, and below 10⁻¹⁶ at lags 3–6, while Y's own
     autocovariances do not cut off.
  2. **The MZ kernels of [CLAIM-389](../claims.d/CLAIM-389.md) are non-zero at every lag yet
     finitely determined.** M_j = K₁₂K₂₂^{j−1}K₂₁ satisfies the linear
     recurrence given by K₂₂'s characteristic polynomial (Cayley–Hamilton),
     of order dim W⊥. Checked: residual 3 × 10⁻¹⁷ for n = 3, with M₁…M₁₀
     all non-zero (−0.144, 0.125, …, −0.0047).
  3. **The order matches the memory.** In four cases the McMillan degree of
     Y (the rank of its autocovariance Hankel matrix) was 1 plus the rank
     of the Hankel matrix of the M_j: 3 = 1 + 2 for a generic n = 3 model;
     2 = 1 + 1 for [QUESTION-222](../questions.d/QUESTION-222.md)'s own example sampled with noise; 2 = 1 + 1
     for an n = 3 model whose third variable is driven by the second but
     does not feed back, where one eliminated direction is invisible to
     the memory; and 1 = 1 + 0 for [CLAIM-389](../claims.d/CLAIM-389.md)'s counterexample, where Y is
     AR(1). Checked numerically in these four cases, not proved in general.
     [NOTE-989](NOTE-989.md) already identifies the Hankel rank as the minimal number of
     memory coordinates; this check ties it to the ARMA order.
  4. **The augmentation is a function of the coarse history.** The ARMA
     state in innovations form consists of past Y and past innovations,
     and the innovations are functions of Y's own past when the MA part is
     invertible. So this augmentation adds nothing from outside the coarse
     variable's history. It is the kind [THEORY-257](../theory.d/THEORY-257.md)'s criterion conditions
     on, unlike the Krylov augmentation [NOTE-989](NOTE-989.md) finds necessary for exact
     dynamical independence, which needs micro coordinates.
  5. **Continuous kernel infinite, discrete representation finite.** In
     [QUESTION-222](../questions.d/QUESTION-222.md)'s example ẋ = −ax + by, ẏ = cx − dy, with unit noise on
     both coordinates, a = b = 1, c = 0.2, d = 0.3, the continuous kernel
     bc e^{−dt} = 0.2e^{−0.3t} never vanishes. Sampled at h = 0.1, x is
     exactly ARMA(2, 1): the autocovariances of det(I − e^{Ah}B)x_n are
     0.1767 and −0.0879 at lags 0–1 and zero beyond. Its MA coefficient is
     θ = −0.9009.
  6. **Truncating lags has a controlled error, set by the MA zero.** Drop
     the moving-average coordinate and keep p lags of x. The best AR(p)
     one-step predictor's excess error over the full-past predictor falls
     from 7.9 × 10⁻⁵ at p = 1 to 1.2 × 10⁻⁵ at p = 10, against an
     innovation variance of 0.0975, with successive ratios tending to
     θ² = 0.8116. In the feed-forward n = 3 case the ratio is 0.0335. The
     rate is a zero of the spectral factor. It is not an eigenvalue of the
     sampled dynamics (0.885, 0.992), nor K₂₂ = 0.888, the rate at which
     the Mori-projection kernels decay, nor e^{−dh} = 0.970, the rate of
     the continuous kernel. Three projections or truncations, three
     memory lengths: that bears out A3's caution that a memory kernel's
     size depends on the projection. It also refines what [QUESTION-222](../questions.d/QUESTION-222.md)
     asks for. In this class, the number that controls the error of a
     lag truncation is the moving-average zero, not "the spectrum of the
     eliminated dynamics".
  7. **The paper's δ = 0.01 fit read in this light.** Its MA coefficient
     d₁ = 0.9997 puts the zero almost on the unit circle. By item 6, a
     pure-lag closure without that coordinate would need of the order of
     10³ lags. The moving-average term is doing the work, and recovering ξ
     from data, as the forecasts do from n₀ = 3 steps, is close to
     unstable.
- **[CLAIM-389](../claims.d/CLAIM-389.md).** Its counterexample is the degenerate case of item 3:
  zero memory ⇔ Y is Markov in its own law ⇔ the ARMA order is 1 with no MA
  part. Nothing in this reading contradicts it.
- **[THEORY-760](../theory.d/THEORY-760.md) and [THEORY-747](../theory.d/THEORY-747.md).** Parish and Duraisamy augment in
  continuous time with a kernel fixed by a quadrature. Chorin and Lu
  augment in discrete time with orders fixed by trial and error. Neither
  bounds its error. Item 6 is the first statement in the record of a
  bounded truncation error, and it holds only for the linear Gaussian
  class.
- **[THEORY-tmpcfuar](../theory.d/THEORY-tmpcfuar.md).** At ε = 0.5 its hypothesis of fast contracting
  eliminated variables fails, and memory helps, as [THEORY-tmpdjsgt](../theory.d/THEORY-tmpdjsgt.md) shows.
  The two readings are consistent.
- **[THEORY-752](../theory.d/THEORY-752.md), [NOTE-975](NOTE-975.md).** The paper says MZ has been carried out in full
  for a non-trivial nonlinear problem only once, citing [LIT-1253](../literature.d/LIT-1253.md).
- **[CLAIM-327](../claims.d/CLAIM-327.md).** A NARMAX state is a variable built from the accumulated
  past of the coarse variable and its innovations. That is the formal
  shape of a standing or reputation that members read and act on.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The Mori–Zwanzig link is analogy, not derivation.** In MZ the noise is
  orthogonal to functions of the resolved variables but is neither white
  nor independent of them ([NOTE-989](NOTE-989.md)), and the memory is a convolution
  with a kernel fixed by the orthogonal dynamics. Equating these with an
  iid ξ and a linear-in-parameters Φ is a modelling choice. Nothing shows
  that the fitted Φ approximates the MZ memory term.
- **"Generalizes the MZ formalism" is overstated.** MZ is an exact identity
  for one sample path. NARMAX is a parametric family fitted to statistics,
  and the paper itself calls its task "less ambitious". Neither contains
  the other as a special case.
- **"Prove the need" for memory is too strong.** The MZ memory can vanish
  exactly ([CLAIM-389](../claims.d/CLAIM-389.md); the deterministic case in [NOTE-989](NOTE-989.md)), so MZ shows
  that memory is generically present, not that it is always needed.
- **Nothing is proved.** Consistency of the estimator is cited. There is no
  error bound, no convergence in the orders, and no case where a finite
  discrete memory is shown to suffice exactly. The record's linear check
  supplies one.
- **Structure selection is ad hoc.** It is trial and error against the same
  long-run statistics that are reported, with no held-out rule, and the
  structure changes between δ = 0.01 and δ = 0.05.
- **Fig. 2's caption overstates at δ = 0.01.** It says NARMAX has smaller
  RMSE than POLYAR. Beyond a lead time of about 2.7, POLYAR's 5- and
  20-member RMSE curves lie slightly below NARMAX's (about 14.3 against
  14.7 at lead 5). The text's "slightly better" for δ = 0.01 is fairer.
- **The RMSE scale is not stated.** It saturates near 14–18, against a
  standard deviation of 3.5 for x₁. That fits an error summed over all 18
  components, but the paper does not say so; the formulas are deferred to
  Crommelin and Vanden-Eijnden.
- **Near-non-invertible MA at δ = 0.01.** With d₁ = 0.9997, an error in
  the initial ξ decays by a factor 0.9997 per step, about 2,300 steps to
  halve. That is harmless for estimation with N = 5 × 10⁵ but makes the
  "initial values … do not affect the result" claim slow to hold, and the
  forecasts initialize ξ from n₀ = 3 steps.
- **A notational slip.** Table 2 labels the δ = 0.01 lag coefficients
  b₁,₁ and b₁,₂, but with r = 2 and d_x = 1, Eq. 10 calls them b₁,₁ and
  b₂,₁.
- **One system, one ε, one component reported.**

## Open questions

- For which classes beyond the linear Gaussian one does the sampled coarse
  process admit an exact finite NARMAX representation, and with what
  orders? Lin and Lu's Wiener-projection paper (arXiv:1908.07725) is the
  lead.
- Is the McMillan degree of a scalar coarse variable of a VAR(1) always
  1 + the Hankel rank of its MZ kernels? It held in four cases here; a
  proof through the innovations form of the Mori decomposition would
  settle it.
- Does the lag-truncation error decay as |θ|^{2p}, with θ the largest MA
  zero, uniformly in the class, and how does θ move with the coupling and
  the sampling step? A bound in θ would give [QUESTION-222](../questions.d/QUESTION-222.md) its controlled
  error for linear systems.
- How do the fitted NARMAX orders scale with ε in Lorenz 96? A sweep
  from ε = 0.5 towards the scale-separated limit would show memory
  becoming unnecessary, as [THEORY-tmpcfuar](../theory.d/THEORY-tmpcfuar.md) predicts.
