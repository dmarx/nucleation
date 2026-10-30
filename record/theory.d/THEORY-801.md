---
number: 801
status: 'Proposed'
formerly:
- THEORY-tmpmmfpx
promote_when: 'The interventional procedure run on real systems, not described: with mechanism interventions actually performed on a thermostat with and without its design process, an RL policy with and without its training loop, and a human, the verdicts coming out as the account says, and the procedure separating an accidentally optimal input-output system from an agent where a compression test does not. It is refuted if natural choices of variables give opposite verdicts on the same system with no principled way to choose (the frame problem THEORY-249 presses), or if the five recovery assumptions fail for the systems that matter. The recovery theorem, which holds, cannot settle whether the definition picks out agency.'
title: 'Agents are the systems that would adapt their policy were their actions to affect the world differently, so the agent is wherever that adaptation is: a thermostat is not an agent while it together with its design process is, an RL training process is while its learnt policy generally is not, and humans are'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    The rivals edge to THEORY-624 is removed by the twenty-fourth status
    review, at the status review's ruling (the owner delegated these
    rulings; ADR-065): THEORY-624 was narrowed to a report of what
    Orseau, McGill and Legg do and argue, and the rival account, their
    relative definition of agency, is now THEORY-1236, Proposed,
    which carries the edge. Status, title and claims are unchanged.
tags:
- agency
- causality
date: '2026-10-20'
source:
- LIT-909
summary: >-
  The definition and verdicts [THEORY-527](THEORY-527.md)'s title carried before the promotion audit (batch 055) narrowed it to the recovery theorem. Kenton, Kumar, Farquhar, Richens, MacDermott and Everitt (2022), [LIT-909](../literature.d/LIT-909.md), propose the definition and argue the verdicts from it in §1 and §4; that it "reliably classifies humans as agents" is asserted. The verdicts are relative to the variables chosen, which the paper states. Filed under [ADR-047](../decisions.d/ADR-047.md) v4.
extends:
- THEORY-527
answers:
- QUESTION-228
bears_on:
- QUESTION-032
---
<!-- inactive-ok-file: THEORY-249 THEORY-1236 — Proposed; the frame objection and the rival account, cited as open -->


# THEORY-801: Agents are the systems that would adapt their policy were their actions to affect the world differently, so the agent is wherever that adaptation is: a thermostat is not an agent while it together with its design process is, an RL training process is while its learnt policy generally is not, and humans are

## Source

Kenton et al. (2022), "Discovering Agents", [LIT-909](../literature.d/LIT-909.md), read in [NOTE-707](../notes.d/NOTE-707.md).
§1 and §4 give the verdicts on thermostats, design processes, RL
training and learnt policies; §5.1 says that "what is a decision or a
utility node is frame-dependent".

## What is asserted, and by whom

That agency is the disposition to adapt one's policy to how one's actions
affect the world, and that on this definition the agent is located at the
adaptation: the design process with the thermostat, the training loop
rather than the frozen policy, which "derive[s] much of [its]
goal-directedness from the process that creates [it]". The authors argue
the verdicts in prose from the definition.

## What the record holds toward it

- [THEORY-527](THEORY-527.md) (Active): under the five assumptions, the game graph, with
  its decisions, utilities and agents, is recovered exactly from
  interventions on mechanisms (Theorem 1, re-derived). That shows the
  definition is operational in principle, not that it picks out agency.
- Against it: the verdicts depend on the chosen variables (§5.1–5.2), the
  frame problem [THEORY-249](THEORY-249.md) presses, and mechanism interventions are not
  available for most systems of interest. [THEORY-1236](THEORY-1236.md) is a rival account, and [THEORY-624](THEORY-624.md) reports the paper that proposes it.
- The owner's question on conditional theorems whose promote_when moves
  to a QUESTION ([THEORY-185](THEORY-185.md), -133, -419, -527) is not decided by filing
  this.

## What would confirm or reject it

The procedure run on real systems with the verdicts as stated, as the
promote_when says. [QUESTION-228](../questions.d/QUESTION-228.md) asks the same thing as a question.
