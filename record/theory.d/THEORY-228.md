---
number: 228
status: Active
formerly:
- THEORY-tmpakup2
title: 'On a finite augmentation space, at the population optimum of the spectral contrastive loss with k ≥ 2r, linear-probe error is bounded, up to constant and logarithmic factors, by the error of recovering the label from an augmentation divided by the squared sparsest-partition conductance of the augmentation graph'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-228 (batch 037, ADR-047 v2). Theorem 3.8 was re-derived
    step by step on a finite augmentation space, in the dated note below,
    citing only the higher-order Cheeger inequality. The title now says
    "on a finite augmentation space" and "up to constant and logarithmic
    factors", and it names α as Assumption 3.6 does: the error of
    recovering the label from an augmentation. The promote_when's two
    further results, a proof off a finite space and a measurement showing
    the bound non-vacuous, move to QUESTION-tmpvw33h.
tags:
- representation-learning
- learning-theory
date: '2026-10-14'
source:
- LIT-249
summary: >-
  HaoChen, Wei, Gaidon & Ma (2021), [LIT-249](../literature.d/LIT-249.md), read in [NOTE-740](../notes.d/NOTE-740.md). On a
  finite augmentation space, with labels recoverable from augmentations up
  to error α and k ≥ 2r, every population minimizer of the spectral
  contrastive loss has linear-probe error Õ(α/ρ²_⌊k/2⌋), where ρ is the
  sparsest-partition conductance of the augmentation graph (Thm 3.8). The
  guarantee needs no conditional independence of the views given the
  label. It is a statement about the population optimum of one loss: it
  says nothing about what training reaches, nothing about InfoNCE, and its
  infinite-space extension is asserted, not proved.
answers:
- QUESTION-052
---
<!-- inactive-ok-file: THEORY-005 QUESTION-052 — Proposed or Open, or Active and cited for context; this account rests on none of them -->

# THEORY-228: On a finite augmentation space, at the population optimum of the spectral contrastive loss with k ≥ 2r, linear-probe error is bounded, up to constant and logarithmic factors, by the error of recovering the label from an augmentation divided by the squared sparsest-partition conductance of the augmentation graph

## Source

HaoChen, Wei, Gaidon & Ma (2021), [LIT-249](../literature.d/LIT-249.md), read in [NOTE-740](../notes.d/NOTE-740.md): §3
(Lemmas 3.1–3.2, Assumptions 3.5–3.7, Theorem 3.8, Proposition 3.9,
Theorem 3.11), Theorems B.2–B.3 with Lemmas B.4 and B.6, and App. F.

## What was actually shown

**The graph.** On a finite augmentation space X, the population
augmentation graph has edge weight w_xx′, the probability that a random
positive pair is (x, x′) (eq. 2). Its normalized adjacency is
Ā = D^(−1/2)AD^(−1/2). The sparsest i-partition ρ_i is the smallest
achievable largest Dirichlet conductance over partitions of X into i
sets (Defs. 3.3–3.4).

**The assumptions.** Labels are recoverable from augmentations: some
classifier predicts y(x̄) from x ∼ A(·|x̄) with error at most α
(Assumption 3.6). At least one global minimizer of the loss lies in the
hypothesis class (Assumption 3.7). The probe ensembles its linear
predictions over a point's augmentations.

**The theorem (Thm 3.8).** For k ≥ 2r, with r the number of classes,
every population minimizer f*_pop of the spectral contrastive loss has
linear-probe error E(f*_pop) ≤ Õ(α/ρ²_⌊k/2⌋). With at most m clusters
(Assumption 3.5, ρ_(m+1) ≥ ρ) and k > 2m, the bound is Õ(α/ρ²). The
engine (Thm B.3) bounds the probe error by φ^ŷ/λ_(k+1) + 4Δ(y, ŷ), the
leakage of a labelling across the graph's cut over the (k+1)-th
Laplacian eigenvalue. The higher-order Cheeger inequality of Louis and
Makarychev (Lemma B.4) turns λ_(k+1) into ρ². The step from the loss to
the top eigenvectors is exact: the loss is ‖Ā − FFᵀ‖²_F up to a constant
(Lemma 3.2), and the row scaling and right factor that minimizers carry
are invisible to a linear probe (Lemma 3.1).

**Instances.** For a mixture of m disjointly supported distributions under
small Gaussian augmentation, ρ_(m+1)/σ is bounded below by the components'
Cheeger constants (Prop. 3.9). For a mixture of manifolds the bound becomes
Õ(κ²/(σ²·poly(d))) (Thm 3.11). Theorems 4.1–4.3 carry the guarantee to
finite pretraining samples with polynomial cost, under realizability.

What could have failed: the error of a probe on the top eigenvectors could
have depended on how the graph is cut inside a class, and it does not. Only
the cross-class leakage α and the conductance enter.

## What this does not say

- **Not what a trained network reaches.** The bound is at the population
  minimizer. The paper says it "does not capture the potential implicit
  bias of optimizers" (§7). Its trained models project outputs onto a
  sphere, a constraint the theory lacks.
- **Not about other losses.** Only the spectral contrastive loss is
  analysed. Its resemblance to SimCLR's loss is an algebraic remark.
- **Not off a finite space.** App. F proves an eigenbasis exists under a
  uniform bound on the density ratio (Assumption F.1, stronger than the
  Hilbert–Schmidt property) and asserts the extension of the main theorems
  with the proof omitted.
- **Not a measurement.** α, ρ and the eigengap are not measured on any
  real dataset. The claim that α is "exponentially small" on ImageNet is
  argued.
- **Not the minimax claim.** Johnson et al.'s Theorem 4.1 ([THEORY-007](THEORY-007.md)) is
  a different guarantee, on view-invariant targets in L²(p), and needs
  d ≥ d*.

## Connections

- **[QUESTION-052](../questions.d/QUESTION-052.md).** An answer in part. When admissible transformations are
  a symmetric distribution over pairs on a finite space, the top
  eigenvectors of the pair operator are decision-sufficient for linear
  classification of any labelling that rarely crosses the graph's sparse
  cuts, with error bounded by α/ρ². The labels must be nearly invariant
  under the transformations. That is the condition that makes the top
  eigenspace the right one.
- **[THEORY-007](THEORY-007.md).** Shares the object, the top eigenvectors of the
  normalized augmentation adjacency, and gives a second, cluster-based
  reason why it is a good representation. The two guarantees use different
  assumptions on the target: label recoverability and conductance here,
  bounded view-discrepancy there.
- **[THEORY-005](THEORY-005.md) and [THEORY-009](THEORY-009.md).** The symmetry w(u,v) = w(v,u), which the
  paper uses throughout and never states, is what makes Ā symmetric and the
  undirected Cheeger inequality applicable.
- The paper carries ML practice (a loss to train with and a projection
  head). That part belongs in the anthology and is not filed here.

## Note of 2026-10-19: Theorem 3.8, re-derived

On a finite X, write u_x = √w_x f(x) and let F have rows u_x. Then the
spectral contrastive loss is
−2 Σ w_xx′ f(x)ᵀf(x′) + Σ w_x w_x′ (f(x)ᵀf(x′))² = ‖Ā − FFᵀ‖²_F − ‖Ā‖²_F
(Lemma 3.2). By Eckart–Young, every minimiser has FFᵀ equal to the
positive part of Ā's top-k spectral truncation, so
f*(x) = Rᵀ Λ^(1/2) V_k(x)ᵀ / √w_x, with R orthogonal. A bias-free linear
probe absorbs Λ^(1/2)R, and the positive factor 1/√w_x leaves its argmax
unchanged (Lemma 3.1). So the probe can realise the argmax of any linear
function of the top-k eigenvector rows.

Take ŷ, the classifier of Assumption 3.6, and the leakage
φ = P(ŷ(x) ≠ ŷ(x′)) over positive pairs. For g_c(x) = √w_x 1[ŷ(x) = c],
Σ_c g_cᵀ(I − Ā)g_c = φ. Every eigenvector outside the top k has Laplacian
eigenvalue at least μ_{k+1}, so Σ_c ‖g_c − P_k g_c‖² ≤ φ/μ_{k+1}. The probe
with scores h_c = P_k g_c/√w_x therefore has augmentation-weighted squared
error at most φ/μ_{k+1} against ŷ. The two members of a positive pair are
each an augmentation of the same datum, so φ ≤ 2α. Averaging scores over a
datum's augmentations, a wrong argmax needs a squared error of at least ¼.
By Jensen and Markov, the error against the true label is at most
8(φ/μ_{k+1} + 2α) = O(α/μ_{k+1}). The higher-order Cheeger inequality
(Louis, Raghavendra, Tetali and Vempala; Lee, Oveis Gharan and Trevisan),
the paper's Lemma B.4, gives μ_{k+1} ≳ ρ²_⌊k/2⌋/log k, and so Õ(α/ρ²_⌊k/2⌋).
The derivation holds for any k. The condition k ≥ 2r makes ρ_⌊k/2⌋ the
conductance of partitions at least as fine as the classes, which is what
makes the bound informative. Whether it extends off a finite space, and
whether it is non-vacuous on a real graph, is [QUESTION-tmpvw33h](../questions.d/QUESTION-tmpvw33h.md).
