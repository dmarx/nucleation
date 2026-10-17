---
number: 527
status: Proposed
formerly:
- THEORY-tmpgjsxj
promote_when: >-
  The interventional procedure run on real systems, not described: with
  mechanism interventions actually performed on a thermostat with and
  without its design process, an RL policy with and without its training
  loop, and a human, the verdicts coming out as the account says, and the
  procedure separating an accidentally optimal input-output system from
  an agent where a compression test does not. It is refuted if natural
  choices of variables give opposite verdicts on the same system with no
  principled way to choose (the frame problem THEORY-249 presses), or if
  the five recovery assumptions fail for the systems that matter. The
  recovery theorem itself, which holds, cannot settle whether the
  definition picks out agency.
title: "If agents are the systems that would adapt their policy were their actions to affect the world differently, then in causal models with mechanism variables they can be found from interventions on mechanisms, provably under five assumptions; on that definition the agent is wherever the adaptation is, so a thermostat is not an agent while it together with its design process is, and an RL training process is while its learnt policy generally is not"
version: 1
tags:
- agency
- causality
date: '2026-10-16'
source:
- LIT-909
rivals:
- THEORY-624
answers:
- QUESTION-032
summary: >-
  Kenton, Kumar, Farquhar, Richens, MacDermott & Everitt (2022), [LIT-909](../literature.d/LIT-909.md),
  read in [NOTE-707](../notes.d/NOTE-707.md). The recovery result is proved (Theorem 1) under five
  assumptions, including the availability of interventions on mechanisms.
  The definition is a proposal, the verdicts on thermostats and RL are
  argued from it, and "reliably classifies humans as agents" is asserted.
  The labels depend on the chosen variables, which the paper states.
---
<!-- inactive-ok-file: CLAIM-170 CLAIM-174 THEORY-208 THEORY-249 THEORY-624 — Proposed; related or rival accounts named in Connections, nothing here rests on their being settled -->

# THEORY-527: If agents are the systems that would adapt their policy were their actions to affect the world differently, then in causal models with mechanism variables they can be found from interventions on mechanisms, provably under five assumptions; on that definition the agent is wherever the adaptation is, so a thermostat is not an agent while it together with its design process is, and an RL training process is while its learnt policy generally is not

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
- On [QUESTION-032](../questions.d/QUESTION-032.md) it gives a level- and variable-relative answer: a factor
  is an agent if its decision mechanism responds to interventions on how its
  actions affect its utility.
