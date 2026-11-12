---
number: 108
status: Open
formerly:
- QUESTION-tmpkbkoh
title: When a structured record does better than a summary, a transcript or a posterior
  on revision tasks, is it because it retains more, because what it retains is easier
  to reach, or because the operations a reviser needs are easier to perform on it?
version: 3
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Line nucleating-argument replaced by records-of-inquiry, at the split of that
    line (ADR-082). No other change.
- version: 3
  date: '2026-11-08'
  note: >-
    Carries nucleating-argument again beside its new line, at ADR-
    tmpyb8vm's rule (version 2): an entry the split moved keeps the old
    line when it answers, refines or objects to one of that line's
    entries, and it refines QUESTION-038. No other change.
tags:
- epistemology
- design-rationale
date: '2026-10-15'
line:
- records-of-inquiry
- nucleating-argument
refines:
- QUESTION-038
summary: >-
  A5's second question, with A3's question B and A4 §4's decomposition: information
  retained, information accessible, information used correctly. The three are different
  findings, and a comparison that does not separate them cannot say which one [CLAIM-295](../claims.d/CLAIM-295.md)
  rests on.
---
<!-- inactive-ok-file: CLAIM-182 CLAIM-184 CLAIM-190 CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: CLAIM-tmp8qsef LIT-tmp9oc9e LIT-tmpiufjk LIT-tmppcaeo LIT-tmpqhq20 — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: LIT-2279 LIT-2281 LIT-2282 SYNTHESIS-015 — Deferred, Proposed; cited in the note of 2026-11-12 for what each holds, not as settled -->

# QUESTION-108: When a structured record does better than a summary, a transcript or a posterior on revision tasks, is it because it retains more, because what it retains is easier to reach, or because the operations a reviser needs are easier to perform on it?

## Why it is a question

A4 §4: "A graph could outperform a summary because it retains more
information, because it retrieves information more reliably, or because
the model is better at executing operations on explicit relationships.
Those are different findings." [QUESTION-038](QUESTION-038.md) asks what turns a persisting
structure into an anchor. This asks which of three mechanisms is doing
the work when one does.

A3's question B, whether structured addressability reduces unannounced
drift, is held here rather than filed apart: it is the drift-measured
special case, and [CLAIM-182](../claims.d/CLAIM-182.md) already states it as a thesis. A3's counter
goes with it: "A structured record may make agents less willing to revise
erroneous commitments. Less drift is not necessarily more epistemic
progress" ([CLAIM-184](../claims.d/CLAIM-184.md)).

An answer is a design that manipulates retention, access budget and
format independently, scored on decisions in an externally specified
environment and not on reproducing the record's own graph ([CLAIM-190](../claims.d/CLAIM-190.md)).
[CASE-091](../cases.d/CASE-091.md) is that design. A negative result counts: "if narrative summaries or
latent representations preserve the same revision competence more
efficiently, that tells us something about the limits of nucleation's
architecture."

## Note of 2026-11-12: the owner's "equip an agent with luria", and the ablations proposed, from "luria experiment design"

At U10 of the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) the owner asked for evaluations, "e.g. equip an agent with
luria and evaluate the agent against some task". A's proposals bear on this
question's three mechanisms, retaining more, easing retrieval, making
operations cheap:

- A27 and A29: run MEME ([LIT-2281](../literature.d/LIT-2281.md), unread), whose Cascade and Absence tasks
  test dependent facts that stop holding, with plain files, retrieval, a
  typed record, and a typed record with checks, under two ingestion modes:
  every arm given the same gold extracted facts, which isolates
  representation and retrieval, and every arm ingesting raw conversation,
  which tests the whole workflow. Ingestion cost is reported apart from
  query cost: "A structured record could gain on update handling while
  losing badly on time and tokens spent writing records."
- A32: hold the record's contents fixed and vary access, a shared
  transcript, indexed notes, a typed record, a governed one, citing this
  question for the split.
- A36 E1: on [CLAIM-293](../claims.d/CLAIM-293.md)'s two worlds, "A Luria agent that simply follows
  graph edges and reaches the same conclusion in both situations has failed
  the substantive task"; and a targeted dependency report against the full
  graph, since a gain there would put the value in "making an operation
  cheap, not in graph structure as such". [CASE-091](../cases.d/CASE-091.md) holds the design these
  extend.
- A17: a counter-effect to test for, that "a well-structured record might
  anchor the assistant too strongly to its existing explanatory
  vocabulary" ([SYNTHESIS-015](../syntheses.d/SYNTHESIS-015.md), [CLAIM-184](../claims.d/CLAIM-184.md)).

A20 and A27 named agent-memory systems as comparators: Generative Agents
([LIT-tmpiufjk](../literature.d/LIT-tmpiufjk.md)), HippoRAG ([LIT-tmp9oc9e](../literature.d/LIT-tmp9oc9e.md)), A-MEM ([LIT-tmpqhq20](../literature.d/LIT-tmpqhq20.md)), GraphRAG
([LIT-tmppcaeo](../literature.d/LIT-tmppcaeo.md)), LongMemEval ([LIT-2282](../literature.d/LIT-2282.md)) and MemoryAgentBench ([LIT-2279](../literature.d/LIT-2279.md)), all
unread. [CLAIM-tmp8qsef](../claims.d/CLAIM-tmp8qsef.md) bears on the third mechanism: what the record makes
cheap is finding the dependants, not deciding them. Open.
