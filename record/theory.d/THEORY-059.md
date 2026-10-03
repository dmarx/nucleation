---
number: 59
status: Proposed
formerly:
- THEORY-tmp1gn9c
promote_when: >-
  Independent replication of the one prediction that separates the
  accounts, and a test the account could fail on single trials. The
  prediction is Schurger et al.'s: when people waiting to move
  spontaneously are interrupted at random and must respond at once, their
  fastest responses are preceded by a slow negativity that began before
  the interruption. It rests on one experiment of 13 people (LIT-605).
  A second laboratory finding it would promote this, as would evidence
  that the readiness potential's early slope is present, at matched
  amplitude, in epochs that do not end in a movement. The account is
  refuted if the early buildup, read on single trials, predicts that a
  movement will follow and when, beyond what a threshold on autocorrelated
  noise predicts with the same fitted parameters; that would make the
  buildup a commitment and not a fluctuation. It is also refuted for the
  timing half if a method of timing the urge that does not rest on the
  clock report puts awareness well after the threshold crossing. What
  cannot settle it: more movement-locked averages, which both accounts
  predict; and decoding of an upcoming choice slightly above chance
  seconds early, which a biased fluctuation also produces.
title: 'The readiness potential does not show that a neural decision to act precedes awareness of the urge to act'
version: 1
tags:
- free-will
- behavioral-integration
- neuroscience
- consciousness
date: '2026-10-03'
source:
- LIT-605
- LIT-431
summary: >-
  Libet read the readiness potential, which begins half a second or more
  before a spontaneous movement and before the reported urge, as the brain
  deciding first. Two independent arguments in the record remove that
  inference. Schurger, Sitt & Dehaene ([LIT-605](../literature.d/LIT-605.md)) show that a leaky
  accumulator driven by noise and fitted to waiting times alone reproduces
  the averaged readiness potential (r² = 0.96), because movement-locked
  averaging recovers the fluctuations that crossed threshold; a prediction
  of theirs held in 13 people. Dennett & Kinsbourne ([LIT-431](../literature.d/LIT-431.md)) argue that
  the clock report times a represented content, not an event in the
  brain. Proposed: the authors say their model shows the potential could
  be fluctuation, not that it is. It says nothing about whether the urge
  causes the act.
---
<!-- inactive-ok-file: THEORY-029 THEORY-040 — Proposed; the record's free-will accounts, named to say they do not rest on Libet -->
<!-- inactive-ok-file: THEORY-061 — Proposed; companion account named for the goal mechanism it generalises from this one -->

# THEORY-059: The readiness potential does not show that a neural decision to act precedes awareness of the urge to act

## Source

- Schurger, Sitt & Dehaene (2012), [LIT-605](../literature.d/LIT-605.md), read in full in
  [NOTE-462](../notes.d/NOTE-462.md), except the supporting information.
- Dennett & Kinsbourne (1992), [LIT-431](../literature.d/LIT-431.md), read in [NOTE-367](../notes.d/NOTE-367.md): §3 on Libet,
  target article only.

## The inference under attack

The readiness potential is a slow negativity in the average of EEG epochs
time-locked to a self-initiated movement. In Libet's task it starts a
second or more before the movement, and people report the urge to move
only about 200 ms before it. Read as the signature of planning, that gives
the inference this account denies: the brain decides to act, unconsciously,
and awareness is told later.

## What was actually shown

**The potential is what averaging noise at a threshold produces.** Schurger
et al. ([LIT-605](../literature.d/LIT-605.md)) model the decision of when to move as a single leaky
accumulator, δx = (I − kx)Δt + cξ√Δt, with a weak constant urgency I, leak
k, Gaussian noise and a threshold. They fitted three parameters to the
waiting times of 14 participants in Libet's task, and only to them. With
those values, the sign-reversed average of simulated traces aligned to
threshold crossings fitted the measured readiness potential from −3 to
−0.15 s with r² = 0.96. The reason is selection. Only epochs that end in a
crossing are averaged, so the average recovers the autocorrelated noise that
happened to carry the trace to threshold. No single trace was building
toward anything.

**A prediction that the planning reading does not make held.** If the
buildup is ongoing fluctuation, it should be present whenever the system
happens to be near threshold, whether or not the person was about to move.
Interrupting 13 participants with clicks at random times, Schurger et al.
found that their fastest responses were preceded by a slow negativity that
began over 0.5 s before the click (P < 0.005), while the times of fast and
slow clicks were spread equally through the trial (P = 0.64). That
excludes a slowly building general readiness as the cause.

**Where the decision goes instead.** On this model the "neural decision to
move now" is the threshold crossing, about 150 ms before movement. It
coincides with the lateralised readiness potential and with the reported
urge, which was 152 ms before movement in their data. So the urge is not
late; the decision has not yet happened when the potential begins. The
authors: Libet's conclusion that the neural decision precedes awareness "by
1/2 s or more" is "unfounded".

**The clock report cannot time awareness anyway.** Dennett and Kinsbourne
([LIT-431](../literature.d/LIT-431.md)) argue that the time a content is represented is not the time it
represents, as a letter dated before a battle can arrive after news of it.
The position of a clock hand reported as simultaneous with the urge is a
judgment the brain concludes about content, "an artifact of the
experimental situation" (p. 198), and not a reading of when an event in the
brain occurred. If that is right, the comparison Libet made has no
well-defined second term.

**Two independent arguments.** Schurger et al. attack the neural premise
and accept the clock report as a rough estimate. Dennett and Kinsbourne
attack the clock report and do not re-analyse the potential. They disagree
on how far the report can be trusted ([NOTE-462](../notes.d/NOTE-462.md)). Either one, if sound,
removes the inference, and that is why both are sources.

## What this does not say

- **Not that the potential is noise.** "Although our study demonstrates
  that the readiness potential could reflect non–goal-directed
  (spontaneous) neural activity, it does not prove that this possibility is
  in fact the case." The claim is that the inference fails, not that its
  negation is established. That is why this is Proposed.
- **Not that the conscious urge causes the movement.** The model is silent
  on the urge. It places the urge and the threshold crossing together in
  time and says nothing about which, if either, does causal work.
- **Not a claim about free will.** It removes an empirical premise
  sometimes used against conscious will. It does not support or test the
  record's free-will accounts, [THEORY-029](THEORY-029.md) and [THEORY-040](THEORY-040.md), which are about
  ownership and manipulation and do not rest on Libet.
- **Narrow task.** One movement per trial, timed for no reason. Deliberate
  choices with something at stake were not tested, and the account says
  nothing about them.

## Connections

- **The unity it is about.** `behavioral-integration`: when a single action
  is triggered, and by what. Awareness enters only as a reported time,
  so this is not a claim about phenomenal unity ([ADR-024](../decisions.d/ADR-024.md)).
- **[THEORY-068](THEORY-068.md).** Schurger et al.'s accumulator is the leak-dominant,
  single-unit case of the Usher–McClelland process that account treats. In
  Bogacz et al.'s terms it is a stable O-U process with an attractor at I/k
  below threshold, so crossings are driven by noise ([NOTE-461](../notes.d/NOTE-461.md); the
  mapping is the record's).
- **[THEORY-061](THEORY-061.md)** generalises Schurger et al.'s picture of how the task
  goal acts: by raising the baseline toward threshold, with "the precise
  moment … not directly decided by a goal-directed operation".
