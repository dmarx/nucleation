---
status: Read
paper: LIT-2325
title: 'Khatua, Zhu et al. — CooperBench: Why Coding Agents Cannot be Your Teammates Yet'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2601.13295. **Read** (main
    text §§1–6 and §8 read; §2.3, §3 skimmed; §7 related work and appendices
    skipped except Appendix prompt excerpt glanced). Read 2026-11-12. A
    delegated reader drafted the reading; quotations were rechecked by script
    against the downloaded copy, and any that did not match were kept as
    paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  CooperBench gives two coding agents, each in its own environment, two
  features on the same repository state that are logically compatible but
  touch overlapping code; they can message each other in real time, and
  success requires their merged patches to pass both features' tests. 652
  tasks from 12 libraries in 4 languages. Against a "Solo" baseline (one
  agent does both features), cooperating agents do markedly worse ("curse of
  coordination"); the gap is largest at middle difficulty and grows with
  more agents. A communication tool reduces merge conflicts but does not
  raise success.
---
<!-- inactive-ok-file: CASE-tmpiocs1 CLAIM-tmpyp3u3 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpp7l8p: Khatua, Zhu et al. — CooperBench: Why Coding Agents Cannot be Your Teammates Yet

## Contribution

- A verifiable benchmark for agent–agent cooperation under partial observability with
  embedded conflicts.
- Evidence that adding a communication channel changes the failure mode (fewer textual
  conflicts) without improving outcomes.
- A taxonomy of coordination failures (symptoms by LLM-judge, causes by manual review of 50
  traces).

## Key results

1. Abstract: "agents achieve on average 30% lower success rates when working together
   compared to performing both tasks individually". §1 and §8 give the leading models'
   figure: "GPT-5 and Claude Sonnet 4.5 based agents achieve only 25% with two-agent
   cooperation on CooperBench, which is around 50% lower than a “Solo” baseline". (The
   paper uses both figures: an average and the leading-model gap.)
2. §4: "This coordination gap is as large as 50% in the leading models".
3. §4, scaling: "performance drops from 68.6% with 2 agents to 46.5% with 3 agents and
   further to 30.0% with 4 agents" (46 tasks; small-scale).
4. §5: "none of the models effectively leverage communication tool to achieve higher
   cooperation success. The difference between “with comm” and “no comm” settings is not
   statistically significant."
5. §5: "Communication reduces merge conflicts", and agents "spent as much as 20% of the
   steps in communication".
6. §5: "Having a Plan message in the very first turn nearly halves the conflict rate
   (29.4% vs 51.5%)."
7. §6: "Coordination failures stem from three capability gaps: communication (failing to
   exchange key information), commitment (not following through on promises), and
   expectation (failing to model what partners are doing)."
8. §1: agents "make unverifiable claims about code state, ignore agreed-upon integration
   points, and break explicit promises."
9. §8, future directions include "lightweight protocols for verifiable commitments (e.g.,
   shared signatures, insertion-point contracts)".

## Assumptions

- For humans, "teams should perform better or faster than individuals" (§4) — the bar is
  asserted, not measured here.
- Merged-patch test passing is the measure of cooperative success; the merge step uses a
  learned resolver for trivial conflicts.
- Failure symptoms coded by GPT-5 as judge (human validation in an appendix not read).
- One channel only: free-text messages; no shared structured workspace beyond git patches.

## Concepts

curse of coordination; Solo vs Coop; coordination gap; mid-difficulty crisis;
communication / commitment / expectation gaps; speech-act types (plan, question, update,
answer, ack); verifiable commitments; role division, resource division, negotiation
(emergent behaviours).

## Bearing on the record

QUESTION-tmpxq2sb says A31 named CooperBench "as external tests" and that it is
"registered unread". Accurate: it is a cooperation benchmark usable as a transfer check.
The record has no finding attributed to it, so nothing to correct.

- **QUESTION-tmpxq2sb** (Open, branch): *supports the premise, leaves the question open*.
  CooperBench shows that a free-text channel between agents with private states can change
  behaviour (fewer conflicts) without improving integration of their work (results 4–5), and
  that failures are of commitment and expectation, not only of information exchange
  (result 7). That is evidence that a structured medium beyond a chat channel is worth
  testing; it does not test a shared record. Its own suggestion, "verifiable commitments"
  (result 9), is close to what a typed record of who committed to what would supply. In
  CLAIM-403's stages, CooperBench's failures sit at uptake (commitments made, then not
  acted on) and at expectation, not at admission.
- **CLAIM-tmpyp3u3** (Proposed, branch: a shared record shows contributions and standing,
  not that collaborators know the standing): *supports*. Agents "hold incorrect
  expectations about their partner’s plans" (§1) even with messages exchanged and read;
  access to a message is not evidence of a shared model of it.
- **CLAIM-346** (Active; feasibility, aggregation and epistemic coordination are
  independent obstructions): *illustrates*. Solo succeeds where Coop fails at equal
  workload, so the failure is coordination, not feasibility.
- **CASE-tmpiocs1** (Proposed, branch): a candidate transfer task, as A31 proposed.

## Limitations

Appendix validation of the LLM-judge symptom coding not read; per-model numbers taken
from text, not figures; the 2→4-agent result is on 46 tasks. The 30% (abstract) vs ~50%
(introduction, conclusion) figures refer to different aggregates and should not be
conflated.
