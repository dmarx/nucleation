---
number: 481
status: Read
formerly:
- NOTE-tmppsytl
paper: 'LIT-612'
title: 'The Convergence Rate of Neural Networks for Learned Functions of Different Frequencies'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv 1906.00425v3 (15 pages) through PyMuPDF text
    extraction, with Eqs. 12–14 and Figure 7 checked against page images
    because the extraction dropped their constants. Sections 1–5 and the
    cross-entropy appendix read in full. The appendix deriving the S^d
    eigenvalues (integrals of powers of sine and cosine, Gegenbauer
    derivatives, Eqs. 17–18) skimmed, not re-derived. The convergence
    theorem (Eq. 5) and the generalisation bound behind Eq. 14 are Arora
    et al.'s Theorems 4.1 and 5.1, taken as the paper reports them.
date: '2026-10-03'
summary: >-
  For uniform data the wide two-layer ReLU Gram matrix H∞ is a convolution
  on the sphere, so its eigenvectors are Fourier modes or spherical
  harmonics. On S¹, bias-free: λ_k = 1/π², 1/4, 2(k²+1)/(π²(k²−1)²) and 0
  for k = 0, 1, even k ≥ 2 and odd k ≥ 3 (Eq. 12). With zero-initialised
  bias, odd k ≥ 3 get 1/(π²k²) (Eq. 13). Learning time grows as k² on S¹
  and about k³ on S², as measured for shallow, deep and residual networks
  (Figs. 6–7).
---

# NOTE-481: The Convergence Rate of Neural Networks for Learned Functions of Different Frequencies

## Contribution

Explicit eigenvalues, frequency by frequency, for the linear dynamics that
govern a wide two-layer ReLU network under gradient descent, on uniform
data on S¹ and S^d. Two consequences were new: the bias-free model used in
the theory of the time cannot represent odd frequencies above one, and with
bias restored the time to learn frequency k grows as a fixed power of k
that real deep networks also show.

## Key insight

When the data are uniform on a sphere, the kernel that governs training
depends only on the angle between inputs, so it acts as a convolution, and
convolutions are diagonal in the Fourier basis. Reading off the Fourier
coefficients of the kernel gives the learning rate of every frequency at
once. One of those coefficients being exactly zero is not a small effect.
It is a family of functions the model cannot express, which a finite
sample hides by mapping them to small eigenvalues.

## Assumptions

- **Model** (Eq. 1): f(x; W, a) = (1/√m) Σ_r a_r σ(w_rᵀx), ReLU, second
  layer a_r ∈ {±1} fixed, first layer w_r ~ N(0, κ²I) trained by GD on L2
  loss. The theory is the linearised (lazy) dynamics of Du et al. and Arora
  et al.
- **Inputs normalised**, ‖x‖ = 1, and **uniformly distributed** on S^d,
  in the limit n → ∞ for the convolution argument (Theorem 1).
- **Bias** is introduced through homogeneous coordinates, x̄ = (xᵀ, 1)ᵀ/√2,
  with bias initialised at zero. This gives the kernel H̄∞ of Eq. 11.
- **Convergence time** is read from Arora et al.'s Eq. 5, ‖y − u(t)‖ =
  (Σ_i (1 − ηλ_i)^(2t)(v_iᵀy)²)^(1/2) ± ε, under its width, initialisation
  and step-size conditions, which depend on the smallest eigenvalue λ₀.

## Key results

- **Theorem 1.** With uniform data, H∞_ij = xᵢᵀxⱼ(π − arccos(xᵢᵀxⱼ))/2π
  discretises a rotation-invariant kernel and so forms a convolution on
  S^d. Its eigenvectors are the Fourier series on S¹ and, by Funk–Hecke
  (Theorem 3), the spherical harmonics on S^d.
- **Theorem 2.** The bias-free network's harmonic expansion has zero
  coefficient at every odd frequency k ≥ 3. A single unit max(wᵀx, 0)
  equals ½ wᵀx plus an even function, so its only odd harmonic is degree 1.
- **Theorem 4.** The eigenvalues of convolution with K∞ vanish on odd
  harmonics with k ≥ 3, on any S^d.
- **Eigenvalues on S¹, bias-free (Eq. 12).** a_k = 1/π² (k = 0), 1/4 (k =
  1), 2(k²+1)/(π²(k²−1)²) for even k ≥ 2, 0 for odd k ≥ 3. Numerically,
  H∞ on a finite sample has its smallest eigenvectors at the low odd
  frequencies (Fig. 4).
- **Eigenvalues on S¹, with bias (Eq. 13).** c_k = 1/(2π²) + 1/8 (k = 0),
  1/π² + 1/8 (k = 1), (k²+1)/(π²(k²−1)²) for even k ≥ 2, 1/(π²k²) for odd
  k ≥ 3. Every frequency passes, and all decay as 1/k².
- **Convergence time.** From (1 − ηλ̄_i)^(t_i) < δ̄ + ε, t_i ≳ −log(δ̄ +
  ε)/(ηλ̄_i), so quadratic in k on S¹. Measured to 5% error: bias-free
  k^2.15 on the even frequencies, odd ones never converging; with bias
  k^1.93; a 5-layer network k^1.94; a 10-layer residual network k^2.11
  (Fig. 6). Under cross-entropy with a residual network, k^2.34 (Fig. 8).
- **On S² (Eqs. 17–18, Fig. 7).** The predicted time is about k³; measured
  k^2.74 bias-free, k^2.87 with bias, k^3.13 for a 10-layer residual
  network. The decay exponent g(d) of the coefficients, computed to k =
  1,000, is plotted from g(2) = 3 up to about 95.8 at d = 100.
- **Generalisation (Eq. 14).** For a band-limited target y = Σ_(k≤k̄)
  α_k e^(2πikx), L_D ≲ √(2yᵀ(H̄∞)⁻¹y/n) ≈ √(2π Σ_k α_k²k²/n), so for a pure
  sine the bound grows linearly in k.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For uniform data on a sphere, the eigenvectors of the wide two-layer ReLU Gram matrix are Fourier modes or spherical harmonics | strong (proof, in the n → ∞ limit) | Theorems 1, 3 |
| C2 | A bias-free two-layer ReLU network cannot represent or learn odd frequencies k ≥ 3 | strong (proof), and shown in training | Theorems 2, 4; Fig. 3 |
| C3 | With bias, the eigenvalues fall as 1/k² on S¹, so learning time grows quadratically in frequency | strong for the model (closed form); moderate empirically | Eq. 13, Fig. 6 |
| C4 | The same power law holds for real deep and residual networks | moderate: one architecture each, 1-D and 2-D data embedded in R³⁰, exponents from curve fits to the measured times | Figs. 6–8 |
| C5 | On S^d the eigenvalues decay roughly as a power of k that grows with d | moderate: computed numerically from closed forms to k = 1,000 | Fig. 7 right |
| C6 | Gradient descent acts as a frequency-based regulariser, and early stopping selects smooth functions | weak: an interpretation, argued by analogy with signal processing | §5 |

## Concepts

- **H∞**: the expected Gram matrix of the linearised two-layer network
  over initialisations; the NTK of the first layer, in later terms.
- **frequency**: the Fourier index on S¹, the harmonic degree on S^d.
- **homogeneous coordinates**: appending a constant to the normalised input
  so that a bias becomes an ordinary weight.
- **convergence time**: iterations until the fitting error falls to 5% of
  its initial value.

## Connections

- **Bietti & Bach ([LIT-608](../literature.d/LIT-608.md))**, which extends this paper. They derive
  its decays from endpoint regularity, use its bias kernel, and prove
  depth-independence.
- **Cao et al. ([LIT-624](../literature.d/LIT-624.md)).** The odd-degree null space again, as part
  of a spectral bound, with a theorem for finite widths and arbitrary
  targets.
- **O'Donnell ([LIT-346](../literature.d/LIT-346.md)).** On the hypercube, operators are diagonal in the
  Fourier–Walsh basis with eigenvalues depending on degree only. That is the
  discrete form of this paper's convolution argument.
- **Nanda et al. ([LIT-345](../literature.d/LIT-345.md)).** A network that ends up using a few mid-range
  Fourier frequencies on Z₁₁₃, under weight decay and long training. That
  regime is far from the lazy one this paper analyses.
- **Anthology.** Tancik et al. ([ANTH-LIT-550](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-550.md)) cite the slow learning of high
  frequencies and fix it by changing the input embedding, which reshapes
  the kernel's spectrum.

## Bearing on the record

The owner filed this beside Fisher-spectrum block structure, Papyan's
spectra and evidence-based model comparison, which are being filed in
parallel. What follows is my reading, not the paper's.

- **A structural zero block.** The bias-free kernel's odd frequencies above
  one are an eigenspace with eigenvalue exactly zero, set by architecture.
  On a finite sample they become the smallest non-zero eigenvalues (Fig. 4),
  indistinguishable by size from genuinely weak directions. A spectral
  threshold would remove them, which is right, but it could not tell them
  apart from directions the data merely under-determine. The difference
  matters for model reduction: one is a model that cannot express the
  function, the other a model whose evidence for it is weak.
- **The bound is a Gaussian-process data-fit term.** yᵀ(H∞)⁻¹y in Eq. 14 is
  the same quadratic form as the data-fit term −½yᵀK⁻¹y in the log marginal
  likelihood of a Gaussian process with covariance K = H∞. (The GP evidence
  also has a log-determinant term, which Eq. 14 lacks.) In the Fourier
  basis it is Σ α_k²/λ_k, so the k² weighting in Eq. 14 is the 1/λ_k
  penalty a GP with this kernel would charge in an evidence comparison.
  Frequencies the kernel deems improbable cost the most, in both the
  generalisation bound and the Occam factor.
- **No THEORY is filed.** A candidate is in the report to the owner.
- **ML practice.** The early-stopping remark is an interpretation (C6), not
  an instruction; `anthology-candidate` is for subject.

## Limitations

- **Lazy regime, two layers, uniform data, normalised inputs.** The authors
  flag the lazy-training critique and leave its relevance to large systems
  open (§2).
- **Convergence times use the asymptotic log(1 − ηλ) ≈ −ηλ** and ignore
  initialisation effects, which the authors say slow the lowest frequencies.
- **The theoretical curves in Figs. 6–7 are scaled by a fitted
  multiplicative constant**, so only the exponents are compared.
- **The S^d eigenvalues are shown only for even d**, "for simplicity"
  (§4.2).

## Open questions

- How do the eigenvalues and convergence times change for non-uniform
  densities? (The same group's later ICML 2020 paper takes this up; the
  record does not hold it.)
- Does the power law persist outside the lazy regime, where the kernel
  moves?

## Corrections

- none to a seeded skim (there was no seed)
- **Loose caption.** Fig. 7 says the coefficients "decay roughly as
  1/k^d", but its own plot gives g(2) = 3, and on S² the predicted and
  measured times are about k³. Near d = 2 the decay is k^(−(d+1)) in this
  paper's convention, where d counts the sphere's dimension. That matches
  Bietti & Bach's k^(−d) in theirs, where d is the ambient dimension. The
  plotted g(d) falls slightly below d + 1 at large d, plausibly because
  k = 1,000 is not yet asymptotic there.
