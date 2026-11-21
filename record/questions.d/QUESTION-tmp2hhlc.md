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
bearing:
- THEORY-2041
- THEORY-2051
- THEORY-1431
- CLAIM-692
- CLAIM-tmpask80
- CLAIM-tmpd1shn
summary: >-
  A's open direction at the close of A13 of the exchange "Rich Get Richer
  Power Laws", "whether scale-free systems have a distinctive
  computational capacity—whether their multiscale correlations make them
  especially capable of storing memories, propagating signals, adapting,
  or performing calculations", which A calls "considerably more subtle"
  than the edge of chaos, and which A15 takes up. The record holds the
  order-to-chaos transition in deep networks (THEORY-2041, THEORY-2051), a
  reservoir (THEORY-1431) and 1/f in brains (CLAIM-692), and no question
  on criticality and computation. The wording is A's (the other assistant
  in the exchange "Rich Get Richer Power Laws", A13 and A15); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-2041 THEORY-2051 THEORY-1431 — Proposed readings bearing on the question -->
<!-- inactive-ok-file: CLAIM-tmpask80 CLAIM-tmpd1shn ARG-tmpubyzo — filed with this question from the same exchange, Proposed -->
<!-- inactive-ok-file: LIT-tmpkvpg4 LIT-tmp7sbn6 LIT-tmpe6jga — Deferred, registered 2026-11-21 from the exchange, unread -->

# QUESTION-tmp2hhlc: Do systems near a dynamical transition, or with scale-free dynamics, have a distinctive computational capacity, or does nearness to the transition only redistribute a bounded capacity among kinds of computation, by task?

## Why it is a question

A15 opens on the hope: "**A system near criticality may be especially
capable of preserving information about the past while remaining
sensitive to new information from its environment.**" It then gives the
reasons to doubt that it is a general advantage: a bound on total
capacity (Dambre and colleagues, LIT-tmp7sbn6, unread), a three-way
tradeoff of sensitivity, reliability and speed, and a finite-window study
in which the best discrimination moves off the critical point
(LIT-tmpe6jga, unread). A's answer is CLAIM-tmpask80; one exactly solved
case is CLAIM-tmpd1shn.

Three things keep it open.

1. **Which transition.** A runs together the order-to-chaos transition
   of recurrent networks, where the edge-of-chaos results live
   (Bertschinger and Natschläger, LIT-tmpkvpg4, unread; the record's
   THEORY-2041 for deep networks), and branching criticality of neural
   avalanches, where a branching ratio of one separates dying from
   exploding cascades (QUESTION-091). They are different transitions: the
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
QUESTION-091 asks for organizations.
