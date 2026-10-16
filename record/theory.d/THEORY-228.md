---
number: 228
status: Proposed
formerly:
- THEORY-tmpakup2
promote_when: >-
  Two kinds of result would settle it, and the account claims no more than
  their conjunction. First, a written-out proof that the guarantee holds
  off a finite augmentation space under a stated integrability condition,
  since App. F proves only the existence of an eigenbasis and asserts the
  extension of Theorems 3.8, 4.2 and 4.3. Second, a measurement of α and of
  the conductance ρ on a real augmentation graph, or a faithful proxy, in
  which the bound is non-vacuous. It is refuted by a finite augmentation
  graph satisfying Assumptions 3.6 and 3.7 whose population spectral
  minimizer has linear-probe error above the bound. What cannot settle it:
  linear-probe accuracies of trained networks, which the theorem does not
  address, since it is about the population minimizer.
title: "At the population optimum of the spectral contrastive loss, linear-probe error is bounded by the probability that augmentation changes the label divided by the squared sparsest-partition conductance of the augmentation graph"
version: 1
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
<!-- inactive-ok-file: THEORY-005 THEORY-009 QUESTION-052 — Proposed or Open, or Active and cited for context; this account rests on none of them -->

# THEORY-228: At the population optimum of the spectral contrastive loss, linear-probe error is bounded by the probability that augmentation changes the label divided by the squared sparsest-partition conductance of the augmentation graph

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
