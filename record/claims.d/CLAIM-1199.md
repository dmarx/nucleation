---
number: 1199
status: Proposed
formerly:
- CLAIM-tmpyf8s0
title: 'Optimizer and network share conflict regulation'
statement: >-
  The crossed intervention on a small conventionally trained network shows
  the regulation of conflict shared between the network's learned state and
  the optimizer, in proportions that the training optimizer sets, so that in
  conventional training most of that governance does not fall outside the
  network as a rule
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, from the lead run of that date, as
    the alternative to the reading that the run corroborates the claim it
    objects to.
role: counter
warrant: interpretive
tags:
- learning-theory
- agency
date: '2026-11-23'
line:
- distributed-agency
- learned-structure
bears_on:
- QUESTION-122
rests_on:
- CLAIM-1030
objects_to:
- CLAIM-367
summary: >-
  Alternative B. [CLAIM-367](CLAIM-367.md) says that in conventional training "most of
  that governance falls to the optimizer–model–data system", and argues
  from the relations outside the network. In the run ([CLAIM-1030](CLAIM-1030.md))
  the learned state accounted for 0.58 of the variation in how much of one
  task the network gave up, against 0.39 for the optimizer, in networks
  trained by heavy ball; and 0.15 against 0.81 in networks trained by
  Adam. Where governance sits is then not a fixed fact about conventional
  training but a result of it: the training optimizer decides how much of
  the later regulation of conflict the network comes to hold. On this
  reading the claim's "most" is an overstatement, though its defeat
  condition is not met. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-367 — Proposed; the claim this reading objects to -->
<!-- inactive-ok-file: CLAIM-1030 CLAIM-1138 — new; the result and the alternative reading filed by the lead run of 2026-11-23 -->

# CLAIM-1199: Optimizer and network share conflict regulation

## The claim

[CLAIM-367](CLAIM-367.md) is written so that the network–optimizer–data system holds
most of the governance of updates, and its argument places the relations
that select effective updates outside the network. A crossed intervention
measures something those relations do not: how the outcome of a conflict
divides when each side is changed. In the run ([CLAIM-1030](CLAIM-1030.md)):

- for heavy-ball-trained networks, disrupting the units that carry the
  learned task separation changed the forgetting more (+0.028) than any
  change of optimizer (at most −0.018), and the state carried the larger
  share of the variation (0.58 against 0.39);
- for Adam-trained networks the optimizer carried most (0.81).

So the same conventional training gives a network that holds more of the
regulation of conflict, or less, depending on the optimizer that trained
it. A statement that *most* of it falls outside the network is then not a
property of conventional training, and the claim should say "a share that
the training itself sets".

## What it does not say

- That the defeat condition is met. Its first limb failed.
- That the network governs its updates. Its learned structure shapes how a
  conflict spreads; it selects nothing.
- That variance shares across one grid of four optimizers and four
  disruptions measure governance in general. They depend on which
  optimizers and which disruptions were chosen, which is the main weakness
  of this reading and why the assistant leans to the other.

## Alternative

[CLAIM-1138](CLAIM-1138.md) reads the run as corroborating [CLAIM-367](CLAIM-367.md): its
defeat condition fails, and the claim already allows the network to hold
some governance. The owner chooses.
