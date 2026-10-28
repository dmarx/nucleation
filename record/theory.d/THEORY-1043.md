---
number: 1043
status: Active
formerly:
- THEORY-tmpo1cju
title: 'The finite feature model in which each of K features has prevalence Beta(α/K, 1) has, as K grows, a limit on equivalence classes of binary matrices that ignore the order of columns, and the Indian buffet process, in which the i-th object takes each earlier feature with probability m/i and Poisson(α/i) new ones, produces the same distribution, so its objects are exchangeable and the number of features they hold is Poisson(αH_N)'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-1208. It is the paper's result, eqs. (2)–(5)
    of Griffiths and Ghahramani (2005), whose details the paper defers to
    a technical report. It was checked numerically at N = 3, α = 1.5: the
    finite model's probability of each lof-class at K = 100,000, eq. (3),
    equals the limit (4) to four decimals for the six commonest classes,
    400,000 runs of the buffet give the same frequencies to within 0.0005,
    and the mean K+ is 2.751 against αH_3 = 2.750 (record script,
    2026-10-27).
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-1623
- LIT-1556
summary: >-
  Griffiths and Ghahramani (2005), [LIT-1623](../literature.d/LIT-1623.md), read in [NOTE-1208](../notes.d/NOTE-1208.md), and
  their review ([LIT-1556](../literature.d/LIT-1556.md)). P([Z]) → α^{K+}/∏_{h≥1} K_h! · exp{−αH_N} ·
  ∏_k (N − m_k)!(m_k − 1)!/N! on lof-classes, and the buffet gives the
  same. It is a statement about the limit: at finite K the expected count
  of occupied features is below αH_N ([THEORY-999](THEORY-999.md)), and an ordered
  truncation of the same limit is a different approximation
  ([THEORY-1041](THEORY-1041.md)).
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this bears on, cited as open -->

# THEORY-1043: The finite feature model in which each of K features has prevalence Beta(α/K, 1) has, as K grows, a limit on equivalence classes of binary matrices that ignore the order of columns, and the Indian buffet process, in which the i-th object takes each earlier feature with probability m/i and Poisson(α/i) new ones, produces the same distribution, so its objects are exchangeable and the number of features they hold is Poisson(αH_N)

## Source

Griffiths and Ghahramani (2005), *Infinite latent feature models and the
Indian buffet process*, [LIT-1623](../literature.d/LIT-1623.md), read in full in [NOTE-1208](../notes.d/NOTE-1208.md):
§2.1 (the finite model, (1)–(2)), §2.2 (lof-classes), §2.3 (the limit,
(3)–(4)) and §2.4 (the buffet, (5)). The derivation is given at length in
the authors' review, [LIT-1556](../literature.d/LIT-1556.md) (§§3–4, Appendix A; [NOTE-1172](../notes.d/NOTE-1172.md)).

## What was actually shown

**The finite model.** With z_ik | π_k ~ Bernoulli(π_k) and π_k ~
Beta(α/K, 1), P(Z) = ∏_k (α/K)Γ(m_k + α/K)Γ(N − m_k + 1)/Γ(N + 1 + α/K),
and the probability of a lof-class multiplies it by K!/∏_h K_h!.

**The limit.** As K → ∞,
P([Z]) → α^{K+}/∏_{h=1}^{2^N − 1} K_h! · exp{−αH_N} · ∏_{k=1}^{K+}
(N − m_k)!(m_k − 1)!/N!.
It depends only on the K_h and m_k, so it is infinitely exchangeable in
the objects.

**The buffet.** The first object takes Poisson(α) features; the i-th takes
each earlier feature with probability m_k/i, then Poisson(α/i) new ones.
Its matrices map to lof-classes with the probabilities of the limit. The
new features over N objects number Poisson(Σ_i α/i) = Poisson(αH_N), and
each object holds Poisson(α).

**The check.** At N = 3 and α = 1.5, for the six commonest lof-classes,
the finite model at K = 100,000, the limit and 400,000 buffet runs give:
the empty matrix 0.0639, 0.0639 and 0.0634; one feature held by the first
object only 0.0320, 0.0320 and 0.0325; one held by all three 0.0320,
0.0320 and 0.0322; one held by the second only 0.0320, 0.0320 and 0.0321;
one held by the third only 0.0320, 0.0320 and 0.0318; one held by all and
one by the first only 0.0160, 0.0160 and 0.0162. The simulated mean of K+
is 2.751; αH_3 = 2.750 (record script, 2026-10-27).

## What this does not say

- **Nothing about finite K.** The count αH_N is the limit's. The finite
  model expects K(1 − (α/K)B(α/K, N + 1)) occupied features, strictly
  fewer ([THEORY-999](THEORY-999.md)).
- **Nothing about a posterior.** The result is about the prior; the
  paper's sampler, and the review's footnote that its posterior version is
  heuristic, are separate matters ([NOTE-1172](../notes.d/NOTE-1172.md)).
- **Not that a column means "has".** The likelihood decides what a
  feature codes; in the paper's own demonstration three of four main
  features code an object's absence ([NOTE-1208](../notes.d/NOTE-1208.md)).

## Connections

- **[CASE-165](../cases.d/CASE-165.md), item 1.** The case's αH₁₂ = 9.31 for α = 3 is this limit's
  mean, and its correction for K = 16 is [THEORY-999](THEORY-999.md)'s.
- **[THEORY-985](THEORY-985.md).** The beta process gives the same count a second way, as
  the IBP's de Finetti measure.
- **[THEORY-1041](THEORY-1041.md).** Ordering the limit's feature probabilities gives the
  stick-breaking construction, whose truncations approximate this limit
  from below.
- **[THEORY-1019](THEORY-1019.md).** The Markov IBP repeats this argument with rows as time
  steps, and keeps this marginal only at the first step.
