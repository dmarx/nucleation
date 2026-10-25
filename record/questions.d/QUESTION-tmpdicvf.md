---
status: Open
title: 'How can an organization evaluate its own processes so that the evaluation decides authority without being captured by it: when wins among the processes cycle, when no common scale scores them all, when the processes in charge can add, filter or duplicate the tests, and when only the processes heeded are evaluated?'
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A41 and A47 asked it again, and CASE-tmpjmerx
    proposes one arm per failure. The question is unchanged.
tags:
- self-governance
- game-theory
- learning-theory
date: '2026-10-24'
line: distributed-agency
summary: >-
  Filed at the owner's direction, 2026-10-24, with the registration of
  works from multi-agent reinforcement learning and learning in games,
  after the owner asked how the record stands on MARL. The governance line
  keeps returning to one gap: the scoring that allocates authority is
  itself governed. The replicator construction makes that gap a lock-in
  threshold, and BoostTheVote assumes it away with an objective metric.
  The question asks what evaluation procedures resist capture, and in
  which of four senses.
---

# QUESTION-tmpdicvf: How can an organization evaluate its own processes so that the evaluation decides authority without being captured by it: when wins among the processes cycle, when no common scale scores them all, when the processes in charge can add, filter or duplicate the tests, and when only the processes heeded are evaluated?

## The question

The record's governance claims all lean on an evaluation of processes:
- endorsement that tracks competence ([CLAIM-277](../claims.d/CLAIM-277.md));
- a learned prior trained by outcomes ([CLAIM-tmp0qupq](../claims.d/CLAIM-tmp0qupq.md));
- evidence-tracking authority as Bayes' rule ([CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md));
- a legibility regime that can score in its own favour ([CASE-124](../cases.d/CASE-124.md)'s μ route).

Four ways the evaluation can fail are now on file:
1. **Cycles.** Wins among processes need admit no ordering ([TERM-077](../terms.d/TERM-077.md),
   [CLAIM-tmpuxcp6](../claims.d/CLAIM-tmpuxcp6.md)), so no ranking is fixed by the record alone.
2. **No common scale.** Processes with different concerns have no shared
   score ([CLAIM-436](../claims.d/CLAIM-436.md), [CLAIM-437](../claims.d/CLAIM-437.md)). The BoostTheVote model of 2014 assumes an
   objective metric that its author says "probably/almost certainly cannot"
   be constructed.
3. **Capture of the tests.** The processes in charge can add, filter or
   duplicate the items they are scored on. [CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md)'s self-scoring c
   then gives lock-in above a threshold.
4. **Bandit feedback.** Only the process heeded gets evaluated, so the
   unheeded can never earn authority back. That is the hive mind's
   architecture ([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)), avoidance's identifiability problem
   ([CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md)), and the case [QUESTION-tmponjie](QUESTION-tmponjie.md) asks about.

## What would answer it

For each failure, a procedure with a stated guarantee, and the price of
the guarantee. The candidates registered with this question have been read
(curation entry of 2026-10-24, 2nd), and the readings cut each guarantee
down:

- **Copies of tests (3).** Nash averaging ([THEORY-tmpzogk3](../theory.d/THEORY-tmpzogk3.md)) resists exact
  copies only when the meta-game's equilibrium is unique. With ties, one
  copy of a null agent moves the maximum-entropy equilibrium and other
  agents' averages: [NOTE-tmpr1f7n](../notes.d/NOTE-tmpr1f7n.md)'s counterexample, which was re-derived
  when filed. The value between populations ([THEORY-tmpxh6cj](../theory.d/THEORY-tmpxh6cj.md)) needs no
  unique equilibrium, but it ranks coalitions, not members. α-Rank,
  according to its reader's own check, not the paper's, moves when a
  strategy is duplicated ([NOTE-tmpxufhw](../notes.d/NOTE-tmpxufhw.md)).
- **Cycles (1).** α-Rank ranks uniquely at each finite α. Its large-α
  limit picks out the sinks of the better-response graph ([THEORY-tmpwc2nk](../theory.d/THEORY-tmpwc2nk.md)).
  Collapsing each strongly connected component of the win graph to a point
  always leaves an acyclic quotient, so an ordering exists one level up.
- **Bandit feedback (4).** Counterfactual credit (COMA, [THEORY-tmp1p6ly](../theory.d/THEORY-tmp1p6ly.md))
  values an action only from the times it was taken, so its price is an
  exploration floor on every action. That is protected access again, not
  an escape from it. In Q-learning, updating only the chosen option adds a
  factor of its own frequency ([THEORY-tmpar5jw](../theory.d/THEORY-tmpar5jw.md)), and inverse-frequency
  weighting is the exact correction.
- **No common scale (2).** Peer prediction ([THEORY-tmpx9mep](../theory.d/THEORY-tmpx9mep.md)) scores
  without ground truth only by substituting the centre's model of how
  honest reports correlate, and truth-telling is one equilibrium among
  uninformative ones. That is the capture regime with no evidence. The
  Bayesian truth serum was sought and is Unavailable. Wolpert and Tumer's
  "factored" utilities ([THEORY-tmpomtdz](../theory.d/THEORY-tmpomtdz.md)) and the monotone mixing of value
  decomposition ([THEORY-tmp56jxv](../theory.d/THEORY-tmp56jxv.md)) state, member by member and ordinally,
  when a member's own ranking agrees with the collective's. That is the
  regime in which no scale needs to be common.
- **Load balancing in mixtures of experts** ([THEORY-tmp2p13l](../theory.d/THEORY-tmp2p13l.md)) imposes equal
  use whatever the competence. It is imposed diversity, not protected
  access, and it works against a rare specialist.

An answer would also say which guarantees can hold together. The obvious
worry is that resistance to duplicated tests needs a game-theoretic
solution concept, and that concept fixes a scale.

## What it is not

It is not [QUESTION-087](QUESTION-087.md), whether a self-reproducing authority structure
can be pathological by a standard it did not set. That question asks for
the standard. This one asks for procedures, given candidate standards, and
what each makes impossible to capture.

## Note of 2026-10-25: asked again, and an arm per failure

Asked again without citation at A41 of the exchange of 2026-10-24,
continued: "under what conditions an organization can evaluate a proposed
change to its governing rules without relying exclusively on the very
evaluation regime being challenged". A41's minimal model blends
historical audit with conformity under a weight α that can itself be
amended. Audit-accountable amendment beat fixed historical scoring on 3 of
10 seeds. At A47, after a contextual router beat audited governance on
every seed, the reply put the framework's possible contribution in tasks
where evaluation "becomes contested, incomplete, selectively observed, or
historically entrenched". Those are, nearly one for one, this question's
cycles, no common scale, bandit feedback and capture. [CASE-tmpjmerx](../cases.d/CASE-tmpjmerx.md)
proposes one arm per failure against a router baseline. The question is
unchanged.
