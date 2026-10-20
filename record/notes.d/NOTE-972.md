---
number: 972
status: Read
formerly:
- NOTE-tmpeh0fp
paper: 'LIT-1254'
title: 'Raju, Machta and Sethna — Information loss under coarse graining'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:1710.05787v2 (17 October 2018), a six-page
    letter, text extracted with pdftotext in plain and layout modes: the
    abstract, the whole main text with Eqs. 1–21, the closing discussion
    of assumptions, and the 29 references. It has no appendix or
    supplement. Fig. 1 is a cartoon and was read from its caption. Some
    displayed equations were garbled by extraction (Eqs. 1–2, 5, 8, 18);
    they were reconstructed from the surrounding prose and the key ones
    re-derived in THEORY-742. The published Phys. Rev. E text was not
    compared. Machta et al. (2013), the source of the numerics the paper
    leans on, is not held and was not read. The diffusion scaling (Eq. 9),
    the drift's information under a non-Gaussian kernel, and the decimated
    1D Ising chain were checked by short scripts in the reader's
    scratchpad.
- version: 2
  date: '2026-10-20'
  note: >-
    Machta et al. (2013) is now read (LIT-1299, NOTE-1018). The
    λ = d/2 dividing line is credited to its supplement, and the
    description of its diffusion numerics is corrected. The reading is
    unchanged.
date: '2026-10-20'
summary: >-
  For a Boltzmann distribution linear in its couplings, the Fisher
  information that coarse-grained data lose is the expected conditional
  covariance of the energy operators. Under an exact RG step with linear
  beta functions it is the Hessian of the analytic constant, so the
  singular part of the metric is kept. In the diffusion model it is exact:
  the metric scales as n^(1−μ) by Hermite order. The claims that every
  relevant direction is kept and that irrelevant ones contract at
  b^−(d−2λ) rest on a scaling argument. On the paper's own scalings the
  dividing line is λ = d/2, not 0.
---
<!-- inactive-ok-file: THEORY-202 — Proposed; accounts this reading bears on, nothing here rests on their being settled -->
# NOTE-972: Raju, Machta and Sethna — Information loss under coarse graining

## Contribution

The paper restates the renormalization group as a statement about the
Fisher information metric on parameter space. As the observation scale
grows, it asks how the distinguishability of the *bare* parameters,
judged from coarse-grained data, changes. It writes the change as a
modified Lie derivative of the metric along the beta-function flow (Eq. 3),
with an added term for the shrinking number of coarse data points. For a
Boltzmann family it identifies the information lost as the Hessian of the
analytic constant that a renormalization step generates. It concludes that
the singular part of the metric, which carries the relevant directions,
is preserved, and that the analytic part, which carries the irrelevant
ones, contracts. The diffusion example is the only fully worked case, and
there the result is exact.

## Key insight

Coarse-graining loses exactly the fluctuations of the energy operators
that the coarse state does not fix: g − g̃ = ⟨Cov(Φ | x̃)⟩. Near a critical
point the diverging, long-wavelength part of those fluctuations is
carried by the coarse modes. What is lost is the short-range part, so the
loss is analytic. Directions whose Fisher information is dominated by the
singular part remain as distinguishable from macroscopic data as from
microscopic data. Directions dominated by the analytic part become
indistinguishable, and "universality" is the name for that loss. The
relevant directions do not grow, as they do in the usual parameter-space
picture: in the space of predictions they are the ones that stay put.

## Assumptions

- **The metric is the total Fisher information**, extensive in the amount
  of data: g_μν = −Σ_x P ∂_μ∂_ν log P (Eq. 1). The physical size L is held
  fixed while the coarse lattice spacing grows, so the coarse system has
  fewer sites. An intensive (density) metric would behave differently: the
  authors say relevant directions would then "spread out" with exponent d
  (they cite Quinn et al. 2017).
- **An exponential family**: H = Σ_μ θ_μ Φ_μ(x), so g = ∂∂ log Z =
  Cov(Φ_μ, Φ_ν) (Eq. 10).
- **Closure.** The renormalized Hamiltonian has the same form with
  renormalized parameters, plus an additive constant G(θ) (Eq. 11). In
  effect, every coupling the flow generates is already among the θ_μ.
- **Linear beta functions**, β^μ = λ_(μ) θ^μ. The authors name this as the
  main assumption and say that nonlinear (normal-form) corrections are
  left for later.
- **G is analytic**, and the singular free energy obeys the scaling
  hypothesis β·∂F^(s) = L ∂_L F^(s) (Eq. 16).
- **For diffusion**: a hopping kernel with finite second moment,
  parametrized by Hermite (Edgeworth-type) coefficients about a Gaussian
  (Eq. 5). The metric is evaluated at θ_μ = 0 for μ ≥ 3, at the Gaussian
  fixed point.
- **Classical systems only.** Quantum systems are excluded (footnote [20]).

## Key results

- **Eq. 3, the flow of the metric.**
  L̄_β g_μν = β^α ∂_α g_μν + g_αμ ∂_ν β^α + g_αν ∂_μ β^α − L ∂_L g_μν. For
  linear β this becomes Eq. 4,
  L̄_β g_μν = λ_(α) θ^α ∂_α g_μν + g_μν (λ_(μ) + λ_(ν)) − L ∂_L g_μν, and
  L ∂_L g = d·g for a bulk system. (The text says "the first term can be
  written −dg"; it means the last.)
- **Diffusion, Eqs. 6–9.** A trajectory of m microscopic steps carries
  g⁽⁰⁾_μν = m δ_μν / (μ! θ₂^μ). Observing every n-th step gives
  θ̃_μ = n^{1−μ/2} θ_μ, β^μ = (1 − μ/2) θ^μ, and g̃⁽ⁿ⁾_μν = n^{1−μ} g⁽⁰⁾_μν.
  The drift (μ = 1, λ = 1/2) is exactly preserved. The standard deviation
  (μ = 2, marginal) falls as 1/n, and higher orders fall faster. *Holds
  when:* at the Gaussian fixed point, to first order in the shape
  parameters. Re-derived and checked numerically in [THEORY-742](../theory.d/THEORY-742.md).
- **Eqs. 13–15, the coarse metric.** With {Φ}_x̃ the conditional mean of Φ
  given the coarse state, g̃ = ⟨{Φ_μ}_x̃ {Φ_ν}_x̃⟩ − ⟨Φ_μ⟩⟨Φ_ν⟩ and
  g − g̃ = ⟨{Φ_μ Φ_ν}_x̃ − {Φ_μ}_x̃ {Φ_ν}_x̃⟩, which is positive
  (semi)definite. "Coarsening reduces the FIM in all directions." *Holds
  for:* any coarse-graining map of an exponential family. This is the law
  of total covariance.
- **After Eq. 15.** g̃_μν = g_μν − ∂_μ∂_ν G. *Holds when:* closure and a
  linear parameter map hold, so that the renormalized Hamiltonian has no
  second derivative in θ.
- **Eq. 17.** L̄_β g^(s)_μν = 0. The singular part of the metric is carried
  unchanged along the flow. *Holds when:* the scaling hypothesis (Eq. 16)
  holds and β is linear. Derived by differentiating Eq. 16 twice.
- **Eq. 18.** The analytic part changes over n steps by
  Δg^(a)_μν = −Σ_{m=1}^{n−1} b^{m(λ_μ+λ_ν)} ∂_μ̃∂_ν̃ G(θ̃). The paper says
  ∂_μ̃∂_ν̃ G is positive definite "as can be explicitly checked" for the 2D
  Ising model on a triangular lattice (Niemeijer and van Leeuwen). The
  summation index and limits are garbled; m from 0 is presumably meant.
- **Eqs. 20–21, scaling near criticality.** g^(s)_μμ ∼ L^d ξ^{−(d−2λ_μ)},
  and g^(a)_μμ ∼ L^d b^{−(d−2λ_μ)}. The first follows from solving Eq. 19
  (Eq. 17 written out). The second is argued: the change in the analytic
  part "should be dominated by the change in parameter space distance in
  Equation 4 (with higher order corrections)".
- **An Ising illustration.** For a scaling form with one irrelevant field u,
  F = L^d t^{d/λ_t} 𝓕(u t^{−λ_u/λ_t}), the singular metric is
  g^(s)_uu = L^d t^{(d−2λ_u)/λ_t} 𝓕″, which vanishes at t = 0 because
  λ_u < 0.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Coarse-graining an exponential family reduces the Fisher metric in every direction, by the expected conditional covariance of the energy operators | strong | Eqs. 13–15; the law of total covariance |
| C2 | In the diffusion hopping model, the metric of a fixed-duration trajectory scales as n^{1−μ} by Hermite order: the drift is exactly preserved and all other parameters contract | strong at the Gaussian fixed point; not shown away from it | Eqs. 5–9; re-derived and checked here |
| C3 | Under an exact RG step, the information lost is the Hessian of the analytic constant, so the singular part of the metric is preserved along the flow | strong under the stated assumptions (closure, linear β, analytic G, the scaling hypothesis) | after Eq. 15; Eqs. 16–17 |
| C4 | Information about relevant directions is preserved under RG flow ("exactly maintained", in the introduction) | moderate for directions with λ > d/2; overstated as worded (see Limitations) | C3 plus the claim that relevant components are dominated by the singular part |
| C5 | Irrelevant directions contract at a rate set by their RG exponents, g^(a) ∼ L^d b^{−(d−2λ)} | moderate; exact only for diffusion | Eq. 21, a scaling argument; the authors cite Machta et al. (2013) for confidence |
| C6 | From a coarsened Ising system one can measure temperature and magnetic field "equally well" | moderate for the 2D Ising model, where λ_h = 15/8 and λ_t = 1 = d/2 (logarithmic) | Eqs. 20–21 |
| C7 | Relevant directions of general coarse-grainings can be identified as Fisher eigendirections that do not contract | weak | a closing suggestion, not tested |

## Concepts

- **Fisher information metric (FIM)**: the total Fisher information of
  the data set about the parameters, used as a Riemannian metric. Here it
  is extensive, so halving the data halves it.
- **Model manifold**: the image of parameter space in the space of
  distributions, with the FIM as its metric.
- **Modified Lie derivative** L̄_β = L_β − L∂_L: the change of the metric
  along the RG flow, with the system's physical size fixed so the number
  of coarse data points falls.
- **Singular and analytic parts of the metric**: the second derivatives of
  the singular and analytic parts of the free energy. The singular part
  diverges at the critical point along strongly relevant directions.
- **Sloppiness**: a Fisher spectrum spanning many decades, roughly evenly
  spaced on a log scale. The paper cites Machta et al. (2013) for the
  finding that renormalizable models become sloppy only after their data
  are coarsened. Eq. 9 gives this exactly for diffusion: at scale n the
  eigenvalues are spaced by a factor of about n per Hermite order.
- **Relevant and irrelevant**: RG eigenvalue λ > 0 and λ < 0, with marginal
  at λ = 0, as usual.

## Method

Take the Fisher metric of the bare model, observe the system through a
coarse-graining map C (decimation, momentum shell or time-blurring), and
compute the Fisher metric of the coarse data *in the bare coordinates*.
Infinitesimally, that is the Lie derivative of the metric along the
beta-function vector field, corrected for the loss of data points. When
renormalized parameters are used along the way, the metric is pulled back
by the Jacobian ∂θ̃/∂θ.

## Connections

It builds on the sloppy-models programme (Transtrum, Machta and Sethna
2011; Transtrum et al. 2015) and directly on Machta et al. (2013, Science),
whose numerics on decimated Ising models, and densities of a hopping
model observed at a later time with fixed Gaussian error, it
sets out to explain. It corrects Maity, Mahapatra and Sarkar (2015). They
derived the metric by assuming distances are preserved under flow along
the beta functions, which the present authors say captures only the
singular part and misses the analytic part, which dominates irrelevant
directions. It cites the geometry-of-RG line (Lässig 1990; O'Connor and
Stephens 1993; Dolan 1994), Ruppeiner's thermodynamic geometry, and Bény
and Osborne's quantum information-geometric RG, which it sets aside. The
companion visualization paper is Quinn et al. (2017, arXiv:1709.02000).

## Bearing on the record

- **[THEORY-742](../theory.d/THEORY-742.md) (filed from this reading, Active).** The proved core:
  the loss identity for any coarse-graining of an exponential family, the
  analytic loss under an exact RG step, which keeps the singular part, and
  the exact diffusion scaling. The scaling claims C4–C5 are kept out of
  its title.
- **[QUESTION-217](../questions.d/QUESTION-217.md).** The paper supplies one precise version of an
  "order of relevance" tied to an order of refinement. Along a chain of
  nested coarse-grainings (σ(x̃_coarse) ⊆ σ(x̃_fine)), the Fisher metric is
  monotone in the Loewner order (C1 applied stepwise). The
  reparametrization-invariant contraction factors, the generalized
  eigenvalues κ of g̃ v = κ g v, order parameter directions from those
  kept to those lost. In diffusion that order is by cumulant order: mean,
  variance, skewness and so on. So *refinement and relevance (to the
  parameters) share a chain* for coarse-grainings of the data, by the
  data-processing inequality. The paper says nothing about *acquisition*:
  it has no learning operator. A reader's remark, not the paper's: for
  gradient flow on the expected log-likelihood near the optimum, the
  linearized rates are the eigenvalues of g in the chosen coordinates.
  These depend on the parametrization (natural gradient makes them all
  equal), and in diffusion the microscopic eigenvalues 1/(μ! θ₂^μ) depend
  on the unit of θ₂. Linking this paper's order to an acquisition order
  therefore needs both a learning operator and a choice of coordinates. In
  [QUESTION-217](../questions.d/QUESTION-217.md)'s terms, a learning operator that commutes with the
  projections onto the RG eigendirections, which here are the Hermite
  directions, where g is diagonal. The answer to the question it was
  registered for is: the contraction of distinguishable directions is
  given exactly (diffusion) or by scaling (critical systems), and no link
  to acquisition is made.
- **[THEORY-202](../theory.d/THEORY-202.md).** It asks for "a stated target" that fixes which variables
  a renormalization keeps. This paper offers one implicitly: keep the
  singular Fisher metric of the bare couplings. The non-interacting
  construction of [THEORY-202](../theory.d/THEORY-202.md) fails that target, because its coarse
  variables carry zero Fisher information about θ. The identity map
  passes, so the target is necessary, not sufficient. The paper itself
  does not derive "being a renormalization" from Fisher preservation:
  its preservation result *assumes* an exact RG step. It does not meet
  [THEORY-202](../theory.d/THEORY-202.md)'s promote_when, since it is not about variational RG and
  shows nothing about the trace condition. A sentence in [THEORY-202](../theory.d/THEORY-202.md)'s
  Connections could cite [THEORY-742](../theory.d/THEORY-742.md) as a candidate target.
- **[THEORY-194](../theory.d/THEORY-194.md).** A different information. [THEORY-194](../theory.d/THEORY-194.md)'s coarse-graining
  maximizes mutual information between a block's coarse variable and the
  far environment, which selects the map. This paper measures the Fisher
  information about the Hamiltonian's parameters for a map already given.
  Both say that what a good coarse-graining keeps is set by what it must
  stay informative about. The targets differ (the environment's spins
  against the couplings), and neither paper relates them. A test of
  whether the RSMI-optimal coarse-graining keeps the singular Fisher
  metric would join them. That would be new evidence of a different kind
  from [THEORY-194](../theory.d/THEORY-194.md)'s promote_when, not a way to meet it.
- **[THEORY-198](../theory.d/THEORY-198.md).** A loose parallel, the reader's: [THEORY-198](../theory.d/THEORY-198.md)'s full capture
  of block–environment information makes the coarse measure factorize, so
  no range is added. Here the loss is the conditional covariance of the
  energy operators given the coarse state, which is analytic when that
  covariance is short-ranged. Neither result implies the other.
- **[QUESTION-220](../questions.d/QUESTION-220.md).** Coarse-grainings in an RG chain are nested by
  construction, so the paper takes nesting as given and asks nothing about
  whether optimal abstractions nest.
- No instruction for machine-learning practice. Nothing for the anthology.

## Limitations

- **"Relevant directions are exactly maintained" is overstated.** The
  introduction says so, while the abstract says "maintained" and the text
  elsewhere says "almost preserved". Only the *singular* part of the
  metric is preserved (Eq. 17). The analytic part along a relevant
  direction is lost like any other.
- **The dividing line is λ = d/2, not λ = 0, on the paper's own
  scalings.** With g^(s) ∼ L^d ξ^{2λ−d} and g^(a) ∼ L^d b^{2λ−d}, their
  ratio is (ξ/b)^{2λ−d}. For b < ξ the singular part dominates only if
  λ > d/2, which is when the corresponding susceptibility diverges. A
  relevant direction with 0 < λ < d/2, such as a thermal direction with
  α < 0 (α > 0 exactly when λ_t > d/2), has a singular metric that
  vanishes at criticality. On Eq. 21 it then loses information as
  b^{−(d−2λ)} until b ∼ ξ. The paper's two named cases sit on or above
  the line: the diffusion drift (λ = 1/2 = d/2) and the 2D Ising field
  (15/8 > 1) and temperature (1 = d/2, logarithmic). Even the marginal
  variance in diffusion contracts. So "relevant ⇔ preserved" holds for
  the examples given, not in general. This paper does not state it;
  Machta et al. (2013, [LIT-1299](../literature.d/LIT-1299.md)) did, in their supplement (Eq. 31
  and the text after Eq. 41), and this paper dropped it.
- **The drift is exactly preserved only at the Gaussian fixed point.** The
  explanation, "the mean drift is given by the two endpoints, unchanged
  under coarse-graining", holds only when the endpoints are sufficient,
  that is for a Gaussian kernel. For a unit-variance Laplace kernel the
  drift information per microscopic step, computed here, is 2.00, 1.19,
  1.09, 1.06 and 1.02 at n = 1, 2, 3, 4 and 8. It falls to the Gaussian
  value 1/θ₂. That is consistent with the paper's broader picture, in
  which non-universal information is lost, but not with the word
  "exactly".
- **Eq. 21, the contraction of irrelevant directions, is argued, not
  derived.** The authors say so: "The argument in statistical mechanics is
  somewhat technical but our confidence in the result comes from the
  numerical work in Ref. [15]". The paper contains no new numerics and no
  explicit lattice calculation. The only fully computed model is diffusion.
- **Positivity of ∂∂G is undersold.** The paper appeals to an explicit
  check on the triangular-lattice Ising model. Under its own closure
  assumption, positivity follows in general from Eq. 14 (∂∂G =
  ⟨Cov(Φ | x̃)⟩). The sentence "the analytic part of the free energy
  decreases" should read "of the metric".
- **Closure and linearity are strong.** A real RG step generates
  infinitely many couplings, and its parameter map is nonlinear (for 1D
  Ising decimation, K′ = ½ ln cosh 2K). The authors flag the linearity;
  they do not flag that Eq. 11 assumes closure. Known pathologies of
  real-space RG maps, where the renormalized measure can fail to be Gibbs,
  are not discussed. (That remark is the reader's.)
- **Eigendirections and invariance.** C7 speaks of "FIM eigendirections
  which do not contract … in a reparameterization invariant way". The
  eigenvectors of g alone depend on the coordinates. The invariant object
  is the relative contraction, the generalized eigenproblem of g̃ against
  g. The suggestion is not tested.
- **Eq. 8 to first order only.** After n steps the kernel is "recast into
  the form of Equation 5" with θ̃_μ = n^{1−μ/2} θ_μ only to linear order.
  Hermite coefficients from μ = 6 up also pick up products of lower ones,
  such as θ₃², which decay more slowly (n⁻¹ against n⁻² for θ₆). The
  metric at θ = 0 is unaffected, so Eq. 9 stands there.
- **A worked illustration, the reader's, not the paper's.** For the 1D
  Ising chain with coupling K and decimation of every other spin, the
  total metric about K falls by g̃/g = 2t²/(1 + t²), t = tanh K. The
  derivation uses tanh K′ = t², with brute-force checks on rings of 14 and
  20 spins, which agree up to finite size. The ratio tends to 1 at the
  zero-temperature fixed point, where 1 − t is relevant with λ = 1 > d/2,
  and to 0 at high temperature. That agrees with the d/2 reading above.

## Open questions

- Does a relevant direction with 0 < λ < d/2 lose Fisher information
  under coarse-graining, as Eqs. 20–21 imply? A computation for a model
  with α < 0 (the 3D XY model, or the O(n) model at large n), or for a
  Gaussian model whose exponents can be tuned, would settle it.
- Does the conditional-covariance loss ⟨Cov(Φ | x̃)⟩ stay analytic for
  real-space maps outside closure? This is the paper's mechanism with its
  strongest assumption removed.
- Do the coarse-grainings that maximize mutual information ([THEORY-194](../theory.d/THEORY-194.md),
  [THEORY-198](../theory.d/THEORY-198.md)) keep the singular Fisher metric, and do maps that keep it
  maximize that information? This would join the two information-theoretic
  accounts of RG.
- Under what learning operator does the contraction order of this paper
  become an acquisition order ([QUESTION-217](../questions.d/QUESTION-217.md))? A first case: a learner
  fitting the Hermite-parametrized diffusion kernel by gradient flow on
  data observed at scale n.
