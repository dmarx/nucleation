---
number: 271
status: Open
formerly:
- QUESTION-tmpdicvf
title: 'How can an organization evaluate its own processes so that the evaluation decides authority without being captured by it: when wins among the processes cycle, when no common scale scores them all, when the processes in charge can add, filter or duplicate the tests, and when only the processes heeded are evaluated?'
version: 4
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A41 and A47 asked it again, and CASE-158
    proposes one arm per failure. The question is unchanged.
- version: 3
  date: '2026-10-26'
  note: >-
    A dated note added: CASE-158's arms for failures 3 and 4 run in
    proxy form, filtering of tests run in a population with a known-
    propensity correction (CASE-162), and the cost of a diagnostic
    (CASE-163). The question is unchanged.
- version: 4
  date: '2026-11-04'
  note: >-
    Vocabulary only, under ADR-070: "endorse" in TERM-053's sense now
    reads conferral (TERM-103) or grant (TERM-101). The
    content is unchanged.
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
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070 (conferral, TERM-103; grant, TERM-101); cited as the term of its time -->
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: THEORY-tmp37mxv THEORY-tmpdjm1o THEORY-tmpl4czv THEORY-tmpq26fh — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# QUESTION-271: How can an organization evaluate its own processes so that the evaluation decides authority without being captured by it: when wins among the processes cycle, when no common scale scores them all, when the processes in charge can add, filter or duplicate the tests, and when only the processes heeded are evaluated?

## The question

The record's governance claims all lean on an evaluation of processes:
- grants that track competence ([TERM-101](../terms.d/TERM-101.md); [CLAIM-277](../claims.d/CLAIM-277.md));
- a learned prior trained by outcomes ([CLAIM-443](../claims.d/CLAIM-443.md));
- evidence-tracking authority as Bayes' rule ([CASE-155](../cases.d/CASE-155.md));
- a legibility regime that can score in its own favour ([CASE-124](../cases.d/CASE-124.md)'s μ route).

Four ways the evaluation can fail are now on file:
1. **Cycles.** Wins among processes need admit no ordering ([TERM-077](../terms.d/TERM-077.md),
   [CLAIM-451](../claims.d/CLAIM-451.md)), so no ranking is fixed by the record alone.
2. **No common scale.** Processes with different concerns have no shared
   score ([CLAIM-436](../claims.d/CLAIM-436.md), [CLAIM-437](../claims.d/CLAIM-437.md)). The BoostTheVote model of 2014 assumes an
   objective metric that its author says "probably/almost certainly cannot"
   be constructed.
3. **Capture of the tests.** The processes in charge can add, filter or
   duplicate the items they are scored on. [CASE-155](../cases.d/CASE-155.md)'s self-scoring c
   then gives lock-in above a threshold.
4. **Bandit feedback.** Only the process heeded gets evaluated, so the
   unheeded can never earn authority back. That is the hive mind's
   architecture ([THEORY-899](../theory.d/THEORY-899.md)), avoidance's identifiability problem
   ([CLAIM-446](../claims.d/CLAIM-446.md)), and the case [QUESTION-270](QUESTION-270.md) asks about.

## What would answer it

For each failure, a procedure with a stated guarantee, and the price of
the guarantee. The candidates registered with this question have been read
(curation entry of 2026-10-24, 2nd), and the readings cut each guarantee
down:

- **Copies of tests (3).** Nash averaging ([THEORY-946](../theory.d/THEORY-946.md)) resists exact
  copies only when the meta-game's equilibrium is unique. With ties, one
  copy of a null agent moves the maximum-entropy equilibrium and other
  agents' averages: [NOTE-1155](../notes.d/NOTE-1155.md)'s counterexample, which was re-derived
  when filed. The value between populations ([THEORY-944](../theory.d/THEORY-944.md)) needs no
  unique equilibrium, but it ranks coalitions, not members. α-Rank,
  according to its reader's own check, not the paper's, moves when a
  strategy is duplicated ([NOTE-1156](../notes.d/NOTE-1156.md)).
- **Cycles (1).** α-Rank ranks uniquely at each finite α. Its large-α
  limit picks out the sinks of the better-response graph ([THEORY-942](../theory.d/THEORY-942.md)).
  Collapsing each strongly connected component of the win graph to a point
  always leaves an acyclic quotient, so an ordering exists one level up.
- **Bandit feedback (4).** Counterfactual credit (COMA, [THEORY-925](../theory.d/THEORY-925.md))
  values an action only from the times it was taken, so its price is an
  exploration floor on every action. That is protected access again, not
  an escape from it. In Q-learning, updating only the chosen option adds a
  factor of its own frequency ([THEORY-932](../theory.d/THEORY-932.md)), and inverse-frequency
  weighting is the exact correction.
- **No common scale (2).** Peer prediction ([THEORY-943](../theory.d/THEORY-943.md)) scores
  without ground truth only by substituting the centre's model of how
  honest reports correlate, and truth-telling is one equilibrium among
  uninformative ones. That is the capture regime with no evidence. The
  Bayesian truth serum was sought and is Unavailable. Wolpert and Tumer's
  "factored" utilities ([THEORY-939](../theory.d/THEORY-939.md)) and the monotone mixing of value
  decomposition ([THEORY-929](../theory.d/THEORY-929.md)) state, member by member and ordinally,
  when a member's own ranking agrees with the collective's. That is the
  regime in which no scale needs to be common.
- **Load balancing in mixtures of experts** ([THEORY-927](../theory.d/THEORY-927.md)) imposes equal
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
cycles, no common scale, bandit feedback and capture. [CASE-158](../cases.d/CASE-158.md)
proposes one arm per failure against a router baseline. The question is
unchanged.

## Note of 2026-10-26: two failures run, in weakened form

<!-- inactive-ok-file: CASE-163 — Proposed; the lab's runs filed 2026-10-26 and the reading on inverse-frequency weighting, cited as bearing on failures 3 and 4, not as answering them -->

- **Proxies in [CASE-158](../cases.d/CASE-158.md)'s design** (v1.1, [CASE-162](../cases.d/CASE-162.md),
  dmarx/PerspectiveLab@7e2edc2). An evaluator scored 80% on agreement
  with the current mixture stands in for capture, and audits attributed to
  one specialist per receiver stand in for bandit feedback. The lab's own
  report says both are weaker than the real failures. The router faces
  the same audit delay and cost, and has the lower error in all four
  cells. Under 80% capture neither recovers on any seed.
- **Filtered tests** (v1.3, [CASE-162](../cases.d/CASE-162.md)). When admission of cues
  depends on the incumbent's record, 41 of 64 worlds keep the worse
  alternative in charge at s = 0.75 and at s = 1, with no self-scoring.
  Weighting by the exact inverse admission propensity brings that to 0
  and 5. That is [THEORY-932](../theory.d/THEORY-932.md)'s inverse-frequency correction applied to
  filtering, and it works only with known propensities that stay
  positive. It does not undo self-scoring: 39 of 64 at c = 0.5 with
  nothing filtered, before and after.
- **The cost of a diagnostic** (v2.1, [CASE-163](../cases.d/CASE-163.md),
  dmarx/PerspectiveLab@9f82bfd). A probe that separates mechanisms costs
  damage, and a more damaging probe can be the less informative one.

Cycles, no common scale, duplicated tests, and unknown or zero
propensities are not touched. The question is unchanged.

## Note of 2026-11-12: the question met in a self-improving collective, from "luria experiment design"

A41 and A43 of the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) meet this question in a team that improves its own
research process: "The system may become better at satisfying the
mechanism that judges improvement, rather than better at the underlying
task." A43 compares self-scored, externally scored and layered
arrangements, and marks where a record cannot answer it alone: "A Git-based
approval policy does not independently protect anything when the agent can
also modify the branch protections, tests and approval credentials." "This
is a boundary of the implementation, not something that can be solved by
stronger instructions in the record." The test is in [CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md). Open.

## Note of 2026-11-12: 4 readings of the works of "luria experiment design"

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Liu and Yadav** (THEORY-tmp37mxv): The benchmark keeps the scorer (deterministic assertions) outside the agent for state tasks, but uses LLM judges for procedure and user experience. That is a mixed instance of separating evaluator from optimized system.
- **Lu et al.** (THEORY-tmpl4czv): Bears as an example. The authors validate the judge against human decisions once, then rely on it.
- **Srikanth et al.** (THEORY-tmpdjm1o): The improvers do not control the grade; leaves open.
- **Bao et al.** (THEORY-tmpq26fh): **bears on, leaves open**. A reward model trained on expert judgements beats the human agreement floor; the paper itself warns it distils "current taste", not the practice by which criteria change.

The question is unchanged.
