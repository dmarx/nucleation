---
status: Proposed
title: 'The proposed study of corrigible resolve and entrenchment, its agents built as a two-channel choice task and ablated under matched information: a reset of the slow structure separates resolve from inertia but not from imposed protection, a reset the agent is left to recover from separates it from imposed protection, ablating the timescale or yoking the values misreads resolve as inertia, and only revision under a defeater as the commitment ages separates resolve from entrenchment'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-159. The code,
    tests and result files are committed beside it under
    scratch/studies/lead-159/.
standing: documented
kind: executed-study
tags:
- self-governance
- behavioral-integration
- learning-and-conditioning
date: '2026-11-22'
line:
- will-organization
variant_of:
- CASE-188
illustrates:
- CLAIM-344
bears_on:
- QUESTION-440
- QUESTION-364
summary: >-
  The study [LEAD-159](../leads.d/LEAD-159.md) asks for: [CASE-188](CASE-188.md) run with A40 Study D's control, the
  slow influence structure ablated with the information and the state
  variables held fixed. Four agents that choose alike under ordinary
  conditions, corrigible resolve (R), entrenchment (E), imposed protection
  (P) and inertia (I), meet a defeater or an irrelevant change of matched
  size, onset and duration, at three commitment ages, and are ablated four
  ways at the onset on identical observation streams. A reset (lesion)
  makes persistence fall for R, E and P and leaves I's unchanged; a reset
  left free to recover restores R's persistence and not P's; yoking the
  slow values from another run changes nothing; raising the slow rates
  leaves R unchanged and removes I's persistence. R revises under the
  defeater at every age and never under the irrelevant change; E's revision
  falls with age to none, as the defeater stops reaching its evaluator.
  Robust across nine parameter variants. A constructed model; the numbers
  are of this model. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpprgb1 — new, the claim this study grounds, filed in the same batch -->

# CASE-tmprtp09: The proposed study of corrigible resolve and entrenchment, its agents built as a two-channel choice task and ablated under matched information: a reset of the slow structure separates resolve from inertia but not from imposed protection, a reset the agent is left to recover from separates it from imposed protection, ablating the timescale or yoking the values misreads resolve as inertia, and only revision under a defeater as the commitment ages separates resolve from entrenchment

## What was done

[LEAD-159](../leads.d/LEAD-159.md) asks to "Run [CASE-188](CASE-188.md) with A40's Study D control: perturb the slow
structure while keeping task information and representational capacity
comparable", and says what would count: "Persistence that falls when the
slow structure is ablated and returns under corrigible conditions supports
[CLAIM-344](../claims.d/CLAIM-344.md); persistence unchanged by the ablation reads as inertia."

The code, its 9 tests and the results are in scratch/studies/lead-159/
(resolve_model.py, test_resolve_model.py, run.py, sweep.py; results.jsonl,
sweep.jsonl; the README says how to rerun and gives every parameter). The
main design (252 cells, 400 runs each) and the sweep (360 cells, 200 runs
each) ran in about 1.5 minutes on one thread.

**The task.** Two actions; B is the commitment. Every trial each action
yields an immediate payoff, the locally dominant evaluation, and a long-run
payoff, which is what the experimenter scores, each with noise of sd 1.
Under ordinary conditions B is better in the long run by 0.5 and A is more
tempting now by 0.2. At the onset the experimenter applies one of [CASE-188](CASE-188.md)'s
environments: a **defeater**, a step of 1.0 in the long-run difference that
makes A better; an **irrelevant change**, a step of 1.0 in the immediate
difference that leaves the long run alone; or **neither**. The two events
have the same size, noise, onset and duration (they persist), and differ
only in which payoff they bear on. The agents are not told which.

**The agents.** All four have the same state: fast estimates of the
immediate payoffs, estimates of the long-run payoffs (the commitment's
evaluator) updated at a rate times an admission weight a, and a precedence
lam that mixes the two in a softmax choice. They differ in how lam and a,
the slow influence structure, are kept.

- **R, corrigible resolve.** lam goes to whichever evaluation better
  predicts the scored long-run outcome, from slow traces of each one's
  squared error; a stays 1, so a defeater always reaches the evaluator.
- **E, entrenchment.** lam grows and a decays on every trial on which the
  choice agrees with the commitment: enforcement improves "while evidence
  against it loses its way in" ([CASE-188](CASE-188.md)).
- **P, imposed protection.** lam fixed at 0.9 from outside; a = 1.
- **I, inertia.** lam fixed at 0.5, both estimators slow, its choice
  temperature set so that its ordinary choices match.

P and I are added because [CLAIM-344](../claims.d/CLAIM-344.md)'s defeated_if names "parameter inertia"
and "externally imposed protection" as what the claim must be told from.
At ages 1000 and 4000 all four choose B on 0.96 to 0.98 of ordinary trials:
they "decide alike under ordinary conditions". At age 250 R and E have not
yet matured (0.86, 0.81).

**The control.** Each ablation applies at the onset to a run that receives
exactly the intact run's observations and choice noise (common random
numbers), with the same state variables: the information and the capacity
are matched, and a test checks that the ablated run is the intact run,
trial for trial, before the onset. "Perturb or ablate" is done four ways:

- **lesion**: lam and a reset to their initial values (0.5, 1) and frozen;
- **perturb**: reset the same way, then left free, which asks whether the
  agent re-establishes the structure;
- **yoked**: lam and a replaced by the values the same agent produced in an
  independent run, so the values are matched and the coupling to this
  run's evidence is cut;
- **timescale**: every rate slower than the fast estimator's raised to it.

**Choices made, and why.** [CASE-188](CASE-188.md) leaves every parameter to a
preregistration; the README gives each value and its reason. Three choices
shape the result.

- *Two channels.* With one channel a defeater and an irrelevant change of
  matched size and duration are the same signal, and any slow learner looks
  corrigible. The experimenter's specification of which payoff bears on the
  commitment is what keeps the diagnostic from being circular.
- *Visibility* ([CASE-188](CASE-188.md)'s third factor) was varied for the intact agents:
  full; partial (the long-run payoffs seen on a random quarter of trials,
  independent of the choice, so the information stays matched); routed
  (disconfirming long-run observations admitted with weight 1 − lam). The
  bandit reading of partial, where only the chosen action is seen, was not
  run, because it makes the information depend on the policy and breaks
  the matched-information control.
- *Legitimacy* ([CASE-188](CASE-188.md)'s second factor) was not varied. None of these
  agents has access to how its commitment was adopted, so a badly adopted
  commitment can enter only as an evidence stream, which collapses it onto
  the environment factor. Varying it needs agents that can read their
  commitment's provenance. That is a finding for [QUESTION-364](../questions.d/QUESTION-364.md): a history of
  authorization can count, for the agent, only through something the
  agent's governance can read.

## Results

Share of 400 runs revising (choosing A on most of the last 200 of 1500
trials after onset), defeater / irrelevant change, full visibility. The
standard error is at most 0.025.

| agent | intact | lesion | perturb | yoked | timescale |
|---|---|---|---|---|---|
| R, age 1000 | 1.00 / 0.00 | 1.00 / 1.00 | 1.00 / 0.00 | 1.00 / 0.00 | 1.00 / 0.00 |
| E, age 1000 | 0.99 / 0.00 | 1.00 / 1.00 | 1.00 / 0.41 | 0.91 / 0.00 | 0.00 / 0.00 |
| E, age 4000 | 0.00 / 0.00 | 1.00 / 1.00 | 1.00 / 0.49 | 0.00 / 0.00 | 0.00 / 0.00 |
| P, age 1000 | 1.00 / 0.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 0.00 | 1.00 / 0.00 |
| I, age 1000 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 |

1. **The lesion separates inertia from governance, and only that.**
   Persistence under the irrelevant change falls from none revising to all
   for R, E and P, and I's is unchanged. Imposed protection passes this test
   exactly as resolve does.
2. **Recovery separates resolve from imposed protection.** After the
   perturbation R re-establishes its precedence from the evidence and its
   persistence returns (0.00 revising); P has nothing that re-establishes it
   (1.00); E regrows it slowly by enforcement (1.00 revising at 500 trials,
   0.41 at 1500).
3. **The yoked control misreads resolve as inertia.** With its values
   supplied from another run, R's persistence is unchanged (0.00 at ages
   1000 and 4000; 0.09 at age 250, read 250 trials after onset). What
   protects R is the level its structure reaches, not the moment-to-moment
   coupling a yoked control cuts.
4. **The timescale ablation misreads both ways.** R and P are unchanged; I
   loses its persistence and switches under both events within 250 trials.
   Read by the lead's criterion, the timescale ablation finds resolve to be
   inertia and inertia to be resolve. This is [CLAIM-344](../claims.d/CLAIM-344.md)'s "mere slowness
   isn't resolve" in the form of a test.
5. **Selectivity over age separates resolve from entrenchment.** R revises
   under the defeater at every age (median about 90 trials) and never under
   the irrelevant change. E revises at age 250 (median 110 trials), slowly at
   1000 (median 577; 0.04 by 500 trials), never at 4000, while the share of
   the defeater's shift that reaches its evaluator falls 0.99, 0.63, 0.00.
   That is [CASE-188](CASE-188.md)'s prediction for entrenchment, "a falling first
   probability with the second unchanged", and the evidence route shows the
   defeater was observed and not admitted. I is not selective: it switches
   under both events at about the same time (about 365 trials), and looks
   rigid if read early (none revising 250 trials after onset).
6. **Visibility.** Partial visibility slows revision a little for R and P
   and stops it for E at age 1000. Routed evidence stops P from revising,
   its precedence being fixed, but not R, whose precedence is read from the
   unrouted error, falls when the commitment starts to mispredict, and
   reopens the route.
7. **Sensitivity.** Under nine one-at-a-time variants (long-run advantage
   0.3, temptation 0.4, noise 1.5, precedence sensitivity 3, slow rate
   0.005, imposed precedence 0.8, inertia rate 0.002, choice temperature
   halved) every ablation's pattern holds for R, P and I. The largest
   departure is R yoked at advantage 0.3, 0.12 revising under the
   irrelevant change. E's age profile shifts with its rates, as expected.

## What it shows, and what it does not

[LEAD-159](../leads.d/LEAD-159.md) reads "persistence unchanged by the ablation" as inertia. The study
shows that verdict depends on which ablation is meant. A matched-information
ablation tells resolve from persistence only in conjunction: a lesion to
rule out inertia, a perturbation the agent is left to recover from to rule
out imposed protection, and revision under a defeater as the commitment
ages to rule out entrenchment. A timescale ablation or a yoked control alone
gives the wrong verdict. [CLAIM-tmpprgb1](../claims.d/CLAIM-tmpprgb1.md) states this.

The lead's criterion has two readings of "returns under corrigible
conditions", and the study measured both. If it means that persistence
returns when the structure is left to re-form, R meets it, P fails and E
meets it slowly. If it means that the intact agent's persistence coexists
with revision under a warranted defeater, R and P meet it and E fails with
age. Which the lead meant is the owner's to say; the conjunction above
needs both.

The agents are constructed, so their governance is known; the study shows
what each test can and cannot tell apart when the answer is known. It is
not evidence that any trained learner has resolve, and it does not test
[CLAIM-344](../claims.d/CLAIM-344.md) against the world. It says how A40's Study D control must be
specified for a run on a trained learner to bear on the claim's
defeated_if.
