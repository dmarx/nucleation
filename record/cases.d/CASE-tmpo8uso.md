---
status: Active
title: 'The self-protecting sentry: a hidden world, safe or dangerous, a sentry process that favours sheltering and can block inspection with weight κg, an investigator that favours inspecting, which reveals the state with 90% accuracy at a small cost; train in danger, switch to safety, and compare a Bayesian baseline, a habit baseline, the learned-authority model, an independent audit and a protected investigator, then cross governance feedback, evidence restriction and correction rights in a 2×2×2 design'
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: re-proposed by A30 and A31, and the record's own run
    of its two axes. The case is unchanged.
standing: stipulated
kind: proposed-study
tags:
- self-governance
- psychopathology-and-treatment
- complex-systems
date: '2026-10-23'
line: distributed-agency
illustrates:
- CLAIM-tmp8z857
- CLAIM-tmp0qupq
variant_of:
- CASE-092
summary: >-
  Proposed in the exchange of 2026-10-23 (workbench entry of 2026-10-24,
  U17), after the owner asked to "brainstorm some minimal toy models we
  could apply to simulate our abstraction for experiments. there may also
  be some readily available options that fit our constraints already."
  The smallest model of the protective lock-in in [CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md), built on
  [CASE-092](CASE-092.md) and [CASE-099](CASE-099.md). At U18 the owner pointed to [CASE-124](CASE-124.md) as the better
  core, and the exchange moved there ([CASE-tmpydmf8](CASE-tmpydmf8.md)). Not run.
---
<!-- inactive-ok-file: CLAIM-404 CLAIM-tmp8z857 — Proposed; cited in the note of 2026-10-25, nothing here rests on their being settled -->

# CASE-tmpo8uso: The self-protecting sentry: a hidden world, safe or dangerous, a sentry process that favours sheltering and can block inspection with weight κg, an investigator that favours inspecting, which reveals the state with 90% accuracy at a small cost; train in danger, switch to safety, and compare a Bayesian baseline, a habit baseline, the learned-authority model, an independent audit and a protected investigator, then cross governance feedback, evidence restriction and correction rights in a 2×2×2 design

## The case

**World.** A hidden state x_t ∈ {safe, dangerous} with known switching.
The experimenter sees it; the agent does not.

**Processes and actions.** A sentry that favours protection when danger is
anticipated, and an investigator that favours acquiring diagnostic
evidence. Two actions: shelter, which yields an uninformative observation,
and inspect, which reveals the state with 90% accuracy at a modest time
cost. Inspection is physically safe in the first version, so that a real
risk of injury does not confound the question.

**Dynamics.** b_t the probability of danger, g_t ∈ [0, 1] the sentry's
authority. P(inspect) = σ(βΔV_t − κg_t), with ΔV_t the current expected
advantage of inspecting, information value and cost included; the κg term
lets the sentry block inspection that is otherwise worth doing. Belief
updates on what is observed; authority updates more slowly,
g_{t+1} = (1 − η)g_t + η F(b_t, g_t, r_t, d_t), with r reinforcement of
protection and d corrective evidence. The manipulation that matters is
whether F rewards the sentry on independent evidence of danger or on its
apparent success under the policy it chose.

**First experiment.** Train in danger, then switch to safe.

| condition | authority | diagnostic evidence |
|---|---|---|
| Bayesian baseline | no separate authority state | by ordinary decision cost |
| habit baseline | persistence of the action policy | same opportunities |
| governance model | learned sentry authority | sentry can restrict inspection |
| independent audit | learned sentry authority | external evidence reaches the evaluator |
| protected investigator | learned sentry authority | investigator keeps some guaranteed access |

Measure time to recognize the change, how long protection outlasts
recognition, and the cumulative cost of needless protection. The result
to look for: a regime in which corrective evidence would suffice to change
the appraisal but the governance structure keeps it from becoming
consequential.

**Factorial version.** Governance feedback (authority fixed or
independently evaluated / reinforced by success under the dominant
regime) × evidence restriction (independent / limited by protective
authority) × correction rights (ordinary update / independent audit or
protected challenge): eight conditions, a matched habit model and a
Bayesian decision-maker, common seeds and event sequences. The tests are
interactions: whether authority feedback is especially persistent when it
also controls evidence, and whether independent correction removes that.
The system must still protect when danger is real.

**Measures shared with the other toys.** Calibration, diagnostic
sampling, authority concentration, authority–evidence responsiveness, exit
delay, hysteresis, regulatory cost, recovery of alternatives, task
performance, and cumulative avoidable loss against a policy with the same
admissible interventions. The diagnostic information available,
I(H; O | do(a)), is kept apart from the information sampled and from the
information granted influence.

## What it can show

Whether the stipulated coupling produces evidence-tracking, inertial,
self-confirming or revisable regimes, and where their boundaries lie (a
phase diagram), within the model.

## What it cannot show

That anxiety or any institution instantiates the mechanism ([CLAIM-427](../claims.d/CLAIM-427.md)).
And if a Bayesian learner with matched information costs, or a habit model
with matched memory, reproduces every intervention response, the extra
authority state has not earned its place. That outcome is to be reported,
not tuned away.

## Neighbours named in the exchange

The exchange also sketched an emergency agency (actual threat T,
authority g, resources r, an agency that influences when an emergency is
declared over), [CASE-144](CASE-144.md)'s evaluator study, a supervisor-against-local-
accommodation design for [CLAIM-358](../claims.d/CLAIM-358.md) ([CASE-109](CASE-109.md)), an agenda-controlled
Condorcet cycle ([CLAIM-tmpd6q2w](../claims.d/CLAIM-tmpd6q2w.md)), and a protected industry
([CLAIM-tmp28sti](../claims.d/CLAIM-tmp28sti.md)). It named off-the-shelf starting points, none of which
implements the abstraction: the Tiger POMDP in pomdp_py, pymdp for an
active-inference comparison, Mesa, NetLogo's Rebellion model (private
grievance against public behaviour under policing), PettingZoo and
Gymnasium's FrozenLake.

## Note of 2026-10-25: proposed again, and partly run

A30's two-specialist experiment and A31's Experiment 1 ("captured
evaluator"), in the exchange of 2026-10-24, continued, re-propose this case
without citing it. Each has a specialist better before an environmental
shift and the other after it, avoidance that yields the same feedback in
both states, and a 2×2 of evidence access (protected against selective) by
scoring (fixed against authority-dependent). The two axes are [CLAIM-404](../claims.d/CLAIM-404.md)'s
two routes, evidence received and criteria of weighing. A31's reading of
the outcome: "If guaranteed evidence access resolves lock-in, but changing
the evaluation criteria adds nothing, the result favors an exploration
explanation." [CASE-tmpffs67](CASE-tmpffs67.md)'s extension (run 2026-10-25) found each route
sufficient alone, in one parameterization with binary decisions. A31 adds
baselines (selection-aware Bayesian learning, a contextual bandit, the
replicator and a history-dependent gate) and a variant in which unused
specialists deteriorate. As partial monitoring, the case's game is locally
observable, so what fails is access, not observability ([CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md)'s
note of 2026-10-25, the approach–avoid game). The case is unchanged.
