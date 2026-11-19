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

## Note of 2026-11-19: follow-up turns of "Topological protection explained"
<!-- inactive-ok-file: CLAIM-754 CLAIM-758 — Proposed or Deferred; cited from the follow-up turns filed 2026-11-19 -->

The second share of the exchange (2026-11-19) adds U34 to U39. At A80 ChatGPT proposed this claim's test: a compositional task family, f = h∘g, where learners matched on first-stage performance (structured, memorizing, shortcut) are compared on the cost of later acquiring h∘g, with an intervention that disrupts the learned representation of g to show it mediates the saving. The owner answered (U37): "I think the pretraining literature ought to already demonstrate this for us." ChatGPT agreed (A82): the basic phenomenon, prior learning making later learning cheaper, is "established background, not ... the novelty we need to prove", and the sharper question is "when the same historically acquired organization both lowers the cost of some future acquisitions and raises the cost of others", which is [CLAIM-754](CLAIM-754.md)'s and [CLAIM-758](CLAIM-758.md)'s. It cited two works, registered and unread: McDermott and colleagues on structure-inducing pre-training ([LIT-tmp995ll](../literature.d/LIT-tmp995ll.md)) and Anguita and colleagues on how pretraining shapes inductive bias in fine-tuning ([LIT-tmplopzs](../literature.d/LIT-tmplopzs.md)). If they show what is cited, the claim's possibility has real instances; the claim is about valuation, which they would not test. No status change.

## Note of 2026-11-19: the pretraining works, read
<!-- inactive-ok-file: THEORY-tmpkjzqg THEORY-tmppm9la — Proposed; cited from the readings of 2026-11-19 -->

The two works cited after the owner's point at U37 (that the pretraining literature ought to show acquired organization making later learning cheaper) were read. They carry less than that. Anguita and colleagues ([THEORY-tmppm9la](../theory.d/THEORY-tmppm9la.md); [NOTE-tmpr453b](../notes.d/NOTE-tmpr453b.md)) give an analytical instance: pretrained features lower the sample cost of fine-tuning where the tasks' features overlap, and beat training from scratch in one deep-network comparison. McDermott and colleagues ([THEORY-tmpkjzqg](../theory.d/THEORY-tmpkjzqg.md); [NOTE-tmp074zx](../notes.d/NOTE-tmp074zx.md)) measure final downstream performance, with one convergence curve and no threshold or budget, so at most a weak instance. Neither bears on the claim's own content, valuation by effect on later acquisitions. The owner's point stands as a reasonable expectation that these two works do not yet bear out in cost terms; a reading of work that measures sample or compute cost to a threshold would. No status change.

## Note of 2026-11-19: Brown and colleagues, and Howard and Ruder, read
<!-- inactive-ok-file: LEAD-tmpn5ruw TERM-131 THEORY-tmp8cm7r THEORY-tmpw8s3h — Proposed or newly filed; cited from the readings of 2026-11-19 -->

The readings the owner asked for after the earlier note ([LEAD-tmpn5ruw](../leads.d/LEAD-tmpn5ruw.md)). Howard and Ruder ([THEORY-tmpw8s3h](../theory.d/THEORY-tmpw8s3h.md), corroborates; [NOTE-tmp44esf](../notes.d/NOTE-tmp44esf.md)) are the first work on record to measure prior learning lowering the cost of a later acquisition to a stated level: with 100 labelled examples their pretrained and fine-tuned model "matches the performance of training from scratch with 10× and 20× more data" on IMDb and AG. That is the claim's premise in cost terms, and the owner's point at U37 borne out. Qualified: the saving is joint between pretraining and the fine-tuning method, which the comparison does not separate, and pretraining is not counted as cost ("it only needs to be performed once"). Brown and colleagues ([THEORY-tmp8cm7r](../theory.d/THEORY-tmp8cm7r.md); [NOTE-tmprmye5](../notes.d/NOTE-tmprmye5.md)) are weaker evidence: larger pretrained models reach a level with fewer in-context examples, but across model sizes, not against no pretraining, and the in-context "acquisition" retains nothing (see [TERM-131](../terms.d/TERM-131.md)). Neither touches the claim's own content, valuing an acquisition by its effect on others. No status change.
