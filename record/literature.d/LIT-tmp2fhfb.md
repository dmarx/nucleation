---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmp7irqb](../notes.d/NOTE-tmp7irqb.md)): main text and Appendix A in full, the proofs in Appendices B and C followed at the level of their lemmas. Worth reading as the general rule behind the NTK eigenvalue decays the record holds: for a dot-product kernel on the sphere, the decay of its spherical-harmonic eigenvalues is fixed by the kernel function''s non-integer exponent at the endpoints ±1 (Theorem 1). Deep ReLU kernels keep the shallow exponent, so depth leaves the spectrum''s shape unchanged: µ_k ~ C(d, L) k^(−d) for the NTK and k^(−d−2) for the random-feature kernel, with only the constant growing in L (Corollaries 2–3).'
title: 'Deep Equals Shallow for ReLU Networks in Kernel Regimes'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv 2009.14397v4 (26 August 2021, the ICLR 2021 camera
    version, 22 PDF pages), text extracted with PyMuPDF. Main text,
    Appendix A (spherical-harmonic background) and the statements of
    Lemmas 4–6 and Theorem 7 read; the proofs in Appendices B and C, and
    C.3 on step activations, followed at the level of their steps, not
    checked line by line. The owner cited "Bietti & Bach (2021)"; this is
    the one, the paper on NTK eigenvalue decay in the spherical-harmonic
    basis, and not Bietti & Mairal's "On the Inductive Bias of Neural
    Tangent Kernels" (NeurIPS 2019), which it builds on and which the
    record does not hold. Not held in the Anthology of the SOTA: a grep of
    its literature for the arXiv id, the title and "Bietti" found only a
    passing citation of a different Bietti et al. paper in ANTH-LIT-654.
tags:
- learning-theory
- representation-learning
- mathematics
- anthology-candidate
date: '2026-10-03'
published: '2020-09-30'
arxiv: '2009.14397'
first_author: 'Bietti'
keywords:
- 'neural tangent kernel'
- 'random features'
- 'dot-product kernels'
- 'spherical harmonics'
- 'eigenvalue decay'
- 'reproducing kernel Hilbert space'
- 'depth'
- 'Laplace kernel'
- 'approximation'
implementations:
- 'https://github.com/albietz/deep_shallow_kernel'
summary: >-
  Bietti & Bach (2021), ICLR 2021. Dot-product kernels on the sphere are
  diagonal in spherical harmonics, with one eigenvalue µ_k per degree k
  shared by N(d, k) ~ k^(d−2) harmonics. Theorem 1 reads the asymptotic
  decay of µ_k off the kernel function's expansion at ±1: a non-integer
  exponent ν there gives µ_k ~ k^(−d−2ν+1). The arc-cosine kernels have
  ν = 1/2 and 3/2, and composing them preserves ν, so the NTK of a deep
  ReLU network decays as k^(−d) and its random-feature kernel as k^(−d−2),
  exactly as for two layers. Deep and shallow ReLU kernels therefore have
  the same RKHS, the same as the Laplace kernel's for the NTK.
extends:
- LIT-tmpb9f8h
---

# LIT-tmp2fhfb: Deep Equals Shallow for ReLU Networks in Kernel Regimes

Alberto Bietti and Francis Bach (2021), *ICLR 2021* — [ARXIV-2009.14397](https://arxiv.org/abs/2009.14397)

## Key takeaways

- A dot-product kernel κ(xᵀx′) on the sphere S^(d−1) is diagonalised by the spherical harmonics. Every harmonic of degree k shares one eigenvalue µ_k (Eq. 8), and there are N(d, k) of them, growing as k^(d−2). The RKHS is the set of functions whose harmonic coefficients satisfy Σ a²_(k,j)/µ_k < ∞ (Eq. 9), so the eigenvalue decay is the whole story of which functions the kernel finds cheap.
- Theorem 1: if κ(1 − t) = p₁(t) + c₁t^ν + o(t^ν) near +1, with the matching expansion near −1 and ν non-integer, then µ_k ~ (c₁ ± c₋₁) C(d, ν) k^(−d−2ν+1), the sign depending on the parity of k. When the two endpoint constants cancel, one parity decays faster. A kernel smooth at both endpoints decays faster than any polynomial. The decay is read from the behaviour at aligned and anti-aligned inputs alone.
- For ReLU networks the arc-cosine kernels have exponents ν = 1/2 (κ₀) and ν = 3/2 (κ₁), and composition keeps them. Corollary 2 gives µ_k ~ C(d, L) k^(−d−2) for the L-layer random-feature kernel, and Corollary 3 gives µ_k ~ C(d, L) k^(−d) for the L-layer NTK. The constant grows linearly or quadratically in L; the exponent does not move. In the kernel regime, depth buys no approximation power for fully connected ReLU networks. Step activations are the exception: there the exponent falls with depth, ν = 1/2^(L−1) (§3.3, Appendix C.3).

## Standing in the record

Filed on 2026-10-03 at the owner's request, with Cao et al.'s proof that
gradient descent learns along NTK eigendirections at rates set by their
eigenvalues ([LIT-tmpycz0j](LIT-tmpycz0j.md)), and Basri et al.'s closed-form NTK eigenvalues
per frequency ([LIT-tmpb9f8h](LIT-tmpb9f8h.md)). The owner listed the three beside work on
Fisher-spectrum block structure, Papyan's spectra of deep-network Hessians,
and model comparison by evidence. Those are being filed in parallel. Read
in that company, this paper supplies the eigenstructure itself: what the
spectrum of the kernel is, how it is organised into blocks, and what sets
its decay.

It extends Basri et al. ([LIT-tmpb9f8h](LIT-tmpb9f8h.md)) in a precise sense. Basri et al.
computed the eigenvalues of the two-layer ReLU NTK, with and without a bias
term, one frequency at a time, and observed numerically that they decay
roughly like a power of k. Theorem 1 here gives the general rule that
produces those decays from the kernel's endpoint behaviour, recovers the
shallow cases, and adopts Basri et al.'s zero-initialised bias as the way to
remove the parity constraint (§2.2, §3.2). It then carries the result to
any depth. Cao et al. ([LIT-tmpycz0j](LIT-tmpycz0j.md)) is cited here among works on the
spectral properties of wide networks; its eigenvalue bound for the
two-layer NTK on S^d, Ω(k^(−d−1)), is the same decay in Cao's convention,
where d counts the sphere's dimension rather than the ambient one.

The block structure is the point for the record. Each degree k is one
eigenvalue with multiplicity N(d, k), so a threshold on this spectrum can
only keep or drop whole degrees. The decay exponent sets how quickly the
blocks shrink, and the theorem says the exponent is fixed by architecture
family (ReLU versus step, NTK versus random features) and not by depth.
That is the kernel-regime object a spectral threshold or a model-reduction
step would act on. The paper itself says nothing about thresholds, priors or
evidence; that reading is mine and is set out in [NOTE-tmp7irqb](../notes.d/NOTE-tmp7irqb.md).

The discrete twin of this picture is already in the record. O'Donnell's
*Analysis of Boolean Functions* ([LIT-346](LIT-346.md)) shows that the operators natural
to the hypercube are diagonal in the Fourier–Walsh basis with eigenvalues
depending only on the degree |S|. That is the same symmetry argument, with
the hypercube in place of the sphere. Peter and Weyl ([LIT-329](LIT-329.md)) is the
general theorem behind both: the decomposition of L² on a compact group, or
a homogeneous space of one, into irreducible pieces.

It carries `anthology-candidate` because its subject is a theory of neural
network kernels, which anthology topics can hold. The anthology already
holds the NTK paper itself ([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md)), Bordelon et al.'s spectrum-dependent
learning curves ([ANTH-LIT-328](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-328.md)), which turn exactly these eigenvalue decays
into generalisation curves, and Tancik et al. on Fourier features
([ANTH-LIT-550](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-550.md)), which reshape the NTK spectrum on purpose. It carries no
instruction for practice.
