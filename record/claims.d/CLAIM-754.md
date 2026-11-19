---
number: 754
status: Proposed
formerly:
- CLAIM-tmp1l2s7
title: 'A learner''s acquired organization fixes three resource-indexed frontiers that move separately: the operational (what it can reliably do now within an operating budget), the developmental (what it can come to do reliably within a further acquisition budget, given a declared interface for what it may learn from) and the inquiry frontier (what it can formulate and pursue); so no scalar measure of competence or plasticity ranks learners or learning processes independently of context, though one can once a task distribution, resource costs, horizon and evaluative preferences are declared'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that one frontier fixes another: that within a declared class
  of learners and tasks, equal operational frontiers imply equal
  developmental frontiers, or that the inquiry frontier is a function of
  the operational one, so that a single measure suffices; or that the
  developmental frontier is not well defined once the learning interface
  and acquisition budget are declared.
tags:
- learning-theory
- complex-systems
date: '2026-11-19'
line:
- learned-structure
- realizability
rests_on:
- CLAIM-697
- CLAIM-569
- CLAIM-675
- CLAIM-475
uses:
- TERM-092
- TERM-131
complements:
- CLAIM-576
- CLAIM-758
bears_on:
- QUESTION-495
summary: >-
  A's, from A71 §6 of the exchange "Topological protection explained"
  (2026-11-19), the refreshed synthesis the owner asked for at U32. The
  operational frontier is [CLAIM-697](CLAIM-697.md)'s resource-conditional disposition
  (the owner's idea, A's formalization), the inquiry frontier is [TERM-092](../terms.d/TERM-092.md)
  and the owner's [CLAIM-475](CLAIM-475.md), and that equal present capabilities can leave
  different later ones is [CLAIM-675](CLAIM-675.md), demonstrated for support. What A71
  adds is the developmental frontier, what can be learned within an
  acquisition budget and a declared learning interface, and the claim
  that the three diverge. A71 introduced the inquiry frontier as new; it
  is [TERM-092](../terms.d/TERM-092.md). The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-294 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-697 CLAIM-758 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-754: A learner's acquired organization fixes three resource-indexed frontiers that move separately: the operational (what it can reliably do now within an operating budget), the developmental (what it can come to do reliably within a further acquisition budget, given a declared interface for what it may learn from) and the inquiry frontier (what it can formulate and pursue); so no scalar measure of competence or plasticity ranks learners or learning processes independently of context, though one can once a task distribution, resource costs, horizon and evaluative preferences are declared

## The claim

A71 §6 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf), with M a
learner's retained organization:

- **Operational**: the tasks q whose best success probability, over
  procedures affordable within an operating budget, reaches a declared
  reliability ρ. This is [CLAIM-697](CLAIM-697.md)'s construction, counting delivered
  success and not success merely sampled.
- **Developmental**: the tasks for which some admissible learning
  procedure, within an acquisition budget, produces an organization M′
  that reaches ρ under the operating budget, with probability at least
  1 − δ. "This depends on an explicitly specified learning-data interface.
  A system cannot be credited for learning a task from information it was
  never allowed to receive."
- **Inquiry**: the questions the system can formulate and pursue within
  its budget, distinct from those it can answer. This is [TERM-092](../terms.d/TERM-092.md)'s
  inquiry frontier and [CLAIM-475](CLAIM-475.md)'s stored inquiry.

"These frontiers can move in different directions. Continued training
might expand the operational frontier while contracting the developmental
one. A new concept might expand the inquiry frontier without improving
immediate task performance."

## Why it holds

The divergence of the first two is [CLAIM-675](CLAIM-675.md) in the learner's own case:
two histories with the same present capability set can leave different
capability sets later. That the cost to acquire is not fixed by the cost
to keep is [CLAIM-569](CLAIM-569.md). That a concept can make a question askable before
it makes it answerable is [CLAIM-475](CLAIM-475.md). The claim's own content is the
developmental frontier as an object with a declared interface, and the
consequence that no context-independent scalar ranks learners; a scalar
objective can, once task distribution, costs, horizon and preferences are
declared (qualified at ChatGPT's review of 2026-11-19, forwarded by the
owner).

## Admission

Tested at the synthesis review of 2026-11-19, because its premises are
claims and it could be only their account. What it adds, in one
sentence: for a learner's own training, and not only for support given
to a party, the frontier of what can still be acquired varies apart from
present competence. Its premises leave that open: [CLAIM-675](CLAIM-675.md) is
demonstrated for support that does a party's work, [CLAIM-569](CLAIM-569.md) for forms
in general, [CLAIM-697](CLAIM-697.md) for elicitation of a fixed system. It passes as a
discriminating prediction. Within one training run of one architecture,
checkpoints with equal operational frontiers on a declared family of
familiar tasks will differ in the budget they need to acquire held-out
task families. The outcome against it is acquisition cost fixed by
present performance across checkpoints. [CASE-294](../cases.d/CASE-294.md) measures exactly
this.

## The stronger reading it invites and does not support

That these three are all there is. A71's own list of routes (in-context
learning, test-time training, sampling, active inquiry) suggests the
developmental frontier depends on which acquisition procedures are
admissible, so it is a family of frontiers indexed by that choice.
Overconsolidation ([CLAIM-758](CLAIM-758.md)) is one pattern of divergence.

## Note of 2026-11-19: follow-up turns of "Topological protection explained"
ChatGPT (A80) proposed a test of the inquiry frontier: after a learner has a strong model, change the environment so the model is incomplete, and compare probe-selection policies (random, uncertainty sampling, information gain, expected free energy, and a planner counting future acquisition costs), asking whether acquired organization changes "the set of probes it can affordably formulate or considers worth performing". It separates "Learning a reusable inquiry strategy" from "Epistemic lock-in", with a forced-probe condition: give a locked-in learner the corrective evidence it would not seek; if it updates, the failure lies in inquiry selection, if not, in inference or plasticity. Two learners with the same present competence and different access to corrective inquiry would show the inquiry frontier moving apart from the operational one. Not run.

## Note of 2026-11-19: Anguita and colleagues, read
<!-- inactive-ok-file: THEORY-tmppm9la — Proposed; cited from the readings of 2026-11-19 -->

Anguita and colleagues (THEORY-tmppm9la, corroborates; NOTE-tmpr453b): in diagonal linear networks with pretraining exact, every relative scale between the layers gives the same pretrained function, the same present capability, yet a different inductive bias for fine-tuning, a different developmental frontier: "even though in diagonal linear networks, the relative scale λP T does not impact the inductive bias of pretraining, it does impact the learned hidden representation and therefore the inductive bias of fine-tuning". And which initialization is best reverses with the declared fine-tuning task: "the optimal learning regime will depend on the task parameters". Independent evidence for the frontiers coming apart, in a solvable model; nothing on their moving in opposite directions over training. McDermott and colleagues (NOTE-tmp074zx) give an analogy only: which later tasks benefit depends on their agreement with the pre-training graph.
