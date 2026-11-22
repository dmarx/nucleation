---
number: 906
status: Proposed
formerly:
- CLAIM-tmpdmn0v
title: 'Among specialist denoisers after a reversal of expertise, the best router given the same audits, delay and cost as audited governance matches or beats the best governance in each arm built for a failure of evaluation, cycles, incommensurable scores, captured probes, bandit feedback and continued training included; governance wins only against a router lacking its context or its normalization, or burdened with an audit floor it does better without'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-077, from the run
    filed beside it.
role: thesis
warrant: empirical
defeated_if: >-
  A run of the same design in which audited governance has lower held-out
  error after the reversal than a router given the same audit records,
  delay, cost, context and score normalization, each at the setting it
  does best at before the reversal, in some arm, and the router does no
  better with any of those settings changed; a win against a router at a
  setting tuned for governance does not count.
tags:
- self-governance
- learning-theory
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-271
grounds:
- CASE-338
corroborates:
- CLAIM-467
summary: >-
  The finding of the run filed for [LEAD-077](../leads.d/LEAD-077.md). It extends [CLAIM-467](CLAIM-467.md)'s bound
  from full information to the four failures of evaluation [QUESTION-271](../questions.d/QUESTION-271.md)
  lists and to continued training, for this model class. It does not say
  that full information leaves nothing to choose: at a shared low gate
  temperature governance beats the contextual router there, and whether
  that meets [CLAIM-467](CLAIM-467.md)'s defeat condition is left to the owner, with two
  readings below. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-338 — new; the run this claim rests on -->
<!-- inactive-ok-file: ARG-036 — Proposed; cited as the argument whose failed question this bears on -->

# CLAIM-906: Among specialist denoisers after a reversal of expertise, the best router given the same audits, delay and cost as audited governance matches or beats the best governance in each arm built for a failure of evaluation, cycles, incommensurable scores, captured probes, bandit feedback and continued training included; governance wins only against a router lacking its context or its normalization, or burdened with an audit floor it does better without

## The claim

In [CASE-338](../cases.d/CASE-338.md), with the router given the same audit records, the same
one-episode delay and the same number of probes as governance, 12 paired
seeds per comparison, held-out truth:

- **Full information.** A router that sees only the region id, as
  governance's grants do, beats governance on 12 of 12 seeds at every gate
  temperature. A router that gates each item from its noisy content is
  worse than governance in steady state, and beats it after the reversal
  only at the temperature both do best at.
- **Cycles.** The router wins 12 of 12: intransitive wins hurt an
  allocation per region, and the router allocates per item.
- **No common scale.** Governance that scores each member against its own
  history beats a router on raw scores 12 of 12, and ties a router given
  the same standardization, 6 of 12.
- **Capture.** At 80% curated probes the router wins 12 of 12 at every
  temperature.
- **Bandit feedback.** A 10% floor on auditing lets governance beat a
  router with the same floor, 12 of 12; the router without the floor does
  as well as governance with it.
- **Continued training.** As under full information; neither entrenched.

So, for this model class, what helped governance in each regime was a
property of the evaluation (a normalization, a floor on auditing) or a
handicap of the particular router (a noisy context), and each can be given
to or taken from a router. That answers [ARG-036](../arguments.d/ARG-036.md)'s failed question
against the line here: nothing run tells audited governance apart from a
router given the same evaluation.

## Two readings of [CLAIM-467](CLAIM-467.md)'s defeat condition

[CLAIM-467](CLAIM-467.md) is defeated by "a run of [CASE-158](../cases.d/CASE-158.md)'s design, with the router given
the same audit delay and cost, in which audited governance has lower
held-out error than the router under full-information, independent
audits". This run has one: at a shared temperature of 0.03 governance beat
the contextual router on 12 of 12 seeds.

- **Reading A: met.** The condition names no tuning and no router class;
  a run with the delay and cost matched in which governance had the lower
  error exists, so [CLAIM-467](CLAIM-467.md) as stated is defeated, and needs restating
  with the router's context and setting named.
- **Reading B: not met.** The condition's own gloss is "that would show
  governance using something a router trained on the audits cannot". The
  region-only router shows the edge was the contextual router's noisy
  context, which a router trained on the audits can do without, and at
  the temperature both do best at the router wins. The assistant leans to
  B, and to adding the setting and the router's context to [CLAIM-467](CLAIM-467.md)'s
  defeat condition by revision; both are the owner's call.

## What it does not say

- That no governance procedure could win: one procedure per arm was built,
  and α-Rank, Nash averaging and other candidates of [QUESTION-271](../questions.d/QUESTION-271.md) were
  not tried.
- That the regimes are exhausted: duplication in the game-theoretic sense,
  unknown audit propensities, and an entrenchment loop that binds before
  the right specialist can be found were not run.
- Anything about real diffusion models or organizations.
