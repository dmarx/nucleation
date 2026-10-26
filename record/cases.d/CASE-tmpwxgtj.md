---
status: Proposed
title: 'A 192-state organization on which one kernel gives several closure verdicts: the description by agents and phase is informationally closed on the intact support and fails global strong lumpability, its deficiency for the next pair of rule integrities under a declared intervention mixture is 0.55·H₂(1/3) ≈ 0.5051 bits and zero once the maintenance mode is kept, and finite-sample predictive gains misread both a positive and a zero information defect'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed at the owner's direction from an owner-supplied package of
    proposed updates (its "Priority A", where it was numbered 162). Its
    numbers were checked against the stored results in
    dmarx/PerspectiveLab@7e2edc2 (v1.8) and @9f82bfd (v1.9). One reading
    was corrected: the package said the refinement witness shows that
    refining a description need not improve informational closure, but
    the witness is in the global strong-lumpability defect, not in
    informational closure.
standing: stipulated
kind: construction
tags:
- information-theory
- causality
- complex-systems
date: '2026-10-26'
line: formal-apparatus
variant_of:
- CASE-125
illustrates:
- CLAIM-407
- CLAIM-409
summary: >-
  v1.8 of the Perspective Population Lab, dmarx/PerspectiveLab@7e2edc2:
  a finite organization small enough to enumerate, on which the senses of
  closure of [TERM-068](../terms.d/TERM-068.md) are computed exactly side by side. The maintenance
  mode plays [CASE-125](CASE-125.md)'s hidden bit: the intact dynamics are the same in
  every mode, and five of six interventions part them. v1.9, at
  @9f82bfd, calibrates finite-sample predictive gains against the exact
  values. It recombines distinctions the record already holds and claims
  no new theorem.
---

# CASE-tmpwxgtj: A 192-state organization on which one kernel gives several closure verdicts: the description by agents and phase is informationally closed on the intact support and fails global strong lumpability, its deficiency for the next pair of rule integrities under a declared intervention mixture is 0.55·H₂(1/3) ≈ 0.5051 bits and zero once the maintenance mode is kept, and finite-sample predictive gains misread both a positive and a zero information defect

## The case

Two perspectives, an authority bit, two record bits, two rule-integrity
bits (audit and admission), a phase clock of period 2, and three
maintenance modes (external reset, reciprocal production, feedback
without production) in one disjoint-union kernel: 192 states
(dmarx/PerspectiveLab@7e2edc2 experiments/finite_organization/). Seven
192 × 192 kernels, the ordinary one and six interventions, are exported
entry by entry.

The chain is reducible: the mode never changes, and damaged feedback
states can absorb. So no unique stationary law exists, and the lab
declares one: an equal-weight mixture of the three intact classes,
tested invariant. Every verdict below is relative to it.

## Results, as stored (results/exact_profile.json)

- **Informational closure.** On the declared law the finite-history
  defect of the agents, and of the agents with phase, is 0 bits. For
  authority alone it is 0.147 bits at h = 1 and 0.132 at h = 6, and for
  authority with one record bit 0.103 at h = 1 and 0.092 at h = 5. These
  are finite h, not an infinite-history limit.
- **Strong lumpability.** The total-variation defect of the agents with
  phase is 0.42 globally and 0 on the intact support. The description
  that omits only the mode has defect 1.0 globally and 0 on the intact
  support. Closure on a support is not lumpability of the chain.
- **Intervention deficiency.** The declared mixture is ordinary 0.45,
  audit loss 0.15, admission loss 0.10, double loss 0.15, audit team off
  0.10 and admission team off 0.05. A seventh intervention, both teams
  off, is enumerated with weight 0. The outcome is the next pair of rule
  integrities. Γ = I(S; Y^(I) | T(S), I) is 0.5051 bits for every
  description that omits the mode and 0 for the full state. It is exactly
  0.55·H₂(1/3), since each non-ordinary intervention splits the three
  modes one against two.
- **Γ depends on the source law.** For the ordinary intervention alone it
  is 0 on the intact support and H₂(1/3) = 0.918 bits on the damaged
  support.
- **Refinement.** For this one law, mixture and outcome,
  Γ(authority) ≥ Γ(organization) ≥ Γ(full), [CLAIM-409](../claims.d/CLAIM-409.md)'s monotone half.
  In an ablation with the authority coupling g = 0, the global
  strong-lumpability defect is 0 for authority, 0.380 for authority with
  one record bit, and 0 for the full state. That pattern is the shape of
  [CLAIM-409](../claims.d/CLAIM-409.md)'s non-monotone half, but it is in strong lumpability, not in
  informational closure, which is what the claim's three-bit chain is
  about.

## Finite samples (v1.9)

dmarx/PerspectiveLab@9f82bfd experiments/closure_estimation/ and
EXPERIMENT_REPORT_V19.md. Windows sampled from the declared law, 12
repetitions at each training size, held-out log-loss gain in bits:

| projection | exact defect | N = 300 | N = 19,200 |
|---|---|---|---|
| authority, h = 1 | 0.1474 | 0.0655 | 0.1468 |
| authority, h = 3 | 0.1323 | 0.0505 | 0.1307 |
| authority with one record bit, h = 2 | 0.0930 | −0.0082 | 0.0921 |
| agents with phase, h = 1 | 0 | −0.3673 | −0.0174 |

A negative gain is a difference of fitted risks, not a negative
conditional information. At N = 300 the positive 0.0930 bits shows a
positive gain in only 3 of 12 repetitions. For the exact zero all 12
gains stay negative at every N tested, because the larger model pays an
estimation cost. So a non-positive gain is no evidence of closure. For
Γ the held-out macro log-loss is 0.7718 bits at N = 300 and 0.5103 at
19,200, against the exact 0.5051.

In the separate 32-member population, a fixed one-step target, the next
change of the mean record, has held-out MSE 6.27 × 10⁻⁶ from the current
six-variable macrostate, 2.65 × 10⁻⁸ with four lags, and 3.8 × 10⁻³³ with
the current mean local endorsement. The last is the update law
recovered, not a discovery. None of this is closure of the macrostate.

## What it can show

That on one exactly known kernel, closure on a support, global
lumpability and sufficiency for a declared intervention mixture give
different verdicts, and that the last is [CLAIM-407](../claims.d/CLAIM-407.md)'s Γ with its zero
condition met once the mode is kept. That a finite-sample sign test of
closure fails in both directions at the sample sizes tested.

## What it cannot show

- Anything about real organizations. The parameters are chosen to give
  non-degenerate kernels, and the model is not a verified reduction of
  the 32-member population.
- A stationary verdict independent of the declared law, or a Γ on a scale
  shared with other intervention mixtures or outcomes.
- That reciprocal Boolean updates are closure of constraints ([TERM-070](../terms.d/TERM-070.md)),
  or agency.

## Provenance

dmarx/PerspectiveLab@7e2edc2 experiments/finite_organization/
(model.py, diagnostics.py, run_exact.py, test_exact.py, results/;
EXPERIMENT_REPORT_V18.md) and dmarx/PerspectiveLab@9f82bfd
experiments/closure_estimation/ (EXPERIMENT_REPORT_V19.md). When filed,
the finite-organization test suite was re-run at
dmarx/PerspectiveLab@11c1495 and passed.
