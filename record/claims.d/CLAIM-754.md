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
<!-- inactive-ok-file: THEORY-2077 — Proposed; cited from the readings of 2026-11-19 -->

Anguita and colleagues ([THEORY-2077](../theory.d/THEORY-2077.md), corroborates; [NOTE-2159](../notes.d/NOTE-2159.md)): in diagonal linear networks with pretraining exact, every relative scale between the layers gives the same pretrained function, the same present capability, yet a different inductive bias for fine-tuning, a different developmental frontier: "even though in diagonal linear networks, the relative scale λP T does not impact the inductive bias of pretraining, it does impact the learned hidden representation and therefore the inductive bias of fine-tuning". And which initialization is best reverses with the declared fine-tuning task: "the optimal learning regime will depend on the task parameters". Independent evidence for the frontiers coming apart, in a solvable model; nothing on their moving in opposite directions over training. McDermott and colleagues ([NOTE-2138](../notes.d/NOTE-2138.md)) give an analogy only: which later tasks benefit depends on their agreement with the pre-training graph.

## Note of 2026-11-19: Brown and colleagues, and Howard and Ruder, read
Parallels from two readings. Brown and colleagues ([NOTE-2160](../notes.d/NOTE-2160.md)) treat in-context use and fine-tuning as distinct "points on this spectrum" of task-specific data, with in-context use bounded by its own budget, the context window: the developmental frontier is indexed by admissible procedures, as the claim says. Howard and Ruder ([NOTE-2141](../notes.d/NOTE-2141.md)): one pretrained model reaches a target at very different cost under different fine-tuning procedures (last layer only, full, gradual unfreezing). Neither compares learners of equal present competence, so neither shows the frontiers coming apart.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2059 THEORY-2069 THEORY-2075 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Parallels from the follow-up readings, none naming this claim: the
procedural paper ([THEORY-2075](../theory.d/THEORY-2075.md)) finds the same first phase lowers some
later costs and raises others, with the best transferring component
differing by domain; Hernandez and colleagues ([THEORY-2059](../theory.d/THEORY-2059.md)) find
whether pretraining helps depends on later data and size; Akter and
colleagues ([THEORY-2069](../theory.d/THEORY-2069.md)) find pretraining choices that barely move
base scores move what fine-tuning reaches. Analogies.

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-2086 THEORY-2090 THEORY-2091 THEORY-2092 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

He and colleagues ([THEORY-2092](../theory.d/THEORY-2092.md)) give the clearest illustration on
record: a shortcut model ahead on present held-out accuracy is behind a
grokked one in acquiring compositions with new facts; observational,
single runs, not matched. Ito and colleagues ([THEORY-2091](../theory.d/THEORY-2091.md)) show
networks stopped at one criterion that differ in what they can reach.
Driscoll and colleagues ([THEORY-2090](../theory.d/THEORY-2090.md)) and Furuta and colleagues
([THEORY-2086](../theory.d/THEORY-2086.md)) give interface-relative instances: with learning
confined to one input or to the unfrozen part, what is reachable depends
on what is held and on which part was transferred. Illustrations, not
tests.

## Note of 2026-11-19: Kuhn, read
<!-- inactive-ok-file: THEORY-2094 THEORY-2096 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Structure ([THEORY-2094](../theory.d/THEORY-2094.md)) illustrates the frontiers moving apart: normal
science extends what a community can do while narrowing what it can ask,
and a revolution moves the inquiry frontier, changing problems and
standards, with only partial overlap in what old and new can solve. The
1959 essay, through a stand-in ([THEORY-2096](../theory.d/THEORY-2096.md)), places the formulation
of anomalies in training in a tradition, an inquiry frontier set by
acquired organization. Interpretive.

## Note of 2026-11-23: Lippl and Lindsey, read
<!-- inactive-ok-file: THEORY-tmpw69kb CLAIM-tmp7n00e CLAIM-tmp2tjpt CLAIM-tmpew899 ARG-tmpbvq7y CASE-tmpjn7jc CLAIM-tmp2k67n — Proposed or new; filed by the lead run of 2026-11-23 -->

Lippl and Lindsey ([THEORY-tmpw69kb](../theory.d/THEORY-tmpw69kb.md); [NOTE-tmpw2i45](../notes.d/NOTE-tmpw2i45.md)), the precursor
of Anguita and colleagues, read for the check of the lead that asked for
it: do their regimes already show the same present capability with
different later learning, outside the initialization Anguita and
colleagues generalize? By a step the paper does not take, yes. A
pretrained diagonal linear network and its rescaling after pretraining
(first layer times c, auxiliary readout divided by c) compute the same
function and reach the same functions by readout-only training, yet full
fine-tuning sends them to different solutions, and which c is best
reverses between a main task using a sparse subset of the pretrained
features and one using all of them ([CLAIM-tmp7n00e](CLAIM-tmp7n00e.md), demonstrated, run in
[CASE-tmpjn7jc](../cases.d/CASE-tmpjn7jc.md)). Two readings: two learners with one operational frontier
and two developmental ones ([CLAIM-tmp2tjpt](CLAIM-tmp2tjpt.md), which corroborates this claim
through [ARG-tmpbvq7y](../arguments.d/ARG-tmpbvq7y.md); the assistant's lean), or one learner under two
procedures, since the rescaling is a change of step sizes
([CLAIM-tmp2k67n](CLAIM-tmp2k67n.md)), which instances only this claim's indexing by
procedure ([CLAIM-tmpew899](CLAIM-tmpew899.md), the objection). On either reading, the
readout's re-initialization scale γ gives the same pretrained network
different fine-tuning penalties: the frontier is indexed by procedure.
Nothing on the frontiers moving in opposite directions over training,
since pretraining is always to convergence. No status change.

## Note of 2026-11-23: the scalar once declared
<!-- inactive-ok-file: CLAIM-tmpy87xn CLAIM-tmp6ppvo CLAIM-tmpl9022 — new; filed by the lead run of 2026-11-23 -->

The lead run of 2026-11-23 qualifies this claim's last clause, that a
scalar ranks learning processes once a task distribution, costs, horizon
and evaluative preferences are declared. A fixed task distribution is more
than is needed: a declared law that depends on what has been learned
suffices (CLAIM-tmpy87xn). The list is less than enough: with all four
declared, a learner whose learnability outgrows the discount has no
optimal policy (CLAIM-tmpl9022), so a finite value and attainment must be
added. And "evaluative preferences" must be one valuation across the
selves a policy could produce; when learning changes them, the
preferences of those selves fix no scalar (CLAIM-tmp6ppvo). The claim's
thesis, that the three frontiers move separately, is untouched. Related
by complements; whether the qualification should be an objection is the
owner's call.
