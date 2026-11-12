---
number: 91
status: Active
formerly:
- CASE-tmpy6hv9
title: 'A memory ablation for revision: synthetic inquiries with known ground truth,
  run under six kinds of persistent memory, with information and token budget controlled
  separately'
version: 2
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Line nucleating-argument replaced by records-of-inquiry, at the split of that
    line (ADR-082). No other change.
standing: stipulated
kind: proposed-study
tags:
- epistemology
- design-rationale
date: '2026-10-15'
line:
- records-of-inquiry
summary: >-
  A6's fifth case, refined from A3, A4 §4 and A5. The design [QUESTION-108](../questions.d/QUESTION-108.md) asks
  for. Not run.
---
<!-- inactive-ok-file: CLAIM-184 CLAIM-190 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpmvfl2 — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: LIT-2272 — Deferred; cited in the note of 2026-11-12 for what each holds, not as settled -->

# CASE-091: A memory ablation for revision: synthetic inquiries with known ground truth, run under six kinds of persistent memory, with information and token budget controlled separately

## The case

Synthetic inquiries with known ground truth pass through hypothesis
choice, accumulation, misleading evidence, discovery of a defective
source, and possible reopening. Agents are randomized to six memories:
current conclusions and confidence; a narrative summary; raw history with
retrieval; a justification graph; a graph with evidence attributes and
revisions; a task-optimized compression.

Two arms. In one every memory has access to the same facts, which tests
access and format. In the other each gets a fixed compression budget,
which tests what it keeps.

Outcomes, in order: decisions on revision tasks scored in the generating
environment, not reproduction of the record's graph ([CLAIM-190](../claims.d/CLAIM-190.md)); whether
the agent can reconstruct its earlier grounds; and rigidity, whether
anchoring keeps a conclusion past when it should have gone ([CLAIM-184](../claims.d/CLAIM-184.md)).

## What each outcome would show

A6: it could tell apart "Structured memory retains more
revision-relevant information under compression", "makes retained
information more accessible to bounded models" and "improves the
execution of revision procedures given equivalent information", or show
that "the apparent advantages of structured memory disappear when
information content and computation are adequately controlled."

## Main threat

A6: "Success in synthetic environments would not automatically establish
that the same representations are sufficient for open-ended scientific
inquiry, where the state space, relevant variables, available
interventions, and even the appropriate questions can change over time."
That is [QUESTION-112](../questions.d/QUESTION-112.md).

## Note of 2026-11-12: the same two controls, proposed again for agent teams, from "luria experiment design"

A36 E1 and A39 §10 of the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) propose this case's separation of
information from budget for a study of agents equipped with the record:
"In an information-equivalent experiment, each condition gets the same
relevant facts, allowing us to compare access and operations. In a
budget-equivalent experiment, each condition gets the same storage,
retrieval, and processing budget". A cites this case for it. A36 adds a
trial on [CLAIM-293](../claims.d/CLAIM-293.md)'s two worlds of equal topology, and a targeted
dependency report as an arm. A39 adds a precedent from group research:
transactive-memory experiments that separate knowing who knows what from
communication itself ([LIT-tmpmvfl2](../literature.d/LIT-tmpmvfl2.md) and [LIT-2272](../literature.d/LIT-2272.md), unread). The design is
unchanged; the study remains unrun.
