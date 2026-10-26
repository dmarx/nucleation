---
status: Active
title: 'In the dependent Indian buffet process each item''s feature indicator is a Gaussian process thresholded at the quantile of a stick length that does not change with the covariate, so its prevalence is the same at every covariate value and its persistence is set separately by the covariance; the whole feature matrix at a covariate value is an Indian buffet process only when there is no shared feature-level process, and with one the items are correlated and fewer features are occupied'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpcg7gu. The construction (3)–(5) is the
    paper's, and so is the claim of IBP marginals. The per-item marginal
    is re-derived below; the failure of the matrix marginal when the
    shared process has positive variance, and the persistence numbers,
    are the record's, derived and checked by simulation, which meets the
    condition for Active under ADR-047 v2.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
source:
- LIT-tmpporrt
summary: >-
  Williamson, Orbanz and Ghahramani (2010), LIT-tmpporrt, read in
  NOTE-tmpcg7gu. Thresholding at a fixed quantile keeps each feature's
  prevalence at its stick length at every covariate value, which is what a
  hand-written logistic transition does not do. The paper's statement that
  Z(t) is an IBP at each t holds for its collapsed model; with a shared
  feature-level GP it holds item by item only. Persistence for a fixed
  correlation still falls with prevalence.
---

# THEORY-tmpumk4q: In the dependent Indian buffet process each item's feature indicator is a Gaussian process thresholded at the quantile of a stick length that does not change with the covariate, so its prevalence is the same at every covariate value and its persistence is set separately by the covariance; the whole feature matrix at a covariate value is an Indian buffet process only when there is no shared feature-level process, and with one the items are correlated and fewer features are occupied

## Source

Williamson, Orbanz and Ghahramani (2010), AISTATS, PMLR 9: 924–931,
LIT-tmpporrt, read in full in NOTE-tmpcg7gu; equations (1), (3)–(5) and
Appendix A. The paper states "For each t, the marginal distribution of
Z(t) is an IBP" (§3) and "has IBP marginals at any covariate value"
(footnote 1). The matrix-level analysis below is the record's.

## What was actually shown

Sticks: vj ~ Beta(α, 1), bk = ∏_{j≤k} vj, the IBP's stick-breaking
construction, not depending on t. Model (4): gk ~ GP(0, Σk),
hnk ~ GP(gk, ρ²I), znk(t) = I{hnk(t) < F⁻¹(bk | 0, Σk(t,t) + ρ²)}.

**Per item, prevalence is fixed.** Integrating out gk, hnk(t) is
N(0, Σk(t,t) + ρ²), so P(znk(t) = 1 | b) = bk at every t. Each row of Z(t)
is therefore distributed as an IBP row, holding Poisson(α) features in
the limit, at every t. Persistence is a separate matter: for a
stationary process with correlation r between hnk(t) and hnk(t + 1),
P(znk(t + 1) = 1 | znk(t) = 1) = Φ₂(c, c; r)/bk with c = Φ⁻¹(bk).

**The matrix, collapsed case.** With Σk = 0 the hnk are independent across
n, so given b the rows of Z(t) are independent with P(znk = 1) = bk. That
is the stick-breaking IBP exactly.

**The matrix, shared case.** With Σk(t,t) > 0, given gk(t) the items are
independent Bernoulli(γk(t)), γk(t) = Φ((c̃k − gk(t))/ρ), and γk(t) is
random with mean bk. So for two items E[z1k z2k | b] = E[γk(t)²] > bk²:
they are positively correlated. Since (1 − x)^N is convex,
E[(1 − γk)^N | b] ≥ (1 − bk)^N by Jensen, so each column is less likely to
be occupied than under the IBP. Simulated at N = 12, α = 3, ρ² = 1, 60
sticks, 40,000 draws: E[K+] = 9.34 with Σk(t,t) = 0 (IBP: αH₁₂ = 9.31),
7.06 with Σk(t,t) = 1 and 5.35 with Σk(t,t) = 4. Mean features per row
3.00 in all three.

**Persistence and prevalence** (exact bivariate normal, 2026-10-26). At
r = 0.5, 0.9 and 0.99 a held feature is kept with probability 0.18, 0.59
and 0.87 when bk = 0.025, and 0.44, 0.75 and 0.92 when bk = 0.2.

## What this does not say

- That the paper's prediction results depend on the matrix marginal. Its
  inference is truncated Gibbs on the model as defined, whatever its
  marginal law.
- That the dIBP makes features depend on one another or on the other
  items' features. Given the sticks and the GPs, columns are
  independent.
- That prevalence can change over t. It can only through the shared gk,
  and then only at the cost above.
- That one covariance holds rare and common features alike. For a given
  correlation, rare features are less persistent; per-feature length
  scales, which the paper uses, are what make persistence a per-feature
  parameter.
