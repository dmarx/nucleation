---
number: 753
status: Read
formerly:
- NOTE-tmpx7mtu
paper: LIT-250
title: 'Harvey, Larsen & Williams — Duality of Bures and Shape Distances'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v1 PDF (2311.11436v1, 19 November 2023,
    15 pp.), text extracted with pdftotext: §§1–6 and the proofs in
    App. A.1–A.3, each step checked. Compared line by line, after
    stripping whitespace, with the published version (Proceedings of
    UniReps, PMLR 243:11–26, from proceedings.mlr.press). The two texts are
    the same apart from the venue line, reference numbering and one
    duplicated reference, and the typos noted below are in both. Figures
    were not seen; their content is taken from captions and text.
    Theorem 1 was checked numerically by script (Procrustes and Bures
    distances agree to about 10⁻⁵ on random 200 × 6 data).
- version: 2
  date: '2026-10-14'
  note: >-
    After the reading of LIT-259 (NOTE-829): the inactive-ok comment
    for LIT-259 and LIT-254, both now Active, removed. The reading is
    unchanged.
date: '2026-10-14'
summary: >-
  For centred linear kernels K_X = CXXᵀC, the Bures distance equals the
  Procrustes distance, B(K_X, K_Y) = P(X, Y), and normalized Bures
  similarity equals the cosine of the Riemannian shape distance. Both
  follow from F(K_X, K_Y) = ‖XᵀCY‖_*. By Uhlmann's theorem, the fidelity
  is the largest overlap between representations consistent with the two
  kernels. CKA is only loosely tied to NBS, inside a rank-dependent
  envelope. The result is finite-dimensional and linear; the infinite
  limits are heuristic.
---
<!-- inactive-ok-file: THEORY-002 THEORY-004 THEORY-008 CLAIM-193 — Proposed; the theories and claim this reading bears on, open -->

# NOTE-753: Harvey, Larsen & Williams — Duality of Bures and Shape Distances

## Contribution

The paper shows that two similarity measures proposed independently for
neural representations are the same. The Procrustes shape distance
aligns neurons by an optimal orthogonal map. The Bures distance compares
stimulus-by-stimulus kernel matrices without any alignment. They are
equal, and the normalized Bures similarity (NBS) is the cosine of the
Riemannian shape distance. The paper uses this to extend shape distances
to networks of different widths, to argue about limits of many stimuli
or many neurons, and to set NBS against CKA. The authors present the
result as a self-contained exposition of facts already known in shape
theory, optimal transport and quantum information.

## Key insight

For a linear kernel, the best rotational alignment of two representations
and the fidelity of their kernels are one number. The nuclear norm of the
cross-covariance, ‖ΣXY‖_*, is both the optimum of the orthogonal
Procrustes problem and Tr[(K_X^½ K_Y K_X^½)^½]. So the kernel is a
complete invariant of a representation under orthogonal maps and
translations. A distance between kernels is a distance between those
equivalence classes.

## Assumptions

- **Linear, centred kernels only.** K_X = CXXᵀC with C = I − (1/M)11ᵀ,
  X ∈ ℝ^(M×N_x) holding the responses to M stimuli. Nonlinear kernels are
  never treated.
- **The nuisance group is fixed in advance.** It is translations and all
  orthogonal maps, reflections included, because a permutation of neuron
  labels can require one. The paper does not argue that this is the right
  group for any purpose.
- **Deterministic responses.** The stochastic case is referred to Duong
  et al.
- **Equal widths where stated.** Eqs. 3–4 assume N_x = N_y. Eqs. 7–8
  define the general case, and Lemma 1 shows they agree when widths are
  equal. Eq. 25 and the §4 normalization ρ = P/√(NM) also assume equal N.
- **§4's limits.** The M → ∞ case assumes stimuli are sampled so that
  (1/M)Σ_X → Σ*_X. The N → ∞ case assumes the same for neurons, which
  amounts to treating recorded neurons as samples from a population.
  Neither is stated as a condition.

## Key results

- **Shape distances in covariance form (eqs. 6–8, Lemma 1, App. A.1).**
  With Σ_X = XᵀCX, Σ_Y = YᵀCY and Σ_XY = XᵀCY:
  - θ*(X, Y) = arccos(‖Σ_XY‖_* / √(Tr Σ_X Tr Σ_Y));
  - P(X, Y) = √(Tr Σ_X + Tr Σ_Y − 2‖Σ_XY‖_*).
  The proof is the orthogonal Procrustes solution of Schönemann (1966),
  max_Q Tr[Σ_XY Q] = ‖Σ_XY‖_*.
- **Lemma 2 (App. A.2).** For linear kernels, F(K_X, K_Y) = ‖Σ_XY‖_*,
  where F(A, B) = Tr[(A^½ B A^½)^½] is the fidelity.
  - XᵀYYᵀX, XXᵀYYᵀ and (XXᵀ)^½YYᵀ(XXᵀ)^½ share their nonzero
    eigenvalues.
  - The proof is written for XXᵀ and applies to the centred case with CX
    in place of X.
- **Theorem 1.** B(K_X, K_Y) = P(X, Y) and NBS(K_X, K_Y) = cos θ*(X, Y).
  - B(K_X, K_Y) = √(Tr K_X + Tr K_Y − 2F(K_X, K_Y)) and
    NBS = F / √(Tr K_X Tr K_Y).
  - It follows from Lemma 2 and Tr K_X = Tr Σ_X.
  - Since B and arccos NBS are metrics, the extended shape distances of
    eqs. 7–8 satisfy the triangle inequality even when N_x ≠ N_y.
- **Uhlmann (§5.3, eq. 25).** For N ≥ max(rank K_X, rank K_Y):
  max{|Tr XᵀY| : XXᵀ = K_X, YYᵀ = K_Y} = max_U |Tr[XᵀYU]| = ‖XᵀY‖_* = F(K_X, K_Y).
  - The paper states, without proof, that matrices with the same XXᵀ and
    the same number of columns are related by XU = X′, with U orthogonal.
  - Eq. 26 writes the same maximum over U(M) with the PSD square roots.
- **Trace normalization.** NBS(K_X, K_Y) = F(K_X/Tr K_X, K_Y/Tr K_Y)
  (eq. 22). App. A.3 treats K/Tr K as a "positive semidefinite matrix with
  trace equal to 1" and applies the Fuchs–van de Graaf inequality to it.
- **Bures as transport.** B is the 2-Wasserstein distance between centred
  Gaussians with covariances K_X and K_Y, cited from Peyré and Cuturi.
- **Limits (§4).** b = B/√(NM) and ρ = P/√(NM).
  - As M → ∞, ρ tends to (1/√N)·√(Tr Σ*_X + Tr Σ*_Y − 2‖Σ*_XY‖_*) (eq. 18).
  - As N → ∞, b tends to (1/√M)·√(Tr K*_X + Tr K*_Y − 2F(K*_X, K*_Y))
    (eq. 20).
  - Theorem 1 transfers each limit to the other quantity.
  - The joint limit M, N → ∞ is asserted only, with a citation: "the Bures
    distance between covariance matrices converges to the Bures distance
    between an associated positive semidefinite covariance operator".
- **CKA against NBS (§5).**
  - CKA = 1 − ½‖K_X/‖K_X‖_F − K_Y/‖K_Y‖_F‖²_F (eq. 21), against
    NBS = 1 − ½B²(K_X/Tr K_X, K_Y/Tr K_Y) (eq. 22). They are the
    Euclidean and the Bures geometry on PSD matrices, which induce the
    same topology.
  - The envelope (eq. 24) is
    CKA/√(r(K_X)r(K_Y)) ≤ NBS² ≤ min[r(K_X), r(K_Y)]·CKA, saturated at
    rank 1.
  - Eq. 27 gives NBS(K_X, K_Y) ≥ CKA(K_X^½, K_Y^½), with equality when
    the kernels commute.
  - Eq. 28 bounds 1 − CKA(K_X^½, K_Y^½) above by √(1 − NBS²).
  - Fig. 2 shows two- to three-fold discrepancies on Wishart samples.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Procrustes distance equals Bures distance between centred linear kernels, and NBS is the cosine of the Riemannian shape distance | strong | Thm 1, Lemmas 1–2, App. A.1–A.2 |
| C2 | The shape distances extend to unequal widths and remain metrics | strong | eqs. 7–8 with Thm 1 and the metric property of B |
| C3 | Fidelity is the maximal overlap over representations consistent with the kernels | strong | eq. 25, Uhlmann's theorem |
| C4 | Normalized shape and Bures distances converge as M → ∞ or N → ∞ | moderate | law-of-large-numbers argument, §4; sampling assumptions unstated |
| C5 | They converge as both M, N → ∞, to a Bures distance between covariance operators | weak | asserted with citations to Pigoli et al. and Mallasto & Feragen, §4 |
| C6 | CKA and NBS can differ substantially and are related only inside a rank-dependent envelope | strong | eqs. 24, 27, 28, App. A.3; Fig. 2 |

## Concepts

- **Shape.** After Kendall: what is left of M landmark points after
  translation, rotation and isotropic scaling are ignored. Here
  reflections are ignored too.
- **Procrustes (size-and-shape) distance P.** min_Q ‖CX − CYQ‖_F over
  orthogonal Q. It keeps scale.
- **Riemannian shape distance θ*.** The geodesic angle after centring and
  optimal rotation. It also ignores scale.
- **Fidelity F, Bures distance B, NBS.** Quantities from quantum
  information, applied to PSD kernel matrices. NBS is the fidelity of the
  trace-normalized kernels.
- **Duality.** Used loosely, after Atiyah, for "two different points of
  view of looking at the same object".

## Connections

The paper unifies Williams et al.'s generalized shape metrics with NBS,
which Tang et al. and Muzellec and Cuturi proposed. It notes that similar
results are in Masarotto, Panaretos and Zemel on Procrustes metrics for
covariance operators; that paper is not held here and was not read. It
mentions Shahbazi et al.'s Riemannian covariance distance only in passing.
Kornblith et al.'s CKA ([LIT-254](../literature.d/LIT-254.md)) is the main foil. The paper does not
mention reproducing kernel Hilbert spaces, the GNS construction or the
Platonic hypothesis. "Kernel" here always means the M × M linear Gram
matrix.

Nielsen et al. ([LIT-253](../literature.d/LIT-253.md), [NOTE-738](NOTE-738.md)) define a dissimilarity m_SVD that,
for standardized coordinates, equals this paper's cos θ*. So by Theorem 1
it equals NBS. Their Theorem 4.7 is then a bound on a Bures-type quantity.
That link is this reader's; neither paper states it.

## Bearing on the record

- **[THEORY-004](../theory.d/THEORY-004.md) is supported, with three corrections of detail.**
  - **Its promote_when is half met.** It asks for a close reading of
    Thm 1's proof (App. A.2). That is done. The proof is short and
    correct. The step that matters is that XᵀYYᵀX and
    (XXᵀ)^½YYᵀ(XXᵀ)^½ share their nonzero eigenvalues. The Jorgensen and
    Tian half ([LIT-259](../literature.d/LIT-259.md)) is not touched by this reading.
  - **A misattribution.** [THEORY-004](../theory.d/THEORY-004.md) says "normalized Bures similarity is
    the cosine of the Riemannian shape distance (Lemma 2)". That is
    Theorem 1, eq. 15. Lemma 2 is F(K_X, K_Y) = ‖Σ_XY‖_*.
  - **Translation as well as rotation.** "A representation is determined
    by its kernel up to an orthogonal transformation" is stated in §5.3,
    as a known fact without proof, for matrices with the same number of
    columns. For the centred kernels the paper uses, the representation is
    fixed only up to translation as well, because C removes column means.
    The title should read "up to translation and an orthogonal
    transformation" when the kernel is centred.
  - **A citation that does not match.** "Centred kernels are equal iff
    their Procrustes distance is zero" is cited to §5.3 and §2.2. §2.2
    states it for RDMs. For kernels it follows from Theorem 1 and the
    metric property of B; the paper does not say it in those words.
- **[THEORY-002](../theory.d/THEORY-002.md)** says this paper supplies "the kernel-side metric under
  which kernel closeness is rotation-aligned closeness". That is accurate,
  for linear centred kernels. [THEORY-002](../theory.d/THEORY-002.md)'s promote_when names "a kernel
  distance (Bures or CKA)". This paper shows the two are not
  interchangeable. NBS² and CKA bound each other only within a factor set
  by the kernels' ranks (eq. 24). So a stability result in CKA is not one
  in Bures with a dimension-free constant.
- **The GNS strand.** The seed asked whether §4 turns the finite Gram
  statement into an RKHS or GNS statement. It does not.
  - §4 is a law-of-large-numbers argument for one limit at a time. The
    joint limit is asserted with citations to Pigoli et al. and to Mallasto
    and Feragen.
  - The paper never uses the words RKHS or GNS. The functional-analytic
    reference, Masarotto et al., is cited for "similar ideas" on
    covariance operators.
  - The GNS reading in [THEORY-004](../theory.d/THEORY-004.md) rests on [LIT-259](../literature.d/LIT-259.md), not on this paper.
- **The trace normalization.** The seed's guess holds. NBS is the fidelity
  of K/Tr K (eq. 22), and App. A.3 treats K/Tr K as a unit-trace PSD
  matrix, a density matrix in all but name. The paper does not cite Bach.
- **[CLAIM-193](../claims.d/CLAIM-193.md)** relies on [THEORY-002](../theory.d/THEORY-002.md) and [THEORY-008](../theory.d/THEORY-008.md) for "kernels fix a
  representation only up to the symmetry of what is observed". For linear
  kernels, this paper gives the orthogonal-plus-translation case and no
  more.
- **Anthology.** It carries no instruction for machine-learning practice.
  The authors say whether Euclidean geometry is "good enough" should be
  "considered carefully on a case-by-case basis".

## Limitations

- Everything is for linear kernels. Nothing is said of nonlinear kernels,
  where the kernel fixes a feature map, not the representation.
- The orthogonal group is assumed as the nuisance group, not argued for.
- §4's limits rest on unstated sampling assumptions. The joint limit is
  cited, not proved.
- The CKA comparison is on random Wishart matrices, not on trained
  networks.
- The authors leave open whether other measures have a similar duality.
- **Typos, present in both the arXiv and the PMLR text.**
  - The squared distance between stimuli i and j is printed as
    [K_X]ᵢᵢ + [K_X]ⱼⱼ − [K_X]²ᵢⱼ. It should be − 2[K_X]ᵢⱼ.
  - Eqs. 28, 42 and 43 write NBS(K_X, K_X) for NBS(K_X, K_Y).
  - Eq. 25 writes U(N) for what, with real matrices, is the orthogonal
    group.

## Open questions

- Do other representational measures have a duality between alignment
  and kernel comparison? The authors pose this. If shape and Bures are the
  only such pair, they say, that is a reason to adopt them.
- What is the rigorous joint M, N → ∞ statement? It would be the
  covariance-operator form that the GNS strand wants. Masarotto et al.,
  and Pigoli et al., are where a reader should look.
- What does the duality become for nonlinear kernels? There, the
  fidelity's "consistent representations" are feature maps.
