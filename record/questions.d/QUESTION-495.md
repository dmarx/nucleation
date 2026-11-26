---
number: 495
status: Open
formerly:
- QUESTION-tmpwqepn
title: 'What would make a learning process optimal, when some of the most valuable consequences of learning are changes in what the learner can later learn, ask and afford, which cannot be specified in advance; and when is investing in future learnability better than improving present competence?'
version: 1
tags:
- learning-theory
- complex-systems
date: '2026-11-19'
line:
- realizability
- learned-structure
- readiness
summary: >-
  The owner's, from U21 of the exchange "Topological protection explained"
  (2026-11-19): "how might we formulate a notion of 'optimal learning'",
  after U20: "I feel like we're reasonably appropriately situated to make
  general claims about how learning works". A48 answered with a
  context-relative definition and an open problem; A50 §8 and A71 §13
  asked the narrower form, when learning widens the frontier of future
  learning rather than concentrating present competence. The record holds
  the parts: capability trajectories ([CLAIM-675](../claims.d/CLAIM-675.md)), the conditional value of
  keeping a corrective capacity ([CLAIM-520](../claims.d/CLAIM-520.md)), resource-indexed repertoires
  ([CLAIM-576](../claims.d/CLAIM-576.md), [CLAIM-697](../claims.d/CLAIM-697.md)), and the questions a realized specification
  makes askable ([CLAIM-475](../claims.d/CLAIM-475.md)). The question's wording is the filer's,
  joining the owner's U21 to A's open problems.
---
<!-- inactive-ok-file: THEORY-2034 THEORY-2046 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-294 CLAIM-576 CLAIM-697 CLAIM-754 CLAIM-756 CLAIM-758 — Proposed; cited in this filing of 2026-11-19 -->

# QUESTION-495: What would make a learning process optimal, when some of the most valuable consequences of learning are changes in what the learner can later learn, ask and afford, which cannot be specified in advance; and when is investing in future learnability better than improving present competence?

## Why it is a question

The owner, at U20 and U21 of the exchange "Topological protection
explained" (https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf):

> I feel like we're reasonably appropriately situated to make general claims about how learning works

> how might we formulate a notion of "optimal learning"

A48 separated optimal inference, optimal learning and optimal
learnability, the last being how a system should be organized so that
acquiring further capabilities becomes cheaper. It closed on "How can
learning be optimal when some of its most important future benefits
cannot yet be specified by the learner?" A50 §8 asked for "a general
measure of how much further organization remains practically accessible
from a learner's current state",
and A71 §13 for when changes "expand the accessible frontier of future
learning, rather than merely concentrating present competence".

## Candidate answers on record

- **A context-relative definition** (A48 §10): optimal only relative to a
  declared family of tasks, budget, horizon and evaluation, counting the
  costs of acquiring, operating, maintaining and revising organization;
  Pareto, viability or robustness where no scalar exists. Optimal learning
  is a policy over that trajectory, not the best final model (A71 §9).
  Meta-learning's objective already targets future adaptability (A54 §3;
  [LIT-2816](../literature.d/LIT-2816.md)), so the record's addition can only be the resource and
  repertoire accounting, not the objective.
- **Robust and open-ended forms** (A48 §5): a max–min over a family of
  task distributions; empowerment as a measure of flexibility
  ([THEORY-1344](../theory.d/THEORY-1344.md)), which is not substantive freedom ([CLAIM-352](../claims.d/CLAIM-352.md)).
- **Not maximum learning** (A48 §3): information that changes no
  consequential decision is not worth acquiring ([CLAIM-520](../claims.d/CLAIM-520.md)).
- **Investment across acquisitions**: an acquisition can be worth making
  for what it does to the cost of other acquisitions, even at a loss on
  its own ([CLAIM-756](../claims.d/CLAIM-756.md)).
- **The three frontiers** ([CLAIM-754](../claims.d/CLAIM-754.md)): operational, developmental
  and inquiry capability move separately, so no single frontier is the
  objective.
- **The failure** to avoid: overconsolidation ([CLAIM-758](../claims.d/CLAIM-758.md)).

## What would answer it

A definition that ranks learning policies in a stated class of
environments and survives the case where the task distribution itself
depends on what the learner becomes, with a measurable proxy for the
developmental frontier. [CASE-294](../cases.d/CASE-294.md) proposes the measurement for one
family of models.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Finn, Abbeel and Levine ([THEORY-2046](../theory.d/THEORY-2046.md)), read: supports the first candidate answer's caveat. MAML's objective is the loss after adaptation on tasks from a declared distribution p(T), parameters "easy to fine-tune" in their words. The future it targets is that declared p(T) and a declared budget of one to a few gradient steps, so it does not reach the question's case of benefits that cannot be specified in advance. The record's addition, resource and repertoire accounting beyond a declared family, stands.

Hospedales, Antoniou, Micaelli and Storkey ([THEORY-2034](../theory.d/THEORY-2034.md)), skimmed: supports the same caveat across the field. They define meta-learning by an explicit objective that improves "future learning performance", and list objectives for speed, asymptotic performance, robustness and continual retention (§4.3, §5.7). Every one presupposes a declared task family or episode design. The survey lists generalization to other task distributions, and settings with no task family, as open (§6), which is the question's unspecifiable future.

No status change.

## Note of 2026-11-19: follow-up turns of "Topological protection explained"
<!-- inactive-ok-file: CLAIM-763 — Proposed or Deferred; cited from the follow-up turns filed 2026-11-19 -->

ChatGPT (A84) ranks this question foundational in its triage ([CLAIM-763](../claims.d/CLAIM-763.md)), as philosophical and decision-theoretic analysis of the evaluative standard. The questions it adds: "Should a learner preserve future adaptability even when its expected instrumental value is currently low?"; "Is the ability to acquire further capabilities intrinsically valuable or merely instrumentally useful?"; and which future possibilities must remain open for learning to count as "flourishing, autonomous, or well-governed". A next advance without an experiment: "Show which assumptions are necessary for a scalar optimum to exist". It also applies the question to the record itself: research triage faces the same problem ([CLAIM-763](../claims.d/CLAIM-763.md)).

## Note of 2026-11-19: the pretraining works, read
Two readings bear on the worry that the value of learning cannot be specified in advance. McDermott and colleagues ([NOTE-2138](../notes.d/NOTE-2138.md)) give a partial criterion: a later task benefits from pre-training as far as it is smooth over the structure pre-training induced, so given that structure, which unknown tasks will benefit is partly predictable. Anguita and colleagues ([NOTE-2159](../notes.d/NOTE-2159.md)) show a pretraining-time choice, the initialization's scales, whose value appears only at fine-tuning and depends on which task comes. Analogies to the question's object; no answer.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2081 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Stern and colleagues ([THEORY-2081](../theory.d/THEORY-2081.md)) give a narrow empirical case where
investing in later learnability does not pay at matched compute except in
very data-poor additive settings. Hernandez and colleagues
([THEORY-2059](../theory.d/THEORY-2059.md)) propose using their transfer exponent to choose between
collecting more fine-tuning data and growing the model, and list the ideal
pretraining ratio for a data-limited target as open.

## Note of 2026-11-19: Kuhn, read
<!-- inactive-ok-file: THEORY-2094 THEORY-2096 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

A partial historical answer from Kuhn ([THEORY-2094](../theory.d/THEORY-2094.md), and through a
stand-in [THEORY-2096](../theory.d/THEORY-2096.md)): invest in the paradigm while its tools keep
solving its problems, retool only at crisis, and keep the capacity to
change through variable individual judgement and new entrants; deep
investment in present competence is itself what pays for later
revolutionary learning, which cuts against reading the question as a
choice between the two.

## Note of 2026-11-23: the conditions for a scalar optimum
<!-- inactive-ok-file: CLAIM-1197 CLAIM-1036 CLAIM-1130 ARG-227 — new; filed by the lead run of 2026-11-23 -->

The lead run for ChatGPT's "Show which assumptions are necessary for a
scalar optimum to exist" filed three claims and an argument. An optimal
learning policy is a scalar optimum under a declared task law, one
valuation, a finite value and attainment ([CLAIM-1197](../claims.d/CLAIM-1197.md)); the task law
may depend on what has been learned, so the question's case of a task
distribution that depends on what the learner becomes does not by itself
defeat a definition. What does: a valuation that learning changes, where
the evaluator that gives an optimum, the present self, excludes by
construction the benefits that cannot be specified in advance
([CLAIM-1036](../claims.d/CLAIM-1036.md)); and learnability that outgrows the discount, where
investing in it is always better and so no amount is best
([CLAIM-1130](../claims.d/CLAIM-1130.md)). The independence of the conditions is [ARG-227](../arguments.d/ARG-227.md). It
narrows what would answer the question: a definition must declare an
evaluator across valuations, or bound the growth of learnability. No
status change.

## Note of 2026-11-26: Veeriah et al. (2019), read

<!-- inactive-ok-block: THEORY-tmpl9xun NOTE-tmpibrnu LIT-tmpl1kcf — new; the reading this note reports -->

Bears on the question. LIT-tmpl1kcf (NOTE-tmpibrnu) invests in future
learnability directly: it chooses what to predict by its effect on later
learning, and shows that valuing only the immediate effect fails. The
valuation is one fixed task over a truncated horizon, so the question's
hard part, consequences that cannot be specified in advance, is not
reached. THEORY-tmpl9xun `bears_on` this question. No status change.
