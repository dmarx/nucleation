---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmp7az9p](../notes.d/NOTE-tmp7az9p.md)), with §3.3–3.4 skimmed, from
  arXiv:1203.1513v2, from arxiv.org. The stability and energy theorems it
  states are proved in Mallat's "Group Invariant Scattering", its ref.
  [22], which was not read. Worth reading here as the source of scattering
  networks, which [NOTE-684](../notes.d/NOTE-684.md) (on [LIT-880](LIT-880.md)) and [NOTE-476](../notes.d/NOTE-476.md) (on [LIT-618](LIT-618.md)) cite as
  not held: a deep convolutional cascade of fixed wavelets, modulus and
  averaging, invariant to translation below a scale and stable to small
  deformations, and the record's contrast to linear multiscale
  coarse-graining ([THEORY-758](../theory.d/THEORY-758.md)).
title: 'Invariant Scattering Convolution Networks'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on wave
    mathematics and learning, where A gives scattering networks as harmonic
    analysis that explains invariance. Citation checked against the arXiv
    API and Crossref (no mailto): Joan Bruna and Stéphane Mallat, IEEE
    Transactions on Pattern Analysis and Machine Intelligence 35(8):
    1872–1886, August 2013, doi:10.1109/TPAMI.2012.230. `published:` is the
    arXiv v1 date, 2012-03-05; v2 (2012-03-08) is the copy read. No email
    address was sent to any service.
tags:
- representation-learning
- mathematics
- anthology-candidate
date: '2026-11-15'
published: '2012-03-05'
arxiv: '1203.1513'
doi: '10.1109/TPAMI.2012.230'
first_author: 'Bruna'
keywords:
- 'scattering transform'
- 'wavelets'
- 'deformation stability'
- 'translation invariance'
- 'deep convolution networks'
- 'texture discrimination'
implementations: []
summary: >-
  Bruna & Mallat (2013). The windowed scattering transform cascades fixed
  wavelet convolutions, complex modulus and local averaging: a deep
  convolution network with designed filters, translation invariant below
  2^J and, by a theorem stated from Mallat's "Group Invariant Scattering",
  Lipschitz-stable to small deformations; its energy is almost all within
  three layers. With an SVM, 0.43% error on MNIST; with a PCA classifier,
  0.2% on CUReT. Fills the gap [NOTE-684](../notes.d/NOTE-684.md) names, and bears on [THEORY-758](../theory.d/THEORY-758.md): a
  linear multiscale decomposition gives covariance, and invariance needs
  the modulus.
---
<!-- inactive-ok-file: THEORY-tmpw4lo5 — Proposed or Skimmed entries of this filing -->

# LIT-tmpfzpbg: Invariant Scattering Convolution Networks

Bruna, J. & Mallat, S. (2013). Invariant Scattering Convolution Networks. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 35(8): 1872–1886. arXiv:1203.1513. doi:10.1109/TPAMI.2012.230.

## Key takeaways

*From the reading, [NOTE-tmp7az9p](../notes.d/NOTE-tmp7az9p.md); the account is [THEORY-tmpw4lo5](../theory.d/THEORY-tmpw4lo5.md).*

- **Architecture** (abstract): "It cascades wavelet transform convolutions
  with non-linear modulus and averaging operators"; the filters are fixed,
  not learned.
- **Why a modulus** (§2.2): a linear invariant of a wavelet output
  vanishes, since ∫ x ⋆ ψλ(u) du = 0; for a non-linearity that commutes
  with deformations and is L²-stable, "one can verify [6] that necessarily"
  it is a pointwise modulus.
- **Stability** (§3.1, Eq. 13, proved in [22]): ‖S_J(L_τ x) − S_J x‖ ≤
  C m_max ‖x‖ (2^−J ‖τ‖∞ + ‖∇τ‖∞) for compactly supported x; the
  transform is contractive, and its energy beyond three layers "is below 1%
  for m ≥ 3".
- **Higher moments** (§3.2): "scattering coefficients of order 2 are highly
  dissimilar because they depend on moments up to order 4", so they
  separate textures with the same power spectrum.
- **Classification** (Tables 4, 9): 0.43% error on MNIST with an SVM
  (convolution net 0.53%); 0.2% on CUReT with PCA.

## Standing in the record

Filed with the optics and holography batch of 2026-11-15. A's description,
that "cascaded wavelet transforms, nonlinear modulus operations, and
averaging yield useful invariance and deformation-stability properties",
holds and closely paraphrases the abstract. It omits that the key theorems
are proved elsewhere, in Mallat's "Group Invariant Scattering", unread, and
that the filters are designed: the claim that scattering "explain[s]
important properties of deep convolution networks" is an argument from
architecture, not an analysis of trained networks.

[NOTE-684](../notes.d/NOTE-684.md), the reading of the Sparse Random Hierarchy Model ([LIT-880](LIT-880.md)), names
Bruna and Mallat's scattering networks as the deformation side of that
model and as not held; [NOTE-476](../notes.d/NOTE-476.md) ([LIT-618](LIT-618.md)) cites scattering-transform theory
too. This filing holds it. Its sharpest bearing is on [THEORY-758](../theory.d/THEORY-758.md) (diffusion
wavelets): both are multiscale wavelet constructions, but [THEORY-758](../theory.d/THEORY-758.md)'s
levels are exactly closed linear coarse-grainings, and this paper shows
that a linear multiscale decomposition is only covariant; invariance needs
the modulus, which moves energy toward lower frequencies.
