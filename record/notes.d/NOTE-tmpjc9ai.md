---
status: Skimmed
paper: LIT-tmpa4ye5
title: 'Spectral contrastive loss (HaoChen et al.)'
version: 1
date: '2026-09-26'
summary: >-
  Minimizing the population spectral contrastive loss L(f) = −2E[f(x)ᵀf(x⁺)] + E[(f(x)ᵀf(x⁻))²] is, up to a constant, a rank-k factorization of the normalized adjacency matrix of the augmentation graph, so its minimizers are the top-k eigenvectors (eigenfunctions, in the infinite case) of that graph up to a row scaling and an invertible linear map — neither of which changes linear-probe accuracy.
---
<!-- inactive-ok-file: LIT-tmpa4ye5 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpjc9ai: Spectral contrastive loss (HaoChen et al.)

## Contribution

Earlier theory of contrastive learning assumed positive pairs are conditionally independent given the class, which augmentations of one image are not. The paper instead defines a population augmentation graph whose vertices are augmented data and whose edge weights are the probability that two augmentations come from the same natural example. It proposes a loss that performs spectral decomposition of this graph and can be written as a contrastive objective on network outputs. Minimizing it gives features with provable linear-probe accuracy guarantees, which transfer to the empirical loss via standard generalization bounds, and the features match or beat strong baselines on vision benchmarks.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §3.1, eqs. 2–3: edge weight w(x,x′) = E_x̄[A(x|x̄)A(x′|x̄)]; the object decomposed is the normalized adjacency D^{−1/2}AD^{−1/2}. X is taken finite "to avoid … functional analysis", with the infinite case deferred to App. F.
- §3.2, eq. 4 and Lemma 3.2: min_F ‖Ā − FFᵀ‖²_F (Eckart–Young gives the top-k eigenvectors up to a scaling and a rotation); substituting u_x = w_x^{1/2} f(x) turns this into the spectral contrastive loss (eq. 6) plus a constant.
- Lemma 3.1: a positive diagonal row scaling D and an invertible right factor Q leave linear-probe predictions unchanged (the probe B becomes Q⁻¹B). This is the paper's formal reason the eigenbasis only needs to be recovered up to a linear map.
- Thm 3.8: linear-probe error of the population minimizer is Õ(α/ρ²_{⌊k/2⌋}), where α is the cross-class edge mass and ρ a sparsest-partition constant; Thm 4.3 adds finite-sample terms.
- App. F, eq. 69 and Thm F.2: for X = ℝᵈ the adjacency becomes an integral operator with kernel w(u,v)/√(w(u)w(v)) on L²(ℝᵈ). Under the regularity condition F.1 this kernel is square-integrable, so L − I is Hilbert–Schmidt and "the spectral theorem applies", giving an orthonormal eigenbasis with λ_i ∈ [0,1]. Symmetry of w (so that the operator is self-adjoint) is used implicitly here and never named.

## Open questions

- It is the founding "SSL = eigenfunctions of an augmentation operator" statement that [LIT-227](../literature.d/LIT-227.md), [LIT-228](../literature.d/LIT-228.md), [LIT-235](../literature.d/LIT-235.md) and Johnson et al. (ra2) all build on or restate.
- Self-adjointness enters only through the symmetric weight w(x,x′) = w(x′,x) and the Hilbert–Schmidt spectral theorem in App. F. A deeper reading should check whether anything else in the proofs (e.g. the Cheeger-type arguments for Thm 3.8) needs it.
- Lemma 3.1 is the formal version of "a linear probe only sees a representation up to GL(k)", which bears on concept-direction geometry (cf. [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md)).

## Skim, from the density-ratio strand

*A second skim, made independently while pursuing the Radon–Nikodym connection, and kept because it reads the paper for a different question.*

- §3.1: w_{xx'} is the probability that a random positive pair is (x, x'); w_x = Σ_{x'} w_{xx'}; Eq. 3 defines the normalized adjacency matrix Ā = D^{-1/2} A D^{-1/2} with A_{xx'} = w_{xx'}, D_{xx} = w_x.
- §3.2, Eq. 4: L_mf(F) = ‖Ā − FFᵀ‖²_F; by Eckart–Young–Mirsky any minimizer is F*·diag(√γ_1..√γ_k)·R for orthonormal R.
- Lemma 3.1: left-multiplying embeddings by a positive diagonal matrix and right-multiplying by an invertible matrix leaves linear-probe performance unchanged.
- Lemma 3.2 and its proof, Eq. 6–7: with u_x = w_x^{1/2} f(x), L_mf = Σ_{x,x'} (w_{xx'}/√(w_x w_{x'}) − u_xᵀu_{x'})², which expands to a constant plus L(f) = −2E_{x,x⁺}[f(x)ᵀf(x⁺)] + E_{x,x⁻}[(f(x)ᵀf(x⁻))²].
- Rewritten per pair, the same sum is Σ w_x w_{x'} (w_{xx'}/(w_x w_{x'}) − f(x)ᵀf(x'))²: the target of f(x)ᵀf(x') is the joint-over-product ratio w_{xx'}/(w_x w_{x'}). This is my algebra on their Eq. 7; the paper does not name the ratio a density ratio or PMI (no occurrence of "mutual information", "PMI" or "density ratio" in the text).
- Theorem 3.8 (main, population case) and 3.11 (mixture of manifolds) give linear-probe error bounds in terms of eigenvalue gaps; not read in detail.

What that strand asks a deeper reading to check:

- It is the spectral half of the PMI–spectral bridge: the matrix it factorizes is a similarity-transformed version of the exponentiated-PMI (density-ratio) matrix. Johnson et al. (rb4, App. B.3) are the ones who say so.
- Held works [LIT-227](../literature.d/LIT-227.md) and [LIT-235](../literature.d/LIT-235.md) build on it; a note for it gives them something to cite.
- Check §4's claim that the population loss admits an unbiased finite-sample estimator, and Theorem 3.8's exact assumptions.
