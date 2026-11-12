---
status: Read
paper: LIT-2283
title: 'Buçinca, Malaya and Gajos — To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2102.09692. A delegated
    reader drafted the reading; quotations were rechecked by script against
    the downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  People given AI recommendations with explanations often follow them when
  they are wrong. The authors read this through dual-process theory: people
  form a general heuristic about whether to trust the AI instead of engaging
  each explanation. They test three "cognitive forcing functions" on a
  nutrition task (replace the highest-carbohydrate ingredient on a plate)
  with a simulated AI that is right 75% of the time: *on demand* (AI
  suggestion hidden until requested), *update* (user decides first, then
  sees the AI and may revise) and *wait* (30 s delay before the AI's
  answer).
---

# NOTE-tmp7uwd1: Buçinca, Malaya and Gajos — To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making

## Contribution

Introduces cognitive forcing functions as an interaction-design intervention against
overreliance on AI advice, shows a trade-off between their effectiveness and their acceptability,
and an unequal benefit by cognitive motivation.

## Key results

1. Hypothesis and premise (§1): people "develop heuristics about the competence of the AI partner overall".
2. Overreliance reduced, not removed (§5): "the cognitive forcing functions reduced, but not yet eliminated, overreliance on the AI".
3. No overall performance gain (§5): "There was no significant difference in performance between simple explainable AI approaches and cognitive forcing functions" (H1b not supported).
4. Acceptability trade-off (§5): "people performed best in conditions that they preferred and trusted the least, and that they rated as the most difficult".
5. Unequal benefit (§5): improvements "held mostly for people with high NFC".
6. Baseline (§5): when the AI was incorrect, "people aided by the simple explainable AI approaches performed less well than people who had no AI support".
7. Proxy tasks (§5): evaluations with proxy tasks "are likely to produce more optimistic results".

## Assumptions

Single, low-stakes lay task; simulated AI with fixed 75% accuracy and designed errors; MTurk
participants with a performance bonus; overreliance operationalised as choosing the AI's wrong
answer when the participant (or the no-AI group) would have done better.

## Concepts

Overreliance; dual-process theory (System 1 / System 2); cognitive forcing function (on demand,
update, wait); simple explainable AI; Need for Cognition; intervention-generated inequality;
proxy task vs actual decision task.

## Bearing on the record

[CASE-188](../cases.d/CASE-188.md)'s note lists "cognitive forcing ([LIT-2283](../literature.d/LIT-2283.md))" among A39 Study C's prior work on revision,
and [LIT-tmpyaj3n](../literature.d/LIT-tmpyaj3n.md) says [LIT-2283](../literature.d/LIT-2283.md) is "held". Both are bare pointers and **accurate** as far as they
go. The work is about a human deciding whether to defer to an advisor, not about belief revision
by an agent or a team; it bears on revision only through the *update* condition (decide first,
then see the advice and revise). It does not show that forcing improves overall performance.

- **[CASE-188](../cases.d/CASE-188.md)** (corrigible resolve vs entrenchment; A36 E7 adds false retraction vs failure to
  retract): **qualifies the design's prior art.** The paper's outcome split, overreliance (adopting
  a wrong external signal) against human error, maps onto "false retraction" when external advice
  is wrong. It also shows the cost of the check is borne in acceptability, and that the
  intervention's benefit depends on a trait of the reviser, a moderator the case does not vary.
- **[CLAIM-349](../claims.d/CLAIM-349.md)** (access to a signal, its authority, and action on it are separable; adaptive
  regulation keeps access and makes authority conditional on evidence): **supports, as a human
  instance.** The *on demand* and *update* conditions keep access to the AI's signal while delaying
  or conditioning its authority, and they reduce acting on wrong signals; but the paper's no-AI
  arm still does best on wrong-AI items, so conditional authority here does not reach the
  performance of no access on those items.
- **[LIT-tmpyaj3n](../literature.d/LIT-tmpyaj3n.md)** (Bansal et al., explanations raise acceptance): the paper cites the same line
  of work ([2] in its numbering) for explanations as a "general signal of competence"; consistent.

## Limitations

One task, one simulated AI accuracy, lay participants online; the authors name "a single
non-critical decision-making task" as their key limitation (§5).
