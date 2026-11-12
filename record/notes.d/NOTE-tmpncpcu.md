---
status: Read
paper: LIT-tmp1bytl
title: 'Salemi et al. — LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2510.01285. Read
    (2026-11-12). A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The paper builds an LLM multi-agent system for data-science questions over
  large "data lakes", where the files needed for a question are not
  identified in advance. A main agent, built on ReAct, posts requests to a
  shared blackboard. Helper agents decide on their own whether to answer.
---

# NOTE-tmpncpcu: Salemi et al. — LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science

## Contribution

The contribution is a communication paradigm for LLM agents. Requests are broadcast and agents self-select; no task is assigned. The paradigm is evaluated against a matched master–slave ablation on the data-discovery problem. The authors present the self-selection as what makes the difference, but this attribution is not separately tested (see Limitations).

## Key results

- **Abstract.** The system achieves "13%–57% relative improvements in end-to-end success and up to a 9% relative gain in data discovery F1 over the best baseline."
- **Figure 1 caption.** "In this framework, the main agent does not assign tasks to subordinate agents."
- **§1.** The design differs from shared memory: "there is no task assignment; instead, requests are broadcast on a blackboard".
- **§3, footnote 2.** Helpers' responses go to a separate response board, read only by the main agent, "to prevent cross-influence of sub-agents". The blackboard therefore carries requests only. No partial solutions accumulate on it for others to build on.
- **Table 1, Gemini 2.5 Pro.** KramaBench average 37.53% for the blackboard against 32.16% for master–slave, 28.26% for RAG and 19.18% for DS-GRU.
- **§4.2, scalability.** "Blackboard achieves its largest gains on the two datasets with the largest data lakes". These are DA-Code (145 files, +70% relative) and KramaBench Astronomy (1556 files, +211%).
- **§4.2, cost.** "Blackboard is more expensive per question (approximately 2.3× the cost of RAG and 1.8× that of Master–Slave)". Runtime for all three systems lies between 132 and 145 s.
- **§4.2, attribution.** "We attribute this improvement to the design of the Blackboard System, where tasks are not explicitly assigned to helper agents".
- **Appendix B, on Han and Zhang (2025).** In that design, "The blackboard in their framework is mainly used as a shared memory for information exchange", and the main agent still picks who acts.

## Assumptions

- The data lake can be partitioned into clusters. By default this is done by filename, using Gemini 2.5 Pro.
- Helpers' self-assessment of whether they can contribute is reliable enough.
- A single main agent integrates all responses and decides. It is the only agent that solves the task.
- Benchmarks were filtered by hand to keep questions with enough discovery hints. DSBench is judged by an LLM (Gemini 2.5 Pro).

## Concepts

- blackboard architecture (after Hearsay-II and Nii)
- master–slave orchestration
- self-selection, or volunteering, by helper agents
- request board and response board
- data discovery in data lakes
- file agents and search agent
- relative gain

## Bearing on the record

The LIT summary has A saying "Google researchers evaluated blackboard-based multi-agent systems for data discovery". That is broadly accurate, with three refinements:

1. It is one system from a Google Cloud AI Research and UMass team, and the first author is a UMass student researcher.
2. The "blackboard" here is a broadcast request channel, not a shared structured state of hypotheses. Responses are deliberately kept off the shared board.
3. The comparison is against an orchestrator that assigns tasks, not against a structured shared record.

The LIT's own gloss, a recent evaluation of blackboard coordination among language-model agents, is fair if read as coordination of task routing. It should not be read as integration of distributed evidence through a common store.

- **[QUESTION-tmpxq2sb](../questions.d/QUESTION-tmpxq2sb.md) (shared typed governed record vs structured protocol): leaves open, and mildly qualifies.**
  - The paper shows that removing assignment and letting holders of partial evidence self-select improves integration of distributed files. That speaks to the "recognition" stage: the right holder answers.
  - It does not test a shared, persistent, typed state. Footnote 2 removes exactly that, to avoid cross-influence.
  - It has no governance and no credence or standing on contributions. Integration is done by one agent in its own context.
  - It is evidence that the communication architecture matters at fixed models. It is not evidence for a record of the luria kind.
  - The design suggests a contrast arm for the question: broadcast request with a private response board against "shared board with visible responses".

## Limitations

- The gain is attributed to self-selection, but the blackboard and master–slave arms also differ in parallelism and in token budget. Blackboard costs 1.8× master–slave. There is no cost-matched control.
- Absolute accuracies are low (KramaBench ≤ ~41%).
- The DSBench judge is an LLM.
- Clustering is done by an LLM over filenames.
- No variance or seeds are reported in the main tables.
