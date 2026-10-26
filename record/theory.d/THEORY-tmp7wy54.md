---
status: Active
title: 'In the author–topic model the likelihood of a corpus depends on the topics Φ and the authors'' topic distributions Θ only through the document–word matrix ΦΘA, A being fixed by the observed authorship, so LDA (each document its own author) and the topic-free author model (each author one topic) are special cases; and the likelihood leaves Φ and Θ unidentified not only up to the permutations of topics the paper names but along a continuum of changes of topic basis whenever every topic gives every word positive probability'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpjg8xz. The factorization and the special
    cases are the paper's Appendix C and §6.1–6.2, and the permutation
    non-identifiability its §3.2. The continuum is the record's, from
    CLAIM-148's NMF gauge. All of it is re-derived below and checked
    numerically, which meets the condition for Active under ADR-047 v2.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
source:
- LIT-tmpnzjy3
summary: >-
  Rosen-Zvi, Chemudugunta, Griffiths, Smyth and Steyvers (2010),
  LIT-tmpnzjy3, read in NOTE-tmpjg8xz. The likelihood sees members' topic
  profiles only through the word distributions they jointly produce, and a
  small change of topic basis that keeps every distribution a distribution
  produces exactly the same corpus probabilities. Only the Dirichlet priors
  then choose among the profiles. It says nothing about the posterior's
  concentration, and nothing about conditions under which Φ and Θ are
  identified up to permutation.
---
<!-- inactive-ok-file: CASE-tmplcm41 CLAIM-135 — Proposed; the case and claim this account bears on, open -->

# THEORY-tmp7wy54: In the author–topic model the likelihood of a corpus depends on the topics Φ and the authors' topic distributions Θ only through the document–word matrix ΦΘA, A being fixed by the observed authorship, so LDA (each document its own author) and the topic-free author model (each author one topic) are special cases; and the likelihood leaves Φ and Θ unidentified not only up to the permutations of topics the paper names but along a continuum of changes of topic basis whenever every topic gives every word positive probability

## Source

Rosen-Zvi, Chemudugunta, Griffiths, Smyth and Steyvers (2010), *ACM TOIS*
28(1), LIT-tmpnzjy3, read in full in NOTE-tmpjg8xz. The factorization is
Appendix C, the special cases §6.1–6.2, and "the posterior probability of
Φ and Θ is unaffected by permuting their columns" §3.2. The continuum, and
the derivations below, are the record's.

## What was actually shown

**The factorization.** Under the generative process of §2, a word of
document d is w with probability Σ_{a∈a_d} (1/A_d) Σ_t φ_wt θ_ta, since the
author is uniform over a_d, the topic is drawn from θ_a, and the word from
φ_t. Let A be the A × D matrix with entries 1/A_d where a ∈ a_d and 0
elsewhere. Then the word distribution of document d is column d of
P = ΦΘA, and words are independent given (Φ, Θ). So the likelihood of the
corpus is Π_d Π_i P_{w_di, d}, a function of P alone.

**The special cases.** If every document has its own single author, A is
the identity (up to ordering) and P = ΦΘ with Θ a T × D matrix of
per-document mixtures, which is LDA. If T = A and Θ is the identity, each
author has one topic of their own and P = ΦA, the author model of §6.2.

**The gauge.** Let R be invertible with every column summing to one
(1ᵀR = 1ᵀ). Then ΦR⁻¹ has columns summing to one, since
1ᵀΦR⁻¹ = 1ᵀR⁻¹ = 1ᵀ, and RΘ has columns summing to one. If both are
nonnegative, (ΦR⁻¹, RΘ) is a valid parameter value and gives the same
P = ΦR⁻¹RΘA. So the likelihood is constant on
{(ΦR⁻¹, RΘ) : 1ᵀR = 1ᵀ, ΦR⁻¹ ≥ 0, RΘ ≥ 0}. Permutation matrices are in
this set, which is §3.2's statement.

The set contains a continuum when every φ_wt > 0. Take
R = (1 − ε)I + (ε/T)J, with J the all-ones matrix. Its columns sum to one
and it is nonnegative, so RΘ ≥ 0. Its inverse is (I − (ε/T)J)/(1 − ε), so
ΦR⁻¹ = (Φ − ε φ̄1ᵀ)/(1 − ε), where φ̄ is the mean of Φ's columns. That is
nonnegative whenever φ_wt ≥ ε φ̄_w for all w and t, which holds for small
enough ε > 0 if Φ is strictly positive. Every posterior mean of Φ is,
since β > 0 in (6). The change mixes each author's topic proportions
toward uniform and sharpens the topics to compensate.

Checked numerically: with W = 8, T = 3, A = 4, D = 5, random Φ
(Dirichlet(5)) and Θ, and ε = 0.05, the transformed Φ and Θ were
column-stochastic and nonnegative, and P changed by at most 6 × 10⁻¹⁷.

What could have failed: a model with observed authorship might have
pinned the topic basis, since the same θ_a must serve every document of
author a. It does not. The authorship matrix A is to the right of Θ, and
the gauge acts between Φ and Θ, where A does not reach.

## What this does not say

- **Not that the posterior is flat.** The Dirichlet priors on Φ and Θ are
  not invariant under R, so the posterior prefers some points of the
  orbit. Which ones is set by α and β, not by the words.
- **Not that the gauge is always a continuum.** If some topic gives a word
  probability zero, as a point estimate might under β = 0, the continuum
  can shrink. Conditions like separability or anchor words, under which
  only permutations remain, are not examined here.
- **Not a claim about the paper's results.** Its perplexities and
  retrievals depend on P, which the gauge leaves alone. Readings of
  individual topics or of an author's profile are what it touches.

## Connections

- **CLAIM-148.** This is that claim's nonnegative-factorization gauge in
  three-factor form with one factor known: the set
  {R : WR ≥ 0, R⁻¹H ≥ 0}, with the column-sum constraint that probability
  matrices add.
- **CLAIM-135.** The AT model reaches the first achievement by perplexity.
  The second needs conditions the paper does not supply. Its §4.2 found
  about 80 of 100 topics aligned across two runs, the empirical face of
  the same gap.
- **CASE-tmplcm41.** The additive latent-feature model of that case has
  the same kind of gauge between its features and their weights, and
  CLAIM-148's note of 2026-10-26 lists it.
- **THEORY-tmplo0xb.** The mixed membership blockmodel has the bilinear
  analogue, between memberships and the block matrix.
