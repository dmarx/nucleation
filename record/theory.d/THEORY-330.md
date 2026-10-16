---
number: 330
status: Proposed
formerly:
- THEORY-tmp1spba
promote_when: >-
  A replication, by another group or in another memory-load task, using the
  choice/no-choice design with each person's best strategy computed from the
  forced phase alone, held out from the choices it predicts. It promotes the
  account if that held-out optimum predicts choices better than its neighbours
  in most participants; it refutes it if the advantage vanishes once the optimum
  is computed without choice-phase trials. Further correlations of chosen load
  with group-level payoff, or a fitted model of memory capacity, cannot settle
  it: the claim is about each person's own measured optimum.
title: "After a forced phase in which each person experienced every memory load from three to nine items, the load that had given that person the best reward rate predicted their later choices better than one item fewer or one more, in a copying task where items are seen once and cannot be looked up again; a steeper reward for long lists raised chosen load, a higher price for errors did not, and about one person in five kept choosing a non-optimal load"
version: 1
tags:
- cognition
date: '2026-10-15'
source:
- LIT-1062
answers:
- QUESTION-095
summary: >-
  Howes, Duggan, Kalidindi, Tseng and Lewis (2016), [LIT-1062](../literature.d/LIT-1062.md), read in [NOTE-882](../notes.d/NOTE-882.md).
  Participants copied names shown one at a time from a mock email to a calendar.
  Each person's best list length in their own data predicted 55% and 46% of their
  choices, against 8–17% for the neighbouring lengths (N = 40 and 20). An
  exponential points schedule raised chosen length (6.99 against 5.07); forfeiting
  the whole trial on one error did not (5.00 against 5.05). 13 of 60 persistently
  chose a non-optimal length. There is no look-up and no model: the prediction is
  each person's empirical argmax. Lieder and Griffiths' description of it as a
  memorize-or-look-up trade ([LIT-1071](../literature.d/LIT-1071.md)) does not fit the task.
---

# THEORY-330: After a forced phase in which each person experienced every memory load from three to nine items, the load that had given that person the best reward rate predicted their later choices better than one item fewer or one more, in a copying task where items are seen once and cannot be looked up again; a steeper reward for long lists raised chosen load, a higher price for errors did not, and about one person in five kept choosing a non-optimal load

## Source

Howes, Duggan, Kalidindi, Tseng and Lewis (2016), [LIT-1062](../literature.d/LIT-1062.md) (Cognitive Science
40(5), 1192–1223), read in [NOTE-882](../notes.d/NOTE-882.md): both experiments, the choice/no-choice
analysis and the strategy-change result of Experiment 2.

## What was actually shown

**The task.** A mock email shows one appointment at a time ("09.00: Appointment
with NAME"); after a trial's list, the participant switches to a calendar and
types the names in order. "Participants could not go back to correct errors",
and nothing lets them return to the email during recall. The only strategy
dimension is list length, 3 to 9. A shorter list means more trials, each with
its overhead, to reach a fixed total. Reward rate is points per trial duration,
including the move to the next trial.

**The design.** A no-choice phase ran every participant through every length in
random order; a choice phase then let them pick. Each person's boundedly optimal
length is the argmax of their own mean rate. "the cost of optimization is paid by
the analyst, not by the participant".

**Experiment 1 (N = 40).** The person's optimum predicted 55% of choices, one
fewer 8%, one more 17% (optimum beat each, p < .001). Its correlation with mean
chosen length was r = .35. Error cost (each wrong item scores zero, or one error
voids the trial) did not change chosen length (5.05 against 5.00).

**Experiment 2 (N = 20).** An exponential points schedule raised chosen length
(6.99 against 5.07, d = 1.33). The optimum predicted 46% of choices, neighbours
12% and 14%; correlation r = .77. People also changed strategy outside the
space: on 49% of exponential trials they typed first letters in every box before
completing names, and chose longer lists when they did.

**Departures.** Across both experiments, 13 of 60 "persistently selected a list
length, and therefore a strategy, that was not bounded optimal", 10 of them by
one item more. In Experiment 1, eight became less likely to choose their optimum
as trials went on.

**What could have come out otherwise.** Choices could have matched each
strategy's probability of being best, or sat one item below the optimum, as an
offloading preference would predict. Neither happened.

## What this does not say

- **That this is a choice between memory and the world.** There is no look-up.
  Lieder and Griffiths ([LIT-1071](../literature.d/LIT-1071.md), [NOTE-873](../notes.d/NOTE-873.md)) call it a memorize-or-look-up trade;
  the task gives no way to consult the source again.
- **That a model predicts the choice.** No capacity, look-up time or error
  parameter appears. The prediction is each person's measured best, and the
  bounds enter only through it.
- **That the optimum was computed from data independent of the choices.** Which
  trials enter each person's mean rate is not stated precisely, and the paper's
  distributions pool both phases.
- **That people price errors.** Voiding the whole trial on one error changed nothing;
  what moved choice was the payoff for long lists.
- **That choice is optimal in general.** About a fifth chose otherwise, persistently,
  and the paper's explanations for this are untested.
- **Anything about precomputation, reuse, staleness or search.** Items are used
  once, within seconds; nothing stored serves a later trial.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md): the "defer and re-read" strategy with the re-read removed. Its
  one addition to the question's terms is a price on a wrong stored item, which
  did not move behaviour. Practice made a chosen length better, the mirror of the
  erosion of an unused route in [LIT-1059](../literature.d/LIT-1059.md).
- [THEORY-346](THEORY-346.md) fits group means with a time-only model; this tests, per person,
  whether people find the best point of their own trade, and keeps the earlier
  conclusion that they neither minimize memory nor favour the world.
