---
number: 267
status: Active
formerly:
- CLAIM-tmpjp2tl
title: Per-step discrepancies between a chain of maps and a reference chain
  compound through the sensitivity of the later steps, so the same local error
  can be damped, accumulated or amplified, and closeness at every step can
  coexist with large end-to-end divergence
version: 3
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-056 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-056 rests on; CLAIM-056
    now rests on this claim.
- version: 2
  date: '2026-10-14'
  note: >-
    Where the record applies it now names LIT-971's closed-form case of
    the bounded regime (THEORY-289), prompted by NOTE-815. The
    claim is unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/CLAIM-267.yaml,
    batch 001, ADR-047). The derivation was checked: one triangle inequality
    per step. The indices are pinned to one map: ε_i is measured at the
    reference point and L_i is the Lipschitz constant of the actual chain's
    map f_i. A section of witnesses for the three regimes is added. The
    claim is otherwise unchanged.
role: thesis
warrant: demonstrated
defeated_if: A chain of maps on a metric space, with per-step discrepancies
  ε_i from a reference chain and later maps with Lipschitz constants L_i,
  whose end-to-end error exceeds Σ ε_i ∏_(j>i) L_j plus the propagated initial
  error. The bound is a derivation, so only an error in it defeats the claim;
  a domain where the constants cannot be estimated does not.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-13'
line:
- formal-apparatus
summary: 'The general content of [CLAIM-056](CLAIM-056.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  the line-neutral recursion does not rest on [CLAIM-106](CLAIM-106.md)''s account of fidelity.
  It is elementary: with e_(i+1) ≤ L_i e_i + ε_i, the end-to-end error is
  bounded by the discrepancies weighted by the later Lipschitz constants.
  Three regimes follow. For stochastic kernels in total variation, contraction
  coefficients do not exceed one, so amplification needs another metric or
  a nonlinear, adaptive state.'
supports:
- CLAIM-056
- CLAIM-191
- CLAIM-059
---
<!-- inactive-ok-file: CLAIM-056 CLAIM-068 CLAIM-106 CLAIM-191 QUESTION-017 — Proposed; cited for what each holds or applies, open, not settled -->
<!-- inactive-ok-file: THEORY-289 — Proposed; filed today, cited as a closed-form instance, not leaned on -->

# CLAIM-267: Per-step discrepancies between a chain of maps and a reference chain compound through the sensitivity of the later steps, so the same local error can be damped, accumulated or amplified, and closeness at every step can coexist with large end-to-end divergence

## The claim

Take a chain u_0 → u_1 → … → u_n produced by maps f_1, …, f_n on a metric
space, u_i = f_i(u_(i−1)), and a reference chain v_i = g_i(v_(i−1)). Let
e_i = d(u_i, v_i). Let ε_i = d(f_i(v_(i−1)), g_i(v_(i−1))) be the
discrepancy step i introduces at the reference point, and L_i a Lipschitz
constant of f_i. By the triangle inequality,

e_i ≤ d(f_i(u_(i−1)), f_i(v_(i−1))) + d(f_i(v_(i−1)), g_i(v_(i−1))) ≤ L_i e_(i−1) + ε_i,

so

e_n ≤ (∏_(j=1..n) L_j) e_0 + Σ_(i=1..n) ε_i ∏_(j>i) L_j.

The impact of a local error depends on the dynamics after it. There are
three regimes: contractive (L < 1, errors are damped), neutral (L = 1, they
accumulate, giving the familiar d(u_0, u_n) ≤ nε), and expansive (L > 1,
they amplify). Closeness at every step is compatible with large divergence
end to end, because similarity is not transitive.

One restriction is exact: for stochastic kernels in total variation,
contraction coefficients do not exceed one. Amplification needs another
metric, an enlarged state, or nonlinear, state-dependent dynamics.

## Where the record applies it

[CLAIM-056](CLAIM-056.md) applies the recursion to translation and reconstruction chains,
with the discrepancy read as a transport error against a reference
transport, which rests on [CLAIM-106](CLAIM-106.md)'s graded fidelity. [CLAIM-191](CLAIM-191.md) applies
it to restatements of an argument across sessions. Both now rest on this
claim for the recursion and keep their own premises for the application.

[THEORY-289](../theory.d/THEORY-289.md), filed from [LIT-971](../literature.d/LIT-971.md) (read in [NOTE-815](../notes.d/NOTE-815.md)), is an exact
closed-form case of the bounded regime. When each round of a linear
regression is refit to labels from the previous fit and earlier rounds'
data are kept, the per-round discrepancy is scaled by 1/i, the weighted sum
converges, and test error is bounded at π²/6 times the first fit's. When
the data are replaced, the discrepancies add and error grows linearly.
Error is accumulated but bounded: every round still adds some.

## What it does not say

- It does not say any departure from the reference chain is an error in a
  normative sense. The bound measures departure relative to a reference.
- It does not say drift is random. Attraction toward conventions is a
  further claim ([CLAIM-068](CLAIM-068.md)).
- It does not cover directed, non-metric distortion ([QUESTION-017](../questions.d/QUESTION-017.md)).

## Note of 2026-10-19: witnesses for the three regimes

The bound is an upper bound. Each regime is also attained, on ℝ with the
reference g_i(x) = c·x and the actual chain f_i(x) = c·x + ε, from
u_0 = v_0. Then e_i = c·e_(i−1) + ε exactly, and every step introduces the
same discrepancy ε.

- c = 1/2: e_n = 2ε(1 − 2⁻ⁿ) < 2ε. Each error is damped, and the total
  stays bounded.
- c = 1: e_n = nε. The errors accumulate, so each step is within ε of the
  reference while the endpoints are nε apart.
- c = 2: e_n = (2ⁿ − 1)ε. The errors are amplified.
