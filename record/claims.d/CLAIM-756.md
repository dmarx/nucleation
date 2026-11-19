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

The second share of the exchange (2026-11-19) adds U34 to U39. At A80 ChatGPT proposed this claim's test: a compositional task family, f = h∘g, where learners matched on first-stage performance (structured, memorizing, shortcut) are compared on the cost of later acquiring h∘g, with an intervention that disrupts the learned representation of g to show it mediates the saving. The owner answered (U37): "I think the pretraining literature ought to already demonstrate this for us." ChatGPT agreed (A82): the basic phenomenon, prior learning making later learning cheaper, is "established background, not ... the novelty we need to prove", and the sharper question is "when the same historically acquired organization both lowers the cost of some future acquisitions and raises the cost of others", which is [CLAIM-754](CLAIM-754.md)'s and [CLAIM-758](CLAIM-758.md)'s. It cited two works, registered and unread: McDermott and colleagues on structure-inducing pre-training ([LIT-2847](../literature.d/LIT-2847.md)) and Anguita and colleagues on how pretraining shapes inductive bias in fine-tuning ([LIT-2861](../literature.d/LIT-2861.md)). If they show what is cited, the claim's possibility has real instances; the claim is about valuation, which they would not test. No status change.

## Note of 2026-11-19: the pretraining works, read
<!-- inactive-ok-file: THEORY-2072 THEORY-2077 — Proposed; cited from the readings of 2026-11-19 -->

The two works cited after the owner's point at U37 (that the pretraining literature ought to show acquired organization making later learning cheaper) were read. They carry less than that. Anguita and colleagues ([THEORY-2077](../theory.d/THEORY-2077.md); [NOTE-2159](../notes.d/NOTE-2159.md)) give an analytical instance: pretrained features lower the sample cost of fine-tuning where the tasks' features overlap, and beat training from scratch in one deep-network comparison. McDermott and colleagues ([THEORY-2072](../theory.d/THEORY-2072.md); [NOTE-2138](../notes.d/NOTE-2138.md)) measure final downstream performance, with one convergence curve and no threshold or budget, so at most a weak instance. Neither bears on the claim's own content, valuation by effect on later acquisitions. The owner's point stands as a reasonable expectation that these two works do not yet bear out in cost terms; a reading of work that measures sample or compute cost to a threshold would. No status change.

## Note of 2026-11-19: Brown and colleagues, and Howard and Ruder, read
<!-- inactive-ok-file: LEAD-009 TERM-131 THEORY-2062 THEORY-2084 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

The readings the owner asked for after the earlier note ([LEAD-009](../leads.d/LEAD-009.md)). Howard and Ruder ([THEORY-2084](../theory.d/THEORY-2084.md), corroborates; [NOTE-2141](../notes.d/NOTE-2141.md)) are the first work on record to measure prior learning lowering the cost of a later acquisition to a stated level: with 100 labelled examples their pretrained and fine-tuned model "matches the performance of training from scratch with 10× and 20× more data" on IMDb and AG. That is the claim's premise in cost terms, and the owner's point at U37 borne out. Qualified: the saving is joint between pretraining and the fine-tuning method, which the comparison does not separate, and pretraining is not counted as cost ("it only needs to be performed once"). Brown and colleagues ([THEORY-2062](../theory.d/THEORY-2062.md), corroborates; [NOTE-2160](../notes.d/NOTE-2160.md)) are evidence of a different kind: pretraining makes in-context learning, which is learning of the model running in an episode ([TERM-131](../terms.d/TERM-131.md), version 2), cheap, with a rough exchange rate of fewer than eight demonstrations against a BERT-Large fine-tuned on 125,000 examples on SuperGLUE. The comparisons are across model sizes and across systems, not one model with and without pretraining. Neither touches the claim's own content, valuing an acquisition by its effect on others. No status change.

## Note of 2026-11-19: the data-scheduling readings, read
<!-- inactive-ok-file: THEORY-2057 THEORY-2065 THEORY-2071 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Six works read for [LEAD-002](../leads.d/LEAD-002.md), the owner's suggestion that ordering experiments have this claim's shape. Two add evidence for the premise with the earlier acquisition's cost counted, which ULMFiT ([THEORY-2084](../theory.d/THEORY-2084.md)) did not. Hu and colleagues ([THEORY-2071](../theory.d/THEORY-2071.md), corroborates): a short formal-language first phase lets a 1B model reach its baseline's final loss with 33 per cent fewer total tokens, the first phase included; a matched natural-language first phase gets much of the saving. Chen and colleagues ([THEORY-2065](../theory.d/THEORY-2065.md), corroborates): at a fixed total budget, mixing a target skill's prerequisites in reaches a loss threshold in about a third fewer steps, though by co-acquisition, not one then the other. Bengio and colleagues ([THEORY-2057](../theory.d/THEORY-2057.md), corroborates) give the claim's pattern in final-error terms: easier shapes, poor alone, belong to the best policy within a fixed budget ([CASE-295](../cases.d/CASE-295.md)'s shape). Gururangan and colleagues, Liu and colleagues, and Feng and colleagues measure final performance: relevant earlier training helps, irrelevant hurts, specialized data early beats late, and developmental order within one corpus barely matters. None tests the claim's own content, valuing an acquisition by its effect on others. No status change.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: ARG-122 LEAD-008 THEORY-2058 THEORY-2059 THEORY-2060 THEORY-2064 THEORY-2069 THEORY-2074 THEORY-2076 THEORY-2081 THEORY-2083 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Fifteen works read for [LEAD-008](../leads.d/LEAD-008.md). Two add evidence for the premise in
cost terms (corroborates). Hernandez and colleagues ([THEORY-2059](../theory.d/THEORY-2059.md)):
pretraining is worth an amount of from-scratch data that grows as a power
law in later data and model size, in the low-data regime; pretraining's
own cost is excluded, and outside that regime small pretrained models do
worse than from scratch. The procedural-pretraining paper
([THEORY-2075](../theory.d/THEORY-2075.md)): a warm-up of well under one per cent of tokens, with no direct
value on the target, saves 14 to 45 per cent of later tokens; no seeds.
Against these, Stern and colleagues ([THEORY-2081](../theory.d/THEORY-2081.md)) find that at matched
compute with a tuned initialization no first phase beats natural language
alone, and that part of an earlier gain was a weak baseline; [ARG-122](../arguments.d/ARG-122.md)
argues that the instances carry the premise as possibility and not as a
rule. The rest measure final scores or attribution, not cost: code first
([THEORY-2064](../theory.d/THEORY-2064.md)) wins before cooldown and loses after it; reasoning data
early ([THEORY-2069](../theory.d/THEORY-2069.md)) raises what fine-tuning reaches; order at fixed
data matters a little ([THEORY-2076](../theory.d/THEORY-2076.md), [THEORY-2074](../theory.d/THEORY-2074.md), [THEORY-2083](../theory.d/THEORY-2083.md));
and the attribution studies ([THEORY-2058](../theory.d/THEORY-2058.md), [THEORY-2060](../theory.d/THEORY-2060.md)) credit only
immediate alignment, so by construction they cannot see an acquisition's
effect on later ones, the accounting this claim says is missing. None
tests the claim's own content. No status change.
