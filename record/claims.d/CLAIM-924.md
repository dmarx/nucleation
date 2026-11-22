---
number: 924
status: Proposed
formerly:
- CLAIM-tmpqp1h6
title: 'In the simulated self-protecting sentry, authority rewarded by the apparent success of protection follows the same law as a habit of protecting, so a habit of matched memory reproduces its response to belief correction, to resetting authority and to restored evidence access, and only interventions on the evaluation, an independent audit or authority rewarded on independent evidence, tell the two apart; with them protection outlasts a corrected belief, restricting the evidence turns that inertia into self-confirmation, and neither an audit nor a protected investigator removes the interaction between success feedback and restriction'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-076, from the run
    in CASE-346 (scratch/studies/lead-076/).
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of the model as filed (scratch/studies/lead-076/) in which the
  matched habit and the success-rewarded authority part under belief
  correction, authority or habit reset, or restored evidence access, by
  more than seed noise; or in which the interaction between success
  feedback and evidence restriction on needless protection is not
  positive, or is removed by the audit or the protected investigator, at
  the filed parameters. A different model or parameterization that
  behaves otherwise narrows the claim; it does not defeat it, since the
  claim is about this model.
tags:
- self-governance
- psychopathology-and-treatment
- learning-and-conditioning
date: '2026-11-22'
line:
- distributed-agency
- will-organization
grounds:
- CASE-346
bears_on:
- QUESTION-131
summary: >-
  [CASE-153](../cases.d/CASE-153.md) set its own check: "if a Bayesian learner with matched
  information costs, or a habit model with matched memory, reproduces
  every intervention response, the extra authority state has not earned
  its place." Run in [CASE-346](../cases.d/CASE-346.md), the Bayesian with matched cost does not
  reproduce the responses. The habit reproduces every intervention it can
  receive, because under success feedback the authority update is the
  habit trace. What separates them is an evaluator that can be audited or
  made to reward on independent evidence, so the authority state earns its
  place only as far as its evaluation can be reached from outside. The
  claim also records the factorial's interaction and the regimes,
  including protection outlasting a corrected belief, and what this does
  to [CLAIM-446](CLAIM-446.md)'s, [CLAIM-443](CLAIM-443.md)'s and [CLAIM-445](CLAIM-445.md)'s defeaters. Two readings of
  the habit comparison are set out for the owner. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-445 CLAIM-446 ARG-025 CASE-346 CLAIM-923 — Proposed or new; the claims whose defeaters this bears on, the grading cited, the study this rests on and the constructions filed with it -->

# CLAIM-924: In the simulated self-protecting sentry, authority rewarded by the apparent success of protection follows the same law as a habit of protecting, so a habit of matched memory reproduces its response to belief correction, to resetting authority and to restored evidence access, and only interventions on the evaluation, an independent audit or authority rewarded on independent evidence, tell the two apart; with them protection outlasts a corrected belief, restricting the evidence turns that inertia into self-confirmation, and neither an audit nor a protected investigator removes the interaction between success feedback and restriction

## The claim

All figures are [CASE-346](../cases.d/CASE-346.md)'s: 1000 paired seeds, κ = 1.5, η = 0.02.

1. **The same law.** Under success feedback, F = 1 whenever the agent
   protects. So, apart from the rare steps on which the agent engages and
   is harmed, g ← (1 − η) g + η · 1[protect]. That is the habit trace of
   protecting. Run side by side they agree:

   | condition | governance | habit |
   |---|---|---|
   | no intervention | 0 % leave protection | 0 % |
   | belief corrected | 0 % | 0 % |
   | authority (habits) reset | 88 % | 88 % |
   | evidence access restored | 78 % | 78 % |
   | protected investigator | 4.5 %, outlasts 87 % | 4.5 %, outlasts 88 % |

   The governance model's own success-and-restricted row and the habit's
   are equal to the unit in needless cost (396).
2. **What tells them apart.** An independent audit reaching the evaluator
   lets 66 % of runs leave. Rewarding authority on the evaluator's belief
   instead of on success, 50 steps after the switch, lets every run leave
   (median 44 steps). Neither intervention has anything to act on in a
   habit. The Bayesian with inspection cost 0.3 differs from both: belief
   correction ends its protection at once.
3. **Inertia and self-confirmation.**
   - Without restriction, success feedback above the boundary leaves the
     belief corrected and protection on. That is [CLAIM-446](CLAIM-446.md)'s "the regime
     can outlast a corrected belief" (inertial).
   - With restriction, the belief itself is not corrected in 43 % of runs
     (self-confirming). Restriction adds 134 [132, 137] units of needless
     protection under success feedback and 35 [32, 38] under independent
     evaluation, an interaction of 99 [95, 103].
   - With an audit the interaction is 107 [104, 111]; with a protected
     investigator, 82 [80, 84]. Each correction right lowers the cost of
     the worst cell but removes neither the persistence nor the
     interaction.
   - Protection when danger returns is kept throughout.

## Two readings of the habit comparison, for the owner

[CLAIM-446](CLAIM-446.md)'s defeater includes "persistent avoidance that ... a habit model
with matched memory reproduces under every intervention the claim
distinguishes (belief correction, authority correction, evidence-access
correction, reinforcement correction)". [CLAIM-443](CLAIM-443.md)'s includes "a cached
action policy reproduces every response to intervention that the learned
authority prior predicts".

- **Reading A: not met.** The habit cannot receive reinforcement
  correction or an audit, so it does not reproduce "every intervention".
  The authority state earns its place in the model through exactly those
  two responses. The decisive pattern [CLAIM-446](CLAIM-446.md)'s test names appears: "a
  trained defense that keeps governing after belief correction and
  becomes revisable after a manipulation restoring independent evidence".
- **Reading B: met in substance.** A habit gated by the outcome, F = 1 on
  protection, is the success-rewarded authority. "Reinforcement
  correction" applied to that habit is the reinforcement made
  independent, and an audit is a change in what reinforces it. On this
  reading the extra state adds nothing in this model; what does the work
  is what the reinforcement signal is computed from, and whether
  something outside can reach it.

Which reading holds is a question about what [CLAIM-446](CLAIM-446.md) and [CLAIM-443](CLAIM-443.md) mean
by authority and by a habit. That is the owner's, and nothing here
changes their status.

## What it bears on

- **[CLAIM-445](CLAIM-445.md).** Within the model, a protective regime whose interventions
  shift the evidence used to judge it maintains itself (the
  success-and-restricted cell), and insulating the evaluation (an audit,
  or independent reinforcement) changes exit. So the model does not meet
  [CLAIM-445](CLAIM-445.md)'s second defeater, "an intervention that insulates the
  evaluation of necessity from the protective regime and leaves exit from
  protection unchanged". Restriction under independent evaluation
  maintains the regime only at a stronger sentry (κ ≥ 2.75), or when the
  agent assumes the world almost never changes (h = 0.002: a median 301
  steps).
- **[QUESTION-131](../questions.d/QUESTION-131.md).** The sentry and the investigator are jointly
  satisfiable (protect and inspect), and the sentry thwarts the
  investigator. This is [CLAIM-923](CLAIM-923.md)'s item 4 in motion.
- **[ARG-025](../arguments.d/ARG-025.md)'s grades.** A stipulated model; nothing about anxiety or
  institutions follows.

## What it does not say

- That the result holds outside the model or its region of parameters.
  The boundary sits near κ = 1.25–1.5, and the default κ = 1.5 is at its
  edge. The protected investigator's persistence falls from 96 % of runs
  not leaving at h = 0.02 to 0.5 % at h = 0.002.
- That any authority state is a habit. The equivalence is for feedback by
  apparent success. Under independent evaluation authority does not
  follow behaviour, and the models part.
