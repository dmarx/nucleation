---
status: Read
paper: LIT-2295
title: 'Wang et al. — PaperArena: An Evaluation Benchmark for Tool-Augmented Agentic Reasoning on Scientific Literature'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2510.10909. A delegated
    reader drafted the reading; quotations were rechecked by script against
    the downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  PaperArena is a benchmark of 784 expert-curated questions over a corpus of
  14,435 open-access AI papers that require reading several papers, using
  tools (PDF parsing, retrieval, web search, code execution, citation
  lookup) and combining the results. A platform, PaperArena-Hub, runs a
  ReAct-style single agent and a centralised multi-agent workflow (a manager
  plans and delegates to workers with separate contexts). The best
  configuration, Gemini 2.5 Pro in the multi-agent workflow, averages 38.78%
  (18.47% on the hard subset) against 83.5% for a Ph.D. expert.
---
<!-- inactive-ok-file: CASE-tmpiocs1 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpyz4se: Wang et al. — PaperArena: An Evaluation Benchmark for Tool-Augmented Agentic Reasoning on Scientific Literature

## Contribution

A benchmark and platform for cross-paper, multi-tool reasoning over scientific literature, with
trace-level diagnostics of tool use and an IRT analysis of difficulty.

## Key results

1. Headline (abstract): the leading configuration "achieves merely 38.78% average accuracy, while on the hard subset, accuracy drops to only 18.47%".
2. Human baseline (§1): "a performance far below the 83.5% achieved by a human expert".
3. Multi-agent design (§4.2): "a centralized design with a manager agent responsible for high-level planning and delegating subtasks to worker agents within independent context spaces".
4. Multi- vs single-agent (§5.1): "multi-agent workflows improve accuracy and efficiency by enabling collaborative reasoning and labor division".
5. Planning ceiling (§5.2): "The single agent, when explicitly prompted with the globally minimal viable tool chain, outperforms multi-agent workflows."
6. Tool imbalance (§5.2): "practical use of the code executor is over five times the minimal viable requirement".
7. Size: "a final set of 784 high-quality questions" (§1).

## Assumptions

Questions and answers from a curated corpus of recent open-access AI papers; LLM-assisted
drafting then expert filtering; single ground-truth answers judged partly by an LLM evaluator
checked against humans (§5.4).

## Concepts

Tool-augmented agentic reasoning; cross-paper integration; minimal viable tool chain; manager–worker
multi-agent workflow; item response theory difficulty.

## Bearing on the record

[QUESTION-tmpxq2sb](../questions.d/QUESTION-tmpxq2sb.md) lists PaperArena, after A31, among "external tests" for whether a shared record
helps agents who hold different parts of the evidence. **Partly inaccurate as a fit.** In
PaperArena the evidence is not distributed among agents: one agent, or a manager that hands
subtasks to workers, has access to the whole corpus and tools. It tests retrieval and tool
orchestration across papers, not pooling of evidence held separately. It could serve as a
transfer task for a record-equipped research agent (cross-paper synthesis is what the record
does), but not as a hidden-profile-style test. The exchange's title for it was also truncated
(the LIT's history already corrects this).

- **[QUESTION-tmpxq2sb](../questions.d/QUESTION-tmpxq2sb.md)**: **leaves open**; at most a downstream transfer task. The manager–worker
  result (separate contexts help planning) is about decomposition, not about shared state.
- **[QUESTION-108](../questions.d/QUESTION-108.md)** (when a structured record does better than a summary, a transcript or a
  posterior): **leaves open**, but offers a candidate task family: questions whose answers need
  facts from several papers, where a record of prior readings could be compared with retrieval.
- **[CASE-tmpiocs1](../cases.d/CASE-tmpiocs1.md)**: does not bear (no distributed information).

## Limitations

AI-paper corpus only; preprint; accuracy partly LLM-judged; the multi-agent workflow is one
centralised design.
