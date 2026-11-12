---
status: Read
paper: LIT-2280
title: 'Zhu et al. — MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2503.01935. **Read**
    (2026-11-12): main text §§1–8 read; appendices skimmed (module
    descriptions incl. the memory module, Werewolf environment). A delegated
    reader drafted the reading; quotations were rechecked by script against
    the downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  MultiAgentBench and its framework MARBLE evaluate LLM multi-agent systems
  in six scenarios: research co-authoring, Minecraft building, database
  error analysis, coding, bargaining and Werewolf. Agents are connected by
  an agent graph whose topology can be star, tree, chain or graph-mesh;
  planning can be naive, chain-of-thought, group discussion or "cognitive
  evolving". Task completion is scored by milestones that an LLM-based
  detector marks as achieved and credits to agents (a KPI), plus task scores
  and LLM-rated communication, planning and collaboration scores.
---

# NOTE-tmpe5ckt: Zhu et al. — MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents

## Contribution

A multi-domain benchmark that scores coordination as well as outcome, a
configurable framework for topologies and planning strategies, and a
milestone-based KPI.

## Key results

- Abstract: "gpt-4o-mini reaches the average highest task score, graph
  structure performs the best among coordination protocols in the research
  scenario,and cognitive planning improves milestone achievement rates by 3%."
- §4.2: "the intrinsic model capabilities are the primary drivers of success
  across diverse tasks"; e.g. Llama-3.1-70B's Minecraft coordination score of
  75.00 with task score 0.21.
- §4.3: "the group discussion method scores the worst across all metrics,
  possibly because an overly large planning group hinders effectiveness".
- §5: "increasing the number of agents leads to a decrease in the overall
  KPI"; coordination improves from 1 to 3 agents.
- §5: task and coordination scores rise from 1 to 7 iterations, "but then
  drop sharply at 10 iterations".
- §3 (KPI): An LLM-based detector continuously monitors the iterative
  process to identify which milestones have been achieved and records the
  corresponding contributing agents.
- Appendix (memory module): shared memory holds global knowledge and
  collective decisions beside each agent's individual memory.
- §8: future work on "different memory mechanisms (e.g. long-term memory,
  short-term memory, shared memory)".

## Assumptions

LLM judges can score milestones, communication, planning and research
output; five models (open-source Llama and two OpenAI models); fixed
iteration caps; unlimited per-agent long-term memory in the main runs.

## Concepts

MARBLE; agent graph; coordination topologies (star, tree, chain,
graph-mesh); planning strategies (naive, CoT, group discussion, cognitive
evolving); milestone-based KPI; task score vs. coordination score; emergent
behaviours (strategic information sharing, trust-polarized collaboration,
role-driven strategy iteration).

## Bearing on the record

QUESTION-tmpxq2sb records A31 naming MultiAgentBench as an "external test".
Fair. it varies communication topology and planning, not a
shared record; its shared memory is a module of the framework and is not
manipulated (the authors list memory ablations as future work). Its scoring
of coordination rests on LLM judges, which matters if the record's study
reuses it.

- **QUESTION-tmpxq2sb** (does a shared, typed, governed record beat a
  structured protocol at integrating distributed evidence?): **leaves open**.
  It supplies environments and a topology/planning comparison class, and two
  cautions relevant to the question's fairness conditions: adding agents
  lowered the KPI, and longer interaction degraded coordination, so
  compute and team size must be matched as A31's fairness conditions require.
  Its Werewolf environment has information asymmetry but is not scored by
  per-clue uptake.

- **CLAIM-346** (Active: feasibility, aggregation, coordination independent):
  §4.2's high-coordination, low-task-score case (Minecraft) is an
  illustration that coordination does not substitute for capability;
  illustrative only.
- **CLAIM-266 / CLAIM-149**: the KPI and coordination scores are LLM judgments;
  no bearing beyond caution.
- Duplicate check: arXiv id, DOI and title not held elsewhere.

## Limitations

LLM-judged metrics; few models (no frontier closed models beyond gpt-4o-mini);
scenario coverage; no memory ablation; the "aha-moment" emergent behaviours
are qualitative.
