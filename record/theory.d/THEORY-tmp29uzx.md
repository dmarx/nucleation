---
status: Active
title: 'Under the Markov Indian buffet process the expected number of features on at the first time step is α, as in the Indian buffet process, but it rises over time toward α·E[ln((2 − b)/(1 − b))] with b ~ Beta(γ, δ), which is 9.04 at γ = 10 and δ = 1, so after the first step the rows are not distributed as an Indian buffet process'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpuk5qe. The record's derivation, not the
    paper's, from the model's definition, (3)–(4) of Van Gael, Teh and
    Ghahramani (2008). It was checked against simulation of the finite
    model (M = 20,000, 200 replicates, α = 3, T = 245) at three settings
    of (γ, δ); the simulated and exact values agree to within about 3% at
    every step checked (record script, 2026-10-27). It confirms, for the
    count of active features, footnote 1 of the dependent IBP
    (NOTE-1175), which says the Markov IBP lacks IBP marginals.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-tmpfd531
- LIT-1548
summary: >-
  Van Gael, Teh and Ghahramani (2008), [LIT-tmpfd531](../literature.d/LIT-tmpfd531.md), read in
  [NOTE-tmpuk5qe](../notes.d/NOTE-tmpuk5qe.md). A chain starting off is on at step t with probability
  a(1 − (b − a)^t)/(1 − b + a). As M → ∞ the a's form a Poisson process
  of intensity α/a on (0, 1), so E[number on at t] = α ∫₀¹ E_b[(1 − (b −
  a)^t)/(1 − b + a)] da. That is α at t = 1 and tends to α·E[ln((2 −
  b)/(1 − b))]. The number of features ever on is still Poisson(αH_T), as
  the paper says. This concerns the expected count only, not the full
  row distribution beyond it.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this bears on, cited as open -->

# THEORY-tmp29uzx: Under the Markov Indian buffet process the expected number of features on at the first time step is α, as in the Indian buffet process, but it rises over time toward α·E[ln((2 − b)/(1 − b))] with b ~ Beta(γ, δ), which is 9.04 at γ = 10 and δ = 1, so after the first step the rows are not distributed as an Indian buffet process

## Source

Van Gael, Teh and Ghahramani (2008), *The infinite factorial hidden
Markov model*, [LIT-tmpfd531](../literature.d/LIT-tmpfd531.md), read in full in [NOTE-tmpuk5qe](../notes.d/NOTE-tmpuk5qe.md): the finite
model (3)–(4), from which this is derived. Williamson, Orbanz and
Ghahramani (2010), [LIT-1548](../literature.d/LIT-1548.md), footnote 1 ([NOTE-1175](../notes.d/NOTE-1175.md)), states the
conclusion without derivation.

## What was actually shown

**The derivation.** A two-state chain with P(0 → 1) = a and
P(1 → 1) = b, started off, is on at step t with probability
π₁(1 − λ^t), where π₁ = a/(1 − b + a) and λ = b − a. With M features and
a_m ~ Beta(α/M, 1), M·E[g(a)] → α ∫₀¹ g(a)/a da for any g with g(0) = 0,
the IBP's limit, since Beta(α/M, 1) has density (α/M)a^{α/M − 1}. So, with
b independent of a,

E[number on at t] → α ∫₀¹ E_b[(1 − (b − a)^t)/(1 − b + a)] da.

At t = 1 the integrand is 1, giving α, the IBP's Poisson(α) mean for one
row. As t → ∞ the limit is α ∫₀¹ E_b[1/(1 − b + a)] da = α E_b[ln((2 −
b)/(1 − b))]. That is finite for every γ, δ > 0, since E[−ln(1 − b)] =
ψ(γ + δ) − ψ(δ).

**The values.** At α = 3:

| (γ, δ) | t = 1 | t = 2 | t = 10 | t = 50 | t = 245 | limit |
|---|---|---|---|---|---|---|
| (10, 1), the paper's prior means | 3.00 | 4.23 | 7.03 | 8.50 | 8.92 | 9.04 |
| (10, 3) | 3.00 | 3.81 | 5.20 | 5.41 | 5.42 | 5.42 |
| (1, 1) | 3.00 | 3.00 | 3.87 | 4.10 | 4.15 | 4.16 |

Simulation of the finite model (M = 20,000, 200 replicates) gave, for
(10, 1), 2.90, 4.32, 7.26, 8.77 and 9.20 at the same steps, and agreed to
within about 3% for the other settings (record simulation, 2026-10-27).

**What the paper does say.** The number of chains ever on, M₊, is
Poisson(αH_T) (§2.3). That is consistent: it counts columns ever used,
not columns on at a step.

## What this does not say

- **Not the full distribution of a row** after the first step. Only the
  expected count is derived; the count at a step is Poisson in the limit
  (a Poisson process thinned independently), but nothing more is claimed.
- **Not a defect relative to the paper's purpose.** The paper wants
  features that persist ("people speak for larger stretches of time"),
  and claims no IBP marginal per row.
- **Not about several objects.** The model has one sequence of rows.

## Connections

- **[CASE-165](../cases.d/CASE-165.md), item 2.** The case finds that T23's sticky term holds the
  buffet's prior properties "at t = 0 only". The Markov IBP has the same
  property for the count of active features: α at the first step,
  three times α later at the paper's own prior means. Neither the sticky
  term nor its closest established relative keeps the prior's marginal
  over time. Of the IBP's dependent variants in the record, only the
  dependent IBP does ([THEORY-1006](THEORY-1006.md)).
- **[THEORY-999](THEORY-999.md).** That account concerns a finite truncation's count of
  occupied features against the limit's αH_N. This one concerns the
  count at a time step against the IBP's α. Both are cases of an IBP
  figure quoted where it does not hold.
