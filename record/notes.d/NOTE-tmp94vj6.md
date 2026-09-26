---
status: Skimmed
paper: LIT-tmpmford
title: 'Similarity of NN Representations Revisited (CKA)'
version: 1
date: '2026-09-26'
summary: >-
  A similarity index for neural representations should be invariant to orthogonal transformation and isotropic scaling but not to arbitrary invertible linear maps, and comparing the example-by-example Gram matrices (linear or kernel CKA) achieves exactly that, while any index invariant to invertible linear maps becomes uninformative once width reaches the number of examples.
---
<!-- inactive-ok-file: LIT-tmpmford — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmp94vj6: Similarity of NN Representations Revisited (CKA)

## Contribution

The paper examines ways of comparing the representations of different layers and networks, starting from CCA-based methods. It shows that CCA is one of a family of multivariate similarity statistics, and proves that no statistic invariant to invertible linear transformation can meaningfully compare representations whose dimension exceeds the number of data points. It proposes centered kernel alignment (CKA), a normalised Hilbert–Schmidt independence criterion on example-by-example kernel matrices, and shows it identifies correspondences between layers of networks trained from different initializations where CCA-style methods fail.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.1, Theorem 1 (proof in App. A): if s(X,Z) = s(XA,Z) for every full-rank A and rank(X) = rank(Y) = n (number of examples), then s(X,Z) = s(Y,Z). Invariance to invertible linear maps makes the index constant once width ≥ n.
- §2.2: the proposed invariance is s(X,Y) = s(XU,YV) for orthonormal U,V. The stated reasons: orthogonal maps preserve scalar products and Euclidean distances between examples, include permutations of units, and leave gradient-descent dynamics unchanged for rotationally symmetric initialization. §2.3 adds isotropic scaling.
- §3, eq. (1): ⟨vec(XXᵀ), vec(YYᵀ)⟩ = tr(XXᵀYYᵀ) = ‖YᵀX‖²_F. Comparing inter-example similarity (Gram) matrices is the same as comparing features pairwise. Eqs. (3)–(4) define HSIC = tr(KHLH)/(n−1)² and CKA = HSIC(K,L)/√(HSIC(K,K)·HSIC(L,L)), for linear or RBF kernels.
- §6.1: a sanity check (the corresponding layer of a re-initialised network should be the most similar) is passed by CKA and mostly failed by CCA variants. §6.4 and Fig. 8 find that the subspace shared by two networks is spanned mainly by the top eigenvectors of the Gram matrix XXᵀ.

## Open questions

- It is the reference the Platonic hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)) cites for comparing representations by their kernels. It is also where "invariant to orthogonal transformation" is argued to be the right equivalence for representations, which is the finite-sample shadow of "determined up to unitary equivalence".
- A deeper reading should check how the centering matrix H interacts with the constant offset c_X in the Platonic paper's PMI-kernel argument (K + c11ᵀ has the same centred form), and how RBF-CKA's bandwidth choice breaks scale invariance (Table 1 footnote).
- The invariance arguments in §2.2 are heuristic, about training dynamics rather than a theorem that O(p) is the right group. Later work (the identifiability literature) argues for other groups.
