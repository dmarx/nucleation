---
number: 316
status: Proposed
formerly:
- CASE-tmp8riid
title: 'Same oversight, the acting institution''s speed varied, in a queueing model run over twenty seeds: at ten times the speed the share of objectionable actions stopped before they became irreversible fell from 0.99 to 0.40, and to 0.04 when speed also multiplied the volume of actions; precommitted limits brought back about the share they foresaw and automatic suspension up to the share detected in time, each keeping most of the speed''s benefit, while pauses brought it back only by giving up the speed, and not at all when volume rose'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-068's simulation
    arm of CASE-285. The model, tests, results and a README are under
    scratch/studies/lead-068/.
standing: documented
kind: executed-study
tags:
- society-and-governance
- operations-research
- probabilistic-modeling
date: '2026-11-22'
line:
- distributed-agency
- dependence-and-domination
variant_of:
- CASE-285
illustrates:
- CLAIM-462
- CLAIM-710
- CLAIM-711
- CLAIM-730
bears_on:
- QUESTION-278
summary: >-
  [CASE-285](CASE-285.md) (A33 §10 C) proposed two arrangements whose overseer has the same
  authority and resources and whose acting institution differs only in how
  fast it can make actions irreversible, then precommitted limits,
  automatic suspension and pauses added in turn. [LEAD-068](../leads.d/LEAD-068.md) asked for it by
  simulation. The assistant built a queueing model: actions arrive, one in
  ten objectionable; the overseer detects each after a random delay,
  evaluates it with four reviewers first come first served, and an
  objection suspends; the time to irreversibility has mean 30 days divided
  by the speed factor. Over 20 seeds, at ten times the speed the share of
  objectionable actions stopped in time fell from 0.994 ± 0.003 to 0.396 ±
  0.019, gradually and from well before A23 §3's timing condition fails at
  the means; where speed also multiplied the volume of actions, it fell to
  0.043 ± 0.003. In the fast arm, limits brought back the share of the gap
  they covered (0.25 to 1.0) keeping 0.92 to 0.99 of the speed's benefit;
  suspension brought back at most 0.54, the share detected before
  irreversibility, keeping 0.91 to 0.99; pauses brought back 0.49 for a
  loss of a third of the benefit and all of it only by giving up all
  the benefit, and under the volume reading nothing at all. The model and its rates are the
  assistant's and invented, so it shows what holds in the model, not in
  any institution. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-285 CASE-280 CLAIM-710 CLAIM-711 CLAIM-730 CLAIM-706 TERM-125 — Proposed; the design this study carries out and the entries it bears on -->

# CASE-316: Same oversight, the acting institution's speed varied, in a queueing model run over twenty seeds: at ten times the speed the share of objectionable actions stopped before they became irreversible fell from 0.99 to 0.40, and to 0.04 when speed also multiplied the volume of actions; precommitted limits brought back about the share they foresaw and automatic suspension up to the share detected in time, each keeping most of the speed's benefit, while pauses brought it back only by giving up the speed, and not at all when volume rose

## The study

[CASE-285](CASE-285.md) is the design, from A33 §10 C of the exchange "Assess Depp Heard
Abuse": "Construct two arrangements in which the overseer has identical
authority and resources. Vary only the speed of the acting institution,
with corresponding deadlines for preventing irreversible consequences.
Then introduce precommitted constraints, automatic suspension, or
temporary pauses". [LEAD-068](../leads.d/LEAD-068.md) asked for it by simulation or matched
historical pairs; this is the simulation arm. The historical arm is not
attempted.

**The model.** Time in days. The acting institution initiates actions at
2 a day. One in ten is objectionable: the overseer, once it has evaluated
one, redirects it. Each action becomes irreversible a time T after
initiation, gamma with shape 4 and mean 30 / s days, where s is the speed
factor: slow arm s = 1, fast arm s = 10.

**Held fixed** at every speed, [CASE-285](CASE-285.md)'s authority, information,
resources, objection channel and policy:

- authority: an objection the overseer issues suspends the action in both
  arms, taking effect 0.25 days after evaluation ([CASE-003](CASE-003.md)'s Northstar-A
  rule, in both arms);
- information: the overseer notices each action after an exponential
  delay, mean 2 days, and evaluates correctly;
- resources: four reviewers, evaluation time gamma with mean 1.5 days,
  first come first served; an action already irreversible when a reviewer
  comes free is skipped.

**The fast arm's variants**, added one at a time:

- *precommitted limits*: checked at initiation; an objectionable action
  falls outside them with probability q (their coverage, what they
  foresee), a benign one with probability fp; an action outside them is
  held at once, clock stopped, and escalated into the same queue;
- *automatic suspension*: at detection an objectionable action is flagged
  with probability h, a benign one with probability fa; a flagged action
  detected before it is irreversible is suspended at once;
- *pauses*: every action waits P days before its clock starts.

**Measures**, A23 §10's three as [CASE-285](CASE-285.md) names them. *Intervention
capacity*: the share of objectionable actions suspended or redirected
before irreversibility. *The fast arm's benefit*: per benign action,
exp(−delay / 5 days), reported as the share of the slow-to-fast gain kept.
*Friction distribution*, per party: the actor's delay (initiating);
reviewer load and reviews per interception (challenging); objectionable
actions that become irreversible per thousand, open only to correction
after the fact (correcting).

**Choices the design left open**, stated before the run and kept:

1. *What speed is.* Two readings are run and reported apart. In the
   *latency* reading s shortens T and the rate of actions is unchanged:
   [CASE-285](CASE-285.md)'s "how fast the acting institution can make its actions
   irreversible", the reading closer to its text. In the *throughput*
   reading s also multiplies the rate of actions, A33 §4's agency that
   "has accelerated one timescale without proportionately increasing
   another's capacity". The record does not say which [CASE-285](CASE-285.md) means;
   both are reported, and neither is chosen.
2. Escalations and suspensions share the reviewers with ordinary review,
   without priority.
3. Limits and suspension act with no lag; an issued objection takes 0.25
   days.
4. Benefit depends on delay alone.

20 seeds per configuration, shared across arms. The whole study runs in
about a minute; `test_model.py` checks the queue, the timing condition,
the no-queue limit against an independent estimate of the race
probability, and the variants' identities (11 tests, all pass).

## Results

Mean ± sd across 20 seeds. Full tables are in
`scratch/studies/lead-068/results.md`.

**Speed alone** (latency reading). Intervention capacity by speed factor:

| s | 1 | 2 | 3 | 5 | 7 | 10 | 15 | 30 |
|---|---|---|---|---|---|---|---|---|
| capacity | 0.994 ± 0.003 | 0.951 ± 0.008 | 0.876 ± 0.011 | 0.711 ± 0.019 | 0.566 ± 0.014 | 0.396 ± 0.019 | 0.223 ± 0.017 | 0.051 ± 0.007 |
| benefit | 0.025 | 0.107 | 0.198 | 0.350 | 0.460 | 0.572 | 0.683 | 0.823 |

A23 §3's condition, detection plus evaluation plus intervention within
the time before harm, read deterministically at the means (2 + 1.5 + 0.25
days against 30 / s), predicts full capacity up to s = 7 and none from
s = 10. The fall is graded instead and begins early: at s = 5, where the
condition holds at the means, a quarter of the objectionable actions
already pass. Reviewer load fell with speed (0.75 to 0.53 at s = 10),
because the overseer skips what is already beyond stopping: speed lost
oversight its effect while leaving it less busy. Objectionable actions
irreversible per thousand rose from 0.6 to 60.8.

**Speed with volume** (throughput reading). The overseer saturates at
once: capacity 0.826 ± 0.024 at s = 1.5, 0.571 at 2, 0.043 ± 0.003 at 10,
with reviewers busy all the time. A23 §3's "ceremonial oversight", in the
model.

**Robustness.** Across ten other settings of the fixed oversight (faster
or slower detection, two or eight reviewers, faster evaluation, longer
lag, wider or narrower spread of T, three times as many objectionable
actions), the fast arm's capacity was 0.22 to 0.59 against the slow arm's
0.62 to 1.00, lower in every setting.

**The variants in the fast arm** (latency reading; gap restored is the
share of the slow-fast difference in capacity won back, benefit kept the
share of the fast arm's gain retained):

| variant | gap restored | benefit kept |
|---|---|---|
| limits, coverage q = 0.25 / 0.5 / 0.75 / 0.9 / 1.0, fp = 0.02 | 0.25 / 0.50 / 0.76 / 0.91 / 1.01 | 0.99 |
| the same, fp = 0.10 | the same | 0.97 |
| the same, fp = 0.30 | the same, within 0.01 | 0.92 |
| suspension, h = 0.5 / 0.8 / 0.95 / 1.0, fa = 0.05 | 0.27 / 0.44 / 0.51 / 0.54 | 0.99 |
| the same, fa = 0.20 / 0.50 | the same, within 0.01 | 0.96 / 0.91 |
| pause P = 0.5 / 1 / 2 / 4 / 8 / 16 days | 0.14 / 0.26 / 0.49 / 0.78 / 0.97 / 1.01 | 0.90 / 0.81 / 0.65 / 0.42 / 0.16 / 0.00 |

Sds of these ratios are 0.03 or less. Limits restore their coverage, q,
whatever their false positives cost. Suspension is capped at the share of
objectionable actions detected before they are irreversible (0.720 at
s = 10, so 0.54 of the gap): it needs the overseer to see in time, where
limits need it to have foreseen. A pause restores capacity only as it
gives back speed: to restore half the gap it gave up a third of the
benefit, to restore it all, all of it.

**The variants under the volume reading.** Pauses restored nothing at any
length (gap restored 0.00 from P = 0.5 to 27), since a fixed review
capacity saturated by volume is still saturated when every action waits.
Limits and suspension still restored about q and up to 0.71, because
what they hold needs no detection race; but their false positives now
land on a saturated queue. With fp = 0.10 and q ≥ 0.5, review load
exceeded capacity (1.05 to 1.42) and held benign actions waited 12 to 82
days on average, a backlog that grows with the length of the run; with
fp = 0.30, two to three times capacity and waits near 700 to 990 days.
Escalation that is cheap when the overseer has slack becomes the
bottleneck when it has none.

## What it can show

That the design's prediction holds in a working model, with its shape.
With the overseer's authority, information and resources held fixed by
construction, speed alone lowered the overseer's effect on what happens:
[CLAIM-462](../claims.d/CLAIM-462.md)'s separation of the capacity to act from the capacity to be
corrected, here by timing alone, and the lead's "Oversight that loses
effect as speed rises, with authority and resources fixed", for [CLAIM-710](../claims.d/CLAIM-710.md)
and [CLAIM-464](../claims.d/CLAIM-464.md), in stipulated form. Past the design's prediction, three
things the deterministic timing condition does not give: the loss is
graded and starts before the condition fails at the means; where speed
also raises volume, oversight fails sooner and pauses become useless;
and the three remedies differ in what they need, limits foresight,
suspension timely detection, pauses the speed itself.

[CASE-285](CASE-285.md): "If precommitted limits restore it without pauses, [CLAIM-730](../claims.d/CLAIM-730.md)'s
second clause is supported over its first." In the model they do, in
exact proportion to what they cover, and with little cost in delay where
their false positives are few. That is the possibility [CLAIM-730](../claims.d/CLAIM-730.md)'s second
clause and [CLAIM-711](../claims.d/CLAIM-711.md) state, made explicit as a dependence on coverage:
outside what the limits foresaw, nothing is won back. [CLAIM-711](../claims.d/CLAIM-711.md)'s own
defeater names that dependence ("interruptibility is kept only for the
transitions foreseen when the limit was set"); the model cannot say how
much real limits foresee.

## What it cannot show

- Anything about a real executive, agency or AI system. The rates, the
  shares and the benefit function are invented. A23 §3's timing condition
  is built into the model, so that speed lowers capacity follows from the
  construction; what the runs add is how much, how early, and how the
  remedies compare.
- [CLAIM-730](../claims.d/CLAIM-730.md)'s first clause. The model has no affected party and never
  revises a limit, so the domination of the harmed by a slow rule they
  cannot reach is not modelled, and the support for the second clause is
  not support "over" the first in any sense but this one.
- Whether a precommitted limit is friction. It holds the actions it
  catches and lets the rest pass undelayed; whether that is a gate
  without impedance ([CLAIM-706](../claims.d/CLAIM-706.md)) or friction relocated ([CLAIM-711](../claims.d/CLAIM-711.md)'s
  defeater) is [TERM-125](../terms.d/TERM-125.md)'s open question, which the model leaves open.
- Intent to outrun review, which [CLAIM-464](../claims.d/CLAIM-464.md) leaves aside.
- The historical arm of [LEAD-068](../leads.d/LEAD-068.md), which is not attempted.

[CASE-280](CASE-280.md) varies endogenous foreclosure at a fixed speed and is distinct.

## Note of 2026-11-25: the timing of defeated standing, modelled, from the manuscript governance-of-becoming, Article 8
<!-- inactive-ok-file: CLAIM-879 CLAIM-723 — Proposed; the executed study, its finding and the held form of the wrong, cited with their standing -->

The manuscript's Article 8 (§8.4.2, join J8.3) links two entries that do
not cite each other. CASE-316 (Proposed, executed study; CLAIM-879 states
its finding) is a queueing model in which an overseer with "the same
authority, information and reviewers at every speed" can suspend an act
until it becomes irreversible. What it counts, the share of objectionable
actions made irreversible before an objection can take effect (0.994
stopped in time at the base speed, 0.396 at ten times, 0.043 with volume
multiplied as well), is how often CLAIM-723's second condition, "the act
made that standing ineffective before it could be exercised", is met, for
objectionable actions only, by timing alone.

It measures the occasion of CLAIM-723's wrong, not the wrong. The model
has no affected party (the standing is the overseer's power to suspend),
does not count objections that would have failed, which are the case
CLAIM-723 is distinctive for, and models neither attribution to the
actor's timing or control over execution (condition three; CASE-316
lists among what it cannot show "Intent to outrun review") nor justification (condition
four). So it says how often the occasion arises as speed rises, and which
remedies (precommitted limits, automatic suspension) win it back, under
invented rates. A dated note, not a claim: the link adds no inference
beyond the two entries. No change of status. The wording is the
assistant's (Claude, in this session).
