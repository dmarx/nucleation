---
status: Open
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
<!-- inactive-ok-file: THEORY-tmpm09s4 THEORY-tmpsw2ct — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-576 CLAIM-697 CLAIM-tmp1l2s7 CLAIM-tmp5gbzr CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# QUESTION-tmpwqepn: What would make a learning process optimal, when some of the most valuable consequences of learning are changes in what the learner can later learn, ask and afford, which cannot be specified in advance; and when is investing in future learnability better than improving present competence?

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
  [LIT-tmphr4nm](../literature.d/LIT-tmphr4nm.md)), so the record's addition can only be the resource and
  repertoire accounting, not the objective.
- **Robust and open-ended forms** (A48 §5): a max–min over a family of
  task distributions; empowerment as a measure of flexibility
  ([THEORY-1344](../theory.d/THEORY-1344.md)), which is not substantive freedom ([CLAIM-352](../claims.d/CLAIM-352.md)).
- **Not maximum learning** (A48 §3): information that changes no
  consequential decision is not worth acquiring ([CLAIM-520](../claims.d/CLAIM-520.md)).
- **Investment across acquisitions**: an acquisition can be worth making
  for what it does to the cost of other acquisitions, even at a loss on
  its own ([CLAIM-tmp5gbzr](../claims.d/CLAIM-tmp5gbzr.md)).
- **The three frontiers** ([CLAIM-tmp1l2s7](../claims.d/CLAIM-tmp1l2s7.md)): operational, developmental
  and inquiry capability move separately, so no single frontier is the
  objective.
- **The failure** to avoid: overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)).

## What would answer it

A definition that ranks learning policies in a stated class of
environments and survives the case where the task distribution itself
depends on what the learner becomes, with a measurable proxy for the
developmental frontier. [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md) proposes the measurement for one
family of models.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Finn, Abbeel and Levine (THEORY-tmpsw2ct), read: supports the first candidate answer's caveat. MAML's objective is the loss after adaptation on tasks from a declared distribution p(T), parameters "easy to fine-tune" in their words. The future it targets is that declared p(T) and a declared budget of one to a few gradient steps, so it does not reach the question's case of benefits that cannot be specified in advance. The record's addition, resource and repertoire accounting beyond a declared family, stands.

Hospedales, Antoniou, Micaelli and Storkey (THEORY-tmpm09s4), skimmed: supports the same caveat across the field. They define meta-learning by an explicit objective that improves "future learning performance", and list objectives for speed, asymptotic performance, robustness and continual retention (§4.3, §5.7). Every one presupposes a declared task family or episode design. The survey lists generalization to other task distributions, and settings with no task family, as open (§6), which is the question's unspecifiable future.

No status change.
