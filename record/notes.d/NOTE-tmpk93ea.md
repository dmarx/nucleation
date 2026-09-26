---
status: Skimmed
paper: LIT-tmptq8db
title: 'Contrastive learning finds an optimal eigenbasis'
version: 1
date: '2026-09-26'
summary: >-
  The InfoNCE, NT-Logistic and spectral contrastive losses all have the same population minimizer, the positive-pair kernel K⁺(a₁,a₂) = p⁺(a₁,a₂)/(p(a₁)p(a₂)). Kernel PCA under K⁺ returns exactly the eigenfunctions of the positive-pair Markov chain, and the top-d of those span the linear-predictor subspace that minimizes worst-case approximation error over approximately view-invariant targets.
---
<!-- inactive-ok-file: LIT-tmptq8db — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpk93ea: Contrastive learning finds an optimal eigenbasis

## Contribution

The paper reinterprets several contrastive objectives as learning a parameterized kernel that approximates one fixed positive-pair kernel. Combining that kernel with kernel PCA gives a representation that provably minimizes the worst-case error of linear predictors, assuming positive pairs have similar labels. The analysis expands target functions in the eigenfunctions of a Markov chain over positive pairs and shows that these eigenfunctions coincide with the kernel-PCA outputs. It gives downstream generalization bounds and shows on synthetic tasks that kernel PCA on trained contrastive models approximately recovers the eigenfunctions, with accuracy depending on the kernel parameterization and the augmentation strength.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2, Table 1 and Def. 2.1: once exp(hᵀh/τ) is read as the model's kernel, NT-XEnt, NT-Logistic and spectral contrastive loss share the population minimum K⁺ (up to a class-dependent constant for NT-XEnt). K⁺ = ⟨φ⁺(a₁),φ⁺(a₂)⟩ is a Mercer kernel with an explicit feature map (eq. 2). A and Z are taken finite (fn. 1).
- §3.2 and Prop. 3.1: the eigenfunctions f_i of the chain p⁺(a_{t+1}|a_t) are orthonormal in L²(p) (citing Levin & Peres ch. 12), and E_{p⁺}[(g(a₁)−g(a₂))²] = Σ(2−2λ_i)c_i², so view-invariant targets concentrate on eigenvalues near 1.
- Thm 3.2: population kernel PCA under K⁺ gives σ_i² = λ_i and h_i = λ_i^{1/2} f_i.
- Thm 4.1 (eqs. 5–6): the span of the top-d eigenfunctions is simultaneously the most view-invariant d-dimensional class and the minimax-optimal one for least-squares approximation of targets satisfying Assumption 1.1. Prop. 4.2 gives an excess-risk bound.
- App. C: the proofs rest on the positive-pair joint matrix P_{A,A} being symmetric. The chain's eigenvectors are rescaled into those of the symmetric M = D^{−1/2}P_{A,A}D^{−1/2}, which "is exactly the symmetrized adjacency matrix described by HaoChen et al." and is diagonalized by an orthogonal V. §5 notes that HaoChen's eigenvectors equal these eigenfunctions scaled by p(a)^{1/2}.
- App. E.2: SpIN and NeuralEF applied to K⁺ recover the same eigenfunctions from paired views, via R_ij = E_{p⁺}[f̂_i(a₁)f̂_j(a₂)], and NeuralEF so rewritten "closely resembles" VICReg.

## Open questions

- It is the most explicit single statement that InfoNCE-family losses target one kernel, and that the downstream-optimal representation is that kernel's top eigenfunctions. It gives the spectral reading an optimality claim, not just a correspondence.
- Where self-adjointness is used: reversibility of the positive-pair chain, p(a₁)p⁺(a₂|a₁) = p⁺(a₁,a₂) = p(a₂)p⁺(a₁|a₂), makes the transition operator self-adjoint on L²(p). That gives the real spectrum and orthonormal eigenbasis every later step needs. A deeper reading should confirm no step survives without it (e.g. asymmetric SSL such as BYOL-style predictors).
- Check how far the finite-A setting and synthetic experiments (overlapping regions, subsampled MNIST) support claims about real ImageNet-scale training.

## Skim, from the density-ratio strand

*A second skim, made independently while pursuing the Radon–Nikodym connection, and kept because it reads the paper for a different question.*

- §2, Table 1: population minimum over all kernels — NT-Xent/InfoNCE: K̂* = p+/(p p)·C[a1] (C constant on communicating classes); NT-Logistic and spectral: K̂* = p+(a1,a2)/(p(a1)p(a2)) exactly. Footnote 1: Z and A are finite (arbitrarily large).
- Definition 2.1, Eq. 1–2: K+(a1,a2) = p+(a1,a2)/(p(a1)p(a2)) = ⟨φ+(a1), φ+(a2)⟩ with φ+(a)_z = p(a|z)√p(z)/p(a), so the density ratio is a positive-definite (Mercer) kernel.
- App. B.1: every InfoNCE minimizer has the form f*(c,a) = [p(a,c)/(p(a)p(c))]·b(c), attributed to van den Oord et al. (2018), with Poole et al. (2019) cited as a different proof; under irreducibility of the positive-pair chain b is constant.
- App. B.2: the logistic (NT-Logistic, "versions described by Mikolov et al. (2013)") loss with one negative per positive is minimized at f* = log p+/(p p), the log-odds of positive vs. negative pair. App. B.3: the spectral contrastive loss rewrites as Σ(p+/√(p p) − √(p p)·K̂)² − C, minimized at K̂ = K+.
- App. B.4: "the log-probability ratio log p(u,v)/(p(u)p(v)) has an information-theoretic interpretation as the pointwise mutual information … We can thus view the positive-pair kernel K+ as being an exponentiated version of the pointwise mutual information between two views"; cites Moustakides & Basioti (2019) on sample-based probability-ratio estimators as generalizations of the Table 1 losses.
- Theorem 3.2 and Proposition C.1: kernel PCA under K+ gives σ_i² = λ_i and h_i = λ_i^{1/2} f_i for the Markov-chain eigenfunctions f_i; K+(a1,a2) = Σ λ_i f_i(a1) f_i(a2). App. C.3: HaoChen et al.'s symmetrized adjacency matrix M has eigenvectors equal to these eigenfunctions scaled by p(a)^{1/2}, described as "a change of measure" between orthonormality in counting measure and in p(a).

What that strand asks a deeper reading to check:

- This is the paper that states the PMI/density-ratio view and the spectral view of contrastive learning are the same object: one kernel, K+ = exp(PMI), is the minimizer of InfoNCE, logistic and spectral losses and its Mercer eigen-expansion is the spectral embedding. It does not cite Levy & Goldberg ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md)); the word2vec link is only via its reference to Mikolov et al.'s logistic loss.
- It is the explicit bridge to strand (a): the density ratio is a reproducing kernel with an explicit feature map, so the Riesz/RKHS machinery applies to it.
- Check the proofs of Theorem 3.2 and 4.1 and whether the finite-A assumption is essential or only convenient.
