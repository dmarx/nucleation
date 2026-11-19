---
number: 756
status: Proposed
formerly:
- CLAIM-tmp5gbzr
title: 'An acquisition can be worth making for what it does to the cost of other acquisitions: valued only by its own savings on a fixed task distribution, a learning step that lowers the cost of a later one can show a loss, and the ranking of learning policies can reverse once its effect on later acquisitions is counted'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in CASE-295's arithmetic, or a showing that its
  stipulations are incoherent, for instance that an acquisition cannot
  lower the cost of another without that being one of its own savings on
  the task distribution as originally declared.
tags:
- learning-theory
- complex-systems
date: '2026-11-19'
line:
- realizability
- learned-structure
works:
- cost-structure-of-possibility
grounds:
- CASE-295
rests_on:
- CLAIM-303
complements:
- CLAIM-605
- CLAIM-761
- CLAIM-754
uses:
- TERM-117
- TERM-131
bears_on:
- QUESTION-495
summary: >-
  A's, from A48 §4 of the exchange "Topological protection explained"
  (2026-11-19), answering the owner's U21, how to formulate optimal
  learning: "The optimal learning policy may prioritize productive nuclei
  of future competence over direct improvement on current tasks." A43
  §5.2 put the same as recursive capability formation. The record held a
  single capacity that needs capacity already present to grow ([CLAIM-605](CLAIM-605.md))
  and the productive nucleus ([TERM-117](../terms.d/TERM-117.md)), but not the valuation of one
  acquisition by its effect on another's cost. Admission by derivation
  with a stipulated case ([CASE-295](../cases.d/CASE-295.md)): the step with a negative direct
  return is part of the best policy. The wording is A's with the filer's
  numbers; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2046 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: ARG-120 CASE-295 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-756: An acquisition can be worth making for what it does to the cost of other acquisitions: valued only by its own savings on a fixed task distribution, a learning step that lowers the cost of a later one can show a loss, and the ranking of learning policies can reverse once its effect on later acquisitions is counted

## The claim

A48 §2 valued a learning step ℓ by its expected savings on a task
distribution minus its cost, with the worked example of memorizing an
answer (cost 1, saves 3 on one question) against learning a procedure
(cost 4, saves 2 per question): with one question memorizing nets +2 and
the procedure −2; with six the procedure nets 8. A48 §4 then said that
this accounting misses an acquisition's effect on the cost of further
acquisitions: "The optimal learning policy may prioritize productive
nuclei of future competence over direct improvement on current tasks."

## Admission

By derivation, with a stipulated separating case ([CASE-295](../cases.d/CASE-295.md), argued
in [ARG-120](../arguments.d/ARG-120.md)). A procedure P costs 4 and saves 2 on the one question it
directly serves: −2 alone. A second competence Q saves 3 on each of three
later questions, 9 in all, and costs 10 to acquire from scratch but 1
once P is held. Then:

| policy | net |
|---|---|
| nothing | 0 |
| P alone | 2 − 4 = −2 |
| Q alone | 9 − 10 = −1 |
| P then Q | (2 − 4) + (9 − 1) = +6 |

Ranked by each step's own return, P is rejected, and so is Q, so the
policy acquires nothing. Counting P's effect on Q's cost, P then Q is
best. (Computed and checked.)

## Rests on

[CLAIM-303](CLAIM-303.md): work stored is worth it when reuse covers it. This claim says
reuse can be the lowered cost of another acquisition and not only savings
on tasks.

## The stronger reading it invites and does not support

That learners should prefer such steps. The case stipulates that the
later questions will come. When they cannot be specified in advance,
which is the owner's U21 problem, the value of a productive step is
uncertain, and that is [QUESTION-495](../questions.d/QUESTION-495.md). [CLAIM-605](CLAIM-605.md) shows the same
compounding for one capacity, with a threshold below which it traps.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Finn, Abbeel and Levine's MAML ([THEORY-2046](../theory.d/THEORY-2046.md)), read, is an empirical instance. The initialization best on the present joint objective, pre-training on all tasks, adapts worse than the MAML initialization chosen by post-adaptation loss (sinusoid, §5.1; Appendix C, Table 2: 5-shot MSE 2.41 against 0.67 after one step). That supports the claim with independent evidence. As in [CASE-295](../cases.d/CASE-295.md), the later tasks are stipulated to come, here from p(T), so it does not touch the stronger reading the claim declines.

No status change.
