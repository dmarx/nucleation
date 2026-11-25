---
number: 777
status: Proposed
formerly:
- CLAIM-tmpve51e
title: 'Drift grows hyperbolically with arrival/anchoring'
statement: >-
  If ideas arrive at rate λ, are coded by one first-come coder at rate κ >
  λ, and are restated once per unit of time while they wait, an idea's
  expected drift before it is coded is σ²/(κ − λ) in mean square for
  features copied with error and (c − x₀)·ln(1/a)/(κ − λ + ln(1/a)) in mean
  for contracted ones, so drift tracks the ratio of arrival to anchoring
  hyperbolically and grows without bound as the ratio reaches one; coding at
  a fixed occurrence caps it at that many restatements' worth
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the M/M/1 sojourn time, exponential with
  rate κ − λ; in E[σ²W] for the diffusive part; in E[1 − a^W] =
  ln(1/a)/(κ − λ + ln(1/a)) for W exponential; or in the cap for coding
  at the k-th occurrence. Or a queue meeting the hypotheses whose mean
  drift before coding does not grow as κ − λ falls to zero.
tags:
- probabilistic-modeling
- operations-research
- design-rationale
date: '2026-11-20'
line:
- formal-apparatus
- nucleating-argument
rests_on:
- CLAIM-773
uses:
- TERM-132
summary: >-
  [CLAIM-186](CLAIM-186.md)'s arrival against anchoring, as a queue. Under Poisson
  arrivals, exponential coding times and one restatement per unit of
  waiting time, the drift an idea accrues before it is coded follows from
  the mean sojourn 1/(κ − λ) and [CLAIM-773](CLAIM-773.md)'s rates. The overload case,
  λ ≥ κ, is [CLAIM-705](CLAIM-705.md)'s in another line. Coding at the k-th occurrence
  ([CLAIM-176](CLAIM-176.md)'s rule is k = 2) caps an idea's uncoded restatements at
  k − 1. Derived and checked by simulation (2026-11-20). The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-773 CLAIM-186 CLAIM-176 CLAIM-705 CLAIM-782 — Proposed; the model this extends, and the claims it bears on -->

# CLAIM-777: Drift grows hyperbolically with arrival/anchoring

## The model

Ideas arrive as a Poisson process of rate λ. One coder files them first
come, first served, with exponential coding times of rate κ. Until it is
coded, an idea is restated once per unit of time, and its features drift as
in [CLAIM-773](CLAIM-773.md), taken in continuous time. Once coded, it is conserved.

## The result

The time W an idea waits uncoded is the M/M/1 sojourn, exponential with rate
κ − λ when ρ = λ/κ < 1, so E[W] = 1/(κ − λ) = 1/(κ(1 − ρ)).

- **Copied with error.** E[d² | W] = σ²W, so E[d²] = σ²/(κ − λ).
- **Contracted.** E[d | W] = (c − x₀)(1 − a^W), and for W exponential with
  rate r = κ − λ, E[a^W] = r/(r + ln(1/a)). So E[d] = (c − x₀)·ln(1/a)/(κ −
  λ + ln(1/a)): near zero when coding is fast beside the contraction, and
  the whole distance to the convention as κ − λ → 0.
- **Copied with bias.** E[d] = μ/(κ − λ).

All three grow without bound as ρ → 1, hyperbolically and not linearly in ρ.
For ρ ≥ 1 the queue is unstable and waits grow without bound, [CLAIM-705](CLAIM-705.md)'s
result for challenges outpacing their resolution.

**Coding at a fixed occurrence.** If an idea is coded the k-th time it turns
up, it is restated uncoded at most k − 1 times, whatever the arrival rate,
so its drift is at most k − 1 steps' worth: for k = 2, [CLAIM-176](CLAIM-176.md)'s rule, one
step, σ² + μ² in mean square plus (1 − a)(c − x₀) toward the convention. The
cap holds because the rule ties coding to the idea's own recurrence and not
to a coder's free time; it says nothing about the cost of keeping up, which
is [CLAIM-176](CLAIM-176.md)'s other half.

## Checks

Simulated on 2026-11-20 (scripts in the curation entry of 2026-11-20,
231623). Mean wait, κ = 1, 400,000 arrivals: 2.00, 4.96, 9.96 and 21.2 at
ρ = 0.5, 0.8, 0.9 and 0.95, against 2, 5, 10 and 20; the run at 0.95 is
still settling, as runs near saturation do. Contracted bias, a = 0.9, D = 2,
10⁶ draws of W: 0.3484, 1.0263 and 1.3559 at κ − λ = 0.5, 0.1 and 0.05,
against 0.3481, 1.0261 and 1.3563. The diffusive figure follows from the
mean wait by E[σ²W] and was not simulated separately.

## What it does not say

- Not that an exchange is an M/M/1 queue. The hyperbolic shape is this
  model's; a different service law changes the constant, and in M/G/1 the
  mean wait still diverges as ρ → 1.
- Not whether drift accrues per restatement or per unit of time. The model
  restates once per unit of time, which makes the two the same; where they
  differ is [CLAIM-782](CLAIM-782.md).
