---
status: Read
paper: LIT-tmpbu984
title: 'Kenton et al. — Discovering Agents'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Read in full from the arXiv PDF (v2, 34 pp.), text extracted with
    pdftotext. A reader working for the assistant read every section,
    including the appendices, and drafted a digest with verbatim
    quotations. The quotations used below were checked against the
    extracted text by script, and thirteen of fourteen matched; the one
    that did not is not used. Definition 1, Definitions 2–3, Algorithms
    1–3 and the proof of Theorem 1 are garbled in extraction, where the
    tilde-marked mechanism variables break. They are described from the
    surrounding prose, not quoted. The figures were not legible.
date: '2026-10-11'
summary: >-
  An interventional, causal definition of agents. Mechanised causal models
  add a mechanism variable for each object-level variable. Decision nodes
  are found as variables whose mechanisms respond to downstream mechanisms
  (terminal edges), and utility nodes as the targets of those responses.
  Recovery of the true game graph is proved under five assumptions,
  including interventional data on mechanisms. The verdicts are
  sensible. The labels are frame-dependent and granularity-sensitive,
  which the paper states but does not treat as a threat.
---
<!-- inactive-ok-file: CLAIM-tmptd6s2 CLAIM-tmpwv313 — Proposed; the claims this reading bears on, open -->

# NOTE-tmpoybi6: Kenton et al. — Discovering Agents

## Contribution

The first formal causal definition of agents, in the authors' words, together
with algorithms to discover them from interventional data. It sets this
against compression-based definitions such as Orseau et al.'s
([LIT-tmpq7txx](../literature.d/LIT-tmpq7txx.md)).

## Key insight

Agents are moved by reasons. A system "would act differently if [it] 'knew'
that the world worked differently". So test agency by changing how actions
affect the world and seeing whether the policy adapts: "agents are systems
that would adapt their policy if their actions influenced the world in a
different way".

## Assumptions

- **Mechanised causal models.** These distinguish object-level variables
  from mechanism variables, which "parameterise how the object-level
  variables depend on their object-level parents".
- **Interventions on mechanisms are available.** Both object-level and
  mechanism variables can be measured and set. A mechanism intervention is
  a soft intervention held across time steps, so the system can adapt to it.
- **Five assumptions for the recovery theorem.** Each connected component of
  the decision–utility graph is one agent; agents play a subgame-perfect
  best response; ties are broken in a fixed order; only decision mechanisms
  have incoming terminal edges; and mechanism interventions can instantiate
  any deterministic function.

## Key results

- **Recovery.** Theorem 1 proves that Algorithm 1 (edge-labelled mechanised
  graph discovery) followed by Algorithm 2 (identifying decision and utility
  nodes) recovers the true game graph under the assumptions. Theorems 2 and
  3 show Algorithms 2 and 3 are left inverses. In the conclusion's words:
  "Algorithms 1 and 2 describe a precise experimental process that can, in
  principle and under some assumptions, be done to assess whether something
  is an agent."
- **Verdicts.**
  - *Thermostat.* "An existing thermostat will not adapt to this change, and
    is therefore not an agent by our account." Yet "the thermostat with its
    creation process is an agent".
  - *RL.* "we consider the system of the RL training process to be an agent,
    but the learnt RL policy itself, in general, won't be an agent according
    to our definition". The moral: "simple forms of agents often derive much
    of their goal-directedness from the process that creates them".
  - *Humans.* "Our method reliably classifies humans as agents". This is
    asserted, not demonstrated.
  - *Actor-critic.* Two agents. The one-agent coarse graph "is also an
    accurate description of the same underlying system, though with less
    detail".
  - *A chain X → Y → Z.* No agents.
- **Failures.** Assistance games, where human and robot share a utility,
  are merged into one agent. A utility that is not downstream of its
  decision is mislabelled.
- **Against compression.** "the compression-based approach only considers
  what the system actually does. It may therefore incorrectly classify as
  agents systems with accidentally optimal input-output mappings".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Agents are systems that would adapt their policy if their actions influenced the world differently | definitional | §1.2, abstract |
| C2 | Algorithms 1 and 2 recover the true game graph under assumptions A1–A5 | proved | Theorem 1 |
| C3 | A thermostat is not an agent; the thermostat with its creation process is | argued | §1.3 |
| C4 | A trained policy is generally not an agent; its training process is | argued | §1.3 |
| C5 | Decision, utility and chance labels depend on the chosen variables | illustrated | §5.1, Appendix C |
| C6 | The choice of coarse-graining can change whether agents are found | asserted | §5.2 |
| C7 | The method does better than compression on accidentally optimal systems | argued | §1.2, §6 |

## Connections

- **The admission test** ([CLAIM-tmpwv313](../claims.d/CLAIM-tmpwv313.md)). C1 is its adaptation half.
- **The owner's jurisdiction thesis** ([CLAIM-tmptd6s2](../claims.d/CLAIM-tmptd6s2.md)). C3 and C4 locate the
  agent where the governing process is, including a designer or trainer
  outside the device. That is an agent individuated by the reach of what
  governs its regimes, which is the bearing the record takes.
- **Level-relativity** ([CLAIM-tmp3qyzh](../claims.d/CLAIM-tmp3qyzh.md)). C5 and C6 are this record's target
  and level relativity, stated for agents: "In a sense, a choice of variables
  represents a frame in which to model the system, and what is a decision or
  a utility node is frame-dependent."
- **The dancing couple** ([CASE-tmpbv3ts](../cases.d/CASE-tmpbv3ts.md)). The assistance-game failure, where
  shared utility merges agents, is the case where a couple sharing one goal
  would be read as one agent. Under the jurisdiction reading that may be the
  right verdict at the level of the room.
