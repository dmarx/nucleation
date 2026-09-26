---
number: 219
status: Skimmed
formerly:
- NOTE-tmp5kviu
paper: LIT-250
title: 'Duality of Bures and Shape Distances'
version: 1
date: '2026-09-26'
summary: >-
  The Procrustes shape distance between two representations (optimal rotational alignment of units) equals the Bures distance between their centred linear kernel matrices, so the rotation-invariant geometry of a representation is exactly the geometry of its kernel, and through Uhlmann's theorem the fidelity of two kernels is the maximum overlap over all representations consistent with them.
---
<!-- inactive-ok-file: LIT-250 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-219: Duality of Bures and Shape Distances

## Contribution

The authors sort representational (dis)similarity measures into two camps: those that fit explicit alignments between neural units (regression, CCA, shape distances), and those that compare stimulus-by-stimulus summary statistics already invariant to nuisance transforms (RSA, CKA, normalised Bures similarity). They show the two camps meet: the cosine of the Riemannian shape distance equals the normalised Bures similarity. They use this duality to reinterpret both measures, including asymptotically, and contrast them with CKA, which they find only loosely related.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.2: "X and Y have the same RDM if and only if the size-and-shape Procrustes distance between X and Y is zero". Kernel matrices K_X = CXXᵀC are invariant to rotations, reflections and translations. NBS and the Bures distance (eqs. 11–13) use the quantum fidelity F(K_X,K_Y) = Tr[(K_X^{1/2} K_Y K_X^{1/2})^{1/2}].
- §3, Theorem 1 with Lemma 2: B(K_X,K_Y) = P(X,Y) and NBS(K_X,K_Y) = cos θ*(X,Y), because F(K_X,K_Y) = ‖Σ_XY‖_* (nuclear norm of the cross-covariance). A corollary is that the generalised shape distances (eqs. 7–8) are metrics even when the networks differ in width.
- §5.3, eqs. (25)–(26): for a fixed PSD K_X, the matrices X with XXᵀ = K_X "are related by orthogonal transformations", XU = X′. Maximising |Tr[XᵀY]| over all X, Y consistent with K_X and K_Y gives F(K_X,K_Y), which is Uhlmann's theorem. Linear CKA of the square roots is a suboptimal value of the same maximisation (eq. 27), with Fuchs–van de Graaf bounds (eq. 28).
- §6: the authors present NBS and Bures as rooted in quantum information theory and optimal transport (the Bures distance is the 2-Wasserstein distance between centred Gaussians, §2.2), and pose as an open question whether other measures have similar dualities.

## Open questions

- It is the clearest statement found, in the representation-similarity literature, that the kernel is the invariant and a representation is one realisation of it, determined up to an orthogonal transform. It also imports density-matrix language (fidelity, Uhlmann's theorem, purification-like "consistent" realisations) to say so. It does not mention GNS.
- A deeper reading should check §4 (limits M→∞ and N→∞), where the kernel becomes an operator. That is where the finite Gram statement should become the RKHS or GNS statement, and whether the authors' functional-analytic citation [34] does that.
- Check the trace normalisation: NBS treats K/Tr K as a density matrix, which is exactly the Bach (2022) move applied to the empirical kernel.
