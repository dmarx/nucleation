---
status: Proposed
title: 'In a four-unit linear model with a beam-like apparatus, a fixed partition, the partition recovered from the dynamics in force and the apparatus''s own partition come apart under five interventions; the apparatus''s partition differs from the recovered one only where the apparatus is in place and its coupling is weaker than the units'' own, and there it predicts worse'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-057 as a
    delegated lead worker. Script, tests and results under
    scratch/studies/lead-057/.
standing: stipulated
kind: executed-study
tags:
- individuation
- complex-systems
- metaphysics
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-284
summary: >-
  LEAD-057 asks, for one model, whether the three partitions of
  QUESTION-284 (A5's "a fixed preexisting partition, a partition
  recovered from measured dynamics, and an arrangement-dependent partition
  produced through coupling to an apparatus") make different
  counterfactual predictions. The model is a four-unit linear Gaussian
  VAR(1) whose units pair as 01 and 23, with an apparatus that couples 02
  and 13, the beam joining two pendulums of CLAIM-194. Each partition is
  scored by what it licenses, that each block can be predicted from its own
  past, computed exactly and checked by simulation. The fixed and recovered
  partitions differ whenever an intervention moves the coupling. The
  apparatus's partition, read as tracking the apparatus, differs from the
  recovered one only with the apparatus in place at gain below about 0.23,
  where it loses 7.5% against 0.1%; read as tracking the dynamics the
  apparatus produces, it never differs. With the probe given states of its
  own, the recovered partition of system and apparatus puts each probe in
  the pair it couples. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpy1gmq CLAIM-157 CLAIM-476 — new or Proposed; the claim this case grounds and neighbours cited as open -->

# CASE-tmp06fbt: In a four-unit linear model with a beam-like apparatus, a fixed partition, the partition recovered from the dynamics in force and the apparatus's own partition come apart under five interventions; the apparatus's partition differs from the recovered one only where the apparatus is in place and its coupling is weaker than the units' own, and there it predicts worse

## Why this model

LEAD-057 leaves the model open. The simplest one in which the three
partitions can come apart needs two candidate pairings of the same units,
one intrinsic and one an apparatus can impose, and a coupling strength the
apparatus can turn up or down. Four units in two pairs, with a probe that
cross-pairs them, is the smallest such system: three units admit no two
disjoint pairings, and a linear Gaussian model makes every prediction
exact. It is the family the record already uses for block and closure
results (CLAIM-388, CASE-120), and the apparatus is CLAIM-194's beam
joining two pendulums, so the result reads directly against those
entries. Nonlinearity, plasticity with its own dynamics, and more units
would add nothing the three accounts disagree about.

## The model

x_{t+1} = M x_t + e_t, e_t ~ N(0, I), four units 0 to 3. Intrinsic M:
self-coupling 0.3, coupling c = 0.25 within the pairs 01 and 23, a
background 0.02 between every other two units. The apparatus adds gain g
(0.35 where not stated) between 0 and 2 and between 1 and 3. In a variant
the apparatus has states of its own: two probes, each driven by the sum of
the two units it joins and feeding back into both.

**What a partition predicts.** A partition into blocks licenses the
prediction that each block can be forecast from its own past alone, which
is what the record's block criterion (CLAIM-157) reads a boundary off.
The score, block loss, is the excess one-step error of the best
block-local linear predictors over the best predictor using all units, as
a fraction of the latter: 0 means the blocks are decoupled for prediction.
It is computed from the stationary covariance and agrees with least-squares
fits on 100,000 simulated steps to within 0.002. A second score, the share
of an impulse to unit 0 that stays in unit 0's block over 30 steps, agrees
in every scenario.

**The three accounts.**

- **F, fixed and preexisting:** 01|23 in every scenario, whatever couples
  the units.
- **R, recovered:** the pairing with least block loss under the dynamics in
  force in that scenario.
- **Arr, arrangement-dependent:** the apparatus's pairing 02|13 whenever
  the apparatus is in place. With no apparatus it has nothing to say; if it
  is made to defer to the dynamics there, it is R.

## Results

| Scenario | F | R | Arr | block loss of 01, 02, 03 pairings |
|---|---|---|---|---|
| S0 no apparatus | 01\|23 | 01\|23 | silent | 0.001, 0.075, 0.075 |
| S1 apparatus in place, g = 0.35 | 01\|23 | 02\|13 | 02\|13 | 0.209, 0.104, 0.382 |
| S2 apparatus in place, g = 0 | 01\|23 | 01\|23 | 02\|13 | 0.001, 0.075, 0.075 |
| S3 apparatus removed, its coupling persists | 01\|23 | 02\|13 | silent | 0.209, 0.104, 0.382 |
| S4 no apparatus, the units rewired to 03\|12 | 01\|23 | 03\|12 | silent | 0.075, 0.075, 0.001 |

Gain sweep with the apparatus in place: R is 01|23 for g ≤ 0.20 and 02|13
for g ≥ 0.25 (the switch is where g plus the background passes c, about
0.23), while Arr is 02|13 throughout. Probe variant: of the ten balanced
splits of the six variables, the best is 0 2 probe | 1 3 probe (loss 0.064,
next 0.088).

## What it shows

- **F against R.** They differ in S1, S3 and S4, every scenario in which an
  intervention moves the coupling, and the measurement decides: in S4, F's
  blocks lose 7.5% and R's 0.1%. A fixed partition that licenses
  block-local prediction is refuted by any such intervention; one that
  licenses nothing is not tested by it.
- **Arr against R.** In S1, where the apparatus is on and strong, they
  agree, and every observable is accounted for by the apparatus's coupling
  plus a recovered partition of the altered dynamics: A5's "a measuring
  apparatus could alter a system's dynamics, and a subsequent analysis
  could correctly discover the boundaries in the altered system". They
  differ only where the arrangement and the dynamics it produces come
  apart: in S2 and the sweep below the switch, the apparatus is in place
  and the dynamics do not follow it, and there Arr's blocks lose 7.5%
  against R's 0.1%; in S3 the change outlasts the apparatus, and Arr, read
  as depending on the apparatus's presence, has nothing to say about a
  boundary the dynamics still show. Read as depending on having been
  coupled, it agrees with R in S3.
- **The apparatus inside the unit.** When the probe has states of its own,
  the recovered partition of system and apparatus together puts each probe
  in the block of the pair it joins. A5's enactment, (𝒟, A) → B_A, is
  here the discovery of a boundary in the joint dynamics, with the
  apparatus as a member.

## Limits

- The score is one licence a partition gives, block-local prediction. An
  account whose partition licenses no prediction about the dynamics is
  untested by it, by construction; that is the point the claim this case
  grounds (CLAIM-tmpy1gmq) draws.
- R is defined as the best-scoring pairing, so its winning is not a
  finding; the finding is where F and Arr coincide with it and where they
  do not.
- Only the three pairings of four units are compared in the main runs,
  not every partition. In S1 no pairing is nearly decoupled (R's loses
  10%); R names the best of the three, not a near-decomposable block.
- One linear model with stipulated parameters. The pattern rests on the
  structure (which pairing the coupling favours), not on the numbers.
- It is about the third of the three relations the note of 2026-11-07 on
  QUESTION-284 distinguishes: dependence on an arrangement or
  apparatus. It says nothing of synchronic part–whole constitution or of
  relations constituting their relata.
