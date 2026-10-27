---
status: Active
title: 'In the Markov Indian buffet process each feature''s probability of staying on is drawn independently of its probability of switching on, so how long a feature persists once on does not depend on how rare it is; the process is defined for the time steps of one sequence, not for several objects over time'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpuk5qe. It is the model's definition, eqs.
    (3)–(4) and §2.4 of Van Gael, Teh and Ghahramani (2008), and was
    checked against the collapsed likelihood (6): the exact predictive
    probability of staying on, computed from (6), is (c¹¹ + γ)/(γ + δ +
    c¹⁰ + c¹¹) and does not involve α or the switching-on counts (record
    script, 2026-10-27).
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-tmpfd531
summary: >-
  Van Gael, Teh and Ghahramani (2008), LIT-tmpfd531, read in
  NOTE-tmpuk5qe. Each column is a two-state chain from an off state with
  a_m = P(0 → 1) ~ Beta(α/M, 1) and b_m = P(1 → 1) ~ Beta(γ, δ),
  independent, and the stick-breaking construction keeps each b paired
  with its a as an independent draw. Rarity (small a) and persistence
  (b) are separate per-feature parameters. It does not say that
  prevalence is held fixed over time, which it is not (THEORY-tmp29uzx),
  nor how to share the chains across several objects.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this bears on, cited as open -->

# THEORY-tmpzv1fw: In the Markov Indian buffet process each feature's probability of staying on is drawn independently of its probability of switching on, so how long a feature persists once on does not depend on how rare it is; the process is defined for the time steps of one sequence, not for several objects over time

## Source

Van Gael, Teh and Ghahramani (2008), *The infinite factorial hidden
Markov model*, LIT-tmpfd531, read in full in NOTE-tmpuk5qe: §2.1 (the
finite model, (3)–(6)), §2.4 (stick-breaking) and §2's statement that
"rows correspond to timesteps and the columns to features or Markov
chains".

## What was actually shown

**The definition.** For M features over T time steps, column m has
transition matrix [[1 − a_m, a_m], [1 − b_m, b_m]], with
a_m ~ Beta(α/M, 1) and b_m ~ Beta(γ, δ) drawn independently, and every
chain starts off. In the collapsed likelihood (6) the a-factor depends
only on c⁰⁰ and c⁰¹ and the b-factor only on c¹⁰ and c¹¹. In the
stick-breaking representation the b paired with the m-th largest a is
"an independent draw from a Beta(γ, δ) distribution which is independent
of M".

**The check.** From (6), the probability that a feature on at t stays on
at t + 1, given its counts, is (c¹¹ + γ)/(γ + δ + c¹⁰ + c¹¹), whatever
c⁰¹, c⁰⁰ or α. The record computed it as a ratio of (6) for three count
vectors. (The paper's buffet prints it with δ for γ; NOTE-tmpuk5qe.)
A priori, a feature on is kept with probability E[b] = γ/(γ + δ). That is
10/11 = 0.91 at the prior means the paper's experiment uses (γ = 10,
δ = 1), for a feature with a = 0.025 as for one with a = 0.5.

**One sequence.** The rows are time steps of a single object, and the
iFHMM explains one multichannel time series. The paper has no axis of
objects and derives no limit for several sequences sharing a feature's
(a_m, b_m).

## What this does not say

- **Not that prevalence is constant.** A chain's stationary on-fraction
  is a/(1 − b + a), which depends on b. The expected number of active
  features rises from α at the first step (THEORY-tmp29uzx).
- **Not that persistence is learned per feature from little data.** The
  b's are independent a priori. A posteriori a rare feature has few 1 → 1
  counts and its b stays near the prior.
- **Not a model of an organization's members.** Using it for N members
  needs a sharing structure the paper does not give.

## Connections

- **CASE-165, item 2.** The case's sticky term is, with its other inputs
  at zero, the same two-state chain with on-rate π_k and stay-rate
  σ(logit π_k + ρ). There the stay-rate is a function of the on-rate,
  which is why a rare feature is kept with probability 0.16 at ρ = 2. In
  the mIBP the two are independent, so the case's "one ρ cannot do that
  for features of different prevalence" does not arise. NOTE-tmpuk5qe
  gives the numbers.
- **THEORY-1006.** The dependent IBP keeps each feature's prevalence
  fixed and sets persistence through its Gaussian process, and only
  per-feature length scales make persistence per feature. The mIBP has
  persistence per feature by construction and fixes no prevalence.
- **NOTE-1172.** The review describes this model in §7.4 in the same terms;
  this is the primary source.
