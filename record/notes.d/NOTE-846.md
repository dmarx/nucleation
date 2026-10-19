---
number: 846
status: Read
formerly:
- NOTE-tmpohlyt
paper: LIT-227
title: 'Tan et al. — contrastive learning is spectral clustering on a similarity graph'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v4 PDF (arxiv.org/pdf/2303.15103, 17 pp.,
    headed "Published as a conference paper at ICLR 2024"), text extracted
    with pdftotext: §1–8, Appendix A (the proofs of Theorems 3.1, 4.2 and
    5.1, line by line), Appendix B (training details, Tables 2–4) and
    Appendix C (the synthetic experiment). Figures 1–3 were seen only
    through their captions. Lemmas 2.3–2.5 are quoted from Van Assel et
    al. (2022) "without proofs"; that paper was not read, so the function
    f_k in Lemma 2.5, which this paper never defines, was reconstructed
    from the proof of Theorem 3.1.
date: '2026-10-14'
summary: >-
  SimCLR's InfoNCE loss, taken over all n objects with a Gaussian kernel on
  the unit sphere and a symmetric augmentation matrix π, is rewritten
  exactly as tr(Zᵀ L(π) Z) + log R(Z): a graph-Laplacian quadratic form
  plus the log of InfoNCE's normalizers. The paper calls this spectral
  clustering under a definition that admits any regularizer. It does not
  show that the minimizer is a set of Laplacian eigenvectors, and it names
  no population optimum.
---
<!-- inactive-ok-file: THEORY-001 THEORY-305 — Proposed; the accounts this reading bears on, and the one filed from it -->
<!-- inactive-ok-file: NOTE-227 — Superseded; the skim of HaoChen et al., named for its wording about this paper -->

# NOTE-846: Tan et al. — contrastive learning is spectral clustering on a similarity graph

## Contribution

The paper rewrites the unmodified InfoNCE loss of SimCLR, over a finite
set of n objects, as a cross-entropy between two Markov random fields on
directed subgraphs, one built from the augmentation matrix π and one from
a kernel Gram matrix of the embeddings. With a Gaussian kernel, that
cross-entropy is a Laplacian quadratic form on π plus a log-partition
term. The paper calls this an equivalence with spectral clustering, and
extends it, in a two-line proof, to CLIP on a bipartite pair graph. It
then argues from a maximum-entropy principle for exponential kernels and
reports small gains from mixtures of Gaussian and Laplacian kernels.

## Key insight

InfoNCE's numerator, averaged over sampled positives, is the Dirichlet
energy Σ π_ij‖Z_i − Z_j‖² of the embedding on the augmentation graph; its
denominators are a repulsion. That is an identity about the loss, true
for every embedding. What it does not supply is the step that makes
classical spectral clustering spectral: an orthonormality constraint whose
solution is the bottom eigenvectors of the Laplacian. The repulsion
log R(Z) is not that constraint, and the paper's Definition 2.7 counts any
regularizer as spectral clustering.

## Assumptions

- **Finitely many objects**, n of them (§3, "the same assumption used by
  HaoChen et al."). Continuous augmentations are to be discretized "in a
  natural way"; no limit is taken.
- **π is row-stochastic and, in §3, symmetric**: π_ij is the probability
  that X_j is sampled as the positive for X_i, and "we assume the sampling
  process is symmetric, i.e., π_ij = π_ji". Self-pairs are excluded
  (W_ii = 0 for every sampled subgraph).
- **Embeddings on the unit sphere**, so that cosine similarity, the inner
  product and −‖Z_i − Z_j‖²/2 differ by constants (Eq. 2).
- **A Gaussian kernel** k(Z_i − Z_j) = exp(−‖Z_i − Z_j‖²/2τ) for the
  equivalence with spectral clustering. The MRF framework itself takes any
  symmetric, translation-invariant k: Z → R₊.
- **All n objects in the denominator.** Theorem 3.1 "requires" the full
  set, not a minibatch (§3.1, Discussion).
- **Exactly one positive per query**: the unitary out-degree filter Ω(W)
  keeps only subgraphs in which every node has one outgoing edge
  (Def. 2.2).
- For CLIP (§4), π_{A,B} is a directed bipartite graph with each node's
  outgoing weights normalized by its out-degree, and objects rather than
  edges are sampled uniformly, which the paper says differs from CLIP's
  implementation.

## Key results

- **Lemma 2.3** (quoted from Van Assel et al.). For W ∼ P(·; π), each row
  W_i ∼ M(1, π_i / Σ_j π_ij), independently across rows.
- **Lemma 2.5** (quoted). min_Z H^k_π(Z) is equivalent to
  min_Z −Σ_(i,j) P_ij log k(Z_i − Z_j) + log R(Z), with P = E[W_X] and
  R(Z) = Σ_W P(Z, W). With the out-degree filter, R(Z) factorizes as
  Π_i Σ_(j≠i) k(Z_i − Z_j), so log R(Z) is the sum of InfoNCE's log
  normalizers. That factorization is my reconstruction; the paper leaves
  f_k undefined.
- **Definition 2.7.** "Spectral clustering" on W is
  min_Z tr(Zᵀ L(W) Z) + E(Z), "where E(Z) is a regularization term", with
  no constraint on E.
- **Theorem 3.1** (proof, App. A). Step 1: by row independence and
  Lemma 2.4, the cross-entropy is −Σ_i Σ_(j≠i) Pr(W_X,ij = 1)
  log Pr(W_Z,ij = 1), and with the Gaussian kernel −log Pr(W_Z,ij = 1) is
  exactly the InfoNCE loss of Eq. (1), with every other object as a
  negative and the positive in the denominator. Step 2: by Lemma 2.5 and
  E[L(W_X)] = L(π), SimCLR is equivalent to
  min_Z tr(Zᵀ L(π) Z) + log R(Z). The factor 1/τ on the trace term is
  dropped in the statement. *Holds when:* n finite, π symmetric, Gaussian
  kernel, all n objects as negatives; the "equivalence" is equality of
  objectives, not a statement about minimizers.
- **Theorem 4.2.** "CLIP is equivalent to running the generalized spectral
  clustering on π_{A,B}." The proof sets K_Z to k on the bipartite blocks
  and zero elsewhere and says "the rest is same as the previous proof".
  "Generalized" because L(π_{A,B}) "is not necessarily the Laplacian of a
  symmetric graph".
- **Theorem 5.1.** The entropy-regularized problem max_α −E(α) on the
  simplex, with E(α) = ψ₁ − Σα_iψ_i + τΣα_i log α_i, has value
  −τ log(exp(ψ₁/τ)/Σ_i exp(ψ_i/τ)). This is the Gibbs variational
  formula; the exponential kernel enters only when ψ_i is set to
  C − ‖f(q) − f(p_i)‖^γ (Eq. 7).
- **Table 1** (ResNet-50, batch 256, linear probe, 500 sampled
  hyperparameter groups per case). At 400 epochs the Simple Sum kernel
  reaches 91.72 / 68.62 / 39.38 on CIFAR-10 / CIFAR-100 / TinyImageNet
  against SimCLR's reproduced 90.60 / 66.29 / 37.83. The single
  Laplacian and γ = 0.5 kernels fall below SimCLR on CIFAR-100 at 400
  epochs (66.09 and 65.81 against 66.29). Table 4 repeats the comparison
  on MoCo with ResNet-18, where the Laplacian kernel is below MoCo on
  CIFAR-100 at 200 epochs. The number of seeds behind the ± values is not
  stated.
- **Appendix C.** InfoNCE on free 2-D vectors for a six-cluster planted
  graph gives embeddings that "exhibit the hallmark pattern of spectral
  clustering". The check is visual.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | InfoNCE over all n objects equals the MRF cross-entropy with one positive per node | strong | Thm 3.1 Step 1, an exact computation |
| C2 | With a Gaussian kernel on the sphere and symmetric π, that loss is tr(Zᵀ L(π) Z) + log R(Z) | strong | Thm 3.1 Step 2, given Lemma 2.5 from Van Assel et al. |
| C3 | Hence contrastive learning "is" spectral clustering on π | weak | true only under Def. 2.7, which admits any regularizer; no minimizer is characterized |
| C4 | CLIP is generalized spectral clustering on the image–text pair graph | weak | a two-sentence proof by analogy, under a sampling scheme CLIP does not use |
| C5 | SimCLR benefits from large batches because Thm 3.1 needs all n objects | weak | asserted in the Discussion, not argued |
| C6 | Exponential kernels are the natural choice for InfoNCE-type losses | weak | Thm 5.1 derives the softmax form for any similarity ψ; the kernel comes from the choice of ψ |
| C7 | Mixtures of Gaussian and Laplacian kernels improve on SimCLR's linear-probe accuracy | moderate | Table 1, three small datasets, 1 to 4 points, gains not uniform across single kernels |

## Concepts

- **Similarity graph π.** The n × n matrix with π_ij the probability that
  X_j is drawn as the positive for X_i. In the record's notation it is
  the transition matrix p⁺(a_j | a_i) of the positive-pair chain.
- **Unitary out-degree filter Ω(W).** The indicator that every node of the
  directed subgraph W has exactly one outgoing edge. It is what matches
  InfoNCE's single positive.
- **Spectral clustering (Def. 2.7).** Any problem min_Z tr(Zᵀ L(W) Z) + E(Z)
  with a regularizer E. This is wider than the field's usage, where the
  constraint ZᵀZ = I or ZᵀDZ = I makes the solution the Laplacian's
  bottom eigenvectors.
- **Repulsion log R(Z).** The log of the MRF partition function of the
  embedding graph, which here is the sum of InfoNCE's log normalizers.
- **Kernel-InfoNCE.** InfoNCE with exp(−‖x − y‖^γ/τ) in place of the
  Gaussian kernel, or a sum or concatenation of two such kernels.

## Connections

The paper sets itself against HaoChen et al. ([LIT-249](../literature.d/LIT-249.md)), whose spectral
result needs the spectral contrastive loss and an extra linear map, and
claims to remove both. It does remove them, but by widening what counts as
spectral clustering rather than by recovering HaoChen et al.'s eigenvector
characterization for InfoNCE. Its machinery is Van Assel et al.'s
probabilistic graph coupling for dimension reduction (2022). It cites
Balestriero and LeCun ([LIT-228](../literature.d/LIT-228.md)), who link a contrastive loss to ISOMAP,
and Hu et al. (2022) on stochastic neighbour embedding, without comparing
characterizations. The reconciliation with [LIT-228](../literature.d/LIT-228.md) that the seed asked
for is not in the paper: Tan et al. read SimCLR's attraction term as a
Laplacian form on π, Balestriero and LeCun read SimCLR as generalized MDS,
and neither paper derives the other's. Johnson et al. ([LIT-258](../literature.d/LIT-258.md)) is later
work and is not cited.

## Bearing on the record

- **[THEORY-001](../theory.d/THEORY-001.md) cites this paper in its Source for something the paper
  does not say.** [THEORY-001](../theory.d/THEORY-001.md) is about a shared population optimum, the
  density ratio K⁺. Tan et al. name no optimum, never mention a density
  ratio, PMI or mutual information, and do not characterize a minimizer
  of any loss. The citation should be removed from Source. If it is kept,
  it belongs under Connections, for the different statement that
  InfoNCE's objective, at every embedding, is a Laplacian form on π plus
  log normalizers.
- **[NOTE-740](NOTE-740.md) (Connections) says that Tan et al. "restate the
  correspondence for InfoNCE-type losses"**, meaning HaoChen et al.'s
  identification of the representation with top eigenvectors. They do
  not. Their theorem is an identity between objectives, and its
  regularizer is not an orthonormality constraint, so no eigenvector
  statement follows. [NOTE-227](NOTE-227.md)'s "build on or restate" is right only
  in the first sense.
- **[THEORY-007](../theory.d/THEORY-007.md) and [THEORY-009](../theory.d/THEORY-009.md)** do not cite the paper. Its CLIP
  theorem is a case of a non-symmetric pair structure, the case
  [THEORY-009](../theory.d/THEORY-009.md) leaves open. It does not meet [THEORY-009](../theory.d/THEORY-009.md)'s promote_when: the
  "generalized spectral clustering" is the same objective identity on an
  asymmetric graph, with no eigen- or singular-function analysis.
- **Filed from this reading:** [THEORY-305](../theory.d/THEORY-305.md), which holds the identity
  at the strength it is shown and says what it does not establish.
- Kernel-InfoNCE (§5.2, §6) is an instruction for machine-learning
  practice. It belongs in the anthology and is not filed here.

## Limitations

- No statement about minimizers. The paper never shows that the solution
  of tr(Zᵀ L(π) Z) + log R(Z) is, or spans, any set of eigenvectors of
  L(π).
- Finite n with all objects as negatives. The batch-size reading is a
  remark, and the minibatch loss SimCLR actually trains (Algorithm 2,
  2N in-batch views) is not analysed.
- The temperature is dropped from the trace term in the statement of
  Theorem 3.1, although it sets the balance between attraction and
  repulsion.
- The CLIP proof is two sentences long and uses a sampling scheme that
  CLIP does not use.
- The kernel experiments are on CIFAR-10/100 and TinyImageNet only, with
  heavy per-method hyperparameter search and unstated seed counts.
- The lemmas it rests on are quoted without proof.

## Open questions

- Is the minimizer of tr(Zᵀ L(π) Z) + log R(Z) on the sphere related to
  the bottom Laplacian eigenvectors of π, for instance in a
  low-temperature limit? A derivation either way would settle what
  "spectral clustering" can mean here.
- How does this objective identity relate to the population optimum of
  InfoNCE in [THEORY-001](../theory.d/THEORY-001.md), where the critic is the log of K⁺? Exp and
  log do not commute with low-rank truncation, which suggests that the
  eigenvectors of L(π) are not what InfoNCE's d-dimensional embedding
  recovers.
