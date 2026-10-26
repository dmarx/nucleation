---
status: Proposed
title: 'Identifying how governing rules are maintained from diagnostic probes: a predictor fitted under reciprocal production fails under self-dependent production with histories matched, an audit pulse with a short producer interruption identifies which of four known mechanisms applies and predicts withheld interventions, and fitting decay and threshold as well helps after the parameters shift and hurts at nominal ones, within a known catalog and with every probe run on a counterfactual reset'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed at the owner's direction from an owner-supplied package of
    proposed updates (its "Priority A", where it was numbered 164). Its
    numbers were checked against the stored results in
    dmarx/PerspectiveLab@9f82bfd and found to agree. Two descriptions
    were made exact: v2.2's audit probe lowers audit integrity to 0.46 and
    is not a complete pulse, and its reported scores are those of one
    three-probe policy among eight.
standing: stipulated
kind: executed-study
tags:
- causality
- probabilistic-modeling
- self-governance
date: '2026-10-26'
line: distributed-agency
variant_of:
- CASE-tmpfmdj6
illustrates:
- CLAIM-414
summary: >-
  Versions 2.0 to 2.2 of the Perspective Population Lab,
  dmarx/PerspectiveLab@9f82bfd, on the maintained population of
  [CASE-tmpfmdj6](CASE-tmpfmdj6.md). v2.0 shows that a response model does not transport across
  a change of production law that ordinary histories do not reveal. v2.1
  and v2.2 infer the mechanism, and then its parameters, from probes, and
  predict interventions never probed. Everything is relative to a catalog
  of four known mechanisms whose equations the forecaster is given, and
  every probe is a separate branch from the same starting state.
---
<!-- inactive-ok-file: CASE-tmpfmdj6 — Proposed; the case this one varies, filed with it -->
<!-- inactive-ok-file: CLAIM-427 CLAIM-278 QUESTION-031 — Proposed or Open; the grades of evidence, the objection and the question on probes this case bears on, nothing here rests on them -->

# CASE-tmpw6jjd: Identifying how governing rules are maintained from diagnostic probes: a predictor fitted under reciprocal production fails under self-dependent production with histories matched, an audit pulse with a short producer interruption identifies which of four known mechanisms applies and predicts withheld interventions, and fitting decay and threshold as well helps after the parameters shift and hurts at nominal ones, within a known catalog and with every probe run on a counterfactual reset

## The case

The 32-member population of [CASE-tmpfmdj6](CASE-tmpfmdj6.md), with its two governing rules,
under four candidate mechanisms: external reset, reciprocal production,
self-dependent production and feedback without production. All four are
alike in ordinary operation.

- **v2.0, transport** (experiments/transport_shifts/). Response models
  are fitted on a reference family (30 seeds, 10 held out) and frozen,
  then tested under graph, evidence and production-law shifts.
- **v2.1, diagnosis** (experiments/diagnostic_identification/). Probes
  after update 45 return noisy readouts of both integrities (SD 0.02, 12
  repeats). A posterior over the four mechanisms, calibrated on 24 source
  seeds, predicts three interventions not used in calibration: complete
  loss of the admission rule, loss of both rules, and an 80-update audit
  producer outage.
- **v2.2, mechanism and parameters** (experiments/joint_parameter_id/).
  252 hypotheses: a 5 × 5 × 5 grid of audit decay, admission decay and
  production threshold for each production mechanism, plus external
  reset and feedback only, with prior mass 1/4 on each class. The
  reported policy probes three times: audit integrity lowered to 0.46,
  and each producer team stopped for 3 updates, read at 1, 2, 4, 7 and 11
  updates. Four interventions are held out: admission loss, double loss,
  and 80-update outages of each team. 16 seeds per family, two
  histories, eight noisy readouts.

## Results, as stored

**v2.0** (EXPERIMENT_REPORT_V20.md). With pre-shock histories matched
exactly, the source-fitted model predicts mean audit integrity 0.97055
twenty updates after an audit pulse, under both reciprocal production
(actual 0.97093) and self-dependent production (actual 0.00000). The
frozen model's audit MSE is 1.55 × 10⁻⁶ on the reference family and
0.0785 under self-dependent production; refitting on that family brings
it to 3.9 × 10⁻⁷. Under graph-only and evidence-only shifts it stays near
10⁻⁶.

**v2.1** (EXPERIMENT_REPORT_V21.md), reference family:

| probe | class accuracy | MSE on withheld interventions |
|---|---|---|
| none | 25.0% | 0.150568 |
| mild audit pulse, to 0.8 | 82.6% | 0.015805 |
| complete audit pulse, to 0 | 75.0% | 0.020127 |
| two-update producer outage | 63.0% | 0.072722 |
| mild pulse and short outage | 90.4% | 0.008446 |
| complete pulse and short outage | 100.0% | 0.0000737 |

The complete pulse alone is less informative than the mild one, because
self-dependent production and feedback only respond alike once audit is
zero; the outage separates them. With labels scrambled, accuracy is
about 26% and MSE about 0.29. Under shifts of graph or evidence the
strong pair keeps 100% and MSE near 0.00007. Under faster decay or a
higher threshold it keeps 100% and MSE rises to 0.0037 and 0.0029:
knowing the class is not enough.

**v2.2** (EXPERIMENT_REPORT_V22.md, results/summary_scores.csv), class
accuracy 100% in every family:

| family | class only | class and parameters |
|---|---|---|
| reference | 0.000065 | 0.002068 |
| decay and threshold shifted | 0.009081 | 0.001071 |
| threshold 0.82, outside the grid's 0.64 | 0.004458 | 0.000402 |

The nominal values (0.18, 0.048, 0.44) are not all grid points, which is
one reason fitting parameters hurts at nominal values. In the
out-of-grid family the prediction improves although the fitted
threshold must be wrong. For self-dependent production at nominal
values, the audit pulse alone gives a local observation Jacobian of rank
2 for the three parameters, and the three-probe design rank 3. The
budget is a prior-predictive mean integrity deficit plus 0.03 per update
a team is stopped, a cost proxy and not a safety bound.

## What it can show

- For a fixed candidate family, a probe family d settles the response to
  a target intervention a exactly when any two candidates with the same
  law under d have the same law under a. That is the ordinary
  factorization condition. Here a complete audit pulse alone fails it:
  self-dependent production and feedback only respond alike to the
  pulse and not to the withheld interventions. Adding a short producer
  outage separates them within the catalog.
- That mechanism class and parameter values are separate verdicts, and
  so are prediction and parameter recovery.
- That information and damage are not monotone in a probe.

## What it cannot show

- Discovery. The four mechanisms and their equations are given, and so
  are the intervention semantics. A posterior over a known catalog is
  not identification of an unknown law.
- Probes on one system. Each probe resets to the same population, so
  this is a counterfactual sandbox, not sequential probing of an
  organization that carries its state.
- Global identifiability: the ranks are local.
- Grade three of [CLAIM-427](../claims.d/CLAIM-427.md). No rival was given the same knowledge of the
  generator, so this bears on [CLAIM-278](../claims.d/CLAIM-278.md) only as a design to beat.

## Provenance

dmarx/PerspectiveLab@9f82bfd experiments/transport_shifts/,
experiments/diagnostic_identification/ and experiments/joint_parameter_id/,
with EXPERIMENT_REPORT_V20.md to EXPERIMENT_REPORT_V22.md and their
stored results (probe_posteriors.json, summary_scores.csv,
local_identifiability.json, paired_seed_bootstrap.csv). When filed, the
joint-parameter test suite was re-run at dmarx/PerspectiveLab@11c1495
and passed.
