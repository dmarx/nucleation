---
number: 833
status: Read
formerly:
- NOTE-tmpc8ts7
paper: LIT-235
title: 'Sun, Shi, Liang & Li — when known classes help discover novel ones'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2308.05017v1, 9 August 2023, PMLR
    202 header), text extracted with pdftotext in raw and layout modes:
    §§1–7, Tables 1–2, appendix A (Lemma 5.1 and Theorem 4.1), appendix
    C.1–C.4 (Theorems C.1 and C.4, Lemma C.2, the proof of Theorem 5.6
    and Lemma C.6). Followed only at the level of their statements:
    appendix B (the eigenvector computations behind Theorems 5.2–5.3 and
    Lemma 5.4), appendix C.5 (the lower bound on κ, Lemma C.10) and
    appendix D (experimental details). The PMLR version itself was not
    read.
date: '2026-10-14'
summary: >-
  In a spectral-contrastive augmentation graph over labelled and
  unlabelled data, the linear-probe residual of a novel labelling is
  exactly the part of it outside the top-k eigenspace that the labelled
  rows of the discarded eigenvectors cannot absorb. Known classes that
  share the novel class's attribute can make it zero, and a toy shows
  that known classes sharing a rival attribute make it worse. The
  general error bound (Theorem 5.6) is approximate and averages all
  known classes into one block.
---
<!-- inactive-ok-file: NOTE-227 — Superseded; the skim of HaoChen et al. that first listed this paper -->
<!-- inactive-ok-file: THEORY-228 THEORY-005 THEORY-320 — Proposed; the bound this paper's framework comes from, an operator account it does not restate, and the account filed from this reading -->

# NOTE-833: Sun, Shi, Liang & Li — when known classes help discover novel ones

## Contribution

It carries HaoChen et al.'s spectral contrastive framework over to novel
class discovery. The vertices are augmented views of both the labelled
and the unlabelled data. Same-class labelled pairs count as positive
pairs alongside augmentation pairs. The paper derives a matching loss
(NSCL). It then writes the novel-class linear-probe residual in terms of
the graph's eigenvectors. This makes precise how adding labelled data
changes which partition of the unlabelled data the learned features
express. A toy example shows that this can help or hurt.

## Key insight

Labelled data does not add information about the novel classes
directly. It changes the graph, and so changes which eigenvectors rank
in the top k. In the toy, unlabelled objects vary in colour and shape,
and shape is the stronger link. Known red objects lift the colour
eigenvector into the top k. Known objects of a shared shape push it
further down. Which kind is discovered is a function of what is already
known.

## Assumptions

- **Population graph.** Edge weight w_xx′ = α Σ_{i∈Y_l} E T(x|x̄_l)T(x′|x̄′_l)
  over same-class labelled pairs, plus β E T(x|x̄_u)T(x′|x̄_u) over views
  of one unlabelled image (Eq. 1). The normalized adjacency is
  Ȧ = D^{−1/2}AD^{−1/2}. Labelled and unlabelled data are linked only
  through augmented views they share.
- **Exact optimum.** The analysis assumes the optimizer reaches the
  rank-k minimizer of ‖Ȧ − FFᵀ‖²_F (Eckart–Young). It works with
  the top-k singular vectors V* split into labelled rows L* and
  unlabelled rows U*.
- **Novel classes do not overlap known ones.**
- **Toy (§5.2).** One sample per kind. τ₁ = 1, τ₀ = 0, and
  τ₁ ≫ max(τ_s, τ_c) ≫ τ₀, with τ_s, τ_c the augmentation probabilities
  between same-shape and same-colour objects. The unnormalized adjacency
  is used "for simplicity".
- **Theorem 5.6 adds three things.** All labelled rows of Ȧ are replaced
  by their average (Ā = PȦPᵀ, Eq. 25), which pools all known classes into
  one block. Lemma C.2 assumes A_uu is PSD. Lemma C.6 requires
  ‖Ȧ − Ā‖₂ < ½(σ_k − σ_{k+1}) and balanced novel classes.

## Key results

- **Theorem 4.1 (appendix A.2).** Minimizing ‖Ȧ − FFᵀ‖²_F with
  f_x = √w_x f(x) equals minimizing
  L_nscl = −2αL₁ − 2βL₂ + α²L₃ + 2αβL₄ + β²L₅. L₁ and L₂ reward
  same-class labelled pairs and same-image unlabelled pairs; L₃–L₅
  penalize squared similarity of labelled–labelled, labelled–unlabelled
  and unlabelled–unlabelled negatives. *Holds when:* exactly, on the
  population graph, following HaoChen et al.
- **Lemma 5.1.** E(f) ≤ 2R(U*), where E is the 0–1 linear-probe error on
  unlabelled data and R(U*) = min_M ‖Y − U*M‖²_F the least-squares
  residual.
- **Theorem 5.2 (toy).** With τ_s < 1.5τ_c: if the known class is a red
  cylinder, R(U₁*, y) = 0 for the label "red". If it is a gray cylinder,
  R(U₂*, y) = 0 when τ_s < τ_c and 1 when τ_s > τ_c.
- **Theorem 5.3.** For a link of strength t between the known class and
  the red novel objects, with 1.5τ_c > τ_s > τ_c, the residual is 1 at
  t = 0, some r(t) ∈ (0, 1) below a threshold t̄ = √(2(τ_s − τ_c)²τ_c/(2τ_c − τ_s)),
  and 0 above it.
- **Lemma 5.4 (harm).** With a gray cube as the known class and
  τ_s/τ_c ∈ (1, 1.5), R(U₃*, y) − R(U₂*, y) = 1. A known class that shares
  the rival attribute (shape) makes the target labelling harder to
  recover than having no informative known class.
- **Theorem 5.5 / C.1.** R(U*, y) ≤ ‖(I − P_{L♭})U♭ᵀy‖²₂, with
  P_{L♭} = L♭ᵀ(L♭L♭ᵀ)†L♭. The proof in C.1 ends in an equality: letting
  the labelled entries of the target float freely, R(U*, y) =
  min_ζ ‖L♭ᵀζ + U♭ᵀy‖² = ‖(I − P_{L♭})U♭ᵀy‖². R = 0 if and only if
  some ω ∈ ℝ^{N_l} has u_iᵀy = l_iᵀω for every discarded index i > k.
  Through u_i = (σ_iI − A_uu)†A_ul l_i this becomes condition (23).
  *Holds when:* exact, for the population graph and its exact rank-k
  factorization.
- **Theorem C.4 (block-averaged graph).** On Ā,
  R(Ū*, y) = (1 − κ(y)²)‖Ū♭ᵀy‖² with κ(y) = cos(Ū♭ᵀy, l̄♭). Once the
  labelled block is averaged, the labelled data supplies a single
  direction l̄♭. Coverage κ is the cosine between that direction and
  the "ignorance" vector Ū♭ᵀy.
- **Theorem 5.6.** E(f) ≲ (2N_u/|Y_u|) Σ_i T(y_i)(1 − κ(y_i)²) +
  ‖Ȧ − Ā‖₂/(σ_k − σ_{k+1}), with κ bounded below through A_uu's
  eigenvectors q_i and the mean labelled–unlabelled link η_u.
  *Holds when:* the assumptions of Lemmas C.6, C.9 and C.10, up to
  unstated constants (≲).
- **Experiments (§6).** ResNet-18 on CIFAR. Novel-class clustering
  accuracy is 97.5 / 85.9 / 64.0 on C10-5 / C100-80 / C100-50 (Table 1,
  transductive). The best baseline on C100-50 is ComEx at 53.4. The
  "10.6%" is that difference in points. SCL on unlabelled data alone
  gets 51.8 on C100-50, and SCL on both sets without labels 53.3.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The NCD matrix-factorization objective equals a contrastive loss with labelled same-class positives | strong | Theorem 4.1, appendix A.2 |
| C2 | The novel-class residual equals the part of the target outside the top-k eigenspace not absorbed by the labelled rows of the remaining eigenvectors | strong | Theorem 5.5 and its proof in C.1 (an equality, stated as ≤) |
| C3 | Known classes can drive the residual to zero when they share the attribute that defines the novel class | strong (toy) | Theorems 5.2–5.3, appendix B |
| C4 | Known classes that share a rival attribute can make the residual worse than no informative known class | strong (toy) | Lemma 5.4 |
| C5 | Linear-probe error is bounded by the novel labels' ignorance degree times one minus squared coverage, plus an approximation term | weak | Theorem 5.6: ≲, block-averaged labelled data, notational slips |
| C6 | NSCL beats existing NCD methods on CIFAR splits | moderate | Tables 1–2, one architecture, no variance reported |

## Concepts

- **Ignorance space.** U♭ᵀy: the coordinates of the novel labelling on
  the eigenvectors left out of the top k. **Ignorance degree**
  T(y) = ‖U♭ᵀy‖₂/‖y‖₂.
- **Extra knowledge.** L♭: the labelled rows of those left-out
  eigenvectors.
- **Coverage.** κ(y) = cos(Ū♭ᵀy, l̄♭), defined only on the block-averaged
  graph Ā.
- **Novel class discovery.** Clustering an unlabelled set of novel
  classes, with a labelled set of disjoint known classes as help.

## Connections

The framework is HaoChen et al. (2021)'s spectral contrastive loss (the
source of [THEORY-228](../theory.d/THEORY-228.md)), with the graph extended to include labelled
same-class pairs. It cites Shen et al. (2022) and HaoChen et al. (2022)
for the spectral treatment of domain adaptation. The block averaging
behind Theorem 5.6 is motivated by the stochastic block model.

## Bearing on the record

- **[THEORY-228](../theory.d/THEORY-228.md) (HaoChen's bound).** This paper uses that bound's
  framework and does not test or extend the bound. Its analysis is
  instead of the exact residual in terms of the discarded eigenvectors,
  which is a sharper and different object from [THEORY-228](../theory.d/THEORY-228.md)'s
  conductance bound. No conflict.
- **[QUESTION-052](../questions.d/QUESTION-052.md)** asks whether a kind's stable, decision-sufficient
  signature is the top eigenspace of its pair operator. This paper bears
  on the "stable" part. Change the other kinds present in the graph and
  you change which partition reaches the top eigenspace. The order of
  attributes in the spectrum is relative to what else the operator
  connects. Lemma 5.4 makes this concrete: a known class sharing shape
  demotes colour. The signature is a function of the whole graph, not of
  the kind alone. Filed as [THEORY-320](../theory.d/THEORY-320.md).
- **[CLAIM-152](../claims.d/CLAIM-152.md)** (individuation by sufficiency is relative to the target).
  Theorem 5.2 vs Lemma 5.4 is a formal instance. The same unlabelled
  data is partitioned by colour or by shape depending on the auxiliary
  labelled data. Supports it.
- **[LIT-249](../literature.d/LIT-249.md) and the superseded skim [NOTE-227](NOTE-227.md)** list this paper among
  works that "build on or restate" the eigenfunction reading of SSL.
  That is right: it restates HaoChen's equivalence with a modified
  graph. It does not restate the operator form of [THEORY-005](../theory.d/THEORY-005.md) or
  [THEORY-007](../theory.d/THEORY-007.md).
- **Anthology.** NSCL as a method for NCD is ML practice. The flag
  `anthology-candidate` is right for that part. The residual analysis is
  learning theory of the kind this record already holds.

## Limitations

- **Exact optimum on a population graph.** No finite-sample or
  optimization analysis. The graph is never built for real data, so
  T(y) and κ(y) are analytical quantities. The paper does not estimate
  them on CIFAR. The seed's question, whether the bound can be estimated
  in practice, gets the answer no.
- **Theorem 5.6 pools the known classes.** Ā replaces every labelled row
  by the mean over all labelled samples, regardless of class. So in the
  main bound the labelled data acts as one undifferentiated block with
  one direction l̄♭. All class structure among known classes goes into
  the error term ‖Ȧ − Ā‖₂/(σ_k − σ_{k+1}), which is not evaluated.
- **Notational slips in Theorem 5.6.** Lemma C.6 redefines |Y_u|, the
  number of novel classes, as E_{i∈I}(1 − ‖ū_i‖²). Theorem C.4 has
  T(y)² where Theorem 5.6 has T(y). The ≲ hides constants.
- **Theorem 5.5 is stated as an inequality** although its proof gives
  equality. This understates the result.
- **The toy has one sample per kind** and specific τ orderings. Theorems
  5.2–5.3 and Lemma 5.4 are exact there and illustrative beyond it.
- **Experiments.** One architecture (ResNet-18), CIFAR only, no error
  bars. The ablations (SCL, SCL‡) show that labels help, not that the
  theory's mechanism is why.

## Open questions

- Can T(y) and κ(y) be estimated from a trained network's features, so
  that Theorem 5.6's prediction (which known classes help) is tested
  rather than illustrated? Computing them on a finite augmentation graph
  for CIFAR, and correlating with per-split discovery accuracy, would
  close it.
- What replaces coverage when known classes are kept separate rather
  than averaged? Theorem C.1's condition (23) holds per discarded
  eigenvector, and it has no scalar summary yet.
