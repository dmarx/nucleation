---
number: 161
status: Proposed
formerly:
- CASE-tmpfmdj6
title: 'Reciprocally produced, externally reset and feedback-only governing rules in a 32-member population: with ordinary trajectories identical, reciprocal production repairs the loss of one rule and not of both and fails after producer outages of 36 updates for audit and 40 for admission, after an audit-rule pulse the next audit integrity is 1.00, 0.18 and 0.00 in the three arrangements, and a self-dependent production graph does not regenerate a zeroed rule'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed at the owner's direction from an owner-supplied package of
    proposed updates (its "Priority A", where it was numbered 163). Its
    numbers were checked against the stored results in
    dmarx/PerspectiveLab@7e2edc2 and found to agree; the wrong-incumbent
    counts and the 80-update outages were added from the v1.6 report.
standing: stipulated
kind: executed-study
tags:
- self-governance
- complex-systems
- causality
date: '2026-10-26'
line: distributed-agency
variant_of:
- CASE-126
illustrates:
- CLAIM-414
summary: >-
  Versions 1.6 and 1.7 of the Perspective Population Lab,
  dmarx/PerspectiveLab@7e2edc2. Two governing rules, the integrity of
  audit and of evidence admission, are kept up in three ways in the same
  32-member population. Ordinary operation cannot tell the three apart,
  and loss, repair and producer interventions do. It carries [CASE-126](CASE-126.md)'s
  second construction to a stochastic population with a different
  production law: here reciprocal production repairs a single loss, where
  the case's closed pair collapses.
variants:
- CASE-163
---

# CASE-161: Reciprocally produced, externally reset and feedback-only governing rules in a 32-member population: with ordinary trajectories identical, reciprocal production repairs the loss of one rule and not of both and fails after producer outages of 36 updates for audit and 40 for admission, after an audit-rule pulse the next audit integrity is 1.00, 0.18 and 0.00 in the three arrangements, and a self-dependent production graph does not regenerate a zeroed rule

## The case

The v1.3 population (32 networked perspectives, sampled cues, admission
that depends on the record, practice) gains two rules that change how
evidence is admitted and scored: audit integrity and admission
integrity (dmarx/PerspectiveLab@7e2edc2 experiments/maintained_population/).
They are kept up in one of three arrangements:

1. **External reset.** Something outside restores them.
2. **Reciprocal production.** Two fixed producer teams of members each
   produce one rule, each rule enabling production of the other. Audit
   decays fast and admission slowly (d_a = 0.18, d_b = 0.048).
3. **Feedback only.** Use-dependent feedback, with no producers.

A fourth graph, in which each rule enables its own production, is a
comparator. Every arm and intervention shares the same world and event
streams, keyed by seed. The lab's test requires the authority,
competence and rule trajectories of the three arrangements to be
identical when undisturbed.

## Results, as stored

**v1.6** (EXPERIMENT_REPORT_V16.md, results/), 48 seeds:

- One rule zeroed once: reciprocal production restores both in 48 of 48,
  external reset in 48 of 48, feedback only in 0 of 48.
- Both rules zeroed: reciprocal 0 of 48, external 48 of 48.
- A producer team disabled for 80 updates: reciprocal loses both rules in
  48 of 48. External and feedback-only are unaffected, since they do not
  depend on the producers.
- Outage length, 24 seeds: the audit team's outage is survived at 32
  updates and not at 36; the admission team's at 36 and not at 40. These
  are grid points under these laws, not a critical duration.
- Self-dependent production leaves the unperturbed trajectory unchanged
  and repairs a zeroed audit rule in 0 of 48.
- Losing a rule is not the same as wrong authority. After the 80-update
  admission outage both rules were lost in every reciprocal run, and 33
  of 48 populations still ended with authority on the better alternative.

**v1.7** (experiments/joint_closure/, EXPERIMENT_REPORT_V17.md). At the
intervention step all three arrangements have the same recorded
21-dimensional source state on every seed and history. After the same
audit pulse, which sets audit integrity to 0, the next audit integrity is
1.00 under external reset, 0.18 under reciprocal production and 0.00
under feedback only. At update 185, after the pulse, mean audit integrity
over 12 paired seeds is 1.0 external, about 1.0 reciprocal and 0.0
self-dependent.

## What it can show

That in one stipulated population, how a rule is maintained is invisible
in ordinary operation and decisive after damage, as [CLAIM-414](../claims.d/CLAIM-414.md) says of
its finite constructions; and that the separating interventions are the
ones A7 named for [QUESTION-086](../questions.d/QUESTION-086.md), damage to a rule and interruption of the
work that produces it. That which constraint produces which, at fixed
ordinary behaviour, decides what can be repaired. And, as [QUESTION-087](../questions.d/QUESTION-087.md)
warns, that internal maintenance can be the more fragile arrangement:
here it fails on double loss and on a producer outage, where outside
reset does not.

## What it cannot show

- That the population draws its own boundary. The producer teams,
  schedules and production law are assigned by the modeller, so
  "internal" means inside the simulated population by stipulation
  ([QUESTION-090](../questions.d/QUESTION-090.md) asks when a population develops such maintenance).
- Closure of constraints in [TERM-070](../terms.d/TERM-070.md)'s sense, agency or normativity.
- That reciprocal production guarantees repair. A total loss of the
  slowly rebuilt admission rule is not reliably repaired before audit
  decays (v2.1, dmarx/PerspectiveLab@9f82bfd
  experiments/diagnostic_identification/).

## Provenance

dmarx/PerspectiveLab@7e2edc2 experiments/maintained_population/ and
experiments/joint_closure/, with EXPERIMENT_REPORT_V16.md,
EXPERIMENT_REPORT_V17.md and their stored results (duration_scan.csv,
successor_witnesses.json, topology_ablation.json). When filed, the
maintained-population test suite was re-run at
dmarx/PerspectiveLab@11c1495 and passed.
