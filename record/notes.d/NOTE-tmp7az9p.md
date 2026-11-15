---
status: Read
paper: 'LIT-tmpfzpbg'
title: 'Bruna and Mallat — Invariant scattering convolution networks'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:1203.1513v2, https://arxiv.org/pdf/1203.1513,
    15 pages, text by pdftotext. Read: §1–2 (against Fourier and
    registration invariants; scattering wavelets; the network), §3.1
    (energy and deformation stability), §3.2 (stationary processes) and §4
    (classification: MNIST and USPS, Tables 4–6; rotated and scaled MNIST,
    Tables 7–8; CUReT, Table 9). Skimmed: §3.3 (cosine transform for
    compression) and §3.4 (fast algorithm). Not in this paper and not read:
    the proofs of the stability and energy theorems, which are in Mallat's
    "Group Invariant Scattering", ref. [22]. The filer rechecked every
    quote below against the downloaded text; all were found. The reader's
    "explains important properties" reads "explain important properties" in
    the abstract and is quoted so. The reader's "Table 2" for the energy
    decay is Table 1 in the text.
date: '2026-11-15'
summary: >-
  A deep convolution network with fixed wavelet filters: cascaded wavelet
  convolutions, complex modulus and local averaging. It is translation
  invariant below 2^J, contractive, and, by a theorem it states from
  Mallat's "Group Invariant Scattering", Lipschitz-stable to small
  deformations; almost all energy is within three layers. Second-order
  coefficients carry moments up to order four. With an SVM or a PCA
  classifier it reaches state-of-the-art error on MNIST, USPS and CUReT
  without learned filters.
---
<!-- inactive-ok-file: LIT-tmpfzpbg THEORY-tmpw4lo5 CLAIM-182 — new entries of this filing, and a Proposed claim cited as having no bearing -->

# NOTE-tmp7az9p: Bruna and Mallat — Invariant scattering convolution networks

## Contribution

A deep convolutional architecture whose properties are proved rather
than trained into it: invariance to translation below a scale,
Lipschitz stability to small diffeomorphisms (proved in [22]),
conservation of energy with fast decay along depth, and fixed filters.
The authors use it to explain properties of learned CNNs and to reach
competitive accuracy without learning any filter.

## Key insight

Wavelets are stable to deformation but only covariant to translation; any
linear invariant built from them is zero. A non-linearity that commutes
with deformations and keeps L² stability must be the modulus, which
pushes energy to lower frequencies where averaging can keep it. Cascading
the two gives invariants that do not throw away the high frequencies.

## Assumptions

- The wavelet frame satisfies the Littlewood–Paley bound (1 − ε) ≤ … ≤ 1;
  Morlet wavelets with ε = 0.25 are used.
- Signals have compact support, for the stability bound.
- Deformations are small, ‖∇τ‖∞ < 1.
- The relevant variability is translation and deformation; rotation and
  scaling are handled by extensions and by PCA.
- The filters are designed, not learned.

## Key results

- **Architecture** (abstract): "It cascades wavelet transform convolutions
  with non-linear modulus and averaging operators." The windowed
  scattering is S_J[p]x = |||x ⋆ ψλ1| ⋆ ψλ2| … ⋆ ψλm| ⋆ φ_2J.
- **The requirement** (Eq. 2): ‖Φ(L_τ x) − Φ(x)‖ ≤ C‖x‖ sup|∇τ(u)|, which
  Fourier modulus and registration invariants fail at high frequencies.
- **The modulus is forced** (§2.2): with M commuting with deformations and
  L²-stable, "one can verify [6] that necessarily" M x = e^{iα}|x|.
- **Stability** (§3.1, Eq. 13): "it is proved in [22] that for signals x of
  compact support" ‖S_J(L_τ x) − S_J x‖ ≤ C m_max ‖x‖ (2^−J ‖τ‖∞ + ‖∇τ‖∞),
  reducing to the Lipschitz form (Eq. 14) for 2^J ≫ ‖τ‖∞.
- **Contraction and energy** (§2–3.1): under the Littlewood–Paley
  condition ‖S_J x − S_J y‖ ≤ ‖x − y‖; with a unitary wavelet transform the
  energy is conserved (proved in [22]); on Caltech-101 images the energy
  on paths of length m "is below 1% for m ≥ 3" (Table 1).
- **Textures** (§3.2): "scattering coefficients of order 2 are highly
  dissimilar because they depend on moments up to order 4", separating
  processes with the same power spectrum.
- **MNIST** (Table 4): with 60,000 training samples, second-order
  scattering with an SVM gives 0.43% error, against 0.53% for a
  convolution network; "below 5 · 10³ training samples" the scattering PCA
  classifier does better than the convolution network.
- **CUReT** (Table 9): second-order scattering with PCA, 0.2% error,
  against 1.53% for a textons SVM and 2.4% for an MRF model.

## Concepts

Scattering transform; wavelet modulus; Lipschitz stability to
diffeomorphisms; translation invariance below 2^J; energy conservation
and decay along frequency-decreasing paths; higher-order moments;
fixed-filter deep network.

## Bearing on the record

- **A's characterization**: "cascaded wavelet transforms, nonlinear
  modulus operations, and averaging yield useful invariance and
  deformation-stability properties" holds. A omits that the theorems are
  proved in [22], unread, and that the filters are not learned; the
  abstract's claim that the analysis "explain[s] important properties of
  deep convolution networks" is by architecture, not by analysis of trained
  networks.
- **THEORY-758 (diffusion wavelets)**: a contrast to file. Both are
  multiscale wavelet constructions, about an octave a scale. THEORY-758's
  levels are exactly closed linear coarse-grainings of a diffusion
  operator. Here a linear multiscale decomposition is only covariant
  (§2.2: ∫ x ⋆ ψλ(u) du = 0 for all x), and invariance needs the modulus.
  Linear coarse-graining gives covariance; invariance needs a
  non-linearity.
- **QUESTION-058**: bears. A representation invariant to a group of
  deformations is obtained here from architecture alone, with no task or
  training, which is one end of that question's division between task,
  architecture and data.
- **NOTE-684 (LIT-880) and NOTE-476 (LIT-618)**: both cite this line of
  work without holding it. NOTE-684 takes it as the deformation side of the
  Sparse Random Hierarchy Model.
- **TERM-064 (legibility)**: interpretive. Scattering is a designed
  observer under which class distinctions become recoverable by a linear
  or Gaussian classifier while translation and small deformation are
  discarded, a case of the term's relation among representation,
  observer's rule class and task.
- **CLAIM-182, THEORY-272, THEORY-1036**: no bearing.

## Limitations

- The stability and energy proofs are in [22], unread; this reading
  verifies the statements and the experiments only.
- MNIST, USPS and CUReT are small benchmarks by later standards.
- The claim to explain deep networks is architectural analogy.
- §3.3–3.4 were skimmed.
