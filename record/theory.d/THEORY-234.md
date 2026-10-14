---
number: 234
status: Proposed
formerly:
- THEORY-tmpoa03p
promote_when: >-
  A second reader's check of the proofs of Theorem 5 (App. B.6) and
  Theorem 14, and either an independent derivation of the extended linear
  equivalence or a measurement in released language models of the
  subspaces M, N and Γ_q for relations where linearity has been reported,
  showing whether Theorem 14's conditions hold there. The first settles the
  characterization. The second settles whether it bears on trained models,
  which the account claims only under exact equality of distributions. It
  is refuted by two softmax predictors on a shared vocabulary that induce
  the same distribution and are not related as Definition 3 says, or by a
  relational linear property within N, with Γ_q ⊆ M, that holds in one of
  them and fails in the other. What cannot settle it: reports of linear
  structure in single trained models, which say nothing about the
  equivalence class.
title: "Two softmax next-token predictors induce the same distribution exactly when their embeddings and unembeddings are related by an invertible linear map on the subspaces that enter the logits, with arbitrary distortion off them, so a linear relational property is shared by all such models or none only when it lies in those subspaces"
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-950
summary: >-
  Marconato et al. (2024), [LIT-950](../literature.d/LIT-950.md), read in [NOTE-746](../notes.d/NOTE-746.md). For
  p(y|s) ∝ exp(f(s)ᵀg(y)) on a shared vocabulary, p_{f,g} = p_{f̃,g̃} iff
  the models are extended-linearly equivalent: invertible linear maps
  between the subspaces M and N that enter the logits, at any dimensions
  and without the diversity condition (Thm 5). The dimension of M is then a
  property of the distribution. Relational linearity, linear subspaces and
  linear probing hold in all equivalent models or none when Γ ⊆ N and
  Γ_q ⊆ M (Thm 14), and parallelism is shared only within N (Thm 15). Exact
  equality of distributions only, and no experiments.
extends:
- THEORY-018
---
<!-- inactive-ok-file: QUESTION-027 CLAIM-193 CLAIM-209 THEORY-002 THEORY-175 — Open or Proposed; cited for context, nothing here rests on them -->

# THEORY-234: Two softmax next-token predictors induce the same distribution exactly when their embeddings and unembeddings are related by an invertible linear map on the subspaces that enter the logits, with arbitrary distortion off them, so a linear relational property is shared by all such models or none only when it lies in those subspaces

## Source

Marconato et al. (2024), [LIT-950](../literature.d/LIT-950.md), read in [NOTE-746](../notes.d/NOTE-746.md): Lemma 2,
Definition 3, Theorem 5 and its proof (App. B.6), Corollary 6, the
counterexample of App. B.5, Lemma 8, Definition 9, Theorems 14 and 15, and
App. D.1.

## What was actually shown

**The model.** p_{f,g}(x_(t+1) | x_(1:t)) = exp(f(x_(1:t))ᵀg(x_(t+1)))/Z, with
f and g nonparametric and a shared vocabulary. App. A shows a decoder-only
transformer's last state with its unembedding has this form. Write
g₀(y) = g(y) − g(y₀) for a pivot token, F and G for the spans of f and g₀,
M = Im(P_F P_G) and N = ker(P_F P_G)^⊥.

**Only M and N enter the logits (Lemma 2).** f(x)ᵀg₀(y) =
(P_M f(x))ᵀ P_N g₀(y), and dim M = dim N.

**The characterization (Thm 5).** For models of any dimensions d and d̃,
p_{f,g} = p_{f̃,g̃} if and only if (f, g) ∼EL (f̃, g̃): dim M = dim M̃, and
full-rank maps, invertible from M̃ to M and from Ñ to N, carry P_M̃ f̃ to
P_M f and P_Ñ g̃₀ to P_N g₀ (Def. 3). So dim M, the "effective complexity",
is fixed by the distribution (Eq. 13). Under the diversity condition
SIm(f) = SIm(g₀) = ℝᵈ and d = d̃, this reduces to f = M f̃, g₀ = M^(−ᵀ) g̃₀,
the known result (Cor. 6). Without diversity, equivalent models need not
be linearly related at all: App. B.5 adds a non-linear term off N and
leaves the distribution unchanged.

**All or none (Thm 14).** If a model linearly represents a query q on
Γ ⊆ N, meaning P_Γ f(s ⌢ q) = P_Γ A_q f(s) + a_q for every context s, and
Γ_q ⊆ M, then every equivalent model does, on the image of Γ. By
Propositions 11 and 13 the same holds for linear subspaces and relational
linear probing. Without Γ_q ⊆ M the property can hold in one model and
fail in an equivalent one (App. D.1, shown up to proportionality).

**Parallelism (Lemma 8, Thm 15).** Two unembedding differences are
parallel in N if and only if their log-odds are proportional over every
context, a property of the distribution itself. Parallelism in N is
shared across the class. Parallelism in the whole space is not.

What could have failed: the equivalence class could have been larger than
linear maps on M and N even under exact equality, which would have left no
linear property shared. It is not.

## What this does not say

- **Not about trained models directly.** Every result needs exact equality
  of distributions over all sequences. The bridge to trained models (§3.4)
  assumes both reach the global likelihood maximum and represent the data
  distribution exactly, which the authors grant fails, since the softmax
  puts mass on every sequence.
- **Not that trained models meet the conditions.** Whether reported
  relational linearity lies in N with Γ_q ⊆ M is not measured. There are no
  experiments.
- **Not a characterization of all shared properties.** Theorem 14 gives
  sufficient conditions for a family of linear properties.
- **Not an account of the parallelism seen in trained models.** The
  authors argue that the parallelism PCA displays is not explained by
  identifiability, since only parallelism in N is shared, and that training
  biases select within the class. That is an informal argument with no
  measurement (§6).
- **Not across vocabularies or under approximate equality.** Both are left
  open. Nielsen et al. ([LIT-253](../literature.d/LIT-253.md), [THEORY-002](THEORY-002.md)) take up the second.

## Connections

- **Extends [THEORY-018](THEORY-018.md).** That account holds that softmax training fixes
  the final representation only up to an invertible linear map, so no inner
  product on it is intrinsic. This one widens the symmetry: without
  diversity the map is linear only on M and N, and off them the distortion
  is arbitrary, even non-linear. [THEORY-018](THEORY-018.md)'s thesis holds a fortiori.
- **[CLAIM-148](../claims.d/CLAIM-148.md).** A refinement of its gauge for bilinear softmax models: a
  property of one fitted model that depends on components outside M and N
  is not a property of the data.
- **[QUESTION-027](../questions.d/QUESTION-027.md) and [CLAIM-209](../claims.d/CLAIM-209.md).** A proved case of structure identified
  when the full latent model is not, but in the unrestricted, in-probe form
  the question counts as answered. The whole conditional distribution is
  observed, so no decision lies outside the probes.
- **[CLAIM-193](../claims.d/CLAIM-193.md).** A relational linear probe is shared across the class only
  for replies whose differences lie in N. A probe trained on one model can
  read structure an equivalent model need not carry.
- **[THEORY-175](THEORY-175.md).** Where independently trained models agree on structure
  outside N, the agreement comes from training or architecture, not from
  the distribution, so cross-model agreement alone is not evidence that a
  structure is identified.
