---
status: Read
paper: LIT-2282
title: 'Wu et al. — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2410.10813. **Read**
    (2026-11-12): main text §§1–6 read; appendices skimmed. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  A benchmark of 500 hand-written questions, each embedded in a coherent,
  length-configurable history of user–assistant sessions (≈115K tokens in
  the S setting; 500 sessions, ≈1.5M tokens, in M), testing five abilities:
  information extraction, multi-session reasoning, temporal reasoning,
  knowledge updates and abstention. In a pilot, commercial memory assistants
  (ChatGPT, Coze) and long-context LLMs lose much accuracy relative to
  reading only the evidence. The authors then decompose memory design into
  indexing, retrieval and reading, with four control points (value, key,
  query, reading strategy), and show gains from storing rounds rather than
  sessions, expanding keys with extracted user facts, time-aware query
  expansion, and Chain-of-Note reading over JSON-formatted items.
---
<!-- inactive-ok-file: CLAIM-184 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpkl0aw: Wu et al. — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

## Contribution

A benchmark covering knowledge updates and abstention in user–assistant
memory, and a design space for memory-augmented assistants with tested
optimizations.

## Key results

- Abstract: "commercial chat assistants and long-context LLMs showing a 30%
  accuracy drop on memorizing information across sustained interactions."
- §3.2: Knowledge Updates: "Ability to recognize the changes in the user's
  personal information and update the knowledge of the user dynamically over
  time." Abstention: answer "I don't know" for information never mentioned.
- §3.4: "We found ChatGPT tended to overwrite crucial information as the chat
  continues, while Coze often failed to record indirectly provided user
  information."
- §3.4: long-context LLMs show "a 30% to 60% performance decline" on the S
  setting relative to the oracle (evidence sessions only); GPT-4o from 0.870 to
  0.606 (Fig. 3b).
- §5.2: "replacing sessions or rounds with extracted summaries or facts
  negatively impacts QA performance due to information loss. The only
  exception is with multi-session reasoning questions, where fact
  decomposition consistently improves performance."
- §5.5: "even with perfect retrieval, a suboptimal reading strategy results in
  up to a 10-point absolute performance drop".

## Assumptions

Synthetic but human-curated question–evidence pairs embedded in filler
sessions; an LLM judge (GPT-4o) for correctness, meta-evaluated by the
authors; online memory evaluation for commercial systems done by hand on a
sample in a simpler setting.

## Concepts

Five memory abilities (IE, MR, KU, TR, ABS); needle-in-a-haystack history
construction; LongMemEval S / M; oracle retrieval; indexing, retrieval,
reading; control points value, key, query, reading strategy; session vs.
round granularity; fact-augmented key expansion; time-aware query expansion;
Chain-of-Note; offline reading vs. online memory.

## Bearing on the record

[QUESTION-108](../questions.d/QUESTION-108.md)'s note names LongMemEval among comparators "named ... as
comparators" by A20 and A27. Accurate as a benchmark comparator. Its
knowledge-update ability is single-fact update; it does not test the
dependants of an update (MEME, [LIT-2281](../literature.d/LIT-2281.md), scores that and lists LongMemEval
as lacking it).

- **[QUESTION-108](../questions.d/QUESTION-108.md)** (when a structured record beats a summary, a transcript or
  a posterior): **qualifies** in a direction the question anticipates
  ("A negative result counts"): compressing sessions into extracted summaries
  or facts lost information and lowered accuracy, except on multi-session
  reasoning where facts helped; and structure at reading time (JSON plus
  Chain-of-Note) helped only together. This is evidence that the value of a
  structured representation depends on the question type and on reading, not
  on structure as such; it does not test a governed record.

- **[CASE-091](../cases.d/CASE-091.md)** (information and token budget controlled separately):
  LongMemEval §5.2 compares value choices "in a budget-aware manner", the
  same control the case requires; a usable external task for the case's
  arms.
- **[CLAIM-184](../claims.d/CLAIM-184.md)** (anchors entrench) is not engaged; no held entry uses
  "knowledge update" or "abstention" in this sense. "LoCoMo" hits  ([CLAIM-152](../claims.d/CLAIM-152.md), [QUESTION-254](../questions.d/QUESTION-254.md) and others) concern other works or senses.
  Duplicate check: arXiv id and title not held elsewhere.

## Limitations

Commercial-system pilot is small and manual; LLM judge; synthetic histories;
updates are to single facts; results on M depend on the retriever chosen
(Stella V5).
