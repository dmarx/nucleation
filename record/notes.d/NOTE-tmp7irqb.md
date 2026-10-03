---
status: Read
paper: 'LIT-tmp2fhfb'
title: 'Deep Equals Shallow for ReLU Networks in Kernel Regimes'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv 2009.14397v4 (22 pages) through PyMuPDF text
    extraction. Sections 1–5 and Appendix A read in full. Theorem 7 (the
    full Theorem 1) and Lemmas 4–6 read as statements, with the proof
    strategy followed: integration by parts against the Legendre
    differential equation for a weak bound, then exact decays for (1 −
    t²)^ν and t(1 − t²)^ν. Appendix B.1 (high-dimensional limits) and
    Appendix C (Corollaries 2–3, step activations) followed at the level
    of their steps, not checked line by line. Results the paper takes from
    Bach (2017a), Bietti & Mairal (2019b), Geifman et al. (2020) and Chen
    & Xu (2021) are taken as it reports them.
date: '2026-10-03'
summary: >-
  For κ(xᵀx′) on S^(d−1), µ_k = (ω_(d−2)/ω_(d−1)) ∫ κ(t)P_k(t)(1 − t²)^((d−3)/2) dt
  (Eq. 8), shared by N(d, k) ~ k^(d−2) harmonics. Theorem 1: an endpoint
  expansion κ(1 − t) = p(t) + c t^ν + o(t^ν) with ν non-integer gives
  µ_k ~ C k^(−d−2ν+1), parity-dependent. ReLU kernels have ν = 1/2 (NTK) and
  3/2 (random features) at any depth, so the deep NTK decays as k^(−d) and
  the deep RF kernel as k^(−d−2) (Corollaries 2–3). MNIST and Fashion-MNIST
  accuracy is flat in depth from L = 2 to 5 (Table 1).
---

# NOTE-tmp7irqb: Deep Equals Shallow for ReLU Networks in Kernel Regimes

## Contribution

A general theorem that reads the eigenvalue decay of any dot-product kernel
on the sphere off the kernel function's behaviour at t = ±1. Before it,
decays were derived kernel by kernel from closed forms. After it, the
decay of a deep NTK follows from composing asymptotic expansions. The
application settles a question the earlier work had raised empirically:
in the kernel regime, fully connected ReLU networks of any depth have the
same spectral decay, and so the same RKHS, as two-layer ones.

## Key insight

On the sphere, rotation invariance makes the spectrum of a dot-product
kernel a sequence of degenerate blocks, one per harmonic degree k, and the
only thing left to know is how fast the block eigenvalues fall. That rate
is local information. A kernel that is smooth where the inputs are aligned
has a rapidly decaying spectrum and a small RKHS of smooth functions. A
kernel with a √t-type kink there has a slowly decaying spectrum and a large
RKHS. ReLU layers compose without changing the kink's exponent, so depth
changes the constants and nothing else.

## Assumptions

- **Inputs on the sphere** S^(d−1) ⊂ R^d, uniformly distributed for the
  regression rates. A non-uniform density changes the eigenbasis
  (footnote 2, §2.2).
- **Kernel regime**: infinite-width random-feature (NNGP) or NTK limits of
  fully connected networks (Eqs. 1, 5–7). The lazy regime, not the mean
  field regime.
- **Theorem 1**: κ is C^∞ on (−1, 1), has the expansions of Eqs. 10–11
  with ν > 0 non-integer, and the derivatives of κ have the expansions
  obtained by differentiating them. Theorem 7 also needs finitely many
  exponents in the expansion between ν and ν + 1. The derivative condition
  was added after David Holzmüller found an error in an earlier version
  (Acknowledgments); for the RF and NTK kernels it follows from
  Δ-analyticity, shown by Chen & Xu (2021).
- **Normalisation** κ(1) = 1, corresponding to He-style initialisation, so
  that deep compositions neither explode nor vanish (§2.1).

## Key results

- **Mercer decomposition on the sphere (§2.2, Eqs. 8–9, 22).** T Y_(k,j) =
  µ_k Y_(k,j), with N(d, k) = ((2k + d − 2)/k)·C(k + d − 3, d − 2)
  harmonics per degree, growing as k^(d−2). The RKHS is {f = Σ a_(k,j)
  Y_(k,j) : Σ a²_(k,j)/µ_k < ∞}. Kernels with the same asymptotic decay have
  equivalent norms and so the same RKHS.
- **Theorem 1 (simplified).** With the expansions above, for even k, µ_k ~
  (c₁ + c₋₁) C(d, ν) k^(−d−2ν+1) if c₁ ≠ −c₋₁; for odd k, µ_k ~ (c₁ − c₋₁)
  C(d, ν) k^(−d−2ν+1) if c₁ ≠ c₋₁. If |c₁| = |c₋₁|, one parity decays
  faster. If κ is C^∞ on [−1, 1], µ_k decays faster than any polynomial.
- **Arc-cosine expansions (Eqs. 12–13).** κ₀(1 − t) = 1 − (√2/π) t^(1/2) +
  O(t^(3/2)); κ₁(1 − t) = 1 − t + (2√2/3π) t^(3/2) + O(t^(5/2)). These
  recover Bach's k^(−d−2) for κ₁ and k^(−d) for κ₀, and Bietti & Mairal's
  decay for the two-layer NTK, κ_NTK = uκ₀(u) + κ₁(u), with a parity
  change.
- **Corollary 2 (deep RF).** For L ≥ 3, µ_k ~ C(d, L) k^(−d−2), with C
  depending on the parity of k and growing linearly in L.
- **Corollary 3 (deep NTK).** For L ≥ 3, µ_k ~ C(d, L) k^(−d), with C
  growing quadratically in L, or linearly for the normalised κ_NTK/L. Both
  parities are non-zero, so the parity constraint of the shallow kernels
  disappears. A zero-initialised bias (Basri et al.) removes it in the
  shallow case too, giving κ_NTK,b(u) = (u + 1)κ₀(u) + κ₁(u).
- **Laplace kernel (§3.3).** e^(−c√(1−u)) has ν = 1/2, hence the same
  k^(−d) decay and the same RKHS as the NTK, recovering Geifman et al.
  The generalisation e^(−c(1−u)^γ) decays as k^(−d−2γ+1).
- **Step activations (§3.3, Appendix C.3).** The L-layer step kernel κ₀ ∘ ⋯ ∘
  κ₀ has ν = 1/2^(L−1), so its decay slows with depth and its RKHS grows
  toward the limiting smoothness (d − 1)/2. The authors note that step
  activations make optimisation beyond the linear regime hard.
- **Taylor coefficients (Appendix B.1).** For κ(u) = Σ b_k u^k, the b_k are
  recovered from µ_k as d → ∞ and decay as k^(−ν−1).
- **Experiments (§4, Fig. 1, Table 1).** Kernel ridge regression on S³:
  with a small enough λ_min all kernels reach similar rates, while with
  larger λ_min the NTK and Laplace kernels do better at large n, because
  their spectra decay more slowly. With m = √n random features, a two-layer
  ReLU network beats a three-layer one. On MNIST the RF kernel scores 98.60
  to 98.67 for L = 2 to 5, and on Fashion-MNIST 90.75 to 90.89; the NTK
  scores 98.46 to 98.53 and 90.50 to 90.65.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The polynomial decay of a dot-product kernel's spherical-harmonic eigenvalues is determined by the non-integer exponent of its expansion at ±1 | strong (proof) | Theorem 1 / Theorem 7, Appendix B |
| C2 | Deep and shallow fully connected ReLU networks have the same eigenvalue decay, hence the same RKHS, in both the RF and NTK regimes | strong (proof) | Corollaries 2–3, Appendix C |
| C3 | The deep ReLU NTK and the Laplace kernel on the sphere have the same RKHS | strong (proof), concurrent with Chen & Xu | §3.3 |
| C4 | Depth in kernel regimes therefore cannot explain the benefit of depth for fully connected ReLU networks | moderate: follows from C2 for approximation; the authors leave convolutional kernels open | §5 |
| C5 | Real-data accuracy is flat in depth, as the theory predicts | weak to moderate: two easy datasets, small differences, which the authors attribute to parity and numerical error | Table 1 |

## Concepts

- **dot-product kernel**: k(x, x′) = κ(xᵀx′) for x, x′ on the sphere;
  rotation-invariant.
- **random-feature (RF) kernel**: the infinite-width kernel of a network
  with fixed random hidden weights and a trained last layer. Also called
  the conjugate or NNGP kernel.
- **eigenvalue decay**: the rate at which µ_k → 0 in the harmonic degree
  k. Polynomial decay means a Sobolev-like RKHS; super-polynomial decay
  means smooth functions only.
- **parity constraint**: shallow ReLU kernels have µ_k exactly zero for
  large k of one parity, so their RKHS holds only even or only odd
  functions beyond low degree.

## Connections

- **Basri et al. ([LIT-tmpb9f8h](../literature.d/LIT-tmpb9f8h.md)).** Closed-form eigenvalues for the shallow
  NTK with and without bias. This paper generalises the decay, adopts its
  bias kernel, and proves the depth-independence Basri et al. saw in their
  deep-network experiments. The LIT declares `extends`.
- **Cao et al. ([LIT-tmpycz0j](../literature.d/LIT-tmpycz0j.md)).** Turns the same spectrum into a statement
  about training: the residual on each eigendirection falls at a rate set
  by its eigenvalue. Cao's bound Ω(k^(−d−1)) on S^d is this paper's
  k^(−d) with d counting the ambient dimension.
- **O'Donnell ([LIT-346](../literature.d/LIT-346.md)) and Peter–Weyl ([LIT-329](../literature.d/LIT-329.md)).** The same structure on
  the hypercube and in general. Operators commuting with the symmetry are
  diagonal in the irreducible decomposition, with one eigenvalue per
  irreducible block.
- **Anthology.** The NTK ([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md)), and Bordelon et al.
  ([ANTH-LIT-328](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-328.md)), whose learning curves are a function of exactly this
  spectrum and the target's coefficients on it.

## Bearing on the record

The owner filed this beside Fisher-spectrum block structure, Papyan's
spectra and evidence-based model comparison, which are being filed in
parallel. What follows is my reading of how the paper bears on that line.
The paper says none of it.

- **The spectrum comes in blocks, and the blocks are what a threshold
  sees.** Each degree k is one eigenvalue with multiplicity N(d, k). Any
  rule that keeps eigendirections above a cut keeps or drops whole degrees.
  The number kept below degree K is Σ_(k<K) N(d, k), which grows like K^(d−1).
- **The Fisher in the lazy regime has this spectrum.** For squared loss
  the Gauss–Newton matrix JᵀJ (parameters × parameters) and the empirical
  NTK Gram matrix JJᵀ (samples × samples) share their non-zero eigenvalues.
  This is a fact of linear algebra, not a claim of the paper. In the kernel
  regime the leading Fisher eigenvalues are therefore the empirical NTK's,
  which approximate n·µ_k with multiplicity N(d, k), so they should appear
  as plateaus of near-degenerate eigenvalues of sizes N(d, k), falling as
  k^(−d). That is a concrete block structure to compare against the Fisher
  spectra being filed alongside. Whether trained networks outside the lazy
  regime keep it is what the comparison would test.
- **Eigenvalues are prior variances.** Read as a Gaussian-process prior,
  a kernel with Mercer expansion Σ µ_k Y_(k,j)(x) Y_(k,j)(x′) gives each
  coefficient a_(k,j) prior variance µ_k, and the RKHS norm Σ a²/µ_k of
  Eq. 9 is the quadratic form in the exponent of that prior. A
  Savage–Dickey test of "the degree-k block is absent" therefore weighs the
  posterior on that block against a prior whose scale is µ_k. Bayesian
  model reduction would prune high-degree blocks exactly when the data do
  not overcome their k^(−d) prior variance. The decay exponent is the Occam
  factor's schedule. This paper's result says that, for ReLU networks in
  this regime, the schedule does not depend on depth.
- **No THEORY is filed.** A candidate is stated in the report to the owner,
  not here.
- **ML practice.** None. The paper is a theory of kernels; it carries
  `anthology-candidate` for its subject only.

## Limitations

- **Kernel regime only.** The authors' own conclusion is that the result
  shows the limits of the kernel view for explaining depth, not that depth
  is useless (§5).
- **Uniform data on the sphere.** With another input density the
  eigenbasis changes, and the rates in footnote 2 hold only up to a
  density bound.
- **Fully connected networks only.** Convolutional kernels may gain from
  depth through stability and invariance; the authors leave this open.
- **Asymptotic in k.** The theorem fixes the exponent; the constants C(d,
  L) and the pre-asymptotic regime, where the finite-width experiments
  live, are not characterised.

## Open questions

- Does depth change the decay for convolutional or attention kernels?
- How much of the depth-dependent constant C(d, L) matters at the sample
  sizes used in practice, where the asymptotic exponent may not yet be
  visible?
- Outside the kernel regime, does the Fisher spectrum of a trained network
  keep a degree-block structure, or does feature learning break the
  degeneracy?

## Corrections

- none to a seeded skim (there was no seed)
- **Citation.** The owner gave "Bietti & Bach (2021)". The paper is on
  arXiv from 30 September 2020 and appeared at ICLR 2021; the ICLR year is
  what the owner cited. It is not Bietti & Mairal (2019), "On the Inductive
  Bias of Neural Tangent Kernels", the other candidate. That paper supplies
  the two-layer NTK decay this one generalises.
