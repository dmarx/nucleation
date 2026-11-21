---
status: Open
title: 'Compute the effective dimensions of the two-dimensional Ising model at and away from its critical point on one set of finite lattices, the stiff Fisher count at several sample sizes, the growth of predictive information, the relevant directions and the cluster dimension, to see which agree'
version: 1
stage: idea
priority: low
method:
- formal
- empirical
tags:
- information-geometry
- information-theory
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
advances:
- QUESTION-tmpzlagu
summary: >-
  A test for [QUESTION-tmpzlagu](../questions.d/QUESTION-tmpzlagu.md), which A raised at A19's close and A21 §1
  of the exchange "Rich Get Richer Power Laws" and left without a
  method. On periodic L×L Ising lattices at T_c and at two temperatures
  either side, compute in one observation scheme (decimated spins, as in
  [THEORY-777](../theory.d/THEORY-777.md)): the number of Fisher eigenvalues resolved by n samples for
  several n; the growth of past–future information along a spatial
  transfer direction; the count of eigenvalues that do not decay under
  decimation; and the fractal dimension of the clusters. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpj0k4q CLAIM-tmpq8q9t — filed with this lead from the same exchange, Open or Proposed -->
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the scheme this lead reuses -->
<!-- inactive-ok-file: TERM-tmpxml4k — filed with this lead from the same exchange, Proposed -->

# LEAD-tmpl5wxz: Compute the effective dimensions of the two-dimensional Ising model at and away from its critical point on one set of finite lattices, the stiff Fisher count at several sample sizes, the growth of predictive information, the relevant directions and the cluster dimension, to see which agree

## Sketch

**Why.** [QUESTION-tmpzlagu](../questions.d/QUESTION-tmpzlagu.md) asks whether four effective dimensions agree.
The record has each in a different setting; no system has had all four
computed under one scheme. The 2D Ising model is the natural first case:
exact exponents, the record's own reading of its decimated Fisher spectrum
([THEORY-777](../theory.d/THEORY-777.md)), and a transfer matrix that gives exact block entropies on
strips.

**Design.**

1. **Family and scheme.** The field and the nearby couplings of
   [THEORY-777](../theory.d/THEORY-777.md), observed through spins left after k checkerboard
   decimations, on L = 16, 32, 64, at T_c and at T = T_c(1 ± 0.1).
2. **Stiff count against sample size.** From the Fisher matrix of the
   decimated spins, count eigenvalues with nλ_j ≥ 1 for n from 10 to 10⁶
   configurations, and fit the growth ([CLAIM-tmpj0k4q](../claims.d/CLAIM-tmpj0k4q.md)).
3. **Predictive information.** On strips of width W, exact by transfer
   matrix: I between adjacent column blocks of length T, as T grows,
   at and off T_c ([TERM-tmpxml4k](../terms.d/TERM-tmpxml4k.md)).
4. **Relevant count.** The number of eigenvalues whose decay with k is
   slower than b^(−d) per step, as [THEORY-777](../theory.d/THEORY-777.md) does.
5. **Cluster dimension.** Box-counting of the largest geometric spin cluster, against
   187/96 at T_c.

**What would count.** Agreement of the stiff count's large-n plateau with
the relevant count across L would support the conjecture that relevance
is stiffness in the limit of coarse observation; a predictive-information
growth that tracks the cluster dimension and not the Fisher count would
show the predictive and parametric dimensions come apart.

**Cost.** Steps 1, 2 and 4 rerun the Monte Carlo of [THEORY-777](../theory.d/THEORY-777.md) (hours on
one machine); step 3 is minutes for W ≤ 12; step 5 is minutes. The
exact Fisher information about the field and coupling on small tori is
already in [CLAIM-tmpq8q9t](../claims.d/CLAIM-tmpq8q9t.md).

## Note of 2026-11-21: Bialek, Nemenman & Tishby, read

Bears on step 3. Bialek, Nemenman and Tishby ([NOTE-tmpilbkz](../notes.d/NOTE-tmpilbkz.md), §6, fn. 9)
assert that "At critical points the predictive information will diverge
with the size of the system", with coefficients "related to the standard
scaling dimensions", the details to be worked out. That is a prediction
this lead's strip computation could test: whether the predictive
information of a strip of width W at T_c grows with W, and at what rate.
Their quantity has an infinite future; the lead's, if it uses T′ = T, is a
constant factor smaller for power-law growth ([TERM-tmpxml4k](../terms.d/TERM-tmpxml4k.md)).
