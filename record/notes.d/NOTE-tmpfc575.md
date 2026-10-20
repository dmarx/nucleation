---
status: Read
paper: 'LIT-tmps1ffa'
title: 'Machta, Chachra, Transtrum and Sethna — Parameter space compression'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:1303.6738v1 (27 March 2013, the only version),
    14 pages: the five-page letter with Figs. 1–3 and the nine-page
    supplement with Fig. 4, §§I–VII and footnotes 1–15, text extracted with
    pdftotext. Many displayed equations were garbled by extraction
    (Eqs. 19–23, 29–30, 34, 36, 40–41); they were reconstructed from the
    prose and the rendered pages. Figs. 2 and 3 were rendered at 300 dpi
    and read as images; the decay rates in Fig. 3 were read off the
    rendered axis by eye. Fig. 1 (spectra of five models) and Fig. 4 were
    read from their captions and the low-resolution render. The published
    Science version was not compared: science.org returned 403 and the
    authors' Cornell copy failed TLS verification from this client. The
    hopping-model Fisher metric was recomputed exactly for the paper's
    N = 3 case and for a random kernel with drift, by a short script in
    the reader's scratchpad.
date: '2026-10-20'
summary: >-
  Two physics models are not sloppy at their microscopic scale and become
  so when observed coarsely. For the hopping model the Fisher eigenvalues of
  the density at time t scale as t^(3/2−k), proved here ([THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md)).
  For a decimated critical Ising model, Monte Carlo shows the field and
  temperature eigenvalues staying put while the rest fall in bands drawn at
  b^(2y−d) per step ([THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md), Proposed). That rate, the source of
  [LIT-1254](../literature.d/LIT-1254.md)'s Eq. 21, is argued by the same scaling argument, read off a
  figure without error bars, so [THEORY-742](../theory.d/THEORY-742.md)'s scaling claim stays
  scaling-only. The supplement already states the d/2 line. The causal
  claim about emergent theories is not shown.
---
<!-- inactive-ok-file: THEORY-tmpzyxwe — Proposed; this reading's empirical claim, filed from it -->
# NOTE-tmpfc575: Machta, Chachra, Transtrum and Sethna — Parameter space compression

## Contribution

It links the sloppy-models programme to the renormalization group and the
continuum limit. In two models where those methods already explain the
effective theory, it computes the Fisher information matrix (FIM) of the
microscopic parameters. Seen at the microscopic scale the spectrum is
clustered: the identity for the hopping model, a common scale apart from
two critical directions for the Ising model. Seen through coarse
observations it spreads over many decades, with the stiff directions being
the relevant, macroscopic ones. The Ising half gives the first numerical
evidence that the irrelevant directions' Fisher eigenvalues contract at
rates set by their RG exponents, the result Raju, Machta and Sethna later
restate ([LIT-1254](../literature.d/LIT-1254.md), Eq. 21).

## Key insight

A model is sloppy because it is observed at a scale much larger than its
own. The ratio of the two scales is the small parameter, and each further
eigendirection is weaker by a further power of it: of the time scale in
diffusion, of the decimation factor in the Ising model. A model's
universality and its sloppiness are then two readings of one fact. The
parameters an effective theory keeps are those whose distinguishability
survives coarse observation, and the rest cannot be learned from coarse
data and need not be known to predict coarse data.

## Assumptions

- **Two different Fisher metrics.** For diffusion, a *least-squares*
  metric g = JᵀJ on the deterministic density ρ_t(j), each site observed
  with Gaussian error σ = 1 (supplement Eqs. 10–11, 14–15; footnote 6
  says that a stochastic treatment "would yield similar but less
  transparent results", which is not shown). For the Ising model, the
  Fisher information of the Boltzmann distribution, g = Cov(Φ_μ, Φ_ν)
  (Eq. 26). Both depend on the choice of coordinates θ_μ.
- **Diffusion: the hopping probabilities are free.** 2N + 1 parameters,
  not constrained to sum to 1, so a particle-creation direction exists.
  All particles start at the origin. Fig. 2 uses N = 3 and θ_μ = 1/7.
- **Diffusion: coarse-graining is in time, by waiting.** The data are the
  density at a single later time t, with the same error per site. This is
  a different experiment at each t, not a function of the data at t = 1.
- **Ising: coarse-graining is in space, by decimation.** Observe only the
  spins on the n-th checkerboard sublattice, b = √2 per step, the
  configurations still drawn from the full-lattice Hamiltonian.
  Footnote 10: the Ising model has no time.
- **Ising: the family.** A field and nearby two-spin couplings (13
  parameters in the main text; the supplement lists the field, the
  nearest-neighbour coupling and 12 others, with vertical and horizontal
  bonds separate), evaluated on the ordinary Ising line at h = 0, on a
  64×64 periodic lattice.
- **The scaling analysis assumes** a linearized RG map in scaling
  variables, u′ = b^y u, an analytic background f^a and smooth matrices
  M^s, M^a with "eigenvalues that all take a characteristic scale"
  (Eqs. 28–31). Footnote 9 assumes the bare parameters may be mapped into
  an infinite-dimensional space of couplings. Eqs. 37–40 take the coarse
  metric to be the Hessian, in the bare θ, of a coarse free energy, which
  needs the renormalized Hamiltonian to stay linear in the parameters.

## Key results

- **Hopping model at t = 1.** ρ₁(j) = θ_j, so g = I (Eq. 15): "no
  parameter hierarchy".
- **Hopping model at time t (Eqs. 18–23).** J_{jμ} = t p_{t−1}(j − μ), so
  g_μν = t² q(μ − ν), with q the law of the difference of two
  (t−1)-step walks. That identity is implicit in Eq. 19, and it removes
  the paper's restriction to zero drift. The paper's asymptotic is
  λ_n ∼ t² (Dt/N²)^{−n−1/2}, n ≥ 0, i.e. λ_n ∝ t^{3/2−n}: creation
  (t^{3/2}) and drift (t^{1/2}) grow, the diffusion constant (t^{−1/2})
  and the skew, kurtosis and higher moments fall. *Holds when:* the walk
  is aperiodic with nonzero variance and t is large. Re-derived with a
  bound valid for every k, and checked numerically, in [THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md).
  The local exponents for N = 3 between t = 40 and 80 are 1.50, 0.50,
  −0.51, −1.52, −2.52, −3.52.
- **Ising before coarsening (Fig. 4, Eq. 31).** λ^s_i ∼ A ξ^{2y_i−d},
  λ^a_i ∼ A. Near T_c the singular part dominates "provided 2y_i − d ≥ 0":
  the field (y = 15/8, eigenvalue diverging like χ ∼ ξ^{7/4}) and the
  gradient of T_c (y = 1, logarithmic like the specific heat). The others
  "cluster together at a characteristic scale".
- **Ising after coarsening (Eqs. 34, 40–41).** The coarse metric is
  g^n = ⟨{Φ_μ}{Φ_ν}⟩ − ⟨{Φ_μ}⟩⟨{Φ_ν}⟩ (Eq. 34, the conditional-mean
  covariance). "The singular piece is exactly maintained", and
  λ^{n,a}_i ∼ A b^{n(2y_i−d)} (Eq. 41). For directions with 2y > d,
  λ^n ∼ Aξ^{2y−d} − A b^{(2y−d)n}, the second term mattering only when
  b^n ∼ ξ. For "irrelevant directions, or relevant ones with 0 < 2y_i < d",
  λ_i ∼ A b^{n(2y_i−d)}. *Holds when:* the scaling assumptions above; it is
  argued, not derived.
- **Ising numerics (Fig. 3).** On the 64×64 lattice at T_c, over six
  steps, the field eigenvalue stays near 10⁵ and ∇T_c near 4 × 10³
  (about 2 × 10³ by step 6). The others fall in three coloured groups with
  shaded bands. Read from the rendered figure, the bands fall by about
  0.27, 0.87 and 1.35 decades per step, against 0.30, 0.90 and 1.51 for
  b^{2y−d} with y = 0, −2, −4. Filed as [THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md), Proposed.
- **Fig. 1.** The coarse spectra of both models resemble those of
  radioactive decay, a neural network and a MAP-kinase model, roughly
  geometric over ten decades, wider than the Wishart spectrum of a random
  least-squares problem.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The hopping model's Fisher spectrum at time t separates as t^{3/2−k}, ordered creation, drift, diffusion constant, then higher moments | strong | Eqs. 19–23 (the series step is loose); re-derived and checked in [THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md) |
| C2 | Neither model is sloppy at its microscopic scale | strong for diffusion (g = I); moderate for Ising (Fig. 4, Monte Carlo along one line) | Eq. 15; Fig. 4 |
| C3 | Under decimation at T_c, the field and temperature eigenvalues do not shrink substantially | moderate | Fig. 3, one lattice, no error bars |
| C4 | The other eigenvalues shrink by b^{2y−d} per step | weak to moderate | Eq. 41 is a scaling argument; Fig. 3 bands drawn by the authors, rates not fitted; the caption states a different, wrong rate |
| C5 | "'Relevant' directions in the RG are exactly those whose FIM eigenvalues do not contract on coarsening" | overstated | contradicted by the supplement's own 0 < 2y < d case |
| C6 | Sloppiness "can be precisely traced to the ratio" of the microscopic and observation scales | strong for diffusion; moderate for Ising | Eq. 23; Eq. 41 |
| C7 | The emergence of effective continuum and universal theories "is due to the same parameter space hierarchy that underlies predictive modeling in other areas of science" | weak | Fig. 1, a resemblance of spectra; no model outside physics is coarsened |

## Method

For diffusion, compute J by differentiating the t-fold convolution, then
g = JᵀJ, exactly for t ≤ 7 and asymptotically by expanding the Fourier
integrand near k = 0. For Ising, generate full-lattice configurations by
the Wolff algorithm; for each, generate replicas with the observed
sublattice frozen ("compatible Monte Carlo", after Ron, Swendsen and
Brandt), using heat-bath moves and integrating out the level-1 free spins
exactly (Eqs. 43–45); estimate the conditional means and from them g^n,
with products over distinct replicas to remove the bias (Eqs. 36, 46).
Diagonalize and plot by level.

## Concepts

- **Fisher information matrix (FIM)**: a metric on parameter space whose
  distances measure distinguishability in "standard deviations"; here
  either a least-squares metric JᵀJ or a Boltzmann covariance.
- **Sloppiness**: a FIM spectrum spread roughly geometrically over many
  decades, so that few "stiff" combinations govern the predictions and
  the "sloppy" ones cannot be inferred and need not be known.
- **Coarsening**: observing at a larger scale, by waiting t steps or by
  keeping a sublattice. The paper calls both coarsening, though only the
  second discards data from a fixed observation.
- **Singular and analytic parts of the metric**: second derivatives of the
  singular and analytic parts of the free energy, scaling as Aξ^{2y−d}
  and A.
- **Compatible Monte Carlo**: sampling the fine configurations consistent
  with a given coarse one, by rejecting any move that changes it.

## Connections

It applies the sloppy-models programme (Waterfall et al. 2006; Gutenkunst
et al. 2007; Transtrum, Machta and Sethna 2010, 2011) to physics, citing
Crooks (2007) and Ruppeiner (1995) for the thermodynamic metric and
Caselle et al. (2002) for the irrelevant exponents of the 2D Ising model.
Its successor in this record is Raju, Machta and Sethna (2018), [LIT-1254](../literature.d/LIT-1254.md),
which restates the Ising analysis as a modified Lie derivative of the
metric and reworks the diffusion case with the stochastic Fisher
information of a subsampled trajectory ([THEORY-742](../theory.d/THEORY-742.md)).

## Bearing on the record

- **[THEORY-742](../theory.d/THEORY-742.md) and [NOTE-972](NOTE-972.md) (Raju, Machta and Sethna).** This is the
  "numerical work in Ref. [15]" on which that paper rests its Eq. 21,
  g^(a) ∼ L^d b^{−(d−2λ)}. Reading it changes nothing about that claim's
  standing. The paper's derivation (Eqs. 37–41) is the same scaling
  argument ("should be smoothly varying", "should continue to take a
  characteristic value"), with the same unstated closure assumption. Its
  numerics are one 64×64 lattice at T_c, at most six steps of √2, rates
  shown by drawn bands without error bars, and a y = 0 band that is the
  bare b^{−d} rate of discarding sites. So [THEORY-742](../theory.d/THEORY-742.md)'s "What this does
  not say" stands, and the claim stays argued only by scaling, now with
  its numerics read: [THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md), Proposed. Three corrections the
  coordinator may wish to make:
  - [THEORY-742](../theory.d/THEORY-742.md) and [NOTE-972](NOTE-972.md) call the λ = d/2 dividing line "the reader's
    algebra on the paper's scalings, not a result the paper states". It is
    not in [LIT-1254](../literature.d/LIT-1254.md), but Machta et al. state it in their supplement
    (Eq. 31: the singular part dominates "provided 2y_i − d ≥ 0"; after
    Eq. 41: "relevant ones with 0 < 2y_i < d" contract like irrelevant
    ones). The finding should be credited to [LIT-tmps1ffa](../literature.d/LIT-tmps1ffa.md), and the record's
    contribution narrowed to noticing that [LIT-1254](../literature.d/LIT-1254.md) dropped it.
  - [NOTE-972](NOTE-972.md)'s Connections calls the 2013 diffusion numerics
    "time-blurred diffusion". They are densities observed once at a later
    time with fixed Gaussian error, not a blurred or subsampled
    trajectory. In that set-up the creation and drift eigenvalues grow
    with t, so it is not a coarse-graining in the data-processing sense,
    and it is not the computation behind [LIT-1254](../literature.d/LIT-1254.md)'s Eq. 9. The two agree
    in relative terms: λ_k/λ₁ ∝ t^{1−k} here, g_μ/g₁ = n^{1−μ} there, k and
    μ both the Hermite order.
  - [THEORY-742](../theory.d/THEORY-742.md)'s bullet "Not that irrelevant directions contract as
    b^−(d−2λ)" could cite [THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md), as the empirical claim at issue
    and the kind of result its promote_when names.
- **[THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md) (filed, Active).** The hopping-model spectrum, with
  an exact identity the paper only implies and a re-derivation of its
  scaling that does not use its loose series step.
- **[QUESTION-217](../questions.d/QUESTION-217.md).** It adds a case in which relevance and refinement share
  one chain, both read from one eigenbasis. In the hopping model, the
  nested effective models (creation; creation and drift; creation, drift
  and diffusion constant) are ordered by FIM eigenvalue. A reader's
  remark, not the paper's: here the FIM is exactly the Gauss–Newton
  Hessian of the least-squares cost, so gradient flow in θ near a
  zero-residual fit acquires the directions in the same order, at rates
  ∝ t^{3/2−k}. This is the commuting case of [THEORY-745](../theory.d/THEORY-745.md) again, and it
  holds only in these coordinates: natural-gradient flow would equalize
  the rates. In the Ising half there is no learning operator, and the
  contraction order along the sublattice chain is an order of relevance
  to the bare couplings only.
- **[QUESTION-220](../questions.d/QUESTION-220.md).** The eigen-truncations are nested by construction; the
  paper asks nothing about whether optimal abstractions nest.
- **[QUESTION-218](../questions.d/QUESTION-218.md), [QUESTION-221](../questions.d/QUESTION-221.md), [QUESTION-222](../questions.d/QUESTION-222.md), [QUESTION-219](../questions.d/QUESTION-219.md).** Nothing
  direct. The continuum diffusion equation is an exactly closed coarse
  description that is not a block of variables, which [QUESTION-218](../questions.d/QUESTION-218.md) may
  wish to note, but the paper does not frame it so.
- **[THEORY-202](../theory.d/THEORY-202.md).** Nothing beyond what [THEORY-742](../theory.d/THEORY-742.md) offers: preserving the
  singular part of the Fisher metric of the bare couplings as a target
  for a renormalization.
- No instruction for machine-learning practice. Nothing for the anthology.

## Limitations

- **The emergence claim overreaches.** The title says compression
  "underlies" emergent theories, and the conclusion that their emergence
  "is due to the same parameter space hierarchy that underlies predictive
  modeling in other areas of science". What is shown is that, in two
  models where the continuum limit and RG already explain the effective
  theory, the coarse FIM is hierarchical with the macroscopic parameters
  stiff. The paper itself traces the hierarchy to the separation of
  scales, which is also what the RG and the continuum limit rest on, so
  the two are effects of one cause, not one the cause of the other. The
  link to biology is a resemblance of spectra (Fig. 1), in models with no
  separation of scales, none of which is coarsened or reduced; the text
  concedes that they "cannot be coarsened or reduced in the same
  systematic way".
- **The hierarchy depends on the coordinates.** Eigenvalues of a metric
  are not invariant under reparametrization, and the least-squares metric
  carries an arbitrary error width. The comparison is meaningful in these
  two models because the microscopic metric is (near) the identity in the
  chosen coordinates, so the coarse spectrum coincides with the invariant
  generalized eigenvalues against it. Fig. 1's cross-model comparison
  has no such anchor.
- **The two "coarsenings" differ.** Waiting t steps is not discarding data
  from one experiment, so eigenvalues may and do grow. Only decimation is
  a coarse-graining in the data-processing sense, where every eigenvalue
  must be non-increasing (footnote 14). The main text treats them alike.
- **The relevant/contracting equivalence is overstated.** The main text
  says relevant directions "are exactly those whose FIM eigenvalues do
  not contract". The supplement restricts it to 2y ≥ d. The 2D Ising
  model has no relevant direction with 0 < 2y < d, so its figure cannot
  test the restriction.
- **The Ising evidence is thin.** One lattice size, one temperature, at
  most six decimation steps (b^n ≤ 8 on a lattice of 64), M = 10⁴–10⁵
  configurations, sub-ensemble sizes not given, no error bars, no fitted
  exponents, groups assigned by colour, and eigenvalues reported ten
  decades below the largest without a noise floor. The y = 0 group is
  labelled marginal, but the 2D Ising model has no marginal operator; it
  falls at b^{−d}, the rate at which discarding sites alone removes
  information.
- **The caption's rate is wrong.** Fig. 3's caption gives 2^{−d−y_i} per
  step, which would make the y = −2 group constant and the y = −4 group
  grow. The supplement's b^{n(2y−d)}, i.e. 2^{y−d/2} per step, matches the
  drawn bands.
- **The diffusion series step is loose.** Eq. 22's claim that "each term
  in the series contributes a single new non-zero eigenvalue" fails: the
  matrix [(μ − ν)^{2n}] has rank 2n + 1. The scaling is right
  ([THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md)). The analysis is also stated for zero drift, which the
  exact identity shows is unnecessary.
- **Minor.** The main text says "the FIM of equation 8", which is in the
  supplement; the supplement's footnote 9 and Eqs. 37–40 assume closure
  without naming it; "relevant ones with 0 < 2y_i < d (corresponding to
  i ≥ 2 in the Ising model)" mislabels the 2D Ising irrelevant directions
  as relevant.

## Open questions

- What are the fitted per-step decay rates of the decimated Ising Fisher
  eigenvalues, with errors, at several lattice sizes, and does the y = 0
  group really fall at b^{−d}? ([THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md)'s promote_when.)
- In a model with a relevant direction of 0 < 2y < d (a transition with
  α < 0), does that direction's Fisher eigenvalue contract under
  decimation, as the supplement's Eq. 41 and [NOTE-972](NOTE-972.md) both predict? The
  2D Ising model cannot answer it.
- Does the stochastic Fisher information of particle counts (footnote 6)
  give the same t^{3/2−k} spectrum as the least-squares metric? The
  footnote asserts it; nothing in the paper shows it.
- Can the resemblance of coarse physics spectra to sloppy biological ones
  be made a statement about mechanism, for instance by exhibiting a
  separation of scales, or a coarse-graining, behind a sloppy biological
  model?
