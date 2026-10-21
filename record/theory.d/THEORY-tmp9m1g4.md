---
status: Active
title: 'When every log-likelihood a predictive family V can assign lies in [−B, B], the V-information estimated from N samples is within 4R_N(G_V) + 2B√(2 log(1/δ)/N) of the true V-information with probability at least 1 − 2δ, with R_N(G_V) the Rademacher complexity of the family''s log-likelihoods; so usable information relative to a family of small complexity can be estimated in high dimension, and what is estimated is that family''s information, not Shannon''s'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmpvnsxo. The bound is Xu et al.'s Theorem 1,
    with Lemmas 3–4. Its proof was checked step by step below: it is a
    standard McDiarmid and symmetrization argument, and the one step the
    paper leaves implicit, that the infimum's estimate is two-sided, is
    supplied. That meets the condition for Active under ADR-047 v2.
    Corollary 1.1's constants were read, not re-derived.
tags:
- learning-theory
- information-theory
date: '2026-10-21'
source:
- LIT-tmp07k7g
summary: >-
  Xu, Zhao, Song, Stewart and Ermon (2020), [LIT-tmp07k7g](../literature.d/LIT-tmp07k7g.md), read in
  [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md), Theorem 1. Restricting the predictor class trades the
  data-processing inequality for estimability. The bound needs bounded
  log-likelihoods and says nothing about Shannon information, which a
  restricted family may under- or over-state ([THEORY-tmpgz4cf](THEORY-tmpgz4cf.md)).
---

# THEORY-tmp9m1g4: When every log-likelihood a predictive family V can assign lies in [−B, B], the V-information estimated from N samples is within 4R_N(G_V) + 2B√(2 log(1/δ)/N) of the true V-information with probability at least 1 − 2δ, with R_N(G_V) the Rademacher complexity of the family's log-likelihoods; so usable information relative to a family of small complexity can be estimated in high dimension, and what is estimated is that family's information, not Shannon's

## Source

Xu, Zhao, Song, Stewart and Ermon (2020), ICLR 2020, [LIT-tmp07k7g](../literature.d/LIT-tmp07k7g.md), read in
full in [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md): Theorem 1 (§4), proved in Appendix A.3 with Lemmas
3 and 4, and Corollary 1.1 for bounded linear-Gaussian families. The
check below is the record's.

## What was actually shown

Let D be N samples of (X, Y), and let Î_V(X → Y; D) be V-information under
the empirical distribution: the least empirical log loss without X minus
the least with X. Let G_V = {(x, y) ↦ log f[x](y) : f ∈ V} and
|log f[x](y)| ≤ B throughout.

**Each V-entropy.** Let Φ(D) = sup_{f∈V} |E[−log f[X](Y)] − Ê_D[−log
f[X](Y)]|. Changing one sample moves Φ by at most 2B/N, so McDiarmid
gives Φ ≤ EΦ + B√(2 log(1/δ)/N) with probability 1 − δ. Symmetrization
gives EΦ ≤ 2R_N(G_V). Let f̂ minimize the empirical loss and f̃ the true
one. Then

E(f̃) − Ê(f̃) ≤ H_V(Y | X) − Ê(f̂) ≤ E(f̂) − Ê(f̂),

because Ê(f̂) ≤ Ê(f̃) and H_V(Y | X) = E(f̃) ≤ E(f̂). Both ends are at
most Φ in absolute value, so |H_V(Y | X) − Ê(f̂)| ≤ 2R_N(G_V) +
B√(2 log(1/δ)/N). This is Lemma 3, whose statement gives the looser 2B.
Lemma 4 is the same for H_V(Y). Optional ignorance maps V into its
constant members, so the input-free class's complexity is at most
R_N(G_V).

**The difference.** The triangle inequality and a union bound over the two
entropies give the theorem with probability 1 − 2δ. Rademacher complexity
is typically O(N^(−1/2)), so the error falls as N^(−1/2) at a rate set by
V, not by the dimension of X.

What could have failed: a V-entropy is an infimum, and an estimated
infimum can be biased in one direction only. The sandwich above shows the
error is controlled in both directions by the one uniform deviation Φ.

## What this does not say

- **Not an estimate of Shannon information.** The quantity estimated is
  I_V. When V is small enough to estimate well, I_V can sit far below
  I(X; Y) (the XOR case, [THEORY-tmpgz4cf](THEORY-tmpgz4cf.md)) or, if V cannot predict the
  marginal of Y, above it.
- **Not unbounded likelihoods.** Gaussian families on unbounded data
  violate |log f| ≤ B. Corollary 1.1 needs bounded inputs, outputs and
  weights.
- **Not that the empirical minimizer is found.** The bound is for the
  exact empirical infimum. Gradient descent on a neural family gives an
  upper bound on the empirical V-entropy, and the theorem does not cover
  the gap.
- **Not a guarantee on structure.** Theorem 2 carries the bound to the
  total weight of a directed Chow–Liu tree, not to its edges.

## Connections

- **[QUESTION-111](../questions.d/QUESTION-111.md)** asks which distinctions a bounded interpreter can
  recover. For a stated family, this says the answer can be measured from
  samples, with an error bar.
- **[NOTE-820](../notes.d/NOTE-820.md) and [THEORY-281](THEORY-281.md).** Leakage estimated by V-information is
  leakage to that family. Xu et al.'s §6.4 shows features that hide an
  attribute from one family of discriminators leaking it to another.
