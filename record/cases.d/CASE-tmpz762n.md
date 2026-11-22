---
status: Proposed
title: 'A simulated ladder on one sensor channel and a forager that learns its own warning signs: a fail-safe relay acts on an absence and keeps nothing, a tester registers a silent fault and cannot place it, a four-probe diagnoser places it, and only a diagnoser that reviews its record of real fires finds a fault that appears in heat; the forager needs to revise which features count only when the warning sign is a feature it never attended to, and loses its gains when its energy account is replaced by a matched score'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-177 as a delegated
    lead worker. The code, its tests and the results are committed under
    scratch/studies/lead-177/.
standing: documented
kind: executed-study
tags:
- control-theory
- learning-and-conditioning
- philosophy-of-biology
date: '2026-11-22'
line:
- distributed-agency
- organizational-normativity
- record-as-apparatus
variant_of:
- CASE-239
- CASE-238
- CASE-240
- CASE-242
draws_on:
- THEORY-220
- THEORY-1646
illustrates:
- CLAIM-651
bears_on:
- QUESTION-285
- QUESTION-128
summary: >-
  [LEAD-177](../leads.d/LEAD-177.md) asked for [CASE-239](CASE-239.md)'s forager to be built, with its smaller
  relatives ([CASE-238](CASE-238.md), [CASE-240](CASE-240.md), [CASE-242](CASE-242.md)) adding one feature each, so that
  the systems share their sensory correlations and differ in memory, use and
  revision. Built in numpy (scratch/studies/lead-177/). In one alarm world,
  four rungs read the same sensor channel (identical mutual information with
  smoke before any fault, in every seed): the fail-safe relay puts out every
  fire under a sensor or relay fault by flooding and registers nothing; the
  tester registers every component fault and names none; the diagnoser names
  it at the first try in 91 or 92 of 100 runs; a fault that appears only in
  heat escapes all three, and a fourth rung that reviews its record of real
  fires adds a test in heat (94 of 100 runs) and names the relay (93). In
  [CASE-239](CASE-239.md)'s forager, over 40 seeds and two learning rules, a delayed cost on
  a feature never attended to kills the arm that may not revise which
  features count in most seeds (survival 13 and 24 of 40) and not the learner
  (40 and 38), while a delayed cost on an attended feature is met by
  re-estimating (35 and 31 of 40 for both); a silent patch is met by
  registering the absence, by every arm. Replacing the energy account with a
  score equal to it in training removes the learner's survival under delayed
  costs (0 of 40). Much follows from the rules; what the run adds is that they
  compose as stated. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-238 CASE-239 CASE-240 CASE-241 CASE-242 CLAIM-649 CLAIM-651 THEORY-220 THEORY-1646 CLAIM-tmp974nn — Proposed; the cases this run builds and the claims and readings it bears on, cited with their standing -->
<!-- inactive-ok-file: CLAIM-tmppa4rs CLAIM-tmpnc1mf CLAIM-tmphrp1s CASE-tmp33vf4 — new; the claims filed from this run and the companion run of the top rung -->

# CASE-tmpz762n: A simulated ladder on one sensor channel and a forager that learns its own warning signs: a fail-safe relay acts on an absence and keeps nothing, a tester registers a silent fault and cannot place it, a four-probe diagnoser places it, and only a diagnoser that reviews its record of real fires finds a fault that appears in heat; the forager needs to revise which features count only when the warning sign is a feature it never attended to, and loses its gains when its energy account is replaced by a matched score

## What was done

[LEAD-177](../leads.d/LEAD-177.md) asks for "systems with identical sensory correlations but different
memory persistence, downstream use and adaptive capacity" ([QUESTION-285](../questions.d/QUESTION-285.md),
answer 2), starting with [CASE-239](CASE-239.md)'s forager, with [CASE-238](CASE-238.md), [CASE-240](CASE-240.md) and
[CASE-242](CASE-242.md) as the lower rungs. Two constructions were built and run; the top
rung, a sensor network revising its correspondences, is [CASE-tmp33vf4](CASE-tmp33vf4.md).
Code, tests (18, passing) and per-run results: scratch/studies/lead-177/
(`ladder.py`, `forager.py`, `results/ladder_summary.md`,
`results/forager_summary.md`).

### The alarm world: four rungs on one channel

[CASE-242](CASE-242.md)'s chain (injector, sensor, relay, actuator), one fault per episode
of 6,000 steps from step 500, fires at random, the ambient hot in daytime
blocks, two irrelevant ambient features (humid, weekend), 2% readout error on
every test and probe; 100 seeds per cell. Every rung reads the same passive
sensor channel. Before the fault its mutual information with smoke is
identical across the rungs in every seed and fault (0 to 0.26 bits by seed).

| rung | what it adds | kept |
|---|---|---|
| R0 relay ([CASE-238](CASE-238.md)) | the sensor's all-clear current holds the valve shut; a spring opens it | nothing |
| R1 tester ([CASE-240](CASE-240.md)) | a test at night, an expected response, a retest on silence, a flag; switches to a backup chain | an interval, an expectation, a flag |
| R2 diagnoser ([CASE-242](CASE-242.md)) | on a flag, four probes and a likelihood match to the catalog; replaces the part named | a catalog |
| R3 reviser | a record of real fires with their ambient features; when failures concentrate on a value (Fisher exact, p < 0.01, at least three) it adds a test under that condition | a history; its test schedule revisable |

| fault | R0 | R1 | R2 | R3 |
|---|---|---|---|---|
| sensor or relay | every fire put out, the valve open on 5,402 fire-free steps of 6,000 (117 with no fault); nothing registered | registered 100/100, named none; 98% of fires put out (on the backup) | named at the first try 91/100 and 92/100, 95 steps after the fault | as R2 |
| actuator | no fire put out | as above | named 92/100 | as R2 |
| relay fails only in heat | every fire put out, by opening in every hot block | 81 of 891 fires in heat put out; 2/100 registered, both false | 77 of 891; nothing named | hot test added 94/100, relay named 93/100 (median 3,060 steps after the fault); 429 of 891 put out |
| none | | false registration 2/100 | no part named | no condition added |

Without the retest, the single test at 2% error registered a fault falsely in
68 of 100 fault-free runs; [CASE-242](CASE-242.md)'s likelihood ratio of 49 is evidence,
not entailment ([CLAIM-649](../claims.d/CLAIM-649.md)), and the retest is [CASE-240](CASE-240.md)'s "additional
interventions". R3 added no condition in any other fault.

### The forager ([CASE-239](CASE-239.md))

A forager with energy E (start 100, store 500) pays upkeep 1 a step and
dissolves at E ≤ 0. One patch a step, five binary features; skip, probe (0.3
for one sample of the first step's yield) or enter for up to ten steps,
leaving on a registered failure. Yield 1.5 + red + warm − 1.5·neighbour,
noise 0.3; the other two features are irrelevant. At step 1,500 one change
nobody trained for: **delayed**, red patches now raise upkeep by 2 for 15
steps after a visit; **new feature**, the same delayed cost on a feature that
was irrelevant until then; **silent**, patches with a fifth feature give no
yield. 4,000 steps; 40 seeds; common random numbers.

The learner predicts the net energy of a visit over its next 20 steps,
including its share of upkeep above its resting rate, from the features it
attends to. It starts attending to none, adds a feature when its residuals
differ by that feature (|z| > 4), sets its failure threshold from its own
residuals, and probes while recent visits fail. It skips a patch it predicts
a loss on. Two learning rules: recursive least squares with forgetting, and a
forgetting table over the attended features. Arms: the learner; [CASE-239](CASE-239.md)'s
arm 5, frozen from the change in its features, threshold and probe policy; a
features-only freeze (added here, to split arm 5); [CASE-241](CASE-241.md)'s self-set and
designer's profiles; the oracle, told the true value after the change; and
two replacements of the learner's target, a score equal to the energy account
in training (immediate intake, no later upkeep) and an arbitrary linear score.

Survival after the change, of 40 (RLS / table where there are two):

| arm | none | delayed | new feature | silent |
|---|---|---|---|---|
| oracle | 40 | 40 | 40 | 40 |
| designer's profile | 40 | 0 | 0 | 40 |
| self-set profile | 40 | 0 | 0 | 40 |
| learner | 40 / 40 | 35 / 31 | 40 / 38 | 40 / 40 |
| features-only freeze | 40 / 40 | 35 / 31 | 21 / 22 | 40 / 40 |
| arm 5, all frozen | 40 / 40 | 32 / 31 | 13 / 24 | 40 / 40 |
| score target | 40 | 0 | 0 | 40 |
| arbitrary target | 40 | 0 | 0 | 0 |

- **New feature.** The learner added the newly relevant feature after the
  change in 40 and 37 of 40 runs, no frozen arm could, and the learner's
  post-change net intake beat arm 5's in 40 and 36 of 40 seeds. Its first
  correct warning came a median 108 (RLS) steps after the change, the
  oracle's 9.
- **Delayed, on an attended feature.** No feature was added; the learner and
  the features-only freeze are identical, and arm 5 differs only by its
  frozen threshold (RLS) or not at all (table). Re-estimating suffices.
- **Silent.** Every arm that registers a shortfall in the visit survives: the
  absence is registered at the first silent step ([CASE-241](CASE-241.md)'s S3). The
  learners added the silence feature (40 and 38 of 40) and probed (95 and 126
  probes on average); that paid against arm 5 under RLS (39 of 40 seeds) and
  cost under the table (lost in 38 of 40). The self-set profile, which never
  learns, did better than both learners (1,421 against 1,172 and 1,050 net).
- **The target.** Where no cost is delayed the score target is the energy
  account and the runs are identical; where one is, the score-target learner
  dies in every seed. The arbitrary target dies under every change, and its
  learner attends to the features of the score it was given.
- **Which features the learner came to warn on** ([CASE-239](CASE-239.md)'s third control):
  at the change, red, warm and neighbour in every RLS run and in 36 of 40
  table runs (the other four also attended one irrelevant feature); after
  it, the feature the change made relevant.

## What it can show

- **Rungs that come apart on one channel** ([QUESTION-285](../questions.d/QUESTION-285.md), answer 2). With the
  sensory correlation held identical, each organization adds a behaviour the
  one below lacks: acting on an absence (R0, nothing kept), registering a
  bounded non-response (R1, an interval, an expectation and a retained flag,
  which is [CLAIM-651](../claims.d/CLAIM-651.md)'s condition; R0 has the consequence without the
  registration, which is [CASE-238](CASE-238.md)'s point), placing the fault (R2), and
  finding a fault outside the catalog (R3). The relay's physical fail-safe
  copes with the heat fault that defeats R1 and R2, by flooding: it acts on
  an absence and does not diagnose one.
- **Revising criteria, separated from revising estimates** ([CASE-239](CASE-239.md)'s first
  test). The learner beats arm 5 on the change that needs a new feature, under
  both rules, and does not on the change that needs only new weights. The
  features-only freeze shows the gain is the feature, not the threshold or the
  probes. This is [CLAIM-tmppa4rs](../claims.d/CLAIM-tmppa4rs.md).
- **[CASE-239](CASE-239.md)'s second test**, read two ways ([CLAIM-tmpnc1mf](../claims.d/CLAIM-tmpnc1mf.md) and
  [CLAIM-tmphrp1s](../claims.d/CLAIM-tmphrp1s.md), alternatives for the owner): the gains vanish when the
  energy account is replaced, which the case's wording counts against
  endogenous revision, and which also shows the criteria bound to the
  condition of the forager's dissolution, as the case's "main threat" asks.

## What it cannot show

- That the norm is the forager's own in Bickhard's sense ([THEORY-220](../theory.d/THEORY-220.md)): the
  modeller wrote the energy variable, the dissolution condition, the learning
  rules and the list of features a criterion can be built from, as Kolchinsky
  and Wolpert concede of theirs ([THEORY-1646](../theory.d/THEORY-1646.md)). On the selection-based reading
  ([CLAIM-tmp974nn](../claims.d/CLAIM-tmp974nn.md)) the learned warnings are stabilized by the forager's own
  past upkeep, which that objection grants; whether that makes them its own is
  [QUESTION-128](../questions.d/QUESTION-128.md)'s and is not settled here.
- Invention of a new question. R3 and the learner choose among features they
  already sense; neither makes a probe or a variable it lacked (A10's caveat
  in [CASE-242](CASE-242.md); [QUESTION-285](../questions.d/QUESTION-285.md)'s out-of-family distinction).
- Anything about real fire systems, or about learners other than the two
  rules run. The delayed and new-feature changes have the same size by
  design, so their contrast isolates attention and not difficulty. Survival
  under the delayed cost depends on the energy store (500); the learning arms'
  ordering, not their counts, is the result.
