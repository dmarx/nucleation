---
number: 743
status: Read
formerly:
- NOTE-tmph96lt
paper: LIT-254
title: 'Kornblith et al. — Similarity of Neural Network Representations Revisited'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arxiv.org/pdf/1905.00414, v4 of
    2019-07-19, 20 pp., the ICML 2019 camera-ready with appendices), text
    extracted with pdftotext: §§1–7 and Appendices A (proof of Theorem 1),
    B (orthogonalisation), C (CCA, linear regression, PWCCA), D (canonical
    ridge; orthogonal Procrustes), E (architectures) and F (Transformer
    sanity check, SVCCA thresholds, CKA at initialisation, BN and
    within-class CKA, other indexes across architectures). Figure contents
    were read from captions and the text, since the plots have no text
    layer. The skim note filed with the paper is NOTE-223.
- version: 2
  date: '2026-10-14'
  note: >-
    After the readings of LIT-259 (NOTE-tmp8nk93) and LIT-257
    (NOTE-tmpcc47a): the inactive-ok comment for LIT-250, LIT-257 and
    LIT-259, all now Active, removed. The reading is unchanged.
date: '2026-10-14'
summary: >-
  Any similarity index invariant to invertible linear maps is constant
  once a representation's rank reaches the number of examples (Theorem 1,
  a four-line proof). Kornblith et al. argue, without a theorem, for
  invariance to orthogonal maps and isotropic scaling only. They propose
  CKA, normalised HSIC of centred Gram matrices, and show that R²_CCA and
  linear regression are CKA of re-weighted Gram matrices. Linear CKA alone
  finds corresponding layers across CNN initialisations (99.3%, against
  at most 45.4% for the other linear indexes).
---
<!-- inactive-ok-file: THEORY-008 — Proposed; the theories that cite this paper as supporting -->

# NOTE-743: Kornblith et al. — Similarity of Neural Network Representations Revisited

## Contribution

The paper settles which invariances a similarity index for neural
representations should have, and introduces centered kernel alignment
(CKA) from kernel learning as the index that has them. It proves that
invariance to invertible linear transformation makes an index useless
once width reaches the sample size. It places CCA, SVCCA, PWCCA and
linear regression in one family with linear CKA. It supplies an
empirical test, matching corresponding layers across random
initialisations, which only CKA passes for CNNs.

## Key insight

Compare the example-by-example similarity matrices, not the features.
With dot products, ⟨vec(XXᵀ), vec(YYᵀ)⟩ = tr(XXᵀYYᵀ) = ‖YᵀX‖²_F (Eq. 1).
So comparing Gram matrices is the same as summing squared feature
covariances. It is automatically invariant to orthogonal transformations
of either representation, and it keeps the scale of principal
directions, which CCA throws away.

## Assumptions

- **Representations are n × p activation matrices on the same n
  examples, with columns centred.** Without loss of generality p₁ ≤ p₂.
- **Theorem 1 needs full row rank**, rank(X) = rank(Y) = n, which
  requires p ≥ n. It concerns indexes invariant to invertible linear maps
  "in the first argument".
- **The case for orthogonal invariance (§2.2) is an argument, not a
  theorem.** It rests on three points:
  - permutation symmetry of networks;
  - LeCun et al.'s result that orthogonal transformation of the input
    does not change gradient-descent dynamics in the linear case;
  - the observation that, for "rotationally symmetric weight
    distributions, e.g. i.i.d. Gaussian weight initialization", training
    with fixed orthogonal transformations of activations "yields the same
    distribution of training trajectories".
  The case against invertible-linear invariance is empirical: networks
  from different seeds share large principal components (Fig. 1).
- **RBF CKA's isotropic-scale invariance depends on the bandwidth rule.**
  σ is set as a fraction of the median inter-example distance, "which
  ensures that the similarity index is invariant to isotropic scaling"
  (Table 1 footnote).

## Key results

- **Theorem 1 (App. A).** If s(X,Z) = s(XA,Z) for every rank-p A and
  rank(X) = rank(Y) = n, then s(X,Z) = s(Y,Z). The proof stacks X and Y
  with bases of their row null spaces to build A = X′⁻¹Y′ with XA = Y.
- **Proposition 1 (App. B).** An orthogonally invariant index applied to
  orthonormalised columns, s(Q_X, Q_Y), is invariant to invertible linear
  maps, "because orthonormal bases with the same span are related to each
  other by orthonormal transformation".
- **Isotropic scaling (§2.3).** An index invariant to orthogonal maps and
  to non-isotropic scaling is invariant to every invertible linear map,
  by the SVD.
- **HSIC and CKA (Eqs. 3–4).** HSIC(K,L) = tr(KHLH)/(n−1)², with
  H = I − (1/n)11ᵀ. CKA(K,L) = HSIC(K,L)/√(HSIC(K,K)HSIC(L,L)). Linear
  CKA is ‖YᵀX‖²_F/(‖XᵀX‖_F‖YᵀY‖_F). It equals the RV coefficient and
  Tucker's congruence coefficient.
- **The family (Eqs. 11–14).**
  - R²_CCA = CKA(Q_XQ_Xᵀ, Q_YQ_Yᵀ)·√(p₂/p₁).
  - R²_LR = CKA(XXᵀ, Q_YQ_Yᵀ)·√p₁‖XᵀX‖_F/‖X‖²_F.
  - In SVD terms, R²_CCA = Σᵢⱼ⟨u_Xⁱ, u_Yʲ⟩²/p₁, while linear CKA weights
    the same overlaps by λ_Xⁱλ_Yʲ and normalises.
  - So "Linear CKA thus resembles CCA weighted by the eigenvalues".
- **Canonical ridge (App. D.1).** The ridge-regularised CCA statistic,
  suitably normalised, recovers R²_CCA at κ = 0 and R²_LR as κ_X → ∞
  with κ_Y = 0. Normalised by the separable bound (Eq. 27), it is
  CKA(Q̃_XQ̃_Xᵀ, Q̃_YQ̃_Yᵀ), and as κ → ∞ it becomes linear CKA (Eqs. 32–36).
- **Orthogonal Procrustes (App. D.2).**
  min_{QᵀQ=I} ‖Y − XQ‖²_F = ‖Y‖²_F + ‖X‖²_F − 2‖YᵀX‖_*. The Procrustes
  optimum replaces the squared Frobenius norm of YᵀX in Eq. 1 with the
  nuclear norm.
- **Sanity check (§6.1, Table 2).** Ten Tiny-10 CNNs on CIFAR-10 from
  different seeds. Accuracy at identifying the corresponding layer:
  - CKA (Linear) 99.3%; CKA (RBF 0.2/0.4/0.8) 80.6/99.1/99.3%;
  - linear regression 45.4%; linear HSIC 22.2%;
  - CCA, SVCCA and PWCCA 1.4–15.1%.
  On Transformer encoders all indexes pass (App. F.1).
- **Other findings (§§6.2–6.4).**
  - CKA flags pathological depth: in an 8× deep plain net, later layers
    match the last layer, and linear probes plateau (Fig. 3).
  - Added depth inserts layers between old ones (Fig. 5).
  - Wider networks are more similar, and early layers saturate first
    (Fig. 6).
  - Early layers transfer between CIFAR-10 and CIFAR-100 (Fig. 7).
  - The shared subspace at the penultimate layer has dimension about 10,
    the number of classes (Fig. 8).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Indexes invariant to invertible linear maps cannot distinguish representations with rank ≥ n | strong | Theorem 1, App. A |
| C2 | A similarity index should be invariant to orthogonal maps and isotropic scaling, not to all invertible linear maps | moderate | §2 arguments from training dynamics and Fig. 1; no theorem fixes the group |
| C3 | CCA, linear regression and linear CKA are one family, differing in how eigen-directions are weighted | strong | Eqs. 11–14, App. C, App. D.1 |
| C4 | CKA identifies corresponding layers across initialisations and architectures where CCA-family indexes fail | strong | Table 2, Figs. 2, 5, F.8 |
| C5 | Mutual information is not a useful similarity index for deterministic representations | weak | a two-sentence argument in §4 |

## Concepts

- **Similarity index** s(X,Y): a scalar comparing two representations of
  the same examples. It need not be a metric.
- **Representational similarity matrix (RSM).** XXᵀ, or a kernel matrix
  K, after neuroscience usage.
- **CKA.** Normalised HSIC of the two kernel matrices, centred by H.
- **Sanity check.** For architecturally identical networks from
  different seeds, each layer should be most similar to its counterpart.

## Connections

The paper builds on SVCCA (Raghu et al. 2017) and PWCCA (Morcos et al.
2018), and shows both fail its sanity check for CNNs. It borrows HSIC
from Gretton et al. (2005) and CKA from Cristianini et al. and Cortes,
Mohri & Rostamizadeh. It cites representational similarity analysis
(Kriegeskorte et al.) as its neuroscience ancestor. App. D.2 relates CKA
to orthogonal Procrustes alignment (Smith et al. 2017). The Procrustes
optimum's nuclear norm ‖YᵀX‖_* is the quantity that Harvey, Larsen &
Williams ([LIT-250](../literature.d/LIT-250.md)) identify with Bures fidelity of the centred linear
kernels. Kornblith et al. do not make that link.

## Bearing on the record

- **[THEORY-004](../theory.d/THEORY-004.md) cites §2.2 for "the case for orthogonal invariance".**
  That is accurate, with three qualifications.
  - The case is an argument from training dynamics and symmetry, not a
    theorem.
  - The paper argues for orthogonal invariance *plus* isotropic scaling,
    and CKA also removes the mean through H. So the group CKA respects is
    larger than O(p).
  - The paper never states the converse that [THEORY-004](../theory.d/THEORY-004.md) needs, that equal
    Gram matrices imply an orthogonal relation. It says only that
    orthogonal maps "preserve scalar products and Euclidean distances",
    and, in App. B, that orthonormal bases of the same span differ by an
    orthogonal map. The converse is in [LIT-250](../literature.d/LIT-250.md) and [LIT-259](../literature.d/LIT-259.md), where
    [THEORY-004](../theory.d/THEORY-004.md) puts it.
  - App. D.2 (Procrustes ↔ ‖YᵀX‖_*) is a closer supporting passage for
    the Procrustes–Bures half of [THEORY-004](../theory.d/THEORY-004.md) than §2.2 is, and the theory
    could cite it.
- **[THEORY-008](../theory.d/THEORY-008.md) cites the paper as supporting** the claim that CKA, CCA and
  GULP are averages of readout agreement. Kornblith et al. support only
  the unification: R²_CCA, linear regression and linear CKA are one
  family, and canonical ridge interpolates among them (Eqs. 11–14, App.
  D.1). That is the precursor of [LIT-257](../literature.d/LIT-257.md)'s choice-of-G parametrisation.
  They say nothing about readouts, decoding or averaging over tasks, and
  nothing about GULP, which postdates them. The citation holds for the
  family structure only.
- **On the question the LIT left for this reading** (how H interacts
  with the constant offset c_X in the Platonic paper's PMI-kernel
  argument): the paper does not discuss it. But since H1 = 0,
  H(K + c11ᵀ)H = HKH, so any constant added to every kernel entry
  disappears from HSIC and CKA. This is algebra from Eq. 3, not a
  statement of the paper.
- **The RBF bandwidth.** The footnote's scale invariance comes from
  setting σ relative to the median distance. With a fixed σ, RBF CKA is
  not scale-invariant.
- **Practice.** CKA as the default similarity index is a tool
  recommendation for ML analysis and belongs in the anthology. The
  `anthology-candidate` flag stands.

## Limitations

- The choice of invariance group is argued, not derived. Other groups,
  such as permutation only or affine, are not tested as alternatives
  beyond CCA-style invertible-linear invariance.
- All CNN results are on CIFAR-10/100 with small architectures. The
  Transformer test does not separate the indexes.
- The conclusion leaves open whether other kernels or other eigenvalue
  weightings in Eq. 14 would be better.
- CKA's sensitivity to a few large principal components is noted as a
  virtue. Its failure modes are not studied.
- CKA is a similarity index, not a metric. It satisfies no triangle
  inequality, and the paper claims none.

## Open questions

- Is O(p) × scaling the right equivalence for learned representations,
  or should it be a smaller or larger group? Identifiability results for
  the training procedure would decide it.
- Which kernel or eigen-weighting best predicts functional equivalence,
  such as matching downstream readouts? [LIT-257](../literature.d/LIT-257.md) answers part of this.
