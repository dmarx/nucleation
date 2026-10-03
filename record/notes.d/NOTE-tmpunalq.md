---
status: Read
paper: 'LIT-tmpycz0j'
title: 'Towards Understanding the Spectral Bias of Deep Learning'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv 1912.01198v3 (29 pages) through PyMuPDF text
    extraction. Sections 1–6, Appendix A and Appendix F read in full.
    Appendix B (Lemma 4.1 by Hoeffding and a union bound; Theorem 4.2 via
    Lemmas B.1–B.4; Theorem 4.3 following Bietti & Mairal's Proposition
    5; Corollaries 4.6–4.7 via the bound |Y_k| ≤ √N(d, k)) followed at the
    level of its steps. Appendices C–E, the supporting lemmas, skimmed.
    Lemmas taken from Su & Yang (2019), Cao & Gu (2019) and Allen-Zhu et
    al. (2019) are taken as the paper reports them.
date: '2026-10-03'
summary: >-
  Theorem 4.2: n^(−1/2)‖V_(r_k)ᵀ(y − ŷ(T))‖ ≤ 2(1 − λ_(r_k))^T n^(−1/2)‖V_(r_k)ᵀy‖ + ε
  for any labels, given n ≥ Ω̃(ε^(−2) max{(λ_(r_k) − λ_(r_k+1))^(−2), M⁴r_k²})
  and m ≥ Ω̃(poly(T, λ_(r_k)^(−1), ε^(−1))). Theorem 4.3: on uniform S^d the
  NTK's eigenfunctions are spherical harmonics, µ_k = 0 for odd k ≥ 3,
  and µ_k = Ω(max(k^(−d−1), d^(−k+1))) for even k. Experiments in R¹⁰ learn
  degrees 1, 2, 4 in that order, also on three non-uniform densities.
---

<!-- inactive-ok-file: LIT-242 — Deferred; cited as the self-supervised counterpart of stepwise eigenmode learning, with no relation claimed -->

# NOTE-tmpunalq: Towards Understanding the Spectral Bias of Deep Learning

## Contribution

A finite-width, finite-sample theorem that gradient descent on a two-layer
ReLU network reduces the training residual along the eigenfunctions of the
NTK integral operator, each at a rate set by its eigenvalue, without
assuming the target lies in the RKHS. Paired with an eigenvalue bound for
uniform spherical data that is sharper in the high-dimensional regime, it
makes "networks learn low frequencies first" a statement with explicit
sample and width requirements per frequency.

## Key insight

Spectral bias is a property of the kernel's eigenvalues, not of the target.
Whatever the labels contain, the part of the residual that lies in the
top-r_k eigenspace of the NTK falls geometrically at rate 1 − λ_(r_k). The
part outside it can be ignored as long as the network is wide enough for
the linearisation to hold over the T steps you run. Low degree means large
eigenvalue, so low-degree components go first. And because the guarantee is
for a whole eigenspace, what has to be resolved from the sample is the gap
below that eigenspace, not each eigenvalue in it.

## Assumptions

- **Architecture and training** (§3.2, Algorithm 1): two-layer fully
  connected ReLU network f_W(x) = √m W₂σ(W₁x), both layers trained by full
  gradient descent on squared loss scaled by a small θ, with He
  initialisation, N(0, 2/m) and N(0, 1/m).
- **Data**: inputs on the unit sphere S^d ⊂ R^(d+1) from an unknown τ,
  labels |y_i| ≤ 1. The uniform case is used for Theorem 4.3 and
  Corollaries 4.6–4.7.
- **Bounded eigenfunctions**: |φ_j(x)| ≤ M for j ≤ r_k (Lemma 4.1, Theorem
  4.2). For spherical harmonics M ≤ √N(d, k).
- **Sample size and width** (Theorem 4.2): n ≥ Ω̃(ε^(−2) max{(λ_(r_k) −
  λ_(r_k+1))^(−2), M⁴r_k²}); m ≥ Ω̃(poly(T, λ_(r_k)^(−1), ε^(−1))); step size η =
  Õ(m^(−1)θ^(−2)), θ = Õ(ε).
- **NTK regime.** The authors state that the results share the limitations
  of lazy-training analyses (§4.1).

## Key results

- **NTK of the two-layer network (Eqs. 3.1–3.3).** κ(x, x′) = ⟨x, x′⟩κ₁ +
  2κ₂, the arc-cosine kernels of degree 0 and 1, because both layers are
  trained.
- **Lemma 4.1.** The sampled eigenfunctions v_i = n^(−1/2)(φ_i(x₁), …,
  φ_i(x_n)) are nearly orthonormal: ‖V_(r_k)ᵀV_(r_k) − I‖_max ≤ CM²√(log(r_k/δ)/n).
- **Theorem 4.2 (projected residual).** As in the summary. Residual
  components in eigenspaces with larger eigenvalues are learned faster,
  with fewer samples and narrower networks.
- **Theorem 4.3 (spectrum on uniform S^d).** Mercer decomposition κ = Σ_k
  µ_k Σ_j Y_(k,j)(x)Y_(k,j)(x′), with N(d, k) = ((2k + d − 1)/k)·C(k + d − 2,
  d − 1). µ₀, µ₁ = Ω(1); µ_k = 0 for odd k = 2j + 1 ≥ 3; for even k, µ_k =
  Ω(k^(−d−1)) when k ≫ d and Ω(d^(−k+1)) when d ≫ k.
- **Corollaries 4.6–4.7.** For k ≫ d the residual on harmonics of degree
  < k falls as (1 − Ω(k^(−d−1)))^T with n ≥ Ω̃(ε^(−2) max{k^(2d+2),
  k^(2d−2)r_k²}). For d ≫ k it falls as (1 − Ω(d^(−k+2)))^T with n ≥
  Ω̃(ε^(−2)d^(2k−2)r_k²).
- **Remark 4.8.** The exponential dependence is unavoidable: r_k = Σ_(k′<k)
  N(d, k′) = Ω(d^(k−1)), and n samples cannot determine more than n
  components.
- **Experiments (§5).** 4,096 hidden units, vanilla GD, n = 1,000, inputs in
  R¹⁰. For f* = a₁P₁ + a₂P₂ + a₄P₄ the degree-1 projection converges
  first, then degree 2, then degree 4, also when the amplitudes are 1, 3, 5
  (Figs. 1–2), and roughly linearly on a log scale. Cosine and even
  polynomial targets with all frequencies present show the same ordering
  after a non-monotone start (Fig. 3). Piecewise-uniform, non-isotropic
  Gaussian and Gaussian-mixture inputs keep the ordering, though spherical
  harmonics are no longer the exact eigenfunctions (Figs. 4–6).
- **Appendix F.** On fresh test points the degree-1 and 2 projections fall
  with the training ones, but the degree-4 projection does not: the network
  fits that component on the training set and overfits it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Gradient descent on a wide two-layer ReLU network reduces the residual on each NTK eigenspace at a rate set by its eigenvalue, for arbitrary targets | strong in the NTK regime (proof) | Theorem 4.2, Appendix B.2 |
| C2 | Learning the top eigenspace needs a sample size scaling with the inverse square of the eigengap below it | strong (it is a sufficient condition in the proof, not shown necessary) | Theorem 4.2 |
| C3 | On uniform spherical data the bias-free two-layer NTK has zero eigenvalue on odd degrees ≥ 3, and its even-degree eigenvalues are Ω(max(k^(−d−1), d^(−k+1))) | strong (proof); lower bounds, not exact rates | Theorem 4.3, Appendix B.3 |
| C4 | Lower-degree spherical harmonics are learned first, faster, and with fewer samples and narrower networks | strong for the bound; moderate as an account of practice | Corollaries 4.6–4.7; §5 |
| C5 | The ordering survives non-uniform input distributions | weak: three synthetic distributions in R¹⁰, no theory | §5.3 |

## Concepts

- **spectral bias**: the tendency of networks to learn components of low
  complexity before high ones (Rahaman et al. 2019). Here made precise as
  eigenspaces of the NTK integral operator.
- **r_k**: the total multiplicity of the first k distinct eigenvalues of
  L_κ. A cut is always at a multiplicity boundary.
- **projected residual**: V_(r_k)ᵀ(y − ŷ), the residual's component in the
  sampled top-r_k eigenspace.
- **NTK integral operator** L_κ f(s) = ∫ κ(x, s) f(x) dτ(x), whose spectrum,
  not the sample Gram matrix's, carries the result.

## Connections

- **Basri et al. ([LIT-tmpb9f8h](../literature.d/LIT-tmpb9f8h.md)).** The same parity null space, the same
  ordering by frequency, exact eigenvalues where this paper has bounds, and
  a fix (bias) for the null space. Neither builds on the other.
- **Bietti & Bach ([LIT-tmp2fhfb](../literature.d/LIT-tmp2fhfb.md)).** Exact asymptotic decay for this kernel
  and its deep versions. This paper's Ω(k^(−d−1)) on S^d is consistent with
  their k^(−d) on S^(d−1).
- **Simon et al. ([LIT-242](../literature.d/LIT-242.md)).** Stepwise, top-eigenmode-first learning in
  linearised self-supervised learning: the kernel-PCA counterpart of this
  paper's kernel-regression dynamics.
- **Anthology.** The NTK ([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md)); Bordelon et al.'s spectral learning
  curves ([ANTH-LIT-328](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-328.md)); Tancik et al. ([ANTH-LIT-550](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-550.md)), who reshape the NTK
  spectrum with Fourier features to make high frequencies learnable.

## Bearing on the record

The owner filed this beside Fisher-spectrum block structure, Papyan's
spectra and evidence-based model comparison, which are being filed in
parallel. What follows is my reading; the paper says nothing about
thresholds or evidence.

- **Where a spectral cut is well posed.** Theorem 4.2 is stated only at
  multiplicity boundaries r_k, and its sample cost is driven by (λ_(r_k) −
  λ_(r_k+1))^(−2). A procedure that thresholds an empirical spectrum,
  whether to choose an effective dimension, prune directions or reduce a
  model, is reliable at a gap and unreliable inside a near-degenerate
  cluster. That is a Davis–Kahan-type condition, and Lemma B.1, taken from
  Su & Yang, is a statement of exactly that kind. Fisher and Hessian
  spectra with block structure would be thresholded safely between blocks.
- **Time as a soft threshold.** After T steps, eigendirection i has been
  fitted to the extent 1 − (1 − λ_i)^T. That is a soft spectral filter
  whose cut-off λ ≈ 1/T moves down the spectrum as training goes on. Early
  stopping is then a choice of cut, and Appendix F's overfitting on degree
  4 is what happens when the cut passes eigendirections the sample cannot
  support.
- **Exact zeros.** The odd-degree null space is a block with eigenvalue
  exactly zero, so no amount of training or data moves it. In a
  model-comparison reading these are directions the kernel's prior rules
  out, not directions with weak evidence.
- **No THEORY is filed.** A candidate is in the report to the owner.
- **ML practice.** None directly; `anthology-candidate` is for subject.

## Limitations

- **Two layers, NTK regime, squared loss.** The width requirement is
  polynomial in λ_(r_k)^(−1) and T, so for high degrees it is very large.
- **Lower bounds on eigenvalues**, not exact rates; the k ≫ d bound matches
  Bietti & Mairal's.
- **The eigengap condition is sufficient, not shown necessary.**
- **Non-uniform data is handled only empirically**, by treating it as model
  misspecification of the spherical-harmonic basis.
- **Experiments are small and synthetic**: one width, one sample size, one
  input dimension.

## Open questions

- Does the projected-residual picture survive feature learning, where the
  kernel moves during training?
- What replaces spherical harmonics as the eigenbasis for realistic input
  distributions, and does the ordering by eigenvalue still track any notion
  of frequency there?
- Is the eigengap dependence of the sample size tight?

## Corrections

- none to a seeded skim (there was no seed)
- **Citation.** The owner gave "Cao, Fang, Wu, Zhou & Gu (2019)", which
  matches the arXiv v1 date. The published version is IJCAI 2021 (Crossref,
  DOI 10.24963/ijcai.2021/304); I read the arXiv v3, not the proceedings
  version.
- **A typo in the source.** The text cites "Lemma 4.2" for near-orthonormality
  of the v_k in §5.1; the lemma is 4.1.
