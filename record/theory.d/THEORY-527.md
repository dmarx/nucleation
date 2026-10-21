---
number: 527
status: Active
formerly:
- THEORY-tmpgjsxj
title: 'If agents are the systems that would adapt their policy were their actions to affect the world differently, then in mechanised causal games meeting Kenton et al.''s five assumptions (one agent per connected component of the decision–utility graph, best response to every mechanism intervention, a fixed tie-breaking order, terminal edges only into decision mechanisms, and mechanism interventions able to set any deterministic function) the game graph, with its decisions, utilities and agents, is recovered exactly from interventions on mechanisms'
version: 4
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-527 (batch 055, ADR-047 v2). Theorem 1 and Lemmas 1–2 were
    re-derived. The verdicts on thermostats, design processes, RL training and
    learnt policies leave the title: they are argued in prose from the
    definition and are relative to the variables chosen, not derived. They
    stay in the body as the authors' arguments. Whether the definition picks
    out agency, the promote_when, moves to QUESTION-228.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 069, ADR-047 v4) filed THEORY-801,
    Proposed, to carry what the narrowing dropped. This entry's status,
    title and claims are unchanged; a dated note says what moved.
- version: 4
  date: '2026-10-21'
  note: >-
    The question audit of 2026-10-21 found the `answers` link to
    QUESTION-032 stale. Since version 2 this entry holds only the
    recovery theorem, conditional on the definition. What answers
    QUESTION-032 is the definition and its verdicts, which THEORY-801
    carries and which already answers it. The link is dropped and the
    Connections bullet says so. Status, title and claims are unchanged.
tags:
- agency
- causality
date: '2026-10-16'
source:
- LIT-909
rivals:
- THEORY-624
summary: >-
  Kenton, Kumar, Farquhar, Richens, MacDermott & Everitt (2022), [LIT-909](../literature.d/LIT-909.md),
  read in [NOTE-707](../notes.d/NOTE-707.md). The recovery result (Theorem 1) is proved under five
  assumptions, including the availability of interventions on mechanisms,
  and was re-derived on promotion (2026-10-20). The definition is a
  proposal; the verdicts on thermostats and RL are argued from it, and
  "reliably classifies humans as agents" is asserted. The labels depend on
  the chosen variables, which the paper states.
extended_by:
- THEORY-801
---
<!-- inactive-ok-file: THEORY-801 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->
<!-- inactive-ok-file: CLAIM-170 CLAIM-174 THEORY-208 THEORY-249 THEORY-624 — Proposed; related or rival accounts named in Connections, nothing here rests on their being settled -->

# THEORY-527: If agents are the systems that would adapt their policy were their actions to affect the world differently, then in mechanised causal games meeting Kenton et al.'s five assumptions (one agent per connected component of the decision–utility graph, best response to every mechanism intervention, a fixed tie-breaking order, terminal edges only into decision mechanisms, and mechanism interventions able to set any deterministic function) the game graph, with its decisions, utilities and agents, is recovered exactly from interventions on mechanisms

## Source

Kenton, Kumar, Farquhar, Richens, MacDermott & Everitt (2022), "Discovering
Agents", [LIT-909](../literature.d/LIT-909.md), read in full in [NOTE-707](../notes.d/NOTE-707.md) from the arXiv PDF (v2).

## What was actually shown

- **The definition (§1.2).** Agents are moved by reasons: a system "would act
  differently if [it] 'knew' that the world worked differently". So "agents
  are systems that would adapt their policy if their actions influenced the
  world in a different way".
- **The models.** Mechanised causal models add mechanism variables, which
  "parameterise how the object-level variables depend on their object-level
  parents". A mechanism intervention is a soft intervention held across time
  steps, so a system can adapt to it.
- **The theorem.** Under five assumptions (each connected component of the
  decision–utility graph is one agent; agents play a subgame-perfect best
  response; ties break in a fixed order; only decision mechanisms have
  incoming terminal edges; mechanism interventions can instantiate any
  deterministic function), Algorithm 1 followed by Algorithm 2 recovers the
  true game graph (Theorem 1). Theorems 2 and 3 show Algorithms 2 and 3 are
  left inverses. In the authors' words, this is "a precise experimental
  process that can, in principle and under some assumptions, be done to
  assess whether something is an agent".
- **The verdicts.** "An existing thermostat will not adapt to this change,
  and is therefore not an agent", but "the thermostat with its creation
  process is an agent". "We consider the system of the RL training process to
  be an agent, but the learnt RL policy itself, in general, won't be". An
  actor-critic is two agents. A chain X → Y → Z has none.
- **Failures.** Assistance games, where human and robot share a utility,
  merge into one agent. A utility not downstream of its decision is
  mislabelled.

The theorem could have failed and did not. The verdicts follow from the
definition; they test it only against intuition.

## What this does not say

- **That the definition is the right one.** It is offered, not derived. Its
  verdicts on thermostats and trained policies are argued from it ([NOTE-707](../notes.d/NOTE-707.md),
  C3, C4). That it "reliably classifies humans as agents" is asserted, not
  demonstrated.
- **That the verdicts are frame-free.** "What is a decision or a utility node
  is frame-dependent" (§5.1), relative to the chosen variables, and the
  choice of coarse-graining can change whether agents are found (§5.2,
  asserted).
- **That the procedure can be run on a given system.** It needs interventional
  data on mechanisms. For most systems of interest, including deployed
  models, those interventions are not available as the theorem assumes.
- **That a frozen policy has no goals.** It says such a policy "derive[s]
  much of [its] goal-directedness from the process that creates [it]", which
  locates the agent elsewhere, not that the policy's behaviour is aimless.
- **That shared goals make one agent in fact.** The assistance-game merger is
  listed by the authors as a failure.

## Connections

- **Rival.** Orseau, McGill & Legg ([THEORY-624](THEORY-624.md)) define agency by which
  description, goal-optimizing or input-output, compresses the behaviour
  better for an observer. Kenton et al. argue that "the compression-based
  approach only considers what the system actually does", and so may count
  as agents "systems with accidentally optimal input-output mappings". The
  two give different verdicts there.
- [THEORY-249](THEORY-249.md) argues that agency is frame-dependent, and cites this method
  giving opposite verdicts under two choices of variables. The paper's own
  §5.1 concedes the dependence.
- [THEORY-208](THEORY-208.md) counts a smart thermostat as an artefactual agent. This account
  does not, unless its design process is included.
- [CLAIM-174](../claims.d/CLAIM-174.md) takes this definition as the adaptation half of its admission
  test, and [CLAIM-170](../claims.d/CLAIM-170.md) reads the location of the agent in the governing
  process as an agent individuated by the reach of what governs it.
- On [QUESTION-032](../questions.d/QUESTION-032.md), the level- and variable-relative answer (a factor
  is an agent if its decision mechanism responds to interventions on how its
  actions affect its utility) is the definition, which [THEORY-801](THEORY-801.md) carries
  since the narrowing. This entry adds only that, under the definition and
  the five assumptions, agents are recoverable from interventions.

## Note of 2026-10-20: Theorem 1, re-derived

- **Lemmas 1–2.** Leave-one-out discovery declares W → V when some
  intervention on all other variables and two values of W change P(V),
  which is the definition of a direct edge, cyclic or not. Algorithm 1 then
  tests terminality by Definition 3, given structural interventions on
  every node.
- **Decisions.** For a decision D of agent A, Assumption 1 gives a utility U
  of A reached by a path from D through no other utility of A. Assumption 5
  sets the path to copy D, makes U = 1 for one value of D, and makes every
  other mechanism ignore D. By Assumption 2 A picks that value; inverting
  U's mechanism makes another uniquely optimal, so the mechanism edge from
  U to D is found. With D's effects cut, every rule ties and Assumption 3
  forbids a switch, so the edge is kept as terminal. Terminal edges into a
  non-decision's mechanism do not exist (Assumption 4), so none is kept.
- **Utilities.** The same construction gives the edge for every utility.
  For a non-utility W with its children cut and every other mechanism
  fixed, W's mechanism can reach expected utility only through W, whose
  effects are cut, so no rule changes and W gets no terminal edge.
- **Agents.** The terminal edges are the reversed edges of the agent
  subgraphs, whose weakly connected components are the agents by
  Assumption 1, and Algorithm 2 colours components.

The theorem does not test the definition in its antecedent, and the
paper's verdicts on particular systems are not consequences of it.

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 069) filed [THEORY-801](THEORY-801.md)
as Proposed, extending this entry. It carries Kenton et al.'s definition of agency and the verdicts they argue from it (thermostat and design process, RL training and learnt policy, humans), which this entry's title carried before batch 055 narrowed it to the recovery theorem. This entry is its evidence and is not changed by the filing.
