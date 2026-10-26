---
status: Proposed
title: 'Capture and selectively admitted evidence in two lab realizations: in a four-variable model of authority, record and competence the equilibrium fold under self-scoring is at c ≈ 0.4247 while the declared history is trapped from c ≈ 0.4469, and in a 32-member event-level population, admission of cues that depends on the record reverses the sign of the admitted evidence and leaves the worse alternative in charge in 41 of 64 worlds, which exact inverse-propensity weighting brings to 0 of 64 below full selectivity'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed at the owner's direction from an owner-supplied package of
    proposed updates (its "Priority A", where it was numbered 161). Its
    numbers were checked against the stored results in
    dmarx/PerspectiveLab@7e2edc2 and its provenance moved from an archive
    to that commit. One description was corrected: the v1.1 comparison is
    a 2 × 2 factorial of four cells, not four arms.
standing: stipulated
kind: executed-study
tags:
- self-governance
- complex-systems
- probabilistic-modeling
date: '2026-10-26'
line: distributed-agency
variant_of:
- CASE-155
- CASE-156
- CASE-158
illustrates:
- CLAIM-297
- CLAIM-277
summary: >-
  Versions 1.1 to 1.3 of the Perspective Population Lab, now held as
  dmarx/PerspectiveLab@7e2edc2. v1.2 is a deterministic four-variable
  model whose analytic fold and whose trapping of a declared history come
  apart. v1.3 is a separately coded event-level population in which the
  filtering of [CASE-156](CASE-156.md) runs on sampled cues, and a known-propensity
  evaluator undoes it while admission stays positive. v1.1 adds capture
  and selective audits to [CASE-158](CASE-158.md)'s design, and the router still wins.
  The sign reversal is [CASE-156](CASE-156.md)'s; what is new is two running
  realizations, with their code.
---
<!-- inactive-ok-file: CLAIM-297 CLAIM-277 CLAIM-286 — Proposed; the claims this case illustrates or bears on, nothing here rests on their being settled -->

# CASE-tmpr1vuv: Capture and selectively admitted evidence in two lab realizations: in a four-variable model of authority, record and competence the equilibrium fold under self-scoring is at c ≈ 0.4247 while the declared history is trapped from c ≈ 0.4469, and in a 32-member event-level population, admission of cues that depends on the record reverses the sign of the admitted evidence and leaves the worse alternative in charge in 41 of 64 worlds, which exact inverse-propensity weighting brings to 0 of 64 below full selectivity

## The case

Two perspectives, A and B, share authority. B is the better one
throughout, and a history starts with A in charge.

- **v1.2, a four-variable model** (dmarx/PerspectiveLab@7e2edc2
  experiments/regime_atlas/). Its state is the log odds z of A's
  authority, a record lean r, and the competences k_A and k_B, which can
  grow with access. Self-scoring c feeds the record back into authority,
  and selectivity s hides evidence that contradicts the record. An
  81 × 81 grid over c and s runs two histories from identical
  competences. In its limit (no leak, no learning, full observation) one
  Euler step is [CASE-155](CASE-155.md)'s map, checked to 12 places by the lab's test.
- **v1.3, an event-level population** (experiments/stochastic_population/).
  32 networked perspectives with credibility weights, local records,
  admission of cues that depends on the local record, and practice. Paired
  histories share a world. The outcome is a wrong incumbent: A holds at
  least 75% of authority at the end of 1,400 updates. 64 world seeds per
  controlled condition. The inverse-propensity arm is given the exact
  admission probabilities, as an oracle.
- **v1.1, a factorial on [CASE-158](CASE-158.md)'s design** (experiments/capture_feedback/,
  EXPERIMENT_REPORT.md). It crosses an independent evaluator with one
  scored 0.2·truth + 0.8·distance to the current mixture, and full audits
  with audits attributed to one specialist per receiver, at equal query
  cost. Receipts arrive after the episode, for the router as for
  governance. 12 paired seeds.

v1.2 is not a reduction of v1.3. They share motifs, and their mechanisms
differ: v1.2's gate only attenuates an expected negative gap, while v1.3's
sampled admission can reverse its sign.

## Results, as stored

**v1.2** (results/atlas_summary.json):

- With competence frozen and full observation, the positive equilibrium
  appears at c = 0.42468, a fold. The declared history is trapped from
  c = 0.4469 at s = 0, and from c = 0.2438 at s = 1.
- With competence that grows with access, the onsets fall to 0.3900 and
  0.2356. B stays the better perspective at every competence the model
  allows, so what entrenches is authority, not merit.
- The onset depends on the starting history. At s = 0 it is 0.6419 from
  z = 1, 0.4388 from z = 2.2, and 0.4306 from z = 3.5 and from z = 5. It
  approaches the fold from above and does not reach it.

**v1.3** (results/summary.json, results/horizon_check.json), worlds with
a wrong incumbent out of 64, with no self-scoring (c = 0):

| selectivity s | 0 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|
| naive credit | 0 | 31 | 41 | 41 |
| exact inverse-propensity weighting | 0 | 0 | 0 | 5 |

- At s = 0.75 the raw cue mean is −0.193 and the mean of the admitted
  cues is +0.184. Selection has reversed the sign of the available
  evidence, as in [CASE-156](CASE-156.md).
- The 41 of 64 hold at 700, 1,400 and 2,800 updates. The corrected 5 of
  64 at s = 1 is 4 of 64 at 2,800. Admission probabilities near zero are
  where the correction's positivity condition fails.
- Self-scoring alone, c = 0.5 with s = 0, leaves 39 of 64 wrong. Nothing
  is censored there, so the correction changes nothing. At c = 0.25,
  s = 0.5 it takes 41 to 0, and at c = 0.5, s = 0.5 it takes 41 to 34.

**v1.1** (EXPERIMENT_REPORT.md). The lab's verify_v10.js reproduces all
48 MSE entries and 12 amendment counts of [CASE-158](CASE-158.md)'s table, so that table
is now reproduced, not only reported. Mean post-reversal MSE:

| evaluator | audits | router | governance |
|---|---|---|---|
| independent | full | 0.02237 | 0.02546 |
| independent | selective | 0.03284 | 0.03477 |
| 80% captured | full | 0.04480 | 0.06965 |
| 80% captured | selective | 0.04382 | 0.06984 |

The router has the lower error in all four cells. Under 80% capture
neither recovers on any seed. Under selective, independent audits
governance recovers on 7 of 12 seeds and the router on 4, with the worse
mean error.

## What it can show

- In two stipulated models, authority scored against what it made
  dominant can hold the worse perspective in place, which is [CLAIM-297](../claims.d/CLAIM-297.md)'s
  amplification without fidelity, and practice that depends on access
  makes it easier, which is [CLAIM-277](../claims.d/CLAIM-277.md)'s loop.
- That the fold and the trapping of a given history are different
  quantities, and the second depends on the history.
- That selection alone can lock in, that an evaluator who knows the
  admission probabilities can undo it while they stay positive, and that
  this correction does not undo self-scoring.
- That in [CASE-158](CASE-158.md)'s design with the router facing the same audit delay
  and cost, the router still wins.

## What it cannot show

- [CASE-092](CASE-092.md) analysed. Neither model has retrieval or a meaning state.
- A phase transition or a critical curve: these are grids and finite
  horizons.
- That the two realizations are one regime. Their mechanisms disagree,
  which counts against reading them as one ([CLAIM-286](../claims.d/CLAIM-286.md)).
- A procedure for unknown or zero propensities. The correction is an
  oracle.
- Any advantage of governance over routing, or anything about real
  organizations.

## Provenance

dmarx/PerspectiveLab@7e2edc2: experiments/regime_atlas/,
experiments/stochastic_population/ and experiments/capture_feedback/,
with their READMEs, stored results, and the handoffs RESEARCH_HANDOFF_V12.md
and RESEARCH_HANDOFF_V13.md. The figures above are read from the stored
results. When filed, the regime-atlas and stochastic-population test
suites were re-run at dmarx/PerspectiveLab@11c1495 and passed; the runs
themselves were not regenerated.
