---
number: 59
status: Proposed
formerly:
- CLAIM-tmph3w8f
title: 'Repeated reconstruction chains fall into different regimes under conditions assigned in advance, contracting toward conventions, accumulating neutrally or amplifying, and amplification needs a metric other than total variation, an enlarged state or state-dependent dynamics'
version: 3
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-208: the metric and the
    estimation of the sensitivities are fixed before the data. Version
    1's condition read: 'Measured per-generation sensitivity of real
    reconstruction chains shows no difference between conditions that
    the theory assigns to different regimes.'
- version: 3
  date: '2026-10-29'
  note: >-
    rests_on adds CLAIM-068 (eleventh status review, ADR-057): the title's
    'contracting toward conventions' is CLAIM-068's attraction, which the
    note of 2026-10-15 cites for it, and ARG-027 and CLAIM-234 say this
    claim takes from it. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Per-generation sensitivities, estimated in a metric fixed in advance
  (not total variation, in which no Markov step amplifies) from several
  independent retellers per generation on held-out and perturbed inputs,
  show no difference between conditions that the theory assigns, in
  advance, to different regimes.
tags:
- complex-systems
- mathematics
date: '2026-10-08'
line: pragmatic-transport
rests_on:
- CLAIM-056
- CLAIM-267
- CLAIM-068
summary: >-
  A50 §3, A52 §5.3 and the crystallized argument §19, recovered. The
  manuscript and C7 Appendix B keep the corrected bound and the remark
  that κ ≤ 1 in total variation; the taxonomy and its third experiment's
  test were dropped.
objected_by:
- CLAIM-208
---
<!-- inactive-ok-file: CLAIM-049 CLAIM-068 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-059: Repeated reconstruction chains fall into different regimes under conditions assigned in advance, contracting toward conventions, accumulating neutrally or amplifying, and amplification needs a metric other than total variation, an enlarged state or state-dependent dynamics

## The claim

A110 §19: contracting (L < 1: "convergence toward stable conventions"), neutral
(L = 1: "Local distortions can accumulate without amplification"), amplifying
(L > 1: "Small deviations may become disproportionately consequential"). "For
Markov kernels acting on probability measures under total variation distance,
the contraction coefficient is at most one. Amplification requires a different
metric, an expanded state model, or an appropriate state-dependent dynamics." The
argument's Experiment 3 tested it: "Do relational structures exhibit identifiable
contraction, instability, or convergence toward conventions distinct from the
source?"

## Where it went

The manuscript §8 corrects the bound, measuring e_i against a reference transport
with Lipschitz constants κ_i, and keeps the caveat: "For stochastic kernels in
total variation, contraction coefficients do not exceed one; amplification may
arise under other metrics or nonlinear, adaptive representations." C7 Appendix B:
"distances on reconstructed relational representations need not satisfy the same
bound." The regimes as a classification, and the experiment that would tell them
apart, are gone. The contracting regime is [CLAIM-068](CLAIM-068.md); the amplifying one needs
the enlarged state of [CLAIM-049](CLAIM-049.md).

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s full classification found this claim compound. The three
regimes, as regimes of the error recursion e_(i+1) ≤ L_i e_i + ε_i, and
the bound that a Markov kernel's contraction coefficient in total
variation is at most one, are demonstrated. They are already held, in
that general form, by [CLAIM-267](CLAIM-267.md), split from [CLAIM-056](CLAIM-056.md) under [ADR-040](../decisions.d/ADR-040.md), so
no new claim was drafted; this claim now rests on [CLAIM-267](CLAIM-267.md) directly as
well as through [CLAIM-056](CLAIM-056.md). What this claim keeps is the application:
that real reconstruction chains fall into different regimes under
conditions the theory assigns in advance, with contraction read as
convergence toward conventions ([CLAIM-068](CLAIM-068.md)), which is what its defeat
condition tests. No observation the record holds supports that, so its
warrant is interpretive, not demonstrated. The title was changed,
because version 2's "Repeated reconstruction has three regimes" read as
the formal taxonomy, which is [CLAIM-267](CLAIM-267.md)'s. It now says the claim is
about real chains and conditions fixed in advance.

## Note of 2026-10-29: what holds it back

Two things. The contracting regime in the title is CLAIM-068's attraction
toward conventions, which is Proposed and now a premise. And the record
assigns no condition to any regime. The defeat condition meets CLAIM-208's
point, that the regime waits on a metric chosen afterwards, by fixing the
metric in advance, but no metric is fixed and no condition is assigned, so
the test it names has nothing yet to test. It moves when a metric and an
assignment of conditions to regimes are filed, or when CLAIM-068 is
promoted.
