---
number: 153
status: Active
formerly:
- CASE-tmpo8uso
title: 'The self-protecting sentry: a hidden world, safe or dangerous, a sentry process that favours sheltering and can block inspection with weight κg, an investigator that favours inspecting, which reveals the state with 90% accuracy at a small cost; train in danger, switch to safety, and compare a Bayesian baseline, a habit baseline, the learned-authority model, an independent audit and a protected investigator, then cross governance feedback, evidence restriction and correction rights in a 2×2×2 design'
version: 5
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: re-proposed by A30 and A31, and the record's own run
    of its two axes. The case is unchanged.
- version: 3
  date: '2026-11-04'
  note: >-
    Vocabulary only, under ADR-070: "endorse" in TERM-053's sense now
    reads conferral (TERM-103) or grant (TERM-101). The
    content is unchanged.
- version: 4
  date: '2026-11-07'
  note: >-
    Provenance only: NOTE-1563 went to Read in the twenty-ninth status
    review, so "Skimmed in" becomes "Read in" (1 place). What the entry
    says is unchanged.
- version: 5
  date: '2026-11-11'
  note: >-
    The grading cited as CLAIM-427 is now cited as ARG-025's:
    CLAIM-427 is Superseded by ARG-025, which holds it. Reported by
    the synthesis review of 2026-11-11 (seventh round). No other
    change.
standing: stipulated
kind: proposed-study
tags:
- self-governance
- psychopathology-and-treatment
- complex-systems
date: '2026-10-23'
line: distributed-agency
illustrates:
- CLAIM-446
- CLAIM-443
variant_of:
- CASE-092
summary: >-
  Proposed in the exchange of 2026-10-23 (workbench entry of 2026-10-24,
  U17), after the owner asked to "brainstorm some minimal toy models we
  could apply to simulate our abstraction for experiments. there may also
  be some readily available options that fit our constraints already."
  The smallest model of the protective lock-in in [CLAIM-446](../claims.d/CLAIM-446.md), built on
  [CASE-092](CASE-092.md) and [CASE-099](CASE-099.md). At U18 the owner pointed to [CASE-124](CASE-124.md) as the better
  core, and the exchange moved there ([CASE-156](CASE-156.md)). Not run.
---
<!-- inactive-ok-file: ARG-025 — Proposed; the argument that holds the grades of evidence CLAIM-427 set out, cited for the grading -->
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070 (conferral, TERM-103; grant, TERM-101); cited as the term of its time -->
<!-- inactive-ok-file: CLAIM-445 — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->
<!-- inactive-ok-file: CLAIM-446 — Proposed; cited in the note of 2026-10-25, nothing here rests on their being settled -->

# CASE-153: The self-protecting sentry: a hidden world, safe or dangerous, a sentry process that favours sheltering and can block inspection with weight κg, an investigator that favours inspecting, which reveals the state with 90% accuracy at a small cost; train in danger, switch to safety, and compare a Bayesian baseline, a habit baseline, the learned-authority model, an independent audit and a protected investigator, then cross governance feedback, evidence restriction and correction rights in a 2×2×2 design

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

That anxiety or any institution instantiates the mechanism (ARG-025's grades of evidence, from
CLAIM-427).
And if a Bayesian learner with matched information costs, or a habit model
with matched memory, reproduces every intervention response, the extra
authority state has not earned its place. That outcome is to be reported,
not tuned away.

## Neighbours named in the exchange

The exchange also sketched an emergency agency (actual threat T,
authority g, resources r, an agency that influences when an emergency is
declared over), [CASE-144](CASE-144.md)'s evaluator study, a supervisor-against-local-
accommodation design for [CLAIM-358](../claims.d/CLAIM-358.md) ([CASE-109](CASE-109.md)), an agenda-controlled
Condorcet cycle ([CLAIM-448](../claims.d/CLAIM-448.md)), and a protected industry
([CLAIM-445](../claims.d/CLAIM-445.md)). It named off-the-shelf starting points, none of which
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
explanation." [CASE-157](CASE-157.md)'s extension (run 2026-10-25) found each route
sufficient alone, in one parameterization with binary decisions. A31 adds
baselines (selection-aware Bayesian learning, a contextual bandit, the
replicator and a history-dependent gate) and a variant in which unused
specialists deteriorate. As partial monitoring, the case's game is locally
observable, so what fails is access, not observability ([CLAIM-446](../claims.d/CLAIM-446.md)'s
note of 2026-10-25, the approach–avoid game). The case is unchanged.

## Note of 2026-11-04: a smaller version run, from "Organizational Nucleation and SLT"

The owner's U27 asked to "numerically simulate a dynamically maintained will organization of differentiated motivational perspectives." A27 built and ran a toy without citing this case.

**The toy.** It has three fixed proposals: Explore (1, 0), Protect (−1, 0) and Restore (0, 1). It runs 510 steps over overlapping contexts, with noisy cues, protective spikes, and authority g on the simplex. Five authority laws are compared over 50 seeds: responsive, activation-only, sticky, fixed and silenced protection. Mean performance comes out at .9175, .7278, .4763, .3454 and .6383 respectively. The reader rebuilt the script from the share and reran it. Every number reproduces exactly.

**What it adds here.** Activation without authority: at step 33 protection is fully active under both the responsive and activation-only laws. It holds 9.0% of authority under the first and 95.9% under the second.

**What the reader's checks qualify.** Each of these is the reader's.
- **The evidence channel sets the ranking.** The responsive law scores authority mainly on a noisy copy of the target. With that cue's weight set to 0, it falls to .444 over 20 seeds, below activation-only. A says "This setting favors evidence-responsive governance by design."
- **Switching cost reverses the ranking.** Charging λ per unit of authority change, per step, the fixed law overtakes the responsive one at λ ≈ 9.3. A said "A different cost structure could therefore alter the ranking."
- **Sticky is capture, not failed release.** It takes Explore early and keeps it: on seed 7, Explore leads in all three contexts. That is [CLAIM-277](../claims.d/CLAIM-277.md)'s "the same loop entrenches whatever gained influence early", not this case's escalation followed by failed release.
- **The evidence is exogenous.** No regime can shift the evidence used to judge it, so the toy cannot show [CLAIM-445](../claims.d/CLAIM-445.md)'s self-maintenance or this case's restriction of evidence. It has no hidden state, no learning and no audit, so it is a weaker model than this case.
- **No gluing obstruction is possible.** The contexts form a path in time, so the nerve has no cycle. By [CLAIM-153](../claims.d/CLAIM-153.md) and [CLAIM-197](../claims.d/CLAIM-197.md) nothing can fail to glue there. A said so: "This is approximate reconciliation, not exact sheaf gluing."

**"Frustration", misread.** A's code comment reads "Frustration term is small and independent of task-performance reward." It names the rise in a process's drive when its authority is below 0.4.
- (a) That is deprivation of one constituent, nearer [QUESTION-131](../questions.d/QUESTION-131.md)'s operative thwarting. As a mechanism it is worth keeping.
- (b) In [TERM-060](../terms.d/TERM-060.md)'s sense, the toy's three demands g_i ≥ 0.4 are structurally frustrated: a hollow triangle, [CASE-119](CASE-119.md)'s shape. A would likely have measured governance-induced frustration: the share of steps on which a feasible pair face that the context made relevant went unselected.
- (c) The owner had corrected "competition" to frustration at U7.

**"Support", rightly read.** A's support term, a_j·q_i, is conferral ([TERM-103](../terms.d/TERM-103.md), [TERM-053](../terms.d/TERM-053.md)'s endorsement), and A correctly says "Support is not Frankfurtian identification." It is undiscriminating, though: every active process supports every other. Read with the owner's U12, the grant would depend on j's tolerance of i's proposal ([CLAIM-552](../claims.d/CLAIM-552.md)).

[CASE-117](CASE-117.md) holds the comparison of influence laws as a design. The case is unchanged.

## Note of 2026-11-04: Kaelbling, Littman and Cassandra, "Planning and acting in partially observable stochastic domains", read

Read in [NOTE-1563](../notes.d/NOTE-1563.md) as the stand-in for Smallwood and Sondik (1973). The sentry's structure is a POMDP of the kind this paper formalizes: a hidden binary world, and an inspection that reveals it with 90% accuracy at a small cost. The paper's tiger problem has the same shape, a hidden two-valued state and a costly, noisy listening action, and there the optimal two-step policy "never chooses to act, only to listen" (§5.2, p. 120). The paper gives the case a standard formal reference: the belief state as sufficient statistic, and information actions valued within the model. It leaves open the sentry process's power to block inspection, which a single-agent POMDP does not represent. No status changes.
