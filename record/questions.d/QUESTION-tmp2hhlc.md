---
status: Open
title: 'Do systems near a dynamical transition, or with scale-free dynamics, have a distinctive computational capacity, or does nearness to the transition only redistribute a bounded capacity among kinds of computation, by task?'
version: 1
tags:
- complex-systems
- information-theory
- neuroscience
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  A's open direction at the close of A13 of the exchange "Rich Get Richer
  Power Laws", "whether scale-free systems have a distinctive
  computational capacity—whether their multiscale correlations make them
  especially capable of storing memories, propagating signals, adapting,
  or performing calculations", which A calls "considerably more subtle"
  than the edge of chaos, and which A15 takes up. The record holds the
  order-to-chaos transition in deep networks ([THEORY-2041](../theory.d/THEORY-2041.md), [THEORY-2051](../theory.d/THEORY-2051.md)), a
  reservoir ([THEORY-1431](../theory.d/THEORY-1431.md)) and 1/f in brains ([CLAIM-692](../claims.d/CLAIM-692.md)), and no question
  on criticality and computation. The wording is A's (the other assistant
  in the exchange "Rich Get Richer Power Laws", A13 and A15); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-2041 THEORY-2051 THEORY-1431 — Proposed readings bearing on the question -->
<!-- inactive-ok-file: CLAIM-tmpask80 CLAIM-tmpd1shn — filed with this question from the same exchange, Proposed -->
<!-- inactive-ok-file: LIT-tmpkvpg4 LIT-tmpe6jga — Deferred, registered 2026-11-21 from the exchange, unread -->
<!-- inactive-ok-file: THEORY-tmpr5fuq CLAIM-tmpyy261 — Proposed; the reading of 2026-11-21 and a claim it bears on -->

# QUESTION-tmp2hhlc: Do systems near a dynamical transition, or with scale-free dynamics, have a distinctive computational capacity, or does nearness to the transition only redistribute a bounded capacity among kinds of computation, by task?

## Why it is a question

A15 opens on the hope: "**A system near criticality may be especially
capable of preserving information about the past while remaining
sensitive to new information from its environment.**" It then gives the
reasons to doubt that it is a general advantage: a bound on total
capacity (Dambre and colleagues, [LIT-tmp7sbn6](../literature.d/LIT-tmp7sbn6.md), read 2026-11-21: see the
dated note), a three-way
tradeoff of sensitivity, reliability and speed, and a finite-window study
in which the best discrimination moves off the critical point
([LIT-tmpe6jga](../literature.d/LIT-tmpe6jga.md), unread). A's answer is [CLAIM-tmpask80](../claims.d/CLAIM-tmpask80.md); one exactly solved
case is [CLAIM-tmpd1shn](../claims.d/CLAIM-tmpd1shn.md).

Three things keep it open.

1. **Which transition.** A runs together the order-to-chaos transition
   of recurrent networks, where the edge-of-chaos results live
   (Bertschinger and Natschläger, [LIT-tmpkvpg4](../literature.d/LIT-tmpkvpg4.md), unread; the record's
   [THEORY-2041](../theory.d/THEORY-2041.md) for deep networks), and branching criticality of neural
   avalanches, where a branching ratio of one separates dying from
   exploding cascades ([QUESTION-091](QUESTION-091.md)). They are different transitions: the
   first is a change in the sign of the largest Lyapunov exponent of a
   deterministic map, the second a change in the mean offspring number of
   a stochastic cascade. A network can sit at one and not the other. A
   claim that critical brains compute well because reservoirs at the edge
   of chaos do needs a step relating the two, and the record has none.
2. **Which measure.** "Different definitions of utility can have optima
   at different parameter values" (A13 §6); "sensitivity isn't the same
   as useful computation". Memory capacity, separation, discrimination in
   a finite window and predictive information each peak, if at all, at
   their own place.
3. **Which environment.** A15 §8: "If the environment has one dominant
   characteristic timescale … a much simpler system tuned to that
   timescale could be more efficient." A scale-free internal dynamics
   pays only where the input has correlations across those scales.

A15 §5 adds a methodological point worth keeping: a study that perturbs
single neurons and follows the spread is "a stronger experimental
approach than relying on a power-law fit alone". A cites a Nature
Communications study of 10 January 2026 that the registration could not
identify, so the record cannot use it.

## What would answer it

For a stated class of systems and a stated family of tasks: a capacity
measure, its bound, and how the bound's allocation moves with distance
from the transition, with the transition named. Dambre and colleagues'
result, once read, may answer the first part for reservoirs with fading
memory and i.i.d. input. An adaptive system that tunes its own distance
from the transition by task (A15 §7, quasicriticality) would make the
question one of control rather than of a fixed operating point, as
[QUESTION-091](QUESTION-091.md) asks for organizations.

## Note of 2026-11-21: Dambre, Verstraeten, Schrauwen and Massar, read

Dambre and colleagues' paper ([LIT-tmp7sbn6](../literature.d/LIT-tmp7sbn6.md), read in [NOTE-tmpkp5gf](../notes.d/NOTE-tmpkp5gf.md); the
reading is [THEORY-tmpr5fuq](../theory.d/THEORY-tmpr5fuq.md)) **answers the first part** of "What would
answer it" and **leaves the rest open**.

- **Measure and bound: given**, for systems driven by i.i.d. input with a
  linear readout: capacities for orthogonal functions of past inputs sum to
  at most N, and to N with fading memory and N independent variables.
  Nearness to the transition cannot raise the total, which is flat at N
  inside the fading-memory regime and falls past the undriven system's
  stability edge.
- **Allocation against distance from the transition: not given.** The
  paper sweeps input scaling and sampling period at a fixed spectral
  radius.
- **Point 1, which transition.** The paper's edge is the stability edge
  of a deterministic map, neither branching criticality nor, strictly,
  the onset of chaos; [CLAIM-tmpyy261](../claims.d/CLAIM-tmpyy261.md) separates chaos, criticality and
  cascades, and this is a further thing.
- **Point 3, which environment.** The paper takes i.i.d. input on purpose,
  "so that any measured structure will be due to the dynamical system
  itself", and calls the bound for correlated input "largely a theoretical
  insight". It cannot speak to the value of multiscale memory in a
  correlated environment.

[THEORY-tmpr5fuq](../theory.d/THEORY-tmpr5fuq.md) `bears_on` this question.
